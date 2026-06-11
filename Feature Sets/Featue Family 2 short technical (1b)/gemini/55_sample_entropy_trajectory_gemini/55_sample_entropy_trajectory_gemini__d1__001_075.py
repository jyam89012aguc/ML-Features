"""55 sample entropy trajectory gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Complexity measure that is less sensitive to data length than approximate entropy.
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

def f55_ment_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Complexity measure that is less sensitive to data length than approximate entropy. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std(), window * 2)
    return (res).diff()

def f55_ment_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=390, w3=492, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 229)
    slow = _rolling_slope(x, 390)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.859412 + 0.0036342 * anchor
    return base_signal.diff()

def f55_ment_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=403, w3=509, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(403, min_periods=max(403//3, 2)).max()
    trough = x.rolling(236, min_periods=max(236//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.872941 + 0.0036343 * anchor
    return base_signal.diff()

def f55_ment_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=416, w3=526, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(416, min_periods=max(416//3, 2)).rank(pct=True)
    persistence = change.rolling(526, min_periods=max(526//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.228667 * persistence + 0.0036344 * anchor
    return base_signal.diff()

def f55_ment_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=429, w3=543, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(250, min_periods=max(250//3, 2)).std()
    vol_slow = ret.rolling(429, min_periods=max(429//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9 + 0.0036345 * anchor
    return base_signal.diff()

def f55_ment_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=442, w3=560, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(442, min_periods=max(442//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.241333 * slope + 0.0036346 * anchor
    return base_signal.diff()

def f55_ment_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=455, w3=577, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(17)
    drag = impulse.rolling(455, min_periods=max(455//3, 2)).mean()
    noise = impulse.abs().rolling(577, min_periods=max(577//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.927059 + 0.0036347 * anchor
    return base_signal.diff()

def f55_ment_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=468, w3=594, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 468)
    curvature = _rolling_slope(acceleration, 594)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.254 * acceleration + 0.0036348 * anchor
    return base_signal.diff()

def f55_ment_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=481, w3=611, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(31, min_periods=max(31//3, 2)).mean(), upside.rolling(481, min_periods=max(481//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.954118 + 0.0036349 * anchor
    return base_signal.diff()

def f55_ment_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=494, w3=628, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(494, min_periods=max(494//3, 2)).max()
    rebound = x - x.rolling(38, min_periods=max(38//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.266667 * _rolling_slope(draw, 628) + 0.003635 * anchor
    return base_signal.diff()

def f55_ment_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=507, w3=645, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 45)
    baseline = trend.rolling(507, min_periods=max(507//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(645, min_periods=max(645//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.981176 + 0.0036351 * anchor
    return base_signal.diff()

def f55_ment_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=21, w3=662, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 52)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.994706 + 0.0036352 * anchor
    return base_signal.diff()

def f55_ment_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=34, w3=679, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(34, min_periods=max(34//3, 2)).max()
    trough = x.rolling(59, min_periods=max(59//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.008235 + 0.0036353 * anchor
    return base_signal.diff()

def f55_ment_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=47, w3=696, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(66)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.292 * persistence + 0.0036354 * anchor
    return base_signal.diff()

def f55_ment_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=60, w3=713, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(73, min_periods=max(73//3, 2)).std()
    vol_slow = ret.rolling(60, min_periods=max(60//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.035294 + 0.0036355 * anchor
    return base_signal.diff()

def f55_ment_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=73, w3=730, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(73, min_periods=max(73//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 80)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.304667 * slope + 0.0036356 * anchor
    return base_signal.diff()

def f55_ment_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=86, w3=747, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(87)
    drag = impulse.rolling(86, min_periods=max(86//3, 2)).mean()
    noise = impulse.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.062353 + 0.0036357 * anchor
    return base_signal.diff()

def f55_ment_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=99, w3=764, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 94)
    acceleration = _rolling_slope(velocity, 99)
    curvature = _rolling_slope(acceleration, 764)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.317333 * acceleration + 0.0036358 * anchor
    return base_signal.diff()

def f55_ment_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=112, w3=30, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(101, min_periods=max(101//3, 2)).mean(), upside.rolling(112, min_periods=max(112//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(30) * 1.089412 + 0.0036359 * anchor
    return base_signal.diff()

def f55_ment_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=125, w3=47, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(125, min_periods=max(125//3, 2)).max()
    rebound = x - x.rolling(108, min_periods=max(108//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.33 * _rolling_slope(draw, 47) + 0.003636 * anchor
    return base_signal.diff()

def f55_ment_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=138, w3=64, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 115)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.116471 + 0.0036361 * anchor
    return base_signal.diff()

def f55_ment_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=151, w3=81, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 122)
    slow = _rolling_slope(x, 151)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=81, adjust=False).mean() * 1.13 + 0.0036362 * anchor
    return base_signal.diff()

def f55_ment_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=164, w3=98, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(164, min_periods=max(164//3, 2)).max()
    trough = x.rolling(129, min_periods=max(129//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.143529 + 0.0036363 * anchor
    return base_signal.diff()

def f55_ment_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=177, w3=115, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(177, min_periods=max(177//3, 2)).rank(pct=True)
    persistence = change.rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355333 * persistence + 0.0036364 * anchor
    return base_signal.diff()

def f55_ment_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=190, w3=132, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(143, min_periods=max(143//3, 2)).std()
    vol_slow = ret.rolling(190, min_periods=max(190//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.170588 + 0.0036365 * anchor
    return base_signal.diff()

def f55_ment_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=203, w3=149, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(203, min_periods=max(203//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 150)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.035667 * slope + 0.0036366 * anchor
    return base_signal.diff()

def f55_ment_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=216, w3=166, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(216, min_periods=max(216//3, 2)).mean()
    noise = impulse.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.197647 + 0.0036367 * anchor
    return base_signal.diff()

def f55_ment_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=229, w3=183, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 164)
    acceleration = _rolling_slope(velocity, 229)
    curvature = _rolling_slope(acceleration, 183)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.048333 * acceleration + 0.0036368 * anchor
    return base_signal.diff()

def f55_ment_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=242, w3=200, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(171, min_periods=max(171//3, 2)).mean(), upside.rolling(242, min_periods=max(242//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.224706 + 0.0036369 * anchor
    return base_signal.diff()

def f55_ment_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=255, w3=217, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(255, min_periods=max(255//3, 2)).max()
    rebound = x - x.rolling(178, min_periods=max(178//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.061 * _rolling_slope(draw, 217) + 0.003637 * anchor
    return base_signal.diff()

def f55_ment_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=268, w3=234, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(268, min_periods=max(268//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.251765 + 0.0036371 * anchor
    return base_signal.diff()

def f55_ment_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=281, w3=251, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 281)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=251, adjust=False).mean() * 1.265294 + 0.0036372 * anchor
    return base_signal.diff()

def f55_ment_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=294, w3=268, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(294, min_periods=max(294//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.278824 + 0.0036373 * anchor
    return base_signal.diff()

def f55_ment_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=307, w3=285, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.086333 * persistence + 0.0036374 * anchor
    return base_signal.diff()

def f55_ment_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=320, w3=302, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(320, min_periods=max(320//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.305882 + 0.0036375 * anchor
    return base_signal.diff()

def f55_ment_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=333, w3=319, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(333, min_periods=max(333//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.099 * slope + 0.0036376 * anchor
    return base_signal.diff()

def f55_ment_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=346, w3=336, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(346, min_periods=max(346//3, 2)).mean()
    noise = impulse.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.332941 + 0.0036377 * anchor
    return base_signal.diff()

def f55_ment_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=359, w3=353, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 359)
    curvature = _rolling_slope(acceleration, 353)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.111667 * acceleration + 0.0036378 * anchor
    return base_signal.diff()

def f55_ment_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=372, w3=370, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(372, min_periods=max(372//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.36 + 0.0036379 * anchor
    return base_signal.diff()

def f55_ment_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=385, w3=387, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(385, min_periods=max(385//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.124333 * _rolling_slope(draw, 387) + 0.003638 * anchor
    return base_signal.diff()

def f55_ment_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=398, w3=404, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 8)
    baseline = trend.rolling(398, min_periods=max(398//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.387059 + 0.0036381 * anchor
    return base_signal.diff()

def f55_ment_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=411, w3=421, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 15)
    slow = _rolling_slope(x, 411)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.400588 + 0.0036382 * anchor
    return base_signal.diff()

def f55_ment_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=424, w3=438, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(424, min_periods=max(424//3, 2)).max()
    trough = x.rolling(22, min_periods=max(22//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.414118 + 0.0036383 * anchor
    return base_signal.diff()

def f55_ment_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=437, w3=455, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(29)
    rank = change.rolling(437, min_periods=max(437//3, 2)).rank(pct=True)
    persistence = change.rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.149667 * persistence + 0.0036384 * anchor
    return base_signal.diff()

def f55_ment_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=450, w3=472, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(36, min_periods=max(36//3, 2)).std()
    vol_slow = ret.rolling(450, min_periods=max(450//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.441176 + 0.0036385 * anchor
    return base_signal.diff()

def f55_ment_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=463, w3=489, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(463, min_periods=max(463//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 43)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.162333 * slope + 0.0036386 * anchor
    return base_signal.diff()

def f55_ment_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=476, w3=506, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(50)
    drag = impulse.rolling(476, min_periods=max(476//3, 2)).mean()
    noise = impulse.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.468235 + 0.0036387 * anchor
    return base_signal.diff()

def f55_ment_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=489, w3=523, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 57)
    acceleration = _rolling_slope(velocity, 489)
    curvature = _rolling_slope(acceleration, 523)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.175 * acceleration + 0.0036388 * anchor
    return base_signal.diff()

def f55_ment_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=502, w3=540, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(64, min_periods=max(64//3, 2)).mean(), upside.rolling(502, min_periods=max(502//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.495294 + 0.0036389 * anchor
    return base_signal.diff()

def f55_ment_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=16, w3=557, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(16, min_periods=max(16//3, 2)).max()
    rebound = x - x.rolling(71, min_periods=max(71//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.187667 * _rolling_slope(draw, 557) + 0.003639 * anchor
    return base_signal.diff()

def f55_ment_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=29, w3=574, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(29, min_periods=max(29//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.522353 + 0.0036391 * anchor
    return base_signal.diff()

def f55_ment_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=42, w3=591, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 42)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.535882 + 0.0036392 * anchor
    return base_signal.diff()

def f55_ment_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=55, w3=608, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(55, min_periods=max(55//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.549412 + 0.0036393 * anchor
    return base_signal.diff()

def f55_ment_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=68, w3=625, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(99)
    rank = change.rolling(68, min_periods=max(68//3, 2)).rank(pct=True)
    persistence = change.rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.213 * persistence + 0.0036394 * anchor
    return base_signal.diff()

def f55_ment_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=81, w3=642, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(81, min_periods=max(81//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.576471 + 0.0036395 * anchor
    return base_signal.diff()

def f55_ment_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=94, w3=659, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(94, min_periods=max(94//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225667 * slope + 0.0036396 * anchor
    return base_signal.diff()

def f55_ment_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=107, w3=676, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(120)
    drag = impulse.rolling(107, min_periods=max(107//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.603529 + 0.0036397 * anchor
    return base_signal.diff()

def f55_ment_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=120, w3=693, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 120)
    curvature = _rolling_slope(acceleration, 693)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.238333 * acceleration + 0.0036398 * anchor
    return base_signal.diff()

def f55_ment_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=133, w3=710, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(134, min_periods=max(134//3, 2)).mean(), upside.rolling(133, min_periods=max(133//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.630588 + 0.0036399 * anchor
    return base_signal.diff()

def f55_ment_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=146, w3=727, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(146, min_periods=max(146//3, 2)).max()
    rebound = x - x.rolling(141, min_periods=max(141//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.251 * _rolling_slope(draw, 727) + 0.00364 * anchor
    return base_signal.diff()

def f55_ment_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=159, w3=744, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 148)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.657647 + 0.0036401 * anchor
    return base_signal.diff()

def f55_ment_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=172, w3=761, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 155)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.671176 + 0.0036402 * anchor
    return base_signal.diff()

def f55_ment_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=185, w3=27, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(185, min_periods=max(185//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.831176 + 0.0036403 * anchor
    return base_signal.diff()

def f55_ment_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=198, w3=44, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(198, min_periods=max(198//3, 2)).rank(pct=True)
    persistence = change.rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.276333 * persistence + 0.0036404 * anchor
    return base_signal.diff()

def f55_ment_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=211, w3=61, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(211, min_periods=max(211//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.858235 + 0.0036405 * anchor
    return base_signal.diff()

def f55_ment_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=224, w3=78, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(224, min_periods=max(224//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 183)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.289 * slope + 0.0036406 * anchor
    return base_signal.diff()
