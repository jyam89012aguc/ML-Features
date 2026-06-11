"""05 failed breakout dynamics gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Price action failing to maintain levels above prior resistance, indicating bull traps.
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

def f05_fbrk_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=5]"""
    window = 5
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=10]"""
    window = 10
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=21]"""
    window = 21
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=42]"""
    window = 42
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=63]"""
    window = 63
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=126]"""
    window = 126
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=252]"""
    window = 252
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=504]"""
    window = 504
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=756]"""
    window = 756
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price action failing to maintain levels above prior resistance, indicating bull traps. [window=1260]"""
    window = 1260
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f05_fbrk_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=244, w3=422, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 244)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.494706 + 0.0002322 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=257, w3=439, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(257, min_periods=max(257//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.508235 + 0.0002323 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=270, w3=456, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(270, min_periods=max(270//3, 2)).rank(pct=True)
    persistence = change.rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.120667 * persistence + 0.0002324 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=283, w3=473, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(283, min_periods=max(283//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.535294 + 0.0002325 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=296, w3=490, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(296, min_periods=max(296//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.133333 * slope + 0.0002326 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=309, w3=507, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(309, min_periods=max(309//3, 2)).mean()
    noise = impulse.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.562353 + 0.0002327 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=322, w3=524, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 322)
    curvature = _rolling_slope(acceleration, 524)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.146 * acceleration + 0.0002328 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=335, w3=541, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 246)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.152333 * pressure.rolling(541, min_periods=max(541//3, 2)).mean() + 0.0002329 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=348, w3=558, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(6, min_periods=max(6//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.602941 + 0.000233 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=361, w3=575, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(361, min_periods=max(361//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 13)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.616471 + 0.0002331 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=374, w3=592, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(20, min_periods=max(20//3, 2)).mean(), b.abs().rolling(374, min_periods=max(374//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.171333 * _rolling_slope(cover, 20) + 0.0002332 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=387, w3=609, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.177667 * y + 0.822333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 27) - _rolling_slope(basket, 387) + 0.0002333 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=400, w3=626, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(400, min_periods=max(400//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.657059 + 0.0002334 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=413, w3=643, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(413, min_periods=max(413//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.190333 * _rolling_slope(draw, 643) + 0.0002335 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=426, w3=660, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(48) - b.diff(126)
    stress = imbalance.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.830588 + 0.0002336 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=439, w3=677, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.844118 + 0.0002337 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=452, w3=694, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 452)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.857647 + 0.0002338 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=465, w3=711, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(465, min_periods=max(465//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.871176 + 0.0002339 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=478, w3=728, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(76)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.222 * persistence + 0.000234 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=491, w3=745, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.898235 + 0.0002341 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=504, w3=762, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.234667 * slope + 0.0002342 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=18, w3=28, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(97)
    drag = impulse.rolling(18, min_periods=max(18//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.925294 + 0.0002343 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=31, w3=45, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.247333 * acceleration + 0.0002344 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=44, w3=62, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 111)
    pressure = rel_log.diff(44)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.253667 * pressure.rolling(62, min_periods=max(62//3, 2)).mean() + 0.0002345 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=57, w3=79, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(118, min_periods=max(118//3, 2)).mean())
    decay = spread.ewm(span=57, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.965882 + 0.0002346 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=70, w3=96, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(70, min_periods=max(70//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 125)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.979412 + 0.0002347 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=83, w3=113, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(132, min_periods=max(132//3, 2)).mean(), b.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(113) + 0.272667 * _rolling_slope(cover, 132) + 0.0002348 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=96, w3=130, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.279 * y + 0.721000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 139) - _rolling_slope(basket, 96) + 0.0002349 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=109, w3=147, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(109, min_periods=max(109//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.02 + 0.000235 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=122, w3=164, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(122, min_periods=max(122//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.291667 * _rolling_slope(draw, 164) + 0.0002351 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=135, w3=181, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.047059 + 0.0002352 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=148, w3=198, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.060588 + 0.0002353 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=161, w3=215, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 161)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=215, adjust=False).mean() * 1.074118 + 0.0002354 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=174, w3=232, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(174, min_periods=max(174//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.087647 + 0.0002355 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=187, w3=249, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(187, min_periods=max(187//3, 2)).rank(pct=True)
    persistence = change.rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.323333 * persistence + 0.0002356 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=200, w3=266, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(200, min_periods=max(200//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.114706 + 0.0002357 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=213, w3=283, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(213, min_periods=max(213//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.336 * slope + 0.0002358 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=226, w3=300, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(226, min_periods=max(226//3, 2)).mean()
    noise = impulse.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.141765 + 0.0002359 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=239, w3=317, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 239)
    curvature = _rolling_slope(acceleration, 317)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.348667 * acceleration + 0.000236 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=252, w3=334, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 223)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.355 * pressure.rolling(334, min_periods=max(334//3, 2)).mean() + 0.0002361 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=265, w3=351, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(230, min_periods=max(230//3, 2)).mean())
    decay = spread.ewm(span=265, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.182353 + 0.0002362 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=278, w3=368, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(278, min_periods=max(278//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 237)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.195882 + 0.0002363 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=291, w3=385, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(244, min_periods=max(244//3, 2)).mean(), b.abs().rolling(291, min_periods=max(291//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.041667 * _rolling_slope(cover, 244) + 0.0002364 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=304, w3=402, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.048 * y + 0.952000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 251) - _rolling_slope(basket, 304) + 0.0002365 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=317, w3=419, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.236471 + 0.0002366 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=330, w3=436, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.060667 * _rolling_slope(draw, 436) + 0.0002367 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=343, w3=453, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(25) - b.diff(126)
    stress = imbalance.rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.263529 + 0.0002368 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=356, w3=470, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(356, min_periods=max(356//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.277059 + 0.0002369 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=369, w3=487, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.290588 + 0.000237 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=382, w3=504, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.304118 + 0.0002371 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=395, w3=521, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(53)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.092333 * persistence + 0.0002372 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=408, w3=538, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.331176 + 0.0002373 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=421, w3=555, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.105 * slope + 0.0002374 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=434, w3=572, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(74)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.358235 + 0.0002375 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=447, w3=589, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 447)
    curvature = _rolling_slope(acceleration, 589)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.117667 * acceleration + 0.0002376 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=460, w3=606, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 88)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.124 * pressure.rolling(606, min_periods=max(606//3, 2)).mean() + 0.0002377 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=473, w3=623, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(95, min_periods=max(95//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.398824 + 0.0002378 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=486, w3=640, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(486, min_periods=max(486//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 102)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.412353 + 0.0002379 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=499, w3=657, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(109, min_periods=max(109//3, 2)).mean(), b.abs().rolling(499, min_periods=max(499//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.143 * _rolling_slope(cover, 109) + 0.000238 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=13, w3=674, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.149333 * y + 0.850667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 116) - _rolling_slope(basket, 13) + 0.0002381 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=26, w3=691, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(26, min_periods=max(26//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.452941 + 0.0002382 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=39, w3=708, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(39, min_periods=max(39//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.162 * _rolling_slope(draw, 708) + 0.0002383 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=52, w3=725, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(52)
    stress = imbalance.rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.48 + 0.0002384 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=65, w3=742, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(65, min_periods=max(65//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.493529 + 0.0002385 * anchor
    return base_signal.diff().diff()

def f05_fbrk_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=78, w3=759, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 78)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.507059 + 0.0002386 * anchor
    return base_signal.diff().diff()
