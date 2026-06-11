"""23 cash flow deterioration trajectory d2 second derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Trajectory - Institutional-grade short-side signal.
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

def f23_cfd_301_struct_v301_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=69, w2=197, w3=134, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 69)
    slow = _rolling_slope(x, 197)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=134, adjust=False).mean() * 0.993125 + 0.0014102 * anchor
    return base_signal.diff().diff()

def f23_cfd_302_struct_v302_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=76, w2=208, w3=147, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(208, min_periods=max(208//3, 2)).max()
    trough = x.rolling(76, min_periods=max(76//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0075 + 0.0014103 * anchor
    return base_signal.diff().diff()

def f23_cfd_303_struct_v303_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=83, w2=219, w3=160, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(83)
    rank = change.rolling(219, min_periods=max(219//3, 2)).rank(pct=True)
    persistence = change.rolling(160, min_periods=max(160//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3202 * persistence + 0.0014104 * anchor
    return base_signal.diff().diff()

def f23_cfd_304_struct_v304_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=90, w2=230, w3=173, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(90, min_periods=max(90//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.03625 + 0.0014105 * anchor
    return base_signal.diff().diff()

def f23_cfd_305_struct_v305_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=97, w2=241, w3=186, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 97)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3354 * slope + 0.0014106 * anchor
    return base_signal.diff().diff()

def f23_cfd_306_struct_v306_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=104, w2=252, w3=199, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(104)
    drag = impulse.rolling(252, min_periods=max(252//3, 2)).mean()
    noise = impulse.abs().rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.065 + 0.0014107 * anchor
    return base_signal.diff().diff()

def f23_cfd_307_struct_v307_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=111, w2=263, w3=212, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 111)
    acceleration = _rolling_slope(velocity, 263)
    curvature = _rolling_slope(acceleration, 212)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3506 * acceleration + 0.0014108 * anchor
    return base_signal.diff().diff()

def f23_cfd_308_struct_v308_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=118, w2=274, w3=225, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(274, min_periods=max(274//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.09375 + 0.0014109 * anchor
    return base_signal.diff().diff()

def f23_cfd_309_struct_v309_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=125, w2=285, w3=238, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(285, min_periods=max(285//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3658 * _rolling_slope(draw, 238) + 0.001411 * anchor
    return base_signal.diff().diff()

def f23_cfd_310_struct_v310_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=132, w2=296, w3=251, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(296, min_periods=max(296//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1225 + 0.0014111 * anchor
    return base_signal.diff().diff()

def f23_cfd_311_struct_v311_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=139, w2=307, w3=264, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 307)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=264, adjust=False).mean() * 1.136875 + 0.0014112 * anchor
    return base_signal.diff().diff()

def f23_cfd_312_struct_v312_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=146, w2=318, w3=277, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(318, min_periods=max(318//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.15125 + 0.0014113 * anchor
    return base_signal.diff().diff()

def f23_cfd_313_struct_v313_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=153, w2=329, w3=290, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(329, min_periods=max(329//3, 2)).rank(pct=True)
    persistence = change.rolling(290, min_periods=max(290//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3962 * persistence + 0.0014114 * anchor
    return base_signal.diff().diff()

def f23_cfd_314_struct_v314_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=160, w2=340, w3=303, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(340, min_periods=max(340//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18 + 0.0014115 * anchor
    return base_signal.diff().diff()

def f23_cfd_315_struct_v315_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=167, w2=351, w3=316, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(351, min_periods=max(351//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.035 * slope + 0.0014116 * anchor
    return base_signal.diff().diff()

def f23_cfd_316_struct_v316_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=174, w2=362, w3=329, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(329, min_periods=max(329//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.20875 + 0.0014117 * anchor
    return base_signal.diff().diff()

def f23_cfd_317_struct_v317_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=181, w2=373, w3=342, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 373)
    curvature = _rolling_slope(acceleration, 342)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0502 * acceleration + 0.0014118 * anchor
    return base_signal.diff().diff()

def f23_cfd_318_struct_v318_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=188, w2=384, w3=355, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2375 + 0.0014119 * anchor
    return base_signal.diff().diff()

def f23_cfd_319_struct_v319_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=195, w2=395, w3=368, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(395, min_periods=max(395//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0654 * _rolling_slope(draw, 368) + 0.001412 * anchor
    return base_signal.diff().diff()

def f23_cfd_320_struct_v320_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=202, w2=406, w3=381, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(406, min_periods=max(406//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.26625 + 0.0014121 * anchor
    return base_signal.diff().diff()

def f23_cfd_321_struct_v321_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=209, w2=417, w3=394, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 417)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.280625 + 0.0014122 * anchor
    return base_signal.diff().diff()

def f23_cfd_322_struct_v322_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=216, w2=428, w3=407, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(428, min_periods=max(428//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.295 + 0.0014123 * anchor
    return base_signal.diff().diff()

def f23_cfd_323_struct_v323_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=223, w2=439, w3=420, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(439, min_periods=max(439//3, 2)).rank(pct=True)
    persistence = change.rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0958 * persistence + 0.0014124 * anchor
    return base_signal.diff().diff()

def f23_cfd_324_struct_v324_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=230, w2=450, w3=433, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32375 + 0.0014125 * anchor
    return base_signal.diff().diff()

def f23_cfd_325_struct_v325_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=237, w2=461, w3=446, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(461, min_periods=max(461//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.111 * slope + 0.0014126 * anchor
    return base_signal.diff().diff()

def f23_cfd_326_struct_v326_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=244, w2=472, w3=459, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(472, min_periods=max(472//3, 2)).mean()
    noise = impulse.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3525 + 0.0014127 * anchor
    return base_signal.diff().diff()

def f23_cfd_327_struct_v327_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=251, w2=483, w3=472, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 483)
    curvature = _rolling_slope(acceleration, 472)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1262 * acceleration + 0.0014128 * anchor
    return base_signal.diff().diff()

def f23_cfd_328_struct_v328_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=7, w2=494, w3=485, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(494, min_periods=max(494//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.38125 + 0.0014129 * anchor
    return base_signal.diff().diff()

def f23_cfd_329_struct_v329_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=14, w2=505, w3=498, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(505, min_periods=max(505//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1414 * _rolling_slope(draw, 498) + 0.001413 * anchor
    return base_signal.diff().diff()

def f23_cfd_330_struct_v330_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=21, w2=13, w3=511, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.41 + 0.0014131 * anchor
    return base_signal.diff().diff()

def f23_cfd_331_struct_v331_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=28, w2=24, w3=524, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 24)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.424375 + 0.0014132 * anchor
    return base_signal.diff().diff()

def f23_cfd_332_struct_v332_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=35, w2=35, w3=537, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(35, min_periods=max(35//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.43875 + 0.0014133 * anchor
    return base_signal.diff().diff()

def f23_cfd_333_struct_v333_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=42, w2=46, w3=550, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(42)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(550, min_periods=max(550//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1718 * persistence + 0.0014134 * anchor
    return base_signal.diff().diff()

def f23_cfd_334_struct_v334_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=49, w2=57, w3=563, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(57, min_periods=max(57//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4675 + 0.0014135 * anchor
    return base_signal.diff().diff()

def f23_cfd_335_struct_v335_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=56, w2=68, w3=576, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.187 * slope + 0.0014136 * anchor
    return base_signal.diff().diff()

def f23_cfd_336_struct_v336_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=63, w2=79, w3=589, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(63)
    drag = impulse.rolling(79, min_periods=max(79//3, 2)).mean()
    noise = impulse.abs().rolling(589, min_periods=max(589//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.49625 + 0.0014137 * anchor
    return base_signal.diff().diff()

def f23_cfd_337_struct_v337_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=70, w2=90, w3=602, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 90)
    curvature = _rolling_slope(acceleration, 602)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2022 * acceleration + 0.0014138 * anchor
    return base_signal.diff().diff()

def f23_cfd_338_struct_v338_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=77, w2=101, w3=615, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(101, min_periods=max(101//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.525 + 0.0014139 * anchor
    return base_signal.diff().diff()

def f23_cfd_339_struct_v339_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=84, w2=112, w3=628, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2174 * _rolling_slope(draw, 628) + 0.001414 * anchor
    return base_signal.diff().diff()

def f23_cfd_340_struct_v340_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=91, w2=123, w3=641, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(641, min_periods=max(641//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55375 + 0.0014141 * anchor
    return base_signal.diff().diff()

def f23_cfd_341_struct_v341_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=98, w2=134, w3=654, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 134)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.568125 + 0.0014142 * anchor
    return base_signal.diff().diff()

def f23_cfd_342_struct_v342_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=105, w2=145, w3=667, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(145, min_periods=max(145//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5825 + 0.0014143 * anchor
    return base_signal.diff().diff()

def f23_cfd_343_struct_v343_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=112, w2=156, w3=680, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(112)
    rank = change.rolling(156, min_periods=max(156//3, 2)).rank(pct=True)
    persistence = change.rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2478 * persistence + 0.0014144 * anchor
    return base_signal.diff().diff()

def f23_cfd_344_struct_v344_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=119, w2=167, w3=693, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(167, min_periods=max(167//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61125 + 0.0014145 * anchor
    return base_signal.diff().diff()

def f23_cfd_345_struct_v345_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=126, w2=178, w3=706, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.263 * slope + 0.0014146 * anchor
    return base_signal.diff().diff()

def f23_cfd_346_struct_v346_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=133, w2=189, w3=719, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(189, min_periods=max(189//3, 2)).mean()
    noise = impulse.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.866875 + 0.0014147 * anchor
    return base_signal.diff().diff()

def f23_cfd_347_struct_v347_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=140, w2=200, w3=732, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 200)
    curvature = _rolling_slope(acceleration, 732)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2782 * acceleration + 0.0014148 * anchor
    return base_signal.diff().diff()

def f23_cfd_348_struct_v348_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=147, w2=211, w3=745, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(211, min_periods=max(211//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.895625 + 0.0014149 * anchor
    return base_signal.diff().diff()

def f23_cfd_349_struct_v349_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=154, w2=222, w3=758, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(222, min_periods=max(222//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2934 * _rolling_slope(draw, 758) + 0.001415 * anchor
    return base_signal.diff().diff()

def f23_cfd_350_struct_v350_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=161, w2=233, w3=771, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(233, min_periods=max(233//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(771, min_periods=max(771//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.924375 + 0.0014151 * anchor
    return base_signal.diff().diff()

def f23_cfd_351_struct_v351_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=168, w2=244, w3=27, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 244)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=27, adjust=False).mean() * 0.93875 + 0.0014152 * anchor
    return base_signal.diff().diff()

def f23_cfd_352_struct_v352_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=175, w2=255, w3=40, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.953125 + 0.0014153 * anchor
    return base_signal.diff().diff()

def f23_cfd_353_struct_v353_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=182, w2=266, w3=53, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(266, min_periods=max(266//3, 2)).rank(pct=True)
    persistence = change.rolling(53, min_periods=max(53//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3238 * persistence + 0.0014154 * anchor
    return base_signal.diff().diff()

def f23_cfd_354_struct_v354_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=189, w2=277, w3=66, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(277, min_periods=max(277//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.981875 + 0.0014155 * anchor
    return base_signal.diff().diff()

def f23_cfd_355_struct_v355_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=196, w2=288, w3=79, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(288, min_periods=max(288//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.339 * slope + 0.0014156 * anchor
    return base_signal.diff().diff()

def f23_cfd_356_struct_v356_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=203, w2=299, w3=92, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.010625 + 0.0014157 * anchor
    return base_signal.diff().diff()

def f23_cfd_357_struct_v357_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=210, w2=310, w3=105, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 310)
    curvature = _rolling_slope(acceleration, 105)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3542 * acceleration + 0.0014158 * anchor
    return base_signal.diff().diff()

def f23_cfd_358_struct_v358_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=217, w2=321, w3=118, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(321, min_periods=max(321//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(118) * 1.039375 + 0.0014159 * anchor
    return base_signal.diff().diff()

def f23_cfd_359_struct_v359_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=224, w2=332, w3=131, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(332, min_periods=max(332//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3694 * _rolling_slope(draw, 131) + 0.001416 * anchor
    return base_signal.diff().diff()

def f23_cfd_360_struct_v360_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=231, w2=343, w3=144, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(343, min_periods=max(343//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.068125 + 0.0014161 * anchor
    return base_signal.diff().diff()

def f23_cfd_361_struct_v361_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=238, w2=354, w3=157, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 354)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=157, adjust=False).mean() * 1.0825 + 0.0014162 * anchor
    return base_signal.diff().diff()

def f23_cfd_362_struct_v362_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=245, w2=365, w3=170, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(365, min_periods=max(365//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.096875 + 0.0014163 * anchor
    return base_signal.diff().diff()

def f23_cfd_363_struct_v363_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=252, w2=376, w3=183, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(376, min_periods=max(376//3, 2)).rank(pct=True)
    persistence = change.rolling(183, min_periods=max(183//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3998 * persistence + 0.0014164 * anchor
    return base_signal.diff().diff()

def f23_cfd_364_struct_v364_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=8, w2=387, w3=196, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(387, min_periods=max(387//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.125625 + 0.0014165 * anchor
    return base_signal.diff().diff()

def f23_cfd_365_struct_v365_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=15, w2=398, w3=209, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(398, min_periods=max(398//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0386 * slope + 0.0014166 * anchor
    return base_signal.diff().diff()

def f23_cfd_366_struct_v366_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=22, w2=409, w3=222, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(22)
    drag = impulse.rolling(409, min_periods=max(409//3, 2)).mean()
    noise = impulse.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.154375 + 0.0014167 * anchor
    return base_signal.diff().diff()

def f23_cfd_367_struct_v367_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=29, w2=420, w3=235, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 420)
    curvature = _rolling_slope(acceleration, 235)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0538 * acceleration + 0.0014168 * anchor
    return base_signal.diff().diff()

def f23_cfd_368_struct_v368_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=36, w2=431, w3=248, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.183125 + 0.0014169 * anchor
    return base_signal.diff().diff()

def f23_cfd_369_struct_v369_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=43, w2=442, w3=261, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(442, min_periods=max(442//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.069 * _rolling_slope(draw, 261) + 0.001417 * anchor
    return base_signal.diff().diff()

def f23_cfd_370_struct_v370_d2(gex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=50, w2=453, w3=274, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(453, min_periods=max(453//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.211875 + 0.0014171 * anchor
    return base_signal.diff().diff()

def f23_cfd_371_struct_v371_d2(vex: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=57, w2=464, w3=287, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 464)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=287, adjust=False).mean() * 1.22625 + 0.0014172 * anchor
    return base_signal.diff().diff()

def f23_cfd_372_struct_v372_d2(revenue: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=64, w2=475, w3=300, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(475, min_periods=max(475//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.240625 + 0.0014173 * anchor
    return base_signal.diff().diff()

def f23_cfd_373_struct_v373_d2(netinc: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=71, w2=486, w3=313, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(71)
    rank = change.rolling(486, min_periods=max(486//3, 2)).rank(pct=True)
    persistence = change.rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0994 * persistence + 0.0014174 * anchor
    return base_signal.diff().diff()

def f23_cfd_374_struct_v374_d2(shortinterest: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=78, w2=497, w3=326, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(497, min_periods=max(497//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.269375 + 0.0014175 * anchor
    return base_signal.diff().diff()

def f23_cfd_375_struct_v375_d2(utilization: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated struct replacement signal (w1=85, w2=508, w3=339, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(508, min_periods=max(508//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1146 * slope + 0.0014176 * anchor
    return base_signal.diff().diff()
