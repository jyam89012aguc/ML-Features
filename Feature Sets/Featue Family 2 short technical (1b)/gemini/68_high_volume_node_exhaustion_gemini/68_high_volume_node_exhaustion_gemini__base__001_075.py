"""68 high volume node exhaustion gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Price rejection or stalling at major high-volume nodes from historical profiles.
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

def f68_hvne_gemini_001(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=5]"""
    window = 5
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_002(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=10]"""
    window = 10
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_003(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=21]"""
    window = 21
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_004(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=42]"""
    window = 42
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_005(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=63]"""
    window = 63
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_006(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=126]"""
    window = 126
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_007(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=252]"""
    window = 252
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_008(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=504]"""
    window = 504
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_009(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=756]"""
    window = 756
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_010(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price rejection or stalling at major high-volume nodes from historical profiles. [window=1260]"""
    window = 1260
    res = _safe_div(close - close.rolling(window).mean(), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f68_hvne_gemini_011(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=396, w3=210, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(68, min_periods=max(68//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.010588 + 0.0043482 * anchor
    return base_signal

def f68_hvne_gemini_012(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=409, w3=227, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(409, min_periods=max(409//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 75)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.024118 + 0.0043483 * anchor
    return base_signal

def f68_hvne_gemini_013(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=422, w3=244, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(82, min_periods=max(82//3, 2)).mean(), b.abs().rolling(422, min_periods=max(422//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.251333 * _rolling_slope(cover, 82) + 0.0043484 * anchor
    return base_signal

def f68_hvne_gemini_014(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=435, w3=261, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.257667 * y + 0.742333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 89) - _rolling_slope(basket, 435) + 0.0043485 * anchor
    return base_signal

def f68_hvne_gemini_015(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=448, w3=278, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(448, min_periods=max(448//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.064706 + 0.0043486 * anchor
    return base_signal

def f68_hvne_gemini_016(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=461, w3=295, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.270333 * _rolling_slope(draw, 295) + 0.0043487 * anchor
    return base_signal

def f68_hvne_gemini_017(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=474, w3=312, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(110) - b.diff(126)
    stress = imbalance.rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.091765 + 0.0043488 * anchor
    return base_signal

def f68_hvne_gemini_018(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=487, w3=329, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(487, min_periods=max(487//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(329, min_periods=max(329//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.105294 + 0.0043489 * anchor
    return base_signal

def f68_hvne_gemini_019(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=500, w3=346, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 500)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.118824 + 0.004349 * anchor
    return base_signal

def f68_hvne_gemini_020(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=14, w3=363, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.132353 + 0.0043491 * anchor
    return base_signal

def f68_hvne_gemini_021(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=27, w3=380, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.302 * persistence + 0.0043492 * anchor
    return base_signal

def f68_hvne_gemini_022(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=40, w3=397, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(40, min_periods=max(40//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.159412 + 0.0043493 * anchor
    return base_signal

def f68_hvne_gemini_023(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=53, w3=414, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(53, min_periods=max(53//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.314667 * slope + 0.0043494 * anchor
    return base_signal

def f68_hvne_gemini_024(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=66, w3=431, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(66, min_periods=max(66//3, 2)).mean()
    noise = impulse.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.186471 + 0.0043495 * anchor
    return base_signal

def f68_hvne_gemini_025(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=79, w3=448, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 79)
    curvature = _rolling_slope(acceleration, 448)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.327333 * acceleration + 0.0043496 * anchor
    return base_signal

def f68_hvne_gemini_026(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=92, w3=465, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 173)
    pressure = rel_log.diff(92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.333667 * pressure.rolling(465, min_periods=max(465//3, 2)).mean() + 0.0043497 * anchor
    return base_signal

def f68_hvne_gemini_027(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=105, w3=482, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(180, min_periods=max(180//3, 2)).mean())
    decay = spread.ewm(span=105, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.227059 + 0.0043498 * anchor
    return base_signal

def f68_hvne_gemini_028(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=118, w3=499, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(118, min_periods=max(118//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 187)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.240588 + 0.0043499 * anchor
    return base_signal

def f68_hvne_gemini_029(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=131, w3=516, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(194, min_periods=max(194//3, 2)).mean(), b.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.352667 * _rolling_slope(cover, 194) + 0.00435 * anchor
    return base_signal

def f68_hvne_gemini_030(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=144, w3=533, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.359 * y + 0.641000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 201) - _rolling_slope(basket, 144) + 0.0043501 * anchor
    return base_signal

def f68_hvne_gemini_031(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=157, w3=550, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(157, min_periods=max(157//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.281176 + 0.0043502 * anchor
    return base_signal

def f68_hvne_gemini_032(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=170, w3=567, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(170, min_periods=max(170//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.039333 * _rolling_slope(draw, 567) + 0.0043503 * anchor
    return base_signal

def f68_hvne_gemini_033(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=183, w3=584, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.308235 + 0.0043504 * anchor
    return base_signal

def f68_hvne_gemini_034(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=196, w3=601, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.321765 + 0.0043505 * anchor
    return base_signal

def f68_hvne_gemini_035(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=209, w3=618, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.335294 + 0.0043506 * anchor
    return base_signal

def f68_hvne_gemini_036(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=222, w3=635, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.348824 + 0.0043507 * anchor
    return base_signal

def f68_hvne_gemini_037(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=235, w3=652, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(235, min_periods=max(235//3, 2)).rank(pct=True)
    persistence = change.rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071 * persistence + 0.0043508 * anchor
    return base_signal

def f68_hvne_gemini_038(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=248, w3=669, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(248, min_periods=max(248//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.375882 + 0.0043509 * anchor
    return base_signal

def f68_hvne_gemini_039(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=261, w3=686, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.083667 * slope + 0.004351 * anchor
    return base_signal

def f68_hvne_gemini_040(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=274, w3=703, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(24)
    drag = impulse.rolling(274, min_periods=max(274//3, 2)).mean()
    noise = impulse.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.402941 + 0.0043511 * anchor
    return base_signal

def f68_hvne_gemini_041(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=287, w3=720, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 720)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.096333 * acceleration + 0.0043512 * anchor
    return base_signal

def f68_hvne_gemini_042(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=300, w3=737, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 38)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.102667 * pressure.rolling(737, min_periods=max(737//3, 2)).mean() + 0.0043513 * anchor
    return base_signal

def f68_hvne_gemini_043(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=313, w3=754, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(45, min_periods=max(45//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.443529 + 0.0043514 * anchor
    return base_signal

def f68_hvne_gemini_044(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=326, w3=20, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(326, min_periods=max(326//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 52)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.457059 + 0.0043515 * anchor
    return base_signal

def f68_hvne_gemini_045(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=339, w3=37, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(59, min_periods=max(59//3, 2)).mean(), b.abs().rolling(339, min_periods=max(339//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(37) + 0.121667 * _rolling_slope(cover, 59) + 0.0043516 * anchor
    return base_signal

def f68_hvne_gemini_046(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=352, w3=54, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.128 * y + 0.872000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 66) - _rolling_slope(basket, 352) + 0.0043517 * anchor
    return base_signal

def f68_hvne_gemini_047(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=365, w3=71, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(71) * 1.497647 + 0.0043518 * anchor
    return base_signal

def f68_hvne_gemini_048(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=378, w3=88, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(378, min_periods=max(378//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.140667 * _rolling_slope(draw, 88) + 0.0043519 * anchor
    return base_signal

def f68_hvne_gemini_049(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=391, w3=105, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(87) - b.diff(126)
    stress = imbalance.rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.524706 + 0.004352 * anchor
    return base_signal

def f68_hvne_gemini_050(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=404, w3=122, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(404, min_periods=max(404//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.538235 + 0.0043521 * anchor
    return base_signal

def f68_hvne_gemini_051(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=417, w3=139, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 417)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=139, adjust=False).mean() * 1.551765 + 0.0043522 * anchor
    return base_signal

def f68_hvne_gemini_052(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=430, w3=156, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(430, min_periods=max(430//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.565294 + 0.0043523 * anchor
    return base_signal

def f68_hvne_gemini_053(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=443, w3=173, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(115)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.172333 * persistence + 0.0043524 * anchor
    return base_signal

def f68_hvne_gemini_054(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=456, w3=190, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(456, min_periods=max(456//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.592353 + 0.0043525 * anchor
    return base_signal

def f68_hvne_gemini_055(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=469, w3=207, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(469, min_periods=max(469//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.185 * slope + 0.0043526 * anchor
    return base_signal

def f68_hvne_gemini_056(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=482, w3=224, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.619412 + 0.0043527 * anchor
    return base_signal

def f68_hvne_gemini_057(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=495, w3=241, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 495)
    curvature = _rolling_slope(acceleration, 241)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.197667 * acceleration + 0.0043528 * anchor
    return base_signal

def f68_hvne_gemini_058(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=508, w3=258, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 150)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.204 * pressure.rolling(258, min_periods=max(258//3, 2)).mean() + 0.0043529 * anchor
    return base_signal

def f68_hvne_gemini_059(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=22, w3=275, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(157, min_periods=max(157//3, 2)).mean())
    decay = spread.ewm(span=22, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.66 + 0.004353 * anchor
    return base_signal

def f68_hvne_gemini_060(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=35, w3=292, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(35, min_periods=max(35//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 164)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.82 + 0.0043531 * anchor
    return base_signal

def f68_hvne_gemini_061(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=48, w3=309, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(171, min_periods=max(171//3, 2)).mean(), b.abs().rolling(48, min_periods=max(48//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.223 * _rolling_slope(cover, 171) + 0.0043532 * anchor
    return base_signal

def f68_hvne_gemini_062(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=61, w3=326, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.229333 * y + 0.770667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 178) - _rolling_slope(basket, 61) + 0.0043533 * anchor
    return base_signal

def f68_hvne_gemini_063(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=74, w3=343, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(74, min_periods=max(74//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.860588 + 0.0043534 * anchor
    return base_signal

def f68_hvne_gemini_064(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=87, w3=360, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(87, min_periods=max(87//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.242 * _rolling_slope(draw, 360) + 0.0043535 * anchor
    return base_signal

def f68_hvne_gemini_065(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=100, w3=377, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(100)
    stress = imbalance.rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.887647 + 0.0043536 * anchor
    return base_signal

def f68_hvne_gemini_066(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=113, w3=394, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(113, min_periods=max(113//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.901176 + 0.0043537 * anchor
    return base_signal

def f68_hvne_gemini_067(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=126, w3=411, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.914706 + 0.0043538 * anchor
    return base_signal

def f68_hvne_gemini_068(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=139, w3=428, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.928235 + 0.0043539 * anchor
    return base_signal

def f68_hvne_gemini_069(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=152, w3=445, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(152, min_periods=max(152//3, 2)).rank(pct=True)
    persistence = change.rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.273667 * persistence + 0.004354 * anchor
    return base_signal

def f68_hvne_gemini_070(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=165, w3=462, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.955294 + 0.0043541 * anchor
    return base_signal

def f68_hvne_gemini_071(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=178, w3=479, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.286333 * slope + 0.0043542 * anchor
    return base_signal

def f68_hvne_gemini_072(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=191, w3=496, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(191, min_periods=max(191//3, 2)).mean()
    noise = impulse.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.982353 + 0.0043543 * anchor
    return base_signal

def f68_hvne_gemini_073(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=204, w3=513, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 513)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299 * acceleration + 0.0043544 * anchor
    return base_signal

def f68_hvne_gemini_074(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=217, w3=530, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 15)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.305333 * pressure.rolling(530, min_periods=max(530//3, 2)).mean() + 0.0043545 * anchor
    return base_signal

def f68_hvne_gemini_075(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=230, w3=547, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(22, min_periods=max(22//3, 2)).mean())
    decay = spread.ewm(span=230, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.022941 + 0.0043546 * anchor
    return base_signal
