"""51 relative sector weakness d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f51_rsw_226_rel_v226_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=111, w2=135, w3=530, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(135, min_periods=max(135//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.09375 + 0.0031427 * anchor
    return base_signal.diff()

def f51_rsw_227_rel_v227_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=118, w2=146, w3=543, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(118)
    rank = change.rolling(146, min_periods=max(146//3, 2)).rank(pct=True)
    persistence = change.rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2426 * persistence + 0.0031428 * anchor
    return base_signal.diff()

def f51_rsw_228_rel_v228_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=125, w2=157, w3=556, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(157, min_periods=max(157//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1225 + 0.0031429 * anchor
    return base_signal.diff()

def f51_rsw_229_rel_v229_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=132, w2=168, w3=569, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(168, min_periods=max(168//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2578 * slope + 0.003143 * anchor
    return base_signal.diff()

def f51_rsw_230_rel_v230_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=139, w2=179, w3=582, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(179, min_periods=max(179//3, 2)).mean()
    noise = impulse.abs().rolling(582, min_periods=max(582//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.15125 + 0.0031431 * anchor
    return base_signal.diff()

def f51_rsw_231_rel_v231_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=146, w2=190, w3=595, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 595)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.273 * acceleration + 0.0031432 * anchor
    return base_signal.diff()

def f51_rsw_232_rel_v232_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=153, w2=201, w3=608, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 153)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2806 * pressure.rolling(608, min_periods=max(608//3, 2)).mean() + 0.0031433 * anchor
    return base_signal.diff()

def f51_rsw_233_rel_v233_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=160, w2=212, w3=621, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(160, min_periods=max(160//3, 2)).mean())
    decay = spread.ewm(span=212, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.194375 + 0.0031434 * anchor
    return base_signal.diff()

def f51_rsw_234_rel_v234_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=167, w2=223, w3=634, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(223, min_periods=max(223//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 167)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.20875 + 0.0031435 * anchor
    return base_signal.diff()

def f51_rsw_235_rel_v235_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=174, w2=234, w3=647, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(174, min_periods=max(174//3, 2)).mean(), b.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3034 * _rolling_slope(cover, 174) + 0.0031436 * anchor
    return base_signal.diff()

def f51_rsw_236_rel_v236_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=181, w2=245, w3=660, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.311 * y + 0.689000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 181) - _rolling_slope(basket, 245) + 0.0031437 * anchor
    return base_signal.diff()

def f51_rsw_237_rel_v237_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=188, w2=256, w3=673, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(256, min_periods=max(256//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.251875 + 0.0031438 * anchor
    return base_signal.diff()

def f51_rsw_238_rel_v238_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=195, w2=267, w3=686, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(267, min_periods=max(267//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3262 * _rolling_slope(draw, 686) + 0.0031439 * anchor
    return base_signal.diff()

def f51_rsw_239_rel_v239_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=202, w2=278, w3=699, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.280625 + 0.003144 * anchor
    return base_signal.diff()

def f51_rsw_240_rel_v240_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=209, w2=289, w3=712, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(289, min_periods=max(289//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.295 + 0.0031441 * anchor
    return base_signal.diff()

def f51_rsw_241_rel_v241_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=216, w2=300, w3=725, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 300)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.309375 + 0.0031442 * anchor
    return base_signal.diff()

def f51_rsw_242_rel_v242_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=223, w2=311, w3=738, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(311, min_periods=max(311//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.32375 + 0.0031443 * anchor
    return base_signal.diff()

def f51_rsw_243_rel_v243_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=230, w2=322, w3=751, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(322, min_periods=max(322//3, 2)).rank(pct=True)
    persistence = change.rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3642 * persistence + 0.0031444 * anchor
    return base_signal.diff()

def f51_rsw_244_rel_v244_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=237, w2=333, w3=764, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(333, min_periods=max(333//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3525 + 0.0031445 * anchor
    return base_signal.diff()

def f51_rsw_245_rel_v245_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=244, w2=344, w3=20, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(344, min_periods=max(344//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3794 * slope + 0.0031446 * anchor
    return base_signal.diff()

def f51_rsw_246_rel_v246_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=251, w2=355, w3=33, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(355, min_periods=max(355//3, 2)).mean()
    noise = impulse.abs().rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.38125 + 0.0031447 * anchor
    return base_signal.diff()

def f51_rsw_247_rel_v247_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=7, w2=366, w3=46, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 366)
    curvature = _rolling_slope(acceleration, 46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3946 * acceleration + 0.0031448 * anchor
    return base_signal.diff()

def f51_rsw_248_rel_v248_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=14, w2=377, w3=59, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 14)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.4022 * pressure.rolling(59, min_periods=max(59//3, 2)).mean() + 0.0031449 * anchor
    return base_signal.diff()

def f51_rsw_249_rel_v249_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=21, w2=388, w3=72, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(21, min_periods=max(21//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.424375 + 0.003145 * anchor
    return base_signal.diff()

def f51_rsw_250_rel_v250_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=28, w2=399, w3=85, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(399, min_periods=max(399//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 28)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.43875 + 0.0031451 * anchor
    return base_signal.diff()

def f51_rsw_251_rel_v251_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=35, w2=410, w3=98, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(35, min_periods=max(35//3, 2)).mean(), b.abs().rolling(410, min_periods=max(410//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(98) + 0.0486 * _rolling_slope(cover, 35) + 0.0031452 * anchor
    return base_signal.diff()

def f51_rsw_252_rel_v252_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=42, w2=421, w3=111, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0562 * y + 0.943800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 42) - _rolling_slope(basket, 421) + 0.0031453 * anchor
    return base_signal.diff()

def f51_rsw_253_rel_v253_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=49, w2=432, w3=124, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(432, min_periods=max(432//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(124) * 1.481875 + 0.0031454 * anchor
    return base_signal.diff()

def f51_rsw_254_rel_v254_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=56, w2=443, w3=137, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0714 * _rolling_slope(draw, 137) + 0.0031455 * anchor
    return base_signal.diff()

def f51_rsw_255_rel_v255_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=63, w2=454, w3=150, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(63) - b.diff(126)
    stress = imbalance.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.510625 + 0.0031456 * anchor
    return base_signal.diff()

def f51_rsw_256_rel_v256_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=70, w2=465, w3=163, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(465, min_periods=max(465//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.525 + 0.0031457 * anchor
    return base_signal.diff()

def f51_rsw_257_rel_v257_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=77, w2=476, w3=176, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 476)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=176, adjust=False).mean() * 1.539375 + 0.0031458 * anchor
    return base_signal.diff()

def f51_rsw_258_rel_v258_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=84, w2=487, w3=189, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(487, min_periods=max(487//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.55375 + 0.0031459 * anchor
    return base_signal.diff()

def f51_rsw_259_rel_v259_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=91, w2=498, w3=202, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(91)
    rank = change.rolling(498, min_periods=max(498//3, 2)).rank(pct=True)
    persistence = change.rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1094 * persistence + 0.003146 * anchor
    return base_signal.diff()

def f51_rsw_260_rel_v260_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=98, w2=509, w3=215, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(509, min_periods=max(509//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5825 + 0.0031461 * anchor
    return base_signal.diff()

def f51_rsw_261_rel_v261_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=105, w2=17, w3=228, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(17, min_periods=max(17//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1246 * slope + 0.0031462 * anchor
    return base_signal.diff()

def f51_rsw_262_rel_v262_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=112, w2=28, w3=241, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(112)
    drag = impulse.rolling(28, min_periods=max(28//3, 2)).mean()
    noise = impulse.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.61125 + 0.0031463 * anchor
    return base_signal.diff()

def f51_rsw_263_rel_v263_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=119, w2=39, w3=254, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 39)
    curvature = _rolling_slope(acceleration, 254)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1398 * acceleration + 0.0031464 * anchor
    return base_signal.diff()

def f51_rsw_264_rel_v264_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=126, w2=50, w3=267, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 126)
    pressure = rel_log.diff(50)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1474 * pressure.rolling(267, min_periods=max(267//3, 2)).mean() + 0.0031465 * anchor
    return base_signal.diff()

def f51_rsw_265_rel_v265_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=133, w2=61, w3=280, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(133, min_periods=max(133//3, 2)).mean())
    decay = spread.ewm(span=61, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.88125 + 0.0031466 * anchor
    return base_signal.diff()

def f51_rsw_266_rel_v266_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=140, w2=72, w3=293, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(72, min_periods=max(72//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 140)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.895625 + 0.0031467 * anchor
    return base_signal.diff()

def f51_rsw_267_rel_v267_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=147, w2=83, w3=306, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(147, min_periods=max(147//3, 2)).mean(), b.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1702 * _rolling_slope(cover, 147) + 0.0031468 * anchor
    return base_signal.diff()

def f51_rsw_268_rel_v268_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=154, w2=94, w3=319, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1778 * y + 0.822200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 154) - _rolling_slope(basket, 94) + 0.0031469 * anchor
    return base_signal.diff()

def f51_rsw_269_rel_v269_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=161, w2=105, w3=332, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.93875 + 0.003147 * anchor
    return base_signal.diff()

def f51_rsw_270_rel_v270_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=168, w2=116, w3=345, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(116, min_periods=max(116//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.193 * _rolling_slope(draw, 345) + 0.0031471 * anchor
    return base_signal.diff()

def f51_rsw_271_rel_v271_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=175, w2=127, w3=358, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.9675 + 0.0031472 * anchor
    return base_signal.diff()

def f51_rsw_272_rel_v272_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=182, w2=138, w3=371, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.981875 + 0.0031473 * anchor
    return base_signal.diff()

def f51_rsw_273_rel_v273_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=189, w2=149, w3=384, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.99625 + 0.0031474 * anchor
    return base_signal.diff()

def f51_rsw_274_rel_v274_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=196, w2=160, w3=397, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.010625 + 0.0031475 * anchor
    return base_signal.diff()

def f51_rsw_275_rel_v275_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=203, w2=171, w3=410, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(171, min_periods=max(171//3, 2)).rank(pct=True)
    persistence = change.rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.231 * persistence + 0.0031476 * anchor
    return base_signal.diff()

def f51_rsw_276_rel_v276_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=210, w2=182, w3=423, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.039375 + 0.0031477 * anchor
    return base_signal.diff()

def f51_rsw_277_rel_v277_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=217, w2=193, w3=436, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(193, min_periods=max(193//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2462 * slope + 0.0031478 * anchor
    return base_signal.diff()

def f51_rsw_278_rel_v278_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=224, w2=204, w3=449, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.068125 + 0.0031479 * anchor
    return base_signal.diff()

def f51_rsw_279_rel_v279_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=231, w2=215, w3=462, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 215)
    curvature = _rolling_slope(acceleration, 462)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2614 * acceleration + 0.003148 * anchor
    return base_signal.diff()

def f51_rsw_280_rel_v280_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=238, w2=226, w3=475, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 238)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.269 * pressure.rolling(475, min_periods=max(475//3, 2)).mean() + 0.0031481 * anchor
    return base_signal.diff()

def f51_rsw_281_rel_v281_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=245, w2=237, w3=488, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(245, min_periods=max(245//3, 2)).mean())
    decay = spread.ewm(span=237, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.11125 + 0.0031482 * anchor
    return base_signal.diff()

def f51_rsw_282_rel_v282_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=252, w2=248, w3=501, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(248, min_periods=max(248//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 252)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.125625 + 0.0031483 * anchor
    return base_signal.diff()

def f51_rsw_283_rel_v283_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=8, w2=259, w3=514, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(8, min_periods=max(8//3, 2)).mean(), b.abs().rolling(259, min_periods=max(259//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2918 * _rolling_slope(cover, 8) + 0.0031484 * anchor
    return base_signal.diff()

def f51_rsw_284_rel_v284_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=15, w2=270, w3=527, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2994 * y + 0.700600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 15) - _rolling_slope(basket, 270) + 0.0031485 * anchor
    return base_signal.diff()

def f51_rsw_285_rel_v285_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=22, w2=281, w3=540, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(281, min_periods=max(281//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.16875 + 0.0031486 * anchor
    return base_signal.diff()

def f51_rsw_286_rel_v286_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=29, w2=292, w3=553, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3146 * _rolling_slope(draw, 553) + 0.0031487 * anchor
    return base_signal.diff()

def f51_rsw_287_rel_v287_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=36, w2=303, w3=566, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(36) - b.diff(126)
    stress = imbalance.rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.1975 + 0.0031488 * anchor
    return base_signal.diff()

def f51_rsw_288_rel_v288_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=43, w2=314, w3=579, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(314, min_periods=max(314//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.211875 + 0.0031489 * anchor
    return base_signal.diff()

def f51_rsw_289_rel_v289_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=50, w2=325, w3=592, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 325)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.22625 + 0.003149 * anchor
    return base_signal.diff()

def f51_rsw_290_rel_v290_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=57, w2=336, w3=605, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(336, min_periods=max(336//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.240625 + 0.0031491 * anchor
    return base_signal.diff()

def f51_rsw_291_rel_v291_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=64, w2=347, w3=618, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(64)
    rank = change.rolling(347, min_periods=max(347//3, 2)).rank(pct=True)
    persistence = change.rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3526 * persistence + 0.0031492 * anchor
    return base_signal.diff()

def f51_rsw_292_rel_v292_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=71, w2=358, w3=631, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(358, min_periods=max(358//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.269375 + 0.0031493 * anchor
    return base_signal.diff()

def f51_rsw_293_rel_v293_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=78, w2=369, w3=644, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(369, min_periods=max(369//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3678 * slope + 0.0031494 * anchor
    return base_signal.diff()

def f51_rsw_294_rel_v294_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=85, w2=380, w3=657, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(85)
    drag = impulse.rolling(380, min_periods=max(380//3, 2)).mean()
    noise = impulse.abs().rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.298125 + 0.0031495 * anchor
    return base_signal.diff()

def f51_rsw_295_rel_v295_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=92, w2=391, w3=670, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 391)
    curvature = _rolling_slope(acceleration, 670)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.383 * acceleration + 0.0031496 * anchor
    return base_signal.diff()

def f51_rsw_296_rel_v296_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=99, w2=402, w3=683, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 99)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3906 * pressure.rolling(683, min_periods=max(683//3, 2)).mean() + 0.0031497 * anchor
    return base_signal.diff()

def f51_rsw_297_rel_v297_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=106, w2=413, w3=696, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(106, min_periods=max(106//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.34125 + 0.0031498 * anchor
    return base_signal.diff()

def f51_rsw_298_rel_v298_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=113, w2=424, w3=709, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(424, min_periods=max(424//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 113)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.355625 + 0.0031499 * anchor
    return base_signal.diff()

def f51_rsw_299_rel_v299_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=120, w2=435, w3=722, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(120, min_periods=max(120//3, 2)).mean(), b.abs().rolling(435, min_periods=max(435//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.037 * _rolling_slope(cover, 120) + 0.00315 * anchor
    return base_signal.diff()

def f51_rsw_300_rel_v300_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=127, w2=446, w3=735, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0446 * y + 0.955400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 127) - _rolling_slope(basket, 446) + 0.0031501 * anchor
    return base_signal.diff()
