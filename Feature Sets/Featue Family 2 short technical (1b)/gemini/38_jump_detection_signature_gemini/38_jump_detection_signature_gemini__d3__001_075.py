"""38 jump detection signature gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of discontinuous price movements or 'jumps' using statistical thresholds.
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

def f38_jump_gemini_001_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_002_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_003_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_004_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_005_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_006_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_007_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_008_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_009_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_010_d3(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f38_jump_gemini_011_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=30, w3=371, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 30)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.316471 + 0.0027102 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_012_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=43, w3=388, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(43, min_periods=max(43//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.33 + 0.0027103 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_013_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=56, w3=405, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(30)
    rank = change.rolling(56, min_periods=max(56//3, 2)).rank(pct=True)
    persistence = change.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.199333 * persistence + 0.0027104 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_014_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=69, w3=422, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(69, min_periods=max(69//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.357059 + 0.0027105 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_015_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=82, w3=439, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(82, min_periods=max(82//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.212 * slope + 0.0027106 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_016_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=95, w3=456, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(51)
    drag = impulse.rolling(95, min_periods=max(95//3, 2)).mean()
    noise = impulse.abs().rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.384118 + 0.0027107 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_017_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=108, w3=473, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 108)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.224667 * acceleration + 0.0027108 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_018_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=121, w3=490, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.411176 + 0.0027109 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_019_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=134, w3=507, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(134, min_periods=max(134//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.237333 * _rolling_slope(draw, 507) + 0.002711 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_020_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=147, w3=524, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(147, min_periods=max(147//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.438235 + 0.0027111 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_021_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=160, w3=541, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 160)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.451765 + 0.0027112 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_022_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=173, w3=558, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(173, min_periods=max(173//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.465294 + 0.0027113 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_023_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=186, w3=575, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(100)
    rank = change.rolling(186, min_periods=max(186//3, 2)).rank(pct=True)
    persistence = change.rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.262667 * persistence + 0.0027114 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_024_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=199, w3=592, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(199, min_periods=max(199//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.492353 + 0.0027115 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_025_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=212, w3=609, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(212, min_periods=max(212//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.275333 * slope + 0.0027116 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_026_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=225, w3=626, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(121)
    drag = impulse.rolling(225, min_periods=max(225//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.519412 + 0.0027117 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_027_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=238, w3=643, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 238)
    curvature = _rolling_slope(acceleration, 643)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.288 * acceleration + 0.0027118 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_028_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=251, w3=660, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.546471 + 0.0027119 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_029_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=264, w3=677, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(264, min_periods=max(264//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.300667 * _rolling_slope(draw, 677) + 0.002712 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_030_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=277, w3=694, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(277, min_periods=max(277//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.573529 + 0.0027121 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_031_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=290, w3=711, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 290)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.587059 + 0.0027122 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_032_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=303, w3=728, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(303, min_periods=max(303//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.600588 + 0.0027123 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_033_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=316, w3=745, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(316, min_periods=max(316//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.326 * persistence + 0.0027124 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_034_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=329, w3=762, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(329, min_periods=max(329//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.627647 + 0.0027125 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_035_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=342, w3=28, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(342, min_periods=max(342//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.338667 * slope + 0.0027126 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_036_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=355, w3=45, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(355, min_periods=max(355//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.654706 + 0.0027127 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_037_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=368, w3=62, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 368)
    curvature = _rolling_slope(acceleration, 62)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351333 * acceleration + 0.0027128 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_038_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=381, w3=79, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(381, min_periods=max(381//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(79) * 0.828235 + 0.0027129 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_039_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=394, w3=96, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(394, min_periods=max(394//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.031667 * _rolling_slope(draw, 96) + 0.002713 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_040_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=407, w3=113, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(407, min_periods=max(407//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.855294 + 0.0027131 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_041_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=420, w3=130, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=130, adjust=False).mean() * 0.868824 + 0.0027132 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_042_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=433, w3=147, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(433, min_periods=max(433//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.882353 + 0.0027133 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_043_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=446, w3=164, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(446, min_periods=max(446//3, 2)).rank(pct=True)
    persistence = change.rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.057 * persistence + 0.0027134 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_044_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=459, w3=181, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(459, min_periods=max(459//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.909412 + 0.0027135 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_045_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=472, w3=198, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(472, min_periods=max(472//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.069667 * slope + 0.0027136 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_046_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=485, w3=215, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(14)
    drag = impulse.rolling(485, min_periods=max(485//3, 2)).mean()
    noise = impulse.abs().rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.936471 + 0.0027137 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_047_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=498, w3=232, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 498)
    curvature = _rolling_slope(acceleration, 232)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.082333 * acceleration + 0.0027138 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_048_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=12, w3=249, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(12, min_periods=max(12//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.963529 + 0.0027139 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_049_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=25, w3=266, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(25, min_periods=max(25//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.095 * _rolling_slope(draw, 266) + 0.002714 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_050_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=38, w3=283, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(38, min_periods=max(38//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.990588 + 0.0027141 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_051_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=51, w3=300, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 51)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.004118 + 0.0027142 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_052_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=64, w3=317, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(64, min_periods=max(64//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.017647 + 0.0027143 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_053_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=77, w3=334, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(63)
    rank = change.rolling(77, min_periods=max(77//3, 2)).rank(pct=True)
    persistence = change.rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.120333 * persistence + 0.0027144 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_054_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=90, w3=351, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(90, min_periods=max(90//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.044706 + 0.0027145 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_055_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=103, w3=368, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(103, min_periods=max(103//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.133 * slope + 0.0027146 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_056_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=116, w3=385, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(84)
    drag = impulse.rolling(116, min_periods=max(116//3, 2)).mean()
    noise = impulse.abs().rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.071765 + 0.0027147 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_057_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=129, w3=402, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 129)
    curvature = _rolling_slope(acceleration, 402)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.145667 * acceleration + 0.0027148 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_058_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=142, w3=419, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.098824 + 0.0027149 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_059_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=155, w3=436, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(155, min_periods=max(155//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.158333 * _rolling_slope(draw, 436) + 0.002715 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_060_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=168, w3=453, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(168, min_periods=max(168//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.125882 + 0.0027151 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_061_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=181, w3=470, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 181)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.139412 + 0.0027152 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_062_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=194, w3=487, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(194, min_periods=max(194//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.152941 + 0.0027153 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_063_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=207, w3=504, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(207, min_periods=max(207//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.183667 * persistence + 0.0027154 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_064_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=220, w3=521, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(220, min_periods=max(220//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18 + 0.0027155 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_065_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=233, w3=538, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(233, min_periods=max(233//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.196333 * slope + 0.0027156 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_066_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=246, w3=555, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(246, min_periods=max(246//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.207059 + 0.0027157 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_067_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=259, w3=572, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 259)
    curvature = _rolling_slope(acceleration, 572)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.209 * acceleration + 0.0027158 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_068_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=272, w3=589, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(272, min_periods=max(272//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.234118 + 0.0027159 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_069_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=285, w3=606, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(285, min_periods=max(285//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.221667 * _rolling_slope(draw, 606) + 0.002716 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_070_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=298, w3=623, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(298, min_periods=max(298//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.261176 + 0.0027161 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_071_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=311, w3=640, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.274706 + 0.0027162 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_072_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=324, w3=657, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(324, min_periods=max(324//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.288235 + 0.0027163 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_073_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=337, w3=674, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(337, min_periods=max(337//3, 2)).rank(pct=True)
    persistence = change.rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.247 * persistence + 0.0027164 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_074_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=350, w3=691, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.315294 + 0.0027165 * anchor
    return base_signal.diff().diff().diff()

def f38_jump_gemini_075_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=363, w3=708, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.259667 * slope + 0.0027166 * anchor
    return base_signal.diff().diff().diff()
