"""31 cash burn acceleration base features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f31_cba_001_struct_v1(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=194, w2=403, w3=345, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 194)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.51125 + 0.0018602 * anchor

def f31_cba_002_struct_v2(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=201, w2=414, w3=358, lag=2)."""
    x = shortinterest.shift(2)
    peak = x.rolling(414, min_periods=max(414//3, 2)).max()
    trough = x.rolling(201, min_periods=max(201//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.525625 + 0.0018603 * anchor

def f31_cba_003_struct_v3(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=208, w2=425, w3=371, lag=5)."""
    x = utilization.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2678 * persistence + 0.0018604 * anchor

def f31_cba_004_struct_v4(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=215, w2=436, w3=384, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(215, min_periods=max(215//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.554375 + 0.0018605 * anchor

def f31_cba_005_struct_v5(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=222, w2=447, w3=397, lag=21)."""
    x = vex.shift(21)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 222)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.283 * slope + 0.0018606 * anchor

def f31_cba_006_struct_v6(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=229, w2=458, w3=410, lag=42)."""
    x = revenue.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(458, min_periods=max(458//3, 2)).mean()
    noise = impulse.abs().rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.583125 + 0.0018607 * anchor

def f31_cba_007_struct_v7(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=236, w2=469, w3=423, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 236)
    acceleration = _rolling_slope(velocity, 469)
    curvature = _rolling_slope(acceleration, 423)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2982 * acceleration + 0.0018608 * anchor

def f31_cba_008_struct_v8(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=243, w2=480, w3=436, lag=0)."""
    x = shortinterest.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(243, min_periods=max(243//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.611875 + 0.0018609 * anchor

def f31_cba_009_struct_v9(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=250, w2=491, w3=449, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(250, min_periods=max(250//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3134 * _rolling_slope(draw, 449) + 0.001861 * anchor

def f31_cba_010_struct_v10(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=6, w2=502, w3=462, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.8675 + 0.0018611 * anchor

def f31_cba_011_struct_v11(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=13, w2=10, w3=475, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 10)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.881875 + 0.0018612 * anchor

def f31_cba_012_struct_v12(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=20, w2=21, w3=488, lag=10)."""
    x = revenue.shift(10)
    peak = x.rolling(21, min_periods=max(21//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.89625 + 0.0018613 * anchor

def f31_cba_013_struct_v13(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=27, w2=32, w3=501, lag=21)."""
    x = netinc.shift(21)
    change = x.pct_change(27)
    rank = change.rolling(32, min_periods=max(32//3, 2)).rank(pct=True)
    persistence = change.rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3438 * persistence + 0.0018614 * anchor

def f31_cba_014_struct_v14(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=34, w2=43, w3=514, lag=42)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.925 + 0.0018615 * anchor

def f31_cba_015_struct_v15(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=41, w2=54, w3=527, lag=63)."""
    x = utilization.shift(63)
    ma = x.rolling(54, min_periods=max(54//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.359 * slope + 0.0018616 * anchor

def f31_cba_016_struct_v16(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=48, w2=65, w3=540, lag=0)."""
    x = gex.shift(0)
    impulse = x.diff(48)
    drag = impulse.rolling(65, min_periods=max(65//3, 2)).mean()
    noise = impulse.abs().rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.95375 + 0.0018617 * anchor

def f31_cba_017_struct_v17(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=55, w2=76, w3=553, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 553)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3742 * acceleration + 0.0018618 * anchor

def f31_cba_018_struct_v18(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=62, w2=87, w3=566, lag=2)."""
    x = revenue.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9825 + 0.0018619 * anchor

def f31_cba_019_struct_v19(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=69, w2=98, w3=579, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    draw = x - x.rolling(98, min_periods=max(98//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3894 * _rolling_slope(draw, 579) + 0.001862 * anchor

def f31_cba_020_struct_v20(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=76, w2=109, w3=592, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(109, min_periods=max(109//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.01125 + 0.0018621 * anchor

def f31_cba_021_struct_v21(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=83, w2=120, w3=605, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 120)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.025625 + 0.0018622 * anchor

def f31_cba_022_struct_v22(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=90, w2=131, w3=618, lag=42)."""
    x = gex.shift(42)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.04 + 0.0018623 * anchor

def f31_cba_023_struct_v23(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=97, w2=142, w3=631, lag=63)."""
    x = vex.shift(63)
    change = x.pct_change(97)
    rank = change.rolling(142, min_periods=max(142//3, 2)).rank(pct=True)
    persistence = change.rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0434 * persistence + 0.0018624 * anchor

def f31_cba_024_struct_v24(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=104, w2=153, w3=644, lag=0)."""
    x = _safe_log(revenue.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06875 + 0.0018625 * anchor

def f31_cba_025_struct_v25(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=111, w2=164, w3=657, lag=1)."""
    x = netinc.shift(1)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0586 * slope + 0.0018626 * anchor

def f31_cba_026_struct_v26(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=118, w2=175, w3=670, lag=2)."""
    x = shortinterest.shift(2)
    impulse = x.diff(118)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0975 + 0.0018627 * anchor

def f31_cba_027_struct_v27(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=125, w2=186, w3=683, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 186)
    curvature = _rolling_slope(acceleration, 683)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0738 * acceleration + 0.0018628 * anchor

def f31_cba_028_struct_v28(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=132, w2=197, w3=696, lag=10)."""
    x = gex.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.12625 + 0.0018629 * anchor

def f31_cba_029_struct_v29(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=139, w2=208, w3=709, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.089 * _rolling_slope(draw, 709) + 0.001863 * anchor

def f31_cba_030_struct_v30(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=146, w2=219, w3=722, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(219, min_periods=max(219//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.155 + 0.0018631 * anchor

def f31_cba_031_struct_v31(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=153, w2=230, w3=735, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 230)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.169375 + 0.0018632 * anchor

def f31_cba_032_struct_v32(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=160, w2=241, w3=748, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(241, min_periods=max(241//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.18375 + 0.0018633 * anchor

def f31_cba_033_struct_v33(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=167, w2=252, w3=761, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1194 * persistence + 0.0018634 * anchor

def f31_cba_034_struct_v34(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=174, w2=263, w3=17, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2125 + 0.0018635 * anchor

def f31_cba_035_struct_v35(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=181, w2=274, w3=30, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(274, min_periods=max(274//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1346 * slope + 0.0018636 * anchor

def f31_cba_036_struct_v36(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=188, w2=285, w3=43, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(285, min_periods=max(285//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.24125 + 0.0018637 * anchor

def f31_cba_037_struct_v37(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=195, w2=296, w3=56, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 56)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1498 * acceleration + 0.0018638 * anchor

def f31_cba_038_struct_v38(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=202, w2=307, w3=69, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(69) * 1.27 + 0.0018639 * anchor

def f31_cba_039_struct_v39(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=209, w2=318, w3=82, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.165 * _rolling_slope(draw, 82) + 0.001864 * anchor

def f31_cba_040_struct_v40(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=216, w2=329, w3=95, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(329, min_periods=max(329//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.29875 + 0.0018641 * anchor

def f31_cba_041_struct_v41(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=223, w2=340, w3=108, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=108, adjust=False).mean() * 1.313125 + 0.0018642 * anchor

def f31_cba_042_struct_v42(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=230, w2=351, w3=121, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(351, min_periods=max(351//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.3275 + 0.0018643 * anchor

def f31_cba_043_struct_v43(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=237, w2=362, w3=134, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(362, min_periods=max(362//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1954 * persistence + 0.0018644 * anchor

def f31_cba_044_struct_v44(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=244, w2=373, w3=147, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(373, min_periods=max(373//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35625 + 0.0018645 * anchor

def f31_cba_045_struct_v45(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=251, w2=384, w3=160, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(384, min_periods=max(384//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2106 * slope + 0.0018646 * anchor

def f31_cba_046_struct_v46(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=7, w2=395, w3=173, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(7)
    drag = impulse.rolling(395, min_periods=max(395//3, 2)).mean()
    noise = impulse.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.385 + 0.0018647 * anchor

def f31_cba_047_struct_v47(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=14, w2=406, w3=186, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 406)
    curvature = _rolling_slope(acceleration, 186)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2258 * acceleration + 0.0018648 * anchor

def f31_cba_048_struct_v48(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=21, w2=417, w3=199, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.41375 + 0.0018649 * anchor

def f31_cba_049_struct_v49(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=28, w2=428, w3=212, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.241 * _rolling_slope(draw, 212) + 0.001865 * anchor

def f31_cba_050_struct_v50(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=35, w2=439, w3=225, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.4425 + 0.0018651 * anchor

def f31_cba_051_struct_v51(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=42, w2=450, w3=238, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 450)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=238, adjust=False).mean() * 1.456875 + 0.0018652 * anchor

def f31_cba_052_struct_v52(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=49, w2=461, w3=251, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.47125 + 0.0018653 * anchor

def f31_cba_053_struct_v53(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=56, w2=472, w3=264, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(56)
    rank = change.rolling(472, min_periods=max(472//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2714 * persistence + 0.0018654 * anchor

def f31_cba_054_struct_v54(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=63, w2=483, w3=277, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(483, min_periods=max(483//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.5 + 0.0018655 * anchor

def f31_cba_055_struct_v55(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=70, w2=494, w3=290, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2866 * slope + 0.0018656 * anchor

def f31_cba_056_struct_v56(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=77, w2=505, w3=303, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(77)
    drag = impulse.rolling(505, min_periods=max(505//3, 2)).mean()
    noise = impulse.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.52875 + 0.0018657 * anchor

def f31_cba_057_struct_v57(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=84, w2=13, w3=316, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 13)
    curvature = _rolling_slope(acceleration, 316)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3018 * acceleration + 0.0018658 * anchor

def f31_cba_058_struct_v58(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=91, w2=24, w3=329, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(24, min_periods=max(24//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.5575 + 0.0018659 * anchor

def f31_cba_059_struct_v59(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=98, w2=35, w3=342, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.317 * _rolling_slope(draw, 342) + 0.001866 * anchor

def f31_cba_060_struct_v60(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=105, w2=46, w3=355, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(46, min_periods=max(46//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.58625 + 0.0018661 * anchor

def f31_cba_061_struct_v61(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=112, w2=57, w3=368, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 57)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.600625 + 0.0018662 * anchor

def f31_cba_062_struct_v62(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=119, w2=68, w3=381, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(68, min_periods=max(68//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.615 + 0.0018663 * anchor

def f31_cba_063_struct_v63(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=126, w2=79, w3=394, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(79, min_periods=max(79//3, 2)).rank(pct=True)
    persistence = change.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3474 * persistence + 0.0018664 * anchor

def f31_cba_064_struct_v64(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=133, w2=90, w3=407, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(90, min_periods=max(90//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.870625 + 0.0018665 * anchor

def f31_cba_065_struct_v65(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=140, w2=101, w3=420, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(101, min_periods=max(101//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3626 * slope + 0.0018666 * anchor

def f31_cba_066_struct_v66(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=147, w2=112, w3=433, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(112, min_periods=max(112//3, 2)).mean()
    noise = impulse.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.899375 + 0.0018667 * anchor

def f31_cba_067_struct_v67(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=154, w2=123, w3=446, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 123)
    curvature = _rolling_slope(acceleration, 446)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3778 * acceleration + 0.0018668 * anchor

def f31_cba_068_struct_v68(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=161, w2=134, w3=459, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(134, min_periods=max(134//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.928125 + 0.0018669 * anchor

def f31_cba_069_struct_v69(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=168, w2=145, w3=472, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(145, min_periods=max(145//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.393 * _rolling_slope(draw, 472) + 0.001867 * anchor

def f31_cba_070_struct_v70(gex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=175, w2=156, w3=485, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(156, min_periods=max(156//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(485, min_periods=max(485//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.956875 + 0.0018671 * anchor

def f31_cba_071_struct_v71(vex: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=182, w2=167, w3=498, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 167)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.97125 + 0.0018672 * anchor

def f31_cba_072_struct_v72(revenue: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=189, w2=178, w3=511, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(178, min_periods=max(178//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.985625 + 0.0018673 * anchor

def f31_cba_073_struct_v73(netinc: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=196, w2=189, w3=524, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(189, min_periods=max(189//3, 2)).rank(pct=True)
    persistence = change.rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.047 * persistence + 0.0018674 * anchor

def f31_cba_074_struct_v74(shortinterest: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=203, w2=200, w3=537, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(200, min_periods=max(200//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.014375 + 0.0018675 * anchor

def f31_cba_075_struct_v75(utilization: pd.Series) -> pd.Series:
    """De-duplicated struct replacement signal (w1=210, w2=211, w3=550, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(211, min_periods=max(211//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0622 * slope + 0.0018676 * anchor
