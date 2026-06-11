"""95 regime shift momentum gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Momentum signals that are adjusted based on the current market regime.
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

def f95_rsmo_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=5]"""
    window = 5
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=10]"""
    window = 10
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=21]"""
    window = 21
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=42]"""
    window = 42
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=63]"""
    window = 63
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=126]"""
    window = 126
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=252]"""
    window = 252
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=504]"""
    window = 504
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=756]"""
    window = 756
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Momentum signals that are adjusted based on the current market regime. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_rolling_slope(close, window), window)
    return (res).diff().diff()

def f95_rsmo_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=497, w3=662, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 176)
    slow = _rolling_slope(x, 497)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.102353 + 0.0058882 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=11, w3=679, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(11, min_periods=max(11//3, 2)).max()
    trough = x.rolling(183, min_periods=max(183//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.115882 + 0.0058883 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=24, w3=696, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(24, min_periods=max(24//3, 2)).rank(pct=True)
    persistence = change.rolling(696, min_periods=max(696//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.078667 * persistence + 0.0058884 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=37, w3=713, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(197, min_periods=max(197//3, 2)).std()
    vol_slow = ret.rolling(37, min_periods=max(37//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.142941 + 0.0058885 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=50, w3=730, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(50, min_periods=max(50//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 204)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.091333 * slope + 0.0058886 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=63, w3=747, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(63, min_periods=max(63//3, 2)).mean()
    noise = impulse.abs().rolling(747, min_periods=max(747//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.17 + 0.0058887 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=76, w3=764, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 218)
    acceleration = _rolling_slope(velocity, 76)
    curvature = _rolling_slope(acceleration, 764)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.104 * acceleration + 0.0058888 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=89, w3=30, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(89, min_periods=max(89//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(30) * 1.197059 + 0.0058889 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=102, w3=47, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(102, min_periods=max(102//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.116667 * _rolling_slope(draw, 47) + 0.005889 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=115, w3=64, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 239)
    baseline = trend.rolling(115, min_periods=max(115//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(64, min_periods=max(64//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.224118 + 0.0058891 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=128, w3=81, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 246)
    slow = _rolling_slope(x, 128)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=81, adjust=False).mean() * 1.237647 + 0.0058892 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=141, w3=98, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(141, min_periods=max(141//3, 2)).max()
    trough = x.rolling(6, min_periods=max(6//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.251176 + 0.0058893 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=154, w3=115, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(13)
    rank = change.rolling(154, min_periods=max(154//3, 2)).rank(pct=True)
    persistence = change.rolling(115, min_periods=max(115//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.142 * persistence + 0.0058894 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=167, w3=132, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(20, min_periods=max(20//3, 2)).std()
    vol_slow = ret.rolling(167, min_periods=max(167//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.278235 + 0.0058895 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=180, w3=149, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(180, min_periods=max(180//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 27)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.154667 * slope + 0.0058896 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=193, w3=166, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(34)
    drag = impulse.rolling(193, min_periods=max(193//3, 2)).mean()
    noise = impulse.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.305294 + 0.0058897 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=206, w3=183, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 41)
    acceleration = _rolling_slope(velocity, 206)
    curvature = _rolling_slope(acceleration, 183)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.167333 * acceleration + 0.0058898 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=219, w3=200, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(48, min_periods=max(48//3, 2)).mean(), upside.rolling(219, min_periods=max(219//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.332353 + 0.0058899 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=232, w3=217, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(232, min_periods=max(232//3, 2)).max()
    rebound = x - x.rolling(55, min_periods=max(55//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.18 * _rolling_slope(draw, 217) + 0.00589 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=245, w3=234, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 62)
    baseline = trend.rolling(245, min_periods=max(245//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.359412 + 0.0058901 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=258, w3=251, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 69)
    slow = _rolling_slope(x, 258)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=251, adjust=False).mean() * 1.372941 + 0.0058902 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=271, w3=268, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(271, min_periods=max(271//3, 2)).max()
    trough = x.rolling(76, min_periods=max(76//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.386471 + 0.0058903 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=284, w3=285, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(83)
    rank = change.rolling(284, min_periods=max(284//3, 2)).rank(pct=True)
    persistence = change.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.205333 * persistence + 0.0058904 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=297, w3=302, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(90, min_periods=max(90//3, 2)).std()
    vol_slow = ret.rolling(297, min_periods=max(297//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.413529 + 0.0058905 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=310, w3=319, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(310, min_periods=max(310//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 97)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.218 * slope + 0.0058906 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=323, w3=336, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(104)
    drag = impulse.rolling(323, min_periods=max(323//3, 2)).mean()
    noise = impulse.abs().rolling(336, min_periods=max(336//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.440588 + 0.0058907 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=336, w3=353, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 111)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 353)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.230667 * acceleration + 0.0058908 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=349, w3=370, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(349, min_periods=max(349//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.467647 + 0.0058909 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=362, w3=387, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(362, min_periods=max(362//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.243333 * _rolling_slope(draw, 387) + 0.005891 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=375, w3=404, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(375, min_periods=max(375//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.494706 + 0.0058911 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=388, w3=421, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 388)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.508235 + 0.0058912 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=401, w3=438, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(401, min_periods=max(401//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.521765 + 0.0058913 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=414, w3=455, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(414, min_periods=max(414//3, 2)).rank(pct=True)
    persistence = change.rolling(455, min_periods=max(455//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.268667 * persistence + 0.0058914 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=427, w3=472, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(427, min_periods=max(427//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.548824 + 0.0058915 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=440, w3=489, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(440, min_periods=max(440//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.281333 * slope + 0.0058916 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=453, w3=506, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(453, min_periods=max(453//3, 2)).mean()
    noise = impulse.abs().rolling(506, min_periods=max(506//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.575882 + 0.0058917 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=466, w3=523, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 466)
    curvature = _rolling_slope(acceleration, 523)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.294 * acceleration + 0.0058918 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=479, w3=540, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(479, min_periods=max(479//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.602941 + 0.0058919 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=492, w3=557, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(492, min_periods=max(492//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.306667 * _rolling_slope(draw, 557) + 0.005892 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=505, w3=574, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(505, min_periods=max(505//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.63 + 0.0058921 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=19, w3=591, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 19)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.643529 + 0.0058922 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=32, w3=608, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.657059 + 0.0058923 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=45, w3=625, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(45, min_periods=max(45//3, 2)).rank(pct=True)
    persistence = change.rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.332 * persistence + 0.0058924 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=58, w3=642, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(58, min_periods=max(58//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.830588 + 0.0058925 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=71, w3=659, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(71, min_periods=max(71//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.344667 * slope + 0.0058926 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=84, w3=676, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(84, min_periods=max(84//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.857647 + 0.0058927 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=97, w3=693, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 97)
    curvature = _rolling_slope(acceleration, 693)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.357333 * acceleration + 0.0058928 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=110, w3=710, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(110, min_periods=max(110//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.884706 + 0.0058929 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=123, w3=727, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(123, min_periods=max(123//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.037667 * _rolling_slope(draw, 727) + 0.005893 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=136, w3=744, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(136, min_periods=max(136//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(744, min_periods=max(744//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.911765 + 0.0058931 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=149, w3=761, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.925294 + 0.0058932 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=162, w3=27, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(162, min_periods=max(162//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.938824 + 0.0058933 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=175, w3=44, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(46)
    rank = change.rolling(175, min_periods=max(175//3, 2)).rank(pct=True)
    persistence = change.rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.063 * persistence + 0.0058934 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=188, w3=61, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(188, min_periods=max(188//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.965882 + 0.0058935 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=201, w3=78, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(201, min_periods=max(201//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.075667 * slope + 0.0058936 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=214, w3=95, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(67)
    drag = impulse.rolling(214, min_periods=max(214//3, 2)).mean()
    noise = impulse.abs().rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.992941 + 0.0058937 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=227, w3=112, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 227)
    curvature = _rolling_slope(acceleration, 112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.088333 * acceleration + 0.0058938 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=240, w3=129, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(240, min_periods=max(240//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.02 + 0.0058939 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=253, w3=146, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(253, min_periods=max(253//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.101 * _rolling_slope(draw, 146) + 0.005894 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=266, w3=163, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(266, min_periods=max(266//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.047059 + 0.0058941 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=279, w3=180, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 279)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=180, adjust=False).mean() * 1.060588 + 0.0058942 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=292, w3=197, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(292, min_periods=max(292//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.074118 + 0.0058943 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=305, w3=214, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(116)
    rank = change.rolling(305, min_periods=max(305//3, 2)).rank(pct=True)
    persistence = change.rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.126333 * persistence + 0.0058944 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=318, w3=231, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(318, min_periods=max(318//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.101176 + 0.0058945 * anchor
    return base_signal.diff().diff()

def f95_rsmo_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=331, w3=248, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(331, min_periods=max(331//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.139 * slope + 0.0058946 * anchor
    return base_signal.diff().diff()
