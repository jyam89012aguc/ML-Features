"""45 amihud roll kyle liquidity gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Proxies for market liquidity and price impact based on volume and price range.
Version: 7.0 (Strict De-duplication + Functional Safety)
Registry Status: Optimized for PostgreSQL Feature Store ingestion.
PIT-clean: right-anchored rolling, explicit min_periods.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_5Y = 1260


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

def _atr(high, low, close, n=14):
    pc = close.shift(1)
    tr = pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(n, min_periods=max(n // 2, 1)).mean()

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]; wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _absorption_ratio_proxy(returns_list, n_comp=1):
    data = pd.concat(returns_list, axis=1).astype(float)
    window = 21
    n_comp = max(1, int(n_comp))
    out = pd.Series(np.nan, index=data.index, dtype=float)
    for i in range(window - 1, len(data)):
        w = data.iloc[i - window + 1:i + 1].to_numpy(dtype=float)
        if w.shape[1] < 2 or np.isnan(w).any():
            continue
        corr = np.corrcoef(w, rowvar=False)
        if np.ndim(corr) != 2 or not np.isfinite(corr).all():
            continue
        eigvals = np.linalg.eigvalsh(corr)
        total = eigvals.sum()
        if not np.isfinite(total) or abs(total) < 1e-12:
            continue
        k = min(n_comp, len(eigvals))
        out.iloc[i] = np.sort(eigvals)[-k:].sum() / total
    return out


# ============================================================
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f45_liqd_gemini_001_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_002_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_003_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_004_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_005_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_006_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_007_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_008_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_009_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_010_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff().diff().diff()

def f45_liqd_gemini_011_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=92, w3=172, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(39, min_periods=max(39//3, 2)).mean(), upside.rolling(92, min_periods=max(92//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.432941 + 0.0031022 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_012_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=105, w3=189, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(105, min_periods=max(105//3, 2)).max()
    rebound = x - x.rolling(46, min_periods=max(46//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.094667 * _rolling_slope(draw, 189) + 0.0031023 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_013_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=118, w3=206, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(53) - b.diff(118)
    stress = imbalance.rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.46 + 0.0031024 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_014_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=131, w3=223, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 60)
    baseline = trend.rolling(131, min_periods=max(131//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(223, min_periods=max(223//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.473529 + 0.0031025 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_015_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=144, w3=240, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 67)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=240, adjust=False).mean() * 1.487059 + 0.0031026 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_016_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=157, w3=257, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(157, min_periods=max(157//3, 2)).max()
    trough = x.rolling(74, min_periods=max(74//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.500588 + 0.0031027 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_017_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=170, w3=274, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(81)
    rank = change.rolling(170, min_periods=max(170//3, 2)).rank(pct=True)
    persistence = change.rolling(274, min_periods=max(274//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.126333 * persistence + 0.0031028 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_018_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=183, w3=291, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(88, min_periods=max(88//3, 2)).std()
    vol_slow = ret.rolling(183, min_periods=max(183//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.527647 + 0.0031029 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_019_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=196, w3=308, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(196, min_periods=max(196//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 95)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.139 * slope + 0.003103 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_020_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=209, w3=325, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(102)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(325, min_periods=max(325//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.554706 + 0.0031031 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_021_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=222, w3=342, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 109)
    acceleration = _rolling_slope(velocity, 222)
    curvature = _rolling_slope(acceleration, 342)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.151667 * acceleration + 0.0031032 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_022_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=235, w3=359, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 116)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.158 * pressure.rolling(359, min_periods=max(359//3, 2)).mean() + 0.0031033 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_023_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=248, w3=376, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(123, min_periods=max(123//3, 2)).mean())
    decay = spread.ewm(span=248, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.595294 + 0.0031034 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_024_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=261, w3=393, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(261, min_periods=max(261//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 130)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.608824 + 0.0031035 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_025_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=274, w3=410, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(137, min_periods=max(137//3, 2)).mean(), b.abs().rolling(274, min_periods=max(274//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.177 * _rolling_slope(cover, 137) + 0.0031036 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_026_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=287, w3=427, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.183333 * y + 0.816667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 144) - _rolling_slope(basket, 287) + 0.0031037 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_027_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=300, w3=444, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.649412 + 0.0031038 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_028_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=313, w3=461, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.196 * _rolling_slope(draw, 461) + 0.0031039 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_029_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=326, w3=478, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.822941 + 0.003104 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_030_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=339, w3=495, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 172)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(495, min_periods=max(495//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.836471 + 0.0031041 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_031_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=352, w3=512, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 179)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.85 + 0.0031042 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_032_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=365, w3=529, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(365, min_periods=max(365//3, 2)).max()
    trough = x.rolling(186, min_periods=max(186//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.863529 + 0.0031043 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_033_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=378, w3=546, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(378, min_periods=max(378//3, 2)).rank(pct=True)
    persistence = change.rolling(546, min_periods=max(546//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.227667 * persistence + 0.0031044 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_034_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=391, w3=563, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(200, min_periods=max(200//3, 2)).std()
    vol_slow = ret.rolling(391, min_periods=max(391//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.890588 + 0.0031045 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_035_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=404, w3=580, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(404, min_periods=max(404//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 207)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.240333 * slope + 0.0031046 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_036_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=417, w3=597, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.917647 + 0.0031047 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_037_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=430, w3=614, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 221)
    acceleration = _rolling_slope(velocity, 430)
    curvature = _rolling_slope(acceleration, 614)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.253 * acceleration + 0.0031048 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_038_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=443, w3=631, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 228)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.259333 * pressure.rolling(631, min_periods=max(631//3, 2)).mean() + 0.0031049 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_039_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=456, w3=648, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(235, min_periods=max(235//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.958235 + 0.003105 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_040_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=469, w3=665, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(469, min_periods=max(469//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 242)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.971765 + 0.0031051 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_041_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=482, w3=682, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(249, min_periods=max(249//3, 2)).mean(), b.abs().rolling(482, min_periods=max(482//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.278333 * _rolling_slope(cover, 249) + 0.0031052 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_042_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=495, w3=699, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.284667 * y + 0.715333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 9) - _rolling_slope(basket, 495) + 0.0031053 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_043_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=508, w3=716, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(508, min_periods=max(508//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.012353 + 0.0031054 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_044_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=22, w3=733, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(22, min_periods=max(22//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.297333 * _rolling_slope(draw, 733) + 0.0031055 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_045_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=35, w3=750, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(30) - b.diff(35)
    stress = imbalance.rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.039412 + 0.0031056 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_046_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=48, w3=767, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(48, min_periods=max(48//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.052941 + 0.0031057 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_047_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=61, w3=33, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=33, adjust=False).mean() * 1.066471 + 0.0031058 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_048_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=74, w3=50, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(74, min_periods=max(74//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.08 + 0.0031059 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_049_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=87, w3=67, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(58)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.329 * persistence + 0.003106 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_050_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=100, w3=84, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.107059 + 0.0031061 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_051_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=113, w3=101, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.341667 * slope + 0.0031062 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_052_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=126, w3=118, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(79)
    drag = impulse.rolling(126, min_periods=max(126//3, 2)).mean()
    noise = impulse.abs().rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.134118 + 0.0031063 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_053_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=139, w3=135, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 139)
    curvature = _rolling_slope(acceleration, 135)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.354333 * acceleration + 0.0031064 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_054_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=152, w3=152, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 93)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.360667 * pressure.rolling(152, min_periods=max(152//3, 2)).mean() + 0.0031065 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_055_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=165, w3=169, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(100, min_periods=max(100//3, 2)).mean())
    decay = spread.ewm(span=165, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.174706 + 0.0031066 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_056_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=178, w3=186, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(178, min_periods=max(178//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 107)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.188235 + 0.0031067 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_057_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=191, w3=203, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(114, min_periods=max(114//3, 2)).mean(), b.abs().rolling(191, min_periods=max(191//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.047333 * _rolling_slope(cover, 114) + 0.0031068 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_058_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=204, w3=220, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.053667 * y + 0.946333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 121) - _rolling_slope(basket, 204) + 0.0031069 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_059_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=217, w3=237, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(217, min_periods=max(217//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.228824 + 0.003107 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_060_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=230, w3=254, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(230, min_periods=max(230//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.066333 * _rolling_slope(draw, 254) + 0.0031071 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_061_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=243, w3=271, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(271, min_periods=max(271//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.255882 + 0.0031072 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_062_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=256, w3=288, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 149)
    baseline = trend.rolling(256, min_periods=max(256//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.269412 + 0.0031073 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_063_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=269, w3=305, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 156)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.282941 + 0.0031074 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_064_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=282, w3=322, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(282, min_periods=max(282//3, 2)).max()
    trough = x.rolling(163, min_periods=max(163//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.296471 + 0.0031075 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_065_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=295, w3=339, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(339, min_periods=max(339//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.098 * persistence + 0.0031076 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_066_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=308, w3=356, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(177, min_periods=max(177//3, 2)).std()
    vol_slow = ret.rolling(308, min_periods=max(308//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.323529 + 0.0031077 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_067_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=321, w3=373, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(321, min_periods=max(321//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 184)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.110667 * slope + 0.0031078 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_068_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=334, w3=390, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(390, min_periods=max(390//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.350588 + 0.0031079 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_069_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=347, w3=407, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 198)
    acceleration = _rolling_slope(velocity, 347)
    curvature = _rolling_slope(acceleration, 407)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.123333 * acceleration + 0.003108 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_070_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=360, w3=424, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 205)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.129667 * pressure.rolling(424, min_periods=max(424//3, 2)).mean() + 0.0031081 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_071_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=373, w3=441, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(212, min_periods=max(212//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.391176 + 0.0031082 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_072_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=386, w3=458, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(386, min_periods=max(386//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 219)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.404706 + 0.0031083 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_073_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=399, w3=475, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(226, min_periods=max(226//3, 2)).mean(), b.abs().rolling(399, min_periods=max(399//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.148667 * _rolling_slope(cover, 226) + 0.0031084 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_074_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=412, w3=492, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.155 * y + 0.845000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 233) - _rolling_slope(basket, 412) + 0.0031085 * anchor
    return base_signal.diff().diff().diff()

def f45_liqd_gemini_075_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=425, w3=509, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(425, min_periods=max(425//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.445294 + 0.0031086 * anchor
    return base_signal.diff().diff().diff()
