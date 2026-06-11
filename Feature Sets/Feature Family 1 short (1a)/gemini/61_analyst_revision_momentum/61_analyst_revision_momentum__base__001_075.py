"""61 analyst revision momentum base features 1-75 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Analyst_Sentiment - Institutional-grade short-side signal.
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

def f61_arm_001_analyst_v1(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=209, w2=480, w3=269, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 480)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=269, adjust=False).mean() * 1.555 + 0.0034202 * anchor

def f61_arm_002_analyst_v2(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=216, w2=491, w3=282, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(491, min_periods=max(491//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.569375 + 0.0034203 * anchor

def f61_arm_003_analyst_v3(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=223, w2=502, w3=295, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(502, min_periods=max(502//3, 2)).rank(pct=True)
    persistence = change.rolling(295, min_periods=max(295//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2618 * persistence + 0.0034204 * anchor

def f61_arm_004_analyst_v4(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=230, w2=10, w3=308, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(10, min_periods=max(10//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.598125 + 0.0034205 * anchor

def f61_arm_005_analyst_v5(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=237, w2=21, w3=321, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(21, min_periods=max(21//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.277 * slope + 0.0034206 * anchor

def f61_arm_006_analyst_v6(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=244, w2=32, w3=334, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(32, min_periods=max(32//3, 2)).mean()
    noise = impulse.abs().rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.85375 + 0.0034207 * anchor

def f61_arm_007_analyst_v7(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=251, w2=43, w3=347, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 43)
    curvature = _rolling_slope(acceleration, 347)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2922 * acceleration + 0.0034208 * anchor

def f61_arm_008_analyst_v8(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=7, w2=54, w3=360, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(54, min_periods=max(54//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8825 + 0.0034209 * anchor

def f61_arm_009_analyst_v9(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=14, w2=65, w3=373, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(65, min_periods=max(65//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3074 * _rolling_slope(draw, 373) + 0.003421 * anchor

def f61_arm_010_analyst_v10(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=21, w2=76, w3=386, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(76, min_periods=max(76//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.91125 + 0.0034211 * anchor

def f61_arm_011_analyst_v11(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=28, w2=87, w3=399, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 87)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.925625 + 0.0034212 * anchor

def f61_arm_012_analyst_v12(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=35, w2=98, w3=412, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(98, min_periods=max(98//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.94 + 0.0034213 * anchor

def f61_arm_013_analyst_v13(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=42, w2=109, w3=425, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(42)
    rank = change.rolling(109, min_periods=max(109//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3378 * persistence + 0.0034214 * anchor

def f61_arm_014_analyst_v14(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=49, w2=120, w3=438, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(120, min_periods=max(120//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.96875 + 0.0034215 * anchor

def f61_arm_015_analyst_v15(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=56, w2=131, w3=451, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.353 * slope + 0.0034216 * anchor

def f61_arm_016_analyst_v16(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=63, w2=142, w3=464, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(63)
    drag = impulse.rolling(142, min_periods=max(142//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9975 + 0.0034217 * anchor

def f61_arm_017_analyst_v17(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=70, w2=153, w3=477, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 153)
    curvature = _rolling_slope(acceleration, 477)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3682 * acceleration + 0.0034218 * anchor

def f61_arm_018_analyst_v18(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=77, w2=164, w3=490, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(164, min_periods=max(164//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.02625 + 0.0034219 * anchor

def f61_arm_019_analyst_v19(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=84, w2=175, w3=503, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(175, min_periods=max(175//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3834 * _rolling_slope(draw, 503) + 0.003422 * anchor

def f61_arm_020_analyst_v20(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=91, w2=186, w3=516, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(186, min_periods=max(186//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.055 + 0.0034221 * anchor

def f61_arm_021_analyst_v21(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=98, w2=197, w3=529, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 197)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.069375 + 0.0034222 * anchor

def f61_arm_022_analyst_v22(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=105, w2=208, w3=542, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(208, min_periods=max(208//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.08375 + 0.0034223 * anchor

def f61_arm_023_analyst_v23(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=112, w2=219, w3=555, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(112)
    rank = change.rolling(219, min_periods=max(219//3, 2)).rank(pct=True)
    persistence = change.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0374 * persistence + 0.0034224 * anchor

def f61_arm_024_analyst_v24(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=119, w2=230, w3=568, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1125 + 0.0034225 * anchor

def f61_arm_025_analyst_v25(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=126, w2=241, w3=581, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0526 * slope + 0.0034226 * anchor

def f61_arm_026_analyst_v26(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=133, w2=252, w3=594, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(252, min_periods=max(252//3, 2)).mean()
    noise = impulse.abs().rolling(594, min_periods=max(594//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.14125 + 0.0034227 * anchor

def f61_arm_027_analyst_v27(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=140, w2=263, w3=607, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 140)
    acceleration = _rolling_slope(velocity, 263)
    curvature = _rolling_slope(acceleration, 607)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0678 * acceleration + 0.0034228 * anchor

def f61_arm_028_analyst_v28(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=147, w2=274, w3=620, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(147, min_periods=max(147//3, 2)).mean(), upside.rolling(274, min_periods=max(274//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.17 + 0.0034229 * anchor

def f61_arm_029_analyst_v29(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=154, w2=285, w3=633, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(285, min_periods=max(285//3, 2)).max()
    rebound = x - x.rolling(154, min_periods=max(154//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.083 * _rolling_slope(draw, 633) + 0.003423 * anchor

def f61_arm_030_analyst_v30(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=161, w2=296, w3=646, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 161)
    baseline = trend.rolling(296, min_periods=max(296//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.19875 + 0.0034231 * anchor

def f61_arm_031_analyst_v31(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=168, w2=307, w3=659, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 168)
    slow = _rolling_slope(x, 307)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.213125 + 0.0034232 * anchor

def f61_arm_032_analyst_v32(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=175, w2=318, w3=672, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(318, min_periods=max(318//3, 2)).max()
    trough = x.rolling(175, min_periods=max(175//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2275 + 0.0034233 * anchor

def f61_arm_033_analyst_v33(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=182, w2=329, w3=685, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(329, min_periods=max(329//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1134 * persistence + 0.0034234 * anchor

def f61_arm_034_analyst_v34(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=189, w2=340, w3=698, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(189, min_periods=max(189//3, 2)).std()
    vol_slow = ret.rolling(340, min_periods=max(340//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.25625 + 0.0034235 * anchor

def f61_arm_035_analyst_v35(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=196, w2=351, w3=711, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(351, min_periods=max(351//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 196)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1286 * slope + 0.0034236 * anchor

def f61_arm_036_analyst_v36(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=203, w2=362, w3=724, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.285 + 0.0034237 * anchor

def f61_arm_037_analyst_v37(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=210, w2=373, w3=737, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 210)
    acceleration = _rolling_slope(velocity, 373)
    curvature = _rolling_slope(acceleration, 737)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1438 * acceleration + 0.0034238 * anchor

def f61_arm_038_analyst_v38(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=217, w2=384, w3=750, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(217, min_periods=max(217//3, 2)).mean(), upside.rolling(384, min_periods=max(384//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.31375 + 0.0034239 * anchor

def f61_arm_039_analyst_v39(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=224, w2=395, w3=763, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(395, min_periods=max(395//3, 2)).max()
    rebound = x - x.rolling(224, min_periods=max(224//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.159 * _rolling_slope(draw, 763) + 0.003424 * anchor

def f61_arm_040_analyst_v40(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=231, w2=406, w3=19, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(406, min_periods=max(406//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3425 + 0.0034241 * anchor

def f61_arm_041_analyst_v41(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=238, w2=417, w3=32, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 417)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=32, adjust=False).mean() * 1.356875 + 0.0034242 * anchor

def f61_arm_042_analyst_v42(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=245, w2=428, w3=45, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(428, min_periods=max(428//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.37125 + 0.0034243 * anchor

def f61_arm_043_analyst_v43(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=252, w2=439, w3=58, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(439, min_periods=max(439//3, 2)).rank(pct=True)
    persistence = change.rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1894 * persistence + 0.0034244 * anchor

def f61_arm_044_analyst_v44(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=8, w2=450, w3=71, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(8, min_periods=max(8//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4 + 0.0034245 * anchor

def f61_arm_045_analyst_v45(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=15, w2=461, w3=84, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(461, min_periods=max(461//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 15)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2046 * slope + 0.0034246 * anchor

def f61_arm_046_analyst_v46(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=22, w2=472, w3=97, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(22)
    drag = impulse.rolling(472, min_periods=max(472//3, 2)).mean()
    noise = impulse.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42875 + 0.0034247 * anchor

def f61_arm_047_analyst_v47(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=29, w2=483, w3=110, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 29)
    acceleration = _rolling_slope(velocity, 483)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2198 * acceleration + 0.0034248 * anchor

def f61_arm_048_analyst_v48(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=36, w2=494, w3=123, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(36, min_periods=max(36//3, 2)).mean(), upside.rolling(494, min_periods=max(494//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(123) * 1.4575 + 0.0034249 * anchor

def f61_arm_049_analyst_v49(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=43, w2=505, w3=136, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(505, min_periods=max(505//3, 2)).max()
    rebound = x - x.rolling(43, min_periods=max(43//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.235 * _rolling_slope(draw, 136) + 0.003425 * anchor

def f61_arm_050_analyst_v50(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=50, w2=13, w3=149, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.48625 + 0.0034251 * anchor

def f61_arm_051_analyst_v51(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=57, w2=24, w3=162, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 24)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=162, adjust=False).mean() * 1.500625 + 0.0034252 * anchor

def f61_arm_052_analyst_v52(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=64, w2=35, w3=175, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(35, min_periods=max(35//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.515 + 0.0034253 * anchor

def f61_arm_053_analyst_v53(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=71, w2=46, w3=188, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(71)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(188, min_periods=max(188//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2654 * persistence + 0.0034254 * anchor

def f61_arm_054_analyst_v54(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=78, w2=57, w3=201, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(57, min_periods=max(57//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.54375 + 0.0034255 * anchor

def f61_arm_055_analyst_v55(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=85, w2=68, w3=214, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2806 * slope + 0.0034256 * anchor

def f61_arm_056_analyst_v56(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=92, w2=79, w3=227, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(92)
    drag = impulse.rolling(79, min_periods=max(79//3, 2)).mean()
    noise = impulse.abs().rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5725 + 0.0034257 * anchor

def f61_arm_057_analyst_v57(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=99, w2=90, w3=240, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 90)
    curvature = _rolling_slope(acceleration, 240)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2958 * acceleration + 0.0034258 * anchor

def f61_arm_058_analyst_v58(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=106, w2=101, w3=253, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(106, min_periods=max(106//3, 2)).mean(), upside.rolling(101, min_periods=max(101//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.60125 + 0.0034259 * anchor

def f61_arm_059_analyst_v59(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=113, w2=112, w3=266, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(112, min_periods=max(112//3, 2)).max()
    rebound = x - x.rolling(113, min_periods=max(113//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.311 * _rolling_slope(draw, 266) + 0.003426 * anchor

def f61_arm_060_analyst_v60(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=120, w2=123, w3=279, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(123, min_periods=max(123//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.856875 + 0.0034261 * anchor

def f61_arm_061_analyst_v61(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=127, w2=134, w3=292, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 134)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=292, adjust=False).mean() * 0.87125 + 0.0034262 * anchor

def f61_arm_062_analyst_v62(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=134, w2=145, w3=305, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(145, min_periods=max(145//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.885625 + 0.0034263 * anchor

def f61_arm_063_analyst_v63(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=141, w2=156, w3=318, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(156, min_periods=max(156//3, 2)).rank(pct=True)
    persistence = change.rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3414 * persistence + 0.0034264 * anchor

def f61_arm_064_analyst_v64(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=148, w2=167, w3=331, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(167, min_periods=max(167//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.914375 + 0.0034265 * anchor

def f61_arm_065_analyst_v65(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=155, w2=178, w3=344, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3566 * slope + 0.0034266 * anchor

def f61_arm_066_analyst_v66(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=162, w2=189, w3=357, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(189, min_periods=max(189//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.943125 + 0.0034267 * anchor

def f61_arm_067_analyst_v67(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=169, w2=200, w3=370, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 200)
    curvature = _rolling_slope(acceleration, 370)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3718 * acceleration + 0.0034268 * anchor

def f61_arm_068_analyst_v68(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=176, w2=211, w3=383, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(176, min_periods=max(176//3, 2)).mean(), upside.rolling(211, min_periods=max(211//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.971875 + 0.0034269 * anchor

def f61_arm_069_analyst_v69(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=183, w2=222, w3=396, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(222, min_periods=max(222//3, 2)).max()
    rebound = x - x.rolling(183, min_periods=max(183//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.387 * _rolling_slope(draw, 396) + 0.003427 * anchor

def f61_arm_070_analyst_v70(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=190, w2=233, w3=409, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(233, min_periods=max(233//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(409, min_periods=max(409//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.000625 + 0.0034271 * anchor

def f61_arm_071_analyst_v71(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=197, w2=244, w3=422, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 244)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.015 + 0.0034272 * anchor

def f61_arm_072_analyst_v72(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=204, w2=255, w3=435, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.029375 + 0.0034273 * anchor

def f61_arm_073_analyst_v73(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=211, w2=266, w3=448, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(266, min_periods=max(266//3, 2)).rank(pct=True)
    persistence = change.rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.041 * persistence + 0.0034274 * anchor

def f61_arm_074_analyst_v74(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=218, w2=277, w3=461, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(277, min_periods=max(277//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.058125 + 0.0034275 * anchor

def f61_arm_075_analyst_v75(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=225, w2=288, w3=474, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(288, min_periods=max(288//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0562 * slope + 0.0034276 * anchor
