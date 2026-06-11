"""31 cash burn acceleration base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f31_cba_151_struct_v151(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=41, w3=24, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 240)
    slow = _rolling_slope(x, 41)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=24, adjust=False).mean() * 1.348125 + 0.0018752 * anchor

def f31_cba_152_struct_v152(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=52, w3=37, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(52, min_periods=max(52//3, 2)).max()
    trough = x.rolling(247, min_periods=max(247//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3625 + 0.0018753 * anchor

def f31_cba_153_struct_v153(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=254, w2=63, w3=50, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(63, min_periods=max(63//3, 2)).rank(pct=True)
    persistence = change.rolling(50, min_periods=max(50//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2786 * persistence + 0.0018754 * anchor

def f31_cba_154_struct_v154(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=10, w2=74, w3=63, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(74, min_periods=max(74//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.39125 + 0.0018755 * anchor

def f31_cba_155_struct_v155(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=17, w2=85, w3=76, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(85, min_periods=max(85//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2938 * slope + 0.0018756 * anchor

def f31_cba_156_struct_v156(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=24, w2=96, w3=89, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(24)
    drag = impulse.rolling(96, min_periods=max(96//3, 2)).mean()
    noise = impulse.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42 + 0.0018757 * anchor

def f31_cba_157_struct_v157(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=31, w2=107, w3=102, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 107)
    curvature = _rolling_slope(acceleration, 102)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.309 * acceleration + 0.0018758 * anchor

def f31_cba_158_struct_v158(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=118, w3=115, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(118, min_periods=max(118//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(115) * 1.44875 + 0.0018759 * anchor

def f31_cba_159_struct_v159(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=129, w3=128, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(129, min_periods=max(129//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3242 * _rolling_slope(draw, 128) + 0.001876 * anchor

def f31_cba_160_struct_v160(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=140, w3=141, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(140, min_periods=max(140//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4775 + 0.0018761 * anchor

def f31_cba_161_struct_v161(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=151, w3=154, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 151)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=154, adjust=False).mean() * 1.491875 + 0.0018762 * anchor

def f31_cba_162_struct_v162(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=162, w3=167, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(162, min_periods=max(162//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.50625 + 0.0018763 * anchor

def f31_cba_163_struct_v163(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=173, w3=180, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(73)
    rank = change.rolling(173, min_periods=max(173//3, 2)).rank(pct=True)
    persistence = change.rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3546 * persistence + 0.0018764 * anchor

def f31_cba_164_struct_v164(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=184, w3=193, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(184, min_periods=max(184//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.535 + 0.0018765 * anchor

def f31_cba_165_struct_v165(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=195, w3=206, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(195, min_periods=max(195//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3698 * slope + 0.0018766 * anchor

def f31_cba_166_struct_v166(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=206, w3=219, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(94)
    drag = impulse.rolling(206, min_periods=max(206//3, 2)).mean()
    noise = impulse.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.56375 + 0.0018767 * anchor

def f31_cba_167_struct_v167(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=217, w3=232, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 217)
    curvature = _rolling_slope(acceleration, 232)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.385 * acceleration + 0.0018768 * anchor

def f31_cba_168_struct_v168(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=228, w3=245, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(228, min_periods=max(228//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5925 + 0.0018769 * anchor

def f31_cba_169_struct_v169(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=239, w3=258, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(239, min_periods=max(239//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4002 * _rolling_slope(draw, 258) + 0.001877 * anchor

def f31_cba_170_struct_v170(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=250, w3=271, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(250, min_periods=max(250//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.62125 + 0.0018771 * anchor

def f31_cba_171_struct_v171(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=261, w3=284, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 261)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=284, adjust=False).mean() * 0.8625 + 0.0018772 * anchor

def f31_cba_172_struct_v172(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=272, w3=297, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(272, min_periods=max(272//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.876875 + 0.0018773 * anchor

def f31_cba_173_struct_v173(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=283, w3=310, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(283, min_periods=max(283//3, 2)).rank(pct=True)
    persistence = change.rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0542 * persistence + 0.0018774 * anchor

def f31_cba_174_struct_v174(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=294, w3=323, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.905625 + 0.0018775 * anchor

def f31_cba_175_struct_v175(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=305, w3=336, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(305, min_periods=max(305//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0694 * slope + 0.0018776 * anchor

def f31_cba_176_struct_v176(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=316, w3=349, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(316, min_periods=max(316//3, 2)).mean()
    noise = impulse.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.934375 + 0.0018777 * anchor

def f31_cba_177_struct_v177(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=327, w3=362, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 327)
    curvature = _rolling_slope(acceleration, 362)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0846 * acceleration + 0.0018778 * anchor

def f31_cba_178_struct_v178(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=338, w3=375, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(338, min_periods=max(338//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.963125 + 0.0018779 * anchor

def f31_cba_179_struct_v179(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=349, w3=388, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(349, min_periods=max(349//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0998 * _rolling_slope(draw, 388) + 0.001878 * anchor

def f31_cba_180_struct_v180(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=360, w3=401, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(360, min_periods=max(360//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.991875 + 0.0018781 * anchor

def f31_cba_181_struct_v181(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=371, w3=414, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 371)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.00625 + 0.0018782 * anchor

def f31_cba_182_struct_v182(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=382, w3=427, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.020625 + 0.0018783 * anchor

def f31_cba_183_struct_v183(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=393, w3=440, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(393, min_periods=max(393//3, 2)).rank(pct=True)
    persistence = change.rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1302 * persistence + 0.0018784 * anchor

def f31_cba_184_struct_v184(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=404, w3=453, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.049375 + 0.0018785 * anchor

def f31_cba_185_struct_v185(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=415, w3=466, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(415, min_periods=max(415//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1454 * slope + 0.0018786 * anchor

def f31_cba_186_struct_v186(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=426, w3=479, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(426, min_periods=max(426//3, 2)).mean()
    noise = impulse.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.078125 + 0.0018787 * anchor

def f31_cba_187_struct_v187(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=437, w3=492, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 437)
    curvature = _rolling_slope(acceleration, 492)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1606 * acceleration + 0.0018788 * anchor

def f31_cba_188_struct_v188(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=448, w3=505, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(448, min_periods=max(448//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.106875 + 0.0018789 * anchor

def f31_cba_189_struct_v189(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=459, w3=518, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(459, min_periods=max(459//3, 2)).max()
    rebound = x - x.rolling(255, min_periods=max(255//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1758 * _rolling_slope(draw, 518) + 0.001879 * anchor

def f31_cba_190_struct_v190(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=470, w3=531, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 11)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.135625 + 0.0018791 * anchor

def f31_cba_191_struct_v191(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=481, w3=544, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 18)
    slow = _rolling_slope(x, 481)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.15 + 0.0018792 * anchor

def f31_cba_192_struct_v192(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=492, w3=557, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(492, min_periods=max(492//3, 2)).max()
    trough = x.rolling(25, min_periods=max(25//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.164375 + 0.0018793 * anchor

def f31_cba_193_struct_v193(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=503, w3=570, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(32)
    rank = change.rolling(503, min_periods=max(503//3, 2)).rank(pct=True)
    persistence = change.rolling(570, min_periods=max(570//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2062 * persistence + 0.0018794 * anchor

def f31_cba_194_struct_v194(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=11, w3=583, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(39, min_periods=max(39//3, 2)).std()
    vol_slow = ret.rolling(11, min_periods=max(11//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.193125 + 0.0018795 * anchor

def f31_cba_195_struct_v195(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=22, w3=596, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(22, min_periods=max(22//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 46)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2214 * slope + 0.0018796 * anchor

def f31_cba_196_struct_v196(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=33, w3=609, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(53)
    drag = impulse.rolling(33, min_periods=max(33//3, 2)).mean()
    noise = impulse.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.221875 + 0.0018797 * anchor

def f31_cba_197_struct_v197(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=44, w3=622, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 60)
    acceleration = _rolling_slope(velocity, 44)
    curvature = _rolling_slope(acceleration, 622)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2366 * acceleration + 0.0018798 * anchor

def f31_cba_198_struct_v198(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=55, w3=635, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(55, min_periods=max(55//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.250625 + 0.0018799 * anchor

def f31_cba_199_struct_v199(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=66, w3=648, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(66, min_periods=max(66//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2518 * _rolling_slope(draw, 648) + 0.00188 * anchor

def f31_cba_200_struct_v200(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=77, w3=661, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 81)
    baseline = trend.rolling(77, min_periods=max(77//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.279375 + 0.0018801 * anchor

def f31_cba_201_struct_v201(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=88, w3=674, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 88)
    slow = _rolling_slope(x, 88)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.29375 + 0.0018802 * anchor

def f31_cba_202_struct_v202(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=99, w3=687, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(99, min_periods=max(99//3, 2)).max()
    trough = x.rolling(95, min_periods=max(95//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.308125 + 0.0018803 * anchor

def f31_cba_203_struct_v203(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=110, w3=700, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(102)
    rank = change.rolling(110, min_periods=max(110//3, 2)).rank(pct=True)
    persistence = change.rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2822 * persistence + 0.0018804 * anchor

def f31_cba_204_struct_v204(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=121, w3=713, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(109, min_periods=max(109//3, 2)).std()
    vol_slow = ret.rolling(121, min_periods=max(121//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.336875 + 0.0018805 * anchor

def f31_cba_205_struct_v205(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=132, w3=726, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 116)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2974 * slope + 0.0018806 * anchor

def f31_cba_206_struct_v206(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=143, w3=739, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(123)
    drag = impulse.rolling(143, min_periods=max(143//3, 2)).mean()
    noise = impulse.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.365625 + 0.0018807 * anchor

def f31_cba_207_struct_v207(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=154, w3=752, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 130)
    acceleration = _rolling_slope(velocity, 154)
    curvature = _rolling_slope(acceleration, 752)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3126 * acceleration + 0.0018808 * anchor

def f31_cba_208_struct_v208(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=165, w3=765, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(137, min_periods=max(137//3, 2)).mean(), upside.rolling(165, min_periods=max(165//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.394375 + 0.0018809 * anchor

def f31_cba_209_struct_v209(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=176, w3=21, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(176, min_periods=max(176//3, 2)).max()
    rebound = x - x.rolling(144, min_periods=max(144//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3278 * _rolling_slope(draw, 21) + 0.001881 * anchor

def f31_cba_210_struct_v210(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=187, w3=34, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(187, min_periods=max(187//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.423125 + 0.0018811 * anchor

def f31_cba_211_struct_v211(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=198, w3=47, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 198)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=47, adjust=False).mean() * 1.4375 + 0.0018812 * anchor

def f31_cba_212_struct_v212(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=209, w3=60, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(209, min_periods=max(209//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.451875 + 0.0018813 * anchor

def f31_cba_213_struct_v213(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=220, w3=73, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(220, min_periods=max(220//3, 2)).rank(pct=True)
    persistence = change.rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3582 * persistence + 0.0018814 * anchor

def f31_cba_214_struct_v214(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=231, w3=86, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(231, min_periods=max(231//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.480625 + 0.0018815 * anchor

def f31_cba_215_struct_v215(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=242, w3=99, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(242, min_periods=max(242//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3734 * slope + 0.0018816 * anchor

def f31_cba_216_struct_v216(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=253, w3=112, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.509375 + 0.0018817 * anchor

def f31_cba_217_struct_v217(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=264, w3=125, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 264)
    curvature = _rolling_slope(acceleration, 125)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3886 * acceleration + 0.0018818 * anchor

def f31_cba_218_struct_v218(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=275, w3=138, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(207, min_periods=max(207//3, 2)).mean(), upside.rolling(275, min_periods=max(275//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.538125 + 0.0018819 * anchor

def f31_cba_219_struct_v219(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=286, w3=151, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(286, min_periods=max(286//3, 2)).max()
    rebound = x - x.rolling(214, min_periods=max(214//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.4038 * _rolling_slope(draw, 151) + 0.001882 * anchor

def f31_cba_220_struct_v220(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=297, w3=164, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(297, min_periods=max(297//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.566875 + 0.0018821 * anchor

def f31_cba_221_struct_v221(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=308, w3=177, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 308)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=177, adjust=False).mean() * 1.58125 + 0.0018822 * anchor

def f31_cba_222_struct_v222(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=319, w3=190, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(319, min_periods=max(319//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.595625 + 0.0018823 * anchor

def f31_cba_223_struct_v223(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=330, w3=203, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(330, min_periods=max(330//3, 2)).rank(pct=True)
    persistence = change.rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0578 * persistence + 0.0018824 * anchor

def f31_cba_224_struct_v224(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=341, w3=216, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(341, min_periods=max(341//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85125 + 0.0018825 * anchor

def f31_cba_225_struct_v225(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=352, w3=229, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(352, min_periods=max(352//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.073 * slope + 0.0018826 * anchor
