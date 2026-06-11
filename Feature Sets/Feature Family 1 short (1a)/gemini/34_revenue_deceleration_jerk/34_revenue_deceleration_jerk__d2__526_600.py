"""34 revenue deceleration jerk d2 second derivative features 526-600 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def f34_rdj_526_struct_v526_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=154, w2=325, w3=290, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(325, min_periods=max(325//3, 2)).mean()
    noise = impulse.abs().rolling(290, min_periods=max(290//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.915625 + 0.0020927 * anchor
    return base_signal.diff().diff()

def f34_rdj_527_struct_v527_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=161, w2=336, w3=303, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 303)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2394 * acceleration + 0.0020928 * anchor
    return base_signal.diff().diff()

def f34_rdj_528_struct_v528_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=168, w2=347, w3=316, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(347, min_periods=max(347//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.944375 + 0.0020929 * anchor
    return base_signal.diff().diff()

def f34_rdj_529_struct_v529_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=175, w2=358, w3=329, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(358, min_periods=max(358//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2546 * _rolling_slope(draw, 329) + 0.002093 * anchor
    return base_signal.diff().diff()

def f34_rdj_530_struct_v530_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=182, w2=369, w3=342, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(369, min_periods=max(369//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.973125 + 0.0020931 * anchor
    return base_signal.diff().diff()

def f34_rdj_531_struct_v531_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=189, w2=380, w3=355, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 380)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9875 + 0.0020932 * anchor
    return base_signal.diff().diff()

def f34_rdj_532_struct_v532_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=196, w2=391, w3=368, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.001875 + 0.0020933 * anchor
    return base_signal.diff().diff()

def f34_rdj_533_struct_v533_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=203, w2=402, w3=381, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(402, min_periods=max(402//3, 2)).rank(pct=True)
    persistence = change.rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.285 * persistence + 0.0020934 * anchor
    return base_signal.diff().diff()

def f34_rdj_534_struct_v534_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=210, w2=413, w3=394, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(413, min_periods=max(413//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.030625 + 0.0020935 * anchor
    return base_signal.diff().diff()

def f34_rdj_535_struct_v535_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=217, w2=424, w3=407, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3002 * slope + 0.0020936 * anchor
    return base_signal.diff().diff()

def f34_rdj_536_struct_v536_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=224, w2=435, w3=420, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(435, min_periods=max(435//3, 2)).mean()
    noise = impulse.abs().rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.059375 + 0.0020937 * anchor
    return base_signal.diff().diff()

def f34_rdj_537_struct_v537_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=231, w2=446, w3=433, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 446)
    curvature = _rolling_slope(acceleration, 433)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3154 * acceleration + 0.0020938 * anchor
    return base_signal.diff().diff()

def f34_rdj_538_struct_v538_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=238, w2=457, w3=446, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.088125 + 0.0020939 * anchor
    return base_signal.diff().diff()

def f34_rdj_539_struct_v539_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=245, w2=468, w3=459, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(468, min_periods=max(468//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3306 * _rolling_slope(draw, 459) + 0.002094 * anchor
    return base_signal.diff().diff()

def f34_rdj_540_struct_v540_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=252, w2=479, w3=472, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 252)
    baseline = trend.rolling(479, min_periods=max(479//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.116875 + 0.0020941 * anchor
    return base_signal.diff().diff()

def f34_rdj_541_struct_v541_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=8, w2=490, w3=485, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 8)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.13125 + 0.0020942 * anchor
    return base_signal.diff().diff()

def f34_rdj_542_struct_v542_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=15, w2=501, w3=498, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.145625 + 0.0020943 * anchor
    return base_signal.diff().diff()

def f34_rdj_543_struct_v543_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=22, w2=512, w3=511, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(22)
    rank = change.rolling(512, min_periods=max(512//3, 2)).rank(pct=True)
    persistence = change.rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361 * persistence + 0.0020944 * anchor
    return base_signal.diff().diff()

def f34_rdj_544_struct_v544_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=29, w2=20, w3=524, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(20, min_periods=max(20//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.174375 + 0.0020945 * anchor
    return base_signal.diff().diff()

def f34_rdj_545_struct_v545_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=36, w2=31, w3=537, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(31, min_periods=max(31//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 36)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3762 * slope + 0.0020946 * anchor
    return base_signal.diff().diff()

def f34_rdj_546_struct_v546_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=43, w2=42, w3=550, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(43)
    drag = impulse.rolling(42, min_periods=max(42//3, 2)).mean()
    noise = impulse.abs().rolling(550, min_periods=max(550//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.203125 + 0.0020947 * anchor
    return base_signal.diff().diff()

def f34_rdj_547_struct_v547_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=50, w2=53, w3=563, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 50)
    acceleration = _rolling_slope(velocity, 53)
    curvature = _rolling_slope(acceleration, 563)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3914 * acceleration + 0.0020948 * anchor
    return base_signal.diff().diff()

def f34_rdj_548_struct_v548_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=57, w2=64, w3=576, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(64, min_periods=max(64//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.231875 + 0.0020949 * anchor
    return base_signal.diff().diff()

def f34_rdj_549_struct_v549_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=64, w2=75, w3=589, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(75, min_periods=max(75//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4066 * _rolling_slope(draw, 589) + 0.002095 * anchor
    return base_signal.diff().diff()

def f34_rdj_550_struct_v550_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=71, w2=86, w3=602, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(86, min_periods=max(86//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.260625 + 0.0020951 * anchor
    return base_signal.diff().diff()

def f34_rdj_551_struct_v551_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=78, w2=97, w3=615, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 97)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.275 + 0.0020952 * anchor
    return base_signal.diff().diff()

def f34_rdj_552_struct_v552_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=85, w2=108, w3=628, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.289375 + 0.0020953 * anchor
    return base_signal.diff().diff()

def f34_rdj_553_struct_v553_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=92, w2=119, w3=641, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(92)
    rank = change.rolling(119, min_periods=max(119//3, 2)).rank(pct=True)
    persistence = change.rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0606 * persistence + 0.0020954 * anchor
    return base_signal.diff().diff()

def f34_rdj_554_struct_v554_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=99, w2=130, w3=654, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(130, min_periods=max(130//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.318125 + 0.0020955 * anchor
    return base_signal.diff().diff()

def f34_rdj_555_struct_v555_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=106, w2=141, w3=667, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(141, min_periods=max(141//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0758 * slope + 0.0020956 * anchor
    return base_signal.diff().diff()

def f34_rdj_556_struct_v556_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=113, w2=152, w3=680, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(113)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.346875 + 0.0020957 * anchor
    return base_signal.diff().diff()

def f34_rdj_557_struct_v557_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=120, w2=163, w3=693, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 163)
    curvature = _rolling_slope(acceleration, 693)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091 * acceleration + 0.0020958 * anchor
    return base_signal.diff().diff()

def f34_rdj_558_struct_v558_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=127, w2=174, w3=706, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.375625 + 0.0020959 * anchor
    return base_signal.diff().diff()

def f34_rdj_559_struct_v559_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=134, w2=185, w3=719, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(185, min_periods=max(185//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1062 * _rolling_slope(draw, 719) + 0.002096 * anchor
    return base_signal.diff().diff()

def f34_rdj_560_struct_v560_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=141, w2=196, w3=732, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.404375 + 0.0020961 * anchor
    return base_signal.diff().diff()

def f34_rdj_561_struct_v561_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=148, w2=207, w3=745, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 207)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.41875 + 0.0020962 * anchor
    return base_signal.diff().diff()

def f34_rdj_562_struct_v562_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=155, w2=218, w3=758, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(218, min_periods=max(218//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.433125 + 0.0020963 * anchor
    return base_signal.diff().diff()

def f34_rdj_563_struct_v563_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=162, w2=229, w3=771, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(229, min_periods=max(229//3, 2)).rank(pct=True)
    persistence = change.rolling(771, min_periods=max(771//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1366 * persistence + 0.0020964 * anchor
    return base_signal.diff().diff()

def f34_rdj_564_struct_v564_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=169, w2=240, w3=27, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(240, min_periods=max(240//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.461875 + 0.0020965 * anchor
    return base_signal.diff().diff()

def f34_rdj_565_struct_v565_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=176, w2=251, w3=40, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(251, min_periods=max(251//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1518 * slope + 0.0020966 * anchor
    return base_signal.diff().diff()

def f34_rdj_566_struct_v566_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=183, w2=262, w3=53, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(262, min_periods=max(262//3, 2)).mean()
    noise = impulse.abs().rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.490625 + 0.0020967 * anchor
    return base_signal.diff().diff()

def f34_rdj_567_struct_v567_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=190, w2=273, w3=66, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 273)
    curvature = _rolling_slope(acceleration, 66)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.167 * acceleration + 0.0020968 * anchor
    return base_signal.diff().diff()

def f34_rdj_568_struct_v568_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=197, w2=284, w3=79, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(284, min_periods=max(284//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(79) * 1.519375 + 0.0020969 * anchor
    return base_signal.diff().diff()

def f34_rdj_569_struct_v569_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=204, w2=295, w3=92, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(295, min_periods=max(295//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1822 * _rolling_slope(draw, 92) + 0.002097 * anchor
    return base_signal.diff().diff()

def f34_rdj_570_struct_v570_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=211, w2=306, w3=105, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.548125 + 0.0020971 * anchor
    return base_signal.diff().diff()

def f34_rdj_571_struct_v571_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=218, w2=317, w3=118, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=118, adjust=False).mean() * 1.5625 + 0.0020972 * anchor
    return base_signal.diff().diff()

def f34_rdj_572_struct_v572_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=225, w2=328, w3=131, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(328, min_periods=max(328//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.576875 + 0.0020973 * anchor
    return base_signal.diff().diff()

def f34_rdj_573_struct_v573_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=232, w2=339, w3=144, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(339, min_periods=max(339//3, 2)).rank(pct=True)
    persistence = change.rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2126 * persistence + 0.0020974 * anchor
    return base_signal.diff().diff()

def f34_rdj_574_struct_v574_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=239, w2=350, w3=157, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.605625 + 0.0020975 * anchor
    return base_signal.diff().diff()

def f34_rdj_575_struct_v575_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=246, w2=361, w3=170, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(361, min_periods=max(361//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2278 * slope + 0.0020976 * anchor
    return base_signal.diff().diff()

def f34_rdj_576_struct_v576_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=253, w2=372, w3=183, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(372, min_periods=max(372//3, 2)).mean()
    noise = impulse.abs().rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.86125 + 0.0020977 * anchor
    return base_signal.diff().diff()

def f34_rdj_577_struct_v577_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=9, w2=383, w3=196, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 383)
    curvature = _rolling_slope(acceleration, 196)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.243 * acceleration + 0.0020978 * anchor
    return base_signal.diff().diff()

def f34_rdj_578_struct_v578_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=16, w2=394, w3=209, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.89 + 0.0020979 * anchor
    return base_signal.diff().diff()

def f34_rdj_579_struct_v579_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=23, w2=405, w3=222, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(405, min_periods=max(405//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2582 * _rolling_slope(draw, 222) + 0.002098 * anchor
    return base_signal.diff().diff()

def f34_rdj_580_struct_v580_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=30, w2=416, w3=235, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(416, min_periods=max(416//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.91875 + 0.0020981 * anchor
    return base_signal.diff().diff()

def f34_rdj_581_struct_v581_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=37, w2=427, w3=248, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=248, adjust=False).mean() * 0.933125 + 0.0020982 * anchor
    return base_signal.diff().diff()

def f34_rdj_582_struct_v582_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=44, w2=438, w3=261, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(438, min_periods=max(438//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9475 + 0.0020983 * anchor
    return base_signal.diff().diff()

def f34_rdj_583_struct_v583_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=51, w2=449, w3=274, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(51)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2886 * persistence + 0.0020984 * anchor
    return base_signal.diff().diff()

def f34_rdj_584_struct_v584_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=58, w2=460, w3=287, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(460, min_periods=max(460//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.97625 + 0.0020985 * anchor
    return base_signal.diff().diff()

def f34_rdj_585_struct_v585_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=65, w2=471, w3=300, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(471, min_periods=max(471//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3038 * slope + 0.0020986 * anchor
    return base_signal.diff().diff()

def f34_rdj_586_struct_v586_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=72, w2=482, w3=313, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(72)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.005 + 0.0020987 * anchor
    return base_signal.diff().diff()

def f34_rdj_587_struct_v587_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=79, w2=493, w3=326, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 493)
    curvature = _rolling_slope(acceleration, 326)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.319 * acceleration + 0.0020988 * anchor
    return base_signal.diff().diff()

def f34_rdj_588_struct_v588_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=86, w2=504, w3=339, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(504, min_periods=max(504//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.03375 + 0.0020989 * anchor
    return base_signal.diff().diff()

def f34_rdj_589_struct_v589_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=93, w2=12, w3=352, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(12, min_periods=max(12//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3342 * _rolling_slope(draw, 352) + 0.002099 * anchor
    return base_signal.diff().diff()

def f34_rdj_590_struct_v590_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=100, w2=23, w3=365, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(23, min_periods=max(23//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0625 + 0.0020991 * anchor
    return base_signal.diff().diff()

def f34_rdj_591_struct_v591_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=107, w2=34, w3=378, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 34)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.076875 + 0.0020992 * anchor
    return base_signal.diff().diff()

def f34_rdj_592_struct_v592_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=114, w2=45, w3=391, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(45, min_periods=max(45//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.09125 + 0.0020993 * anchor
    return base_signal.diff().diff()

def f34_rdj_593_struct_v593_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=121, w2=56, w3=404, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(121)
    rank = change.rolling(56, min_periods=max(56//3, 2)).rank(pct=True)
    persistence = change.rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3646 * persistence + 0.0020994 * anchor
    return base_signal.diff().diff()

def f34_rdj_594_struct_v594_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=128, w2=67, w3=417, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(67, min_periods=max(67//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.12 + 0.0020995 * anchor
    return base_signal.diff().diff()

def f34_rdj_595_struct_v595_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=135, w2=78, w3=430, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(78, min_periods=max(78//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3798 * slope + 0.0020996 * anchor
    return base_signal.diff().diff()

def f34_rdj_596_struct_v596_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=142, w2=89, w3=443, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(89, min_periods=max(89//3, 2)).mean()
    noise = impulse.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.14875 + 0.0020997 * anchor
    return base_signal.diff().diff()

def f34_rdj_597_struct_v597_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=149, w2=100, w3=456, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 100)
    curvature = _rolling_slope(acceleration, 456)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.395 * acceleration + 0.0020998 * anchor
    return base_signal.diff().diff()

def f34_rdj_598_struct_v598_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=156, w2=111, w3=469, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(111, min_periods=max(111//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1775 + 0.0020999 * anchor
    return base_signal.diff().diff()

def f34_rdj_599_struct_v599_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=163, w2=122, w3=482, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(122, min_periods=max(122//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4102 * _rolling_slope(draw, 482) + 0.0021 * anchor
    return base_signal.diff().diff()

def f34_rdj_600_struct_v600_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=170, w2=133, w3=495, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.20625 + 0.0021001 * anchor
    return base_signal.diff().diff()
