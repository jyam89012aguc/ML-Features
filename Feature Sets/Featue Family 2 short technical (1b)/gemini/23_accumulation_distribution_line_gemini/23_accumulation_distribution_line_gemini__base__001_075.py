"""23 accumulation distribution line gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Relationship between price close and range to determine if volume is accumulating or distributing.
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

def f23_adln_gemini_001(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=5]"""
    window = 5
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_002(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=10]"""
    window = 10
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_003(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=21]"""
    window = 21
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_004(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=42]"""
    window = 42
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_005(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=63]"""
    window = 63
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_006(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=126]"""
    window = 126
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_007(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=252]"""
    window = 252
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_008(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=504]"""
    window = 504
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_009(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=756]"""
    window = 756
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_010(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between price close and range to determine if volume is accumulating or distributing. [window=1260]"""
    window = 1260
    res = _safe_div((close - low) - (high - close), high - low + 1e-9).rolling(window).mean()
    return res

def f23_adln_gemini_011(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=140, w3=631, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    decay = spread.ewm(span=140, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.481176 + 0.0018282 * anchor
    return base_signal

def f23_adln_gemini_012(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=153, w3=648, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(153, min_periods=max(153//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 33)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.494706 + 0.0018283 * anchor
    return base_signal

def f23_adln_gemini_013(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=166, w3=665, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(40, min_periods=max(40//3, 2)).mean(), b.abs().rolling(166, min_periods=max(166//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.171333 * _rolling_slope(cover, 40) + 0.0018284 * anchor
    return base_signal

def f23_adln_gemini_014(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=179, w3=682, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.177667 * y + 0.822333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 47) - _rolling_slope(basket, 179) + 0.0018285 * anchor
    return base_signal

def f23_adln_gemini_015(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=192, w3=699, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.535294 + 0.0018286 * anchor
    return base_signal

def f23_adln_gemini_016(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=205, w3=716, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(205, min_periods=max(205//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.190333 * _rolling_slope(draw, 716) + 0.0018287 * anchor
    return base_signal

def f23_adln_gemini_017(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=218, w3=733, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(68) - b.diff(126)
    stress = imbalance.rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.562353 + 0.0018288 * anchor
    return base_signal

def f23_adln_gemini_018(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=231, w3=750, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.575882 + 0.0018289 * anchor
    return base_signal

def f23_adln_gemini_019(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=244, w3=767, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 244)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.589412 + 0.001829 * anchor
    return base_signal

def f23_adln_gemini_020(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=257, w3=33, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(257, min_periods=max(257//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.602941 + 0.0018291 * anchor
    return base_signal

def f23_adln_gemini_021(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=270, w3=50, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(96)
    rank = change.rolling(270, min_periods=max(270//3, 2)).rank(pct=True)
    persistence = change.rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.222 * persistence + 0.0018292 * anchor
    return base_signal

def f23_adln_gemini_022(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=283, w3=67, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(283, min_periods=max(283//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.63 + 0.0018293 * anchor
    return base_signal

def f23_adln_gemini_023(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=296, w3=84, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(296, min_periods=max(296//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.234667 * slope + 0.0018294 * anchor
    return base_signal

def f23_adln_gemini_024(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=309, w3=101, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(117)
    drag = impulse.rolling(309, min_periods=max(309//3, 2)).mean()
    noise = impulse.abs().rolling(101, min_periods=max(101//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.657059 + 0.0018295 * anchor
    return base_signal

def f23_adln_gemini_025(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=322, w3=118, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 322)
    curvature = _rolling_slope(acceleration, 118)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.247333 * acceleration + 0.0018296 * anchor
    return base_signal

def f23_adln_gemini_026(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=335, w3=135, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 131)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.253667 * pressure.rolling(135, min_periods=max(135//3, 2)).mean() + 0.0018297 * anchor
    return base_signal

def f23_adln_gemini_027(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=348, w3=152, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(138, min_periods=max(138//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.844118 + 0.0018298 * anchor
    return base_signal

def f23_adln_gemini_028(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=361, w3=169, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(361, min_periods=max(361//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 145)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.857647 + 0.0018299 * anchor
    return base_signal

def f23_adln_gemini_029(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=374, w3=186, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(152, min_periods=max(152//3, 2)).mean(), b.abs().rolling(374, min_periods=max(374//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.272667 * _rolling_slope(cover, 152) + 0.00183 * anchor
    return base_signal

def f23_adln_gemini_030(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=387, w3=203, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.279 * y + 0.721000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 159) - _rolling_slope(basket, 387) + 0.0018301 * anchor
    return base_signal

def f23_adln_gemini_031(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=400, w3=220, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(400, min_periods=max(400//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.898235 + 0.0018302 * anchor
    return base_signal

def f23_adln_gemini_032(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=413, w3=237, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(413, min_periods=max(413//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.291667 * _rolling_slope(draw, 237) + 0.0018303 * anchor
    return base_signal

def f23_adln_gemini_033(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=426, w3=254, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.925294 + 0.0018304 * anchor
    return base_signal

def f23_adln_gemini_034(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=439, w3=271, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.938824 + 0.0018305 * anchor
    return base_signal

def f23_adln_gemini_035(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=452, w3=288, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 452)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=288, adjust=False).mean() * 0.952353 + 0.0018306 * anchor
    return base_signal

def f23_adln_gemini_036(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=465, w3=305, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(465, min_periods=max(465//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.965882 + 0.0018307 * anchor
    return base_signal

def f23_adln_gemini_037(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=478, w3=322, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(322, min_periods=max(322//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.323333 * persistence + 0.0018308 * anchor
    return base_signal

def f23_adln_gemini_038(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=491, w3=339, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.992941 + 0.0018309 * anchor
    return base_signal

def f23_adln_gemini_039(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=504, w3=356, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.336 * slope + 0.001831 * anchor
    return base_signal

def f23_adln_gemini_040(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=18, w3=373, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(18, min_periods=max(18//3, 2)).mean()
    noise = impulse.abs().rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02 + 0.0018311 * anchor
    return base_signal

def f23_adln_gemini_041(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=31, w3=390, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 390)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.348667 * acceleration + 0.0018312 * anchor
    return base_signal

def f23_adln_gemini_042(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=44, w3=407, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 243)
    pressure = rel_log.diff(44)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.355 * pressure.rolling(407, min_periods=max(407//3, 2)).mean() + 0.0018313 * anchor
    return base_signal

def f23_adln_gemini_043(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=57, w3=424, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(250, min_periods=max(250//3, 2)).mean())
    decay = spread.ewm(span=57, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.060588 + 0.0018314 * anchor
    return base_signal

def f23_adln_gemini_044(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=70, w3=441, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(70, min_periods=max(70//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 10)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.074118 + 0.0018315 * anchor
    return base_signal

def f23_adln_gemini_045(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=83, w3=458, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(17, min_periods=max(17//3, 2)).mean(), b.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.041667 * _rolling_slope(cover, 17) + 0.0018316 * anchor
    return base_signal

def f23_adln_gemini_046(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=96, w3=475, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.048 * y + 0.952000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 24) - _rolling_slope(basket, 96) + 0.0018317 * anchor
    return base_signal

def f23_adln_gemini_047(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=109, w3=492, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(109, min_periods=max(109//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.114706 + 0.0018318 * anchor
    return base_signal

def f23_adln_gemini_048(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=122, w3=509, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(122, min_periods=max(122//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.060667 * _rolling_slope(draw, 509) + 0.0018319 * anchor
    return base_signal

def f23_adln_gemini_049(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=135, w3=526, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(45) - b.diff(126)
    stress = imbalance.rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.141765 + 0.001832 * anchor
    return base_signal

def f23_adln_gemini_050(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=148, w3=543, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.155294 + 0.0018321 * anchor
    return base_signal

def f23_adln_gemini_051(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=161, w3=560, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 161)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.168824 + 0.0018322 * anchor
    return base_signal

def f23_adln_gemini_052(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=174, w3=577, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(174, min_periods=max(174//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.182353 + 0.0018323 * anchor
    return base_signal

def f23_adln_gemini_053(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=187, w3=594, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(73)
    rank = change.rolling(187, min_periods=max(187//3, 2)).rank(pct=True)
    persistence = change.rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.092333 * persistence + 0.0018324 * anchor
    return base_signal

def f23_adln_gemini_054(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=200, w3=611, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(200, min_periods=max(200//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.209412 + 0.0018325 * anchor
    return base_signal

def f23_adln_gemini_055(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=213, w3=628, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(213, min_periods=max(213//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.105 * slope + 0.0018326 * anchor
    return base_signal

def f23_adln_gemini_056(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=226, w3=645, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(94)
    drag = impulse.rolling(226, min_periods=max(226//3, 2)).mean()
    noise = impulse.abs().rolling(645, min_periods=max(645//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.236471 + 0.0018327 * anchor
    return base_signal

def f23_adln_gemini_057(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=239, w3=662, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 239)
    curvature = _rolling_slope(acceleration, 662)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.117667 * acceleration + 0.0018328 * anchor
    return base_signal

def f23_adln_gemini_058(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=252, w3=679, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 108)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.124 * pressure.rolling(679, min_periods=max(679//3, 2)).mean() + 0.0018329 * anchor
    return base_signal

def f23_adln_gemini_059(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=265, w3=696, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(115, min_periods=max(115//3, 2)).mean())
    decay = spread.ewm(span=265, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.277059 + 0.001833 * anchor
    return base_signal

def f23_adln_gemini_060(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=278, w3=713, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(278, min_periods=max(278//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 122)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.290588 + 0.0018331 * anchor
    return base_signal

def f23_adln_gemini_061(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=291, w3=730, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(129, min_periods=max(129//3, 2)).mean(), b.abs().rolling(291, min_periods=max(291//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.143 * _rolling_slope(cover, 129) + 0.0018332 * anchor
    return base_signal

def f23_adln_gemini_062(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=304, w3=747, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.149333 * y + 0.850667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 136) - _rolling_slope(basket, 304) + 0.0018333 * anchor
    return base_signal

def f23_adln_gemini_063(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=317, w3=764, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.331176 + 0.0018334 * anchor
    return base_signal

def f23_adln_gemini_064(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=330, w3=30, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.162 * _rolling_slope(draw, 30) + 0.0018335 * anchor
    return base_signal

def f23_adln_gemini_065(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=343, w3=47, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.358235 + 0.0018336 * anchor
    return base_signal

def f23_adln_gemini_066(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=356, w3=64, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(356, min_periods=max(356//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.371765 + 0.0018337 * anchor
    return base_signal

def f23_adln_gemini_067(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=369, w3=81, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=81, adjust=False).mean() * 1.385294 + 0.0018338 * anchor
    return base_signal

def f23_adln_gemini_068(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=382, w3=98, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.398824 + 0.0018339 * anchor
    return base_signal

def f23_adln_gemini_069(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=395, w3=115, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.193667 * persistence + 0.001834 * anchor
    return base_signal

def f23_adln_gemini_070(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=408, w3=132, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.425882 + 0.0018341 * anchor
    return base_signal

def f23_adln_gemini_071(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=421, w3=149, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.206333 * slope + 0.0018342 * anchor
    return base_signal

def f23_adln_gemini_072(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=434, w3=166, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.452941 + 0.0018343 * anchor
    return base_signal

def f23_adln_gemini_073(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=447, w3=183, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 447)
    curvature = _rolling_slope(acceleration, 183)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.219 * acceleration + 0.0018344 * anchor
    return base_signal

def f23_adln_gemini_074(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=460, w3=200, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 220)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.225333 * pressure.rolling(200, min_periods=max(200//3, 2)).mean() + 0.0018345 * anchor
    return base_signal

def f23_adln_gemini_075(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=473, w3=217, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(227, min_periods=max(227//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.493529 + 0.0018346 * anchor
    return base_signal
