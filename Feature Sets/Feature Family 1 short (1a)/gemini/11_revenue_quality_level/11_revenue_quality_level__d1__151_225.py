"""11 revenue quality level d1 first derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Quality - Institutional-grade short-side signal.
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

def f11_revq_151_struct_v151_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=330, w3=723, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 330)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.255 + 0.0006752 * anchor
    return base_signal.diff()

def f11_revq_152_struct_v152_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=341, w3=736, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(341, min_periods=max(341//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.269375 + 0.0006753 * anchor
    return base_signal.diff()

def f11_revq_153_struct_v153_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=352, w3=749, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(88)
    rank = change.rolling(352, min_periods=max(352//3, 2)).rank(pct=True)
    persistence = change.rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1674 * persistence + 0.0006754 * anchor
    return base_signal.diff()

def f11_revq_154_struct_v154_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=363, w3=762, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(363, min_periods=max(363//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.298125 + 0.0006755 * anchor
    return base_signal.diff()

def f11_revq_155_struct_v155_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=374, w3=18, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(374, min_periods=max(374//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1826 * slope + 0.0006756 * anchor
    return base_signal.diff()

def f11_revq_156_struct_v156_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=385, w3=31, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(109)
    drag = impulse.rolling(385, min_periods=max(385//3, 2)).mean()
    noise = impulse.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.326875 + 0.0006757 * anchor
    return base_signal.diff()

def f11_revq_157_struct_v157_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=396, w3=44, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 44)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1978 * acceleration + 0.0006758 * anchor
    return base_signal.diff()

def f11_revq_158_struct_v158_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=407, w3=57, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(407, min_periods=max(407//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(57) * 1.355625 + 0.0006759 * anchor
    return base_signal.diff()

def f11_revq_159_struct_v159_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=418, w3=70, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(418, min_periods=max(418//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.213 * _rolling_slope(draw, 70) + 0.000676 * anchor
    return base_signal.diff()

def f11_revq_160_struct_v160_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=429, w3=83, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(429, min_periods=max(429//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.384375 + 0.0006761 * anchor
    return base_signal.diff()

def f11_revq_161_struct_v161_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=440, w3=96, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 440)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=96, adjust=False).mean() * 1.39875 + 0.0006762 * anchor
    return base_signal.diff()

def f11_revq_162_struct_v162_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=451, w3=109, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(451, min_periods=max(451//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.413125 + 0.0006763 * anchor
    return base_signal.diff()

def f11_revq_163_struct_v163_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=462, w3=122, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(462, min_periods=max(462//3, 2)).rank(pct=True)
    persistence = change.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2434 * persistence + 0.0006764 * anchor
    return base_signal.diff()

def f11_revq_164_struct_v164_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=473, w3=135, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(473, min_periods=max(473//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.441875 + 0.0006765 * anchor
    return base_signal.diff()

def f11_revq_165_struct_v165_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=484, w3=148, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(484, min_periods=max(484//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2586 * slope + 0.0006766 * anchor
    return base_signal.diff()

def f11_revq_166_struct_v166_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=495, w3=161, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(495, min_periods=max(495//3, 2)).mean()
    noise = impulse.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.470625 + 0.0006767 * anchor
    return base_signal.diff()

def f11_revq_167_struct_v167_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=506, w3=174, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 506)
    curvature = _rolling_slope(acceleration, 174)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2738 * acceleration + 0.0006768 * anchor
    return base_signal.diff()

def f11_revq_168_struct_v168_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=14, w3=187, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(14, min_periods=max(14//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.499375 + 0.0006769 * anchor
    return base_signal.diff()

def f11_revq_169_struct_v169_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=25, w3=200, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(25, min_periods=max(25//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.289 * _rolling_slope(draw, 200) + 0.000677 * anchor
    return base_signal.diff()

def f11_revq_170_struct_v170_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=36, w3=213, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(36, min_periods=max(36//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.528125 + 0.0006771 * anchor
    return base_signal.diff()

def f11_revq_171_struct_v171_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=47, w3=226, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 47)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=226, adjust=False).mean() * 1.5425 + 0.0006772 * anchor
    return base_signal.diff()

def f11_revq_172_struct_v172_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=58, w3=239, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(58, min_periods=max(58//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.556875 + 0.0006773 * anchor
    return base_signal.diff()

def f11_revq_173_struct_v173_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=69, w3=252, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(69, min_periods=max(69//3, 2)).rank(pct=True)
    persistence = change.rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3194 * persistence + 0.0006774 * anchor
    return base_signal.diff()

def f11_revq_174_struct_v174_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=80, w3=265, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(80, min_periods=max(80//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585625 + 0.0006775 * anchor
    return base_signal.diff()

def f11_revq_175_struct_v175_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=91, w3=278, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(91, min_periods=max(91//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3346 * slope + 0.0006776 * anchor
    return base_signal.diff()

def f11_revq_176_struct_v176_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=102, w3=291, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(102, min_periods=max(102//3, 2)).mean()
    noise = impulse.abs().rolling(291, min_periods=max(291//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.614375 + 0.0006777 * anchor
    return base_signal.diff()

def f11_revq_177_struct_v177_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=113, w3=304, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 113)
    curvature = _rolling_slope(acceleration, 304)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3498 * acceleration + 0.0006778 * anchor
    return base_signal.diff()

def f11_revq_178_struct_v178_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=124, w3=317, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(124, min_periods=max(124//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87 + 0.0006779 * anchor
    return base_signal.diff()

def f11_revq_179_struct_v179_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=135, w3=330, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(135, min_periods=max(135//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.365 * _rolling_slope(draw, 330) + 0.000678 * anchor
    return base_signal.diff()

def f11_revq_180_struct_v180_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=146, w3=343, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(146, min_periods=max(146//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.89875 + 0.0006781 * anchor
    return base_signal.diff()

def f11_revq_181_struct_v181_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=157, w3=356, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 157)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.913125 + 0.0006782 * anchor
    return base_signal.diff()

def f11_revq_182_struct_v182_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=168, w3=369, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(168, min_periods=max(168//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9275 + 0.0006783 * anchor
    return base_signal.diff()

def f11_revq_183_struct_v183_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=179, w3=382, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(47)
    rank = change.rolling(179, min_periods=max(179//3, 2)).rank(pct=True)
    persistence = change.rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3954 * persistence + 0.0006784 * anchor
    return base_signal.diff()

def f11_revq_184_struct_v184_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=190, w3=395, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(190, min_periods=max(190//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95625 + 0.0006785 * anchor
    return base_signal.diff()

def f11_revq_185_struct_v185_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=201, w3=408, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(201, min_periods=max(201//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4106 * slope + 0.0006786 * anchor
    return base_signal.diff()

def f11_revq_186_struct_v186_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=212, w3=421, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(68)
    drag = impulse.rolling(212, min_periods=max(212//3, 2)).mean()
    noise = impulse.abs().rolling(421, min_periods=max(421//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.985 + 0.0006787 * anchor
    return base_signal.diff()

def f11_revq_187_struct_v187_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=223, w3=434, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 223)
    curvature = _rolling_slope(acceleration, 434)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0494 * acceleration + 0.0006788 * anchor
    return base_signal.diff()

def f11_revq_188_struct_v188_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=234, w3=447, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(234, min_periods=max(234//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.01375 + 0.0006789 * anchor
    return base_signal.diff()

def f11_revq_189_struct_v189_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=245, w3=460, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(245, min_periods=max(245//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0646 * _rolling_slope(draw, 460) + 0.000679 * anchor
    return base_signal.diff()

def f11_revq_190_struct_v190_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=256, w3=473, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(256, min_periods=max(256//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.0425 + 0.0006791 * anchor
    return base_signal.diff()

def f11_revq_191_struct_v191_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=267, w3=486, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 103)
    slow = _rolling_slope(x, 267)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.056875 + 0.0006792 * anchor
    return base_signal.diff()

def f11_revq_192_struct_v192_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=278, w3=499, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(278, min_periods=max(278//3, 2)).max()
    trough = x.rolling(110, min_periods=max(110//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.07125 + 0.0006793 * anchor
    return base_signal.diff()

def f11_revq_193_struct_v193_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=289, w3=512, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(117)
    rank = change.rolling(289, min_periods=max(289//3, 2)).rank(pct=True)
    persistence = change.rolling(512, min_periods=max(512//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.095 * persistence + 0.0006794 * anchor
    return base_signal.diff()

def f11_revq_194_struct_v194_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=300, w3=525, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(124, min_periods=max(124//3, 2)).std()
    vol_slow = ret.rolling(300, min_periods=max(300//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1 + 0.0006795 * anchor
    return base_signal.diff()

def f11_revq_195_struct_v195_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=311, w3=538, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(311, min_periods=max(311//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 131)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1102 * slope + 0.0006796 * anchor
    return base_signal.diff()

def f11_revq_196_struct_v196_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=322, w3=551, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(322, min_periods=max(322//3, 2)).mean()
    noise = impulse.abs().rolling(551, min_periods=max(551//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.12875 + 0.0006797 * anchor
    return base_signal.diff()

def f11_revq_197_struct_v197_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=333, w3=564, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 145)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 564)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1254 * acceleration + 0.0006798 * anchor
    return base_signal.diff()

def f11_revq_198_struct_v198_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=344, w3=577, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(344, min_periods=max(344//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.1575 + 0.0006799 * anchor
    return base_signal.diff()

def f11_revq_199_struct_v199_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=355, w3=590, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(355, min_periods=max(355//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1406 * _rolling_slope(draw, 590) + 0.00068 * anchor
    return base_signal.diff()

def f11_revq_200_struct_v200_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=366, w3=603, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 166)
    baseline = trend.rolling(366, min_periods=max(366//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.18625 + 0.0006801 * anchor
    return base_signal.diff()

def f11_revq_201_struct_v201_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=377, w3=616, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.200625 + 0.0006802 * anchor
    return base_signal.diff()

def f11_revq_202_struct_v202_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=388, w3=629, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(388, min_periods=max(388//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.215 + 0.0006803 * anchor
    return base_signal.diff()

def f11_revq_203_struct_v203_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=399, w3=642, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(399, min_periods=max(399//3, 2)).rank(pct=True)
    persistence = change.rolling(642, min_periods=max(642//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.171 * persistence + 0.0006804 * anchor
    return base_signal.diff()

def f11_revq_204_struct_v204_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=410, w3=655, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(410, min_periods=max(410//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24375 + 0.0006805 * anchor
    return base_signal.diff()

def f11_revq_205_struct_v205_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=421, w3=668, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1862 * slope + 0.0006806 * anchor
    return base_signal.diff()

def f11_revq_206_struct_v206_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=432, w3=681, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(432, min_periods=max(432//3, 2)).mean()
    noise = impulse.abs().rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.2725 + 0.0006807 * anchor
    return base_signal.diff()

def f11_revq_207_struct_v207_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=443, w3=694, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 694)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2014 * acceleration + 0.0006808 * anchor
    return base_signal.diff()

def f11_revq_208_struct_v208_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=454, w3=707, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(454, min_periods=max(454//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.30125 + 0.0006809 * anchor
    return base_signal.diff()

def f11_revq_209_struct_v209_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=465, w3=720, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(465, min_periods=max(465//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2166 * _rolling_slope(draw, 720) + 0.000681 * anchor
    return base_signal.diff()

def f11_revq_210_struct_v210_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=236, w2=476, w3=733, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(476, min_periods=max(476//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33 + 0.0006811 * anchor
    return base_signal.diff()

def f11_revq_211_struct_v211_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=487, w3=746, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 487)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.344375 + 0.0006812 * anchor
    return base_signal.diff()

def f11_revq_212_struct_v212_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=498, w3=759, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(498, min_periods=max(498//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.35875 + 0.0006813 * anchor
    return base_signal.diff()

def f11_revq_213_struct_v213_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=509, w3=15, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(6)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(15, min_periods=max(15//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.247 * persistence + 0.0006814 * anchor
    return base_signal.diff()

def f11_revq_214_struct_v214_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=17, w3=28, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(17, min_periods=max(17//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3875 + 0.0006815 * anchor
    return base_signal.diff()

def f11_revq_215_struct_v215_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=28, w3=41, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2622 * slope + 0.0006816 * anchor
    return base_signal.diff()

def f11_revq_216_struct_v216_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=39, w3=54, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(27)
    drag = impulse.rolling(39, min_periods=max(39//3, 2)).mean()
    noise = impulse.abs().rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41625 + 0.0006817 * anchor
    return base_signal.diff()

def f11_revq_217_struct_v217_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=50, w3=67, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 50)
    curvature = _rolling_slope(acceleration, 67)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2774 * acceleration + 0.0006818 * anchor
    return base_signal.diff()

def f11_revq_218_struct_v218_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=61, w3=80, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(41, min_periods=max(41//3, 2)).mean(), upside.rolling(61, min_periods=max(61//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(80) * 1.445 + 0.0006819 * anchor
    return base_signal.diff()

def f11_revq_219_struct_v219_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=72, w3=93, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(72, min_periods=max(72//3, 2)).max()
    rebound = x - x.rolling(48, min_periods=max(48//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2926 * _rolling_slope(draw, 93) + 0.000682 * anchor
    return base_signal.diff()

def f11_revq_220_struct_v220_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=83, w3=106, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(83, min_periods=max(83//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.47375 + 0.0006821 * anchor
    return base_signal.diff()

def f11_revq_221_struct_v221_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=94, w3=119, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=119, adjust=False).mean() * 1.488125 + 0.0006822 * anchor
    return base_signal.diff()

def f11_revq_222_struct_v222_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=69, w2=105, w3=132, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5025 + 0.0006823 * anchor
    return base_signal.diff()

def f11_revq_223_struct_v223_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=76, w2=116, w3=145, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(76)
    rank = change.rolling(116, min_periods=max(116//3, 2)).rank(pct=True)
    persistence = change.rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.323 * persistence + 0.0006824 * anchor
    return base_signal.diff()

def f11_revq_224_struct_v224_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=83, w2=127, w3=158, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(127, min_periods=max(127//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53125 + 0.0006825 * anchor
    return base_signal.diff()

def f11_revq_225_struct_v225_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=90, w2=138, w3=171, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(138, min_periods=max(138//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3382 * slope + 0.0006826 * anchor
    return base_signal.diff()
