"""94 beta decay and regime shift base features 76-150 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Macro_Factor - Institutional-grade short-side signal.
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

def f94_beta_076_struct_v76(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=231, w2=208, w3=152, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(208, min_periods=max(208//3, 2)).mean()
    noise = impulse.abs().rolling(152, min_periods=max(152//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.35 + 0.0043277 * anchor

def f94_beta_077_struct_v77(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=238, w2=219, w3=165, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 219)
    curvature = _rolling_slope(acceleration, 165)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.343 * acceleration + 0.0043278 * anchor

def f94_beta_078_struct_v78(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=245, w2=230, w3=178, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.37875 + 0.0043279 * anchor

def f94_beta_079_struct_v79(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=252, w2=241, w3=191, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(241, min_periods=max(241//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3582 * _rolling_slope(draw, 191) + 0.004328 * anchor

def f94_beta_080_struct_v80(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=8, w2=252, w3=204, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(252, min_periods=max(252//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4075 + 0.0043281 * anchor

def f94_beta_081_struct_v81(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=15, w2=263, w3=217, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 263)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=217, adjust=False).mean() * 1.421875 + 0.0043282 * anchor

def f94_beta_082_struct_v82(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=22, w2=274, w3=230, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(274, min_periods=max(274//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.43625 + 0.0043283 * anchor

def f94_beta_083_struct_v83(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=29, w2=285, w3=243, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(29)
    rank = change.rolling(285, min_periods=max(285//3, 2)).rank(pct=True)
    persistence = change.rolling(243, min_periods=max(243//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3886 * persistence + 0.0043284 * anchor

def f94_beta_084_struct_v84(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=36, w2=296, w3=256, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(296, min_periods=max(296//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.465 + 0.0043285 * anchor

def f94_beta_085_struct_v85(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=43, w2=307, w3=269, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4038 * slope + 0.0043286 * anchor

def f94_beta_086_struct_v86(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=50, w2=318, w3=282, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(50)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(282, min_periods=max(282//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.49375 + 0.0043287 * anchor

def f94_beta_087_struct_v87(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=57, w2=329, w3=295, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 329)
    curvature = _rolling_slope(acceleration, 295)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0426 * acceleration + 0.0043288 * anchor

def f94_beta_088_struct_v88(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=64, w2=340, w3=308, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5225 + 0.0043289 * anchor

def f94_beta_089_struct_v89(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=71, w2=351, w3=321, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(351, min_periods=max(351//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0578 * _rolling_slope(draw, 321) + 0.004329 * anchor

def f94_beta_090_struct_v90(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=78, w2=362, w3=334, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.55125 + 0.0043291 * anchor

def f94_beta_091_struct_v91(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=85, w2=373, w3=347, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 373)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.565625 + 0.0043292 * anchor

def f94_beta_092_struct_v92(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=92, w2=384, w3=360, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.58 + 0.0043293 * anchor

def f94_beta_093_struct_v93(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=99, w2=395, w3=373, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(99)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(373, min_periods=max(373//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0882 * persistence + 0.0043294 * anchor

def f94_beta_094_struct_v94(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=106, w2=406, w3=386, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60875 + 0.0043295 * anchor

def f94_beta_095_struct_v95(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=113, w2=417, w3=399, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1034 * slope + 0.0043296 * anchor

def f94_beta_096_struct_v96(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=120, w2=428, w3=412, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(120)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.864375 + 0.0043297 * anchor

def f94_beta_097_struct_v97(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=127, w2=439, w3=425, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 425)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1186 * acceleration + 0.0043298 * anchor

def f94_beta_098_struct_v98(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=134, w2=450, w3=438, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(450, min_periods=max(450//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.893125 + 0.0043299 * anchor

def f94_beta_099_struct_v99(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=141, w2=461, w3=451, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(461, min_periods=max(461//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1338 * _rolling_slope(draw, 451) + 0.00433 * anchor

def f94_beta_100_struct_v100(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=148, w2=472, w3=464, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(472, min_periods=max(472//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.921875 + 0.0043301 * anchor

def f94_beta_101_struct_v101(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=155, w2=483, w3=477, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.93625 + 0.0043302 * anchor

def f94_beta_102_struct_v102(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=162, w2=494, w3=490, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(494, min_periods=max(494//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.950625 + 0.0043303 * anchor

def f94_beta_103_struct_v103(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=169, w2=505, w3=503, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(503, min_periods=max(503//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1642 * persistence + 0.0043304 * anchor

def f94_beta_104_struct_v104(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=176, w2=13, w3=516, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.979375 + 0.0043305 * anchor

def f94_beta_105_struct_v105(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=183, w2=24, w3=529, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(24, min_periods=max(24//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1794 * slope + 0.0043306 * anchor

def f94_beta_106_struct_v106(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=190, w2=35, w3=542, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.008125 + 0.0043307 * anchor

def f94_beta_107_struct_v107(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=197, w2=46, w3=555, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 197)
    acceleration = _rolling_slope(velocity, 46)
    curvature = _rolling_slope(acceleration, 555)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1946 * acceleration + 0.0043308 * anchor

def f94_beta_108_struct_v108(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=204, w2=57, w3=568, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(57, min_periods=max(57//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.036875 + 0.0043309 * anchor

def f94_beta_109_struct_v109(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=211, w2=68, w3=581, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2098 * _rolling_slope(draw, 581) + 0.004331 * anchor

def f94_beta_110_struct_v110(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=218, w2=79, w3=594, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.065625 + 0.0043311 * anchor

def f94_beta_111_struct_v111(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=225, w2=90, w3=607, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 225)
    slow = _rolling_slope(x, 90)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.08 + 0.0043312 * anchor

def f94_beta_112_struct_v112(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=232, w2=101, w3=620, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(101, min_periods=max(101//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.094375 + 0.0043313 * anchor

def f94_beta_113_struct_v113(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=239, w2=112, w3=633, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(112, min_periods=max(112//3, 2)).rank(pct=True)
    persistence = change.rolling(633, min_periods=max(633//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2402 * persistence + 0.0043314 * anchor

def f94_beta_114_struct_v114(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=246, w2=123, w3=646, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(123, min_periods=max(123//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.123125 + 0.0043315 * anchor

def f94_beta_115_struct_v115(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=253, w2=134, w3=659, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(134, min_periods=max(134//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 253)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2554 * slope + 0.0043316 * anchor

def f94_beta_116_struct_v116(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=9, w2=145, w3=672, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(9)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(672, min_periods=max(672//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.151875 + 0.0043317 * anchor

def f94_beta_117_struct_v117(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=16, w2=156, w3=685, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 685)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2706 * acceleration + 0.0043318 * anchor

def f94_beta_118_struct_v118(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=23, w2=167, w3=698, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(167, min_periods=max(167//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.180625 + 0.0043319 * anchor

def f94_beta_119_struct_v119(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=30, w2=178, w3=711, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(178, min_periods=max(178//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2858 * _rolling_slope(draw, 711) + 0.004332 * anchor

def f94_beta_120_struct_v120(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=37, w2=189, w3=724, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(189, min_periods=max(189//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.209375 + 0.0043321 * anchor

def f94_beta_121_struct_v121(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=44, w2=200, w3=737, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.22375 + 0.0043322 * anchor

def f94_beta_122_struct_v122(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=51, w2=211, w3=750, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(211, min_periods=max(211//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.238125 + 0.0043323 * anchor

def f94_beta_123_struct_v123(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=58, w2=222, w3=763, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(58)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3162 * persistence + 0.0043324 * anchor

def f94_beta_124_struct_v124(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=65, w2=233, w3=19, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.266875 + 0.0043325 * anchor

def f94_beta_125_struct_v125(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=72, w2=244, w3=32, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3314 * slope + 0.0043326 * anchor

def f94_beta_126_struct_v126(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=79, w2=255, w3=45, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(79)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.295625 + 0.0043327 * anchor

def f94_beta_127_struct_v127(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=86, w2=266, w3=58, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 58)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3466 * acceleration + 0.0043328 * anchor

def f94_beta_128_struct_v128(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=93, w2=277, w3=71, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(277, min_periods=max(277//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(71) * 1.324375 + 0.0043329 * anchor

def f94_beta_129_struct_v129(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=100, w2=288, w3=84, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(288, min_periods=max(288//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3618 * _rolling_slope(draw, 84) + 0.004333 * anchor

def f94_beta_130_struct_v130(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=107, w2=299, w3=97, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.353125 + 0.0043331 * anchor

def f94_beta_131_struct_v131(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=114, w2=310, w3=110, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 310)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=110, adjust=False).mean() * 1.3675 + 0.0043332 * anchor

def f94_beta_132_struct_v132(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=121, w2=321, w3=123, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(321, min_periods=max(321//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.381875 + 0.0043333 * anchor

def f94_beta_133_struct_v133(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=128, w2=332, w3=136, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(332, min_periods=max(332//3, 2)).rank(pct=True)
    persistence = change.rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3922 * persistence + 0.0043334 * anchor

def f94_beta_134_struct_v134(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=135, w2=343, w3=149, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(343, min_periods=max(343//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.410625 + 0.0043335 * anchor

def f94_beta_135_struct_v135(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=142, w2=354, w3=162, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(354, min_periods=max(354//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4074 * slope + 0.0043336 * anchor

def f94_beta_136_struct_v136(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=149, w2=365, w3=175, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(365, min_periods=max(365//3, 2)).mean()
    noise = impulse.abs().rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.439375 + 0.0043337 * anchor

def f94_beta_137_struct_v137(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=156, w2=376, w3=188, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 376)
    curvature = _rolling_slope(acceleration, 188)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0462 * acceleration + 0.0043338 * anchor

def f94_beta_138_struct_v138(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=163, w2=387, w3=201, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.468125 + 0.0043339 * anchor

def f94_beta_139_struct_v139(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=170, w2=398, w3=214, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(398, min_periods=max(398//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0614 * _rolling_slope(draw, 214) + 0.004334 * anchor

def f94_beta_140_struct_v140(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=177, w2=409, w3=227, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(409, min_periods=max(409//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.496875 + 0.0043341 * anchor

def f94_beta_141_struct_v141(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=184, w2=420, w3=240, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=240, adjust=False).mean() * 1.51125 + 0.0043342 * anchor

def f94_beta_142_struct_v142(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=191, w2=431, w3=253, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(431, min_periods=max(431//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.525625 + 0.0043343 * anchor

def f94_beta_143_struct_v143(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=198, w2=442, w3=266, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(442, min_periods=max(442//3, 2)).rank(pct=True)
    persistence = change.rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0918 * persistence + 0.0043344 * anchor

def f94_beta_144_struct_v144(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=205, w2=453, w3=279, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(453, min_periods=max(453//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.554375 + 0.0043345 * anchor

def f94_beta_145_struct_v145(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=212, w2=464, w3=292, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(464, min_periods=max(464//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.107 * slope + 0.0043346 * anchor

def f94_beta_146_struct_v146(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=219, w2=475, w3=305, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(475, min_periods=max(475//3, 2)).mean()
    noise = impulse.abs().rolling(305, min_periods=max(305//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.583125 + 0.0043347 * anchor

def f94_beta_147_struct_v147(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=226, w2=486, w3=318, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 486)
    curvature = _rolling_slope(acceleration, 318)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1222 * acceleration + 0.0043348 * anchor

def f94_beta_148_struct_v148(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=233, w2=497, w3=331, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.611875 + 0.0043349 * anchor

def f94_beta_149_struct_v149(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=240, w2=508, w3=344, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1374 * _rolling_slope(draw, 344) + 0.004335 * anchor

def f94_beta_150_struct_v150(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=247, w2=16, w3=357, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.8675 + 0.0043351 * anchor
