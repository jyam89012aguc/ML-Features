"""40 earnings quality divergence d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f40_eqd_001_accrual_v1_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=93, w2=449, w3=144, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=144, adjust=False).mean() * 1.050625 + 0.0024002 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_002_accrual_v2_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=100, w2=460, w3=157, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.065 + 0.0024003 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_003_accrual_v3_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=107, w2=471, w3=170, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(107)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2802 * persistence + 0.0024004 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_004_accrual_v4_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=114, w2=482, w3=183, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(482, min_periods=max(482//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.09375 + 0.0024005 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_005_accrual_v5_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=121, w2=493, w3=196, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2954 * slope + 0.0024006 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_006_accrual_v6_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=128, w2=504, w3=209, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(504, min_periods=max(504//3, 2)).mean()
    noise = impulse.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1225 + 0.0024007 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_007_accrual_v7_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=135, w2=12, w3=222, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 12)
    curvature = _rolling_slope(acceleration, 222)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3106 * acceleration + 0.0024008 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_008_accrual_v8_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=142, w2=23, w3=235, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 142)
    pressure = rel_log.diff(23)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3182 * pressure.rolling(235, min_periods=max(235//3, 2)).mean() + 0.0024009 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_009_accrual_v9_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=149, w2=34, w3=248, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(149, min_periods=max(149//3, 2)).mean())
    decay = spread.ewm(span=34, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.165625 + 0.002401 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_010_accrual_v10_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=156, w2=45, w3=261, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(45, min_periods=max(45//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 156)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.18 + 0.0024011 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_011_accrual_v11_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=163, w2=56, w3=274, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(163, min_periods=max(163//3, 2)).mean(), b.abs().rolling(56, min_periods=max(56//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.341 * _rolling_slope(cover, 163) + 0.0024012 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_012_accrual_v12_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=170, w2=67, w3=287, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.3486 * y + 0.651400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 170) - _rolling_slope(basket, 67) + 0.0024013 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_013_accrual_v13_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=177, w2=78, w3=300, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(78, min_periods=max(78//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.223125 + 0.0024014 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_014_accrual_v14_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=184, w2=89, w3=313, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(89, min_periods=max(89//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3638 * _rolling_slope(draw, 313) + 0.0024015 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_015_accrual_v15_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=191, w2=100, w3=326, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(100)
    stress = imbalance.rolling(326, min_periods=max(326//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.251875 + 0.0024016 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_016_accrual_v16_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=198, w2=111, w3=339, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(111, min_periods=max(111//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.26625 + 0.0024017 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_017_accrual_v17_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=205, w2=122, w3=352, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 122)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.280625 + 0.0024018 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_018_accrual_v18_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=212, w2=133, w3=365, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(133, min_periods=max(133//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.295 + 0.0024019 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_019_accrual_v19_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=219, w2=144, w3=378, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4018 * persistence + 0.002402 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_020_accrual_v20_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=226, w2=155, w3=391, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(155, min_periods=max(155//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32375 + 0.0024021 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_021_accrual_v21_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=233, w2=166, w3=404, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0406 * slope + 0.0024022 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_022_accrual_v22_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=240, w2=177, w3=417, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3525 + 0.0024023 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_023_accrual_v23_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=247, w2=188, w3=430, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 188)
    curvature = _rolling_slope(acceleration, 430)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0558 * acceleration + 0.0024024 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_024_accrual_v24_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=254, w2=199, w3=443, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 254)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0634 * pressure.rolling(443, min_periods=max(443//3, 2)).mean() + 0.0024025 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_025_accrual_v25_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=10, w2=210, w3=456, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(10, min_periods=max(10//3, 2)).mean())
    decay = spread.ewm(span=210, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.395625 + 0.0024026 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_026_accrual_v26_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=17, w2=221, w3=469, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(221, min_periods=max(221//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 17)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.41 + 0.0024027 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_027_accrual_v27_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=24, w2=232, w3=482, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(24, min_periods=max(24//3, 2)).mean(), b.abs().rolling(232, min_periods=max(232//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0862 * _rolling_slope(cover, 24) + 0.0024028 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_028_accrual_v28_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=31, w2=243, w3=495, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.0938 * y + 0.906200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 31) - _rolling_slope(basket, 243) + 0.0024029 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_029_accrual_v29_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=38, w2=254, w3=508, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.453125 + 0.002403 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_030_accrual_v30_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=45, w2=265, w3=521, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.109 * _rolling_slope(draw, 521) + 0.0024031 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_031_accrual_v31_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=52, w2=276, w3=534, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(52) - b.diff(126)
    stress = imbalance.rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.481875 + 0.0024032 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_032_accrual_v32_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=59, w2=287, w3=547, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(287, min_periods=max(287//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.49625 + 0.0024033 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_033_accrual_v33_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=66, w2=298, w3=560, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 298)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.510625 + 0.0024034 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_034_accrual_v34_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=73, w2=309, w3=573, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(309, min_periods=max(309//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.525 + 0.0024035 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_035_accrual_v35_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=80, w2=320, w3=586, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(80)
    rank = change.rolling(320, min_periods=max(320//3, 2)).rank(pct=True)
    persistence = change.rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.147 * persistence + 0.0024036 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_036_accrual_v36_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=87, w2=331, w3=599, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(331, min_periods=max(331//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55375 + 0.0024037 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_037_accrual_v37_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=94, w2=342, w3=612, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(342, min_periods=max(342//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1622 * slope + 0.0024038 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_038_accrual_v38_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=101, w2=353, w3=625, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(101)
    drag = impulse.rolling(353, min_periods=max(353//3, 2)).mean()
    noise = impulse.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5825 + 0.0024039 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_039_accrual_v39_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=108, w2=364, w3=638, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 364)
    curvature = _rolling_slope(acceleration, 638)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1774 * acceleration + 0.002404 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_040_accrual_v40_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=115, w2=375, w3=651, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 115)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.185 * pressure.rolling(651, min_periods=max(651//3, 2)).mean() + 0.0024041 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_041_accrual_v41_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=122, w2=386, w3=664, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(122, min_periods=max(122//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.8525 + 0.0024042 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_042_accrual_v42_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=129, w2=397, w3=677, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(397, min_periods=max(397//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 129)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.866875 + 0.0024043 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_043_accrual_v43_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=136, w2=408, w3=690, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(136, min_periods=max(136//3, 2)).mean(), b.abs().rolling(408, min_periods=max(408//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2078 * _rolling_slope(cover, 136) + 0.0024044 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_044_accrual_v44_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=143, w2=419, w3=703, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.2154 * y + 0.784600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 143) - _rolling_slope(basket, 419) + 0.0024045 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_045_accrual_v45_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=150, w2=430, w3=716, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.91 + 0.0024046 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_046_accrual_v46_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=157, w2=441, w3=729, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(441, min_periods=max(441//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2306 * _rolling_slope(draw, 729) + 0.0024047 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_047_accrual_v47_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=164, w2=452, w3=742, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.93875 + 0.0024048 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_048_accrual_v48_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=171, w2=463, w3=755, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(463, min_periods=max(463//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.953125 + 0.0024049 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_049_accrual_v49_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=178, w2=474, w3=768, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9675 + 0.002405 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_050_accrual_v50_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=185, w2=485, w3=24, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(485, min_periods=max(485//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.981875 + 0.0024051 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_051_accrual_v51_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=192, w2=496, w3=37, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2686 * persistence + 0.0024052 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_052_accrual_v52_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=199, w2=507, w3=50, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(507, min_periods=max(507//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.010625 + 0.0024053 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_053_accrual_v53_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=206, w2=15, w3=63, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(15, min_periods=max(15//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2838 * slope + 0.0024054 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_054_accrual_v54_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=213, w2=26, w3=76, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(26, min_periods=max(26//3, 2)).mean()
    noise = impulse.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.039375 + 0.0024055 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_055_accrual_v55_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=220, w2=37, w3=89, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 37)
    curvature = _rolling_slope(acceleration, 89)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299 * acceleration + 0.0024056 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_056_accrual_v56_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=227, w2=48, w3=102, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 227)
    pressure = rel_log.diff(48)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3066 * pressure.rolling(102, min_periods=max(102//3, 2)).mean() + 0.0024057 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_057_accrual_v57_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=234, w2=59, w3=115, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    decay = spread.ewm(span=59, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.0825 + 0.0024058 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_058_accrual_v58_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=241, w2=70, w3=128, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(70, min_periods=max(70//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 241)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.096875 + 0.0024059 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_059_accrual_v59_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=248, w2=81, w3=141, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(248, min_periods=max(248//3, 2)).mean(), b.abs().rolling(81, min_periods=max(81//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3294 * _rolling_slope(cover, 248) + 0.002406 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_060_accrual_v60_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=255, w2=92, w3=154, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.337 * y + 0.663000 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 255) - _rolling_slope(basket, 92) + 0.0024061 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_061_accrual_v61_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=11, w2=103, w3=167, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(103, min_periods=max(103//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.14 + 0.0024062 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_062_accrual_v62_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=18, w2=114, w3=180, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(114, min_periods=max(114//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3522 * _rolling_slope(draw, 180) + 0.0024063 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_063_accrual_v63_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=25, w2=125, w3=193, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(25) - b.diff(125)
    stress = imbalance.rolling(193, min_periods=max(193//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.16875 + 0.0024064 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_064_accrual_v64_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=32, w2=136, w3=206, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(136, min_periods=max(136//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.183125 + 0.0024065 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_065_accrual_v65_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=39, w2=147, w3=219, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 147)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=219, adjust=False).mean() * 1.1975 + 0.0024066 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_066_accrual_v66_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=46, w2=158, w3=232, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(158, min_periods=max(158//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.211875 + 0.0024067 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_067_accrual_v67_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=53, w2=169, w3=245, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(53)
    rank = change.rolling(169, min_periods=max(169//3, 2)).rank(pct=True)
    persistence = change.rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3902 * persistence + 0.0024068 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_068_accrual_v68_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=60, w2=180, w3=258, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(180, min_periods=max(180//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.240625 + 0.0024069 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_069_accrual_v69_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=67, w2=191, w3=271, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(191, min_periods=max(191//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4054 * slope + 0.002407 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_070_accrual_v70_d3(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=74, w2=202, w3=284, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(74)
    drag = impulse.rolling(202, min_periods=max(202//3, 2)).mean()
    noise = impulse.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.269375 + 0.0024071 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_071_accrual_v71_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=81, w2=213, w3=297, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 213)
    curvature = _rolling_slope(acceleration, 297)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0442 * acceleration + 0.0024072 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_072_accrual_v72_d3(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=88, w2=224, w3=310, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 88)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0518 * pressure.rolling(310, min_periods=max(310//3, 2)).mean() + 0.0024073 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_073_accrual_v73_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=95, w2=235, w3=323, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(95, min_periods=max(95//3, 2)).mean())
    decay = spread.ewm(span=235, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.3125 + 0.0024074 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_074_accrual_v74_d3(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=102, w2=246, w3=336, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(246, min_periods=max(246//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 102)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.326875 + 0.0024075 * anchor
    return base_signal.diff().diff().diff()

def f40_eqd_075_accrual_v75_d3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=109, w2=257, w3=349, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(109, min_periods=max(109//3, 2)).mean(), b.abs().rolling(257, min_periods=max(257//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0746 * _rolling_slope(cover, 109) + 0.0024076 * anchor
    return base_signal.diff().diff().diff()
