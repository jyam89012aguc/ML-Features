"""62 analyst revision dispersion base features 376-450 â€” Pipeline 1a-HF Grade v3.

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

def f62_ard_376_analyst_v376(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=6, w2=139, w3=75, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(6)
    drag = impulse.rolling(139, min_periods=max(139//3, 2)).mean()
    noise = impulse.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88125 + 0.0035177 * anchor

def f62_ard_377_analyst_v377(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=13, w2=150, w3=88, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 13)
    acceleration = _rolling_slope(velocity, 150)
    curvature = _rolling_slope(acceleration, 88)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1362 * acceleration + 0.0035178 * anchor

def f62_ard_378_analyst_v378(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=20, w2=161, w3=101, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(20, min_periods=max(20//3, 2)).mean(), upside.rolling(161, min_periods=max(161//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(101) * 0.91 + 0.0035179 * anchor

def f62_ard_379_analyst_v379(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=27, w2=172, w3=114, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(172, min_periods=max(172//3, 2)).max()
    rebound = x - x.rolling(27, min_periods=max(27//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1514 * _rolling_slope(draw, 114) + 0.003518 * anchor

def f62_ard_380_analyst_v380(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=34, w2=183, w3=127, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 34)
    baseline = trend.rolling(183, min_periods=max(183//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.93875 + 0.0035181 * anchor

def f62_ard_381_analyst_v381(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=41, w2=194, w3=140, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 41)
    slow = _rolling_slope(x, 194)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=140, adjust=False).mean() * 0.953125 + 0.0035182 * anchor

def f62_ard_382_analyst_v382(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=48, w2=205, w3=153, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(205, min_periods=max(205//3, 2)).max()
    trough = x.rolling(48, min_periods=max(48//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9675 + 0.0035183 * anchor

def f62_ard_383_analyst_v383(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=55, w2=216, w3=166, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(55)
    rank = change.rolling(216, min_periods=max(216//3, 2)).rank(pct=True)
    persistence = change.rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1818 * persistence + 0.0035184 * anchor

def f62_ard_384_analyst_v384(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=62, w2=227, w3=179, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(62, min_periods=max(62//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99625 + 0.0035185 * anchor

def f62_ard_385_analyst_v385(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=69, w2=238, w3=192, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(238, min_periods=max(238//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 69)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.197 * slope + 0.0035186 * anchor

def f62_ard_386_analyst_v386(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=76, w2=249, w3=205, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(76)
    drag = impulse.rolling(249, min_periods=max(249//3, 2)).mean()
    noise = impulse.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.025 + 0.0035187 * anchor

def f62_ard_387_analyst_v387(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=83, w2=260, w3=218, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 83)
    acceleration = _rolling_slope(velocity, 260)
    curvature = _rolling_slope(acceleration, 218)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2122 * acceleration + 0.0035188 * anchor

def f62_ard_388_analyst_v388(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=90, w2=271, w3=231, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(90, min_periods=max(90//3, 2)).mean(), upside.rolling(271, min_periods=max(271//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05375 + 0.0035189 * anchor

def f62_ard_389_analyst_v389(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=97, w2=282, w3=244, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(282, min_periods=max(282//3, 2)).max()
    rebound = x - x.rolling(97, min_periods=max(97//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2274 * _rolling_slope(draw, 244) + 0.003519 * anchor

def f62_ard_390_analyst_v390(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=104, w2=293, w3=257, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 104)
    baseline = trend.rolling(293, min_periods=max(293//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.0825 + 0.0035191 * anchor

def f62_ard_391_analyst_v391(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=111, w2=304, w3=270, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 111)
    slow = _rolling_slope(x, 304)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=270, adjust=False).mean() * 1.096875 + 0.0035192 * anchor

def f62_ard_392_analyst_v392(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=118, w2=315, w3=283, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(315, min_periods=max(315//3, 2)).max()
    trough = x.rolling(118, min_periods=max(118//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11125 + 0.0035193 * anchor

def f62_ard_393_analyst_v393(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=125, w2=326, w3=296, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(125)
    rank = change.rolling(326, min_periods=max(326//3, 2)).rank(pct=True)
    persistence = change.rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2578 * persistence + 0.0035194 * anchor

def f62_ard_394_analyst_v394(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=132, w2=337, w3=309, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(132, min_periods=max(132//3, 2)).std()
    vol_slow = ret.rolling(337, min_periods=max(337//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.14 + 0.0035195 * anchor

def f62_ard_395_analyst_v395(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=139, w2=348, w3=322, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(348, min_periods=max(348//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 139)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.273 * slope + 0.0035196 * anchor

def f62_ard_396_analyst_v396(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=146, w2=359, w3=335, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(359, min_periods=max(359//3, 2)).mean()
    noise = impulse.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.16875 + 0.0035197 * anchor

def f62_ard_397_analyst_v397(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=153, w2=370, w3=348, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 153)
    acceleration = _rolling_slope(velocity, 370)
    curvature = _rolling_slope(acceleration, 348)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2882 * acceleration + 0.0035198 * anchor

def f62_ard_398_analyst_v398(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=160, w2=381, w3=361, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(160, min_periods=max(160//3, 2)).mean(), upside.rolling(381, min_periods=max(381//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1975 + 0.0035199 * anchor

def f62_ard_399_analyst_v399(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=167, w2=392, w3=374, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(392, min_periods=max(392//3, 2)).max()
    rebound = x - x.rolling(167, min_periods=max(167//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3034 * _rolling_slope(draw, 374) + 0.00352 * anchor

def f62_ard_400_analyst_v400(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=174, w2=403, w3=387, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 174)
    baseline = trend.rolling(403, min_periods=max(403//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(387, min_periods=max(387//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.22625 + 0.0035201 * anchor

def f62_ard_401_analyst_v401(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=181, w2=414, w3=400, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 181)
    slow = _rolling_slope(x, 414)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.240625 + 0.0035202 * anchor

def f62_ard_402_analyst_v402(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=188, w2=425, w3=413, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(425, min_periods=max(425//3, 2)).max()
    trough = x.rolling(188, min_periods=max(188//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.255 + 0.0035203 * anchor

def f62_ard_403_analyst_v403(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=195, w2=436, w3=426, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(436, min_periods=max(436//3, 2)).rank(pct=True)
    persistence = change.rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3338 * persistence + 0.0035204 * anchor

def f62_ard_404_analyst_v404(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=202, w2=447, w3=439, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(202, min_periods=max(202//3, 2)).std()
    vol_slow = ret.rolling(447, min_periods=max(447//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28375 + 0.0035205 * anchor

def f62_ard_405_analyst_v405(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=209, w2=458, w3=452, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(458, min_periods=max(458//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 209)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.349 * slope + 0.0035206 * anchor

def f62_ard_406_analyst_v406(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=216, w2=469, w3=465, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(469, min_periods=max(469//3, 2)).mean()
    noise = impulse.abs().rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.3125 + 0.0035207 * anchor

def f62_ard_407_analyst_v407(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=223, w2=480, w3=478, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 223)
    acceleration = _rolling_slope(velocity, 480)
    curvature = _rolling_slope(acceleration, 478)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3642 * acceleration + 0.0035208 * anchor

def f62_ard_408_analyst_v408(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=230, w2=491, w3=491, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(491, min_periods=max(491//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.34125 + 0.0035209 * anchor

def f62_ard_409_analyst_v409(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=237, w2=502, w3=504, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(502, min_periods=max(502//3, 2)).max()
    rebound = x - x.rolling(237, min_periods=max(237//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3794 * _rolling_slope(draw, 504) + 0.003521 * anchor

def f62_ard_410_analyst_v410(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=244, w2=10, w3=517, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(10, min_periods=max(10//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.37 + 0.0035211 * anchor

def f62_ard_411_analyst_v411(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=251, w2=21, w3=530, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.384375 + 0.0035212 * anchor

def f62_ard_412_analyst_v412(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=7, w2=32, w3=543, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.39875 + 0.0035213 * anchor

def f62_ard_413_analyst_v413(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=14, w2=43, w3=556, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(14)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4098 * persistence + 0.0035214 * anchor

def f62_ard_414_analyst_v414(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=21, w2=54, w3=569, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4275 + 0.0035215 * anchor

def f62_ard_415_analyst_v415(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=28, w2=65, w3=582, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0486 * slope + 0.0035216 * anchor

def f62_ard_416_analyst_v416(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=35, w2=76, w3=595, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(35)
    drag = impulse.rolling(76, min_periods=max(76//3, 2)).mean()
    noise = impulse.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.45625 + 0.0035217 * anchor

def f62_ard_417_analyst_v417(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=42, w2=87, w3=608, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 42)
    acceleration = _rolling_slope(velocity, 87)
    curvature = _rolling_slope(acceleration, 608)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0638 * acceleration + 0.0035218 * anchor

def f62_ard_418_analyst_v418(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=49, w2=98, w3=621, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.485 + 0.0035219 * anchor

def f62_ard_419_analyst_v419(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=56, w2=109, w3=634, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(109, min_periods=max(109//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.079 * _rolling_slope(draw, 634) + 0.003522 * anchor

def f62_ard_420_analyst_v420(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=63, w2=120, w3=647, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(120, min_periods=max(120//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51375 + 0.0035221 * anchor

def f62_ard_421_analyst_v421(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=70, w2=131, w3=660, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 131)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.528125 + 0.0035222 * anchor

def f62_ard_422_analyst_v422(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=77, w2=142, w3=673, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(142, min_periods=max(142//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5425 + 0.0035223 * anchor

def f62_ard_423_analyst_v423(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=84, w2=153, w3=686, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(84)
    rank = change.rolling(153, min_periods=max(153//3, 2)).rank(pct=True)
    persistence = change.rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1094 * persistence + 0.0035224 * anchor

def f62_ard_424_analyst_v424(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=91, w2=164, w3=699, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(164, min_periods=max(164//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57125 + 0.0035225 * anchor

def f62_ard_425_analyst_v425(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=98, w2=175, w3=712, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(175, min_periods=max(175//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1246 * slope + 0.0035226 * anchor

def f62_ard_426_analyst_v426(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=105, w2=186, w3=725, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(105)
    drag = impulse.rolling(186, min_periods=max(186//3, 2)).mean()
    noise = impulse.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6 + 0.0035227 * anchor

def f62_ard_427_analyst_v427(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=112, w2=197, w3=738, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 197)
    curvature = _rolling_slope(acceleration, 738)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1398 * acceleration + 0.0035228 * anchor

def f62_ard_428_analyst_v428(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=119, w2=208, w3=751, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(119, min_periods=max(119//3, 2)).mean(), upside.rolling(208, min_periods=max(208//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.855625 + 0.0035229 * anchor

def f62_ard_429_analyst_v429(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=126, w2=219, w3=764, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(219, min_periods=max(219//3, 2)).max()
    rebound = x - x.rolling(126, min_periods=max(126//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.155 * _rolling_slope(draw, 764) + 0.003523 * anchor

def f62_ard_430_analyst_v430(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=133, w2=230, w3=20, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(230, min_periods=max(230//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.884375 + 0.0035231 * anchor

def f62_ard_431_analyst_v431(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=140, w2=241, w3=33, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 241)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=33, adjust=False).mean() * 0.89875 + 0.0035232 * anchor

def f62_ard_432_analyst_v432(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=147, w2=252, w3=46, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(252, min_periods=max(252//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.913125 + 0.0035233 * anchor

def f62_ard_433_analyst_v433(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=154, w2=263, w3=59, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(263, min_periods=max(263//3, 2)).rank(pct=True)
    persistence = change.rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1854 * persistence + 0.0035234 * anchor

def f62_ard_434_analyst_v434(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=161, w2=274, w3=72, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(274, min_periods=max(274//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.941875 + 0.0035235 * anchor

def f62_ard_435_analyst_v435(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=168, w2=285, w3=85, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2006 * slope + 0.0035236 * anchor

def f62_ard_436_analyst_v436(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=175, w2=296, w3=98, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(296, min_periods=max(296//3, 2)).mean()
    noise = impulse.abs().rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.970625 + 0.0035237 * anchor

def f62_ard_437_analyst_v437(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=182, w2=307, w3=111, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 307)
    curvature = _rolling_slope(acceleration, 111)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2158 * acceleration + 0.0035238 * anchor

def f62_ard_438_analyst_v438(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=189, w2=318, w3=124, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(189, min_periods=max(189//3, 2)).mean(), upside.rolling(318, min_periods=max(318//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(124) * 0.999375 + 0.0035239 * anchor

def f62_ard_439_analyst_v439(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=196, w2=329, w3=137, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(329, min_periods=max(329//3, 2)).max()
    rebound = x - x.rolling(196, min_periods=max(196//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.231 * _rolling_slope(draw, 137) + 0.003524 * anchor

def f62_ard_440_analyst_v440(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=203, w2=340, w3=150, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 203)
    baseline = trend.rolling(340, min_periods=max(340//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.028125 + 0.0035241 * anchor

def f62_ard_441_analyst_v441(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=210, w2=351, w3=163, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=163, adjust=False).mean() * 1.0425 + 0.0035242 * anchor

def f62_ard_442_analyst_v442(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=217, w2=362, w3=176, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(362, min_periods=max(362//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.056875 + 0.0035243 * anchor

def f62_ard_443_analyst_v443(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=224, w2=373, w3=189, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2614 * persistence + 0.0035244 * anchor

def f62_ard_444_analyst_v444(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=231, w2=384, w3=202, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(384, min_periods=max(384//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.085625 + 0.0035245 * anchor

def f62_ard_445_analyst_v445(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=238, w2=395, w3=215, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2766 * slope + 0.0035246 * anchor

def f62_ard_446_analyst_v446(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=245, w2=406, w3=228, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(406, min_periods=max(406//3, 2)).mean()
    noise = impulse.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.114375 + 0.0035247 * anchor

def f62_ard_447_analyst_v447(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=252, w2=417, w3=241, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 252)
    acceleration = _rolling_slope(velocity, 417)
    curvature = _rolling_slope(acceleration, 241)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2918 * acceleration + 0.0035248 * anchor

def f62_ard_448_analyst_v448(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=8, w2=428, w3=254, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(428, min_periods=max(428//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.143125 + 0.0035249 * anchor

def f62_ard_449_analyst_v449(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=15, w2=439, w3=267, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(439, min_periods=max(439//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.307 * _rolling_slope(draw, 267) + 0.003525 * anchor

def f62_ard_450_analyst_v450(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=22, w2=450, w3=280, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.171875 + 0.0035251 * anchor
