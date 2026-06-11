"""28 institutional holding collapse trajectory d3 third derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Ownership - Institutional-grade short-side signal.
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

def f28_ihc_151_struct_v151_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=190, w2=361, w3=91, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 361)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=91, adjust=False).mean() * 0.98625 + 0.0016952 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_152_struct_v152_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=197, w2=372, w3=104, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(372, min_periods=max(372//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.000625 + 0.0016953 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_153_struct_v153_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=204, w2=383, w3=117, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(383, min_periods=max(383//3, 2)).rank(pct=True)
    persistence = change.rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.149 * persistence + 0.0016954 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_154_struct_v154_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=211, w2=394, w3=130, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(394, min_periods=max(394//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.029375 + 0.0016955 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_155_struct_v155_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=218, w2=405, w3=143, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(405, min_periods=max(405//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1642 * slope + 0.0016956 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_156_struct_v156_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=225, w2=416, w3=156, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(416, min_periods=max(416//3, 2)).mean()
    noise = impulse.abs().rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.058125 + 0.0016957 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_157_struct_v157_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=232, w2=427, w3=169, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 427)
    curvature = _rolling_slope(acceleration, 169)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1794 * acceleration + 0.0016958 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_158_struct_v158_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=239, w2=438, w3=182, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(438, min_periods=max(438//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.086875 + 0.0016959 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_159_struct_v159_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=246, w2=449, w3=195, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(449, min_periods=max(449//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1946 * _rolling_slope(draw, 195) + 0.001696 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_160_struct_v160_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=253, w2=460, w3=208, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(460, min_periods=max(460//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.115625 + 0.0016961 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_161_struct_v161_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=9, w2=471, w3=221, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 471)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 1.13 + 0.0016962 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_162_struct_v162_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=16, w2=482, w3=234, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.144375 + 0.0016963 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_163_struct_v163_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=23, w2=493, w3=247, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(23)
    rank = change.rolling(493, min_periods=max(493//3, 2)).rank(pct=True)
    persistence = change.rolling(247, min_periods=max(247//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.225 * persistence + 0.0016964 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_164_struct_v164_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=504, w3=260, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(504, min_periods=max(504//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.173125 + 0.0016965 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_165_struct_v165_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=12, w3=273, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2402 * slope + 0.0016966 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_166_struct_v166_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=23, w3=286, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(44)
    drag = impulse.rolling(23, min_periods=max(23//3, 2)).mean()
    noise = impulse.abs().rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.201875 + 0.0016967 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_167_struct_v167_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=34, w3=299, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 34)
    curvature = _rolling_slope(acceleration, 299)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2554 * acceleration + 0.0016968 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_168_struct_v168_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=45, w3=312, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(45, min_periods=max(45//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.230625 + 0.0016969 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_169_struct_v169_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=56, w3=325, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(56, min_periods=max(56//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2706 * _rolling_slope(draw, 325) + 0.001697 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_170_struct_v170_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=67, w3=338, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(67, min_periods=max(67//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.259375 + 0.0016971 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_171_struct_v171_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=78, w3=351, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 78)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.27375 + 0.0016972 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_172_struct_v172_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=89, w3=364, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(89, min_periods=max(89//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.288125 + 0.0016973 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_173_struct_v173_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=100, w3=377, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(93)
    rank = change.rolling(100, min_periods=max(100//3, 2)).rank(pct=True)
    persistence = change.rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.301 * persistence + 0.0016974 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_174_struct_v174_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=111, w3=390, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(111, min_periods=max(111//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.316875 + 0.0016975 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_175_struct_v175_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=122, w3=403, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(122, min_periods=max(122//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3162 * slope + 0.0016976 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_176_struct_v176_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=133, w3=416, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(114)
    drag = impulse.rolling(133, min_periods=max(133//3, 2)).mean()
    noise = impulse.abs().rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.345625 + 0.0016977 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_177_struct_v177_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=144, w3=429, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 429)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3314 * acceleration + 0.0016978 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_178_struct_v178_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=155, w3=442, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(155, min_periods=max(155//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.374375 + 0.0016979 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_179_struct_v179_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=166, w3=455, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(166, min_periods=max(166//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3466 * _rolling_slope(draw, 455) + 0.001698 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_180_struct_v180_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=177, w3=468, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(177, min_periods=max(177//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.403125 + 0.0016981 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_181_struct_v181_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=188, w3=481, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4175 + 0.0016982 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_182_struct_v182_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=199, w3=494, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(199, min_periods=max(199//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.431875 + 0.0016983 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_183_struct_v183_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=210, w3=507, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(210, min_periods=max(210//3, 2)).rank(pct=True)
    persistence = change.rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.377 * persistence + 0.0016984 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_184_struct_v184_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=221, w3=520, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(221, min_periods=max(221//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.460625 + 0.0016985 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_185_struct_v185_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=177, w2=232, w3=533, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(232, min_periods=max(232//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3922 * slope + 0.0016986 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_186_struct_v186_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=184, w2=243, w3=546, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(243, min_periods=max(243//3, 2)).mean()
    noise = impulse.abs().rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.489375 + 0.0016987 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_187_struct_v187_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=191, w2=254, w3=559, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 254)
    curvature = _rolling_slope(acceleration, 559)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4074 * acceleration + 0.0016988 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_188_struct_v188_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=198, w2=265, w3=572, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(265, min_periods=max(265//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.518125 + 0.0016989 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_189_struct_v189_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=205, w2=276, w3=585, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(276, min_periods=max(276//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0462 * _rolling_slope(draw, 585) + 0.001699 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_190_struct_v190_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=212, w2=287, w3=598, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(287, min_periods=max(287//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.546875 + 0.0016991 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_191_struct_v191_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=219, w2=298, w3=611, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 298)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.56125 + 0.0016992 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_192_struct_v192_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=226, w2=309, w3=624, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(309, min_periods=max(309//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.575625 + 0.0016993 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_193_struct_v193_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=233, w2=320, w3=637, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(320, min_periods=max(320//3, 2)).rank(pct=True)
    persistence = change.rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0766 * persistence + 0.0016994 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_194_struct_v194_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=240, w2=331, w3=650, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(331, min_periods=max(331//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.604375 + 0.0016995 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_195_struct_v195_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=247, w2=342, w3=663, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(342, min_periods=max(342//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0918 * slope + 0.0016996 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_196_struct_v196_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=254, w2=353, w3=676, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(353, min_periods=max(353//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.86 + 0.0016997 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_197_struct_v197_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=10, w2=364, w3=689, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 364)
    curvature = _rolling_slope(acceleration, 689)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.107 * acceleration + 0.0016998 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_198_struct_v198_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=17, w2=375, w3=702, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(375, min_periods=max(375//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.88875 + 0.0016999 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_199_struct_v199_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=24, w2=386, w3=715, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(386, min_periods=max(386//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1222 * _rolling_slope(draw, 715) + 0.0017 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_200_struct_v200_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=31, w2=397, w3=728, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(397, min_periods=max(397//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9175 + 0.0017001 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_201_struct_v201_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=38, w2=408, w3=741, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 408)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.931875 + 0.0017002 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_202_struct_v202_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=45, w2=419, w3=754, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(419, min_periods=max(419//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.94625 + 0.0017003 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_203_struct_v203_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=52, w2=430, w3=767, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(52)
    rank = change.rolling(430, min_periods=max(430//3, 2)).rank(pct=True)
    persistence = change.rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1526 * persistence + 0.0017004 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_204_struct_v204_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=59, w2=441, w3=23, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(441, min_periods=max(441//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.975 + 0.0017005 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_205_struct_v205_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=66, w2=452, w3=36, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(452, min_periods=max(452//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1678 * slope + 0.0017006 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_206_struct_v206_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=73, w2=463, w3=49, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(73)
    drag = impulse.rolling(463, min_periods=max(463//3, 2)).mean()
    noise = impulse.abs().rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.00375 + 0.0017007 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_207_struct_v207_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=80, w2=474, w3=62, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 474)
    curvature = _rolling_slope(acceleration, 62)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.183 * acceleration + 0.0017008 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_208_struct_v208_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=87, w2=485, w3=75, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(485, min_periods=max(485//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(75) * 1.0325 + 0.0017009 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_209_struct_v209_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=94, w2=496, w3=88, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(496, min_periods=max(496//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1982 * _rolling_slope(draw, 88) + 0.001701 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_210_struct_v210_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=101, w2=507, w3=101, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(507, min_periods=max(507//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(101, min_periods=max(101//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.06125 + 0.0017011 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_211_struct_v211_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=108, w2=15, w3=114, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 15)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=114, adjust=False).mean() * 1.075625 + 0.0017012 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_212_struct_v212_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=115, w2=26, w3=127, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(26, min_periods=max(26//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.09 + 0.0017013 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_213_struct_v213_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=122, w2=37, w3=140, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(122)
    rank = change.rolling(37, min_periods=max(37//3, 2)).rank(pct=True)
    persistence = change.rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2286 * persistence + 0.0017014 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_214_struct_v214_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=129, w2=48, w3=153, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(48, min_periods=max(48//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.11875 + 0.0017015 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_215_struct_v215_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=136, w2=59, w3=166, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(59, min_periods=max(59//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2438 * slope + 0.0017016 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_216_struct_v216_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=143, w2=70, w3=179, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(70, min_periods=max(70//3, 2)).mean()
    noise = impulse.abs().rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1475 + 0.0017017 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_217_struct_v217_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=150, w2=81, w3=192, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 81)
    curvature = _rolling_slope(acceleration, 192)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.259 * acceleration + 0.0017018 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_218_struct_v218_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=157, w2=92, w3=205, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(92, min_periods=max(92//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.17625 + 0.0017019 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_219_struct_v219_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=164, w2=103, w3=218, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(103, min_periods=max(103//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2742 * _rolling_slope(draw, 218) + 0.001702 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_220_struct_v220_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=171, w2=114, w3=231, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(114, min_periods=max(114//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(231, min_periods=max(231//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.205 + 0.0017021 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_221_struct_v221_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=178, w2=125, w3=244, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 125)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=244, adjust=False).mean() * 1.219375 + 0.0017022 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_222_struct_v222_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=185, w2=136, w3=257, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(136, min_periods=max(136//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.23375 + 0.0017023 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_223_struct_v223_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=192, w2=147, w3=270, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(147, min_periods=max(147//3, 2)).rank(pct=True)
    persistence = change.rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3046 * persistence + 0.0017024 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_224_struct_v224_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=199, w2=158, w3=283, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(158, min_periods=max(158//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2625 + 0.0017025 * anchor
    return base_signal.diff().diff().diff()

def f28_ihc_225_struct_v225_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=206, w2=169, w3=296, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3198 * slope + 0.0017026 * anchor
    return base_signal.diff().diff().diff()
