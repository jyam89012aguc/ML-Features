"""21 revenue growth deceleration d1 first derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Trajectory - Institutional-grade short-side signal.
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

def f21_rgd_151_struct_v151_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=437, w3=752, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 437)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.915 + 0.0012752 * anchor
    return base_signal.diff()

def f21_rgd_152_struct_v152_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=448, w3=765, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(448, min_periods=max(448//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.929375 + 0.0012753 * anchor
    return base_signal.diff()

def f21_rgd_153_struct_v153_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=459, w3=21, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(459, min_periods=max(459//3, 2)).rank(pct=True)
    persistence = change.rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.223 * persistence + 0.0012754 * anchor
    return base_signal.diff()

def f21_rgd_154_struct_v154_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=470, w3=34, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(470, min_periods=max(470//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.958125 + 0.0012755 * anchor
    return base_signal.diff()

def f21_rgd_155_struct_v155_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=481, w3=47, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(481, min_periods=max(481//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2382 * slope + 0.0012756 * anchor
    return base_signal.diff()

def f21_rgd_156_struct_v156_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=492, w3=60, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.986875 + 0.0012757 * anchor
    return base_signal.diff()

def f21_rgd_157_struct_v157_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=503, w3=73, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 503)
    curvature = _rolling_slope(acceleration, 73)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2534 * acceleration + 0.0012758 * anchor
    return base_signal.diff()

def f21_rgd_158_struct_v158_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=11, w3=86, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(11, min_periods=max(11//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(86) * 1.015625 + 0.0012759 * anchor
    return base_signal.diff()

def f21_rgd_159_struct_v159_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=22, w3=99, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(22, min_periods=max(22//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2686 * _rolling_slope(draw, 99) + 0.001276 * anchor
    return base_signal.diff()

def f21_rgd_160_struct_v160_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=33, w3=112, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(33, min_periods=max(33//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.044375 + 0.0012761 * anchor
    return base_signal.diff()

def f21_rgd_161_struct_v161_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=44, w3=125, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 44)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=125, adjust=False).mean() * 1.05875 + 0.0012762 * anchor
    return base_signal.diff()

def f21_rgd_162_struct_v162_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=55, w3=138, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.073125 + 0.0012763 * anchor
    return base_signal.diff()

def f21_rgd_163_struct_v163_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=66, w3=151, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(66, min_periods=max(66//3, 2)).rank(pct=True)
    persistence = change.rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.299 * persistence + 0.0012764 * anchor
    return base_signal.diff()

def f21_rgd_164_struct_v164_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=77, w3=164, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(77, min_periods=max(77//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.101875 + 0.0012765 * anchor
    return base_signal.diff()

def f21_rgd_165_struct_v165_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=88, w3=177, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(88, min_periods=max(88//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 255)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3142 * slope + 0.0012766 * anchor
    return base_signal.diff()

def f21_rgd_166_struct_v166_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=99, w3=190, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(11)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.130625 + 0.0012767 * anchor
    return base_signal.diff()

def f21_rgd_167_struct_v167_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=110, w3=203, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 110)
    curvature = _rolling_slope(acceleration, 203)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3294 * acceleration + 0.0012768 * anchor
    return base_signal.diff()

def f21_rgd_168_struct_v168_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=121, w3=216, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(121, min_periods=max(121//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.159375 + 0.0012769 * anchor
    return base_signal.diff()

def f21_rgd_169_struct_v169_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=132, w3=229, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(132, min_periods=max(132//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3446 * _rolling_slope(draw, 229) + 0.001277 * anchor
    return base_signal.diff()

def f21_rgd_170_struct_v170_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=143, w3=242, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(143, min_periods=max(143//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.188125 + 0.0012771 * anchor
    return base_signal.diff()

def f21_rgd_171_struct_v171_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=154, w3=255, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 154)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=255, adjust=False).mean() * 1.2025 + 0.0012772 * anchor
    return base_signal.diff()

def f21_rgd_172_struct_v172_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=165, w3=268, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(165, min_periods=max(165//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.216875 + 0.0012773 * anchor
    return base_signal.diff()

def f21_rgd_173_struct_v173_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=176, w3=281, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(60)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.375 * persistence + 0.0012774 * anchor
    return base_signal.diff()

def f21_rgd_174_struct_v174_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=187, w3=294, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(187, min_periods=max(187//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245625 + 0.0012775 * anchor
    return base_signal.diff()

def f21_rgd_175_struct_v175_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=198, w3=307, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3902 * slope + 0.0012776 * anchor
    return base_signal.diff()

def f21_rgd_176_struct_v176_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=209, w3=320, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(81)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.274375 + 0.0012777 * anchor
    return base_signal.diff()

def f21_rgd_177_struct_v177_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=220, w3=333, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 220)
    curvature = _rolling_slope(acceleration, 333)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4054 * acceleration + 0.0012778 * anchor
    return base_signal.diff()

def f21_rgd_178_struct_v178_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=231, w3=346, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(231, min_periods=max(231//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.303125 + 0.0012779 * anchor
    return base_signal.diff()

def f21_rgd_179_struct_v179_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=242, w3=359, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(242, min_periods=max(242//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0442 * _rolling_slope(draw, 359) + 0.001278 * anchor
    return base_signal.diff()

def f21_rgd_180_struct_v180_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=253, w3=372, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(253, min_periods=max(253//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(372, min_periods=max(372//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.331875 + 0.0012781 * anchor
    return base_signal.diff()

def f21_rgd_181_struct_v181_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=264, w3=385, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 264)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.34625 + 0.0012782 * anchor
    return base_signal.diff()

def f21_rgd_182_struct_v182_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=275, w3=398, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(275, min_periods=max(275//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.360625 + 0.0012783 * anchor
    return base_signal.diff()

def f21_rgd_183_struct_v183_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=286, w3=411, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(286, min_periods=max(286//3, 2)).rank(pct=True)
    persistence = change.rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0746 * persistence + 0.0012784 * anchor
    return base_signal.diff()

def f21_rgd_184_struct_v184_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=297, w3=424, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(297, min_periods=max(297//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.389375 + 0.0012785 * anchor
    return base_signal.diff()

def f21_rgd_185_struct_v185_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=308, w3=437, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0898 * slope + 0.0012786 * anchor
    return base_signal.diff()

def f21_rgd_186_struct_v186_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=319, w3=450, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(319, min_periods=max(319//3, 2)).mean()
    noise = impulse.abs().rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.418125 + 0.0012787 * anchor
    return base_signal.diff()

def f21_rgd_187_struct_v187_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=330, w3=463, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 330)
    curvature = _rolling_slope(acceleration, 463)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.105 * acceleration + 0.0012788 * anchor
    return base_signal.diff()

def f21_rgd_188_struct_v188_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=341, w3=476, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(341, min_periods=max(341//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.446875 + 0.0012789 * anchor
    return base_signal.diff()

def f21_rgd_189_struct_v189_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=352, w3=489, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1202 * _rolling_slope(draw, 489) + 0.001279 * anchor
    return base_signal.diff()

def f21_rgd_190_struct_v190_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=363, w3=502, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(363, min_periods=max(363//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(502, min_periods=max(502//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.475625 + 0.0012791 * anchor
    return base_signal.diff()

def f21_rgd_191_struct_v191_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=374, w3=515, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 374)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.49 + 0.0012792 * anchor
    return base_signal.diff()

def f21_rgd_192_struct_v192_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=385, w3=528, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(385, min_periods=max(385//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.504375 + 0.0012793 * anchor
    return base_signal.diff()

def f21_rgd_193_struct_v193_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=396, w3=541, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1506 * persistence + 0.0012794 * anchor
    return base_signal.diff()

def f21_rgd_194_struct_v194_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=407, w3=554, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(407, min_periods=max(407//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.533125 + 0.0012795 * anchor
    return base_signal.diff()

def f21_rgd_195_struct_v195_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=418, w3=567, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1658 * slope + 0.0012796 * anchor
    return base_signal.diff()

def f21_rgd_196_struct_v196_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=429, w3=580, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(580, min_periods=max(580//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.561875 + 0.0012797 * anchor
    return base_signal.diff()

def f21_rgd_197_struct_v197_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=440, w3=593, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 440)
    curvature = _rolling_slope(acceleration, 593)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.181 * acceleration + 0.0012798 * anchor
    return base_signal.diff()

def f21_rgd_198_struct_v198_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=451, w3=606, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.590625 + 0.0012799 * anchor
    return base_signal.diff()

def f21_rgd_199_struct_v199_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=462, w3=619, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1962 * _rolling_slope(draw, 619) + 0.00128 * anchor
    return base_signal.diff()

def f21_rgd_200_struct_v200_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=473, w3=632, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(473, min_periods=max(473//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.619375 + 0.0012801 * anchor
    return base_signal.diff()

def f21_rgd_201_struct_v201_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=484, w3=645, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 484)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.860625 + 0.0012802 * anchor
    return base_signal.diff()

def f21_rgd_202_struct_v202_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=495, w3=658, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.875 + 0.0012803 * anchor
    return base_signal.diff()

def f21_rgd_203_struct_v203_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=506, w3=671, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(19)
    rank = change.rolling(506, min_periods=max(506//3, 2)).rank(pct=True)
    persistence = change.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2266 * persistence + 0.0012804 * anchor
    return base_signal.diff()

def f21_rgd_204_struct_v204_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=14, w3=684, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90375 + 0.0012805 * anchor
    return base_signal.diff()

def f21_rgd_205_struct_v205_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=25, w3=697, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(25, min_periods=max(25//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2418 * slope + 0.0012806 * anchor
    return base_signal.diff()

def f21_rgd_206_struct_v206_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=36, w3=710, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(40)
    drag = impulse.rolling(36, min_periods=max(36//3, 2)).mean()
    noise = impulse.abs().rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9325 + 0.0012807 * anchor
    return base_signal.diff()

def f21_rgd_207_struct_v207_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=47, w3=723, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 47)
    curvature = _rolling_slope(acceleration, 723)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.257 * acceleration + 0.0012808 * anchor
    return base_signal.diff()

def f21_rgd_208_struct_v208_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=58, w3=736, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(58, min_periods=max(58//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.96125 + 0.0012809 * anchor
    return base_signal.diff()

def f21_rgd_209_struct_v209_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=69, w3=749, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(69, min_periods=max(69//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2722 * _rolling_slope(draw, 749) + 0.001281 * anchor
    return base_signal.diff()

def f21_rgd_210_struct_v210_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=80, w3=762, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(80, min_periods=max(80//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.99 + 0.0012811 * anchor
    return base_signal.diff()

def f21_rgd_211_struct_v211_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=91, w3=18, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 91)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=18, adjust=False).mean() * 1.004375 + 0.0012812 * anchor
    return base_signal.diff()

def f21_rgd_212_struct_v212_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=102, w3=31, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(102, min_periods=max(102//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01875 + 0.0012813 * anchor
    return base_signal.diff()

def f21_rgd_213_struct_v213_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=113, w3=44, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(89)
    rank = change.rolling(113, min_periods=max(113//3, 2)).rank(pct=True)
    persistence = change.rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3026 * persistence + 0.0012814 * anchor
    return base_signal.diff()

def f21_rgd_214_struct_v214_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=124, w3=57, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(124, min_periods=max(124//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0475 + 0.0012815 * anchor
    return base_signal.diff()

def f21_rgd_215_struct_v215_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=135, w3=70, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(135, min_periods=max(135//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3178 * slope + 0.0012816 * anchor
    return base_signal.diff()

def f21_rgd_216_struct_v216_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=146, w3=83, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(110)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.07625 + 0.0012817 * anchor
    return base_signal.diff()

def f21_rgd_217_struct_v217_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=157, w3=96, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 96)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.333 * acceleration + 0.0012818 * anchor
    return base_signal.diff()

def f21_rgd_218_struct_v218_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=168, w3=109, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(168, min_periods=max(168//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(109) * 1.105 + 0.0012819 * anchor
    return base_signal.diff()

def f21_rgd_219_struct_v219_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=179, w3=122, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(179, min_periods=max(179//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3482 * _rolling_slope(draw, 122) + 0.001282 * anchor
    return base_signal.diff()

def f21_rgd_220_struct_v220_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=190, w3=135, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(135, min_periods=max(135//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.13375 + 0.0012821 * anchor
    return base_signal.diff()

def f21_rgd_221_struct_v221_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=201, w3=148, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=148, adjust=False).mean() * 1.148125 + 0.0012822 * anchor
    return base_signal.diff()

def f21_rgd_222_struct_v222_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=212, w3=161, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(212, min_periods=max(212//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1625 + 0.0012823 * anchor
    return base_signal.diff()

def f21_rgd_223_struct_v223_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=223, w3=174, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3786 * persistence + 0.0012824 * anchor
    return base_signal.diff()

def f21_rgd_224_struct_v224_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=234, w3=187, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(234, min_periods=max(234//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.19125 + 0.0012825 * anchor
    return base_signal.diff()

def f21_rgd_225_struct_v225_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=245, w3=200, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(245, min_periods=max(245//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3938 * slope + 0.0012826 * anchor
    return base_signal.diff()
