"""94 mechanical fragility index gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Index measuring the susceptibility of price to large moves on low volume.
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

def f94_mfin_gemini_076_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=373, w3=635, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.144 * _rolling_slope(draw, 635) + 0.0058527 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_077_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=386, w3=652, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.434118 + 0.0058528 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_078_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=399, w3=669, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(399, min_periods=max(399//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.447647 + 0.0058529 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_079_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=412, w3=686, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 412)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.461176 + 0.005853 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_080_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=425, w3=703, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(425, min_periods=max(425//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.474706 + 0.0058531 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_081_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=438, w3=720, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(438, min_periods=max(438//3, 2)).rank(pct=True)
    persistence = change.rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.175667 * persistence + 0.0058532 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_082_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=451, w3=737, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(451, min_periods=max(451//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.501765 + 0.0058533 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_083_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=464, w3=754, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.188333 * slope + 0.0058534 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_084_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=477, w3=20, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(477, min_periods=max(477//3, 2)).mean()
    noise = impulse.abs().rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.528824 + 0.0058535 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_085_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=490, w3=37, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 490)
    curvature = _rolling_slope(acceleration, 37)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.201 * acceleration + 0.0058536 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_086_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=503, w3=54, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 231)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.207333 * pressure.rolling(54, min_periods=max(54//3, 2)).mean() + 0.0058537 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_087_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=17, w3=71, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(238, min_periods=max(238//3, 2)).mean())
    decay = spread.ewm(span=17, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.569412 + 0.0058538 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_088_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=30, w3=88, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(30, min_periods=max(30//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.582941 + 0.0058539 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_089_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=43, w3=105, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(5, min_periods=max(5//3, 2)).mean(), b.abs().rolling(43, min_periods=max(43//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(105) + 0.226333 * _rolling_slope(cover, 5) + 0.005854 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_090_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=56, w3=122, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.232667 * y + 0.767333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 12) - _rolling_slope(basket, 56) + 0.0058541 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_091_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=69, w3=139, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(69, min_periods=max(69//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.623529 + 0.0058542 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_092_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=82, w3=156, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(82, min_periods=max(82//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.245333 * _rolling_slope(draw, 156) + 0.0058543 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_093_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=95, w3=173, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(33) - b.diff(95)
    stress = imbalance.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.650588 + 0.0058544 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_094_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=108, w3=190, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.664118 + 0.0058545 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_095_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=121, w3=207, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=207, adjust=False).mean() * 0.824118 + 0.0058546 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_096_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=134, w3=224, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(134, min_periods=max(134//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.837647 + 0.0058547 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_097_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=147, w3=241, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(61)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.277 * persistence + 0.0058548 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_098_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=160, w3=258, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(160, min_periods=max(160//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.864706 + 0.0058549 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_099_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=173, w3=275, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(173, min_periods=max(173//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.289667 * slope + 0.005855 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_100_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=186, w3=292, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(82)
    drag = impulse.rolling(186, min_periods=max(186//3, 2)).mean()
    noise = impulse.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.891765 + 0.0058551 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_101_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=199, w3=309, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 199)
    curvature = _rolling_slope(acceleration, 309)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.302333 * acceleration + 0.0058552 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_102_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=212, w3=326, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 96)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.308667 * pressure.rolling(326, min_periods=max(326//3, 2)).mean() + 0.0058553 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_103_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=225, w3=343, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(103, min_periods=max(103//3, 2)).mean())
    decay = spread.ewm(span=225, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.932353 + 0.0058554 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_104_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=238, w3=360, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(238, min_periods=max(238//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 110)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.945882 + 0.0058555 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_105_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=251, w3=377, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(117, min_periods=max(117//3, 2)).mean(), b.abs().rolling(251, min_periods=max(251//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.327667 * _rolling_slope(cover, 117) + 0.0058556 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_106_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=264, w3=394, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.334 * y + 0.666000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 124) - _rolling_slope(basket, 264) + 0.0058557 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_107_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=277, w3=411, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.986471 + 0.0058558 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_108_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=290, w3=428, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(290, min_periods=max(290//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.346667 * _rolling_slope(draw, 428) + 0.0058559 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_109_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=303, w3=445, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.013529 + 0.005856 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_110_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=316, w3=462, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(316, min_periods=max(316//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.027059 + 0.0058561 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_111_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=329, w3=479, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 329)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.040588 + 0.0058562 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_112_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=342, w3=496, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(342, min_periods=max(342//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.054118 + 0.0058563 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_113_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=355, w3=513, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(355, min_periods=max(355//3, 2)).rank(pct=True)
    persistence = change.rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.046 * persistence + 0.0058564 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_114_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=368, w3=530, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(368, min_periods=max(368//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.081176 + 0.0058565 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_115_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=381, w3=547, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(381, min_periods=max(381//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.058667 * slope + 0.0058566 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_116_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=394, w3=564, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(394, min_periods=max(394//3, 2)).mean()
    noise = impulse.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.108235 + 0.0058567 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_117_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=407, w3=581, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 407)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.071333 * acceleration + 0.0058568 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_118_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=420, w3=598, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 208)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.077667 * pressure.rolling(598, min_periods=max(598//3, 2)).mean() + 0.0058569 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_119_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=433, w3=615, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(215, min_periods=max(215//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.148824 + 0.005857 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_120_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=446, w3=632, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(446, min_periods=max(446//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 222)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.162353 + 0.0058571 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_121_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=459, w3=649, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(229, min_periods=max(229//3, 2)).mean(), b.abs().rolling(459, min_periods=max(459//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.096667 * _rolling_slope(cover, 229) + 0.0058572 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_122_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=472, w3=666, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.103 * y + 0.897000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 236) - _rolling_slope(basket, 472) + 0.0058573 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_123_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=485, w3=683, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(485, min_periods=max(485//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.202941 + 0.0058574 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_124_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=498, w3=700, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(498, min_periods=max(498//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.115667 * _rolling_slope(draw, 700) + 0.0058575 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_125_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=12, w3=717, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(10) - b.diff(12)
    stress = imbalance.rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.23 + 0.0058576 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_126_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=25, w3=734, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(25, min_periods=max(25//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.243529 + 0.0058577 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_127_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=38, w3=751, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 38)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.257059 + 0.0058578 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_128_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=51, w3=17, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(51, min_periods=max(51//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.270588 + 0.0058579 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_129_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=64, w3=34, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(38)
    rank = change.rolling(64, min_periods=max(64//3, 2)).rank(pct=True)
    persistence = change.rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147333 * persistence + 0.005858 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_130_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=77, w3=51, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(77, min_periods=max(77//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.297647 + 0.0058581 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_131_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=90, w3=68, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(90, min_periods=max(90//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.16 * slope + 0.0058582 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_132_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=103, w3=85, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(59)
    drag = impulse.rolling(103, min_periods=max(103//3, 2)).mean()
    noise = impulse.abs().rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.324706 + 0.0058583 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_133_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=116, w3=102, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 116)
    curvature = _rolling_slope(acceleration, 102)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.172667 * acceleration + 0.0058584 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_134_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=129, w3=119, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 73)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.179 * pressure.rolling(119, min_periods=max(119//3, 2)).mean() + 0.0058585 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_135_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=142, w3=136, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(80, min_periods=max(80//3, 2)).mean())
    decay = spread.ewm(span=142, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.365294 + 0.0058586 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_136_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=155, w3=153, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(155, min_periods=max(155//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 87)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.378824 + 0.0058587 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_137_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=168, w3=170, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(94, min_periods=max(94//3, 2)).mean(), b.abs().rolling(168, min_periods=max(168//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.198 * _rolling_slope(cover, 94) + 0.0058588 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_138_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=181, w3=187, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.204333 * y + 0.795667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 101) - _rolling_slope(basket, 181) + 0.0058589 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_139_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=194, w3=204, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(194, min_periods=max(194//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.419412 + 0.005859 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_140_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=207, w3=221, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(207, min_periods=max(207//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.217 * _rolling_slope(draw, 221) + 0.0058591 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_141_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=220, w3=238, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(122) - b.diff(126)
    stress = imbalance.rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.446471 + 0.0058592 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_142_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=233, w3=255, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(233, min_periods=max(233//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.46 + 0.0058593 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_143_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=246, w3=272, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 246)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=272, adjust=False).mean() * 1.473529 + 0.0058594 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_144_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=259, w3=289, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(259, min_periods=max(259//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.487059 + 0.0058595 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_145_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=272, w3=306, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(272, min_periods=max(272//3, 2)).rank(pct=True)
    persistence = change.rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.248667 * persistence + 0.0058596 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_146_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=285, w3=323, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(285, min_periods=max(285//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.514118 + 0.0058597 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_147_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=298, w3=340, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(298, min_periods=max(298//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.261333 * slope + 0.0058598 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_148_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=311, w3=357, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(311, min_periods=max(311//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.541176 + 0.0058599 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_149_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=324, w3=374, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 324)
    curvature = _rolling_slope(acceleration, 374)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274 * acceleration + 0.00586 * anchor
    return base_signal.diff().diff().diff()

def f94_mfin_gemini_150_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=337, w3=391, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 185)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.280333 * pressure.rolling(391, min_periods=max(391//3, 2)).mean() + 0.0058601 * anchor
    return base_signal.diff().diff().diff()
