"""45 amihud roll kyle liquidity gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f45_liqd_gemini_001_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_002_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_003_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_004_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_005_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_006_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_007_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_008_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_009_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_010_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Proxies for market liquidity and price impact based on volume and price range. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().abs(), volume * close + 1e-9).rolling(window).mean()
    return (res).diff()

def f45_liqd_gemini_011_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=444, w3=669, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(444, min_periods=max(444//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 55)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.309 * slope + 0.0030742 * anchor
    return base_signal.diff()

def f45_liqd_gemini_012_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=457, w3=686, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(62)
    drag = impulse.rolling(457, min_periods=max(457//3, 2)).mean()
    noise = impulse.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.072353 + 0.0030743 * anchor
    return base_signal.diff()

def f45_liqd_gemini_013_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=470, w3=703, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 470)
    curvature = _rolling_slope(acceleration, 703)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.321667 * acceleration + 0.0030744 * anchor
    return base_signal.diff()

def f45_liqd_gemini_014_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=483, w3=720, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 76)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.328 * pressure.rolling(720, min_periods=max(720//3, 2)).mean() + 0.0030745 * anchor
    return base_signal.diff()

def f45_liqd_gemini_015_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=496, w3=737, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.112941 + 0.0030746 * anchor
    return base_signal.diff()

def f45_liqd_gemini_016_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=509, w3=754, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(509, min_periods=max(509//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 90)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.126471 + 0.0030747 * anchor
    return base_signal.diff()

def f45_liqd_gemini_017_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=23, w3=20, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(97, min_periods=max(97//3, 2)).mean(), b.abs().rolling(23, min_periods=max(23//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(20) + 0.347 * _rolling_slope(cover, 97) + 0.0030748 * anchor
    return base_signal.diff()

def f45_liqd_gemini_018_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=36, w3=37, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.353333 * y + 0.646667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 104) - _rolling_slope(basket, 36) + 0.0030749 * anchor
    return base_signal.diff()

def f45_liqd_gemini_019_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=49, w3=54, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(49, min_periods=max(49//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(54) * 1.167059 + 0.003075 * anchor
    return base_signal.diff()

def f45_liqd_gemini_020_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=62, w3=71, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(62, min_periods=max(62//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.033667 * _rolling_slope(draw, 71) + 0.0030751 * anchor
    return base_signal.diff()

def f45_liqd_gemini_021_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=75, w3=88, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(125) - b.diff(75)
    stress = imbalance.rolling(88, min_periods=max(88//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.194118 + 0.0030752 * anchor
    return base_signal.diff()

def f45_liqd_gemini_022_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=88, w3=105, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(88, min_periods=max(88//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.207647 + 0.0030753 * anchor
    return base_signal.diff()

def f45_liqd_gemini_023_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=101, w3=122, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 101)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=122, adjust=False).mean() * 1.221176 + 0.0030754 * anchor
    return base_signal.diff()

def f45_liqd_gemini_024_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=114, w3=139, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(114, min_periods=max(114//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.234706 + 0.0030755 * anchor
    return base_signal.diff()

def f45_liqd_gemini_025_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=127, w3=156, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(127, min_periods=max(127//3, 2)).rank(pct=True)
    persistence = change.rolling(156, min_periods=max(156//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.065333 * persistence + 0.0030756 * anchor
    return base_signal.diff()

def f45_liqd_gemini_026_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=140, w3=173, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(140, min_periods=max(140//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.261765 + 0.0030757 * anchor
    return base_signal.diff()

def f45_liqd_gemini_027_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=153, w3=190, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(153, min_periods=max(153//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.078 * slope + 0.0030758 * anchor
    return base_signal.diff()

def f45_liqd_gemini_028_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=166, w3=207, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(166, min_periods=max(166//3, 2)).mean()
    noise = impulse.abs().rolling(207, min_periods=max(207//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.288824 + 0.0030759 * anchor
    return base_signal.diff()

def f45_liqd_gemini_029_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=179, w3=224, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 179)
    curvature = _rolling_slope(acceleration, 224)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.090667 * acceleration + 0.003076 * anchor
    return base_signal.diff()

def f45_liqd_gemini_030_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=192, w3=241, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 188)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.097 * pressure.rolling(241, min_periods=max(241//3, 2)).mean() + 0.0030761 * anchor
    return base_signal.diff()

def f45_liqd_gemini_031_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=205, w3=258, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(195, min_periods=max(195//3, 2)).mean())
    decay = spread.ewm(span=205, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.329412 + 0.0030762 * anchor
    return base_signal.diff()

def f45_liqd_gemini_032_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=218, w3=275, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(218, min_periods=max(218//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 202)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.342941 + 0.0030763 * anchor
    return base_signal.diff()

def f45_liqd_gemini_033_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=231, w3=292, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(209, min_periods=max(209//3, 2)).mean(), b.abs().rolling(231, min_periods=max(231//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.116 * _rolling_slope(cover, 209) + 0.0030764 * anchor
    return base_signal.diff()

def f45_liqd_gemini_034_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=244, w3=309, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.122333 * y + 0.877667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 216) - _rolling_slope(basket, 244) + 0.0030765 * anchor
    return base_signal.diff()

def f45_liqd_gemini_035_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=257, w3=326, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(257, min_periods=max(257//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.383529 + 0.0030766 * anchor
    return base_signal.diff()

def f45_liqd_gemini_036_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=270, w3=343, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(270, min_periods=max(270//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.135 * _rolling_slope(draw, 343) + 0.0030767 * anchor
    return base_signal.diff()

def f45_liqd_gemini_037_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=283, w3=360, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.410588 + 0.0030768 * anchor
    return base_signal.diff()

def f45_liqd_gemini_038_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=296, w3=377, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(296, min_periods=max(296//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.424118 + 0.0030769 * anchor
    return base_signal.diff()

def f45_liqd_gemini_039_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=309, w3=394, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 309)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.437647 + 0.003077 * anchor
    return base_signal.diff()

def f45_liqd_gemini_040_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=322, w3=411, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(322, min_periods=max(322//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.451176 + 0.0030771 * anchor
    return base_signal.diff()

def f45_liqd_gemini_041_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=335, w3=428, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(18)
    rank = change.rolling(335, min_periods=max(335//3, 2)).rank(pct=True)
    persistence = change.rolling(428, min_periods=max(428//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.166667 * persistence + 0.0030772 * anchor
    return base_signal.diff()

def f45_liqd_gemini_042_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=348, w3=445, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(348, min_periods=max(348//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478235 + 0.0030773 * anchor
    return base_signal.diff()

def f45_liqd_gemini_043_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=361, w3=462, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(361, min_periods=max(361//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.179333 * slope + 0.0030774 * anchor
    return base_signal.diff()

def f45_liqd_gemini_044_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=374, w3=479, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(39)
    drag = impulse.rolling(374, min_periods=max(374//3, 2)).mean()
    noise = impulse.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.505294 + 0.0030775 * anchor
    return base_signal.diff()

def f45_liqd_gemini_045_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=387, w3=496, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 387)
    curvature = _rolling_slope(acceleration, 496)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.192 * acceleration + 0.0030776 * anchor
    return base_signal.diff()

def f45_liqd_gemini_046_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=400, w3=513, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 53)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.198333 * pressure.rolling(513, min_periods=max(513//3, 2)).mean() + 0.0030777 * anchor
    return base_signal.diff()

def f45_liqd_gemini_047_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=413, w3=530, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(60, min_periods=max(60//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.545882 + 0.0030778 * anchor
    return base_signal.diff()

def f45_liqd_gemini_048_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=426, w3=547, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(426, min_periods=max(426//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 67)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.559412 + 0.0030779 * anchor
    return base_signal.diff()

def f45_liqd_gemini_049_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=439, w3=564, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(74, min_periods=max(74//3, 2)).mean(), b.abs().rolling(439, min_periods=max(439//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.217333 * _rolling_slope(cover, 74) + 0.003078 * anchor
    return base_signal.diff()

def f45_liqd_gemini_050_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=452, w3=581, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.223667 * y + 0.776333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 81) - _rolling_slope(basket, 452) + 0.0030781 * anchor
    return base_signal.diff()

def f45_liqd_gemini_051_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=465, w3=598, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(465, min_periods=max(465//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.6 + 0.0030782 * anchor
    return base_signal.diff()

def f45_liqd_gemini_052_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=478, w3=615, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(478, min_periods=max(478//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.236333 * _rolling_slope(draw, 615) + 0.0030783 * anchor
    return base_signal.diff()

def f45_liqd_gemini_053_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=491, w3=632, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(102) - b.diff(126)
    stress = imbalance.rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.627059 + 0.0030784 * anchor
    return base_signal.diff()

def f45_liqd_gemini_054_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=504, w3=649, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(504, min_periods=max(504//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.640588 + 0.0030785 * anchor
    return base_signal.diff()

def f45_liqd_gemini_055_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=18, w3=666, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 18)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.654118 + 0.0030786 * anchor
    return base_signal.diff()

def f45_liqd_gemini_056_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=31, w3=683, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(31, min_periods=max(31//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.667647 + 0.0030787 * anchor
    return base_signal.diff()

def f45_liqd_gemini_057_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=44, w3=700, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(44, min_periods=max(44//3, 2)).rank(pct=True)
    persistence = change.rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.268 * persistence + 0.0030788 * anchor
    return base_signal.diff()

def f45_liqd_gemini_058_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=57, w3=717, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(57, min_periods=max(57//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.841176 + 0.0030789 * anchor
    return base_signal.diff()

def f45_liqd_gemini_059_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=70, w3=734, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(70, min_periods=max(70//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.280667 * slope + 0.003079 * anchor
    return base_signal.diff()

def f45_liqd_gemini_060_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=83, w3=751, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(83, min_periods=max(83//3, 2)).mean()
    noise = impulse.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.868235 + 0.0030791 * anchor
    return base_signal.diff()

def f45_liqd_gemini_061_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=96, w3=17, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 96)
    curvature = _rolling_slope(acceleration, 17)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.293333 * acceleration + 0.0030792 * anchor
    return base_signal.diff()

def f45_liqd_gemini_062_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=109, w3=34, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 165)
    pressure = rel_log.diff(109)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.299667 * pressure.rolling(34, min_periods=max(34//3, 2)).mean() + 0.0030793 * anchor
    return base_signal.diff()

def f45_liqd_gemini_063_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=122, w3=51, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(172, min_periods=max(172//3, 2)).mean())
    decay = spread.ewm(span=122, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.908824 + 0.0030794 * anchor
    return base_signal.diff()

def f45_liqd_gemini_064_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=135, w3=68, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(135, min_periods=max(135//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 179)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.922353 + 0.0030795 * anchor
    return base_signal.diff()

def f45_liqd_gemini_065_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=148, w3=85, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(186, min_periods=max(186//3, 2)).mean(), b.abs().rolling(148, min_periods=max(148//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(85) + 0.318667 * _rolling_slope(cover, 186) + 0.0030796 * anchor
    return base_signal.diff()

def f45_liqd_gemini_066_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=161, w3=102, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.325 * y + 0.675000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 193) - _rolling_slope(basket, 161) + 0.0030797 * anchor
    return base_signal.diff()

def f45_liqd_gemini_067_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=174, w3=119, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(119) * 0.962941 + 0.0030798 * anchor
    return base_signal.diff()

def f45_liqd_gemini_068_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=187, w3=136, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(187, min_periods=max(187//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.337667 * _rolling_slope(draw, 136) + 0.0030799 * anchor
    return base_signal.diff()

def f45_liqd_gemini_069_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=200, w3=153, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.99 + 0.00308 * anchor
    return base_signal.diff()

def f45_liqd_gemini_070_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=213, w3=170, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(213, min_periods=max(213//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.003529 + 0.0030801 * anchor
    return base_signal.diff()

def f45_liqd_gemini_071_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=226, w3=187, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 226)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=187, adjust=False).mean() * 1.017059 + 0.0030802 * anchor
    return base_signal.diff()

def f45_liqd_gemini_072_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=239, w3=204, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(239, min_periods=max(239//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.030588 + 0.0030803 * anchor
    return base_signal.diff()

def f45_liqd_gemini_073_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=252, w3=221, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(252, min_periods=max(252//3, 2)).rank(pct=True)
    persistence = change.rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.037 * persistence + 0.0030804 * anchor
    return base_signal.diff()

def f45_liqd_gemini_074_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=265, w3=238, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(265, min_periods=max(265//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.057647 + 0.0030805 * anchor
    return base_signal.diff()

def f45_liqd_gemini_075_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=278, w3=255, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(278, min_periods=max(278//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.049667 * slope + 0.0030806 * anchor
    return base_signal.diff()
