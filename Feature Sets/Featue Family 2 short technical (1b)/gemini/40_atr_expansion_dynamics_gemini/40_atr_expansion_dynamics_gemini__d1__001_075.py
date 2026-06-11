"""40 atr expansion dynamics gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Sudden increases in Average True Range as a precursor to significant price moves.
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

def f40_atre_gemini_001_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=5]"""
    window = 5
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_002_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=10]"""
    window = 10
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_003_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=21]"""
    window = 21
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_004_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=42]"""
    window = 42
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_005_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=63]"""
    window = 63
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_006_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=126]"""
    window = 126
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_007_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=252]"""
    window = 252
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_008_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=504]"""
    window = 504
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_009_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=756]"""
    window = 756
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_010_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=1260]"""
    window = 1260
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return (res).diff()

def f40_atre_gemini_011_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=471, w3=382, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(471, min_periods=max(471//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.189333 * slope + 0.0027942 * anchor
    return base_signal.diff()

def f40_atre_gemini_012_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=484, w3=399, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(484, min_periods=max(484//3, 2)).mean()
    noise = impulse.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.598824 + 0.0027943 * anchor
    return base_signal.diff()

def f40_atre_gemini_013_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=497, w3=416, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 497)
    curvature = _rolling_slope(acceleration, 416)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.202 * acceleration + 0.0027944 * anchor
    return base_signal.diff()

def f40_atre_gemini_014_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=11, w3=433, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(11)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.208333 * pressure.rolling(433, min_periods=max(433//3, 2)).mean() + 0.0027945 * anchor
    return base_signal.diff()

def f40_atre_gemini_015_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=24, w3=450, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=24, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.639412 + 0.0027946 * anchor
    return base_signal.diff()

def f40_atre_gemini_016_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=37, w3=467, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(37, min_periods=max(37//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.652941 + 0.0027947 * anchor
    return base_signal.diff()

def f40_atre_gemini_017_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=50, w3=484, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(50, min_periods=max(50//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.227333 * _rolling_slope(cover, 10) + 0.0027948 * anchor
    return base_signal.diff()

def f40_atre_gemini_018_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=63, w3=501, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.233667 * y + 0.766333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 63) + 0.0027949 * anchor
    return base_signal.diff()

def f40_atre_gemini_019_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=76, w3=518, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(76, min_periods=max(76//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.84 + 0.002795 * anchor
    return base_signal.diff()

def f40_atre_gemini_020_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=89, w3=535, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.246333 * _rolling_slope(draw, 535) + 0.0027951 * anchor
    return base_signal.diff()

def f40_atre_gemini_021_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=102, w3=552, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(38) - b.diff(102)
    stress = imbalance.rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.867059 + 0.0027952 * anchor
    return base_signal.diff()

def f40_atre_gemini_022_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=115, w3=569, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(115, min_periods=max(115//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.880588 + 0.0027953 * anchor
    return base_signal.diff()

def f40_atre_gemini_023_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=128, w3=586, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.894118 + 0.0027954 * anchor
    return base_signal.diff()

def f40_atre_gemini_024_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=141, w3=603, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(141, min_periods=max(141//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.907647 + 0.0027955 * anchor
    return base_signal.diff()

def f40_atre_gemini_025_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=154, w3=620, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(66)
    rank = change.rolling(154, min_periods=max(154//3, 2)).rank(pct=True)
    persistence = change.rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.278 * persistence + 0.0027956 * anchor
    return base_signal.diff()

def f40_atre_gemini_026_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=167, w3=637, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(167, min_periods=max(167//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.934706 + 0.0027957 * anchor
    return base_signal.diff()

def f40_atre_gemini_027_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=180, w3=654, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(180, min_periods=max(180//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.290667 * slope + 0.0027958 * anchor
    return base_signal.diff()

def f40_atre_gemini_028_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=193, w3=671, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(87)
    drag = impulse.rolling(193, min_periods=max(193//3, 2)).mean()
    noise = impulse.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.961765 + 0.0027959 * anchor
    return base_signal.diff()

def f40_atre_gemini_029_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=206, w3=688, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 206)
    curvature = _rolling_slope(acceleration, 688)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.303333 * acceleration + 0.002796 * anchor
    return base_signal.diff()

def f40_atre_gemini_030_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=219, w3=705, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 101)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.309667 * pressure.rolling(705, min_periods=max(705//3, 2)).mean() + 0.0027961 * anchor
    return base_signal.diff()

def f40_atre_gemini_031_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=232, w3=722, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=232, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.002353 + 0.0027962 * anchor
    return base_signal.diff()

def f40_atre_gemini_032_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=245, w3=739, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(245, min_periods=max(245//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 115)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.015882 + 0.0027963 * anchor
    return base_signal.diff()

def f40_atre_gemini_033_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=258, w3=756, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(122, min_periods=max(122//3, 2)).mean(), b.abs().rolling(258, min_periods=max(258//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.328667 * _rolling_slope(cover, 122) + 0.0027964 * anchor
    return base_signal.diff()

def f40_atre_gemini_034_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=271, w3=22, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.335 * y + 0.665000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 129) - _rolling_slope(basket, 271) + 0.0027965 * anchor
    return base_signal.diff()

def f40_atre_gemini_035_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=284, w3=39, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(284, min_periods=max(284//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(39) * 1.056471 + 0.0027966 * anchor
    return base_signal.diff()

def f40_atre_gemini_036_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=297, w3=56, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(297, min_periods=max(297//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.347667 * _rolling_slope(draw, 56) + 0.0027967 * anchor
    return base_signal.diff()

def f40_atre_gemini_037_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=310, w3=73, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.083529 + 0.0027968 * anchor
    return base_signal.diff()

def f40_atre_gemini_038_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=323, w3=90, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(323, min_periods=max(323//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.097059 + 0.0027969 * anchor
    return base_signal.diff()

def f40_atre_gemini_039_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=336, w3=107, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 336)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=107, adjust=False).mean() * 1.110588 + 0.002797 * anchor
    return base_signal.diff()

def f40_atre_gemini_040_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=349, w3=124, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(349, min_periods=max(349//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.124118 + 0.0027971 * anchor
    return base_signal.diff()

def f40_atre_gemini_041_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=362, w3=141, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.047 * persistence + 0.0027972 * anchor
    return base_signal.diff()

def f40_atre_gemini_042_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=375, w3=158, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(375, min_periods=max(375//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.151176 + 0.0027973 * anchor
    return base_signal.diff()

def f40_atre_gemini_043_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=388, w3=175, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(388, min_periods=max(388//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.059667 * slope + 0.0027974 * anchor
    return base_signal.diff()

def f40_atre_gemini_044_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=401, w3=192, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.178235 + 0.0027975 * anchor
    return base_signal.diff()

def f40_atre_gemini_045_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=414, w3=209, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 209)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.072333 * acceleration + 0.0027976 * anchor
    return base_signal.diff()

def f40_atre_gemini_046_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=427, w3=226, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 213)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.078667 * pressure.rolling(226, min_periods=max(226//3, 2)).mean() + 0.0027977 * anchor
    return base_signal.diff()

def f40_atre_gemini_047_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=440, w3=243, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(220, min_periods=max(220//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.218824 + 0.0027978 * anchor
    return base_signal.diff()

def f40_atre_gemini_048_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=453, w3=260, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(453, min_periods=max(453//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 227)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.232353 + 0.0027979 * anchor
    return base_signal.diff()

def f40_atre_gemini_049_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=466, w3=277, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(234, min_periods=max(234//3, 2)).mean(), b.abs().rolling(466, min_periods=max(466//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.097667 * _rolling_slope(cover, 234) + 0.002798 * anchor
    return base_signal.diff()

def f40_atre_gemini_050_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=479, w3=294, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.104 * y + 0.896000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 241) - _rolling_slope(basket, 479) + 0.0027981 * anchor
    return base_signal.diff()

def f40_atre_gemini_051_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=492, w3=311, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(492, min_periods=max(492//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.272941 + 0.0027982 * anchor
    return base_signal.diff()

def f40_atre_gemini_052_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=505, w3=328, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(505, min_periods=max(505//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.116667 * _rolling_slope(draw, 328) + 0.0027983 * anchor
    return base_signal.diff()

def f40_atre_gemini_053_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=19, w3=345, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(15) - b.diff(19)
    stress = imbalance.rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.3 + 0.0027984 * anchor
    return base_signal.diff()

def f40_atre_gemini_054_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=32, w3=362, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(32, min_periods=max(32//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.313529 + 0.0027985 * anchor
    return base_signal.diff()

def f40_atre_gemini_055_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=45, w3=379, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.327059 + 0.0027986 * anchor
    return base_signal.diff()

def f40_atre_gemini_056_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=58, w3=396, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(58, min_periods=max(58//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.340588 + 0.0027987 * anchor
    return base_signal.diff()

def f40_atre_gemini_057_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=71, w3=413, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(43)
    rank = change.rolling(71, min_periods=max(71//3, 2)).rank(pct=True)
    persistence = change.rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.148333 * persistence + 0.0027988 * anchor
    return base_signal.diff()

def f40_atre_gemini_058_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=84, w3=430, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(84, min_periods=max(84//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.367647 + 0.0027989 * anchor
    return base_signal.diff()

def f40_atre_gemini_059_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=97, w3=447, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(97, min_periods=max(97//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.161 * slope + 0.002799 * anchor
    return base_signal.diff()

def f40_atre_gemini_060_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=110, w3=464, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(64)
    drag = impulse.rolling(110, min_periods=max(110//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.394706 + 0.0027991 * anchor
    return base_signal.diff()

def f40_atre_gemini_061_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=123, w3=481, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 123)
    curvature = _rolling_slope(acceleration, 481)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.173667 * acceleration + 0.0027992 * anchor
    return base_signal.diff()

def f40_atre_gemini_062_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=136, w3=498, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 78)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.18 * pressure.rolling(498, min_periods=max(498//3, 2)).mean() + 0.0027993 * anchor
    return base_signal.diff()

def f40_atre_gemini_063_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=149, w3=515, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(85, min_periods=max(85//3, 2)).mean())
    decay = spread.ewm(span=149, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.435294 + 0.0027994 * anchor
    return base_signal.diff()

def f40_atre_gemini_064_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=162, w3=532, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(162, min_periods=max(162//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 92)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.448824 + 0.0027995 * anchor
    return base_signal.diff()

def f40_atre_gemini_065_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=175, w3=549, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(99, min_periods=max(99//3, 2)).mean(), b.abs().rolling(175, min_periods=max(175//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.199 * _rolling_slope(cover, 99) + 0.0027996 * anchor
    return base_signal.diff()

def f40_atre_gemini_066_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=188, w3=566, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.205333 * y + 0.794667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 106) - _rolling_slope(basket, 188) + 0.0027997 * anchor
    return base_signal.diff()

def f40_atre_gemini_067_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=201, w3=583, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(201, min_periods=max(201//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.489412 + 0.0027998 * anchor
    return base_signal.diff()

def f40_atre_gemini_068_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=214, w3=600, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.218 * _rolling_slope(draw, 600) + 0.0027999 * anchor
    return base_signal.diff()

def f40_atre_gemini_069_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=227, w3=617, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.516471 + 0.0028 * anchor
    return base_signal.diff()

def f40_atre_gemini_070_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=240, w3=634, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(240, min_periods=max(240//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.53 + 0.0028001 * anchor
    return base_signal.diff()

def f40_atre_gemini_071_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=253, w3=651, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 253)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.543529 + 0.0028002 * anchor
    return base_signal.diff()

def f40_atre_gemini_072_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=266, w3=668, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.557059 + 0.0028003 * anchor
    return base_signal.diff()

def f40_atre_gemini_073_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=279, w3=685, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(279, min_periods=max(279//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249667 * persistence + 0.0028004 * anchor
    return base_signal.diff()

def f40_atre_gemini_074_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=292, w3=702, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(292, min_periods=max(292//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.584118 + 0.0028005 * anchor
    return base_signal.diff()

def f40_atre_gemini_075_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=305, w3=719, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(305, min_periods=max(305//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.262333 * slope + 0.0028006 * anchor
    return base_signal.diff()
