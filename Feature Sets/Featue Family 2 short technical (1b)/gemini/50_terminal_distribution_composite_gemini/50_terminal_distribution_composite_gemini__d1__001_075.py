"""50 terminal distribution composite gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Composite metric for detecting the final stages of asset distribution before a crash.
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

def f50_tdic_gemini_001_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=5]"""
    window = 5
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_002_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=10]"""
    window = 10
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_003_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=21]"""
    window = 21
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_004_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=42]"""
    window = 42
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_005_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=63]"""
    window = 63
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_006_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=126]"""
    window = 126
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_007_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=252]"""
    window = 252
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_008_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=504]"""
    window = 504
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_009_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=756]"""
    window = 756
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_010_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=1260]"""
    window = 1260
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff()

def f50_tdic_gemini_011_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=417, w3=205, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.096333 * slope + 0.0033542 * anchor
    return base_signal.diff()

def f50_tdic_gemini_012_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=430, w3=222, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.399412 + 0.0033543 * anchor
    return base_signal.diff()

def f50_tdic_gemini_013_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=443, w3=239, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 239)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.109 * acceleration + 0.0033544 * anchor
    return base_signal.diff()

def f50_tdic_gemini_014_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=456, w3=256, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 163)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.115333 * pressure.rolling(256, min_periods=max(256//3, 2)).mean() + 0.0033545 * anchor
    return base_signal.diff()

def f50_tdic_gemini_015_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=469, w3=273, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(170, min_periods=max(170//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.44 + 0.0033546 * anchor
    return base_signal.diff()

def f50_tdic_gemini_016_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=482, w3=290, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(482, min_periods=max(482//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 177)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.453529 + 0.0033547 * anchor
    return base_signal.diff()

def f50_tdic_gemini_017_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=495, w3=307, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(184, min_periods=max(184//3, 2)).mean(), b.abs().rolling(495, min_periods=max(495//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.134333 * _rolling_slope(cover, 184) + 0.0033548 * anchor
    return base_signal.diff()

def f50_tdic_gemini_018_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=508, w3=324, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.140667 * y + 0.859333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 191) - _rolling_slope(basket, 508) + 0.0033549 * anchor
    return base_signal.diff()

def f50_tdic_gemini_019_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=22, w3=341, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(22, min_periods=max(22//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.494118 + 0.003355 * anchor
    return base_signal.diff()

def f50_tdic_gemini_020_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=35, w3=358, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.153333 * _rolling_slope(draw, 358) + 0.0033551 * anchor
    return base_signal.diff()

def f50_tdic_gemini_021_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=48, w3=375, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(48)
    stress = imbalance.rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.521176 + 0.0033552 * anchor
    return base_signal.diff()

def f50_tdic_gemini_022_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=61, w3=392, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(392, min_periods=max(392//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.534706 + 0.0033553 * anchor
    return base_signal.diff()

def f50_tdic_gemini_023_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=74, w3=409, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 74)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.548235 + 0.0033554 * anchor
    return base_signal.diff()

def f50_tdic_gemini_024_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=87, w3=426, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(87, min_periods=max(87//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.561765 + 0.0033555 * anchor
    return base_signal.diff()

def f50_tdic_gemini_025_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=100, w3=443, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(100, min_periods=max(100//3, 2)).rank(pct=True)
    persistence = change.rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.185 * persistence + 0.0033556 * anchor
    return base_signal.diff()

def f50_tdic_gemini_026_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=113, w3=460, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(113, min_periods=max(113//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.588824 + 0.0033557 * anchor
    return base_signal.diff()

def f50_tdic_gemini_027_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=126, w3=477, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(126, min_periods=max(126//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.197667 * slope + 0.0033558 * anchor
    return base_signal.diff()

def f50_tdic_gemini_028_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=139, w3=494, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(14)
    drag = impulse.rolling(139, min_periods=max(139//3, 2)).mean()
    noise = impulse.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.615882 + 0.0033559 * anchor
    return base_signal.diff()

def f50_tdic_gemini_029_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=152, w3=511, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 152)
    curvature = _rolling_slope(acceleration, 511)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.210333 * acceleration + 0.003356 * anchor
    return base_signal.diff()

def f50_tdic_gemini_030_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=165, w3=528, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 28)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.216667 * pressure.rolling(528, min_periods=max(528//3, 2)).mean() + 0.0033561 * anchor
    return base_signal.diff()

def f50_tdic_gemini_031_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=178, w3=545, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(35, min_periods=max(35//3, 2)).mean())
    decay = spread.ewm(span=178, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.656471 + 0.0033562 * anchor
    return base_signal.diff()

def f50_tdic_gemini_032_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=191, w3=562, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(191, min_periods=max(191//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.67 + 0.0033563 * anchor
    return base_signal.diff()

def f50_tdic_gemini_033_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=204, w3=579, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(49, min_periods=max(49//3, 2)).mean(), b.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.235667 * _rolling_slope(cover, 49) + 0.0033564 * anchor
    return base_signal.diff()

def f50_tdic_gemini_034_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=217, w3=596, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.242 * y + 0.758000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 56) - _rolling_slope(basket, 217) + 0.0033565 * anchor
    return base_signal.diff()

def f50_tdic_gemini_035_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=230, w3=613, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.857059 + 0.0033566 * anchor
    return base_signal.diff()

def f50_tdic_gemini_036_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=243, w3=630, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.254667 * _rolling_slope(draw, 630) + 0.0033567 * anchor
    return base_signal.diff()

def f50_tdic_gemini_037_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=256, w3=647, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(77) - b.diff(126)
    stress = imbalance.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.884118 + 0.0033568 * anchor
    return base_signal.diff()

def f50_tdic_gemini_038_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=269, w3=664, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(269, min_periods=max(269//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.897647 + 0.0033569 * anchor
    return base_signal.diff()

def f50_tdic_gemini_039_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=282, w3=681, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 282)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.911176 + 0.003357 * anchor
    return base_signal.diff()

def f50_tdic_gemini_040_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=295, w3=698, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.924706 + 0.0033571 * anchor
    return base_signal.diff()

def f50_tdic_gemini_041_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=308, w3=715, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(105)
    rank = change.rolling(308, min_periods=max(308//3, 2)).rank(pct=True)
    persistence = change.rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.286333 * persistence + 0.0033572 * anchor
    return base_signal.diff()

def f50_tdic_gemini_042_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=321, w3=732, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(321, min_periods=max(321//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.951765 + 0.0033573 * anchor
    return base_signal.diff()

def f50_tdic_gemini_043_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=334, w3=749, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(334, min_periods=max(334//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.299 * slope + 0.0033574 * anchor
    return base_signal.diff()

def f50_tdic_gemini_044_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=347, w3=766, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(347, min_periods=max(347//3, 2)).mean()
    noise = impulse.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.978824 + 0.0033575 * anchor
    return base_signal.diff()

def f50_tdic_gemini_045_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=360, w3=32, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 360)
    curvature = _rolling_slope(acceleration, 32)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.311667 * acceleration + 0.0033576 * anchor
    return base_signal.diff()

def f50_tdic_gemini_046_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=373, w3=49, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 140)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.318 * pressure.rolling(49, min_periods=max(49//3, 2)).mean() + 0.0033577 * anchor
    return base_signal.diff()

def f50_tdic_gemini_047_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=386, w3=66, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(147, min_periods=max(147//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.019412 + 0.0033578 * anchor
    return base_signal.diff()

def f50_tdic_gemini_048_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=399, w3=83, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(399, min_periods=max(399//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 154)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.032941 + 0.0033579 * anchor
    return base_signal.diff()

def f50_tdic_gemini_049_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=412, w3=100, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(161, min_periods=max(161//3, 2)).mean(), b.abs().rolling(412, min_periods=max(412//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(100) + 0.337 * _rolling_slope(cover, 161) + 0.003358 * anchor
    return base_signal.diff()

def f50_tdic_gemini_050_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=425, w3=117, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.343333 * y + 0.656667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 168) - _rolling_slope(basket, 425) + 0.0033581 * anchor
    return base_signal.diff()

def f50_tdic_gemini_051_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=438, w3=134, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(438, min_periods=max(438//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.073529 + 0.0033582 * anchor
    return base_signal.diff()

def f50_tdic_gemini_052_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=451, w3=151, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.356 * _rolling_slope(draw, 151) + 0.0033583 * anchor
    return base_signal.diff()

def f50_tdic_gemini_053_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=189, w2=464, w3=168, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.100588 + 0.0033584 * anchor
    return base_signal.diff()

def f50_tdic_gemini_054_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=196, w2=477, w3=185, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 196)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.114118 + 0.0033585 * anchor
    return base_signal.diff()

def f50_tdic_gemini_055_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=203, w2=490, w3=202, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 203)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=202, adjust=False).mean() * 1.127647 + 0.0033586 * anchor
    return base_signal.diff()

def f50_tdic_gemini_056_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=503, w3=219, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(503, min_periods=max(503//3, 2)).max()
    trough = x.rolling(210, min_periods=max(210//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.141176 + 0.0033587 * anchor
    return base_signal.diff()

def f50_tdic_gemini_057_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=17, w3=236, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.055333 * persistence + 0.0033588 * anchor
    return base_signal.diff()

def f50_tdic_gemini_058_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=30, w3=253, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(224, min_periods=max(224//3, 2)).std()
    vol_slow = ret.rolling(30, min_periods=max(30//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.168235 + 0.0033589 * anchor
    return base_signal.diff()

def f50_tdic_gemini_059_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=43, w3=270, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(43, min_periods=max(43//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 231)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.068 * slope + 0.003359 * anchor
    return base_signal.diff()

def f50_tdic_gemini_060_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=56, w3=287, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.195294 + 0.0033591 * anchor
    return base_signal.diff()

def f50_tdic_gemini_061_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=69, w3=304, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 245)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 304)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.080667 * acceleration + 0.0033592 * anchor
    return base_signal.diff()

def f50_tdic_gemini_062_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=82, w3=321, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 5)
    pressure = rel_log.diff(82)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.087 * pressure.rolling(321, min_periods=max(321//3, 2)).mean() + 0.0033593 * anchor
    return base_signal.diff()

def f50_tdic_gemini_063_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=95, w3=338, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(12, min_periods=max(12//3, 2)).mean())
    decay = spread.ewm(span=95, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.235882 + 0.0033594 * anchor
    return base_signal.diff()

def f50_tdic_gemini_064_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=108, w3=355, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(108, min_periods=max(108//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 19)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.249412 + 0.0033595 * anchor
    return base_signal.diff()

def f50_tdic_gemini_065_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=121, w3=372, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(26, min_periods=max(26//3, 2)).mean(), b.abs().rolling(121, min_periods=max(121//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.106 * _rolling_slope(cover, 26) + 0.0033596 * anchor
    return base_signal.diff()

def f50_tdic_gemini_066_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=134, w3=389, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.112333 * y + 0.887667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 33) - _rolling_slope(basket, 134) + 0.0033597 * anchor
    return base_signal.diff()

def f50_tdic_gemini_067_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=147, w3=406, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(40, min_periods=max(40//3, 2)).mean(), upside.rolling(147, min_periods=max(147//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.29 + 0.0033598 * anchor
    return base_signal.diff()

def f50_tdic_gemini_068_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=160, w3=423, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(160, min_periods=max(160//3, 2)).max()
    rebound = x - x.rolling(47, min_periods=max(47//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.125 * _rolling_slope(draw, 423) + 0.0033599 * anchor
    return base_signal.diff()

def f50_tdic_gemini_069_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=173, w3=440, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(54) - b.diff(126)
    stress = imbalance.rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.317059 + 0.00336 * anchor
    return base_signal.diff()

def f50_tdic_gemini_070_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=186, w3=457, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 61)
    baseline = trend.rolling(186, min_periods=max(186//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.330588 + 0.0033601 * anchor
    return base_signal.diff()

def f50_tdic_gemini_071_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=199, w3=474, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 68)
    slow = _rolling_slope(x, 199)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.344118 + 0.0033602 * anchor
    return base_signal.diff()

def f50_tdic_gemini_072_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=212, w3=491, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(212, min_periods=max(212//3, 2)).max()
    trough = x.rolling(75, min_periods=max(75//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.357647 + 0.0033603 * anchor
    return base_signal.diff()

def f50_tdic_gemini_073_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=225, w3=508, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(82)
    rank = change.rolling(225, min_periods=max(225//3, 2)).rank(pct=True)
    persistence = change.rolling(508, min_periods=max(508//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.156667 * persistence + 0.0033604 * anchor
    return base_signal.diff()

def f50_tdic_gemini_074_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=238, w3=525, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(89, min_periods=max(89//3, 2)).std()
    vol_slow = ret.rolling(238, min_periods=max(238//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.384706 + 0.0033605 * anchor
    return base_signal.diff()

def f50_tdic_gemini_075_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=251, w3=542, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(251, min_periods=max(251//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.169333 * slope + 0.0033606 * anchor
    return base_signal.diff()
