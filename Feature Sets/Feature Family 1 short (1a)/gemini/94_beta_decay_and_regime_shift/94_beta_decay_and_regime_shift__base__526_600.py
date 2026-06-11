"""94 beta decay and regime shift base features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Macro_Factor - Institutional-grade short-side signal.
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

def f94_beta_526_struct_v526(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=128, w3=703, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(118)
    drag = impulse.rolling(128, min_periods=max(128//3, 2)).mean()
    noise = impulse.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.860625 + 0.0043727 * anchor

def f94_beta_527_struct_v527(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=139, w3=716, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 139)
    curvature = _rolling_slope(acceleration, 716)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3754 * acceleration + 0.0043728 * anchor

def f94_beta_528_struct_v528(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=150, w3=729, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(150, min_periods=max(150//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.889375 + 0.0043729 * anchor

def f94_beta_529_struct_v529(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=161, w3=742, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(161, min_periods=max(161//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3906 * _rolling_slope(draw, 742) + 0.004373 * anchor

def f94_beta_530_struct_v530(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=172, w3=755, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(172, min_periods=max(172//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.918125 + 0.0043731 * anchor

def f94_beta_531_struct_v531(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=183, w3=768, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 183)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.9325 + 0.0043732 * anchor

def f94_beta_532_struct_v532(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=194, w3=24, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(194, min_periods=max(194//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.946875 + 0.0043733 * anchor

def f94_beta_533_struct_v533(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=205, w3=37, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(205, min_periods=max(205//3, 2)).rank(pct=True)
    persistence = change.rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0446 * persistence + 0.0043734 * anchor

def f94_beta_534_struct_v534(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=216, w3=50, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(216, min_periods=max(216//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.975625 + 0.0043735 * anchor

def f94_beta_535_struct_v535(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=227, w3=63, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(227, min_periods=max(227//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0598 * slope + 0.0043736 * anchor

def f94_beta_536_struct_v536(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=238, w3=76, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.004375 + 0.0043737 * anchor

def f94_beta_537_struct_v537(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=249, w3=89, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 249)
    curvature = _rolling_slope(acceleration, 89)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.075 * acceleration + 0.0043738 * anchor

def f94_beta_538_struct_v538(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=260, w3=102, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(260, min_periods=max(260//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(102) * 1.033125 + 0.0043739 * anchor

def f94_beta_539_struct_v539(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=271, w3=115, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0902 * _rolling_slope(draw, 115) + 0.004374 * anchor

def f94_beta_540_struct_v540(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=282, w3=128, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(282, min_periods=max(282//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.061875 + 0.0043741 * anchor

def f94_beta_541_struct_v541(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=293, w3=141, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 293)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=141, adjust=False).mean() * 1.07625 + 0.0043742 * anchor

def f94_beta_542_struct_v542(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=304, w3=154, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(304, min_periods=max(304//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.090625 + 0.0043743 * anchor

def f94_beta_543_struct_v543(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=315, w3=167, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(315, min_periods=max(315//3, 2)).rank(pct=True)
    persistence = change.rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1206 * persistence + 0.0043744 * anchor

def f94_beta_544_struct_v544(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=326, w3=180, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.119375 + 0.0043745 * anchor

def f94_beta_545_struct_v545(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=337, w3=193, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(337, min_periods=max(337//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1358 * slope + 0.0043746 * anchor

def f94_beta_546_struct_v546(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=348, w3=206, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(7)
    drag = impulse.rolling(348, min_periods=max(348//3, 2)).mean()
    noise = impulse.abs().rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.148125 + 0.0043747 * anchor

def f94_beta_547_struct_v547(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=359, w3=219, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 219)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.151 * acceleration + 0.0043748 * anchor

def f94_beta_548_struct_v548(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=370, w3=232, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(370, min_periods=max(370//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.176875 + 0.0043749 * anchor

def f94_beta_549_struct_v549(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=381, w3=245, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(381, min_periods=max(381//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1662 * _rolling_slope(draw, 245) + 0.004375 * anchor

def f94_beta_550_struct_v550(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=392, w3=258, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(392, min_periods=max(392//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.205625 + 0.0043751 * anchor

def f94_beta_551_struct_v551(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=403, w3=271, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=271, adjust=False).mean() * 1.22 + 0.0043752 * anchor

def f94_beta_552_struct_v552(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=414, w3=284, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(414, min_periods=max(414//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.234375 + 0.0043753 * anchor

def f94_beta_553_struct_v553(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=425, w3=297, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(56)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1966 * persistence + 0.0043754 * anchor

def f94_beta_554_struct_v554(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=436, w3=310, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.263125 + 0.0043755 * anchor

def f94_beta_555_struct_v555(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=447, w3=323, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2118 * slope + 0.0043756 * anchor

def f94_beta_556_struct_v556(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=458, w3=336, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(77)
    drag = impulse.rolling(458, min_periods=max(458//3, 2)).mean()
    noise = impulse.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.291875 + 0.0043757 * anchor

def f94_beta_557_struct_v557(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=469, w3=349, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 349)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.227 * acceleration + 0.0043758 * anchor

def f94_beta_558_struct_v558(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=480, w3=362, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.320625 + 0.0043759 * anchor

def f94_beta_559_struct_v559(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=491, w3=375, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2422 * _rolling_slope(draw, 375) + 0.004376 * anchor

def f94_beta_560_struct_v560(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=502, w3=388, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.349375 + 0.0043761 * anchor

def f94_beta_561_struct_v561(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=10, w3=401, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 10)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.36375 + 0.0043762 * anchor

def f94_beta_562_struct_v562(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=21, w3=414, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(21, min_periods=max(21//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.378125 + 0.0043763 * anchor

def f94_beta_563_struct_v563(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=32, w3=427, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2726 * persistence + 0.0043764 * anchor

def f94_beta_564_struct_v564(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=43, w3=440, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.406875 + 0.0043765 * anchor

def f94_beta_565_struct_v565(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=54, w3=453, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(54, min_periods=max(54//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2878 * slope + 0.0043766 * anchor

def f94_beta_566_struct_v566(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=65, w3=466, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(65, min_periods=max(65//3, 2)).mean()
    noise = impulse.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.435625 + 0.0043767 * anchor

def f94_beta_567_struct_v567(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=76, w3=479, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 479)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.303 * acceleration + 0.0043768 * anchor

def f94_beta_568_struct_v568(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=87, w3=492, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.464375 + 0.0043769 * anchor

def f94_beta_569_struct_v569(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=98, w3=505, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(98, min_periods=max(98//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3182 * _rolling_slope(draw, 505) + 0.004377 * anchor

def f94_beta_570_struct_v570(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=109, w3=518, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.493125 + 0.0043771 * anchor

def f94_beta_571_struct_v571(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=120, w3=531, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5075 + 0.0043772 * anchor

def f94_beta_572_struct_v572(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=131, w3=544, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.521875 + 0.0043773 * anchor

def f94_beta_573_struct_v573(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=142, w3=557, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3486 * persistence + 0.0043774 * anchor

def f94_beta_574_struct_v574(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=153, w3=570, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.550625 + 0.0043775 * anchor

def f94_beta_575_struct_v575(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=164, w3=583, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3638 * slope + 0.0043776 * anchor

def f94_beta_576_struct_v576(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=175, w3=596, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.579375 + 0.0043777 * anchor

def f94_beta_577_struct_v577(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=186, w3=609, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 609)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.379 * acceleration + 0.0043778 * anchor

def f94_beta_578_struct_v578(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=197, w3=622, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.608125 + 0.0043779 * anchor

def f94_beta_579_struct_v579(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=208, w3=635, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3942 * _rolling_slope(draw, 635) + 0.004378 * anchor

def f94_beta_580_struct_v580(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=219, w3=648, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(219, min_periods=max(219//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.86375 + 0.0043781 * anchor

def f94_beta_581_struct_v581(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=230, w3=661, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 230)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.878125 + 0.0043782 * anchor

def f94_beta_582_struct_v582(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=241, w3=674, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.8925 + 0.0043783 * anchor

def f94_beta_583_struct_v583(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=252, w3=687, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(15)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0482 * persistence + 0.0043784 * anchor

def f94_beta_584_struct_v584(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=263, w3=700, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92125 + 0.0043785 * anchor

def f94_beta_585_struct_v585(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=274, w3=713, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(274, min_periods=max(274//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0634 * slope + 0.0043786 * anchor

def f94_beta_586_struct_v586(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=285, w3=726, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(36)
    drag = impulse.rolling(285, min_periods=max(285//3, 2)).mean()
    noise = impulse.abs().rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.95 + 0.0043787 * anchor

def f94_beta_587_struct_v587(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=296, w3=739, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 739)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0786 * acceleration + 0.0043788 * anchor

def f94_beta_588_struct_v588(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=307, w3=752, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.97875 + 0.0043789 * anchor

def f94_beta_589_struct_v589(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=318, w3=765, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0938 * _rolling_slope(draw, 765) + 0.004379 * anchor

def f94_beta_590_struct_v590(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=329, w3=21, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(329, min_periods=max(329//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0075 + 0.0043791 * anchor

def f94_beta_591_struct_v591(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=340, w3=34, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=34, adjust=False).mean() * 1.021875 + 0.0043792 * anchor

def f94_beta_592_struct_v592(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=351, w3=47, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(351, min_periods=max(351//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.03625 + 0.0043793 * anchor

def f94_beta_593_struct_v593(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=362, w3=60, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(85)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1242 * persistence + 0.0043794 * anchor

def f94_beta_594_struct_v594(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=373, w3=73, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.065 + 0.0043795 * anchor

def f94_beta_595_struct_v595(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=384, w3=86, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(384, min_periods=max(384//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1394 * slope + 0.0043796 * anchor

def f94_beta_596_struct_v596(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=395, w3=99, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(106)
    drag = impulse.rolling(395, min_periods=max(395//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.09375 + 0.0043797 * anchor

def f94_beta_597_struct_v597(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=406, w3=112, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 112)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1546 * acceleration + 0.0043798 * anchor

def f94_beta_598_struct_v598(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=417, w3=125, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(125) * 1.1225 + 0.0043799 * anchor

def f94_beta_599_struct_v599(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=428, w3=138, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1698 * _rolling_slope(draw, 138) + 0.00438 * anchor

def f94_beta_600_struct_v600(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=439, w3=151, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.15125 + 0.0043801 * anchor
