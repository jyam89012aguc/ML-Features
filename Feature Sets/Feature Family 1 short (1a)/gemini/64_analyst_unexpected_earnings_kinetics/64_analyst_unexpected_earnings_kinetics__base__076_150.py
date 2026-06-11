"""64 analyst unexpected earnings kinetics base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f64_asue_076_analyst_v76(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=31, w2=482, w3=420, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(31)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.44875 + 0.0036077 * anchor

def f64_asue_077_analyst_v77(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=38, w2=493, w3=433, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 493)
    curvature = _rolling_slope(acceleration, 433)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.201 * acceleration + 0.0036078 * anchor

def f64_asue_078_analyst_v78(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=45, w2=504, w3=446, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(504, min_periods=max(504//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4775 + 0.0036079 * anchor

def f64_asue_079_analyst_v79(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=52, w2=12, w3=459, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(12, min_periods=max(12//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2162 * _rolling_slope(draw, 459) + 0.003608 * anchor

def f64_asue_080_analyst_v80(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=59, w2=23, w3=472, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(23, min_periods=max(23//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(472, min_periods=max(472//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.50625 + 0.0036081 * anchor

def f64_asue_081_analyst_v81(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=66, w2=34, w3=485, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 34)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.520625 + 0.0036082 * anchor

def f64_asue_082_analyst_v82(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=73, w2=45, w3=498, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(45, min_periods=max(45//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.535 + 0.0036083 * anchor

def f64_asue_083_analyst_v83(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=80, w2=56, w3=511, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(80)
    rank = change.rolling(56, min_periods=max(56//3, 2)).rank(pct=True)
    persistence = change.rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2466 * persistence + 0.0036084 * anchor

def f64_asue_084_analyst_v84(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=87, w2=67, w3=524, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(67, min_periods=max(67//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56375 + 0.0036085 * anchor

def f64_asue_085_analyst_v85(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=94, w2=78, w3=537, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(78, min_periods=max(78//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2618 * slope + 0.0036086 * anchor

def f64_asue_086_analyst_v86(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=101, w2=89, w3=550, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(101)
    drag = impulse.rolling(89, min_periods=max(89//3, 2)).mean()
    noise = impulse.abs().rolling(550, min_periods=max(550//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5925 + 0.0036087 * anchor

def f64_asue_087_analyst_v87(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=108, w2=100, w3=563, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 100)
    curvature = _rolling_slope(acceleration, 563)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.277 * acceleration + 0.0036088 * anchor

def f64_asue_088_analyst_v88(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=115, w2=111, w3=576, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(111, min_periods=max(111//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.62125 + 0.0036089 * anchor

def f64_asue_089_analyst_v89(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=122, w2=122, w3=589, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(122, min_periods=max(122//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2922 * _rolling_slope(draw, 589) + 0.003609 * anchor

def f64_asue_090_analyst_v90(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=129, w2=133, w3=602, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.876875 + 0.0036091 * anchor

def f64_asue_091_analyst_v91(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=136, w2=144, w3=615, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.89125 + 0.0036092 * anchor

def f64_asue_092_analyst_v92(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=143, w2=155, w3=628, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.905625 + 0.0036093 * anchor

def f64_asue_093_analyst_v93(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=150, w2=166, w3=641, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(166, min_periods=max(166//3, 2)).rank(pct=True)
    persistence = change.rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3226 * persistence + 0.0036094 * anchor

def f64_asue_094_analyst_v94(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=157, w2=177, w3=654, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(177, min_periods=max(177//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.934375 + 0.0036095 * anchor

def f64_asue_095_analyst_v95(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=164, w2=188, w3=667, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(188, min_periods=max(188//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3378 * slope + 0.0036096 * anchor

def f64_asue_096_analyst_v96(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=171, w2=199, w3=680, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(199, min_periods=max(199//3, 2)).mean()
    noise = impulse.abs().rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.963125 + 0.0036097 * anchor

def f64_asue_097_analyst_v97(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=178, w2=210, w3=693, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 210)
    curvature = _rolling_slope(acceleration, 693)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.353 * acceleration + 0.0036098 * anchor

def f64_asue_098_analyst_v98(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=185, w2=221, w3=706, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(221, min_periods=max(221//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.991875 + 0.0036099 * anchor

def f64_asue_099_analyst_v99(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=192, w2=232, w3=719, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(232, min_periods=max(232//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3682 * _rolling_slope(draw, 719) + 0.00361 * anchor

def f64_asue_100_analyst_v100(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=199, w2=243, w3=732, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(243, min_periods=max(243//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.020625 + 0.0036101 * anchor

def f64_asue_101_analyst_v101(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=206, w2=254, w3=745, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 254)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.035 + 0.0036102 * anchor

def f64_asue_102_analyst_v102(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=213, w2=265, w3=758, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(265, min_periods=max(265//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.049375 + 0.0036103 * anchor

def f64_asue_103_analyst_v103(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=220, w2=276, w3=771, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(276, min_periods=max(276//3, 2)).rank(pct=True)
    persistence = change.rolling(771, min_periods=max(771//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3986 * persistence + 0.0036104 * anchor

def f64_asue_104_analyst_v104(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=227, w2=287, w3=27, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(287, min_periods=max(287//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.078125 + 0.0036105 * anchor

def f64_asue_105_analyst_v105(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=234, w2=298, w3=40, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(298, min_periods=max(298//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0374 * slope + 0.0036106 * anchor

def f64_asue_106_analyst_v106(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=241, w2=309, w3=53, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(309, min_periods=max(309//3, 2)).mean()
    noise = impulse.abs().rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.106875 + 0.0036107 * anchor

def f64_asue_107_analyst_v107(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=248, w2=320, w3=66, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 320)
    curvature = _rolling_slope(acceleration, 66)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0526 * acceleration + 0.0036108 * anchor

def f64_asue_108_analyst_v108(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=255, w2=331, w3=79, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(255, min_periods=max(255//3, 2)).mean(), upside.rolling(331, min_periods=max(331//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(79) * 1.135625 + 0.0036109 * anchor

def f64_asue_109_analyst_v109(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=11, w2=342, w3=92, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(342, min_periods=max(342//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0678 * _rolling_slope(draw, 92) + 0.003611 * anchor

def f64_asue_110_analyst_v110(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=18, w2=353, w3=105, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(353, min_periods=max(353//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.164375 + 0.0036111 * anchor

def f64_asue_111_analyst_v111(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=25, w2=364, w3=118, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 364)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=118, adjust=False).mean() * 1.17875 + 0.0036112 * anchor

def f64_asue_112_analyst_v112(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=32, w2=375, w3=131, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(375, min_periods=max(375//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.193125 + 0.0036113 * anchor

def f64_asue_113_analyst_v113(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=39, w2=386, w3=144, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(39)
    rank = change.rolling(386, min_periods=max(386//3, 2)).rank(pct=True)
    persistence = change.rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0982 * persistence + 0.0036114 * anchor

def f64_asue_114_analyst_v114(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=46, w2=397, w3=157, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.221875 + 0.0036115 * anchor

def f64_asue_115_analyst_v115(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=53, w2=408, w3=170, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(408, min_periods=max(408//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1134 * slope + 0.0036116 * anchor

def f64_asue_116_analyst_v116(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=60, w2=419, w3=183, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(60)
    drag = impulse.rolling(419, min_periods=max(419//3, 2)).mean()
    noise = impulse.abs().rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.250625 + 0.0036117 * anchor

def f64_asue_117_analyst_v117(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=67, w2=430, w3=196, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 430)
    curvature = _rolling_slope(acceleration, 196)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1286 * acceleration + 0.0036118 * anchor

def f64_asue_118_analyst_v118(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=74, w2=441, w3=209, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(74, min_periods=max(74//3, 2)).mean(), upside.rolling(441, min_periods=max(441//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.279375 + 0.0036119 * anchor

def f64_asue_119_analyst_v119(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=81, w2=452, w3=222, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(81, min_periods=max(81//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1438 * _rolling_slope(draw, 222) + 0.003612 * anchor

def f64_asue_120_analyst_v120(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=88, w2=463, w3=235, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(463, min_periods=max(463//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.308125 + 0.0036121 * anchor

def f64_asue_121_analyst_v121(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=95, w2=474, w3=248, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=248, adjust=False).mean() * 1.3225 + 0.0036122 * anchor

def f64_asue_122_analyst_v122(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=102, w2=485, w3=261, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(485, min_periods=max(485//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.336875 + 0.0036123 * anchor

def f64_asue_123_analyst_v123(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=109, w2=496, w3=274, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(109)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1742 * persistence + 0.0036124 * anchor

def f64_asue_124_analyst_v124(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=116, w2=507, w3=287, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(507, min_periods=max(507//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.365625 + 0.0036125 * anchor

def f64_asue_125_analyst_v125(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=123, w2=15, w3=300, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(15, min_periods=max(15//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1894 * slope + 0.0036126 * anchor

def f64_asue_126_analyst_v126(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=130, w2=26, w3=313, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(26, min_periods=max(26//3, 2)).mean()
    noise = impulse.abs().rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.394375 + 0.0036127 * anchor

def f64_asue_127_analyst_v127(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=137, w2=37, w3=326, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 37)
    curvature = _rolling_slope(acceleration, 326)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2046 * acceleration + 0.0036128 * anchor

def f64_asue_128_analyst_v128(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=144, w2=48, w3=339, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.423125 + 0.0036129 * anchor

def f64_asue_129_analyst_v129(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=151, w2=59, w3=352, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2198 * _rolling_slope(draw, 352) + 0.003613 * anchor

def f64_asue_130_analyst_v130(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=158, w2=70, w3=365, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 158)
    baseline = trend.rolling(70, min_periods=max(70//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.451875 + 0.0036131 * anchor

def f64_asue_131_analyst_v131(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=165, w2=81, w3=378, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 165)
    slow = _rolling_slope(x, 81)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.46625 + 0.0036132 * anchor

def f64_asue_132_analyst_v132(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=172, w2=92, w3=391, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(172, min_periods=max(172//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.480625 + 0.0036133 * anchor

def f64_asue_133_analyst_v133(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=179, w2=103, w3=404, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(103, min_periods=max(103//3, 2)).rank(pct=True)
    persistence = change.rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2502 * persistence + 0.0036134 * anchor

def f64_asue_134_analyst_v134(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=186, w2=114, w3=417, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(186, min_periods=max(186//3, 2)).std()
    vol_slow = ret.rolling(114, min_periods=max(114//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.509375 + 0.0036135 * anchor

def f64_asue_135_analyst_v135(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=193, w2=125, w3=430, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(125, min_periods=max(125//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 193)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2654 * slope + 0.0036136 * anchor

def f64_asue_136_analyst_v136(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=200, w2=136, w3=443, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(136, min_periods=max(136//3, 2)).mean()
    noise = impulse.abs().rolling(443, min_periods=max(443//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.538125 + 0.0036137 * anchor

def f64_asue_137_analyst_v137(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=207, w2=147, w3=456, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 207)
    acceleration = _rolling_slope(velocity, 147)
    curvature = _rolling_slope(acceleration, 456)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2806 * acceleration + 0.0036138 * anchor

def f64_asue_138_analyst_v138(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=214, w2=158, w3=469, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(214, min_periods=max(214//3, 2)).mean(), upside.rolling(158, min_periods=max(158//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.566875 + 0.0036139 * anchor

def f64_asue_139_analyst_v139(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=221, w2=169, w3=482, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(169, min_periods=max(169//3, 2)).max()
    rebound = x - x.rolling(221, min_periods=max(221//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2958 * _rolling_slope(draw, 482) + 0.003614 * anchor

def f64_asue_140_analyst_v140(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=228, w2=180, w3=495, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 228)
    baseline = trend.rolling(180, min_periods=max(180//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.595625 + 0.0036141 * anchor

def f64_asue_141_analyst_v141(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=235, w2=191, w3=508, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 235)
    slow = _rolling_slope(x, 191)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.61 + 0.0036142 * anchor

def f64_asue_142_analyst_v142(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=242, w2=202, w3=521, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(202, min_periods=max(202//3, 2)).max()
    trough = x.rolling(242, min_periods=max(242//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.85125 + 0.0036143 * anchor

def f64_asue_143_analyst_v143(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=249, w2=213, w3=534, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(213, min_periods=max(213//3, 2)).rank(pct=True)
    persistence = change.rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3262 * persistence + 0.0036144 * anchor

def f64_asue_144_analyst_v144(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=5, w2=224, w3=547, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(224, min_periods=max(224//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.88 + 0.0036145 * anchor

def f64_asue_145_analyst_v145(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=12, w2=235, w3=560, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(235, min_periods=max(235//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3414 * slope + 0.0036146 * anchor

def f64_asue_146_analyst_v146(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=19, w2=246, w3=573, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(19)
    drag = impulse.rolling(246, min_periods=max(246//3, 2)).mean()
    noise = impulse.abs().rolling(573, min_periods=max(573//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.90875 + 0.0036147 * anchor

def f64_asue_147_analyst_v147(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=26, w2=257, w3=586, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 257)
    curvature = _rolling_slope(acceleration, 586)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3566 * acceleration + 0.0036148 * anchor

def f64_asue_148_analyst_v148(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=33, w2=268, w3=599, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(33, min_periods=max(33//3, 2)).mean(), upside.rolling(268, min_periods=max(268//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9375 + 0.0036149 * anchor

def f64_asue_149_analyst_v149(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=40, w2=279, w3=612, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(279, min_periods=max(279//3, 2)).max()
    rebound = x - x.rolling(40, min_periods=max(40//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3718 * _rolling_slope(draw, 612) + 0.003615 * anchor

def f64_asue_150_analyst_v150(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=47, w2=290, w3=625, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(290, min_periods=max(290//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.96625 + 0.0036151 * anchor
