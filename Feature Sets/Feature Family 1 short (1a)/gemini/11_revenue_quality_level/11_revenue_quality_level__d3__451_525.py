"""11 revenue quality level d3 third derivative features 451-525 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Fundamental_Quality - Institutional-grade short-side signal.
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

def f11_revq_451_struct_v451_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=166, w2=109, w3=81, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 109)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=81, adjust=False).mean() * 0.92875 + 0.0007052 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_452_struct_v452_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=173, w2=120, w3=94, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(120, min_periods=max(120//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.943125 + 0.0007053 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_453_struct_v453_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=180, w2=131, w3=107, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(131, min_periods=max(131//3, 2)).rank(pct=True)
    persistence = change.rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189 * persistence + 0.0007054 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_454_struct_v454_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=187, w2=142, w3=120, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(142, min_periods=max(142//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.971875 + 0.0007055 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_455_struct_v455_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=194, w2=153, w3=133, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(153, min_periods=max(153//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2042 * slope + 0.0007056 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_456_struct_v456_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=201, w2=164, w3=146, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(164, min_periods=max(164//3, 2)).mean()
    noise = impulse.abs().rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.000625 + 0.0007057 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_457_struct_v457_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=208, w2=175, w3=159, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 175)
    curvature = _rolling_slope(acceleration, 159)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2194 * acceleration + 0.0007058 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_458_struct_v458_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=215, w2=186, w3=172, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(186, min_periods=max(186//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.029375 + 0.0007059 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_459_struct_v459_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=222, w2=197, w3=185, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(197, min_periods=max(197//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2346 * _rolling_slope(draw, 185) + 0.000706 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_460_struct_v460_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=229, w2=208, w3=198, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(208, min_periods=max(208//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.058125 + 0.0007061 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_461_struct_v461_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=236, w2=219, w3=211, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 219)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=211, adjust=False).mean() * 1.0725 + 0.0007062 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_462_struct_v462_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=243, w2=230, w3=224, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(230, min_periods=max(230//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.086875 + 0.0007063 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_463_struct_v463_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=250, w2=241, w3=237, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(241, min_periods=max(241//3, 2)).rank(pct=True)
    persistence = change.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265 * persistence + 0.0007064 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_464_struct_v464_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=6, w2=252, w3=250, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(252, min_periods=max(252//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.115625 + 0.0007065 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_465_struct_v465_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=13, w2=263, w3=263, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(263, min_periods=max(263//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2802 * slope + 0.0007066 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_466_struct_v466_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=20, w2=274, w3=276, lag=2)."""
    x = gex.shift(2)
    impulse = x.diff(20)
    drag = impulse.rolling(274, min_periods=max(274//3, 2)).mean()
    noise = impulse.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.144375 + 0.0007067 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_467_struct_v467_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=27, w2=285, w3=289, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 285)
    curvature = _rolling_slope(acceleration, 289)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2954 * acceleration + 0.0007068 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_468_struct_v468_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=34, w2=296, w3=302, lag=10)."""
    x = revenue.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(296, min_periods=max(296//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.173125 + 0.0007069 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_469_struct_v469_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=41, w2=307, w3=315, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    draw = x - x.rolling(307, min_periods=max(307//3, 2)).max()
    rebound = x - x.rolling(41, min_periods=max(41//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3106 * _rolling_slope(draw, 315) + 0.000707 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_470_struct_v470_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=48, w2=318, w3=328, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 48)
    baseline = trend.rolling(318, min_periods=max(318//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.201875 + 0.0007071 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_471_struct_v471_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=55, w2=329, w3=341, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 55)
    slow = _rolling_slope(x, 329)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.21625 + 0.0007072 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_472_struct_v472_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=62, w2=340, w3=354, lag=0)."""
    x = gex.shift(0)
    peak = x.rolling(340, min_periods=max(340//3, 2)).max()
    trough = x.rolling(62, min_periods=max(62//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.230625 + 0.0007073 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_473_struct_v473_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=69, w2=351, w3=367, lag=1)."""
    x = vex.shift(1)
    change = x.pct_change(69)
    rank = change.rolling(351, min_periods=max(351//3, 2)).rank(pct=True)
    persistence = change.rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341 * persistence + 0.0007074 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_474_struct_v474_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=76, w2=362, w3=380, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(76, min_periods=max(76//3, 2)).std()
    vol_slow = ret.rolling(362, min_periods=max(362//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.259375 + 0.0007075 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_475_struct_v475_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=83, w2=373, w3=393, lag=5)."""
    x = netinc.shift(5)
    ma = x.rolling(373, min_periods=max(373//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 83)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3562 * slope + 0.0007076 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_476_struct_v476_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=90, w2=384, w3=406, lag=10)."""
    x = shortinterest.shift(10)
    impulse = x.diff(90)
    drag = impulse.rolling(384, min_periods=max(384//3, 2)).mean()
    noise = impulse.abs().rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.288125 + 0.0007077 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_477_struct_v477_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=97, w2=395, w3=419, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 97)
    acceleration = _rolling_slope(velocity, 395)
    curvature = _rolling_slope(acceleration, 419)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3714 * acceleration + 0.0007078 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_478_struct_v478_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=104, w2=406, w3=432, lag=42)."""
    x = gex.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(104, min_periods=max(104//3, 2)).mean(), upside.rolling(406, min_periods=max(406//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.316875 + 0.0007079 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_479_struct_v479_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=111, w2=417, w3=445, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    draw = x - x.rolling(417, min_periods=max(417//3, 2)).max()
    rebound = x - x.rolling(111, min_periods=max(111//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3866 * _rolling_slope(draw, 445) + 0.000708 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_480_struct_v480_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=118, w2=428, w3=458, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(428, min_periods=max(428//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.345625 + 0.0007081 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_481_struct_v481_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=125, w2=439, w3=471, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 125)
    slow = _rolling_slope(x, 439)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.36 + 0.0007082 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_482_struct_v482_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=132, w2=450, w3=484, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(450, min_periods=max(450//3, 2)).max()
    trough = x.rolling(132, min_periods=max(132//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.374375 + 0.0007083 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_483_struct_v483_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=139, w2=461, w3=497, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(461, min_periods=max(461//3, 2)).rank(pct=True)
    persistence = change.rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0406 * persistence + 0.0007084 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_484_struct_v484_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=146, w2=472, w3=510, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(146, min_periods=max(146//3, 2)).std()
    vol_slow = ret.rolling(472, min_periods=max(472//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.403125 + 0.0007085 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_485_struct_v485_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=153, w2=483, w3=523, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(483, min_periods=max(483//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 153)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0558 * slope + 0.0007086 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_486_struct_v486_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=160, w2=494, w3=536, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(494, min_periods=max(494//3, 2)).mean()
    noise = impulse.abs().rolling(536, min_periods=max(536//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.431875 + 0.0007087 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_487_struct_v487_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=167, w2=505, w3=549, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 167)
    acceleration = _rolling_slope(velocity, 505)
    curvature = _rolling_slope(acceleration, 549)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.071 * acceleration + 0.0007088 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_488_struct_v488_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=174, w2=13, w3=562, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(174, min_periods=max(174//3, 2)).mean(), upside.rolling(13, min_periods=max(13//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.460625 + 0.0007089 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_489_struct_v489_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=181, w2=24, w3=575, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(24, min_periods=max(24//3, 2)).max()
    rebound = x - x.rolling(181, min_periods=max(181//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0862 * _rolling_slope(draw, 575) + 0.000709 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_490_struct_v490_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=188, w2=35, w3=588, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 188)
    baseline = trend.rolling(35, min_periods=max(35//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.489375 + 0.0007091 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_491_struct_v491_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=195, w2=46, w3=601, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 195)
    slow = _rolling_slope(x, 46)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.50375 + 0.0007092 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_492_struct_v492_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=202, w2=57, w3=614, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(57, min_periods=max(57//3, 2)).max()
    trough = x.rolling(202, min_periods=max(202//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.518125 + 0.0007093 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_493_struct_v493_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=209, w2=68, w3=627, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(68, min_periods=max(68//3, 2)).rank(pct=True)
    persistence = change.rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1166 * persistence + 0.0007094 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_494_struct_v494_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=216, w2=79, w3=640, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(216, min_periods=max(216//3, 2)).std()
    vol_slow = ret.rolling(79, min_periods=max(79//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.546875 + 0.0007095 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_495_struct_v495_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=223, w2=90, w3=653, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(90, min_periods=max(90//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 223)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1318 * slope + 0.0007096 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_496_struct_v496_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=230, w2=101, w3=666, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(101, min_periods=max(101//3, 2)).mean()
    noise = impulse.abs().rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.575625 + 0.0007097 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_497_struct_v497_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=237, w2=112, w3=679, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 237)
    acceleration = _rolling_slope(velocity, 112)
    curvature = _rolling_slope(acceleration, 679)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.147 * acceleration + 0.0007098 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_498_struct_v498_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=244, w2=123, w3=692, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(123, min_periods=max(123//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.604375 + 0.0007099 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_499_struct_v499_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=251, w2=134, w3=705, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(134, min_periods=max(134//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1622 * _rolling_slope(draw, 705) + 0.00071 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_500_struct_v500_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=7, w2=145, w3=718, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(145, min_periods=max(145//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.86 + 0.0007101 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_501_struct_v501_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=14, w2=156, w3=731, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 156)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.874375 + 0.0007102 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_502_struct_v502_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=21, w2=167, w3=744, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(167, min_periods=max(167//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.88875 + 0.0007103 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_503_struct_v503_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=28, w2=178, w3=757, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(28)
    rank = change.rolling(178, min_periods=max(178//3, 2)).rank(pct=True)
    persistence = change.rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1926 * persistence + 0.0007104 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_504_struct_v504_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=35, w2=189, w3=770, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(189, min_periods=max(189//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9175 + 0.0007105 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_505_struct_v505_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=42, w2=200, w3=26, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(200, min_periods=max(200//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 42)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2078 * slope + 0.0007106 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_506_struct_v506_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=49, w2=211, w3=39, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(49)
    drag = impulse.rolling(211, min_periods=max(211//3, 2)).mean()
    noise = impulse.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94625 + 0.0007107 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_507_struct_v507_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=56, w2=222, w3=52, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 56)
    acceleration = _rolling_slope(velocity, 222)
    curvature = _rolling_slope(acceleration, 52)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.223 * acceleration + 0.0007108 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_508_struct_v508_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=63, w2=233, w3=65, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(233, min_periods=max(233//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(65) * 0.975 + 0.0007109 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_509_struct_v509_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=70, w2=244, w3=78, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(244, min_periods=max(244//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2382 * _rolling_slope(draw, 78) + 0.000711 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_510_struct_v510_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=77, w2=255, w3=91, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(255, min_periods=max(255//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.00375 + 0.0007111 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_511_struct_v511_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=84, w2=266, w3=104, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 266)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=104, adjust=False).mean() * 1.018125 + 0.0007112 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_512_struct_v512_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=91, w2=277, w3=117, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(277, min_periods=max(277//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0325 + 0.0007113 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_513_struct_v513_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=98, w2=288, w3=130, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(98)
    rank = change.rolling(288, min_periods=max(288//3, 2)).rank(pct=True)
    persistence = change.rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2686 * persistence + 0.0007114 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_514_struct_v514_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=105, w2=299, w3=143, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(299, min_periods=max(299//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06125 + 0.0007115 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_515_struct_v515_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=112, w2=310, w3=156, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(310, min_periods=max(310//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2838 * slope + 0.0007116 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_516_struct_v516_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=119, w2=321, w3=169, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(119)
    drag = impulse.rolling(321, min_periods=max(321//3, 2)).mean()
    noise = impulse.abs().rolling(169, min_periods=max(169//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.09 + 0.0007117 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_517_struct_v517_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=126, w2=332, w3=182, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 332)
    curvature = _rolling_slope(acceleration, 182)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299 * acceleration + 0.0007118 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_518_struct_v518_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=133, w2=343, w3=195, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(343, min_periods=max(343//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.11875 + 0.0007119 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_519_struct_v519_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=140, w2=354, w3=208, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(354, min_periods=max(354//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3142 * _rolling_slope(draw, 208) + 0.000712 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_520_struct_v520_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=147, w2=365, w3=221, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1475 + 0.0007121 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_521_struct_v521_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=154, w2=376, w3=234, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 376)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=234, adjust=False).mean() * 1.161875 + 0.0007122 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_522_struct_v522_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=161, w2=387, w3=247, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(387, min_periods=max(387//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17625 + 0.0007123 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_523_struct_v523_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=168, w2=398, w3=260, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3446 * persistence + 0.0007124 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_524_struct_v524_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=175, w2=409, w3=273, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.205 + 0.0007125 * anchor
    return base_signal.diff().diff().diff()

def f11_revq_525_struct_v525_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=182, w2=420, w3=286, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(420, min_periods=max(420//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3598 * slope + 0.0007126 * anchor
    return base_signal.diff().diff().diff()
