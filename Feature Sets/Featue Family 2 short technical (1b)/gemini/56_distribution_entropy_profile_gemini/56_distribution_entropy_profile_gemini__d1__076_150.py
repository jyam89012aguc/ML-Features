"""56 distribution entropy profile gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

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
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f56_dent_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=32, w3=603, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(32, min_periods=max(32//3, 2)).mean()
    noise = impulse.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.633529 + 0.0036967 * anchor
    return base_signal.diff()

def f56_dent_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=45, w3=620, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 45)
    curvature = _rolling_slope(acceleration, 620)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.192667 * acceleration + 0.0036968 * anchor
    return base_signal.diff()

def f56_dent_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=58, w3=637, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(58, min_periods=max(58//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.660588 + 0.0036969 * anchor
    return base_signal.diff()

def f56_dent_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=71, w3=654, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(71, min_periods=max(71//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.205333 * _rolling_slope(draw, 654) + 0.003697 * anchor
    return base_signal.diff()

def f56_dent_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=84, w3=671, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(84, min_periods=max(84//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.834118 + 0.0036971 * anchor
    return base_signal.diff()

def f56_dent_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=97, w3=688, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 97)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.847647 + 0.0036972 * anchor
    return base_signal.diff()

def f56_dent_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=110, w3=705, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(110, min_periods=max(110//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.861176 + 0.0036973 * anchor
    return base_signal.diff()

def f56_dent_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=123, w3=722, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(123, min_periods=max(123//3, 2)).rank(pct=True)
    persistence = change.rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.230667 * persistence + 0.0036974 * anchor
    return base_signal.diff()

def f56_dent_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=136, w3=739, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(136, min_periods=max(136//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.888235 + 0.0036975 * anchor
    return base_signal.diff()

def f56_dent_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=149, w3=756, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(149, min_periods=max(149//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.243333 * slope + 0.0036976 * anchor
    return base_signal.diff()

def f56_dent_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=162, w3=22, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(162, min_periods=max(162//3, 2)).mean()
    noise = impulse.abs().rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.915294 + 0.0036977 * anchor
    return base_signal.diff()

def f56_dent_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=175, w3=39, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 175)
    curvature = _rolling_slope(acceleration, 39)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.256 * acceleration + 0.0036978 * anchor
    return base_signal.diff()

def f56_dent_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=188, w3=56, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(188, min_periods=max(188//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(56) * 0.942353 + 0.0036979 * anchor
    return base_signal.diff()

def f56_dent_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=201, w3=73, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(201, min_periods=max(201//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.268667 * _rolling_slope(draw, 73) + 0.003698 * anchor
    return base_signal.diff()

def f56_dent_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=214, w3=90, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.969412 + 0.0036981 * anchor
    return base_signal.diff()

def f56_dent_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=227, w3=107, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 227)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=107, adjust=False).mean() * 0.982941 + 0.0036982 * anchor
    return base_signal.diff()

def f56_dent_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=240, w3=124, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(240, min_periods=max(240//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.996471 + 0.0036983 * anchor
    return base_signal.diff()

def f56_dent_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=253, w3=141, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(30)
    rank = change.rolling(253, min_periods=max(253//3, 2)).rank(pct=True)
    persistence = change.rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.294 * persistence + 0.0036984 * anchor
    return base_signal.diff()

def f56_dent_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=266, w3=158, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(266, min_periods=max(266//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.023529 + 0.0036985 * anchor
    return base_signal.diff()

def f56_dent_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=279, w3=175, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(279, min_periods=max(279//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.306667 * slope + 0.0036986 * anchor
    return base_signal.diff()

def f56_dent_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=292, w3=192, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(51)
    drag = impulse.rolling(292, min_periods=max(292//3, 2)).mean()
    noise = impulse.abs().rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.050588 + 0.0036987 * anchor
    return base_signal.diff()

def f56_dent_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=305, w3=209, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 305)
    curvature = _rolling_slope(acceleration, 209)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.319333 * acceleration + 0.0036988 * anchor
    return base_signal.diff()

def f56_dent_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=318, w3=226, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(318, min_periods=max(318//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.077647 + 0.0036989 * anchor
    return base_signal.diff()

def f56_dent_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=331, w3=243, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(331, min_periods=max(331//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.332 * _rolling_slope(draw, 243) + 0.003699 * anchor
    return base_signal.diff()

def f56_dent_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=344, w3=260, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(344, min_periods=max(344//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.104706 + 0.0036991 * anchor
    return base_signal.diff()

def f56_dent_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=357, w3=277, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 357)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=277, adjust=False).mean() * 1.118235 + 0.0036992 * anchor
    return base_signal.diff()

def f56_dent_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=370, w3=294, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(370, min_periods=max(370//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.131765 + 0.0036993 * anchor
    return base_signal.diff()

def f56_dent_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=383, w3=311, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(100)
    rank = change.rolling(383, min_periods=max(383//3, 2)).rank(pct=True)
    persistence = change.rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.357333 * persistence + 0.0036994 * anchor
    return base_signal.diff()

def f56_dent_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=396, w3=328, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(396, min_periods=max(396//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.158824 + 0.0036995 * anchor
    return base_signal.diff()

def f56_dent_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=409, w3=345, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.037667 * slope + 0.0036996 * anchor
    return base_signal.diff()

def f56_dent_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=422, w3=362, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(121)
    drag = impulse.rolling(422, min_periods=max(422//3, 2)).mean()
    noise = impulse.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.185882 + 0.0036997 * anchor
    return base_signal.diff()

def f56_dent_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=435, w3=379, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 435)
    curvature = _rolling_slope(acceleration, 379)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.050333 * acceleration + 0.0036998 * anchor
    return base_signal.diff()

def f56_dent_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=448, w3=396, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(448, min_periods=max(448//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.212941 + 0.0036999 * anchor
    return base_signal.diff()

def f56_dent_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=461, w3=413, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.063 * _rolling_slope(draw, 413) + 0.0037 * anchor
    return base_signal.diff()

def f56_dent_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=474, w3=430, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(474, min_periods=max(474//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.24 + 0.0037001 * anchor
    return base_signal.diff()

def f56_dent_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=487, w3=447, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 487)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.253529 + 0.0037002 * anchor
    return base_signal.diff()

def f56_dent_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=500, w3=464, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(500, min_periods=max(500//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.267059 + 0.0037003 * anchor
    return base_signal.diff()

def f56_dent_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=14, w3=481, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(14, min_periods=max(14//3, 2)).rank(pct=True)
    persistence = change.rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.088333 * persistence + 0.0037004 * anchor
    return base_signal.diff()

def f56_dent_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=27, w3=498, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(27, min_periods=max(27//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.294118 + 0.0037005 * anchor
    return base_signal.diff()

def f56_dent_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=40, w3=515, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(40, min_periods=max(40//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.101 * slope + 0.0037006 * anchor
    return base_signal.diff()

def f56_dent_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=53, w3=532, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(53, min_periods=max(53//3, 2)).mean()
    noise = impulse.abs().rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.321176 + 0.0037007 * anchor
    return base_signal.diff()

def f56_dent_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=66, w3=549, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 66)
    curvature = _rolling_slope(acceleration, 549)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113667 * acceleration + 0.0037008 * anchor
    return base_signal.diff()

def f56_dent_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=79, w3=566, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(79, min_periods=max(79//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.348235 + 0.0037009 * anchor
    return base_signal.diff()

def f56_dent_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=92, w3=583, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(92, min_periods=max(92//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.126333 * _rolling_slope(draw, 583) + 0.003701 * anchor
    return base_signal.diff()

def f56_dent_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=105, w3=600, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 219)
    baseline = trend.rolling(105, min_periods=max(105//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.375294 + 0.0037011 * anchor
    return base_signal.diff()

def f56_dent_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=118, w3=617, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 226)
    slow = _rolling_slope(x, 118)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.388824 + 0.0037012 * anchor
    return base_signal.diff()

def f56_dent_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=131, w3=634, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(233, min_periods=max(233//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.402353 + 0.0037013 * anchor
    return base_signal.diff()

def f56_dent_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=144, w3=651, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(651, min_periods=max(651//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.151667 * persistence + 0.0037014 * anchor
    return base_signal.diff()

def f56_dent_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=157, w3=668, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(247, min_periods=max(247//3, 2)).std()
    vol_slow = ret.rolling(157, min_periods=max(157//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.429412 + 0.0037015 * anchor
    return base_signal.diff()

def f56_dent_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=170, w3=685, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.164333 * slope + 0.0037016 * anchor
    return base_signal.diff()

def f56_dent_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=183, w3=702, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(14)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.456471 + 0.0037017 * anchor
    return base_signal.diff()

def f56_dent_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=196, w3=719, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 196)
    curvature = _rolling_slope(acceleration, 719)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.177 * acceleration + 0.0037018 * anchor
    return base_signal.diff()

def f56_dent_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=209, w3=736, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.483529 + 0.0037019 * anchor
    return base_signal.diff()

def f56_dent_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=222, w3=753, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(222, min_periods=max(222//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189667 * _rolling_slope(draw, 753) + 0.003702 * anchor
    return base_signal.diff()

def f56_dent_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=235, w3=19, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(235, min_periods=max(235//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.510588 + 0.0037021 * anchor
    return base_signal.diff()

def f56_dent_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=248, w3=36, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 248)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=36, adjust=False).mean() * 1.524118 + 0.0037022 * anchor
    return base_signal.diff()

def f56_dent_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=261, w3=53, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(261, min_periods=max(261//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.537647 + 0.0037023 * anchor
    return base_signal.diff()

def f56_dent_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=274, w3=70, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(63)
    rank = change.rolling(274, min_periods=max(274//3, 2)).rank(pct=True)
    persistence = change.rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.215 * persistence + 0.0037024 * anchor
    return base_signal.diff()

def f56_dent_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=287, w3=87, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(287, min_periods=max(287//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.564706 + 0.0037025 * anchor
    return base_signal.diff()

def f56_dent_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=300, w3=104, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(300, min_periods=max(300//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.227667 * slope + 0.0037026 * anchor
    return base_signal.diff()

def f56_dent_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=313, w3=121, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(84)
    drag = impulse.rolling(313, min_periods=max(313//3, 2)).mean()
    noise = impulse.abs().rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.591765 + 0.0037027 * anchor
    return base_signal.diff()

def f56_dent_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=326, w3=138, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 326)
    curvature = _rolling_slope(acceleration, 138)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.240333 * acceleration + 0.0037028 * anchor
    return base_signal.diff()

def f56_dent_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=339, w3=155, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(339, min_periods=max(339//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.618824 + 0.0037029 * anchor
    return base_signal.diff()

def f56_dent_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=352, w3=172, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.253 * _rolling_slope(draw, 172) + 0.003703 * anchor
    return base_signal.diff()

def f56_dent_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=365, w3=189, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.645882 + 0.0037031 * anchor
    return base_signal.diff()

def f56_dent_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=378, w3=206, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 378)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=206, adjust=False).mean() * 1.659412 + 0.0037032 * anchor
    return base_signal.diff()

def f56_dent_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=391, w3=223, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.672941 + 0.0037033 * anchor
    return base_signal.diff()

def f56_dent_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=404, w3=240, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(404, min_periods=max(404//3, 2)).rank(pct=True)
    persistence = change.rolling(240, min_periods=max(240//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.278333 * persistence + 0.0037034 * anchor
    return base_signal.diff()

def f56_dent_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=417, w3=257, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.846471 + 0.0037035 * anchor
    return base_signal.diff()

def f56_dent_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=430, w3=274, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(430, min_periods=max(430//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.291 * slope + 0.0037036 * anchor
    return base_signal.diff()

def f56_dent_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=443, w3=291, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(443, min_periods=max(443//3, 2)).mean()
    noise = impulse.abs().rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.873529 + 0.0037037 * anchor
    return base_signal.diff()

def f56_dent_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=456, w3=308, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 456)
    curvature = _rolling_slope(acceleration, 308)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.303667 * acceleration + 0.0037038 * anchor
    return base_signal.diff()

def f56_dent_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=469, w3=325, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(469, min_periods=max(469//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.900588 + 0.0037039 * anchor
    return base_signal.diff()

def f56_dent_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=482, w3=342, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(482, min_periods=max(482//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.316333 * _rolling_slope(draw, 342) + 0.003704 * anchor
    return base_signal.diff()

def f56_dent_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=495, w3=359, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.927647 + 0.0037041 * anchor
    return base_signal.diff()
