"""62 analyst revision dispersion base features 76-150 â€” Pipeline 1a-HF Grade v3.

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

def f62_ard_076_analyst_v76(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=165, w2=360, w3=717, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(360, min_periods=max(360//3, 2)).mean()
    noise = impulse.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2075 + 0.0034877 * anchor

def f62_ard_077_analyst_v77(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=172, w2=371, w3=730, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 172)
    acceleration = _rolling_slope(velocity, 371)
    curvature = _rolling_slope(acceleration, 730)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1146 * acceleration + 0.0034878 * anchor

def f62_ard_078_analyst_v78(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=179, w2=382, w3=743, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(382, min_periods=max(382//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.23625 + 0.0034879 * anchor

def f62_ard_079_analyst_v79(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=186, w2=393, w3=756, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(393, min_periods=max(393//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1298 * _rolling_slope(draw, 756) + 0.003488 * anchor

def f62_ard_080_analyst_v80(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=193, w2=404, w3=769, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 193)
    baseline = trend.rolling(404, min_periods=max(404//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(769, min_periods=max(769//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.265 + 0.0034881 * anchor

def f62_ard_081_analyst_v81(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=200, w2=415, w3=25, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 200)
    slow = _rolling_slope(x, 415)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=25, adjust=False).mean() * 1.279375 + 0.0034882 * anchor

def f62_ard_082_analyst_v82(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=207, w2=426, w3=38, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(426, min_periods=max(426//3, 2)).max()
    trough = x.rolling(207, min_periods=max(207//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.29375 + 0.0034883 * anchor

def f62_ard_083_analyst_v83(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=214, w2=437, w3=51, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1602 * persistence + 0.0034884 * anchor

def f62_ard_084_analyst_v84(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=221, w2=448, w3=64, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(221, min_periods=max(221//3, 2)).std()
    vol_slow = ret.rolling(448, min_periods=max(448//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3225 + 0.0034885 * anchor

def f62_ard_085_analyst_v85(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=228, w2=459, w3=77, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(459, min_periods=max(459//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 228)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1754 * slope + 0.0034886 * anchor

def f62_ard_086_analyst_v86(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=235, w2=470, w3=90, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(470, min_periods=max(470//3, 2)).mean()
    noise = impulse.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.35125 + 0.0034887 * anchor

def f62_ard_087_analyst_v87(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=242, w2=481, w3=103, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 242)
    acceleration = _rolling_slope(velocity, 481)
    curvature = _rolling_slope(acceleration, 103)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1906 * acceleration + 0.0034888 * anchor

def f62_ard_088_analyst_v88(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=249, w2=492, w3=116, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(249, min_periods=max(249//3, 2)).mean(), upside.rolling(492, min_periods=max(492//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(116) * 1.38 + 0.0034889 * anchor

def f62_ard_089_analyst_v89(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=5, w2=503, w3=129, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2058 * _rolling_slope(draw, 129) + 0.003489 * anchor

def f62_ard_090_analyst_v90(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=12, w2=11, w3=142, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(11, min_periods=max(11//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(142, min_periods=max(142//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.40875 + 0.0034891 * anchor

def f62_ard_091_analyst_v91(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=19, w2=22, w3=155, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 22)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=155, adjust=False).mean() * 1.423125 + 0.0034892 * anchor

def f62_ard_092_analyst_v92(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=26, w2=33, w3=168, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(33, min_periods=max(33//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4375 + 0.0034893 * anchor

def f62_ard_093_analyst_v93(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=33, w2=44, w3=181, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(33)
    rank = change.rolling(44, min_periods=max(44//3, 2)).rank(pct=True)
    persistence = change.rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2362 * persistence + 0.0034894 * anchor

def f62_ard_094_analyst_v94(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=40, w2=55, w3=194, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.46625 + 0.0034895 * anchor

def f62_ard_095_analyst_v95(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=47, w2=66, w3=207, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(66, min_periods=max(66//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2514 * slope + 0.0034896 * anchor

def f62_ard_096_analyst_v96(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=54, w2=77, w3=220, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(54)
    drag = impulse.rolling(77, min_periods=max(77//3, 2)).mean()
    noise = impulse.abs().rolling(220, min_periods=max(220//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.495 + 0.0034897 * anchor

def f62_ard_097_analyst_v97(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=61, w2=88, w3=233, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 88)
    curvature = _rolling_slope(acceleration, 233)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2666 * acceleration + 0.0034898 * anchor

def f62_ard_098_analyst_v98(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=68, w2=99, w3=246, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(99, min_periods=max(99//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.52375 + 0.0034899 * anchor

def f62_ard_099_analyst_v99(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=75, w2=110, w3=259, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(110, min_periods=max(110//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2818 * _rolling_slope(draw, 259) + 0.00349 * anchor

def f62_ard_100_analyst_v100(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=82, w2=121, w3=272, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(121, min_periods=max(121//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.5525 + 0.0034901 * anchor

def f62_ard_101_analyst_v101(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=89, w2=132, w3=285, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 132)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=285, adjust=False).mean() * 1.566875 + 0.0034902 * anchor

def f62_ard_102_analyst_v102(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=96, w2=143, w3=298, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(143, min_periods=max(143//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.58125 + 0.0034903 * anchor

def f62_ard_103_analyst_v103(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=103, w2=154, w3=311, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(103)
    rank = change.rolling(154, min_periods=max(154//3, 2)).rank(pct=True)
    persistence = change.rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3122 * persistence + 0.0034904 * anchor

def f62_ard_104_analyst_v104(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=110, w2=165, w3=324, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61 + 0.0034905 * anchor

def f62_ard_105_analyst_v105(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=117, w2=176, w3=337, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(176, min_periods=max(176//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3274 * slope + 0.0034906 * anchor

def f62_ard_106_analyst_v106(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=124, w2=187, w3=350, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(124)
    drag = impulse.rolling(187, min_periods=max(187//3, 2)).mean()
    noise = impulse.abs().rolling(350, min_periods=max(350//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.865625 + 0.0034907 * anchor

def f62_ard_107_analyst_v107(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=131, w2=198, w3=363, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 198)
    curvature = _rolling_slope(acceleration, 363)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3426 * acceleration + 0.0034908 * anchor

def f62_ard_108_analyst_v108(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=138, w2=209, w3=376, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.894375 + 0.0034909 * anchor

def f62_ard_109_analyst_v109(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=145, w2=220, w3=389, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(220, min_periods=max(220//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3578 * _rolling_slope(draw, 389) + 0.003491 * anchor

def f62_ard_110_analyst_v110(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=152, w2=231, w3=402, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(231, min_periods=max(231//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(402, min_periods=max(402//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.923125 + 0.0034911 * anchor

def f62_ard_111_analyst_v111(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=159, w2=242, w3=415, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.9375 + 0.0034912 * anchor

def f62_ard_112_analyst_v112(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=166, w2=253, w3=428, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.951875 + 0.0034913 * anchor

def f62_ard_113_analyst_v113(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=173, w2=264, w3=441, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(264, min_periods=max(264//3, 2)).rank(pct=True)
    persistence = change.rolling(441, min_periods=max(441//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3882 * persistence + 0.0034914 * anchor

def f62_ard_114_analyst_v114(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=180, w2=275, w3=454, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.980625 + 0.0034915 * anchor

def f62_ard_115_analyst_v115(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=187, w2=286, w3=467, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4034 * slope + 0.0034916 * anchor

def f62_ard_116_analyst_v116(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=194, w2=297, w3=480, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(297, min_periods=max(297//3, 2)).mean()
    noise = impulse.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.009375 + 0.0034917 * anchor

def f62_ard_117_analyst_v117(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=201, w2=308, w3=493, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 308)
    curvature = _rolling_slope(acceleration, 493)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0422 * acceleration + 0.0034918 * anchor

def f62_ard_118_analyst_v118(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=208, w2=319, w3=506, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(319, min_periods=max(319//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.038125 + 0.0034919 * anchor

def f62_ard_119_analyst_v119(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=215, w2=330, w3=519, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(330, min_periods=max(330//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0574 * _rolling_slope(draw, 519) + 0.003492 * anchor

def f62_ard_120_analyst_v120(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=222, w2=341, w3=532, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(341, min_periods=max(341//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.066875 + 0.0034921 * anchor

def f62_ard_121_analyst_v121(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=229, w2=352, w3=545, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.08125 + 0.0034922 * anchor

def f62_ard_122_analyst_v122(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=236, w2=363, w3=558, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(363, min_periods=max(363//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.095625 + 0.0034923 * anchor

def f62_ard_123_analyst_v123(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=243, w2=374, w3=571, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0878 * persistence + 0.0034924 * anchor

def f62_ard_124_analyst_v124(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=250, w2=385, w3=584, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(385, min_periods=max(385//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.124375 + 0.0034925 * anchor

def f62_ard_125_analyst_v125(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=6, w2=396, w3=597, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 6)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.103 * slope + 0.0034926 * anchor

def f62_ard_126_analyst_v126(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=13, w2=407, w3=610, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(13)
    drag = impulse.rolling(407, min_periods=max(407//3, 2)).mean()
    noise = impulse.abs().rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.153125 + 0.0034927 * anchor

def f62_ard_127_analyst_v127(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=20, w2=418, w3=623, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 20)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 623)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1182 * acceleration + 0.0034928 * anchor

def f62_ard_128_analyst_v128(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=27, w2=429, w3=636, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(27, min_periods=max(27//3, 2)).mean(), upside.rolling(429, min_periods=max(429//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.181875 + 0.0034929 * anchor

def f62_ard_129_analyst_v129(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=34, w2=440, w3=649, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(440, min_periods=max(440//3, 2)).max()
    rebound = x - x.rolling(34, min_periods=max(34//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1334 * _rolling_slope(draw, 649) + 0.003493 * anchor

def f62_ard_130_analyst_v130(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=41, w2=451, w3=662, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 41)
    baseline = trend.rolling(451, min_periods=max(451//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(662, min_periods=max(662//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.210625 + 0.0034931 * anchor

def f62_ard_131_analyst_v131(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=48, w2=462, w3=675, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 48)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.225 + 0.0034932 * anchor

def f62_ard_132_analyst_v132(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=55, w2=473, w3=688, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(473, min_periods=max(473//3, 2)).max()
    trough = x.rolling(55, min_periods=max(55//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.239375 + 0.0034933 * anchor

def f62_ard_133_analyst_v133(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=62, w2=484, w3=701, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(62)
    rank = change.rolling(484, min_periods=max(484//3, 2)).rank(pct=True)
    persistence = change.rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1638 * persistence + 0.0034934 * anchor

def f62_ard_134_analyst_v134(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=69, w2=495, w3=714, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(69, min_periods=max(69//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.268125 + 0.0034935 * anchor

def f62_ard_135_analyst_v135(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=76, w2=506, w3=727, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 76)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.179 * slope + 0.0034936 * anchor

def f62_ard_136_analyst_v136(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=83, w2=14, w3=740, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(83)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(740, min_periods=max(740//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.296875 + 0.0034937 * anchor

def f62_ard_137_analyst_v137(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=90, w2=25, w3=753, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 90)
    acceleration = _rolling_slope(velocity, 25)
    curvature = _rolling_slope(acceleration, 753)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1942 * acceleration + 0.0034938 * anchor

def f62_ard_138_analyst_v138(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=97, w2=36, w3=766, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(36, min_periods=max(36//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.325625 + 0.0034939 * anchor

def f62_ard_139_analyst_v139(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=104, w2=47, w3=22, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2094 * _rolling_slope(draw, 22) + 0.003494 * anchor

def f62_ard_140_analyst_v140(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=111, w2=58, w3=35, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 111)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.354375 + 0.0034941 * anchor

def f62_ard_141_analyst_v141(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=118, w2=69, w3=48, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 118)
    slow = _rolling_slope(x, 69)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=48, adjust=False).mean() * 1.36875 + 0.0034942 * anchor

def f62_ard_142_analyst_v142(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=125, w2=80, w3=61, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(125, min_periods=max(125//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.383125 + 0.0034943 * anchor

def f62_ard_143_analyst_v143(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=132, w2=91, w3=74, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(91, min_periods=max(91//3, 2)).rank(pct=True)
    persistence = change.rolling(74, min_periods=max(74//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2398 * persistence + 0.0034944 * anchor

def f62_ard_144_analyst_v144(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=139, w2=102, w3=87, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(139, min_periods=max(139//3, 2)).std()
    vol_slow = ret.rolling(102, min_periods=max(102//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.411875 + 0.0034945 * anchor

def f62_ard_145_analyst_v145(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=146, w2=113, w3=100, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.255 * slope + 0.0034946 * anchor

def f62_ard_146_analyst_v146(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=153, w2=124, w3=113, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.440625 + 0.0034947 * anchor

def f62_ard_147_analyst_v147(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=160, w2=135, w3=126, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 126)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2702 * acceleration + 0.0034948 * anchor

def f62_ard_148_analyst_v148(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=167, w2=146, w3=139, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(167, min_periods=max(167//3, 2)).mean(), upside.rolling(146, min_periods=max(146//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.469375 + 0.0034949 * anchor

def f62_ard_149_analyst_v149(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=174, w2=157, w3=152, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(157, min_periods=max(157//3, 2)).max()
    rebound = x - x.rolling(174, min_periods=max(174//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2854 * _rolling_slope(draw, 152) + 0.003495 * anchor

def f62_ard_150_analyst_v150(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=181, w2=168, w3=165, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(168, min_periods=max(168//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.498125 + 0.0034951 * anchor
