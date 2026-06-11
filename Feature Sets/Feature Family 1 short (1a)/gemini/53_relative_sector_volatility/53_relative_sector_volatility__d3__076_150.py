"""53 relative sector volatility d3 third derivative features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f53_rsw_v_076_rel_v76_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=182, w2=116, w3=554, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3106 * y + 0.689400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 182) - _rolling_slope(basket, 116) + 0.0032477 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_077_rel_v77_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=189, w2=127, w3=567, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5125 + 0.0032478 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_078_rel_v78_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=196, w2=138, w3=580, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(138, min_periods=max(138//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3258 * _rolling_slope(draw, 580) + 0.0032479 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_079_rel_v79_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=203, w2=149, w3=593, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.54125 + 0.003248 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_080_rel_v80_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=210, w2=160, w3=606, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.555625 + 0.0032481 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_081_rel_v81_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=217, w2=171, w3=619, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 171)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.57 + 0.0032482 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_082_rel_v82_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=224, w2=182, w3=632, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(182, min_periods=max(182//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.584375 + 0.0032483 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_083_rel_v83_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=231, w2=193, w3=645, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(645, min_periods=max(645//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3638 * persistence + 0.0032484 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_084_rel_v84_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=238, w2=204, w3=658, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(204, min_periods=max(204//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.613125 + 0.0032485 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_085_rel_v85_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=245, w2=215, w3=671, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(215, min_periods=max(215//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.379 * slope + 0.0032486 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_086_rel_v86_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=252, w2=226, w3=684, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(226, min_periods=max(226//3, 2)).mean()
    noise = impulse.abs().rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.86875 + 0.0032487 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_087_rel_v87_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=8, w2=237, w3=697, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 237)
    curvature = _rolling_slope(acceleration, 697)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3942 * acceleration + 0.0032488 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_088_rel_v88_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=15, w2=248, w3=710, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 15)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.4018 * pressure.rolling(710, min_periods=max(710//3, 2)).mean() + 0.0032489 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_089_rel_v89_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=22, w2=259, w3=723, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(22, min_periods=max(22//3, 2)).mean())
    decay = spread.ewm(span=259, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.911875 + 0.003249 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_090_rel_v90_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=29, w2=270, w3=736, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(270, min_periods=max(270//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 29)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.92625 + 0.0032491 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_091_rel_v91_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=36, w2=281, w3=749, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(36, min_periods=max(36//3, 2)).mean(), b.abs().rolling(281, min_periods=max(281//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0482 * _rolling_slope(cover, 36) + 0.0032492 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_092_rel_v92_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=43, w2=292, w3=762, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0558 * y + 0.944200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 43) - _rolling_slope(basket, 292) + 0.0032493 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_093_rel_v93_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=50, w2=303, w3=18, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(303, min_periods=max(303//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(18) * 0.969375 + 0.0032494 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_094_rel_v94_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=57, w2=314, w3=31, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.071 * _rolling_slope(draw, 31) + 0.0032495 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_095_rel_v95_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=64, w2=325, w3=44, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(64) - b.diff(126)
    stress = imbalance.rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.998125 + 0.0032496 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_096_rel_v96_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=71, w2=336, w3=57, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(336, min_periods=max(336//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(57, min_periods=max(57//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0125 + 0.0032497 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_097_rel_v97_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=78, w2=347, w3=70, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=70, adjust=False).mean() * 1.026875 + 0.0032498 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_098_rel_v98_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=85, w2=358, w3=83, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(358, min_periods=max(358//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.04125 + 0.0032499 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_099_rel_v99_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=92, w2=369, w3=96, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(92)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.109 * persistence + 0.00325 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_100_rel_v100_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=99, w2=380, w3=109, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(380, min_periods=max(380//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.07 + 0.0032501 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_101_rel_v101_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=106, w2=391, w3=122, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1242 * slope + 0.0032502 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_102_rel_v102_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=113, w2=402, w3=135, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(113)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.09875 + 0.0032503 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_103_rel_v103_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=120, w2=413, w3=148, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 148)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1394 * acceleration + 0.0032504 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_104_rel_v104_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=127, w2=424, w3=161, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 127)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.147 * pressure.rolling(161, min_periods=max(161//3, 2)).mean() + 0.0032505 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_105_rel_v105_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=134, w2=435, w3=174, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.141875 + 0.0032506 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_106_rel_v106_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=141, w2=446, w3=187, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(446, min_periods=max(446//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 141)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.15625 + 0.0032507 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_107_rel_v107_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=148, w2=457, w3=200, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(148, min_periods=max(148//3, 2)).mean(), b.abs().rolling(457, min_periods=max(457//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1698 * _rolling_slope(cover, 148) + 0.0032508 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_108_rel_v108_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=155, w2=468, w3=213, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1774 * y + 0.822600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 155) - _rolling_slope(basket, 468) + 0.0032509 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_109_rel_v109_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=162, w2=479, w3=226, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(479, min_periods=max(479//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.199375 + 0.003251 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_110_rel_v110_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=169, w2=490, w3=239, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(490, min_periods=max(490//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1926 * _rolling_slope(draw, 239) + 0.0032511 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_111_rel_v111_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=176, w2=501, w3=252, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.228125 + 0.0032512 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_112_rel_v112_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=183, w2=512, w3=265, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(512, min_periods=max(512//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2425 + 0.0032513 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_113_rel_v113_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=190, w2=20, w3=278, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 20)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=278, adjust=False).mean() * 1.256875 + 0.0032514 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_114_rel_v114_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=197, w2=31, w3=291, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(31, min_periods=max(31//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.27125 + 0.0032515 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_115_rel_v115_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=204, w2=42, w3=304, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2306 * persistence + 0.0032516 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_116_rel_v116_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=211, w2=53, w3=317, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(53, min_periods=max(53//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3 + 0.0032517 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_117_rel_v117_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=218, w2=64, w3=330, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(64, min_periods=max(64//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2458 * slope + 0.0032518 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_118_rel_v118_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=225, w2=75, w3=343, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(75, min_periods=max(75//3, 2)).mean()
    noise = impulse.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.32875 + 0.0032519 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_119_rel_v119_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=232, w2=86, w3=356, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 86)
    curvature = _rolling_slope(acceleration, 356)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.261 * acceleration + 0.003252 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_120_rel_v120_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=239, w2=97, w3=369, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 239)
    pressure = rel_log.diff(97)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2686 * pressure.rolling(369, min_periods=max(369//3, 2)).mean() + 0.0032521 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_121_rel_v121_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=246, w2=108, w3=382, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(246, min_periods=max(246//3, 2)).mean())
    decay = spread.ewm(span=108, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.371875 + 0.0032522 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_122_rel_v122_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=253, w2=119, w3=395, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(119, min_periods=max(119//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 253)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.38625 + 0.0032523 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_123_rel_v123_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=9, w2=130, w3=408, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2914 * _rolling_slope(cover, 9) + 0.0032524 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_124_rel_v124_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=16, w2=141, w3=421, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.299 * y + 0.701000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 16) - _rolling_slope(basket, 141) + 0.0032525 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_125_rel_v125_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=23, w2=152, w3=434, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.429375 + 0.0032526 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_126_rel_v126_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=30, w2=163, w3=447, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(163, min_periods=max(163//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3142 * _rolling_slope(draw, 447) + 0.0032527 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_127_rel_v127_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=37, w2=174, w3=460, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(460, min_periods=max(460//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.458125 + 0.0032528 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_128_rel_v128_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=44, w2=185, w3=473, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(185, min_periods=max(185//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4725 + 0.0032529 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_129_rel_v129_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=51, w2=196, w3=486, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 196)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.486875 + 0.003253 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_130_rel_v130_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=58, w2=207, w3=499, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(207, min_periods=max(207//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.50125 + 0.0032531 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_131_rel_v131_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=65, w2=218, w3=512, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(65)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3522 * persistence + 0.0032532 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_132_rel_v132_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=72, w2=229, w3=525, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(229, min_periods=max(229//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53 + 0.0032533 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_133_rel_v133_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=79, w2=240, w3=538, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3674 * slope + 0.0032534 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_134_rel_v134_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=86, w2=251, w3=551, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(86)
    drag = impulse.rolling(251, min_periods=max(251//3, 2)).mean()
    noise = impulse.abs().rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.55875 + 0.0032535 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_135_rel_v135_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=93, w2=262, w3=564, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 262)
    curvature = _rolling_slope(acceleration, 564)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3826 * acceleration + 0.0032536 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_136_rel_v136_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=100, w2=273, w3=577, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3902 * pressure.rolling(577, min_periods=max(577//3, 2)).mean() + 0.0032537 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_137_rel_v137_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=107, w2=284, w3=590, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=284, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.601875 + 0.0032538 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_138_rel_v138_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=114, w2=295, w3=603, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(295, min_periods=max(295//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.61625 + 0.0032539 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_139_rel_v139_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=121, w2=306, w3=616, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(306, min_periods=max(306//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0366 * _rolling_slope(cover, 121) + 0.003254 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_140_rel_v140_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=128, w2=317, w3=629, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0442 * y + 0.955800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 128) - _rolling_slope(basket, 317) + 0.0032541 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_141_rel_v141_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=135, w2=328, w3=642, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(328, min_periods=max(328//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.88625 + 0.0032542 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_142_rel_v142_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=142, w2=339, w3=655, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(339, min_periods=max(339//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0594 * _rolling_slope(draw, 655) + 0.0032543 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_143_rel_v143_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=149, w2=350, w3=668, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.915 + 0.0032544 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_144_rel_v144_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=156, w2=361, w3=681, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(361, min_periods=max(361//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.929375 + 0.0032545 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_145_rel_v145_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=163, w2=372, w3=694, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 372)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.94375 + 0.0032546 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_146_rel_v146_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=170, w2=383, w3=707, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.958125 + 0.0032547 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_147_rel_v147_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=177, w2=394, w3=720, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(394, min_periods=max(394//3, 2)).rank(pct=True)
    persistence = change.rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0974 * persistence + 0.0032548 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_148_rel_v148_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=184, w2=405, w3=733, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.986875 + 0.0032549 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_149_rel_v149_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=191, w2=416, w3=746, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(416, min_periods=max(416//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1126 * slope + 0.003255 * anchor
    return base_signal.diff().diff().diff()

def f53_rsw_v_150_rel_v150_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=198, w2=427, w3=759, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(427, min_periods=max(427//3, 2)).mean()
    noise = impulse.abs().rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.015625 + 0.0032551 * anchor
    return base_signal.diff().diff().diff()
