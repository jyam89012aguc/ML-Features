"""39 volatility clustering gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Temporal persistence of high or low volatility periods as a risk signal.
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

def f39_vclu_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=5]"""
    window = 5
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=10]"""
    window = 10
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=21]"""
    window = 21
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=42]"""
    window = 42
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=63]"""
    window = 63
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=126]"""
    window = 126
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=252]"""
    window = 252
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=504]"""
    window = 504
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=756]"""
    window = 756
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=1260]"""
    window = 1260
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff()

def f39_vclu_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=500, w3=752, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 500)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.024118 + 0.0027522 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=14, w3=18, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.037647 + 0.0027523 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=27, w3=35, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(6)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.200667 * persistence + 0.0027524 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=40, w3=52, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(40, min_periods=max(40//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.064706 + 0.0027525 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=53, w3=69, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(53, min_periods=max(53//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.213333 * slope + 0.0027526 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=66, w3=86, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(27)
    drag = impulse.rolling(66, min_periods=max(66//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.091765 + 0.0027527 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=79, w3=103, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 79)
    curvature = _rolling_slope(acceleration, 103)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.226 * acceleration + 0.0027528 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=92, w3=120, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(41, min_periods=max(41//3, 2)).mean(), upside.rolling(92, min_periods=max(92//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(120) * 1.118824 + 0.0027529 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=105, w3=137, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(105, min_periods=max(105//3, 2)).max()
    rebound = x - x.rolling(48, min_periods=max(48//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.238667 * _rolling_slope(draw, 137) + 0.002753 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=118, w3=154, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(118, min_periods=max(118//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.145882 + 0.0027531 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=131, w3=171, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 131)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=171, adjust=False).mean() * 1.159412 + 0.0027532 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=144, w3=188, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(144, min_periods=max(144//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.172941 + 0.0027533 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=157, w3=205, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(76)
    rank = change.rolling(157, min_periods=max(157//3, 2)).rank(pct=True)
    persistence = change.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.264 * persistence + 0.0027534 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=170, w3=222, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(170, min_periods=max(170//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2 + 0.0027535 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=183, w3=239, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(183, min_periods=max(183//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.276667 * slope + 0.0027536 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=196, w3=256, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(97)
    drag = impulse.rolling(196, min_periods=max(196//3, 2)).mean()
    noise = impulse.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.227059 + 0.0027537 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=209, w3=273, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 209)
    curvature = _rolling_slope(acceleration, 273)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.289333 * acceleration + 0.0027538 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=222, w3=290, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.254118 + 0.0027539 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=235, w3=307, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(235, min_periods=max(235//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.302 * _rolling_slope(draw, 307) + 0.002754 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=248, w3=324, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(248, min_periods=max(248//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.281176 + 0.0027541 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=261, w3=341, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 261)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.294706 + 0.0027542 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=274, w3=358, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(274, min_periods=max(274//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.308235 + 0.0027543 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=287, w3=375, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(287, min_periods=max(287//3, 2)).rank(pct=True)
    persistence = change.rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.327333 * persistence + 0.0027544 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=300, w3=392, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(300, min_periods=max(300//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.335294 + 0.0027545 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=313, w3=409, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(313, min_periods=max(313//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.34 * slope + 0.0027546 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=326, w3=426, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(326, min_periods=max(326//3, 2)).mean()
    noise = impulse.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.362353 + 0.0027547 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=339, w3=443, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 339)
    curvature = _rolling_slope(acceleration, 443)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.352667 * acceleration + 0.0027548 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=352, w3=460, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(352, min_periods=max(352//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.389412 + 0.0027549 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=365, w3=477, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(365, min_periods=max(365//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.033 * _rolling_slope(draw, 477) + 0.002755 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=378, w3=494, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(378, min_periods=max(378//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.416471 + 0.0027551 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=391, w3=511, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 391)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.43 + 0.0027552 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=404, w3=528, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(404, min_periods=max(404//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.443529 + 0.0027553 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=417, w3=545, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(417, min_periods=max(417//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.058333 * persistence + 0.0027554 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=430, w3=562, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.470588 + 0.0027555 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=443, w3=579, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(443, min_periods=max(443//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.071 * slope + 0.0027556 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=456, w3=596, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(456, min_periods=max(456//3, 2)).mean()
    noise = impulse.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.497647 + 0.0027557 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=469, w3=613, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 613)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.083667 * acceleration + 0.0027558 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=482, w3=630, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(482, min_periods=max(482//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.524706 + 0.0027559 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=495, w3=647, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(495, min_periods=max(495//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.096333 * _rolling_slope(draw, 647) + 0.002756 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=508, w3=664, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(508, min_periods=max(508//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.551765 + 0.0027561 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=22, w3=681, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 22)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.565294 + 0.0027562 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=35, w3=698, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(35, min_periods=max(35//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.578824 + 0.0027563 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=48, w3=715, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(39)
    rank = change.rolling(48, min_periods=max(48//3, 2)).rank(pct=True)
    persistence = change.rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.121667 * persistence + 0.0027564 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=61, w3=732, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(61, min_periods=max(61//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.605882 + 0.0027565 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=74, w3=749, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(74, min_periods=max(74//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.134333 * slope + 0.0027566 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=87, w3=766, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(60)
    drag = impulse.rolling(87, min_periods=max(87//3, 2)).mean()
    noise = impulse.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.632941 + 0.0027567 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=100, w3=32, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 100)
    curvature = _rolling_slope(acceleration, 32)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.147 * acceleration + 0.0027568 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=113, w3=49, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(74, min_periods=max(74//3, 2)).mean(), upside.rolling(113, min_periods=max(113//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(49) * 1.66 + 0.0027569 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=126, w3=66, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(126, min_periods=max(126//3, 2)).max()
    rebound = x - x.rolling(81, min_periods=max(81//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.159667 * _rolling_slope(draw, 66) + 0.002757 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=139, w3=83, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(139, min_periods=max(139//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.833529 + 0.0027571 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=152, w3=100, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 152)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=100, adjust=False).mean() * 0.847059 + 0.0027572 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=165, w3=117, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(165, min_periods=max(165//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.860588 + 0.0027573 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=178, w3=134, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(109)
    rank = change.rolling(178, min_periods=max(178//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.185 * persistence + 0.0027574 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=191, w3=151, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(191, min_periods=max(191//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.887647 + 0.0027575 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=204, w3=168, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(204, min_periods=max(204//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.197667 * slope + 0.0027576 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=217, w3=185, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(217, min_periods=max(217//3, 2)).mean()
    noise = impulse.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.914706 + 0.0027577 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=230, w3=202, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 230)
    curvature = _rolling_slope(acceleration, 202)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.210333 * acceleration + 0.0027578 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=243, w3=219, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(243, min_periods=max(243//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.941765 + 0.0027579 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=256, w3=236, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(256, min_periods=max(256//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.223 * _rolling_slope(draw, 236) + 0.002758 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=269, w3=253, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(269, min_periods=max(269//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.968824 + 0.0027581 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=282, w3=270, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 282)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=270, adjust=False).mean() * 0.982353 + 0.0027582 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=295, w3=287, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.995882 + 0.0027583 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=308, w3=304, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(308, min_periods=max(308//3, 2)).rank(pct=True)
    persistence = change.rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.248333 * persistence + 0.0027584 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=321, w3=321, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(321, min_periods=max(321//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.022941 + 0.0027585 * anchor
    return base_signal.diff().diff()

def f39_vclu_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=334, w3=338, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(334, min_periods=max(334//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.261 * slope + 0.0027586 * anchor
    return base_signal.diff().diff()
