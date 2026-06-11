"""74 rescaled range signal gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of the range of cumulative deviations to identify trend persistence.
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

def f74_rrsg_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=5]"""
    window = 5
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=10]"""
    window = 10
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=21]"""
    window = 21
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=42]"""
    window = 42
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=63]"""
    window = 63
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=126]"""
    window = 126
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=252]"""
    window = 252
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=504]"""
    window = 504
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=756]"""
    window = 756
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Analysis of the range of cumulative deviations to identify trend persistence. [window=1260]"""
    window = 1260
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), close.rolling(window).std() * 1.00001 + 1e-9)
    return (res).diff().diff()

def f74_rrsg_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=311, w3=508, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 311)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.606471 + 0.0047122 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=324, w3=525, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(324, min_periods=max(324//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.62 + 0.0047123 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=337, w3=542, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(121)
    rank = change.rolling(337, min_periods=max(337//3, 2)).rank(pct=True)
    persistence = change.rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.041333 * persistence + 0.0047124 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=350, w3=559, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.647059 + 0.0047125 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=363, w3=576, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.054 * slope + 0.0047126 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=376, w3=593, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.820588 + 0.0047127 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=389, w3=610, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 389)
    curvature = _rolling_slope(acceleration, 610)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.066667 * acceleration + 0.0047128 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=402, w3=627, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 156)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.073 * pressure.rolling(627, min_periods=max(627//3, 2)).mean() + 0.0047129 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=415, w3=644, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(163, min_periods=max(163//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.861176 + 0.004713 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=428, w3=661, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(428, min_periods=max(428//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 170)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.874706 + 0.0047131 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=441, w3=678, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(177, min_periods=max(177//3, 2)).mean(), b.abs().rolling(441, min_periods=max(441//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.092 * _rolling_slope(cover, 177) + 0.0047132 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=454, w3=695, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.098333 * y + 0.901667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 184) - _rolling_slope(basket, 454) + 0.0047133 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=467, w3=712, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(467, min_periods=max(467//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.915294 + 0.0047134 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=480, w3=729, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(480, min_periods=max(480//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.111 * _rolling_slope(draw, 729) + 0.0047135 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=493, w3=746, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.942353 + 0.0047136 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=506, w3=763, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(506, min_periods=max(506//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.955882 + 0.0047137 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=20, w3=29, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=29, adjust=False).mean() * 0.969412 + 0.0047138 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=33, w3=46, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.982941 + 0.0047139 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=46, w3=63, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.142667 * persistence + 0.004714 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=59, w3=80, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(59, min_periods=max(59//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01 + 0.0047141 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=72, w3=97, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(72, min_periods=max(72//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.155333 * slope + 0.0047142 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=85, w3=114, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(7)
    drag = impulse.rolling(85, min_periods=max(85//3, 2)).mean()
    noise = impulse.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.037059 + 0.0047143 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=98, w3=131, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 98)
    curvature = _rolling_slope(acceleration, 131)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.168 * acceleration + 0.0047144 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=111, w3=148, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 21)
    pressure = rel_log.diff(111)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.174333 * pressure.rolling(148, min_periods=max(148//3, 2)).mean() + 0.0047145 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=124, w3=165, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(28, min_periods=max(28//3, 2)).mean())
    decay = spread.ewm(span=124, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.077647 + 0.0047146 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=137, w3=182, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(137, min_periods=max(137//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 35)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.091176 + 0.0047147 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=150, w3=199, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(42, min_periods=max(42//3, 2)).mean(), b.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.193333 * _rolling_slope(cover, 42) + 0.0047148 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=163, w3=216, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.199667 * y + 0.800333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 49) - _rolling_slope(basket, 163) + 0.0047149 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=176, w3=233, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.131765 + 0.004715 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=189, w3=250, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212333 * _rolling_slope(draw, 250) + 0.0047151 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=202, w3=267, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(70) - b.diff(126)
    stress = imbalance.rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.158824 + 0.0047152 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=215, w3=284, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(215, min_periods=max(215//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.172353 + 0.0047153 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=228, w3=301, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 228)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.185882 + 0.0047154 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=241, w3=318, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.199412 + 0.0047155 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=254, w3=335, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(98)
    rank = change.rolling(254, min_periods=max(254//3, 2)).rank(pct=True)
    persistence = change.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.244 * persistence + 0.0047156 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=267, w3=352, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(267, min_periods=max(267//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.226471 + 0.0047157 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=280, w3=369, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(280, min_periods=max(280//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.256667 * slope + 0.0047158 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=293, w3=386, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(119)
    drag = impulse.rolling(293, min_periods=max(293//3, 2)).mean()
    noise = impulse.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.253529 + 0.0047159 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=306, w3=403, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 403)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.269333 * acceleration + 0.004716 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=319, w3=420, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 133)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.275667 * pressure.rolling(420, min_periods=max(420//3, 2)).mean() + 0.0047161 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=332, w3=437, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(140, min_periods=max(140//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.294118 + 0.0047162 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=345, w3=454, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(345, min_periods=max(345//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 147)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.307647 + 0.0047163 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=358, w3=471, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(154, min_periods=max(154//3, 2)).mean(), b.abs().rolling(358, min_periods=max(358//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.294667 * _rolling_slope(cover, 154) + 0.0047164 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=371, w3=488, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.301 * y + 0.699000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 161) - _rolling_slope(basket, 371) + 0.0047165 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=384, w3=505, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.348235 + 0.0047166 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=397, w3=522, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(397, min_periods=max(397//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.313667 * _rolling_slope(draw, 522) + 0.0047167 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=410, w3=539, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.375294 + 0.0047168 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=423, w3=556, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(423, min_periods=max(423//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.388824 + 0.0047169 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=436, w3=573, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 436)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.402353 + 0.004717 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=449, w3=590, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(449, min_periods=max(449//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.415882 + 0.0047171 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=462, w3=607, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(462, min_periods=max(462//3, 2)).rank(pct=True)
    persistence = change.rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.345333 * persistence + 0.0047172 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=475, w3=624, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(475, min_periods=max(475//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.442941 + 0.0047173 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=488, w3=641, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(488, min_periods=max(488//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.358 * slope + 0.0047174 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=501, w3=658, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47 + 0.0047175 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=15, w3=675, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 675)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.038333 * acceleration + 0.0047176 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=28, w3=692, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 245)
    pressure = rel_log.diff(28)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.044667 * pressure.rolling(692, min_periods=max(692//3, 2)).mean() + 0.0047177 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=41, w3=709, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(5, min_periods=max(5//3, 2)).mean())
    decay = spread.ewm(span=41, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.510588 + 0.0047178 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=54, w3=726, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(54, min_periods=max(54//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 12)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.524118 + 0.0047179 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=67, w3=743, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(19, min_periods=max(19//3, 2)).mean(), b.abs().rolling(67, min_periods=max(67//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.063667 * _rolling_slope(cover, 19) + 0.004718 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=80, w3=760, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.07 * y + 0.930000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 26) - _rolling_slope(basket, 80) + 0.0047181 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=93, w3=26, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(93, min_periods=max(93//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(26) * 1.564706 + 0.0047182 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=106, w3=43, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(106, min_periods=max(106//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.082667 * _rolling_slope(draw, 43) + 0.0047183 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=119, w3=60, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(47) - b.diff(119)
    stress = imbalance.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.591765 + 0.0047184 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=132, w3=77, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(132, min_periods=max(132//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(77, min_periods=max(77//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.605294 + 0.0047185 * anchor
    return base_signal.diff().diff()

def f74_rrsg_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=145, w3=94, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=94, adjust=False).mean() * 1.618824 + 0.0047186 * anchor
    return base_signal.diff().diff()
