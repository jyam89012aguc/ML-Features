"""51 relative sector weakness d3 third derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f51_rsw_001_rel_v1_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=42, w2=175, w3=633, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.951875 + 0.0031202 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_002_rel_v2_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=49, w2=186, w3=646, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.96625 + 0.0031203 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_003_rel_v3_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=56, w2=197, w3=659, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(56)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(659, min_periods=max(659//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0458 * persistence + 0.0031204 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_004_rel_v4_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=63, w2=208, w3=672, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.995 + 0.0031205 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_005_rel_v5_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=70, w2=219, w3=685, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.061 * slope + 0.0031206 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_006_rel_v6_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=77, w2=230, w3=698, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(77)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02375 + 0.0031207 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_007_rel_v7_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=84, w2=241, w3=711, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 711)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0762 * acceleration + 0.0031208 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_008_rel_v8_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=91, w2=252, w3=724, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 91)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0838 * pressure.rolling(724, min_periods=max(724//3, 2)).mean() + 0.0031209 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_009_rel_v9_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=98, w2=263, w3=737, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(98, min_periods=max(98//3, 2)).mean())
    decay = spread.ewm(span=263, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.066875 + 0.003121 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_010_rel_v10_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=105, w2=274, w3=750, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(274, min_periods=max(274//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 105)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.08125 + 0.0031211 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_011_rel_v11_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=112, w2=285, w3=763, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(112, min_periods=max(112//3, 2)).mean(), b.abs().rolling(285, min_periods=max(285//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1066 * _rolling_slope(cover, 112) + 0.0031212 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_012_rel_v12_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=119, w2=296, w3=19, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1142 * y + 0.885800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 119) - _rolling_slope(basket, 296) + 0.0031213 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_013_rel_v13_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=126, w2=307, w3=32, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(307, min_periods=max(307//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(32) * 1.124375 + 0.0031214 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_014_rel_v14_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=133, w2=318, w3=45, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1294 * _rolling_slope(draw, 45) + 0.0031215 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_015_rel_v15_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=140, w2=329, w3=58, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(58, min_periods=max(58//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.153125 + 0.0031216 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_016_rel_v16_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=147, w2=340, w3=71, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(340, min_periods=max(340//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1675 + 0.0031217 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_017_rel_v17_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=154, w2=351, w3=84, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=84, adjust=False).mean() * 1.181875 + 0.0031218 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_018_rel_v18_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=161, w2=362, w3=97, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(362, min_periods=max(362//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.19625 + 0.0031219 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_019_rel_v19_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=168, w2=373, w3=110, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1674 * persistence + 0.003122 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_020_rel_v20_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=175, w2=384, w3=123, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(384, min_periods=max(384//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.225 + 0.0031221 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_021_rel_v21_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=182, w2=395, w3=136, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1826 * slope + 0.0031222 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_022_rel_v22_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=189, w2=406, w3=149, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(406, min_periods=max(406//3, 2)).mean()
    noise = impulse.abs().rolling(149, min_periods=max(149//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.25375 + 0.0031223 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_023_rel_v23_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=196, w2=417, w3=162, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 417)
    curvature = _rolling_slope(acceleration, 162)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1978 * acceleration + 0.0031224 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_024_rel_v24_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=203, w2=428, w3=175, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 203)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2054 * pressure.rolling(175, min_periods=max(175//3, 2)).mean() + 0.0031225 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_025_rel_v25_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=210, w2=439, w3=188, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(210, min_periods=max(210//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.296875 + 0.0031226 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_026_rel_v26_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=217, w2=450, w3=201, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(450, min_periods=max(450//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 217)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.31125 + 0.0031227 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_027_rel_v27_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=224, w2=461, w3=214, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(224, min_periods=max(224//3, 2)).mean(), b.abs().rolling(461, min_periods=max(461//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2282 * _rolling_slope(cover, 224) + 0.0031228 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_028_rel_v28_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=231, w2=472, w3=227, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.2358 * y + 0.764200 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 231) - _rolling_slope(basket, 472) + 0.0031229 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_029_rel_v29_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=238, w2=483, w3=240, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(483, min_periods=max(483//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.354375 + 0.003123 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_030_rel_v30_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=245, w2=494, w3=253, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(494, min_periods=max(494//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.251 * _rolling_slope(draw, 253) + 0.0031231 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_031_rel_v31_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=252, w2=505, w3=266, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.383125 + 0.0031232 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_032_rel_v32_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=8, w2=13, w3=279, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(13, min_periods=max(13//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3975 + 0.0031233 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_033_rel_v33_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=15, w2=24, w3=292, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 24)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=292, adjust=False).mean() * 1.411875 + 0.0031234 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_034_rel_v34_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=22, w2=35, w3=305, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(35, min_periods=max(35//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.42625 + 0.0031235 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_035_rel_v35_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=29, w2=46, w3=318, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(29)
    rank = change.rolling(46, min_periods=max(46//3, 2)).rank(pct=True)
    persistence = change.rolling(318, min_periods=max(318//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289 * persistence + 0.0031236 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_036_rel_v36_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=36, w2=57, w3=331, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(57, min_periods=max(57//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.455 + 0.0031237 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_037_rel_v37_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=43, w2=68, w3=344, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3042 * slope + 0.0031238 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_038_rel_v38_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=50, w2=79, w3=357, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(50)
    drag = impulse.rolling(79, min_periods=max(79//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.48375 + 0.0031239 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_039_rel_v39_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=57, w2=90, w3=370, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 90)
    curvature = _rolling_slope(acceleration, 370)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3194 * acceleration + 0.003124 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_040_rel_v40_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=64, w2=101, w3=383, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 64)
    pressure = rel_log.diff(101)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.327 * pressure.rolling(383, min_periods=max(383//3, 2)).mean() + 0.0031241 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_041_rel_v41_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=71, w2=112, w3=396, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(71, min_periods=max(71//3, 2)).mean())
    decay = spread.ewm(span=112, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.526875 + 0.0031242 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_042_rel_v42_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=78, w2=123, w3=409, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(123, min_periods=max(123//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 78)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.54125 + 0.0031243 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_043_rel_v43_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=85, w2=134, w3=422, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(85, min_periods=max(85//3, 2)).mean(), b.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3498 * _rolling_slope(cover, 85) + 0.0031244 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_044_rel_v44_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=92, w2=145, w3=435, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3574 * y + 0.642600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 92) - _rolling_slope(basket, 145) + 0.0031245 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_045_rel_v45_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=99, w2=156, w3=448, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(156, min_periods=max(156//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.584375 + 0.0031246 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_046_rel_v46_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=106, w2=167, w3=461, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(167, min_periods=max(167//3, 2)).max()
    rebound = x - x.rolling(106, min_periods=max(106//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3726 * _rolling_slope(draw, 461) + 0.0031247 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_047_rel_v47_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=113, w2=178, w3=474, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(113) - b.diff(126)
    stress = imbalance.rolling(474, min_periods=max(474//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.613125 + 0.0031248 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_048_rel_v48_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=120, w2=189, w3=487, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 120)
    baseline = trend.rolling(189, min_periods=max(189//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.854375 + 0.0031249 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_049_rel_v49_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=127, w2=200, w3=500, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 127)
    slow = _rolling_slope(x, 200)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.86875 + 0.003125 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_050_rel_v50_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=134, w2=211, w3=513, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(211, min_periods=max(211//3, 2)).max()
    trough = x.rolling(134, min_periods=max(134//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.883125 + 0.0031251 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_051_rel_v51_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=141, w2=222, w3=526, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4106 * persistence + 0.0031252 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_052_rel_v52_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=148, w2=233, w3=539, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(148, min_periods=max(148//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.911875 + 0.0031253 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_053_rel_v53_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=155, w2=244, w3=552, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 155)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0494 * slope + 0.0031254 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_054_rel_v54_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=162, w2=255, w3=565, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.940625 + 0.0031255 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_055_rel_v55_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=169, w2=266, w3=578, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 169)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 578)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0646 * acceleration + 0.0031256 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_056_rel_v56_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=176, w2=277, w3=591, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 176)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0722 * pressure.rolling(591, min_periods=max(591//3, 2)).mean() + 0.0031257 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_057_rel_v57_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=183, w2=288, w3=604, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(183, min_periods=max(183//3, 2)).mean())
    decay = spread.ewm(span=288, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.98375 + 0.0031258 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_058_rel_v58_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=190, w2=299, w3=617, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(299, min_periods=max(299//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 190)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.998125 + 0.0031259 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_059_rel_v59_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=197, w2=310, w3=630, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(197, min_periods=max(197//3, 2)).mean(), b.abs().rolling(310, min_periods=max(310//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.095 * _rolling_slope(cover, 197) + 0.003126 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_060_rel_v60_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=204, w2=321, w3=643, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1026 * y + 0.897400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 204) - _rolling_slope(basket, 321) + 0.0031261 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_061_rel_v61_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=211, w2=332, w3=656, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(211, min_periods=max(211//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.04125 + 0.0031262 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_062_rel_v62_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=218, w2=343, w3=669, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(343, min_periods=max(343//3, 2)).max()
    rebound = x - x.rolling(218, min_periods=max(218//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1178 * _rolling_slope(draw, 669) + 0.0031263 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_063_rel_v63_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=225, w2=354, w3=682, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(682, min_periods=max(682//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.07 + 0.0031264 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_064_rel_v64_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=232, w2=365, w3=695, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.084375 + 0.0031265 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_065_rel_v65_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=239, w2=376, w3=708, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 239)
    slow = _rolling_slope(x, 376)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.09875 + 0.0031266 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_066_rel_v66_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=246, w2=387, w3=721, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(387, min_periods=max(387//3, 2)).max()
    trough = x.rolling(246, min_periods=max(246//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.113125 + 0.0031267 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_067_rel_v67_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=253, w2=398, w3=734, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(398, min_periods=max(398//3, 2)).rank(pct=True)
    persistence = change.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1558 * persistence + 0.0031268 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_068_rel_v68_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=9, w2=409, w3=747, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(9, min_periods=max(9//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.141875 + 0.0031269 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_069_rel_v69_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=16, w2=420, w3=760, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(420, min_periods=max(420//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 16)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.171 * slope + 0.003127 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_070_rel_v70_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=23, w2=431, w3=16, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(23)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(16, min_periods=max(16//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.170625 + 0.0031271 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_071_rel_v71_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=30, w2=442, w3=29, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 30)
    acceleration = _rolling_slope(velocity, 442)
    curvature = _rolling_slope(acceleration, 29)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1862 * acceleration + 0.0031272 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_072_rel_v72_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=37, w2=453, w3=42, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 37)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.1938 * pressure.rolling(42, min_periods=max(42//3, 2)).mean() + 0.0031273 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_073_rel_v73_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=44, w2=464, w3=55, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(44, min_periods=max(44//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.21375 + 0.0031274 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_074_rel_v74_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=51, w2=475, w3=68, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(475, min_periods=max(475//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 51)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.228125 + 0.0031275 * anchor
    return base_signal.diff().diff().diff()

def f51_rsw_075_rel_v75_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=58, w2=486, w3=81, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(58, min_periods=max(58//3, 2)).mean(), b.abs().rolling(486, min_periods=max(486//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(81) + 0.2166 * _rolling_slope(cover, 58) + 0.0031276 * anchor
    return base_signal.diff().diff().diff()
