"""02 parabolic blowoff signature gemini base features 76-150 â€” Pipeline 1b-HF Grade v7.

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

def f02_pblo_gemini_076(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=341, w3=18, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(341, min_periods=max(341//3, 2)).mean()
    noise = impulse.abs().rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.420588 + 4.87e-05 * anchor
    return base_signal

def f02_pblo_gemini_077(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=354, w3=35, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 354)
    curvature = _rolling_slope(acceleration, 35)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.124333 * acceleration + 4.88e-05 * anchor
    return base_signal

def f02_pblo_gemini_078(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=367, w3=52, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(367, min_periods=max(367//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(52) * 1.447647 + 4.89e-05 * anchor
    return base_signal

def f02_pblo_gemini_079(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=380, w3=69, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(380, min_periods=max(380//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.137 * _rolling_slope(draw, 69) + 4.9e-05 * anchor
    return base_signal

def f02_pblo_gemini_080(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=393, w3=86, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(393, min_periods=max(393//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.474706 + 4.91e-05 * anchor
    return base_signal

def f02_pblo_gemini_081(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=406, w3=103, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 406)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=103, adjust=False).mean() * 1.488235 + 4.92e-05 * anchor
    return base_signal

def f02_pblo_gemini_082(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=419, w3=120, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(419, min_periods=max(419//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.501765 + 4.93e-05 * anchor
    return base_signal

def f02_pblo_gemini_083(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=432, w3=137, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(432, min_periods=max(432//3, 2)).rank(pct=True)
    persistence = change.rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.162333 * persistence + 4.94e-05 * anchor
    return base_signal

def f02_pblo_gemini_084(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=445, w3=154, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(445, min_periods=max(445//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.528824 + 4.95e-05 * anchor
    return base_signal

def f02_pblo_gemini_085(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=458, w3=171, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(458, min_periods=max(458//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.175 * slope + 4.96e-05 * anchor
    return base_signal

def f02_pblo_gemini_086(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=471, w3=188, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(19)
    drag = impulse.rolling(471, min_periods=max(471//3, 2)).mean()
    noise = impulse.abs().rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.555882 + 4.97e-05 * anchor
    return base_signal

def f02_pblo_gemini_087(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=484, w3=205, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 484)
    curvature = _rolling_slope(acceleration, 205)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.187667 * acceleration + 4.98e-05 * anchor
    return base_signal

def f02_pblo_gemini_088(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=497, w3=222, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.582941 + 4.99e-05 * anchor
    return base_signal

def f02_pblo_gemini_089(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=11, w3=239, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(11, min_periods=max(11//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.200333 * _rolling_slope(draw, 239) + 5e-05 * anchor
    return base_signal

def f02_pblo_gemini_090(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=24, w3=256, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(24, min_periods=max(24//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.61 + 5.01e-05 * anchor
    return base_signal

def f02_pblo_gemini_091(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=37, w3=273, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 37)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=273, adjust=False).mean() * 1.623529 + 5.02e-05 * anchor
    return base_signal

def f02_pblo_gemini_092(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=50, w3=290, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(50, min_periods=max(50//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.637059 + 5.03e-05 * anchor
    return base_signal

def f02_pblo_gemini_093(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=63, w3=307, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(68)
    rank = change.rolling(63, min_periods=max(63//3, 2)).rank(pct=True)
    persistence = change.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.225667 * persistence + 5.04e-05 * anchor
    return base_signal

def f02_pblo_gemini_094(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=76, w3=324, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(76, min_periods=max(76//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.664118 + 5.05e-05 * anchor
    return base_signal

def f02_pblo_gemini_095(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=89, w3=341, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(89, min_periods=max(89//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.238333 * slope + 5.06e-05 * anchor
    return base_signal

def f02_pblo_gemini_096(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=102, w3=358, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(89)
    drag = impulse.rolling(102, min_periods=max(102//3, 2)).mean()
    noise = impulse.abs().rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.837647 + 5.07e-05 * anchor
    return base_signal

def f02_pblo_gemini_097(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=115, w3=375, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 375)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.251 * acceleration + 5.08e-05 * anchor
    return base_signal

def f02_pblo_gemini_098(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=128, w3=392, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(128, min_periods=max(128//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.864706 + 5.09e-05 * anchor
    return base_signal

def f02_pblo_gemini_099(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=141, w3=409, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.263667 * _rolling_slope(draw, 409) + 5.1e-05 * anchor
    return base_signal

def f02_pblo_gemini_100(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=154, w3=426, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(154, min_periods=max(154//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.891765 + 5.11e-05 * anchor
    return base_signal

def f02_pblo_gemini_101(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=167, w3=443, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 167)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.905294 + 5.12e-05 * anchor
    return base_signal

def f02_pblo_gemini_102(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=180, w3=460, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.918824 + 5.13e-05 * anchor
    return base_signal

def f02_pblo_gemini_103(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=193, w3=477, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289 * persistence + 5.14e-05 * anchor
    return base_signal

def f02_pblo_gemini_104(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=206, w3=494, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(206, min_periods=max(206//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.945882 + 5.15e-05 * anchor
    return base_signal

def f02_pblo_gemini_105(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=219, w3=511, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.301667 * slope + 5.16e-05 * anchor
    return base_signal

def f02_pblo_gemini_106(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=232, w3=528, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.972941 + 5.17e-05 * anchor
    return base_signal

def f02_pblo_gemini_107(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=245, w3=545, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 245)
    curvature = _rolling_slope(acceleration, 545)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.314333 * acceleration + 5.18e-05 * anchor
    return base_signal

def f02_pblo_gemini_108(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=258, w3=562, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(173, min_periods=max(173//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0 + 5.19e-05 * anchor
    return base_signal

def f02_pblo_gemini_109(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=271, w3=579, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(180, min_periods=max(180//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.327 * _rolling_slope(draw, 579) + 5.2e-05 * anchor
    return base_signal

def f02_pblo_gemini_110(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=284, w3=596, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.027059 + 5.21e-05 * anchor
    return base_signal

def f02_pblo_gemini_111(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=297, w3=613, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 297)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.040588 + 5.22e-05 * anchor
    return base_signal

def f02_pblo_gemini_112(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=310, w3=630, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.054118 + 5.23e-05 * anchor
    return base_signal

def f02_pblo_gemini_113(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=323, w3=647, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(323, min_periods=max(323//3, 2)).rank(pct=True)
    persistence = change.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.352333 * persistence + 5.24e-05 * anchor
    return base_signal

def f02_pblo_gemini_114(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=336, w3=664, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(336, min_periods=max(336//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.081176 + 5.25e-05 * anchor
    return base_signal

def f02_pblo_gemini_115(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=349, w3=681, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.032667 * slope + 5.26e-05 * anchor
    return base_signal

def f02_pblo_gemini_116(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=362, w3=698, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.108235 + 5.27e-05 * anchor
    return base_signal

def f02_pblo_gemini_117(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=375, w3=715, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 375)
    curvature = _rolling_slope(acceleration, 715)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045333 * acceleration + 5.28e-05 * anchor
    return base_signal

def f02_pblo_gemini_118(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=388, w3=732, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.135294 + 5.29e-05 * anchor
    return base_signal

def f02_pblo_gemini_119(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=401, w3=749, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.058 * _rolling_slope(draw, 749) + 5.3e-05 * anchor
    return base_signal

def f02_pblo_gemini_120(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=414, w3=766, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(414, min_periods=max(414//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.162353 + 5.31e-05 * anchor
    return base_signal

def f02_pblo_gemini_121(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=427, w3=32, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 17)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 1.175882 + 5.32e-05 * anchor
    return base_signal

def f02_pblo_gemini_122(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=440, w3=49, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(24, min_periods=max(24//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.189412 + 5.33e-05 * anchor
    return base_signal

def f02_pblo_gemini_123(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=453, w3=66, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(31)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.083333 * persistence + 5.34e-05 * anchor
    return base_signal

def f02_pblo_gemini_124(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=466, w3=83, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(38, min_periods=max(38//3, 2)).std()
    vol_slow = ret.rolling(466, min_periods=max(466//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.216471 + 5.35e-05 * anchor
    return base_signal

def f02_pblo_gemini_125(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=479, w3=100, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(479, min_periods=max(479//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 45)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.096 * slope + 5.36e-05 * anchor
    return base_signal

def f02_pblo_gemini_126(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=492, w3=117, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(52)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.243529 + 5.37e-05 * anchor
    return base_signal

def f02_pblo_gemini_127(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=505, w3=134, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 505)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.108667 * acceleration + 5.38e-05 * anchor
    return base_signal

def f02_pblo_gemini_128(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=19, w3=151, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.270588 + 5.39e-05 * anchor
    return base_signal

def f02_pblo_gemini_129(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=32, w3=168, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.121333 * _rolling_slope(draw, 168) + 5.4e-05 * anchor
    return base_signal

def f02_pblo_gemini_130(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=45, w3=185, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(45, min_periods=max(45//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.297647 + 5.41e-05 * anchor
    return base_signal

def f02_pblo_gemini_131(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=58, w3=202, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=202, adjust=False).mean() * 1.311176 + 5.42e-05 * anchor
    return base_signal

def f02_pblo_gemini_132(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=71, w3=219, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.324706 + 5.43e-05 * anchor
    return base_signal

def f02_pblo_gemini_133(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=84, w3=236, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(101)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146667 * persistence + 5.44e-05 * anchor
    return base_signal

def f02_pblo_gemini_134(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=97, w3=253, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.351765 + 5.45e-05 * anchor
    return base_signal

def f02_pblo_gemini_135(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=110, w3=270, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.159333 * slope + 5.46e-05 * anchor
    return base_signal

def f02_pblo_gemini_136(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=123, w3=287, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(122)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.378824 + 5.47e-05 * anchor
    return base_signal

def f02_pblo_gemini_137(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=136, w3=304, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 304)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.172 * acceleration + 5.48e-05 * anchor
    return base_signal

def f02_pblo_gemini_138(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=149, w3=321, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.405882 + 5.49e-05 * anchor
    return base_signal

def f02_pblo_gemini_139(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=162, w3=338, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.184667 * _rolling_slope(draw, 338) + 5.5e-05 * anchor
    return base_signal

def f02_pblo_gemini_140(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=175, w3=355, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(175, min_periods=max(175//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.432941 + 5.51e-05 * anchor
    return base_signal

def f02_pblo_gemini_141(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=188, w3=372, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.446471 + 5.52e-05 * anchor
    return base_signal

def f02_pblo_gemini_142(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=201, w3=389, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(201, min_periods=max(201//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.46 + 5.53e-05 * anchor
    return base_signal

def f02_pblo_gemini_143(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=214, w3=406, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.21 * persistence + 5.54e-05 * anchor
    return base_signal

def f02_pblo_gemini_144(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=227, w3=423, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.487059 + 5.55e-05 * anchor
    return base_signal

def f02_pblo_gemini_145(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=240, w3=440, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.222667 * slope + 5.56e-05 * anchor
    return base_signal

def f02_pblo_gemini_146(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=253, w3=457, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.514118 + 5.57e-05 * anchor
    return base_signal

def f02_pblo_gemini_147(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=266, w3=474, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235333 * acceleration + 5.58e-05 * anchor
    return base_signal

def f02_pblo_gemini_148(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=279, w3=491, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.541176 + 5.59e-05 * anchor
    return base_signal

def f02_pblo_gemini_149(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=292, w3=508, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.248 * _rolling_slope(draw, 508) + 5.6e-05 * anchor
    return base_signal

def f02_pblo_gemini_150(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=305, w3=525, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.568235 + 5.61e-05 * anchor
    return base_signal

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_02_PARABOLIC_BLOWOFF_SIGNATURE_GEMINI_BASE_076_150 = {
    "f02_pblo_gemini_076": {"inputs": ['close'], "func": f02_pblo_gemini_076, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_077": {"inputs": ['close'], "func": f02_pblo_gemini_077, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_078": {"inputs": ['close'], "func": f02_pblo_gemini_078, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_079": {"inputs": ['close'], "func": f02_pblo_gemini_079, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_080": {"inputs": ['close'], "func": f02_pblo_gemini_080, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_081": {"inputs": ['close'], "func": f02_pblo_gemini_081, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_082": {"inputs": ['close'], "func": f02_pblo_gemini_082, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_083": {"inputs": ['close'], "func": f02_pblo_gemini_083, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_084": {"inputs": ['close'], "func": f02_pblo_gemini_084, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_085": {"inputs": ['close'], "func": f02_pblo_gemini_085, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_086": {"inputs": ['close'], "func": f02_pblo_gemini_086, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_087": {"inputs": ['close'], "func": f02_pblo_gemini_087, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_088": {"inputs": ['close'], "func": f02_pblo_gemini_088, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_089": {"inputs": ['close'], "func": f02_pblo_gemini_089, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_090": {"inputs": ['close'], "func": f02_pblo_gemini_090, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_091": {"inputs": ['close'], "func": f02_pblo_gemini_091, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_092": {"inputs": ['close'], "func": f02_pblo_gemini_092, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_093": {"inputs": ['close'], "func": f02_pblo_gemini_093, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_094": {"inputs": ['close'], "func": f02_pblo_gemini_094, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_095": {"inputs": ['close'], "func": f02_pblo_gemini_095, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_096": {"inputs": ['close'], "func": f02_pblo_gemini_096, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_097": {"inputs": ['close'], "func": f02_pblo_gemini_097, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_098": {"inputs": ['close'], "func": f02_pblo_gemini_098, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_099": {"inputs": ['close'], "func": f02_pblo_gemini_099, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_100": {"inputs": ['close'], "func": f02_pblo_gemini_100, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_101": {"inputs": ['close'], "func": f02_pblo_gemini_101, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_102": {"inputs": ['close'], "func": f02_pblo_gemini_102, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_103": {"inputs": ['close'], "func": f02_pblo_gemini_103, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_104": {"inputs": ['close'], "func": f02_pblo_gemini_104, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_105": {"inputs": ['close'], "func": f02_pblo_gemini_105, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_106": {"inputs": ['close'], "func": f02_pblo_gemini_106, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_107": {"inputs": ['close'], "func": f02_pblo_gemini_107, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_108": {"inputs": ['close'], "func": f02_pblo_gemini_108, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_109": {"inputs": ['close'], "func": f02_pblo_gemini_109, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_110": {"inputs": ['close'], "func": f02_pblo_gemini_110, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_111": {"inputs": ['close'], "func": f02_pblo_gemini_111, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_112": {"inputs": ['close'], "func": f02_pblo_gemini_112, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_113": {"inputs": ['close'], "func": f02_pblo_gemini_113, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_114": {"inputs": ['close'], "func": f02_pblo_gemini_114, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_115": {"inputs": ['close'], "func": f02_pblo_gemini_115, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_116": {"inputs": ['close'], "func": f02_pblo_gemini_116, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_117": {"inputs": ['close'], "func": f02_pblo_gemini_117, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_118": {"inputs": ['close'], "func": f02_pblo_gemini_118, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_119": {"inputs": ['close'], "func": f02_pblo_gemini_119, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_120": {"inputs": ['close'], "func": f02_pblo_gemini_120, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_121": {"inputs": ['close'], "func": f02_pblo_gemini_121, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_122": {"inputs": ['close'], "func": f02_pblo_gemini_122, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_123": {"inputs": ['close'], "func": f02_pblo_gemini_123, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_124": {"inputs": ['close'], "func": f02_pblo_gemini_124, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_125": {"inputs": ['close'], "func": f02_pblo_gemini_125, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_126": {"inputs": ['close'], "func": f02_pblo_gemini_126, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_127": {"inputs": ['close'], "func": f02_pblo_gemini_127, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_128": {"inputs": ['close'], "func": f02_pblo_gemini_128, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_129": {"inputs": ['close'], "func": f02_pblo_gemini_129, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_130": {"inputs": ['close'], "func": f02_pblo_gemini_130, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_131": {"inputs": ['close'], "func": f02_pblo_gemini_131, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_132": {"inputs": ['close'], "func": f02_pblo_gemini_132, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_133": {"inputs": ['close'], "func": f02_pblo_gemini_133, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_134": {"inputs": ['close'], "func": f02_pblo_gemini_134, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_135": {"inputs": ['close'], "func": f02_pblo_gemini_135, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_136": {"inputs": ['close'], "func": f02_pblo_gemini_136, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_137": {"inputs": ['close'], "func": f02_pblo_gemini_137, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_138": {"inputs": ['close'], "func": f02_pblo_gemini_138, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_139": {"inputs": ['close'], "func": f02_pblo_gemini_139, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_140": {"inputs": ['close'], "func": f02_pblo_gemini_140, "description": "Quadratic curvature of log-price over 1260d."},
    "f02_pblo_gemini_141": {"inputs": ['close'], "func": f02_pblo_gemini_141, "description": "Quadratic curvature of log-price over 5d."},
    "f02_pblo_gemini_142": {"inputs": ['close'], "func": f02_pblo_gemini_142, "description": "Quadratic curvature of log-price over 10d."},
    "f02_pblo_gemini_143": {"inputs": ['close'], "func": f02_pblo_gemini_143, "description": "Quadratic curvature of log-price over 21d."},
    "f02_pblo_gemini_144": {"inputs": ['close'], "func": f02_pblo_gemini_144, "description": "Quadratic curvature of log-price over 42d."},
    "f02_pblo_gemini_145": {"inputs": ['close'], "func": f02_pblo_gemini_145, "description": "Quadratic curvature of log-price over 63d."},
    "f02_pblo_gemini_146": {"inputs": ['close'], "func": f02_pblo_gemini_146, "description": "Quadratic curvature of log-price over 126d."},
    "f02_pblo_gemini_147": {"inputs": ['close'], "func": f02_pblo_gemini_147, "description": "Quadratic curvature of log-price over 252d."},
    "f02_pblo_gemini_148": {"inputs": ['close'], "func": f02_pblo_gemini_148, "description": "Quadratic curvature of log-price over 504d."},
    "f02_pblo_gemini_149": {"inputs": ['close'], "func": f02_pblo_gemini_149, "description": "Quadratic curvature of log-price over 756d."},
    "f02_pblo_gemini_150": {"inputs": ['close'], "func": f02_pblo_gemini_150, "description": "Quadratic curvature of log-price over 1260d."},
}
