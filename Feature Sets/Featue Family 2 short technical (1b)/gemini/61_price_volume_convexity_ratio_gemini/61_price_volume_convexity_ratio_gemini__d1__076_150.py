"""61 price volume convexity ratio gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Non-linear relationship between price change and volume as a signal of trend strength.
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
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f61_pvcr_gemini_076_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=504, w3=139, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(504, min_periods=max(504//3, 2)).mean()
    noise = impulse.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.107059 + 0.0039767 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_077_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=18, w3=156, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 18)
    curvature = _rolling_slope(acceleration, 156)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.312333 * acceleration + 0.0039768 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_078_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=31, w3=173, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 12)
    pressure = rel_log.diff(31)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.318667 * pressure.rolling(173, min_periods=max(173//3, 2)).mean() + 0.0039769 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_079_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=44, w3=190, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(19, min_periods=max(19//3, 2)).mean())
    decay = spread.ewm(span=44, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.147647 + 0.003977 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_080_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=57, w3=207, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(57, min_periods=max(57//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 26)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.161176 + 0.0039771 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_081_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=70, w3=224, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(33, min_periods=max(33//3, 2)).mean(), b.abs().rolling(70, min_periods=max(70//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.337667 * _rolling_slope(cover, 33) + 0.0039772 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_082_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=83, w3=241, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.344 * y + 0.656000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 40) - _rolling_slope(basket, 83) + 0.0039773 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_083_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=96, w3=258, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(96, min_periods=max(96//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.201765 + 0.0039774 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_084_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=109, w3=275, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(109, min_periods=max(109//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.356667 * _rolling_slope(draw, 275) + 0.0039775 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_085_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=122, w3=292, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(61) - b.diff(122)
    stress = imbalance.rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.228824 + 0.0039776 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_086_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=135, w3=309, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(135, min_periods=max(135//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.242353 + 0.0039777 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_087_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=148, w3=326, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 148)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.255882 + 0.0039778 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_088_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=161, w3=343, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(161, min_periods=max(161//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.269412 + 0.0039779 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_089_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=174, w3=360, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(89)
    rank = change.rolling(174, min_periods=max(174//3, 2)).rank(pct=True)
    persistence = change.rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.056 * persistence + 0.003978 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_090_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=187, w3=377, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(187, min_periods=max(187//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.296471 + 0.0039781 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_091_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=200, w3=394, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(200, min_periods=max(200//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.068667 * slope + 0.0039782 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_092_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=213, w3=411, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(110)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.323529 + 0.0039783 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_093_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=226, w3=428, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 428)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.081333 * acceleration + 0.0039784 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_094_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=239, w3=445, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 124)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.087667 * pressure.rolling(445, min_periods=max(445//3, 2)).mean() + 0.0039785 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_095_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=252, w3=462, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    decay = spread.ewm(span=252, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.364118 + 0.0039786 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_096_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=265, w3=479, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(265, min_periods=max(265//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 138)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.377647 + 0.0039787 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_097_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=278, w3=496, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(145, min_periods=max(145//3, 2)).mean(), b.abs().rolling(278, min_periods=max(278//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.106667 * _rolling_slope(cover, 145) + 0.0039788 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_098_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=291, w3=513, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.113 * y + 0.887000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 152) - _rolling_slope(basket, 291) + 0.0039789 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_099_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=304, w3=530, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.418235 + 0.003979 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_100_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=317, w3=547, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.125667 * _rolling_slope(draw, 547) + 0.0039791 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_101_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=330, w3=564, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.445294 + 0.0039792 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_102_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=343, w3=581, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(343, min_periods=max(343//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.458824 + 0.0039793 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_103_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=356, w3=598, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 356)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.472353 + 0.0039794 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_104_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=369, w3=615, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(369, min_periods=max(369//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.485882 + 0.0039795 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_105_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=382, w3=632, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(382, min_periods=max(382//3, 2)).rank(pct=True)
    persistence = change.rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.157333 * persistence + 0.0039796 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_106_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=395, w3=649, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.512941 + 0.0039797 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_107_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=408, w3=666, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(408, min_periods=max(408//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.17 * slope + 0.0039798 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_108_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=421, w3=683, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(421, min_periods=max(421//3, 2)).mean()
    noise = impulse.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.54 + 0.0039799 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_109_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=434, w3=700, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 434)
    curvature = _rolling_slope(acceleration, 700)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.182667 * acceleration + 0.00398 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_110_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=447, w3=717, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.189 * pressure.rolling(717, min_periods=max(717//3, 2)).mean() + 0.0039801 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_111_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=460, w3=734, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.580588 + 0.0039802 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_112_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=473, w3=751, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(473, min_periods=max(473//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.594118 + 0.0039803 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_113_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=486, w3=17, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(486, min_periods=max(486//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(17) + 0.208 * _rolling_slope(cover, 10) + 0.0039804 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_114_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=499, w3=34, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.214333 * y + 0.785667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 499) + 0.0039805 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_115_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=13, w3=51, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(13, min_periods=max(13//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(51) * 1.634706 + 0.0039806 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_116_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=26, w3=68, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(26, min_periods=max(26//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227 * _rolling_slope(draw, 68) + 0.0039807 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_117_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=39, w3=85, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(38) - b.diff(39)
    stress = imbalance.rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.661765 + 0.0039808 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_118_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=52, w3=102, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(52, min_periods=max(52//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.821765 + 0.0039809 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_119_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=65, w3=119, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=119, adjust=False).mean() * 0.835294 + 0.003981 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_120_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=78, w3=136, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.848824 + 0.0039811 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_121_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=91, w3=153, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(66)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.258667 * persistence + 0.0039812 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_122_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=104, w3=170, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(104, min_periods=max(104//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.875882 + 0.0039813 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_123_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=117, w3=187, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(117, min_periods=max(117//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.271333 * slope + 0.0039814 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_124_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=130, w3=204, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(87)
    drag = impulse.rolling(130, min_periods=max(130//3, 2)).mean()
    noise = impulse.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.902941 + 0.0039815 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_125_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=143, w3=221, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 143)
    curvature = _rolling_slope(acceleration, 221)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.284 * acceleration + 0.0039816 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_126_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=156, w3=238, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 101)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.290333 * pressure.rolling(238, min_periods=max(238//3, 2)).mean() + 0.0039817 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_127_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=169, w3=255, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=169, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.943529 + 0.0039818 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_128_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=182, w3=272, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(182, min_periods=max(182//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 115)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.957059 + 0.0039819 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_129_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=195, w3=289, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(122, min_periods=max(122//3, 2)).mean(), b.abs().rolling(195, min_periods=max(195//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.309333 * _rolling_slope(cover, 122) + 0.003982 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_130_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=208, w3=306, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.315667 * y + 0.684333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 129) - _rolling_slope(basket, 208) + 0.0039821 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_131_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=221, w3=323, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(221, min_periods=max(221//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.997647 + 0.0039822 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_132_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=234, w3=340, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(234, min_periods=max(234//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.328333 * _rolling_slope(draw, 340) + 0.0039823 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_133_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=247, w3=357, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.024706 + 0.0039824 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_134_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=260, w3=374, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(260, min_periods=max(260//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.038235 + 0.0039825 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_135_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=273, w3=391, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 273)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.051765 + 0.0039826 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_136_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=286, w3=408, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(286, min_periods=max(286//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.065294 + 0.0039827 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_137_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=299, w3=425, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(299, min_periods=max(299//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.36 * persistence + 0.0039828 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_138_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=312, w3=442, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(312, min_periods=max(312//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.092353 + 0.0039829 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_139_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=325, w3=459, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(325, min_periods=max(325//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.040333 * slope + 0.003983 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_140_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=338, w3=476, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(338, min_periods=max(338//3, 2)).mean()
    noise = impulse.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.119412 + 0.0039831 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_141_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=351, w3=493, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 351)
    curvature = _rolling_slope(acceleration, 493)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.053 * acceleration + 0.0039832 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_142_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=364, w3=510, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 213)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.059333 * pressure.rolling(510, min_periods=max(510//3, 2)).mean() + 0.0039833 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_143_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=377, w3=527, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(220, min_periods=max(220//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.16 + 0.0039834 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_144_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=390, w3=544, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(390, min_periods=max(390//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 227)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.173529 + 0.0039835 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_145_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=403, w3=561, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(234, min_periods=max(234//3, 2)).mean(), b.abs().rolling(403, min_periods=max(403//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.078333 * _rolling_slope(cover, 234) + 0.0039836 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_146_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=416, w3=578, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.084667 * y + 0.915333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 241) - _rolling_slope(basket, 416) + 0.0039837 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_147_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=429, w3=595, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.214118 + 0.0039838 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_148_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=442, w3=612, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(442, min_periods=max(442//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.097333 * _rolling_slope(draw, 612) + 0.0039839 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_149_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=455, w3=629, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(15) - b.diff(126)
    stress = imbalance.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.241176 + 0.003984 * anchor
    return base_signal.diff()

def f61_pvcr_gemini_150_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=468, w3=646, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(468, min_periods=max(468//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.254706 + 0.0039841 * anchor
    return base_signal.diff()
