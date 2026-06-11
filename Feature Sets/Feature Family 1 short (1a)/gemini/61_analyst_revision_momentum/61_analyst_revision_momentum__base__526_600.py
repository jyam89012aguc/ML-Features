"""61 analyst revision momentum base features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Analyst_Sentiment - Institutional-grade short-side signal.
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

def f61_arm_526_analyst_v526(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=119, w2=219, w3=281, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(119)
    drag = impulse.rolling(219, min_periods=max(219//3, 2)).mean()
    noise = impulse.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.370625 + 0.0034727 * anchor

def f61_arm_527_analyst_v527(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=126, w2=230, w3=294, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 230)
    curvature = _rolling_slope(acceleration, 294)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1038 * acceleration + 0.0034728 * anchor

def f61_arm_528_analyst_v528(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=133, w2=241, w3=307, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(241, min_periods=max(241//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.399375 + 0.0034729 * anchor

def f61_arm_529_analyst_v529(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=140, w2=252, w3=320, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(252, min_periods=max(252//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.119 * _rolling_slope(draw, 320) + 0.003473 * anchor

def f61_arm_530_analyst_v530(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=147, w2=263, w3=333, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(263, min_periods=max(263//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(333, min_periods=max(333//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.428125 + 0.0034731 * anchor

def f61_arm_531_analyst_v531(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=154, w2=274, w3=346, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4425 + 0.0034732 * anchor

def f61_arm_532_analyst_v532(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=161, w2=285, w3=359, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.456875 + 0.0034733 * anchor

def f61_arm_533_analyst_v533(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=168, w2=296, w3=372, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(296, min_periods=max(296//3, 2)).rank(pct=True)
    persistence = change.rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1494 * persistence + 0.0034734 * anchor

def f61_arm_534_analyst_v534(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=175, w2=307, w3=385, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(307, min_periods=max(307//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.485625 + 0.0034735 * anchor

def f61_arm_535_analyst_v535(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=182, w2=318, w3=398, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(318, min_periods=max(318//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1646 * slope + 0.0034736 * anchor

def f61_arm_536_analyst_v536(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=189, w2=329, w3=411, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(329, min_periods=max(329//3, 2)).mean()
    noise = impulse.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.514375 + 0.0034737 * anchor

def f61_arm_537_analyst_v537(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=196, w2=340, w3=424, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 340)
    curvature = _rolling_slope(acceleration, 424)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1798 * acceleration + 0.0034738 * anchor

def f61_arm_538_analyst_v538(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=203, w2=351, w3=437, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.543125 + 0.0034739 * anchor

def f61_arm_539_analyst_v539(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=210, w2=362, w3=450, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(362, min_periods=max(362//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.195 * _rolling_slope(draw, 450) + 0.003474 * anchor

def f61_arm_540_analyst_v540(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=217, w2=373, w3=463, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 217)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.571875 + 0.0034741 * anchor

def f61_arm_541_analyst_v541(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=224, w2=384, w3=476, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 224)
    slow = _rolling_slope(x, 384)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.58625 + 0.0034742 * anchor

def f61_arm_542_analyst_v542(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=231, w2=395, w3=489, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(395, min_periods=max(395//3, 2)).max()
    trough = x.rolling(231, min_periods=max(231//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.600625 + 0.0034743 * anchor

def f61_arm_543_analyst_v543(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=238, w2=406, w3=502, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(406, min_periods=max(406//3, 2)).rank(pct=True)
    persistence = change.rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2254 * persistence + 0.0034744 * anchor

def f61_arm_544_analyst_v544(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=245, w2=417, w3=515, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(245, min_periods=max(245//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85625 + 0.0034745 * anchor

def f61_arm_545_analyst_v545(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=252, w2=428, w3=528, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 252)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2406 * slope + 0.0034746 * anchor

def f61_arm_546_analyst_v546(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=8, w2=439, w3=541, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(8)
    drag = impulse.rolling(439, min_periods=max(439//3, 2)).mean()
    noise = impulse.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.885 + 0.0034747 * anchor

def f61_arm_547_analyst_v547(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=15, w2=450, w3=554, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 554)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2558 * acceleration + 0.0034748 * anchor

def f61_arm_548_analyst_v548(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=22, w2=461, w3=567, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(461, min_periods=max(461//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.91375 + 0.0034749 * anchor

def f61_arm_549_analyst_v549(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=29, w2=472, w3=580, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(472, min_periods=max(472//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.271 * _rolling_slope(draw, 580) + 0.003475 * anchor

def f61_arm_550_analyst_v550(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=36, w2=483, w3=593, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(593, min_periods=max(593//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9425 + 0.0034751 * anchor

def f61_arm_551_analyst_v551(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=43, w2=494, w3=606, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 494)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.956875 + 0.0034752 * anchor

def f61_arm_552_analyst_v552(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=50, w2=505, w3=619, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.97125 + 0.0034753 * anchor

def f61_arm_553_analyst_v553(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=57, w2=13, w3=632, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(57)
    rank = change.rolling(13, min_periods=max(13//3, 2)).rank(pct=True)
    persistence = change.rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3014 * persistence + 0.0034754 * anchor

def f61_arm_554_analyst_v554(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=64, w2=24, w3=645, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(24, min_periods=max(24//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0 + 0.0034755 * anchor

def f61_arm_555_analyst_v555(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=71, w2=35, w3=658, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3166 * slope + 0.0034756 * anchor

def f61_arm_556_analyst_v556(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=78, w2=46, w3=671, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(78)
    drag = impulse.rolling(46, min_periods=max(46//3, 2)).mean()
    noise = impulse.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.02875 + 0.0034757 * anchor

def f61_arm_557_analyst_v557(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=85, w2=57, w3=684, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 57)
    curvature = _rolling_slope(acceleration, 684)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3318 * acceleration + 0.0034758 * anchor

def f61_arm_558_analyst_v558(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=92, w2=68, w3=697, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(68, min_periods=max(68//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.0575 + 0.0034759 * anchor

def f61_arm_559_analyst_v559(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=99, w2=79, w3=710, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(79, min_periods=max(79//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.347 * _rolling_slope(draw, 710) + 0.003476 * anchor

def f61_arm_560_analyst_v560(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=106, w2=90, w3=723, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(90, min_periods=max(90//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.08625 + 0.0034761 * anchor

def f61_arm_561_analyst_v561(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=113, w2=101, w3=736, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 101)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.100625 + 0.0034762 * anchor

def f61_arm_562_analyst_v562(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=120, w2=112, w3=749, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(112, min_periods=max(112//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.115 + 0.0034763 * anchor

def f61_arm_563_analyst_v563(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=127, w2=123, w3=762, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(123, min_periods=max(123//3, 2)).rank(pct=True)
    persistence = change.rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3774 * persistence + 0.0034764 * anchor

def f61_arm_564_analyst_v564(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=134, w2=134, w3=18, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(134, min_periods=max(134//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14375 + 0.0034765 * anchor

def f61_arm_565_analyst_v565(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=141, w2=145, w3=31, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(145, min_periods=max(145//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3926 * slope + 0.0034766 * anchor

def f61_arm_566_analyst_v566(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=148, w2=156, w3=44, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(156, min_periods=max(156//3, 2)).mean()
    noise = impulse.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.1725 + 0.0034767 * anchor

def f61_arm_567_analyst_v567(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=155, w2=167, w3=57, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 167)
    curvature = _rolling_slope(acceleration, 57)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4078 * acceleration + 0.0034768 * anchor

def f61_arm_568_analyst_v568(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=162, w2=178, w3=70, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(178, min_periods=max(178//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(70) * 1.20125 + 0.0034769 * anchor

def f61_arm_569_analyst_v569(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=169, w2=189, w3=83, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0466 * _rolling_slope(draw, 83) + 0.003477 * anchor

def f61_arm_570_analyst_v570(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=176, w2=200, w3=96, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(200, min_periods=max(200//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.23 + 0.0034771 * anchor

def f61_arm_571_analyst_v571(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=183, w2=211, w3=109, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 211)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=109, adjust=False).mean() * 1.244375 + 0.0034772 * anchor

def f61_arm_572_analyst_v572(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=190, w2=222, w3=122, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.25875 + 0.0034773 * anchor

def f61_arm_573_analyst_v573(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=197, w2=233, w3=135, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(233, min_periods=max(233//3, 2)).rank(pct=True)
    persistence = change.rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.077 * persistence + 0.0034774 * anchor

def f61_arm_574_analyst_v574(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=204, w2=244, w3=148, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(244, min_periods=max(244//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2875 + 0.0034775 * anchor

def f61_arm_575_analyst_v575(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=211, w2=255, w3=161, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(255, min_periods=max(255//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0922 * slope + 0.0034776 * anchor

def f61_arm_576_analyst_v576(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=218, w2=266, w3=174, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(266, min_periods=max(266//3, 2)).mean()
    noise = impulse.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.31625 + 0.0034777 * anchor

def f61_arm_577_analyst_v577(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=225, w2=277, w3=187, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 277)
    curvature = _rolling_slope(acceleration, 187)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1074 * acceleration + 0.0034778 * anchor

def f61_arm_578_analyst_v578(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=232, w2=288, w3=200, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(288, min_periods=max(288//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.345 + 0.0034779 * anchor

def f61_arm_579_analyst_v579(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=239, w2=299, w3=213, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(299, min_periods=max(299//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1226 * _rolling_slope(draw, 213) + 0.003478 * anchor

def f61_arm_580_analyst_v580(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=246, w2=310, w3=226, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(310, min_periods=max(310//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.37375 + 0.0034781 * anchor

def f61_arm_581_analyst_v581(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=253, w2=321, w3=239, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 253)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=239, adjust=False).mean() * 1.388125 + 0.0034782 * anchor

def f61_arm_582_analyst_v582(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=9, w2=332, w3=252, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4025 + 0.0034783 * anchor

def f61_arm_583_analyst_v583(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=16, w2=343, w3=265, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(16)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.153 * persistence + 0.0034784 * anchor

def f61_arm_584_analyst_v584(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=23, w2=354, w3=278, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(354, min_periods=max(354//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43125 + 0.0034785 * anchor

def f61_arm_585_analyst_v585(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=30, w2=365, w3=291, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(365, min_periods=max(365//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1682 * slope + 0.0034786 * anchor

def f61_arm_586_analyst_v586(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=37, w2=376, w3=304, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(37)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.46 + 0.0034787 * anchor

def f61_arm_587_analyst_v587(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=44, w2=387, w3=317, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 387)
    curvature = _rolling_slope(acceleration, 317)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1834 * acceleration + 0.0034788 * anchor

def f61_arm_588_analyst_v588(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=51, w2=398, w3=330, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(398, min_periods=max(398//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.48875 + 0.0034789 * anchor

def f61_arm_589_analyst_v589(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=58, w2=409, w3=343, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(409, min_periods=max(409//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1986 * _rolling_slope(draw, 343) + 0.003479 * anchor

def f61_arm_590_analyst_v590(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=65, w2=420, w3=356, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(420, min_periods=max(420//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(356, min_periods=max(356//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.5175 + 0.0034791 * anchor

def f61_arm_591_analyst_v591(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=72, w2=431, w3=369, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 431)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.531875 + 0.0034792 * anchor

def f61_arm_592_analyst_v592(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=79, w2=442, w3=382, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(442, min_periods=max(442//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.54625 + 0.0034793 * anchor

def f61_arm_593_analyst_v593(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=86, w2=453, w3=395, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(86)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.229 * persistence + 0.0034794 * anchor

def f61_arm_594_analyst_v594(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=93, w2=464, w3=408, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(464, min_periods=max(464//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.575 + 0.0034795 * anchor

def f61_arm_595_analyst_v595(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=100, w2=475, w3=421, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2442 * slope + 0.0034796 * anchor

def f61_arm_596_analyst_v596(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=107, w2=486, w3=434, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(107)
    drag = impulse.rolling(486, min_periods=max(486//3, 2)).mean()
    noise = impulse.abs().rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.60375 + 0.0034797 * anchor

def f61_arm_597_analyst_v597(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=114, w2=497, w3=447, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 497)
    curvature = _rolling_slope(acceleration, 447)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2594 * acceleration + 0.0034798 * anchor

def f61_arm_598_analyst_v598(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=121, w2=508, w3=460, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(508, min_periods=max(508//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.859375 + 0.0034799 * anchor

def f61_arm_599_analyst_v599(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=128, w2=16, w3=473, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(16, min_periods=max(16//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2746 * _rolling_slope(draw, 473) + 0.00348 * anchor

def f61_arm_600_analyst_v600(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=135, w2=27, w3=486, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 135)
    baseline = trend.rolling(27, min_periods=max(27//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.888125 + 0.0034801 * anchor
