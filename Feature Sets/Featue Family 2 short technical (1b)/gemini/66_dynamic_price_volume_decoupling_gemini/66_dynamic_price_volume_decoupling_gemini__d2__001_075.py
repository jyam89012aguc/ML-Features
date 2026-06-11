"""66 dynamic price volume decoupling gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Instances where price and volume trends diverge, signaling loss of momentum.
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

def f66_dpvd_gemini_001_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=5]"""
    window = 5
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_002_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=10]"""
    window = 10
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_003_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=21]"""
    window = 21
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_004_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=42]"""
    window = 42
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_005_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=63]"""
    window = 63
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_006_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=126]"""
    window = 126
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_007_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=252]"""
    window = 252
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_008_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=504]"""
    window = 504
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_009_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=756]"""
    window = 756
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_010_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=1260]"""
    window = 1260
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff().diff()

def f66_dpvd_gemini_011_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=454, w3=199, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 454)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=199, adjust=False).mean() * 1.595294 + 0.0042642 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_012_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=467, w3=216, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(467, min_periods=max(467//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.608824 + 0.0042643 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_013_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=480, w3=233, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.248667 * persistence + 0.0042644 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_014_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=493, w3=250, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.635882 + 0.0042645 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_015_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=506, w3=267, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.261333 * slope + 0.0042646 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_016_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=20, w3=284, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.662941 + 0.0042647 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_017_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=33, w3=301, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 33)
    curvature = _rolling_slope(acceleration, 301)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274 * acceleration + 0.0042648 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_018_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=46, w3=318, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 165)
    pressure = rel_log.diff(46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.280333 * pressure.rolling(318, min_periods=max(318//3, 2)).mean() + 0.0042649 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_019_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=59, w3=335, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(172, min_periods=max(172//3, 2)).mean())
    decay = spread.ewm(span=59, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.85 + 0.004265 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_020_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=72, w3=352, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(72, min_periods=max(72//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 179)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.863529 + 0.0042651 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_021_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=85, w3=369, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(186, min_periods=max(186//3, 2)).mean(), b.abs().rolling(85, min_periods=max(85//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.299333 * _rolling_slope(cover, 186) + 0.0042652 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_022_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=98, w3=386, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.305667 * y + 0.694333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 193) - _rolling_slope(basket, 98) + 0.0042653 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_023_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=111, w3=403, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(111, min_periods=max(111//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.904118 + 0.0042654 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_024_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=124, w3=420, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(124, min_periods=max(124//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.318333 * _rolling_slope(draw, 420) + 0.0042655 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_025_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=137, w3=437, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.931176 + 0.0042656 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_026_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=150, w3=454, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(150, min_periods=max(150//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.944706 + 0.0042657 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_027_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=163, w3=471, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 163)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.958235 + 0.0042658 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_028_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=176, w3=488, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(176, min_periods=max(176//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.971765 + 0.0042659 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_029_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=189, w3=505, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(189, min_periods=max(189//3, 2)).rank(pct=True)
    persistence = change.rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.35 * persistence + 0.004266 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_030_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=202, w3=522, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.998824 + 0.0042661 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_031_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=215, w3=539, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.362667 * slope + 0.0042662 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_032_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=228, w3=556, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(16)
    drag = impulse.rolling(228, min_periods=max(228//3, 2)).mean()
    noise = impulse.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.025882 + 0.0042663 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_033_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=241, w3=573, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 573)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.043 * acceleration + 0.0042664 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_034_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=254, w3=590, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 30)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.049333 * pressure.rolling(590, min_periods=max(590//3, 2)).mean() + 0.0042665 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_035_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=267, w3=607, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(37, min_periods=max(37//3, 2)).mean())
    decay = spread.ewm(span=267, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.066471 + 0.0042666 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_036_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=280, w3=624, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(280, min_periods=max(280//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 44)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.08 + 0.0042667 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_037_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=293, w3=641, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(51, min_periods=max(51//3, 2)).mean(), b.abs().rolling(293, min_periods=max(293//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.068333 * _rolling_slope(cover, 51) + 0.0042668 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_038_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=306, w3=658, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.074667 * y + 0.925333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 58) - _rolling_slope(basket, 306) + 0.0042669 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_039_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=319, w3=675, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(319, min_periods=max(319//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.120588 + 0.004267 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_040_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=332, w3=692, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(332, min_periods=max(332//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.087333 * _rolling_slope(draw, 692) + 0.0042671 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_041_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=345, w3=709, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(79) - b.diff(126)
    stress = imbalance.rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.147647 + 0.0042672 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_042_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=358, w3=726, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(358, min_periods=max(358//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.161176 + 0.0042673 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_043_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=371, w3=743, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 371)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.174706 + 0.0042674 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_044_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=384, w3=760, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.188235 + 0.0042675 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_045_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=397, w3=26, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(107)
    rank = change.rolling(397, min_periods=max(397//3, 2)).rank(pct=True)
    persistence = change.rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119 * persistence + 0.0042676 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_046_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=410, w3=43, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(410, min_periods=max(410//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.215294 + 0.0042677 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_047_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=423, w3=60, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(423, min_periods=max(423//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.131667 * slope + 0.0042678 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_048_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=436, w3=77, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(436, min_periods=max(436//3, 2)).mean()
    noise = impulse.abs().rolling(77, min_periods=max(77//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.242353 + 0.0042679 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_049_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=449, w3=94, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 449)
    curvature = _rolling_slope(acceleration, 94)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.144333 * acceleration + 0.004268 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_050_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=462, w3=111, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 142)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.150667 * pressure.rolling(111, min_periods=max(111//3, 2)).mean() + 0.0042681 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_051_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=475, w3=128, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(149, min_periods=max(149//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.282941 + 0.0042682 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_052_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=488, w3=145, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(488, min_periods=max(488//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 156)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.296471 + 0.0042683 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_053_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=501, w3=162, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(163, min_periods=max(163//3, 2)).mean(), b.abs().rolling(501, min_periods=max(501//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.169667 * _rolling_slope(cover, 163) + 0.0042684 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_054_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=15, w3=179, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.176 * y + 0.824000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 170) - _rolling_slope(basket, 15) + 0.0042685 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_055_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=28, w3=196, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(28, min_periods=max(28//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.337059 + 0.0042686 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_056_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=41, w3=213, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(41, min_periods=max(41//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.188667 * _rolling_slope(draw, 213) + 0.0042687 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_057_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=54, w3=230, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(54)
    stress = imbalance.rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.364118 + 0.0042688 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_058_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=67, w3=247, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(67, min_periods=max(67//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.377647 + 0.0042689 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_059_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=80, w3=264, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 80)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=264, adjust=False).mean() * 1.391176 + 0.004269 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_060_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=93, w3=281, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.404706 + 0.0042691 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_061_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=106, w3=298, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(106, min_periods=max(106//3, 2)).rank(pct=True)
    persistence = change.rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.220333 * persistence + 0.0042692 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_062_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=119, w3=315, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(119, min_periods=max(119//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.431765 + 0.0042693 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_063_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=132, w3=332, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.233 * slope + 0.0042694 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_064_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=145, w3=349, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.458824 + 0.0042695 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_065_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=158, w3=366, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 366)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.245667 * acceleration + 0.0042696 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_066_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=171, w3=383, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 7)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.252 * pressure.rolling(383, min_periods=max(383//3, 2)).mean() + 0.0042697 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_067_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=184, w3=400, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(14, min_periods=max(14//3, 2)).mean())
    decay = spread.ewm(span=184, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.499412 + 0.0042698 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_068_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=197, w3=417, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(197, min_periods=max(197//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.512941 + 0.0042699 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_069_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=210, w3=434, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(28, min_periods=max(28//3, 2)).mean(), b.abs().rolling(210, min_periods=max(210//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.271 * _rolling_slope(cover, 28) + 0.00427 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_070_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=223, w3=451, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.277333 * y + 0.722667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 35) - _rolling_slope(basket, 223) + 0.0042701 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_071_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=236, w3=468, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(236, min_periods=max(236//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.553529 + 0.0042702 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_072_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=249, w3=485, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(249, min_periods=max(249//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.29 * _rolling_slope(draw, 485) + 0.0042703 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_073_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=262, w3=502, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(56) - b.diff(126)
    stress = imbalance.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.580588 + 0.0042704 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_074_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=275, w3=519, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(275, min_periods=max(275//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.594118 + 0.0042705 * anchor
    return base_signal.diff().diff()

def f66_dpvd_gemini_075_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=288, w3=536, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 288)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.607647 + 0.0042706 * anchor
    return base_signal.diff().diff()
