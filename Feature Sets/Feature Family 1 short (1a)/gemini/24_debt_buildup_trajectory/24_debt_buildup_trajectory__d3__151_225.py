"""24 debt buildup trajectory d3 third derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Trajectory - Institutional-grade short-side signal.
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

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)
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

def f24_dbt_151_struct_v151_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=207, w2=117, w3=685, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.276875 + 0.0014552 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_152_struct_v152_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=214, w2=128, w3=698, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.29125 + 0.0014553 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_153_struct_v153_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=221, w2=139, w3=711, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(139, min_periods=max(139//3, 2)).rank(pct=True)
    persistence = change.rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3526 * persistence + 0.0014554 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_154_struct_v154_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=228, w2=150, w3=724, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(150, min_periods=max(150//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32 + 0.0014555 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_155_struct_v155_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=235, w2=161, w3=737, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3678 * slope + 0.0014556 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_156_struct_v156_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=242, w2=172, w3=750, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(172, min_periods=max(172//3, 2)).mean()
    noise = impulse.abs().rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.34875 + 0.0014557 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_157_struct_v157_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=249, w2=183, w3=763, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 183)
    curvature = _rolling_slope(acceleration, 763)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.383 * acceleration + 0.0014558 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_158_struct_v158_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=5, w2=194, w3=19, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(194, min_periods=max(194//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(19) * 1.3775 + 0.0014559 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_159_struct_v159_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=12, w2=205, w3=32, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(205, min_periods=max(205//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3982 * _rolling_slope(draw, 32) + 0.001456 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_160_struct_v160_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=19, w2=216, w3=45, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(216, min_periods=max(216//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.40625 + 0.0014561 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_161_struct_v161_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=26, w2=227, w3=58, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 227)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=58, adjust=False).mean() * 1.420625 + 0.0014562 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_162_struct_v162_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=33, w2=238, w3=71, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(238, min_periods=max(238//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.435 + 0.0014563 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_163_struct_v163_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=40, w2=249, w3=84, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(40)
    rank = change.rolling(249, min_periods=max(249//3, 2)).rank(pct=True)
    persistence = change.rolling(84, min_periods=max(84//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0522 * persistence + 0.0014564 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_164_struct_v164_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=47, w2=260, w3=97, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(260, min_periods=max(260//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46375 + 0.0014565 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_165_struct_v165_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=54, w2=271, w3=110, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(271, min_periods=max(271//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0674 * slope + 0.0014566 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_166_struct_v166_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=61, w2=282, w3=123, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(61)
    drag = impulse.rolling(282, min_periods=max(282//3, 2)).mean()
    noise = impulse.abs().rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4925 + 0.0014567 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_167_struct_v167_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=68, w2=293, w3=136, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 293)
    curvature = _rolling_slope(acceleration, 136)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0826 * acceleration + 0.0014568 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_168_struct_v168_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=75, w2=304, w3=149, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.52125 + 0.0014569 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_169_struct_v169_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=82, w2=315, w3=162, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(315, min_periods=max(315//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0978 * _rolling_slope(draw, 162) + 0.001457 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_170_struct_v170_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=89, w2=326, w3=175, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(326, min_periods=max(326//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55 + 0.0014571 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_171_struct_v171_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=96, w2=337, w3=188, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 337)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=188, adjust=False).mean() * 1.564375 + 0.0014572 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_172_struct_v172_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=103, w2=348, w3=201, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(348, min_periods=max(348//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.57875 + 0.0014573 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_173_struct_v173_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=110, w2=359, w3=214, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(110)
    rank = change.rolling(359, min_periods=max(359//3, 2)).rank(pct=True)
    persistence = change.rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1282 * persistence + 0.0014574 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_174_struct_v174_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=117, w2=370, w3=227, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(370, min_periods=max(370//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6075 + 0.0014575 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_175_struct_v175_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=124, w2=381, w3=240, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(381, min_periods=max(381//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1434 * slope + 0.0014576 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_176_struct_v176_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=131, w2=392, w3=253, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(392, min_periods=max(392//3, 2)).mean()
    noise = impulse.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.863125 + 0.0014577 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_177_struct_v177_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=138, w2=403, w3=266, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 403)
    curvature = _rolling_slope(acceleration, 266)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1586 * acceleration + 0.0014578 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_178_struct_v178_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=145, w2=414, w3=279, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(414, min_periods=max(414//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.891875 + 0.0014579 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_179_struct_v179_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=152, w2=425, w3=292, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(425, min_periods=max(425//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1738 * _rolling_slope(draw, 292) + 0.001458 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_180_struct_v180_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=159, w2=436, w3=305, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.920625 + 0.0014581 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_181_struct_v181_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=447, w3=318, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 447)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.935 + 0.0014582 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_182_struct_v182_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=458, w3=331, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(458, min_periods=max(458//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.949375 + 0.0014583 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_183_struct_v183_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=469, w3=344, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(469, min_periods=max(469//3, 2)).rank(pct=True)
    persistence = change.rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2042 * persistence + 0.0014584 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_184_struct_v184_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=480, w3=357, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.978125 + 0.0014585 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_185_struct_v185_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=491, w3=370, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(491, min_periods=max(491//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2194 * slope + 0.0014586 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_186_struct_v186_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=502, w3=383, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(502, min_periods=max(502//3, 2)).mean()
    noise = impulse.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.006875 + 0.0014587 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_187_struct_v187_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=10, w3=396, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 10)
    curvature = _rolling_slope(acceleration, 396)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2346 * acceleration + 0.0014588 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_188_struct_v188_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=21, w3=409, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(21, min_periods=max(21//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.035625 + 0.0014589 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_189_struct_v189_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=32, w3=422, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2498 * _rolling_slope(draw, 422) + 0.001459 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_190_struct_v190_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=43, w3=435, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(43, min_periods=max(43//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.064375 + 0.0014591 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_191_struct_v191_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=54, w3=448, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 54)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.07875 + 0.0014592 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_192_struct_v192_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=65, w3=461, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(65, min_periods=max(65//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.093125 + 0.0014593 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_193_struct_v193_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=76, w3=474, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(76, min_periods=max(76//3, 2)).rank(pct=True)
    persistence = change.rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2802 * persistence + 0.0014594 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_194_struct_v194_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=87, w3=487, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(87, min_periods=max(87//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.121875 + 0.0014595 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_195_struct_v195_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=98, w3=500, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(98, min_periods=max(98//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2954 * slope + 0.0014596 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_196_struct_v196_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=109, w3=513, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(20)
    drag = impulse.rolling(109, min_periods=max(109//3, 2)).mean()
    noise = impulse.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.150625 + 0.0014597 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_197_struct_v197_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=120, w3=526, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 120)
    curvature = _rolling_slope(acceleration, 526)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3106 * acceleration + 0.0014598 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_198_struct_v198_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=131, w3=539, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(131, min_periods=max(131//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.179375 + 0.0014599 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_199_struct_v199_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=142, w3=552, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(142, min_periods=max(142//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3258 * _rolling_slope(draw, 552) + 0.00146 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_200_struct_v200_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=153, w3=565, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(153, min_periods=max(153//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.208125 + 0.0014601 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_201_struct_v201_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=164, w3=578, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 164)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2225 + 0.0014602 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_202_struct_v202_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=175, w3=591, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(175, min_periods=max(175//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.236875 + 0.0014603 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_203_struct_v203_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=186, w3=604, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(69)
    rank = change.rolling(186, min_periods=max(186//3, 2)).rank(pct=True)
    persistence = change.rolling(604, min_periods=max(604//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3562 * persistence + 0.0014604 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_204_struct_v204_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=197, w3=617, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(197, min_periods=max(197//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.265625 + 0.0014605 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_205_struct_v205_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=208, w3=630, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(208, min_periods=max(208//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3714 * slope + 0.0014606 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_206_struct_v206_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=219, w3=643, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(90)
    drag = impulse.rolling(219, min_periods=max(219//3, 2)).mean()
    noise = impulse.abs().rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.294375 + 0.0014607 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_207_struct_v207_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=230, w3=656, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 230)
    curvature = _rolling_slope(acceleration, 656)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3866 * acceleration + 0.0014608 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_208_struct_v208_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=241, w3=669, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(104, min_periods=max(104//3, 2)).mean(), upside.rolling(241, min_periods=max(241//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.323125 + 0.0014609 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_209_struct_v209_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=252, w3=682, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(252, min_periods=max(252//3, 2)).max()
    rebound = x - x.rolling(111, min_periods=max(111//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4018 * _rolling_slope(draw, 682) + 0.001461 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_210_struct_v210_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=263, w3=695, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(263, min_periods=max(263//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.351875 + 0.0014611 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_211_struct_v211_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=274, w3=708, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 125)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.36625 + 0.0014612 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_212_struct_v212_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=285, w3=721, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(132, min_periods=max(132//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.380625 + 0.0014613 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_213_struct_v213_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=296, w3=734, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(296, min_periods=max(296//3, 2)).rank(pct=True)
    persistence = change.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0558 * persistence + 0.0014614 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_214_struct_v214_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=307, w3=747, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(146, min_periods=max(146//3, 2)).std()
    vol_slow = ret.rolling(307, min_periods=max(307//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.409375 + 0.0014615 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_215_struct_v215_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=318, w3=760, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(318, min_periods=max(318//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 153)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.071 * slope + 0.0014616 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_216_struct_v216_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=329, w3=16, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(329, min_periods=max(329//3, 2)).mean()
    noise = impulse.abs().rolling(16, min_periods=max(16//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.438125 + 0.0014617 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_217_struct_v217_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=340, w3=29, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 167)
    acceleration = _rolling_slope(velocity, 340)
    curvature = _rolling_slope(acceleration, 29)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0862 * acceleration + 0.0014618 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_218_struct_v218_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=351, w3=42, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(174, min_periods=max(174//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(42) * 1.466875 + 0.0014619 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_219_struct_v219_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=362, w3=55, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(362, min_periods=max(362//3, 2)).max()
    rebound = x - x.rolling(181, min_periods=max(181//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1014 * _rolling_slope(draw, 55) + 0.001462 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_220_struct_v220_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=373, w3=68, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 188)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.495625 + 0.0014621 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_221_struct_v221_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=384, w3=81, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 195)
    slow = _rolling_slope(x, 384)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=81, adjust=False).mean() * 1.51 + 0.0014622 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_222_struct_v222_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=395, w3=94, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(395, min_periods=max(395//3, 2)).max()
    trough = x.rolling(202, min_periods=max(202//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.524375 + 0.0014623 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_223_struct_v223_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=406, w3=107, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(406, min_periods=max(406//3, 2)).rank(pct=True)
    persistence = change.rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1318 * persistence + 0.0014624 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_224_struct_v224_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=417, w3=120, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(216, min_periods=max(216//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.553125 + 0.0014625 * anchor
    return base_signal.diff().diff().diff()

def f24_dbt_225_struct_v225_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=428, w3=133, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 223)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147 * slope + 0.0014626 * anchor
    return base_signal.diff().diff().diff()
