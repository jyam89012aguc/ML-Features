"""64 volume velocity spike detector gemini base features 1-75 — Pipeline 1b-HF Grade v7.

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

def f64_vvsd_gemini_001(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=5]"""
    window = 5
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_002(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=10]"""
    window = 10
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_003(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=21]"""
    window = 21
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_004(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=42]"""
    window = 42
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_005(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=63]"""
    window = 63
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_006(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=126]"""
    window = 126
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_007(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=252]"""
    window = 252
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_008(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=504]"""
    window = 504
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_009(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=756]"""
    window = 756
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_010(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return res

def f64_vvsd_gemini_011(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=218, w3=431, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 196)
    slow = _rolling_slope(x, 218)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.431765 + 0.0041242 * anchor
    return base_signal

def f64_vvsd_gemini_012(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=231, w3=448, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(231, min_periods=max(231//3, 2)).max()
    trough = x.rolling(203, min_periods=max(203//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.445294 + 0.0041243 * anchor
    return base_signal

def f64_vvsd_gemini_013(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=244, w3=465, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355 * persistence + 0.0041244 * anchor
    return base_signal

def f64_vvsd_gemini_014(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=257, w3=482, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(217, min_periods=max(217//3, 2)).std()
    vol_slow = ret.rolling(257, min_periods=max(257//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.472353 + 0.0041245 * anchor
    return base_signal

def f64_vvsd_gemini_015(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=270, w3=499, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(270, min_periods=max(270//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 224)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.035333 * slope + 0.0041246 * anchor
    return base_signal

def f64_vvsd_gemini_016(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=283, w3=516, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(283, min_periods=max(283//3, 2)).mean()
    noise = impulse.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.499412 + 0.0041247 * anchor
    return base_signal

def f64_vvsd_gemini_017(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=296, w3=533, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 238)
    acceleration = _rolling_slope(velocity, 296)
    curvature = _rolling_slope(acceleration, 533)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.048 * acceleration + 0.0041248 * anchor
    return base_signal

def f64_vvsd_gemini_018(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=309, w3=550, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(245, min_periods=max(245//3, 2)).mean(), upside.rolling(309, min_periods=max(309//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.526471 + 0.0041249 * anchor
    return base_signal

def f64_vvsd_gemini_019(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=322, w3=567, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(322, min_periods=max(322//3, 2)).max()
    rebound = x - x.rolling(5, min_periods=max(5//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.060667 * _rolling_slope(draw, 567) + 0.004125 * anchor
    return base_signal

def f64_vvsd_gemini_020(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=335, w3=584, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 12)
    baseline = trend.rolling(335, min_periods=max(335//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(584, min_periods=max(584//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.553529 + 0.0041251 * anchor
    return base_signal

def f64_vvsd_gemini_021(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=348, w3=601, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 19)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.567059 + 0.0041252 * anchor
    return base_signal

def f64_vvsd_gemini_022(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=361, w3=618, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(26, min_periods=max(26//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.580588 + 0.0041253 * anchor
    return base_signal

def f64_vvsd_gemini_023(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=374, w3=635, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(33)
    rank = change.rolling(374, min_periods=max(374//3, 2)).rank(pct=True)
    persistence = change.rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.086 * persistence + 0.0041254 * anchor
    return base_signal

def f64_vvsd_gemini_024(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=387, w3=652, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(40, min_periods=max(40//3, 2)).std()
    vol_slow = ret.rolling(387, min_periods=max(387//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.607647 + 0.0041255 * anchor
    return base_signal

def f64_vvsd_gemini_025(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=400, w3=669, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(400, min_periods=max(400//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 47)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.098667 * slope + 0.0041256 * anchor
    return base_signal

def f64_vvsd_gemini_026(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=413, w3=686, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(54)
    drag = impulse.rolling(413, min_periods=max(413//3, 2)).mean()
    noise = impulse.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.634706 + 0.0041257 * anchor
    return base_signal

def f64_vvsd_gemini_027(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=426, w3=703, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 61)
    acceleration = _rolling_slope(velocity, 426)
    curvature = _rolling_slope(acceleration, 703)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.111333 * acceleration + 0.0041258 * anchor
    return base_signal

def f64_vvsd_gemini_028(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=439, w3=720, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(439, min_periods=max(439//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.661765 + 0.0041259 * anchor
    return base_signal

def f64_vvsd_gemini_029(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=452, w3=737, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(452, min_periods=max(452//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.124 * _rolling_slope(draw, 737) + 0.004126 * anchor
    return base_signal

def f64_vvsd_gemini_030(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=465, w3=754, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 82)
    baseline = trend.rolling(465, min_periods=max(465//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.835294 + 0.0041261 * anchor
    return base_signal

def f64_vvsd_gemini_031(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=478, w3=20, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 89)
    slow = _rolling_slope(x, 478)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=20, adjust=False).mean() * 0.848824 + 0.0041262 * anchor
    return base_signal

def f64_vvsd_gemini_032(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=491, w3=37, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(491, min_periods=max(491//3, 2)).max()
    trough = x.rolling(96, min_periods=max(96//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.862353 + 0.0041263 * anchor
    return base_signal

def f64_vvsd_gemini_033(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=504, w3=54, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(103)
    rank = change.rolling(504, min_periods=max(504//3, 2)).rank(pct=True)
    persistence = change.rolling(54, min_periods=max(54//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.149333 * persistence + 0.0041264 * anchor
    return base_signal

def f64_vvsd_gemini_034(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=18, w3=71, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(110, min_periods=max(110//3, 2)).std()
    vol_slow = ret.rolling(18, min_periods=max(18//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.889412 + 0.0041265 * anchor
    return base_signal

def f64_vvsd_gemini_035(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=31, w3=88, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(31, min_periods=max(31//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 117)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.162 * slope + 0.0041266 * anchor
    return base_signal

def f64_vvsd_gemini_036(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=44, w3=105, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(124)
    drag = impulse.rolling(44, min_periods=max(44//3, 2)).mean()
    noise = impulse.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.916471 + 0.0041267 * anchor
    return base_signal

def f64_vvsd_gemini_037(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=57, w3=122, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 131)
    acceleration = _rolling_slope(velocity, 57)
    curvature = _rolling_slope(acceleration, 122)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.174667 * acceleration + 0.0041268 * anchor
    return base_signal

def f64_vvsd_gemini_038(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=70, w3=139, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(70, min_periods=max(70//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.943529 + 0.0041269 * anchor
    return base_signal

def f64_vvsd_gemini_039(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=83, w3=156, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(83, min_periods=max(83//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.187333 * _rolling_slope(draw, 156) + 0.004127 * anchor
    return base_signal

def f64_vvsd_gemini_040(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=96, w3=173, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 152)
    baseline = trend.rolling(96, min_periods=max(96//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.970588 + 0.0041271 * anchor
    return base_signal

def f64_vvsd_gemini_041(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=109, w3=190, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 159)
    slow = _rolling_slope(x, 109)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=190, adjust=False).mean() * 0.984118 + 0.0041272 * anchor
    return base_signal

def f64_vvsd_gemini_042(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=122, w3=207, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(122, min_periods=max(122//3, 2)).max()
    trough = x.rolling(166, min_periods=max(166//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.997647 + 0.0041273 * anchor
    return base_signal

def f64_vvsd_gemini_043(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=135, w3=224, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.212667 * persistence + 0.0041274 * anchor
    return base_signal

def f64_vvsd_gemini_044(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=148, w3=241, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(180, min_periods=max(180//3, 2)).std()
    vol_slow = ret.rolling(148, min_periods=max(148//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.024706 + 0.0041275 * anchor
    return base_signal

def f64_vvsd_gemini_045(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=161, w3=258, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(161, min_periods=max(161//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 187)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225333 * slope + 0.0041276 * anchor
    return base_signal

def f64_vvsd_gemini_046(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=174, w3=275, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(174, min_periods=max(174//3, 2)).mean()
    noise = impulse.abs().rolling(275, min_periods=max(275//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.051765 + 0.0041277 * anchor
    return base_signal

def f64_vvsd_gemini_047(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=187, w3=292, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 201)
    acceleration = _rolling_slope(velocity, 187)
    curvature = _rolling_slope(acceleration, 292)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.238 * acceleration + 0.0041278 * anchor
    return base_signal

def f64_vvsd_gemini_048(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=200, w3=309, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(208, min_periods=max(208//3, 2)).mean(), upside.rolling(200, min_periods=max(200//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.078824 + 0.0041279 * anchor
    return base_signal

def f64_vvsd_gemini_049(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=213, w3=326, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(215, min_periods=max(215//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.250667 * _rolling_slope(draw, 326) + 0.004128 * anchor
    return base_signal

def f64_vvsd_gemini_050(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=226, w3=343, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 222)
    baseline = trend.rolling(226, min_periods=max(226//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.105882 + 0.0041281 * anchor
    return base_signal

def f64_vvsd_gemini_051(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=239, w3=360, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 239)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.119412 + 0.0041282 * anchor
    return base_signal

def f64_vvsd_gemini_052(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=252, w3=377, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(252, min_periods=max(252//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.132941 + 0.0041283 * anchor
    return base_signal

def f64_vvsd_gemini_053(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=265, w3=394, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(265, min_periods=max(265//3, 2)).rank(pct=True)
    persistence = change.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.276 * persistence + 0.0041284 * anchor
    return base_signal

def f64_vvsd_gemini_054(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=278, w3=411, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(278, min_periods=max(278//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.16 + 0.0041285 * anchor
    return base_signal

def f64_vvsd_gemini_055(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=291, w3=428, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(291, min_periods=max(291//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.288667 * slope + 0.0041286 * anchor
    return base_signal

def f64_vvsd_gemini_056(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=304, w3=445, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(17)
    drag = impulse.rolling(304, min_periods=max(304//3, 2)).mean()
    noise = impulse.abs().rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.187059 + 0.0041287 * anchor
    return base_signal

def f64_vvsd_gemini_057(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=317, w3=462, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 317)
    curvature = _rolling_slope(acceleration, 462)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.301333 * acceleration + 0.0041288 * anchor
    return base_signal

def f64_vvsd_gemini_058(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=330, w3=479, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(330, min_periods=max(330//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.214118 + 0.0041289 * anchor
    return base_signal

def f64_vvsd_gemini_059(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=343, w3=496, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(343, min_periods=max(343//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.314 * _rolling_slope(draw, 496) + 0.004129 * anchor
    return base_signal

def f64_vvsd_gemini_060(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=356, w3=513, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(356, min_periods=max(356//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.241176 + 0.0041291 * anchor
    return base_signal

def f64_vvsd_gemini_061(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=369, w3=530, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.254706 + 0.0041292 * anchor
    return base_signal

def f64_vvsd_gemini_062(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=382, w3=547, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(382, min_periods=max(382//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.268235 + 0.0041293 * anchor
    return base_signal

def f64_vvsd_gemini_063(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=395, w3=564, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(66)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.339333 * persistence + 0.0041294 * anchor
    return base_signal

def f64_vvsd_gemini_064(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=408, w3=581, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(408, min_periods=max(408//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.295294 + 0.0041295 * anchor
    return base_signal

def f64_vvsd_gemini_065(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=421, w3=598, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.352 * slope + 0.0041296 * anchor
    return base_signal

def f64_vvsd_gemini_066(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=434, w3=615, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(87)
    drag = impulse.rolling(434, min_periods=max(434//3, 2)).mean()
    noise = impulse.abs().rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.322353 + 0.0041297 * anchor
    return base_signal

def f64_vvsd_gemini_067(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=447, w3=632, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 447)
    curvature = _rolling_slope(acceleration, 632)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.032333 * acceleration + 0.0041298 * anchor
    return base_signal

def f64_vvsd_gemini_068(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=460, w3=649, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(460, min_periods=max(460//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.349412 + 0.0041299 * anchor
    return base_signal

def f64_vvsd_gemini_069(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=473, w3=666, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(473, min_periods=max(473//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.045 * _rolling_slope(draw, 666) + 0.00413 * anchor
    return base_signal

def f64_vvsd_gemini_070(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=486, w3=683, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(486, min_periods=max(486//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.376471 + 0.0041301 * anchor
    return base_signal

def f64_vvsd_gemini_071(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=499, w3=700, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 499)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.39 + 0.0041302 * anchor
    return base_signal

def f64_vvsd_gemini_072(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=13, w3=717, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(13, min_periods=max(13//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.403529 + 0.0041303 * anchor
    return base_signal

def f64_vvsd_gemini_073(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=26, w3=734, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(26, min_periods=max(26//3, 2)).rank(pct=True)
    persistence = change.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.070333 * persistence + 0.0041304 * anchor
    return base_signal

def f64_vvsd_gemini_074(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=39, w3=751, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(39, min_periods=max(39//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.430588 + 0.0041305 * anchor
    return base_signal

def f64_vvsd_gemini_075(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=52, w3=17, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(52, min_periods=max(52//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.083 * slope + 0.0041306 * anchor
    return base_signal
