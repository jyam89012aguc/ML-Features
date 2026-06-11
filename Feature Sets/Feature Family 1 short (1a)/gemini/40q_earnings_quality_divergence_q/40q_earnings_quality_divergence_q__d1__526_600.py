"""40q earnings quality divergence q d1 first derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Accounting_Fraud - Institutional-grade short-side signal.
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

def f40q_eqdq_526_accrual_v526_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=187, w2=249, w3=386, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(249, min_periods=max(249//3, 2)).mean()
    noise = impulse.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.986875 + 0.0025127 * anchor
    return base_signal.diff()

def f40q_eqdq_527_accrual_v527_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=194, w2=260, w3=399, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 260)
    curvature = _rolling_slope(acceleration, 399)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1654 * acceleration + 0.0025128 * anchor
    return base_signal.diff()

def f40q_eqdq_528_accrual_v528_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=201, w2=271, w3=412, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 201)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.173 * pressure.rolling(412, min_periods=max(412//3, 2)).mean() + 0.0025129 * anchor
    return base_signal.diff()

def f40q_eqdq_529_accrual_v529_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=208, w2=282, w3=425, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(208, min_periods=max(208//3, 2)).mean())
    decay = spread.ewm(span=282, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.03 + 0.002513 * anchor
    return base_signal.diff()

def f40q_eqdq_530_accrual_v530_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=215, w2=293, w3=438, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(293, min_periods=max(293//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 215)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.044375 + 0.0025131 * anchor
    return base_signal.diff()

def f40q_eqdq_531_accrual_v531_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=222, w2=304, w3=451, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(222, min_periods=max(222//3, 2)).mean(), b.abs().rolling(304, min_periods=max(304//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1958 * _rolling_slope(cover, 222) + 0.0025132 * anchor
    return base_signal.diff()

def f40q_eqdq_532_accrual_v532_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=229, w2=315, w3=464, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2034 * y + 0.796600 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 229) - _rolling_slope(basket, 315) + 0.0025133 * anchor
    return base_signal.diff()

def f40q_eqdq_533_accrual_v533_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=236, w2=326, w3=477, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(326, min_periods=max(326//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0875 + 0.0025134 * anchor
    return base_signal.diff()

def f40q_eqdq_534_accrual_v534_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=243, w2=337, w3=490, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(337, min_periods=max(337//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2186 * _rolling_slope(draw, 490) + 0.0025135 * anchor
    return base_signal.diff()

def f40q_eqdq_535_accrual_v535_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=250, w2=348, w3=503, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.11625 + 0.0025136 * anchor
    return base_signal.diff()

def f40q_eqdq_536_accrual_v536_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=6, w2=359, w3=516, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(359, min_periods=max(359//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.130625 + 0.0025137 * anchor
    return base_signal.diff()

def f40q_eqdq_537_accrual_v537_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=13, w2=370, w3=529, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 370)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.145 + 0.0025138 * anchor
    return base_signal.diff()

def f40q_eqdq_538_accrual_v538_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=20, w2=381, w3=542, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(381, min_periods=max(381//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.159375 + 0.0025139 * anchor
    return base_signal.diff()

def f40q_eqdq_539_accrual_v539_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=27, w2=392, w3=555, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(27)
    rank = change.rolling(392, min_periods=max(392//3, 2)).rank(pct=True)
    persistence = change.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2566 * persistence + 0.002514 * anchor
    return base_signal.diff()

def f40q_eqdq_540_accrual_v540_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=34, w2=403, w3=568, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(403, min_periods=max(403//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.188125 + 0.0025141 * anchor
    return base_signal.diff()

def f40q_eqdq_541_accrual_v541_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=41, w2=414, w3=581, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(414, min_periods=max(414//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2718 * slope + 0.0025142 * anchor
    return base_signal.diff()

def f40q_eqdq_542_accrual_v542_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=48, w2=425, w3=594, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(48)
    drag = impulse.rolling(425, min_periods=max(425//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.216875 + 0.0025143 * anchor
    return base_signal.diff()

def f40q_eqdq_543_accrual_v543_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=55, w2=436, w3=607, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.287 * acceleration + 0.0025144 * anchor
    return base_signal.diff()

def f40q_eqdq_544_accrual_v544_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=62, w2=447, w3=620, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 62)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2946 * pressure.rolling(620, min_periods=max(620//3, 2)).mean() + 0.0025145 * anchor
    return base_signal.diff()

def f40q_eqdq_545_accrual_v545_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=69, w2=458, w3=633, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(69, min_periods=max(69//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.26 + 0.0025146 * anchor
    return base_signal.diff()

def f40q_eqdq_546_accrual_v546_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=76, w2=469, w3=646, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(469, min_periods=max(469//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 76)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.274375 + 0.0025147 * anchor
    return base_signal.diff()

def f40q_eqdq_547_accrual_v547_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=83, w2=480, w3=659, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(83, min_periods=max(83//3, 2)).mean(), b.abs().rolling(480, min_periods=max(480//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3174 * _rolling_slope(cover, 83) + 0.0025148 * anchor
    return base_signal.diff()

def f40q_eqdq_548_accrual_v548_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=90, w2=491, w3=672, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.325 * y + 0.675000 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 90) - _rolling_slope(basket, 491) + 0.0025149 * anchor
    return base_signal.diff()

def f40q_eqdq_549_accrual_v549_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=97, w2=502, w3=685, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(502, min_periods=max(502//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3175 + 0.002515 * anchor
    return base_signal.diff()

def f40q_eqdq_550_accrual_v550_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=104, w2=10, w3=698, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(10, min_periods=max(10//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3402 * _rolling_slope(draw, 698) + 0.0025151 * anchor
    return base_signal.diff()

def f40q_eqdq_551_accrual_v551_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=111, w2=21, w3=711, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(111) - b.diff(21)
    stress = imbalance.rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.34625 + 0.0025152 * anchor
    return base_signal.diff()

def f40q_eqdq_552_accrual_v552_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=118, w2=32, w3=724, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(32, min_periods=max(32//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.360625 + 0.0025153 * anchor
    return base_signal.diff()

def f40q_eqdq_553_accrual_v553_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=125, w2=43, w3=737, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 125)
    slow = _rolling_slope(x, 43)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.375 + 0.0025154 * anchor
    return base_signal.diff()

def f40q_eqdq_554_accrual_v554_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=132, w2=54, w3=750, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(54, min_periods=max(54//3, 2)).max()
    trough = x.rolling(132, min_periods=max(132//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.389375 + 0.0025155 * anchor
    return base_signal.diff()

def f40q_eqdq_555_accrual_v555_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=139, w2=65, w3=763, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(65, min_periods=max(65//3, 2)).rank(pct=True)
    persistence = change.rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3782 * persistence + 0.0025156 * anchor
    return base_signal.diff()

def f40q_eqdq_556_accrual_v556_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=146, w2=76, w3=19, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(146, min_periods=max(146//3, 2)).std()
    vol_slow = ret.rolling(76, min_periods=max(76//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.418125 + 0.0025157 * anchor
    return base_signal.diff()

def f40q_eqdq_557_accrual_v557_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=153, w2=87, w3=32, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(87, min_periods=max(87//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 153)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3934 * slope + 0.0025158 * anchor
    return base_signal.diff()

def f40q_eqdq_558_accrual_v558_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=160, w2=98, w3=45, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(98, min_periods=max(98//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.446875 + 0.0025159 * anchor
    return base_signal.diff()

def f40q_eqdq_559_accrual_v559_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=167, w2=109, w3=58, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 167)
    acceleration = _rolling_slope(velocity, 109)
    curvature = _rolling_slope(acceleration, 58)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4086 * acceleration + 0.002516 * anchor
    return base_signal.diff()

def f40q_eqdq_560_accrual_v560_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=174, w2=120, w3=71, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 174)
    pressure = rel_log.diff(120)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0398 * pressure.rolling(71, min_periods=max(71//3, 2)).mean() + 0.0025161 * anchor
    return base_signal.diff()

def f40q_eqdq_561_accrual_v561_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=181, w2=131, w3=84, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(181, min_periods=max(181//3, 2)).mean())
    decay = spread.ewm(span=131, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.49 + 0.0025162 * anchor
    return base_signal.diff()

def f40q_eqdq_562_accrual_v562_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=188, w2=142, w3=97, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(142, min_periods=max(142//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 188)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.504375 + 0.0025163 * anchor
    return base_signal.diff()

def f40q_eqdq_563_accrual_v563_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=195, w2=153, w3=110, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(195, min_periods=max(195//3, 2)).mean(), b.abs().rolling(153, min_periods=max(153//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(110) + 0.0626 * _rolling_slope(cover, 195) + 0.0025164 * anchor
    return base_signal.diff()

def f40q_eqdq_564_accrual_v564_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=202, w2=164, w3=123, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.0702 * y + 0.929800 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 202) - _rolling_slope(basket, 164) + 0.0025165 * anchor
    return base_signal.diff()

def f40q_eqdq_565_accrual_v565_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=209, w2=175, w3=136, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(175, min_periods=max(175//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5475 + 0.0025166 * anchor
    return base_signal.diff()

def f40q_eqdq_566_accrual_v566_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=216, w2=186, w3=149, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(186, min_periods=max(186//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0854 * _rolling_slope(draw, 149) + 0.0025167 * anchor
    return base_signal.diff()

def f40q_eqdq_567_accrual_v567_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=223, w2=197, w3=162, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(162, min_periods=max(162//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.57625 + 0.0025168 * anchor
    return base_signal.diff()

def f40q_eqdq_568_accrual_v568_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=230, w2=208, w3=175, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(208, min_periods=max(208//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.590625 + 0.0025169 * anchor
    return base_signal.diff()

def f40q_eqdq_569_accrual_v569_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=237, w2=219, w3=188, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 219)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=188, adjust=False).mean() * 1.605 + 0.002517 * anchor
    return base_signal.diff()

def f40q_eqdq_570_accrual_v570_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=244, w2=230, w3=201, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(230, min_periods=max(230//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.619375 + 0.0025171 * anchor
    return base_signal.diff()

def f40q_eqdq_571_accrual_v571_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=251, w2=241, w3=214, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(241, min_periods=max(241//3, 2)).rank(pct=True)
    persistence = change.rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1234 * persistence + 0.0025172 * anchor
    return base_signal.diff()

def f40q_eqdq_572_accrual_v572_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=7, w2=252, w3=227, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(252, min_periods=max(252//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.875 + 0.0025173 * anchor
    return base_signal.diff()

def f40q_eqdq_573_accrual_v573_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=14, w2=263, w3=240, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(263, min_periods=max(263//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1386 * slope + 0.0025174 * anchor
    return base_signal.diff()

def f40q_eqdq_574_accrual_v574_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=21, w2=274, w3=253, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(21)
    drag = impulse.rolling(274, min_periods=max(274//3, 2)).mean()
    noise = impulse.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.90375 + 0.0025175 * anchor
    return base_signal.diff()

def f40q_eqdq_575_accrual_v575_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=28, w2=285, w3=266, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 285)
    curvature = _rolling_slope(acceleration, 266)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1538 * acceleration + 0.0025176 * anchor
    return base_signal.diff()

def f40q_eqdq_576_accrual_v576_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=35, w2=296, w3=279, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 35)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1614 * pressure.rolling(279, min_periods=max(279//3, 2)).mean() + 0.0025177 * anchor
    return base_signal.diff()

def f40q_eqdq_577_accrual_v577_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=42, w2=307, w3=292, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(42, min_periods=max(42//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.946875 + 0.0025178 * anchor
    return base_signal.diff()

def f40q_eqdq_578_accrual_v578_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=49, w2=318, w3=305, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(318, min_periods=max(318//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 49)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.96125 + 0.0025179 * anchor
    return base_signal.diff()

def f40q_eqdq_579_accrual_v579_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=56, w2=329, w3=318, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(56, min_periods=max(56//3, 2)).mean(), b.abs().rolling(329, min_periods=max(329//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1842 * _rolling_slope(cover, 56) + 0.002518 * anchor
    return base_signal.diff()

def f40q_eqdq_580_accrual_v580_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=63, w2=340, w3=331, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.1918 * y + 0.808200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 63) - _rolling_slope(basket, 340) + 0.0025181 * anchor
    return base_signal.diff()

def f40q_eqdq_581_accrual_v581_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=70, w2=351, w3=344, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.004375 + 0.0025182 * anchor
    return base_signal.diff()

def f40q_eqdq_582_accrual_v582_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=77, w2=362, w3=357, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(362, min_periods=max(362//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.207 * _rolling_slope(draw, 357) + 0.0025183 * anchor
    return base_signal.diff()

def f40q_eqdq_583_accrual_v583_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=84, w2=373, w3=370, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(84) - b.diff(126)
    stress = imbalance.rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.033125 + 0.0025184 * anchor
    return base_signal.diff()

def f40q_eqdq_584_accrual_v584_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=91, w2=384, w3=383, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(383, min_periods=max(383//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0475 + 0.0025185 * anchor
    return base_signal.diff()

def f40q_eqdq_585_accrual_v585_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=98, w2=395, w3=396, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.061875 + 0.0025186 * anchor
    return base_signal.diff()

def f40q_eqdq_586_accrual_v586_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=105, w2=406, w3=409, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(406, min_periods=max(406//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07625 + 0.0025187 * anchor
    return base_signal.diff()

def f40q_eqdq_587_accrual_v587_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=112, w2=417, w3=422, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(112)
    rank = change.rolling(417, min_periods=max(417//3, 2)).rank(pct=True)
    persistence = change.rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245 * persistence + 0.0025188 * anchor
    return base_signal.diff()

def f40q_eqdq_588_accrual_v588_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=119, w2=428, w3=435, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(428, min_periods=max(428//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.105 + 0.0025189 * anchor
    return base_signal.diff()

def f40q_eqdq_589_accrual_v589_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=126, w2=439, w3=448, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2602 * slope + 0.002519 * anchor
    return base_signal.diff()

def f40q_eqdq_590_accrual_v590_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=133, w2=450, w3=461, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(461, min_periods=max(461//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13375 + 0.0025191 * anchor
    return base_signal.diff()

def f40q_eqdq_591_accrual_v591_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=140, w2=461, w3=474, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 461)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2754 * acceleration + 0.0025192 * anchor
    return base_signal.diff()

def f40q_eqdq_592_accrual_v592_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=147, w2=472, w3=487, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 147)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.283 * pressure.rolling(487, min_periods=max(487//3, 2)).mean() + 0.0025193 * anchor
    return base_signal.diff()

def f40q_eqdq_593_accrual_v593_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=154, w2=483, w3=500, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(154, min_periods=max(154//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.176875 + 0.0025194 * anchor
    return base_signal.diff()

def f40q_eqdq_594_accrual_v594_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=161, w2=494, w3=513, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(494, min_periods=max(494//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 161)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.19125 + 0.0025195 * anchor
    return base_signal.diff()

def f40q_eqdq_595_accrual_v595_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=168, w2=505, w3=526, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(168, min_periods=max(168//3, 2)).mean(), b.abs().rolling(505, min_periods=max(505//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3058 * _rolling_slope(cover, 168) + 0.0025196 * anchor
    return base_signal.diff()

def f40q_eqdq_596_accrual_v596_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=175, w2=13, w3=539, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3134 * y + 0.686600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 175) - _rolling_slope(basket, 13) + 0.0025197 * anchor
    return base_signal.diff()

def f40q_eqdq_597_accrual_v597_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=182, w2=24, w3=552, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(182, min_periods=max(182//3, 2)).mean(), upside.rolling(24, min_periods=max(24//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.234375 + 0.0025198 * anchor
    return base_signal.diff()

def f40q_eqdq_598_accrual_v598_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=189, w2=35, w3=565, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(189, min_periods=max(189//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3286 * _rolling_slope(draw, 565) + 0.0025199 * anchor
    return base_signal.diff()

def f40q_eqdq_599_accrual_v599_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=196, w2=46, w3=578, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(46)
    stress = imbalance.rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.263125 + 0.00252 * anchor
    return base_signal.diff()

def f40q_eqdq_600_accrual_v600_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=203, w2=57, w3=591, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(57, min_periods=max(57//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(591, min_periods=max(591//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2775 + 0.0025201 * anchor
    return base_signal.diff()
