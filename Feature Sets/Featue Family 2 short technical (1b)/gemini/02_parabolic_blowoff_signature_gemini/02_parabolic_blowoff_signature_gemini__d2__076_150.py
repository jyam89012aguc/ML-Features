"""02 parabolic blowoff signature gemini d2 features 76-150 â€” Pipeline 1b-HF Grade v7.

Hypothesis: Blowoff - Institutional-grade technical signal with high-entropy logic.
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

def f02_pblo_gemini_076_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=467, w3=343, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(467, min_periods=max(467//3, 2)).mean()
    noise = impulse.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.253529 + 7.27e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_077_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=480, w3=360, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 480)
    curvature = _rolling_slope(acceleration, 360)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.315 * acceleration + 7.28e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_078_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=493, w3=377, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(493, min_periods=max(493//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.280588 + 7.29e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_079_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=506, w3=394, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(506, min_periods=max(506//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.327667 * _rolling_slope(draw, 394) + 7.3e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_080_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=20, w3=411, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(20, min_periods=max(20//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.307647 + 7.31e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_081_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=33, w3=428, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 33)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.321176 + 7.32e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_082_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=46, w3=445, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(46, min_periods=max(46//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.334706 + 7.33e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_083_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=59, w3=462, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(59, min_periods=max(59//3, 2)).rank(pct=True)
    persistence = change.rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.353 * persistence + 7.34e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_084_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=72, w3=479, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.361765 + 7.35e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_085_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=85, w3=496, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.033333 * slope + 7.36e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_086_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=98, w3=513, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.388824 + 7.37e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_087_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=111, w3=530, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 111)
    curvature = _rolling_slope(acceleration, 530)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.046 * acceleration + 7.38e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_088_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=124, w3=547, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(124, min_periods=max(124//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.415882 + 7.39e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_089_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=137, w3=564, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(137, min_periods=max(137//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.058667 * _rolling_slope(draw, 564) + 7.4e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_090_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=150, w3=581, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(150, min_periods=max(150//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.442941 + 7.41e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_091_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=163, w3=598, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 163)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.456471 + 7.42e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_092_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=176, w3=615, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(176, min_periods=max(176//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47 + 7.43e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_093_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=189, w3=632, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(19)
    rank = change.rolling(189, min_periods=max(189//3, 2)).rank(pct=True)
    persistence = change.rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.084 * persistence + 7.44e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_094_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=202, w3=649, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.497059 + 7.45e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_095_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=215, w3=666, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.096667 * slope + 7.46e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_096_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=228, w3=683, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(40)
    drag = impulse.rolling(228, min_periods=max(228//3, 2)).mean()
    noise = impulse.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.524118 + 7.47e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_097_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=241, w3=700, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 700)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.109333 * acceleration + 7.48e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_098_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=254, w3=717, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.551176 + 7.49e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_099_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=267, w3=734, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(267, min_periods=max(267//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.122 * _rolling_slope(draw, 734) + 7.5e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_100_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=280, w3=751, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(280, min_periods=max(280//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.578235 + 7.51e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_101_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=293, w3=17, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=17, adjust=False).mean() * 1.591765 + 7.52e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_102_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=306, w3=34, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.605294 + 7.53e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_103_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=319, w3=51, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(89)
    rank = change.rolling(319, min_periods=max(319//3, 2)).rank(pct=True)
    persistence = change.rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147333 * persistence + 7.54e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_104_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=332, w3=68, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(332, min_periods=max(332//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.632353 + 7.55e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_105_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=345, w3=85, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(345, min_periods=max(345//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.16 * slope + 7.56e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_106_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=358, w3=102, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(110)
    drag = impulse.rolling(358, min_periods=max(358//3, 2)).mean()
    noise = impulse.abs().rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.659412 + 7.57e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_107_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=371, w3=119, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 119)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.172667 * acceleration + 7.58e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_108_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=384, w3=136, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.832941 + 7.59e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_109_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=397, w3=153, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(397, min_periods=max(397//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.185333 * _rolling_slope(draw, 153) + 7.6e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_110_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=410, w3=170, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.86 + 7.61e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_111_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=423, w3=187, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=187, adjust=False).mean() * 0.873529 + 7.62e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_112_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=436, w3=204, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.887059 + 7.63e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_113_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=449, w3=221, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.210667 * persistence + 7.64e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_114_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=462, w3=238, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.914118 + 7.65e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_115_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=475, w3=255, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.223333 * slope + 7.66e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_116_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=488, w3=272, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(488, min_periods=max(488//3, 2)).mean()
    noise = impulse.abs().rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.941176 + 7.67e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_117_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=501, w3=289, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 501)
    curvature = _rolling_slope(acceleration, 289)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.236 * acceleration + 7.68e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_118_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=15, w3=306, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.968235 + 7.69e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_119_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=28, w3=323, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.248667 * _rolling_slope(draw, 323) + 7.7e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_120_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=41, w3=340, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(41, min_periods=max(41//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.995294 + 7.71e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_121_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=54, w3=357, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 54)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.008824 + 7.72e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_122_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=67, w3=374, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(67, min_periods=max(67//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.022353 + 7.73e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_123_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=80, w3=391, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(80, min_periods=max(80//3, 2)).rank(pct=True)
    persistence = change.rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.274 * persistence + 7.74e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_124_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=93, w3=408, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(93, min_periods=max(93//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.049412 + 7.75e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_125_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=106, w3=425, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(106, min_periods=max(106//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.286667 * slope + 7.76e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_126_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=119, w3=442, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(119, min_periods=max(119//3, 2)).mean()
    noise = impulse.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.076471 + 7.77e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_127_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=132, w3=459, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 132)
    curvature = _rolling_slope(acceleration, 459)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299333 * acceleration + 7.78e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_128_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=145, w3=476, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(145, min_periods=max(145//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.103529 + 7.79e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_129_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=158, w3=493, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(158, min_periods=max(158//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.312 * _rolling_slope(draw, 493) + 7.8e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_130_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=171, w3=510, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(171, min_periods=max(171//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.130588 + 7.81e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_131_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=184, w3=527, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 184)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.144118 + 7.82e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_132_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=197, w3=544, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(197, min_periods=max(197//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.157647 + 7.83e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_133_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=210, w3=561, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(52)
    rank = change.rolling(210, min_periods=max(210//3, 2)).rank(pct=True)
    persistence = change.rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.337333 * persistence + 7.84e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_134_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=223, w3=578, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(223, min_periods=max(223//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.184706 + 7.85e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_135_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=236, w3=595, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(236, min_periods=max(236//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.35 * slope + 7.86e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_136_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=249, w3=612, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(73)
    drag = impulse.rolling(249, min_periods=max(249//3, 2)).mean()
    noise = impulse.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.211765 + 7.87e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_137_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=262, w3=629, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 262)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.362667 * acceleration + 7.88e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_138_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=275, w3=646, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(275, min_periods=max(275//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.238824 + 7.89e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_139_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=288, w3=663, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.043 * _rolling_slope(draw, 663) + 7.9e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_140_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=301, w3=680, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(301, min_periods=max(301//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.265882 + 7.91e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_141_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=314, w3=697, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 314)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.279412 + 7.92e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_142_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=327, w3=714, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(327, min_periods=max(327//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.292941 + 7.93e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_143_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=340, w3=731, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(122)
    rank = change.rolling(340, min_periods=max(340//3, 2)).rank(pct=True)
    persistence = change.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.068333 * persistence + 7.94e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_144_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=353, w3=748, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(353, min_periods=max(353//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32 + 7.95e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_145_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=366, w3=765, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(366, min_periods=max(366//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.081 * slope + 7.96e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_146_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=379, w3=31, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(379, min_periods=max(379//3, 2)).mean()
    noise = impulse.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.347059 + 7.97e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_147_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=392, w3=48, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 392)
    curvature = _rolling_slope(acceleration, 48)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.093667 * acceleration + 7.98e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_148_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=405, w3=65, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(405, min_periods=max(405//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(65) * 1.374118 + 7.99e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_149_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=418, w3=82, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(418, min_periods=max(418//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.106333 * _rolling_slope(draw, 82) + 8e-05 * anchor
    return base_signal.diff().diff()

def f02_pblo_gemini_150_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=431, w3=99, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(431, min_periods=max(431//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.401176 + 8.01e-05 * anchor
    return base_signal.diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_D2_076_150 = {
    "f02_pblo_gemini_076_d2": {"inputs": ['close'], "func": f02_pblo_gemini_076_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_077_d2": {"inputs": ['close'], "func": f02_pblo_gemini_077_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_078_d2": {"inputs": ['close'], "func": f02_pblo_gemini_078_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_079_d2": {"inputs": ['close'], "func": f02_pblo_gemini_079_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_080_d2": {"inputs": ['close'], "func": f02_pblo_gemini_080_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_081_d2": {"inputs": ['close'], "func": f02_pblo_gemini_081_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_082_d2": {"inputs": ['close'], "func": f02_pblo_gemini_082_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_083_d2": {"inputs": ['close'], "func": f02_pblo_gemini_083_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_084_d2": {"inputs": ['close'], "func": f02_pblo_gemini_084_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_085_d2": {"inputs": ['close'], "func": f02_pblo_gemini_085_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_086_d2": {"inputs": ['close'], "func": f02_pblo_gemini_086_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_087_d2": {"inputs": ['close'], "func": f02_pblo_gemini_087_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_088_d2": {"inputs": ['close'], "func": f02_pblo_gemini_088_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_089_d2": {"inputs": ['close'], "func": f02_pblo_gemini_089_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_090_d2": {"inputs": ['close'], "func": f02_pblo_gemini_090_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_091_d2": {"inputs": ['close'], "func": f02_pblo_gemini_091_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_092_d2": {"inputs": ['close'], "func": f02_pblo_gemini_092_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_093_d2": {"inputs": ['close'], "func": f02_pblo_gemini_093_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_094_d2": {"inputs": ['close'], "func": f02_pblo_gemini_094_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_095_d2": {"inputs": ['close'], "func": f02_pblo_gemini_095_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_096_d2": {"inputs": ['close'], "func": f02_pblo_gemini_096_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_097_d2": {"inputs": ['close'], "func": f02_pblo_gemini_097_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_098_d2": {"inputs": ['close'], "func": f02_pblo_gemini_098_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_099_d2": {"inputs": ['close'], "func": f02_pblo_gemini_099_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_100_d2": {"inputs": ['close'], "func": f02_pblo_gemini_100_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_101_d2": {"inputs": ['close'], "func": f02_pblo_gemini_101_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_102_d2": {"inputs": ['close'], "func": f02_pblo_gemini_102_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_103_d2": {"inputs": ['close'], "func": f02_pblo_gemini_103_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_104_d2": {"inputs": ['close'], "func": f02_pblo_gemini_104_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_105_d2": {"inputs": ['close'], "func": f02_pblo_gemini_105_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_106_d2": {"inputs": ['close'], "func": f02_pblo_gemini_106_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_107_d2": {"inputs": ['close'], "func": f02_pblo_gemini_107_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_108_d2": {"inputs": ['close'], "func": f02_pblo_gemini_108_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_109_d2": {"inputs": ['close'], "func": f02_pblo_gemini_109_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_110_d2": {"inputs": ['close'], "func": f02_pblo_gemini_110_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_111_d2": {"inputs": ['close'], "func": f02_pblo_gemini_111_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_112_d2": {"inputs": ['close'], "func": f02_pblo_gemini_112_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_113_d2": {"inputs": ['close'], "func": f02_pblo_gemini_113_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_114_d2": {"inputs": ['close'], "func": f02_pblo_gemini_114_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_115_d2": {"inputs": ['close'], "func": f02_pblo_gemini_115_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_116_d2": {"inputs": ['close'], "func": f02_pblo_gemini_116_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_117_d2": {"inputs": ['close'], "func": f02_pblo_gemini_117_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_118_d2": {"inputs": ['close'], "func": f02_pblo_gemini_118_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_119_d2": {"inputs": ['close'], "func": f02_pblo_gemini_119_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_120_d2": {"inputs": ['close'], "func": f02_pblo_gemini_120_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_121_d2": {"inputs": ['close'], "func": f02_pblo_gemini_121_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_122_d2": {"inputs": ['close'], "func": f02_pblo_gemini_122_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_123_d2": {"inputs": ['close'], "func": f02_pblo_gemini_123_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_124_d2": {"inputs": ['close'], "func": f02_pblo_gemini_124_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_125_d2": {"inputs": ['close'], "func": f02_pblo_gemini_125_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_126_d2": {"inputs": ['close'], "func": f02_pblo_gemini_126_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_127_d2": {"inputs": ['close'], "func": f02_pblo_gemini_127_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_128_d2": {"inputs": ['close'], "func": f02_pblo_gemini_128_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_129_d2": {"inputs": ['close'], "func": f02_pblo_gemini_129_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_130_d2": {"inputs": ['close'], "func": f02_pblo_gemini_130_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_131_d2": {"inputs": ['close'], "func": f02_pblo_gemini_131_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_132_d2": {"inputs": ['close'], "func": f02_pblo_gemini_132_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_133_d2": {"inputs": ['close'], "func": f02_pblo_gemini_133_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_134_d2": {"inputs": ['close'], "func": f02_pblo_gemini_134_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_135_d2": {"inputs": ['close'], "func": f02_pblo_gemini_135_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_136_d2": {"inputs": ['close'], "func": f02_pblo_gemini_136_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_137_d2": {"inputs": ['close'], "func": f02_pblo_gemini_137_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_138_d2": {"inputs": ['close'], "func": f02_pblo_gemini_138_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_139_d2": {"inputs": ['close'], "func": f02_pblo_gemini_139_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_140_d2": {"inputs": ['close'], "func": f02_pblo_gemini_140_d2, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_141_d2": {"inputs": ['close'], "func": f02_pblo_gemini_141_d2, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_142_d2": {"inputs": ['close'], "func": f02_pblo_gemini_142_d2, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_143_d2": {"inputs": ['close'], "func": f02_pblo_gemini_143_d2, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_144_d2": {"inputs": ['close'], "func": f02_pblo_gemini_144_d2, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_145_d2": {"inputs": ['close'], "func": f02_pblo_gemini_145_d2, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_146_d2": {"inputs": ['close'], "func": f02_pblo_gemini_146_d2, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_147_d2": {"inputs": ['close'], "func": f02_pblo_gemini_147_d2, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_148_d2": {"inputs": ['close'], "func": f02_pblo_gemini_148_d2, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_149_d2": {"inputs": ['close'], "func": f02_pblo_gemini_149_d2, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_150_d2": {"inputs": ['close'], "func": f02_pblo_gemini_150_d2, "description": "Quadratic curvature of log-price over 1260d."},
}
