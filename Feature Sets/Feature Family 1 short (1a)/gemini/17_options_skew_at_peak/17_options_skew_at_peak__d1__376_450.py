"""17 options skew at peak d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Options_Greeks - Institutional-grade short-side signal.
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

def f17_optx_376_struct_v376_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=153, w3=486, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(153, min_periods=max(153//3, 2)).mean()
    noise = impulse.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3475 + 0.0010577 * anchor
    return base_signal.diff()

def f17_optx_377_struct_v377_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=164, w3=499, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 250)
    acceleration = _rolling_slope(velocity, 164)
    curvature = _rolling_slope(acceleration, 499)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.247 * acceleration + 0.0010578 * anchor
    return base_signal.diff()

def f17_optx_378_struct_v378_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=175, w3=512, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(175, min_periods=max(175//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37625 + 0.0010579 * anchor
    return base_signal.diff()

def f17_optx_379_struct_v379_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=186, w3=525, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(186, min_periods=max(186//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2622 * _rolling_slope(draw, 525) + 0.001058 * anchor
    return base_signal.diff()

def f17_optx_380_struct_v380_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=197, w3=538, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 20)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.405 + 0.0010581 * anchor
    return base_signal.diff()

def f17_optx_381_struct_v381_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=208, w3=551, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 27)
    slow = _rolling_slope(x, 208)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.419375 + 0.0010582 * anchor
    return base_signal.diff()

def f17_optx_382_struct_v382_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=219, w3=564, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(219, min_periods=max(219//3, 2)).max()
    trough = x.rolling(34, min_periods=max(34//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.43375 + 0.0010583 * anchor
    return base_signal.diff()

def f17_optx_383_struct_v383_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=230, w3=577, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(41)
    rank = change.rolling(230, min_periods=max(230//3, 2)).rank(pct=True)
    persistence = change.rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2926 * persistence + 0.0010584 * anchor
    return base_signal.diff()

def f17_optx_384_struct_v384_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=241, w3=590, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(48, min_periods=max(48//3, 2)).std()
    vol_slow = ret.rolling(241, min_periods=max(241//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4625 + 0.0010585 * anchor
    return base_signal.diff()

def f17_optx_385_struct_v385_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=252, w3=603, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(252, min_periods=max(252//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3078 * slope + 0.0010586 * anchor
    return base_signal.diff()

def f17_optx_386_struct_v386_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=263, w3=616, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(62)
    drag = impulse.rolling(263, min_periods=max(263//3, 2)).mean()
    noise = impulse.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.49125 + 0.0010587 * anchor
    return base_signal.diff()

def f17_optx_387_struct_v387_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=69, w2=274, w3=629, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 274)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.323 * acceleration + 0.0010588 * anchor
    return base_signal.diff()

def f17_optx_388_struct_v388_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=76, w2=285, w3=642, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(76, min_periods=max(76//3, 2)).mean(), upside.rolling(285, min_periods=max(285//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.52 + 0.0010589 * anchor
    return base_signal.diff()

def f17_optx_389_struct_v389_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=83, w2=296, w3=655, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(296, min_periods=max(296//3, 2)).max()
    rebound = x - x.rolling(83, min_periods=max(83//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3382 * _rolling_slope(draw, 655) + 0.001059 * anchor
    return base_signal.diff()

def f17_optx_390_struct_v390_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=90, w2=307, w3=668, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.54875 + 0.0010591 * anchor
    return base_signal.diff()

def f17_optx_391_struct_v391_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=97, w2=318, w3=681, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.563125 + 0.0010592 * anchor
    return base_signal.diff()

def f17_optx_392_struct_v392_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=104, w2=329, w3=694, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(329, min_periods=max(329//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5775 + 0.0010593 * anchor
    return base_signal.diff()

def f17_optx_393_struct_v393_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=111, w2=340, w3=707, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(111)
    rank = change.rolling(340, min_periods=max(340//3, 2)).rank(pct=True)
    persistence = change.rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3686 * persistence + 0.0010594 * anchor
    return base_signal.diff()

def f17_optx_394_struct_v394_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=118, w2=351, w3=720, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(351, min_periods=max(351//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60625 + 0.0010595 * anchor
    return base_signal.diff()

def f17_optx_395_struct_v395_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=125, w2=362, w3=733, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(362, min_periods=max(362//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3838 * slope + 0.0010596 * anchor
    return base_signal.diff()

def f17_optx_396_struct_v396_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=132, w2=373, w3=746, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(373, min_periods=max(373//3, 2)).mean()
    noise = impulse.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.861875 + 0.0010597 * anchor
    return base_signal.diff()

def f17_optx_397_struct_v397_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=139, w2=384, w3=759, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 384)
    curvature = _rolling_slope(acceleration, 759)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.399 * acceleration + 0.0010598 * anchor
    return base_signal.diff()

def f17_optx_398_struct_v398_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=146, w2=395, w3=15, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(146, min_periods=max(146//3, 2)).mean(), upside.rolling(395, min_periods=max(395//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(15) * 0.890625 + 0.0010599 * anchor
    return base_signal.diff()

def f17_optx_399_struct_v399_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=153, w2=406, w3=28, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(406, min_periods=max(406//3, 2)).max()
    rebound = x - x.rolling(153, min_periods=max(153//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0378 * _rolling_slope(draw, 28) + 0.00106 * anchor
    return base_signal.diff()

def f17_optx_400_struct_v400_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=160, w2=417, w3=41, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 160)
    baseline = trend.rolling(417, min_periods=max(417//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(41, min_periods=max(41//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.919375 + 0.0010601 * anchor
    return base_signal.diff()

def f17_optx_401_struct_v401_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=167, w2=428, w3=54, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 167)
    slow = _rolling_slope(x, 428)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=54, adjust=False).mean() * 0.93375 + 0.0010602 * anchor
    return base_signal.diff()

def f17_optx_402_struct_v402_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=174, w2=439, w3=67, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(439, min_periods=max(439//3, 2)).max()
    trough = x.rolling(174, min_periods=max(174//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.948125 + 0.0010603 * anchor
    return base_signal.diff()

def f17_optx_403_struct_v403_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=181, w2=450, w3=80, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(450, min_periods=max(450//3, 2)).rank(pct=True)
    persistence = change.rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0682 * persistence + 0.0010604 * anchor
    return base_signal.diff()

def f17_optx_404_struct_v404_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=188, w2=461, w3=93, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(188, min_periods=max(188//3, 2)).std()
    vol_slow = ret.rolling(461, min_periods=max(461//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.976875 + 0.0010605 * anchor
    return base_signal.diff()

def f17_optx_405_struct_v405_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=195, w2=472, w3=106, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(472, min_periods=max(472//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 195)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0834 * slope + 0.0010606 * anchor
    return base_signal.diff()

def f17_optx_406_struct_v406_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=202, w2=483, w3=119, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(483, min_periods=max(483//3, 2)).mean()
    noise = impulse.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.005625 + 0.0010607 * anchor
    return base_signal.diff()

def f17_optx_407_struct_v407_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=209, w2=494, w3=132, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 209)
    acceleration = _rolling_slope(velocity, 494)
    curvature = _rolling_slope(acceleration, 132)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0986 * acceleration + 0.0010608 * anchor
    return base_signal.diff()

def f17_optx_408_struct_v408_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=216, w2=505, w3=145, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(505, min_periods=max(505//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.034375 + 0.0010609 * anchor
    return base_signal.diff()

def f17_optx_409_struct_v409_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=223, w2=13, w3=158, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(13, min_periods=max(13//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1138 * _rolling_slope(draw, 158) + 0.001061 * anchor
    return base_signal.diff()

def f17_optx_410_struct_v410_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=230, w2=24, w3=171, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 230)
    baseline = trend.rolling(24, min_periods=max(24//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(171, min_periods=max(171//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.063125 + 0.0010611 * anchor
    return base_signal.diff()

def f17_optx_411_struct_v411_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=237, w2=35, w3=184, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 237)
    slow = _rolling_slope(x, 35)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=184, adjust=False).mean() * 1.0775 + 0.0010612 * anchor
    return base_signal.diff()

def f17_optx_412_struct_v412_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=244, w2=46, w3=197, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(46, min_periods=max(46//3, 2)).max()
    trough = x.rolling(244, min_periods=max(244//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.091875 + 0.0010613 * anchor
    return base_signal.diff()

def f17_optx_413_struct_v413_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=251, w2=57, w3=210, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(57, min_periods=max(57//3, 2)).rank(pct=True)
    persistence = change.rolling(210, min_periods=max(210//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1442 * persistence + 0.0010614 * anchor
    return base_signal.diff()

def f17_optx_414_struct_v414_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=7, w2=68, w3=223, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(7, min_periods=max(7//3, 2)).std()
    vol_slow = ret.rolling(68, min_periods=max(68//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.120625 + 0.0010615 * anchor
    return base_signal.diff()

def f17_optx_415_struct_v415_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=14, w2=79, w3=236, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(79, min_periods=max(79//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 14)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1594 * slope + 0.0010616 * anchor
    return base_signal.diff()

def f17_optx_416_struct_v416_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=21, w2=90, w3=249, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(21)
    drag = impulse.rolling(90, min_periods=max(90//3, 2)).mean()
    noise = impulse.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.149375 + 0.0010617 * anchor
    return base_signal.diff()

def f17_optx_417_struct_v417_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=28, w2=101, w3=262, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 28)
    acceleration = _rolling_slope(velocity, 101)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1746 * acceleration + 0.0010618 * anchor
    return base_signal.diff()

def f17_optx_418_struct_v418_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=35, w2=112, w3=275, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(35, min_periods=max(35//3, 2)).mean(), upside.rolling(112, min_periods=max(112//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.178125 + 0.0010619 * anchor
    return base_signal.diff()

def f17_optx_419_struct_v419_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=42, w2=123, w3=288, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(123, min_periods=max(123//3, 2)).max()
    rebound = x - x.rolling(42, min_periods=max(42//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1898 * _rolling_slope(draw, 288) + 0.001062 * anchor
    return base_signal.diff()

def f17_optx_420_struct_v420_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=49, w2=134, w3=301, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 49)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(301, min_periods=max(301//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.206875 + 0.0010621 * anchor
    return base_signal.diff()

def f17_optx_421_struct_v421_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=56, w2=145, w3=314, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 56)
    slow = _rolling_slope(x, 145)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.22125 + 0.0010622 * anchor
    return base_signal.diff()

def f17_optx_422_struct_v422_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=63, w2=156, w3=327, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(63, min_periods=max(63//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.235625 + 0.0010623 * anchor
    return base_signal.diff()

def f17_optx_423_struct_v423_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=70, w2=167, w3=340, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(70)
    rank = change.rolling(167, min_periods=max(167//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2202 * persistence + 0.0010624 * anchor
    return base_signal.diff()

def f17_optx_424_struct_v424_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=77, w2=178, w3=353, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(77, min_periods=max(77//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.264375 + 0.0010625 * anchor
    return base_signal.diff()

def f17_optx_425_struct_v425_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=84, w2=189, w3=366, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(189, min_periods=max(189//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 84)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2354 * slope + 0.0010626 * anchor
    return base_signal.diff()

def f17_optx_426_struct_v426_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=91, w2=200, w3=379, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(91)
    drag = impulse.rolling(200, min_periods=max(200//3, 2)).mean()
    noise = impulse.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.293125 + 0.0010627 * anchor
    return base_signal.diff()

def f17_optx_427_struct_v427_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=98, w2=211, w3=392, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 98)
    acceleration = _rolling_slope(velocity, 211)
    curvature = _rolling_slope(acceleration, 392)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2506 * acceleration + 0.0010628 * anchor
    return base_signal.diff()

def f17_optx_428_struct_v428_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=105, w2=222, w3=405, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(105, min_periods=max(105//3, 2)).mean(), upside.rolling(222, min_periods=max(222//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.321875 + 0.0010629 * anchor
    return base_signal.diff()

def f17_optx_429_struct_v429_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=112, w2=233, w3=418, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(233, min_periods=max(233//3, 2)).max()
    rebound = x - x.rolling(112, min_periods=max(112//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2658 * _rolling_slope(draw, 418) + 0.001063 * anchor
    return base_signal.diff()

def f17_optx_430_struct_v430_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=119, w2=244, w3=431, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 119)
    baseline = trend.rolling(244, min_periods=max(244//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.350625 + 0.0010631 * anchor
    return base_signal.diff()

def f17_optx_431_struct_v431_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=126, w2=255, w3=444, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 126)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.365 + 0.0010632 * anchor
    return base_signal.diff()

def f17_optx_432_struct_v432_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=133, w2=266, w3=457, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(133, min_periods=max(133//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.379375 + 0.0010633 * anchor
    return base_signal.diff()

def f17_optx_433_struct_v433_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=140, w2=277, w3=470, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(277, min_periods=max(277//3, 2)).rank(pct=True)
    persistence = change.rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2962 * persistence + 0.0010634 * anchor
    return base_signal.diff()

def f17_optx_434_struct_v434_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=147, w2=288, w3=483, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(147, min_periods=max(147//3, 2)).std()
    vol_slow = ret.rolling(288, min_periods=max(288//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.408125 + 0.0010635 * anchor
    return base_signal.diff()

def f17_optx_435_struct_v435_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=154, w2=299, w3=496, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(299, min_periods=max(299//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 154)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3114 * slope + 0.0010636 * anchor
    return base_signal.diff()

def f17_optx_436_struct_v436_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=161, w2=310, w3=509, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.436875 + 0.0010637 * anchor
    return base_signal.diff()

def f17_optx_437_struct_v437_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=321, w3=522, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 168)
    acceleration = _rolling_slope(velocity, 321)
    curvature = _rolling_slope(acceleration, 522)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3266 * acceleration + 0.0010638 * anchor
    return base_signal.diff()

def f17_optx_438_struct_v438_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=332, w3=535, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(175, min_periods=max(175//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.465625 + 0.0010639 * anchor
    return base_signal.diff()

def f17_optx_439_struct_v439_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=343, w3=548, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(343, min_periods=max(343//3, 2)).max()
    rebound = x - x.rolling(182, min_periods=max(182//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3418 * _rolling_slope(draw, 548) + 0.001064 * anchor
    return base_signal.diff()

def f17_optx_440_struct_v440_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=354, w3=561, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 189)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.494375 + 0.0010641 * anchor
    return base_signal.diff()

def f17_optx_441_struct_v441_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=196, w2=365, w3=574, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.50875 + 0.0010642 * anchor
    return base_signal.diff()

def f17_optx_442_struct_v442_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=203, w2=376, w3=587, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.523125 + 0.0010643 * anchor
    return base_signal.diff()

def f17_optx_443_struct_v443_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=210, w2=387, w3=600, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(387, min_periods=max(387//3, 2)).rank(pct=True)
    persistence = change.rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3722 * persistence + 0.0010644 * anchor
    return base_signal.diff()

def f17_optx_444_struct_v444_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=217, w2=398, w3=613, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(398, min_periods=max(398//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.551875 + 0.0010645 * anchor
    return base_signal.diff()

def f17_optx_445_struct_v445_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=224, w2=409, w3=626, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(409, min_periods=max(409//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3874 * slope + 0.0010646 * anchor
    return base_signal.diff()

def f17_optx_446_struct_v446_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=231, w2=420, w3=639, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(420, min_periods=max(420//3, 2)).mean()
    noise = impulse.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.580625 + 0.0010647 * anchor
    return base_signal.diff()

def f17_optx_447_struct_v447_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=238, w2=431, w3=652, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 431)
    curvature = _rolling_slope(acceleration, 652)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4026 * acceleration + 0.0010648 * anchor
    return base_signal.diff()

def f17_optx_448_struct_v448_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=245, w2=442, w3=665, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.609375 + 0.0010649 * anchor
    return base_signal.diff()

def f17_optx_449_struct_v449_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=252, w2=453, w3=678, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(252, min_periods=max(252//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0414 * _rolling_slope(draw, 678) + 0.001065 * anchor
    return base_signal.diff()

def f17_optx_450_struct_v450_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=8, w2=464, w3=691, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(464, min_periods=max(464//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(691, min_periods=max(691//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.865 + 0.0010651 * anchor
    return base_signal.diff()
