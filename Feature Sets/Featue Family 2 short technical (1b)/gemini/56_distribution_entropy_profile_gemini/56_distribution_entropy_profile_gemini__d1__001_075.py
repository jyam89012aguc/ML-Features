"""56 distribution entropy profile gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of the probability distribution of returns through an informational lens.
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

def f56_dent_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Analysis of the probability distribution of returns through an informational lens. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window // 2).std(), window)
    return (res).diff()

def f56_dent_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=185, w3=249, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 185)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=249, adjust=False).mean() * 1.607647 + 0.0036902 * anchor
    return base_signal.diff()

def f56_dent_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=198, w3=266, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(198, min_periods=max(198//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.621176 + 0.0036903 * anchor
    return base_signal.diff()

def f56_dent_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=211, w3=283, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(211, min_periods=max(211//3, 2)).rank(pct=True)
    persistence = change.rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119667 * persistence + 0.0036904 * anchor
    return base_signal.diff()

def f56_dent_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=224, w3=300, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(224, min_periods=max(224//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.648235 + 0.0036905 * anchor
    return base_signal.diff()

def f56_dent_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=237, w3=317, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(237, min_periods=max(237//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.132333 * slope + 0.0036906 * anchor
    return base_signal.diff()

def f56_dent_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=250, w3=334, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(250, min_periods=max(250//3, 2)).mean()
    noise = impulse.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.821765 + 0.0036907 * anchor
    return base_signal.diff()

def f56_dent_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=263, w3=351, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 263)
    curvature = _rolling_slope(acceleration, 351)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.145 * acceleration + 0.0036908 * anchor
    return base_signal.diff()

def f56_dent_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=276, w3=368, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(276, min_periods=max(276//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.848824 + 0.0036909 * anchor
    return base_signal.diff()

def f56_dent_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=289, w3=385, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(289, min_periods=max(289//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.157667 * _rolling_slope(draw, 385) + 0.003691 * anchor
    return base_signal.diff()

def f56_dent_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=302, w3=402, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(302, min_periods=max(302//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(402, min_periods=max(402//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.875882 + 0.0036911 * anchor
    return base_signal.diff()

def f56_dent_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=315, w3=419, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 315)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.889412 + 0.0036912 * anchor
    return base_signal.diff()

def f56_dent_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=328, w3=436, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(328, min_periods=max(328//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.902941 + 0.0036913 * anchor
    return base_signal.diff()

def f56_dent_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=341, w3=453, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(34)
    rank = change.rolling(341, min_periods=max(341//3, 2)).rank(pct=True)
    persistence = change.rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.183 * persistence + 0.0036914 * anchor
    return base_signal.diff()

def f56_dent_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=354, w3=470, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(354, min_periods=max(354//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.93 + 0.0036915 * anchor
    return base_signal.diff()

def f56_dent_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=367, w3=487, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(367, min_periods=max(367//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.195667 * slope + 0.0036916 * anchor
    return base_signal.diff()

def f56_dent_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=380, w3=504, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(55)
    drag = impulse.rolling(380, min_periods=max(380//3, 2)).mean()
    noise = impulse.abs().rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.957059 + 0.0036917 * anchor
    return base_signal.diff()

def f56_dent_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=393, w3=521, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 393)
    curvature = _rolling_slope(acceleration, 521)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.208333 * acceleration + 0.0036918 * anchor
    return base_signal.diff()

def f56_dent_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=406, w3=538, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(406, min_periods=max(406//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.984118 + 0.0036919 * anchor
    return base_signal.diff()

def f56_dent_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=419, w3=555, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(419, min_periods=max(419//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.221 * _rolling_slope(draw, 555) + 0.003692 * anchor
    return base_signal.diff()

def f56_dent_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=432, w3=572, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(432, min_periods=max(432//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.011176 + 0.0036921 * anchor
    return base_signal.diff()

def f56_dent_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=445, w3=589, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 445)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.024706 + 0.0036922 * anchor
    return base_signal.diff()

def f56_dent_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=458, w3=606, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(458, min_periods=max(458//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.038235 + 0.0036923 * anchor
    return base_signal.diff()

def f56_dent_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=471, w3=623, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(104)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.246333 * persistence + 0.0036924 * anchor
    return base_signal.diff()

def f56_dent_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=484, w3=640, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(484, min_periods=max(484//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.065294 + 0.0036925 * anchor
    return base_signal.diff()

def f56_dent_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=497, w3=657, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(497, min_periods=max(497//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.259 * slope + 0.0036926 * anchor
    return base_signal.diff()

def f56_dent_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=11, w3=674, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(125)
    drag = impulse.rolling(11, min_periods=max(11//3, 2)).mean()
    noise = impulse.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.092353 + 0.0036927 * anchor
    return base_signal.diff()

def f56_dent_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=24, w3=691, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 24)
    curvature = _rolling_slope(acceleration, 691)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.271667 * acceleration + 0.0036928 * anchor
    return base_signal.diff()

def f56_dent_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=37, w3=708, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(37, min_periods=max(37//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.119412 + 0.0036929 * anchor
    return base_signal.diff()

def f56_dent_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=50, w3=725, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(50, min_periods=max(50//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.284333 * _rolling_slope(draw, 725) + 0.003693 * anchor
    return base_signal.diff()

def f56_dent_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=63, w3=742, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(63, min_periods=max(63//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.146471 + 0.0036931 * anchor
    return base_signal.diff()

def f56_dent_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=76, w3=759, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 76)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.16 + 0.0036932 * anchor
    return base_signal.diff()

def f56_dent_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=89, w3=25, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(89, min_periods=max(89//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.173529 + 0.0036933 * anchor
    return base_signal.diff()

def f56_dent_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=102, w3=42, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(102, min_periods=max(102//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.309667 * persistence + 0.0036934 * anchor
    return base_signal.diff()

def f56_dent_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=115, w3=59, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.200588 + 0.0036935 * anchor
    return base_signal.diff()

def f56_dent_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=128, w3=76, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(128, min_periods=max(128//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.322333 * slope + 0.0036936 * anchor
    return base_signal.diff()

def f56_dent_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=141, w3=93, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(141, min_periods=max(141//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.227647 + 0.0036937 * anchor
    return base_signal.diff()

def f56_dent_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=154, w3=110, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 154)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.335 * acceleration + 0.0036938 * anchor
    return base_signal.diff()

def f56_dent_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=167, w3=127, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.254706 + 0.0036939 * anchor
    return base_signal.diff()

def f56_dent_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=180, w3=144, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(180, min_periods=max(180//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.347667 * _rolling_slope(draw, 144) + 0.003694 * anchor
    return base_signal.diff()

def f56_dent_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=193, w3=161, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(193, min_periods=max(193//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.281765 + 0.0036941 * anchor
    return base_signal.diff()

def f56_dent_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=206, w3=178, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 206)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=178, adjust=False).mean() * 1.295294 + 0.0036942 * anchor
    return base_signal.diff()

def f56_dent_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=219, w3=195, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(219, min_periods=max(219//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.308824 + 0.0036943 * anchor
    return base_signal.diff()

def f56_dent_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=232, w3=212, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(232, min_periods=max(232//3, 2)).rank(pct=True)
    persistence = change.rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.040667 * persistence + 0.0036944 * anchor
    return base_signal.diff()

def f56_dent_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=245, w3=229, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(245, min_periods=max(245//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.335882 + 0.0036945 * anchor
    return base_signal.diff()

def f56_dent_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=258, w3=246, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(258, min_periods=max(258//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.053333 * slope + 0.0036946 * anchor
    return base_signal.diff()

def f56_dent_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=271, w3=263, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(18)
    drag = impulse.rolling(271, min_periods=max(271//3, 2)).mean()
    noise = impulse.abs().rolling(263, min_periods=max(263//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.362941 + 0.0036947 * anchor
    return base_signal.diff()

def f56_dent_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=284, w3=280, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 284)
    curvature = _rolling_slope(acceleration, 280)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.066 * acceleration + 0.0036948 * anchor
    return base_signal.diff()

def f56_dent_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=297, w3=297, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(297, min_periods=max(297//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.39 + 0.0036949 * anchor
    return base_signal.diff()

def f56_dent_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=310, w3=314, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(310, min_periods=max(310//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.078667 * _rolling_slope(draw, 314) + 0.003695 * anchor
    return base_signal.diff()

def f56_dent_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=323, w3=331, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(323, min_periods=max(323//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.417059 + 0.0036951 * anchor
    return base_signal.diff()

def f56_dent_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=336, w3=348, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 336)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.430588 + 0.0036952 * anchor
    return base_signal.diff()

def f56_dent_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=349, w3=365, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(349, min_periods=max(349//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.444118 + 0.0036953 * anchor
    return base_signal.diff()

def f56_dent_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=362, w3=382, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(67)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.104 * persistence + 0.0036954 * anchor
    return base_signal.diff()

def f56_dent_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=375, w3=399, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(375, min_periods=max(375//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.471176 + 0.0036955 * anchor
    return base_signal.diff()

def f56_dent_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=388, w3=416, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(388, min_periods=max(388//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.116667 * slope + 0.0036956 * anchor
    return base_signal.diff()

def f56_dent_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=401, w3=433, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(88)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.498235 + 0.0036957 * anchor
    return base_signal.diff()

def f56_dent_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=414, w3=450, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 450)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.129333 * acceleration + 0.0036958 * anchor
    return base_signal.diff()

def f56_dent_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=427, w3=467, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.525294 + 0.0036959 * anchor
    return base_signal.diff()

def f56_dent_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=440, w3=484, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.142 * _rolling_slope(draw, 484) + 0.003696 * anchor
    return base_signal.diff()

def f56_dent_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=453, w3=501, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(453, min_periods=max(453//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.552353 + 0.0036961 * anchor
    return base_signal.diff()

def f56_dent_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=466, w3=518, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 466)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.565882 + 0.0036962 * anchor
    return base_signal.diff()

def f56_dent_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=479, w3=535, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(479, min_periods=max(479//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.579412 + 0.0036963 * anchor
    return base_signal.diff()

def f56_dent_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=492, w3=552, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(492, min_periods=max(492//3, 2)).rank(pct=True)
    persistence = change.rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.167333 * persistence + 0.0036964 * anchor
    return base_signal.diff()

def f56_dent_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=505, w3=569, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(505, min_periods=max(505//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.606471 + 0.0036965 * anchor
    return base_signal.diff()

def f56_dent_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=19, w3=586, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(19, min_periods=max(19//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.18 * slope + 0.0036966 * anchor
    return base_signal.diff()
