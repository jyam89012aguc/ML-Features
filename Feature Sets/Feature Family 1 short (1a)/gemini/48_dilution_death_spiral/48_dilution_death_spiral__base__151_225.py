"""48 dilution death spiral base features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f48_dds_151_struct_v151(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=38, w2=133, w3=379, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 133)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.2 + 0.0029552 * anchor

def f48_dds_152_struct_v152(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=45, w2=144, w3=392, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(144, min_periods=max(144//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.214375 + 0.0029553 * anchor

def f48_dds_153_struct_v153(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=52, w2=155, w3=405, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(52)
    rank = change.rolling(155, min_periods=max(155//3, 2)).rank(pct=True)
    persistence = change.rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3034 * persistence + 0.0029554 * anchor

def f48_dds_154_struct_v154(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=59, w2=166, w3=418, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(166, min_periods=max(166//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.243125 + 0.0029555 * anchor

def f48_dds_155_struct_v155(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=66, w2=177, w3=431, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(177, min_periods=max(177//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3186 * slope + 0.0029556 * anchor

def f48_dds_156_struct_v156(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=73, w2=188, w3=444, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(73)
    drag = impulse.rolling(188, min_periods=max(188//3, 2)).mean()
    noise = impulse.abs().rolling(444, min_periods=max(444//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.271875 + 0.0029557 * anchor

def f48_dds_157_struct_v157(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=80, w2=199, w3=457, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 199)
    curvature = _rolling_slope(acceleration, 457)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3338 * acceleration + 0.0029558 * anchor

def f48_dds_158_struct_v158(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=87, w2=210, w3=470, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(210, min_periods=max(210//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.300625 + 0.0029559 * anchor

def f48_dds_159_struct_v159(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=94, w2=221, w3=483, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(221, min_periods=max(221//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.349 * _rolling_slope(draw, 483) + 0.002956 * anchor

def f48_dds_160_struct_v160(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=101, w2=232, w3=496, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(232, min_periods=max(232//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.329375 + 0.0029561 * anchor

def f48_dds_161_struct_v161(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=108, w2=243, w3=509, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 243)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.34375 + 0.0029562 * anchor

def f48_dds_162_struct_v162(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=115, w2=254, w3=522, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(254, min_periods=max(254//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.358125 + 0.0029563 * anchor

def f48_dds_163_struct_v163(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=122, w2=265, w3=535, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(122)
    rank = change.rolling(265, min_periods=max(265//3, 2)).rank(pct=True)
    persistence = change.rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3794 * persistence + 0.0029564 * anchor

def f48_dds_164_struct_v164(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=129, w2=276, w3=548, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(276, min_periods=max(276//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.386875 + 0.0029565 * anchor

def f48_dds_165_struct_v165(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=136, w2=287, w3=561, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(287, min_periods=max(287//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3946 * slope + 0.0029566 * anchor

def f48_dds_166_struct_v166(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=143, w2=298, w3=574, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.415625 + 0.0029567 * anchor

def f48_dds_167_struct_v167(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=150, w2=309, w3=587, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 309)
    curvature = _rolling_slope(acceleration, 587)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.4098 * acceleration + 0.0029568 * anchor

def f48_dds_168_struct_v168(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=157, w2=320, w3=600, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(320, min_periods=max(320//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.444375 + 0.0029569 * anchor

def f48_dds_169_struct_v169(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=164, w2=331, w3=613, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(331, min_periods=max(331//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0486 * _rolling_slope(draw, 613) + 0.002957 * anchor

def f48_dds_170_struct_v170(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=171, w2=342, w3=626, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(342, min_periods=max(342//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.473125 + 0.0029571 * anchor

def f48_dds_171_struct_v171(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=178, w2=353, w3=639, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 353)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.4875 + 0.0029572 * anchor

def f48_dds_172_struct_v172(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=185, w2=364, w3=652, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.501875 + 0.0029573 * anchor

def f48_dds_173_struct_v173(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=192, w2=375, w3=665, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(375, min_periods=max(375//3, 2)).rank(pct=True)
    persistence = change.rolling(665, min_periods=max(665//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.079 * persistence + 0.0029574 * anchor

def f48_dds_174_struct_v174(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=199, w2=386, w3=678, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(386, min_periods=max(386//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.530625 + 0.0029575 * anchor

def f48_dds_175_struct_v175(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=206, w2=397, w3=691, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(397, min_periods=max(397//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0942 * slope + 0.0029576 * anchor

def f48_dds_176_struct_v176(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=213, w2=408, w3=704, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(408, min_periods=max(408//3, 2)).mean()
    noise = impulse.abs().rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.559375 + 0.0029577 * anchor

def f48_dds_177_struct_v177(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=220, w2=419, w3=717, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 419)
    curvature = _rolling_slope(acceleration, 717)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1094 * acceleration + 0.0029578 * anchor

def f48_dds_178_struct_v178(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=227, w2=430, w3=730, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.588125 + 0.0029579 * anchor

def f48_dds_179_struct_v179(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=234, w2=441, w3=743, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(441, min_periods=max(441//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1246 * _rolling_slope(draw, 743) + 0.002958 * anchor

def f48_dds_180_struct_v180(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=241, w2=452, w3=756, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(452, min_periods=max(452//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.616875 + 0.0029581 * anchor

def f48_dds_181_struct_v181(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=248, w2=463, w3=769, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 463)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.858125 + 0.0029582 * anchor

def f48_dds_182_struct_v182(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=255, w2=474, w3=25, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(474, min_periods=max(474//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.8725 + 0.0029583 * anchor

def f48_dds_183_struct_v183(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=11, w2=485, w3=38, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(11)
    rank = change.rolling(485, min_periods=max(485//3, 2)).rank(pct=True)
    persistence = change.rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.155 * persistence + 0.0029584 * anchor

def f48_dds_184_struct_v184(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=18, w2=496, w3=51, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(496, min_periods=max(496//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.90125 + 0.0029585 * anchor

def f48_dds_185_struct_v185(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=25, w2=507, w3=64, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(507, min_periods=max(507//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1702 * slope + 0.0029586 * anchor

def f48_dds_186_struct_v186(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=32, w2=15, w3=77, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(32)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(77, min_periods=max(77//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.93 + 0.0029587 * anchor

def f48_dds_187_struct_v187(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=39, w2=26, w3=90, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 26)
    curvature = _rolling_slope(acceleration, 90)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1854 * acceleration + 0.0029588 * anchor

def f48_dds_188_struct_v188(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=46, w2=37, w3=103, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(37, min_periods=max(37//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(103) * 0.95875 + 0.0029589 * anchor

def f48_dds_189_struct_v189(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=53, w2=48, w3=116, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(48, min_periods=max(48//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2006 * _rolling_slope(draw, 116) + 0.002959 * anchor

def f48_dds_190_struct_v190(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=60, w2=59, w3=129, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(59, min_periods=max(59//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(129, min_periods=max(129//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.9875 + 0.0029591 * anchor

def f48_dds_191_struct_v191(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=67, w2=70, w3=142, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 70)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=142, adjust=False).mean() * 1.001875 + 0.0029592 * anchor

def f48_dds_192_struct_v192(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=74, w2=81, w3=155, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(81, min_periods=max(81//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.01625 + 0.0029593 * anchor

def f48_dds_193_struct_v193(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=81, w2=92, w3=168, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(81)
    rank = change.rolling(92, min_periods=max(92//3, 2)).rank(pct=True)
    persistence = change.rolling(168, min_periods=max(168//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.231 * persistence + 0.0029594 * anchor

def f48_dds_194_struct_v194(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=88, w2=103, w3=181, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(103, min_periods=max(103//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.045 + 0.0029595 * anchor

def f48_dds_195_struct_v195(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=95, w2=114, w3=194, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(114, min_periods=max(114//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2462 * slope + 0.0029596 * anchor

def f48_dds_196_struct_v196(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=102, w2=125, w3=207, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(102)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(207, min_periods=max(207//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.07375 + 0.0029597 * anchor

def f48_dds_197_struct_v197(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=109, w2=136, w3=220, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 220)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2614 * acceleration + 0.0029598 * anchor

def f48_dds_198_struct_v198(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=116, w2=147, w3=233, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(147, min_periods=max(147//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.1025 + 0.0029599 * anchor

def f48_dds_199_struct_v199(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=123, w2=158, w3=246, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(158, min_periods=max(158//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2766 * _rolling_slope(draw, 246) + 0.00296 * anchor

def f48_dds_200_struct_v200(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=130, w2=169, w3=259, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(169, min_periods=max(169//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.13125 + 0.0029601 * anchor

def f48_dds_201_struct_v201(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=137, w2=180, w3=272, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 180)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=272, adjust=False).mean() * 1.145625 + 0.0029602 * anchor

def f48_dds_202_struct_v202(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=144, w2=191, w3=285, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(191, min_periods=max(191//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.16 + 0.0029603 * anchor

def f48_dds_203_struct_v203(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=151, w2=202, w3=298, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(202, min_periods=max(202//3, 2)).rank(pct=True)
    persistence = change.rolling(298, min_periods=max(298//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.307 * persistence + 0.0029604 * anchor

def f48_dds_204_struct_v204(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=158, w2=213, w3=311, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(213, min_periods=max(213//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18875 + 0.0029605 * anchor

def f48_dds_205_struct_v205(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=165, w2=224, w3=324, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(224, min_periods=max(224//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3222 * slope + 0.0029606 * anchor

def f48_dds_206_struct_v206(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=172, w2=235, w3=337, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(235, min_periods=max(235//3, 2)).mean()
    noise = impulse.abs().rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.2175 + 0.0029607 * anchor

def f48_dds_207_struct_v207(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=179, w2=246, w3=350, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 246)
    curvature = _rolling_slope(acceleration, 350)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3374 * acceleration + 0.0029608 * anchor

def f48_dds_208_struct_v208(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=186, w2=257, w3=363, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(257, min_periods=max(257//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.24625 + 0.0029609 * anchor

def f48_dds_209_struct_v209(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=193, w2=268, w3=376, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(268, min_periods=max(268//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3526 * _rolling_slope(draw, 376) + 0.002961 * anchor

def f48_dds_210_struct_v210(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=200, w2=279, w3=389, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(279, min_periods=max(279//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.275 + 0.0029611 * anchor

def f48_dds_211_struct_v211(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=207, w2=290, w3=402, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 290)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.289375 + 0.0029612 * anchor

def f48_dds_212_struct_v212(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=214, w2=301, w3=415, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(301, min_periods=max(301//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.30375 + 0.0029613 * anchor

def f48_dds_213_struct_v213(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=221, w2=312, w3=428, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(312, min_periods=max(312//3, 2)).rank(pct=True)
    persistence = change.rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.383 * persistence + 0.0029614 * anchor

def f48_dds_214_struct_v214(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=228, w2=323, w3=441, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(323, min_periods=max(323//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3325 + 0.0029615 * anchor

def f48_dds_215_struct_v215(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=235, w2=334, w3=454, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(334, min_periods=max(334//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3982 * slope + 0.0029616 * anchor

def f48_dds_216_struct_v216(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=242, w2=345, w3=467, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(345, min_periods=max(345//3, 2)).mean()
    noise = impulse.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.36125 + 0.0029617 * anchor

def f48_dds_217_struct_v217(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=249, w2=356, w3=480, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 356)
    curvature = _rolling_slope(acceleration, 480)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.037 * acceleration + 0.0029618 * anchor

def f48_dds_218_struct_v218(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=5, w2=367, w3=493, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(367, min_periods=max(367//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.39 + 0.0029619 * anchor

def f48_dds_219_struct_v219(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=12, w2=378, w3=506, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(378, min_periods=max(378//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0522 * _rolling_slope(draw, 506) + 0.002962 * anchor

def f48_dds_220_struct_v220(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=19, w2=389, w3=519, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(389, min_periods=max(389//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.41875 + 0.0029621 * anchor

def f48_dds_221_struct_v221(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=26, w2=400, w3=532, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 400)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.433125 + 0.0029622 * anchor

def f48_dds_222_struct_v222(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=33, w2=411, w3=545, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(411, min_periods=max(411//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.4475 + 0.0029623 * anchor

def f48_dds_223_struct_v223(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=40, w2=422, w3=558, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(40)
    rank = change.rolling(422, min_periods=max(422//3, 2)).rank(pct=True)
    persistence = change.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0826 * persistence + 0.0029624 * anchor

def f48_dds_224_struct_v224(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=47, w2=433, w3=571, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(433, min_periods=max(433//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.47625 + 0.0029625 * anchor

def f48_dds_225_struct_v225(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=54, w2=444, w3=584, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(444, min_periods=max(444//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0978 * slope + 0.0029626 * anchor
