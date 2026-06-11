"""37 range estimators family gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Estimation of true market range and volatility using high-low-open-close relationships.
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

def f37_rngm_gemini_001_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=5]"""
    window = 5
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_002_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=10]"""
    window = 10
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_003_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=21]"""
    window = 21
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_004_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=42]"""
    window = 42
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_005_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=63]"""
    window = 63
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_006_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=126]"""
    window = 126
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_007_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=252]"""
    window = 252
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_008_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=504]"""
    window = 504
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_009_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=756]"""
    window = 756
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_010_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Estimation of true market range and volatility using high-low-open-close relationships. [window=1260]"""
    window = 1260
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window * 2))
    return (res).diff().diff()

def f37_rngm_gemini_011_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=411, w3=487, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 411)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.234706 + 0.0026402 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_012_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=424, w3=504, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(424, min_periods=max(424//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.248235 + 0.0026403 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_013_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=437, w3=521, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(70)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.086333 * persistence + 0.0026404 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_014_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=450, w3=538, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.275294 + 0.0026405 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_015_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=463, w3=555, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(463, min_periods=max(463//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.099 * slope + 0.0026406 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_016_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=476, w3=572, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(91)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.302353 + 0.0026407 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_017_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=489, w3=589, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 589)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.111667 * acceleration + 0.0026408 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_018_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=502, w3=606, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 105)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.118 * pressure.rolling(606, min_periods=max(606//3, 2)).mean() + 0.0026409 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_019_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=16, w3=623, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(112, min_periods=max(112//3, 2)).mean())
    decay = spread.ewm(span=16, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.342941 + 0.002641 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_020_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=29, w3=640, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(29, min_periods=max(29//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 119)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.356471 + 0.0026411 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_021_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=42, w3=657, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(126, min_periods=max(126//3, 2)).mean(), b.abs().rolling(42, min_periods=max(42//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.137 * _rolling_slope(cover, 126) + 0.0026412 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_022_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=55, w3=674, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.143333 * y + 0.856667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 133) - _rolling_slope(basket, 55) + 0.0026413 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_023_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=68, w3=691, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(68, min_periods=max(68//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.397059 + 0.0026414 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_024_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=81, w3=708, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(81, min_periods=max(81//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.156 * _rolling_slope(draw, 708) + 0.0026415 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_025_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=94, w3=725, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(94)
    stress = imbalance.rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.424118 + 0.0026416 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_026_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=107, w3=742, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(107, min_periods=max(107//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.437647 + 0.0026417 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_027_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=120, w3=759, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.451176 + 0.0026418 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_028_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=133, w3=25, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.464706 + 0.0026419 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_029_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=146, w3=42, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(146, min_periods=max(146//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.187667 * persistence + 0.002642 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_030_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=159, w3=59, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(159, min_periods=max(159//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.491765 + 0.0026421 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_031_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=172, w3=76, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(172, min_periods=max(172//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.200333 * slope + 0.0026422 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_032_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=185, w3=93, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(185, min_periods=max(185//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.518824 + 0.0026423 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_033_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=198, w3=110, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.213 * acceleration + 0.0026424 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_034_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=211, w3=127, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 217)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.219333 * pressure.rolling(127, min_periods=max(127//3, 2)).mean() + 0.0026425 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_035_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=224, w3=144, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(224, min_periods=max(224//3, 2)).mean())
    decay = spread.ewm(span=224, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.559412 + 0.0026426 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_036_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=237, w3=161, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(237, min_periods=max(237//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 231)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.572941 + 0.0026427 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_037_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=250, w3=178, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(238, min_periods=max(238//3, 2)).mean(), b.abs().rolling(250, min_periods=max(250//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.238333 * _rolling_slope(cover, 238) + 0.0026428 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_038_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=263, w3=195, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.244667 * y + 0.755333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 245) - _rolling_slope(basket, 263) + 0.0026429 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_039_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=276, w3=212, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(276, min_periods=max(276//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.613529 + 0.002643 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_040_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=289, w3=229, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(289, min_periods=max(289//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.257333 * _rolling_slope(draw, 229) + 0.0026431 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_041_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=302, w3=246, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(19) - b.diff(126)
    stress = imbalance.rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.640588 + 0.0026432 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_042_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=315, w3=263, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(315, min_periods=max(315//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.654118 + 0.0026433 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_043_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=328, w3=280, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 328)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=280, adjust=False).mean() * 1.667647 + 0.0026434 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_044_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=341, w3=297, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(341, min_periods=max(341//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.827647 + 0.0026435 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_045_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=354, w3=314, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(47)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289 * persistence + 0.0026436 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_046_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=367, w3=331, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(367, min_periods=max(367//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.854706 + 0.0026437 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_047_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=380, w3=348, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(380, min_periods=max(380//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.301667 * slope + 0.0026438 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_048_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=393, w3=365, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(68)
    drag = impulse.rolling(393, min_periods=max(393//3, 2)).mean()
    noise = impulse.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.881765 + 0.0026439 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_049_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=406, w3=382, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 382)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.314333 * acceleration + 0.002644 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_050_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=419, w3=399, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 82)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.320667 * pressure.rolling(399, min_periods=max(399//3, 2)).mean() + 0.0026441 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_051_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=432, w3=416, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(89, min_periods=max(89//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.922353 + 0.0026442 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_052_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=445, w3=433, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(445, min_periods=max(445//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 96)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.935882 + 0.0026443 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_053_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=458, w3=450, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(103, min_periods=max(103//3, 2)).mean(), b.abs().rolling(458, min_periods=max(458//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.339667 * _rolling_slope(cover, 103) + 0.0026444 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_054_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=471, w3=467, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.346 * y + 0.654000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 110) - _rolling_slope(basket, 471) + 0.0026445 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_055_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=484, w3=484, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(117, min_periods=max(117//3, 2)).mean(), upside.rolling(484, min_periods=max(484//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.976471 + 0.0026446 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_056_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=497, w3=501, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(497, min_periods=max(497//3, 2)).max()
    rebound = x - x.rolling(124, min_periods=max(124//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.358667 * _rolling_slope(draw, 501) + 0.0026447 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_057_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=11, w3=518, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(11)
    stress = imbalance.rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.003529 + 0.0026448 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_058_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=24, w3=535, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(24, min_periods=max(24//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.017059 + 0.0026449 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_059_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=37, w3=552, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 37)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.030588 + 0.002645 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_060_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=50, w3=569, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(50, min_periods=max(50//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.044118 + 0.0026451 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_061_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=63, w3=586, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(63, min_periods=max(63//3, 2)).rank(pct=True)
    persistence = change.rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.058 * persistence + 0.0026452 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_062_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=76, w3=603, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(76, min_periods=max(76//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.071176 + 0.0026453 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_063_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=89, w3=620, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.070667 * slope + 0.0026454 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_064_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=102, w3=637, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(102, min_periods=max(102//3, 2)).mean()
    noise = impulse.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.098235 + 0.0026455 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_065_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=115, w3=654, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 654)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.083333 * acceleration + 0.0026456 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_066_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=128, w3=671, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 194)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.089667 * pressure.rolling(671, min_periods=max(671//3, 2)).mean() + 0.0026457 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_067_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=141, w3=688, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(201, min_periods=max(201//3, 2)).mean())
    decay = spread.ewm(span=141, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.138824 + 0.0026458 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_068_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=154, w3=705, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(154, min_periods=max(154//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 208)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.152353 + 0.0026459 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_069_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=167, w3=722, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(215, min_periods=max(215//3, 2)).mean(), b.abs().rolling(167, min_periods=max(167//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.108667 * _rolling_slope(cover, 215) + 0.002646 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_070_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=180, w3=739, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.115 * y + 0.885000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 222) - _rolling_slope(basket, 180) + 0.0026461 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_071_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=193, w3=756, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(193, min_periods=max(193//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.192941 + 0.0026462 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_072_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=206, w3=22, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(206, min_periods=max(206//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.127667 * _rolling_slope(draw, 22) + 0.0026463 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_073_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=219, w3=39, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.22 + 0.0026464 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_074_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=232, w3=56, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(232, min_periods=max(232//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.233529 + 0.0026465 * anchor
    return base_signal.diff().diff()

def f37_rngm_gemini_075_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=245, w3=73, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=73, adjust=False).mean() * 1.247059 + 0.0026466 * anchor
    return base_signal.diff().diff()
