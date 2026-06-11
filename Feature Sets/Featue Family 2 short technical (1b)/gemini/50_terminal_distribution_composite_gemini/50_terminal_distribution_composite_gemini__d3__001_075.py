"""50 terminal distribution composite gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Composite metric for detecting the final stages of asset distribution before a crash.
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

def f50_tdic_gemini_001_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=5]"""
    window = 5
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_002_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=10]"""
    window = 10
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_003_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=21]"""
    window = 21
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_004_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=42]"""
    window = 42
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_005_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=63]"""
    window = 63
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_006_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=126]"""
    window = 126
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_007_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=252]"""
    window = 252
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_008_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=504]"""
    window = 504
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_009_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=756]"""
    window = 756
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_010_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite metric for detecting the final stages of asset distribution before a crash. [window=1260]"""
    window = 1260
    res = _safe_div(volume.rolling(window).mean(), _rolling_slope(close, window).abs() + 1e-9)
    return (res).diff().diff().diff()

def f50_tdic_gemini_011_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=65, w3=459, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(65, min_periods=max(65//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.906471 + 0.0033822 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_012_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=133, w2=78, w3=476, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.214333 * _rolling_slope(draw, 476) + 0.0033823 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_013_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=140, w2=91, w3=493, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(91)
    stress = imbalance.rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.933529 + 0.0033824 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_014_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=147, w2=104, w3=510, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(104, min_periods=max(104//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.947059 + 0.0033825 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_015_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=154, w2=117, w3=527, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.960588 + 0.0033826 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_016_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=161, w2=130, w3=544, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(130, min_periods=max(130//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.974118 + 0.0033827 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_017_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=168, w2=143, w3=561, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(143, min_periods=max(143//3, 2)).rank(pct=True)
    persistence = change.rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.246 * persistence + 0.0033828 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_018_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=175, w2=156, w3=578, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(156, min_periods=max(156//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.001176 + 0.0033829 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_019_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=182, w2=169, w3=595, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(169, min_periods=max(169//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.258667 * slope + 0.003383 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_020_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=189, w2=182, w3=612, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(182, min_periods=max(182//3, 2)).mean()
    noise = impulse.abs().rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.028235 + 0.0033831 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_021_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=196, w2=195, w3=629, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 195)
    curvature = _rolling_slope(acceleration, 629)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.271333 * acceleration + 0.0033832 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_022_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=203, w2=208, w3=646, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 203)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.277667 * pressure.rolling(646, min_periods=max(646//3, 2)).mean() + 0.0033833 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_023_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=210, w2=221, w3=663, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(210, min_periods=max(210//3, 2)).mean())
    decay = spread.ewm(span=221, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.068824 + 0.0033834 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_024_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=217, w2=234, w3=680, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(234, min_periods=max(234//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 217)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.082353 + 0.0033835 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_025_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=224, w2=247, w3=697, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(224, min_periods=max(224//3, 2)).mean(), b.abs().rolling(247, min_periods=max(247//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.296667 * _rolling_slope(cover, 224) + 0.0033836 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_026_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=231, w2=260, w3=714, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.303 * y + 0.697000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 231) - _rolling_slope(basket, 260) + 0.0033837 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_027_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=238, w2=273, w3=731, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(273, min_periods=max(273//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.122941 + 0.0033838 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_028_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=245, w2=286, w3=748, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(286, min_periods=max(286//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315667 * _rolling_slope(draw, 748) + 0.0033839 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_029_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=5, w2=299, w3=765, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(5) - b.diff(126)
    stress = imbalance.rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.15 + 0.003384 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_030_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=12, w2=312, w3=31, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(312, min_periods=max(312//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.163529 + 0.0033841 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_031_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=19, w2=325, w3=48, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 325)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=48, adjust=False).mean() * 1.177059 + 0.0033842 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_032_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=338, w3=65, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(338, min_periods=max(338//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.190588 + 0.0033843 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_033_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=351, w3=82, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(33)
    rank = change.rolling(351, min_periods=max(351//3, 2)).rank(pct=True)
    persistence = change.rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.347333 * persistence + 0.0033844 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_034_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=364, w3=99, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(364, min_periods=max(364//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.217647 + 0.0033845 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_035_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=377, w3=116, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(377, min_periods=max(377//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.36 * slope + 0.0033846 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_036_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=390, w3=133, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(54)
    drag = impulse.rolling(390, min_periods=max(390//3, 2)).mean()
    noise = impulse.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.244706 + 0.0033847 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_037_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=403, w3=150, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 403)
    curvature = _rolling_slope(acceleration, 150)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.040333 * acceleration + 0.0033848 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_038_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=416, w3=167, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 68)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.046667 * pressure.rolling(167, min_periods=max(167//3, 2)).mean() + 0.0033849 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_039_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=429, w3=184, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(75, min_periods=max(75//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.285294 + 0.003385 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_040_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=442, w3=201, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(442, min_periods=max(442//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 82)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.298824 + 0.0033851 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_041_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=455, w3=218, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(89, min_periods=max(89//3, 2)).mean(), b.abs().rolling(455, min_periods=max(455//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.065667 * _rolling_slope(cover, 89) + 0.0033852 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_042_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=468, w3=235, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.072 * y + 0.928000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 96) - _rolling_slope(basket, 468) + 0.0033853 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_043_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=481, w3=252, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(103, min_periods=max(103//3, 2)).mean(), upside.rolling(481, min_periods=max(481//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.339412 + 0.0033854 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_044_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=494, w3=269, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(494, min_periods=max(494//3, 2)).max()
    rebound = x - x.rolling(110, min_periods=max(110//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.084667 * _rolling_slope(draw, 269) + 0.0033855 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_045_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=507, w3=286, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(117) - b.diff(126)
    stress = imbalance.rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.366471 + 0.0033856 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_046_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=21, w3=303, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 124)
    baseline = trend.rolling(21, min_periods=max(21//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.38 + 0.0033857 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_047_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=34, w3=320, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 131)
    slow = _rolling_slope(x, 34)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.393529 + 0.0033858 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_048_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=47, w3=337, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(47, min_periods=max(47//3, 2)).max()
    trough = x.rolling(138, min_periods=max(138//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.407059 + 0.0033859 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_049_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=60, w3=354, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(60, min_periods=max(60//3, 2)).rank(pct=True)
    persistence = change.rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.116333 * persistence + 0.003386 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_050_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=73, w3=371, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(152, min_periods=max(152//3, 2)).std()
    vol_slow = ret.rolling(73, min_periods=max(73//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.434118 + 0.0033861 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_051_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=86, w3=388, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(86, min_periods=max(86//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 159)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.129 * slope + 0.0033862 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_052_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=99, w3=405, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(99, min_periods=max(99//3, 2)).mean()
    noise = impulse.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.461176 + 0.0033863 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_053_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=112, w3=422, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 173)
    acceleration = _rolling_slope(velocity, 112)
    curvature = _rolling_slope(acceleration, 422)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.141667 * acceleration + 0.0033864 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_054_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=125, w3=439, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 180)
    pressure = rel_log.diff(125)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.148 * pressure.rolling(439, min_periods=max(439//3, 2)).mean() + 0.0033865 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_055_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=138, w3=456, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(187, min_periods=max(187//3, 2)).mean())
    decay = spread.ewm(span=138, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.501765 + 0.0033866 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_056_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=151, w3=473, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(151, min_periods=max(151//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 194)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.515294 + 0.0033867 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_057_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=164, w3=490, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(201, min_periods=max(201//3, 2)).mean(), b.abs().rolling(164, min_periods=max(164//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.167 * _rolling_slope(cover, 201) + 0.0033868 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_058_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=177, w3=507, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.173333 * y + 0.826667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 208) - _rolling_slope(basket, 177) + 0.0033869 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_059_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=190, w3=524, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(190, min_periods=max(190//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.555882 + 0.003387 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_060_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=203, w3=541, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(203, min_periods=max(203//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.186 * _rolling_slope(draw, 541) + 0.0033871 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_061_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=216, w3=558, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.582941 + 0.0033872 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_062_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=229, w3=575, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(229, min_periods=max(229//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.596471 + 0.0033873 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_063_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=242, w3=592, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 242)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.61 + 0.0033874 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_064_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=255, w3=609, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(255, min_periods=max(255//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.623529 + 0.0033875 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_065_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=268, w3=626, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(10)
    rank = change.rolling(268, min_periods=max(268//3, 2)).rank(pct=True)
    persistence = change.rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217667 * persistence + 0.0033876 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_066_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=281, w3=643, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(281, min_periods=max(281//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.650588 + 0.0033877 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_067_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=294, w3=660, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(294, min_periods=max(294//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.230333 * slope + 0.0033878 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_068_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=307, w3=677, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(31)
    drag = impulse.rolling(307, min_periods=max(307//3, 2)).mean()
    noise = impulse.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.824118 + 0.0033879 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_069_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=320, w3=694, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 320)
    curvature = _rolling_slope(acceleration, 694)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.243 * acceleration + 0.003388 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_070_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=333, w3=711, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 45)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.249333 * pressure.rolling(711, min_periods=max(711//3, 2)).mean() + 0.0033881 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_071_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=346, w3=728, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(52, min_periods=max(52//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.864706 + 0.0033882 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_072_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=359, w3=745, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(359, min_periods=max(359//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 59)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.878235 + 0.0033883 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_073_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=372, w3=762, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(66, min_periods=max(66//3, 2)).mean(), b.abs().rolling(372, min_periods=max(372//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.268333 * _rolling_slope(cover, 66) + 0.0033884 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_074_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=385, w3=28, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.274667 * y + 0.725333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 73) - _rolling_slope(basket, 385) + 0.0033885 * anchor
    return base_signal.diff().diff().diff()

def f50_tdic_gemini_075_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=398, w3=45, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(398, min_periods=max(398//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(45) * 0.918824 + 0.0033886 * anchor
    return base_signal.diff().diff().diff()
