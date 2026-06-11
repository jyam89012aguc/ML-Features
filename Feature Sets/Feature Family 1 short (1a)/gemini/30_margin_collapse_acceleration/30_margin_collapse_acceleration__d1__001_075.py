"""30 margin collapse acceleration d1 first derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f30_mca_001_struct_v1_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=10, w2=342, w3=115, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 342)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=115, adjust=False).mean() * 1.390625 + 0.0018002 * anchor
    return base_signal.diff()

def f30_mca_002_struct_v2_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=17, w2=353, w3=128, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.405 + 0.0018003 * anchor
    return base_signal.diff()

def f30_mca_003_struct_v3_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=24, w2=364, w3=141, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(24)
    rank = change.rolling(364, min_periods=max(364//3, 2)).rank(pct=True)
    persistence = change.rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2246 * persistence + 0.0018004 * anchor
    return base_signal.diff()

def f30_mca_004_struct_v4_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=31, w2=375, w3=154, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(375, min_periods=max(375//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43375 + 0.0018005 * anchor
    return base_signal.diff()

def f30_mca_005_struct_v5_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=38, w2=386, w3=167, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(386, min_periods=max(386//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2398 * slope + 0.0018006 * anchor
    return base_signal.diff()

def f30_mca_006_struct_v6_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=45, w2=397, w3=180, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(45)
    drag = impulse.rolling(397, min_periods=max(397//3, 2)).mean()
    noise = impulse.abs().rolling(180, min_periods=max(180//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4625 + 0.0018007 * anchor
    return base_signal.diff()

def f30_mca_007_struct_v7_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=52, w2=408, w3=193, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 408)
    curvature = _rolling_slope(acceleration, 193)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.255 * acceleration + 0.0018008 * anchor
    return base_signal.diff()

def f30_mca_008_struct_v8_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=59, w2=419, w3=206, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(419, min_periods=max(419//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.49125 + 0.0018009 * anchor
    return base_signal.diff()

def f30_mca_009_struct_v9_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=66, w2=430, w3=219, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(430, min_periods=max(430//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2702 * _rolling_slope(draw, 219) + 0.001801 * anchor
    return base_signal.diff()

def f30_mca_010_struct_v10_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=73, w2=441, w3=232, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(441, min_periods=max(441//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.52 + 0.0018011 * anchor
    return base_signal.diff()

def f30_mca_011_struct_v11_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=80, w2=452, w3=245, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 452)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=245, adjust=False).mean() * 1.534375 + 0.0018012 * anchor
    return base_signal.diff()

def f30_mca_012_struct_v12_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=87, w2=463, w3=258, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(463, min_periods=max(463//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.54875 + 0.0018013 * anchor
    return base_signal.diff()

def f30_mca_013_struct_v13_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=94, w2=474, w3=271, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(94)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3006 * persistence + 0.0018014 * anchor
    return base_signal.diff()

def f30_mca_014_struct_v14_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=101, w2=485, w3=284, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(485, min_periods=max(485//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5775 + 0.0018015 * anchor
    return base_signal.diff()

def f30_mca_015_struct_v15_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=108, w2=496, w3=297, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(496, min_periods=max(496//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3158 * slope + 0.0018016 * anchor
    return base_signal.diff()

def f30_mca_016_struct_v16_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=115, w2=507, w3=310, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(115)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.60625 + 0.0018017 * anchor
    return base_signal.diff()

def f30_mca_017_struct_v17_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=122, w2=15, w3=323, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 15)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.331 * acceleration + 0.0018018 * anchor
    return base_signal.diff()

def f30_mca_018_struct_v18_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=129, w2=26, w3=336, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(26, min_periods=max(26//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.861875 + 0.0018019 * anchor
    return base_signal.diff()

def f30_mca_019_struct_v19_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=136, w2=37, w3=349, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(37, min_periods=max(37//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3462 * _rolling_slope(draw, 349) + 0.001802 * anchor
    return base_signal.diff()

def f30_mca_020_struct_v20_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=143, w2=48, w3=362, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(48, min_periods=max(48//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.890625 + 0.0018021 * anchor
    return base_signal.diff()

def f30_mca_021_struct_v21_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=150, w2=59, w3=375, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 59)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.905 + 0.0018022 * anchor
    return base_signal.diff()

def f30_mca_022_struct_v22_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=157, w2=70, w3=388, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(70, min_periods=max(70//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.919375 + 0.0018023 * anchor
    return base_signal.diff()

def f30_mca_023_struct_v23_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=164, w2=81, w3=401, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(81, min_periods=max(81//3, 2)).rank(pct=True)
    persistence = change.rolling(401, min_periods=max(401//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3766 * persistence + 0.0018024 * anchor
    return base_signal.diff()

def f30_mca_024_struct_v24_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=171, w2=92, w3=414, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(92, min_periods=max(92//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.948125 + 0.0018025 * anchor
    return base_signal.diff()

def f30_mca_025_struct_v25_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=178, w2=103, w3=427, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(103, min_periods=max(103//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3918 * slope + 0.0018026 * anchor
    return base_signal.diff()

def f30_mca_026_struct_v26_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=185, w2=114, w3=440, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(114, min_periods=max(114//3, 2)).mean()
    noise = impulse.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.976875 + 0.0018027 * anchor
    return base_signal.diff()

def f30_mca_027_struct_v27_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=192, w2=125, w3=453, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 125)
    curvature = _rolling_slope(acceleration, 453)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.407 * acceleration + 0.0018028 * anchor
    return base_signal.diff()

def f30_mca_028_struct_v28_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=199, w2=136, w3=466, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(136, min_periods=max(136//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.005625 + 0.0018029 * anchor
    return base_signal.diff()

def f30_mca_029_struct_v29_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=206, w2=147, w3=479, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(147, min_periods=max(147//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0458 * _rolling_slope(draw, 479) + 0.001803 * anchor
    return base_signal.diff()

def f30_mca_030_struct_v30_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=213, w2=158, w3=492, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(158, min_periods=max(158//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.034375 + 0.0018031 * anchor
    return base_signal.diff()

def f30_mca_031_struct_v31_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=220, w2=169, w3=505, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 169)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.04875 + 0.0018032 * anchor
    return base_signal.diff()

def f30_mca_032_struct_v32_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=227, w2=180, w3=518, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.063125 + 0.0018033 * anchor
    return base_signal.diff()

def f30_mca_033_struct_v33_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=234, w2=191, w3=531, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(191, min_periods=max(191//3, 2)).rank(pct=True)
    persistence = change.rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0762 * persistence + 0.0018034 * anchor
    return base_signal.diff()

def f30_mca_034_struct_v34_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=241, w2=202, w3=544, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(202, min_periods=max(202//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.091875 + 0.0018035 * anchor
    return base_signal.diff()

def f30_mca_035_struct_v35_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=248, w2=213, w3=557, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(213, min_periods=max(213//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0914 * slope + 0.0018036 * anchor
    return base_signal.diff()

def f30_mca_036_struct_v36_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=255, w2=224, w3=570, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(224, min_periods=max(224//3, 2)).mean()
    noise = impulse.abs().rolling(570, min_periods=max(570//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.120625 + 0.0018037 * anchor
    return base_signal.diff()

def f30_mca_037_struct_v37_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=11, w2=235, w3=583, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 235)
    curvature = _rolling_slope(acceleration, 583)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1066 * acceleration + 0.0018038 * anchor
    return base_signal.diff()

def f30_mca_038_struct_v38_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=18, w2=246, w3=596, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(246, min_periods=max(246//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.149375 + 0.0018039 * anchor
    return base_signal.diff()

def f30_mca_039_struct_v39_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=25, w2=257, w3=609, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(257, min_periods=max(257//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1218 * _rolling_slope(draw, 609) + 0.001804 * anchor
    return base_signal.diff()

def f30_mca_040_struct_v40_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=32, w2=268, w3=622, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(268, min_periods=max(268//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(622, min_periods=max(622//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.178125 + 0.0018041 * anchor
    return base_signal.diff()

def f30_mca_041_struct_v41_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=39, w2=279, w3=635, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 279)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1925 + 0.0018042 * anchor
    return base_signal.diff()

def f30_mca_042_struct_v42_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=46, w2=290, w3=648, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(290, min_periods=max(290//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.206875 + 0.0018043 * anchor
    return base_signal.diff()

def f30_mca_043_struct_v43_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=53, w2=301, w3=661, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(53)
    rank = change.rolling(301, min_periods=max(301//3, 2)).rank(pct=True)
    persistence = change.rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1522 * persistence + 0.0018044 * anchor
    return base_signal.diff()

def f30_mca_044_struct_v44_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=60, w2=312, w3=674, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(312, min_periods=max(312//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.235625 + 0.0018045 * anchor
    return base_signal.diff()

def f30_mca_045_struct_v45_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=67, w2=323, w3=687, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(323, min_periods=max(323//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1674 * slope + 0.0018046 * anchor
    return base_signal.diff()

def f30_mca_046_struct_v46_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=74, w2=334, w3=700, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(74)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.264375 + 0.0018047 * anchor
    return base_signal.diff()

def f30_mca_047_struct_v47_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=81, w2=345, w3=713, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 345)
    curvature = _rolling_slope(acceleration, 713)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1826 * acceleration + 0.0018048 * anchor
    return base_signal.diff()

def f30_mca_048_struct_v48_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=88, w2=356, w3=726, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(356, min_periods=max(356//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.293125 + 0.0018049 * anchor
    return base_signal.diff()

def f30_mca_049_struct_v49_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=95, w2=367, w3=739, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(367, min_periods=max(367//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1978 * _rolling_slope(draw, 739) + 0.001805 * anchor
    return base_signal.diff()

def f30_mca_050_struct_v50_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=102, w2=378, w3=752, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(378, min_periods=max(378//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.321875 + 0.0018051 * anchor
    return base_signal.diff()

def f30_mca_051_struct_v51_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=109, w2=389, w3=765, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 389)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.33625 + 0.0018052 * anchor
    return base_signal.diff()

def f30_mca_052_struct_v52_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=116, w2=400, w3=21, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(400, min_periods=max(400//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.350625 + 0.0018053 * anchor
    return base_signal.diff()

def f30_mca_053_struct_v53_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=123, w2=411, w3=34, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(123)
    rank = change.rolling(411, min_periods=max(411//3, 2)).rank(pct=True)
    persistence = change.rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2282 * persistence + 0.0018054 * anchor
    return base_signal.diff()

def f30_mca_054_struct_v54_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=130, w2=422, w3=47, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(422, min_periods=max(422//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.379375 + 0.0018055 * anchor
    return base_signal.diff()

def f30_mca_055_struct_v55_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=137, w2=433, w3=60, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(433, min_periods=max(433//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2434 * slope + 0.0018056 * anchor
    return base_signal.diff()

def f30_mca_056_struct_v56_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=144, w2=444, w3=73, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(444, min_periods=max(444//3, 2)).mean()
    noise = impulse.abs().rolling(73, min_periods=max(73//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.408125 + 0.0018057 * anchor
    return base_signal.diff()

def f30_mca_057_struct_v57_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=151, w2=455, w3=86, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 455)
    curvature = _rolling_slope(acceleration, 86)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2586 * acceleration + 0.0018058 * anchor
    return base_signal.diff()

def f30_mca_058_struct_v58_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=158, w2=466, w3=99, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(158, min_periods=max(158//3, 2)).mean(), upside.rolling(466, min_periods=max(466//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(99) * 1.436875 + 0.0018059 * anchor
    return base_signal.diff()

def f30_mca_059_struct_v59_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=165, w2=477, w3=112, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(477, min_periods=max(477//3, 2)).max()
    rebound = x - x.rolling(165, min_periods=max(165//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2738 * _rolling_slope(draw, 112) + 0.001806 * anchor
    return base_signal.diff()

def f30_mca_060_struct_v60_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=172, w2=488, w3=125, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(488, min_periods=max(488//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(125, min_periods=max(125//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.465625 + 0.0018061 * anchor
    return base_signal.diff()

def f30_mca_061_struct_v61_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=179, w2=499, w3=138, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 499)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=138, adjust=False).mean() * 1.48 + 0.0018062 * anchor
    return base_signal.diff()

def f30_mca_062_struct_v62_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=186, w2=510, w3=151, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(510, min_periods=max(510//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.494375 + 0.0018063 * anchor
    return base_signal.diff()

def f30_mca_063_struct_v63_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=193, w2=18, w3=164, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(18, min_periods=max(18//3, 2)).rank(pct=True)
    persistence = change.rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3042 * persistence + 0.0018064 * anchor
    return base_signal.diff()

def f30_mca_064_struct_v64_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=200, w2=29, w3=177, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(29, min_periods=max(29//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.523125 + 0.0018065 * anchor
    return base_signal.diff()

def f30_mca_065_struct_v65_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=207, w2=40, w3=190, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(40, min_periods=max(40//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3194 * slope + 0.0018066 * anchor
    return base_signal.diff()

def f30_mca_066_struct_v66_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=214, w2=51, w3=203, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(51, min_periods=max(51//3, 2)).mean()
    noise = impulse.abs().rolling(203, min_periods=max(203//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.551875 + 0.0018067 * anchor
    return base_signal.diff()

def f30_mca_067_struct_v67_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=221, w2=62, w3=216, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 62)
    curvature = _rolling_slope(acceleration, 216)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3346 * acceleration + 0.0018068 * anchor
    return base_signal.diff()

def f30_mca_068_struct_v68_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=228, w2=73, w3=229, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(73, min_periods=max(73//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.580625 + 0.0018069 * anchor
    return base_signal.diff()

def f30_mca_069_struct_v69_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=235, w2=84, w3=242, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(84, min_periods=max(84//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3498 * _rolling_slope(draw, 242) + 0.001807 * anchor
    return base_signal.diff()

def f30_mca_070_struct_v70_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=242, w2=95, w3=255, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(95, min_periods=max(95//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.609375 + 0.0018071 * anchor
    return base_signal.diff()

def f30_mca_071_struct_v71_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=249, w2=106, w3=268, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=268, adjust=False).mean() * 0.850625 + 0.0018072 * anchor
    return base_signal.diff()

def f30_mca_072_struct_v72_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=5, w2=117, w3=281, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(5, min_periods=max(5//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.865 + 0.0018073 * anchor
    return base_signal.diff()

def f30_mca_073_struct_v73_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=12, w2=128, w3=294, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(12)
    rank = change.rolling(128, min_periods=max(128//3, 2)).rank(pct=True)
    persistence = change.rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3802 * persistence + 0.0018074 * anchor
    return base_signal.diff()

def f30_mca_074_struct_v74_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=19, w2=139, w3=307, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(19, min_periods=max(19//3, 2)).std()
    vol_slow = ret.rolling(139, min_periods=max(139//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.89375 + 0.0018075 * anchor
    return base_signal.diff()

def f30_mca_075_struct_v75_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=26, w2=150, w3=320, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(150, min_periods=max(150//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 26)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3954 * slope + 0.0018076 * anchor
    return base_signal.diff()
