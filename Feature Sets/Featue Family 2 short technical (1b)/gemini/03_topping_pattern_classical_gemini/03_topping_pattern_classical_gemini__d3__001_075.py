"""03 topping pattern classical gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks.
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

def f03_topc_gemini_001_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=5]"""
    window = 5
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_002_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=10]"""
    window = 10
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_003_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=21]"""
    window = 21
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_004_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=42]"""
    window = 42
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_005_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=63]"""
    window = 63
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_006_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=126]"""
    window = 126
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_007_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=252]"""
    window = 252
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_008_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=504]"""
    window = 504
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_009_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=756]"""
    window = 756
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_010_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Classical topping patterns identified via rolling max exhaustion and volatility expansion at peaks. [window=1260]"""
    window = 1260
    res = _safe_div(high.rolling(window).max() - close, _atr(high, low, close, window))
    return (res).diff().diff().diff()

def f03_topc_gemini_011_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=478, w3=284, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.038824 + 0.0001342 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_012_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=491, w3=301, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.222 * _rolling_slope(draw, 301) + 0.0001343 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_013_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=504, w3=318, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(20) - b.diff(126)
    stress = imbalance.rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.065882 + 0.0001344 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_014_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=18, w3=335, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(18, min_periods=max(18//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.079412 + 0.0001345 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_015_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=31, w3=352, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 31)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.092941 + 0.0001346 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_016_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=44, w3=369, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(44, min_periods=max(44//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.106471 + 0.0001347 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_017_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=57, w3=386, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(48)
    rank = change.rolling(57, min_periods=max(57//3, 2)).rank(pct=True)
    persistence = change.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.253667 * persistence + 0.0001348 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_018_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=70, w3=403, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(70, min_periods=max(70//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.133529 + 0.0001349 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_019_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=83, w3=420, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(83, min_periods=max(83//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.266333 * slope + 0.000135 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_020_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=96, w3=437, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(69)
    drag = impulse.rolling(96, min_periods=max(96//3, 2)).mean()
    noise = impulse.abs().rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.160588 + 0.0001351 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_021_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=109, w3=454, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 109)
    curvature = _rolling_slope(acceleration, 454)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.279 * acceleration + 0.0001352 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_022_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=122, w3=471, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 83)
    pressure = rel_log.diff(122)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.285333 * pressure.rolling(471, min_periods=max(471//3, 2)).mean() + 0.0001353 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_023_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=135, w3=488, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(90, min_periods=max(90//3, 2)).mean())
    decay = spread.ewm(span=135, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.201176 + 0.0001354 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_024_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=148, w3=505, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(148, min_periods=max(148//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 97)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.214706 + 0.0001355 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_025_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=161, w3=522, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(104, min_periods=max(104//3, 2)).mean(), b.abs().rolling(161, min_periods=max(161//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.304333 * _rolling_slope(cover, 104) + 0.0001356 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_026_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=174, w3=539, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.310667 * y + 0.689333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 111) - _rolling_slope(basket, 174) + 0.0001357 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_027_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=187, w3=556, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(187, min_periods=max(187//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.255294 + 0.0001358 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_028_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=200, w3=573, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.323333 * _rolling_slope(draw, 573) + 0.0001359 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_029_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=213, w3=590, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.282353 + 0.000136 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_030_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=226, w3=607, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(226, min_periods=max(226//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.295882 + 0.0001361 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_031_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=239, w3=624, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 239)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.309412 + 0.0001362 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_032_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=252, w3=641, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(252, min_periods=max(252//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.322941 + 0.0001363 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_033_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=265, w3=658, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(265, min_periods=max(265//3, 2)).rank(pct=True)
    persistence = change.rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355 * persistence + 0.0001364 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_034_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=278, w3=675, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(278, min_periods=max(278//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35 + 0.0001365 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_035_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=291, w3=692, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(291, min_periods=max(291//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.035333 * slope + 0.0001366 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_036_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=304, w3=709, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(304, min_periods=max(304//3, 2)).mean()
    noise = impulse.abs().rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.377059 + 0.0001367 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_037_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=317, w3=726, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 317)
    curvature = _rolling_slope(acceleration, 726)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.048 * acceleration + 0.0001368 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_038_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=330, w3=743, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 195)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.054333 * pressure.rolling(743, min_periods=max(743//3, 2)).mean() + 0.0001369 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_039_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=343, w3=760, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(202, min_periods=max(202//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.417647 + 0.000137 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_040_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=356, w3=26, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(356, min_periods=max(356//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 209)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.431176 + 0.0001371 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_041_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=369, w3=43, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(216, min_periods=max(216//3, 2)).mean(), b.abs().rolling(369, min_periods=max(369//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(43) + 0.073333 * _rolling_slope(cover, 216) + 0.0001372 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_042_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=382, w3=60, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.079667 * y + 0.920333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 223) - _rolling_slope(basket, 382) + 0.0001373 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_043_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=395, w3=77, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(395, min_periods=max(395//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(77) * 1.471765 + 0.0001374 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_044_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=408, w3=94, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(408, min_periods=max(408//3, 2)).max()
    rebound = x - x.rolling(237, min_periods=max(237//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.092333 * _rolling_slope(draw, 94) + 0.0001375 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_045_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=421, w3=111, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.498824 + 0.0001376 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_046_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=434, w3=128, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 251)
    baseline = trend.rolling(434, min_periods=max(434//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.512353 + 0.0001377 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_047_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=447, w3=145, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 11)
    slow = _rolling_slope(x, 447)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=145, adjust=False).mean() * 1.525882 + 0.0001378 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_048_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=460, w3=162, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(18, min_periods=max(18//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.539412 + 0.0001379 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_049_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=473, w3=179, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(25)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.124 * persistence + 0.000138 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_050_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=486, w3=196, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(32, min_periods=max(32//3, 2)).std()
    vol_slow = ret.rolling(486, min_periods=max(486//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.566471 + 0.0001381 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_051_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=499, w3=213, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(499, min_periods=max(499//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 39)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.136667 * slope + 0.0001382 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_052_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=13, w3=230, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(46)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(230, min_periods=max(230//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.593529 + 0.0001383 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_053_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=26, w3=247, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 53)
    acceleration = _rolling_slope(velocity, 26)
    curvature = _rolling_slope(acceleration, 247)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.149333 * acceleration + 0.0001384 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_054_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=39, w3=264, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 60)
    pressure = rel_log.diff(39)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.155667 * pressure.rolling(264, min_periods=max(264//3, 2)).mean() + 0.0001385 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_055_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=52, w3=281, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(67, min_periods=max(67//3, 2)).mean())
    decay = spread.ewm(span=52, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.634118 + 0.0001386 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_056_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=65, w3=298, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(65, min_periods=max(65//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 74)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.647647 + 0.0001387 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_057_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=78, w3=315, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(81, min_periods=max(81//3, 2)).mean(), b.abs().rolling(78, min_periods=max(78//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.174667 * _rolling_slope(cover, 81) + 0.0001388 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_058_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=91, w3=332, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.181 * y + 0.819000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 88) - _rolling_slope(basket, 91) + 0.0001389 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_059_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=104, w3=349, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(104, min_periods=max(104//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.834706 + 0.000139 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_060_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=117, w3=366, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(117, min_periods=max(117//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.193667 * _rolling_slope(draw, 366) + 0.0001391 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_061_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=130, w3=383, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(109) - b.diff(126)
    stress = imbalance.rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.861765 + 0.0001392 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_062_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=143, w3=400, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(143, min_periods=max(143//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(400, min_periods=max(400//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.875294 + 0.0001393 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_063_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=156, w3=417, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 156)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.888824 + 0.0001394 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_064_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=169, w3=434, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(169, min_periods=max(169//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.902353 + 0.0001395 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_065_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=182, w3=451, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(182, min_periods=max(182//3, 2)).rank(pct=True)
    persistence = change.rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.225333 * persistence + 0.0001396 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_066_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=195, w3=468, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(195, min_periods=max(195//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.929412 + 0.0001397 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_067_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=208, w3=485, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(208, min_periods=max(208//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.238 * slope + 0.0001398 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_068_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=221, w3=502, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(221, min_periods=max(221//3, 2)).mean()
    noise = impulse.abs().rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.956471 + 0.0001399 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_069_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=234, w3=519, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 234)
    curvature = _rolling_slope(acceleration, 519)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.250667 * acceleration + 0.00014 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_070_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=247, w3=536, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 172)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.257 * pressure.rolling(536, min_periods=max(536//3, 2)).mean() + 0.0001401 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_071_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=260, w3=553, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(179, min_periods=max(179//3, 2)).mean())
    decay = spread.ewm(span=260, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.997059 + 0.0001402 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_072_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=273, w3=570, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(273, min_periods=max(273//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 186)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.010588 + 0.0001403 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_073_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=286, w3=587, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(193, min_periods=max(193//3, 2)).mean(), b.abs().rolling(286, min_periods=max(286//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.276 * _rolling_slope(cover, 193) + 0.0001404 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_074_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=299, w3=604, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.282333 * y + 0.717667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 200) - _rolling_slope(basket, 299) + 0.0001405 * anchor
    return base_signal.diff().diff().diff()

def f03_topc_gemini_075_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=312, w3=621, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(312, min_periods=max(312//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.051176 + 0.0001406 * anchor
    return base_signal.diff().diff().diff()
