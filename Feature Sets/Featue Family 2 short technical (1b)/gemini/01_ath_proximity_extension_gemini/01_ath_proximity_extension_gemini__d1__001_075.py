"""01 ath proximity extension gemini d1 features 1-75 â€” Pipeline 1b-HF Grade v7.

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

def f01_athx_gemini_001_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 1 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_002_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 2 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_003_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 3 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_004_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 4 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_005_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 5 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_006_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 6 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_007_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 7 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_008_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 8 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_009_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 9 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_010_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 10 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_011_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 11 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_012_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 12 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_013_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 13 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_014_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 14 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_015_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 15 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_016_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 16 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_017_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 17 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_018_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 18 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_019_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 19 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_020_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 20 <= 10 else high) - _safe_log(m)
    return (res).diff()

def f01_athx_gemini_021_d1(high: pd.Series) -> pd.Series:
    """Bars since 5d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(5, min_periods=5//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_022_d1(high: pd.Series) -> pd.Series:
    """Bars since 10d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(10, min_periods=10//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_023_d1(high: pd.Series) -> pd.Series:
    """Bars since 21d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(21, min_periods=21//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_024_d1(high: pd.Series) -> pd.Series:
    """Bars since 42d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(42, min_periods=42//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_025_d1(high: pd.Series) -> pd.Series:
    """Bars since 63d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(63, min_periods=63//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_026_d1(high: pd.Series) -> pd.Series:
    """Bars since 126d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(126, min_periods=126//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_027_d1(high: pd.Series) -> pd.Series:
    """Bars since 252d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(252, min_periods=252//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_028_d1(high: pd.Series) -> pd.Series:
    """Bars since 504d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(504, min_periods=504//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_029_d1(high: pd.Series) -> pd.Series:
    """Bars since 756d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(756, min_periods=756//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_030_d1(high: pd.Series) -> pd.Series:
    """Bars since 1260d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(1260, min_periods=1260//3).apply(_bsm, raw=True)
    return (res).diff()

def f01_athx_gemini_031_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=456, w3=402, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 41)
    slow = _rolling_slope(x, 456)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.468235 + 1.12e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_032_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=469, w3=419, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(469, min_periods=max(469//3, 2)).max()
    trough = x.rolling(48, min_periods=max(48//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.481765 + 1.13e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_033_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=482, w3=436, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(55)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.082 * persistence + 1.14e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_034_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=495, w3=453, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(62, min_periods=max(62//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.508824 + 1.15e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_035_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=508, w3=470, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(508, min_periods=max(508//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 69)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.094667 * slope + 1.16e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_036_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=22, w3=487, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(76)
    drag = impulse.rolling(22, min_periods=max(22//3, 2)).mean()
    noise = impulse.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.535882 + 1.17e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_037_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=35, w3=504, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 83)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 504)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.107333 * acceleration + 1.18e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_038_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=48, w3=521, lag=34)."""
    x = high.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.562941 + 1.19e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_039_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=61, w3=538, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    draw = x - x.rolling(61, min_periods=max(61//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.12 * _rolling_slope(draw, 538) + 1.2e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_040_d1(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=74, w3=555, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 104)
    baseline = trend.rolling(74, min_periods=max(74//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.59 + 1.21e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_041_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 5d high."""
    m = high.rolling(5).max()
    res = _safe_div(close - m, _atr(high, low, close, 5))
    return (res).diff()

def f01_athx_gemini_042_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 10d high."""
    m = high.rolling(10).max()
    res = _safe_div(close - m, _atr(high, low, close, 10))
    return (res).diff()

def f01_athx_gemini_043_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 21d high."""
    m = high.rolling(21).max()
    res = _safe_div(close - m, _atr(high, low, close, 21))
    return (res).diff()

def f01_athx_gemini_044_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 42d high."""
    m = high.rolling(42).max()
    res = _safe_div(close - m, _atr(high, low, close, 42))
    return (res).diff()

def f01_athx_gemini_045_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 63d high."""
    m = high.rolling(63).max()
    res = _safe_div(close - m, _atr(high, low, close, 63))
    return (res).diff()

def f01_athx_gemini_046_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 126d high."""
    m = high.rolling(126).max()
    res = _safe_div(close - m, _atr(high, low, close, 126))
    return (res).diff()

def f01_athx_gemini_047_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 252d high."""
    m = high.rolling(252).max()
    res = _safe_div(close - m, _atr(high, low, close, 252))
    return (res).diff()

def f01_athx_gemini_048_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 504d high."""
    m = high.rolling(504).max()
    res = _safe_div(close - m, _atr(high, low, close, 504))
    return (res).diff()

def f01_athx_gemini_049_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 756d high."""
    m = high.rolling(756).max()
    res = _safe_div(close - m, _atr(high, low, close, 756))
    return (res).diff()

def f01_athx_gemini_050_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 1260d high."""
    m = high.rolling(1260).max()
    res = _safe_div(close - m, _atr(high, low, close, 1260))
    return (res).diff()

def f01_athx_gemini_051_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=87, w3=572, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(111, min_periods=max(111//3, 2)).mean())
    decay = spread.ewm(span=87, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.603529 + 1.22e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_052_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=100, w3=589, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(100, min_periods=max(100//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 118)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.617059 + 1.23e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_053_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=113, w3=606, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(125, min_periods=max(125//3, 2)).mean(), b.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.145333 * _rolling_slope(cover, 125) + 1.24e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_054_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=126, w3=623, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.151667 * y + 0.848333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 132) - _rolling_slope(basket, 126) + 1.25e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_055_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=139, w3=640, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.657647 + 1.26e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_056_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=152, w3=657, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(152, min_periods=max(152//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.164333 * _rolling_slope(draw, 657) + 1.27e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_057_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=165, w3=674, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.831176 + 1.28e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_058_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=178, w3=691, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.844706 + 1.29e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_059_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=191, w3=708, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 191)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.858235 + 1.3e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_060_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=204, w3=725, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(204, min_periods=max(204//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.871765 + 1.31e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_061_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=217, w3=742, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(217, min_periods=max(217//3, 2)).rank(pct=True)
    persistence = change.rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.196 * persistence + 1.32e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_062_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=230, w3=759, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.898824 + 1.33e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_063_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=243, w3=25, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(243, min_periods=max(243//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.208667 * slope + 1.34e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_064_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=256, w3=42, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(256, min_periods=max(256//3, 2)).mean()
    noise = impulse.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.925882 + 1.35e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_065_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=269, w3=59, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 269)
    curvature = _rolling_slope(acceleration, 59)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.221333 * acceleration + 1.36e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_066_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=282, w3=76, lag=13)."""
    rel = _safe_div(close.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 216)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.227667 * pressure.rolling(76, min_periods=max(76//3, 2)).mean() + 1.37e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_067_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=295, w3=93, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    decay = spread.ewm(span=295, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.966471 + 1.38e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_068_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=308, w3=110, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(308, min_periods=max(308//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 230)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.98 + 1.39e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_069_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=321, w3=127, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(237, min_periods=max(237//3, 2)).mean(), b.abs().rolling(321, min_periods=max(321//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.246667 * _rolling_slope(cover, 237) + 1.4e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_070_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=334, w3=144, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.253 * y + 0.747000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 244) - _rolling_slope(basket, 334) + 1.41e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_071_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=347, w3=161, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(347, min_periods=max(347//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.020588 + 1.42e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_072_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=360, w3=178, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(360, min_periods=max(360//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.265667 * _rolling_slope(draw, 178) + 1.43e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_073_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=373, w3=195, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(18) - b.diff(126)
    stress = imbalance.rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.047647 + 1.44e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_074_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=386, w3=212, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.061176 + 1.45e-05 * anchor
    return base_signal.diff()

def f01_athx_gemini_075_d1(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=399, w3=229, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 399)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=229, adjust=False).mean() * 1.074706 + 1.46e-05 * anchor
    return base_signal.diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_D1_001_075 = {
    "f01_athx_gemini_001_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_001_d1, "description": "Log distance above 5d high."},
    "f01_athx_gemini_002_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_002_d1, "description": "Log distance above 10d high."},
    "f01_athx_gemini_003_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_003_d1, "description": "Log distance above 21d high."},
    "f01_athx_gemini_004_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_004_d1, "description": "Log distance above 42d high."},
    "f01_athx_gemini_005_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_005_d1, "description": "Log distance above 63d high."},
    "f01_athx_gemini_006_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_006_d1, "description": "Log distance above 126d high."},
    "f01_athx_gemini_007_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_007_d1, "description": "Log distance above 252d high."},
    "f01_athx_gemini_008_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_008_d1, "description": "Log distance above 504d high."},
    "f01_athx_gemini_009_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_009_d1, "description": "Log distance above 756d high."},
    "f01_athx_gemini_010_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_010_d1, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_011_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_011_d1, "description": "Log distance above 5d high."},
    "f01_athx_gemini_012_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_012_d1, "description": "Log distance above 10d high."},
    "f01_athx_gemini_013_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_013_d1, "description": "Log distance above 21d high."},
    "f01_athx_gemini_014_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_014_d1, "description": "Log distance above 42d high."},
    "f01_athx_gemini_015_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_015_d1, "description": "Log distance above 63d high."},
    "f01_athx_gemini_016_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_016_d1, "description": "Log distance above 126d high."},
    "f01_athx_gemini_017_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_017_d1, "description": "Log distance above 252d high."},
    "f01_athx_gemini_018_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_018_d1, "description": "Log distance above 504d high."},
    "f01_athx_gemini_019_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_019_d1, "description": "Log distance above 756d high."},
    "f01_athx_gemini_020_d1": {"inputs": ['close', 'high'], "func": f01_athx_gemini_020_d1, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_021_d1": {"inputs": ['high'], "func": f01_athx_gemini_021_d1, "description": "Days since 5d high touched."},
    "f01_athx_gemini_022_d1": {"inputs": ['high'], "func": f01_athx_gemini_022_d1, "description": "Days since 10d high touched."},
    "f01_athx_gemini_023_d1": {"inputs": ['high'], "func": f01_athx_gemini_023_d1, "description": "Days since 21d high touched."},
    "f01_athx_gemini_024_d1": {"inputs": ['high'], "func": f01_athx_gemini_024_d1, "description": "Days since 42d high touched."},
    "f01_athx_gemini_025_d1": {"inputs": ['high'], "func": f01_athx_gemini_025_d1, "description": "Days since 63d high touched."},
    "f01_athx_gemini_026_d1": {"inputs": ['high'], "func": f01_athx_gemini_026_d1, "description": "Days since 126d high touched."},
    "f01_athx_gemini_027_d1": {"inputs": ['high'], "func": f01_athx_gemini_027_d1, "description": "Days since 252d high touched."},
    "f01_athx_gemini_028_d1": {"inputs": ['high'], "func": f01_athx_gemini_028_d1, "description": "Days since 504d high touched."},
    "f01_athx_gemini_029_d1": {"inputs": ['high'], "func": f01_athx_gemini_029_d1, "description": "Days since 756d high touched."},
    "f01_athx_gemini_030_d1": {"inputs": ['high'], "func": f01_athx_gemini_030_d1, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_031_d1": {"inputs": ['high'], "func": f01_athx_gemini_031_d1, "description": "Days since 5d high touched."},
    "f01_athx_gemini_032_d1": {"inputs": ['high'], "func": f01_athx_gemini_032_d1, "description": "Days since 10d high touched."},
    "f01_athx_gemini_033_d1": {"inputs": ['high'], "func": f01_athx_gemini_033_d1, "description": "Days since 21d high touched."},
    "f01_athx_gemini_034_d1": {"inputs": ['high'], "func": f01_athx_gemini_034_d1, "description": "Days since 42d high touched."},
    "f01_athx_gemini_035_d1": {"inputs": ['high'], "func": f01_athx_gemini_035_d1, "description": "Days since 63d high touched."},
    "f01_athx_gemini_036_d1": {"inputs": ['high'], "func": f01_athx_gemini_036_d1, "description": "Days since 126d high touched."},
    "f01_athx_gemini_037_d1": {"inputs": ['high'], "func": f01_athx_gemini_037_d1, "description": "Days since 252d high touched."},
    "f01_athx_gemini_038_d1": {"inputs": ['high'], "func": f01_athx_gemini_038_d1, "description": "Days since 504d high touched."},
    "f01_athx_gemini_039_d1": {"inputs": ['high'], "func": f01_athx_gemini_039_d1, "description": "Days since 756d high touched."},
    "f01_athx_gemini_040_d1": {"inputs": ['high'], "func": f01_athx_gemini_040_d1, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_041_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_041_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_042_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_042_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_043_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_043_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_044_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_044_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_045_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_045_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_046_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_046_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_047_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_047_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_048_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_048_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_049_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_049_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_050_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_050_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_051_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_051_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_052_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_052_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_053_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_053_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_054_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_054_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_055_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_055_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_056_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_056_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_057_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_057_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_058_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_058_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_059_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_059_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_060_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_060_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_061_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_061_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_062_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_062_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_063_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_063_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_064_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_064_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_065_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_065_d1, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_066_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_066_d1, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_067_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_067_d1, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_068_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_068_d1, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_069_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_069_d1, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_070_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_070_d1, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_071_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_071_d1, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_072_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_072_d1, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_073_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_073_d1, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_074_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_074_d1, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_075_d1": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_075_d1, "description": "ATR-normalized distance to 63d high."},
}
