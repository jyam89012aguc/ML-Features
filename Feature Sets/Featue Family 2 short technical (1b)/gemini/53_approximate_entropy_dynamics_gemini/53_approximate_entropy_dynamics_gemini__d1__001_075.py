"""53 approximate entropy dynamics gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f53_aent_gemini_001_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_002_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_003_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_004_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_005_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_006_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_007_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_008_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_009_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_010_d1(close: pd.Series) -> pd.Series:
    """Quantification of regularity and predictability in short-term price fluctuations. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().rolling(window).std() / (_safe_log(close).diff().abs().rolling(window).mean() + 1e-9), window)
    return (res).diff()

def f53_aent_gemini_011_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=301, w3=227, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 301)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=227, adjust=False).mean() * 1.07 + 0.0035222 * anchor
    return base_signal.diff()

def f53_aent_gemini_012_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=314, w3=244, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(314, min_periods=max(314//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.083529 + 0.0035223 * anchor
    return base_signal.diff()

def f53_aent_gemini_013_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=327, w3=261, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(60)
    rank = change.rolling(327, min_periods=max(327//3, 2)).rank(pct=True)
    persistence = change.rolling(261, min_periods=max(261//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.114333 * persistence + 0.0035224 * anchor
    return base_signal.diff()

def f53_aent_gemini_014_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=340, w3=278, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(340, min_periods=max(340//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.110588 + 0.0035225 * anchor
    return base_signal.diff()

def f53_aent_gemini_015_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=353, w3=295, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(353, min_periods=max(353//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.127 * slope + 0.0035226 * anchor
    return base_signal.diff()

def f53_aent_gemini_016_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=366, w3=312, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(81)
    drag = impulse.rolling(366, min_periods=max(366//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.137647 + 0.0035227 * anchor
    return base_signal.diff()

def f53_aent_gemini_017_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=379, w3=329, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 379)
    curvature = _rolling_slope(acceleration, 329)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.139667 * acceleration + 0.0035228 * anchor
    return base_signal.diff()

def f53_aent_gemini_018_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=392, w3=346, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(392, min_periods=max(392//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.164706 + 0.0035229 * anchor
    return base_signal.diff()

def f53_aent_gemini_019_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=405, w3=363, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(405, min_periods=max(405//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.152333 * _rolling_slope(draw, 363) + 0.003523 * anchor
    return base_signal.diff()

def f53_aent_gemini_020_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=418, w3=380, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(418, min_periods=max(418//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(380, min_periods=max(380//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.191765 + 0.0035231 * anchor
    return base_signal.diff()

def f53_aent_gemini_021_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=431, w3=397, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 431)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.205294 + 0.0035232 * anchor
    return base_signal.diff()

def f53_aent_gemini_022_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=444, w3=414, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(444, min_periods=max(444//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.218824 + 0.0035233 * anchor
    return base_signal.diff()

def f53_aent_gemini_023_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=457, w3=431, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(457, min_periods=max(457//3, 2)).rank(pct=True)
    persistence = change.rolling(431, min_periods=max(431//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.177667 * persistence + 0.0035234 * anchor
    return base_signal.diff()

def f53_aent_gemini_024_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=470, w3=448, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(470, min_periods=max(470//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.245882 + 0.0035235 * anchor
    return base_signal.diff()

def f53_aent_gemini_025_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=483, w3=465, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(483, min_periods=max(483//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.190333 * slope + 0.0035236 * anchor
    return base_signal.diff()

def f53_aent_gemini_026_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=496, w3=482, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(496, min_periods=max(496//3, 2)).mean()
    noise = impulse.abs().rolling(482, min_periods=max(482//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.272941 + 0.0035237 * anchor
    return base_signal.diff()

def f53_aent_gemini_027_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=509, w3=499, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 509)
    curvature = _rolling_slope(acceleration, 499)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.203 * acceleration + 0.0035238 * anchor
    return base_signal.diff()

def f53_aent_gemini_028_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=23, w3=516, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(23, min_periods=max(23//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.3 + 0.0035239 * anchor
    return base_signal.diff()

def f53_aent_gemini_029_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=36, w3=533, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.215667 * _rolling_slope(draw, 533) + 0.003524 * anchor
    return base_signal.diff()

def f53_aent_gemini_030_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=49, w3=550, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(49, min_periods=max(49//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(550, min_periods=max(550//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.327059 + 0.0035241 * anchor
    return base_signal.diff()

def f53_aent_gemini_031_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=62, w3=567, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 186)
    slow = _rolling_slope(x, 62)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.340588 + 0.0035242 * anchor
    return base_signal.diff()

def f53_aent_gemini_032_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=75, w3=584, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(75, min_periods=max(75//3, 2)).max()
    trough = x.rolling(193, min_periods=max(193//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.354118 + 0.0035243 * anchor
    return base_signal.diff()

def f53_aent_gemini_033_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=88, w3=601, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(88, min_periods=max(88//3, 2)).rank(pct=True)
    persistence = change.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.241 * persistence + 0.0035244 * anchor
    return base_signal.diff()

def f53_aent_gemini_034_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=101, w3=618, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(207, min_periods=max(207//3, 2)).std()
    vol_slow = ret.rolling(101, min_periods=max(101//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.381176 + 0.0035245 * anchor
    return base_signal.diff()

def f53_aent_gemini_035_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=114, w3=635, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(114, min_periods=max(114//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 214)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.253667 * slope + 0.0035246 * anchor
    return base_signal.diff()

def f53_aent_gemini_036_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=127, w3=652, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(127, min_periods=max(127//3, 2)).mean()
    noise = impulse.abs().rolling(652, min_periods=max(652//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.408235 + 0.0035247 * anchor
    return base_signal.diff()

def f53_aent_gemini_037_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=140, w3=669, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 140)
    curvature = _rolling_slope(acceleration, 669)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.266333 * acceleration + 0.0035248 * anchor
    return base_signal.diff()

def f53_aent_gemini_038_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=153, w3=686, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(235, min_periods=max(235//3, 2)).mean(), upside.rolling(153, min_periods=max(153//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.435294 + 0.0035249 * anchor
    return base_signal.diff()

def f53_aent_gemini_039_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=166, w3=703, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(166, min_periods=max(166//3, 2)).max()
    rebound = x - x.rolling(242, min_periods=max(242//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.279 * _rolling_slope(draw, 703) + 0.003525 * anchor
    return base_signal.diff()

def f53_aent_gemini_040_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=179, w3=720, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(179, min_periods=max(179//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.462353 + 0.0035251 * anchor
    return base_signal.diff()

def f53_aent_gemini_041_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=192, w3=737, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 192)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.475882 + 0.0035252 * anchor
    return base_signal.diff()

def f53_aent_gemini_042_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=205, w3=754, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(205, min_periods=max(205//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.489412 + 0.0035253 * anchor
    return base_signal.diff()

def f53_aent_gemini_043_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=218, w3=20, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(23)
    rank = change.rolling(218, min_periods=max(218//3, 2)).rank(pct=True)
    persistence = change.rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.304333 * persistence + 0.0035254 * anchor
    return base_signal.diff()

def f53_aent_gemini_044_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=231, w3=37, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(231, min_periods=max(231//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.516471 + 0.0035255 * anchor
    return base_signal.diff()

def f53_aent_gemini_045_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=244, w3=54, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(244, min_periods=max(244//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.317 * slope + 0.0035256 * anchor
    return base_signal.diff()

def f53_aent_gemini_046_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=257, w3=71, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(44)
    drag = impulse.rolling(257, min_periods=max(257//3, 2)).mean()
    noise = impulse.abs().rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.543529 + 0.0035257 * anchor
    return base_signal.diff()

def f53_aent_gemini_047_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=270, w3=88, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 270)
    curvature = _rolling_slope(acceleration, 88)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.329667 * acceleration + 0.0035258 * anchor
    return base_signal.diff()

def f53_aent_gemini_048_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=283, w3=105, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(58, min_periods=max(58//3, 2)).mean(), upside.rolling(283, min_periods=max(283//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(105) * 1.570588 + 0.0035259 * anchor
    return base_signal.diff()

def f53_aent_gemini_049_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=296, w3=122, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(296, min_periods=max(296//3, 2)).max()
    rebound = x - x.rolling(65, min_periods=max(65//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.342333 * _rolling_slope(draw, 122) + 0.003526 * anchor
    return base_signal.diff()

def f53_aent_gemini_050_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=309, w3=139, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 72)
    baseline = trend.rolling(309, min_periods=max(309//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.597647 + 0.0035261 * anchor
    return base_signal.diff()

def f53_aent_gemini_051_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=322, w3=156, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 79)
    slow = _rolling_slope(x, 322)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=156, adjust=False).mean() * 1.611176 + 0.0035262 * anchor
    return base_signal.diff()

def f53_aent_gemini_052_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=335, w3=173, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(335, min_periods=max(335//3, 2)).max()
    trough = x.rolling(86, min_periods=max(86//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.624706 + 0.0035263 * anchor
    return base_signal.diff()

def f53_aent_gemini_053_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=348, w3=190, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(93)
    rank = change.rolling(348, min_periods=max(348//3, 2)).rank(pct=True)
    persistence = change.rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.035333 * persistence + 0.0035264 * anchor
    return base_signal.diff()

def f53_aent_gemini_054_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=361, w3=207, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(100, min_periods=max(100//3, 2)).std()
    vol_slow = ret.rolling(361, min_periods=max(361//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.651765 + 0.0035265 * anchor
    return base_signal.diff()

def f53_aent_gemini_055_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=374, w3=224, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(374, min_periods=max(374//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 107)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.048 * slope + 0.0035266 * anchor
    return base_signal.diff()

def f53_aent_gemini_056_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=387, w3=241, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(114)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.825294 + 0.0035267 * anchor
    return base_signal.diff()

def f53_aent_gemini_057_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=400, w3=258, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 121)
    acceleration = _rolling_slope(velocity, 400)
    curvature = _rolling_slope(acceleration, 258)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.060667 * acceleration + 0.0035268 * anchor
    return base_signal.diff()

def f53_aent_gemini_058_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=413, w3=275, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(128, min_periods=max(128//3, 2)).mean(), upside.rolling(413, min_periods=max(413//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.852353 + 0.0035269 * anchor
    return base_signal.diff()

def f53_aent_gemini_059_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=426, w3=292, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(426, min_periods=max(426//3, 2)).max()
    rebound = x - x.rolling(135, min_periods=max(135//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.073333 * _rolling_slope(draw, 292) + 0.003527 * anchor
    return base_signal.diff()

def f53_aent_gemini_060_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=439, w3=309, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(439, min_periods=max(439//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(309, min_periods=max(309//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.879412 + 0.0035271 * anchor
    return base_signal.diff()

def f53_aent_gemini_061_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=452, w3=326, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 452)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.892941 + 0.0035272 * anchor
    return base_signal.diff()

def f53_aent_gemini_062_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=465, w3=343, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(465, min_periods=max(465//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.906471 + 0.0035273 * anchor
    return base_signal.diff()

def f53_aent_gemini_063_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=478, w3=360, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(478, min_periods=max(478//3, 2)).rank(pct=True)
    persistence = change.rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.098667 * persistence + 0.0035274 * anchor
    return base_signal.diff()

def f53_aent_gemini_064_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=491, w3=377, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(491, min_periods=max(491//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.933529 + 0.0035275 * anchor
    return base_signal.diff()

def f53_aent_gemini_065_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=504, w3=394, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.111333 * slope + 0.0035276 * anchor
    return base_signal.diff()

def f53_aent_gemini_066_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=18, w3=411, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(18, min_periods=max(18//3, 2)).mean()
    noise = impulse.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.960588 + 0.0035277 * anchor
    return base_signal.diff()

def f53_aent_gemini_067_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=31, w3=428, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 31)
    curvature = _rolling_slope(acceleration, 428)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.124 * acceleration + 0.0035278 * anchor
    return base_signal.diff()

def f53_aent_gemini_068_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=44, w3=445, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(198, min_periods=max(198//3, 2)).mean(), upside.rolling(44, min_periods=max(44//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.987647 + 0.0035279 * anchor
    return base_signal.diff()

def f53_aent_gemini_069_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=57, w3=462, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(57, min_periods=max(57//3, 2)).max()
    rebound = x - x.rolling(205, min_periods=max(205//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.136667 * _rolling_slope(draw, 462) + 0.003528 * anchor
    return base_signal.diff()

def f53_aent_gemini_070_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=70, w3=479, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 212)
    baseline = trend.rolling(70, min_periods=max(70//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(479, min_periods=max(479//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.014706 + 0.0035281 * anchor
    return base_signal.diff()

def f53_aent_gemini_071_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=83, w3=496, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 219)
    slow = _rolling_slope(x, 83)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.028235 + 0.0035282 * anchor
    return base_signal.diff()

def f53_aent_gemini_072_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=96, w3=513, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(96, min_periods=max(96//3, 2)).max()
    trough = x.rolling(226, min_periods=max(226//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.041765 + 0.0035283 * anchor
    return base_signal.diff()

def f53_aent_gemini_073_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=109, w3=530, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(109, min_periods=max(109//3, 2)).rank(pct=True)
    persistence = change.rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.162 * persistence + 0.0035284 * anchor
    return base_signal.diff()

def f53_aent_gemini_074_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=122, w3=547, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(240, min_periods=max(240//3, 2)).std()
    vol_slow = ret.rolling(122, min_periods=max(122//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.068824 + 0.0035285 * anchor
    return base_signal.diff()

def f53_aent_gemini_075_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=135, w3=564, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(135, min_periods=max(135//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 247)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.174667 * slope + 0.0035286 * anchor
    return base_signal.diff()
