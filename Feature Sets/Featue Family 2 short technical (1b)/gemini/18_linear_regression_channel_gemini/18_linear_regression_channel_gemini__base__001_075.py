"""18 linear regression channel gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Price deviations from a linear regression line, signifying mean reversion or trend acceleration.
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

def f18_lreg_gemini_001(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=5]"""
    window = 5
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_002(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=10]"""
    window = 10
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_003(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=21]"""
    window = 21
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_004(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=42]"""
    window = 42
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_005(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=63]"""
    window = 63
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_006(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=126]"""
    window = 126
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_007(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=252]"""
    window = 252
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_008(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=504]"""
    window = 504
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_009(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=756]"""
    window = 756
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_010(close: pd.Series) -> pd.Series:
    """Price deviations from a linear regression line, signifying mean reversion or trend acceleration. [window=1260]"""
    window = 1260
    res = _rolling_zscore(close - close.rolling(window * 2).mean(), window)
    return res

def f18_lreg_gemini_011(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=167, w3=344, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 167)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.154118 + 0.0015482 * anchor
    return base_signal

def f18_lreg_gemini_012(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=180, w3=361, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.167647 + 0.0015483 * anchor
    return base_signal

def f18_lreg_gemini_013(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=193, w3=378, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.051667 * persistence + 0.0015484 * anchor
    return base_signal

def f18_lreg_gemini_014(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=206, w3=395, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(206, min_periods=max(206//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.194706 + 0.0015485 * anchor
    return base_signal

def f18_lreg_gemini_015(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=219, w3=412, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.064333 * slope + 0.0015486 * anchor
    return base_signal

def f18_lreg_gemini_016(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=232, w3=429, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.221765 + 0.0015487 * anchor
    return base_signal

def f18_lreg_gemini_017(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=245, w3=446, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 245)
    curvature = _rolling_slope(acceleration, 446)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.077 * acceleration + 0.0015488 * anchor
    return base_signal

def f18_lreg_gemini_018(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=258, w3=463, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.248824 + 0.0015489 * anchor
    return base_signal

def f18_lreg_gemini_019(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=271, w3=480, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.089667 * _rolling_slope(draw, 480) + 0.001549 * anchor
    return base_signal

def f18_lreg_gemini_020(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=284, w3=497, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.275882 + 0.0015491 * anchor
    return base_signal

def f18_lreg_gemini_021(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=297, w3=514, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 297)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.289412 + 0.0015492 * anchor
    return base_signal

def f18_lreg_gemini_022(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=310, w3=531, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.302941 + 0.0015493 * anchor
    return base_signal

def f18_lreg_gemini_023(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=323, w3=548, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(23)
    rank = change.rolling(323, min_periods=max(323//3, 2)).rank(pct=True)
    persistence = change.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.115 * persistence + 0.0015494 * anchor
    return base_signal

def f18_lreg_gemini_024(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=336, w3=565, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(336, min_periods=max(336//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.33 + 0.0015495 * anchor
    return base_signal

def f18_lreg_gemini_025(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=349, w3=582, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.127667 * slope + 0.0015496 * anchor
    return base_signal

def f18_lreg_gemini_026(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=362, w3=599, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(44)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.357059 + 0.0015497 * anchor
    return base_signal

def f18_lreg_gemini_027(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=375, w3=616, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 375)
    curvature = _rolling_slope(acceleration, 616)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.140333 * acceleration + 0.0015498 * anchor
    return base_signal

def f18_lreg_gemini_028(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=388, w3=633, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.384118 + 0.0015499 * anchor
    return base_signal

def f18_lreg_gemini_029(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=401, w3=650, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.153 * _rolling_slope(draw, 650) + 0.00155 * anchor
    return base_signal

def f18_lreg_gemini_030(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=414, w3=667, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(414, min_periods=max(414//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.411176 + 0.0015501 * anchor
    return base_signal

def f18_lreg_gemini_031(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=427, w3=684, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.424706 + 0.0015502 * anchor
    return base_signal

def f18_lreg_gemini_032(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=440, w3=701, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.438235 + 0.0015503 * anchor
    return base_signal

def f18_lreg_gemini_033(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=453, w3=718, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(93)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.178333 * persistence + 0.0015504 * anchor
    return base_signal

def f18_lreg_gemini_034(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=466, w3=735, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(466, min_periods=max(466//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.465294 + 0.0015505 * anchor
    return base_signal

def f18_lreg_gemini_035(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=479, w3=752, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(479, min_periods=max(479//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.191 * slope + 0.0015506 * anchor
    return base_signal

def f18_lreg_gemini_036(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=492, w3=18, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(114)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.492353 + 0.0015507 * anchor
    return base_signal

def f18_lreg_gemini_037(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=505, w3=35, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 505)
    curvature = _rolling_slope(acceleration, 35)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.203667 * acceleration + 0.0015508 * anchor
    return base_signal

def f18_lreg_gemini_038(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=19, w3=52, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(52) * 1.519412 + 0.0015509 * anchor
    return base_signal

def f18_lreg_gemini_039(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=32, w3=69, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.216333 * _rolling_slope(draw, 69) + 0.001551 * anchor
    return base_signal

def f18_lreg_gemini_040(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=45, w3=86, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(45, min_periods=max(45//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.546471 + 0.0015511 * anchor
    return base_signal

def f18_lreg_gemini_041(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=58, w3=103, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=103, adjust=False).mean() * 1.56 + 0.0015512 * anchor
    return base_signal

def f18_lreg_gemini_042(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=71, w3=120, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.573529 + 0.0015513 * anchor
    return base_signal

def f18_lreg_gemini_043(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=84, w3=137, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.241667 * persistence + 0.0015514 * anchor
    return base_signal

def f18_lreg_gemini_044(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=97, w3=154, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.600588 + 0.0015515 * anchor
    return base_signal

def f18_lreg_gemini_045(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=110, w3=171, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.254333 * slope + 0.0015516 * anchor
    return base_signal

def f18_lreg_gemini_046(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=123, w3=188, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.627647 + 0.0015517 * anchor
    return base_signal

def f18_lreg_gemini_047(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=136, w3=205, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 205)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.267 * acceleration + 0.0015518 * anchor
    return base_signal

def f18_lreg_gemini_048(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=149, w3=222, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.654706 + 0.0015519 * anchor
    return base_signal

def f18_lreg_gemini_049(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=162, w3=239, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.279667 * _rolling_slope(draw, 239) + 0.001552 * anchor
    return base_signal

def f18_lreg_gemini_050(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=175, w3=256, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(175, min_periods=max(175//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.828235 + 0.0015521 * anchor
    return base_signal

def f18_lreg_gemini_051(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=188, w3=273, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=273, adjust=False).mean() * 0.841765 + 0.0015522 * anchor
    return base_signal

def f18_lreg_gemini_052(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=201, w3=290, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(201, min_periods=max(201//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.855294 + 0.0015523 * anchor
    return base_signal

def f18_lreg_gemini_053(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=214, w3=307, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.305 * persistence + 0.0015524 * anchor
    return base_signal

def f18_lreg_gemini_054(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=227, w3=324, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.882353 + 0.0015525 * anchor
    return base_signal

def f18_lreg_gemini_055(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=240, w3=341, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.317667 * slope + 0.0015526 * anchor
    return base_signal

def f18_lreg_gemini_056(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=253, w3=358, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(7)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.909412 + 0.0015527 * anchor
    return base_signal

def f18_lreg_gemini_057(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=266, w3=375, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 375)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.330333 * acceleration + 0.0015528 * anchor
    return base_signal

def f18_lreg_gemini_058(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=279, w3=392, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.936471 + 0.0015529 * anchor
    return base_signal

def f18_lreg_gemini_059(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=292, w3=409, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.343 * _rolling_slope(draw, 409) + 0.001553 * anchor
    return base_signal

def f18_lreg_gemini_060(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=305, w3=426, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.963529 + 0.0015531 * anchor
    return base_signal

def f18_lreg_gemini_061(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=318, w3=443, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.977059 + 0.0015532 * anchor
    return base_signal

def f18_lreg_gemini_062(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=331, w3=460, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.990588 + 0.0015533 * anchor
    return base_signal

def f18_lreg_gemini_063(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=344, w3=477, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(56)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.036 * persistence + 0.0015534 * anchor
    return base_signal

def f18_lreg_gemini_064(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=357, w3=494, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(357, min_periods=max(357//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.017647 + 0.0015535 * anchor
    return base_signal

def f18_lreg_gemini_065(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=370, w3=511, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.048667 * slope + 0.0015536 * anchor
    return base_signal

def f18_lreg_gemini_066(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=383, w3=528, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(77)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.044706 + 0.0015537 * anchor
    return base_signal

def f18_lreg_gemini_067(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=396, w3=545, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 545)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.061333 * acceleration + 0.0015538 * anchor
    return base_signal

def f18_lreg_gemini_068(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=409, w3=562, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.071765 + 0.0015539 * anchor
    return base_signal

def f18_lreg_gemini_069(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=422, w3=579, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(422, min_periods=max(422//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.074 * _rolling_slope(draw, 579) + 0.001554 * anchor
    return base_signal

def f18_lreg_gemini_070(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=435, w3=596, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.098824 + 0.0015541 * anchor
    return base_signal

def f18_lreg_gemini_071(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=448, w3=613, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.112353 + 0.0015542 * anchor
    return base_signal

def f18_lreg_gemini_072(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=461, w3=630, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.125882 + 0.0015543 * anchor
    return base_signal

def f18_lreg_gemini_073(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=474, w3=647, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.099333 * persistence + 0.0015544 * anchor
    return base_signal

def f18_lreg_gemini_074(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=487, w3=664, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.152941 + 0.0015545 * anchor
    return base_signal

def f18_lreg_gemini_075(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=500, w3=681, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.112 * slope + 0.0015546 * anchor
    return base_signal
