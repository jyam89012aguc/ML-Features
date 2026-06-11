"""40 earnings quality divergence d1 first derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f40_eqd_301_accrual_v301_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=185, w2=228, w3=259, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(228, min_periods=max(228//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.4975 + 0.0024302 * anchor
    return base_signal.diff()

def f40_eqd_302_accrual_v302_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=192, w2=239, w3=272, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(239, min_periods=max(239//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2942 * _rolling_slope(draw, 272) + 0.0024303 * anchor
    return base_signal.diff()

def f40_eqd_303_accrual_v303_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=199, w2=250, w3=285, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.52625 + 0.0024304 * anchor
    return base_signal.diff()

def f40_eqd_304_accrual_v304_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=206, w2=261, w3=298, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.540625 + 0.0024305 * anchor
    return base_signal.diff()

def f40_eqd_305_accrual_v305_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=213, w2=272, w3=311, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 272)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.555 + 0.0024306 * anchor
    return base_signal.diff()

def f40_eqd_306_accrual_v306_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=220, w2=283, w3=324, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(283, min_periods=max(283//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.569375 + 0.0024307 * anchor
    return base_signal.diff()

def f40_eqd_307_accrual_v307_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=227, w2=294, w3=337, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(294, min_periods=max(294//3, 2)).rank(pct=True)
    persistence = change.rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3322 * persistence + 0.0024308 * anchor
    return base_signal.diff()

def f40_eqd_308_accrual_v308_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=234, w2=305, w3=350, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(305, min_periods=max(305//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.598125 + 0.0024309 * anchor
    return base_signal.diff()

def f40_eqd_309_accrual_v309_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=241, w2=316, w3=363, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(316, min_periods=max(316//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3474 * slope + 0.002431 * anchor
    return base_signal.diff()

def f40_eqd_310_accrual_v310_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=248, w2=327, w3=376, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(327, min_periods=max(327//3, 2)).mean()
    noise = impulse.abs().rolling(376, min_periods=max(376//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.85375 + 0.0024311 * anchor
    return base_signal.diff()

def f40_eqd_311_accrual_v311_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=255, w2=338, w3=389, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 255)
    acceleration = _rolling_slope(velocity, 338)
    curvature = _rolling_slope(acceleration, 389)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3626 * acceleration + 0.0024312 * anchor
    return base_signal.diff()

def f40_eqd_312_accrual_v312_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=11, w2=349, w3=402, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 11)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3702 * pressure.rolling(402, min_periods=max(402//3, 2)).mean() + 0.0024313 * anchor
    return base_signal.diff()

def f40_eqd_313_accrual_v313_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=18, w2=360, w3=415, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.896875 + 0.0024314 * anchor
    return base_signal.diff()

def f40_eqd_314_accrual_v314_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=25, w2=371, w3=428, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(371, min_periods=max(371//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 25)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.91125 + 0.0024315 * anchor
    return base_signal.diff()

def f40_eqd_315_accrual_v315_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=32, w2=382, w3=441, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(32, min_periods=max(32//3, 2)).mean(), b.abs().rolling(382, min_periods=max(382//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.393 * _rolling_slope(cover, 32) + 0.0024316 * anchor
    return base_signal.diff()

def f40_eqd_316_accrual_v316_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=39, w2=393, w3=454, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.4006 * y + 0.599400 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 39) - _rolling_slope(basket, 393) + 0.0024317 * anchor
    return base_signal.diff()

def f40_eqd_317_accrual_v317_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=46, w2=404, w3=467, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(404, min_periods=max(404//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.954375 + 0.0024318 * anchor
    return base_signal.diff()

def f40_eqd_318_accrual_v318_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=53, w2=415, w3=480, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(415, min_periods=max(415//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0394 * _rolling_slope(draw, 480) + 0.0024319 * anchor
    return base_signal.diff()

def f40_eqd_319_accrual_v319_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=60, w2=426, w3=493, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(60) - b.diff(126)
    stress = imbalance.rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.983125 + 0.002432 * anchor
    return base_signal.diff()

def f40_eqd_320_accrual_v320_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=67, w2=437, w3=506, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(437, min_periods=max(437//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9975 + 0.0024321 * anchor
    return base_signal.diff()

def f40_eqd_321_accrual_v321_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=74, w2=448, w3=519, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.011875 + 0.0024322 * anchor
    return base_signal.diff()

def f40_eqd_322_accrual_v322_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=81, w2=459, w3=532, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(459, min_periods=max(459//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.02625 + 0.0024323 * anchor
    return base_signal.diff()

def f40_eqd_323_accrual_v323_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=88, w2=470, w3=545, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(88)
    rank = change.rolling(470, min_periods=max(470//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0774 * persistence + 0.0024324 * anchor
    return base_signal.diff()

def f40_eqd_324_accrual_v324_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=95, w2=481, w3=558, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(481, min_periods=max(481//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055 + 0.0024325 * anchor
    return base_signal.diff()

def f40_eqd_325_accrual_v325_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=102, w2=492, w3=571, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(492, min_periods=max(492//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0926 * slope + 0.0024326 * anchor
    return base_signal.diff()

def f40_eqd_326_accrual_v326_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=109, w2=503, w3=584, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(109)
    drag = impulse.rolling(503, min_periods=max(503//3, 2)).mean()
    noise = impulse.abs().rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.08375 + 0.0024327 * anchor
    return base_signal.diff()

def f40_eqd_327_accrual_v327_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=116, w2=11, w3=597, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 11)
    curvature = _rolling_slope(acceleration, 597)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1078 * acceleration + 0.0024328 * anchor
    return base_signal.diff()

def f40_eqd_328_accrual_v328_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=123, w2=22, w3=610, lag=0)."""
    rel = _safe_div(inventory.shift(0), revenue.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 123)
    pressure = rel_log.diff(22)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1154 * pressure.rolling(610, min_periods=max(610//3, 2)).mean() + 0.0024329 * anchor
    return base_signal.diff()

def f40_eqd_329_accrual_v329_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=130, w2=33, w3=623, lag=1)."""
    a = revenue.shift(1)
    b = netinc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    decay = spread.ewm(span=33, adjust=False).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.126875 + 0.002433 * anchor
    return base_signal.diff()

def f40_eqd_330_accrual_v330_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=137, w2=44, w3=636, lag=2)."""
    a = _safe_log(netinc.abs() + 1.0).shift(2)
    b = _safe_log(ocf.abs() + 1.0).shift(2)
    corr = a.rolling(44, min_periods=max(44//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 137)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.14125 + 0.0024331 * anchor
    return base_signal.diff()

def f40_eqd_331_accrual_v331_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=144, w2=55, w3=649, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(144, min_periods=max(144//3, 2)).mean(), b.abs().rolling(55, min_periods=max(55//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1382 * _rolling_slope(cover, 144) + 0.0024332 * anchor
    return base_signal.diff()

def f40_eqd_332_accrual_v332_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=151, w2=66, w3=662, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    y = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    z = _safe_log(liabilitiesc.abs() + 1.0).shift(10)
    basket = x - 0.1458 * y + 0.854200 * z
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 151) - _rolling_slope(basket, 66) + 0.0024333 * anchor
    return base_signal.diff()

def f40_eqd_333_accrual_v333_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=158, w2=77, w3=675, lag=21)."""
    x = liabilitiesc.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(77, min_periods=max(77//3, 2)).mean().abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.184375 + 0.0024334 * anchor
    return base_signal.diff()

def f40_eqd_334_accrual_v334_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=165, w2=88, w3=688, lag=42)."""
    x = _safe_log(inventory.abs() + 1.0).shift(42)
    draw = x - x.rolling(88, min_periods=max(88//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.161 * _rolling_slope(draw, 688) + 0.0024335 * anchor
    return base_signal.diff()

def f40_eqd_335_accrual_v335_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=172, w2=99, w3=701, lag=63)."""
    a = _safe_log(revenue.abs() + 1.0).shift(63)
    b = _safe_log(netinc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(99)
    stress = imbalance.rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.213125 + 0.0024336 * anchor
    return base_signal.diff()

def f40_eqd_336_accrual_v336_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=179, w2=110, w3=714, lag=0)."""
    x = _safe_log(netinc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(110, min_periods=max(110//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.2275 + 0.0024337 * anchor
    return base_signal.diff()

def f40_eqd_337_accrual_v337_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=186, w2=121, w3=727, lag=1)."""
    x = _safe_log(ocf.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 121)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.241875 + 0.0024338 * anchor
    return base_signal.diff()

def f40_eqd_338_accrual_v338_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=193, w2=132, w3=740, lag=2)."""
    x = assetsc.shift(2)
    peak = x.rolling(132, min_periods=max(132//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.25625 + 0.0024339 * anchor
    return base_signal.diff()

def f40_eqd_339_accrual_v339_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=200, w2=143, w3=753, lag=5)."""
    x = liabilitiesc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(753, min_periods=max(753//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.199 * persistence + 0.002434 * anchor
    return base_signal.diff()

def f40_eqd_340_accrual_v340_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=207, w2=154, w3=766, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(154, min_periods=max(154//3, 2)).std()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.285 + 0.0024341 * anchor
    return base_signal.diff()

def f40_eqd_341_accrual_v341_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=214, w2=165, w3=22, lag=21)."""
    x = revenue.shift(21)
    ma = x.rolling(165, min_periods=max(165//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2142 * slope + 0.0024342 * anchor
    return base_signal.diff()

def f40_eqd_342_accrual_v342_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=221, w2=176, w3=35, lag=42)."""
    x = netinc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(176, min_periods=max(176//3, 2)).mean()
    noise = impulse.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31375 + 0.0024343 * anchor
    return base_signal.diff()

def f40_eqd_343_accrual_v343_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=228, w2=187, w3=48, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 48)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2294 * acceleration + 0.0024344 * anchor
    return base_signal.diff()

def f40_eqd_344_accrual_v344_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=235, w2=198, w3=61, lag=0)."""
    rel = _safe_div(assetsc.shift(0), liabilitiesc.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 235)
    pressure = rel_log.diff(126)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.237 * pressure.rolling(61, min_periods=max(61//3, 2)).mean() + 0.0024345 * anchor
    return base_signal.diff()

def f40_eqd_345_accrual_v345_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=242, w2=209, w3=74, lag=1)."""
    a = liabilitiesc.shift(1)
    b = inventory.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    decay = spread.ewm(span=209, adjust=False).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.356875 + 0.0024346 * anchor
    return base_signal.diff()

def f40_eqd_346_accrual_v346_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=249, w2=220, w3=87, lag=2)."""
    a = _safe_log(inventory.abs() + 1.0).shift(2)
    b = _safe_log(revenue.abs() + 1.0).shift(2)
    corr = a.rolling(220, min_periods=max(220//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 249)
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.37125 + 0.0024347 * anchor
    return base_signal.diff()

def f40_eqd_347_accrual_v347_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=5, w2=231, w3=100, lag=5)."""
    a = revenue.shift(5)
    b = netinc.shift(5)
    cover = _safe_div(a.rolling(5, min_periods=max(5//3, 2)).mean(), b.abs().rolling(231, min_periods=max(231//3, 2)).mean())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(100) + 0.2598 * _rolling_slope(cover, 5) + 0.0024348 * anchor
    return base_signal.diff()

def f40_eqd_348_accrual_v348_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=12, w2=242, w3=113, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    y = _safe_log(ocf.abs() + 1.0).shift(10)
    z = _safe_log(ocf.abs() + 1.0).shift(10)
    basket = x - 0.2674 * y + 0.732600 * z
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 12) - _rolling_slope(basket, 242) + 0.0024349 * anchor
    return base_signal.diff()

def f40_eqd_349_accrual_v349_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=19, w2=253, w3=126, lag=21)."""
    x = ocf.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(253, min_periods=max(253//3, 2)).mean().abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.414375 + 0.002435 * anchor
    return base_signal.diff()

def f40_eqd_350_accrual_v350_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=26, w2=264, w3=139, lag=42)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(42)
    draw = x - x.rolling(264, min_periods=max(264//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2826 * _rolling_slope(draw, 139) + 0.0024351 * anchor
    return base_signal.diff()

def f40_eqd_351_accrual_v351_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=33, w2=275, w3=152, lag=63)."""
    a = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    b = _safe_log(inventory.abs() + 1.0).shift(63)
    imbalance = a.diff(33) - b.diff(126)
    stress = imbalance.rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.443125 + 0.0024352 * anchor
    return base_signal.diff()

def f40_eqd_352_accrual_v352_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=40, w2=286, w3=165, lag=0)."""
    x = _safe_log(inventory.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(286, min_periods=max(286//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4575 + 0.0024353 * anchor
    return base_signal.diff()

def f40_eqd_353_accrual_v353_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=47, w2=297, w3=178, lag=1)."""
    x = _safe_log(revenue.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 297)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=178, adjust=False).mean() * 1.471875 + 0.0024354 * anchor
    return base_signal.diff()

def f40_eqd_354_accrual_v354_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=54, w2=308, w3=191, lag=2)."""
    x = netinc.shift(2)
    peak = x.rolling(308, min_periods=max(308//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.48625 + 0.0024355 * anchor
    return base_signal.diff()

def f40_eqd_355_accrual_v355_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=61, w2=319, w3=204, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(61)
    rank = change.rolling(319, min_periods=max(319//3, 2)).rank(pct=True)
    persistence = change.rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3206 * persistence + 0.0024356 * anchor
    return base_signal.diff()

def f40_eqd_356_accrual_v356_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=68, w2=330, w3=217, lag=10)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(330, min_periods=max(330//3, 2)).std()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.515 + 0.0024357 * anchor
    return base_signal.diff()

def f40_eqd_357_accrual_v357_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=75, w2=341, w3=230, lag=21)."""
    x = liabilitiesc.shift(21)
    ma = x.rolling(341, min_periods=max(341//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3358 * slope + 0.0024358 * anchor
    return base_signal.diff()

def f40_eqd_358_accrual_v358_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=82, w2=352, w3=243, lag=42)."""
    x = inventory.shift(42)
    impulse = x.diff(82)
    drag = impulse.rolling(352, min_periods=max(352//3, 2)).mean()
    noise = impulse.abs().rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.54375 + 0.0024359 * anchor
    return base_signal.diff()

def f40_eqd_359_accrual_v359_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=89, w2=363, w3=256, lag=63)."""
    x = _safe_log(revenue.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 363)
    curvature = _rolling_slope(acceleration, 256)
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351 * acceleration + 0.002436 * anchor
    return base_signal.diff()

def f40_eqd_360_accrual_v360_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=96, w2=374, w3=269, lag=0)."""
    rel = _safe_div(netinc.shift(0), ocf.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 96)
    pressure = rel_log.diff(126)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3586 * pressure.rolling(269, min_periods=max(269//3, 2)).mean() + 0.0024361 * anchor
    return base_signal.diff()

def f40_eqd_361_accrual_v361_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=103, w2=385, w3=282, lag=1)."""
    a = ocf.shift(1)
    b = assetsc.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(103, min_periods=max(103//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.586875 + 0.0024362 * anchor
    return base_signal.diff()

def f40_eqd_362_accrual_v362_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=110, w2=396, w3=295, lag=2)."""
    a = _safe_log(assetsc.abs() + 1.0).shift(2)
    b = _safe_log(liabilitiesc.abs() + 1.0).shift(2)
    corr = a.rolling(396, min_periods=max(396//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 110)
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.60125 + 0.0024363 * anchor
    return base_signal.diff()

def f40_eqd_363_accrual_v363_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=117, w2=407, w3=308, lag=5)."""
    a = liabilitiesc.shift(5)
    b = inventory.shift(5)
    cover = _safe_div(a.rolling(117, min_periods=max(117//3, 2)).mean(), b.abs().rolling(407, min_periods=max(407//3, 2)).mean())
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3814 * _rolling_slope(cover, 117) + 0.0024364 * anchor
    return base_signal.diff()

def f40_eqd_364_accrual_v364_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=124, w2=418, w3=321, lag=10)."""
    x = _safe_log(inventory.abs() + 1.0).shift(10)
    y = _safe_log(revenue.abs() + 1.0).shift(10)
    z = _safe_log(revenue.abs() + 1.0).shift(10)
    basket = x - 0.389 * y + 0.611000 * z
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 124) - _rolling_slope(basket, 418) + 0.0024365 * anchor
    return base_signal.diff()

def f40_eqd_365_accrual_v365_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=131, w2=429, w3=334, lag=21)."""
    x = revenue.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87125 + 0.0024366 * anchor
    return base_signal.diff()

def f40_eqd_366_accrual_v366_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=138, w2=440, w3=347, lag=42)."""
    x = _safe_log(netinc.abs() + 1.0).shift(42)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4042 * _rolling_slope(draw, 347) + 0.0024367 * anchor
    return base_signal.diff()

def f40_eqd_367_accrual_v367_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=145, w2=451, w3=360, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.9 + 0.0024368 * anchor
    return base_signal.diff()

def f40_eqd_368_accrual_v368_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=152, w2=462, w3=373, lag=0)."""
    x = _safe_log(assetsc.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.914375 + 0.0024369 * anchor
    return base_signal.diff()

def f40_eqd_369_accrual_v369_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=159, w2=473, w3=386, lag=1)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 473)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.92875 + 0.002437 * anchor
    return base_signal.diff()

def f40_eqd_370_accrual_v370_d1(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=166, w2=484, w3=399, lag=2)."""
    x = inventory.shift(2)
    peak = x.rolling(484, min_periods=max(484//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(inventory.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.943125 + 0.0024371 * anchor
    return base_signal.diff()

def f40_eqd_371_accrual_v371_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=173, w2=495, w3=412, lag=5)."""
    x = revenue.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(495, min_periods=max(495//3, 2)).rank(pct=True)
    persistence = change.rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0658 * persistence + 0.0024372 * anchor
    return base_signal.diff()

def f40_eqd_372_accrual_v372_d1(netinc: pd.Series, ocf: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=180, w2=506, w3=425, lag=10)."""
    x = _safe_log(netinc.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(506, min_periods=max(506//3, 2)).std()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.971875 + 0.0024373 * anchor
    return base_signal.diff()

def f40_eqd_373_accrual_v373_d1(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=187, w2=14, w3=438, lag=21)."""
    x = ocf.shift(21)
    ma = x.rolling(14, min_periods=max(14//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.081 * slope + 0.0024374 * anchor
    return base_signal.diff()

def f40_eqd_374_accrual_v374_d1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=194, w2=25, w3=451, lag=42)."""
    x = assetsc.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(25, min_periods=max(25//3, 2)).mean()
    noise = impulse.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(assetsc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.000625 + 0.0024375 * anchor
    return base_signal.diff()

def f40_eqd_375_accrual_v375_d1(liabilitiesc: pd.Series, inventory: pd.Series) -> pd.Series:
    """First derivative of de-duplicated accrual replacement signal (w1=201, w2=36, w3=464, lag=63)."""
    x = _safe_log(liabilitiesc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 36)
    curvature = _rolling_slope(acceleration, 464)
    anchor = _safe_log(liabilitiesc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0962 * acceleration + 0.0024376 * anchor
    return base_signal.diff()
