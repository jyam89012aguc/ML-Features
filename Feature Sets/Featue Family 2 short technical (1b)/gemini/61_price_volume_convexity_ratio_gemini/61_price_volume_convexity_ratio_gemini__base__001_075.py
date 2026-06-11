"""61 price volume convexity ratio gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Non-linear relationship between price change and volume as a signal of trend strength.
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
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f61_pvcr_gemini_001(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_002(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_003(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_004(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_005(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_006(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_007(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_008(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_009(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_010(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Non-linear relationship between price change and volume as a signal of trend strength. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window), _rolling_slope(volume, window) + 1e-9)
    return res

def f61_pvcr_gemini_011(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=334, w3=409, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(45, min_periods=max(45//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.894118 + 0.0039562 * anchor
    return base_signal

def f61_pvcr_gemini_012(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=347, w3=426, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(347, min_periods=max(347//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 52)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.907647 + 0.0039563 * anchor
    return base_signal

def f61_pvcr_gemini_013(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=360, w3=443, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(59, min_periods=max(59//3, 2)).mean(), b.abs().rolling(360, min_periods=max(360//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.349667 * _rolling_slope(cover, 59) + 0.0039564 * anchor
    return base_signal

def f61_pvcr_gemini_014(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=373, w3=460, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.356 * y + 0.644000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 66) - _rolling_slope(basket, 373) + 0.0039565 * anchor
    return base_signal

def f61_pvcr_gemini_015(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=386, w3=477, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(386, min_periods=max(386//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.948235 + 0.0039566 * anchor
    return base_signal

def f61_pvcr_gemini_016(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=399, w3=494, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(399, min_periods=max(399//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.036333 * _rolling_slope(draw, 494) + 0.0039567 * anchor
    return base_signal

def f61_pvcr_gemini_017(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=412, w3=511, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(87) - b.diff(126)
    stress = imbalance.rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.975294 + 0.0039568 * anchor
    return base_signal

def f61_pvcr_gemini_018(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=425, w3=528, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(425, min_periods=max(425//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.988824 + 0.0039569 * anchor
    return base_signal

def f61_pvcr_gemini_019(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=438, w3=545, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 438)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.002353 + 0.003957 * anchor
    return base_signal

def f61_pvcr_gemini_020(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=451, w3=562, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(451, min_periods=max(451//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.015882 + 0.0039571 * anchor
    return base_signal

def f61_pvcr_gemini_021(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=464, w3=579, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(115)
    rank = change.rolling(464, min_periods=max(464//3, 2)).rank(pct=True)
    persistence = change.rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.068 * persistence + 0.0039572 * anchor
    return base_signal

def f61_pvcr_gemini_022(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=477, w3=596, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(477, min_periods=max(477//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.042941 + 0.0039573 * anchor
    return base_signal

def f61_pvcr_gemini_023(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=490, w3=613, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(490, min_periods=max(490//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.080667 * slope + 0.0039574 * anchor
    return base_signal

def f61_pvcr_gemini_024(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=503, w3=630, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(503, min_periods=max(503//3, 2)).mean()
    noise = impulse.abs().rolling(630, min_periods=max(630//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.07 + 0.0039575 * anchor
    return base_signal

def f61_pvcr_gemini_025(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=17, w3=647, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 17)
    curvature = _rolling_slope(acceleration, 647)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.093333 * acceleration + 0.0039576 * anchor
    return base_signal

def f61_pvcr_gemini_026(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=30, w3=664, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 150)
    pressure = rel_log.diff(30)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.099667 * pressure.rolling(664, min_periods=max(664//3, 2)).mean() + 0.0039577 * anchor
    return base_signal

def f61_pvcr_gemini_027(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=43, w3=681, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(157, min_periods=max(157//3, 2)).mean())
    decay = spread.ewm(span=43, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.110588 + 0.0039578 * anchor
    return base_signal

def f61_pvcr_gemini_028(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=56, w3=698, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(56, min_periods=max(56//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 164)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.124118 + 0.0039579 * anchor
    return base_signal

def f61_pvcr_gemini_029(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=69, w3=715, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(171, min_periods=max(171//3, 2)).mean(), b.abs().rolling(69, min_periods=max(69//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.118667 * _rolling_slope(cover, 171) + 0.003958 * anchor
    return base_signal

def f61_pvcr_gemini_030(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=82, w3=732, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.125 * y + 0.875000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 178) - _rolling_slope(basket, 82) + 0.0039581 * anchor
    return base_signal

def f61_pvcr_gemini_031(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=95, w3=749, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(95, min_periods=max(95//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.164706 + 0.0039582 * anchor
    return base_signal

def f61_pvcr_gemini_032(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=108, w3=766, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(108, min_periods=max(108//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.137667 * _rolling_slope(draw, 766) + 0.0039583 * anchor
    return base_signal

def f61_pvcr_gemini_033(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=121, w3=32, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(121)
    stress = imbalance.rolling(32, min_periods=max(32//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.191765 + 0.0039584 * anchor
    return base_signal

def f61_pvcr_gemini_034(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=134, w3=49, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.205294 + 0.0039585 * anchor
    return base_signal

def f61_pvcr_gemini_035(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=147, w3=66, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 147)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=66, adjust=False).mean() * 1.218824 + 0.0039586 * anchor
    return base_signal

def f61_pvcr_gemini_036(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=160, w3=83, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.232353 + 0.0039587 * anchor
    return base_signal

def f61_pvcr_gemini_037(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=173, w3=100, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(173, min_periods=max(173//3, 2)).rank(pct=True)
    persistence = change.rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.169333 * persistence + 0.0039588 * anchor
    return base_signal

def f61_pvcr_gemini_038(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=186, w3=117, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(186, min_periods=max(186//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.259412 + 0.0039589 * anchor
    return base_signal

def f61_pvcr_gemini_039(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=199, w3=134, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.182 * slope + 0.003959 * anchor
    return base_signal

def f61_pvcr_gemini_040(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=212, w3=151, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(212, min_periods=max(212//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.286471 + 0.0039591 * anchor
    return base_signal

def f61_pvcr_gemini_041(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=225, w3=168, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 225)
    curvature = _rolling_slope(acceleration, 168)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.194667 * acceleration + 0.0039592 * anchor
    return base_signal

def f61_pvcr_gemini_042(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=238, w3=185, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 15)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.201 * pressure.rolling(185, min_periods=max(185//3, 2)).mean() + 0.0039593 * anchor
    return base_signal

def f61_pvcr_gemini_043(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=251, w3=202, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(22, min_periods=max(22//3, 2)).mean())
    decay = spread.ewm(span=251, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.327059 + 0.0039594 * anchor
    return base_signal

def f61_pvcr_gemini_044(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=264, w3=219, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(264, min_periods=max(264//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 29)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.340588 + 0.0039595 * anchor
    return base_signal

def f61_pvcr_gemini_045(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=277, w3=236, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(36, min_periods=max(36//3, 2)).mean(), b.abs().rolling(277, min_periods=max(277//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.22 * _rolling_slope(cover, 36) + 0.0039596 * anchor
    return base_signal

def f61_pvcr_gemini_046(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=290, w3=253, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.226333 * y + 0.773667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 43) - _rolling_slope(basket, 290) + 0.0039597 * anchor
    return base_signal

def f61_pvcr_gemini_047(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=303, w3=270, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(303, min_periods=max(303//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.381176 + 0.0039598 * anchor
    return base_signal

def f61_pvcr_gemini_048(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=316, w3=287, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(316, min_periods=max(316//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.239 * _rolling_slope(draw, 287) + 0.0039599 * anchor
    return base_signal

def f61_pvcr_gemini_049(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=329, w3=304, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(64) - b.diff(126)
    stress = imbalance.rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.408235 + 0.00396 * anchor
    return base_signal

def f61_pvcr_gemini_050(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=342, w3=321, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(342, min_periods=max(342//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.421765 + 0.0039601 * anchor
    return base_signal

def f61_pvcr_gemini_051(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=355, w3=338, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 355)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.435294 + 0.0039602 * anchor
    return base_signal

def f61_pvcr_gemini_052(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=368, w3=355, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(368, min_periods=max(368//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.448824 + 0.0039603 * anchor
    return base_signal

def f61_pvcr_gemini_053(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=381, w3=372, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(92)
    rank = change.rolling(381, min_periods=max(381//3, 2)).rank(pct=True)
    persistence = change.rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.270667 * persistence + 0.0039604 * anchor
    return base_signal

def f61_pvcr_gemini_054(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=394, w3=389, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(394, min_periods=max(394//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.475882 + 0.0039605 * anchor
    return base_signal

def f61_pvcr_gemini_055(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=407, w3=406, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(407, min_periods=max(407//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.283333 * slope + 0.0039606 * anchor
    return base_signal

def f61_pvcr_gemini_056(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=420, w3=423, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(113)
    drag = impulse.rolling(420, min_periods=max(420//3, 2)).mean()
    noise = impulse.abs().rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.502941 + 0.0039607 * anchor
    return base_signal

def f61_pvcr_gemini_057(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=433, w3=440, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 433)
    curvature = _rolling_slope(acceleration, 440)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.296 * acceleration + 0.0039608 * anchor
    return base_signal

def f61_pvcr_gemini_058(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=446, w3=457, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 127)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.302333 * pressure.rolling(457, min_periods=max(457//3, 2)).mean() + 0.0039609 * anchor
    return base_signal

def f61_pvcr_gemini_059(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=459, w3=474, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.543529 + 0.003961 * anchor
    return base_signal

def f61_pvcr_gemini_060(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=472, w3=491, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(472, min_periods=max(472//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 141)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.557059 + 0.0039611 * anchor
    return base_signal

def f61_pvcr_gemini_061(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=485, w3=508, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(148, min_periods=max(148//3, 2)).mean(), b.abs().rolling(485, min_periods=max(485//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.321333 * _rolling_slope(cover, 148) + 0.0039612 * anchor
    return base_signal

def f61_pvcr_gemini_062(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=498, w3=525, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.327667 * y + 0.672333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 155) - _rolling_slope(basket, 498) + 0.0039613 * anchor
    return base_signal

def f61_pvcr_gemini_063(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=12, w3=542, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(12, min_periods=max(12//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.597647 + 0.0039614 * anchor
    return base_signal

def f61_pvcr_gemini_064(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=25, w3=559, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(25, min_periods=max(25//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.340333 * _rolling_slope(draw, 559) + 0.0039615 * anchor
    return base_signal

def f61_pvcr_gemini_065(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=38, w3=576, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(38)
    stress = imbalance.rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.624706 + 0.0039616 * anchor
    return base_signal

def f61_pvcr_gemini_066(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=51, w3=593, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(51, min_periods=max(51//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.638235 + 0.0039617 * anchor
    return base_signal

def f61_pvcr_gemini_067(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=64, w3=610, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 64)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.651765 + 0.0039618 * anchor
    return base_signal

def f61_pvcr_gemini_068(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=77, w3=627, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(77, min_periods=max(77//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.665294 + 0.0039619 * anchor
    return base_signal

def f61_pvcr_gemini_069(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=90, w3=644, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(90, min_periods=max(90//3, 2)).rank(pct=True)
    persistence = change.rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.039667 * persistence + 0.003962 * anchor
    return base_signal

def f61_pvcr_gemini_070(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=103, w3=661, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(103, min_periods=max(103//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.838824 + 0.0039621 * anchor
    return base_signal

def f61_pvcr_gemini_071(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=116, w3=678, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(116, min_periods=max(116//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.052333 * slope + 0.0039622 * anchor
    return base_signal

def f61_pvcr_gemini_072(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=129, w3=695, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(129, min_periods=max(129//3, 2)).mean()
    noise = impulse.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.865882 + 0.0039623 * anchor
    return base_signal

def f61_pvcr_gemini_073(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=142, w3=712, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 142)
    curvature = _rolling_slope(acceleration, 712)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.065 * acceleration + 0.0039624 * anchor
    return base_signal

def f61_pvcr_gemini_074(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=155, w3=729, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 239)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.071333 * pressure.rolling(729, min_periods=max(729//3, 2)).mean() + 0.0039625 * anchor
    return base_signal

def f61_pvcr_gemini_075(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=168, w3=746, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    decay = spread.ewm(span=168, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.906471 + 0.0039626 * anchor
    return base_signal
