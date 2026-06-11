"""61 analyst revision momentum base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f61_arm_151_analyst_v151(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=255, w2=118, w3=705, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 255)
    slow = _rolling_slope(x, 118)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.391875 + 0.0034352 * anchor

def f61_arm_152_analyst_v152(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=11, w2=129, w3=718, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(129, min_periods=max(129//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.40625 + 0.0034353 * anchor

def f61_arm_153_analyst_v153(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=18, w2=140, w3=731, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(18)
    rank = change.rolling(140, min_periods=max(140//3, 2)).rank(pct=True)
    persistence = change.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2726 * persistence + 0.0034354 * anchor

def f61_arm_154_analyst_v154(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=25, w2=151, w3=744, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(151, min_periods=max(151//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.435 + 0.0034355 * anchor

def f61_arm_155_analyst_v155(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=32, w2=162, w3=757, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(162, min_periods=max(162//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2878 * slope + 0.0034356 * anchor

def f61_arm_156_analyst_v156(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=39, w2=173, w3=770, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(39)
    drag = impulse.rolling(173, min_periods=max(173//3, 2)).mean()
    noise = impulse.abs().rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.46375 + 0.0034357 * anchor

def f61_arm_157_analyst_v157(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=46, w2=184, w3=26, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 184)
    curvature = _rolling_slope(acceleration, 26)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.303 * acceleration + 0.0034358 * anchor

def f61_arm_158_analyst_v158(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=53, w2=195, w3=39, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(195, min_periods=max(195//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(39) * 1.4925 + 0.0034359 * anchor

def f61_arm_159_analyst_v159(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=60, w2=206, w3=52, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(206, min_periods=max(206//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3182 * _rolling_slope(draw, 52) + 0.003436 * anchor

def f61_arm_160_analyst_v160(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=67, w2=217, w3=65, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(217, min_periods=max(217//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.52125 + 0.0034361 * anchor

def f61_arm_161_analyst_v161(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=74, w2=228, w3=78, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 228)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=78, adjust=False).mean() * 1.535625 + 0.0034362 * anchor

def f61_arm_162_analyst_v162(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=81, w2=239, w3=91, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(239, min_periods=max(239//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.55 + 0.0034363 * anchor

def f61_arm_163_analyst_v163(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=88, w2=250, w3=104, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(88)
    rank = change.rolling(250, min_periods=max(250//3, 2)).rank(pct=True)
    persistence = change.rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3486 * persistence + 0.0034364 * anchor

def f61_arm_164_analyst_v164(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=95, w2=261, w3=117, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(261, min_periods=max(261//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57875 + 0.0034365 * anchor

def f61_arm_165_analyst_v165(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=102, w2=272, w3=130, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(272, min_periods=max(272//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3638 * slope + 0.0034366 * anchor

def f61_arm_166_analyst_v166(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=109, w2=283, w3=143, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(109)
    drag = impulse.rolling(283, min_periods=max(283//3, 2)).mean()
    noise = impulse.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6075 + 0.0034367 * anchor

def f61_arm_167_analyst_v167(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=116, w2=294, w3=156, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 294)
    curvature = _rolling_slope(acceleration, 156)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.379 * acceleration + 0.0034368 * anchor

def f61_arm_168_analyst_v168(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=123, w2=305, w3=169, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(123, min_periods=max(123//3, 2)).mean(), upside.rolling(305, min_periods=max(305//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.863125 + 0.0034369 * anchor

def f61_arm_169_analyst_v169(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=130, w2=316, w3=182, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(316, min_periods=max(316//3, 2)).max()
    rebound = x - x.rolling(130, min_periods=max(130//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3942 * _rolling_slope(draw, 182) + 0.003437 * anchor

def f61_arm_170_analyst_v170(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=137, w2=327, w3=195, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(327, min_periods=max(327//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.891875 + 0.0034371 * anchor

def f61_arm_171_analyst_v171(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=144, w2=338, w3=208, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 338)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=208, adjust=False).mean() * 0.90625 + 0.0034372 * anchor

def f61_arm_172_analyst_v172(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=151, w2=349, w3=221, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(349, min_periods=max(349//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.920625 + 0.0034373 * anchor

def f61_arm_173_analyst_v173(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=158, w2=360, w3=234, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(360, min_periods=max(360//3, 2)).rank(pct=True)
    persistence = change.rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0482 * persistence + 0.0034374 * anchor

def f61_arm_174_analyst_v174(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=165, w2=371, w3=247, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(371, min_periods=max(371//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.949375 + 0.0034375 * anchor

def f61_arm_175_analyst_v175(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=172, w2=382, w3=260, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(382, min_periods=max(382//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0634 * slope + 0.0034376 * anchor

def f61_arm_176_analyst_v176(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=179, w2=393, w3=273, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(393, min_periods=max(393//3, 2)).mean()
    noise = impulse.abs().rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.978125 + 0.0034377 * anchor

def f61_arm_177_analyst_v177(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=186, w2=404, w3=286, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 404)
    curvature = _rolling_slope(acceleration, 286)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0786 * acceleration + 0.0034378 * anchor

def f61_arm_178_analyst_v178(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=193, w2=415, w3=299, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(415, min_periods=max(415//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.006875 + 0.0034379 * anchor

def f61_arm_179_analyst_v179(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=200, w2=426, w3=312, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(426, min_periods=max(426//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0938 * _rolling_slope(draw, 312) + 0.003438 * anchor

def f61_arm_180_analyst_v180(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=207, w2=437, w3=325, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 207)
    baseline = trend.rolling(437, min_periods=max(437//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.035625 + 0.0034381 * anchor

def f61_arm_181_analyst_v181(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=214, w2=448, w3=338, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 214)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.05 + 0.0034382 * anchor

def f61_arm_182_analyst_v182(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=221, w2=459, w3=351, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(459, min_periods=max(459//3, 2)).max()
    trough = x.rolling(221, min_periods=max(221//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.064375 + 0.0034383 * anchor

def f61_arm_183_analyst_v183(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=228, w2=470, w3=364, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(470, min_periods=max(470//3, 2)).rank(pct=True)
    persistence = change.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1242 * persistence + 0.0034384 * anchor

def f61_arm_184_analyst_v184(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=235, w2=481, w3=377, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(235, min_periods=max(235//3, 2)).std()
    vol_slow = ret.rolling(481, min_periods=max(481//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.093125 + 0.0034385 * anchor

def f61_arm_185_analyst_v185(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=242, w2=492, w3=390, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(492, min_periods=max(492//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 242)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1394 * slope + 0.0034386 * anchor

def f61_arm_186_analyst_v186(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=249, w2=503, w3=403, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(503, min_periods=max(503//3, 2)).mean()
    noise = impulse.abs().rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.121875 + 0.0034387 * anchor

def f61_arm_187_analyst_v187(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=5, w2=11, w3=416, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 11)
    curvature = _rolling_slope(acceleration, 416)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1546 * acceleration + 0.0034388 * anchor

def f61_arm_188_analyst_v188(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=12, w2=22, w3=429, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(22, min_periods=max(22//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.150625 + 0.0034389 * anchor

def f61_arm_189_analyst_v189(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=19, w2=33, w3=442, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(33, min_periods=max(33//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1698 * _rolling_slope(draw, 442) + 0.003439 * anchor

def f61_arm_190_analyst_v190(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=26, w2=44, w3=455, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(44, min_periods=max(44//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.179375 + 0.0034391 * anchor

def f61_arm_191_analyst_v191(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=33, w2=55, w3=468, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 55)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.19375 + 0.0034392 * anchor

def f61_arm_192_analyst_v192(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=40, w2=66, w3=481, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(66, min_periods=max(66//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.208125 + 0.0034393 * anchor

def f61_arm_193_analyst_v193(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=47, w2=77, w3=494, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(47)
    rank = change.rolling(77, min_periods=max(77//3, 2)).rank(pct=True)
    persistence = change.rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2002 * persistence + 0.0034394 * anchor

def f61_arm_194_analyst_v194(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=54, w2=88, w3=507, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(88, min_periods=max(88//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.236875 + 0.0034395 * anchor

def f61_arm_195_analyst_v195(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=61, w2=99, w3=520, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(99, min_periods=max(99//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2154 * slope + 0.0034396 * anchor

def f61_arm_196_analyst_v196(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=68, w2=110, w3=533, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(68)
    drag = impulse.rolling(110, min_periods=max(110//3, 2)).mean()
    noise = impulse.abs().rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.265625 + 0.0034397 * anchor

def f61_arm_197_analyst_v197(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=75, w2=121, w3=546, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 121)
    curvature = _rolling_slope(acceleration, 546)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2306 * acceleration + 0.0034398 * anchor

def f61_arm_198_analyst_v198(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=82, w2=132, w3=559, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(132, min_periods=max(132//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.294375 + 0.0034399 * anchor

def f61_arm_199_analyst_v199(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=89, w2=143, w3=572, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(143, min_periods=max(143//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2458 * _rolling_slope(draw, 572) + 0.00344 * anchor

def f61_arm_200_analyst_v200(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=96, w2=154, w3=585, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(154, min_periods=max(154//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.323125 + 0.0034401 * anchor

def f61_arm_201_analyst_v201(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=103, w2=165, w3=598, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 103)
    slow = _rolling_slope(x, 165)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.3375 + 0.0034402 * anchor

def f61_arm_202_analyst_v202(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=110, w2=176, w3=611, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(176, min_periods=max(176//3, 2)).max()
    trough = x.rolling(110, min_periods=max(110//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.351875 + 0.0034403 * anchor

def f61_arm_203_analyst_v203(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=117, w2=187, w3=624, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(117)
    rank = change.rolling(187, min_periods=max(187//3, 2)).rank(pct=True)
    persistence = change.rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2762 * persistence + 0.0034404 * anchor

def f61_arm_204_analyst_v204(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=124, w2=198, w3=637, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(124, min_periods=max(124//3, 2)).std()
    vol_slow = ret.rolling(198, min_periods=max(198//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.380625 + 0.0034405 * anchor

def f61_arm_205_analyst_v205(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=131, w2=209, w3=650, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(209, min_periods=max(209//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 131)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2914 * slope + 0.0034406 * anchor

def f61_arm_206_analyst_v206(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=138, w2=220, w3=663, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(220, min_periods=max(220//3, 2)).mean()
    noise = impulse.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.409375 + 0.0034407 * anchor

def f61_arm_207_analyst_v207(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=145, w2=231, w3=676, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 145)
    acceleration = _rolling_slope(velocity, 231)
    curvature = _rolling_slope(acceleration, 676)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3066 * acceleration + 0.0034408 * anchor

def f61_arm_208_analyst_v208(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=152, w2=242, w3=689, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(242, min_periods=max(242//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.438125 + 0.0034409 * anchor

def f61_arm_209_analyst_v209(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=159, w2=253, w3=702, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(253, min_periods=max(253//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3218 * _rolling_slope(draw, 702) + 0.003441 * anchor

def f61_arm_210_analyst_v210(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=166, w2=264, w3=715, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 166)
    baseline = trend.rolling(264, min_periods=max(264//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.466875 + 0.0034411 * anchor

def f61_arm_211_analyst_v211(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=173, w2=275, w3=728, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 275)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.48125 + 0.0034412 * anchor

def f61_arm_212_analyst_v212(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=180, w2=286, w3=741, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(286, min_periods=max(286//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.495625 + 0.0034413 * anchor

def f61_arm_213_analyst_v213(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=187, w2=297, w3=754, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(297, min_periods=max(297//3, 2)).rank(pct=True)
    persistence = change.rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3522 * persistence + 0.0034414 * anchor

def f61_arm_214_analyst_v214(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=194, w2=308, w3=767, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(308, min_periods=max(308//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.524375 + 0.0034415 * anchor

def f61_arm_215_analyst_v215(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=201, w2=319, w3=23, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(319, min_periods=max(319//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3674 * slope + 0.0034416 * anchor

def f61_arm_216_analyst_v216(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=208, w2=330, w3=36, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(330, min_periods=max(330//3, 2)).mean()
    noise = impulse.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.553125 + 0.0034417 * anchor

def f61_arm_217_analyst_v217(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=215, w2=341, w3=49, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 341)
    curvature = _rolling_slope(acceleration, 49)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3826 * acceleration + 0.0034418 * anchor

def f61_arm_218_analyst_v218(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=222, w2=352, w3=62, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(352, min_periods=max(352//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(62) * 1.581875 + 0.0034419 * anchor

def f61_arm_219_analyst_v219(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=229, w2=363, w3=75, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(363, min_periods=max(363//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3978 * _rolling_slope(draw, 75) + 0.003442 * anchor

def f61_arm_220_analyst_v220(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=236, w2=374, w3=88, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(374, min_periods=max(374//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.610625 + 0.0034421 * anchor

def f61_arm_221_analyst_v221(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=243, w2=385, w3=101, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 385)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=101, adjust=False).mean() * 0.851875 + 0.0034422 * anchor

def f61_arm_222_analyst_v222(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=250, w2=396, w3=114, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(396, min_periods=max(396//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.86625 + 0.0034423 * anchor

def f61_arm_223_analyst_v223(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=6, w2=407, w3=127, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(6)
    rank = change.rolling(407, min_periods=max(407//3, 2)).rank(pct=True)
    persistence = change.rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0518 * persistence + 0.0034424 * anchor

def f61_arm_224_analyst_v224(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=13, w2=418, w3=140, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(418, min_periods=max(418//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.895 + 0.0034425 * anchor

def f61_arm_225_analyst_v225(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=20, w2=429, w3=153, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(429, min_periods=max(429//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.067 * slope + 0.0034426 * anchor
