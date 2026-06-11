"""16 short interest structure base features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Securities_Lending - Institutional-grade short-side signal.
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

def f16_sist_526_struct_v526(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=233, w3=692, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(105)
    drag = impulse.rolling(233, min_periods=max(233//3, 2)).mean()
    noise = impulse.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.06375 + 0.0010127 * anchor

def f16_sist_527_struct_v527(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=244, w3=705, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 244)
    curvature = _rolling_slope(acceleration, 705)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2146 * acceleration + 0.0010128 * anchor

def f16_sist_528_struct_v528(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=255, w3=718, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(255, min_periods=max(255//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0925 + 0.0010129 * anchor

def f16_sist_529_struct_v529(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=266, w3=731, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(266, min_periods=max(266//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2298 * _rolling_slope(draw, 731) + 0.001013 * anchor

def f16_sist_530_struct_v530(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=277, w3=744, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(277, min_periods=max(277//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.12125 + 0.0010131 * anchor

def f16_sist_531_struct_v531(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=288, w3=757, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 288)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.135625 + 0.0010132 * anchor

def f16_sist_532_struct_v532(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=299, w3=770, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(299, min_periods=max(299//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.15 + 0.0010133 * anchor

def f16_sist_533_struct_v533(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=310, w3=26, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(310, min_periods=max(310//3, 2)).rank(pct=True)
    persistence = change.rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2602 * persistence + 0.0010134 * anchor

def f16_sist_534_struct_v534(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=321, w3=39, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(321, min_periods=max(321//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17875 + 0.0010135 * anchor

def f16_sist_535_struct_v535(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=332, w3=52, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(332, min_periods=max(332//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2754 * slope + 0.0010136 * anchor

def f16_sist_536_struct_v536(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=343, w3=65, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(343, min_periods=max(343//3, 2)).mean()
    noise = impulse.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2075 + 0.0010137 * anchor

def f16_sist_537_struct_v537(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=354, w3=78, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 354)
    curvature = _rolling_slope(acceleration, 78)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2906 * acceleration + 0.0010138 * anchor

def f16_sist_538_struct_v538(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=365, w3=91, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(91) * 1.23625 + 0.0010139 * anchor

def f16_sist_539_struct_v539(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=376, w3=104, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(376, min_periods=max(376//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3058 * _rolling_slope(draw, 104) + 0.001014 * anchor

def f16_sist_540_struct_v540(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=387, w3=117, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(387, min_periods=max(387//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.265 + 0.0010141 * anchor

def f16_sist_541_struct_v541(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=398, w3=130, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 398)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=130, adjust=False).mean() * 1.279375 + 0.0010142 * anchor

def f16_sist_542_struct_v542(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=409, w3=143, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(409, min_periods=max(409//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.29375 + 0.0010143 * anchor

def f16_sist_543_struct_v543(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=420, w3=156, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(420, min_periods=max(420//3, 2)).rank(pct=True)
    persistence = change.rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3362 * persistence + 0.0010144 * anchor

def f16_sist_544_struct_v544(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=431, w3=169, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(431, min_periods=max(431//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3225 + 0.0010145 * anchor

def f16_sist_545_struct_v545(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=442, w3=182, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(442, min_periods=max(442//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3514 * slope + 0.0010146 * anchor

def f16_sist_546_struct_v546(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=453, w3=195, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(453, min_periods=max(453//3, 2)).mean()
    noise = impulse.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.35125 + 0.0010147 * anchor

def f16_sist_547_struct_v547(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=464, w3=208, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 252)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 208)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3666 * acceleration + 0.0010148 * anchor

def f16_sist_548_struct_v548(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=475, w3=221, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(475, min_periods=max(475//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.38 + 0.0010149 * anchor

def f16_sist_549_struct_v549(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=486, w3=234, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(486, min_periods=max(486//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3818 * _rolling_slope(draw, 234) + 0.001015 * anchor

def f16_sist_550_struct_v550(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=497, w3=247, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(497, min_periods=max(497//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.40875 + 0.0010151 * anchor

def f16_sist_551_struct_v551(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=508, w3=260, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 508)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=260, adjust=False).mean() * 1.423125 + 0.0010152 * anchor

def f16_sist_552_struct_v552(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=16, w3=273, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(16, min_periods=max(16//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4375 + 0.0010153 * anchor

def f16_sist_553_struct_v553(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=27, w3=286, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(43)
    rank = change.rolling(27, min_periods=max(27//3, 2)).rank(pct=True)
    persistence = change.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0358 * persistence + 0.0010154 * anchor

def f16_sist_554_struct_v554(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=38, w3=299, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(38, min_periods=max(38//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46625 + 0.0010155 * anchor

def f16_sist_555_struct_v555(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=49, w3=312, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.051 * slope + 0.0010156 * anchor

def f16_sist_556_struct_v556(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=60, w3=325, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(64)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.495 + 0.0010157 * anchor

def f16_sist_557_struct_v557(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=71, w3=338, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 338)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0662 * acceleration + 0.0010158 * anchor

def f16_sist_558_struct_v558(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=82, w3=351, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.52375 + 0.0010159 * anchor

def f16_sist_559_struct_v559(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=93, w3=364, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(93, min_periods=max(93//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0814 * _rolling_slope(draw, 364) + 0.001016 * anchor

def f16_sist_560_struct_v560(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=104, w3=377, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.5525 + 0.0010161 * anchor

def f16_sist_561_struct_v561(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=115, w3=390, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 115)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.566875 + 0.0010162 * anchor

def f16_sist_562_struct_v562(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=126, w3=403, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(126, min_periods=max(126//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.58125 + 0.0010163 * anchor

def f16_sist_563_struct_v563(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=137, w3=416, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(113)
    rank = change.rolling(137, min_periods=max(137//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1118 * persistence + 0.0010164 * anchor

def f16_sist_564_struct_v564(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=148, w3=429, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61 + 0.0010165 * anchor

def f16_sist_565_struct_v565(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=159, w3=442, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(159, min_periods=max(159//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.127 * slope + 0.0010166 * anchor

def f16_sist_566_struct_v566(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=170, w3=455, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(170, min_periods=max(170//3, 2)).mean()
    noise = impulse.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.865625 + 0.0010167 * anchor

def f16_sist_567_struct_v567(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=181, w3=468, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 181)
    curvature = _rolling_slope(acceleration, 468)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1422 * acceleration + 0.0010168 * anchor

def f16_sist_568_struct_v568(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=192, w3=481, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.894375 + 0.0010169 * anchor

def f16_sist_569_struct_v569(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=203, w3=494, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(203, min_periods=max(203//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1574 * _rolling_slope(draw, 494) + 0.001017 * anchor

def f16_sist_570_struct_v570(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=214, w3=507, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(214, min_periods=max(214//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.923125 + 0.0010171 * anchor

def f16_sist_571_struct_v571(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=225, w3=520, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 225)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.9375 + 0.0010172 * anchor

def f16_sist_572_struct_v572(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=236, w3=533, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.951875 + 0.0010173 * anchor

def f16_sist_573_struct_v573(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=247, w3=546, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(247, min_periods=max(247//3, 2)).rank(pct=True)
    persistence = change.rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1878 * persistence + 0.0010174 * anchor

def f16_sist_574_struct_v574(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=258, w3=559, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.980625 + 0.0010175 * anchor

def f16_sist_575_struct_v575(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=269, w3=572, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(269, min_periods=max(269//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.203 * slope + 0.0010176 * anchor

def f16_sist_576_struct_v576(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=280, w3=585, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.009375 + 0.0010177 * anchor

def f16_sist_577_struct_v577(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=291, w3=598, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 291)
    curvature = _rolling_slope(acceleration, 598)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2182 * acceleration + 0.0010178 * anchor

def f16_sist_578_struct_v578(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=302, w3=611, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.038125 + 0.0010179 * anchor

def f16_sist_579_struct_v579(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=313, w3=624, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2334 * _rolling_slope(draw, 624) + 0.001018 * anchor

def f16_sist_580_struct_v580(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=324, w3=637, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(324, min_periods=max(324//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.066875 + 0.0010181 * anchor

def f16_sist_581_struct_v581(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=335, w3=650, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 335)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.08125 + 0.0010182 * anchor

def f16_sist_582_struct_v582(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=346, w3=663, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(346, min_periods=max(346//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.095625 + 0.0010183 * anchor

def f16_sist_583_struct_v583(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=357, w3=676, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(357, min_periods=max(357//3, 2)).rank(pct=True)
    persistence = change.rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2638 * persistence + 0.0010184 * anchor

def f16_sist_584_struct_v584(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=368, w3=689, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(368, min_periods=max(368//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.124375 + 0.0010185 * anchor

def f16_sist_585_struct_v585(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=379, w3=702, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(379, min_periods=max(379//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.279 * slope + 0.0010186 * anchor

def f16_sist_586_struct_v586(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=390, w3=715, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(23)
    drag = impulse.rolling(390, min_periods=max(390//3, 2)).mean()
    noise = impulse.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.153125 + 0.0010187 * anchor

def f16_sist_587_struct_v587(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=401, w3=728, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 401)
    curvature = _rolling_slope(acceleration, 728)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2942 * acceleration + 0.0010188 * anchor

def f16_sist_588_struct_v588(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=412, w3=741, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(37, min_periods=max(37//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.181875 + 0.0010189 * anchor

def f16_sist_589_struct_v589(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=423, w3=754, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(44, min_periods=max(44//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3094 * _rolling_slope(draw, 754) + 0.001019 * anchor

def f16_sist_590_struct_v590(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=434, w3=767, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(434, min_periods=max(434//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.210625 + 0.0010191 * anchor

def f16_sist_591_struct_v591(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=445, w3=23, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 445)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=23, adjust=False).mean() * 1.225 + 0.0010192 * anchor

def f16_sist_592_struct_v592(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=456, w3=36, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(456, min_periods=max(456//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.239375 + 0.0010193 * anchor

def f16_sist_593_struct_v593(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=467, w3=49, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(72)
    rank = change.rolling(467, min_periods=max(467//3, 2)).rank(pct=True)
    persistence = change.rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3398 * persistence + 0.0010194 * anchor

def f16_sist_594_struct_v594(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=478, w3=62, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(478, min_periods=max(478//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.268125 + 0.0010195 * anchor

def f16_sist_595_struct_v595(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=489, w3=75, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(489, min_periods=max(489//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.355 * slope + 0.0010196 * anchor

def f16_sist_596_struct_v596(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=500, w3=88, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(93)
    drag = impulse.rolling(500, min_periods=max(500//3, 2)).mean()
    noise = impulse.abs().rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.296875 + 0.0010197 * anchor

def f16_sist_597_struct_v597(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=511, w3=101, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 511)
    curvature = _rolling_slope(acceleration, 101)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3702 * acceleration + 0.0010198 * anchor

def f16_sist_598_struct_v598(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=19, w3=114, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(114) * 1.325625 + 0.0010199 * anchor

def f16_sist_599_struct_v599(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=30, w3=127, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(30, min_periods=max(30//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3854 * _rolling_slope(draw, 127) + 0.00102 * anchor

def f16_sist_600_struct_v600(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=41, w3=140, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(41, min_periods=max(41//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.354375 + 0.0010201 * anchor
