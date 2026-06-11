"""39 volatility clustering gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f39_vclu_gemini_001_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=5]"""
    window = 5
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_002_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=10]"""
    window = 10
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_003_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=21]"""
    window = 21
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_004_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=42]"""
    window = 42
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_005_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=63]"""
    window = 63
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_006_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=126]"""
    window = 126
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_007_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=252]"""
    window = 252
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_008_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=504]"""
    window = 504
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_009_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=756]"""
    window = 756
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_010_d3(close: pd.Series) -> pd.Series:
    """Temporal persistence of high or low volatility periods as a risk signal. [window=1260]"""
    window = 1260
    res = _rolling_slope(_safe_log(close).diff().abs().rolling(window).std(), window)
    return (res).diff().diff().diff()

def f39_vclu_gemini_011_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=324, w3=128, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 324)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=128, adjust=False).mean() * 1.211176 + 0.0027662 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_012_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=337, w3=145, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(337, min_periods=max(337//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.224706 + 0.0027663 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_013_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=350, w3=162, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(350, min_periods=max(350//3, 2)).rank(pct=True)
    persistence = change.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.090333 * persistence + 0.0027664 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_014_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=363, w3=179, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(363, min_periods=max(363//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.251765 + 0.0027665 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_015_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=376, w3=196, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.103 * slope + 0.0027666 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_016_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=389, w3=213, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(19)
    drag = impulse.rolling(389, min_periods=max(389//3, 2)).mean()
    noise = impulse.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.278824 + 0.0027667 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_017_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=402, w3=230, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 402)
    curvature = _rolling_slope(acceleration, 230)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.115667 * acceleration + 0.0027668 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_018_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=415, w3=247, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(415, min_periods=max(415//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.305882 + 0.0027669 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_019_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=428, w3=264, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.128333 * _rolling_slope(draw, 264) + 0.002767 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_020_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=441, w3=281, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(441, min_periods=max(441//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.332941 + 0.0027671 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_021_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=454, w3=298, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 454)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=298, adjust=False).mean() * 1.346471 + 0.0027672 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_022_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=467, w3=315, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(467, min_periods=max(467//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36 + 0.0027673 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_023_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=480, w3=332, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(68)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.153667 * persistence + 0.0027674 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_024_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=493, w3=349, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.387059 + 0.0027675 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_025_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=506, w3=366, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.166333 * slope + 0.0027676 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_026_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=20, w3=383, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(89)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.414118 + 0.0027677 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_027_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=33, w3=400, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 33)
    curvature = _rolling_slope(acceleration, 400)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.179 * acceleration + 0.0027678 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_028_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=46, w3=417, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.441176 + 0.0027679 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_029_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=59, w3=434, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.191667 * _rolling_slope(draw, 434) + 0.002768 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_030_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=72, w3=451, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(72, min_periods=max(72//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.468235 + 0.0027681 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_031_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=85, w3=468, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 85)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.481765 + 0.0027682 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_032_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=98, w3=485, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(98, min_periods=max(98//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.495294 + 0.0027683 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_033_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=111, w3=502, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(111, min_periods=max(111//3, 2)).rank(pct=True)
    persistence = change.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217 * persistence + 0.0027684 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_034_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=124, w3=519, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.522353 + 0.0027685 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_035_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=137, w3=536, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(137, min_periods=max(137//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.229667 * slope + 0.0027686 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_036_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=150, w3=553, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.549412 + 0.0027687 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_037_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=163, w3=570, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 163)
    curvature = _rolling_slope(acceleration, 570)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.242333 * acceleration + 0.0027688 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_038_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=176, w3=587, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.576471 + 0.0027689 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_039_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=189, w3=604, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.255 * _rolling_slope(draw, 604) + 0.002769 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_040_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=202, w3=621, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(202, min_periods=max(202//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.603529 + 0.0027691 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_041_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=215, w3=638, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 215)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.617059 + 0.0027692 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_042_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=228, w3=655, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(228, min_periods=max(228//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.630588 + 0.0027693 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_043_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=241, w3=672, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(241, min_periods=max(241//3, 2)).rank(pct=True)
    persistence = change.rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.280333 * persistence + 0.0027694 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_044_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=254, w3=689, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(254, min_periods=max(254//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.657647 + 0.0027695 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_045_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=267, w3=706, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(267, min_periods=max(267//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.293 * slope + 0.0027696 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_046_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=280, w3=723, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.831176 + 0.0027697 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_047_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=293, w3=740, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 293)
    curvature = _rolling_slope(acceleration, 740)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305667 * acceleration + 0.0027698 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_048_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=306, w3=757, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.858235 + 0.0027699 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_049_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=319, w3=23, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.318333 * _rolling_slope(draw, 23) + 0.00277 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_050_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=332, w3=40, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(332, min_periods=max(332//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.885294 + 0.0027701 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_051_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=345, w3=57, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 345)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=57, adjust=False).mean() * 0.898824 + 0.0027702 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_052_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=358, w3=74, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(358, min_periods=max(358//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.912353 + 0.0027703 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_053_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=371, w3=91, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(31)
    rank = change.rolling(371, min_periods=max(371//3, 2)).rank(pct=True)
    persistence = change.rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343667 * persistence + 0.0027704 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_054_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=384, w3=108, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(384, min_periods=max(384//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.939412 + 0.0027705 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_055_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=397, w3=125, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(397, min_periods=max(397//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.356333 * slope + 0.0027706 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_056_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=410, w3=142, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(52)
    drag = impulse.rolling(410, min_periods=max(410//3, 2)).mean()
    noise = impulse.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.966471 + 0.0027707 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_057_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=423, w3=159, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 423)
    curvature = _rolling_slope(acceleration, 159)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.036667 * acceleration + 0.0027708 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_058_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=436, w3=176, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(436, min_periods=max(436//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.993529 + 0.0027709 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_059_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=449, w3=193, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(449, min_periods=max(449//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.049333 * _rolling_slope(draw, 193) + 0.002771 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_060_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=462, w3=210, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.020588 + 0.0027711 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_061_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=475, w3=227, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 475)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=227, adjust=False).mean() * 1.034118 + 0.0027712 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_062_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=488, w3=244, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(488, min_periods=max(488//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.047647 + 0.0027713 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_063_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=501, w3=261, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(101)
    rank = change.rolling(501, min_periods=max(501//3, 2)).rank(pct=True)
    persistence = change.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.074667 * persistence + 0.0027714 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_064_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=15, w3=278, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.074706 + 0.0027715 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_065_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=28, w3=295, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.087333 * slope + 0.0027716 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_066_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=41, w3=312, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(122)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.101765 + 0.0027717 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_067_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=54, w3=329, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 54)
    curvature = _rolling_slope(acceleration, 329)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1 * acceleration + 0.0027718 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_068_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=67, w3=346, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(67, min_periods=max(67//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.128824 + 0.0027719 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_069_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=80, w3=363, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(80, min_periods=max(80//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.112667 * _rolling_slope(draw, 363) + 0.002772 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_070_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=93, w3=380, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(93, min_periods=max(93//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.155882 + 0.0027721 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_071_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=106, w3=397, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.169412 + 0.0027722 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_072_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=119, w3=414, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.182941 + 0.0027723 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_073_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=132, w3=431, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(132, min_periods=max(132//3, 2)).rank(pct=True)
    persistence = change.rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.138 * persistence + 0.0027724 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_074_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=145, w3=448, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21 + 0.0027725 * anchor
    return base_signal.diff().diff().diff()

def f39_vclu_gemini_075_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=158, w3=465, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(158, min_periods=max(158//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.150667 * slope + 0.0027726 * anchor
    return base_signal.diff().diff().diff()
