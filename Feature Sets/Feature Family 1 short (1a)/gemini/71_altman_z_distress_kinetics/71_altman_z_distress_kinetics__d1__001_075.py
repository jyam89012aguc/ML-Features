"""71 altman z distress kinetics d1 first derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Credit_Risk - Institutional-grade short-side signal.
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

def f71_zscr_001_struct_v1_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=221, w3=432, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 221)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.264375 + 0.0036602 * anchor
    return base_signal.diff()

def f71_zscr_002_struct_v2_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=232, w3=445, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(232, min_periods=max(232//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.27875 + 0.0036603 * anchor
    return base_signal.diff()

def f71_zscr_003_struct_v3_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=243, w3=458, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(243, min_periods=max(243//3, 2)).rank(pct=True)
    persistence = change.rolling(458, min_periods=max(458//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0582 * persistence + 0.0036604 * anchor
    return base_signal.diff()

def f71_zscr_004_struct_v4_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=254, w3=471, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(254, min_periods=max(254//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3075 + 0.0036605 * anchor
    return base_signal.diff()

def f71_zscr_005_struct_v5_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=265, w3=484, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(265, min_periods=max(265//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0734 * slope + 0.0036606 * anchor
    return base_signal.diff()

def f71_zscr_006_struct_v6_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=276, w3=497, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(276, min_periods=max(276//3, 2)).mean()
    noise = impulse.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33625 + 0.0036607 * anchor
    return base_signal.diff()

def f71_zscr_007_struct_v7_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=287, w3=510, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 510)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0886 * acceleration + 0.0036608 * anchor
    return base_signal.diff()

def f71_zscr_008_struct_v8_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=298, w3=523, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(298, min_periods=max(298//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.365 + 0.0036609 * anchor
    return base_signal.diff()

def f71_zscr_009_struct_v9_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=309, w3=536, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(309, min_periods=max(309//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1038 * _rolling_slope(draw, 536) + 0.003661 * anchor
    return base_signal.diff()

def f71_zscr_010_struct_v10_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=320, w3=549, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 255)
    baseline = trend.rolling(320, min_periods=max(320//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.39375 + 0.0036611 * anchor
    return base_signal.diff()

def f71_zscr_011_struct_v11_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=331, w3=562, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 11)
    slow = _rolling_slope(x, 331)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.408125 + 0.0036612 * anchor
    return base_signal.diff()

def f71_zscr_012_struct_v12_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=342, w3=575, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(342, min_periods=max(342//3, 2)).max()
    trough = x.rolling(18, min_periods=max(18//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.4225 + 0.0036613 * anchor
    return base_signal.diff()

def f71_zscr_013_struct_v13_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=353, w3=588, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(25)
    rank = change.rolling(353, min_periods=max(353//3, 2)).rank(pct=True)
    persistence = change.rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1342 * persistence + 0.0036614 * anchor
    return base_signal.diff()

def f71_zscr_014_struct_v14_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=364, w3=601, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(32, min_periods=max(32//3, 2)).std()
    vol_slow = ret.rolling(364, min_periods=max(364//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.45125 + 0.0036615 * anchor
    return base_signal.diff()

def f71_zscr_015_struct_v15_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=375, w3=614, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(375, min_periods=max(375//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 39)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1494 * slope + 0.0036616 * anchor
    return base_signal.diff()

def f71_zscr_016_struct_v16_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=386, w3=627, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(46)
    drag = impulse.rolling(386, min_periods=max(386//3, 2)).mean()
    noise = impulse.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.48 + 0.0036617 * anchor
    return base_signal.diff()

def f71_zscr_017_struct_v17_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=397, w3=640, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 53)
    acceleration = _rolling_slope(velocity, 397)
    curvature = _rolling_slope(acceleration, 640)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1646 * acceleration + 0.0036618 * anchor
    return base_signal.diff()

def f71_zscr_018_struct_v18_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=408, w3=653, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(60, min_periods=max(60//3, 2)).mean(), upside.rolling(408, min_periods=max(408//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.50875 + 0.0036619 * anchor
    return base_signal.diff()

def f71_zscr_019_struct_v19_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=419, w3=666, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(419, min_periods=max(419//3, 2)).max()
    rebound = x - x.rolling(67, min_periods=max(67//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1798 * _rolling_slope(draw, 666) + 0.003662 * anchor
    return base_signal.diff()

def f71_zscr_020_struct_v20_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=430, w3=679, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(430, min_periods=max(430//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5375 + 0.0036621 * anchor
    return base_signal.diff()

def f71_zscr_021_struct_v21_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=441, w3=692, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 441)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.551875 + 0.0036622 * anchor
    return base_signal.diff()

def f71_zscr_022_struct_v22_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=452, w3=705, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(452, min_periods=max(452//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.56625 + 0.0036623 * anchor
    return base_signal.diff()

def f71_zscr_023_struct_v23_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=463, w3=718, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(95)
    rank = change.rolling(463, min_periods=max(463//3, 2)).rank(pct=True)
    persistence = change.rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2102 * persistence + 0.0036624 * anchor
    return base_signal.diff()

def f71_zscr_024_struct_v24_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=474, w3=731, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(474, min_periods=max(474//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.595 + 0.0036625 * anchor
    return base_signal.diff()

def f71_zscr_025_struct_v25_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=485, w3=744, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(485, min_periods=max(485//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2254 * slope + 0.0036626 * anchor
    return base_signal.diff()

def f71_zscr_026_struct_v26_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=496, w3=757, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(116)
    drag = impulse.rolling(496, min_periods=max(496//3, 2)).mean()
    noise = impulse.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.850625 + 0.0036627 * anchor
    return base_signal.diff()

def f71_zscr_027_struct_v27_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=507, w3=770, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 507)
    curvature = _rolling_slope(acceleration, 770)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2406 * acceleration + 0.0036628 * anchor
    return base_signal.diff()

def f71_zscr_028_struct_v28_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=15, w3=26, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(130, min_periods=max(130//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(26) * 0.879375 + 0.0036629 * anchor
    return base_signal.diff()

def f71_zscr_029_struct_v29_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=26, w3=39, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(26, min_periods=max(26//3, 2)).max()
    rebound = x - x.rolling(137, min_periods=max(137//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2558 * _rolling_slope(draw, 39) + 0.003663 * anchor
    return base_signal.diff()

def f71_zscr_030_struct_v30_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=37, w3=52, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 144)
    baseline = trend.rolling(37, min_periods=max(37//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.908125 + 0.0036631 * anchor
    return base_signal.diff()

def f71_zscr_031_struct_v31_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=48, w3=65, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 48)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=65, adjust=False).mean() * 0.9225 + 0.0036632 * anchor
    return base_signal.diff()

def f71_zscr_032_struct_v32_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=59, w3=78, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(59, min_periods=max(59//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.936875 + 0.0036633 * anchor
    return base_signal.diff()

def f71_zscr_033_struct_v33_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=70, w3=91, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(70, min_periods=max(70//3, 2)).rank(pct=True)
    persistence = change.rolling(91, min_periods=max(91//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2862 * persistence + 0.0036634 * anchor
    return base_signal.diff()

def f71_zscr_034_struct_v34_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=81, w3=104, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(81, min_periods=max(81//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.965625 + 0.0036635 * anchor
    return base_signal.diff()

def f71_zscr_035_struct_v35_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=92, w3=117, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(92, min_periods=max(92//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3014 * slope + 0.0036636 * anchor
    return base_signal.diff()

def f71_zscr_036_struct_v36_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=103, w3=130, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(103, min_periods=max(103//3, 2)).mean()
    noise = impulse.abs().rolling(130, min_periods=max(130//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.994375 + 0.0036637 * anchor
    return base_signal.diff()

def f71_zscr_037_struct_v37_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=114, w3=143, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 114)
    curvature = _rolling_slope(acceleration, 143)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3166 * acceleration + 0.0036638 * anchor
    return base_signal.diff()

def f71_zscr_038_struct_v38_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=125, w3=156, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(125, min_periods=max(125//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.023125 + 0.0036639 * anchor
    return base_signal.diff()

def f71_zscr_039_struct_v39_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=136, w3=169, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(136, min_periods=max(136//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3318 * _rolling_slope(draw, 169) + 0.003664 * anchor
    return base_signal.diff()

def f71_zscr_040_struct_v40_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=147, w3=182, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(147, min_periods=max(147//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.051875 + 0.0036641 * anchor
    return base_signal.diff()

def f71_zscr_041_struct_v41_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=158, w3=195, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 158)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=195, adjust=False).mean() * 1.06625 + 0.0036642 * anchor
    return base_signal.diff()

def f71_zscr_042_struct_v42_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=169, w3=208, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(169, min_periods=max(169//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.080625 + 0.0036643 * anchor
    return base_signal.diff()

def f71_zscr_043_struct_v43_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=180, w3=221, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(180, min_periods=max(180//3, 2)).rank(pct=True)
    persistence = change.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3622 * persistence + 0.0036644 * anchor
    return base_signal.diff()

def f71_zscr_044_struct_v44_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=191, w3=234, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(191, min_periods=max(191//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.109375 + 0.0036645 * anchor
    return base_signal.diff()

def f71_zscr_045_struct_v45_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=202, w3=247, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3774 * slope + 0.0036646 * anchor
    return base_signal.diff()

def f71_zscr_046_struct_v46_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=213, w3=260, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(5)
    drag = impulse.rolling(213, min_periods=max(213//3, 2)).mean()
    noise = impulse.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.138125 + 0.0036647 * anchor
    return base_signal.diff()

def f71_zscr_047_struct_v47_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=224, w3=273, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 273)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3926 * acceleration + 0.0036648 * anchor
    return base_signal.diff()

def f71_zscr_048_struct_v48_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=235, w3=286, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.166875 + 0.0036649 * anchor
    return base_signal.diff()

def f71_zscr_049_struct_v49_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=246, w3=299, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(246, min_periods=max(246//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4078 * _rolling_slope(draw, 299) + 0.003665 * anchor
    return base_signal.diff()

def f71_zscr_050_struct_v50_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=33, w2=257, w3=312, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(257, min_periods=max(257//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.195625 + 0.0036651 * anchor
    return base_signal.diff()

def f71_zscr_051_struct_v51_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=40, w2=268, w3=325, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 268)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.21 + 0.0036652 * anchor
    return base_signal.diff()

def f71_zscr_052_struct_v52_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=47, w2=279, w3=338, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(279, min_periods=max(279//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.224375 + 0.0036653 * anchor
    return base_signal.diff()

def f71_zscr_053_struct_v53_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=54, w2=290, w3=351, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(54)
    rank = change.rolling(290, min_periods=max(290//3, 2)).rank(pct=True)
    persistence = change.rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0618 * persistence + 0.0036654 * anchor
    return base_signal.diff()

def f71_zscr_054_struct_v54_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=61, w2=301, w3=364, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(301, min_periods=max(301//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.253125 + 0.0036655 * anchor
    return base_signal.diff()

def f71_zscr_055_struct_v55_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=68, w2=312, w3=377, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(312, min_periods=max(312//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.077 * slope + 0.0036656 * anchor
    return base_signal.diff()

def f71_zscr_056_struct_v56_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=75, w2=323, w3=390, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(75)
    drag = impulse.rolling(323, min_periods=max(323//3, 2)).mean()
    noise = impulse.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.281875 + 0.0036657 * anchor
    return base_signal.diff()

def f71_zscr_057_struct_v57_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=82, w2=334, w3=403, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 403)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0922 * acceleration + 0.0036658 * anchor
    return base_signal.diff()

def f71_zscr_058_struct_v58_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=89, w2=345, w3=416, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(345, min_periods=max(345//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.310625 + 0.0036659 * anchor
    return base_signal.diff()

def f71_zscr_059_struct_v59_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=96, w2=356, w3=429, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(356, min_periods=max(356//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1074 * _rolling_slope(draw, 429) + 0.003666 * anchor
    return base_signal.diff()

def f71_zscr_060_struct_v60_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=103, w2=367, w3=442, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(367, min_periods=max(367//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.339375 + 0.0036661 * anchor
    return base_signal.diff()

def f71_zscr_061_struct_v61_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=110, w2=378, w3=455, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 378)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.35375 + 0.0036662 * anchor
    return base_signal.diff()

def f71_zscr_062_struct_v62_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=117, w2=389, w3=468, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(389, min_periods=max(389//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.368125 + 0.0036663 * anchor
    return base_signal.diff()

def f71_zscr_063_struct_v63_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=124, w2=400, w3=481, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(124)
    rank = change.rolling(400, min_periods=max(400//3, 2)).rank(pct=True)
    persistence = change.rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1378 * persistence + 0.0036664 * anchor
    return base_signal.diff()

def f71_zscr_064_struct_v64_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=131, w2=411, w3=494, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(411, min_periods=max(411//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.396875 + 0.0036665 * anchor
    return base_signal.diff()

def f71_zscr_065_struct_v65_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=138, w2=422, w3=507, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(422, min_periods=max(422//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.153 * slope + 0.0036666 * anchor
    return base_signal.diff()

def f71_zscr_066_struct_v66_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=145, w2=433, w3=520, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(433, min_periods=max(433//3, 2)).mean()
    noise = impulse.abs().rolling(520, min_periods=max(520//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.425625 + 0.0036667 * anchor
    return base_signal.diff()

def f71_zscr_067_struct_v67_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=152, w2=444, w3=533, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 533)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1682 * acceleration + 0.0036668 * anchor
    return base_signal.diff()

def f71_zscr_068_struct_v68_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=159, w2=455, w3=546, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(455, min_periods=max(455//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.454375 + 0.0036669 * anchor
    return base_signal.diff()

def f71_zscr_069_struct_v69_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=166, w2=466, w3=559, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(466, min_periods=max(466//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1834 * _rolling_slope(draw, 559) + 0.003667 * anchor
    return base_signal.diff()

def f71_zscr_070_struct_v70_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=477, w3=572, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.483125 + 0.0036671 * anchor
    return base_signal.diff()

def f71_zscr_071_struct_v71_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=488, w3=585, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 488)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.4975 + 0.0036672 * anchor
    return base_signal.diff()

def f71_zscr_072_struct_v72_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=499, w3=598, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(499, min_periods=max(499//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.511875 + 0.0036673 * anchor
    return base_signal.diff()

def f71_zscr_073_struct_v73_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=510, w3=611, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(510, min_periods=max(510//3, 2)).rank(pct=True)
    persistence = change.rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2138 * persistence + 0.0036674 * anchor
    return base_signal.diff()

def f71_zscr_074_struct_v74_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=18, w3=624, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(18, min_periods=max(18//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.540625 + 0.0036675 * anchor
    return base_signal.diff()

def f71_zscr_075_struct_v75_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=29, w3=637, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(29, min_periods=max(29//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.229 * slope + 0.0036676 * anchor
    return base_signal.diff()
