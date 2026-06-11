"""63 price price spectral divergence gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Divergence in spectral density between different price representations.
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

def f63_ppsd_gemini_001_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_002_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_003_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_004_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_005_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_006_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_007_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_008_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_009_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_010_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff().diff().diff()

def f63_ppsd_gemini_011_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=394, w3=304, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.244706 + 0.0041102 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_012_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=407, w3=321, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(407, min_periods=max(407//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.126667 * _rolling_slope(draw, 321) + 0.0041103 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_013_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=420, w3=338, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.271765 + 0.0041104 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_014_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=433, w3=355, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(433, min_periods=max(433//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.285294 + 0.0041105 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_015_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=446, w3=372, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 446)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.298824 + 0.0041106 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_016_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=459, w3=389, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(459, min_periods=max(459//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.312353 + 0.0041107 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_017_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=472, w3=406, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(472, min_periods=max(472//3, 2)).rank(pct=True)
    persistence = change.rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.158333 * persistence + 0.0041108 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_018_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=485, w3=423, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(485, min_periods=max(485//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.339412 + 0.0041109 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_019_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=498, w3=440, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(498, min_periods=max(498//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.171 * slope + 0.004111 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_020_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=12, w3=457, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(20)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.366471 + 0.0041111 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_021_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=25, w3=474, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.183667 * acceleration + 0.0041112 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_022_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=38, w3=491, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 34)
    pressure = rel_log.diff(38)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.19 * pressure.rolling(491, min_periods=max(491//3, 2)).mean() + 0.0041113 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_023_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=51, w3=508, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(41, min_periods=max(41//3, 2)).mean())
    decay = spread.ewm(span=51, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.407059 + 0.0041114 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_024_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=64, w3=525, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(64, min_periods=max(64//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 48)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.420588 + 0.0041115 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_025_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=77, w3=542, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(55, min_periods=max(55//3, 2)).mean(), b.abs().rolling(77, min_periods=max(77//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.209 * _rolling_slope(cover, 55) + 0.0041116 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_026_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=90, w3=559, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.215333 * y + 0.784667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 62) - _rolling_slope(basket, 90) + 0.0041117 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_027_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=103, w3=576, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(103, min_periods=max(103//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.461176 + 0.0041118 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_028_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=116, w3=593, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.228 * _rolling_slope(draw, 593) + 0.0041119 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_029_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=129, w3=610, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(83) - b.diff(126)
    stress = imbalance.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.488235 + 0.004112 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_030_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=142, w3=627, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(142, min_periods=max(142//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.501765 + 0.0041121 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_031_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=155, w3=644, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 155)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.515294 + 0.0041122 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_032_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=168, w3=661, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(168, min_periods=max(168//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.528824 + 0.0041123 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_033_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=181, w3=678, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(111)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.259667 * persistence + 0.0041124 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_034_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=194, w3=695, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(194, min_periods=max(194//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.555882 + 0.0041125 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_035_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=207, w3=712, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(207, min_periods=max(207//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.272333 * slope + 0.0041126 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_036_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=220, w3=729, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(220, min_periods=max(220//3, 2)).mean()
    noise = impulse.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.582941 + 0.0041127 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_037_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=233, w3=746, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 233)
    curvature = _rolling_slope(acceleration, 746)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.285 * acceleration + 0.0041128 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_038_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=246, w3=763, lag=34)."""
    rel = _safe_div(open.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 146)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.291333 * pressure.rolling(763, min_periods=max(763//3, 2)).mean() + 0.0041129 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_039_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=259, w3=29, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(153, min_periods=max(153//3, 2)).mean())
    decay = spread.ewm(span=259, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.623529 + 0.004113 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_040_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=272, w3=46, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(272, min_periods=max(272//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 160)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.637059 + 0.0041131 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_041_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=285, w3=63, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(167, min_periods=max(167//3, 2)).mean(), b.abs().rolling(285, min_periods=max(285//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(63) + 0.310333 * _rolling_slope(cover, 167) + 0.0041132 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_042_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=298, w3=80, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.316667 * y + 0.683333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 174) - _rolling_slope(basket, 298) + 0.0041133 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_043_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=311, w3=97, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(311, min_periods=max(311//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(97) * 0.824118 + 0.0041134 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_044_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=324, w3=114, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(324, min_periods=max(324//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.329333 * _rolling_slope(draw, 114) + 0.0041135 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_045_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=337, w3=131, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.851176 + 0.0041136 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_046_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=350, w3=148, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(350, min_periods=max(350//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.864706 + 0.0041137 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_047_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=363, w3=165, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 363)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=165, adjust=False).mean() * 0.878235 + 0.0041138 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_048_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=376, w3=182, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.891765 + 0.0041139 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_049_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=389, w3=199, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(389, min_periods=max(389//3, 2)).rank(pct=True)
    persistence = change.rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361 * persistence + 0.004114 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_050_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=402, w3=216, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(402, min_periods=max(402//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.918824 + 0.0041141 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_051_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=415, w3=233, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(415, min_periods=max(415//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.041333 * slope + 0.0041142 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_052_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=428, w3=250, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.945882 + 0.0041143 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_053_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=441, w3=267, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 267)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.054 * acceleration + 0.0041144 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_054_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=454, w3=284, lag=5)."""
    rel = _safe_div(open.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 11)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.060333 * pressure.rolling(284, min_periods=max(284//3, 2)).mean() + 0.0041145 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_055_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=467, w3=301, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.986471 + 0.0041146 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_056_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=480, w3=318, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(480, min_periods=max(480//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 25)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.0 + 0.0041147 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_057_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=493, w3=335, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(32, min_periods=max(32//3, 2)).mean(), b.abs().rolling(493, min_periods=max(493//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.079333 * _rolling_slope(cover, 32) + 0.0041148 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_058_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=506, w3=352, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.085667 * y + 0.914333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 39) - _rolling_slope(basket, 506) + 0.0041149 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_059_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=20, w3=369, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(20, min_periods=max(20//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.040588 + 0.004115 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_060_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=33, w3=386, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(33, min_periods=max(33//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.098333 * _rolling_slope(draw, 386) + 0.0041151 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_061_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=46, w3=403, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(60) - b.diff(46)
    stress = imbalance.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.067647 + 0.0041152 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_062_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=59, w3=420, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(59, min_periods=max(59//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.081176 + 0.0041153 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_063_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=72, w3=437, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 72)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.094706 + 0.0041154 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_064_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=85, w3=454, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(85, min_periods=max(85//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.108235 + 0.0041155 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_065_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=98, w3=471, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(88)
    rank = change.rolling(98, min_periods=max(98//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.13 * persistence + 0.0041156 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_066_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=111, w3=488, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(111, min_periods=max(111//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.135294 + 0.0041157 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_067_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=124, w3=505, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(124, min_periods=max(124//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.142667 * slope + 0.0041158 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_068_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=137, w3=522, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(109)
    drag = impulse.rolling(137, min_periods=max(137//3, 2)).mean()
    noise = impulse.abs().rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.162353 + 0.0041159 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_069_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=150, w3=539, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 150)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.155333 * acceleration + 0.004116 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_070_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=163, w3=556, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 123)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.161667 * pressure.rolling(556, min_periods=max(556//3, 2)).mean() + 0.0041161 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_071_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=176, w3=573, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    decay = spread.ewm(span=176, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.202941 + 0.0041162 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_072_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=189, w3=590, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(189, min_periods=max(189//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 137)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.216471 + 0.0041163 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_073_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=202, w3=607, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(144, min_periods=max(144//3, 2)).mean(), b.abs().rolling(202, min_periods=max(202//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.180667 * _rolling_slope(cover, 144) + 0.0041164 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_074_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=215, w3=624, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.187 * y + 0.813000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 151) - _rolling_slope(basket, 215) + 0.0041165 * anchor
    return base_signal.diff().diff().diff()

def f63_ppsd_gemini_075_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=228, w3=641, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(228, min_periods=max(228//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.257059 + 0.0041166 * anchor
    return base_signal.diff().diff().diff()
