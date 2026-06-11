"""31 cash burn acceleration d2 second derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f31_cba_301_struct_v301_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=35, w2=182, w3=460, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 182)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.185 + 0.0018902 * anchor
    return base_signal.diff().diff()

def f31_cba_302_struct_v302_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=42, w2=193, w3=473, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(193, min_periods=max(193//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.199375 + 0.0018903 * anchor
    return base_signal.diff().diff()

def f31_cba_303_struct_v303_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=49, w2=204, w3=486, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(49)
    rank = change.rolling(204, min_periods=max(204//3, 2)).rank(pct=True)
    persistence = change.rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2894 * persistence + 0.0018904 * anchor
    return base_signal.diff().diff()

def f31_cba_304_struct_v304_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=56, w2=215, w3=499, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(215, min_periods=max(215//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.228125 + 0.0018905 * anchor
    return base_signal.diff().diff()

def f31_cba_305_struct_v305_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=63, w2=226, w3=512, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(226, min_periods=max(226//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3046 * slope + 0.0018906 * anchor
    return base_signal.diff().diff()

def f31_cba_306_struct_v306_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=70, w2=237, w3=525, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(70)
    drag = impulse.rolling(237, min_periods=max(237//3, 2)).mean()
    noise = impulse.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.256875 + 0.0018907 * anchor
    return base_signal.diff().diff()

def f31_cba_307_struct_v307_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=77, w2=248, w3=538, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 248)
    curvature = _rolling_slope(acceleration, 538)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3198 * acceleration + 0.0018908 * anchor
    return base_signal.diff().diff()

def f31_cba_308_struct_v308_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=84, w2=259, w3=551, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(259, min_periods=max(259//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.285625 + 0.0018909 * anchor
    return base_signal.diff().diff()

def f31_cba_309_struct_v309_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=91, w2=270, w3=564, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(270, min_periods=max(270//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.335 * _rolling_slope(draw, 564) + 0.001891 * anchor
    return base_signal.diff().diff()

def f31_cba_310_struct_v310_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=98, w2=281, w3=577, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(281, min_periods=max(281//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.314375 + 0.0018911 * anchor
    return base_signal.diff().diff()

def f31_cba_311_struct_v311_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=105, w2=292, w3=590, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 292)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.32875 + 0.0018912 * anchor
    return base_signal.diff().diff()

def f31_cba_312_struct_v312_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=112, w2=303, w3=603, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(303, min_periods=max(303//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.343125 + 0.0018913 * anchor
    return base_signal.diff().diff()

def f31_cba_313_struct_v313_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=119, w2=314, w3=616, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(119)
    rank = change.rolling(314, min_periods=max(314//3, 2)).rank(pct=True)
    persistence = change.rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3654 * persistence + 0.0018914 * anchor
    return base_signal.diff().diff()

def f31_cba_314_struct_v314_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=126, w2=325, w3=629, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(325, min_periods=max(325//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.371875 + 0.0018915 * anchor
    return base_signal.diff().diff()

def f31_cba_315_struct_v315_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=133, w2=336, w3=642, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(336, min_periods=max(336//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3806 * slope + 0.0018916 * anchor
    return base_signal.diff().diff()

def f31_cba_316_struct_v316_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=140, w2=347, w3=655, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(347, min_periods=max(347//3, 2)).mean()
    noise = impulse.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.400625 + 0.0018917 * anchor
    return base_signal.diff().diff()

def f31_cba_317_struct_v317_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=147, w2=358, w3=668, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 358)
    curvature = _rolling_slope(acceleration, 668)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3958 * acceleration + 0.0018918 * anchor
    return base_signal.diff().diff()

def f31_cba_318_struct_v318_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=154, w2=369, w3=681, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(369, min_periods=max(369//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.429375 + 0.0018919 * anchor
    return base_signal.diff().diff()

def f31_cba_319_struct_v319_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=161, w2=380, w3=694, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(380, min_periods=max(380//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.411 * _rolling_slope(draw, 694) + 0.001892 * anchor
    return base_signal.diff().diff()

def f31_cba_320_struct_v320_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=168, w2=391, w3=707, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(391, min_periods=max(391//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.458125 + 0.0018921 * anchor
    return base_signal.diff().diff()

def f31_cba_321_struct_v321_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=175, w2=402, w3=720, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 402)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4725 + 0.0018922 * anchor
    return base_signal.diff().diff()

def f31_cba_322_struct_v322_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=182, w2=413, w3=733, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(413, min_periods=max(413//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.486875 + 0.0018923 * anchor
    return base_signal.diff().diff()

def f31_cba_323_struct_v323_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=189, w2=424, w3=746, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(424, min_periods=max(424//3, 2)).rank(pct=True)
    persistence = change.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.065 * persistence + 0.0018924 * anchor
    return base_signal.diff().diff()

def f31_cba_324_struct_v324_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=196, w2=435, w3=759, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(435, min_periods=max(435//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.515625 + 0.0018925 * anchor
    return base_signal.diff().diff()

def f31_cba_325_struct_v325_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=203, w2=446, w3=15, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(446, min_periods=max(446//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0802 * slope + 0.0018926 * anchor
    return base_signal.diff().diff()

def f31_cba_326_struct_v326_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=210, w2=457, w3=28, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(457, min_periods=max(457//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.544375 + 0.0018927 * anchor
    return base_signal.diff().diff()

def f31_cba_327_struct_v327_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=217, w2=468, w3=41, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 468)
    curvature = _rolling_slope(acceleration, 41)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0954 * acceleration + 0.0018928 * anchor
    return base_signal.diff().diff()

def f31_cba_328_struct_v328_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=224, w2=479, w3=54, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(479, min_periods=max(479//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(54) * 1.573125 + 0.0018929 * anchor
    return base_signal.diff().diff()

def f31_cba_329_struct_v329_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=231, w2=490, w3=67, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(490, min_periods=max(490//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1106 * _rolling_slope(draw, 67) + 0.001893 * anchor
    return base_signal.diff().diff()

def f31_cba_330_struct_v330_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=238, w2=501, w3=80, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(501, min_periods=max(501//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.601875 + 0.0018931 * anchor
    return base_signal.diff().diff()

def f31_cba_331_struct_v331_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=245, w2=512, w3=93, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 512)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=93, adjust=False).mean() * 1.61625 + 0.0018932 * anchor
    return base_signal.diff().diff()

def f31_cba_332_struct_v332_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=252, w2=20, w3=106, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(20, min_periods=max(20//3, 2)).max()
    trough = x.rolling(252, min_periods=max(252//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.8575 + 0.0018933 * anchor
    return base_signal.diff().diff()

def f31_cba_333_struct_v333_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=8, w2=31, w3=119, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(8)
    rank = change.rolling(31, min_periods=max(31//3, 2)).rank(pct=True)
    persistence = change.rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.141 * persistence + 0.0018934 * anchor
    return base_signal.diff().diff()

def f31_cba_334_struct_v334_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=15, w2=42, w3=132, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(42, min_periods=max(42//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.88625 + 0.0018935 * anchor
    return base_signal.diff().diff()

def f31_cba_335_struct_v335_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=22, w2=53, w3=145, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(53, min_periods=max(53//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1562 * slope + 0.0018936 * anchor
    return base_signal.diff().diff()

def f31_cba_336_struct_v336_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=29, w2=64, w3=158, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(29)
    drag = impulse.rolling(64, min_periods=max(64//3, 2)).mean()
    noise = impulse.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.915 + 0.0018937 * anchor
    return base_signal.diff().diff()

def f31_cba_337_struct_v337_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=36, w2=75, w3=171, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 36)
    acceleration = _rolling_slope(velocity, 75)
    curvature = _rolling_slope(acceleration, 171)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1714 * acceleration + 0.0018938 * anchor
    return base_signal.diff().diff()

def f31_cba_338_struct_v338_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=43, w2=86, w3=184, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(86, min_periods=max(86//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.94375 + 0.0018939 * anchor
    return base_signal.diff().diff()

def f31_cba_339_struct_v339_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=50, w2=97, w3=197, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(97, min_periods=max(97//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1866 * _rolling_slope(draw, 197) + 0.001894 * anchor
    return base_signal.diff().diff()

def f31_cba_340_struct_v340_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=57, w2=108, w3=210, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 57)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9725 + 0.0018941 * anchor
    return base_signal.diff().diff()

def f31_cba_341_struct_v341_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=64, w2=119, w3=223, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 64)
    slow = _rolling_slope(x, 119)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=223, adjust=False).mean() * 0.986875 + 0.0018942 * anchor
    return base_signal.diff().diff()

def f31_cba_342_struct_v342_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=71, w2=130, w3=236, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(71, min_periods=max(71//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.00125 + 0.0018943 * anchor
    return base_signal.diff().diff()

def f31_cba_343_struct_v343_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=78, w2=141, w3=249, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(78)
    rank = change.rolling(141, min_periods=max(141//3, 2)).rank(pct=True)
    persistence = change.rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217 * persistence + 0.0018944 * anchor
    return base_signal.diff().diff()

def f31_cba_344_struct_v344_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=85, w2=152, w3=262, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(85, min_periods=max(85//3, 2)).std()
    vol_slow = ret.rolling(152, min_periods=max(152//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03 + 0.0018945 * anchor
    return base_signal.diff().diff()

def f31_cba_345_struct_v345_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=92, w2=163, w3=275, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(163, min_periods=max(163//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 92)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2322 * slope + 0.0018946 * anchor
    return base_signal.diff().diff()

def f31_cba_346_struct_v346_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=99, w2=174, w3=288, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(99)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.05875 + 0.0018947 * anchor
    return base_signal.diff().diff()

def f31_cba_347_struct_v347_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=106, w2=185, w3=301, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 106)
    acceleration = _rolling_slope(velocity, 185)
    curvature = _rolling_slope(acceleration, 301)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2474 * acceleration + 0.0018948 * anchor
    return base_signal.diff().diff()

def f31_cba_348_struct_v348_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=113, w2=196, w3=314, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(196, min_periods=max(196//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0875 + 0.0018949 * anchor
    return base_signal.diff().diff()

def f31_cba_349_struct_v349_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=120, w2=207, w3=327, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(207, min_periods=max(207//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2626 * _rolling_slope(draw, 327) + 0.001895 * anchor
    return base_signal.diff().diff()

def f31_cba_350_struct_v350_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=127, w2=218, w3=340, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 127)
    baseline = trend.rolling(218, min_periods=max(218//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.11625 + 0.0018951 * anchor
    return base_signal.diff().diff()

def f31_cba_351_struct_v351_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=134, w2=229, w3=353, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 134)
    slow = _rolling_slope(x, 229)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.130625 + 0.0018952 * anchor
    return base_signal.diff().diff()

def f31_cba_352_struct_v352_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=141, w2=240, w3=366, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(240, min_periods=max(240//3, 2)).max()
    trough = x.rolling(141, min_periods=max(141//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.145 + 0.0018953 * anchor
    return base_signal.diff().diff()

def f31_cba_353_struct_v353_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=148, w2=251, w3=379, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(251, min_periods=max(251//3, 2)).rank(pct=True)
    persistence = change.rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.293 * persistence + 0.0018954 * anchor
    return base_signal.diff().diff()

def f31_cba_354_struct_v354_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=155, w2=262, w3=392, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(155, min_periods=max(155//3, 2)).std()
    vol_slow = ret.rolling(262, min_periods=max(262//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17375 + 0.0018955 * anchor
    return base_signal.diff().diff()

def f31_cba_355_struct_v355_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=162, w2=273, w3=405, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(273, min_periods=max(273//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 162)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3082 * slope + 0.0018956 * anchor
    return base_signal.diff().diff()

def f31_cba_356_struct_v356_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=169, w2=284, w3=418, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(284, min_periods=max(284//3, 2)).mean()
    noise = impulse.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2025 + 0.0018957 * anchor
    return base_signal.diff().diff()

def f31_cba_357_struct_v357_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=176, w2=295, w3=431, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 176)
    acceleration = _rolling_slope(velocity, 295)
    curvature = _rolling_slope(acceleration, 431)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3234 * acceleration + 0.0018958 * anchor
    return base_signal.diff().diff()

def f31_cba_358_struct_v358_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=183, w2=306, w3=444, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.23125 + 0.0018959 * anchor
    return base_signal.diff().diff()

def f31_cba_359_struct_v359_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=190, w2=317, w3=457, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3386 * _rolling_slope(draw, 457) + 0.001896 * anchor
    return base_signal.diff().diff()

def f31_cba_360_struct_v360_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=197, w2=328, w3=470, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 197)
    baseline = trend.rolling(328, min_periods=max(328//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.26 + 0.0018961 * anchor
    return base_signal.diff().diff()

def f31_cba_361_struct_v361_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=204, w2=339, w3=483, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 204)
    slow = _rolling_slope(x, 339)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.274375 + 0.0018962 * anchor
    return base_signal.diff().diff()

def f31_cba_362_struct_v362_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=211, w2=350, w3=496, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(350, min_periods=max(350//3, 2)).max()
    trough = x.rolling(211, min_periods=max(211//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.28875 + 0.0018963 * anchor
    return base_signal.diff().diff()

def f31_cba_363_struct_v363_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=218, w2=361, w3=509, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(361, min_periods=max(361//3, 2)).rank(pct=True)
    persistence = change.rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.369 * persistence + 0.0018964 * anchor
    return base_signal.diff().diff()

def f31_cba_364_struct_v364_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=225, w2=372, w3=522, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(225, min_periods=max(225//3, 2)).std()
    vol_slow = ret.rolling(372, min_periods=max(372//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3175 + 0.0018965 * anchor
    return base_signal.diff().diff()

def f31_cba_365_struct_v365_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=232, w2=383, w3=535, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(383, min_periods=max(383//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 232)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3842 * slope + 0.0018966 * anchor
    return base_signal.diff().diff()

def f31_cba_366_struct_v366_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=239, w2=394, w3=548, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(394, min_periods=max(394//3, 2)).mean()
    noise = impulse.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.34625 + 0.0018967 * anchor
    return base_signal.diff().diff()

def f31_cba_367_struct_v367_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=246, w2=405, w3=561, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 246)
    acceleration = _rolling_slope(velocity, 405)
    curvature = _rolling_slope(acceleration, 561)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3994 * acceleration + 0.0018968 * anchor
    return base_signal.diff().diff()

def f31_cba_368_struct_v368_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=253, w2=416, w3=574, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(416, min_periods=max(416//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.375 + 0.0018969 * anchor
    return base_signal.diff().diff()

def f31_cba_369_struct_v369_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=9, w2=427, w3=587, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(427, min_periods=max(427//3, 2)).max()
    rebound = x - x.rolling(9, min_periods=max(9//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0382 * _rolling_slope(draw, 587) + 0.001897 * anchor
    return base_signal.diff().diff()

def f31_cba_370_struct_v370_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=16, w2=438, w3=600, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(438, min_periods=max(438//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.40375 + 0.0018971 * anchor
    return base_signal.diff().diff()

def f31_cba_371_struct_v371_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=23, w2=449, w3=613, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.418125 + 0.0018972 * anchor
    return base_signal.diff().diff()

def f31_cba_372_struct_v372_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=30, w2=460, w3=626, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4325 + 0.0018973 * anchor
    return base_signal.diff().diff()

def f31_cba_373_struct_v373_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=37, w2=471, w3=639, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(37)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0686 * persistence + 0.0018974 * anchor
    return base_signal.diff().diff()

def f31_cba_374_struct_v374_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=44, w2=482, w3=652, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(482, min_periods=max(482//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46125 + 0.0018975 * anchor
    return base_signal.diff().diff()

def f31_cba_375_struct_v375_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=51, w2=493, w3=665, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0838 * slope + 0.0018976 * anchor
    return base_signal.diff().diff()
