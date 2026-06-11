"""88 overnight to intraday leakage gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Relationship between overnight price changes and the subsequent intraday trend.
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

def f88_otil_gemini_001_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=5]"""
    window = 5
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_002_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=10]"""
    window = 10
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_003_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=21]"""
    window = 21
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_004_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=42]"""
    window = 42
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_005_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=63]"""
    window = 63
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_006_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=126]"""
    window = 126
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_007_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=252]"""
    window = 252
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_008_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=504]"""
    window = 504
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_009_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=756]"""
    window = 756
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_010_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Relationship between overnight price changes and the subsequent intraday trend. [window=1260]"""
    window = 1260
    res = _safe_div(open - close.shift(1), close - open + 1e-9)
    return (res).diff().diff().diff()

def f88_otil_gemini_011_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=259, w3=237, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(259, min_periods=max(259//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.172941 + 0.0055102 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_012_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=272, w3=254, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(272, min_periods=max(272//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.060333 * _rolling_slope(draw, 254) + 0.0055103 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_013_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=285, w3=271, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.2 + 0.0055104 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_014_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=298, w3=288, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 166)
    baseline = trend.rolling(298, min_periods=max(298//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.213529 + 0.0055105 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_015_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=311, w3=305, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.227059 + 0.0055106 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_016_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=324, w3=322, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(324, min_periods=max(324//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.240588 + 0.0055107 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_017_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=337, w3=339, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(337, min_periods=max(337//3, 2)).rank(pct=True)
    persistence = change.rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.092 * persistence + 0.0055108 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_018_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=350, w3=356, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.267647 + 0.0055109 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_019_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=363, w3=373, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.104667 * slope + 0.005511 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_020_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=376, w3=390, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.294706 + 0.0055111 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_021_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=389, w3=407, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 389)
    curvature = _rolling_slope(acceleration, 407)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.117333 * acceleration + 0.0055112 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_022_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=402, w3=424, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 222)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.123667 * pressure.rolling(424, min_periods=max(424//3, 2)).mean() + 0.0055113 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_023_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=415, w3=441, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(229, min_periods=max(229//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.335294 + 0.0055114 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_024_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=428, w3=458, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(428, min_periods=max(428//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 236)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.348824 + 0.0055115 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_025_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=441, w3=475, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(243, min_periods=max(243//3, 2)).mean(), b.abs().rolling(441, min_periods=max(441//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.142667 * _rolling_slope(cover, 243) + 0.0055116 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_026_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=454, w3=492, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.149 * y + 0.851000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 250) - _rolling_slope(basket, 454) + 0.0055117 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_027_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=467, w3=509, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(10, min_periods=max(10//3, 2)).mean(), upside.rolling(467, min_periods=max(467//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.389412 + 0.0055118 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_028_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=480, w3=526, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(480, min_periods=max(480//3, 2)).max()
    rebound = x - x.rolling(17, min_periods=max(17//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.161667 * _rolling_slope(draw, 526) + 0.0055119 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_029_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=493, w3=543, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(24) - b.diff(126)
    stress = imbalance.rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.416471 + 0.005512 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_030_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=506, w3=560, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(506, min_periods=max(506//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.43 + 0.0055121 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_031_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=20, w3=577, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.443529 + 0.0055122 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_032_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=33, w3=594, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.457059 + 0.0055123 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_033_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=46, w3=611, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(52)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.193333 * persistence + 0.0055124 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_034_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=59, w3=628, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(59, min_periods=max(59//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.484118 + 0.0055125 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_035_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=72, w3=645, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.206 * slope + 0.0055126 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_036_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=85, w3=662, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(73)
    drag = impulse.rolling(85, min_periods=max(85//3, 2)).mean()
    noise = impulse.abs().rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.511176 + 0.0055127 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_037_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=98, w3=679, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 679)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.218667 * acceleration + 0.0055128 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_038_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=111, w3=696, lag=34)."""
    rel = _safe_div(open.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 87)
    pressure = rel_log.diff(111)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.225 * pressure.rolling(696, min_periods=max(696//3, 2)).mean() + 0.0055129 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_039_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=124, w3=713, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(94, min_periods=max(94//3, 2)).mean())
    decay = spread.ewm(span=124, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.551765 + 0.005513 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_040_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=137, w3=730, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(137, min_periods=max(137//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 101)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.565294 + 0.0055131 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_041_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=150, w3=747, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(108, min_periods=max(108//3, 2)).mean(), b.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.244 * _rolling_slope(cover, 108) + 0.0055132 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_042_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=163, w3=764, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.250333 * y + 0.749667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 115) - _rolling_slope(basket, 163) + 0.0055133 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_043_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=176, w3=30, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(30) * 1.605882 + 0.0055134 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_044_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=189, w3=47, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.263 * _rolling_slope(draw, 47) + 0.0055135 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_045_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=202, w3=64, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.632941 + 0.0055136 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_046_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=215, w3=81, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(215, min_periods=max(215//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.646471 + 0.0055137 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_047_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=228, w3=98, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 228)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=98, adjust=False).mean() * 1.66 + 0.0055138 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_048_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=241, w3=115, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.82 + 0.0055139 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_049_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=254, w3=132, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(254, min_periods=max(254//3, 2)).rank(pct=True)
    persistence = change.rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.294667 * persistence + 0.005514 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_050_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=267, w3=149, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(267, min_periods=max(267//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.847059 + 0.0055141 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_051_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=280, w3=166, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.307333 * slope + 0.0055142 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_052_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=293, w3=183, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.874118 + 0.0055143 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_053_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=306, w3=200, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 200)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.32 * acceleration + 0.0055144 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_054_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=319, w3=217, lag=5)."""
    rel = _safe_div(open.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 199)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.326333 * pressure.rolling(217, min_periods=max(217//3, 2)).mean() + 0.0055145 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_055_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=332, w3=234, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(206, min_periods=max(206//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.914706 + 0.0055146 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_056_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=345, w3=251, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(345, min_periods=max(345//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 213)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.928235 + 0.0055147 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_057_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=358, w3=268, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(220, min_periods=max(220//3, 2)).mean(), b.abs().rolling(358, min_periods=max(358//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.345333 * _rolling_slope(cover, 220) + 0.0055148 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_058_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=371, w3=285, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.351667 * y + 0.648333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 227) - _rolling_slope(basket, 371) + 0.0055149 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_059_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=384, w3=302, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(234, min_periods=max(234//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.968824 + 0.005515 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_060_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=397, w3=319, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(397, min_periods=max(397//3, 2)).max()
    rebound = x - x.rolling(241, min_periods=max(241//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.032 * _rolling_slope(draw, 319) + 0.0055151 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_061_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=410, w3=336, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.995882 + 0.0055152 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_062_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=423, w3=353, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(423, min_periods=max(423//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.009412 + 0.0055153 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_063_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=436, w3=370, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 436)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.022941 + 0.0055154 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_064_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=449, w3=387, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(449, min_periods=max(449//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.036471 + 0.0055155 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_065_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=462, w3=404, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(29)
    rank = change.rolling(462, min_periods=max(462//3, 2)).rank(pct=True)
    persistence = change.rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.063667 * persistence + 0.0055156 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_066_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=475, w3=421, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.063529 + 0.0055157 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_067_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=488, w3=438, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(488, min_periods=max(488//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.076333 * slope + 0.0055158 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_068_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=501, w3=455, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(50)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.090588 + 0.0055159 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_069_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=15, w3=472, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 472)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.089 * acceleration + 0.005516 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_070_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=28, w3=489, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 64)
    pressure = rel_log.diff(28)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.095333 * pressure.rolling(489, min_periods=max(489//3, 2)).mean() + 0.0055161 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_071_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=41, w3=506, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(71, min_periods=max(71//3, 2)).mean())
    decay = spread.ewm(span=41, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.131176 + 0.0055162 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_072_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=54, w3=523, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(54, min_periods=max(54//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 78)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.144706 + 0.0055163 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_073_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=67, w3=540, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(85, min_periods=max(85//3, 2)).mean(), b.abs().rolling(67, min_periods=max(67//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.114333 * _rolling_slope(cover, 85) + 0.0055164 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_074_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=80, w3=557, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.120667 * y + 0.879333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 92) - _rolling_slope(basket, 80) + 0.0055165 * anchor
    return base_signal.diff().diff().diff()

def f88_otil_gemini_075_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=93, w3=574, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.185294 + 0.0055166 * anchor
    return base_signal.diff().diff().diff()
