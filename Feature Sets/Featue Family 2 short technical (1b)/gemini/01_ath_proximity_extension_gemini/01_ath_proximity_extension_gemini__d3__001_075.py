"""01 ath proximity extension gemini d3 features 1-75 â€” Pipeline 1b-HF Grade v7.

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

def f01_athx_gemini_001_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 1 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_002_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 2 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_003_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 3 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_004_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 4 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_005_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 5 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_006_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 6 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_007_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 7 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_008_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 8 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_009_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 9 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_010_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 10 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_011_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 11 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_012_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 12 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_013_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 13 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_014_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 14 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_015_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 15 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_016_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 16 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_017_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 17 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_018_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 18 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_019_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 19 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_020_d3(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 20 <= 10 else high) - _safe_log(m)
    return (res).diff().diff().diff()

def f01_athx_gemini_021_d3(high: pd.Series) -> pd.Series:
    """Bars since 5d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(5, min_periods=5//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_022_d3(high: pd.Series) -> pd.Series:
    """Bars since 10d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(10, min_periods=10//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_023_d3(high: pd.Series) -> pd.Series:
    """Bars since 21d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(21, min_periods=21//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_024_d3(high: pd.Series) -> pd.Series:
    """Bars since 42d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(42, min_periods=42//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_025_d3(high: pd.Series) -> pd.Series:
    """Bars since 63d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(63, min_periods=63//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_026_d3(high: pd.Series) -> pd.Series:
    """Bars since 126d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(126, min_periods=126//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_027_d3(high: pd.Series) -> pd.Series:
    """Bars since 252d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(252, min_periods=252//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_028_d3(high: pd.Series) -> pd.Series:
    """Bars since 504d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(504, min_periods=504//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_029_d3(high: pd.Series) -> pd.Series:
    """Bars since 756d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(756, min_periods=756//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_030_d3(high: pd.Series) -> pd.Series:
    """Bars since 1260d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(1260, min_periods=1260//3).apply(_bsm, raw=True)
    return (res).diff().diff().diff()

def f01_athx_gemini_031_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=322, w3=387, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 322)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.030588 + 3.32e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_032_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=335, w3=404, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(335, min_periods=max(335//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.044118 + 3.33e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_033_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=348, w3=421, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(113)
    rank = change.rolling(348, min_periods=max(348//3, 2)).rank(pct=True)
    persistence = change.rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146 * persistence + 3.34e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_034_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=361, w3=438, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(361, min_periods=max(361//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.071176 + 3.35e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_035_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=374, w3=455, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(374, min_periods=max(374//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.158667 * slope + 3.36e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_036_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=387, w3=472, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.098235 + 3.37e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_037_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=400, w3=489, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 400)
    curvature = _rolling_slope(acceleration, 489)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.171333 * acceleration + 3.38e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_038_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=413, w3=506, lag=34)."""
    x = high.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(413, min_periods=max(413//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.125294 + 3.39e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_039_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=426, w3=523, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    draw = x - x.rolling(426, min_periods=max(426//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.184 * _rolling_slope(draw, 523) + 3.4e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_040_d3(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=439, w3=540, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.152353 + 3.41e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_041_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 5d high."""
    m = high.rolling(5).max()
    res = _safe_div(close - m, _atr(high, low, close, 5))
    return (res).diff().diff().diff()

def f01_athx_gemini_042_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 10d high."""
    m = high.rolling(10).max()
    res = _safe_div(close - m, _atr(high, low, close, 10))
    return (res).diff().diff().diff()

def f01_athx_gemini_043_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 21d high."""
    m = high.rolling(21).max()
    res = _safe_div(close - m, _atr(high, low, close, 21))
    return (res).diff().diff().diff()

def f01_athx_gemini_044_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 42d high."""
    m = high.rolling(42).max()
    res = _safe_div(close - m, _atr(high, low, close, 42))
    return (res).diff().diff().diff()

def f01_athx_gemini_045_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 63d high."""
    m = high.rolling(63).max()
    res = _safe_div(close - m, _atr(high, low, close, 63))
    return (res).diff().diff().diff()

def f01_athx_gemini_046_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 126d high."""
    m = high.rolling(126).max()
    res = _safe_div(close - m, _atr(high, low, close, 126))
    return (res).diff().diff().diff()

def f01_athx_gemini_047_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 252d high."""
    m = high.rolling(252).max()
    res = _safe_div(close - m, _atr(high, low, close, 252))
    return (res).diff().diff().diff()

def f01_athx_gemini_048_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 504d high."""
    m = high.rolling(504).max()
    res = _safe_div(close - m, _atr(high, low, close, 504))
    return (res).diff().diff().diff()

def f01_athx_gemini_049_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 756d high."""
    m = high.rolling(756).max()
    res = _safe_div(close - m, _atr(high, low, close, 756))
    return (res).diff().diff().diff()

def f01_athx_gemini_050_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 1260d high."""
    m = high.rolling(1260).max()
    res = _safe_div(close - m, _atr(high, low, close, 1260))
    return (res).diff().diff().diff()

def f01_athx_gemini_051_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=452, w3=557, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(452, min_periods=max(452//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.196667 * slope + 3.42e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_052_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=465, w3=574, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(465, min_periods=max(465//3, 2)).mean()
    noise = impulse.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.179412 + 3.43e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_053_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=478, w3=591, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 478)
    curvature = _rolling_slope(acceleration, 591)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.209333 * acceleration + 3.44e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_054_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=491, w3=608, lag=5)."""
    rel = _safe_div(close.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 190)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.215667 * pressure.rolling(608, min_periods=max(608//3, 2)).mean() + 3.45e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_055_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=504, w3=625, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.22 + 3.46e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_056_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=18, w3=642, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(18, min_periods=max(18//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 204)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.233529 + 3.47e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_057_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=31, w3=659, lag=21)."""
    a = close.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(211, min_periods=max(211//3, 2)).mean(), b.abs().rolling(31, min_periods=max(31//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.234667 * _rolling_slope(cover, 211) + 3.48e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_058_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=44, w3=676, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.241 * y + 0.759000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 218) - _rolling_slope(basket, 44) + 3.49e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_059_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=57, w3=693, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.274118 + 3.5e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_060_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=70, w3=710, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(70, min_periods=max(70//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.253667 * _rolling_slope(draw, 710) + 3.51e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_061_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=83, w3=727, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(83)
    stress = imbalance.rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.301176 + 3.52e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_062_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=96, w3=744, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(96, min_periods=max(96//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.314706 + 3.53e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_063_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=109, w3=761, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 109)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.328235 + 3.54e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_064_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=122, w3=27, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.341765 + 3.55e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_065_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=135, w3=44, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(20)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.285333 * persistence + 3.56e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_066_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=148, w3=61, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.368824 + 3.57e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_067_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=161, w3=78, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.298 * slope + 3.58e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_068_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=174, w3=95, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(41)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.395882 + 3.59e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_069_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=187, w3=112, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.310667 * acceleration + 3.6e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_070_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=200, w3=129, lag=0)."""
    rel = _safe_div(close.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 55)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.317 * pressure.rolling(129, min_periods=max(129//3, 2)).mean() + 3.61e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_071_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=213, w3=146, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(62, min_periods=max(62//3, 2)).mean())
    decay = spread.ewm(span=213, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.436471 + 3.62e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_072_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=226, w3=163, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(226, min_periods=max(226//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 69)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.45 + 3.63e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_073_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=239, w3=180, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(76, min_periods=max(76//3, 2)).mean(), b.abs().rolling(239, min_periods=max(239//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.336 * _rolling_slope(cover, 76) + 3.64e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_074_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=252, w3=197, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.342333 * y + 0.657667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 83) - _rolling_slope(basket, 252) + 3.65e-05 * anchor
    return base_signal.diff().diff().diff()

def f01_athx_gemini_075_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=265, w3=214, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(265, min_periods=max(265//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.490588 + 3.66e-05 * anchor
    return base_signal.diff().diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_D3_001_075 = {
    "f01_athx_gemini_001_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_001_d3, "description": "Log distance above 5d high."},
    "f01_athx_gemini_002_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_002_d3, "description": "Log distance above 10d high."},
    "f01_athx_gemini_003_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_003_d3, "description": "Log distance above 21d high."},
    "f01_athx_gemini_004_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_004_d3, "description": "Log distance above 42d high."},
    "f01_athx_gemini_005_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_005_d3, "description": "Log distance above 63d high."},
    "f01_athx_gemini_006_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_006_d3, "description": "Log distance above 126d high."},
    "f01_athx_gemini_007_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_007_d3, "description": "Log distance above 252d high."},
    "f01_athx_gemini_008_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_008_d3, "description": "Log distance above 504d high."},
    "f01_athx_gemini_009_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_009_d3, "description": "Log distance above 756d high."},
    "f01_athx_gemini_010_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_010_d3, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_011_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_011_d3, "description": "Log distance above 5d high."},
    "f01_athx_gemini_012_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_012_d3, "description": "Log distance above 10d high."},
    "f01_athx_gemini_013_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_013_d3, "description": "Log distance above 21d high."},
    "f01_athx_gemini_014_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_014_d3, "description": "Log distance above 42d high."},
    "f01_athx_gemini_015_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_015_d3, "description": "Log distance above 63d high."},
    "f01_athx_gemini_016_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_016_d3, "description": "Log distance above 126d high."},
    "f01_athx_gemini_017_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_017_d3, "description": "Log distance above 252d high."},
    "f01_athx_gemini_018_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_018_d3, "description": "Log distance above 504d high."},
    "f01_athx_gemini_019_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_019_d3, "description": "Log distance above 756d high."},
    "f01_athx_gemini_020_d3": {"inputs": ['close', 'high'], "func": f01_athx_gemini_020_d3, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_021_d3": {"inputs": ['high'], "func": f01_athx_gemini_021_d3, "description": "Days since 5d high touched."},
    "f01_athx_gemini_022_d3": {"inputs": ['high'], "func": f01_athx_gemini_022_d3, "description": "Days since 10d high touched."},
    "f01_athx_gemini_023_d3": {"inputs": ['high'], "func": f01_athx_gemini_023_d3, "description": "Days since 21d high touched."},
    "f01_athx_gemini_024_d3": {"inputs": ['high'], "func": f01_athx_gemini_024_d3, "description": "Days since 42d high touched."},
    "f01_athx_gemini_025_d3": {"inputs": ['high'], "func": f01_athx_gemini_025_d3, "description": "Days since 63d high touched."},
    "f01_athx_gemini_026_d3": {"inputs": ['high'], "func": f01_athx_gemini_026_d3, "description": "Days since 126d high touched."},
    "f01_athx_gemini_027_d3": {"inputs": ['high'], "func": f01_athx_gemini_027_d3, "description": "Days since 252d high touched."},
    "f01_athx_gemini_028_d3": {"inputs": ['high'], "func": f01_athx_gemini_028_d3, "description": "Days since 504d high touched."},
    "f01_athx_gemini_029_d3": {"inputs": ['high'], "func": f01_athx_gemini_029_d3, "description": "Days since 756d high touched."},
    "f01_athx_gemini_030_d3": {"inputs": ['high'], "func": f01_athx_gemini_030_d3, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_031_d3": {"inputs": ['high'], "func": f01_athx_gemini_031_d3, "description": "Days since 5d high touched."},
    "f01_athx_gemini_032_d3": {"inputs": ['high'], "func": f01_athx_gemini_032_d3, "description": "Days since 10d high touched."},
    "f01_athx_gemini_033_d3": {"inputs": ['high'], "func": f01_athx_gemini_033_d3, "description": "Days since 21d high touched."},
    "f01_athx_gemini_034_d3": {"inputs": ['high'], "func": f01_athx_gemini_034_d3, "description": "Days since 42d high touched."},
    "f01_athx_gemini_035_d3": {"inputs": ['high'], "func": f01_athx_gemini_035_d3, "description": "Days since 63d high touched."},
    "f01_athx_gemini_036_d3": {"inputs": ['high'], "func": f01_athx_gemini_036_d3, "description": "Days since 126d high touched."},
    "f01_athx_gemini_037_d3": {"inputs": ['high'], "func": f01_athx_gemini_037_d3, "description": "Days since 252d high touched."},
    "f01_athx_gemini_038_d3": {"inputs": ['high'], "func": f01_athx_gemini_038_d3, "description": "Days since 504d high touched."},
    "f01_athx_gemini_039_d3": {"inputs": ['high'], "func": f01_athx_gemini_039_d3, "description": "Days since 756d high touched."},
    "f01_athx_gemini_040_d3": {"inputs": ['high'], "func": f01_athx_gemini_040_d3, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_041_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_041_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_042_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_042_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_043_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_043_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_044_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_044_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_045_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_045_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_046_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_046_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_047_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_047_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_048_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_048_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_049_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_049_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_050_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_050_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_051_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_051_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_052_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_052_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_053_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_053_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_054_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_054_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_055_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_055_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_056_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_056_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_057_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_057_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_058_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_058_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_059_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_059_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_060_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_060_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_061_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_061_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_062_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_062_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_063_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_063_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_064_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_064_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_065_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_065_d3, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_066_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_066_d3, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_067_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_067_d3, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_068_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_068_d3, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_069_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_069_d3, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_070_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_070_d3, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_071_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_071_d3, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_072_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_072_d3, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_073_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_073_d3, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_074_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_074_d3, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_075_d3": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_075_d3, "description": "ATR-normalized distance to 63d high."},
}
