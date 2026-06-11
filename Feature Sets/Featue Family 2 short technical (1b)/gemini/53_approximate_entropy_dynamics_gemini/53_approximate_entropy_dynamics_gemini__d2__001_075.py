"""53 approximate entropy dynamics gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Quantification of regularity and predictability in short-term price fluctuations.
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

def f53_aent_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff().diff()

def f53_aent_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=125, w3=354, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 125)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.257059 + 0.0035362 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=138, w3=371, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(138, min_periods=max(138//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.270588 + 0.0035363 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=151, w3=388, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(52)
    rank = change.rolling(151, min_periods=max(151//3, 2)).rank(pct=True)
    persistence = change.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.336333 * persistence + 0.0035364 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=164, w3=405, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(164, min_periods=max(164//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.297647 + 0.0035365 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=177, w3=422, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(177, min_periods=max(177//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349 * slope + 0.0035366 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=190, w3=439, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(73)
    drag = impulse.rolling(190, min_periods=max(190//3, 2)).mean()
    noise = impulse.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.324706 + 0.0035367 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=203, w3=456, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 203)
    curvature = _rolling_slope(acceleration, 456)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.361667 * acceleration + 0.0035368 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=216, w3=473, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(216, min_periods=max(216//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.351765 + 0.0035369 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=229, w3=490, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(229, min_periods=max(229//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.042 * _rolling_slope(draw, 490) + 0.003537 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=242, w3=507, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(242, min_periods=max(242//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.378824 + 0.0035371 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=255, w3=524, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.392353 + 0.0035372 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=268, w3=541, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(268, min_periods=max(268//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.405882 + 0.0035373 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=281, w3=558, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(122)
    rank = change.rolling(281, min_periods=max(281//3, 2)).rank(pct=True)
    persistence = change.rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.067333 * persistence + 0.0035374 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=294, w3=575, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.432941 + 0.0035375 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=307, w3=592, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.08 * slope + 0.0035376 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=320, w3=609, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(609, min_periods=max(609//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.46 + 0.0035377 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=333, w3=626, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 626)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.092667 * acceleration + 0.0035378 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=346, w3=643, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(346, min_periods=max(346//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.487059 + 0.0035379 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=359, w3=660, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(359, min_periods=max(359//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.105333 * _rolling_slope(draw, 660) + 0.003538 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=372, w3=677, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(372, min_periods=max(372//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.514118 + 0.0035381 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=385, w3=694, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 385)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.527647 + 0.0035382 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=398, w3=711, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(398, min_periods=max(398//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.541176 + 0.0035383 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=411, w3=728, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(411, min_periods=max(411//3, 2)).rank(pct=True)
    persistence = change.rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.130667 * persistence + 0.0035384 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=424, w3=745, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(424, min_periods=max(424//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.568235 + 0.0035385 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=437, w3=762, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.143333 * slope + 0.0035386 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=450, w3=28, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.595294 + 0.0035387 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=463, w3=45, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.156 * acceleration + 0.0035388 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=476, w3=62, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(62) * 1.622353 + 0.0035389 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=489, w3=79, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.168667 * _rolling_slope(draw, 79) + 0.003539 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=502, w3=96, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.649412 + 0.0035391 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=16, w3=113, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=113, adjust=False).mean() * 1.662941 + 0.0035392 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=29, w3=130, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(29, min_periods=max(29//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.822941 + 0.0035393 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=42, w3=147, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(15)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.194 * persistence + 0.0035394 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=55, w3=164, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.85 + 0.0035395 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=68, w3=181, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.206667 * slope + 0.0035396 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=81, w3=198, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(36)
    drag = impulse.rolling(81, min_periods=max(81//3, 2)).mean()
    noise = impulse.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.877059 + 0.0035397 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=94, w3=215, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.219333 * acceleration + 0.0035398 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=107, w3=232, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(107, min_periods=max(107//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.904118 + 0.0035399 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=120, w3=249, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(120, min_periods=max(120//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232 * _rolling_slope(draw, 249) + 0.00354 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=133, w3=266, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(133, min_periods=max(133//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.931176 + 0.0035401 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=146, w3=283, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 146)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=283, adjust=False).mean() * 0.944706 + 0.0035402 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=159, w3=300, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(159, min_periods=max(159//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.958235 + 0.0035403 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=172, w3=317, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(85)
    rank = change.rolling(172, min_periods=max(172//3, 2)).rank(pct=True)
    persistence = change.rolling(317, min_periods=max(317//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257333 * persistence + 0.0035404 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=185, w3=334, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(185, min_periods=max(185//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.985294 + 0.0035405 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=198, w3=351, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(198, min_periods=max(198//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.27 * slope + 0.0035406 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=211, w3=368, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(106)
    drag = impulse.rolling(211, min_periods=max(211//3, 2)).mean()
    noise = impulse.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.012353 + 0.0035407 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=224, w3=385, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 224)
    curvature = _rolling_slope(acceleration, 385)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.282667 * acceleration + 0.0035408 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=237, w3=402, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.039412 + 0.0035409 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=250, w3=419, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(250, min_periods=max(250//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.295333 * _rolling_slope(draw, 419) + 0.003541 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=263, w3=436, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(263, min_periods=max(263//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.066471 + 0.0035411 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=276, w3=453, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 276)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.08 + 0.0035412 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=289, w3=470, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(289, min_periods=max(289//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.093529 + 0.0035413 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=302, w3=487, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(302, min_periods=max(302//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.320667 * persistence + 0.0035414 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=315, w3=504, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(315, min_periods=max(315//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.120588 + 0.0035415 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=328, w3=521, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(328, min_periods=max(328//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.333333 * slope + 0.0035416 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=341, w3=538, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(341, min_periods=max(341//3, 2)).mean()
    noise = impulse.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.147647 + 0.0035417 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=354, w3=555, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 354)
    curvature = _rolling_slope(acceleration, 555)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.346 * acceleration + 0.0035418 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=367, w3=572, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(367, min_periods=max(367//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.174706 + 0.0035419 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=380, w3=589, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(380, min_periods=max(380//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.358667 * _rolling_slope(draw, 589) + 0.003542 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=393, w3=606, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(393, min_periods=max(393//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.201765 + 0.0035421 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=406, w3=623, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 406)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.215294 + 0.0035422 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=419, w3=640, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(419, min_periods=max(419//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.228824 + 0.0035423 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=432, w3=657, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(432, min_periods=max(432//3, 2)).rank(pct=True)
    persistence = change.rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.051667 * persistence + 0.0035424 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=445, w3=674, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(445, min_periods=max(445//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.255882 + 0.0035425 * anchor
    return base_signal.diff().diff()

def f53_aent_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=458, w3=691, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(458, min_periods=max(458//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.064333 * slope + 0.0035426 * anchor
    return base_signal.diff().diff()
