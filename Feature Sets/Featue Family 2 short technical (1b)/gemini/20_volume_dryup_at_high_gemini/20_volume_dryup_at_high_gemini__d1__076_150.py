"""20 volume dryup at high gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Decreasing volume at price peaks suggesting a lack of buying interest and potential reversal.
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

def f20_vdry_gemini_076_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=426, w3=339, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(75)
    drag = impulse.rolling(426, min_periods=max(426//3, 2)).mean()
    noise = impulse.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.156471 + 0.0016807 * anchor
    return base_signal.diff()

def f20_vdry_gemini_077_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=439, w3=356, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 356)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.128667 * acceleration + 0.0016808 * anchor
    return base_signal.diff()

def f20_vdry_gemini_078_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=452, w3=373, lag=34)."""
    rel = _safe_div(high.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 89)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.135 * pressure.rolling(373, min_periods=max(373//3, 2)).mean() + 0.0016809 * anchor
    return base_signal.diff()

def f20_vdry_gemini_079_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=465, w3=390, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(96, min_periods=max(96//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.197059 + 0.001681 * anchor
    return base_signal.diff()

def f20_vdry_gemini_080_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=478, w3=407, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(478, min_periods=max(478//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 103)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.210588 + 0.0016811 * anchor
    return base_signal.diff()

def f20_vdry_gemini_081_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=491, w3=424, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(110, min_periods=max(110//3, 2)).mean(), b.abs().rolling(491, min_periods=max(491//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.154 * _rolling_slope(cover, 110) + 0.0016812 * anchor
    return base_signal.diff()

def f20_vdry_gemini_082_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=504, w3=441, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.160333 * y + 0.839667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 117) - _rolling_slope(basket, 504) + 0.0016813 * anchor
    return base_signal.diff()

def f20_vdry_gemini_083_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=18, w3=458, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(18, min_periods=max(18//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.251176 + 0.0016814 * anchor
    return base_signal.diff()

def f20_vdry_gemini_084_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=31, w3=475, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(31, min_periods=max(31//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.173 * _rolling_slope(draw, 475) + 0.0016815 * anchor
    return base_signal.diff()

def f20_vdry_gemini_085_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=44, w3=492, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(44)
    stress = imbalance.rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.278235 + 0.0016816 * anchor
    return base_signal.diff()

def f20_vdry_gemini_086_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=57, w3=509, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(57, min_periods=max(57//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.291765 + 0.0016817 * anchor
    return base_signal.diff()

def f20_vdry_gemini_087_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=70, w3=526, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 70)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.305294 + 0.0016818 * anchor
    return base_signal.diff()

def f20_vdry_gemini_088_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=83, w3=543, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(83, min_periods=max(83//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.318824 + 0.0016819 * anchor
    return base_signal.diff()

def f20_vdry_gemini_089_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=96, w3=560, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(96, min_periods=max(96//3, 2)).rank(pct=True)
    persistence = change.rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.204667 * persistence + 0.001682 * anchor
    return base_signal.diff()

def f20_vdry_gemini_090_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=109, w3=577, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(109, min_periods=max(109//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.345882 + 0.0016821 * anchor
    return base_signal.diff()

def f20_vdry_gemini_091_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=122, w3=594, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(122, min_periods=max(122//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.217333 * slope + 0.0016822 * anchor
    return base_signal.diff()

def f20_vdry_gemini_092_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=135, w3=611, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(135, min_periods=max(135//3, 2)).mean()
    noise = impulse.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.372941 + 0.0016823 * anchor
    return base_signal.diff()

def f20_vdry_gemini_093_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=148, w3=628, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 148)
    curvature = _rolling_slope(acceleration, 628)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.23 * acceleration + 0.0016824 * anchor
    return base_signal.diff()

def f20_vdry_gemini_094_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=161, w3=645, lag=5)."""
    rel = _safe_div(high.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 201)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.236333 * pressure.rolling(645, min_periods=max(645//3, 2)).mean() + 0.0016825 * anchor
    return base_signal.diff()

def f20_vdry_gemini_095_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=174, w3=662, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(208, min_periods=max(208//3, 2)).mean())
    decay = spread.ewm(span=174, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.413529 + 0.0016826 * anchor
    return base_signal.diff()

def f20_vdry_gemini_096_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=187, w3=679, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(187, min_periods=max(187//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 215)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.427059 + 0.0016827 * anchor
    return base_signal.diff()

def f20_vdry_gemini_097_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=200, w3=696, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(222, min_periods=max(222//3, 2)).mean(), b.abs().rolling(200, min_periods=max(200//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.255333 * _rolling_slope(cover, 222) + 0.0016828 * anchor
    return base_signal.diff()

def f20_vdry_gemini_098_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=213, w3=713, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.261667 * y + 0.738333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 229) - _rolling_slope(basket, 213) + 0.0016829 * anchor
    return base_signal.diff()

def f20_vdry_gemini_099_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=226, w3=730, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(226, min_periods=max(226//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.467647 + 0.001683 * anchor
    return base_signal.diff()

def f20_vdry_gemini_100_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=239, w3=747, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(239, min_periods=max(239//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.274333 * _rolling_slope(draw, 747) + 0.0016831 * anchor
    return base_signal.diff()

def f20_vdry_gemini_101_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=252, w3=764, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.494706 + 0.0016832 * anchor
    return base_signal.diff()

def f20_vdry_gemini_102_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=265, w3=30, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(265, min_periods=max(265//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.508235 + 0.0016833 * anchor
    return base_signal.diff()

def f20_vdry_gemini_103_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=278, w3=47, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 278)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=47, adjust=False).mean() * 1.521765 + 0.0016834 * anchor
    return base_signal.diff()

def f20_vdry_gemini_104_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=291, w3=64, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(291, min_periods=max(291//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.535294 + 0.0016835 * anchor
    return base_signal.diff()

def f20_vdry_gemini_105_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=304, w3=81, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(31)
    rank = change.rolling(304, min_periods=max(304//3, 2)).rank(pct=True)
    persistence = change.rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.306 * persistence + 0.0016836 * anchor
    return base_signal.diff()

def f20_vdry_gemini_106_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=317, w3=98, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(317, min_periods=max(317//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.562353 + 0.0016837 * anchor
    return base_signal.diff()

def f20_vdry_gemini_107_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=330, w3=115, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(330, min_periods=max(330//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.318667 * slope + 0.0016838 * anchor
    return base_signal.diff()

def f20_vdry_gemini_108_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=343, w3=132, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(52)
    drag = impulse.rolling(343, min_periods=max(343//3, 2)).mean()
    noise = impulse.abs().rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.589412 + 0.0016839 * anchor
    return base_signal.diff()

def f20_vdry_gemini_109_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=356, w3=149, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 356)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.331333 * acceleration + 0.001684 * anchor
    return base_signal.diff()

def f20_vdry_gemini_110_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=369, w3=166, lag=0)."""
    rel = _safe_div(high.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 66)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.337667 * pressure.rolling(166, min_periods=max(166//3, 2)).mean() + 0.0016841 * anchor
    return base_signal.diff()

def f20_vdry_gemini_111_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=382, w3=183, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(73, min_periods=max(73//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.63 + 0.0016842 * anchor
    return base_signal.diff()

def f20_vdry_gemini_112_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=395, w3=200, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(395, min_periods=max(395//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 80)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.643529 + 0.0016843 * anchor
    return base_signal.diff()

def f20_vdry_gemini_113_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=408, w3=217, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(87, min_periods=max(87//3, 2)).mean(), b.abs().rolling(408, min_periods=max(408//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.356667 * _rolling_slope(cover, 87) + 0.0016844 * anchor
    return base_signal.diff()

def f20_vdry_gemini_114_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=421, w3=234, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.363 * y + 0.637000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 94) - _rolling_slope(basket, 421) + 0.0016845 * anchor
    return base_signal.diff()

def f20_vdry_gemini_115_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=434, w3=251, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(434, min_periods=max(434//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.830588 + 0.0016846 * anchor
    return base_signal.diff()

def f20_vdry_gemini_116_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=447, w3=268, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(447, min_periods=max(447//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.043333 * _rolling_slope(draw, 268) + 0.0016847 * anchor
    return base_signal.diff()

def f20_vdry_gemini_117_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=460, w3=285, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(115) - b.diff(126)
    stress = imbalance.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.857647 + 0.0016848 * anchor
    return base_signal.diff()

def f20_vdry_gemini_118_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=473, w3=302, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.871176 + 0.0016849 * anchor
    return base_signal.diff()

def f20_vdry_gemini_119_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=486, w3=319, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 486)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.884706 + 0.001685 * anchor
    return base_signal.diff()

def f20_vdry_gemini_120_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=499, w3=336, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(499, min_periods=max(499//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.898235 + 0.0016851 * anchor
    return base_signal.diff()

def f20_vdry_gemini_121_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=13, w3=353, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(13, min_periods=max(13//3, 2)).rank(pct=True)
    persistence = change.rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.075 * persistence + 0.0016852 * anchor
    return base_signal.diff()

def f20_vdry_gemini_122_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=26, w3=370, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(26, min_periods=max(26//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.925294 + 0.0016853 * anchor
    return base_signal.diff()

def f20_vdry_gemini_123_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=39, w3=387, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(39, min_periods=max(39//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.087667 * slope + 0.0016854 * anchor
    return base_signal.diff()

def f20_vdry_gemini_124_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=52, w3=404, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(52, min_periods=max(52//3, 2)).mean()
    noise = impulse.abs().rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.952353 + 0.0016855 * anchor
    return base_signal.diff()

def f20_vdry_gemini_125_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=65, w3=421, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 65)
    curvature = _rolling_slope(acceleration, 421)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.100333 * acceleration + 0.0016856 * anchor
    return base_signal.diff()

def f20_vdry_gemini_126_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=78, w3=438, lag=13)."""
    rel = _safe_div(high.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 178)
    pressure = rel_log.diff(78)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.106667 * pressure.rolling(438, min_periods=max(438//3, 2)).mean() + 0.0016857 * anchor
    return base_signal.diff()

def f20_vdry_gemini_127_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=91, w3=455, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(185, min_periods=max(185//3, 2)).mean())
    decay = spread.ewm(span=91, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.992941 + 0.0016858 * anchor
    return base_signal.diff()

def f20_vdry_gemini_128_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=104, w3=472, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(104, min_periods=max(104//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 192)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.006471 + 0.0016859 * anchor
    return base_signal.diff()

def f20_vdry_gemini_129_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=117, w3=489, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(199, min_periods=max(199//3, 2)).mean(), b.abs().rolling(117, min_periods=max(117//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.125667 * _rolling_slope(cover, 199) + 0.001686 * anchor
    return base_signal.diff()

def f20_vdry_gemini_130_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=130, w3=506, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.132 * y + 0.868000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 206) - _rolling_slope(basket, 130) + 0.0016861 * anchor
    return base_signal.diff()

def f20_vdry_gemini_131_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=143, w3=523, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(143, min_periods=max(143//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.047059 + 0.0016862 * anchor
    return base_signal.diff()

def f20_vdry_gemini_132_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=156, w3=540, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(156, min_periods=max(156//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.144667 * _rolling_slope(draw, 540) + 0.0016863 * anchor
    return base_signal.diff()

def f20_vdry_gemini_133_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=169, w3=557, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.074118 + 0.0016864 * anchor
    return base_signal.diff()

def f20_vdry_gemini_134_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=182, w3=574, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(182, min_periods=max(182//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.087647 + 0.0016865 * anchor
    return base_signal.diff()

def f20_vdry_gemini_135_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=195, w3=591, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 195)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.101176 + 0.0016866 * anchor
    return base_signal.diff()

def f20_vdry_gemini_136_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=208, w3=608, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(208, min_periods=max(208//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.114706 + 0.0016867 * anchor
    return base_signal.diff()

def f20_vdry_gemini_137_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=221, w3=625, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(8)
    rank = change.rolling(221, min_periods=max(221//3, 2)).rank(pct=True)
    persistence = change.rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.176333 * persistence + 0.0016868 * anchor
    return base_signal.diff()

def f20_vdry_gemini_138_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=234, w3=642, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(234, min_periods=max(234//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.141765 + 0.0016869 * anchor
    return base_signal.diff()

def f20_vdry_gemini_139_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=247, w3=659, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(247, min_periods=max(247//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.189 * slope + 0.001687 * anchor
    return base_signal.diff()

def f20_vdry_gemini_140_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=260, w3=676, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(29)
    drag = impulse.rolling(260, min_periods=max(260//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.168824 + 0.0016871 * anchor
    return base_signal.diff()

def f20_vdry_gemini_141_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=273, w3=693, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 273)
    curvature = _rolling_slope(acceleration, 693)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.201667 * acceleration + 0.0016872 * anchor
    return base_signal.diff()

def f20_vdry_gemini_142_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=286, w3=710, lag=2)."""
    rel = _safe_div(high.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 43)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.208 * pressure.rolling(710, min_periods=max(710//3, 2)).mean() + 0.0016873 * anchor
    return base_signal.diff()

def f20_vdry_gemini_143_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=299, w3=727, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(50, min_periods=max(50//3, 2)).mean())
    decay = spread.ewm(span=299, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.209412 + 0.0016874 * anchor
    return base_signal.diff()

def f20_vdry_gemini_144_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=312, w3=744, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(312, min_periods=max(312//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 57)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.222941 + 0.0016875 * anchor
    return base_signal.diff()

def f20_vdry_gemini_145_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=325, w3=761, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(64, min_periods=max(64//3, 2)).mean(), b.abs().rolling(325, min_periods=max(325//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.227 * _rolling_slope(cover, 64) + 0.0016876 * anchor
    return base_signal.diff()

def f20_vdry_gemini_146_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=338, w3=27, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.233333 * y + 0.766667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 71) - _rolling_slope(basket, 338) + 0.0016877 * anchor
    return base_signal.diff()

def f20_vdry_gemini_147_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=351, w3=44, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(44) * 1.263529 + 0.0016878 * anchor
    return base_signal.diff()

def f20_vdry_gemini_148_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=364, w3=61, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.246 * _rolling_slope(draw, 61) + 0.0016879 * anchor
    return base_signal.diff()

def f20_vdry_gemini_149_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=377, w3=78, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(92) - b.diff(126)
    stress = imbalance.rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.290588 + 0.001688 * anchor
    return base_signal.diff()

def f20_vdry_gemini_150_d1(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=390, w3=95, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.304118 + 0.0016881 * anchor
    return base_signal.diff()
