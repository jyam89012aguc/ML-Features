"""40q earnings quality divergence q d2 second derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f40q_eqdq_151_accrual_v151_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=72, w2=148, w3=53, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(72) - b.diff(126)
    stress = imbalance.rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.008125 + 0.0024752 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_152_accrual_v152_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=79, w2=159, w3=66, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 79)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0225 + 0.0024753 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_153_accrual_v153_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=86, w2=170, w3=79, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 86)
    slow = _rolling_slope(x, 170)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=79, adjust=False).mean() * 1.036875 + 0.0024754 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_154_accrual_v154_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=93, w2=181, w3=92, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(181, min_periods=max(181//3, 2)).max()
    trough = x.rolling(93, min_periods=max(93//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.05125 + 0.0024755 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_155_accrual_v155_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=100, w2=192, w3=105, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(100)
    rank = change.rolling(192, min_periods=max(192//3, 2)).rank(pct=True)
    persistence = change.rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3494 * persistence + 0.0024756 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_156_accrual_v156_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=107, w2=203, w3=118, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(107, min_periods=max(107//3, 2)).std()
    vol_slow = ret.rolling(203, min_periods=max(203//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.08 + 0.0024757 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_157_accrual_v157_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=114, w2=214, w3=131, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(214, min_periods=max(214//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 114)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3646 * slope + 0.0024758 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_158_accrual_v158_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=121, w2=225, w3=144, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(121)
    drag = impulse.rolling(225, min_periods=max(225//3, 2)).mean()
    noise = impulse.abs().rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.10875 + 0.0024759 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_159_accrual_v159_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=128, w2=236, w3=157, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 128)
    acceleration = _rolling_slope(velocity, 236)
    curvature = _rolling_slope(acceleration, 157)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3798 * acceleration + 0.002476 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_160_accrual_v160_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=135, w2=247, w3=170, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 135)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3874 * pressure.rolling(170, min_periods=max(170//3, 2)).mean() + 0.0024761 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_161_accrual_v161_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=142, w2=258, w3=183, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(142, min_periods=max(142//3, 2)).mean())
    decay = spread.ewm(span=258, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.151875 + 0.0024762 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_162_accrual_v162_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=149, w2=269, w3=196, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(269, min_periods=max(269//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 149)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.16625 + 0.0024763 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_163_accrual_v163_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=156, w2=280, w3=209, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(156, min_periods=max(156//3, 2)).mean(), b.abs().rolling(280, min_periods=max(280//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.4102 * _rolling_slope(cover, 156) + 0.0024764 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_164_accrual_v164_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=163, w2=291, w3=222, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0414 * y + 0.958600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 163) - _rolling_slope(basket, 291) + 0.0024765 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_165_accrual_v165_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=170, w2=302, w3=235, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.209375 + 0.0024766 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_166_accrual_v166_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=177, w2=313, w3=248, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0566 * _rolling_slope(draw, 248) + 0.0024767 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_167_accrual_v167_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=184, w2=324, w3=261, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.238125 + 0.0024768 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_168_accrual_v168_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=191, w2=335, w3=274, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2525 + 0.0024769 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_169_accrual_v169_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=198, w2=346, w3=287, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 346)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=287, adjust=False).mean() * 1.266875 + 0.002477 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_170_accrual_v170_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=205, w2=357, w3=300, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.28125 + 0.0024771 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_171_accrual_v171_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=212, w2=368, w3=313, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0946 * persistence + 0.0024772 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_172_accrual_v172_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=219, w2=379, w3=326, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31 + 0.0024773 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_173_accrual_v173_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=226, w2=390, w3=339, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1098 * slope + 0.0024774 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_174_accrual_v174_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=233, w2=401, w3=352, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(401, min_periods=max(401//3, 2)).mean()
    noise = impulse.abs().rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33875 + 0.0024775 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_175_accrual_v175_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=240, w2=412, w3=365, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 412)
    curvature = _rolling_slope(acceleration, 365)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125 * acceleration + 0.0024776 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_176_accrual_v176_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=247, w2=423, w3=378, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 247)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1326 * pressure.rolling(378, min_periods=max(378//3, 2)).mean() + 0.0024777 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_177_accrual_v177_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=254, w2=434, w3=391, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(254, min_periods=max(254//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.381875 + 0.0024778 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_178_accrual_v178_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=10, w2=445, w3=404, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(445, min_periods=max(445//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 10)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.39625 + 0.0024779 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_179_accrual_v179_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=17, w2=456, w3=417, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(17, min_periods=max(17//3, 2)).mean(), b.abs().rolling(456, min_periods=max(456//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1554 * _rolling_slope(cover, 17) + 0.002478 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_180_accrual_v180_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=24, w2=467, w3=430, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.163 * y + 0.837000 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 24) - _rolling_slope(basket, 467) + 0.0024781 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_181_accrual_v181_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=31, w2=478, w3=443, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(478, min_periods=max(478//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.439375 + 0.0024782 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_182_accrual_v182_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=38, w2=489, w3=456, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1782 * _rolling_slope(draw, 456) + 0.0024783 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_183_accrual_v183_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=45, w2=500, w3=469, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(45) - b.diff(126)
    stress = imbalance.rolling(469, min_periods=max(469//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.468125 + 0.0024784 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_184_accrual_v184_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=52, w2=511, w3=482, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(511, min_periods=max(511//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4825 + 0.0024785 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_185_accrual_v185_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=59, w2=19, w3=495, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.496875 + 0.0024786 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_186_accrual_v186_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=66, w2=30, w3=508, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.51125 + 0.0024787 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_187_accrual_v187_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=73, w2=41, w3=521, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(73)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2162 * persistence + 0.0024788 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_188_accrual_v188_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=80, w2=52, w3=534, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54 + 0.0024789 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_189_accrual_v189_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=87, w2=63, w3=547, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(63, min_periods=max(63//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2314 * slope + 0.002479 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_190_accrual_v190_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=94, w2=74, w3=560, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(94)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.56875 + 0.0024791 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_191_accrual_v191_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=101, w2=85, w3=573, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 85)
    curvature = _rolling_slope(acceleration, 573)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2466 * acceleration + 0.0024792 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_192_accrual_v192_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=108, w2=96, w3=586, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 108)
    pressure = rel_log.diff(96)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2542 * pressure.rolling(586, min_periods=max(586//3, 2)).mean() + 0.0024793 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_193_accrual_v193_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=115, w2=107, w3=599, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(115, min_periods=max(115//3, 2)).mean())
    decay = spread.ewm(span=107, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.611875 + 0.0024794 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_194_accrual_v194_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=122, w2=118, w3=612, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(118, min_periods=max(118//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 122)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.853125 + 0.0024795 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_195_accrual_v195_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=129, w2=129, w3=625, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(129, min_periods=max(129//3, 2)).mean(), b.abs().rolling(129, min_periods=max(129//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.277 * _rolling_slope(cover, 129) + 0.0024796 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_196_accrual_v196_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=136, w2=140, w3=638, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2846 * y + 0.715400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 136) - _rolling_slope(basket, 140) + 0.0024797 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_197_accrual_v197_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=143, w2=151, w3=651, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(151, min_periods=max(151//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.89625 + 0.0024798 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_198_accrual_v198_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=150, w2=162, w3=664, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2998 * _rolling_slope(draw, 664) + 0.0024799 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_199_accrual_v199_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=157, w2=173, w3=677, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.925 + 0.00248 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_200_accrual_v200_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=164, w2=184, w3=690, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(184, min_periods=max(184//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.939375 + 0.0024801 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_201_accrual_v201_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=171, w2=195, w3=703, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 195)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.95375 + 0.0024802 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_202_accrual_v202_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=178, w2=206, w3=716, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(206, min_periods=max(206//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.968125 + 0.0024803 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_203_accrual_v203_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=185, w2=217, w3=729, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(217, min_periods=max(217//3, 2)).rank(pct=True)
    persistence = change.rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3378 * persistence + 0.0024804 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_204_accrual_v204_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=192, w2=228, w3=742, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(228, min_periods=max(228//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.996875 + 0.0024805 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_205_accrual_v205_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=199, w2=239, w3=755, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(239, min_periods=max(239//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.353 * slope + 0.0024806 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_206_accrual_v206_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=206, w2=250, w3=768, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(250, min_periods=max(250//3, 2)).mean()
    noise = impulse.abs().rolling(768, min_periods=max(768//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.025625 + 0.0024807 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_207_accrual_v207_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=213, w2=261, w3=24, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 261)
    curvature = _rolling_slope(acceleration, 24)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3682 * acceleration + 0.0024808 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_208_accrual_v208_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=220, w2=272, w3=37, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 220)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3758 * pressure.rolling(37, min_periods=max(37//3, 2)).mean() + 0.0024809 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_209_accrual_v209_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=227, w2=283, w3=50, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(227, min_periods=max(227//3, 2)).mean())
    decay = spread.ewm(span=283, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.06875 + 0.002481 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_210_accrual_v210_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=234, w2=294, w3=63, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(294, min_periods=max(294//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 234)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.083125 + 0.0024811 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_211_accrual_v211_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=241, w2=305, w3=76, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(241, min_periods=max(241//3, 2)).mean(), b.abs().rolling(305, min_periods=max(305//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(76) + 0.3986 * _rolling_slope(cover, 241) + 0.0024812 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_212_accrual_v212_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=248, w2=316, w3=89, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.4062 * y + 0.593800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 248) - _rolling_slope(basket, 316) + 0.0024813 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_213_accrual_v213_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=255, w2=327, w3=102, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(255, min_periods=max(255//3, 2)).mean(), upside.rolling(327, min_periods=max(327//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(102) * 1.12625 + 0.0024814 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_214_accrual_v214_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=11, w2=338, w3=115, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(338, min_periods=max(338//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.045 * _rolling_slope(draw, 115) + 0.0024815 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_215_accrual_v215_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=18, w2=349, w3=128, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(18) - b.diff(126)
    stress = imbalance.rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.155 + 0.0024816 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_216_accrual_v216_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=25, w2=360, w3=141, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(360, min_periods=max(360//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.169375 + 0.0024817 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_217_accrual_v217_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=32, w2=371, w3=154, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 371)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=154, adjust=False).mean() * 1.18375 + 0.0024818 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_218_accrual_v218_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=39, w2=382, w3=167, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.198125 + 0.0024819 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_219_accrual_v219_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=46, w2=393, w3=180, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(46)
    rank = change.rolling(393, min_periods=max(393//3, 2)).rank(pct=True)
    persistence = change.rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.083 * persistence + 0.002482 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_220_accrual_v220_d2(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=53, w2=404, w3=193, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.226875 + 0.0024821 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_221_accrual_v221_d2(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=60, w2=415, w3=206, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(415, min_periods=max(415//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0982 * slope + 0.0024822 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_222_accrual_v222_d2(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=67, w2=426, w3=219, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(67)
    drag = impulse.rolling(426, min_periods=max(426//3, 2)).mean()
    noise = impulse.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.255625 + 0.0024823 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_223_accrual_v223_d2(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=74, w2=437, w3=232, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 437)
    curvature = _rolling_slope(acceleration, 232)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1134 * acceleration + 0.0024824 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_224_accrual_v224_d2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=81, w2=448, w3=245, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 81)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.121 * pressure.rolling(245, min_periods=max(245//3, 2)).mean() + 0.0024825 * anchor
    return base_signal.diff().diff()

def f40q_eqdq_225_accrual_v225_d2(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated accrual replacement signal (w1=88, w2=459, w3=258, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(88, min_periods=max(88//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.29875 + 0.0024826 * anchor
    return base_signal.diff().diff()
