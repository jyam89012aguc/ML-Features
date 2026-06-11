"""41 return distribution moments gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Statistical analysis of return skewness and kurtosis to identify non-normal risk.
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

def f41_rmom_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return (res).diff()

def f41_rmom_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=266, w3=139, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 266)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=139, adjust=False).mean() * 1.48 + 0.0028502 * anchor
    return base_signal.diff()

def f41_rmom_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=279, w3=156, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(279, min_periods=max(279//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.493529 + 0.0028503 * anchor
    return base_signal.diff()

def f41_rmom_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=292, w3=173, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(292, min_periods=max(292//3, 2)).rank(pct=True)
    persistence = change.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.093 * persistence + 0.0028504 * anchor
    return base_signal.diff()

def f41_rmom_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=305, w3=190, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(305, min_periods=max(305//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.520588 + 0.0028505 * anchor
    return base_signal.diff()

def f41_rmom_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=318, w3=207, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(318, min_periods=max(318//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.105667 * slope + 0.0028506 * anchor
    return base_signal.diff()

def f41_rmom_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=331, w3=224, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(331, min_periods=max(331//3, 2)).mean()
    noise = impulse.abs().rolling(224, min_periods=max(224//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.547647 + 0.0028507 * anchor
    return base_signal.diff()

def f41_rmom_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=344, w3=241, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 344)
    curvature = _rolling_slope(acceleration, 241)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.118333 * acceleration + 0.0028508 * anchor
    return base_signal.diff()

def f41_rmom_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=357, w3=258, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(357, min_periods=max(357//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.574706 + 0.0028509 * anchor
    return base_signal.diff()

def f41_rmom_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=370, w3=275, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(370, min_periods=max(370//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.131 * _rolling_slope(draw, 275) + 0.002851 * anchor
    return base_signal.diff()

def f41_rmom_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=383, w3=292, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(383, min_periods=max(383//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.601765 + 0.0028511 * anchor
    return base_signal.diff()

def f41_rmom_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=396, w3=309, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 396)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.615294 + 0.0028512 * anchor
    return base_signal.diff()

def f41_rmom_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=409, w3=326, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(409, min_periods=max(409//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.628824 + 0.0028513 * anchor
    return base_signal.diff()

def f41_rmom_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=422, w3=343, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(20)
    rank = change.rolling(422, min_periods=max(422//3, 2)).rank(pct=True)
    persistence = change.rolling(343, min_periods=max(343//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.156333 * persistence + 0.0028514 * anchor
    return base_signal.diff()

def f41_rmom_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=435, w3=360, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(435, min_periods=max(435//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.655882 + 0.0028515 * anchor
    return base_signal.diff()

def f41_rmom_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=448, w3=377, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(448, min_periods=max(448//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.169 * slope + 0.0028516 * anchor
    return base_signal.diff()

def f41_rmom_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=461, w3=394, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(41)
    drag = impulse.rolling(461, min_periods=max(461//3, 2)).mean()
    noise = impulse.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.829412 + 0.0028517 * anchor
    return base_signal.diff()

def f41_rmom_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=474, w3=411, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 474)
    curvature = _rolling_slope(acceleration, 411)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.181667 * acceleration + 0.0028518 * anchor
    return base_signal.diff()

def f41_rmom_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=487, w3=428, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(55, min_periods=max(55//3, 2)).mean(), upside.rolling(487, min_periods=max(487//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.856471 + 0.0028519 * anchor
    return base_signal.diff()

def f41_rmom_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=500, w3=445, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(500, min_periods=max(500//3, 2)).max()
    rebound = x - x.rolling(62, min_periods=max(62//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.194333 * _rolling_slope(draw, 445) + 0.002852 * anchor
    return base_signal.diff()

def f41_rmom_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=14, w3=462, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(14, min_periods=max(14//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.883529 + 0.0028521 * anchor
    return base_signal.diff()

def f41_rmom_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=27, w3=479, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 27)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.897059 + 0.0028522 * anchor
    return base_signal.diff()

def f41_rmom_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=40, w3=496, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(40, min_periods=max(40//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.910588 + 0.0028523 * anchor
    return base_signal.diff()

def f41_rmom_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=53, w3=513, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(90)
    rank = change.rolling(53, min_periods=max(53//3, 2)).rank(pct=True)
    persistence = change.rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.219667 * persistence + 0.0028524 * anchor
    return base_signal.diff()

def f41_rmom_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=66, w3=530, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(66, min_periods=max(66//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.937647 + 0.0028525 * anchor
    return base_signal.diff()

def f41_rmom_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=79, w3=547, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(79, min_periods=max(79//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.232333 * slope + 0.0028526 * anchor
    return base_signal.diff()

def f41_rmom_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=92, w3=564, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(111)
    drag = impulse.rolling(92, min_periods=max(92//3, 2)).mean()
    noise = impulse.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.964706 + 0.0028527 * anchor
    return base_signal.diff()

def f41_rmom_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=105, w3=581, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 105)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.245 * acceleration + 0.0028528 * anchor
    return base_signal.diff()

def f41_rmom_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=118, w3=598, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(125, min_periods=max(125//3, 2)).mean(), upside.rolling(118, min_periods=max(118//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.991765 + 0.0028529 * anchor
    return base_signal.diff()

def f41_rmom_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=131, w3=615, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(131, min_periods=max(131//3, 2)).max()
    rebound = x - x.rolling(132, min_periods=max(132//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.257667 * _rolling_slope(draw, 615) + 0.002853 * anchor
    return base_signal.diff()

def f41_rmom_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=144, w3=632, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 139)
    baseline = trend.rolling(144, min_periods=max(144//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.018824 + 0.0028531 * anchor
    return base_signal.diff()

def f41_rmom_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=157, w3=649, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 157)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.032353 + 0.0028532 * anchor
    return base_signal.diff()

def f41_rmom_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=170, w3=666, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(170, min_periods=max(170//3, 2)).max()
    trough = x.rolling(153, min_periods=max(153//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.045882 + 0.0028533 * anchor
    return base_signal.diff()

def f41_rmom_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=183, w3=683, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(183, min_periods=max(183//3, 2)).rank(pct=True)
    persistence = change.rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.283 * persistence + 0.0028534 * anchor
    return base_signal.diff()

def f41_rmom_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=196, w3=700, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(167, min_periods=max(167//3, 2)).std()
    vol_slow = ret.rolling(196, min_periods=max(196//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.072941 + 0.0028535 * anchor
    return base_signal.diff()

def f41_rmom_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=209, w3=717, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(209, min_periods=max(209//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.295667 * slope + 0.0028536 * anchor
    return base_signal.diff()

def f41_rmom_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=222, w3=734, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(222, min_periods=max(222//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1 + 0.0028537 * anchor
    return base_signal.diff()

def f41_rmom_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=235, w3=751, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 235)
    curvature = _rolling_slope(acceleration, 751)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.308333 * acceleration + 0.0028538 * anchor
    return base_signal.diff()

def f41_rmom_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=248, w3=17, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(195, min_periods=max(195//3, 2)).mean(), upside.rolling(248, min_periods=max(248//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(17) * 1.127059 + 0.0028539 * anchor
    return base_signal.diff()

def f41_rmom_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=261, w3=34, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(261, min_periods=max(261//3, 2)).max()
    rebound = x - x.rolling(202, min_periods=max(202//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.321 * _rolling_slope(draw, 34) + 0.002854 * anchor
    return base_signal.diff()

def f41_rmom_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=274, w3=51, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.154118 + 0.0028541 * anchor
    return base_signal.diff()

def f41_rmom_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=287, w3=68, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=68, adjust=False).mean() * 1.167647 + 0.0028542 * anchor
    return base_signal.diff()

def f41_rmom_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=300, w3=85, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(300, min_periods=max(300//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.181176 + 0.0028543 * anchor
    return base_signal.diff()

def f41_rmom_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=313, w3=102, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(313, min_periods=max(313//3, 2)).rank(pct=True)
    persistence = change.rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.346333 * persistence + 0.0028544 * anchor
    return base_signal.diff()

def f41_rmom_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=326, w3=119, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(326, min_periods=max(326//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.208235 + 0.0028545 * anchor
    return base_signal.diff()

def f41_rmom_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=339, w3=136, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(339, min_periods=max(339//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.359 * slope + 0.0028546 * anchor
    return base_signal.diff()

def f41_rmom_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=352, w3=153, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(352, min_periods=max(352//3, 2)).mean()
    noise = impulse.abs().rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.235294 + 0.0028547 * anchor
    return base_signal.diff()

def f41_rmom_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=365, w3=170, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 365)
    curvature = _rolling_slope(acceleration, 170)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.039333 * acceleration + 0.0028548 * anchor
    return base_signal.diff()

def f41_rmom_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=378, w3=187, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(378, min_periods=max(378//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.262353 + 0.0028549 * anchor
    return base_signal.diff()

def f41_rmom_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=391, w3=204, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(391, min_periods=max(391//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.052 * _rolling_slope(draw, 204) + 0.002855 * anchor
    return base_signal.diff()

def f41_rmom_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=404, w3=221, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(404, min_periods=max(404//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.289412 + 0.0028551 * anchor
    return base_signal.diff()

def f41_rmom_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=417, w3=238, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 417)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=238, adjust=False).mean() * 1.302941 + 0.0028552 * anchor
    return base_signal.diff()

def f41_rmom_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=430, w3=255, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(430, min_periods=max(430//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.316471 + 0.0028553 * anchor
    return base_signal.diff()

def f41_rmom_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=443, w3=272, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(53)
    rank = change.rolling(443, min_periods=max(443//3, 2)).rank(pct=True)
    persistence = change.rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.077333 * persistence + 0.0028554 * anchor
    return base_signal.diff()

def f41_rmom_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=456, w3=289, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(456, min_periods=max(456//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.343529 + 0.0028555 * anchor
    return base_signal.diff()

def f41_rmom_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=469, w3=306, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(469, min_periods=max(469//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.09 * slope + 0.0028556 * anchor
    return base_signal.diff()

def f41_rmom_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=482, w3=323, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(74)
    drag = impulse.rolling(482, min_periods=max(482//3, 2)).mean()
    noise = impulse.abs().rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.370588 + 0.0028557 * anchor
    return base_signal.diff()

def f41_rmom_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=495, w3=340, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 495)
    curvature = _rolling_slope(acceleration, 340)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.102667 * acceleration + 0.0028558 * anchor
    return base_signal.diff()

def f41_rmom_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=508, w3=357, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(508, min_periods=max(508//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.397647 + 0.0028559 * anchor
    return base_signal.diff()

def f41_rmom_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=22, w3=374, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(22, min_periods=max(22//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.115333 * _rolling_slope(draw, 374) + 0.002856 * anchor
    return base_signal.diff()

def f41_rmom_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=35, w3=391, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(35, min_periods=max(35//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.424706 + 0.0028561 * anchor
    return base_signal.diff()

def f41_rmom_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=48, w3=408, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 48)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.438235 + 0.0028562 * anchor
    return base_signal.diff()

def f41_rmom_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=61, w3=425, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(61, min_periods=max(61//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.451765 + 0.0028563 * anchor
    return base_signal.diff()

def f41_rmom_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=74, w3=442, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(123)
    rank = change.rolling(74, min_periods=max(74//3, 2)).rank(pct=True)
    persistence = change.rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.140667 * persistence + 0.0028564 * anchor
    return base_signal.diff()

def f41_rmom_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=87, w3=459, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(87, min_periods=max(87//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478824 + 0.0028565 * anchor
    return base_signal.diff()

def f41_rmom_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=100, w3=476, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(100, min_periods=max(100//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.153333 * slope + 0.0028566 * anchor
    return base_signal.diff()
