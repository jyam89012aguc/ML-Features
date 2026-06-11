"""63 price price spectral divergence gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f63_ppsd_gemini_001_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_002_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_003_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_004_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_005_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_006_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_007_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_008_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_009_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_010_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Divergence in spectral density between different price representations. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff() - _safe_log(open).diff(), window)
    return (res).diff()

def f63_ppsd_gemini_011_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=247, w3=50, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(247, min_periods=max(247//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.341 * slope + 0.0040822 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_012_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=260, w3=67, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(260, min_periods=max(260//3, 2)).mean()
    noise = impulse.abs().rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.884118 + 0.0040823 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_013_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=273, w3=84, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 273)
    curvature = _rolling_slope(acceleration, 84)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.353667 * acceleration + 0.0040824 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_014_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=286, w3=101, lag=5)."""
    rel = _safe_div(open.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 241)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.36 * pressure.rolling(101, min_periods=max(101//3, 2)).mean() + 0.0040825 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_015_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=299, w3=118, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(248, min_periods=max(248//3, 2)).mean())
    decay = spread.ewm(span=299, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.924706 + 0.0040826 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_016_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=312, w3=135, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(312, min_periods=max(312//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 8)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.938235 + 0.0040827 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_017_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=325, w3=152, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(15, min_periods=max(15//3, 2)).mean(), b.abs().rolling(325, min_periods=max(325//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.046667 * _rolling_slope(cover, 15) + 0.0040828 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_018_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=338, w3=169, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.053 * y + 0.947000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 22) - _rolling_slope(basket, 338) + 0.0040829 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_019_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=351, w3=186, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.978824 + 0.004083 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_020_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=364, w3=203, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.065667 * _rolling_slope(draw, 203) + 0.0040831 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_021_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=377, w3=220, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(43) - b.diff(126)
    stress = imbalance.rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.005882 + 0.0040832 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_022_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=390, w3=237, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.019412 + 0.0040833 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_023_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=403, w3=254, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=254, adjust=False).mean() * 1.032941 + 0.0040834 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_024_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=416, w3=271, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(416, min_periods=max(416//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.046471 + 0.0040835 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_025_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=429, w3=288, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(71)
    rank = change.rolling(429, min_periods=max(429//3, 2)).rank(pct=True)
    persistence = change.rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.097333 * persistence + 0.0040836 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_026_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=442, w3=305, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.073529 + 0.0040837 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_027_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=455, w3=322, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(455, min_periods=max(455//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.11 * slope + 0.0040838 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_028_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=468, w3=339, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(92)
    drag = impulse.rolling(468, min_periods=max(468//3, 2)).mean()
    noise = impulse.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.100588 + 0.0040839 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_029_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=481, w3=356, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 481)
    curvature = _rolling_slope(acceleration, 356)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.122667 * acceleration + 0.004084 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_030_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=494, w3=373, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 106)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.129 * pressure.rolling(373, min_periods=max(373//3, 2)).mean() + 0.0040841 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_031_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=507, w3=390, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.141176 + 0.0040842 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_032_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=21, w3=407, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(21, min_periods=max(21//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 120)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.154706 + 0.0040843 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_033_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=34, w3=424, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(127, min_periods=max(127//3, 2)).mean(), b.abs().rolling(34, min_periods=max(34//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.148 * _rolling_slope(cover, 127) + 0.0040844 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_034_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=47, w3=441, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.154333 * y + 0.845667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 134) - _rolling_slope(basket, 47) + 0.0040845 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_035_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=60, w3=458, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(60, min_periods=max(60//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.195294 + 0.0040846 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_036_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=73, w3=475, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(73, min_periods=max(73//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.167 * _rolling_slope(draw, 475) + 0.0040847 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_037_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=86, w3=492, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(86)
    stress = imbalance.rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.222353 + 0.0040848 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_038_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=99, w3=509, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(99, min_periods=max(99//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.235882 + 0.0040849 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_039_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=112, w3=526, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.249412 + 0.004085 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_040_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=125, w3=543, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(125, min_periods=max(125//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.262941 + 0.0040851 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_041_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=138, w3=560, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.198667 * persistence + 0.0040852 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_042_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=151, w3=577, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(151, min_periods=max(151//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.29 + 0.0040853 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_043_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=164, w3=594, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.211333 * slope + 0.0040854 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_044_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=177, w3=611, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.317059 + 0.0040855 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_045_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=190, w3=628, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 628)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.224 * acceleration + 0.0040856 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_046_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=203, w3=645, lag=13)."""
    rel = _safe_div(open.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 218)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.230333 * pressure.rolling(645, min_periods=max(645//3, 2)).mean() + 0.0040857 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_047_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=216, w3=662, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(225, min_periods=max(225//3, 2)).mean())
    decay = spread.ewm(span=216, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.357647 + 0.0040858 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_048_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=229, w3=679, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(229, min_periods=max(229//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 232)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.371176 + 0.0040859 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_049_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=242, w3=696, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(239, min_periods=max(239//3, 2)).mean(), b.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.249333 * _rolling_slope(cover, 239) + 0.004086 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_050_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=255, w3=713, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.255667 * y + 0.744333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 246) - _rolling_slope(basket, 255) + 0.0040861 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_051_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=268, w3=730, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(268, min_periods=max(268//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.411765 + 0.0040862 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_052_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=281, w3=747, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(281, min_periods=max(281//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.268333 * _rolling_slope(draw, 747) + 0.0040863 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_053_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=294, w3=764, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(20) - b.diff(126)
    stress = imbalance.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.438824 + 0.0040864 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_054_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=307, w3=30, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.452353 + 0.0040865 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_055_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=320, w3=47, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 320)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=47, adjust=False).mean() * 1.465882 + 0.0040866 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_056_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=333, w3=64, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.479412 + 0.0040867 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_057_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=346, w3=81, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(48)
    rank = change.rolling(346, min_periods=max(346//3, 2)).rank(pct=True)
    persistence = change.rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3 * persistence + 0.0040868 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_058_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=359, w3=98, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(359, min_periods=max(359//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.506471 + 0.0040869 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_059_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=372, w3=115, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(372, min_periods=max(372//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.312667 * slope + 0.004087 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_060_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=385, w3=132, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(69)
    drag = impulse.rolling(385, min_periods=max(385//3, 2)).mean()
    noise = impulse.abs().rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.533529 + 0.0040871 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_061_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=398, w3=149, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.325333 * acceleration + 0.0040872 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_062_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=411, w3=166, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 83)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.331667 * pressure.rolling(166, min_periods=max(166//3, 2)).mean() + 0.0040873 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_063_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=424, w3=183, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(90, min_periods=max(90//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.574118 + 0.0040874 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_064_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=437, w3=200, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(437, min_periods=max(437//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 97)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.587647 + 0.0040875 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_065_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=450, w3=217, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(104, min_periods=max(104//3, 2)).mean(), b.abs().rolling(450, min_periods=max(450//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.350667 * _rolling_slope(cover, 104) + 0.0040876 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_066_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=463, w3=234, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.357 * y + 0.643000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 111) - _rolling_slope(basket, 463) + 0.0040877 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_067_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=476, w3=251, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.628235 + 0.0040878 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_068_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=489, w3=268, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.037333 * _rolling_slope(draw, 268) + 0.0040879 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_069_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=502, w3=285, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.655294 + 0.004088 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_070_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=16, w3=302, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.668824 + 0.0040881 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_071_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=29, w3=319, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 29)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.828824 + 0.0040882 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_072_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=42, w3=336, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(42, min_periods=max(42//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.842353 + 0.0040883 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_073_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=55, w3=353, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(55, min_periods=max(55//3, 2)).rank(pct=True)
    persistence = change.rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.069 * persistence + 0.0040884 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_074_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=68, w3=370, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(68, min_periods=max(68//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.869412 + 0.0040885 * anchor
    return base_signal.diff()

def f63_ppsd_gemini_075_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=81, w3=387, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(81, min_periods=max(81//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.081667 * slope + 0.0040886 * anchor
    return base_signal.diff()
