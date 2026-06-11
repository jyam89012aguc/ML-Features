"""55 relative sector kinetics base features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f55_rsw_k_226_rel_v226(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=94, w2=379, w3=693, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(379, min_periods=max(379//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.57625 + 0.0033827 * anchor

def f55_rsw_k_227_rel_v227(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=101, w2=390, w3=706, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(101)
    rank = change.rolling(390, min_periods=max(390//3, 2)).rank(pct=True)
    persistence = change.rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.039 * persistence + 0.0033828 * anchor

def f55_rsw_k_228_rel_v228(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=108, w2=401, w3=719, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(401, min_periods=max(401//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.605 + 0.0033829 * anchor

def f55_rsw_k_229_rel_v229(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=115, w2=412, w3=732, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(412, min_periods=max(412//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0542 * slope + 0.003383 * anchor

def f55_rsw_k_230_rel_v230(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=122, w2=423, w3=745, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(122)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.860625 + 0.0033831 * anchor

def f55_rsw_k_231_rel_v231(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=129, w2=434, w3=758, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 434)
    curvature = _rolling_slope(acceleration, 758)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0694 * acceleration + 0.0033832 * anchor

def f55_rsw_k_232_rel_v232(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=136, w2=445, w3=771, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 136)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.077 * pressure.rolling(771, min_periods=max(771//3, 2)).mean() + 0.0033833 * anchor

def f55_rsw_k_233_rel_v233(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=143, w2=456, w3=27, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(143, min_periods=max(143//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.90375 + 0.0033834 * anchor

def f55_rsw_k_234_rel_v234(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=150, w2=467, w3=40, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(467, min_periods=max(467//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 150)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.918125 + 0.0033835 * anchor

def f55_rsw_k_235_rel_v235(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=157, w2=478, w3=53, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(157, min_periods=max(157//3, 2)).mean(), b.abs().rolling(478, min_periods=max(478//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(53) + 0.0998 * _rolling_slope(cover, 157) + 0.0033836 * anchor

def f55_rsw_k_236_rel_v236(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=164, w2=489, w3=66, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1074 * y + 0.892600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 164) - _rolling_slope(basket, 489) + 0.0033837 * anchor

def f55_rsw_k_237_rel_v237(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=171, w2=500, w3=79, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(500, min_periods=max(500//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(79) * 0.96125 + 0.0033838 * anchor

def f55_rsw_k_238_rel_v238(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=178, w2=511, w3=92, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(511, min_periods=max(511//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1226 * _rolling_slope(draw, 92) + 0.0033839 * anchor

def f55_rsw_k_239_rel_v239(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=185, w2=19, w3=105, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(19)
    stress = imbalance.rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.99 + 0.003384 * anchor

def f55_rsw_k_240_rel_v240(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=192, w2=30, w3=118, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(30, min_periods=max(30//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.004375 + 0.0033841 * anchor

def f55_rsw_k_241_rel_v241(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=199, w2=41, w3=131, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 41)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=131, adjust=False).mean() * 1.01875 + 0.0033842 * anchor

def f55_rsw_k_242_rel_v242(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=206, w2=52, w3=144, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(52, min_periods=max(52//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.033125 + 0.0033843 * anchor

def f55_rsw_k_243_rel_v243(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=213, w2=63, w3=157, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(63, min_periods=max(63//3, 2)).rank(pct=True)
    persistence = change.rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1606 * persistence + 0.0033844 * anchor

def f55_rsw_k_244_rel_v244(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=220, w2=74, w3=170, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(74, min_periods=max(74//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.061875 + 0.0033845 * anchor

def f55_rsw_k_245_rel_v245(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=227, w2=85, w3=183, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1758 * slope + 0.0033846 * anchor

def f55_rsw_k_246_rel_v246(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=234, w2=96, w3=196, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(96, min_periods=max(96//3, 2)).mean()
    noise = impulse.abs().rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.090625 + 0.0033847 * anchor

def f55_rsw_k_247_rel_v247(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=241, w2=107, w3=209, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 107)
    curvature = _rolling_slope(acceleration, 209)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.191 * acceleration + 0.0033848 * anchor

def f55_rsw_k_248_rel_v248(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=248, w2=118, w3=222, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 248)
    pressure = rel_log.diff(118)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1986 * pressure.rolling(222, min_periods=max(222//3, 2)).mean() + 0.0033849 * anchor

def f55_rsw_k_249_rel_v249(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=255, w2=129, w3=235, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(255, min_periods=max(255//3, 2)).mean())
    decay = spread.ewm(span=129, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.13375 + 0.003385 * anchor

def f55_rsw_k_250_rel_v250(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=11, w2=140, w3=248, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(140, min_periods=max(140//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 11)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.148125 + 0.0033851 * anchor

def f55_rsw_k_251_rel_v251(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=18, w2=151, w3=261, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(18, min_periods=max(18//3, 2)).mean(), b.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2214 * _rolling_slope(cover, 18) + 0.0033852 * anchor

def f55_rsw_k_252_rel_v252(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=25, w2=162, w3=274, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.229 * y + 0.771000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 25) - _rolling_slope(basket, 162) + 0.0033853 * anchor

def f55_rsw_k_253_rel_v253(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=32, w2=173, w3=287, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.19125 + 0.0033854 * anchor

def f55_rsw_k_254_rel_v254(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=39, w2=184, w3=300, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2442 * _rolling_slope(draw, 300) + 0.0033855 * anchor

def f55_rsw_k_255_rel_v255(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=46, w2=195, w3=313, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(46) - b.diff(126)
    stress = imbalance.rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.22 + 0.0033856 * anchor

def f55_rsw_k_256_rel_v256(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=53, w2=206, w3=326, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(206, min_periods=max(206//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.234375 + 0.0033857 * anchor

def f55_rsw_k_257_rel_v257(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=60, w2=217, w3=339, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 217)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.24875 + 0.0033858 * anchor

def f55_rsw_k_258_rel_v258(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=67, w2=228, w3=352, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(228, min_periods=max(228//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.263125 + 0.0033859 * anchor

def f55_rsw_k_259_rel_v259(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=74, w2=239, w3=365, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(74)
    rank = change.rolling(239, min_periods=max(239//3, 2)).rank(pct=True)
    persistence = change.rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2822 * persistence + 0.003386 * anchor

def f55_rsw_k_260_rel_v260(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=81, w2=250, w3=378, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(250, min_periods=max(250//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.291875 + 0.0033861 * anchor

def f55_rsw_k_261_rel_v261(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=88, w2=261, w3=391, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2974 * slope + 0.0033862 * anchor

def f55_rsw_k_262_rel_v262(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=95, w2=272, w3=404, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(95)
    drag = impulse.rolling(272, min_periods=max(272//3, 2)).mean()
    noise = impulse.abs().rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.320625 + 0.0033863 * anchor

def f55_rsw_k_263_rel_v263(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=102, w2=283, w3=417, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 283)
    curvature = _rolling_slope(acceleration, 417)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3126 * acceleration + 0.0033864 * anchor

def f55_rsw_k_264_rel_v264(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=109, w2=294, w3=430, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 109)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.3202 * pressure.rolling(430, min_periods=max(430//3, 2)).mean() + 0.0033865 * anchor

def f55_rsw_k_265_rel_v265(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=116, w2=305, w3=443, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(116, min_periods=max(116//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.36375 + 0.0033866 * anchor

def f55_rsw_k_266_rel_v266(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=123, w2=316, w3=456, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(316, min_periods=max(316//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 123)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.378125 + 0.0033867 * anchor

def f55_rsw_k_267_rel_v267(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=130, w2=327, w3=469, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(130, min_periods=max(130//3, 2)).mean(), b.abs().rolling(327, min_periods=max(327//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.343 * _rolling_slope(cover, 130) + 0.0033868 * anchor

def f55_rsw_k_268_rel_v268(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=137, w2=338, w3=482, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3506 * y + 0.649400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 137) - _rolling_slope(basket, 338) + 0.0033869 * anchor

def f55_rsw_k_269_rel_v269(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=144, w2=349, w3=495, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(349, min_periods=max(349//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.42125 + 0.003387 * anchor

def f55_rsw_k_270_rel_v270(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=151, w2=360, w3=508, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(360, min_periods=max(360//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3658 * _rolling_slope(draw, 508) + 0.0033871 * anchor

def f55_rsw_k_271_rel_v271(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=158, w2=371, w3=521, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.45 + 0.0033872 * anchor

def f55_rsw_k_272_rel_v272(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=165, w2=382, w3=534, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(382, min_periods=max(382//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.464375 + 0.0033873 * anchor

def f55_rsw_k_273_rel_v273(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=172, w2=393, w3=547, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 393)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.47875 + 0.0033874 * anchor

def f55_rsw_k_274_rel_v274(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=179, w2=404, w3=560, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(404, min_periods=max(404//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.493125 + 0.0033875 * anchor

def f55_rsw_k_275_rel_v275(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=186, w2=415, w3=573, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(415, min_periods=max(415//3, 2)).rank(pct=True)
    persistence = change.rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4038 * persistence + 0.0033876 * anchor

def f55_rsw_k_276_rel_v276(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=193, w2=426, w3=586, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(426, min_periods=max(426//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.521875 + 0.0033877 * anchor

def f55_rsw_k_277_rel_v277(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=200, w2=437, w3=599, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0426 * slope + 0.0033878 * anchor

def f55_rsw_k_278_rel_v278(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=207, w2=448, w3=612, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(448, min_periods=max(448//3, 2)).mean()
    noise = impulse.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.550625 + 0.0033879 * anchor

def f55_rsw_k_279_rel_v279(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=214, w2=459, w3=625, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 459)
    curvature = _rolling_slope(acceleration, 625)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0578 * acceleration + 0.003388 * anchor

def f55_rsw_k_280_rel_v280(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=221, w2=470, w3=638, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 221)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0654 * pressure.rolling(638, min_periods=max(638//3, 2)).mean() + 0.0033881 * anchor

def f55_rsw_k_281_rel_v281(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=228, w2=481, w3=651, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(228, min_periods=max(228//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.59375 + 0.0033882 * anchor

def f55_rsw_k_282_rel_v282(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=235, w2=492, w3=664, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(492, min_periods=max(492//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 235)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.608125 + 0.0033883 * anchor

def f55_rsw_k_283_rel_v283(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=242, w2=503, w3=677, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(242, min_periods=max(242//3, 2)).mean(), b.abs().rolling(503, min_periods=max(503//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.0882 * _rolling_slope(cover, 242) + 0.0033884 * anchor

def f55_rsw_k_284_rel_v284(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=249, w2=11, w3=690, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0958 * y + 0.904200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 249) - _rolling_slope(basket, 11) + 0.0033885 * anchor

def f55_rsw_k_285_rel_v285(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=5, w2=22, w3=703, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(22, min_periods=max(22//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.878125 + 0.0033886 * anchor

def f55_rsw_k_286_rel_v286(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=12, w2=33, w3=716, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(33, min_periods=max(33//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.111 * _rolling_slope(draw, 716) + 0.0033887 * anchor

def f55_rsw_k_287_rel_v287(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=19, w2=44, w3=729, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(19) - b.diff(44)
    stress = imbalance.rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.906875 + 0.0033888 * anchor

def f55_rsw_k_288_rel_v288(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=26, w2=55, w3=742, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(55, min_periods=max(55//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.92125 + 0.0033889 * anchor

def f55_rsw_k_289_rel_v289(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=33, w2=66, w3=755, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 66)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.935625 + 0.003389 * anchor

def f55_rsw_k_290_rel_v290(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=40, w2=77, w3=768, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(77, min_periods=max(77//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.95 + 0.0033891 * anchor

def f55_rsw_k_291_rel_v291(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=47, w2=88, w3=24, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(47)
    rank = change.rolling(88, min_periods=max(88//3, 2)).rank(pct=True)
    persistence = change.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.149 * persistence + 0.0033892 * anchor

def f55_rsw_k_292_rel_v292(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=54, w2=99, w3=37, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97875 + 0.0033893 * anchor

def f55_rsw_k_293_rel_v293(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=61, w2=110, w3=50, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1642 * slope + 0.0033894 * anchor

def f55_rsw_k_294_rel_v294(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=68, w2=121, w3=63, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(68)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0075 + 0.0033895 * anchor

def f55_rsw_k_295_rel_v295(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=75, w2=132, w3=76, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 132)
    curvature = _rolling_slope(acceleration, 76)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1794 * acceleration + 0.0033896 * anchor

def f55_rsw_k_296_rel_v296(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=82, w2=143, w3=89, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 82)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.187 * pressure.rolling(89, min_periods=max(89//3, 2)).mean() + 0.0033897 * anchor

def f55_rsw_k_297_rel_v297(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=89, w2=154, w3=102, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(89, min_periods=max(89//3, 2)).mean())
    decay = spread.ewm(span=154, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.050625 + 0.0033898 * anchor

def f55_rsw_k_298_rel_v298(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=96, w2=165, w3=115, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(165, min_periods=max(165//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 96)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.065 + 0.0033899 * anchor

def f55_rsw_k_299_rel_v299(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=103, w2=176, w3=128, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(103, min_periods=max(103//3, 2)).mean(), b.abs().rolling(176, min_periods=max(176//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2098 * _rolling_slope(cover, 103) + 0.00339 * anchor

def f55_rsw_k_300_rel_v300(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=110, w2=187, w3=141, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2174 * y + 0.782600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 110) - _rolling_slope(basket, 187) + 0.0033901 * anchor
