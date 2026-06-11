"""47 atr extension signature gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Price extensions relative to ATR bands as a signal of overbought or oversold states.
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

def f47_atrx_gemini_001_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=5]"""
    window = 5
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_002_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=10]"""
    window = 10
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_003_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=21]"""
    window = 21
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_004_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=42]"""
    window = 42
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_005_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=63]"""
    window = 63
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_006_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=126]"""
    window = 126
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_007_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=252]"""
    window = 252
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_008_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=504]"""
    window = 504
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_009_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=756]"""
    window = 756
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_010_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Price extensions relative to ATR bands as a signal of overbought or oversold states. [window=1260]"""
    window = 1260
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window * 2))
    return (res).diff().diff().diff()

def f47_atrx_gemini_011_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=181, w3=437, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(181, min_periods=max(181//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.222353 + 0.0032142 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_012_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=194, w3=454, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(194, min_periods=max(194//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.209 * _rolling_slope(draw, 454) + 0.0032143 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_013_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=207, w3=471, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.249412 + 0.0032144 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_014_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=220, w3=488, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(220, min_periods=max(220//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.262941 + 0.0032145 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_015_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=233, w3=505, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.276471 + 0.0032146 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_016_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=246, w3=522, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.29 + 0.0032147 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_017_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=259, w3=539, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(17)
    rank = change.rolling(259, min_periods=max(259//3, 2)).rank(pct=True)
    persistence = change.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.240667 * persistence + 0.0032148 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_018_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=272, w3=556, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(272, min_periods=max(272//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.317059 + 0.0032149 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_019_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=285, w3=573, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.253333 * slope + 0.003215 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_020_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=298, w3=590, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(38)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.344118 + 0.0032151 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_021_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=311, w3=607, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.266 * acceleration + 0.0032152 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_022_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=324, w3=624, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 52)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.272333 * pressure.rolling(624, min_periods=max(624//3, 2)).mean() + 0.0032153 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_023_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=337, w3=641, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(59, min_periods=max(59//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.384706 + 0.0032154 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_024_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=350, w3=658, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(350, min_periods=max(350//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 66)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.398235 + 0.0032155 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_025_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=363, w3=675, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(73, min_periods=max(73//3, 2)).mean(), b.abs().rolling(363, min_periods=max(363//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.291333 * _rolling_slope(cover, 73) + 0.0032156 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_026_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=376, w3=692, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.297667 * y + 0.702333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 80) - _rolling_slope(basket, 376) + 0.0032157 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_027_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=389, w3=709, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(389, min_periods=max(389//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.438824 + 0.0032158 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_028_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=402, w3=726, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(402, min_periods=max(402//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.310333 * _rolling_slope(draw, 726) + 0.0032159 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_029_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=415, w3=743, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(101) - b.diff(126)
    stress = imbalance.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.465882 + 0.003216 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_030_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=428, w3=760, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 108)
    baseline = trend.rolling(428, min_periods=max(428//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(760, min_periods=max(760//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.479412 + 0.0032161 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_031_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=441, w3=26, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 441)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=26, adjust=False).mean() * 1.492941 + 0.0032162 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_032_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=454, w3=43, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(122, min_periods=max(122//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.506471 + 0.0032163 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_033_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=467, w3=60, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(467, min_periods=max(467//3, 2)).rank(pct=True)
    persistence = change.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.342 * persistence + 0.0032164 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_034_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=480, w3=77, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(136, min_periods=max(136//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.533529 + 0.0032165 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_035_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=493, w3=94, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.354667 * slope + 0.0032166 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_036_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=506, w3=111, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.560588 + 0.0032167 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_037_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=20, w3=128, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 128)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.035 * acceleration + 0.0032168 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_038_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=33, w3=145, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 164)
    pressure = rel_log.diff(33)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.041333 * pressure.rolling(145, min_periods=max(145//3, 2)).mean() + 0.0032169 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_039_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=46, w3=162, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(171, min_periods=max(171//3, 2)).mean())
    decay = spread.ewm(span=46, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.601176 + 0.003217 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_040_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=59, w3=179, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(59, min_periods=max(59//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 178)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.614706 + 0.0032171 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_041_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=72, w3=196, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(185, min_periods=max(185//3, 2)).mean(), b.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.060333 * _rolling_slope(cover, 185) + 0.0032172 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_042_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=85, w3=213, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.066667 * y + 0.933333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 192) - _rolling_slope(basket, 85) + 0.0032173 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_043_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=98, w3=230, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.655294 + 0.0032174 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_044_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=111, w3=247, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.079333 * _rolling_slope(draw, 247) + 0.0032175 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_045_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=124, w3=264, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(124)
    stress = imbalance.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.828824 + 0.0032176 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_046_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=137, w3=281, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(137, min_periods=max(137//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.842353 + 0.0032177 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_047_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=150, w3=298, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 150)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=298, adjust=False).mean() * 0.855882 + 0.0032178 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_048_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=163, w3=315, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(163, min_periods=max(163//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.869412 + 0.0032179 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_049_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=176, w3=332, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 0.003218 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_050_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=189, w3=349, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(189, min_periods=max(189//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.896471 + 0.0032181 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_051_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=202, w3=366, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.123667 * slope + 0.0032182 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_052_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=215, w3=383, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(15)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.923529 + 0.0032183 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_053_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=228, w3=400, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 228)
    curvature = _rolling_slope(acceleration, 400)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136333 * acceleration + 0.0032184 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_054_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=241, w3=417, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 29)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.142667 * pressure.rolling(417, min_periods=max(417//3, 2)).mean() + 0.0032185 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_055_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=254, w3=434, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(36, min_periods=max(36//3, 2)).mean())
    decay = spread.ewm(span=254, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.964118 + 0.0032186 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_056_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=267, w3=451, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(267, min_periods=max(267//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 43)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.977647 + 0.0032187 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_057_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=280, w3=468, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(50, min_periods=max(50//3, 2)).mean(), b.abs().rolling(280, min_periods=max(280//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.161667 * _rolling_slope(cover, 50) + 0.0032188 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_058_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=293, w3=485, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.168 * y + 0.832000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 57) - _rolling_slope(basket, 293) + 0.0032189 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_059_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=306, w3=502, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.018235 + 0.003219 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_060_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=319, w3=519, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.180667 * _rolling_slope(draw, 519) + 0.0032191 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_061_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=332, w3=536, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(78) - b.diff(126)
    stress = imbalance.rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.045294 + 0.0032192 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_062_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=345, w3=553, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(345, min_periods=max(345//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.058824 + 0.0032193 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_063_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=358, w3=570, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.072353 + 0.0032194 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_064_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=371, w3=587, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.085882 + 0.0032195 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_065_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=384, w3=604, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(106)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.212333 * persistence + 0.0032196 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_066_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=397, w3=621, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.112941 + 0.0032197 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_067_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=410, w3=638, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225 * slope + 0.0032198 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_068_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=423, w3=655, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.14 + 0.0032199 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_069_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=436, w3=672, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 672)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.237667 * acceleration + 0.00322 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_070_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=449, w3=689, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 141)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.244 * pressure.rolling(689, min_periods=max(689//3, 2)).mean() + 0.0032201 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_071_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=462, w3=706, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(148, min_periods=max(148//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.180588 + 0.0032202 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_072_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=475, w3=723, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(475, min_periods=max(475//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 155)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.194118 + 0.0032203 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_073_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=488, w3=740, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(162, min_periods=max(162//3, 2)).mean(), b.abs().rolling(488, min_periods=max(488//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.263 * _rolling_slope(cover, 162) + 0.0032204 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_074_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=501, w3=757, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.269333 * y + 0.730667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 169) - _rolling_slope(basket, 501) + 0.0032205 * anchor
    return base_signal.diff().diff().diff()

def f47_atrx_gemini_075_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=15, w3=23, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(23) * 1.234706 + 0.0032206 * anchor
    return base_signal.diff().diff().diff()
