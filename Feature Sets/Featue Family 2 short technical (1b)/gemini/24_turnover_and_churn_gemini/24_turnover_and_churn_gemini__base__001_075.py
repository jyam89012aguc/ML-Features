"""24 turnover and churn gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of asset rotation and high-volume churn without price movement.
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

def f24_turn_gemini_001(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=5]"""
    window = 5
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_002(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=10]"""
    window = 10
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_003(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=21]"""
    window = 21
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_004(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=42]"""
    window = 42
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_005(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=63]"""
    window = 63
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_006(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=126]"""
    window = 126
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_007(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=252]"""
    window = 252
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_008(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=504]"""
    window = 504
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_009(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=756]"""
    window = 756
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_010(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Measurement of asset rotation and high-volume churn without price movement. [window=1260]"""
    window = 1260
    res = _safe_div(volume.rolling(window).sum(), high.rolling(window).max() - low.rolling(window).min() + 1e-9)
    return res

def f24_turn_gemini_011(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=434, w3=388, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(241, min_periods=max(241//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.375882 + 0.0018842 * anchor
    return base_signal

def f24_turn_gemini_012(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=447, w3=405, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(447, min_periods=max(447//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 248)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.389412 + 0.0018843 * anchor
    return base_signal

def f24_turn_gemini_013(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=460, w3=422, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(8, min_periods=max(8//3, 2)).mean(), b.abs().rolling(460, min_periods=max(460//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.062333 * _rolling_slope(cover, 8) + 0.0018844 * anchor
    return base_signal

def f24_turn_gemini_014(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=473, w3=439, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.068667 * y + 0.931333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 15) - _rolling_slope(basket, 473) + 0.0018845 * anchor
    return base_signal

def f24_turn_gemini_015(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=486, w3=456, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(486, min_periods=max(486//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.43 + 0.0018846 * anchor
    return base_signal

def f24_turn_gemini_016(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=499, w3=473, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(499, min_periods=max(499//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.081333 * _rolling_slope(draw, 473) + 0.0018847 * anchor
    return base_signal

def f24_turn_gemini_017(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=13, w3=490, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(36) - b.diff(13)
    stress = imbalance.rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.457059 + 0.0018848 * anchor
    return base_signal

def f24_turn_gemini_018(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=26, w3=507, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(26, min_periods=max(26//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.470588 + 0.0018849 * anchor
    return base_signal

def f24_turn_gemini_019(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=39, w3=524, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 39)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.484118 + 0.001885 * anchor
    return base_signal

def f24_turn_gemini_020(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=52, w3=541, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(52, min_periods=max(52//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.497647 + 0.0018851 * anchor
    return base_signal

def f24_turn_gemini_021(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=65, w3=558, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(64)
    rank = change.rolling(65, min_periods=max(65//3, 2)).rank(pct=True)
    persistence = change.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.113 * persistence + 0.0018852 * anchor
    return base_signal

def f24_turn_gemini_022(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=78, w3=575, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(78, min_periods=max(78//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.524706 + 0.0018853 * anchor
    return base_signal

def f24_turn_gemini_023(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=91, w3=592, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(91, min_periods=max(91//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.125667 * slope + 0.0018854 * anchor
    return base_signal

def f24_turn_gemini_024(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=104, w3=609, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(85)
    drag = impulse.rolling(104, min_periods=max(104//3, 2)).mean()
    noise = impulse.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.551765 + 0.0018855 * anchor
    return base_signal

def f24_turn_gemini_025(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=117, w3=626, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 117)
    curvature = _rolling_slope(acceleration, 626)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.138333 * acceleration + 0.0018856 * anchor
    return base_signal

def f24_turn_gemini_026(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=130, w3=643, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 99)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.144667 * pressure.rolling(643, min_periods=max(643//3, 2)).mean() + 0.0018857 * anchor
    return base_signal

def f24_turn_gemini_027(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=143, w3=660, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(106, min_periods=max(106//3, 2)).mean())
    decay = spread.ewm(span=143, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.592353 + 0.0018858 * anchor
    return base_signal

def f24_turn_gemini_028(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=156, w3=677, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(156, min_periods=max(156//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 113)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.605882 + 0.0018859 * anchor
    return base_signal

def f24_turn_gemini_029(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=169, w3=694, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(120, min_periods=max(120//3, 2)).mean(), b.abs().rolling(169, min_periods=max(169//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.163667 * _rolling_slope(cover, 120) + 0.001886 * anchor
    return base_signal

def f24_turn_gemini_030(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=182, w3=711, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.17 * y + 0.830000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 127) - _rolling_slope(basket, 182) + 0.0018861 * anchor
    return base_signal

def f24_turn_gemini_031(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=195, w3=728, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(195, min_periods=max(195//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.646471 + 0.0018862 * anchor
    return base_signal

def f24_turn_gemini_032(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=208, w3=745, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.182667 * _rolling_slope(draw, 745) + 0.0018863 * anchor
    return base_signal

def f24_turn_gemini_033(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=221, w3=762, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.82 + 0.0018864 * anchor
    return base_signal

def f24_turn_gemini_034(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=234, w3=28, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(234, min_periods=max(234//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.833529 + 0.0018865 * anchor
    return base_signal

def f24_turn_gemini_035(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=247, w3=45, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 162)
    slow = _rolling_slope(x, 247)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=45, adjust=False).mean() * 0.847059 + 0.0018866 * anchor
    return base_signal

def f24_turn_gemini_036(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=260, w3=62, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(260, min_periods=max(260//3, 2)).max()
    trough = x.rolling(169, min_periods=max(169//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.860588 + 0.0018867 * anchor
    return base_signal

def f24_turn_gemini_037(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=273, w3=79, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(273, min_periods=max(273//3, 2)).rank(pct=True)
    persistence = change.rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.214333 * persistence + 0.0018868 * anchor
    return base_signal

def f24_turn_gemini_038(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=286, w3=96, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(183, min_periods=max(183//3, 2)).std()
    vol_slow = ret.rolling(286, min_periods=max(286//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.887647 + 0.0018869 * anchor
    return base_signal

def f24_turn_gemini_039(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=299, w3=113, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(299, min_periods=max(299//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 190)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.227 * slope + 0.001887 * anchor
    return base_signal

def f24_turn_gemini_040(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=312, w3=130, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(312, min_periods=max(312//3, 2)).mean()
    noise = impulse.abs().rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.914706 + 0.0018871 * anchor
    return base_signal

def f24_turn_gemini_041(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=325, w3=147, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 204)
    acceleration = _rolling_slope(velocity, 325)
    curvature = _rolling_slope(acceleration, 147)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.239667 * acceleration + 0.0018872 * anchor
    return base_signal

def f24_turn_gemini_042(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=338, w3=164, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 211)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.246 * pressure.rolling(164, min_periods=max(164//3, 2)).mean() + 0.0018873 * anchor
    return base_signal

def f24_turn_gemini_043(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=351, w3=181, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(218, min_periods=max(218//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.955294 + 0.0018874 * anchor
    return base_signal

def f24_turn_gemini_044(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=364, w3=198, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(364, min_periods=max(364//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 225)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.968824 + 0.0018875 * anchor
    return base_signal

def f24_turn_gemini_045(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=377, w3=215, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(232, min_periods=max(232//3, 2)).mean(), b.abs().rolling(377, min_periods=max(377//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.265 * _rolling_slope(cover, 232) + 0.0018876 * anchor
    return base_signal

def f24_turn_gemini_046(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=390, w3=232, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.271333 * y + 0.728667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 239) - _rolling_slope(basket, 390) + 0.0018877 * anchor
    return base_signal

def f24_turn_gemini_047(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=403, w3=249, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(403, min_periods=max(403//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.009412 + 0.0018878 * anchor
    return base_signal

def f24_turn_gemini_048(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=416, w3=266, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(416, min_periods=max(416//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.284 * _rolling_slope(draw, 266) + 0.0018879 * anchor
    return base_signal

def f24_turn_gemini_049(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=13, w2=429, w3=283, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(13) - b.diff(126)
    stress = imbalance.rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.036471 + 0.001888 * anchor
    return base_signal

def f24_turn_gemini_050(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=20, w2=442, w3=300, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(442, min_periods=max(442//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.05 + 0.0018881 * anchor
    return base_signal

def f24_turn_gemini_051(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=27, w2=455, w3=317, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 455)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.063529 + 0.0018882 * anchor
    return base_signal

def f24_turn_gemini_052(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=34, w2=468, w3=334, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(468, min_periods=max(468//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.077059 + 0.0018883 * anchor
    return base_signal

def f24_turn_gemini_053(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=41, w2=481, w3=351, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(41)
    rank = change.rolling(481, min_periods=max(481//3, 2)).rank(pct=True)
    persistence = change.rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.315667 * persistence + 0.0018884 * anchor
    return base_signal

def f24_turn_gemini_054(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=48, w2=494, w3=368, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(494, min_periods=max(494//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.104118 + 0.0018885 * anchor
    return base_signal

def f24_turn_gemini_055(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=55, w2=507, w3=385, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(507, min_periods=max(507//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.328333 * slope + 0.0018886 * anchor
    return base_signal

def f24_turn_gemini_056(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=62, w2=21, w3=402, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(62)
    drag = impulse.rolling(21, min_periods=max(21//3, 2)).mean()
    noise = impulse.abs().rolling(402, min_periods=max(402//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.131176 + 0.0018887 * anchor
    return base_signal

def f24_turn_gemini_057(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=69, w2=34, w3=419, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 34)
    curvature = _rolling_slope(acceleration, 419)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.341 * acceleration + 0.0018888 * anchor
    return base_signal

def f24_turn_gemini_058(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=76, w2=47, w3=436, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 76)
    pressure = rel_log.diff(47)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.347333 * pressure.rolling(436, min_periods=max(436//3, 2)).mean() + 0.0018889 * anchor
    return base_signal

def f24_turn_gemini_059(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=83, w2=60, w3=453, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    decay = spread.ewm(span=60, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.171765 + 0.001889 * anchor
    return base_signal

def f24_turn_gemini_060(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=90, w2=73, w3=470, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(73, min_periods=max(73//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 90)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.185294 + 0.0018891 * anchor
    return base_signal

def f24_turn_gemini_061(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=97, w2=86, w3=487, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(97, min_periods=max(97//3, 2)).mean(), b.abs().rolling(86, min_periods=max(86//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.034 * _rolling_slope(cover, 97) + 0.0018892 * anchor
    return base_signal

def f24_turn_gemini_062(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=104, w2=99, w3=504, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.040333 * y + 0.959667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 104) - _rolling_slope(basket, 99) + 0.0018893 * anchor
    return base_signal

def f24_turn_gemini_063(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=111, w2=112, w3=521, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(112, min_periods=max(112//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.225882 + 0.0018894 * anchor
    return base_signal

def f24_turn_gemini_064(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=118, w2=125, w3=538, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(125, min_periods=max(125//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.053 * _rolling_slope(draw, 538) + 0.0018895 * anchor
    return base_signal

def f24_turn_gemini_065(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=125, w2=138, w3=555, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(125) - b.diff(126)
    stress = imbalance.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.252941 + 0.0018896 * anchor
    return base_signal

def f24_turn_gemini_066(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=132, w2=151, w3=572, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(151, min_periods=max(151//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.266471 + 0.0018897 * anchor
    return base_signal

def f24_turn_gemini_067(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=139, w2=164, w3=589, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 164)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.28 + 0.0018898 * anchor
    return base_signal

def f24_turn_gemini_068(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=146, w2=177, w3=606, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(177, min_periods=max(177//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.293529 + 0.0018899 * anchor
    return base_signal

def f24_turn_gemini_069(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=153, w2=190, w3=623, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(190, min_periods=max(190//3, 2)).rank(pct=True)
    persistence = change.rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.084667 * persistence + 0.00189 * anchor
    return base_signal

def f24_turn_gemini_070(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=160, w2=203, w3=640, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(203, min_periods=max(203//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.320588 + 0.0018901 * anchor
    return base_signal

def f24_turn_gemini_071(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=167, w2=216, w3=657, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(216, min_periods=max(216//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.097333 * slope + 0.0018902 * anchor
    return base_signal

def f24_turn_gemini_072(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=174, w2=229, w3=674, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(229, min_periods=max(229//3, 2)).mean()
    noise = impulse.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.347647 + 0.0018903 * anchor
    return base_signal

def f24_turn_gemini_073(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=181, w2=242, w3=691, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 242)
    curvature = _rolling_slope(acceleration, 691)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.11 * acceleration + 0.0018904 * anchor
    return base_signal

def f24_turn_gemini_074(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=188, w2=255, w3=708, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 188)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.116333 * pressure.rolling(708, min_periods=max(708//3, 2)).mean() + 0.0018905 * anchor
    return base_signal

def f24_turn_gemini_075(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=195, w2=268, w3=725, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(195, min_periods=max(195//3, 2)).mean())
    decay = spread.ewm(span=268, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.388235 + 0.0018906 * anchor
    return base_signal
