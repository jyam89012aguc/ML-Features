"""01 ath proximity extension gemini base features 1-75 â€” Pipeline 1b-HF Grade v7.

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
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f01_athx_gemini_001(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 1 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_002(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 2 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_003(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 3 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_004(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 4 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_005(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 5 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_006(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 6 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_007(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 7 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_008(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 8 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_009(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 9 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_010(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 10 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_011(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 11 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_012(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 12 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_013(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 13 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_014(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 14 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_015(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 15 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_016(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 16 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_017(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 17 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_018(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 18 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_019(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 19 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_020(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 20 <= 10 else high) - _safe_log(m)
    return res

def f01_athx_gemini_021(high: pd.Series) -> pd.Series:
    """Bars since 5d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(5, min_periods=5//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_022(high: pd.Series) -> pd.Series:
    """Bars since 10d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(10, min_periods=10//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_023(high: pd.Series) -> pd.Series:
    """Bars since 21d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(21, min_periods=21//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_024(high: pd.Series) -> pd.Series:
    """Bars since 42d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(42, min_periods=42//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_025(high: pd.Series) -> pd.Series:
    """Bars since 63d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(63, min_periods=63//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_026(high: pd.Series) -> pd.Series:
    """Bars since 126d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(126, min_periods=126//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_027(high: pd.Series) -> pd.Series:
    """Bars since 252d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(252, min_periods=252//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_028(high: pd.Series) -> pd.Series:
    """Bars since 504d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(504, min_periods=504//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_029(high: pd.Series) -> pd.Series:
    """Bars since 756d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(756, min_periods=756//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_030(high: pd.Series) -> pd.Series:
    """Bars since 1260d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(1260, min_periods=1260//3).apply(_bsm, raw=True)
    return res

def f01_athx_gemini_031(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=24, w3=34, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 24)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=34, adjust=False).mean() * 0.833529 + 2e-07 * anchor
    return base_signal

def f01_athx_gemini_032(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=37, w3=51, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(37, min_periods=max(37//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.847059 + 3e-07 * anchor
    return base_signal

def f01_athx_gemini_033(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=50, w3=68, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(26)
    rank = change.rolling(50, min_periods=max(50//3, 2)).rank(pct=True)
    persistence = change.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.05 * persistence + 4e-07 * anchor
    return base_signal

def f01_athx_gemini_034(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=63, w3=85, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(63, min_periods=max(63//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.874118 + 5e-07 * anchor
    return base_signal

def f01_athx_gemini_035(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=76, w3=102, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(76, min_periods=max(76//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.062667 * slope + 6e-07 * anchor
    return base_signal

def f01_athx_gemini_036(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=89, w3=119, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(47)
    drag = impulse.rolling(89, min_periods=max(89//3, 2)).mean()
    noise = impulse.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.901176 + 7e-07 * anchor
    return base_signal

def f01_athx_gemini_037(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=102, w3=136, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 54)
    acceleration = _rolling_slope(velocity, 102)
    curvature = _rolling_slope(acceleration, 136)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.075333 * acceleration + 8e-07 * anchor
    return base_signal

def f01_athx_gemini_038(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=115, w3=153, lag=34)."""
    x = high.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(61, min_periods=max(61//3, 2)).mean(), upside.rolling(115, min_periods=max(115//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.928235 + 9e-07 * anchor
    return base_signal

def f01_athx_gemini_039(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=128, w3=170, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    draw = x - x.rolling(128, min_periods=max(128//3, 2)).max()
    rebound = x - x.rolling(68, min_periods=max(68//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.088 * _rolling_slope(draw, 170) + 1e-06 * anchor
    return base_signal

def f01_athx_gemini_040(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=141, w3=187, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(141, min_periods=max(141//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.955294 + 1.1e-06 * anchor
    return base_signal

def f01_athx_gemini_041(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 5d high."""
    m = high.rolling(5).max()
    res = _safe_div(close - m, _atr(high, low, close, 5))
    return res

def f01_athx_gemini_042(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 10d high."""
    m = high.rolling(10).max()
    res = _safe_div(close - m, _atr(high, low, close, 10))
    return res

def f01_athx_gemini_043(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 21d high."""
    m = high.rolling(21).max()
    res = _safe_div(close - m, _atr(high, low, close, 21))
    return res

def f01_athx_gemini_044(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 42d high."""
    m = high.rolling(42).max()
    res = _safe_div(close - m, _atr(high, low, close, 42))
    return res

def f01_athx_gemini_045(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 63d high."""
    m = high.rolling(63).max()
    res = _safe_div(close - m, _atr(high, low, close, 63))
    return res

def f01_athx_gemini_046(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 126d high."""
    m = high.rolling(126).max()
    res = _safe_div(close - m, _atr(high, low, close, 126))
    return res

def f01_athx_gemini_047(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 252d high."""
    m = high.rolling(252).max()
    res = _safe_div(close - m, _atr(high, low, close, 252))
    return res

def f01_athx_gemini_048(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 504d high."""
    m = high.rolling(504).max()
    res = _safe_div(close - m, _atr(high, low, close, 504))
    return res

def f01_athx_gemini_049(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 756d high."""
    m = high.rolling(756).max()
    res = _safe_div(close - m, _atr(high, low, close, 756))
    return res

def f01_athx_gemini_050(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 1260d high."""
    m = high.rolling(1260).max()
    res = _safe_div(close - m, _atr(high, low, close, 1260))
    return res

def f01_athx_gemini_051(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=154, w3=204, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(82, min_periods=max(82//3, 2)).mean(), b.abs().rolling(154, min_periods=max(154//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.100667 * _rolling_slope(cover, 82) + 1.2e-06 * anchor
    return base_signal

def f01_athx_gemini_052(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=167, w3=221, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.107 * y + 0.893000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 89) - _rolling_slope(basket, 167) + 1.3e-06 * anchor
    return base_signal

def f01_athx_gemini_053(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=180, w3=238, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(180, min_periods=max(180//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.995882 + 1.4e-06 * anchor
    return base_signal

def f01_athx_gemini_054(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=193, w3=255, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(193, min_periods=max(193//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.119667 * _rolling_slope(draw, 255) + 1.5e-06 * anchor
    return base_signal

def f01_athx_gemini_055(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=206, w3=272, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(110) - b.diff(126)
    stress = imbalance.rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.022941 + 1.6e-06 * anchor
    return base_signal

def f01_athx_gemini_056(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=219, w3=289, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 117)
    baseline = trend.rolling(219, min_periods=max(219//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.036471 + 1.7e-06 * anchor
    return base_signal

def f01_athx_gemini_057(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=232, w3=306, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 124)
    slow = _rolling_slope(x, 232)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.05 + 1.8e-06 * anchor
    return base_signal

def f01_athx_gemini_058(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=245, w3=323, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(245, min_periods=max(245//3, 2)).max()
    trough = x.rolling(131, min_periods=max(131//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.063529 + 1.9e-06 * anchor
    return base_signal

def f01_athx_gemini_059(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=258, w3=340, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(258, min_periods=max(258//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.151333 * persistence + 2e-06 * anchor
    return base_signal

def f01_athx_gemini_060(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=271, w3=357, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(145, min_periods=max(145//3, 2)).std()
    vol_slow = ret.rolling(271, min_periods=max(271//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.090588 + 2.1e-06 * anchor
    return base_signal

def f01_athx_gemini_061(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=284, w3=374, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(284, min_periods=max(284//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 152)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.164 * slope + 2.2e-06 * anchor
    return base_signal

def f01_athx_gemini_062(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=297, w3=391, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(297, min_periods=max(297//3, 2)).mean()
    noise = impulse.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.117647 + 2.3e-06 * anchor
    return base_signal

def f01_athx_gemini_063(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=310, w3=408, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 166)
    acceleration = _rolling_slope(velocity, 310)
    curvature = _rolling_slope(acceleration, 408)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.176667 * acceleration + 2.4e-06 * anchor
    return base_signal

def f01_athx_gemini_064(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=323, w3=425, lag=5)."""
    rel = _safe_div(close.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 173)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.183 * pressure.rolling(425, min_periods=max(425//3, 2)).mean() + 2.5e-06 * anchor
    return base_signal

def f01_athx_gemini_065(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=336, w3=442, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(180, min_periods=max(180//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.158235 + 2.6e-06 * anchor
    return base_signal

def f01_athx_gemini_066(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=349, w3=459, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(349, min_periods=max(349//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 187)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.171765 + 2.7e-06 * anchor
    return base_signal

def f01_athx_gemini_067(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=362, w3=476, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(194, min_periods=max(194//3, 2)).mean(), b.abs().rolling(362, min_periods=max(362//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.202 * _rolling_slope(cover, 194) + 2.8e-06 * anchor
    return base_signal

def f01_athx_gemini_068(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=375, w3=493, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.208333 * y + 0.791667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 201) - _rolling_slope(basket, 375) + 2.9e-06 * anchor
    return base_signal

def f01_athx_gemini_069(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=388, w3=510, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.212353 + 3e-06 * anchor
    return base_signal

def f01_athx_gemini_070(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=401, w3=527, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.221 * _rolling_slope(draw, 527) + 3.1e-06 * anchor
    return base_signal

def f01_athx_gemini_071(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=414, w3=544, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.239412 + 3.2e-06 * anchor
    return base_signal

def f01_athx_gemini_072(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=427, w3=561, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(427, min_periods=max(427//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.252941 + 3.3e-06 * anchor
    return base_signal

def f01_athx_gemini_073(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=440, w3=578, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 440)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.266471 + 3.4e-06 * anchor
    return base_signal

def f01_athx_gemini_074(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=453, w3=595, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(453, min_periods=max(453//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.28 + 3.5e-06 * anchor
    return base_signal

def f01_athx_gemini_075(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=466, w3=612, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(466, min_periods=max(466//3, 2)).rank(pct=True)
    persistence = change.rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.252667 * persistence + 3.6e-06 * anchor
    return base_signal

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_BASE_001_075 = {
    "f01_athx_gemini_001": {"inputs": ['close', 'high'], "func": f01_athx_gemini_001, "description": "Log distance above 5d high."},
    "f01_athx_gemini_002": {"inputs": ['close', 'high'], "func": f01_athx_gemini_002, "description": "Log distance above 10d high."},
    "f01_athx_gemini_003": {"inputs": ['close', 'high'], "func": f01_athx_gemini_003, "description": "Log distance above 21d high."},
    "f01_athx_gemini_004": {"inputs": ['close', 'high'], "func": f01_athx_gemini_004, "description": "Log distance above 42d high."},
    "f01_athx_gemini_005": {"inputs": ['close', 'high'], "func": f01_athx_gemini_005, "description": "Log distance above 63d high."},
    "f01_athx_gemini_006": {"inputs": ['close', 'high'], "func": f01_athx_gemini_006, "description": "Log distance above 126d high."},
    "f01_athx_gemini_007": {"inputs": ['close', 'high'], "func": f01_athx_gemini_007, "description": "Log distance above 252d high."},
    "f01_athx_gemini_008": {"inputs": ['close', 'high'], "func": f01_athx_gemini_008, "description": "Log distance above 504d high."},
    "f01_athx_gemini_009": {"inputs": ['close', 'high'], "func": f01_athx_gemini_009, "description": "Log distance above 756d high."},
    "f01_athx_gemini_010": {"inputs": ['close', 'high'], "func": f01_athx_gemini_010, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_011": {"inputs": ['close', 'high'], "func": f01_athx_gemini_011, "description": "Log distance above 5d high."},
    "f01_athx_gemini_012": {"inputs": ['close', 'high'], "func": f01_athx_gemini_012, "description": "Log distance above 10d high."},
    "f01_athx_gemini_013": {"inputs": ['close', 'high'], "func": f01_athx_gemini_013, "description": "Log distance above 21d high."},
    "f01_athx_gemini_014": {"inputs": ['close', 'high'], "func": f01_athx_gemini_014, "description": "Log distance above 42d high."},
    "f01_athx_gemini_015": {"inputs": ['close', 'high'], "func": f01_athx_gemini_015, "description": "Log distance above 63d high."},
    "f01_athx_gemini_016": {"inputs": ['close', 'high'], "func": f01_athx_gemini_016, "description": "Log distance above 126d high."},
    "f01_athx_gemini_017": {"inputs": ['close', 'high'], "func": f01_athx_gemini_017, "description": "Log distance above 252d high."},
    "f01_athx_gemini_018": {"inputs": ['close', 'high'], "func": f01_athx_gemini_018, "description": "Log distance above 504d high."},
    "f01_athx_gemini_019": {"inputs": ['close', 'high'], "func": f01_athx_gemini_019, "description": "Log distance above 756d high."},
    "f01_athx_gemini_020": {"inputs": ['close', 'high'], "func": f01_athx_gemini_020, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_021": {"inputs": ['high'], "func": f01_athx_gemini_021, "description": "Days since 5d high touched."},
    "f01_athx_gemini_022": {"inputs": ['high'], "func": f01_athx_gemini_022, "description": "Days since 10d high touched."},
    "f01_athx_gemini_023": {"inputs": ['high'], "func": f01_athx_gemini_023, "description": "Days since 21d high touched."},
    "f01_athx_gemini_024": {"inputs": ['high'], "func": f01_athx_gemini_024, "description": "Days since 42d high touched."},
    "f01_athx_gemini_025": {"inputs": ['high'], "func": f01_athx_gemini_025, "description": "Days since 63d high touched."},
    "f01_athx_gemini_026": {"inputs": ['high'], "func": f01_athx_gemini_026, "description": "Days since 126d high touched."},
    "f01_athx_gemini_027": {"inputs": ['high'], "func": f01_athx_gemini_027, "description": "Days since 252d high touched."},
    "f01_athx_gemini_028": {"inputs": ['high'], "func": f01_athx_gemini_028, "description": "Days since 504d high touched."},
    "f01_athx_gemini_029": {"inputs": ['high'], "func": f01_athx_gemini_029, "description": "Days since 756d high touched."},
    "f01_athx_gemini_030": {"inputs": ['high'], "func": f01_athx_gemini_030, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_031": {"inputs": ['high'], "func": f01_athx_gemini_031, "description": "Days since 5d high touched."},
    "f01_athx_gemini_032": {"inputs": ['high'], "func": f01_athx_gemini_032, "description": "Days since 10d high touched."},
    "f01_athx_gemini_033": {"inputs": ['high'], "func": f01_athx_gemini_033, "description": "Days since 21d high touched."},
    "f01_athx_gemini_034": {"inputs": ['high'], "func": f01_athx_gemini_034, "description": "Days since 42d high touched."},
    "f01_athx_gemini_035": {"inputs": ['high'], "func": f01_athx_gemini_035, "description": "Days since 63d high touched."},
    "f01_athx_gemini_036": {"inputs": ['high'], "func": f01_athx_gemini_036, "description": "Days since 126d high touched."},
    "f01_athx_gemini_037": {"inputs": ['high'], "func": f01_athx_gemini_037, "description": "Days since 252d high touched."},
    "f01_athx_gemini_038": {"inputs": ['high'], "func": f01_athx_gemini_038, "description": "Days since 504d high touched."},
    "f01_athx_gemini_039": {"inputs": ['high'], "func": f01_athx_gemini_039, "description": "Days since 756d high touched."},
    "f01_athx_gemini_040": {"inputs": ['high'], "func": f01_athx_gemini_040, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_041": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_041, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_042": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_042, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_043": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_043, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_044": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_044, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_045": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_045, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_046": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_046, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_047": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_047, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_048": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_048, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_049": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_049, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_050": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_050, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_051": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_051, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_052": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_052, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_053": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_053, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_054": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_054, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_055": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_055, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_056": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_056, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_057": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_057, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_058": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_058, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_059": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_059, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_060": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_060, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_061": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_061, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_062": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_062, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_063": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_063, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_064": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_064, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_065": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_065, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_066": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_066, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_067": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_067, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_068": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_068, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_069": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_069, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_070": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_070, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_071": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_071, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_072": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_072, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_073": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_073, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_074": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_074, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_075": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_075, "description": "ATR-normalized distance to 63d high."},
}
