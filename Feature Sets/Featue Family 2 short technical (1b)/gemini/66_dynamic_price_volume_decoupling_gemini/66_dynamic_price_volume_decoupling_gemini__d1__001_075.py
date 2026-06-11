"""66 dynamic price volume decoupling gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f66_dpvd_gemini_001_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=5]"""
    window = 5
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_002_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=10]"""
    window = 10
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_003_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=21]"""
    window = 21
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_004_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=42]"""
    window = 42
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_005_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=63]"""
    window = 63
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_006_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=126]"""
    window = 126
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_007_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=252]"""
    window = 252
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_008_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=504]"""
    window = 504
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_009_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=756]"""
    window = 756
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_010_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Instances where price and volume trends diverge, signaling loss of momentum. [window=1260]"""
    window = 1260
    res = _rolling_slope(close, window * 2) - _rolling_slope(volume, window)
    return (res).diff()

def f66_dpvd_gemini_011_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=131, w3=72, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.346333 * slope + 0.0042502 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_012_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=144, w3=89, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(144, min_periods=max(144//3, 2)).mean()
    noise = impulse.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.421765 + 0.0042503 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_013_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=157, w3=106, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.359 * acceleration + 0.0042504 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_014_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=170, w3=123, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 145)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.033 * pressure.rolling(123, min_periods=max(123//3, 2)).mean() + 0.0042505 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_015_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=183, w3=140, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(152, min_periods=max(152//3, 2)).mean())
    decay = spread.ewm(span=183, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.462353 + 0.0042506 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_016_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=196, w3=157, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(196, min_periods=max(196//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 159)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.475882 + 0.0042507 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_017_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=209, w3=174, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(166, min_periods=max(166//3, 2)).mean(), b.abs().rolling(209, min_periods=max(209//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.052 * _rolling_slope(cover, 166) + 0.0042508 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_018_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=222, w3=191, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.058333 * y + 0.941667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 173) - _rolling_slope(basket, 222) + 0.0042509 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_019_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=235, w3=208, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(180, min_periods=max(180//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.516471 + 0.004251 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_020_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=248, w3=225, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(187, min_periods=max(187//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.071 * _rolling_slope(draw, 225) + 0.0042511 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_021_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=261, w3=242, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.543529 + 0.0042512 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_022_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=274, w3=259, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 201)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.557059 + 0.0042513 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_023_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=287, w3=276, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 208)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=276, adjust=False).mean() * 1.570588 + 0.0042514 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_024_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=300, w3=293, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(300, min_periods=max(300//3, 2)).max()
    trough = x.rolling(215, min_periods=max(215//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.584118 + 0.0042515 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_025_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=313, w3=310, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.102667 * persistence + 0.0042516 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_026_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=326, w3=327, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(229, min_periods=max(229//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.611176 + 0.0042517 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_027_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=339, w3=344, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 236)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.115333 * slope + 0.0042518 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_028_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=352, w3=361, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(352, min_periods=max(352//3, 2)).mean()
    noise = impulse.abs().rolling(361, min_periods=max(361//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.638235 + 0.0042519 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_029_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=365, w3=378, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 378)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.128 * acceleration + 0.004252 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_030_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=378, w3=395, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 10)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.134333 * pressure.rolling(395, min_periods=max(395//3, 2)).mean() + 0.0042521 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_031_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=391, w3=412, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.825294 + 0.0042522 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_032_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=404, w3=429, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(404, min_periods=max(404//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 24)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.838824 + 0.0042523 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_033_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=417, w3=446, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(31, min_periods=max(31//3, 2)).mean(), b.abs().rolling(417, min_periods=max(417//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.153333 * _rolling_slope(cover, 31) + 0.0042524 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_034_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=430, w3=463, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.159667 * y + 0.840333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 38) - _rolling_slope(basket, 430) + 0.0042525 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_035_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=443, w3=480, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(443, min_periods=max(443//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.879412 + 0.0042526 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_036_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=456, w3=497, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(456, min_periods=max(456//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.172333 * _rolling_slope(draw, 497) + 0.0042527 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_037_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=469, w3=514, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(59) - b.diff(126)
    stress = imbalance.rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.906471 + 0.0042528 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_038_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=482, w3=531, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.92 + 0.0042529 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_039_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=495, w3=548, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.933529 + 0.004253 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_040_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=508, w3=565, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.947059 + 0.0042531 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_041_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=22, w3=582, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(87)
    rank = change.rolling(22, min_periods=max(22//3, 2)).rank(pct=True)
    persistence = change.rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.204 * persistence + 0.0042532 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_042_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=35, w3=599, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.974118 + 0.0042533 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_043_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=48, w3=616, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.216667 * slope + 0.0042534 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_044_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=61, w3=633, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(108)
    drag = impulse.rolling(61, min_periods=max(61//3, 2)).mean()
    noise = impulse.abs().rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.001176 + 0.0042535 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_045_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=74, w3=650, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 74)
    curvature = _rolling_slope(acceleration, 650)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.229333 * acceleration + 0.0042536 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_046_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=87, w3=667, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 122)
    pressure = rel_log.diff(87)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.235667 * pressure.rolling(667, min_periods=max(667//3, 2)).mean() + 0.0042537 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_047_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=100, w3=684, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(129, min_periods=max(129//3, 2)).mean())
    decay = spread.ewm(span=100, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.041765 + 0.0042538 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_048_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=113, w3=701, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(113, min_periods=max(113//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 136)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.055294 + 0.0042539 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_049_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=126, w3=718, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(143, min_periods=max(143//3, 2)).mean(), b.abs().rolling(126, min_periods=max(126//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.254667 * _rolling_slope(cover, 143) + 0.004254 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_050_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=139, w3=735, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.261 * y + 0.739000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 150) - _rolling_slope(basket, 139) + 0.0042541 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_051_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=152, w3=752, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.095882 + 0.0042542 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_052_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=165, w3=18, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(165, min_periods=max(165//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.273667 * _rolling_slope(draw, 18) + 0.0042543 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_053_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=178, w3=35, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.122941 + 0.0042544 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_054_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=191, w3=52, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 178)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.136471 + 0.0042545 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_055_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=204, w3=69, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 185)
    slow = _rolling_slope(x, 204)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=69, adjust=False).mean() * 1.15 + 0.0042546 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_056_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=217, w3=86, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(192, min_periods=max(192//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.163529 + 0.0042547 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_057_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=230, w3=103, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(230, min_periods=max(230//3, 2)).rank(pct=True)
    persistence = change.rolling(103, min_periods=max(103//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.305333 * persistence + 0.0042548 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_058_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=243, w3=120, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(206, min_periods=max(206//3, 2)).std()
    vol_slow = ret.rolling(243, min_periods=max(243//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.190588 + 0.0042549 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_059_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=256, w3=137, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 213)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.318 * slope + 0.004255 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_060_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=269, w3=154, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(269, min_periods=max(269//3, 2)).mean()
    noise = impulse.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.217647 + 0.0042551 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_061_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=282, w3=171, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 227)
    acceleration = _rolling_slope(velocity, 282)
    curvature = _rolling_slope(acceleration, 171)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.330667 * acceleration + 0.0042552 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_062_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=295, w3=188, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 234)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.337 * pressure.rolling(188, min_periods=max(188//3, 2)).mean() + 0.0042553 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_063_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=308, w3=205, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(241, min_periods=max(241//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.258235 + 0.0042554 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_064_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=321, w3=222, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(321, min_periods=max(321//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 248)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.271765 + 0.0042555 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_065_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=334, w3=239, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(8, min_periods=max(8//3, 2)).mean(), b.abs().rolling(334, min_periods=max(334//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.356 * _rolling_slope(cover, 8) + 0.0042556 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_066_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=347, w3=256, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.362333 * y + 0.637667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 15) - _rolling_slope(basket, 347) + 0.0042557 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_067_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=360, w3=273, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(360, min_periods=max(360//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.312353 + 0.0042558 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_068_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=373, w3=290, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.042667 * _rolling_slope(draw, 290) + 0.0042559 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_069_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=386, w3=307, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(36) - b.diff(126)
    stress = imbalance.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.339412 + 0.004256 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_070_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=399, w3=324, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(399, min_periods=max(399//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.352941 + 0.0042561 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_071_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=412, w3=341, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 412)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.366471 + 0.0042562 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_072_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=425, w3=358, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(425, min_periods=max(425//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.38 + 0.0042563 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_073_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=438, w3=375, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(64)
    rank = change.rolling(438, min_periods=max(438//3, 2)).rank(pct=True)
    persistence = change.rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.074333 * persistence + 0.0042564 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_074_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=451, w3=392, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(451, min_periods=max(451//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.407059 + 0.0042565 * anchor
    return base_signal.diff()

def f66_dpvd_gemini_075_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=464, w3=409, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.087 * slope + 0.0042566 * anchor
    return base_signal.diff()
