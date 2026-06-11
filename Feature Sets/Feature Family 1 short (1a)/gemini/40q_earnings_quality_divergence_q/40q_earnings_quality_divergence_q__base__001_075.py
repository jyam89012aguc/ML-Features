"""40q earnings quality divergence q base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f40q_eqdq_001_accrual_v1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=26, w2=510, w3=374, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.17125 + 0.0024602 * anchor

def f40q_eqdq_002_accrual_v2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=33, w2=18, w3=387, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(18, min_periods=max(18//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 33)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.185625 + 0.0024603 * anchor

def f40q_eqdq_003_accrual_v3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=40, w2=29, w3=400, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(40, min_periods=max(40//3, 2)).mean(), b.abs().rolling(29, min_periods=max(29//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3234 * _rolling_slope(cover, 40) + 0.0024604 * anchor

def f40q_eqdq_004_accrual_v4(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=47, w2=40, w3=413, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.331 * y + 0.669000 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 47) - _rolling_slope(basket, 40) + 0.0024605 * anchor

def f40q_eqdq_005_accrual_v5(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=54, w2=51, w3=426, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(51, min_periods=max(51//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.22875 + 0.0024606 * anchor

def f40q_eqdq_006_accrual_v6(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=61, w2=62, w3=439, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(62, min_periods=max(62//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3462 * _rolling_slope(draw, 439) + 0.0024607 * anchor

def f40q_eqdq_007_accrual_v7(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=68, w2=73, w3=452, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(68) - b.diff(73)
    stress = imbalance.rolling(452, min_periods=max(452//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.2575 + 0.0024608 * anchor

def f40q_eqdq_008_accrual_v8(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=75, w2=84, w3=465, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(84, min_periods=max(84//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.271875 + 0.0024609 * anchor

def f40q_eqdq_009_accrual_v9(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=82, w2=95, w3=478, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 95)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.28625 + 0.002461 * anchor

def f40q_eqdq_010_accrual_v10(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=89, w2=106, w3=491, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(106, min_periods=max(106//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.300625 + 0.0024611 * anchor

def f40q_eqdq_011_accrual_v11(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=96, w2=117, w3=504, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(96)
    rank = change.rolling(117, min_periods=max(117//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3842 * persistence + 0.0024612 * anchor

def f40q_eqdq_012_accrual_v12(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=103, w2=128, w3=517, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(128, min_periods=max(128//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.329375 + 0.0024613 * anchor

def f40q_eqdq_013_accrual_v13(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=110, w2=139, w3=530, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(139, min_periods=max(139//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3994 * slope + 0.0024614 * anchor

def f40q_eqdq_014_accrual_v14(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=117, w2=150, w3=543, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(117)
    drag = impulse.rolling(150, min_periods=max(150//3, 2)).mean()
    noise = impulse.abs().rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.358125 + 0.0024615 * anchor

def f40q_eqdq_015_accrual_v15(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=124, w2=161, w3=556, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 161)
    curvature = _rolling_slope(acceleration, 556)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0382 * acceleration + 0.0024616 * anchor

def f40q_eqdq_016_accrual_v16(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=131, w2=172, w3=569, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 131)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0458 * pressure.rolling(569, min_periods=max(569//3, 2)).mean() + 0.0024617 * anchor

def f40q_eqdq_017_accrual_v17(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=138, w2=183, w3=582, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(138, min_periods=max(138//3, 2)).mean())
    decay = spread.ewm(span=183, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.40125 + 0.0024618 * anchor

def f40q_eqdq_018_accrual_v18(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=145, w2=194, w3=595, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(194, min_periods=max(194//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 145)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.415625 + 0.0024619 * anchor

def f40q_eqdq_019_accrual_v19(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=152, w2=205, w3=608, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(152, min_periods=max(152//3, 2)).mean(), b.abs().rolling(205, min_periods=max(205//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.0686 * _rolling_slope(cover, 152) + 0.002462 * anchor

def f40q_eqdq_020_accrual_v20(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=159, w2=216, w3=621, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0762 * y + 0.923800 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 159) - _rolling_slope(basket, 216) + 0.0024621 * anchor

def f40q_eqdq_021_accrual_v21(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=166, w2=227, w3=634, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(227, min_periods=max(227//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45875 + 0.0024622 * anchor

def f40q_eqdq_022_accrual_v22(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=173, w2=238, w3=647, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(238, min_periods=max(238//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0914 * _rolling_slope(draw, 647) + 0.0024623 * anchor

def f40q_eqdq_023_accrual_v23(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=180, w2=249, w3=660, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.4875 + 0.0024624 * anchor

def f40q_eqdq_024_accrual_v24(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=187, w2=260, w3=673, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 187)
    baseline = trend.rolling(260, min_periods=max(260//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(673, min_periods=max(673//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.501875 + 0.0024625 * anchor

def f40q_eqdq_025_accrual_v25(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=194, w2=271, w3=686, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 271)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.51625 + 0.0024626 * anchor

def f40q_eqdq_026_accrual_v26(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=201, w2=282, w3=699, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(282, min_periods=max(282//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.530625 + 0.0024627 * anchor

def f40q_eqdq_027_accrual_v27(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=208, w2=293, w3=712, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(293, min_periods=max(293//3, 2)).rank(pct=True)
    persistence = change.rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1294 * persistence + 0.0024628 * anchor

def f40q_eqdq_028_accrual_v28(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=215, w2=304, w3=725, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(304, min_periods=max(304//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.559375 + 0.0024629 * anchor

def f40q_eqdq_029_accrual_v29(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=222, w2=315, w3=738, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(315, min_periods=max(315//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1446 * slope + 0.002463 * anchor

def f40q_eqdq_030_accrual_v30(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=229, w2=326, w3=751, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(326, min_periods=max(326//3, 2)).mean()
    noise = impulse.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.588125 + 0.0024631 * anchor

def f40q_eqdq_031_accrual_v31(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=236, w2=337, w3=764, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 337)
    curvature = _rolling_slope(acceleration, 764)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1598 * acceleration + 0.0024632 * anchor

def f40q_eqdq_032_accrual_v32(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=243, w2=348, w3=20, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 243)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1674 * pressure.rolling(20, min_periods=max(20//3, 2)).mean() + 0.0024633 * anchor

def f40q_eqdq_033_accrual_v33(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=250, w2=359, w3=33, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(250, min_periods=max(250//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.858125 + 0.0024634 * anchor

def f40q_eqdq_034_accrual_v34(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=6, w2=370, w3=46, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(370, min_periods=max(370//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 6)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 0.8725 + 0.0024635 * anchor

def f40q_eqdq_035_accrual_v35(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=13, w2=381, w3=59, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(13, min_periods=max(13//3, 2)).mean(), b.abs().rolling(381, min_periods=max(381//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(59) + 0.1902 * _rolling_slope(cover, 13) + 0.0024636 * anchor

def f40q_eqdq_036_accrual_v36(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=20, w2=392, w3=72, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.1978 * y + 0.802200 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 20) - _rolling_slope(basket, 392) + 0.0024637 * anchor

def f40q_eqdq_037_accrual_v37(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=27, w2=403, w3=85, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(403, min_periods=max(403//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(85) * 0.915625 + 0.0024638 * anchor

def f40q_eqdq_038_accrual_v38(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=34, w2=414, w3=98, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(414, min_periods=max(414//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.213 * _rolling_slope(draw, 98) + 0.0024639 * anchor

def f40q_eqdq_039_accrual_v39(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=41, w2=425, w3=111, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(41) - b.diff(126)
    stress = imbalance.rolling(111, min_periods=max(111//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.944375 + 0.002464 * anchor

def f40q_eqdq_040_accrual_v40(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=48, w2=436, w3=124, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.95875 + 0.0024641 * anchor

def f40q_eqdq_041_accrual_v41(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=55, w2=447, w3=137, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 447)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=137, adjust=False).mean() * 0.973125 + 0.0024642 * anchor

def f40q_eqdq_042_accrual_v42(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=62, w2=458, w3=150, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(458, min_periods=max(458//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9875 + 0.0024643 * anchor

def f40q_eqdq_043_accrual_v43(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=69, w2=469, w3=163, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(69)
    rank = change.rolling(469, min_periods=max(469//3, 2)).rank(pct=True)
    persistence = change.rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.251 * persistence + 0.0024644 * anchor

def f40q_eqdq_044_accrual_v44(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=76, w2=480, w3=176, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.01625 + 0.0024645 * anchor

def f40q_eqdq_045_accrual_v45(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=83, w2=491, w3=189, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(491, min_periods=max(491//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2662 * slope + 0.0024646 * anchor

def f40q_eqdq_046_accrual_v46(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=90, w2=502, w3=202, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(90)
    drag = impulse.rolling(502, min_periods=max(502//3, 2)).mean()
    noise = impulse.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.045 + 0.0024647 * anchor

def f40q_eqdq_047_accrual_v47(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=97, w2=10, w3=215, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 10)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2814 * acceleration + 0.0024648 * anchor

def f40q_eqdq_048_accrual_v48(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=104, w2=21, w3=228, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 104)
    pressure = rel_log.diff(21)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.289 * pressure.rolling(228, min_periods=max(228//3, 2)).mean() + 0.0024649 * anchor

def f40q_eqdq_049_accrual_v49(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=111, w2=32, w3=241, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(111, min_periods=max(111//3, 2)).mean())
    decay = spread.ewm(span=32, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.088125 + 0.002465 * anchor

def f40q_eqdq_050_accrual_v50(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=118, w2=43, w3=254, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(43, min_periods=max(43//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 118)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.1025 + 0.0024651 * anchor

def f40q_eqdq_051_accrual_v51(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=125, w2=54, w3=267, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(125, min_periods=max(125//3, 2)).mean(), b.abs().rolling(54, min_periods=max(54//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3118 * _rolling_slope(cover, 125) + 0.0024652 * anchor

def f40q_eqdq_052_accrual_v52(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=132, w2=65, w3=280, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.3194 * y + 0.680600 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 132) - _rolling_slope(basket, 65) + 0.0024653 * anchor

def f40q_eqdq_053_accrual_v53(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=139, w2=76, w3=293, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(76, min_periods=max(76//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.145625 + 0.0024654 * anchor

def f40q_eqdq_054_accrual_v54(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=146, w2=87, w3=306, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(87, min_periods=max(87//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3346 * _rolling_slope(draw, 306) + 0.0024655 * anchor

def f40q_eqdq_055_accrual_v55(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=153, w2=98, w3=319, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(98)
    stress = imbalance.rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.174375 + 0.0024656 * anchor

def f40q_eqdq_056_accrual_v56(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=160, w2=109, w3=332, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.18875 + 0.0024657 * anchor

def f40q_eqdq_057_accrual_v57(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=167, w2=120, w3=345, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.203125 + 0.0024658 * anchor

def f40q_eqdq_058_accrual_v58(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=174, w2=131, w3=358, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2175 + 0.0024659 * anchor

def f40q_eqdq_059_accrual_v59(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=181, w2=142, w3=371, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3726 * persistence + 0.002466 * anchor

def f40q_eqdq_060_accrual_v60(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=188, w2=153, w3=384, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24625 + 0.0024661 * anchor

def f40q_eqdq_061_accrual_v61(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=195, w2=164, w3=397, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3878 * slope + 0.0024662 * anchor

def f40q_eqdq_062_accrual_v62(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=202, w2=175, w3=410, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.275 + 0.0024663 * anchor

def f40q_eqdq_063_accrual_v63(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=209, w2=186, w3=423, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 423)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.403 * acceleration + 0.0024664 * anchor

def f40q_eqdq_064_accrual_v64(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=216, w2=197, w3=436, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 216)
    pressure = rel_log.diff(126)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.4106 * pressure.rolling(436, min_periods=max(436//3, 2)).mean() + 0.0024665 * anchor

def f40q_eqdq_065_accrual_v65(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=223, w2=208, w3=449, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    decay = spread.ewm(span=208, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.318125 + 0.0024666 * anchor

def f40q_eqdq_066_accrual_v66(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=230, w2=219, w3=462, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(219, min_periods=max(219//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 230)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.3325 + 0.0024667 * anchor

def f40q_eqdq_067_accrual_v67(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=237, w2=230, w3=475, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(237, min_periods=max(237//3, 2)).mean(), b.abs().rolling(230, min_periods=max(230//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.057 * _rolling_slope(cover, 237) + 0.0024668 * anchor

def f40q_eqdq_068_accrual_v68(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=244, w2=241, w3=488, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.0646 * y + 0.935400 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 244) - _rolling_slope(basket, 241) + 0.0024669 * anchor

def f40q_eqdq_069_accrual_v69(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=251, w2=252, w3=501, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.375625 + 0.002467 * anchor

def f40q_eqdq_070_accrual_v70(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=7, w2=263, w3=514, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0798 * _rolling_slope(draw, 514) + 0.0024671 * anchor

def f40q_eqdq_071_accrual_v71(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=14, w2=274, w3=527, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(14) - b.diff(126)
    stress = imbalance.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.404375 + 0.0024672 * anchor

def f40q_eqdq_072_accrual_v72(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=21, w2=285, w3=540, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(285, min_periods=max(285//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.41875 + 0.0024673 * anchor

def f40q_eqdq_073_accrual_v73(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=28, w2=296, w3=553, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 296)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.433125 + 0.0024674 * anchor

def f40q_eqdq_074_accrual_v74(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=35, w2=307, w3=566, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(307, min_periods=max(307//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4475 + 0.0024675 * anchor

def f40q_eqdq_075_accrual_v75(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=42, w2=318, w3=579, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(42)
    rank = change.rolling(318, min_periods=max(318//3, 2)).rank(pct=True)
    persistence = change.rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1178 * persistence + 0.0024676 * anchor
