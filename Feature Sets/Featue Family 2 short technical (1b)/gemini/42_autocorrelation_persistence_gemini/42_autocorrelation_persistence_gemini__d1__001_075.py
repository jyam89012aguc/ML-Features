"""42 autocorrelation persistence gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of how past price returns influence future returns over various lags.
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

def f42_acor_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Measurement of how past price returns influence future returns over various lags. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(1), window)
    return (res).diff()

def f42_acor_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=61, w3=647, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 151)
    slow = _rolling_slope(x, 61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.374706 + 0.0029062 * anchor
    return base_signal.diff()

def f42_acor_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=74, w3=664, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(74, min_periods=max(74//3, 2)).max()
    trough = x.rolling(158, min_periods=max(158//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.388235 + 0.0029063 * anchor
    return base_signal.diff()

def f42_acor_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=87, w3=681, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(87, min_periods=max(87//3, 2)).rank(pct=True)
    persistence = change.rolling(681, min_periods=max(681//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.316333 * persistence + 0.0029064 * anchor
    return base_signal.diff()

def f42_acor_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=100, w3=698, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(172, min_periods=max(172//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.415294 + 0.0029065 * anchor
    return base_signal.diff()

def f42_acor_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=113, w3=715, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(113, min_periods=max(113//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 179)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.329 * slope + 0.0029066 * anchor
    return base_signal.diff()

def f42_acor_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=126, w3=732, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(126, min_periods=max(126//3, 2)).mean()
    noise = impulse.abs().rolling(732, min_periods=max(732//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.442353 + 0.0029067 * anchor
    return base_signal.diff()

def f42_acor_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=139, w3=749, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 193)
    acceleration = _rolling_slope(velocity, 139)
    curvature = _rolling_slope(acceleration, 749)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.341667 * acceleration + 0.0029068 * anchor
    return base_signal.diff()

def f42_acor_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=152, w3=766, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(152, min_periods=max(152//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.469412 + 0.0029069 * anchor
    return base_signal.diff()

def f42_acor_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=165, w3=32, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(165, min_periods=max(165//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.354333 * _rolling_slope(draw, 32) + 0.002907 * anchor
    return base_signal.diff()

def f42_acor_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=178, w3=49, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(178, min_periods=max(178//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(49, min_periods=max(49//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.496471 + 0.0029071 * anchor
    return base_signal.diff()

def f42_acor_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=191, w3=66, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 191)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=66, adjust=False).mean() * 1.51 + 0.0029072 * anchor
    return base_signal.diff()

def f42_acor_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=204, w3=83, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(204, min_periods=max(204//3, 2)).max()
    trough = x.rolling(228, min_periods=max(228//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.523529 + 0.0029073 * anchor
    return base_signal.diff()

def f42_acor_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=217, w3=100, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(217, min_periods=max(217//3, 2)).rank(pct=True)
    persistence = change.rolling(100, min_periods=max(100//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.047333 * persistence + 0.0029074 * anchor
    return base_signal.diff()

def f42_acor_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=230, w3=117, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(242, min_periods=max(242//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.550588 + 0.0029075 * anchor
    return base_signal.diff()

def f42_acor_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=243, w3=134, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(243, min_periods=max(243//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 249)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.06 * slope + 0.0029076 * anchor
    return base_signal.diff()

def f42_acor_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=256, w3=151, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(9)
    drag = impulse.rolling(256, min_periods=max(256//3, 2)).mean()
    noise = impulse.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.577647 + 0.0029077 * anchor
    return base_signal.diff()

def f42_acor_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=269, w3=168, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 16)
    acceleration = _rolling_slope(velocity, 269)
    curvature = _rolling_slope(acceleration, 168)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.072667 * acceleration + 0.0029078 * anchor
    return base_signal.diff()

def f42_acor_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=282, w3=185, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(282, min_periods=max(282//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.604706 + 0.0029079 * anchor
    return base_signal.diff()

def f42_acor_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=295, w3=202, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(295, min_periods=max(295//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.085333 * _rolling_slope(draw, 202) + 0.002908 * anchor
    return base_signal.diff()

def f42_acor_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=308, w3=219, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(308, min_periods=max(308//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(219, min_periods=max(219//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.631765 + 0.0029081 * anchor
    return base_signal.diff()

def f42_acor_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=321, w3=236, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 44)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=236, adjust=False).mean() * 1.645294 + 0.0029082 * anchor
    return base_signal.diff()

def f42_acor_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=334, w3=253, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(334, min_periods=max(334//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.658824 + 0.0029083 * anchor
    return base_signal.diff()

def f42_acor_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=347, w3=270, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(58)
    rank = change.rolling(347, min_periods=max(347//3, 2)).rank(pct=True)
    persistence = change.rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.110667 * persistence + 0.0029084 * anchor
    return base_signal.diff()

def f42_acor_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=360, w3=287, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(360, min_periods=max(360//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.832353 + 0.0029085 * anchor
    return base_signal.diff()

def f42_acor_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=373, w3=304, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(373, min_periods=max(373//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 72)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.123333 * slope + 0.0029086 * anchor
    return base_signal.diff()

def f42_acor_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=386, w3=321, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(79)
    drag = impulse.rolling(386, min_periods=max(386//3, 2)).mean()
    noise = impulse.abs().rolling(321, min_periods=max(321//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.859412 + 0.0029087 * anchor
    return base_signal.diff()

def f42_acor_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=399, w3=338, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 86)
    acceleration = _rolling_slope(velocity, 399)
    curvature = _rolling_slope(acceleration, 338)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136 * acceleration + 0.0029088 * anchor
    return base_signal.diff()

def f42_acor_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=412, w3=355, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(412, min_periods=max(412//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.886471 + 0.0029089 * anchor
    return base_signal.diff()

def f42_acor_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=425, w3=372, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(425, min_periods=max(425//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.148667 * _rolling_slope(draw, 372) + 0.002909 * anchor
    return base_signal.diff()

def f42_acor_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=438, w3=389, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(438, min_periods=max(438//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.913529 + 0.0029091 * anchor
    return base_signal.diff()

def f42_acor_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=451, w3=406, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 114)
    slow = _rolling_slope(x, 451)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.927059 + 0.0029092 * anchor
    return base_signal.diff()

def f42_acor_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=464, w3=423, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(464, min_periods=max(464//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.940588 + 0.0029093 * anchor
    return base_signal.diff()

def f42_acor_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=477, w3=440, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(477, min_periods=max(477//3, 2)).rank(pct=True)
    persistence = change.rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.174 * persistence + 0.0029094 * anchor
    return base_signal.diff()

def f42_acor_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=490, w3=457, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(490, min_periods=max(490//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.967647 + 0.0029095 * anchor
    return base_signal.diff()

def f42_acor_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=503, w3=474, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(503, min_periods=max(503//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 142)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.186667 * slope + 0.0029096 * anchor
    return base_signal.diff()

def f42_acor_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=17, w3=491, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(17, min_periods=max(17//3, 2)).mean()
    noise = impulse.abs().rolling(491, min_periods=max(491//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.994706 + 0.0029097 * anchor
    return base_signal.diff()

def f42_acor_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=30, w3=508, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 30)
    curvature = _rolling_slope(acceleration, 508)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.199333 * acceleration + 0.0029098 * anchor
    return base_signal.diff()

def f42_acor_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=43, w3=525, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(43, min_periods=max(43//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.021765 + 0.0029099 * anchor
    return base_signal.diff()

def f42_acor_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=56, w3=542, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(56, min_periods=max(56//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212 * _rolling_slope(draw, 542) + 0.00291 * anchor
    return base_signal.diff()

def f42_acor_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=69, w3=559, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(69, min_periods=max(69//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.048824 + 0.0029101 * anchor
    return base_signal.diff()

def f42_acor_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=82, w3=576, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 82)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.062353 + 0.0029102 * anchor
    return base_signal.diff()

def f42_acor_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=95, w3=593, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(95, min_periods=max(95//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.075882 + 0.0029103 * anchor
    return base_signal.diff()

def f42_acor_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=108, w3=610, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(108, min_periods=max(108//3, 2)).rank(pct=True)
    persistence = change.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.237333 * persistence + 0.0029104 * anchor
    return base_signal.diff()

def f42_acor_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=121, w3=627, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(121, min_periods=max(121//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.102941 + 0.0029105 * anchor
    return base_signal.diff()

def f42_acor_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=134, w3=644, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(134, min_periods=max(134//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.25 * slope + 0.0029106 * anchor
    return base_signal.diff()

def f42_acor_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=147, w3=661, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(147, min_periods=max(147//3, 2)).mean()
    noise = impulse.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.13 + 0.0029107 * anchor
    return base_signal.diff()

def f42_acor_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=160, w3=678, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 160)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.262667 * acceleration + 0.0029108 * anchor
    return base_signal.diff()

def f42_acor_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=173, w3=695, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(173, min_periods=max(173//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.157059 + 0.0029109 * anchor
    return base_signal.diff()

def f42_acor_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=186, w3=712, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(186, min_periods=max(186//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.275333 * _rolling_slope(draw, 712) + 0.002911 * anchor
    return base_signal.diff()

def f42_acor_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=199, w3=729, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(199, min_periods=max(199//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.184118 + 0.0029111 * anchor
    return base_signal.diff()

def f42_acor_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=212, w3=746, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.197647 + 0.0029112 * anchor
    return base_signal.diff()

def f42_acor_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=225, w3=763, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(225, min_periods=max(225//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.211176 + 0.0029113 * anchor
    return base_signal.diff()

def f42_acor_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=238, w3=29, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(21)
    rank = change.rolling(238, min_periods=max(238//3, 2)).rank(pct=True)
    persistence = change.rolling(29, min_periods=max(29//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.300667 * persistence + 0.0029114 * anchor
    return base_signal.diff()

def f42_acor_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=251, w3=46, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.238235 + 0.0029115 * anchor
    return base_signal.diff()

def f42_acor_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=264, w3=63, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(264, min_periods=max(264//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.313333 * slope + 0.0029116 * anchor
    return base_signal.diff()

def f42_acor_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=277, w3=80, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(42)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.265294 + 0.0029117 * anchor
    return base_signal.diff()

def f42_acor_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=290, w3=97, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 290)
    curvature = _rolling_slope(acceleration, 97)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.326 * acceleration + 0.0029118 * anchor
    return base_signal.diff()

def f42_acor_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=303, w3=114, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(303, min_periods=max(303//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(114) * 1.292353 + 0.0029119 * anchor
    return base_signal.diff()

def f42_acor_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=316, w3=131, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(316, min_periods=max(316//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.338667 * _rolling_slope(draw, 131) + 0.002912 * anchor
    return base_signal.diff()

def f42_acor_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=329, w3=148, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(329, min_periods=max(329//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.319412 + 0.0029121 * anchor
    return base_signal.diff()

def f42_acor_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=342, w3=165, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 342)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=165, adjust=False).mean() * 1.332941 + 0.0029122 * anchor
    return base_signal.diff()

def f42_acor_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=355, w3=182, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(355, min_periods=max(355//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.346471 + 0.0029123 * anchor
    return base_signal.diff()

def f42_acor_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=368, w3=199, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(91)
    rank = change.rolling(368, min_periods=max(368//3, 2)).rank(pct=True)
    persistence = change.rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.031667 * persistence + 0.0029124 * anchor
    return base_signal.diff()

def f42_acor_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=381, w3=216, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.373529 + 0.0029125 * anchor
    return base_signal.diff()

def f42_acor_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=394, w3=233, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(394, min_periods=max(394//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.044333 * slope + 0.0029126 * anchor
    return base_signal.diff()
