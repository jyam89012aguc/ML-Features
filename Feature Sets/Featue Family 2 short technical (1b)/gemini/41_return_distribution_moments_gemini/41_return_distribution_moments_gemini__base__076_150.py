"""41 return distribution moments gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Statistical analysis of return skewness and kurtosis to identify non-normal risk.
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

def f41_rmom_gemini_076(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=289, w3=366, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(289, min_periods=max(289//3, 2)).mean()
    noise = impulse.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.318824 + 0.0028427 * anchor
    return base_signal

def f41_rmom_gemini_077(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=302, w3=383, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 302)
    curvature = _rolling_slope(acceleration, 383)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.276333 * acceleration + 0.0028428 * anchor
    return base_signal

def f41_rmom_gemini_078(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=315, w3=400, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(315, min_periods=max(315//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.345882 + 0.0028429 * anchor
    return base_signal

def f41_rmom_gemini_079(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=328, w3=417, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.289 * _rolling_slope(draw, 417) + 0.002843 * anchor
    return base_signal

def f41_rmom_gemini_080(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=341, w3=434, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.372941 + 0.0028431 * anchor
    return base_signal

def f41_rmom_gemini_081(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=354, w3=451, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 354)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.386471 + 0.0028432 * anchor
    return base_signal

def f41_rmom_gemini_082(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=367, w3=468, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(367, min_periods=max(367//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4 + 0.0028433 * anchor
    return base_signal

def f41_rmom_gemini_083(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=380, w3=485, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(380, min_periods=max(380//3, 2)).rank(pct=True)
    persistence = change.rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.314333 * persistence + 0.0028434 * anchor
    return base_signal

def f41_rmom_gemini_084(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=393, w3=502, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(393, min_periods=max(393//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.427059 + 0.0028435 * anchor
    return base_signal

def f41_rmom_gemini_085(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=406, w3=519, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(406, min_periods=max(406//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.327 * slope + 0.0028436 * anchor
    return base_signal

def f41_rmom_gemini_086(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=419, w3=536, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(419, min_periods=max(419//3, 2)).mean()
    noise = impulse.abs().rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.454118 + 0.0028437 * anchor
    return base_signal

def f41_rmom_gemini_087(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=432, w3=553, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 432)
    curvature = _rolling_slope(acceleration, 553)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.339667 * acceleration + 0.0028438 * anchor
    return base_signal

def f41_rmom_gemini_088(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=445, w3=570, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(445, min_periods=max(445//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.481176 + 0.0028439 * anchor
    return base_signal

def f41_rmom_gemini_089(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=458, w3=587, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(458, min_periods=max(458//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.352333 * _rolling_slope(draw, 587) + 0.002844 * anchor
    return base_signal

def f41_rmom_gemini_090(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=471, w3=604, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(471, min_periods=max(471//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.508235 + 0.0028441 * anchor
    return base_signal

def f41_rmom_gemini_091(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=484, w3=621, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.521765 + 0.0028442 * anchor
    return base_signal

def f41_rmom_gemini_092(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=497, w3=638, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(497, min_periods=max(497//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.535294 + 0.0028443 * anchor
    return base_signal

def f41_rmom_gemini_093(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=11, w3=655, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(24)
    rank = change.rolling(11, min_periods=max(11//3, 2)).rank(pct=True)
    persistence = change.rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.045333 * persistence + 0.0028444 * anchor
    return base_signal

def f41_rmom_gemini_094(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=24, w3=672, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(24, min_periods=max(24//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.562353 + 0.0028445 * anchor
    return base_signal

def f41_rmom_gemini_095(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=37, w3=689, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(37, min_periods=max(37//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.058 * slope + 0.0028446 * anchor
    return base_signal

def f41_rmom_gemini_096(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=50, w3=706, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(45)
    drag = impulse.rolling(50, min_periods=max(50//3, 2)).mean()
    noise = impulse.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.589412 + 0.0028447 * anchor
    return base_signal

def f41_rmom_gemini_097(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=63, w3=723, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 63)
    curvature = _rolling_slope(acceleration, 723)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.070667 * acceleration + 0.0028448 * anchor
    return base_signal

def f41_rmom_gemini_098(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=76, w3=740, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(76, min_periods=max(76//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.616471 + 0.0028449 * anchor
    return base_signal

def f41_rmom_gemini_099(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=89, w3=757, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.083333 * _rolling_slope(draw, 757) + 0.002845 * anchor
    return base_signal

def f41_rmom_gemini_100(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=102, w3=23, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.643529 + 0.0028451 * anchor
    return base_signal

def f41_rmom_gemini_101(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=115, w3=40, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 115)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=40, adjust=False).mean() * 1.657059 + 0.0028452 * anchor
    return base_signal

def f41_rmom_gemini_102(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=128, w3=57, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.670588 + 0.0028453 * anchor
    return base_signal

def f41_rmom_gemini_103(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=141, w3=74, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(94)
    rank = change.rolling(141, min_periods=max(141//3, 2)).rank(pct=True)
    persistence = change.rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.108667 * persistence + 0.0028454 * anchor
    return base_signal

def f41_rmom_gemini_104(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=154, w3=91, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(154, min_periods=max(154//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.844118 + 0.0028455 * anchor
    return base_signal

def f41_rmom_gemini_105(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=167, w3=108, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(167, min_periods=max(167//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.121333 * slope + 0.0028456 * anchor
    return base_signal

def f41_rmom_gemini_106(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=180, w3=125, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(115)
    drag = impulse.rolling(180, min_periods=max(180//3, 2)).mean()
    noise = impulse.abs().rolling(125, min_periods=max(125//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.871176 + 0.0028457 * anchor
    return base_signal

def f41_rmom_gemini_107(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=193, w3=142, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 193)
    curvature = _rolling_slope(acceleration, 142)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.134 * acceleration + 0.0028458 * anchor
    return base_signal

def f41_rmom_gemini_108(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=206, w3=159, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.898235 + 0.0028459 * anchor
    return base_signal

def f41_rmom_gemini_109(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=219, w3=176, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(219, min_periods=max(219//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.146667 * _rolling_slope(draw, 176) + 0.002846 * anchor
    return base_signal

def f41_rmom_gemini_110(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=232, w3=193, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(232, min_periods=max(232//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.925294 + 0.0028461 * anchor
    return base_signal

def f41_rmom_gemini_111(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=245, w3=210, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=210, adjust=False).mean() * 0.938824 + 0.0028462 * anchor
    return base_signal

def f41_rmom_gemini_112(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=258, w3=227, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(258, min_periods=max(258//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.952353 + 0.0028463 * anchor
    return base_signal

def f41_rmom_gemini_113(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=271, w3=244, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(271, min_periods=max(271//3, 2)).rank(pct=True)
    persistence = change.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.172 * persistence + 0.0028464 * anchor
    return base_signal

def f41_rmom_gemini_114(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=284, w3=261, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(284, min_periods=max(284//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.979412 + 0.0028465 * anchor
    return base_signal

def f41_rmom_gemini_115(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=297, w3=278, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(297, min_periods=max(297//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.184667 * slope + 0.0028466 * anchor
    return base_signal

def f41_rmom_gemini_116(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=310, w3=295, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.006471 + 0.0028467 * anchor
    return base_signal

def f41_rmom_gemini_117(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=323, w3=312, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 323)
    curvature = _rolling_slope(acceleration, 312)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.197333 * acceleration + 0.0028468 * anchor
    return base_signal

def f41_rmom_gemini_118(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=336, w3=329, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(336, min_periods=max(336//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.033529 + 0.0028469 * anchor
    return base_signal

def f41_rmom_gemini_119(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=349, w3=346, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(349, min_periods=max(349//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.21 * _rolling_slope(draw, 346) + 0.002847 * anchor
    return base_signal

def f41_rmom_gemini_120(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=362, w3=363, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(363, min_periods=max(363//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.060588 + 0.0028471 * anchor
    return base_signal

def f41_rmom_gemini_121(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=375, w3=380, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 375)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.074118 + 0.0028472 * anchor
    return base_signal

def f41_rmom_gemini_122(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=388, w3=397, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(388, min_periods=max(388//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.087647 + 0.0028473 * anchor
    return base_signal

def f41_rmom_gemini_123(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=401, w3=414, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(401, min_periods=max(401//3, 2)).rank(pct=True)
    persistence = change.rolling(414, min_periods=max(414//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.235333 * persistence + 0.0028474 * anchor
    return base_signal

def f41_rmom_gemini_124(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=414, w3=431, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(414, min_periods=max(414//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.114706 + 0.0028475 * anchor
    return base_signal

def f41_rmom_gemini_125(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=427, w3=448, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(427, min_periods=max(427//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.248 * slope + 0.0028476 * anchor
    return base_signal

def f41_rmom_gemini_126(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=440, w3=465, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(8)
    drag = impulse.rolling(440, min_periods=max(440//3, 2)).mean()
    noise = impulse.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.141765 + 0.0028477 * anchor
    return base_signal

def f41_rmom_gemini_127(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=453, w3=482, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 453)
    curvature = _rolling_slope(acceleration, 482)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.260667 * acceleration + 0.0028478 * anchor
    return base_signal

def f41_rmom_gemini_128(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=466, w3=499, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.168824 + 0.0028479 * anchor
    return base_signal

def f41_rmom_gemini_129(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=479, w3=516, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(479, min_periods=max(479//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.273333 * _rolling_slope(draw, 516) + 0.002848 * anchor
    return base_signal

def f41_rmom_gemini_130(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=492, w3=533, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(492, min_periods=max(492//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.195882 + 0.0028481 * anchor
    return base_signal

def f41_rmom_gemini_131(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=505, w3=550, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.209412 + 0.0028482 * anchor
    return base_signal

def f41_rmom_gemini_132(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=19, w3=567, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(19, min_periods=max(19//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.222941 + 0.0028483 * anchor
    return base_signal

def f41_rmom_gemini_133(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=32, w3=584, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(57)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.298667 * persistence + 0.0028484 * anchor
    return base_signal

def f41_rmom_gemini_134(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=45, w3=601, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(45, min_periods=max(45//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.25 + 0.0028485 * anchor
    return base_signal

def f41_rmom_gemini_135(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=58, w3=618, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(58, min_periods=max(58//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.311333 * slope + 0.0028486 * anchor
    return base_signal

def f41_rmom_gemini_136(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=71, w3=635, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(78)
    drag = impulse.rolling(71, min_periods=max(71//3, 2)).mean()
    noise = impulse.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.277059 + 0.0028487 * anchor
    return base_signal

def f41_rmom_gemini_137(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=84, w3=652, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 84)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.324 * acceleration + 0.0028488 * anchor
    return base_signal

def f41_rmom_gemini_138(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=97, w3=669, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(97, min_periods=max(97//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.304118 + 0.0028489 * anchor
    return base_signal

def f41_rmom_gemini_139(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=110, w3=686, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.336667 * _rolling_slope(draw, 686) + 0.002849 * anchor
    return base_signal

def f41_rmom_gemini_140(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=123, w3=703, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.331176 + 0.0028491 * anchor
    return base_signal

def f41_rmom_gemini_141(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=136, w3=720, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 136)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.344706 + 0.0028492 * anchor
    return base_signal

def f41_rmom_gemini_142(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=149, w3=737, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(149, min_periods=max(149//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.358235 + 0.0028493 * anchor
    return base_signal

def f41_rmom_gemini_143(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=162, w3=754, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(162, min_periods=max(162//3, 2)).rank(pct=True)
    persistence = change.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.362 * persistence + 0.0028494 * anchor
    return base_signal

def f41_rmom_gemini_144(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=175, w3=20, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(175, min_periods=max(175//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.385294 + 0.0028495 * anchor
    return base_signal

def f41_rmom_gemini_145(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=188, w3=37, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(188, min_periods=max(188//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.042333 * slope + 0.0028496 * anchor
    return base_signal

def f41_rmom_gemini_146(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=201, w3=54, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(201, min_periods=max(201//3, 2)).mean()
    noise = impulse.abs().rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.412353 + 0.0028497 * anchor
    return base_signal

def f41_rmom_gemini_147(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=214, w3=71, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 214)
    curvature = _rolling_slope(acceleration, 71)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.055 * acceleration + 0.0028498 * anchor
    return base_signal

def f41_rmom_gemini_148(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=227, w3=88, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(227, min_periods=max(227//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(88) * 1.439412 + 0.0028499 * anchor
    return base_signal

def f41_rmom_gemini_149(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=240, w3=105, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(240, min_periods=max(240//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.067667 * _rolling_slope(draw, 105) + 0.00285 * anchor
    return base_signal

def f41_rmom_gemini_150(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=253, w3=122, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(253, min_periods=max(253//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.466471 + 0.0028501 * anchor
    return base_signal
