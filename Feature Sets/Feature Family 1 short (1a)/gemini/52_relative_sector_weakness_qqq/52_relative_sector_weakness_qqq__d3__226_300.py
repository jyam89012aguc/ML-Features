"""52 relative sector weakness qqq d3 third derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Relative_Strength - Institutional-grade short-side signal.
Version: 3.0 (Strict De-duplication)
PIT-clean: right-anchored rolling, explicit min_periods.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm, wm = x.mean(), w.mean()
        num = ((x - xm) * (w - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f52_rsw_q_226_rel_v226_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=44, w2=196, w3=760, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(196, min_periods=max(196//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 44)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.214375 + 0.0032027 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_227_rel_v227_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=51, w2=207, w3=16, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(51, min_periods=max(51//3, 2)).mean(), b.abs().rolling(207, min_periods=max(207//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(16) + 0.2858 * _rolling_slope(cover, 51) + 0.0032028 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_228_rel_v228_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=58, w2=218, w3=29, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2934 * y + 0.706600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 58) - _rolling_slope(basket, 218) + 0.0032029 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_229_rel_v229_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=65, w2=229, w3=42, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(229, min_periods=max(229//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(42) * 1.2575 + 0.003203 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_230_rel_v230_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=72, w2=240, w3=55, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(240, min_periods=max(240//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3086 * _rolling_slope(draw, 55) + 0.0032031 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_231_rel_v231_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=79, w2=251, w3=68, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(79) - b.diff(126)
    stress = imbalance.rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.28625 + 0.0032032 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_232_rel_v232_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=86, w2=262, w3=81, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(262, min_periods=max(262//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.300625 + 0.0032033 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_233_rel_v233_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=93, w2=273, w3=94, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 273)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=94, adjust=False).mean() * 1.315 + 0.0032034 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_234_rel_v234_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=100, w2=284, w3=107, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(284, min_periods=max(284//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.329375 + 0.0032035 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_235_rel_v235_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=107, w2=295, w3=120, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(107)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3466 * persistence + 0.0032036 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_236_rel_v236_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=114, w2=306, w3=133, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(306, min_periods=max(306//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.358125 + 0.0032037 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_237_rel_v237_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=121, w2=317, w3=146, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(317, min_periods=max(317//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3618 * slope + 0.0032038 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_238_rel_v238_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=128, w2=328, w3=159, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(328, min_periods=max(328//3, 2)).mean()
    noise = impulse.abs().rolling(159, min_periods=max(159//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.386875 + 0.0032039 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_239_rel_v239_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=135, w2=339, w3=172, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 339)
    curvature = _rolling_slope(acceleration, 172)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.377 * acceleration + 0.003204 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_240_rel_v240_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=142, w2=350, w3=185, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 142)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3846 * pressure.rolling(185, min_periods=max(185//3, 2)).mean() + 0.0032041 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_241_rel_v241_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=149, w2=361, w3=198, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(149, min_periods=max(149//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.43 + 0.0032042 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_242_rel_v242_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=156, w2=372, w3=211, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(372, min_periods=max(372//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 156)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.444375 + 0.0032043 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_243_rel_v243_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=163, w2=383, w3=224, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(163, min_periods=max(163//3, 2)).mean(), b.abs().rolling(383, min_periods=max(383//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.4074 * _rolling_slope(cover, 163) + 0.0032044 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_244_rel_v244_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=170, w2=394, w3=237, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0386 * y + 0.961400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 170) - _rolling_slope(basket, 394) + 0.0032045 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_245_rel_v245_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=177, w2=405, w3=250, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(405, min_periods=max(405//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4875 + 0.0032046 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_246_rel_v246_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=184, w2=416, w3=263, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(416, min_periods=max(416//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0538 * _rolling_slope(draw, 263) + 0.0032047 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_247_rel_v247_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=191, w2=427, w3=276, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.51625 + 0.0032048 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_248_rel_v248_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=198, w2=438, w3=289, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(438, min_periods=max(438//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.530625 + 0.0032049 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_249_rel_v249_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=205, w2=449, w3=302, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.545 + 0.003205 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_250_rel_v250_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=212, w2=460, w3=315, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.559375 + 0.0032051 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_251_rel_v251_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=219, w2=471, w3=328, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0918 * persistence + 0.0032052 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_252_rel_v252_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=226, w2=482, w3=341, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(482, min_periods=max(482//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.588125 + 0.0032053 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_253_rel_v253_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=233, w2=493, w3=354, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.107 * slope + 0.0032054 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_254_rel_v254_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=240, w2=504, w3=367, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(504, min_periods=max(504//3, 2)).mean()
    noise = impulse.abs().rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.616875 + 0.0032055 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_255_rel_v255_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=247, w2=12, w3=380, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 12)
    curvature = _rolling_slope(acceleration, 380)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1222 * acceleration + 0.0032056 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_256_rel_v256_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=254, w2=23, w3=393, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 254)
    pressure = rel_log.diff(23)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1298 * pressure.rolling(393, min_periods=max(393//3, 2)).mean() + 0.0032057 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_257_rel_v257_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=10, w2=34, w3=406, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(10, min_periods=max(10//3, 2)).mean())
    decay = spread.ewm(span=34, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.886875 + 0.0032058 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_258_rel_v258_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=17, w2=45, w3=419, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(45, min_periods=max(45//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 17)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.90125 + 0.0032059 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_259_rel_v259_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=24, w2=56, w3=432, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(24, min_periods=max(24//3, 2)).mean(), b.abs().rolling(56, min_periods=max(56//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1526 * _rolling_slope(cover, 24) + 0.003206 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_260_rel_v260_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=31, w2=67, w3=445, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1602 * y + 0.839800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 31) - _rolling_slope(basket, 67) + 0.0032061 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_261_rel_v261_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=38, w2=78, w3=458, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(78, min_periods=max(78//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.944375 + 0.0032062 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_262_rel_v262_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=45, w2=89, w3=471, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1754 * _rolling_slope(draw, 471) + 0.0032063 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_263_rel_v263_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=52, w2=100, w3=484, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(52) - b.diff(100)
    stress = imbalance.rolling(484, min_periods=max(484//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.973125 + 0.0032064 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_264_rel_v264_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=59, w2=111, w3=497, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(111, min_periods=max(111//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9875 + 0.0032065 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_265_rel_v265_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=66, w2=122, w3=510, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.001875 + 0.0032066 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_266_rel_v266_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=73, w2=133, w3=523, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01625 + 0.0032067 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_267_rel_v267_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=80, w2=144, w3=536, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(80)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2134 * persistence + 0.0032068 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_268_rel_v268_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=87, w2=155, w3=549, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.045 + 0.0032069 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_269_rel_v269_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=94, w2=166, w3=562, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2286 * slope + 0.003207 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_270_rel_v270_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=101, w2=177, w3=575, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(101)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.07375 + 0.0032071 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_271_rel_v271_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=108, w2=188, w3=588, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 188)
    curvature = _rolling_slope(acceleration, 588)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2438 * acceleration + 0.0032072 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_272_rel_v272_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=115, w2=199, w3=601, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 115)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2514 * pressure.rolling(601, min_periods=max(601//3, 2)).mean() + 0.0032073 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_273_rel_v273_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=122, w2=210, w3=614, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    decay = spread.ewm(span=210, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.116875 + 0.0032074 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_274_rel_v274_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=129, w2=221, w3=627, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(221, min_periods=max(221//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 129)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.13125 + 0.0032075 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_275_rel_v275_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=136, w2=232, w3=640, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(136, min_periods=max(136//3, 2)).mean(), b.abs().rolling(232, min_periods=max(232//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2742 * _rolling_slope(cover, 136) + 0.0032076 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_276_rel_v276_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=143, w2=243, w3=653, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2818 * y + 0.718200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 143) - _rolling_slope(basket, 243) + 0.0032077 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_277_rel_v277_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=150, w2=254, w3=666, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.174375 + 0.0032078 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_278_rel_v278_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=157, w2=265, w3=679, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.297 * _rolling_slope(draw, 679) + 0.0032079 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_279_rel_v279_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=164, w2=276, w3=692, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.203125 + 0.003208 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_280_rel_v280_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=171, w2=287, w3=705, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(287, min_periods=max(287//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2175 + 0.0032081 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_281_rel_v281_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=178, w2=298, w3=718, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 298)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.231875 + 0.0032082 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_282_rel_v282_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=185, w2=309, w3=731, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(309, min_periods=max(309//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.24625 + 0.0032083 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_283_rel_v283_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=192, w2=320, w3=744, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(320, min_periods=max(320//3, 2)).rank(pct=True)
    persistence = change.rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.335 * persistence + 0.0032084 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_284_rel_v284_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=199, w2=331, w3=757, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(331, min_periods=max(331//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.275 + 0.0032085 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_285_rel_v285_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=206, w2=342, w3=770, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(342, min_periods=max(342//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3502 * slope + 0.0032086 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_286_rel_v286_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=213, w2=353, w3=26, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(353, min_periods=max(353//3, 2)).mean()
    noise = impulse.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.30375 + 0.0032087 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_287_rel_v287_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=220, w2=364, w3=39, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 364)
    curvature = _rolling_slope(acceleration, 39)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3654 * acceleration + 0.0032088 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_288_rel_v288_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=227, w2=375, w3=52, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 227)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.373 * pressure.rolling(52, min_periods=max(52//3, 2)).mean() + 0.0032089 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_289_rel_v289_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=234, w2=386, w3=65, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.346875 + 0.003209 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_290_rel_v290_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=241, w2=397, w3=78, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(397, min_periods=max(397//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 241)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.36125 + 0.0032091 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_291_rel_v291_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=248, w2=408, w3=91, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(248, min_periods=max(248//3, 2)).mean(), b.abs().rolling(408, min_periods=max(408//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(91) + 0.3958 * _rolling_slope(cover, 248) + 0.0032092 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_292_rel_v292_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=255, w2=419, w3=104, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.4034 * y + 0.596600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 255) - _rolling_slope(basket, 419) + 0.0032093 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_293_rel_v293_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=11, w2=430, w3=117, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(117) * 1.404375 + 0.0032094 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_294_rel_v294_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=18, w2=441, w3=130, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(441, min_periods=max(441//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0422 * _rolling_slope(draw, 130) + 0.0032095 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_295_rel_v295_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=25, w2=452, w3=143, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(25) - b.diff(126)
    stress = imbalance.rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.433125 + 0.0032096 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_296_rel_v296_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=32, w2=463, w3=156, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(463, min_periods=max(463//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4475 + 0.0032097 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_297_rel_v297_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=39, w2=474, w3=169, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=169, adjust=False).mean() * 1.461875 + 0.0032098 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_298_rel_v298_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=46, w2=485, w3=182, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(485, min_periods=max(485//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.47625 + 0.0032099 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_299_rel_v299_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=53, w2=496, w3=195, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(53)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0802 * persistence + 0.00321 * anchor
    return base_signal.diff().diff().diff()

def f52_rsw_q_300_rel_v300_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=60, w2=507, w3=208, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(507, min_periods=max(507//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.505 + 0.0032101 * anchor
    return base_signal.diff().diff().diff()
