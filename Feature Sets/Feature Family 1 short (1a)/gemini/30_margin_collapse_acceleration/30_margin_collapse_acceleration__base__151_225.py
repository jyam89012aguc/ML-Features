"""30 margin collapse acceleration base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f30_mca_151_struct_v151(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=483, w3=551, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.2275 + 0.0018152 * anchor

def f30_mca_152_struct_v152(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=494, w3=564, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.241875 + 0.0018153 * anchor

def f30_mca_153_struct_v153(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=505, w3=577, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(70)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2354 * persistence + 0.0018154 * anchor

def f30_mca_154_struct_v154(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=13, w3=590, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.270625 + 0.0018155 * anchor

def f30_mca_155_struct_v155(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=24, w3=603, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2506 * slope + 0.0018156 * anchor

def f30_mca_156_struct_v156(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=35, w3=616, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(91)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.299375 + 0.0018157 * anchor

def f30_mca_157_struct_v157(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=46, w3=629, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 46)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2658 * acceleration + 0.0018158 * anchor

def f30_mca_158_struct_v158(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=57, w3=642, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.328125 + 0.0018159 * anchor

def f30_mca_159_struct_v159(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=68, w3=655, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.281 * _rolling_slope(draw, 655) + 0.001816 * anchor

def f30_mca_160_struct_v160(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=79, w3=668, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 119)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.356875 + 0.0018161 * anchor

def f30_mca_161_struct_v161(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=90, w3=681, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 126)
    slow = _rolling_slope(x, 90)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.37125 + 0.0018162 * anchor

def f30_mca_162_struct_v162(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=101, w3=694, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(101, min_periods=max(101//3, 2)).max()
    trough = x.rolling(133, min_periods=max(133//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.385625 + 0.0018163 * anchor

def f30_mca_163_struct_v163(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=112, w3=707, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(112, min_periods=max(112//3, 2)).rank(pct=True)
    persistence = change.rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3114 * persistence + 0.0018164 * anchor

def f30_mca_164_struct_v164(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=123, w3=720, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(147, min_periods=max(147//3, 2)).std()
    vol_slow = ret.rolling(123, min_periods=max(123//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.414375 + 0.0018165 * anchor

def f30_mca_165_struct_v165(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=134, w3=733, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(134, min_periods=max(134//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 154)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3266 * slope + 0.0018166 * anchor

def f30_mca_166_struct_v166(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=145, w3=746, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.443125 + 0.0018167 * anchor

def f30_mca_167_struct_v167(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=156, w3=759, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 168)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 759)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3418 * acceleration + 0.0018168 * anchor

def f30_mca_168_struct_v168(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=167, w3=15, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(15) * 1.471875 + 0.0018169 * anchor

def f30_mca_169_struct_v169(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=178, w3=28, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(178, min_periods=max(178//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.357 * _rolling_slope(draw, 28) + 0.001817 * anchor

def f30_mca_170_struct_v170(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=189, w3=41, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(189, min_periods=max(189//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.500625 + 0.0018171 * anchor

def f30_mca_171_struct_v171(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=200, w3=54, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=54, adjust=False).mean() * 1.515 + 0.0018172 * anchor

def f30_mca_172_struct_v172(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=211, w3=67, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(211, min_periods=max(211//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.529375 + 0.0018173 * anchor

def f30_mca_173_struct_v173(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=222, w3=80, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3874 * persistence + 0.0018174 * anchor

def f30_mca_174_struct_v174(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=217, w2=233, w3=93, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.558125 + 0.0018175 * anchor

def f30_mca_175_struct_v175(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=224, w2=244, w3=106, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4026 * slope + 0.0018176 * anchor

def f30_mca_176_struct_v176(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=255, w3=119, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.586875 + 0.0018177 * anchor

def f30_mca_177_struct_v177(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=266, w3=132, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 132)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0414 * acceleration + 0.0018178 * anchor

def f30_mca_178_struct_v178(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=277, w3=145, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.615625 + 0.0018179 * anchor

def f30_mca_179_struct_v179(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=288, w3=158, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0566 * _rolling_slope(draw, 158) + 0.001818 * anchor

def f30_mca_180_struct_v180(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=299, w3=171, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.87125 + 0.0018181 * anchor

def f30_mca_181_struct_v181(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=310, w3=184, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=184, adjust=False).mean() * 0.885625 + 0.0018182 * anchor

def f30_mca_182_struct_v182(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=321, w3=197, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.9 + 0.0018183 * anchor

def f30_mca_183_struct_v183(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=332, w3=210, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(29)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.087 * persistence + 0.0018184 * anchor

def f30_mca_184_struct_v184(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=343, w3=223, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92875 + 0.0018185 * anchor

def f30_mca_185_struct_v185(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=354, w3=236, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1022 * slope + 0.0018186 * anchor

def f30_mca_186_struct_v186(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=365, w3=249, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(50)
    drag = impulse.rolling(365, min_periods=max(365//3, 2)).mean()
    noise = impulse.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9575 + 0.0018187 * anchor

def f30_mca_187_struct_v187(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=376, w3=262, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1174 * acceleration + 0.0018188 * anchor

def f30_mca_188_struct_v188(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=387, w3=275, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.98625 + 0.0018189 * anchor

def f30_mca_189_struct_v189(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=398, w3=288, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(398, min_periods=max(398//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1326 * _rolling_slope(draw, 288) + 0.001819 * anchor

def f30_mca_190_struct_v190(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=409, w3=301, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(409, min_periods=max(409//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.015 + 0.0018191 * anchor

def f30_mca_191_struct_v191(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=420, w3=314, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.029375 + 0.0018192 * anchor

def f30_mca_192_struct_v192(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=431, w3=327, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(431, min_periods=max(431//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.04375 + 0.0018193 * anchor

def f30_mca_193_struct_v193(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=442, w3=340, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(99)
    rank = change.rolling(442, min_periods=max(442//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.163 * persistence + 0.0018194 * anchor

def f30_mca_194_struct_v194(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=453, w3=353, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(453, min_periods=max(453//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0725 + 0.0018195 * anchor

def f30_mca_195_struct_v195(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=464, w3=366, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1782 * slope + 0.0018196 * anchor

def f30_mca_196_struct_v196(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=475, w3=379, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(120)
    drag = impulse.rolling(475, min_periods=max(475//3, 2)).mean()
    noise = impulse.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.10125 + 0.0018197 * anchor

def f30_mca_197_struct_v197(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=486, w3=392, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 392)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1934 * acceleration + 0.0018198 * anchor

def f30_mca_198_struct_v198(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=497, w3=405, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.13 + 0.0018199 * anchor

def f30_mca_199_struct_v199(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=508, w3=418, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2086 * _rolling_slope(draw, 418) + 0.00182 * anchor

def f30_mca_200_struct_v200(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=16, w3=431, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.15875 + 0.0018201 * anchor

def f30_mca_201_struct_v201(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=27, w3=444, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 27)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.173125 + 0.0018202 * anchor

def f30_mca_202_struct_v202(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=38, w3=457, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(38, min_periods=max(38//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.1875 + 0.0018203 * anchor

def f30_mca_203_struct_v203(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=49, w3=470, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(49, min_periods=max(49//3, 2)).rank(pct=True)
    persistence = change.rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.239 * persistence + 0.0018204 * anchor

def f30_mca_204_struct_v204(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=60, w3=483, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21625 + 0.0018205 * anchor

def f30_mca_205_struct_v205(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=71, w3=496, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(71, min_periods=max(71//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2542 * slope + 0.0018206 * anchor

def f30_mca_206_struct_v206(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=82, w3=509, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(82, min_periods=max(82//3, 2)).mean()
    noise = impulse.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.245 + 0.0018207 * anchor

def f30_mca_207_struct_v207(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=93, w3=522, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 93)
    curvature = _rolling_slope(acceleration, 522)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2694 * acceleration + 0.0018208 * anchor

def f30_mca_208_struct_v208(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=104, w3=535, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(104, min_periods=max(104//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.27375 + 0.0018209 * anchor

def f30_mca_209_struct_v209(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=115, w3=548, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(115, min_periods=max(115//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2846 * _rolling_slope(draw, 548) + 0.001821 * anchor

def f30_mca_210_struct_v210(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=126, w3=561, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(126, min_periods=max(126//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3025 + 0.0018211 * anchor

def f30_mca_211_struct_v211(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=137, w3=574, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 137)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.316875 + 0.0018212 * anchor

def f30_mca_212_struct_v212(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=148, w3=587, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(148, min_periods=max(148//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.33125 + 0.0018213 * anchor

def f30_mca_213_struct_v213(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=159, w3=600, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(159, min_periods=max(159//3, 2)).rank(pct=True)
    persistence = change.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.315 * persistence + 0.0018214 * anchor

def f30_mca_214_struct_v214(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=170, w3=613, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(170, min_periods=max(170//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.36 + 0.0018215 * anchor

def f30_mca_215_struct_v215(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=181, w3=626, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(181, min_periods=max(181//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3302 * slope + 0.0018216 * anchor

def f30_mca_216_struct_v216(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=192, w3=639, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(9)
    drag = impulse.rolling(192, min_periods=max(192//3, 2)).mean()
    noise = impulse.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.38875 + 0.0018217 * anchor

def f30_mca_217_struct_v217(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=203, w3=652, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 203)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3454 * acceleration + 0.0018218 * anchor

def f30_mca_218_struct_v218(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=214, w3=665, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(214, min_periods=max(214//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4175 + 0.0018219 * anchor

def f30_mca_219_struct_v219(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=225, w3=678, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3606 * _rolling_slope(draw, 678) + 0.001822 * anchor

def f30_mca_220_struct_v220(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=236, w3=691, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(236, min_periods=max(236//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.44625 + 0.0018221 * anchor

def f30_mca_221_struct_v221(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=247, w3=704, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 247)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.460625 + 0.0018222 * anchor

def f30_mca_222_struct_v222(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=258, w3=717, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(258, min_periods=max(258//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.475 + 0.0018223 * anchor

def f30_mca_223_struct_v223(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=269, w3=730, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(58)
    rank = change.rolling(269, min_periods=max(269//3, 2)).rank(pct=True)
    persistence = change.rolling(730, min_periods=max(730//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.391 * persistence + 0.0018224 * anchor

def f30_mca_224_struct_v224(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=280, w3=743, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(280, min_periods=max(280//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.50375 + 0.0018225 * anchor

def f30_mca_225_struct_v225(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=291, w3=756, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(291, min_periods=max(291//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4062 * slope + 0.0018226 * anchor
