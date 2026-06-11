"""23 cash flow deterioration trajectory base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f23_cfd_151_struct_v151(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=56, w3=455, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 56)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.15625 + 0.0013952 * anchor

def f23_cfd_152_struct_v152(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=67, w3=468, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(67, min_periods=max(67//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.170625 + 0.0013953 * anchor

def f23_cfd_153_struct_v153(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=78, w3=481, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(37)
    rank = change.rolling(78, min_periods=max(78//3, 2)).rank(pct=True)
    persistence = change.rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3094 * persistence + 0.0013954 * anchor

def f23_cfd_154_struct_v154(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=89, w3=494, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(89, min_periods=max(89//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.199375 + 0.0013955 * anchor

def f23_cfd_155_struct_v155(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=100, w3=507, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(100, min_periods=max(100//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3246 * slope + 0.0013956 * anchor

def f23_cfd_156_struct_v156(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=111, w3=520, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(58)
    drag = impulse.rolling(111, min_periods=max(111//3, 2)).mean()
    noise = impulse.abs().rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.228125 + 0.0013957 * anchor

def f23_cfd_157_struct_v157(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=122, w3=533, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 122)
    curvature = _rolling_slope(acceleration, 533)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3398 * acceleration + 0.0013958 * anchor

def f23_cfd_158_struct_v158(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=133, w3=546, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(72, min_periods=max(72//3, 2)).mean(), upside.rolling(133, min_periods=max(133//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.256875 + 0.0013959 * anchor

def f23_cfd_159_struct_v159(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=144, w3=559, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(144, min_periods=max(144//3, 2)).max()
    rebound = x - x.rolling(79, min_periods=max(79//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.355 * _rolling_slope(draw, 559) + 0.001396 * anchor

def f23_cfd_160_struct_v160(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=155, w3=572, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(155, min_periods=max(155//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.285625 + 0.0013961 * anchor

def f23_cfd_161_struct_v161(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=166, w3=585, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 93)
    slow = _rolling_slope(x, 166)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3 + 0.0013962 * anchor

def f23_cfd_162_struct_v162(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=177, w3=598, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(177, min_periods=max(177//3, 2)).max()
    trough = x.rolling(100, min_periods=max(100//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.314375 + 0.0013963 * anchor

def f23_cfd_163_struct_v163(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=188, w3=611, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(107)
    rank = change.rolling(188, min_periods=max(188//3, 2)).rank(pct=True)
    persistence = change.rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3854 * persistence + 0.0013964 * anchor

def f23_cfd_164_struct_v164(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=199, w3=624, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(114, min_periods=max(114//3, 2)).std()
    vol_slow = ret.rolling(199, min_periods=max(199//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.343125 + 0.0013965 * anchor

def f23_cfd_165_struct_v165(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=210, w3=637, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(210, min_periods=max(210//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 121)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4006 * slope + 0.0013966 * anchor

def f23_cfd_166_struct_v166(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=221, w3=650, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(221, min_periods=max(221//3, 2)).mean()
    noise = impulse.abs().rolling(650, min_periods=max(650//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.371875 + 0.0013967 * anchor

def f23_cfd_167_struct_v167(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=232, w3=663, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 135)
    acceleration = _rolling_slope(velocity, 232)
    curvature = _rolling_slope(acceleration, 663)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0394 * acceleration + 0.0013968 * anchor

def f23_cfd_168_struct_v168(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=243, w3=676, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(243, min_periods=max(243//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.400625 + 0.0013969 * anchor

def f23_cfd_169_struct_v169(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=254, w3=689, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(254, min_periods=max(254//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0546 * _rolling_slope(draw, 689) + 0.001397 * anchor

def f23_cfd_170_struct_v170(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=265, w3=702, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(265, min_periods=max(265//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.429375 + 0.0013971 * anchor

def f23_cfd_171_struct_v171(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=276, w3=715, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 276)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.44375 + 0.0013972 * anchor

def f23_cfd_172_struct_v172(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=287, w3=728, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.458125 + 0.0013973 * anchor

def f23_cfd_173_struct_v173(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=298, w3=741, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(298, min_periods=max(298//3, 2)).rank(pct=True)
    persistence = change.rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.085 * persistence + 0.0013974 * anchor

def f23_cfd_174_struct_v174(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=309, w3=754, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(309, min_periods=max(309//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.486875 + 0.0013975 * anchor

def f23_cfd_175_struct_v175(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=320, w3=767, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(320, min_periods=max(320//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1002 * slope + 0.0013976 * anchor

def f23_cfd_176_struct_v176(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=331, w3=23, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(331, min_periods=max(331//3, 2)).mean()
    noise = impulse.abs().rolling(23, min_periods=max(23//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.515625 + 0.0013977 * anchor

def f23_cfd_177_struct_v177(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=342, w3=36, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 342)
    curvature = _rolling_slope(acceleration, 36)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1154 * acceleration + 0.0013978 * anchor

def f23_cfd_178_struct_v178(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=353, w3=49, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(212, min_periods=max(212//3, 2)).mean(), upside.rolling(353, min_periods=max(353//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(49) * 1.544375 + 0.0013979 * anchor

def f23_cfd_179_struct_v179(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=364, w3=62, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(219, min_periods=max(219//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1306 * _rolling_slope(draw, 62) + 0.001398 * anchor

def f23_cfd_180_struct_v180(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=375, w3=75, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(375, min_periods=max(375//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.573125 + 0.0013981 * anchor

def f23_cfd_181_struct_v181(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=386, w3=88, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 386)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=88, adjust=False).mean() * 1.5875 + 0.0013982 * anchor

def f23_cfd_182_struct_v182(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=397, w3=101, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(397, min_periods=max(397//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.601875 + 0.0013983 * anchor

def f23_cfd_183_struct_v183(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=408, w3=114, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(408, min_periods=max(408//3, 2)).rank(pct=True)
    persistence = change.rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.161 * persistence + 0.0013984 * anchor

def f23_cfd_184_struct_v184(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=419, w3=127, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(419, min_periods=max(419//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8575 + 0.0013985 * anchor

def f23_cfd_185_struct_v185(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=430, w3=140, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(430, min_periods=max(430//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1762 * slope + 0.0013986 * anchor

def f23_cfd_186_struct_v186(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=441, w3=153, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(17)
    drag = impulse.rolling(441, min_periods=max(441//3, 2)).mean()
    noise = impulse.abs().rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88625 + 0.0013987 * anchor

def f23_cfd_187_struct_v187(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=452, w3=166, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 452)
    curvature = _rolling_slope(acceleration, 166)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1914 * acceleration + 0.0013988 * anchor

def f23_cfd_188_struct_v188(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=463, w3=179, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(463, min_periods=max(463//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.915 + 0.0013989 * anchor

def f23_cfd_189_struct_v189(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=474, w3=192, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(474, min_periods=max(474//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2066 * _rolling_slope(draw, 192) + 0.001399 * anchor

def f23_cfd_190_struct_v190(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=485, w3=205, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(485, min_periods=max(485//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.94375 + 0.0013991 * anchor

def f23_cfd_191_struct_v191(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=496, w3=218, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=218, adjust=False).mean() * 0.958125 + 0.0013992 * anchor

def f23_cfd_192_struct_v192(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=507, w3=231, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(507, min_periods=max(507//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9725 + 0.0013993 * anchor

def f23_cfd_193_struct_v193(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=15, w3=244, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(66)
    rank = change.rolling(15, min_periods=max(15//3, 2)).rank(pct=True)
    persistence = change.rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.237 * persistence + 0.0013994 * anchor

def f23_cfd_194_struct_v194(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=26, w3=257, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(26, min_periods=max(26//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.00125 + 0.0013995 * anchor

def f23_cfd_195_struct_v195(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=37, w3=270, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(37, min_periods=max(37//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2522 * slope + 0.0013996 * anchor

def f23_cfd_196_struct_v196(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=48, w3=283, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(87)
    drag = impulse.rolling(48, min_periods=max(48//3, 2)).mean()
    noise = impulse.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.03 + 0.0013997 * anchor

def f23_cfd_197_struct_v197(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=59, w3=296, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 59)
    curvature = _rolling_slope(acceleration, 296)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2674 * acceleration + 0.0013998 * anchor

def f23_cfd_198_struct_v198(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=70, w3=309, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(70, min_periods=max(70//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05875 + 0.0013999 * anchor

def f23_cfd_199_struct_v199(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=81, w3=322, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(81, min_periods=max(81//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2826 * _rolling_slope(draw, 322) + 0.0014 * anchor

def f23_cfd_200_struct_v200(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=92, w3=335, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(92, min_periods=max(92//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0875 + 0.0014001 * anchor

def f23_cfd_201_struct_v201(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=103, w3=348, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 103)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.101875 + 0.0014002 * anchor

def f23_cfd_202_struct_v202(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=114, w3=361, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(114, min_periods=max(114//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11625 + 0.0014003 * anchor

def f23_cfd_203_struct_v203(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=125, w3=374, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(125, min_periods=max(125//3, 2)).rank(pct=True)
    persistence = change.rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.313 * persistence + 0.0014004 * anchor

def f23_cfd_204_struct_v204(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=136, w3=387, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(136, min_periods=max(136//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.145 + 0.0014005 * anchor

def f23_cfd_205_struct_v205(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=147, w3=400, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(147, min_periods=max(147//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3282 * slope + 0.0014006 * anchor

def f23_cfd_206_struct_v206(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=158, w3=413, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(158, min_periods=max(158//3, 2)).mean()
    noise = impulse.abs().rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.17375 + 0.0014007 * anchor

def f23_cfd_207_struct_v207(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=169, w3=426, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 169)
    curvature = _rolling_slope(acceleration, 426)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3434 * acceleration + 0.0014008 * anchor

def f23_cfd_208_struct_v208(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=180, w3=439, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(180, min_periods=max(180//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2025 + 0.0014009 * anchor

def f23_cfd_209_struct_v209(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=191, w3=452, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(191, min_periods=max(191//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3586 * _rolling_slope(draw, 452) + 0.001401 * anchor

def f23_cfd_210_struct_v210(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=202, w3=465, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(202, min_periods=max(202//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.23125 + 0.0014011 * anchor

def f23_cfd_211_struct_v211(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=213, w3=478, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 213)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.245625 + 0.0014012 * anchor

def f23_cfd_212_struct_v212(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=224, w3=491, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(224, min_periods=max(224//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.26 + 0.0014013 * anchor

def f23_cfd_213_struct_v213(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=235, w3=504, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(235, min_periods=max(235//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.389 * persistence + 0.0014014 * anchor

def f23_cfd_214_struct_v214(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=246, w3=517, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(246, min_periods=max(246//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28875 + 0.0014015 * anchor

def f23_cfd_215_struct_v215(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=257, w3=530, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(257, min_periods=max(257//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4042 * slope + 0.0014016 * anchor

def f23_cfd_216_struct_v216(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=268, w3=543, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(268, min_periods=max(268//3, 2)).mean()
    noise = impulse.abs().rolling(543, min_periods=max(543//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3175 + 0.0014017 * anchor

def f23_cfd_217_struct_v217(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=279, w3=556, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 279)
    curvature = _rolling_slope(acceleration, 556)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.043 * acceleration + 0.0014018 * anchor

def f23_cfd_218_struct_v218(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=290, w3=569, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(290, min_periods=max(290//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.34625 + 0.0014019 * anchor

def f23_cfd_219_struct_v219(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=301, w3=582, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(301, min_periods=max(301//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0582 * _rolling_slope(draw, 582) + 0.001402 * anchor

def f23_cfd_220_struct_v220(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=312, w3=595, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 255)
    baseline = trend.rolling(312, min_periods=max(312//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.375 + 0.0014021 * anchor

def f23_cfd_221_struct_v221(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=323, w3=608, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 11)
    slow = _rolling_slope(x, 323)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.389375 + 0.0014022 * anchor

def f23_cfd_222_struct_v222(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=334, w3=621, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(334, min_periods=max(334//3, 2)).max()
    trough = x.rolling(18, min_periods=max(18//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.40375 + 0.0014023 * anchor

def f23_cfd_223_struct_v223(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=345, w3=634, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(25)
    rank = change.rolling(345, min_periods=max(345//3, 2)).rank(pct=True)
    persistence = change.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0886 * persistence + 0.0014024 * anchor

def f23_cfd_224_struct_v224(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=356, w3=647, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(32, min_periods=max(32//3, 2)).std()
    vol_slow = ret.rolling(356, min_periods=max(356//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4325 + 0.0014025 * anchor

def f23_cfd_225_struct_v225(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=367, w3=660, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(367, min_periods=max(367//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 39)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1038 * slope + 0.0014026 * anchor
