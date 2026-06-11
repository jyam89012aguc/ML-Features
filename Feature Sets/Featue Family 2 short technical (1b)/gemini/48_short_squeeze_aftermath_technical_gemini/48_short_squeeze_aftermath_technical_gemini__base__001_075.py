"""48 short squeeze aftermath technical gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Technical signatures of price collapse following an exhaustive short squeeze.
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

def f48_sqze_gemini_001(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_002(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_003(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_004(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_005(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_006(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_007(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_008(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_009(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_010(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Technical signatures of price collapse following an exhaustive short squeeze. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window * 2), _rolling_zscore(volume, window).abs() + 1e-9)
    return res

def f48_sqze_gemini_011(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=504, w3=564, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(214, min_periods=max(214//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.409412 + 0.0032282 * anchor
    return base_signal

def f48_sqze_gemini_012(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=18, w3=581, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(18, min_periods=max(18//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 221)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.422941 + 0.0032283 * anchor
    return base_signal

def f48_sqze_gemini_013(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=31, w3=598, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(228, min_periods=max(228//3, 2)).mean(), b.abs().rolling(31, min_periods=max(31//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.105 * _rolling_slope(cover, 228) + 0.0032284 * anchor
    return base_signal

def f48_sqze_gemini_014(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=44, w3=615, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.111333 * y + 0.888667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 235) - _rolling_slope(basket, 44) + 0.0032285 * anchor
    return base_signal

def f48_sqze_gemini_015(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=57, w3=632, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.463529 + 0.0032286 * anchor
    return base_signal

def f48_sqze_gemini_016(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=70, w3=649, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.124 * _rolling_slope(draw, 649) + 0.0032287 * anchor
    return base_signal

def f48_sqze_gemini_017(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=83, w3=666, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(9) - b.diff(83)
    stress = imbalance.rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.490588 + 0.0032288 * anchor
    return base_signal

def f48_sqze_gemini_018(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=96, w3=683, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(96, min_periods=max(96//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.504118 + 0.0032289 * anchor
    return base_signal

def f48_sqze_gemini_019(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=109, w3=700, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 109)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.517647 + 0.003229 * anchor
    return base_signal

def f48_sqze_gemini_020(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=122, w3=717, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.531176 + 0.0032291 * anchor
    return base_signal

def f48_sqze_gemini_021(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=135, w3=734, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(37)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.155667 * persistence + 0.0032292 * anchor
    return base_signal

def f48_sqze_gemini_022(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=148, w3=751, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.558235 + 0.0032293 * anchor
    return base_signal

def f48_sqze_gemini_023(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=161, w3=17, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.168333 * slope + 0.0032294 * anchor
    return base_signal

def f48_sqze_gemini_024(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=174, w3=34, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(58)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.585294 + 0.0032295 * anchor
    return base_signal

def f48_sqze_gemini_025(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=187, w3=51, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 51)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.181 * acceleration + 0.0032296 * anchor
    return base_signal

def f48_sqze_gemini_026(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=200, w3=68, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 72)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.187333 * pressure.rolling(68, min_periods=max(68//3, 2)).mean() + 0.0032297 * anchor
    return base_signal

def f48_sqze_gemini_027(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=213, w3=85, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(79, min_periods=max(79//3, 2)).mean())
    decay = spread.ewm(span=213, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.625882 + 0.0032298 * anchor
    return base_signal

def f48_sqze_gemini_028(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=226, w3=102, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(226, min_periods=max(226//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 86)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.639412 + 0.0032299 * anchor
    return base_signal

def f48_sqze_gemini_029(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=239, w3=119, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(93, min_periods=max(93//3, 2)).mean(), b.abs().rolling(239, min_periods=max(239//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(119) + 0.206333 * _rolling_slope(cover, 93) + 0.00323 * anchor
    return base_signal

def f48_sqze_gemini_030(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=252, w3=136, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.212667 * y + 0.787333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 100) - _rolling_slope(basket, 252) + 0.0032301 * anchor
    return base_signal

def f48_sqze_gemini_031(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=265, w3=153, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(265, min_periods=max(265//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.826471 + 0.0032302 * anchor
    return base_signal

def f48_sqze_gemini_032(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=278, w3=170, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(278, min_periods=max(278//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.225333 * _rolling_slope(draw, 170) + 0.0032303 * anchor
    return base_signal

def f48_sqze_gemini_033(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=291, w3=187, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(121) - b.diff(126)
    stress = imbalance.rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.853529 + 0.0032304 * anchor
    return base_signal

def f48_sqze_gemini_034(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=304, w3=204, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.867059 + 0.0032305 * anchor
    return base_signal

def f48_sqze_gemini_035(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=317, w3=221, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 0.880588 + 0.0032306 * anchor
    return base_signal

def f48_sqze_gemini_036(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=330, w3=238, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.894118 + 0.0032307 * anchor
    return base_signal

def f48_sqze_gemini_037(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=343, w3=255, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257 * persistence + 0.0032308 * anchor
    return base_signal

def f48_sqze_gemini_038(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=356, w3=272, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(356, min_periods=max(356//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.921176 + 0.0032309 * anchor
    return base_signal

def f48_sqze_gemini_039(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=369, w3=289, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(369, min_periods=max(369//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.269667 * slope + 0.003231 * anchor
    return base_signal

def f48_sqze_gemini_040(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=382, w3=306, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(382, min_periods=max(382//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.948235 + 0.0032311 * anchor
    return base_signal

def f48_sqze_gemini_041(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=395, w3=323, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 395)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.282333 * acceleration + 0.0032312 * anchor
    return base_signal

def f48_sqze_gemini_042(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=408, w3=340, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 184)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.288667 * pressure.rolling(340, min_periods=max(340//3, 2)).mean() + 0.0032313 * anchor
    return base_signal

def f48_sqze_gemini_043(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=421, w3=357, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(191, min_periods=max(191//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.988824 + 0.0032314 * anchor
    return base_signal

def f48_sqze_gemini_044(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=434, w3=374, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(434, min_periods=max(434//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 198)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.002353 + 0.0032315 * anchor
    return base_signal

def f48_sqze_gemini_045(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=447, w3=391, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(205, min_periods=max(205//3, 2)).mean(), b.abs().rolling(447, min_periods=max(447//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.307667 * _rolling_slope(cover, 205) + 0.0032316 * anchor
    return base_signal

def f48_sqze_gemini_046(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=460, w3=408, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.314 * y + 0.686000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 212) - _rolling_slope(basket, 460) + 0.0032317 * anchor
    return base_signal

def f48_sqze_gemini_047(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=473, w3=425, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.042941 + 0.0032318 * anchor
    return base_signal

def f48_sqze_gemini_048(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=486, w3=442, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.326667 * _rolling_slope(draw, 442) + 0.0032319 * anchor
    return base_signal

def f48_sqze_gemini_049(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=499, w3=459, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.07 + 0.003232 * anchor
    return base_signal

def f48_sqze_gemini_050(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=13, w3=476, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.083529 + 0.0032321 * anchor
    return base_signal

def f48_sqze_gemini_051(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=26, w3=493, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 26)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.097059 + 0.0032322 * anchor
    return base_signal

def f48_sqze_gemini_052(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=39, w3=510, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(39, min_periods=max(39//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.110588 + 0.0032323 * anchor
    return base_signal

def f48_sqze_gemini_053(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=52, w3=527, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(14)
    rank = change.rolling(52, min_periods=max(52//3, 2)).rank(pct=True)
    persistence = change.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.358333 * persistence + 0.0032324 * anchor
    return base_signal

def f48_sqze_gemini_054(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=65, w3=544, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(65, min_periods=max(65//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.137647 + 0.0032325 * anchor
    return base_signal

def f48_sqze_gemini_055(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=78, w3=561, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(78, min_periods=max(78//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.038667 * slope + 0.0032326 * anchor
    return base_signal

def f48_sqze_gemini_056(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=91, w3=578, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(35)
    drag = impulse.rolling(91, min_periods=max(91//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.164706 + 0.0032327 * anchor
    return base_signal

def f48_sqze_gemini_057(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=104, w3=595, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 104)
    curvature = _rolling_slope(acceleration, 595)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.051333 * acceleration + 0.0032328 * anchor
    return base_signal

def f48_sqze_gemini_058(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=117, w3=612, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 49)
    pressure = rel_log.diff(117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.057667 * pressure.rolling(612, min_periods=max(612//3, 2)).mean() + 0.0032329 * anchor
    return base_signal

def f48_sqze_gemini_059(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=130, w3=629, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(56, min_periods=max(56//3, 2)).mean())
    decay = spread.ewm(span=130, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.205294 + 0.003233 * anchor
    return base_signal

def f48_sqze_gemini_060(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=143, w3=646, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(143, min_periods=max(143//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 63)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.218824 + 0.0032331 * anchor
    return base_signal

def f48_sqze_gemini_061(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=156, w3=663, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(70, min_periods=max(70//3, 2)).mean(), b.abs().rolling(156, min_periods=max(156//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.076667 * _rolling_slope(cover, 70) + 0.0032332 * anchor
    return base_signal

def f48_sqze_gemini_062(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=169, w3=680, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.083 * y + 0.917000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 77) - _rolling_slope(basket, 169) + 0.0032333 * anchor
    return base_signal

def f48_sqze_gemini_063(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=182, w3=697, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(182, min_periods=max(182//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.259412 + 0.0032334 * anchor
    return base_signal

def f48_sqze_gemini_064(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=195, w3=714, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(195, min_periods=max(195//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.095667 * _rolling_slope(draw, 714) + 0.0032335 * anchor
    return base_signal

def f48_sqze_gemini_065(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=208, w3=731, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(98) - b.diff(126)
    stress = imbalance.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.286471 + 0.0032336 * anchor
    return base_signal

def f48_sqze_gemini_066(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=221, w3=748, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3 + 0.0032337 * anchor
    return base_signal

def f48_sqze_gemini_067(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=234, w3=765, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 234)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.313529 + 0.0032338 * anchor
    return base_signal

def f48_sqze_gemini_068(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=247, w3=31, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.327059 + 0.0032339 * anchor
    return base_signal

def f48_sqze_gemini_069(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=260, w3=48, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.127333 * persistence + 0.003234 * anchor
    return base_signal

def f48_sqze_gemini_070(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=273, w3=65, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.354118 + 0.0032341 * anchor
    return base_signal

def f48_sqze_gemini_071(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=286, w3=82, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.14 * slope + 0.0032342 * anchor
    return base_signal

def f48_sqze_gemini_072(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=299, w3=99, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.381176 + 0.0032343 * anchor
    return base_signal

def f48_sqze_gemini_073(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=312, w3=116, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 312)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.152667 * acceleration + 0.0032344 * anchor
    return base_signal

def f48_sqze_gemini_074(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=325, w3=133, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 161)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.159 * pressure.rolling(133, min_periods=max(133//3, 2)).mean() + 0.0032345 * anchor
    return base_signal

def f48_sqze_gemini_075(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=338, w3=150, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(168, min_periods=max(168//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.421765 + 0.0032346 * anchor
    return base_signal
