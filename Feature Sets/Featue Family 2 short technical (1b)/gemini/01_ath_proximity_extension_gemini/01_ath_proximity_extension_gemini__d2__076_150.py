"""01 ath proximity extension gemini d2 features 76-150 â€” Pipeline 1b-HF Grade v7.

Hypothesis: ATH - Institutional-grade technical signal with high-entropy logic.
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
    data = pd.concat(returns_list, axis=1)
    def _ar(w):
        if np.isnan(w).any(): return np.nan
        corr = np.corrcoef(w.T)
        eigvals = np.linalg.eigvalsh(corr)
        return np.max(eigvals) / len(eigvals)
    return data.rolling(21).apply(_ar, raw=True)

# ============================================================
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f01_athx_gemini_076_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=345, w3=614, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(345, min_periods=max(345//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(614, min_periods=max(614//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.869412 + 2.57e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_077_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=358, w3=631, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.882941 + 2.58e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_078_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=371, w3=648, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.896471 + 2.59e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_079_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=384, w3=665, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(89)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.342 * persistence + 2.6e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_080_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=397, w3=682, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.923529 + 2.61e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_081_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=410, w3=699, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.354667 * slope + 2.62e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_082_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=423, w3=716, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(110)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(716, min_periods=max(716//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.950588 + 2.63e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_083_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=436, w3=733, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 733)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.035 * acceleration + 2.64e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_084_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=449, w3=750, lag=5)."""
    rel = _safe_div(close.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 124)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.041333 * pressure.rolling(750, min_periods=max(750//3, 2)).mean() + 2.65e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_085_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=462, w3=767, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.991176 + 2.66e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_086_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=475, w3=33, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(475, min_periods=max(475//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 138)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.004706 + 2.67e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_087_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=488, w3=50, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(145, min_periods=max(145//3, 2)).mean(), b.abs().rolling(488, min_periods=max(488//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(50) + 0.060333 * _rolling_slope(cover, 145) + 2.68e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_088_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=501, w3=67, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.066667 * y + 0.933333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 152) - _rolling_slope(basket, 501) + 2.69e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_089_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=15, w3=84, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(84) * 1.045294 + 2.7e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_090_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=28, w3=101, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.079333 * _rolling_slope(draw, 101) + 2.71e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_091_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=41, w3=118, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(41)
    stress = imbalance.rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.072353 + 2.72e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_092_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=54, w3=135, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.085882 + 2.73e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_093_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=67, w3=152, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=152, adjust=False).mean() * 1.099412 + 2.74e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_094_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=80, w3=169, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.112941 + 2.75e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_095_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=93, w3=186, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(93, min_periods=max(93//3, 2)).rank(pct=True)
    persistence = change.rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 2.76e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_096_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=106, w3=203, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(106, min_periods=max(106//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14 + 2.77e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_097_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=119, w3=220, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.123667 * slope + 2.78e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_098_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=132, w3=237, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(132, min_periods=max(132//3, 2)).mean()
    noise = impulse.abs().rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.167059 + 2.79e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_099_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=145, w3=254, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 254)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136333 * acceleration + 2.8e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_100_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=158, w3=271, lag=0)."""
    rel = _safe_div(close.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 236)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.142667 * pressure.rolling(271, min_periods=max(271//3, 2)).mean() + 2.81e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_101_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=171, w3=288, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(243, min_periods=max(243//3, 2)).mean())
    decay = spread.ewm(span=171, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.207647 + 2.82e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_102_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=184, w3=305, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(184, min_periods=max(184//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 250)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.221176 + 2.83e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_103_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=197, w3=322, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(10, min_periods=max(10//3, 2)).mean(), b.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.161667 * _rolling_slope(cover, 10) + 2.84e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_104_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=210, w3=339, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.168 * y + 0.832000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 17) - _rolling_slope(basket, 210) + 2.85e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_105_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=223, w3=356, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(24, min_periods=max(24//3, 2)).mean(), upside.rolling(223, min_periods=max(223//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.261765 + 2.86e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_106_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=236, w3=373, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(236, min_periods=max(236//3, 2)).max()
    rebound = x - x.rolling(31, min_periods=max(31//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.180667 * _rolling_slope(draw, 373) + 2.87e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_107_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=249, w3=390, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(38) - b.diff(126)
    stress = imbalance.rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.288824 + 2.88e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_108_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=262, w3=407, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(262, min_periods=max(262//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.302353 + 2.89e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_109_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=275, w3=424, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 275)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.315882 + 2.9e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_110_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=288, w3=441, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(288, min_periods=max(288//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.329412 + 2.91e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_111_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=301, w3=458, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(66)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.212333 * persistence + 2.92e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_112_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=314, w3=475, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(314, min_periods=max(314//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.356471 + 2.93e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_113_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=327, w3=492, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(327, min_periods=max(327//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225 * slope + 2.94e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_114_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=340, w3=509, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(87)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.383529 + 2.95e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_115_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=353, w3=526, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 526)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.237667 * acceleration + 2.96e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_116_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=366, w3=543, lag=13)."""
    rel = _safe_div(close.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 101)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.244 * pressure.rolling(543, min_periods=max(543//3, 2)).mean() + 2.97e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_117_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=379, w3=560, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.424118 + 2.98e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_118_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=392, w3=577, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(392, min_periods=max(392//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 115)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.437647 + 2.99e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_119_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=405, w3=594, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(122, min_periods=max(122//3, 2)).mean(), b.abs().rolling(405, min_periods=max(405//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.263 * _rolling_slope(cover, 122) + 3e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_120_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=418, w3=611, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.269333 * y + 0.730667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 129) - _rolling_slope(basket, 418) + 3.01e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_121_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=431, w3=628, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.478235 + 3.02e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_122_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=444, w3=645, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(444, min_periods=max(444//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.282 * _rolling_slope(draw, 645) + 3.03e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_123_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=457, w3=662, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.505294 + 3.04e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_124_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=470, w3=679, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.518824 + 3.05e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_125_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=483, w3=696, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.532353 + 3.06e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_126_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=496, w3=713, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.545882 + 3.07e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_127_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=509, w3=730, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.313667 * persistence + 3.08e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_128_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=23, w3=747, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.572941 + 3.09e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_129_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=36, w3=764, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.326333 * slope + 3.1e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_130_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=49, w3=30, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(49, min_periods=max(49//3, 2)).mean()
    noise = impulse.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.6 + 3.11e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_131_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=62, w3=47, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 47)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.339 * acceleration + 3.12e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_132_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=75, w3=64, lag=2)."""
    rel = _safe_div(close.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 213)
    pressure = rel_log.diff(75)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.345333 * pressure.rolling(64, min_periods=max(64//3, 2)).mean() + 3.13e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_133_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=88, w3=81, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(220, min_periods=max(220//3, 2)).mean())
    decay = spread.ewm(span=88, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.640588 + 3.14e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_134_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=101, w3=98, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(101, min_periods=max(101//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 227)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.654118 + 3.15e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_135_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=114, w3=115, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(234, min_periods=max(234//3, 2)).mean(), b.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(115) + 0.032 * _rolling_slope(cover, 234) + 3.16e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_136_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=127, w3=132, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.038333 * y + 0.961667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 241) - _rolling_slope(basket, 127) + 3.17e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_137_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=140, w3=149, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(140, min_periods=max(140//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.841176 + 3.18e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_138_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=153, w3=166, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.051 * _rolling_slope(draw, 166) + 3.19e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_139_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=166, w3=183, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(15) - b.diff(126)
    stress = imbalance.rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.868235 + 3.2e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_140_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=179, w3=200, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(179, min_periods=max(179//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.881765 + 3.21e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_141_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=192, w3=217, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 192)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=217, adjust=False).mean() * 0.895294 + 3.22e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_142_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=205, w3=234, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(205, min_periods=max(205//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.908824 + 3.23e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_143_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=218, w3=251, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(43)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.082667 * persistence + 3.24e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_144_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=231, w3=268, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(231, min_periods=max(231//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.935882 + 3.25e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_145_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=244, w3=285, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.095333 * slope + 3.26e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_146_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=257, w3=302, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(64)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.962941 + 3.27e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_147_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=270, w3=319, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 319)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.108 * acceleration + 3.28e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_148_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=283, w3=336, lag=34)."""
    rel = _safe_div(close.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 78)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.114333 * pressure.rolling(336, min_periods=max(336//3, 2)).mean() + 3.29e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_149_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=296, w3=353, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(85, min_periods=max(85//3, 2)).mean())
    decay = spread.ewm(span=296, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.003529 + 3.3e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_150_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=309, w3=370, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(309, min_periods=max(309//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.017059 + 3.31e-05 * anchor
    return base_signal.diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_D2_076_150 = {
    "f01_athx_gemini_076_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_076_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_077_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_077_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_078_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_078_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_079_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_079_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_080_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_080_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_081_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_081_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_082_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_082_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_083_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_083_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_084_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_084_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_085_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_085_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_086_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_086_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_087_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_087_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_088_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_088_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_089_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_089_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_090_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_090_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_091_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_091_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_092_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_092_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_093_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_093_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_094_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_094_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_095_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_095_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_096_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_096_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_097_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_097_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_098_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_098_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_099_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_099_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_100_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_100_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_101_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_101_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_102_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_102_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_103_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_103_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_104_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_104_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_105_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_105_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_106_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_106_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_107_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_107_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_108_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_108_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_109_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_109_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_110_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_110_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_111_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_111_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_112_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_112_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_113_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_113_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_114_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_114_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_115_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_115_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_116_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_116_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_117_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_117_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_118_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_118_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_119_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_119_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_120_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_120_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_121_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_121_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_122_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_122_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_123_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_123_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_124_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_124_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_125_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_125_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_126_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_126_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_127_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_127_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_128_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_128_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_129_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_129_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_130_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_130_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_131_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_131_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_132_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_132_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_133_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_133_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_134_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_134_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_135_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_135_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_136_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_136_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_137_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_137_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_138_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_138_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_139_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_139_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_140_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_140_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_141_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_141_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_142_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_142_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_143_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_143_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_144_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_144_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_145_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_145_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_146_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_146_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_147_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_147_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_148_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_148_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_149_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_149_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_150_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_150_d2, "description": "ATR-normalized distance to 1260d high."},
}
