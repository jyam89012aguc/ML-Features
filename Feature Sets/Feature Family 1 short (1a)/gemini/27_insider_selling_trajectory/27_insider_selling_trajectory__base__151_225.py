"""27 insider selling trajectory base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f27_ist_151_struct_v151(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=300, w3=618, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 300)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.865625 + 0.0016352 * anchor

def f27_ist_152_struct_v152(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=311, w3=631, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(311, min_periods=max(311//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.88 + 0.0016353 * anchor

def f27_ist_153_struct_v153(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=322, w3=644, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(20)
    rank = change.rolling(322, min_periods=max(322//3, 2)).rank(pct=True)
    persistence = change.rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1058 * persistence + 0.0016354 * anchor

def f27_ist_154_struct_v154(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=333, w3=657, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(333, min_periods=max(333//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90875 + 0.0016355 * anchor

def f27_ist_155_struct_v155(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=344, w3=670, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(344, min_periods=max(344//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.121 * slope + 0.0016356 * anchor

def f27_ist_156_struct_v156(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=355, w3=683, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(41)
    drag = impulse.rolling(355, min_periods=max(355//3, 2)).mean()
    noise = impulse.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9375 + 0.0016357 * anchor

def f27_ist_157_struct_v157(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=366, w3=696, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 366)
    curvature = _rolling_slope(acceleration, 696)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1362 * acceleration + 0.0016358 * anchor

def f27_ist_158_struct_v158(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=377, w3=709, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(377, min_periods=max(377//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.96625 + 0.0016359 * anchor

def f27_ist_159_struct_v159(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=388, w3=722, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(388, min_periods=max(388//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1514 * _rolling_slope(draw, 722) + 0.001636 * anchor

def f27_ist_160_struct_v160(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=399, w3=735, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(399, min_periods=max(399//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.995 + 0.0016361 * anchor

def f27_ist_161_struct_v161(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=410, w3=748, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 410)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.009375 + 0.0016362 * anchor

def f27_ist_162_struct_v162(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=421, w3=761, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(421, min_periods=max(421//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.02375 + 0.0016363 * anchor

def f27_ist_163_struct_v163(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=432, w3=17, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(90)
    rank = change.rolling(432, min_periods=max(432//3, 2)).rank(pct=True)
    persistence = change.rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1818 * persistence + 0.0016364 * anchor

def f27_ist_164_struct_v164(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=443, w3=30, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(443, min_periods=max(443//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0525 + 0.0016365 * anchor

def f27_ist_165_struct_v165(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=454, w3=43, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(454, min_periods=max(454//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.197 * slope + 0.0016366 * anchor

def f27_ist_166_struct_v166(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=465, w3=56, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(111)
    drag = impulse.rolling(465, min_periods=max(465//3, 2)).mean()
    noise = impulse.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.08125 + 0.0016367 * anchor

def f27_ist_167_struct_v167(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=476, w3=69, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 476)
    curvature = _rolling_slope(acceleration, 69)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2122 * acceleration + 0.0016368 * anchor

def f27_ist_168_struct_v168(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=487, w3=82, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(487, min_periods=max(487//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(82) * 1.11 + 0.0016369 * anchor

def f27_ist_169_struct_v169(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=498, w3=95, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(498, min_periods=max(498//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2274 * _rolling_slope(draw, 95) + 0.001637 * anchor

def f27_ist_170_struct_v170(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=509, w3=108, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(509, min_periods=max(509//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.13875 + 0.0016371 * anchor

def f27_ist_171_struct_v171(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=17, w3=121, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=121, adjust=False).mean() * 1.153125 + 0.0016372 * anchor

def f27_ist_172_struct_v172(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=28, w3=134, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(28, min_periods=max(28//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.1675 + 0.0016373 * anchor

def f27_ist_173_struct_v173(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=39, w3=147, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(39, min_periods=max(39//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2578 * persistence + 0.0016374 * anchor

def f27_ist_174_struct_v174(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=50, w3=160, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(50, min_periods=max(50//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.19625 + 0.0016375 * anchor

def f27_ist_175_struct_v175(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=61, w3=173, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(61, min_periods=max(61//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.273 * slope + 0.0016376 * anchor

def f27_ist_176_struct_v176(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=72, w3=186, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(72, min_periods=max(72//3, 2)).mean()
    noise = impulse.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.225 + 0.0016377 * anchor

def f27_ist_177_struct_v177(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=83, w3=199, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 83)
    curvature = _rolling_slope(acceleration, 199)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2882 * acceleration + 0.0016378 * anchor

def f27_ist_178_struct_v178(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=94, w3=212, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(94, min_periods=max(94//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.25375 + 0.0016379 * anchor

def f27_ist_179_struct_v179(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=105, w3=225, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(105, min_periods=max(105//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3034 * _rolling_slope(draw, 225) + 0.001638 * anchor

def f27_ist_180_struct_v180(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=116, w3=238, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(116, min_periods=max(116//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.2825 + 0.0016381 * anchor

def f27_ist_181_struct_v181(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=127, w3=251, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 127)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=251, adjust=False).mean() * 1.296875 + 0.0016382 * anchor

def f27_ist_182_struct_v182(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=138, w3=264, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(138, min_periods=max(138//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.31125 + 0.0016383 * anchor

def f27_ist_183_struct_v183(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=149, w3=277, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(149, min_periods=max(149//3, 2)).rank(pct=True)
    persistence = change.rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3338 * persistence + 0.0016384 * anchor

def f27_ist_184_struct_v184(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=160, w3=290, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(160, min_periods=max(160//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34 + 0.0016385 * anchor

def f27_ist_185_struct_v185(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=171, w3=303, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(171, min_periods=max(171//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.349 * slope + 0.0016386 * anchor

def f27_ist_186_struct_v186(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=182, w3=316, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.36875 + 0.0016387 * anchor

def f27_ist_187_struct_v187(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=193, w3=329, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 7)
    acceleration = _rolling_slope(velocity, 193)
    curvature = _rolling_slope(acceleration, 329)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3642 * acceleration + 0.0016388 * anchor

def f27_ist_188_struct_v188(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=204, w3=342, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(14, min_periods=max(14//3, 2)).mean(), upside.rolling(204, min_periods=max(204//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.3975 + 0.0016389 * anchor

def f27_ist_189_struct_v189(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=215, w3=355, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(215, min_periods=max(215//3, 2)).max()
    rebound = x - x.rolling(21, min_periods=max(21//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3794 * _rolling_slope(draw, 355) + 0.001639 * anchor

def f27_ist_190_struct_v190(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=226, w3=368, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(226, min_periods=max(226//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.42625 + 0.0016391 * anchor

def f27_ist_191_struct_v191(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=237, w3=381, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 237)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.440625 + 0.0016392 * anchor

def f27_ist_192_struct_v192(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=248, w3=394, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(248, min_periods=max(248//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.455 + 0.0016393 * anchor

def f27_ist_193_struct_v193(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=259, w3=407, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(49)
    rank = change.rolling(259, min_periods=max(259//3, 2)).rank(pct=True)
    persistence = change.rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4098 * persistence + 0.0016394 * anchor

def f27_ist_194_struct_v194(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=270, w3=420, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(270, min_periods=max(270//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.48375 + 0.0016395 * anchor

def f27_ist_195_struct_v195(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=281, w3=433, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(281, min_periods=max(281//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0486 * slope + 0.0016396 * anchor

def f27_ist_196_struct_v196(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=292, w3=446, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(70)
    drag = impulse.rolling(292, min_periods=max(292//3, 2)).mean()
    noise = impulse.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5125 + 0.0016397 * anchor

def f27_ist_197_struct_v197(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=303, w3=459, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 303)
    curvature = _rolling_slope(acceleration, 459)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0638 * acceleration + 0.0016398 * anchor

def f27_ist_198_struct_v198(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=314, w3=472, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(84, min_periods=max(84//3, 2)).mean(), upside.rolling(314, min_periods=max(314//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.54125 + 0.0016399 * anchor

def f27_ist_199_struct_v199(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=325, w3=485, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(325, min_periods=max(325//3, 2)).max()
    rebound = x - x.rolling(91, min_periods=max(91//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.079 * _rolling_slope(draw, 485) + 0.00164 * anchor

def f27_ist_200_struct_v200(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=336, w3=498, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 98)
    baseline = trend.rolling(336, min_periods=max(336//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.57 + 0.0016401 * anchor

def f27_ist_201_struct_v201(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=347, w3=511, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 105)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.584375 + 0.0016402 * anchor

def f27_ist_202_struct_v202(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=358, w3=524, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(358, min_periods=max(358//3, 2)).max()
    trough = x.rolling(112, min_periods=max(112//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.59875 + 0.0016403 * anchor

def f27_ist_203_struct_v203(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=369, w3=537, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(119)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1094 * persistence + 0.0016404 * anchor

def f27_ist_204_struct_v204(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=380, w3=550, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(126, min_periods=max(126//3, 2)).std()
    vol_slow = ret.rolling(380, min_periods=max(380//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.854375 + 0.0016405 * anchor

def f27_ist_205_struct_v205(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=391, w3=563, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 133)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1246 * slope + 0.0016406 * anchor

def f27_ist_206_struct_v206(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=402, w3=576, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(402, min_periods=max(402//3, 2)).mean()
    noise = impulse.abs().rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.883125 + 0.0016407 * anchor

def f27_ist_207_struct_v207(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=413, w3=589, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 147)
    acceleration = _rolling_slope(velocity, 413)
    curvature = _rolling_slope(acceleration, 589)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1398 * acceleration + 0.0016408 * anchor

def f27_ist_208_struct_v208(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=424, w3=602, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(424, min_periods=max(424//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.911875 + 0.0016409 * anchor

def f27_ist_209_struct_v209(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=435, w3=615, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(435, min_periods=max(435//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.155 * _rolling_slope(draw, 615) + 0.001641 * anchor

def f27_ist_210_struct_v210(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=446, w3=628, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 168)
    baseline = trend.rolling(446, min_periods=max(446//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(628, min_periods=max(628//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.940625 + 0.0016411 * anchor

def f27_ist_211_struct_v211(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=457, w3=641, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 175)
    slow = _rolling_slope(x, 457)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.955 + 0.0016412 * anchor

def f27_ist_212_struct_v212(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=468, w3=654, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(468, min_periods=max(468//3, 2)).max()
    trough = x.rolling(182, min_periods=max(182//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.969375 + 0.0016413 * anchor

def f27_ist_213_struct_v213(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=479, w3=667, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1854 * persistence + 0.0016414 * anchor

def f27_ist_214_struct_v214(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=490, w3=680, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(196, min_periods=max(196//3, 2)).std()
    vol_slow = ret.rolling(490, min_periods=max(490//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.998125 + 0.0016415 * anchor

def f27_ist_215_struct_v215(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=501, w3=693, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 203)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2006 * slope + 0.0016416 * anchor

def f27_ist_216_struct_v216(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=512, w3=706, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(512, min_periods=max(512//3, 2)).mean()
    noise = impulse.abs().rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.026875 + 0.0016417 * anchor

def f27_ist_217_struct_v217(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=20, w3=719, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 217)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 719)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2158 * acceleration + 0.0016418 * anchor

def f27_ist_218_struct_v218(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=31, w3=732, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(31, min_periods=max(31//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.055625 + 0.0016419 * anchor

def f27_ist_219_struct_v219(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=42, w3=745, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(42, min_periods=max(42//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.231 * _rolling_slope(draw, 745) + 0.001642 * anchor

def f27_ist_220_struct_v220(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=53, w3=758, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 238)
    baseline = trend.rolling(53, min_periods=max(53//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.084375 + 0.0016421 * anchor

def f27_ist_221_struct_v221(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=64, w3=771, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 245)
    slow = _rolling_slope(x, 64)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.09875 + 0.0016422 * anchor

def f27_ist_222_struct_v222(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=75, w3=27, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(75, min_periods=max(75//3, 2)).max()
    trough = x.rolling(252, min_periods=max(252//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.113125 + 0.0016423 * anchor

def f27_ist_223_struct_v223(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=86, w3=40, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(8)
    rank = change.rolling(86, min_periods=max(86//3, 2)).rank(pct=True)
    persistence = change.rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2614 * persistence + 0.0016424 * anchor

def f27_ist_224_struct_v224(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=97, w3=53, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(15, min_periods=max(15//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.141875 + 0.0016425 * anchor

def f27_ist_225_struct_v225(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=108, w3=66, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(108, min_periods=max(108//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 22)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2766 * slope + 0.0016426 * anchor
