"""63 analyst downgrade cluster d1 first derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f63_adc_001_analyst_v1_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=75, w2=99, w3=729, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 99)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.023125 + 0.0035402 * anchor
    return base_signal.diff()

def f63_adc_002_analyst_v2_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=82, w2=110, w3=742, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(110, min_periods=max(110//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0375 + 0.0035403 * anchor
    return base_signal.diff()

def f63_adc_003_analyst_v3_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=89, w2=121, w3=755, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(89)
    rank = change.rolling(121, min_periods=max(121//3, 2)).rank(pct=True)
    persistence = change.rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3482 * persistence + 0.0035404 * anchor
    return base_signal.diff()

def f63_adc_004_analyst_v4_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=96, w2=132, w3=768, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(132, min_periods=max(132//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06625 + 0.0035405 * anchor
    return base_signal.diff()

def f63_adc_005_analyst_v5_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=103, w2=143, w3=24, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(143, min_periods=max(143//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3634 * slope + 0.0035406 * anchor
    return base_signal.diff()

def f63_adc_006_analyst_v6_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=110, w2=154, w3=37, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(110)
    drag = impulse.rolling(154, min_periods=max(154//3, 2)).mean()
    noise = impulse.abs().rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.095 + 0.0035407 * anchor
    return base_signal.diff()

def f63_adc_007_analyst_v7_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=117, w2=165, w3=50, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 165)
    curvature = _rolling_slope(acceleration, 50)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3786 * acceleration + 0.0035408 * anchor
    return base_signal.diff()

def f63_adc_008_analyst_v8_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=124, w2=176, w3=63, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(176, min_periods=max(176//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(63) * 1.12375 + 0.0035409 * anchor
    return base_signal.diff()

def f63_adc_009_analyst_v9_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=131, w2=187, w3=76, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(187, min_periods=max(187//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3938 * _rolling_slope(draw, 76) + 0.003541 * anchor
    return base_signal.diff()

def f63_adc_010_analyst_v10_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=138, w2=198, w3=89, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(198, min_periods=max(198//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(89, min_periods=max(89//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1525 + 0.0035411 * anchor
    return base_signal.diff()

def f63_adc_011_analyst_v11_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=145, w2=209, w3=102, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=102, adjust=False).mean() * 1.166875 + 0.0035412 * anchor
    return base_signal.diff()

def f63_adc_012_analyst_v12_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=152, w2=220, w3=115, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(220, min_periods=max(220//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.18125 + 0.0035413 * anchor
    return base_signal.diff()

def f63_adc_013_analyst_v13_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=159, w2=231, w3=128, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(231, min_periods=max(231//3, 2)).rank(pct=True)
    persistence = change.rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0478 * persistence + 0.0035414 * anchor
    return base_signal.diff()

def f63_adc_014_analyst_v14_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=166, w2=242, w3=141, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(242, min_periods=max(242//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.21 + 0.0035415 * anchor
    return base_signal.diff()

def f63_adc_015_analyst_v15_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=173, w2=253, w3=154, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(253, min_periods=max(253//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.063 * slope + 0.0035416 * anchor
    return base_signal.diff()

def f63_adc_016_analyst_v16_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=180, w2=264, w3=167, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(264, min_periods=max(264//3, 2)).mean()
    noise = impulse.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.23875 + 0.0035417 * anchor
    return base_signal.diff()

def f63_adc_017_analyst_v17_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=187, w2=275, w3=180, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 275)
    curvature = _rolling_slope(acceleration, 180)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0782 * acceleration + 0.0035418 * anchor
    return base_signal.diff()

def f63_adc_018_analyst_v18_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=194, w2=286, w3=193, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(286, min_periods=max(286//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2675 + 0.0035419 * anchor
    return base_signal.diff()

def f63_adc_019_analyst_v19_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=201, w2=297, w3=206, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(297, min_periods=max(297//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0934 * _rolling_slope(draw, 206) + 0.003542 * anchor
    return base_signal.diff()

def f63_adc_020_analyst_v20_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=208, w2=308, w3=219, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(308, min_periods=max(308//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.29625 + 0.0035421 * anchor
    return base_signal.diff()

def f63_adc_021_analyst_v21_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=215, w2=319, w3=232, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 319)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=232, adjust=False).mean() * 1.310625 + 0.0035422 * anchor
    return base_signal.diff()

def f63_adc_022_analyst_v22_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=222, w2=330, w3=245, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.325 + 0.0035423 * anchor
    return base_signal.diff()

def f63_adc_023_analyst_v23_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=229, w2=341, w3=258, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(341, min_periods=max(341//3, 2)).rank(pct=True)
    persistence = change.rolling(258, min_periods=max(258//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1238 * persistence + 0.0035424 * anchor
    return base_signal.diff()

def f63_adc_024_analyst_v24_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=236, w2=352, w3=271, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(352, min_periods=max(352//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.35375 + 0.0035425 * anchor
    return base_signal.diff()

def f63_adc_025_analyst_v25_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=243, w2=363, w3=284, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(363, min_periods=max(363//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.139 * slope + 0.0035426 * anchor
    return base_signal.diff()

def f63_adc_026_analyst_v26_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=250, w2=374, w3=297, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(374, min_periods=max(374//3, 2)).mean()
    noise = impulse.abs().rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3825 + 0.0035427 * anchor
    return base_signal.diff()

def f63_adc_027_analyst_v27_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=6, w2=385, w3=310, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 385)
    curvature = _rolling_slope(acceleration, 310)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1542 * acceleration + 0.0035428 * anchor
    return base_signal.diff()

def f63_adc_028_analyst_v28_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=13, w2=396, w3=323, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(396, min_periods=max(396//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.41125 + 0.0035429 * anchor
    return base_signal.diff()

def f63_adc_029_analyst_v29_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=20, w2=407, w3=336, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(407, min_periods=max(407//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1694 * _rolling_slope(draw, 336) + 0.003543 * anchor
    return base_signal.diff()

def f63_adc_030_analyst_v30_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=27, w2=418, w3=349, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(418, min_periods=max(418//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.44 + 0.0035431 * anchor
    return base_signal.diff()

def f63_adc_031_analyst_v31_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=34, w2=429, w3=362, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 429)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.454375 + 0.0035432 * anchor
    return base_signal.diff()

def f63_adc_032_analyst_v32_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=41, w2=440, w3=375, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.46875 + 0.0035433 * anchor
    return base_signal.diff()

def f63_adc_033_analyst_v33_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=48, w2=451, w3=388, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(48)
    rank = change.rolling(451, min_periods=max(451//3, 2)).rank(pct=True)
    persistence = change.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1998 * persistence + 0.0035434 * anchor
    return base_signal.diff()

def f63_adc_034_analyst_v34_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=55, w2=462, w3=401, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4975 + 0.0035435 * anchor
    return base_signal.diff()

def f63_adc_035_analyst_v35_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=62, w2=473, w3=414, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(473, min_periods=max(473//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.215 * slope + 0.0035436 * anchor
    return base_signal.diff()

def f63_adc_036_analyst_v36_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=69, w2=484, w3=427, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(69)
    drag = impulse.rolling(484, min_periods=max(484//3, 2)).mean()
    noise = impulse.abs().rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.52625 + 0.0035437 * anchor
    return base_signal.diff()

def f63_adc_037_analyst_v37_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=76, w2=495, w3=440, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 495)
    curvature = _rolling_slope(acceleration, 440)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2302 * acceleration + 0.0035438 * anchor
    return base_signal.diff()

def f63_adc_038_analyst_v38_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=83, w2=506, w3=453, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(506, min_periods=max(506//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.555 + 0.0035439 * anchor
    return base_signal.diff()

def f63_adc_039_analyst_v39_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=90, w2=14, w3=466, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(14, min_periods=max(14//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2454 * _rolling_slope(draw, 466) + 0.003544 * anchor
    return base_signal.diff()

def f63_adc_040_analyst_v40_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=97, w2=25, w3=479, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(25, min_periods=max(25//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.58375 + 0.0035441 * anchor
    return base_signal.diff()

def f63_adc_041_analyst_v41_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=104, w2=36, w3=492, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 36)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.598125 + 0.0035442 * anchor
    return base_signal.diff()

def f63_adc_042_analyst_v42_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=111, w2=47, w3=505, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(47, min_periods=max(47//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6125 + 0.0035443 * anchor
    return base_signal.diff()

def f63_adc_043_analyst_v43_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=118, w2=58, w3=518, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(118)
    rank = change.rolling(58, min_periods=max(58//3, 2)).rank(pct=True)
    persistence = change.rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2758 * persistence + 0.0035444 * anchor
    return base_signal.diff()

def f63_adc_044_analyst_v44_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=125, w2=69, w3=531, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(69, min_periods=max(69//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.868125 + 0.0035445 * anchor
    return base_signal.diff()

def f63_adc_045_analyst_v45_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=132, w2=80, w3=544, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(80, min_periods=max(80//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.291 * slope + 0.0035446 * anchor
    return base_signal.diff()

def f63_adc_046_analyst_v46_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=139, w2=91, w3=557, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(91, min_periods=max(91//3, 2)).mean()
    noise = impulse.abs().rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.896875 + 0.0035447 * anchor
    return base_signal.diff()

def f63_adc_047_analyst_v47_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=146, w2=102, w3=570, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 102)
    curvature = _rolling_slope(acceleration, 570)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3062 * acceleration + 0.0035448 * anchor
    return base_signal.diff()

def f63_adc_048_analyst_v48_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=153, w2=113, w3=583, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(113, min_periods=max(113//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.925625 + 0.0035449 * anchor
    return base_signal.diff()

def f63_adc_049_analyst_v49_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=160, w2=124, w3=596, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(124, min_periods=max(124//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3214 * _rolling_slope(draw, 596) + 0.003545 * anchor
    return base_signal.diff()

def f63_adc_050_analyst_v50_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=167, w2=135, w3=609, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(135, min_periods=max(135//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.954375 + 0.0035451 * anchor
    return base_signal.diff()

def f63_adc_051_analyst_v51_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=174, w2=146, w3=622, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 146)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.96875 + 0.0035452 * anchor
    return base_signal.diff()

def f63_adc_052_analyst_v52_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=181, w2=157, w3=635, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(157, min_periods=max(157//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.983125 + 0.0035453 * anchor
    return base_signal.diff()

def f63_adc_053_analyst_v53_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=188, w2=168, w3=648, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(168, min_periods=max(168//3, 2)).rank(pct=True)
    persistence = change.rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3518 * persistence + 0.0035454 * anchor
    return base_signal.diff()

def f63_adc_054_analyst_v54_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=195, w2=179, w3=661, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(179, min_periods=max(179//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.011875 + 0.0035455 * anchor
    return base_signal.diff()

def f63_adc_055_analyst_v55_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=202, w2=190, w3=674, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(190, min_periods=max(190//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.367 * slope + 0.0035456 * anchor
    return base_signal.diff()

def f63_adc_056_analyst_v56_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=209, w2=201, w3=687, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(201, min_periods=max(201//3, 2)).mean()
    noise = impulse.abs().rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.040625 + 0.0035457 * anchor
    return base_signal.diff()

def f63_adc_057_analyst_v57_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=216, w2=212, w3=700, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 216)
    acceleration = _rolling_slope(velocity, 212)
    curvature = _rolling_slope(acceleration, 700)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3822 * acceleration + 0.0035458 * anchor
    return base_signal.diff()

def f63_adc_058_analyst_v58_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=223, w2=223, w3=713, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(223, min_periods=max(223//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.069375 + 0.0035459 * anchor
    return base_signal.diff()

def f63_adc_059_analyst_v59_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=230, w2=234, w3=726, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(234, min_periods=max(234//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3974 * _rolling_slope(draw, 726) + 0.003546 * anchor
    return base_signal.diff()

def f63_adc_060_analyst_v60_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=237, w2=245, w3=739, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(245, min_periods=max(245//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.098125 + 0.0035461 * anchor
    return base_signal.diff()

def f63_adc_061_analyst_v61_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=244, w2=256, w3=752, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 256)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1125 + 0.0035462 * anchor
    return base_signal.diff()

def f63_adc_062_analyst_v62_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=251, w2=267, w3=765, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(267, min_periods=max(267//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.126875 + 0.0035463 * anchor
    return base_signal.diff()

def f63_adc_063_analyst_v63_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=7, w2=278, w3=21, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(7)
    rank = change.rolling(278, min_periods=max(278//3, 2)).rank(pct=True)
    persistence = change.rolling(21, min_periods=max(21//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0514 * persistence + 0.0035464 * anchor
    return base_signal.diff()

def f63_adc_064_analyst_v64_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=14, w2=289, w3=34, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(14, min_periods=max(14//3, 2)).std()
    vol_slow = ret.rolling(289, min_periods=max(289//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.155625 + 0.0035465 * anchor
    return base_signal.diff()

def f63_adc_065_analyst_v65_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=21, w2=300, w3=47, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(300, min_periods=max(300//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 21)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0666 * slope + 0.0035466 * anchor
    return base_signal.diff()

def f63_adc_066_analyst_v66_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=28, w2=311, w3=60, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(28)
    drag = impulse.rolling(311, min_periods=max(311//3, 2)).mean()
    noise = impulse.abs().rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.184375 + 0.0035467 * anchor
    return base_signal.diff()

def f63_adc_067_analyst_v67_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=35, w2=322, w3=73, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 35)
    acceleration = _rolling_slope(velocity, 322)
    curvature = _rolling_slope(acceleration, 73)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0818 * acceleration + 0.0035468 * anchor
    return base_signal.diff()

def f63_adc_068_analyst_v68_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=42, w2=333, w3=86, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(86) * 1.213125 + 0.0035469 * anchor
    return base_signal.diff()

def f63_adc_069_analyst_v69_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=49, w2=344, w3=99, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(344, min_periods=max(344//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.097 * _rolling_slope(draw, 99) + 0.003547 * anchor
    return base_signal.diff()

def f63_adc_070_analyst_v70_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=56, w2=355, w3=112, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 56)
    baseline = trend.rolling(355, min_periods=max(355//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.241875 + 0.0035471 * anchor
    return base_signal.diff()

def f63_adc_071_analyst_v71_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=63, w2=366, w3=125, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 63)
    slow = _rolling_slope(x, 366)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=125, adjust=False).mean() * 1.25625 + 0.0035472 * anchor
    return base_signal.diff()

def f63_adc_072_analyst_v72_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=70, w2=377, w3=138, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(377, min_periods=max(377//3, 2)).max()
    trough = x.rolling(70, min_periods=max(70//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.270625 + 0.0035473 * anchor
    return base_signal.diff()

def f63_adc_073_analyst_v73_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=77, w2=388, w3=151, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(77)
    rank = change.rolling(388, min_periods=max(388//3, 2)).rank(pct=True)
    persistence = change.rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1274 * persistence + 0.0035474 * anchor
    return base_signal.diff()

def f63_adc_074_analyst_v74_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=84, w2=399, w3=164, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(84, min_periods=max(84//3, 2)).std()
    vol_slow = ret.rolling(399, min_periods=max(399//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.299375 + 0.0035475 * anchor
    return base_signal.diff()

def f63_adc_075_analyst_v75_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=91, w2=410, w3=177, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 91)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1426 * slope + 0.0035476 * anchor
    return base_signal.diff()
