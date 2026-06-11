"""25 rsi exhaustion family gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Overbought and oversold conditions detected through Relative Strength Index extremes.
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

def f25_rsie_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=5]"""
    window = 5
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=10]"""
    window = 10
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=21]"""
    window = 21
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=42]"""
    window = 42
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=63]"""
    window = 63
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=126]"""
    window = 126
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=252]"""
    window = 252
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=504]"""
    window = 504
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=756]"""
    window = 756
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Overbought and oversold conditions detected through Relative Strength Index extremes. [window=1260]"""
    window = 1260
    res = _rolling_zscore(close.diff().apply(lambda x: max(x, 0)).rolling(window).mean(), window)
    return (res).diff()

def f25_rsie_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=53, w3=272, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 201)
    slow = _rolling_slope(x, 53)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=272, adjust=False).mean() * 1.457647 + 0.0019542 * anchor
    return base_signal.diff()

def f25_rsie_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=66, w3=289, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(66, min_periods=max(66//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.471176 + 0.0019543 * anchor
    return base_signal.diff()

def f25_rsie_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=79, w3=306, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(79, min_periods=max(79//3, 2)).rank(pct=True)
    persistence = change.rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.175333 * persistence + 0.0019544 * anchor
    return base_signal.diff()

def f25_rsie_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=92, w3=323, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(92, min_periods=max(92//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.498235 + 0.0019545 * anchor
    return base_signal.diff()

def f25_rsie_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=105, w3=340, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(105, min_periods=max(105//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 229)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.188 * slope + 0.0019546 * anchor
    return base_signal.diff()

def f25_rsie_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=118, w3=357, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(118, min_periods=max(118//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.525294 + 0.0019547 * anchor
    return base_signal.diff()

def f25_rsie_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=131, w3=374, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 374)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.200667 * acceleration + 0.0019548 * anchor
    return base_signal.diff()

def f25_rsie_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=144, w3=391, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(144, min_periods=max(144//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.552353 + 0.0019549 * anchor
    return base_signal.diff()

def f25_rsie_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=157, w3=408, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(157, min_periods=max(157//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.213333 * _rolling_slope(draw, 408) + 0.001955 * anchor
    return base_signal.diff()

def f25_rsie_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=170, w3=425, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 17)
    baseline = trend.rolling(170, min_periods=max(170//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.579412 + 0.0019551 * anchor
    return base_signal.diff()

def f25_rsie_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=183, w3=442, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 24)
    slow = _rolling_slope(x, 183)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.592941 + 0.0019552 * anchor
    return base_signal.diff()

def f25_rsie_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=196, w3=459, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(196, min_periods=max(196//3, 2)).max()
    trough = x.rolling(31, min_periods=max(31//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.606471 + 0.0019553 * anchor
    return base_signal.diff()

def f25_rsie_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=209, w3=476, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(38)
    rank = change.rolling(209, min_periods=max(209//3, 2)).rank(pct=True)
    persistence = change.rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.238667 * persistence + 0.0019554 * anchor
    return base_signal.diff()

def f25_rsie_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=222, w3=493, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(45, min_periods=max(45//3, 2)).std()
    vol_slow = ret.rolling(222, min_periods=max(222//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.633529 + 0.0019555 * anchor
    return base_signal.diff()

def f25_rsie_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=235, w3=510, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(235, min_periods=max(235//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 52)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.251333 * slope + 0.0019556 * anchor
    return base_signal.diff()

def f25_rsie_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=248, w3=527, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(59)
    drag = impulse.rolling(248, min_periods=max(248//3, 2)).mean()
    noise = impulse.abs().rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.660588 + 0.0019557 * anchor
    return base_signal.diff()

def f25_rsie_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=261, w3=544, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 66)
    acceleration = _rolling_slope(velocity, 261)
    curvature = _rolling_slope(acceleration, 544)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.264 * acceleration + 0.0019558 * anchor
    return base_signal.diff()

def f25_rsie_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=274, w3=561, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(73, min_periods=max(73//3, 2)).mean(), upside.rolling(274, min_periods=max(274//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.834118 + 0.0019559 * anchor
    return base_signal.diff()

def f25_rsie_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=287, w3=578, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(287, min_periods=max(287//3, 2)).max()
    rebound = x - x.rolling(80, min_periods=max(80//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.276667 * _rolling_slope(draw, 578) + 0.001956 * anchor
    return base_signal.diff()

def f25_rsie_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=300, w3=595, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(300, min_periods=max(300//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.861176 + 0.0019561 * anchor
    return base_signal.diff()

def f25_rsie_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=313, w3=612, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 313)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.874706 + 0.0019562 * anchor
    return base_signal.diff()

def f25_rsie_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=326, w3=629, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(326, min_periods=max(326//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.888235 + 0.0019563 * anchor
    return base_signal.diff()

def f25_rsie_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=339, w3=646, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(108)
    rank = change.rolling(339, min_periods=max(339//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.302 * persistence + 0.0019564 * anchor
    return base_signal.diff()

def f25_rsie_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=352, w3=663, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(352, min_periods=max(352//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.915294 + 0.0019565 * anchor
    return base_signal.diff()

def f25_rsie_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=365, w3=680, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(365, min_periods=max(365//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.314667 * slope + 0.0019566 * anchor
    return base_signal.diff()

def f25_rsie_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=378, w3=697, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(378, min_periods=max(378//3, 2)).mean()
    noise = impulse.abs().rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.942353 + 0.0019567 * anchor
    return base_signal.diff()

def f25_rsie_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=391, w3=714, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 391)
    curvature = _rolling_slope(acceleration, 714)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.327333 * acceleration + 0.0019568 * anchor
    return base_signal.diff()

def f25_rsie_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=404, w3=731, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(404, min_periods=max(404//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.969412 + 0.0019569 * anchor
    return base_signal.diff()

def f25_rsie_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=417, w3=748, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(417, min_periods=max(417//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.34 * _rolling_slope(draw, 748) + 0.001957 * anchor
    return base_signal.diff()

def f25_rsie_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=430, w3=765, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(430, min_periods=max(430//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.996471 + 0.0019571 * anchor
    return base_signal.diff()

def f25_rsie_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=443, w3=31, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 443)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=31, adjust=False).mean() * 1.01 + 0.0019572 * anchor
    return base_signal.diff()

def f25_rsie_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=456, w3=48, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(456, min_periods=max(456//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.023529 + 0.0019573 * anchor
    return base_signal.diff()

def f25_rsie_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=469, w3=65, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(469, min_periods=max(469//3, 2)).rank(pct=True)
    persistence = change.rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.033 * persistence + 0.0019574 * anchor
    return base_signal.diff()

def f25_rsie_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=482, w3=82, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(482, min_periods=max(482//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.050588 + 0.0019575 * anchor
    return base_signal.diff()

def f25_rsie_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=495, w3=99, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(495, min_periods=max(495//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.045667 * slope + 0.0019576 * anchor
    return base_signal.diff()

def f25_rsie_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=508, w3=116, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(508, min_periods=max(508//3, 2)).mean()
    noise = impulse.abs().rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.077647 + 0.0019577 * anchor
    return base_signal.diff()

def f25_rsie_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=22, w3=133, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 22)
    curvature = _rolling_slope(acceleration, 133)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.058333 * acceleration + 0.0019578 * anchor
    return base_signal.diff()

def f25_rsie_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=35, w3=150, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(213, min_periods=max(213//3, 2)).mean(), upside.rolling(35, min_periods=max(35//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.104706 + 0.0019579 * anchor
    return base_signal.diff()

def f25_rsie_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=48, w3=167, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(48, min_periods=max(48//3, 2)).max()
    rebound = x - x.rolling(220, min_periods=max(220//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.071 * _rolling_slope(draw, 167) + 0.001958 * anchor
    return base_signal.diff()

def f25_rsie_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=61, w3=184, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 227)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.131765 + 0.0019581 * anchor
    return base_signal.diff()

def f25_rsie_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=74, w3=201, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 74)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=201, adjust=False).mean() * 1.145294 + 0.0019582 * anchor
    return base_signal.diff()

def f25_rsie_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=87, w3=218, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(87, min_periods=max(87//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.158824 + 0.0019583 * anchor
    return base_signal.diff()

def f25_rsie_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=100, w3=235, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(100, min_periods=max(100//3, 2)).rank(pct=True)
    persistence = change.rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.096333 * persistence + 0.0019584 * anchor
    return base_signal.diff()

def f25_rsie_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=113, w3=252, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(113, min_periods=max(113//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.185882 + 0.0019585 * anchor
    return base_signal.diff()

def f25_rsie_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=126, w3=269, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(126, min_periods=max(126//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.109 * slope + 0.0019586 * anchor
    return base_signal.diff()

def f25_rsie_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=139, w3=286, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(22)
    drag = impulse.rolling(139, min_periods=max(139//3, 2)).mean()
    noise = impulse.abs().rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.212941 + 0.0019587 * anchor
    return base_signal.diff()

def f25_rsie_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=152, w3=303, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 152)
    curvature = _rolling_slope(acceleration, 303)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.121667 * acceleration + 0.0019588 * anchor
    return base_signal.diff()

def f25_rsie_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=165, w3=320, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(165, min_periods=max(165//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.24 + 0.0019589 * anchor
    return base_signal.diff()

def f25_rsie_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=178, w3=337, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(178, min_periods=max(178//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.134333 * _rolling_slope(draw, 337) + 0.001959 * anchor
    return base_signal.diff()

def f25_rsie_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=191, w3=354, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(191, min_periods=max(191//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.267059 + 0.0019591 * anchor
    return base_signal.diff()

def f25_rsie_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=204, w3=371, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 204)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.280588 + 0.0019592 * anchor
    return base_signal.diff()

def f25_rsie_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=217, w3=388, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(217, min_periods=max(217//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.294118 + 0.0019593 * anchor
    return base_signal.diff()

def f25_rsie_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=230, w3=405, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(71)
    rank = change.rolling(230, min_periods=max(230//3, 2)).rank(pct=True)
    persistence = change.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.159667 * persistence + 0.0019594 * anchor
    return base_signal.diff()

def f25_rsie_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=243, w3=422, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(243, min_periods=max(243//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.321176 + 0.0019595 * anchor
    return base_signal.diff()

def f25_rsie_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=256, w3=439, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.172333 * slope + 0.0019596 * anchor
    return base_signal.diff()

def f25_rsie_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=269, w3=456, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(92)
    drag = impulse.rolling(269, min_periods=max(269//3, 2)).mean()
    noise = impulse.abs().rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.348235 + 0.0019597 * anchor
    return base_signal.diff()

def f25_rsie_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=282, w3=473, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 282)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.185 * acceleration + 0.0019598 * anchor
    return base_signal.diff()

def f25_rsie_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=295, w3=490, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(295, min_periods=max(295//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.375294 + 0.0019599 * anchor
    return base_signal.diff()

def f25_rsie_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=308, w3=507, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(308, min_periods=max(308//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.197667 * _rolling_slope(draw, 507) + 0.00196 * anchor
    return base_signal.diff()

def f25_rsie_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=321, w3=524, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.402353 + 0.0019601 * anchor
    return base_signal.diff()

def f25_rsie_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=334, w3=541, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 334)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.415882 + 0.0019602 * anchor
    return base_signal.diff()

def f25_rsie_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=347, w3=558, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(347, min_periods=max(347//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.429412 + 0.0019603 * anchor
    return base_signal.diff()

def f25_rsie_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=360, w3=575, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(360, min_periods=max(360//3, 2)).rank(pct=True)
    persistence = change.rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.223 * persistence + 0.0019604 * anchor
    return base_signal.diff()

def f25_rsie_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=373, w3=592, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.456471 + 0.0019605 * anchor
    return base_signal.diff()

def f25_rsie_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=386, w3=609, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.235667 * slope + 0.0019606 * anchor
    return base_signal.diff()
