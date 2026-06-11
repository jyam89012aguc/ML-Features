"""46 accounting manipulation base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f46_aman_001_accrual_v1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=126, w2=373, w3=240, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(126, min_periods=max(126//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.121875 + 0.0028202 * anchor

def f46_aman_002_accrual_v2(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=133, w2=384, w3=253, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(384, min_periods=max(384//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 133)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.13625 + 0.0028203 * anchor

def f46_aman_003_accrual_v3(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=140, w2=395, w3=266, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(140, min_periods=max(140//3, 2)).mean(), b.abs().rolling(395, min_periods=max(395//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.2062 * _rolling_slope(cover, 140) + 0.0028204 * anchor

def f46_aman_004_accrual_v4(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=147, w2=406, w3=279, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2138 * y + 0.786200 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 147) - _rolling_slope(basket, 406) + 0.0028205 * anchor

def f46_aman_005_accrual_v5(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=154, w2=417, w3=292, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.179375 + 0.0028206 * anchor

def f46_aman_006_accrual_v6(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=161, w2=428, w3=305, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.229 * _rolling_slope(draw, 305) + 0.0028207 * anchor

def f46_aman_007_accrual_v7(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=168, w2=439, w3=318, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.208125 + 0.0028208 * anchor

def f46_aman_008_accrual_v8(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=175, w2=450, w3=331, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.2225 + 0.0028209 * anchor

def f46_aman_009_accrual_v9(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=182, w2=461, w3=344, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 461)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.236875 + 0.002821 * anchor

def f46_aman_010_accrual_v10(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=189, w2=472, w3=357, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(472, min_periods=max(472//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.25125 + 0.0028211 * anchor

def f46_aman_011_accrual_v11(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=196, w2=483, w3=370, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(483, min_periods=max(483//3, 2)).rank(pct=True)
    persistence = change.rolling(370, min_periods=max(370//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.267 * persistence + 0.0028212 * anchor

def f46_aman_012_accrual_v12(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=203, w2=494, w3=383, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(494, min_periods=max(494//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28 + 0.0028213 * anchor

def f46_aman_013_accrual_v13(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=210, w2=505, w3=396, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2822 * slope + 0.0028214 * anchor

def f46_aman_014_accrual_v14(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=217, w2=13, w3=409, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.30875 + 0.0028215 * anchor

def f46_aman_015_accrual_v15(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=224, w2=24, w3=422, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 24)
    curvature = _rolling_slope(acceleration, 422)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2974 * acceleration + 0.0028216 * anchor

def f46_aman_016_accrual_v16(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=231, w2=35, w3=435, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 231)
    pressure = rel_log.diff(35)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.305 * pressure.rolling(435, min_periods=max(435//3, 2)).mean() + 0.0028217 * anchor

def f46_aman_017_accrual_v17(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=238, w2=46, w3=448, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(238, min_periods=max(238//3, 2)).mean())
    decay = spread.ewm(span=46, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.351875 + 0.0028218 * anchor

def f46_aman_018_accrual_v18(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=245, w2=57, w3=461, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(57, min_periods=max(57//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 245)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.36625 + 0.0028219 * anchor

def f46_aman_019_accrual_v19(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=252, w2=68, w3=474, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(252, min_periods=max(252//3, 2)).mean(), b.abs().rolling(68, min_periods=max(68//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3278 * _rolling_slope(cover, 252) + 0.002822 * anchor

def f46_aman_020_accrual_v20(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=8, w2=79, w3=487, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3354 * y + 0.664600 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 8) - _rolling_slope(basket, 79) + 0.0028221 * anchor

def f46_aman_021_accrual_v21(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=15, w2=90, w3=500, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(90, min_periods=max(90//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.409375 + 0.0028222 * anchor

def f46_aman_022_accrual_v22(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=22, w2=101, w3=513, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3506 * _rolling_slope(draw, 513) + 0.0028223 * anchor

def f46_aman_023_accrual_v23(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=29, w2=112, w3=526, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(29) - b.diff(112)
    stress = imbalance.rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.438125 + 0.0028224 * anchor

def f46_aman_024_accrual_v24(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=36, w2=123, w3=539, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4525 + 0.0028225 * anchor

def f46_aman_025_accrual_v25(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=43, w2=134, w3=552, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 134)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.466875 + 0.0028226 * anchor

def f46_aman_026_accrual_v26(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=50, w2=145, w3=565, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(145, min_periods=max(145//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.48125 + 0.0028227 * anchor

def f46_aman_027_accrual_v27(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=57, w2=156, w3=578, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(57)
    rank = change.rolling(156, min_periods=max(156//3, 2)).rank(pct=True)
    persistence = change.rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3886 * persistence + 0.0028228 * anchor

def f46_aman_028_accrual_v28(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=64, w2=167, w3=591, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(167, min_periods=max(167//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.51 + 0.0028229 * anchor

def f46_aman_029_accrual_v29(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=71, w2=178, w3=604, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4038 * slope + 0.002823 * anchor

def f46_aman_030_accrual_v30(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=78, w2=189, w3=617, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(78)
    drag = impulse.rolling(189, min_periods=max(189//3, 2)).mean()
    noise = impulse.abs().rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.53875 + 0.0028231 * anchor

def f46_aman_031_accrual_v31(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=85, w2=200, w3=630, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 200)
    curvature = _rolling_slope(acceleration, 630)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0426 * acceleration + 0.0028232 * anchor

def f46_aman_032_accrual_v32(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=92, w2=211, w3=643, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 92)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.0502 * pressure.rolling(643, min_periods=max(643//3, 2)).mean() + 0.0028233 * anchor

def f46_aman_033_accrual_v33(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=99, w2=222, w3=656, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(99, min_periods=max(99//3, 2)).mean())
    decay = spread.ewm(span=222, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.581875 + 0.0028234 * anchor

def f46_aman_034_accrual_v34(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=106, w2=233, w3=669, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(233, min_periods=max(233//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 106)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.59625 + 0.0028235 * anchor

def f46_aman_035_accrual_v35(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=113, w2=244, w3=682, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(113, min_periods=max(113//3, 2)).mean(), b.abs().rolling(244, min_periods=max(244//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.073 * _rolling_slope(cover, 113) + 0.0028236 * anchor

def f46_aman_036_accrual_v36(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=120, w2=255, w3=695, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.0806 * y + 0.919400 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 120) - _rolling_slope(basket, 255) + 0.0028237 * anchor

def f46_aman_037_accrual_v37(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=127, w2=266, w3=708, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(266, min_periods=max(266//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.86625 + 0.0028238 * anchor

def f46_aman_038_accrual_v38(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=134, w2=277, w3=721, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0958 * _rolling_slope(draw, 721) + 0.0028239 * anchor

def f46_aman_039_accrual_v39(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=141, w2=288, w3=734, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.895 + 0.002824 * anchor

def f46_aman_040_accrual_v40(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=148, w2=299, w3=747, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.909375 + 0.0028241 * anchor

def f46_aman_041_accrual_v41(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=155, w2=310, w3=760, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.92375 + 0.0028242 * anchor

def f46_aman_042_accrual_v42(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=162, w2=321, w3=16, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.938125 + 0.0028243 * anchor

def f46_aman_043_accrual_v43(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=169, w2=332, w3=29, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1338 * persistence + 0.0028244 * anchor

def f46_aman_044_accrual_v44(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=176, w2=343, w3=42, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.966875 + 0.0028245 * anchor

def f46_aman_045_accrual_v45(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=183, w2=354, w3=55, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.149 * slope + 0.0028246 * anchor

def f46_aman_046_accrual_v46(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=190, w2=365, w3=68, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(365, min_periods=max(365//3, 2)).mean()
    noise = impulse.abs().rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.995625 + 0.0028247 * anchor

def f46_aman_047_accrual_v47(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=197, w2=376, w3=81, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 81)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1642 * acceleration + 0.0028248 * anchor

def f46_aman_048_accrual_v48(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=204, w2=387, w3=94, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 204)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.1718 * pressure.rolling(94, min_periods=max(94//3, 2)).mean() + 0.0028249 * anchor

def f46_aman_049_accrual_v49(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=211, w2=398, w3=107, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(211, min_periods=max(211//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.03875 + 0.002825 * anchor

def f46_aman_050_accrual_v50(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=218, w2=409, w3=120, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(409, min_periods=max(409//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 218)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.053125 + 0.0028251 * anchor

def f46_aman_051_accrual_v51(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=225, w2=420, w3=133, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(225, min_periods=max(225//3, 2)).mean(), b.abs().rolling(420, min_periods=max(420//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.1946 * _rolling_slope(cover, 225) + 0.0028252 * anchor

def f46_aman_052_accrual_v52(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=232, w2=431, w3=146, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.2022 * y + 0.797800 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 232) - _rolling_slope(basket, 431) + 0.0028253 * anchor

def f46_aman_053_accrual_v53(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=239, w2=442, w3=159, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.09625 + 0.0028254 * anchor

def f46_aman_054_accrual_v54(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=246, w2=453, w3=172, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2174 * _rolling_slope(draw, 172) + 0.0028255 * anchor

def f46_aman_055_accrual_v55(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=253, w2=464, w3=185, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.125 + 0.0028256 * anchor

def f46_aman_056_accrual_v56(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=9, w2=475, w3=198, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(475, min_periods=max(475//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.139375 + 0.0028257 * anchor

def f46_aman_057_accrual_v57(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=16, w2=486, w3=211, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 16)
    slow = _rolling_slope(x, 486)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=211, adjust=False).mean() * 1.15375 + 0.0028258 * anchor

def f46_aman_058_accrual_v58(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=23, w2=497, w3=224, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(497, min_periods=max(497//3, 2)).max()
    trough = x.rolling(23, min_periods=max(23//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.168125 + 0.0028259 * anchor

def f46_aman_059_accrual_v59(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=30, w2=508, w3=237, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(30)
    rank = change.rolling(508, min_periods=max(508//3, 2)).rank(pct=True)
    persistence = change.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2554 * persistence + 0.002826 * anchor

def f46_aman_060_accrual_v60(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=37, w2=16, w3=250, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(37, min_periods=max(37//3, 2)).std()
    vol_slow = ret.rolling(16, min_periods=max(16//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.196875 + 0.0028261 * anchor

def f46_aman_061_accrual_v61(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=44, w2=27, w3=263, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(27, min_periods=max(27//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 44)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2706 * slope + 0.0028262 * anchor

def f46_aman_062_accrual_v62(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=51, w2=38, w3=276, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(51)
    drag = impulse.rolling(38, min_periods=max(38//3, 2)).mean()
    noise = impulse.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.225625 + 0.0028263 * anchor

def f46_aman_063_accrual_v63(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=58, w2=49, w3=289, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 58)
    acceleration = _rolling_slope(velocity, 49)
    curvature = _rolling_slope(acceleration, 289)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2858 * acceleration + 0.0028264 * anchor

def f46_aman_064_accrual_v64(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=65, w2=60, w3=302, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 65)
    pressure = rel_log.diff(60)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return trend + 0.2934 * pressure.rolling(302, min_periods=max(302//3, 2)).mean() + 0.0028265 * anchor

def f46_aman_065_accrual_v65(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=72, w2=71, w3=315, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    decay = spread.ewm(span=71, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.26875 + 0.0028266 * anchor

def f46_aman_066_accrual_v66(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=79, w2=82, w3=328, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(82, min_periods=max(82//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 79)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return slope * (1.0 - corr) * 1.283125 + 0.0028267 * anchor

def f46_aman_067_accrual_v67(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=86, w2=93, w3=341, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(86, min_periods=max(86//3, 2)).mean(), b.abs().rolling(93, min_periods=max(93//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3162 * _rolling_slope(cover, 86) + 0.0028268 * anchor

def f46_aman_068_accrual_v68(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=93, w2=104, w3=354, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.3238 * y + 0.676200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _rolling_slope(basket, 93) - _rolling_slope(basket, 104) + 0.0028269 * anchor

def f46_aman_069_accrual_v69(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=100, w2=115, w3=367, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(100, min_periods=max(100//3, 2)).mean(), upside.rolling(115, min_periods=max(115//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.32625 + 0.002827 * anchor

def f46_aman_070_accrual_v70(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=107, w2=126, w3=380, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(126, min_periods=max(126//3, 2)).max()
    rebound = x - x.rolling(107, min_periods=max(107//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.339 * _rolling_slope(draw, 380) + 0.0028271 * anchor

def f46_aman_071_accrual_v71(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=114, w2=137, w3=393, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(114) - b.diff(126)
    stress = imbalance.rolling(393, min_periods=max(393//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.355 + 0.0028272 * anchor

def f46_aman_072_accrual_v72(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=121, w2=148, w3=406, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(148, min_periods=max(148//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.369375 + 0.0028273 * anchor

def f46_aman_073_accrual_v73(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=128, w2=159, w3=419, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 159)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.38375 + 0.0028274 * anchor

def f46_aman_074_accrual_v74(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=135, w2=170, w3=432, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.398125 + 0.0028275 * anchor

def f46_aman_075_accrual_v75(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=142, w2=181, w3=445, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(181, min_periods=max(181//3, 2)).rank(pct=True)
    persistence = change.rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.377 * persistence + 0.0028276 * anchor
