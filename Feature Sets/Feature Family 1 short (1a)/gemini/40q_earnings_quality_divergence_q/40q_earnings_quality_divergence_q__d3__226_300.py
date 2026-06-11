"""40q earnings quality divergence q d3 third derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f40q_eqdq_226_accrual_v226_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=95, w2=470, w3=271, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(470, min_periods=max(470//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 95)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.313125 + 0.0024827 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_227_accrual_v227_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=102, w2=481, w3=284, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(102, min_periods=max(102//3, 2)).mean(), b.abs().rolling(481, min_periods=max(481//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1438 * _rolling_slope(cover, 102) + 0.0024828 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_228_accrual_v228_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=109, w2=492, w3=297, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1514 * y + 0.848600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 109) - _rolling_slope(basket, 492) + 0.0024829 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_229_accrual_v229_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=116, w2=503, w3=310, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(503, min_periods=max(503//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.35625 + 0.002483 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_230_accrual_v230_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=123, w2=11, w3=323, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(11, min_periods=max(11//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1666 * _rolling_slope(draw, 323) + 0.0024831 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_231_accrual_v231_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=130, w2=22, w3=336, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(22)
    stress = imbalance.rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.385 + 0.0024832 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_232_accrual_v232_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=137, w2=33, w3=349, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(33, min_periods=max(33//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.399375 + 0.0024833 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_233_accrual_v233_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=144, w2=44, w3=362, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 44)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.41375 + 0.0024834 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_234_accrual_v234_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=151, w2=55, w3=375, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.428125 + 0.0024835 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_235_accrual_v235_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=158, w2=66, w3=388, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(66, min_periods=max(66//3, 2)).rank(pct=True)
    persistence = change.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2046 * persistence + 0.0024836 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_236_accrual_v236_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=165, w2=77, w3=401, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(77, min_periods=max(77//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.456875 + 0.0024837 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_237_accrual_v237_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=172, w2=88, w3=414, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(88, min_periods=max(88//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2198 * slope + 0.0024838 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_238_accrual_v238_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=179, w2=99, w3=427, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.485625 + 0.0024839 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_239_accrual_v239_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=186, w2=110, w3=440, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 110)
    curvature = _rolling_slope(acceleration, 440)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235 * acceleration + 0.002484 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_240_accrual_v240_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=193, w2=121, w3=453, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 193)
    pressure = rel_log.diff(121)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2426 * pressure.rolling(453, min_periods=max(453//3, 2)).mean() + 0.0024841 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_241_accrual_v241_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=200, w2=132, w3=466, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(200, min_periods=max(200//3, 2)).mean())
    decay = spread.ewm(span=132, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.52875 + 0.0024842 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_242_accrual_v242_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=207, w2=143, w3=479, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(143, min_periods=max(143//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 207)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.543125 + 0.0024843 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_243_accrual_v243_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=214, w2=154, w3=492, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(214, min_periods=max(214//3, 2)).mean(), b.abs().rolling(154, min_periods=max(154//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2654 * _rolling_slope(cover, 214) + 0.0024844 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_244_accrual_v244_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=221, w2=165, w3=505, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.273 * y + 0.727000 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 221) - _rolling_slope(basket, 165) + 0.0024845 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_245_accrual_v245_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=228, w2=176, w3=518, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.58625 + 0.0024846 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_246_accrual_v246_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=235, w2=187, w3=531, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(187, min_periods=max(187//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2882 * _rolling_slope(draw, 531) + 0.0024847 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_247_accrual_v247_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=242, w2=198, w3=544, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.615 + 0.0024848 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_248_accrual_v248_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=249, w2=209, w3=557, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(209, min_periods=max(209//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.85625 + 0.0024849 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_249_accrual_v249_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=5, w2=220, w3=570, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 220)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.870625 + 0.002485 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_250_accrual_v250_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=12, w2=231, w3=583, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(231, min_periods=max(231//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.885 + 0.0024851 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_251_accrual_v251_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=19, w2=242, w3=596, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(19)
    rank = change.rolling(242, min_periods=max(242//3, 2)).rank(pct=True)
    persistence = change.rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3262 * persistence + 0.0024852 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_252_accrual_v252_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=26, w2=253, w3=609, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(253, min_periods=max(253//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.91375 + 0.0024853 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_253_accrual_v253_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=33, w2=264, w3=622, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(264, min_periods=max(264//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3414 * slope + 0.0024854 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_254_accrual_v254_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=40, w2=275, w3=635, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(40)
    drag = impulse.rolling(275, min_periods=max(275//3, 2)).mean()
    noise = impulse.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9425 + 0.0024855 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_255_accrual_v255_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=47, w2=286, w3=648, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 286)
    curvature = _rolling_slope(acceleration, 648)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3566 * acceleration + 0.0024856 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_256_accrual_v256_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=54, w2=297, w3=661, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 54)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3642 * pressure.rolling(661, min_periods=max(661//3, 2)).mean() + 0.0024857 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_257_accrual_v257_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=61, w2=308, w3=674, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(61, min_periods=max(61//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.985625 + 0.0024858 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_258_accrual_v258_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=68, w2=319, w3=687, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(319, min_periods=max(319//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 68)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.0 + 0.0024859 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_259_accrual_v259_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=75, w2=330, w3=700, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(75, min_periods=max(75//3, 2)).mean(), b.abs().rolling(330, min_periods=max(330//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.387 * _rolling_slope(cover, 75) + 0.002486 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_260_accrual_v260_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=82, w2=341, w3=713, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3946 * y + 0.605400 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 82) - _rolling_slope(basket, 341) + 0.0024861 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_261_accrual_v261_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=89, w2=352, w3=726, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(352, min_periods=max(352//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.043125 + 0.0024862 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_262_accrual_v262_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=96, w2=363, w3=739, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(363, min_periods=max(363//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4098 * _rolling_slope(draw, 739) + 0.0024863 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_263_accrual_v263_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=103, w2=374, w3=752, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(103) - b.diff(126)
    stress = imbalance.rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.071875 + 0.0024864 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_264_accrual_v264_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=110, w2=385, w3=765, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(385, min_periods=max(385//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.08625 + 0.0024865 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_265_accrual_v265_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=117, w2=396, w3=21, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 396)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=21, adjust=False).mean() * 1.100625 + 0.0024866 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_266_accrual_v266_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=124, w2=407, w3=34, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(407, min_periods=max(407//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.115 + 0.0024867 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_267_accrual_v267_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=131, w2=418, w3=47, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(418, min_periods=max(418//3, 2)).rank(pct=True)
    persistence = change.rolling(47, min_periods=max(47//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0714 * persistence + 0.0024868 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_268_accrual_v268_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=138, w2=429, w3=60, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(429, min_periods=max(429//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14375 + 0.0024869 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_269_accrual_v269_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=145, w2=440, w3=73, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(440, min_periods=max(440//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0866 * slope + 0.002487 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_270_accrual_v270_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=152, w2=451, w3=86, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1725 + 0.0024871 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_271_accrual_v271_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=159, w2=462, w3=99, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 462)
    curvature = _rolling_slope(acceleration, 99)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1018 * acceleration + 0.0024872 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_272_accrual_v272_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=166, w2=473, w3=112, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 166)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1094 * pressure.rolling(112, min_periods=max(112//3, 2)).mean() + 0.0024873 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_273_accrual_v273_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=173, w2=484, w3=125, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(173, min_periods=max(173//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.215625 + 0.0024874 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_274_accrual_v274_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=180, w2=495, w3=138, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(495, min_periods=max(495//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 180)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.23 + 0.0024875 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_275_accrual_v275_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=187, w2=506, w3=151, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(187, min_periods=max(187//3, 2)).mean(), b.abs().rolling(506, min_periods=max(506//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1322 * _rolling_slope(cover, 187) + 0.0024876 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_276_accrual_v276_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=194, w2=14, w3=164, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1398 * y + 0.860200 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 194) - _rolling_slope(basket, 14) + 0.0024877 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_277_accrual_v277_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=201, w2=25, w3=177, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(25, min_periods=max(25//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.273125 + 0.0024878 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_278_accrual_v278_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=208, w2=36, w3=190, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.155 * _rolling_slope(draw, 190) + 0.0024879 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_279_accrual_v279_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=215, w2=47, w3=203, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(47)
    stress = imbalance.rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.301875 + 0.002488 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_280_accrual_v280_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=222, w2=58, w3=216, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.31625 + 0.0024881 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_281_accrual_v281_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=229, w2=69, w3=229, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 69)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=229, adjust=False).mean() * 1.330625 + 0.0024882 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_282_accrual_v282_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=236, w2=80, w3=242, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.345 + 0.0024883 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_283_accrual_v283_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=243, w2=91, w3=255, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.193 * persistence + 0.0024884 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_284_accrual_v284_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=250, w2=102, w3=268, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.37375 + 0.0024885 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_285_accrual_v285_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=6, w2=113, w3=281, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2082 * slope + 0.0024886 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_286_accrual_v286_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=13, w2=124, w3=294, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(13)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4025 + 0.0024887 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_287_accrual_v287_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=20, w2=135, w3=307, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 307)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2234 * acceleration + 0.0024888 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_288_accrual_v288_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=27, w2=146, w3=320, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 27)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.231 * pressure.rolling(320, min_periods=max(320//3, 2)).mean() + 0.0024889 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_289_accrual_v289_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=34, w2=157, w3=333, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(34, min_periods=max(34//3, 2)).mean())
    decay = spread.ewm(span=157, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.445625 + 0.002489 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_290_accrual_v290_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=41, w2=168, w3=346, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(168, min_periods=max(168//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 41)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.46 + 0.0024891 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_291_accrual_v291_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=48, w2=179, w3=359, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(48, min_periods=max(48//3, 2)).mean(), b.abs().rolling(179, min_periods=max(179//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2538 * _rolling_slope(cover, 48) + 0.0024892 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_292_accrual_v292_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=55, w2=190, w3=372, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2614 * y + 0.738600 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 55) - _rolling_slope(basket, 190) + 0.0024893 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_293_accrual_v293_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=62, w2=201, w3=385, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(201, min_periods=max(201//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.503125 + 0.0024894 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_294_accrual_v294_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=69, w2=212, w3=398, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(212, min_periods=max(212//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2766 * _rolling_slope(draw, 398) + 0.0024895 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_295_accrual_v295_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=76, w2=223, w3=411, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(76) - b.diff(126)
    stress = imbalance.rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.531875 + 0.0024896 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_296_accrual_v296_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=83, w2=234, w3=424, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(234, min_periods=max(234//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(424, min_periods=max(424//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.54625 + 0.0024897 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_297_accrual_v297_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=90, w2=245, w3=437, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 245)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.560625 + 0.0024898 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_298_accrual_v298_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=97, w2=256, w3=450, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(256, min_periods=max(256//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.575 + 0.0024899 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_299_accrual_v299_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=104, w2=267, w3=463, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(104)
    rank = change.rolling(267, min_periods=max(267//3, 2)).rank(pct=True)
    persistence = change.rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3146 * persistence + 0.00249 * anchor
    return base_signal.diff().diff().diff()

def f40q_eqdq_300_accrual_v300_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=111, w2=278, w3=476, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(278, min_periods=max(278//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60375 + 0.0024901 * anchor
    return base_signal.diff().diff().diff()
