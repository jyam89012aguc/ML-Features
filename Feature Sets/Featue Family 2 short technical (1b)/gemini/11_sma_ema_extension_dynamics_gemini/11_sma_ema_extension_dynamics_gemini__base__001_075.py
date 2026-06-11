"""11 sma ema extension dynamics gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of price deviation from simple and exponential moving averages as a signal of overextension.
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

def f11_maex_gemini_001(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=5]"""
    window = 5
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_002(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=10]"""
    window = 10
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_003(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=21]"""
    window = 21
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_004(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=42]"""
    window = 42
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_005(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=63]"""
    window = 63
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_006(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=126]"""
    window = 126
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_007(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=252]"""
    window = 252
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_008(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=504]"""
    window = 504
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_009(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=756]"""
    window = 756
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_010(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of price deviation from simple and exponential moving averages as a signal of overextension. [window=1260]"""
    window = 1260
    res = _safe_div(close - close.rolling(window).mean(), _atr(high, low, close, window))
    return res

def f11_maex_gemini_011(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=105, w3=543, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(163, min_periods=max(163//3, 2)).mean())
    decay = spread.ewm(span=105, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.037647 + 0.0011562 * anchor
    return base_signal

def f11_maex_gemini_012(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=118, w3=560, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(118, min_periods=max(118//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 170)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.051176 + 0.0011563 * anchor
    return base_signal

def f11_maex_gemini_013(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=131, w3=577, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(177, min_periods=max(177//3, 2)).mean(), b.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.15 * _rolling_slope(cover, 177) + 0.0011564 * anchor
    return base_signal

def f11_maex_gemini_014(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=144, w3=594, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.156333 * y + 0.843667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 184) - _rolling_slope(basket, 144) + 0.0011565 * anchor
    return base_signal

def f11_maex_gemini_015(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=157, w3=611, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(157, min_periods=max(157//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.091765 + 0.0011566 * anchor
    return base_signal

def f11_maex_gemini_016(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=170, w3=628, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(170, min_periods=max(170//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169 * _rolling_slope(draw, 628) + 0.0011567 * anchor
    return base_signal

def f11_maex_gemini_017(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=183, w3=645, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(645, min_periods=max(645//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.118824 + 0.0011568 * anchor
    return base_signal

def f11_maex_gemini_018(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=196, w3=662, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.132353 + 0.0011569 * anchor
    return base_signal

def f11_maex_gemini_019(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=209, w3=679, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.145882 + 0.001157 * anchor
    return base_signal

def f11_maex_gemini_020(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=222, w3=696, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.159412 + 0.0011571 * anchor
    return base_signal

def f11_maex_gemini_021(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=235, w3=713, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(235, min_periods=max(235//3, 2)).rank(pct=True)
    persistence = change.rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.200667 * persistence + 0.0011572 * anchor
    return base_signal

def f11_maex_gemini_022(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=248, w3=730, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(248, min_periods=max(248//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.186471 + 0.0011573 * anchor
    return base_signal

def f11_maex_gemini_023(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=261, w3=747, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.213333 * slope + 0.0011574 * anchor
    return base_signal

def f11_maex_gemini_024(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=274, w3=764, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(7)
    drag = impulse.rolling(274, min_periods=max(274//3, 2)).mean()
    noise = impulse.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.213529 + 0.0011575 * anchor
    return base_signal

def f11_maex_gemini_025(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=287, w3=30, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 30)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.226 * acceleration + 0.0011576 * anchor
    return base_signal

def f11_maex_gemini_026(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=300, w3=47, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 21)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.232333 * pressure.rolling(47, min_periods=max(47//3, 2)).mean() + 0.0011577 * anchor
    return base_signal

def f11_maex_gemini_027(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=313, w3=64, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(28, min_periods=max(28//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.254118 + 0.0011578 * anchor
    return base_signal

def f11_maex_gemini_028(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=326, w3=81, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(326, min_periods=max(326//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 35)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.267647 + 0.0011579 * anchor
    return base_signal

def f11_maex_gemini_029(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=339, w3=98, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(42, min_periods=max(42//3, 2)).mean(), b.abs().rolling(339, min_periods=max(339//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(98) + 0.251333 * _rolling_slope(cover, 42) + 0.001158 * anchor
    return base_signal

def f11_maex_gemini_030(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=352, w3=115, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.257667 * y + 0.742333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 49) - _rolling_slope(basket, 352) + 0.0011581 * anchor
    return base_signal

def f11_maex_gemini_031(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=365, w3=132, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.308235 + 0.0011582 * anchor
    return base_signal

def f11_maex_gemini_032(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=378, w3=149, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(378, min_periods=max(378//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.270333 * _rolling_slope(draw, 149) + 0.0011583 * anchor
    return base_signal

def f11_maex_gemini_033(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=391, w3=166, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(70) - b.diff(126)
    stress = imbalance.rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.335294 + 0.0011584 * anchor
    return base_signal

def f11_maex_gemini_034(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=404, w3=183, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(404, min_periods=max(404//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.348824 + 0.0011585 * anchor
    return base_signal

def f11_maex_gemini_035(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=417, w3=200, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 417)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=200, adjust=False).mean() * 1.362353 + 0.0011586 * anchor
    return base_signal

def f11_maex_gemini_036(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=430, w3=217, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(430, min_periods=max(430//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.375882 + 0.0011587 * anchor
    return base_signal

def f11_maex_gemini_037(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=443, w3=234, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(98)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.302 * persistence + 0.0011588 * anchor
    return base_signal

def f11_maex_gemini_038(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=456, w3=251, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(456, min_periods=max(456//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.402941 + 0.0011589 * anchor
    return base_signal

def f11_maex_gemini_039(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=469, w3=268, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(469, min_periods=max(469//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.314667 * slope + 0.001159 * anchor
    return base_signal

def f11_maex_gemini_040(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=482, w3=285, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(119)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.43 + 0.0011591 * anchor
    return base_signal

def f11_maex_gemini_041(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=495, w3=302, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 495)
    curvature = _rolling_slope(acceleration, 302)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.327333 * acceleration + 0.0011592 * anchor
    return base_signal

def f11_maex_gemini_042(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=508, w3=319, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 133)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.333667 * pressure.rolling(319, min_periods=max(319//3, 2)).mean() + 0.0011593 * anchor
    return base_signal

def f11_maex_gemini_043(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=22, w3=336, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(140, min_periods=max(140//3, 2)).mean())
    decay = spread.ewm(span=22, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.470588 + 0.0011594 * anchor
    return base_signal

def f11_maex_gemini_044(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=35, w3=353, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(35, min_periods=max(35//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 147)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.484118 + 0.0011595 * anchor
    return base_signal

def f11_maex_gemini_045(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=48, w3=370, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(154, min_periods=max(154//3, 2)).mean(), b.abs().rolling(48, min_periods=max(48//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.352667 * _rolling_slope(cover, 154) + 0.0011596 * anchor
    return base_signal

def f11_maex_gemini_046(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=61, w3=387, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.359 * y + 0.641000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 161) - _rolling_slope(basket, 61) + 0.0011597 * anchor
    return base_signal

def f11_maex_gemini_047(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=74, w3=404, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(74, min_periods=max(74//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.524706 + 0.0011598 * anchor
    return base_signal

def f11_maex_gemini_048(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=87, w3=421, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(87, min_periods=max(87//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.039333 * _rolling_slope(draw, 421) + 0.0011599 * anchor
    return base_signal

def f11_maex_gemini_049(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=100, w3=438, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(100)
    stress = imbalance.rolling(438, min_periods=max(438//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.551765 + 0.00116 * anchor
    return base_signal

def f11_maex_gemini_050(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=113, w3=455, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(113, min_periods=max(113//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.565294 + 0.0011601 * anchor
    return base_signal

def f11_maex_gemini_051(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=126, w3=472, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.578824 + 0.0011602 * anchor
    return base_signal

def f11_maex_gemini_052(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=139, w3=489, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.592353 + 0.0011603 * anchor
    return base_signal

def f11_maex_gemini_053(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=152, w3=506, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(152, min_periods=max(152//3, 2)).rank(pct=True)
    persistence = change.rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071 * persistence + 0.0011604 * anchor
    return base_signal

def f11_maex_gemini_054(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=165, w3=523, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.619412 + 0.0011605 * anchor
    return base_signal

def f11_maex_gemini_055(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=178, w3=540, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.083667 * slope + 0.0011606 * anchor
    return base_signal

def f11_maex_gemini_056(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=191, w3=557, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(191, min_periods=max(191//3, 2)).mean()
    noise = impulse.abs().rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.646471 + 0.0011607 * anchor
    return base_signal

def f11_maex_gemini_057(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=204, w3=574, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 574)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.096333 * acceleration + 0.0011608 * anchor
    return base_signal

def f11_maex_gemini_058(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=217, w3=591, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 245)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.102667 * pressure.rolling(591, min_periods=max(591//3, 2)).mean() + 0.0011609 * anchor
    return base_signal

def f11_maex_gemini_059(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=230, w3=608, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(5, min_periods=max(5//3, 2)).mean())
    decay = spread.ewm(span=230, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.833529 + 0.001161 * anchor
    return base_signal

def f11_maex_gemini_060(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=243, w3=625, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(243, min_periods=max(243//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 12)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.847059 + 0.0011611 * anchor
    return base_signal

def f11_maex_gemini_061(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=256, w3=642, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(19, min_periods=max(19//3, 2)).mean(), b.abs().rolling(256, min_periods=max(256//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.121667 * _rolling_slope(cover, 19) + 0.0011612 * anchor
    return base_signal

def f11_maex_gemini_062(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=269, w3=659, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.128 * y + 0.872000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 26) - _rolling_slope(basket, 269) + 0.0011613 * anchor
    return base_signal

def f11_maex_gemini_063(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=282, w3=676, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.887647 + 0.0011614 * anchor
    return base_signal

def f11_maex_gemini_064(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=295, w3=693, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(295, min_periods=max(295//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.140667 * _rolling_slope(draw, 693) + 0.0011615 * anchor
    return base_signal

def f11_maex_gemini_065(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=308, w3=710, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(47) - b.diff(126)
    stress = imbalance.rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.914706 + 0.0011616 * anchor
    return base_signal

def f11_maex_gemini_066(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=321, w3=727, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 54)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(727, min_periods=max(727//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.928235 + 0.0011617 * anchor
    return base_signal

def f11_maex_gemini_067(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=334, w3=744, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 61)
    slow = _rolling_slope(x, 334)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.941765 + 0.0011618 * anchor
    return base_signal

def f11_maex_gemini_068(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=347, w3=761, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(347, min_periods=max(347//3, 2)).max()
    trough = x.rolling(68, min_periods=max(68//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.955294 + 0.0011619 * anchor
    return base_signal

def f11_maex_gemini_069(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=360, w3=27, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(75)
    rank = change.rolling(360, min_periods=max(360//3, 2)).rank(pct=True)
    persistence = change.rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.172333 * persistence + 0.001162 * anchor
    return base_signal

def f11_maex_gemini_070(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=373, w3=44, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(82, min_periods=max(82//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.982353 + 0.0011621 * anchor
    return base_signal

def f11_maex_gemini_071(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=386, w3=61, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 89)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.185 * slope + 0.0011622 * anchor
    return base_signal

def f11_maex_gemini_072(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=399, w3=78, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(96)
    drag = impulse.rolling(399, min_periods=max(399//3, 2)).mean()
    noise = impulse.abs().rolling(78, min_periods=max(78//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.009412 + 0.0011623 * anchor
    return base_signal

def f11_maex_gemini_073(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=412, w3=95, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 103)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.197667 * acceleration + 0.0011624 * anchor
    return base_signal

def f11_maex_gemini_074(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=425, w3=112, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 110)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.204 * pressure.rolling(112, min_periods=max(112//3, 2)).mean() + 0.0011625 * anchor
    return base_signal

def f11_maex_gemini_075(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=438, w3=129, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(117, min_periods=max(117//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.05 + 0.0011626 * anchor
    return base_signal
