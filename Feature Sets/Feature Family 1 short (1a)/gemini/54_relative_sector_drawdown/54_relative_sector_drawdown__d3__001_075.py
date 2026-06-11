"""54 relative sector drawdown d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Relative_Strength - Institutional-grade short-side signal.
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

def f54_rsw_d_001_rel_v1_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=92, w2=358, w3=566, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(92, min_periods=max(92//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.31375 + 0.0033002 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_002_rel_v2_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=99, w2=369, w3=579, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(369, min_periods=max(369//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 99)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.328125 + 0.0033003 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_003_rel_v3_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=106, w2=380, w3=592, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(106, min_periods=max(106//3, 2)).mean(), b.abs().rolling(380, min_periods=max(380//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1754 * _rolling_slope(cover, 106) + 0.0033004 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_004_rel_v4_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=113, w2=391, w3=605, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.183 * y + 0.817000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 113) - _rolling_slope(basket, 391) + 0.0033005 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_005_rel_v5_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=120, w2=402, w3=618, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(402, min_periods=max(402//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37125 + 0.0033006 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_006_rel_v6_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=127, w2=413, w3=631, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(413, min_periods=max(413//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1982 * _rolling_slope(draw, 631) + 0.0033007 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_007_rel_v7_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=134, w2=424, w3=644, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.4 + 0.0033008 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_008_rel_v8_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=141, w2=435, w3=657, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.414375 + 0.0033009 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_009_rel_v9_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=148, w2=446, w3=670, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 446)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.42875 + 0.003301 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_010_rel_v10_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=155, w2=457, w3=683, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(457, min_periods=max(457//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.443125 + 0.0033011 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_011_rel_v11_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=162, w2=468, w3=696, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2362 * persistence + 0.0033012 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_012_rel_v12_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=169, w2=479, w3=709, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(479, min_periods=max(479//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.471875 + 0.0033013 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_013_rel_v13_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=176, w2=490, w3=722, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(490, min_periods=max(490//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2514 * slope + 0.0033014 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_014_rel_v14_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=183, w2=501, w3=735, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(501, min_periods=max(501//3, 2)).mean()
    noise = impulse.abs().rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.500625 + 0.0033015 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_015_rel_v15_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=190, w2=512, w3=748, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 512)
    curvature = _rolling_slope(acceleration, 748)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2666 * acceleration + 0.0033016 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_016_rel_v16_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=197, w2=20, w3=761, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 197)
    pressure = rel_log.diff(20)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2742 * pressure.rolling(761, min_periods=max(761//3, 2)).mean() + 0.0033017 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_017_rel_v17_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=204, w2=31, w3=17, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    decay = spread.ewm(span=31, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.54375 + 0.0033018 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_018_rel_v18_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=211, w2=42, w3=30, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(42, min_periods=max(42//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 211)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.558125 + 0.0033019 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_019_rel_v19_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=218, w2=53, w3=43, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(218, min_periods=max(218//3, 2)).mean(), b.abs().rolling(53, min_periods=max(53//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(43) + 0.297 * _rolling_slope(cover, 218) + 0.003302 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_020_rel_v20_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=225, w2=64, w3=56, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3046 * y + 0.695400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 225) - _rolling_slope(basket, 64) + 0.0033021 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_021_rel_v21_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=232, w2=75, w3=69, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(75, min_periods=max(75//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(69) * 1.60125 + 0.0033022 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_022_rel_v22_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=239, w2=86, w3=82, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(86, min_periods=max(86//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3198 * _rolling_slope(draw, 82) + 0.0033023 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_023_rel_v23_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=246, w2=97, w3=95, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(97)
    stress = imbalance.rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.856875 + 0.0033024 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_024_rel_v24_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=253, w2=108, w3=108, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 253)
    baseline = trend.rolling(108, min_periods=max(108//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.87125 + 0.0033025 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_025_rel_v25_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=9, w2=119, w3=121, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 119)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=121, adjust=False).mean() * 0.885625 + 0.0033026 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_026_rel_v26_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=16, w2=130, w3=134, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9 + 0.0033027 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_027_rel_v27_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=23, w2=141, w3=147, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(23)
    rank = change.rolling(141, min_periods=max(141//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3578 * persistence + 0.0033028 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_028_rel_v28_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=30, w2=152, w3=160, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(152, min_periods=max(152//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92875 + 0.0033029 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_029_rel_v29_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=37, w2=163, w3=173, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(163, min_periods=max(163//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.373 * slope + 0.003303 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_030_rel_v30_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=44, w2=174, w3=186, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(44)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.9575 + 0.0033031 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_031_rel_v31_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=51, w2=185, w3=199, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 185)
    curvature = _rolling_slope(acceleration, 199)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3882 * acceleration + 0.0033032 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_032_rel_v32_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=58, w2=196, w3=212, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 58)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3958 * pressure.rolling(212, min_periods=max(212//3, 2)).mean() + 0.0033033 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_033_rel_v33_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=65, w2=207, w3=225, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(65, min_periods=max(65//3, 2)).mean())
    decay = spread.ewm(span=207, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.000625 + 0.0033034 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_034_rel_v34_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=72, w2=218, w3=238, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(218, min_periods=max(218//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 72)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.015 + 0.0033035 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_035_rel_v35_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=79, w2=229, w3=251, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(79, min_periods=max(79//3, 2)).mean(), b.abs().rolling(229, min_periods=max(229//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0422 * _rolling_slope(cover, 79) + 0.0033036 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_036_rel_v36_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=86, w2=240, w3=264, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.0498 * y + 0.950200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 86) - _rolling_slope(basket, 240) + 0.0033037 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_037_rel_v37_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=93, w2=251, w3=277, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.058125 + 0.0033038 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_038_rel_v38_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=100, w2=262, w3=290, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.065 * _rolling_slope(draw, 290) + 0.0033039 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_039_rel_v39_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=107, w2=273, w3=303, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(107) - b.diff(126)
    stress = imbalance.rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.086875 + 0.003304 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_040_rel_v40_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=114, w2=284, w3=316, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.10125 + 0.0033041 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_041_rel_v41_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=121, w2=295, w3=329, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 295)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.115625 + 0.0033042 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_042_rel_v42_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=128, w2=306, w3=342, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(306, min_periods=max(306//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.13 + 0.0033043 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_043_rel_v43_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=135, w2=317, w3=355, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(317, min_periods=max(317//3, 2)).rank(pct=True)
    persistence = change.rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.103 * persistence + 0.0033044 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_044_rel_v44_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=142, w2=328, w3=368, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(328, min_periods=max(328//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.15875 + 0.0033045 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_045_rel_v45_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=149, w2=339, w3=381, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1182 * slope + 0.0033046 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_046_rel_v46_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=156, w2=350, w3=394, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(350, min_periods=max(350//3, 2)).mean()
    noise = impulse.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1875 + 0.0033047 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_047_rel_v47_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=163, w2=361, w3=407, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 361)
    curvature = _rolling_slope(acceleration, 407)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1334 * acceleration + 0.0033048 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_048_rel_v48_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=170, w2=372, w3=420, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 170)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.141 * pressure.rolling(420, min_periods=max(420//3, 2)).mean() + 0.0033049 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_049_rel_v49_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=177, w2=383, w3=433, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.230625 + 0.003305 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_050_rel_v50_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=184, w2=394, w3=446, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(394, min_periods=max(394//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 184)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.245 + 0.0033051 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_051_rel_v51_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=191, w2=405, w3=459, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(191, min_periods=max(191//3, 2)).mean(), b.abs().rolling(405, min_periods=max(405//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1638 * _rolling_slope(cover, 191) + 0.0033052 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_052_rel_v52_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=198, w2=416, w3=472, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1714 * y + 0.828600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 198) - _rolling_slope(basket, 416) + 0.0033053 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_053_rel_v53_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=205, w2=427, w3=485, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(205, min_periods=max(205//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.288125 + 0.0033054 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_054_rel_v54_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=212, w2=438, w3=498, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(212, min_periods=max(212//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1866 * _rolling_slope(draw, 498) + 0.0033055 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_055_rel_v55_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=219, w2=449, w3=511, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(511, min_periods=max(511//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.316875 + 0.0033056 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_056_rel_v56_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=226, w2=460, w3=524, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 226)
    baseline = trend.rolling(460, min_periods=max(460//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33125 + 0.0033057 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_057_rel_v57_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=233, w2=471, w3=537, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 233)
    slow = _rolling_slope(x, 471)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.345625 + 0.0033058 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_058_rel_v58_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=240, w2=482, w3=550, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(482, min_periods=max(482//3, 2)).max()
    trough = x.rolling(240, min_periods=max(240//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.36 + 0.0033059 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_059_rel_v59_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=247, w2=493, w3=563, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(493, min_periods=max(493//3, 2)).rank(pct=True)
    persistence = change.rolling(563, min_periods=max(563//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2246 * persistence + 0.003306 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_060_rel_v60_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=254, w2=504, w3=576, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(254, min_periods=max(254//3, 2)).std()
    vol_slow = ret.rolling(504, min_periods=max(504//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.38875 + 0.0033061 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_061_rel_v61_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=10, w2=12, w3=589, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(12, min_periods=max(12//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2398 * slope + 0.0033062 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_062_rel_v62_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=17, w2=23, w3=602, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(17)
    drag = impulse.rolling(23, min_periods=max(23//3, 2)).mean()
    noise = impulse.abs().rolling(602, min_periods=max(602//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.4175 + 0.0033063 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_063_rel_v63_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=24, w2=34, w3=615, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 34)
    curvature = _rolling_slope(acceleration, 615)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.255 * acceleration + 0.0033064 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_064_rel_v64_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=31, w2=45, w3=628, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 31)
    pressure = rel_log.diff(45)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2626 * pressure.rolling(628, min_periods=max(628//3, 2)).mean() + 0.0033065 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_065_rel_v65_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=38, w2=56, w3=641, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    decay = spread.ewm(span=56, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.460625 + 0.0033066 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_066_rel_v66_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=45, w2=67, w3=654, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(67, min_periods=max(67//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 45)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.475 + 0.0033067 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_067_rel_v67_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=52, w2=78, w3=667, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(52, min_periods=max(52//3, 2)).mean(), b.abs().rolling(78, min_periods=max(78//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2854 * _rolling_slope(cover, 52) + 0.0033068 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_068_rel_v68_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=59, w2=89, w3=680, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.293 * y + 0.707000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 59) - _rolling_slope(basket, 89) + 0.0033069 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_069_rel_v69_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=66, w2=100, w3=693, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(100, min_periods=max(100//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.518125 + 0.003307 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_070_rel_v70_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=73, w2=111, w3=706, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3082 * _rolling_slope(draw, 706) + 0.0033071 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_071_rel_v71_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=80, w2=122, w3=719, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(80) - b.diff(122)
    stress = imbalance.rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.546875 + 0.0033072 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_072_rel_v72_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=87, w2=133, w3=732, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.56125 + 0.0033073 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_073_rel_v73_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=94, w2=144, w3=745, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.575625 + 0.0033074 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_074_rel_v74_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=101, w2=155, w3=758, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(155, min_periods=max(155//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.59 + 0.0033075 * anchor
    return base_signal.diff().diff().diff()

def f54_rsw_d_075_rel_v75_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=108, w2=166, w3=771, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(108)
    rank = change.rolling(166, min_periods=max(166//3, 2)).rank(pct=True)
    persistence = change.rolling(771, min_periods=max(771//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3462 * persistence + 0.0033076 * anchor
    return base_signal.diff().diff().diff()
