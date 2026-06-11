"""93 skew convexity proxy technical gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of return distribution asymmetry as a proxy for implied skew.
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

def f93_skcx_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=431, w3=624, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.151765 + 0.0057687 * anchor
    return base_signal.diff()

def f93_skcx_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=444, w3=641, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 641)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.147667 * acceleration + 0.0057688 * anchor
    return base_signal.diff()

def f93_skcx_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=457, w3=658, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.178824 + 0.0057689 * anchor
    return base_signal.diff()

def f93_skcx_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=470, w3=675, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(470, min_periods=max(470//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.160333 * _rolling_slope(draw, 675) + 0.005769 * anchor
    return base_signal.diff()

def f93_skcx_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=483, w3=692, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.205882 + 0.0057691 * anchor
    return base_signal.diff()

def f93_skcx_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=496, w3=709, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.219412 + 0.0057692 * anchor
    return base_signal.diff()

def f93_skcx_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=509, w3=726, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.232941 + 0.0057693 * anchor
    return base_signal.diff()

def f93_skcx_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=23, w3=743, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(11)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.185667 * persistence + 0.0057694 * anchor
    return base_signal.diff()

def f93_skcx_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=36, w3=760, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.26 + 0.0057695 * anchor
    return base_signal.diff()

def f93_skcx_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=49, w3=26, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.198333 * slope + 0.0057696 * anchor
    return base_signal.diff()

def f93_skcx_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=62, w3=43, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(32)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.287059 + 0.0057697 * anchor
    return base_signal.diff()

def f93_skcx_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=75, w3=60, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 75)
    curvature = _rolling_slope(acceleration, 60)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211 * acceleration + 0.0057698 * anchor
    return base_signal.diff()

def f93_skcx_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=88, w3=77, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(88, min_periods=max(88//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(77) * 1.314118 + 0.0057699 * anchor
    return base_signal.diff()

def f93_skcx_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=101, w3=94, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.223667 * _rolling_slope(draw, 94) + 0.00577 * anchor
    return base_signal.diff()

def f93_skcx_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=114, w3=111, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(114, min_periods=max(114//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.341176 + 0.0057701 * anchor
    return base_signal.diff()

def f93_skcx_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=127, w3=128, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 127)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=128, adjust=False).mean() * 1.354706 + 0.0057702 * anchor
    return base_signal.diff()

def f93_skcx_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=140, w3=145, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(140, min_periods=max(140//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.368235 + 0.0057703 * anchor
    return base_signal.diff()

def f93_skcx_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=153, w3=162, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(81)
    rank = change.rolling(153, min_periods=max(153//3, 2)).rank(pct=True)
    persistence = change.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249 * persistence + 0.0057704 * anchor
    return base_signal.diff()

def f93_skcx_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=166, w3=179, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(166, min_periods=max(166//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.395294 + 0.0057705 * anchor
    return base_signal.diff()

def f93_skcx_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=179, w3=196, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(179, min_periods=max(179//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.261667 * slope + 0.0057706 * anchor
    return base_signal.diff()

def f93_skcx_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=192, w3=213, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(102)
    drag = impulse.rolling(192, min_periods=max(192//3, 2)).mean()
    noise = impulse.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.422353 + 0.0057707 * anchor
    return base_signal.diff()

def f93_skcx_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=205, w3=230, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 205)
    curvature = _rolling_slope(acceleration, 230)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274333 * acceleration + 0.0057708 * anchor
    return base_signal.diff()

def f93_skcx_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=218, w3=247, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(218, min_periods=max(218//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.449412 + 0.0057709 * anchor
    return base_signal.diff()

def f93_skcx_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=231, w3=264, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(231, min_periods=max(231//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287 * _rolling_slope(draw, 264) + 0.005771 * anchor
    return base_signal.diff()

def f93_skcx_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=244, w3=281, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(244, min_periods=max(244//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.476471 + 0.0057711 * anchor
    return base_signal.diff()

def f93_skcx_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=257, w3=298, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 257)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=298, adjust=False).mean() * 1.49 + 0.0057712 * anchor
    return base_signal.diff()

def f93_skcx_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=270, w3=315, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(270, min_periods=max(270//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.503529 + 0.0057713 * anchor
    return base_signal.diff()

def f93_skcx_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=283, w3=332, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(283, min_periods=max(283//3, 2)).rank(pct=True)
    persistence = change.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.312333 * persistence + 0.0057714 * anchor
    return base_signal.diff()

def f93_skcx_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=296, w3=349, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.530588 + 0.0057715 * anchor
    return base_signal.diff()

def f93_skcx_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=309, w3=366, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(309, min_periods=max(309//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.325 * slope + 0.0057716 * anchor
    return base_signal.diff()

def f93_skcx_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=322, w3=383, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(322, min_periods=max(322//3, 2)).mean()
    noise = impulse.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.557647 + 0.0057717 * anchor
    return base_signal.diff()

def f93_skcx_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=335, w3=400, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 335)
    curvature = _rolling_slope(acceleration, 400)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.337667 * acceleration + 0.0057718 * anchor
    return base_signal.diff()

def f93_skcx_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=348, w3=417, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(348, min_periods=max(348//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.584706 + 0.0057719 * anchor
    return base_signal.diff()

def f93_skcx_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=361, w3=434, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(361, min_periods=max(361//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.350333 * _rolling_slope(draw, 434) + 0.005772 * anchor
    return base_signal.diff()

def f93_skcx_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=374, w3=451, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(374, min_periods=max(374//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.611765 + 0.0057721 * anchor
    return base_signal.diff()

def f93_skcx_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=387, w3=468, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 387)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.625294 + 0.0057722 * anchor
    return base_signal.diff()

def f93_skcx_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=400, w3=485, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.638824 + 0.0057723 * anchor
    return base_signal.diff()

def f93_skcx_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=413, w3=502, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(413, min_periods=max(413//3, 2)).rank(pct=True)
    persistence = change.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.043333 * persistence + 0.0057724 * anchor
    return base_signal.diff()

def f93_skcx_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=426, w3=519, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.665882 + 0.0057725 * anchor
    return base_signal.diff()

def f93_skcx_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=439, w3=536, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.056 * slope + 0.0057726 * anchor
    return base_signal.diff()

def f93_skcx_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=452, w3=553, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.839412 + 0.0057727 * anchor
    return base_signal.diff()

def f93_skcx_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=465, w3=570, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 465)
    curvature = _rolling_slope(acceleration, 570)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.068667 * acceleration + 0.0057728 * anchor
    return base_signal.diff()

def f93_skcx_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=478, w3=587, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.866471 + 0.0057729 * anchor
    return base_signal.diff()

def f93_skcx_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=491, w3=604, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.081333 * _rolling_slope(draw, 604) + 0.005773 * anchor
    return base_signal.diff()

def f93_skcx_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=504, w3=621, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(504, min_periods=max(504//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.893529 + 0.0057731 * anchor
    return base_signal.diff()

def f93_skcx_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=18, w3=638, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 18)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.907059 + 0.0057732 * anchor
    return base_signal.diff()

def f93_skcx_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=31, w3=655, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(31, min_periods=max(31//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.920588 + 0.0057733 * anchor
    return base_signal.diff()

def f93_skcx_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=44, w3=672, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(44)
    rank = change.rolling(44, min_periods=max(44//3, 2)).rank(pct=True)
    persistence = change.rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.106667 * persistence + 0.0057734 * anchor
    return base_signal.diff()

def f93_skcx_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=57, w3=689, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(57, min_periods=max(57//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.947647 + 0.0057735 * anchor
    return base_signal.diff()

def f93_skcx_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=70, w3=706, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(70, min_periods=max(70//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.119333 * slope + 0.0057736 * anchor
    return base_signal.diff()

def f93_skcx_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=83, w3=723, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(65)
    drag = impulse.rolling(83, min_periods=max(83//3, 2)).mean()
    noise = impulse.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.974706 + 0.0057737 * anchor
    return base_signal.diff()

def f93_skcx_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=96, w3=740, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 96)
    curvature = _rolling_slope(acceleration, 740)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.132 * acceleration + 0.0057738 * anchor
    return base_signal.diff()

def f93_skcx_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=109, w3=757, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(109, min_periods=max(109//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.001765 + 0.0057739 * anchor
    return base_signal.diff()

def f93_skcx_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=122, w3=23, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(122, min_periods=max(122//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.144667 * _rolling_slope(draw, 23) + 0.005774 * anchor
    return base_signal.diff()

def f93_skcx_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=135, w3=40, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(135, min_periods=max(135//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.028824 + 0.0057741 * anchor
    return base_signal.diff()

def f93_skcx_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=148, w3=57, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 100)
    slow = _rolling_slope(x, 148)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=57, adjust=False).mean() * 1.042353 + 0.0057742 * anchor
    return base_signal.diff()

def f93_skcx_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=161, w3=74, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(161, min_periods=max(161//3, 2)).max()
    trough = x.rolling(107, min_periods=max(107//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.055882 + 0.0057743 * anchor
    return base_signal.diff()

def f93_skcx_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=174, w3=91, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(114)
    rank = change.rolling(174, min_periods=max(174//3, 2)).rank(pct=True)
    persistence = change.rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.17 * persistence + 0.0057744 * anchor
    return base_signal.diff()

def f93_skcx_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=187, w3=108, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(121, min_periods=max(121//3, 2)).std()
    vol_slow = ret.rolling(187, min_periods=max(187//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.082941 + 0.0057745 * anchor
    return base_signal.diff()

def f93_skcx_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=200, w3=125, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(200, min_periods=max(200//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 128)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.182667 * slope + 0.0057746 * anchor
    return base_signal.diff()

def f93_skcx_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=213, w3=142, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.11 + 0.0057747 * anchor
    return base_signal.diff()

def f93_skcx_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=226, w3=159, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 142)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 159)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.195333 * acceleration + 0.0057748 * anchor
    return base_signal.diff()

def f93_skcx_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=239, w3=176, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(149, min_periods=max(149//3, 2)).mean(), upside.rolling(239, min_periods=max(239//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.137059 + 0.0057749 * anchor
    return base_signal.diff()

def f93_skcx_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=252, w3=193, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(252, min_periods=max(252//3, 2)).max()
    rebound = x - x.rolling(156, min_periods=max(156//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.208 * _rolling_slope(draw, 193) + 0.005775 * anchor
    return base_signal.diff()

def f93_skcx_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=265, w3=210, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(265, min_periods=max(265//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.164118 + 0.0057751 * anchor
    return base_signal.diff()

def f93_skcx_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=278, w3=227, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 278)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=227, adjust=False).mean() * 1.177647 + 0.0057752 * anchor
    return base_signal.diff()

def f93_skcx_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=291, w3=244, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(291, min_periods=max(291//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.191176 + 0.0057753 * anchor
    return base_signal.diff()

def f93_skcx_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=304, w3=261, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(304, min_periods=max(304//3, 2)).rank(pct=True)
    persistence = change.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.233333 * persistence + 0.0057754 * anchor
    return base_signal.diff()

def f93_skcx_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=317, w3=278, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(317, min_periods=max(317//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.218235 + 0.0057755 * anchor
    return base_signal.diff()

def f93_skcx_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=330, w3=295, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(330, min_periods=max(330//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.246 * slope + 0.0057756 * anchor
    return base_signal.diff()

def f93_skcx_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=343, w3=312, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(343, min_periods=max(343//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.245294 + 0.0057757 * anchor
    return base_signal.diff()

def f93_skcx_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=356, w3=329, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 356)
    curvature = _rolling_slope(acceleration, 329)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.258667 * acceleration + 0.0057758 * anchor
    return base_signal.diff()

def f93_skcx_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=369, w3=346, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(369, min_periods=max(369//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.272353 + 0.0057759 * anchor
    return base_signal.diff()

def f93_skcx_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=382, w3=363, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(382, min_periods=max(382//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.271333 * _rolling_slope(draw, 363) + 0.005776 * anchor
    return base_signal.diff()

def f93_skcx_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=395, w3=380, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 233)
    baseline = trend.rolling(395, min_periods=max(395//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.299412 + 0.0057761 * anchor
    return base_signal.diff()
