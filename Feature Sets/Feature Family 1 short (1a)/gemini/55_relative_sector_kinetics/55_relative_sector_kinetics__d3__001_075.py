"""55 relative sector kinetics d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f55_rsw_k_001_rel_v1_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=25, w2=419, w3=39, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 419)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=39, adjust=False).mean() * 1.434375 + 0.0033602 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_002_rel_v2_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=32, w2=430, w3=52, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(430, min_periods=max(430//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.44875 + 0.0033603 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_003_rel_v3_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=39, w2=441, w3=65, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(39)
    rank = change.rolling(441, min_periods=max(441//3, 2)).rank(pct=True)
    persistence = change.rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2186 * persistence + 0.0033604 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_004_rel_v4_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=46, w2=452, w3=78, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(452, min_periods=max(452//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4775 + 0.0033605 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_005_rel_v5_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=53, w2=463, w3=91, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(463, min_periods=max(463//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2338 * slope + 0.0033606 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_006_rel_v6_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=60, w2=474, w3=104, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(60)
    drag = impulse.rolling(474, min_periods=max(474//3, 2)).mean()
    noise = impulse.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.50625 + 0.0033607 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_007_rel_v7_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=67, w2=485, w3=117, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 485)
    curvature = _rolling_slope(acceleration, 117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.249 * acceleration + 0.0033608 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_008_rel_v8_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=74, w2=496, w3=130, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 74)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2566 * pressure.rolling(130, min_periods=max(130//3, 2)).mean() + 0.0033609 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_009_rel_v9_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=81, w2=507, w3=143, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(81, min_periods=max(81//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.549375 + 0.003361 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_010_rel_v10_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=88, w2=15, w3=156, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(15, min_periods=max(15//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 88)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.56375 + 0.0033611 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_011_rel_v11_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=95, w2=26, w3=169, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(95, min_periods=max(95//3, 2)).mean(), b.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2794 * _rolling_slope(cover, 95) + 0.0033612 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_012_rel_v12_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=102, w2=37, w3=182, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.287 * y + 0.713000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 102) - _rolling_slope(basket, 37) + 0.0033613 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_013_rel_v13_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=109, w2=48, w3=195, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.606875 + 0.0033614 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_014_rel_v14_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=116, w2=59, w3=208, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3022 * _rolling_slope(draw, 208) + 0.0033615 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_015_rel_v15_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=123, w2=70, w3=221, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(123) - b.diff(70)
    stress = imbalance.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.8625 + 0.0033616 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_016_rel_v16_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=130, w2=81, w3=234, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.876875 + 0.0033617 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_017_rel_v17_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=137, w2=92, w3=247, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=247, adjust=False).mean() * 0.89125 + 0.0033618 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_018_rel_v18_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=144, w2=103, w3=260, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(103, min_periods=max(103//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.905625 + 0.0033619 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_019_rel_v19_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=151, w2=114, w3=273, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(114, min_periods=max(114//3, 2)).rank(pct=True)
    persistence = change.rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3402 * persistence + 0.003362 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_020_rel_v20_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=158, w2=125, w3=286, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(125, min_periods=max(125//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.934375 + 0.0033621 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_021_rel_v21_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=165, w2=136, w3=299, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3554 * slope + 0.0033622 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_022_rel_v22_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=172, w2=147, w3=312, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.963125 + 0.0033623 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_023_rel_v23_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=179, w2=158, w3=325, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 325)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3706 * acceleration + 0.0033624 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_024_rel_v24_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=186, w2=169, w3=338, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 186)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3782 * pressure.rolling(338, min_periods=max(338//3, 2)).mean() + 0.0033625 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_025_rel_v25_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=193, w2=180, w3=351, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(193, min_periods=max(193//3, 2)).mean())
    decay = spread.ewm(span=180, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.00625 + 0.0033626 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_026_rel_v26_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=200, w2=191, w3=364, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(191, min_periods=max(191//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 200)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.020625 + 0.0033627 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_027_rel_v27_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=207, w2=202, w3=377, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(207, min_periods=max(207//3, 2)).mean(), b.abs().rolling(202, min_periods=max(202//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.401 * _rolling_slope(cover, 207) + 0.0033628 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_028_rel_v28_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=214, w2=213, w3=390, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.4086 * y + 0.591400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 214) - _rolling_slope(basket, 213) + 0.0033629 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_029_rel_v29_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=221, w2=224, w3=403, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(224, min_periods=max(224//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.06375 + 0.003363 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_030_rel_v30_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=228, w2=235, w3=416, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(235, min_periods=max(235//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0474 * _rolling_slope(draw, 416) + 0.0033631 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_031_rel_v31_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=235, w2=246, w3=429, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.0925 + 0.0033632 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_032_rel_v32_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=242, w2=257, w3=442, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(257, min_periods=max(257//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.106875 + 0.0033633 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_033_rel_v33_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=249, w2=268, w3=455, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 268)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.12125 + 0.0033634 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_034_rel_v34_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=5, w2=279, w3=468, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(279, min_periods=max(279//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.135625 + 0.0033635 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_035_rel_v35_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=12, w2=290, w3=481, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(12)
    rank = change.rolling(290, min_periods=max(290//3, 2)).rank(pct=True)
    persistence = change.rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0854 * persistence + 0.0033636 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_036_rel_v36_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=19, w2=301, w3=494, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(301, min_periods=max(301//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.164375 + 0.0033637 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_037_rel_v37_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=26, w2=312, w3=507, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(312, min_periods=max(312//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1006 * slope + 0.0033638 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_038_rel_v38_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=33, w2=323, w3=520, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(33)
    drag = impulse.rolling(323, min_periods=max(323//3, 2)).mean()
    noise = impulse.abs().rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.193125 + 0.0033639 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_039_rel_v39_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=40, w2=334, w3=533, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 40)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 533)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1158 * acceleration + 0.003364 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_040_rel_v40_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=47, w2=345, w3=546, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 47)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1234 * pressure.rolling(546, min_periods=max(546//3, 2)).mean() + 0.0033641 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_041_rel_v41_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=54, w2=356, w3=559, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(54, min_periods=max(54//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.23625 + 0.0033642 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_042_rel_v42_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=61, w2=367, w3=572, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(367, min_periods=max(367//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.250625 + 0.0033643 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_043_rel_v43_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=68, w2=378, w3=585, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(68, min_periods=max(68//3, 2)).mean(), b.abs().rolling(378, min_periods=max(378//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1462 * _rolling_slope(cover, 68) + 0.0033644 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_044_rel_v44_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=75, w2=389, w3=598, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1538 * y + 0.846200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 75) - _rolling_slope(basket, 389) + 0.0033645 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_045_rel_v45_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=82, w2=400, w3=611, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(400, min_periods=max(400//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.29375 + 0.0033646 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_046_rel_v46_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=89, w2=411, w3=624, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(411, min_periods=max(411//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169 * _rolling_slope(draw, 624) + 0.0033647 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_047_rel_v47_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=96, w2=422, w3=637, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(96) - b.diff(126)
    stress = imbalance.rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.3225 + 0.0033648 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_048_rel_v48_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=103, w2=433, w3=650, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(433, min_periods=max(433//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(650, min_periods=max(650//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.336875 + 0.0033649 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_049_rel_v49_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=110, w2=444, w3=663, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 444)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.35125 + 0.003365 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_050_rel_v50_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=117, w2=455, w3=676, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(455, min_periods=max(455//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.365625 + 0.0033651 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_051_rel_v51_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=124, w2=466, w3=689, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(124)
    rank = change.rolling(466, min_periods=max(466//3, 2)).rank(pct=True)
    persistence = change.rolling(689, min_periods=max(689//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.207 * persistence + 0.0033652 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_052_rel_v52_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=131, w2=477, w3=702, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(477, min_periods=max(477//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.394375 + 0.0033653 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_053_rel_v53_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=138, w2=488, w3=715, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(488, min_periods=max(488//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2222 * slope + 0.0033654 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_054_rel_v54_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=145, w2=499, w3=728, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(499, min_periods=max(499//3, 2)).mean()
    noise = impulse.abs().rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.423125 + 0.0033655 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_055_rel_v55_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=152, w2=510, w3=741, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 510)
    curvature = _rolling_slope(acceleration, 741)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2374 * acceleration + 0.0033656 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_056_rel_v56_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=159, w2=18, w3=754, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 159)
    pressure = rel_log.diff(18)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.245 * pressure.rolling(754, min_periods=max(754//3, 2)).mean() + 0.0033657 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_057_rel_v57_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=166, w2=29, w3=767, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(166, min_periods=max(166//3, 2)).mean())
    decay = spread.ewm(span=29, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.46625 + 0.0033658 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_058_rel_v58_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=173, w2=40, w3=23, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(40, min_periods=max(40//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 173)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.480625 + 0.0033659 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_059_rel_v59_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=180, w2=51, w3=36, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(180, min_periods=max(180//3, 2)).mean(), b.abs().rolling(51, min_periods=max(51//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(36) + 0.2678 * _rolling_slope(cover, 180) + 0.003366 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_060_rel_v60_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=187, w2=62, w3=49, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2754 * y + 0.724600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 187) - _rolling_slope(basket, 62) + 0.0033661 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_061_rel_v61_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=194, w2=73, w3=62, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(73, min_periods=max(73//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(62) * 1.52375 + 0.0033662 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_062_rel_v62_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=201, w2=84, w3=75, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(84, min_periods=max(84//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2906 * _rolling_slope(draw, 75) + 0.0033663 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_063_rel_v63_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=208, w2=95, w3=88, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(95)
    stress = imbalance.rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.5525 + 0.0033664 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_064_rel_v64_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=215, w2=106, w3=101, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 215)
    baseline = trend.rolling(106, min_periods=max(106//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(101, min_periods=max(101//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.566875 + 0.0033665 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_065_rel_v65_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=222, w2=117, w3=114, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=114, adjust=False).mean() * 1.58125 + 0.0033666 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_066_rel_v66_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=229, w2=128, w3=127, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(128, min_periods=max(128//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.595625 + 0.0033667 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_067_rel_v67_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=236, w2=139, w3=140, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(139, min_periods=max(139//3, 2)).rank(pct=True)
    persistence = change.rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3286 * persistence + 0.0033668 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_068_rel_v68_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=243, w2=150, w3=153, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(150, min_periods=max(150//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85125 + 0.0033669 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_069_rel_v69_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=250, w2=161, w3=166, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3438 * slope + 0.003367 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_070_rel_v70_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=6, w2=172, w3=179, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(6)
    drag = impulse.rolling(172, min_periods=max(172//3, 2)).mean()
    noise = impulse.abs().rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.88 + 0.0033671 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_071_rel_v71_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=13, w2=183, w3=192, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 13)
    acceleration = _rolling_slope(velocity, 183)
    curvature = _rolling_slope(acceleration, 192)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.359 * acceleration + 0.0033672 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_072_rel_v72_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=20, w2=194, w3=205, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 20)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3666 * pressure.rolling(205, min_periods=max(205//3, 2)).mean() + 0.0033673 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_073_rel_v73_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=27, w2=205, w3=218, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(27, min_periods=max(27//3, 2)).mean())
    decay = spread.ewm(span=205, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.923125 + 0.0033674 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_074_rel_v74_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=34, w2=216, w3=231, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(216, min_periods=max(216//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 34)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.9375 + 0.0033675 * anchor
    return base_signal.diff().diff().diff()

def f55_rsw_k_075_rel_v75_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=41, w2=227, w3=244, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(41, min_periods=max(41//3, 2)).mean(), b.abs().rolling(227, min_periods=max(227//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3894 * _rolling_slope(cover, 41) + 0.0033676 * anchor
    return base_signal.diff().diff().diff()
