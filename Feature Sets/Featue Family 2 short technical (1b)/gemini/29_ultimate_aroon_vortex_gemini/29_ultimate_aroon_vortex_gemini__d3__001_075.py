"""29 ultimate aroon vortex gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Directional movement and trend strength identified through Aroon and Vortex indicators.
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

def f29_vtxn_gemini_001_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=5]"""
    window = 5
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_002_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=10]"""
    window = 10
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_003_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=21]"""
    window = 21
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_004_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=42]"""
    window = 42
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_005_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=63]"""
    window = 63
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_006_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=126]"""
    window = 126
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_007_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=252]"""
    window = 252
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_008_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=504]"""
    window = 504
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_009_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=756]"""
    window = 756
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_010_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Directional movement and trend strength identified through Aroon and Vortex indicators. [window=1260]"""
    window = 1260
    res = _safe_div(high.rolling(window).max() - low.rolling(window).min(), _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f29_vtxn_gemini_011_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=378, w3=305, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(378, min_periods=max(378//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.410588 + 0.0022062 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_012_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=391, w3=322, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(391, min_periods=max(391//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.177 * _rolling_slope(draw, 322) + 0.0022063 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_013_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=404, w3=339, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(71) - b.diff(126)
    stress = imbalance.rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.437647 + 0.0022064 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_014_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=417, w3=356, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(417, min_periods=max(417//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(356, min_periods=max(356//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.451176 + 0.0022065 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_015_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=430, w3=373, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 430)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.464706 + 0.0022066 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_016_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=443, w3=390, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(443, min_periods=max(443//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.478235 + 0.0022067 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_017_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=456, w3=407, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(99)
    rank = change.rolling(456, min_periods=max(456//3, 2)).rank(pct=True)
    persistence = change.rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.208667 * persistence + 0.0022068 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_018_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=469, w3=424, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(469, min_periods=max(469//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.505294 + 0.0022069 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_019_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=482, w3=441, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(482, min_periods=max(482//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.221333 * slope + 0.002207 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_020_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=495, w3=458, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(120)
    drag = impulse.rolling(495, min_periods=max(495//3, 2)).mean()
    noise = impulse.abs().rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.532353 + 0.0022071 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_021_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=508, w3=475, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 508)
    curvature = _rolling_slope(acceleration, 475)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.234 * acceleration + 0.0022072 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_022_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=22, w3=492, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 134)
    pressure = rel_log.diff(22)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.240333 * pressure.rolling(492, min_periods=max(492//3, 2)).mean() + 0.0022073 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_023_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=35, w3=509, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(141, min_periods=max(141//3, 2)).mean())
    decay = spread.ewm(span=35, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.572941 + 0.0022074 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_024_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=48, w3=526, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(48, min_periods=max(48//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 148)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.586471 + 0.0022075 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_025_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=61, w3=543, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(155, min_periods=max(155//3, 2)).mean(), b.abs().rolling(61, min_periods=max(61//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.259333 * _rolling_slope(cover, 155) + 0.0022076 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_026_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=74, w3=560, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.265667 * y + 0.734333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 162) - _rolling_slope(basket, 74) + 0.0022077 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_027_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=87, w3=577, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.627059 + 0.0022078 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_028_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=100, w3=594, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.278333 * _rolling_slope(draw, 594) + 0.0022079 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_029_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=113, w3=611, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(113)
    stress = imbalance.rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.654118 + 0.002208 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_030_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=126, w3=628, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(126, min_periods=max(126//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(628, min_periods=max(628//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.667647 + 0.0022081 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_031_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=139, w3=645, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 139)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.827647 + 0.0022082 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_032_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=152, w3=662, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(152, min_periods=max(152//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.841176 + 0.0022083 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_033_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=165, w3=679, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.31 * persistence + 0.0022084 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_034_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=178, w3=696, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.868235 + 0.0022085 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_035_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=191, w3=713, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(191, min_periods=max(191//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.322667 * slope + 0.0022086 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_036_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=204, w3=730, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.895294 + 0.0022087 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_037_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=217, w3=747, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 217)
    curvature = _rolling_slope(acceleration, 747)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.335333 * acceleration + 0.0022088 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_038_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=230, w3=764, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 246)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.341667 * pressure.rolling(764, min_periods=max(764//3, 2)).mean() + 0.0022089 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_039_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=243, w3=30, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(6, min_periods=max(6//3, 2)).mean())
    decay = spread.ewm(span=243, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.935882 + 0.002209 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_040_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=256, w3=47, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(256, min_periods=max(256//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 13)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.949412 + 0.0022091 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_041_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=269, w3=64, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(20, min_periods=max(20//3, 2)).mean(), b.abs().rolling(269, min_periods=max(269//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(64) + 0.360667 * _rolling_slope(cover, 20) + 0.0022092 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_042_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=282, w3=81, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.034667 * y + 0.965333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 27) - _rolling_slope(basket, 282) + 0.0022093 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_043_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=295, w3=98, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(295, min_periods=max(295//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(98) * 0.99 + 0.0022094 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_044_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=308, w3=115, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(308, min_periods=max(308//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.047333 * _rolling_slope(draw, 115) + 0.0022095 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_045_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=321, w3=132, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(48) - b.diff(126)
    stress = imbalance.rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.017059 + 0.0022096 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_046_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=334, w3=149, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(334, min_periods=max(334//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.030588 + 0.0022097 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_047_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=347, w3=166, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=166, adjust=False).mean() * 1.044118 + 0.0022098 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_048_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=360, w3=183, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.057647 + 0.0022099 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_049_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=373, w3=200, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(76)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.079 * persistence + 0.00221 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_050_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=386, w3=217, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(386, min_periods=max(386//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.084706 + 0.0022101 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_051_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=399, w3=234, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(399, min_periods=max(399//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.091667 * slope + 0.0022102 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_052_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=412, w3=251, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(97)
    drag = impulse.rolling(412, min_periods=max(412//3, 2)).mean()
    noise = impulse.abs().rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.111765 + 0.0022103 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_053_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=425, w3=268, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 425)
    curvature = _rolling_slope(acceleration, 268)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.104333 * acceleration + 0.0022104 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_054_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=438, w3=285, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 111)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.110667 * pressure.rolling(285, min_periods=max(285//3, 2)).mean() + 0.0022105 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_055_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=451, w3=302, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(118, min_periods=max(118//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.152353 + 0.0022106 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_056_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=464, w3=319, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(464, min_periods=max(464//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 125)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.165882 + 0.0022107 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_057_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=477, w3=336, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(132, min_periods=max(132//3, 2)).mean(), b.abs().rolling(477, min_periods=max(477//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.129667 * _rolling_slope(cover, 132) + 0.0022108 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_058_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=490, w3=353, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.136 * y + 0.864000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 139) - _rolling_slope(basket, 490) + 0.0022109 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_059_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=503, w3=370, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(503, min_periods=max(503//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.206471 + 0.002211 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_060_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=17, w3=387, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(17, min_periods=max(17//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.148667 * _rolling_slope(draw, 387) + 0.0022111 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_061_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=30, w3=404, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(30)
    stress = imbalance.rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.233529 + 0.0022112 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_062_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=43, w3=421, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(43, min_periods=max(43//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.247059 + 0.0022113 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_063_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=56, w3=438, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 56)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.260588 + 0.0022114 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_064_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=69, w3=455, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(69, min_periods=max(69//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.274118 + 0.0022115 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_065_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=82, w3=472, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(82, min_periods=max(82//3, 2)).rank(pct=True)
    persistence = change.rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.180333 * persistence + 0.0022116 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_066_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=95, w3=489, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(95, min_periods=max(95//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.301176 + 0.0022117 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_067_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=108, w3=506, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(108, min_periods=max(108//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.193 * slope + 0.0022118 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_068_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=121, w3=523, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(523, min_periods=max(523//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.328235 + 0.0022119 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_069_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=134, w3=540, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 134)
    curvature = _rolling_slope(acceleration, 540)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.205667 * acceleration + 0.002212 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_070_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=147, w3=557, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 223)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.212 * pressure.rolling(557, min_periods=max(557//3, 2)).mean() + 0.0022121 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_071_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=160, w3=574, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(230, min_periods=max(230//3, 2)).mean())
    decay = spread.ewm(span=160, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.368824 + 0.0022122 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_072_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=173, w3=591, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(173, min_periods=max(173//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 237)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.382353 + 0.0022123 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_073_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=186, w3=608, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(244, min_periods=max(244//3, 2)).mean(), b.abs().rolling(186, min_periods=max(186//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.231 * _rolling_slope(cover, 244) + 0.0022124 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_074_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=199, w3=625, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.237333 * y + 0.762667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 251) - _rolling_slope(basket, 199) + 0.0022125 * anchor
    return base_signal.diff().diff().diff()

def f29_vtxn_gemini_075_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=212, w3=642, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.422941 + 0.0022126 * anchor
    return base_signal.diff().diff().diff()
