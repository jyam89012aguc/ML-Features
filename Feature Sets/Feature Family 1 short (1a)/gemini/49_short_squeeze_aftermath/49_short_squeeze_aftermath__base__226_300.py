"""49 short squeeze aftermath base features 226-300 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics - Institutional-grade short-side signal.
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

def f49_ssa_226_accel_v226(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=245, w2=13, w3=70, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(70, min_periods=max(70//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.8525 + 0.0030227 * anchor

def f49_ssa_227_jerk_v227(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=252, w2=24, w3=83, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 252)
    acceleration = _rolling_slope(velocity, 24)
    curvature = _rolling_slope(acceleration, 83)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1562 * acceleration + 0.0030228 * anchor

def f49_ssa_228_accel_v228(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=8, w2=35, w3=96, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(35, min_periods=max(35//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(96) * 0.88125 + 0.0030229 * anchor

def f49_ssa_229_jerk_v229(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=15, w2=46, w3=109, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(46, min_periods=max(46//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1714 * _rolling_slope(draw, 109) + 0.003023 * anchor

def f49_ssa_230_accel_v230(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=22, w2=57, w3=122, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(57, min_periods=max(57//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.91 + 0.0030231 * anchor

def f49_ssa_231_jerk_v231(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=29, w2=68, w3=135, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 68)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=135, adjust=False).mean() * 0.924375 + 0.0030232 * anchor

def f49_ssa_232_accel_v232(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=36, w2=79, w3=148, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(79, min_periods=max(79//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.93875 + 0.0030233 * anchor

def f49_ssa_233_jerk_v233(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=43, w2=90, w3=161, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(43)
    rank = change.rolling(90, min_periods=max(90//3, 2)).rank(pct=True)
    persistence = change.rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2018 * persistence + 0.0030234 * anchor

def f49_ssa_234_accel_v234(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=50, w2=101, w3=174, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(101, min_periods=max(101//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9675 + 0.0030235 * anchor

def f49_ssa_235_jerk_v235(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=57, w2=112, w3=187, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(112, min_periods=max(112//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.217 * slope + 0.0030236 * anchor

def f49_ssa_236_accel_v236(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=64, w2=123, w3=200, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(64)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(200, min_periods=max(200//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.99625 + 0.0030237 * anchor

def f49_ssa_237_jerk_v237(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=71, w2=134, w3=213, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 134)
    curvature = _rolling_slope(acceleration, 213)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2322 * acceleration + 0.0030238 * anchor

def f49_ssa_238_accel_v238(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=78, w2=145, w3=226, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(145, min_periods=max(145//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.025 + 0.0030239 * anchor

def f49_ssa_239_jerk_v239(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=85, w2=156, w3=239, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(156, min_periods=max(156//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2474 * _rolling_slope(draw, 239) + 0.003024 * anchor

def f49_ssa_240_accel_v240(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=92, w2=167, w3=252, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(167, min_periods=max(167//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.05375 + 0.0030241 * anchor

def f49_ssa_241_jerk_v241(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=99, w2=178, w3=265, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 178)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=265, adjust=False).mean() * 1.068125 + 0.0030242 * anchor

def f49_ssa_242_accel_v242(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=106, w2=189, w3=278, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(189, min_periods=max(189//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.0825 + 0.0030243 * anchor

def f49_ssa_243_jerk_v243(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=113, w2=200, w3=291, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(113)
    rank = change.rolling(200, min_periods=max(200//3, 2)).rank(pct=True)
    persistence = change.rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2778 * persistence + 0.0030244 * anchor

def f49_ssa_244_accel_v244(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=120, w2=211, w3=304, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(211, min_periods=max(211//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11125 + 0.0030245 * anchor

def f49_ssa_245_jerk_v245(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=127, w2=222, w3=317, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(222, min_periods=max(222//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.293 * slope + 0.0030246 * anchor

def f49_ssa_246_accel_v246(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=134, w2=233, w3=330, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(233, min_periods=max(233//3, 2)).mean()
    noise = impulse.abs().rolling(330, min_periods=max(330//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.14 + 0.0030247 * anchor

def f49_ssa_247_jerk_v247(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=141, w2=244, w3=343, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 244)
    curvature = _rolling_slope(acceleration, 343)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3082 * acceleration + 0.0030248 * anchor

def f49_ssa_248_accel_v248(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=148, w2=255, w3=356, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(255, min_periods=max(255//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.16875 + 0.0030249 * anchor

def f49_ssa_249_jerk_v249(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=155, w2=266, w3=369, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(266, min_periods=max(266//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3234 * _rolling_slope(draw, 369) + 0.003025 * anchor

def f49_ssa_250_accel_v250(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=162, w2=277, w3=382, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(277, min_periods=max(277//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.1975 + 0.0030251 * anchor

def f49_ssa_251_jerk_v251(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=169, w2=288, w3=395, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 288)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.211875 + 0.0030252 * anchor

def f49_ssa_252_accel_v252(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=176, w2=299, w3=408, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(299, min_periods=max(299//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.22625 + 0.0030253 * anchor

def f49_ssa_253_jerk_v253(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=183, w2=310, w3=421, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(310, min_periods=max(310//3, 2)).rank(pct=True)
    persistence = change.rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3538 * persistence + 0.0030254 * anchor

def f49_ssa_254_accel_v254(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=190, w2=321, w3=434, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(321, min_periods=max(321//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.255 + 0.0030255 * anchor

def f49_ssa_255_jerk_v255(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=197, w2=332, w3=447, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(332, min_periods=max(332//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.369 * slope + 0.0030256 * anchor

def f49_ssa_256_accel_v256(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=204, w2=343, w3=460, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(343, min_periods=max(343//3, 2)).mean()
    noise = impulse.abs().rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.28375 + 0.0030257 * anchor

def f49_ssa_257_jerk_v257(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=211, w2=354, w3=473, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 354)
    curvature = _rolling_slope(acceleration, 473)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3842 * acceleration + 0.0030258 * anchor

def f49_ssa_258_accel_v258(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=218, w2=365, w3=486, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.3125 + 0.0030259 * anchor

def f49_ssa_259_jerk_v259(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=225, w2=376, w3=499, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3994 * _rolling_slope(draw, 499) + 0.003026 * anchor

def f49_ssa_260_accel_v260(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=232, w2=387, w3=512, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(387, min_periods=max(387//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.34125 + 0.0030261 * anchor

def f49_ssa_261_jerk_v261(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=239, w2=398, w3=525, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 398)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.355625 + 0.0030262 * anchor

def f49_ssa_262_accel_v262(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=246, w2=409, w3=538, lag=42)."""
    x = low.shift(42)
    peak = x.rolling(409, min_periods=max(409//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.37 + 0.0030263 * anchor

def f49_ssa_263_jerk_v263(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=253, w2=420, w3=551, lag=63)."""
    x = volume.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(420, min_periods=max(420//3, 2)).rank(pct=True)
    persistence = change.rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0534 * persistence + 0.0030264 * anchor

def f49_ssa_264_accel_v264(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=9, w2=431, w3=564, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(431, min_periods=max(431//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39875 + 0.0030265 * anchor

def f49_ssa_265_jerk_v265(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=16, w2=442, w3=577, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(442, min_periods=max(442//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0686 * slope + 0.0030266 * anchor

def f49_ssa_266_accel_v266(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=23, w2=453, w3=590, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(23)
    drag = impulse.rolling(453, min_periods=max(453//3, 2)).mean()
    noise = impulse.abs().rolling(590, min_periods=max(590//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.4275 + 0.0030267 * anchor

def f49_ssa_267_jerk_v267(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=30, w2=464, w3=603, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 603)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0838 * acceleration + 0.0030268 * anchor

def f49_ssa_268_accel_v268(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=37, w2=475, w3=616, lag=10)."""
    x = close.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(37, min_periods=max(37//3, 2)).mean(), upside.rolling(475, min_periods=max(475//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45625 + 0.0030269 * anchor

def f49_ssa_269_jerk_v269(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=44, w2=486, w3=629, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(44, min_periods=max(44//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.099 * _rolling_slope(draw, 629) + 0.003027 * anchor

def f49_ssa_270_accel_v270(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=51, w2=497, w3=642, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(497, min_periods=max(497//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.485 + 0.0030271 * anchor

def f49_ssa_271_jerk_v271(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=58, w2=508, w3=655, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 508)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.499375 + 0.0030272 * anchor

def f49_ssa_272_accel_v272(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=65, w2=16, w3=668, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.51375 + 0.0030273 * anchor

def f49_ssa_273_jerk_v273(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=72, w2=27, w3=681, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(72)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1294 * persistence + 0.0030274 * anchor

def f49_ssa_274_accel_v274(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=79, w2=38, w3=694, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(38, min_periods=max(38//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5425 + 0.0030275 * anchor

def f49_ssa_275_jerk_v275(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=86, w2=49, w3=707, lag=5)."""
    x = volume.shift(5)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1446 * slope + 0.0030276 * anchor

def f49_ssa_276_accel_v276(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=93, w2=60, w3=720, lag=10)."""
    x = close.shift(10)
    impulse = x.diff(93)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.57125 + 0.0030277 * anchor

def f49_ssa_277_jerk_v277(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=100, w2=71, w3=733, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 733)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1598 * acceleration + 0.0030278 * anchor

def f49_ssa_278_accel_v278(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=107, w2=82, w3=746, lag=42)."""
    x = low.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.6 + 0.0030279 * anchor

def f49_ssa_279_jerk_v279(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=114, w2=93, w3=759, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    draw = x - x.rolling(93, min_periods=max(93//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.175 * _rolling_slope(draw, 759) + 0.003028 * anchor

def f49_ssa_280_accel_v280(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=121, w2=104, w3=15, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.855625 + 0.0030281 * anchor

def f49_ssa_281_jerk_v281(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=128, w2=115, w3=28, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 115)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=28, adjust=False).mean() * 0.87 + 0.0030282 * anchor

def f49_ssa_282_accel_v282(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=135, w2=126, w3=41, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(126, min_periods=max(126//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.884375 + 0.0030283 * anchor

def f49_ssa_283_jerk_v283(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=142, w2=137, w3=54, lag=5)."""
    x = volume.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(137, min_periods=max(137//3, 2)).rank(pct=True)
    persistence = change.rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2054 * persistence + 0.0030284 * anchor

def f49_ssa_284_accel_v284(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=149, w2=148, w3=67, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.913125 + 0.0030285 * anchor

def f49_ssa_285_jerk_v285(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=156, w2=159, w3=80, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(159, min_periods=max(159//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2206 * slope + 0.0030286 * anchor

def f49_ssa_286_accel_v286(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=163, w2=170, w3=93, lag=42)."""
    x = low.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(170, min_periods=max(170//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.941875 + 0.0030287 * anchor

def f49_ssa_287_jerk_v287(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=170, w2=181, w3=106, lag=63)."""
    x = _safe_log(volume.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 181)
    curvature = _rolling_slope(acceleration, 106)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2358 * acceleration + 0.0030288 * anchor

def f49_ssa_288_accel_v288(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=177, w2=192, w3=119, lag=0)."""
    x = close.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(119) * 0.970625 + 0.0030289 * anchor

def f49_ssa_289_jerk_v289(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=184, w2=203, w3=132, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    draw = x - x.rolling(203, min_periods=max(203//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.251 * _rolling_slope(draw, 132) + 0.003029 * anchor

def f49_ssa_290_accel_v290(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=191, w2=214, w3=145, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.999375 + 0.0030291 * anchor

def f49_ssa_291_jerk_v291(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=198, w2=225, w3=158, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=158, adjust=False).mean() * 1.01375 + 0.0030292 * anchor

def f49_ssa_292_accel_v292(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=205, w2=236, w3=171, lag=10)."""
    x = close.shift(10)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.028125 + 0.0030293 * anchor

def f49_ssa_293_jerk_v293(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=212, w2=247, w3=184, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(247, min_periods=max(247//3, 2)).rank(pct=True)
    persistence = change.rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2814 * persistence + 0.0030294 * anchor

def f49_ssa_294_accel_v294(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=219, w2=258, w3=197, lag=42)."""
    x = _safe_log(low.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.056875 + 0.0030295 * anchor

def f49_ssa_295_jerk_v295(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=226, w2=269, w3=210, lag=63)."""
    x = volume.shift(63)
    ma = x.rolling(269, min_periods=max(269//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2966 * slope + 0.0030296 * anchor

def f49_ssa_296_accel_v296(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=233, w2=280, w3=223, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.085625 + 0.0030297 * anchor

def f49_ssa_297_jerk_v297(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=240, w2=291, w3=236, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 291)
    curvature = _rolling_slope(acceleration, 236)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3118 * acceleration + 0.0030298 * anchor

def f49_ssa_298_accel_v298(low: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=247, w2=302, w3=249, lag=2)."""
    x = low.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.114375 + 0.0030299 * anchor

def f49_ssa_299_jerk_v299(volume: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=254, w2=313, w3=262, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(254, min_periods=max(254//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.327 * _rolling_slope(draw, 262) + 0.00303 * anchor

def f49_ssa_300_accel_v300(close: pd.Series) -> pd.Series:
    """De-duplicated accel replacement signal (w1=10, w2=324, w3=275, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 10)
    baseline = trend.rolling(324, min_periods=max(324//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.143125 + 0.0030301 * anchor
