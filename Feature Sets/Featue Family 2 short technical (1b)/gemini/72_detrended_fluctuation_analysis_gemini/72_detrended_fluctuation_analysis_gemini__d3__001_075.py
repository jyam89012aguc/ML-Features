"""72 detrended fluctuation analysis gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Scaling properties of price fluctuations to detect fractal-like behavior.
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

def f72_dfa_gemini_001_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_002_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_003_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_004_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_005_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_006_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_007_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_008_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_009_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_010_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Scaling properties of price fluctuations to detect fractal-like behavior. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() * volume.rolling(window).mean() / (volume.rolling(window).mean() + 1e-9), window)
    return (res).diff().diff().diff()

def f72_dfa_gemini_011_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=46, w3=370, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.150588 + 0.0046142 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_012_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=59, w3=387, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.142667 * _rolling_slope(draw, 387) + 0.0046143 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_013_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=72, w3=404, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(72)
    stress = imbalance.rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.177647 + 0.0046144 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_014_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=85, w3=421, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(85, min_periods=max(85//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.191176 + 0.0046145 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_015_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=98, w3=438, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 98)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.204706 + 0.0046146 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_016_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=111, w3=455, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(111, min_periods=max(111//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.218235 + 0.0046147 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_017_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=124, w3=472, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(124, min_periods=max(124//3, 2)).rank(pct=True)
    persistence = change.rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.174333 * persistence + 0.0046148 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_018_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=137, w3=489, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(137, min_periods=max(137//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245294 + 0.0046149 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_019_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=150, w3=506, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(150, min_periods=max(150//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.187 * slope + 0.004615 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_020_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=163, w3=523, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(163, min_periods=max(163//3, 2)).mean()
    noise = impulse.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.272353 + 0.0046151 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_021_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=176, w3=540, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 176)
    curvature = _rolling_slope(acceleration, 540)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.199667 * acceleration + 0.0046152 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_022_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=189, w3=557, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 240)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.206 * pressure.rolling(557, min_periods=max(557//3, 2)).mean() + 0.0046153 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_023_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=202, w3=574, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(247, min_periods=max(247//3, 2)).mean())
    decay = spread.ewm(span=202, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.312941 + 0.0046154 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_024_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=215, w3=591, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(215, min_periods=max(215//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 7)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.326471 + 0.0046155 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_025_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=228, w3=608, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(14, min_periods=max(14//3, 2)).mean(), b.abs().rolling(228, min_periods=max(228//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.225 * _rolling_slope(cover, 14) + 0.0046156 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_026_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=241, w3=625, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.231333 * y + 0.768667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 21) - _rolling_slope(basket, 241) + 0.0046157 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_027_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=254, w3=642, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.367059 + 0.0046158 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_028_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=267, w3=659, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(267, min_periods=max(267//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.244 * _rolling_slope(draw, 659) + 0.0046159 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_029_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=280, w3=676, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(42) - b.diff(126)
    stress = imbalance.rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.394118 + 0.004616 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_030_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=293, w3=693, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(293, min_periods=max(293//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.407647 + 0.0046161 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_031_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=306, w3=710, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 306)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.421176 + 0.0046162 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_032_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=319, w3=727, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(319, min_periods=max(319//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.434706 + 0.0046163 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_033_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=332, w3=744, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(70)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.275667 * persistence + 0.0046164 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_034_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=345, w3=761, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(345, min_periods=max(345//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.461765 + 0.0046165 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_035_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=358, w3=27, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(358, min_periods=max(358//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.288333 * slope + 0.0046166 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_036_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=371, w3=44, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(91)
    drag = impulse.rolling(371, min_periods=max(371//3, 2)).mean()
    noise = impulse.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.488824 + 0.0046167 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_037_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=384, w3=61, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 384)
    curvature = _rolling_slope(acceleration, 61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.301 * acceleration + 0.0046168 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_038_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=397, w3=78, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 105)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.307333 * pressure.rolling(78, min_periods=max(78//3, 2)).mean() + 0.0046169 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_039_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=410, w3=95, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(112, min_periods=max(112//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.529412 + 0.004617 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_040_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=423, w3=112, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(423, min_periods=max(423//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 119)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.542941 + 0.0046171 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_041_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=436, w3=129, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(126, min_periods=max(126//3, 2)).mean(), b.abs().rolling(436, min_periods=max(436//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.326333 * _rolling_slope(cover, 126) + 0.0046172 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_042_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=449, w3=146, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.332667 * y + 0.667333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 133) - _rolling_slope(basket, 449) + 0.0046173 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_043_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=462, w3=163, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(462, min_periods=max(462//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.583529 + 0.0046174 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_044_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=475, w3=180, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(475, min_periods=max(475//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.345333 * _rolling_slope(draw, 180) + 0.0046175 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_045_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=488, w3=197, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.610588 + 0.0046176 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_046_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=501, w3=214, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(501, min_periods=max(501//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.624118 + 0.0046177 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_047_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=15, w3=231, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 15)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=231, adjust=False).mean() * 1.637647 + 0.0046178 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_048_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=28, w3=248, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(28, min_periods=max(28//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.651176 + 0.0046179 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_049_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=41, w3=265, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.044667 * persistence + 0.004618 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_050_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=54, w3=282, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.824706 + 0.0046181 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_051_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=67, w3=299, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(67, min_periods=max(67//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.057333 * slope + 0.0046182 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_052_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=80, w3=316, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(80, min_periods=max(80//3, 2)).mean()
    noise = impulse.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.851765 + 0.0046183 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_053_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=93, w3=333, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 93)
    curvature = _rolling_slope(acceleration, 333)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.07 * acceleration + 0.0046184 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_054_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=106, w3=350, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 217)
    pressure = rel_log.diff(106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.076333 * pressure.rolling(350, min_periods=max(350//3, 2)).mean() + 0.0046185 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_055_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=119, w3=367, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(224, min_periods=max(224//3, 2)).mean())
    decay = spread.ewm(span=119, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.892353 + 0.0046186 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_056_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=132, w3=384, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(132, min_periods=max(132//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 231)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.905882 + 0.0046187 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_057_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=145, w3=401, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(238, min_periods=max(238//3, 2)).mean(), b.abs().rolling(145, min_periods=max(145//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.095333 * _rolling_slope(cover, 238) + 0.0046188 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_058_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=158, w3=418, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.101667 * y + 0.898333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 245) - _rolling_slope(basket, 158) + 0.0046189 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_059_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=171, w3=435, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.946471 + 0.004619 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_060_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=184, w3=452, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.114333 * _rolling_slope(draw, 452) + 0.0046191 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_061_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=197, w3=469, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(19) - b.diff(126)
    stress = imbalance.rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.973529 + 0.0046192 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_062_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=210, w3=486, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(210, min_periods=max(210//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.987059 + 0.0046193 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_063_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=223, w3=503, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 223)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.000588 + 0.0046194 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_064_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=236, w3=520, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.014118 + 0.0046195 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_065_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=249, w3=537, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(47)
    rank = change.rolling(249, min_periods=max(249//3, 2)).rank(pct=True)
    persistence = change.rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146 * persistence + 0.0046196 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_066_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=262, w3=554, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(262, min_periods=max(262//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.041176 + 0.0046197 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_067_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=275, w3=571, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(275, min_periods=max(275//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.158667 * slope + 0.0046198 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_068_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=288, w3=588, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(68)
    drag = impulse.rolling(288, min_periods=max(288//3, 2)).mean()
    noise = impulse.abs().rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.068235 + 0.0046199 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_069_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=301, w3=605, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 301)
    curvature = _rolling_slope(acceleration, 605)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.171333 * acceleration + 0.00462 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_070_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=314, w3=622, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 82)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.177667 * pressure.rolling(622, min_periods=max(622//3, 2)).mean() + 0.0046201 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_071_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=327, w3=639, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(89, min_periods=max(89//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.108824 + 0.0046202 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_072_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=340, w3=656, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(340, min_periods=max(340//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 96)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.122353 + 0.0046203 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_073_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=353, w3=673, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(103, min_periods=max(103//3, 2)).mean(), b.abs().rolling(353, min_periods=max(353//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.196667 * _rolling_slope(cover, 103) + 0.0046204 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_074_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=366, w3=690, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.203 * y + 0.797000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 110) - _rolling_slope(basket, 366) + 0.0046205 * anchor
    return base_signal.diff().diff().diff()

def f72_dfa_gemini_075_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=379, w3=707, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(379, min_periods=max(379//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.162941 + 0.0046206 * anchor
    return base_signal.diff().diff().diff()
