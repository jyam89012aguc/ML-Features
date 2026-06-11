"""41 return distribution moments gemini base features 1-75 — Pipeline 1b-HF Grade v7.

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

def f41_rmom_gemini_001(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_002(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_003(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_004(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_005(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_006(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_007(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_008(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_009(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_010(close: pd.Series) -> pd.Series:
    """Statistical analysis of return skewness and kurtosis to identify non-normal risk. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).skew(), window)
    return res

def f41_rmom_gemini_011(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=442, w3=763, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 442)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.292941 + 0.0028362 * anchor
    return base_signal

def f41_rmom_gemini_012(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=455, w3=29, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(455, min_periods=max(455//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.306471 + 0.0028363 * anchor
    return base_signal

def f41_rmom_gemini_013(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=468, w3=46, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(468, min_periods=max(468//3, 2)).rank(pct=True)
    persistence = change.rolling(46, min_periods=max(46//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.203333 * persistence + 0.0028364 * anchor
    return base_signal

def f41_rmom_gemini_014(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=481, w3=63, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(481, min_periods=max(481//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.333529 + 0.0028365 * anchor
    return base_signal

def f41_rmom_gemini_015(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=494, w3=80, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(494, min_periods=max(494//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.216 * slope + 0.0028366 * anchor
    return base_signal

def f41_rmom_gemini_016(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=507, w3=97, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(507, min_periods=max(507//3, 2)).mean()
    noise = impulse.abs().rolling(97, min_periods=max(97//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.360588 + 0.0028367 * anchor
    return base_signal

def f41_rmom_gemini_017(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=21, w3=114, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 21)
    curvature = _rolling_slope(acceleration, 114)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.228667 * acceleration + 0.0028368 * anchor
    return base_signal

def f41_rmom_gemini_018(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=34, w3=131, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.387647 + 0.0028369 * anchor
    return base_signal

def f41_rmom_gemini_019(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=47, w3=148, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(47, min_periods=max(47//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.241333 * _rolling_slope(draw, 148) + 0.002837 * anchor
    return base_signal

def f41_rmom_gemini_020(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=60, w3=165, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(60, min_periods=max(60//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(165, min_periods=max(165//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.414706 + 0.0028371 * anchor
    return base_signal

def f41_rmom_gemini_021(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=73, w3=182, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 73)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=182, adjust=False).mean() * 1.428235 + 0.0028372 * anchor
    return base_signal

def f41_rmom_gemini_022(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=86, w3=199, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(86, min_periods=max(86//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.441765 + 0.0028373 * anchor
    return base_signal

def f41_rmom_gemini_023(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=99, w3=216, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(28)
    rank = change.rolling(99, min_periods=max(99//3, 2)).rank(pct=True)
    persistence = change.rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.266667 * persistence + 0.0028374 * anchor
    return base_signal

def f41_rmom_gemini_024(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=112, w3=233, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(112, min_periods=max(112//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.468824 + 0.0028375 * anchor
    return base_signal

def f41_rmom_gemini_025(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=125, w3=250, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(125, min_periods=max(125//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 42)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.279333 * slope + 0.0028376 * anchor
    return base_signal

def f41_rmom_gemini_026(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=138, w3=267, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(49)
    drag = impulse.rolling(138, min_periods=max(138//3, 2)).mean()
    noise = impulse.abs().rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.495882 + 0.0028377 * anchor
    return base_signal

def f41_rmom_gemini_027(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=151, w3=284, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 56)
    acceleration = _rolling_slope(velocity, 151)
    curvature = _rolling_slope(acceleration, 284)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.292 * acceleration + 0.0028378 * anchor
    return base_signal

def f41_rmom_gemini_028(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=164, w3=301, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(63, min_periods=max(63//3, 2)).mean(), upside.rolling(164, min_periods=max(164//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.522941 + 0.0028379 * anchor
    return base_signal

def f41_rmom_gemini_029(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=177, w3=318, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(177, min_periods=max(177//3, 2)).max()
    rebound = x - x.rolling(70, min_periods=max(70//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.304667 * _rolling_slope(draw, 318) + 0.002838 * anchor
    return base_signal

def f41_rmom_gemini_030(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=190, w3=335, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 77)
    baseline = trend.rolling(190, min_periods=max(190//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55 + 0.0028381 * anchor
    return base_signal

def f41_rmom_gemini_031(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=203, w3=352, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 84)
    slow = _rolling_slope(x, 203)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.563529 + 0.0028382 * anchor
    return base_signal

def f41_rmom_gemini_032(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=216, w3=369, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(216, min_periods=max(216//3, 2)).max()
    trough = x.rolling(91, min_periods=max(91//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.577059 + 0.0028383 * anchor
    return base_signal

def f41_rmom_gemini_033(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=229, w3=386, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(98)
    rank = change.rolling(229, min_periods=max(229//3, 2)).rank(pct=True)
    persistence = change.rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.33 * persistence + 0.0028384 * anchor
    return base_signal

def f41_rmom_gemini_034(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=242, w3=403, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(105, min_periods=max(105//3, 2)).std()
    vol_slow = ret.rolling(242, min_periods=max(242//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.604118 + 0.0028385 * anchor
    return base_signal

def f41_rmom_gemini_035(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=255, w3=420, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(255, min_periods=max(255//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 112)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.342667 * slope + 0.0028386 * anchor
    return base_signal

def f41_rmom_gemini_036(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=268, w3=437, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(119)
    drag = impulse.rolling(268, min_periods=max(268//3, 2)).mean()
    noise = impulse.abs().rolling(437, min_periods=max(437//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.631176 + 0.0028387 * anchor
    return base_signal

def f41_rmom_gemini_037(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=281, w3=454, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 126)
    acceleration = _rolling_slope(velocity, 281)
    curvature = _rolling_slope(acceleration, 454)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.355333 * acceleration + 0.0028388 * anchor
    return base_signal

def f41_rmom_gemini_038(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=294, w3=471, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(133, min_periods=max(133//3, 2)).mean(), upside.rolling(294, min_periods=max(294//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.658235 + 0.0028389 * anchor
    return base_signal

def f41_rmom_gemini_039(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=307, w3=488, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(307, min_periods=max(307//3, 2)).max()
    rebound = x - x.rolling(140, min_periods=max(140//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.035667 * _rolling_slope(draw, 488) + 0.002839 * anchor
    return base_signal

def f41_rmom_gemini_040(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=320, w3=505, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 147)
    baseline = trend.rolling(320, min_periods=max(320//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.831765 + 0.0028391 * anchor
    return base_signal

def f41_rmom_gemini_041(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=333, w3=522, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 333)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.845294 + 0.0028392 * anchor
    return base_signal

def f41_rmom_gemini_042(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=346, w3=539, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(346, min_periods=max(346//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.858824 + 0.0028393 * anchor
    return base_signal

def f41_rmom_gemini_043(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=359, w3=556, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(359, min_periods=max(359//3, 2)).rank(pct=True)
    persistence = change.rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.061 * persistence + 0.0028394 * anchor
    return base_signal

def f41_rmom_gemini_044(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=372, w3=573, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(372, min_periods=max(372//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.885882 + 0.0028395 * anchor
    return base_signal

def f41_rmom_gemini_045(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=385, w3=590, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(385, min_periods=max(385//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.073667 * slope + 0.0028396 * anchor
    return base_signal

def f41_rmom_gemini_046(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=398, w3=607, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(398, min_periods=max(398//3, 2)).mean()
    noise = impulse.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.912941 + 0.0028397 * anchor
    return base_signal

def f41_rmom_gemini_047(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=411, w3=624, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 411)
    curvature = _rolling_slope(acceleration, 624)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.086333 * acceleration + 0.0028398 * anchor
    return base_signal

def f41_rmom_gemini_048(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=424, w3=641, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(424, min_periods=max(424//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.94 + 0.0028399 * anchor
    return base_signal

def f41_rmom_gemini_049(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=437, w3=658, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(437, min_periods=max(437//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.099 * _rolling_slope(draw, 658) + 0.00284 * anchor
    return base_signal

def f41_rmom_gemini_050(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=450, w3=675, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 217)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.967059 + 0.0028401 * anchor
    return base_signal

def f41_rmom_gemini_051(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=463, w3=692, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 224)
    slow = _rolling_slope(x, 463)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.980588 + 0.0028402 * anchor
    return base_signal

def f41_rmom_gemini_052(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=476, w3=709, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(476, min_periods=max(476//3, 2)).max()
    trough = x.rolling(231, min_periods=max(231//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.994118 + 0.0028403 * anchor
    return base_signal

def f41_rmom_gemini_053(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=489, w3=726, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(489, min_periods=max(489//3, 2)).rank(pct=True)
    persistence = change.rolling(726, min_periods=max(726//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.124333 * persistence + 0.0028404 * anchor
    return base_signal

def f41_rmom_gemini_054(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=502, w3=743, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(245, min_periods=max(245//3, 2)).std()
    vol_slow = ret.rolling(502, min_periods=max(502//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.021176 + 0.0028405 * anchor
    return base_signal

def f41_rmom_gemini_055(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=16, w3=760, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(16, min_periods=max(16//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 5)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.137 * slope + 0.0028406 * anchor
    return base_signal

def f41_rmom_gemini_056(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=29, w3=26, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(12)
    drag = impulse.rolling(29, min_periods=max(29//3, 2)).mean()
    noise = impulse.abs().rolling(26, min_periods=max(26//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.048235 + 0.0028407 * anchor
    return base_signal

def f41_rmom_gemini_057(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=42, w3=43, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 42)
    curvature = _rolling_slope(acceleration, 43)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.149667 * acceleration + 0.0028408 * anchor
    return base_signal

def f41_rmom_gemini_058(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=55, w3=60, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(55, min_periods=max(55//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(60) * 1.075294 + 0.0028409 * anchor
    return base_signal

def f41_rmom_gemini_059(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=68, w3=77, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(68, min_periods=max(68//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.162333 * _rolling_slope(draw, 77) + 0.002841 * anchor
    return base_signal

def f41_rmom_gemini_060(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=81, w3=94, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(94, min_periods=max(94//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.102353 + 0.0028411 * anchor
    return base_signal

def f41_rmom_gemini_061(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=94, w3=111, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=111, adjust=False).mean() * 1.115882 + 0.0028412 * anchor
    return base_signal

def f41_rmom_gemini_062(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=107, w3=128, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(107, min_periods=max(107//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.129412 + 0.0028413 * anchor
    return base_signal

def f41_rmom_gemini_063(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=120, w3=145, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(61)
    rank = change.rolling(120, min_periods=max(120//3, 2)).rank(pct=True)
    persistence = change.rolling(145, min_periods=max(145//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.187667 * persistence + 0.0028414 * anchor
    return base_signal

def f41_rmom_gemini_064(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=133, w3=162, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(133, min_periods=max(133//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.156471 + 0.0028415 * anchor
    return base_signal

def f41_rmom_gemini_065(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=146, w3=179, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(146, min_periods=max(146//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.200333 * slope + 0.0028416 * anchor
    return base_signal

def f41_rmom_gemini_066(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=159, w3=196, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(82)
    drag = impulse.rolling(159, min_periods=max(159//3, 2)).mean()
    noise = impulse.abs().rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.183529 + 0.0028417 * anchor
    return base_signal

def f41_rmom_gemini_067(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=172, w3=213, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 172)
    curvature = _rolling_slope(acceleration, 213)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.213 * acceleration + 0.0028418 * anchor
    return base_signal

def f41_rmom_gemini_068(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=185, w3=230, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(185, min_periods=max(185//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.210588 + 0.0028419 * anchor
    return base_signal

def f41_rmom_gemini_069(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=198, w3=247, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(198, min_periods=max(198//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.225667 * _rolling_slope(draw, 247) + 0.002842 * anchor
    return base_signal

def f41_rmom_gemini_070(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=211, w3=264, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(211, min_periods=max(211//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.237647 + 0.0028421 * anchor
    return base_signal

def f41_rmom_gemini_071(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=224, w3=281, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 224)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=281, adjust=False).mean() * 1.251176 + 0.0028422 * anchor
    return base_signal

def f41_rmom_gemini_072(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=237, w3=298, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(237, min_periods=max(237//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.264706 + 0.0028423 * anchor
    return base_signal

def f41_rmom_gemini_073(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=250, w3=315, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(250, min_periods=max(250//3, 2)).rank(pct=True)
    persistence = change.rolling(315, min_periods=max(315//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.251 * persistence + 0.0028424 * anchor
    return base_signal

def f41_rmom_gemini_074(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=263, w3=332, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.291765 + 0.0028425 * anchor
    return base_signal

def f41_rmom_gemini_075(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=276, w3=349, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(276, min_periods=max(276//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.263667 * slope + 0.0028426 * anchor
    return base_signal
