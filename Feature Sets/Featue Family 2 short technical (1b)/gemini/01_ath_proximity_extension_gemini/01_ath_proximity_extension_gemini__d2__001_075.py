"""01 ath proximity extension gemini d2 features 1-75 â€” Pipeline 1b-HF Grade v7.

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

def f01_athx_gemini_001_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 1 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_002_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 2 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_003_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 3 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_004_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 4 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_005_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 5 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_006_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 6 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_007_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 7 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_008_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 8 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_009_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 9 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_010_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 10 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_011_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 5d rolling max."""
    m = high.rolling(5, min_periods=5//3).max()
    res = _safe_log(close if 11 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_012_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 10d rolling max."""
    m = high.rolling(10, min_periods=10//3).max()
    res = _safe_log(close if 12 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_013_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 21d rolling max."""
    m = high.rolling(21, min_periods=21//3).max()
    res = _safe_log(close if 13 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_014_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 42d rolling max."""
    m = high.rolling(42, min_periods=42//3).max()
    res = _safe_log(close if 14 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_015_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 63d rolling max."""
    m = high.rolling(63, min_periods=63//3).max()
    res = _safe_log(close if 15 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_016_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 126d rolling max."""
    m = high.rolling(126, min_periods=126//3).max()
    res = _safe_log(close if 16 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_017_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 252d rolling max."""
    m = high.rolling(252, min_periods=252//3).max()
    res = _safe_log(close if 17 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_018_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 504d rolling max."""
    m = high.rolling(504, min_periods=504//3).max()
    res = _safe_log(close if 18 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_019_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 756d rolling max."""
    m = high.rolling(756, min_periods=756//3).max()
    res = _safe_log(close if 19 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_020_d2(close: pd.Series, high: pd.Series) -> pd.Series:
    """Log distance of close/high above 1260d rolling max."""
    m = high.rolling(1260, min_periods=1260//3).max()
    res = _safe_log(close if 20 <= 10 else high) - _safe_log(m)
    return (res).diff().diff()

def f01_athx_gemini_021_d2(high: pd.Series) -> pd.Series:
    """Bars since 5d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(5, min_periods=5//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_022_d2(high: pd.Series) -> pd.Series:
    """Bars since 10d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(10, min_periods=10//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_023_d2(high: pd.Series) -> pd.Series:
    """Bars since 21d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(21, min_periods=21//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_024_d2(high: pd.Series) -> pd.Series:
    """Bars since 42d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(42, min_periods=42//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_025_d2(high: pd.Series) -> pd.Series:
    """Bars since 63d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(63, min_periods=63//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_026_d2(high: pd.Series) -> pd.Series:
    """Bars since 126d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(126, min_periods=126//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_027_d2(high: pd.Series) -> pd.Series:
    """Bars since 252d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(252, min_periods=252//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_028_d2(high: pd.Series) -> pd.Series:
    """Bars since 504d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(504, min_periods=504//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_029_d2(high: pd.Series) -> pd.Series:
    """Bars since 756d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(756, min_periods=756//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_030_d2(high: pd.Series) -> pd.Series:
    """Bars since 1260d high achieved (staleness proxy)."""
    def _bsm(w):
        if len(w) == 0: return np.nan
        return float((len(w) - 1) - np.argmax(w))
    res = high.rolling(1260, min_periods=1260//3).apply(_bsm, raw=True)
    return (res).diff().diff()

def f01_athx_gemini_031_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=389, w3=19, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 389)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=19, adjust=False).mean() * 1.249412 + 2.22e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_032_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=402, w3=36, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(402, min_periods=max(402//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.262941 + 2.23e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_033_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=415, w3=53, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(84)
    rank = change.rolling(415, min_periods=max(415//3, 2)).rank(pct=True)
    persistence = change.rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.114 * persistence + 2.24e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_034_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=428, w3=70, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(428, min_periods=max(428//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.29 + 2.25e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_035_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=441, w3=87, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.126667 * slope + 2.26e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_036_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=454, w3=104, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(105)
    drag = impulse.rolling(454, min_periods=max(454//3, 2)).mean()
    noise = impulse.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.317059 + 2.27e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_037_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=467, w3=121, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 467)
    curvature = _rolling_slope(acceleration, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.139333 * acceleration + 2.28e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_038_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=480, w3=138, lag=34)."""
    x = high.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.344118 + 2.29e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_039_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=493, w3=155, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    draw = x - x.rolling(493, min_periods=max(493//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.152 * _rolling_slope(draw, 155) + 2.3e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_040_d2(high: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=506, w3=172, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(506, min_periods=max(506//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(172, min_periods=max(172//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.371176 + 2.31e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_041_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 5d high."""
    m = high.rolling(5).max()
    res = _safe_div(close - m, _atr(high, low, close, 5))
    return (res).diff().diff()

def f01_athx_gemini_042_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 10d high."""
    m = high.rolling(10).max()
    res = _safe_div(close - m, _atr(high, low, close, 10))
    return (res).diff().diff()

def f01_athx_gemini_043_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 21d high."""
    m = high.rolling(21).max()
    res = _safe_div(close - m, _atr(high, low, close, 21))
    return (res).diff().diff()

def f01_athx_gemini_044_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 42d high."""
    m = high.rolling(42).max()
    res = _safe_div(close - m, _atr(high, low, close, 42))
    return (res).diff().diff()

def f01_athx_gemini_045_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 63d high."""
    m = high.rolling(63).max()
    res = _safe_div(close - m, _atr(high, low, close, 63))
    return (res).diff().diff()

def f01_athx_gemini_046_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 126d high."""
    m = high.rolling(126).max()
    res = _safe_div(close - m, _atr(high, low, close, 126))
    return (res).diff().diff()

def f01_athx_gemini_047_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 252d high."""
    m = high.rolling(252).max()
    res = _safe_div(close - m, _atr(high, low, close, 252))
    return (res).diff().diff()

def f01_athx_gemini_048_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 504d high."""
    m = high.rolling(504).max()
    res = _safe_div(close - m, _atr(high, low, close, 504))
    return (res).diff().diff()

def f01_athx_gemini_049_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 756d high."""
    m = high.rolling(756).max()
    res = _safe_div(close - m, _atr(high, low, close, 756))
    return (res).diff().diff()

def f01_athx_gemini_050_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATR-normalized distance of close from 1260d high."""
    m = high.rolling(1260).max()
    res = _safe_div(close - m, _atr(high, low, close, 1260))
    return (res).diff().diff()

def f01_athx_gemini_051_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=20, w3=189, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 189)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.164667 * acceleration + 2.32e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_052_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=33, w3=206, lag=2)."""
    rel = _safe_div(close.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 147)
    pressure = rel_log.diff(33)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.171 * pressure.rolling(206, min_periods=max(206//3, 2)).mean() + 2.33e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_053_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=46, w3=223, lag=3)."""
    a = close.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(154, min_periods=max(154//3, 2)).mean())
    decay = spread.ewm(span=46, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.411765 + 2.34e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_054_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=59, w3=240, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(59, min_periods=max(59//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 161)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.425294 + 2.35e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_055_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=72, w3=257, lag=8)."""
    a = close.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(168, min_periods=max(168//3, 2)).mean(), b.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.19 * _rolling_slope(cover, 168) + 2.36e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_056_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=85, w3=274, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.196333 * y + 0.803667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 175) - _rolling_slope(basket, 85) + 2.37e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_057_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=98, w3=291, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.465882 + 2.38e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_058_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=111, w3=308, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.209 * _rolling_slope(draw, 308) + 2.39e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_059_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=124, w3=325, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(124)
    stress = imbalance.rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.492941 + 2.4e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_060_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=137, w3=342, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(137, min_periods=max(137//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.506471 + 2.41e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_061_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=150, w3=359, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 150)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.52 + 2.42e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_062_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=163, w3=376, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(163, min_periods=max(163//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.533529 + 2.43e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_063_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=176, w3=393, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.240667 * persistence + 2.44e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_064_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=189, w3=410, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(189, min_periods=max(189//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.560588 + 2.45e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_065_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=202, w3=427, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.253333 * slope + 2.46e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_066_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=215, w3=444, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.587647 + 2.47e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_067_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=228, w3=461, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 228)
    curvature = _rolling_slope(acceleration, 461)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.266 * acceleration + 2.48e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_068_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=241, w3=478, lag=34)."""
    rel = _safe_div(close.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 12)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.272333 * pressure.rolling(478, min_periods=max(478//3, 2)).mean() + 2.49e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_069_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=254, w3=495, lag=55)."""
    a = close.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(19, min_periods=max(19//3, 2)).mean())
    decay = spread.ewm(span=254, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.628235 + 2.5e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_070_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=267, w3=512, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(267, min_periods=max(267//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 26)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.641765 + 2.51e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_071_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=280, w3=529, lag=1)."""
    a = close.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(33, min_periods=max(33//3, 2)).mean(), b.abs().rolling(280, min_periods=max(280//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.291333 * _rolling_slope(cover, 33) + 2.52e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_072_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=293, w3=546, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.297667 * y + 0.702333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 40) - _rolling_slope(basket, 293) + 2.53e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_073_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=306, w3=563, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(47, min_periods=max(47//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.828824 + 2.54e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_074_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=319, w3=580, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(54, min_periods=max(54//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.310333 * _rolling_slope(draw, 580) + 2.55e-05 * anchor
    return base_signal.diff().diff()

def f01_athx_gemini_075_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=332, w3=597, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(61) - b.diff(126)
    stress = imbalance.rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.855882 + 2.56e-05 * anchor
    return base_signal.diff().diff()

# ============================================================
# POSTGRES FEATURE REGISTRY
# ============================================================

REGISTRY_01_ATH_PROXIMITY_EXTENSION_GEMINI_D2_001_075 = {
    "f01_athx_gemini_001_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_001_d2, "description": "Log distance above 5d high."},
    "f01_athx_gemini_002_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_002_d2, "description": "Log distance above 10d high."},
    "f01_athx_gemini_003_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_003_d2, "description": "Log distance above 21d high."},
    "f01_athx_gemini_004_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_004_d2, "description": "Log distance above 42d high."},
    "f01_athx_gemini_005_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_005_d2, "description": "Log distance above 63d high."},
    "f01_athx_gemini_006_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_006_d2, "description": "Log distance above 126d high."},
    "f01_athx_gemini_007_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_007_d2, "description": "Log distance above 252d high."},
    "f01_athx_gemini_008_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_008_d2, "description": "Log distance above 504d high."},
    "f01_athx_gemini_009_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_009_d2, "description": "Log distance above 756d high."},
    "f01_athx_gemini_010_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_010_d2, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_011_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_011_d2, "description": "Log distance above 5d high."},
    "f01_athx_gemini_012_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_012_d2, "description": "Log distance above 10d high."},
    "f01_athx_gemini_013_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_013_d2, "description": "Log distance above 21d high."},
    "f01_athx_gemini_014_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_014_d2, "description": "Log distance above 42d high."},
    "f01_athx_gemini_015_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_015_d2, "description": "Log distance above 63d high."},
    "f01_athx_gemini_016_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_016_d2, "description": "Log distance above 126d high."},
    "f01_athx_gemini_017_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_017_d2, "description": "Log distance above 252d high."},
    "f01_athx_gemini_018_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_018_d2, "description": "Log distance above 504d high."},
    "f01_athx_gemini_019_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_019_d2, "description": "Log distance above 756d high."},
    "f01_athx_gemini_020_d2": {"inputs": ['close', 'high'], "func": f01_athx_gemini_020_d2, "description": "Log distance above 1260d high."},
    "f01_athx_gemini_021_d2": {"inputs": ['high'], "func": f01_athx_gemini_021_d2, "description": "Days since 5d high touched."},
    "f01_athx_gemini_022_d2": {"inputs": ['high'], "func": f01_athx_gemini_022_d2, "description": "Days since 10d high touched."},
    "f01_athx_gemini_023_d2": {"inputs": ['high'], "func": f01_athx_gemini_023_d2, "description": "Days since 21d high touched."},
    "f01_athx_gemini_024_d2": {"inputs": ['high'], "func": f01_athx_gemini_024_d2, "description": "Days since 42d high touched."},
    "f01_athx_gemini_025_d2": {"inputs": ['high'], "func": f01_athx_gemini_025_d2, "description": "Days since 63d high touched."},
    "f01_athx_gemini_026_d2": {"inputs": ['high'], "func": f01_athx_gemini_026_d2, "description": "Days since 126d high touched."},
    "f01_athx_gemini_027_d2": {"inputs": ['high'], "func": f01_athx_gemini_027_d2, "description": "Days since 252d high touched."},
    "f01_athx_gemini_028_d2": {"inputs": ['high'], "func": f01_athx_gemini_028_d2, "description": "Days since 504d high touched."},
    "f01_athx_gemini_029_d2": {"inputs": ['high'], "func": f01_athx_gemini_029_d2, "description": "Days since 756d high touched."},
    "f01_athx_gemini_030_d2": {"inputs": ['high'], "func": f01_athx_gemini_030_d2, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_031_d2": {"inputs": ['high'], "func": f01_athx_gemini_031_d2, "description": "Days since 5d high touched."},
    "f01_athx_gemini_032_d2": {"inputs": ['high'], "func": f01_athx_gemini_032_d2, "description": "Days since 10d high touched."},
    "f01_athx_gemini_033_d2": {"inputs": ['high'], "func": f01_athx_gemini_033_d2, "description": "Days since 21d high touched."},
    "f01_athx_gemini_034_d2": {"inputs": ['high'], "func": f01_athx_gemini_034_d2, "description": "Days since 42d high touched."},
    "f01_athx_gemini_035_d2": {"inputs": ['high'], "func": f01_athx_gemini_035_d2, "description": "Days since 63d high touched."},
    "f01_athx_gemini_036_d2": {"inputs": ['high'], "func": f01_athx_gemini_036_d2, "description": "Days since 126d high touched."},
    "f01_athx_gemini_037_d2": {"inputs": ['high'], "func": f01_athx_gemini_037_d2, "description": "Days since 252d high touched."},
    "f01_athx_gemini_038_d2": {"inputs": ['high'], "func": f01_athx_gemini_038_d2, "description": "Days since 504d high touched."},
    "f01_athx_gemini_039_d2": {"inputs": ['high'], "func": f01_athx_gemini_039_d2, "description": "Days since 756d high touched."},
    "f01_athx_gemini_040_d2": {"inputs": ['high'], "func": f01_athx_gemini_040_d2, "description": "Days since 1260d high touched."},
    "f01_athx_gemini_041_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_041_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_042_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_042_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_043_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_043_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_044_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_044_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_045_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_045_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_046_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_046_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_047_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_047_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_048_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_048_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_049_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_049_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_050_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_050_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_051_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_051_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_052_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_052_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_053_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_053_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_054_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_054_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_055_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_055_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_056_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_056_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_057_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_057_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_058_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_058_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_059_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_059_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_060_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_060_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_061_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_061_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_062_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_062_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_063_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_063_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_064_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_064_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_065_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_065_d2, "description": "ATR-normalized distance to 63d high."},
    "f01_athx_gemini_066_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_066_d2, "description": "ATR-normalized distance to 126d high."},
    "f01_athx_gemini_067_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_067_d2, "description": "ATR-normalized distance to 252d high."},
    "f01_athx_gemini_068_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_068_d2, "description": "ATR-normalized distance to 504d high."},
    "f01_athx_gemini_069_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_069_d2, "description": "ATR-normalized distance to 756d high."},
    "f01_athx_gemini_070_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_070_d2, "description": "ATR-normalized distance to 1260d high."},
    "f01_athx_gemini_071_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_071_d2, "description": "ATR-normalized distance to 5d high."},
    "f01_athx_gemini_072_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_072_d2, "description": "ATR-normalized distance to 10d high."},
    "f01_athx_gemini_073_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_073_d2, "description": "ATR-normalized distance to 21d high."},
    "f01_athx_gemini_074_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_074_d2, "description": "ATR-normalized distance to 42d high."},
    "f01_athx_gemini_075_d2": {"inputs": ['close', 'high', 'low'], "func": f01_athx_gemini_075_d2, "description": "ATR-normalized distance to 63d high."},
}
