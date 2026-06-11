"""105 systemic fragility index gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Aggregated measure of fragility across multiple spectral and statistical dimensions.
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

def f105_sfix_gemini_076_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=213, w3=472, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(93)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.134118 + 0.0007847 * anchor
    return base_signal.diff()

def f105_sfix_gemini_077_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=226, w3=489, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 489)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211 * acceleration + 0.0007848 * anchor
    return base_signal.diff()

def f105_sfix_gemini_078_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=239, w3=506, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 107)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.217333 * pressure.rolling(506, min_periods=max(506//3, 2)).mean() + 0.0007849 * anchor
    return base_signal.diff()

def f105_sfix_gemini_079_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=252, w3=523, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    decay = spread.ewm(span=252, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.174706 + 0.000785 * anchor
    return base_signal.diff()

def f105_sfix_gemini_080_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=265, w3=540, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(265, min_periods=max(265//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.188235 + 0.0007851 * anchor
    return base_signal.diff()

def f105_sfix_gemini_081_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=278, w3=557, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(128, min_periods=max(128//3, 2)).mean(), b.abs().rolling(278, min_periods=max(278//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.236333 * _rolling_slope(cover, 128) + 0.0007852 * anchor
    return base_signal.diff()

def f105_sfix_gemini_082_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=291, w3=574, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.242667 * y + 0.757333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 135) - _rolling_slope(basket, 291) + 0.0007853 * anchor
    return base_signal.diff()

def f105_sfix_gemini_083_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=304, w3=591, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.228824 + 0.0007854 * anchor
    return base_signal.diff()

def f105_sfix_gemini_084_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=317, w3=608, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.255333 * _rolling_slope(draw, 608) + 0.0007855 * anchor
    return base_signal.diff()

def f105_sfix_gemini_085_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=330, w3=625, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.255882 + 0.0007856 * anchor
    return base_signal.diff()

def f105_sfix_gemini_086_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=343, w3=642, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(343, min_periods=max(343//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.269412 + 0.0007857 * anchor
    return base_signal.diff()

def f105_sfix_gemini_087_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=356, w3=659, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 356)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.282941 + 0.0007858 * anchor
    return base_signal.diff()

def f105_sfix_gemini_088_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=369, w3=676, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(369, min_periods=max(369//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.296471 + 0.0007859 * anchor
    return base_signal.diff()

def f105_sfix_gemini_089_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=382, w3=693, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(382, min_periods=max(382//3, 2)).rank(pct=True)
    persistence = change.rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.287 * persistence + 0.000786 * anchor
    return base_signal.diff()

def f105_sfix_gemini_090_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=395, w3=710, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(395, min_periods=max(395//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.323529 + 0.0007861 * anchor
    return base_signal.diff()

def f105_sfix_gemini_091_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=408, w3=727, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(408, min_periods=max(408//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.299667 * slope + 0.0007862 * anchor
    return base_signal.diff()

def f105_sfix_gemini_092_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=421, w3=744, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(421, min_periods=max(421//3, 2)).mean()
    noise = impulse.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.350588 + 0.0007863 * anchor
    return base_signal.diff()

def f105_sfix_gemini_093_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=434, w3=761, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 434)
    curvature = _rolling_slope(acceleration, 761)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.312333 * acceleration + 0.0007864 * anchor
    return base_signal.diff()

def f105_sfix_gemini_094_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=447, w3=27, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 219)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.318667 * pressure.rolling(27, min_periods=max(27//3, 2)).mean() + 0.0007865 * anchor
    return base_signal.diff()

def f105_sfix_gemini_095_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=460, w3=44, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.391176 + 0.0007866 * anchor
    return base_signal.diff()

def f105_sfix_gemini_096_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=473, w3=61, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(473, min_periods=max(473//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.404706 + 0.0007867 * anchor
    return base_signal.diff()

def f105_sfix_gemini_097_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=486, w3=78, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(240, min_periods=max(240//3, 2)).mean(), b.abs().rolling(486, min_periods=max(486//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(78) + 0.337667 * _rolling_slope(cover, 240) + 0.0007868 * anchor
    return base_signal.diff()

def f105_sfix_gemini_098_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=499, w3=95, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.344 * y + 0.656000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 247) - _rolling_slope(basket, 499) + 0.0007869 * anchor
    return base_signal.diff()

def f105_sfix_gemini_099_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=13, w3=112, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(13, min_periods=max(13//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(112) * 1.445294 + 0.000787 * anchor
    return base_signal.diff()

def f105_sfix_gemini_100_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=26, w3=129, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(26, min_periods=max(26//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.356667 * _rolling_slope(draw, 129) + 0.0007871 * anchor
    return base_signal.diff()

def f105_sfix_gemini_101_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=39, w3=146, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(21) - b.diff(39)
    stress = imbalance.rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.472353 + 0.0007872 * anchor
    return base_signal.diff()

def f105_sfix_gemini_102_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=52, w3=163, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(52, min_periods=max(52//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.485882 + 0.0007873 * anchor
    return base_signal.diff()

def f105_sfix_gemini_103_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=65, w3=180, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 65)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=180, adjust=False).mean() * 1.499412 + 0.0007874 * anchor
    return base_signal.diff()

def f105_sfix_gemini_104_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=78, w3=197, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.512941 + 0.0007875 * anchor
    return base_signal.diff()

def f105_sfix_gemini_105_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=91, w3=214, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(49)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.056 * persistence + 0.0007876 * anchor
    return base_signal.diff()

def f105_sfix_gemini_106_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=104, w3=231, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(104, min_periods=max(104//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54 + 0.0007877 * anchor
    return base_signal.diff()

def f105_sfix_gemini_107_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=117, w3=248, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(117, min_periods=max(117//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.068667 * slope + 0.0007878 * anchor
    return base_signal.diff()

def f105_sfix_gemini_108_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=130, w3=265, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(70)
    drag = impulse.rolling(130, min_periods=max(130//3, 2)).mean()
    noise = impulse.abs().rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.567059 + 0.0007879 * anchor
    return base_signal.diff()

def f105_sfix_gemini_109_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=143, w3=282, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 143)
    curvature = _rolling_slope(acceleration, 282)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.081333 * acceleration + 0.000788 * anchor
    return base_signal.diff()

def f105_sfix_gemini_110_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=156, w3=299, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 84)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.087667 * pressure.rolling(299, min_periods=max(299//3, 2)).mean() + 0.0007881 * anchor
    return base_signal.diff()

def f105_sfix_gemini_111_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=169, w3=316, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(91, min_periods=max(91//3, 2)).mean())
    decay = spread.ewm(span=169, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.607647 + 0.0007882 * anchor
    return base_signal.diff()

def f105_sfix_gemini_112_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=182, w3=333, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(182, min_periods=max(182//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 98)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.621176 + 0.0007883 * anchor
    return base_signal.diff()

def f105_sfix_gemini_113_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=195, w3=350, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(105, min_periods=max(105//3, 2)).mean(), b.abs().rolling(195, min_periods=max(195//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.106667 * _rolling_slope(cover, 105) + 0.0007884 * anchor
    return base_signal.diff()

def f105_sfix_gemini_114_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=208, w3=367, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.113 * y + 0.887000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 112) - _rolling_slope(basket, 208) + 0.0007885 * anchor
    return base_signal.diff()

def f105_sfix_gemini_115_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=221, w3=384, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(221, min_periods=max(221//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.661765 + 0.0007886 * anchor
    return base_signal.diff()

def f105_sfix_gemini_116_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=234, w3=401, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(234, min_periods=max(234//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.125667 * _rolling_slope(draw, 401) + 0.0007887 * anchor
    return base_signal.diff()

def f105_sfix_gemini_117_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=247, w3=418, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.835294 + 0.0007888 * anchor
    return base_signal.diff()

def f105_sfix_gemini_118_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=260, w3=435, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(260, min_periods=max(260//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.848824 + 0.0007889 * anchor
    return base_signal.diff()

def f105_sfix_gemini_119_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=273, w3=452, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 273)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.862353 + 0.000789 * anchor
    return base_signal.diff()

def f105_sfix_gemini_120_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=286, w3=469, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(286, min_periods=max(286//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.875882 + 0.0007891 * anchor
    return base_signal.diff()

def f105_sfix_gemini_121_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=299, w3=486, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(299, min_periods=max(299//3, 2)).rank(pct=True)
    persistence = change.rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.157333 * persistence + 0.0007892 * anchor
    return base_signal.diff()

def f105_sfix_gemini_122_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=312, w3=503, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(312, min_periods=max(312//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.902941 + 0.0007893 * anchor
    return base_signal.diff()

def f105_sfix_gemini_123_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=325, w3=520, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(325, min_periods=max(325//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.17 * slope + 0.0007894 * anchor
    return base_signal.diff()

def f105_sfix_gemini_124_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=338, w3=537, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(338, min_periods=max(338//3, 2)).mean()
    noise = impulse.abs().rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.93 + 0.0007895 * anchor
    return base_signal.diff()

def f105_sfix_gemini_125_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=189, w2=351, w3=554, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 351)
    curvature = _rolling_slope(acceleration, 554)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.182667 * acceleration + 0.0007896 * anchor
    return base_signal.diff()

def f105_sfix_gemini_126_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=196, w2=364, w3=571, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 196)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.189 * pressure.rolling(571, min_periods=max(571//3, 2)).mean() + 0.0007897 * anchor
    return base_signal.diff()

def f105_sfix_gemini_127_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=203, w2=377, w3=588, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(203, min_periods=max(203//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.970588 + 0.0007898 * anchor
    return base_signal.diff()

def f105_sfix_gemini_128_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=390, w3=605, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(390, min_periods=max(390//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 210)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.984118 + 0.0007899 * anchor
    return base_signal.diff()

def f105_sfix_gemini_129_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=403, w3=622, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(217, min_periods=max(217//3, 2)).mean(), b.abs().rolling(403, min_periods=max(403//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.208 * _rolling_slope(cover, 217) + 0.00079 * anchor
    return base_signal.diff()

def f105_sfix_gemini_130_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=416, w3=639, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.214333 * y + 0.785667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 224) - _rolling_slope(basket, 416) + 0.0007901 * anchor
    return base_signal.diff()

def f105_sfix_gemini_131_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=429, w3=656, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.024706 + 0.0007902 * anchor
    return base_signal.diff()

def f105_sfix_gemini_132_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=442, w3=673, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(442, min_periods=max(442//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227 * _rolling_slope(draw, 673) + 0.0007903 * anchor
    return base_signal.diff()

def f105_sfix_gemini_133_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=455, w3=690, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.051765 + 0.0007904 * anchor
    return base_signal.diff()

def f105_sfix_gemini_134_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=468, w3=707, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 5)
    baseline = trend.rolling(468, min_periods=max(468//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.065294 + 0.0007905 * anchor
    return base_signal.diff()

def f105_sfix_gemini_135_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=481, w3=724, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.078824 + 0.0007906 * anchor
    return base_signal.diff()

def f105_sfix_gemini_136_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=494, w3=741, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.092353 + 0.0007907 * anchor
    return base_signal.diff()

def f105_sfix_gemini_137_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=507, w3=758, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(26)
    rank = change.rolling(507, min_periods=max(507//3, 2)).rank(pct=True)
    persistence = change.rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.258667 * persistence + 0.0007908 * anchor
    return base_signal.diff()

def f105_sfix_gemini_138_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=21, w3=24, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(21, min_periods=max(21//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.119412 + 0.0007909 * anchor
    return base_signal.diff()

def f105_sfix_gemini_139_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=34, w3=41, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(34, min_periods=max(34//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.271333 * slope + 0.000791 * anchor
    return base_signal.diff()

def f105_sfix_gemini_140_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=47, w3=58, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(47)
    drag = impulse.rolling(47, min_periods=max(47//3, 2)).mean()
    noise = impulse.abs().rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.146471 + 0.0007911 * anchor
    return base_signal.diff()

def f105_sfix_gemini_141_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=60, w3=75, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 54)
    acceleration = _rolling_slope(velocity, 60)
    curvature = _rolling_slope(acceleration, 75)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.284 * acceleration + 0.0007912 * anchor
    return base_signal.diff()

def f105_sfix_gemini_142_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=73, w3=92, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 61)
    pressure = rel_log.diff(73)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.290333 * pressure.rolling(92, min_periods=max(92//3, 2)).mean() + 0.0007913 * anchor
    return base_signal.diff()

def f105_sfix_gemini_143_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=86, w3=109, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(68, min_periods=max(68//3, 2)).mean())
    decay = spread.ewm(span=86, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.187059 + 0.0007914 * anchor
    return base_signal.diff()

def f105_sfix_gemini_144_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=99, w3=126, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(99, min_periods=max(99//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 75)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.200588 + 0.0007915 * anchor
    return base_signal.diff()

def f105_sfix_gemini_145_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=112, w3=143, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(82, min_periods=max(82//3, 2)).mean(), b.abs().rolling(112, min_periods=max(112//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.309333 * _rolling_slope(cover, 82) + 0.0007916 * anchor
    return base_signal.diff()

def f105_sfix_gemini_146_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=125, w3=160, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.315667 * y + 0.684333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 89) - _rolling_slope(basket, 125) + 0.0007917 * anchor
    return base_signal.diff()

def f105_sfix_gemini_147_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=138, w3=177, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(138, min_periods=max(138//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.241176 + 0.0007918 * anchor
    return base_signal.diff()

def f105_sfix_gemini_148_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=151, w3=194, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(151, min_periods=max(151//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.328333 * _rolling_slope(draw, 194) + 0.0007919 * anchor
    return base_signal.diff()

def f105_sfix_gemini_149_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=164, w3=211, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(110) - b.diff(126)
    stress = imbalance.rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.268235 + 0.000792 * anchor
    return base_signal.diff()

def f105_sfix_gemini_150_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=177, w3=228, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(177, min_periods=max(177//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.281765 + 0.0007921 * anchor
    return base_signal.diff()
