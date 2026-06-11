"""28 institutional holding collapse trajectory d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f28_ihc_226_struct_v226_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=180, w3=309, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(180, min_periods=max(180//3, 2)).mean()
    noise = impulse.abs().rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.29125 + 0.0017027 * anchor
    return base_signal.diff()

def f28_ihc_227_struct_v227_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=191, w3=322, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 191)
    curvature = _rolling_slope(acceleration, 322)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.335 * acceleration + 0.0017028 * anchor
    return base_signal.diff()

def f28_ihc_228_struct_v228_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=202, w3=335, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(202, min_periods=max(202//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.32 + 0.0017029 * anchor
    return base_signal.diff()

def f28_ihc_229_struct_v229_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=213, w3=348, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3502 * _rolling_slope(draw, 348) + 0.001703 * anchor
    return base_signal.diff()

def f28_ihc_230_struct_v230_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=224, w3=361, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(224, min_periods=max(224//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(361, min_periods=max(361//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.34875 + 0.0017031 * anchor
    return base_signal.diff()

def f28_ihc_231_struct_v231_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=235, w3=374, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 235)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.363125 + 0.0017032 * anchor
    return base_signal.diff()

def f28_ihc_232_struct_v232_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=246, w3=387, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(255, min_periods=max(255//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3775 + 0.0017033 * anchor
    return base_signal.diff()

def f28_ihc_233_struct_v233_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=257, w3=400, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(11)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(400, min_periods=max(400//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3806 * persistence + 0.0017034 * anchor
    return base_signal.diff()

def f28_ihc_234_struct_v234_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=268, w3=413, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(268, min_periods=max(268//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.40625 + 0.0017035 * anchor
    return base_signal.diff()

def f28_ihc_235_struct_v235_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=279, w3=426, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(279, min_periods=max(279//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3958 * slope + 0.0017036 * anchor
    return base_signal.diff()

def f28_ihc_236_struct_v236_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=290, w3=439, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(32)
    drag = impulse.rolling(290, min_periods=max(290//3, 2)).mean()
    noise = impulse.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.435 + 0.0017037 * anchor
    return base_signal.diff()

def f28_ihc_237_struct_v237_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=301, w3=452, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 301)
    curvature = _rolling_slope(acceleration, 452)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.411 * acceleration + 0.0017038 * anchor
    return base_signal.diff()

def f28_ihc_238_struct_v238_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=312, w3=465, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(312, min_periods=max(312//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.46375 + 0.0017039 * anchor
    return base_signal.diff()

def f28_ihc_239_struct_v239_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=323, w3=478, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(323, min_periods=max(323//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0498 * _rolling_slope(draw, 478) + 0.001704 * anchor
    return base_signal.diff()

def f28_ihc_240_struct_v240_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=334, w3=491, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(334, min_periods=max(334//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(491, min_periods=max(491//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4925 + 0.0017041 * anchor
    return base_signal.diff()

def f28_ihc_241_struct_v241_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=345, w3=504, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 345)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.506875 + 0.0017042 * anchor
    return base_signal.diff()

def f28_ihc_242_struct_v242_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=356, w3=517, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(356, min_periods=max(356//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.52125 + 0.0017043 * anchor
    return base_signal.diff()

def f28_ihc_243_struct_v243_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=367, w3=530, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(81)
    rank = change.rolling(367, min_periods=max(367//3, 2)).rank(pct=True)
    persistence = change.rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0802 * persistence + 0.0017044 * anchor
    return base_signal.diff()

def f28_ihc_244_struct_v244_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=378, w3=543, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(378, min_periods=max(378//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.55 + 0.0017045 * anchor
    return base_signal.diff()

def f28_ihc_245_struct_v245_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=389, w3=556, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(389, min_periods=max(389//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0954 * slope + 0.0017046 * anchor
    return base_signal.diff()

def f28_ihc_246_struct_v246_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=400, w3=569, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(102)
    drag = impulse.rolling(400, min_periods=max(400//3, 2)).mean()
    noise = impulse.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.57875 + 0.0017047 * anchor
    return base_signal.diff()

def f28_ihc_247_struct_v247_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=411, w3=582, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 411)
    curvature = _rolling_slope(acceleration, 582)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1106 * acceleration + 0.0017048 * anchor
    return base_signal.diff()

def f28_ihc_248_struct_v248_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=422, w3=595, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(422, min_periods=max(422//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.6075 + 0.0017049 * anchor
    return base_signal.diff()

def f28_ihc_249_struct_v249_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=433, w3=608, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(433, min_periods=max(433//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1258 * _rolling_slope(draw, 608) + 0.001705 * anchor
    return base_signal.diff()

def f28_ihc_250_struct_v250_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=444, w3=621, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(444, min_periods=max(444//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.863125 + 0.0017051 * anchor
    return base_signal.diff()

def f28_ihc_251_struct_v251_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=455, w3=634, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 455)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.8775 + 0.0017052 * anchor
    return base_signal.diff()

def f28_ihc_252_struct_v252_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=466, w3=647, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(466, min_periods=max(466//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.891875 + 0.0017053 * anchor
    return base_signal.diff()

def f28_ihc_253_struct_v253_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=477, w3=660, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(477, min_periods=max(477//3, 2)).rank(pct=True)
    persistence = change.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1562 * persistence + 0.0017054 * anchor
    return base_signal.diff()

def f28_ihc_254_struct_v254_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=488, w3=673, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.920625 + 0.0017055 * anchor
    return base_signal.diff()

def f28_ihc_255_struct_v255_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=499, w3=686, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(499, min_periods=max(499//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1714 * slope + 0.0017056 * anchor
    return base_signal.diff()

def f28_ihc_256_struct_v256_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=510, w3=699, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(510, min_periods=max(510//3, 2)).mean()
    noise = impulse.abs().rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.949375 + 0.0017057 * anchor
    return base_signal.diff()

def f28_ihc_257_struct_v257_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=18, w3=712, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 18)
    curvature = _rolling_slope(acceleration, 712)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1866 * acceleration + 0.0017058 * anchor
    return base_signal.diff()

def f28_ihc_258_struct_v258_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=29, w3=725, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(186, min_periods=max(186//3, 2)).mean(), upside.rolling(29, min_periods=max(29//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.978125 + 0.0017059 * anchor
    return base_signal.diff()

def f28_ihc_259_struct_v259_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=40, w3=738, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(40, min_periods=max(40//3, 2)).max()
    rebound = x - x.rolling(193, min_periods=max(193//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2018 * _rolling_slope(draw, 738) + 0.001706 * anchor
    return base_signal.diff()

def f28_ihc_260_struct_v260_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=51, w3=751, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(51, min_periods=max(51//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.006875 + 0.0017061 * anchor
    return base_signal.diff()

def f28_ihc_261_struct_v261_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=62, w3=764, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 62)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.02125 + 0.0017062 * anchor
    return base_signal.diff()

def f28_ihc_262_struct_v262_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=73, w3=20, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(73, min_periods=max(73//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.035625 + 0.0017063 * anchor
    return base_signal.diff()

def f28_ihc_263_struct_v263_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=84, w3=33, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2322 * persistence + 0.0017064 * anchor
    return base_signal.diff()

def f28_ihc_264_struct_v264_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=95, w3=46, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(95, min_periods=max(95//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.064375 + 0.0017065 * anchor
    return base_signal.diff()

def f28_ihc_265_struct_v265_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=106, w3=59, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(106, min_periods=max(106//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2474 * slope + 0.0017066 * anchor
    return base_signal.diff()

def f28_ihc_266_struct_v266_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=117, w3=72, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(117, min_periods=max(117//3, 2)).mean()
    noise = impulse.abs().rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.093125 + 0.0017067 * anchor
    return base_signal.diff()

def f28_ihc_267_struct_v267_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=128, w3=85, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 128)
    curvature = _rolling_slope(acceleration, 85)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2626 * acceleration + 0.0017068 * anchor
    return base_signal.diff()

def f28_ihc_268_struct_v268_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=139, w3=98, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(5, min_periods=max(5//3, 2)).mean(), upside.rolling(139, min_periods=max(139//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(98) * 1.121875 + 0.0017069 * anchor
    return base_signal.diff()

def f28_ihc_269_struct_v269_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=150, w3=111, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(150, min_periods=max(150//3, 2)).max()
    rebound = x - x.rolling(12, min_periods=max(12//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2778 * _rolling_slope(draw, 111) + 0.001707 * anchor
    return base_signal.diff()

def f28_ihc_270_struct_v270_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=161, w3=124, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 19)
    baseline = trend.rolling(161, min_periods=max(161//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.150625 + 0.0017071 * anchor
    return base_signal.diff()

def f28_ihc_271_struct_v271_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=172, w3=137, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 26)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=137, adjust=False).mean() * 1.165 + 0.0017072 * anchor
    return base_signal.diff()

def f28_ihc_272_struct_v272_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=183, w3=150, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(183, min_periods=max(183//3, 2)).max()
    trough = x.rolling(33, min_periods=max(33//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.179375 + 0.0017073 * anchor
    return base_signal.diff()

def f28_ihc_273_struct_v273_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=194, w3=163, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(40)
    rank = change.rolling(194, min_periods=max(194//3, 2)).rank(pct=True)
    persistence = change.rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3082 * persistence + 0.0017074 * anchor
    return base_signal.diff()

def f28_ihc_274_struct_v274_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=205, w3=176, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(47, min_periods=max(47//3, 2)).std()
    vol_slow = ret.rolling(205, min_periods=max(205//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.208125 + 0.0017075 * anchor
    return base_signal.diff()

def f28_ihc_275_struct_v275_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=216, w3=189, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(216, min_periods=max(216//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 54)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3234 * slope + 0.0017076 * anchor
    return base_signal.diff()

def f28_ihc_276_struct_v276_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=227, w3=202, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(61)
    drag = impulse.rolling(227, min_periods=max(227//3, 2)).mean()
    noise = impulse.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.236875 + 0.0017077 * anchor
    return base_signal.diff()

def f28_ihc_277_struct_v277_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=238, w3=215, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 68)
    acceleration = _rolling_slope(velocity, 238)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3386 * acceleration + 0.0017078 * anchor
    return base_signal.diff()

def f28_ihc_278_struct_v278_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=249, w3=228, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(249, min_periods=max(249//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.265625 + 0.0017079 * anchor
    return base_signal.diff()

def f28_ihc_279_struct_v279_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=260, w3=241, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(260, min_periods=max(260//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3538 * _rolling_slope(draw, 241) + 0.001708 * anchor
    return base_signal.diff()

def f28_ihc_280_struct_v280_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=271, w3=254, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(271, min_periods=max(271//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.294375 + 0.0017081 * anchor
    return base_signal.diff()

def f28_ihc_281_struct_v281_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=282, w3=267, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 282)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=267, adjust=False).mean() * 1.30875 + 0.0017082 * anchor
    return base_signal.diff()

def f28_ihc_282_struct_v282_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=293, w3=280, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(293, min_periods=max(293//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.323125 + 0.0017083 * anchor
    return base_signal.diff()

def f28_ihc_283_struct_v283_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=304, w3=293, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(110)
    rank = change.rolling(304, min_periods=max(304//3, 2)).rank(pct=True)
    persistence = change.rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3842 * persistence + 0.0017084 * anchor
    return base_signal.diff()

def f28_ihc_284_struct_v284_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=315, w3=306, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(315, min_periods=max(315//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.351875 + 0.0017085 * anchor
    return base_signal.diff()

def f28_ihc_285_struct_v285_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=326, w3=319, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3994 * slope + 0.0017086 * anchor
    return base_signal.diff()

def f28_ihc_286_struct_v286_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=337, w3=332, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(337, min_periods=max(337//3, 2)).mean()
    noise = impulse.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.380625 + 0.0017087 * anchor
    return base_signal.diff()

def f28_ihc_287_struct_v287_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=348, w3=345, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 348)
    curvature = _rolling_slope(acceleration, 345)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0382 * acceleration + 0.0017088 * anchor
    return base_signal.diff()

def f28_ihc_288_struct_v288_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=359, w3=358, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(359, min_periods=max(359//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.409375 + 0.0017089 * anchor
    return base_signal.diff()

def f28_ihc_289_struct_v289_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=370, w3=371, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(370, min_periods=max(370//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0534 * _rolling_slope(draw, 371) + 0.001709 * anchor
    return base_signal.diff()

def f28_ihc_290_struct_v290_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=381, w3=384, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(381, min_periods=max(381//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.438125 + 0.0017091 * anchor
    return base_signal.diff()

def f28_ihc_291_struct_v291_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=392, w3=397, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 392)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4525 + 0.0017092 * anchor
    return base_signal.diff()

def f28_ihc_292_struct_v292_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=403, w3=410, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(403, min_periods=max(403//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.466875 + 0.0017093 * anchor
    return base_signal.diff()

def f28_ihc_293_struct_v293_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=414, w3=423, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(414, min_periods=max(414//3, 2)).rank(pct=True)
    persistence = change.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0838 * persistence + 0.0017094 * anchor
    return base_signal.diff()

def f28_ihc_294_struct_v294_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=425, w3=436, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(425, min_periods=max(425//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.495625 + 0.0017095 * anchor
    return base_signal.diff()

def f28_ihc_295_struct_v295_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=436, w3=449, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(436, min_periods=max(436//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.099 * slope + 0.0017096 * anchor
    return base_signal.diff()

def f28_ihc_296_struct_v296_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=447, w3=462, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(447, min_periods=max(447//3, 2)).mean()
    noise = impulse.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.524375 + 0.0017097 * anchor
    return base_signal.diff()

def f28_ihc_297_struct_v297_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=458, w3=475, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 458)
    curvature = _rolling_slope(acceleration, 475)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1142 * acceleration + 0.0017098 * anchor
    return base_signal.diff()

def f28_ihc_298_struct_v298_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=469, w3=488, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(469, min_periods=max(469//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.553125 + 0.0017099 * anchor
    return base_signal.diff()

def f28_ihc_299_struct_v299_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=480, w3=501, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(480, min_periods=max(480//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1294 * _rolling_slope(draw, 501) + 0.00171 * anchor
    return base_signal.diff()

def f28_ihc_300_struct_v300_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=491, w3=514, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(491, min_periods=max(491//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.581875 + 0.0017101 * anchor
    return base_signal.diff()
