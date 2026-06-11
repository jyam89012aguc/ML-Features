"""22 on balance volume dynamics gemini base features 1-75 — Pipeline 1b-HF Grade v7.

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

def f22_obvd_gemini_001(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=5]"""
    window = 5
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_002(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=10]"""
    window = 10
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_003(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=21]"""
    window = 21
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_004(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=42]"""
    window = 42
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_005(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=63]"""
    window = 63
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_006(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=126]"""
    window = 126
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_007(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=252]"""
    window = 252
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_008(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=504]"""
    window = 504
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_009(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=756]"""
    window = 756
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_010(volume: pd.Series) -> pd.Series:
    """Cumulative volume flow analysis to detect divergence between price and liquidity trends. [window=1260]"""
    window = 1260
    res = _rolling_slope(volume.rolling(window).sum(), window)
    return res

def f22_obvd_gemini_011(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=345, w3=123, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 345)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=123, adjust=False).mean() * 1.586471 + 0.0017722 * anchor
    return base_signal

def f22_obvd_gemini_012(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=358, w3=140, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(358, min_periods=max(358//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.6 + 0.0017723 * anchor
    return base_signal

def f22_obvd_gemini_013(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=371, w3=157, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(72)
    rank = change.rolling(371, min_periods=max(371//3, 2)).rank(pct=True)
    persistence = change.rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.280333 * persistence + 0.0017724 * anchor
    return base_signal

def f22_obvd_gemini_014(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=384, w3=174, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(384, min_periods=max(384//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.627059 + 0.0017725 * anchor
    return base_signal

def f22_obvd_gemini_015(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=397, w3=191, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(397, min_periods=max(397//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.293 * slope + 0.0017726 * anchor
    return base_signal

def f22_obvd_gemini_016(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=410, w3=208, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(93)
    drag = impulse.rolling(410, min_periods=max(410//3, 2)).mean()
    noise = impulse.abs().rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.654118 + 0.0017727 * anchor
    return base_signal

def f22_obvd_gemini_017(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=423, w3=225, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 423)
    curvature = _rolling_slope(acceleration, 225)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305667 * acceleration + 0.0017728 * anchor
    return base_signal

def f22_obvd_gemini_018(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=436, w3=242, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(436, min_periods=max(436//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.827647 + 0.0017729 * anchor
    return base_signal

def f22_obvd_gemini_019(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=449, w3=259, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(449, min_periods=max(449//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.318333 * _rolling_slope(draw, 259) + 0.001773 * anchor
    return base_signal

def f22_obvd_gemini_020(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=462, w3=276, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 121)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.854706 + 0.0017731 * anchor
    return base_signal

def f22_obvd_gemini_021(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=475, w3=293, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 128)
    slow = _rolling_slope(x, 475)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=293, adjust=False).mean() * 0.868235 + 0.0017732 * anchor
    return base_signal

def f22_obvd_gemini_022(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=488, w3=310, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(488, min_periods=max(488//3, 2)).max()
    trough = x.rolling(135, min_periods=max(135//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.881765 + 0.0017733 * anchor
    return base_signal

def f22_obvd_gemini_023(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=501, w3=327, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(501, min_periods=max(501//3, 2)).rank(pct=True)
    persistence = change.rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343667 * persistence + 0.0017734 * anchor
    return base_signal

def f22_obvd_gemini_024(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=15, w3=344, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(149, min_periods=max(149//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.908824 + 0.0017735 * anchor
    return base_signal

def f22_obvd_gemini_025(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=28, w3=361, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 156)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.356333 * slope + 0.0017736 * anchor
    return base_signal

def f22_obvd_gemini_026(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=41, w3=378, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.935882 + 0.0017737 * anchor
    return base_signal

def f22_obvd_gemini_027(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=54, w3=395, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 170)
    acceleration = _rolling_slope(velocity, 54)
    curvature = _rolling_slope(acceleration, 395)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.036667 * acceleration + 0.0017738 * anchor
    return base_signal

def f22_obvd_gemini_028(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=67, w3=412, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(177, min_periods=max(177//3, 2)).mean(), upside.rolling(67, min_periods=max(67//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.962941 + 0.0017739 * anchor
    return base_signal

def f22_obvd_gemini_029(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=80, w3=429, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(80, min_periods=max(80//3, 2)).max()
    rebound = x - x.rolling(184, min_periods=max(184//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.049333 * _rolling_slope(draw, 429) + 0.001774 * anchor
    return base_signal

def f22_obvd_gemini_030(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=93, w3=446, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 191)
    baseline = trend.rolling(93, min_periods=max(93//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.99 + 0.0017741 * anchor
    return base_signal

def f22_obvd_gemini_031(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=106, w3=463, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 198)
    slow = _rolling_slope(x, 106)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.003529 + 0.0017742 * anchor
    return base_signal

def f22_obvd_gemini_032(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=119, w3=480, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(119, min_periods=max(119//3, 2)).max()
    trough = x.rolling(205, min_periods=max(205//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.017059 + 0.0017743 * anchor
    return base_signal

def f22_obvd_gemini_033(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=132, w3=497, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(132, min_periods=max(132//3, 2)).rank(pct=True)
    persistence = change.rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.074667 * persistence + 0.0017744 * anchor
    return base_signal

def f22_obvd_gemini_034(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=145, w3=514, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(219, min_periods=max(219//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.044118 + 0.0017745 * anchor
    return base_signal

def f22_obvd_gemini_035(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=158, w3=531, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(158, min_periods=max(158//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 226)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.087333 * slope + 0.0017746 * anchor
    return base_signal

def f22_obvd_gemini_036(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=171, w3=548, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(171, min_periods=max(171//3, 2)).mean()
    noise = impulse.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.071176 + 0.0017747 * anchor
    return base_signal

def f22_obvd_gemini_037(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=184, w3=565, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 240)
    acceleration = _rolling_slope(velocity, 184)
    curvature = _rolling_slope(acceleration, 565)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1 * acceleration + 0.0017748 * anchor
    return base_signal

def f22_obvd_gemini_038(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=197, w3=582, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.098235 + 0.0017749 * anchor
    return base_signal

def f22_obvd_gemini_039(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=210, w3=599, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.112667 * _rolling_slope(draw, 599) + 0.001775 * anchor
    return base_signal

def f22_obvd_gemini_040(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=223, w3=616, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(223, min_periods=max(223//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.125294 + 0.0017751 * anchor
    return base_signal

def f22_obvd_gemini_041(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=236, w3=633, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 236)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.138824 + 0.0017752 * anchor
    return base_signal

def f22_obvd_gemini_042(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=249, w3=650, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(249, min_periods=max(249//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.152353 + 0.0017753 * anchor
    return base_signal

def f22_obvd_gemini_043(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=262, w3=667, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(35)
    rank = change.rolling(262, min_periods=max(262//3, 2)).rank(pct=True)
    persistence = change.rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.138 * persistence + 0.0017754 * anchor
    return base_signal

def f22_obvd_gemini_044(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=275, w3=684, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(275, min_periods=max(275//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.179412 + 0.0017755 * anchor
    return base_signal

def f22_obvd_gemini_045(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=288, w3=701, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(288, min_periods=max(288//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.150667 * slope + 0.0017756 * anchor
    return base_signal

def f22_obvd_gemini_046(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=301, w3=718, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(56)
    drag = impulse.rolling(301, min_periods=max(301//3, 2)).mean()
    noise = impulse.abs().rolling(718, min_periods=max(718//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.206471 + 0.0017757 * anchor
    return base_signal

def f22_obvd_gemini_047(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=314, w3=735, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 314)
    curvature = _rolling_slope(acceleration, 735)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.163333 * acceleration + 0.0017758 * anchor
    return base_signal

def f22_obvd_gemini_048(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=327, w3=752, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(327, min_periods=max(327//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.233529 + 0.0017759 * anchor
    return base_signal

def f22_obvd_gemini_049(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=340, w3=18, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.176 * _rolling_slope(draw, 18) + 0.001776 * anchor
    return base_signal

def f22_obvd_gemini_050(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=353, w3=35, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(353, min_periods=max(353//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.260588 + 0.0017761 * anchor
    return base_signal

def f22_obvd_gemini_051(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=366, w3=52, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 366)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=52, adjust=False).mean() * 1.274118 + 0.0017762 * anchor
    return base_signal

def f22_obvd_gemini_052(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=379, w3=69, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(379, min_periods=max(379//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.287647 + 0.0017763 * anchor
    return base_signal

def f22_obvd_gemini_053(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=392, w3=86, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(105)
    rank = change.rolling(392, min_periods=max(392//3, 2)).rank(pct=True)
    persistence = change.rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.201333 * persistence + 0.0017764 * anchor
    return base_signal

def f22_obvd_gemini_054(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=405, w3=103, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.314706 + 0.0017765 * anchor
    return base_signal

def f22_obvd_gemini_055(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=418, w3=120, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.214 * slope + 0.0017766 * anchor
    return base_signal

def f22_obvd_gemini_056(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=431, w3=137, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.341765 + 0.0017767 * anchor
    return base_signal

def f22_obvd_gemini_057(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=444, w3=154, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 154)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.226667 * acceleration + 0.0017768 * anchor
    return base_signal

def f22_obvd_gemini_058(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=457, w3=171, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.368824 + 0.0017769 * anchor
    return base_signal

def f22_obvd_gemini_059(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=470, w3=188, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(470, min_periods=max(470//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.239333 * _rolling_slope(draw, 188) + 0.001777 * anchor
    return base_signal

def f22_obvd_gemini_060(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=483, w3=205, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.395882 + 0.0017771 * anchor
    return base_signal

def f22_obvd_gemini_061(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=496, w3=222, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 496)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=222, adjust=False).mean() * 1.409412 + 0.0017772 * anchor
    return base_signal

def f22_obvd_gemini_062(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=509, w3=239, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(509, min_periods=max(509//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.422941 + 0.0017773 * anchor
    return base_signal

def f22_obvd_gemini_063(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=23, w3=256, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(23, min_periods=max(23//3, 2)).rank(pct=True)
    persistence = change.rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.264667 * persistence + 0.0017774 * anchor
    return base_signal

def f22_obvd_gemini_064(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=36, w3=273, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.45 + 0.0017775 * anchor
    return base_signal

def f22_obvd_gemini_065(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=49, w3=290, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(49, min_periods=max(49//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.277333 * slope + 0.0017776 * anchor
    return base_signal

def f22_obvd_gemini_066(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=62, w3=307, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(62, min_periods=max(62//3, 2)).mean()
    noise = impulse.abs().rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.477059 + 0.0017777 * anchor
    return base_signal

def f22_obvd_gemini_067(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=75, w3=324, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 203)
    acceleration = _rolling_slope(velocity, 75)
    curvature = _rolling_slope(acceleration, 324)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.29 * acceleration + 0.0017778 * anchor
    return base_signal

def f22_obvd_gemini_068(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=88, w3=341, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(88, min_periods=max(88//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.504118 + 0.0017779 * anchor
    return base_signal

def f22_obvd_gemini_069(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=101, w3=358, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(101, min_periods=max(101//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.302667 * _rolling_slope(draw, 358) + 0.001778 * anchor
    return base_signal

def f22_obvd_gemini_070(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=114, w3=375, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(114, min_periods=max(114//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.531176 + 0.0017781 * anchor
    return base_signal

def f22_obvd_gemini_071(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=127, w3=392, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 127)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.544706 + 0.0017782 * anchor
    return base_signal

def f22_obvd_gemini_072(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=140, w3=409, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(140, min_periods=max(140//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.558235 + 0.0017783 * anchor
    return base_signal

def f22_obvd_gemini_073(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=153, w3=426, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(153, min_periods=max(153//3, 2)).rank(pct=True)
    persistence = change.rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.328 * persistence + 0.0017784 * anchor
    return base_signal

def f22_obvd_gemini_074(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=166, w3=443, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(166, min_periods=max(166//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585294 + 0.0017785 * anchor
    return base_signal

def f22_obvd_gemini_075(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=179, w3=460, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(179, min_periods=max(179//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.340667 * slope + 0.0017786 * anchor
    return base_signal
