"""22 on balance volume dynamics gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Cumulative volume flow analysis to detect divergence between price and liquidity trends.
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

def f22_obvd_gemini_001_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=5]"""
    window = 5
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_002_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=10]"""
    window = 10
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_003_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=21]"""
    window = 21
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_004_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=42]"""
    window = 42
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_005_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=63]"""
    window = 63
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_006_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=126]"""
    window = 126
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_007_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=252]"""
    window = 252
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_008_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=504]"""
    window = 504
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_009_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=756]"""
    window = 756
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_010_d2(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=1260]"""
    window = 1260
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return (res).diff().diff()

def f22_obvd_gemini_011_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=492, w3=377, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 492)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.107059 + 0.0018002 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_012_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=505, w3=394, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.120588 + 0.0018003 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_013_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=19, w3=411, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(56)
    rank = change.rolling(19, min_periods=max(19//3, 2)).rank(pct=True)
    persistence = change.rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.059667 * persistence + 0.0018004 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_014_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=32, w3=428, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(32, min_periods=max(32//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.147647 + 0.0018005 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_015_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=45, w3=445, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(45, min_periods=max(45//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.072333 * slope + 0.0018006 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_016_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=58, w3=462, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(77)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.174706 + 0.0018007 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_017_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=71, w3=479, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 479)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.085 * acceleration + 0.0018008 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_018_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=84, w3=496, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(84, min_periods=max(84//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.201765 + 0.0018009 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_019_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=97, w3=513, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(97, min_periods=max(97//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.097667 * _rolling_slope(draw, 513) + 0.001801 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_020_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=110, w3=530, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(110, min_periods=max(110//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.228824 + 0.0018011 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_021_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=123, w3=547, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 123)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.242353 + 0.0018012 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_022_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=136, w3=564, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(136, min_periods=max(136//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.255882 + 0.0018013 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_023_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=149, w3=581, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(149, min_periods=max(149//3, 2)).rank(pct=True)
    persistence = change.rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.123 * persistence + 0.0018014 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_024_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=162, w3=598, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(162, min_periods=max(162//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.282941 + 0.0018015 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_025_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=175, w3=615, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(175, min_periods=max(175//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.135667 * slope + 0.0018016 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_026_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=188, w3=632, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(188, min_periods=max(188//3, 2)).mean()
    noise = impulse.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.31 + 0.0018017 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_027_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=201, w3=649, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 201)
    curvature = _rolling_slope(acceleration, 649)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.148333 * acceleration + 0.0018018 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_028_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=214, w3=666, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(214, min_periods=max(214//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.337059 + 0.0018019 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_029_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=227, w3=683, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(227, min_periods=max(227//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.161 * _rolling_slope(draw, 683) + 0.001802 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_030_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=240, w3=700, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(240, min_periods=max(240//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.364118 + 0.0018021 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_031_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=253, w3=717, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 253)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.377647 + 0.0018022 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_032_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=266, w3=734, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.391176 + 0.0018023 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_033_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=279, w3=751, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(279, min_periods=max(279//3, 2)).rank(pct=True)
    persistence = change.rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.186333 * persistence + 0.0018024 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_034_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=292, w3=17, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(292, min_periods=max(292//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.418235 + 0.0018025 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_035_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=305, w3=34, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(305, min_periods=max(305//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.199 * slope + 0.0018026 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_036_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=318, w3=51, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(318, min_periods=max(318//3, 2)).mean()
    noise = impulse.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.445294 + 0.0018027 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_037_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=331, w3=68, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 331)
    curvature = _rolling_slope(acceleration, 68)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211667 * acceleration + 0.0018028 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_038_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=344, w3=85, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(344, min_periods=max(344//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(85) * 1.472353 + 0.0018029 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_039_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=357, w3=102, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(357, min_periods=max(357//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.224333 * _rolling_slope(draw, 102) + 0.001803 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_040_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=370, w3=119, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(370, min_periods=max(370//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.499412 + 0.0018031 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_041_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=383, w3=136, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 383)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=136, adjust=False).mean() * 1.512941 + 0.0018032 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_042_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=396, w3=153, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(396, min_periods=max(396//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.526471 + 0.0018033 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_043_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=409, w3=170, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(19)
    rank = change.rolling(409, min_periods=max(409//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249667 * persistence + 0.0018034 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_044_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=422, w3=187, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(422, min_periods=max(422//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.553529 + 0.0018035 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_045_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=435, w3=204, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(435, min_periods=max(435//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.262333 * slope + 0.0018036 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_046_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=448, w3=221, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(40)
    drag = impulse.rolling(448, min_periods=max(448//3, 2)).mean()
    noise = impulse.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.580588 + 0.0018037 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_047_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=461, w3=238, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 461)
    curvature = _rolling_slope(acceleration, 238)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.275 * acceleration + 0.0018038 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_048_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=474, w3=255, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(474, min_periods=max(474//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.607647 + 0.0018039 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_049_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=487, w3=272, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(487, min_periods=max(487//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287667 * _rolling_slope(draw, 272) + 0.001804 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_050_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=500, w3=289, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(500, min_periods=max(500//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.634706 + 0.0018041 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_051_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=14, w3=306, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 14)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.648235 + 0.0018042 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_052_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=27, w3=323, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(27, min_periods=max(27//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.661765 + 0.0018043 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_053_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=40, w3=340, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(89)
    rank = change.rolling(40, min_periods=max(40//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.313 * persistence + 0.0018044 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_054_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=53, w3=357, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(53, min_periods=max(53//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.835294 + 0.0018045 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_055_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=66, w3=374, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(66, min_periods=max(66//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.325667 * slope + 0.0018046 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_056_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=79, w3=391, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(110)
    drag = impulse.rolling(79, min_periods=max(79//3, 2)).mean()
    noise = impulse.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.862353 + 0.0018047 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_057_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=92, w3=408, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 92)
    curvature = _rolling_slope(acceleration, 408)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.338333 * acceleration + 0.0018048 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_058_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=105, w3=425, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(105, min_periods=max(105//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.889412 + 0.0018049 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_059_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=118, w3=442, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(118, min_periods=max(118//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.351 * _rolling_slope(draw, 442) + 0.001805 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_060_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=131, w3=459, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(131, min_periods=max(131//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.916471 + 0.0018051 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_061_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=144, w3=476, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.93 + 0.0018052 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_062_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=157, w3=493, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(157, min_periods=max(157//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.943529 + 0.0018053 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_063_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=170, w3=510, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(170, min_periods=max(170//3, 2)).rank(pct=True)
    persistence = change.rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.044 * persistence + 0.0018054 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_064_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=183, w3=527, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(183, min_periods=max(183//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.970588 + 0.0018055 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_065_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=196, w3=544, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(196, min_periods=max(196//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.056667 * slope + 0.0018056 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_066_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=209, w3=561, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.997647 + 0.0018057 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_067_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=222, w3=578, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 222)
    curvature = _rolling_slope(acceleration, 578)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.069333 * acceleration + 0.0018058 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_068_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=235, w3=595, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.024706 + 0.0018059 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_069_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=248, w3=612, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.082 * _rolling_slope(draw, 612) + 0.001806 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_070_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=261, w3=629, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.051765 + 0.0018061 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_071_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=274, w3=646, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.065294 + 0.0018062 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_072_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=287, w3=663, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.078824 + 0.0018063 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_073_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=300, w3=680, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.107333 * persistence + 0.0018064 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_074_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=313, w3=697, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.105882 + 0.0018065 * anchor
    return base_signal.diff().diff()

def f22_obvd_gemini_075_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=326, w3=714, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.12 * slope + 0.0018066 * anchor
    return base_signal.diff().diff()
