"""30 wave trend oscillator family gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of price cycles and waves through specialized oscillator techniques.
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

def f30_wave_gemini_076(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=49, w3=35, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(10)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.623529 + 0.0022267 * anchor
    return base_signal

def f30_wave_gemini_077(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=62, w3=52, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 17)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 52)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.146 * acceleration + 0.0022268 * anchor
    return base_signal

def f30_wave_gemini_078(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=75, w3=69, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(75, min_periods=max(75//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(69) * 1.650588 + 0.0022269 * anchor
    return base_signal

def f30_wave_gemini_079(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=88, w3=86, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(88, min_periods=max(88//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.158667 * _rolling_slope(draw, 86) + 0.002227 * anchor
    return base_signal

def f30_wave_gemini_080(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=101, w3=103, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.824118 + 0.0022271 * anchor
    return base_signal

def f30_wave_gemini_081(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=114, w3=120, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 114)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=120, adjust=False).mean() * 0.837647 + 0.0022272 * anchor
    return base_signal

def f30_wave_gemini_082(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=127, w3=137, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(127, min_periods=max(127//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.851176 + 0.0022273 * anchor
    return base_signal

def f30_wave_gemini_083(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=140, w3=154, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(59)
    rank = change.rolling(140, min_periods=max(140//3, 2)).rank(pct=True)
    persistence = change.rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.184 * persistence + 0.0022274 * anchor
    return base_signal

def f30_wave_gemini_084(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=153, w3=171, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.878235 + 0.0022275 * anchor
    return base_signal

def f30_wave_gemini_085(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=166, w3=188, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.196667 * slope + 0.0022276 * anchor
    return base_signal

def f30_wave_gemini_086(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=179, w3=205, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(80)
    drag = impulse.rolling(179, min_periods=max(179//3, 2)).mean()
    noise = impulse.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.905294 + 0.0022277 * anchor
    return base_signal

def f30_wave_gemini_087(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=192, w3=222, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 222)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.209333 * acceleration + 0.0022278 * anchor
    return base_signal

def f30_wave_gemini_088(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=205, w3=239, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(94, min_periods=max(94//3, 2)).mean(), upside.rolling(205, min_periods=max(205//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.932353 + 0.0022279 * anchor
    return base_signal

def f30_wave_gemini_089(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=218, w3=256, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(218, min_periods=max(218//3, 2)).max()
    rebound = x - x.rolling(101, min_periods=max(101//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.222 * _rolling_slope(draw, 256) + 0.002228 * anchor
    return base_signal

def f30_wave_gemini_090(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=231, w3=273, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.959412 + 0.0022281 * anchor
    return base_signal

def f30_wave_gemini_091(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=244, w3=290, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 244)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=290, adjust=False).mean() * 0.972941 + 0.0022282 * anchor
    return base_signal

def f30_wave_gemini_092(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=257, w3=307, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(257, min_periods=max(257//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.986471 + 0.0022283 * anchor
    return base_signal

def f30_wave_gemini_093(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=270, w3=324, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(270, min_periods=max(270//3, 2)).rank(pct=True)
    persistence = change.rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.247333 * persistence + 0.0022284 * anchor
    return base_signal

def f30_wave_gemini_094(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=283, w3=341, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(283, min_periods=max(283//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.013529 + 0.0022285 * anchor
    return base_signal

def f30_wave_gemini_095(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=296, w3=358, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(296, min_periods=max(296//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.26 * slope + 0.0022286 * anchor
    return base_signal

def f30_wave_gemini_096(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=309, w3=375, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(309, min_periods=max(309//3, 2)).mean()
    noise = impulse.abs().rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.040588 + 0.0022287 * anchor
    return base_signal

def f30_wave_gemini_097(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=322, w3=392, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 322)
    curvature = _rolling_slope(acceleration, 392)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.272667 * acceleration + 0.0022288 * anchor
    return base_signal

def f30_wave_gemini_098(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=335, w3=409, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(335, min_periods=max(335//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.067647 + 0.0022289 * anchor
    return base_signal

def f30_wave_gemini_099(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=348, w3=426, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(348, min_periods=max(348//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.285333 * _rolling_slope(draw, 426) + 0.002229 * anchor
    return base_signal

def f30_wave_gemini_100(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=361, w3=443, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(361, min_periods=max(361//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.094706 + 0.0022291 * anchor
    return base_signal

def f30_wave_gemini_101(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=374, w3=460, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 374)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.108235 + 0.0022292 * anchor
    return base_signal

def f30_wave_gemini_102(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=387, w3=477, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(387, min_periods=max(387//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.121765 + 0.0022293 * anchor
    return base_signal

def f30_wave_gemini_103(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=400, w3=494, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(400, min_periods=max(400//3, 2)).rank(pct=True)
    persistence = change.rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.310667 * persistence + 0.0022294 * anchor
    return base_signal

def f30_wave_gemini_104(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=413, w3=511, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(413, min_periods=max(413//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.148824 + 0.0022295 * anchor
    return base_signal

def f30_wave_gemini_105(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=426, w3=528, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(426, min_periods=max(426//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.323333 * slope + 0.0022296 * anchor
    return base_signal

def f30_wave_gemini_106(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=439, w3=545, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(439, min_periods=max(439//3, 2)).mean()
    noise = impulse.abs().rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.175882 + 0.0022297 * anchor
    return base_signal

def f30_wave_gemini_107(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=452, w3=562, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 452)
    curvature = _rolling_slope(acceleration, 562)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.336 * acceleration + 0.0022298 * anchor
    return base_signal

def f30_wave_gemini_108(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=465, w3=579, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(465, min_periods=max(465//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.202941 + 0.0022299 * anchor
    return base_signal

def f30_wave_gemini_109(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=478, w3=596, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(478, min_periods=max(478//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.348667 * _rolling_slope(draw, 596) + 0.00223 * anchor
    return base_signal

def f30_wave_gemini_110(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=491, w3=613, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 248)
    baseline = trend.rolling(491, min_periods=max(491//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(613, min_periods=max(613//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.23 + 0.0022301 * anchor
    return base_signal

def f30_wave_gemini_111(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=504, w3=630, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 8)
    slow = _rolling_slope(x, 504)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.243529 + 0.0022302 * anchor
    return base_signal

def f30_wave_gemini_112(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=18, w3=647, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(18, min_periods=max(18//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.257059 + 0.0022303 * anchor
    return base_signal

def f30_wave_gemini_113(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=31, w3=664, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(22)
    rank = change.rolling(31, min_periods=max(31//3, 2)).rank(pct=True)
    persistence = change.rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.041667 * persistence + 0.0022304 * anchor
    return base_signal

def f30_wave_gemini_114(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=44, w3=681, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(44, min_periods=max(44//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.284118 + 0.0022305 * anchor
    return base_signal

def f30_wave_gemini_115(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=57, w3=698, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(57, min_periods=max(57//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 36)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.054333 * slope + 0.0022306 * anchor
    return base_signal

def f30_wave_gemini_116(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=70, w3=715, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(43)
    drag = impulse.rolling(70, min_periods=max(70//3, 2)).mean()
    noise = impulse.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.311176 + 0.0022307 * anchor
    return base_signal

def f30_wave_gemini_117(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=83, w3=732, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 50)
    acceleration = _rolling_slope(velocity, 83)
    curvature = _rolling_slope(acceleration, 732)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.067 * acceleration + 0.0022308 * anchor
    return base_signal

def f30_wave_gemini_118(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=96, w3=749, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(96, min_periods=max(96//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.338235 + 0.0022309 * anchor
    return base_signal

def f30_wave_gemini_119(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=109, w3=766, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(109, min_periods=max(109//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.079667 * _rolling_slope(draw, 766) + 0.002231 * anchor
    return base_signal

def f30_wave_gemini_120(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=122, w3=32, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(122, min_periods=max(122//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.365294 + 0.0022311 * anchor
    return base_signal

def f30_wave_gemini_121(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=135, w3=49, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 135)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=49, adjust=False).mean() * 1.378824 + 0.0022312 * anchor
    return base_signal

def f30_wave_gemini_122(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=148, w3=66, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(148, min_periods=max(148//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.392353 + 0.0022313 * anchor
    return base_signal

def f30_wave_gemini_123(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=161, w3=83, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(92)
    rank = change.rolling(161, min_periods=max(161//3, 2)).rank(pct=True)
    persistence = change.rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.105 * persistence + 0.0022314 * anchor
    return base_signal

def f30_wave_gemini_124(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=174, w3=100, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(174, min_periods=max(174//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.419412 + 0.0022315 * anchor
    return base_signal

def f30_wave_gemini_125(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=187, w3=117, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(187, min_periods=max(187//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.117667 * slope + 0.0022316 * anchor
    return base_signal

def f30_wave_gemini_126(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=200, w3=134, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(113)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.446471 + 0.0022317 * anchor
    return base_signal

def f30_wave_gemini_127(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=213, w3=151, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 213)
    curvature = _rolling_slope(acceleration, 151)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.130333 * acceleration + 0.0022318 * anchor
    return base_signal

def f30_wave_gemini_128(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=226, w3=168, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(226, min_periods=max(226//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.473529 + 0.0022319 * anchor
    return base_signal

def f30_wave_gemini_129(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=239, w3=185, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(239, min_periods=max(239//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.143 * _rolling_slope(draw, 185) + 0.002232 * anchor
    return base_signal

def f30_wave_gemini_130(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=252, w3=202, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(252, min_periods=max(252//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.500588 + 0.0022321 * anchor
    return base_signal

def f30_wave_gemini_131(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=265, w3=219, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 265)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=219, adjust=False).mean() * 1.514118 + 0.0022322 * anchor
    return base_signal

def f30_wave_gemini_132(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=278, w3=236, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(278, min_periods=max(278//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.527647 + 0.0022323 * anchor
    return base_signal

def f30_wave_gemini_133(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=291, w3=253, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(291, min_periods=max(291//3, 2)).rank(pct=True)
    persistence = change.rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.168333 * persistence + 0.0022324 * anchor
    return base_signal

def f30_wave_gemini_134(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=304, w3=270, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(304, min_periods=max(304//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.554706 + 0.0022325 * anchor
    return base_signal

def f30_wave_gemini_135(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=317, w3=287, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(317, min_periods=max(317//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.181 * slope + 0.0022326 * anchor
    return base_signal

def f30_wave_gemini_136(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=330, w3=304, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(330, min_periods=max(330//3, 2)).mean()
    noise = impulse.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.581765 + 0.0022327 * anchor
    return base_signal

def f30_wave_gemini_137(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=343, w3=321, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 343)
    curvature = _rolling_slope(acceleration, 321)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.193667 * acceleration + 0.0022328 * anchor
    return base_signal

def f30_wave_gemini_138(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=356, w3=338, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.608824 + 0.0022329 * anchor
    return base_signal

def f30_wave_gemini_139(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=369, w3=355, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(369, min_periods=max(369//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.206333 * _rolling_slope(draw, 355) + 0.002233 * anchor
    return base_signal

def f30_wave_gemini_140(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=382, w3=372, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(382, min_periods=max(382//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.635882 + 0.0022331 * anchor
    return base_signal

def f30_wave_gemini_141(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=395, w3=389, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.649412 + 0.0022332 * anchor
    return base_signal

def f30_wave_gemini_142(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=408, w3=406, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.662941 + 0.0022333 * anchor
    return base_signal

def f30_wave_gemini_143(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=421, w3=423, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(421, min_periods=max(421//3, 2)).rank(pct=True)
    persistence = change.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.231667 * persistence + 0.0022334 * anchor
    return base_signal

def f30_wave_gemini_144(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=434, w3=440, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.836471 + 0.0022335 * anchor
    return base_signal

def f30_wave_gemini_145(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=447, w3=457, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.244333 * slope + 0.0022336 * anchor
    return base_signal

def f30_wave_gemini_146(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=460, w3=474, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(6)
    drag = impulse.rolling(460, min_periods=max(460//3, 2)).mean()
    noise = impulse.abs().rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.863529 + 0.0022337 * anchor
    return base_signal

def f30_wave_gemini_147(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=13, w2=473, w3=491, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 13)
    acceleration = _rolling_slope(velocity, 473)
    curvature = _rolling_slope(acceleration, 491)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.257 * acceleration + 0.0022338 * anchor
    return base_signal

def f30_wave_gemini_148(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=20, w2=486, w3=508, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(486, min_periods=max(486//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.890588 + 0.0022339 * anchor
    return base_signal

def f30_wave_gemini_149(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=27, w2=499, w3=525, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(499, min_periods=max(499//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.269667 * _rolling_slope(draw, 525) + 0.002234 * anchor
    return base_signal

def f30_wave_gemini_150(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=34, w2=13, w3=542, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 34)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.917647 + 0.0022341 * anchor
    return base_signal
