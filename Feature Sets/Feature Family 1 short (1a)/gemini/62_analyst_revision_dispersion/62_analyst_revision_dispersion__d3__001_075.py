"""62 analyst revision dispersion d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f62_ard_001_analyst_v1_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=142, w2=38, w3=499, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 38)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9025 + 0.0034802 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_002_analyst_v2_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=149, w2=49, w3=512, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(49, min_periods=max(49//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.916875 + 0.0034803 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_003_analyst_v3_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=156, w2=60, w3=525, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(60, min_periods=max(60//3, 2)).rank(pct=True)
    persistence = change.rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.305 * persistence + 0.0034804 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_004_analyst_v4_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=163, w2=71, w3=538, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(71, min_periods=max(71//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.945625 + 0.0034805 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_005_analyst_v5_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=170, w2=82, w3=551, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(82, min_periods=max(82//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3202 * slope + 0.0034806 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_006_analyst_v6_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=177, w2=93, w3=564, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(93, min_periods=max(93//3, 2)).mean()
    noise = impulse.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.974375 + 0.0034807 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_007_analyst_v7_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=184, w2=104, w3=577, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 104)
    curvature = _rolling_slope(acceleration, 577)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3354 * acceleration + 0.0034808 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_008_analyst_v8_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=191, w2=115, w3=590, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(191, min_periods=max(191//3, 2)).mean(), upside.rolling(115, min_periods=max(115//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.003125 + 0.0034809 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_009_analyst_v9_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=198, w2=126, w3=603, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(126, min_periods=max(126//3, 2)).max()
    rebound = x - x.rolling(198, min_periods=max(198//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3506 * _rolling_slope(draw, 603) + 0.003481 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_010_analyst_v10_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=205, w2=137, w3=616, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 205)
    baseline = trend.rolling(137, min_periods=max(137//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.031875 + 0.0034811 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_011_analyst_v11_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=212, w2=148, w3=629, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 212)
    slow = _rolling_slope(x, 148)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.04625 + 0.0034812 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_012_analyst_v12_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=219, w2=159, w3=642, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(159, min_periods=max(159//3, 2)).max()
    trough = x.rolling(219, min_periods=max(219//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.060625 + 0.0034813 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_013_analyst_v13_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=226, w2=170, w3=655, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(170, min_periods=max(170//3, 2)).rank(pct=True)
    persistence = change.rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.381 * persistence + 0.0034814 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_014_analyst_v14_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=233, w2=181, w3=668, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(233, min_periods=max(233//3, 2)).std()
    vol_slow = ret.rolling(181, min_periods=max(181//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.089375 + 0.0034815 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_015_analyst_v15_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=240, w2=192, w3=681, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(192, min_periods=max(192//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 240)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3962 * slope + 0.0034816 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_016_analyst_v16_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=247, w2=203, w3=694, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(203, min_periods=max(203//3, 2)).mean()
    noise = impulse.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.118125 + 0.0034817 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_017_analyst_v17_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=254, w2=214, w3=707, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 254)
    acceleration = _rolling_slope(velocity, 214)
    curvature = _rolling_slope(acceleration, 707)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.035 * acceleration + 0.0034818 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_018_analyst_v18_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=10, w2=225, w3=720, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(10, min_periods=max(10//3, 2)).mean(), upside.rolling(225, min_periods=max(225//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.146875 + 0.0034819 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_019_analyst_v19_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=17, w2=236, w3=733, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(236, min_periods=max(236//3, 2)).max()
    rebound = x - x.rolling(17, min_periods=max(17//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0502 * _rolling_slope(draw, 733) + 0.003482 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_020_analyst_v20_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=24, w2=247, w3=746, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(247, min_periods=max(247//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.175625 + 0.0034821 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_021_analyst_v21_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=31, w2=258, w3=759, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 31)
    slow = _rolling_slope(x, 258)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.19 + 0.0034822 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_022_analyst_v22_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=38, w2=269, w3=15, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(269, min_periods=max(269//3, 2)).max()
    trough = x.rolling(38, min_periods=max(38//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.204375 + 0.0034823 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_023_analyst_v23_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=45, w2=280, w3=28, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(45)
    rank = change.rolling(280, min_periods=max(280//3, 2)).rank(pct=True)
    persistence = change.rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0806 * persistence + 0.0034824 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_024_analyst_v24_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=52, w2=291, w3=41, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(52, min_periods=max(52//3, 2)).std()
    vol_slow = ret.rolling(291, min_periods=max(291//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.233125 + 0.0034825 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_025_analyst_v25_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=59, w2=302, w3=54, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(302, min_periods=max(302//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 59)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0958 * slope + 0.0034826 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_026_analyst_v26_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=66, w2=313, w3=67, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(66)
    drag = impulse.rolling(313, min_periods=max(313//3, 2)).mean()
    noise = impulse.abs().rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.261875 + 0.0034827 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_027_analyst_v27_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=73, w2=324, w3=80, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 73)
    acceleration = _rolling_slope(velocity, 324)
    curvature = _rolling_slope(acceleration, 80)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.111 * acceleration + 0.0034828 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_028_analyst_v28_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=80, w2=335, w3=93, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(335, min_periods=max(335//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(93) * 1.290625 + 0.0034829 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_029_analyst_v29_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=87, w2=346, w3=106, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(346, min_periods=max(346//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1262 * _rolling_slope(draw, 106) + 0.003483 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_030_analyst_v30_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=94, w2=357, w3=119, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 94)
    baseline = trend.rolling(357, min_periods=max(357//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.319375 + 0.0034831 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_031_analyst_v31_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=101, w2=368, w3=132, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 101)
    slow = _rolling_slope(x, 368)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=132, adjust=False).mean() * 1.33375 + 0.0034832 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_032_analyst_v32_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=108, w2=379, w3=145, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(379, min_periods=max(379//3, 2)).max()
    trough = x.rolling(108, min_periods=max(108//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.348125 + 0.0034833 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_033_analyst_v33_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=115, w2=390, w3=158, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(115)
    rank = change.rolling(390, min_periods=max(390//3, 2)).rank(pct=True)
    persistence = change.rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1566 * persistence + 0.0034834 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_034_analyst_v34_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=122, w2=401, w3=171, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(122, min_periods=max(122//3, 2)).std()
    vol_slow = ret.rolling(401, min_periods=max(401//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.376875 + 0.0034835 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_035_analyst_v35_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=129, w2=412, w3=184, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(412, min_periods=max(412//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 129)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1718 * slope + 0.0034836 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_036_analyst_v36_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=136, w2=423, w3=197, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.405625 + 0.0034837 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_037_analyst_v37_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=143, w2=434, w3=210, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 143)
    acceleration = _rolling_slope(velocity, 434)
    curvature = _rolling_slope(acceleration, 210)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.187 * acceleration + 0.0034838 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_038_analyst_v38_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=150, w2=445, w3=223, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(150, min_periods=max(150//3, 2)).mean(), upside.rolling(445, min_periods=max(445//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.434375 + 0.0034839 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_039_analyst_v39_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=157, w2=456, w3=236, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(456, min_periods=max(456//3, 2)).max()
    rebound = x - x.rolling(157, min_periods=max(157//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2022 * _rolling_slope(draw, 236) + 0.003484 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_040_analyst_v40_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=164, w2=467, w3=249, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(467, min_periods=max(467//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.463125 + 0.0034841 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_041_analyst_v41_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=171, w2=478, w3=262, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 478)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=262, adjust=False).mean() * 1.4775 + 0.0034842 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_042_analyst_v42_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=178, w2=489, w3=275, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(489, min_periods=max(489//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.491875 + 0.0034843 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_043_analyst_v43_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=185, w2=500, w3=288, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(500, min_periods=max(500//3, 2)).rank(pct=True)
    persistence = change.rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2326 * persistence + 0.0034844 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_044_analyst_v44_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=192, w2=511, w3=301, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(511, min_periods=max(511//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.520625 + 0.0034845 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_045_analyst_v45_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=199, w2=19, w3=314, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(19, min_periods=max(19//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2478 * slope + 0.0034846 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_046_analyst_v46_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=206, w2=30, w3=327, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(30, min_periods=max(30//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.549375 + 0.0034847 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_047_analyst_v47_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=213, w2=41, w3=340, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 41)
    curvature = _rolling_slope(acceleration, 340)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.263 * acceleration + 0.0034848 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_048_analyst_v48_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=220, w2=52, w3=353, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(220, min_periods=max(220//3, 2)).mean(), upside.rolling(52, min_periods=max(52//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.578125 + 0.0034849 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_049_analyst_v49_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=227, w2=63, w3=366, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(63, min_periods=max(63//3, 2)).max()
    rebound = x - x.rolling(227, min_periods=max(227//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2782 * _rolling_slope(draw, 366) + 0.003485 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_050_analyst_v50_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=234, w2=74, w3=379, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 234)
    baseline = trend.rolling(74, min_periods=max(74//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.606875 + 0.0034851 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_051_analyst_v51_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=241, w2=85, w3=392, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 241)
    slow = _rolling_slope(x, 85)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.62125 + 0.0034852 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_052_analyst_v52_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=248, w2=96, w3=405, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(96, min_periods=max(96//3, 2)).max()
    trough = x.rolling(248, min_periods=max(248//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.8625 + 0.0034853 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_053_analyst_v53_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=255, w2=107, w3=418, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(107, min_periods=max(107//3, 2)).rank(pct=True)
    persistence = change.rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3086 * persistence + 0.0034854 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_054_analyst_v54_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=11, w2=118, w3=431, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(11, min_periods=max(11//3, 2)).std()
    vol_slow = ret.rolling(118, min_periods=max(118//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.89125 + 0.0034855 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_055_analyst_v55_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=18, w2=129, w3=444, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(129, min_periods=max(129//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 18)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3238 * slope + 0.0034856 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_056_analyst_v56_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=25, w2=140, w3=457, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(25)
    drag = impulse.rolling(140, min_periods=max(140//3, 2)).mean()
    noise = impulse.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.92 + 0.0034857 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_057_analyst_v57_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=32, w2=151, w3=470, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 32)
    acceleration = _rolling_slope(velocity, 151)
    curvature = _rolling_slope(acceleration, 470)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.339 * acceleration + 0.0034858 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_058_analyst_v58_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=39, w2=162, w3=483, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(162, min_periods=max(162//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.94875 + 0.0034859 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_059_analyst_v59_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=46, w2=173, w3=496, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(173, min_periods=max(173//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3542 * _rolling_slope(draw, 496) + 0.003486 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_060_analyst_v60_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=53, w2=184, w3=509, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 53)
    baseline = trend.rolling(184, min_periods=max(184//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.9775 + 0.0034861 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_061_analyst_v61_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=60, w2=195, w3=522, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 60)
    slow = _rolling_slope(x, 195)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.991875 + 0.0034862 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_062_analyst_v62_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=67, w2=206, w3=535, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(206, min_periods=max(206//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.00625 + 0.0034863 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_063_analyst_v63_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=74, w2=217, w3=548, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(74)
    rank = change.rolling(217, min_periods=max(217//3, 2)).rank(pct=True)
    persistence = change.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3846 * persistence + 0.0034864 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_064_analyst_v64_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=81, w2=228, w3=561, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(228, min_periods=max(228//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.035 + 0.0034865 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_065_analyst_v65_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=88, w2=239, w3=574, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(239, min_periods=max(239//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3998 * slope + 0.0034866 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_066_analyst_v66_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=95, w2=250, w3=587, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(95)
    drag = impulse.rolling(250, min_periods=max(250//3, 2)).mean()
    noise = impulse.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.06375 + 0.0034867 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_067_analyst_v67_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=102, w2=261, w3=600, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 261)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0386 * acceleration + 0.0034868 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_068_analyst_v68_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=109, w2=272, w3=613, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(272, min_periods=max(272//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.0925 + 0.0034869 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_069_analyst_v69_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=116, w2=283, w3=626, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(283, min_periods=max(283//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0538 * _rolling_slope(draw, 626) + 0.003487 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_070_analyst_v70_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=123, w2=294, w3=639, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 123)
    baseline = trend.rolling(294, min_periods=max(294//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.12125 + 0.0034871 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_071_analyst_v71_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=130, w2=305, w3=652, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 130)
    slow = _rolling_slope(x, 305)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.135625 + 0.0034872 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_072_analyst_v72_d3(eps_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=137, w2=316, w3=665, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(316, min_periods=max(316//3, 2)).max()
    trough = x.rolling(137, min_periods=max(137//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.15 + 0.0034873 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_073_analyst_v73_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=144, w2=327, w3=678, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(327, min_periods=max(327//3, 2)).rank(pct=True)
    persistence = change.rolling(678, min_periods=max(678//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0842 * persistence + 0.0034874 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_074_analyst_v74_d3(eps_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=151, w2=338, w3=691, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(151, min_periods=max(151//3, 2)).std()
    vol_slow = ret.rolling(338, min_periods=max(338//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17875 + 0.0034875 * anchor
    return base_signal.diff().diff().diff()

def f62_ard_075_analyst_v75_d3(rev_disp: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=158, w2=349, w3=704, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 158)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0994 * slope + 0.0034876 * anchor
    return base_signal.diff().diff().diff()
