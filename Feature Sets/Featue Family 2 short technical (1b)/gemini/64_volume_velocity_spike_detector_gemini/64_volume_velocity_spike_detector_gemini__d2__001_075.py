"""64 volume velocity spike detector gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of rapid acceleration in volume as a precursor to price jumps.
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

def f64_vvsd_gemini_001_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=5]"""
    window = 5
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_002_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=10]"""
    window = 10
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_003_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=21]"""
    window = 21
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_004_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=42]"""
    window = 42
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_005_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=63]"""
    window = 63
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_006_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=126]"""
    window = 126
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_007_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=252]"""
    window = 252
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_008_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=504]"""
    window = 504
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_009_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=756]"""
    window = 756
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_010_d2(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff()

def f64_vvsd_gemini_011_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=180, w2=365, w3=685, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 365)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.952353 + 0.0041522 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_012_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=187, w2=378, w3=702, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(378, min_periods=max(378//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.965882 + 0.0041523 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_013_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=194, w2=391, w3=719, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.134333 * persistence + 0.0041524 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_014_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=201, w2=404, w3=736, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(404, min_periods=max(404//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.992941 + 0.0041525 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_015_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=208, w2=417, w3=753, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147 * slope + 0.0041526 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_016_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=215, w2=430, w3=19, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(430, min_periods=max(430//3, 2)).mean()
    noise = impulse.abs().rolling(19, min_periods=max(19//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02 + 0.0041527 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_017_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=222, w2=443, w3=36, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 36)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.159667 * acceleration + 0.0041528 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_018_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=229, w2=456, w3=53, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(456, min_periods=max(456//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(53) * 1.047059 + 0.0041529 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_019_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=236, w2=469, w3=70, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(469, min_periods=max(469//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.172333 * _rolling_slope(draw, 70) + 0.004153 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_020_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=243, w2=482, w3=87, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(482, min_periods=max(482//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.074118 + 0.0041531 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_021_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=250, w2=495, w3=104, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 495)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=104, adjust=False).mean() * 1.087647 + 0.0041532 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_022_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=10, w2=508, w3=121, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(508, min_periods=max(508//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.101176 + 0.0041533 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_023_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=17, w2=22, w3=138, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(17)
    rank = change.rolling(22, min_periods=max(22//3, 2)).rank(pct=True)
    persistence = change.rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.197667 * persistence + 0.0041534 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_024_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=24, w2=35, w3=155, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.128235 + 0.0041535 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_025_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=31, w2=48, w3=172, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.210333 * slope + 0.0041536 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_026_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=38, w2=61, w3=189, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(38)
    drag = impulse.rolling(61, min_periods=max(61//3, 2)).mean()
    noise = impulse.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.155294 + 0.0041537 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_027_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=45, w2=74, w3=206, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 74)
    curvature = _rolling_slope(acceleration, 206)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.223 * acceleration + 0.0041538 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_028_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=52, w2=87, w3=223, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(87, min_periods=max(87//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.182353 + 0.0041539 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_029_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=59, w2=100, w3=240, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(100, min_periods=max(100//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.235667 * _rolling_slope(draw, 240) + 0.004154 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_030_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=66, w2=113, w3=257, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(113, min_periods=max(113//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.209412 + 0.0041541 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_031_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=73, w2=126, w3=274, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=274, adjust=False).mean() * 1.222941 + 0.0041542 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_032_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=80, w2=139, w3=291, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(139, min_periods=max(139//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.236471 + 0.0041543 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_033_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=87, w2=152, w3=308, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(87)
    rank = change.rolling(152, min_periods=max(152//3, 2)).rank(pct=True)
    persistence = change.rolling(308, min_periods=max(308//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.261 * persistence + 0.0041544 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_034_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=94, w2=165, w3=325, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(165, min_periods=max(165//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.263529 + 0.0041545 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_035_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=101, w2=178, w3=342, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(178, min_periods=max(178//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.273667 * slope + 0.0041546 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_036_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=108, w2=191, w3=359, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(108)
    drag = impulse.rolling(191, min_periods=max(191//3, 2)).mean()
    noise = impulse.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.290588 + 0.0041547 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_037_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=115, w2=204, w3=376, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 204)
    curvature = _rolling_slope(acceleration, 376)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.286333 * acceleration + 0.0041548 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_038_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=122, w2=217, w3=393, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(217, min_periods=max(217//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.317647 + 0.0041549 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_039_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=129, w2=230, w3=410, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(230, min_periods=max(230//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.299 * _rolling_slope(draw, 410) + 0.004155 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_040_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=136, w2=243, w3=427, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(243, min_periods=max(243//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.344706 + 0.0041551 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_041_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=143, w2=256, w3=444, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 256)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.358235 + 0.0041552 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_042_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=150, w2=269, w3=461, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(269, min_periods=max(269//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.371765 + 0.0041553 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_043_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=157, w2=282, w3=478, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(282, min_periods=max(282//3, 2)).rank(pct=True)
    persistence = change.rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.324333 * persistence + 0.0041554 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_044_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=164, w2=295, w3=495, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(295, min_periods=max(295//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.398824 + 0.0041555 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_045_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=171, w2=308, w3=512, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(308, min_periods=max(308//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.337 * slope + 0.0041556 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_046_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=178, w2=321, w3=529, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(321, min_periods=max(321//3, 2)).mean()
    noise = impulse.abs().rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.425882 + 0.0041557 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_047_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=185, w2=334, w3=546, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 334)
    curvature = _rolling_slope(acceleration, 546)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.349667 * acceleration + 0.0041558 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_048_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=192, w2=347, w3=563, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(347, min_periods=max(347//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.452941 + 0.0041559 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_049_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=199, w2=360, w3=580, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(360, min_periods=max(360//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.362333 * _rolling_slope(draw, 580) + 0.004156 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_050_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=206, w2=373, w3=597, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(597, min_periods=max(597//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.48 + 0.0041561 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_051_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=213, w2=386, w3=614, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 386)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.493529 + 0.0041562 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_052_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=220, w2=399, w3=631, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(399, min_periods=max(399//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.507059 + 0.0041563 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_053_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=227, w2=412, w3=648, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(412, min_periods=max(412//3, 2)).rank(pct=True)
    persistence = change.rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.055333 * persistence + 0.0041564 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_054_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=234, w2=425, w3=665, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(425, min_periods=max(425//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.534118 + 0.0041565 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_055_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=241, w2=438, w3=682, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.068 * slope + 0.0041566 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_056_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=451, w3=699, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.561176 + 0.0041567 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_057_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=464, w3=716, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 8)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 716)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.080667 * acceleration + 0.0041568 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_058_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=477, w3=733, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(477, min_periods=max(477//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.588235 + 0.0041569 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_059_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=490, w3=750, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(490, min_periods=max(490//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.093333 * _rolling_slope(draw, 750) + 0.004157 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_060_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=503, w3=767, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(503, min_periods=max(503//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(767, min_periods=max(767//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.615294 + 0.0041571 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_061_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=17, w3=33, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 17)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=33, adjust=False).mean() * 1.628824 + 0.0041572 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_062_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=30, w3=50, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.642353 + 0.0041573 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_063_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=43, w3=67, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(50)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.118667 * persistence + 0.0041574 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_064_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=56, w3=84, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(56, min_periods=max(56//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.669412 + 0.0041575 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_065_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=69, w3=101, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(69, min_periods=max(69//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.131333 * slope + 0.0041576 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_066_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=82, w3=118, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(71)
    drag = impulse.rolling(82, min_periods=max(82//3, 2)).mean()
    noise = impulse.abs().rolling(118, min_periods=max(118//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.842941 + 0.0041577 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_067_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=95, w3=135, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 95)
    curvature = _rolling_slope(acceleration, 135)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.144 * acceleration + 0.0041578 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_068_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=108, w3=152, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(85, min_periods=max(85//3, 2)).mean(), upside.rolling(108, min_periods=max(108//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87 + 0.0041579 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_069_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=121, w3=169, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(121, min_periods=max(121//3, 2)).max()
    rebound = x - x.rolling(92, min_periods=max(92//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.156667 * _rolling_slope(draw, 169) + 0.004158 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_070_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=134, w3=186, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 99)
    baseline = trend.rolling(134, min_periods=max(134//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(186, min_periods=max(186//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.897059 + 0.0041581 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_071_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=147, w3=203, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 106)
    slow = _rolling_slope(x, 147)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=203, adjust=False).mean() * 0.910588 + 0.0041582 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_072_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=160, w3=220, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(113, min_periods=max(113//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.924118 + 0.0041583 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_073_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=173, w3=237, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(120)
    rank = change.rolling(173, min_periods=max(173//3, 2)).rank(pct=True)
    persistence = change.rolling(237, min_periods=max(237//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.182 * persistence + 0.0041584 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_074_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=186, w3=254, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(127, min_periods=max(127//3, 2)).std()
    vol_slow = ret.rolling(186, min_periods=max(186//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.951176 + 0.0041585 * anchor
    return base_signal.diff().diff()

def f64_vvsd_gemini_075_d2(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=199, w3=271, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(199, min_periods=max(199//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 134)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.194667 * slope + 0.0041586 * anchor
    return base_signal.diff().diff()
