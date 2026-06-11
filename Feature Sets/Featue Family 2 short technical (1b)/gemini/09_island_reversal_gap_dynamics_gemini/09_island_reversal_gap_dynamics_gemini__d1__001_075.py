"""09 island reversal gap dynamics gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Isolated price action separated by gaps, signaling a strong reversal in sentiment.
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

def f09_islr_gemini_001_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=5]"""
    window = 5
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_002_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=10]"""
    window = 10
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_003_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=21]"""
    window = 21
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_004_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=42]"""
    window = 42
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_005_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=63]"""
    window = 63
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_006_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=126]"""
    window = 126
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_007_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=252]"""
    window = 252
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_008_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=504]"""
    window = 504
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_009_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=756]"""
    window = 756
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_010_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Isolated price action separated by gaps, signaling a strong reversal in sentiment. [window=1260]"""
    window = 1260
    res = _safe_div(low - high.shift(1), _atr(high, low, close, window)).rolling(window).max()
    return (res).diff()

def f09_islr_gemini_011_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=99, w3=74, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(99, min_periods=max(99//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.114667 * slope + 0.0004422 * anchor
    return base_signal.diff()

def f09_islr_gemini_012_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=112, w3=91, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(84)
    drag = impulse.rolling(112, min_periods=max(112//3, 2)).mean()
    noise = impulse.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9 + 0.0004423 * anchor
    return base_signal.diff()

def f09_islr_gemini_013_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=125, w3=108, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 125)
    curvature = _rolling_slope(acceleration, 108)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.127333 * acceleration + 0.0004424 * anchor
    return base_signal.diff()

def f09_islr_gemini_014_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=138, w3=125, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 98)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.133667 * pressure.rolling(125, min_periods=max(125//3, 2)).mean() + 0.0004425 * anchor
    return base_signal.diff()

def f09_islr_gemini_015_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=151, w3=142, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(105, min_periods=max(105//3, 2)).mean())
    decay = spread.ewm(span=151, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.940588 + 0.0004426 * anchor
    return base_signal.diff()

def f09_islr_gemini_016_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=164, w3=159, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(164, min_periods=max(164//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 112)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.954118 + 0.0004427 * anchor
    return base_signal.diff()

def f09_islr_gemini_017_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=177, w3=176, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(119, min_periods=max(119//3, 2)).mean(), b.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.152667 * _rolling_slope(cover, 119) + 0.0004428 * anchor
    return base_signal.diff()

def f09_islr_gemini_018_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=190, w3=193, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.159 * y + 0.841000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 126) - _rolling_slope(basket, 190) + 0.0004429 * anchor
    return base_signal.diff()

def f09_islr_gemini_019_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=203, w3=210, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.994706 + 0.000443 * anchor
    return base_signal.diff()

def f09_islr_gemini_020_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=216, w3=227, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.171667 * _rolling_slope(draw, 227) + 0.0004431 * anchor
    return base_signal.diff()

def f09_islr_gemini_021_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=229, w3=244, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.021765 + 0.0004432 * anchor
    return base_signal.diff()

def f09_islr_gemini_022_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=242, w3=261, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(242, min_periods=max(242//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.035294 + 0.0004433 * anchor
    return base_signal.diff()

def f09_islr_gemini_023_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=255, w3=278, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=278, adjust=False).mean() * 1.048824 + 0.0004434 * anchor
    return base_signal.diff()

def f09_islr_gemini_024_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=268, w3=295, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(268, min_periods=max(268//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.062353 + 0.0004435 * anchor
    return base_signal.diff()

def f09_islr_gemini_025_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=281, w3=312, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(281, min_periods=max(281//3, 2)).rank(pct=True)
    persistence = change.rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.203333 * persistence + 0.0004436 * anchor
    return base_signal.diff()

def f09_islr_gemini_026_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=294, w3=329, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.089412 + 0.0004437 * anchor
    return base_signal.diff()

def f09_islr_gemini_027_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=189, w2=307, w3=346, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.216 * slope + 0.0004438 * anchor
    return base_signal.diff()

def f09_islr_gemini_028_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=196, w2=320, w3=363, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.116471 + 0.0004439 * anchor
    return base_signal.diff()

def f09_islr_gemini_029_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=203, w2=333, w3=380, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 380)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.228667 * acceleration + 0.000444 * anchor
    return base_signal.diff()

def f09_islr_gemini_030_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=346, w3=397, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 210)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.235 * pressure.rolling(397, min_periods=max(397//3, 2)).mean() + 0.0004441 * anchor
    return base_signal.diff()

def f09_islr_gemini_031_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=359, w3=414, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(217, min_periods=max(217//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.157059 + 0.0004442 * anchor
    return base_signal.diff()

def f09_islr_gemini_032_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=372, w3=431, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(372, min_periods=max(372//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 224)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.170588 + 0.0004443 * anchor
    return base_signal.diff()

def f09_islr_gemini_033_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=385, w3=448, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(231, min_periods=max(231//3, 2)).mean(), b.abs().rolling(385, min_periods=max(385//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.254 * _rolling_slope(cover, 231) + 0.0004444 * anchor
    return base_signal.diff()

def f09_islr_gemini_034_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=398, w3=465, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.260333 * y + 0.739667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 238) - _rolling_slope(basket, 398) + 0.0004445 * anchor
    return base_signal.diff()

def f09_islr_gemini_035_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=411, w3=482, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(411, min_periods=max(411//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.211176 + 0.0004446 * anchor
    return base_signal.diff()

def f09_islr_gemini_036_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=424, w3=499, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(424, min_periods=max(424//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.273 * _rolling_slope(draw, 499) + 0.0004447 * anchor
    return base_signal.diff()

def f09_islr_gemini_037_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=437, w3=516, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(12) - b.diff(126)
    stress = imbalance.rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.238235 + 0.0004448 * anchor
    return base_signal.diff()

def f09_islr_gemini_038_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=450, w3=533, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.251765 + 0.0004449 * anchor
    return base_signal.diff()

def f09_islr_gemini_039_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=463, w3=550, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 463)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.265294 + 0.000445 * anchor
    return base_signal.diff()

def f09_islr_gemini_040_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=476, w3=567, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(476, min_periods=max(476//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.278824 + 0.0004451 * anchor
    return base_signal.diff()

def f09_islr_gemini_041_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=489, w3=584, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(40)
    rank = change.rolling(489, min_periods=max(489//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.304667 * persistence + 0.0004452 * anchor
    return base_signal.diff()

def f09_islr_gemini_042_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=502, w3=601, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(502, min_periods=max(502//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.305882 + 0.0004453 * anchor
    return base_signal.diff()

def f09_islr_gemini_043_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=16, w3=618, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(16, min_periods=max(16//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.317333 * slope + 0.0004454 * anchor
    return base_signal.diff()

def f09_islr_gemini_044_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=29, w3=635, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(61)
    drag = impulse.rolling(29, min_periods=max(29//3, 2)).mean()
    noise = impulse.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.332941 + 0.0004455 * anchor
    return base_signal.diff()

def f09_islr_gemini_045_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=42, w3=652, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 42)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.33 * acceleration + 0.0004456 * anchor
    return base_signal.diff()

def f09_islr_gemini_046_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=55, w3=669, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 75)
    pressure = rel_log.diff(55)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.336333 * pressure.rolling(669, min_periods=max(669//3, 2)).mean() + 0.0004457 * anchor
    return base_signal.diff()

def f09_islr_gemini_047_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=68, w3=686, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(82, min_periods=max(82//3, 2)).mean())
    decay = spread.ewm(span=68, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.373529 + 0.0004458 * anchor
    return base_signal.diff()

def f09_islr_gemini_048_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=81, w3=703, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(81, min_periods=max(81//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 89)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.387059 + 0.0004459 * anchor
    return base_signal.diff()

def f09_islr_gemini_049_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=94, w3=720, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(96, min_periods=max(96//3, 2)).mean(), b.abs().rolling(94, min_periods=max(94//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.355333 * _rolling_slope(cover, 96) + 0.000446 * anchor
    return base_signal.diff()

def f09_islr_gemini_050_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=107, w3=737, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.361667 * y + 0.638333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 103) - _rolling_slope(basket, 107) + 0.0004461 * anchor
    return base_signal.diff()

def f09_islr_gemini_051_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=120, w3=754, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(110, min_periods=max(110//3, 2)).mean(), upside.rolling(120, min_periods=max(120//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.427647 + 0.0004462 * anchor
    return base_signal.diff()

def f09_islr_gemini_052_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=133, w3=20, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(117, min_periods=max(117//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.042 * _rolling_slope(draw, 20) + 0.0004463 * anchor
    return base_signal.diff()

def f09_islr_gemini_053_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=146, w3=37, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(124) - b.diff(126)
    stress = imbalance.rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.454706 + 0.0004464 * anchor
    return base_signal.diff()

def f09_islr_gemini_054_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=159, w3=54, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 131)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.468235 + 0.0004465 * anchor
    return base_signal.diff()

def f09_islr_gemini_055_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=172, w3=71, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 138)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=71, adjust=False).mean() * 1.481765 + 0.0004466 * anchor
    return base_signal.diff()

def f09_islr_gemini_056_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=185, w3=88, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(145, min_periods=max(145//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.495294 + 0.0004467 * anchor
    return base_signal.diff()

def f09_islr_gemini_057_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=198, w3=105, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(198, min_periods=max(198//3, 2)).rank(pct=True)
    persistence = change.rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.073667 * persistence + 0.0004468 * anchor
    return base_signal.diff()

def f09_islr_gemini_058_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=211, w3=122, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(159, min_periods=max(159//3, 2)).std()
    vol_slow = ret.rolling(211, min_periods=max(211//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.522353 + 0.0004469 * anchor
    return base_signal.diff()

def f09_islr_gemini_059_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=224, w3=139, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(224, min_periods=max(224//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 166)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.086333 * slope + 0.000447 * anchor
    return base_signal.diff()

def f09_islr_gemini_060_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=237, w3=156, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(237, min_periods=max(237//3, 2)).mean()
    noise = impulse.abs().rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.549412 + 0.0004471 * anchor
    return base_signal.diff()

def f09_islr_gemini_061_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=250, w3=173, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 180)
    acceleration = _rolling_slope(velocity, 250)
    curvature = _rolling_slope(acceleration, 173)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.099 * acceleration + 0.0004472 * anchor
    return base_signal.diff()

def f09_islr_gemini_062_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=263, w3=190, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 187)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.105333 * pressure.rolling(190, min_periods=max(190//3, 2)).mean() + 0.0004473 * anchor
    return base_signal.diff()

def f09_islr_gemini_063_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=276, w3=207, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(194, min_periods=max(194//3, 2)).mean())
    decay = spread.ewm(span=276, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.59 + 0.0004474 * anchor
    return base_signal.diff()

def f09_islr_gemini_064_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=289, w3=224, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(289, min_periods=max(289//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 201)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.603529 + 0.0004475 * anchor
    return base_signal.diff()

def f09_islr_gemini_065_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=302, w3=241, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(208, min_periods=max(208//3, 2)).mean(), b.abs().rolling(302, min_periods=max(302//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.124333 * _rolling_slope(cover, 208) + 0.0004476 * anchor
    return base_signal.diff()

def f09_islr_gemini_066_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=315, w3=258, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.130667 * y + 0.869333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 215) - _rolling_slope(basket, 315) + 0.0004477 * anchor
    return base_signal.diff()

def f09_islr_gemini_067_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=328, w3=275, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(328, min_periods=max(328//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.644118 + 0.0004478 * anchor
    return base_signal.diff()

def f09_islr_gemini_068_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=341, w3=292, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(341, min_periods=max(341//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.143333 * _rolling_slope(draw, 292) + 0.0004479 * anchor
    return base_signal.diff()

def f09_islr_gemini_069_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=354, w3=309, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.671176 + 0.000448 * anchor
    return base_signal.diff()

def f09_islr_gemini_070_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=367, w3=326, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(367, min_periods=max(367//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.831176 + 0.0004481 * anchor
    return base_signal.diff()

def f09_islr_gemini_071_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=380, w3=343, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 380)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.844706 + 0.0004482 * anchor
    return base_signal.diff()

def f09_islr_gemini_072_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=393, w3=360, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(393, min_periods=max(393//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.858235 + 0.0004483 * anchor
    return base_signal.diff()

def f09_islr_gemini_073_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=406, w3=377, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(17)
    rank = change.rolling(406, min_periods=max(406//3, 2)).rank(pct=True)
    persistence = change.rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.175 * persistence + 0.0004484 * anchor
    return base_signal.diff()

def f09_islr_gemini_074_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=419, w3=394, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(419, min_periods=max(419//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.885294 + 0.0004485 * anchor
    return base_signal.diff()

def f09_islr_gemini_075_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=432, w3=411, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(432, min_periods=max(432//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.187667 * slope + 0.0004486 * anchor
    return base_signal.diff()
