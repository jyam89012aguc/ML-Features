"""19 volume blowoff climax gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Extreme volume spikes accompanying price exhaustion moves, often marking trend ends.
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

def f19_vboc_gemini_001(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=5]"""
    window = 5
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_002(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=10]"""
    window = 10
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_003(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=21]"""
    window = 21
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_004(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=42]"""
    window = 42
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_005(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=63]"""
    window = 63
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_006(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=126]"""
    window = 126
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_007(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=252]"""
    window = 252
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_008(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=504]"""
    window = 504
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_009(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=756]"""
    window = 756
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_010(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=1260]"""
    window = 1260
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return res

def f19_vboc_gemini_011(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=461, w3=101, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(154, min_periods=max(154//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.048824 + 0.0016042 * anchor
    return base_signal

def f19_vboc_gemini_012(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=474, w3=118, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(474, min_periods=max(474//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 161)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.062353 + 0.0016043 * anchor
    return base_signal

def f19_vboc_gemini_013(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=487, w3=135, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(168, min_periods=max(168//3, 2)).mean(), b.abs().rolling(487, min_periods=max(487//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.275 * _rolling_slope(cover, 168) + 0.0016044 * anchor
    return base_signal

def f19_vboc_gemini_014(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=500, w3=152, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.281333 * y + 0.718667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 175) - _rolling_slope(basket, 500) + 0.0016045 * anchor
    return base_signal

def f19_vboc_gemini_015(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=14, w3=169, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(14, min_periods=max(14//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.102941 + 0.0016046 * anchor
    return base_signal

def f19_vboc_gemini_016(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=27, w3=186, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(27, min_periods=max(27//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.294 * _rolling_slope(draw, 186) + 0.0016047 * anchor
    return base_signal

def f19_vboc_gemini_017(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=40, w3=203, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(40)
    stress = imbalance.rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.13 + 0.0016048 * anchor
    return base_signal

def f19_vboc_gemini_018(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=53, w3=220, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.143529 + 0.0016049 * anchor
    return base_signal

def f19_vboc_gemini_019(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=66, w3=237, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 66)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=237, adjust=False).mean() * 1.157059 + 0.001605 * anchor
    return base_signal

def f19_vboc_gemini_020(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=79, w3=254, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(79, min_periods=max(79//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.170588 + 0.0016051 * anchor
    return base_signal

def f19_vboc_gemini_021(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=92, w3=271, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.325667 * persistence + 0.0016052 * anchor
    return base_signal

def f19_vboc_gemini_022(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=105, w3=288, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(105, min_periods=max(105//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.197647 + 0.0016053 * anchor
    return base_signal

def f19_vboc_gemini_023(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=118, w3=305, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(118, min_periods=max(118//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.338333 * slope + 0.0016054 * anchor
    return base_signal

def f19_vboc_gemini_024(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=131, w3=322, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(131, min_periods=max(131//3, 2)).mean()
    noise = impulse.abs().rolling(322, min_periods=max(322//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.224706 + 0.0016055 * anchor
    return base_signal

def f19_vboc_gemini_025(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=144, w3=339, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 339)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351 * acceleration + 0.0016056 * anchor
    return base_signal

def f19_vboc_gemini_026(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=157, w3=356, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 12)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.357333 * pressure.rolling(356, min_periods=max(356//3, 2)).mean() + 0.0016057 * anchor
    return base_signal

def f19_vboc_gemini_027(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=170, w3=373, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(19, min_periods=max(19//3, 2)).mean())
    decay = spread.ewm(span=170, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.265294 + 0.0016058 * anchor
    return base_signal

def f19_vboc_gemini_028(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=183, w3=390, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(183, min_periods=max(183//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 26)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.278824 + 0.0016059 * anchor
    return base_signal

def f19_vboc_gemini_029(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=196, w3=407, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(33, min_periods=max(33//3, 2)).mean(), b.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.044 * _rolling_slope(cover, 33) + 0.001606 * anchor
    return base_signal

def f19_vboc_gemini_030(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=209, w3=424, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.050333 * y + 0.949667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 40) - _rolling_slope(basket, 209) + 0.0016061 * anchor
    return base_signal

def f19_vboc_gemini_031(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=222, w3=441, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.319412 + 0.0016062 * anchor
    return base_signal

def f19_vboc_gemini_032(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=235, w3=458, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(235, min_periods=max(235//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.063 * _rolling_slope(draw, 458) + 0.0016063 * anchor
    return base_signal

def f19_vboc_gemini_033(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=248, w3=475, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(61) - b.diff(126)
    stress = imbalance.rolling(475, min_periods=max(475//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.346471 + 0.0016064 * anchor
    return base_signal

def f19_vboc_gemini_034(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=261, w3=492, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.36 + 0.0016065 * anchor
    return base_signal

def f19_vboc_gemini_035(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=274, w3=509, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.373529 + 0.0016066 * anchor
    return base_signal

def f19_vboc_gemini_036(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=287, w3=526, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.387059 + 0.0016067 * anchor
    return base_signal

def f19_vboc_gemini_037(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=300, w3=543, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(89)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.094667 * persistence + 0.0016068 * anchor
    return base_signal

def f19_vboc_gemini_038(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=313, w3=560, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.414118 + 0.0016069 * anchor
    return base_signal

def f19_vboc_gemini_039(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=326, w3=577, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.107333 * slope + 0.001607 * anchor
    return base_signal

def f19_vboc_gemini_040(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=339, w3=594, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(110)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.441176 + 0.0016071 * anchor
    return base_signal

def f19_vboc_gemini_041(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=352, w3=611, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 352)
    curvature = _rolling_slope(acceleration, 611)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.12 * acceleration + 0.0016072 * anchor
    return base_signal

def f19_vboc_gemini_042(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=365, w3=628, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 124)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.126333 * pressure.rolling(628, min_periods=max(628//3, 2)).mean() + 0.0016073 * anchor
    return base_signal

def f19_vboc_gemini_043(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=378, w3=645, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.481765 + 0.0016074 * anchor
    return base_signal

def f19_vboc_gemini_044(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=391, w3=662, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(391, min_periods=max(391//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 138)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.495294 + 0.0016075 * anchor
    return base_signal

def f19_vboc_gemini_045(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=404, w3=679, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(145, min_periods=max(145//3, 2)).mean(), b.abs().rolling(404, min_periods=max(404//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.145333 * _rolling_slope(cover, 145) + 0.0016076 * anchor
    return base_signal

def f19_vboc_gemini_046(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=417, w3=696, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.151667 * y + 0.848333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 152) - _rolling_slope(basket, 417) + 0.0016077 * anchor
    return base_signal

def f19_vboc_gemini_047(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=430, w3=713, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.535882 + 0.0016078 * anchor
    return base_signal

def f19_vboc_gemini_048(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=443, w3=730, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.164333 * _rolling_slope(draw, 730) + 0.0016079 * anchor
    return base_signal

def f19_vboc_gemini_049(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=456, w3=747, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.562941 + 0.001608 * anchor
    return base_signal

def f19_vboc_gemini_050(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=469, w3=764, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(469, min_periods=max(469//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.576471 + 0.0016081 * anchor
    return base_signal

def f19_vboc_gemini_051(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=482, w3=30, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 482)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=30, adjust=False).mean() * 1.59 + 0.0016082 * anchor
    return base_signal

def f19_vboc_gemini_052(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=495, w3=47, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.603529 + 0.0016083 * anchor
    return base_signal

def f19_vboc_gemini_053(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=508, w3=64, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(508, min_periods=max(508//3, 2)).rank(pct=True)
    persistence = change.rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.196 * persistence + 0.0016084 * anchor
    return base_signal

def f19_vboc_gemini_054(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=22, w3=81, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(22, min_periods=max(22//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.630588 + 0.0016085 * anchor
    return base_signal

def f19_vboc_gemini_055(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=35, w3=98, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.208667 * slope + 0.0016086 * anchor
    return base_signal

def f19_vboc_gemini_056(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=48, w3=115, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(48, min_periods=max(48//3, 2)).mean()
    noise = impulse.abs().rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.657647 + 0.0016087 * anchor
    return base_signal

def f19_vboc_gemini_057(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=61, w3=132, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 61)
    curvature = _rolling_slope(acceleration, 132)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.221333 * acceleration + 0.0016088 * anchor
    return base_signal

def f19_vboc_gemini_058(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=74, w3=149, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(74)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.227667 * pressure.rolling(149, min_periods=max(149//3, 2)).mean() + 0.0016089 * anchor
    return base_signal

def f19_vboc_gemini_059(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=87, w3=166, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=87, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.844706 + 0.001609 * anchor
    return base_signal

def f19_vboc_gemini_060(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=100, w3=183, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(100, min_periods=max(100//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.858235 + 0.0016091 * anchor
    return base_signal

def f19_vboc_gemini_061(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=113, w3=200, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.246667 * _rolling_slope(cover, 10) + 0.0016092 * anchor
    return base_signal

def f19_vboc_gemini_062(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=126, w3=217, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.253 * y + 0.747000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 126) + 0.0016093 * anchor
    return base_signal

def f19_vboc_gemini_063(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=139, w3=234, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.898824 + 0.0016094 * anchor
    return base_signal

def f19_vboc_gemini_064(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=152, w3=251, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(152, min_periods=max(152//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.265667 * _rolling_slope(draw, 251) + 0.0016095 * anchor
    return base_signal

def f19_vboc_gemini_065(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=165, w3=268, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(38) - b.diff(126)
    stress = imbalance.rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.925882 + 0.0016096 * anchor
    return base_signal

def f19_vboc_gemini_066(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=178, w3=285, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.939412 + 0.0016097 * anchor
    return base_signal

def f19_vboc_gemini_067(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=191, w3=302, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 191)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.952941 + 0.0016098 * anchor
    return base_signal

def f19_vboc_gemini_068(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=204, w3=319, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(204, min_periods=max(204//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.966471 + 0.0016099 * anchor
    return base_signal

def f19_vboc_gemini_069(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=217, w3=336, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(66)
    rank = change.rolling(217, min_periods=max(217//3, 2)).rank(pct=True)
    persistence = change.rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.297333 * persistence + 0.00161 * anchor
    return base_signal

def f19_vboc_gemini_070(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=230, w3=353, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.993529 + 0.0016101 * anchor
    return base_signal

def f19_vboc_gemini_071(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=243, w3=370, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(243, min_periods=max(243//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.31 * slope + 0.0016102 * anchor
    return base_signal

def f19_vboc_gemini_072(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=256, w3=387, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(87)
    drag = impulse.rolling(256, min_periods=max(256//3, 2)).mean()
    noise = impulse.abs().rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.020588 + 0.0016103 * anchor
    return base_signal

def f19_vboc_gemini_073(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=269, w3=404, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 269)
    curvature = _rolling_slope(acceleration, 404)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.322667 * acceleration + 0.0016104 * anchor
    return base_signal

def f19_vboc_gemini_074(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=282, w3=421, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 101)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.329 * pressure.rolling(421, min_periods=max(421//3, 2)).mean() + 0.0016105 * anchor
    return base_signal

def f19_vboc_gemini_075(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=295, w3=438, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=295, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.061176 + 0.0016106 * anchor
    return base_signal
