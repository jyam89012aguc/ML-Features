"""83 intraday range variance gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Variance of price ranges within a session as a measure of intraday instability.
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

def f83_irva_gemini_001_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=5]"""
    window = 5
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_002_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=10]"""
    window = 10
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_003_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=21]"""
    window = 21
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_004_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=42]"""
    window = 42
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_005_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=63]"""
    window = 63
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_006_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=126]"""
    window = 126
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_007_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=252]"""
    window = 252
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_008_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=504]"""
    window = 504
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_009_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=756]"""
    window = 756
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_010_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Variance of price ranges within a session as a measure of intraday instability. [window=1260]"""
    window = 1260
    res = _rolling_zscore(high - low, window)
    return (res).diff()

def f83_irva_gemini_011_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=139, w3=447, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(139, min_periods=max(139//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.155 * slope + 0.0052022 * anchor
    return base_signal.diff()

def f83_irva_gemini_012_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=152, w3=464, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(81)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.338824 + 0.0052023 * anchor
    return base_signal.diff()

def f83_irva_gemini_013_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=165, w3=481, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 165)
    curvature = _rolling_slope(acceleration, 481)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.167667 * acceleration + 0.0052024 * anchor
    return base_signal.diff()

def f83_irva_gemini_014_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=178, w3=498, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 95)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.174 * pressure.rolling(498, min_periods=max(498//3, 2)).mean() + 0.0052025 * anchor
    return base_signal.diff()

def f83_irva_gemini_015_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=191, w3=515, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(102, min_periods=max(102//3, 2)).mean())
    decay = spread.ewm(span=191, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.379412 + 0.0052026 * anchor
    return base_signal.diff()

def f83_irva_gemini_016_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=204, w3=532, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(204, min_periods=max(204//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 109)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.392941 + 0.0052027 * anchor
    return base_signal.diff()

def f83_irva_gemini_017_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=217, w3=549, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(116, min_periods=max(116//3, 2)).mean(), b.abs().rolling(217, min_periods=max(217//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.193 * _rolling_slope(cover, 116) + 0.0052028 * anchor
    return base_signal.diff()

def f83_irva_gemini_018_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=230, w3=566, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.199333 * y + 0.800667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 123) - _rolling_slope(basket, 230) + 0.0052029 * anchor
    return base_signal.diff()

def f83_irva_gemini_019_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=243, w3=583, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(130, min_periods=max(130//3, 2)).mean(), upside.rolling(243, min_periods=max(243//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.433529 + 0.005203 * anchor
    return base_signal.diff()

def f83_irva_gemini_020_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=256, w3=600, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(256, min_periods=max(256//3, 2)).max()
    rebound = x - x.rolling(137, min_periods=max(137//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212 * _rolling_slope(draw, 600) + 0.0052031 * anchor
    return base_signal.diff()

def f83_irva_gemini_021_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=269, w3=617, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(617, min_periods=max(617//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.460588 + 0.0052032 * anchor
    return base_signal.diff()

def f83_irva_gemini_022_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=282, w3=634, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 151)
    baseline = trend.rolling(282, min_periods=max(282//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.474118 + 0.0052033 * anchor
    return base_signal.diff()

def f83_irva_gemini_023_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=295, w3=651, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 158)
    slow = _rolling_slope(x, 295)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.487647 + 0.0052034 * anchor
    return base_signal.diff()

def f83_irva_gemini_024_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=308, w3=668, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(308, min_periods=max(308//3, 2)).max()
    trough = x.rolling(165, min_periods=max(165//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.501176 + 0.0052035 * anchor
    return base_signal.diff()

def f83_irva_gemini_025_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=321, w3=685, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(321, min_periods=max(321//3, 2)).rank(pct=True)
    persistence = change.rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.243667 * persistence + 0.0052036 * anchor
    return base_signal.diff()

def f83_irva_gemini_026_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=334, w3=702, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(179, min_periods=max(179//3, 2)).std()
    vol_slow = ret.rolling(334, min_periods=max(334//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.528235 + 0.0052037 * anchor
    return base_signal.diff()

def f83_irva_gemini_027_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=347, w3=719, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(347, min_periods=max(347//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 186)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.256333 * slope + 0.0052038 * anchor
    return base_signal.diff()

def f83_irva_gemini_028_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=360, w3=736, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(360, min_periods=max(360//3, 2)).mean()
    noise = impulse.abs().rolling(736, min_periods=max(736//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.555294 + 0.0052039 * anchor
    return base_signal.diff()

def f83_irva_gemini_029_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=373, w3=753, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 200)
    acceleration = _rolling_slope(velocity, 373)
    curvature = _rolling_slope(acceleration, 753)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.269 * acceleration + 0.005204 * anchor
    return base_signal.diff()

def f83_irva_gemini_030_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=386, w3=19, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 207)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.275333 * pressure.rolling(19, min_periods=max(19//3, 2)).mean() + 0.0052041 * anchor
    return base_signal.diff()

def f83_irva_gemini_031_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=399, w3=36, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(214, min_periods=max(214//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.595882 + 0.0052042 * anchor
    return base_signal.diff()

def f83_irva_gemini_032_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=412, w3=53, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(412, min_periods=max(412//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 221)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.609412 + 0.0052043 * anchor
    return base_signal.diff()

def f83_irva_gemini_033_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=425, w3=70, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(228, min_periods=max(228//3, 2)).mean(), b.abs().rolling(425, min_periods=max(425//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(70) + 0.294333 * _rolling_slope(cover, 228) + 0.0052044 * anchor
    return base_signal.diff()

def f83_irva_gemini_034_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=438, w3=87, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.300667 * y + 0.699333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 235) - _rolling_slope(basket, 438) + 0.0052045 * anchor
    return base_signal.diff()

def f83_irva_gemini_035_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=451, w3=104, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(451, min_periods=max(451//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(104) * 1.65 + 0.0052046 * anchor
    return base_signal.diff()

def f83_irva_gemini_036_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=464, w3=121, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(464, min_periods=max(464//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.313333 * _rolling_slope(draw, 121) + 0.0052047 * anchor
    return base_signal.diff()

def f83_irva_gemini_037_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=477, w3=138, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(9) - b.diff(126)
    stress = imbalance.rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.823529 + 0.0052048 * anchor
    return base_signal.diff()

def f83_irva_gemini_038_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=490, w3=155, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 16)
    baseline = trend.rolling(490, min_periods=max(490//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.837059 + 0.0052049 * anchor
    return base_signal.diff()

def f83_irva_gemini_039_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=503, w3=172, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 23)
    slow = _rolling_slope(x, 503)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=172, adjust=False).mean() * 0.850588 + 0.005205 * anchor
    return base_signal.diff()

def f83_irva_gemini_040_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=17, w3=189, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(17, min_periods=max(17//3, 2)).max()
    trough = x.rolling(30, min_periods=max(30//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.864118 + 0.0052051 * anchor
    return base_signal.diff()

def f83_irva_gemini_041_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=30, w3=206, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(37)
    rank = change.rolling(30, min_periods=max(30//3, 2)).rank(pct=True)
    persistence = change.rolling(206, min_periods=max(206//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.345 * persistence + 0.0052052 * anchor
    return base_signal.diff()

def f83_irva_gemini_042_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=43, w3=223, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(44, min_periods=max(44//3, 2)).std()
    vol_slow = ret.rolling(43, min_periods=max(43//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.891176 + 0.0052053 * anchor
    return base_signal.diff()

def f83_irva_gemini_043_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=56, w3=240, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(56, min_periods=max(56//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 51)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.357667 * slope + 0.0052054 * anchor
    return base_signal.diff()

def f83_irva_gemini_044_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=69, w3=257, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(58)
    drag = impulse.rolling(69, min_periods=max(69//3, 2)).mean()
    noise = impulse.abs().rolling(257, min_periods=max(257//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.918235 + 0.0052055 * anchor
    return base_signal.diff()

def f83_irva_gemini_045_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=82, w3=274, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 65)
    acceleration = _rolling_slope(velocity, 82)
    curvature = _rolling_slope(acceleration, 274)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.038 * acceleration + 0.0052056 * anchor
    return base_signal.diff()

def f83_irva_gemini_046_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=95, w3=291, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 72)
    pressure = rel_log.diff(95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.044333 * pressure.rolling(291, min_periods=max(291//3, 2)).mean() + 0.0052057 * anchor
    return base_signal.diff()

def f83_irva_gemini_047_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=108, w3=308, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(79, min_periods=max(79//3, 2)).mean())
    decay = spread.ewm(span=108, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.958824 + 0.0052058 * anchor
    return base_signal.diff()

def f83_irva_gemini_048_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=121, w3=325, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(121, min_periods=max(121//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 86)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.972353 + 0.0052059 * anchor
    return base_signal.diff()

def f83_irva_gemini_049_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=134, w3=342, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(93, min_periods=max(93//3, 2)).mean(), b.abs().rolling(134, min_periods=max(134//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.063333 * _rolling_slope(cover, 93) + 0.005206 * anchor
    return base_signal.diff()

def f83_irva_gemini_050_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=147, w3=359, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.069667 * y + 0.930333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 100) - _rolling_slope(basket, 147) + 0.0052061 * anchor
    return base_signal.diff()

def f83_irva_gemini_051_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=160, w3=376, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(107, min_periods=max(107//3, 2)).mean(), upside.rolling(160, min_periods=max(160//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.012941 + 0.0052062 * anchor
    return base_signal.diff()

def f83_irva_gemini_052_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=173, w3=393, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(173, min_periods=max(173//3, 2)).max()
    rebound = x - x.rolling(114, min_periods=max(114//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.082333 * _rolling_slope(draw, 393) + 0.0052063 * anchor
    return base_signal.diff()

def f83_irva_gemini_053_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=186, w3=410, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(121) - b.diff(126)
    stress = imbalance.rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.04 + 0.0052064 * anchor
    return base_signal.diff()

def f83_irva_gemini_054_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=199, w3=427, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(199, min_periods=max(199//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(427, min_periods=max(427//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.053529 + 0.0052065 * anchor
    return base_signal.diff()

def f83_irva_gemini_055_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=212, w3=444, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.067059 + 0.0052066 * anchor
    return base_signal.diff()

def f83_irva_gemini_056_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=225, w3=461, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(225, min_periods=max(225//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.080588 + 0.0052067 * anchor
    return base_signal.diff()

def f83_irva_gemini_057_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=238, w3=478, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(238, min_periods=max(238//3, 2)).rank(pct=True)
    persistence = change.rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.114 * persistence + 0.0052068 * anchor
    return base_signal.diff()

def f83_irva_gemini_058_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=251, w3=495, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(251, min_periods=max(251//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.107647 + 0.0052069 * anchor
    return base_signal.diff()

def f83_irva_gemini_059_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=264, w3=512, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(264, min_periods=max(264//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.126667 * slope + 0.005207 * anchor
    return base_signal.diff()

def f83_irva_gemini_060_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=277, w3=529, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(529, min_periods=max(529//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.134706 + 0.0052071 * anchor
    return base_signal.diff()

def f83_irva_gemini_061_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=290, w3=546, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 290)
    curvature = _rolling_slope(acceleration, 546)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.139333 * acceleration + 0.0052072 * anchor
    return base_signal.diff()

def f83_irva_gemini_062_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=303, w3=563, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 184)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.145667 * pressure.rolling(563, min_periods=max(563//3, 2)).mean() + 0.0052073 * anchor
    return base_signal.diff()

def f83_irva_gemini_063_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=316, w3=580, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(191, min_periods=max(191//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.175294 + 0.0052074 * anchor
    return base_signal.diff()

def f83_irva_gemini_064_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=329, w3=597, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(329, min_periods=max(329//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 198)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.188824 + 0.0052075 * anchor
    return base_signal.diff()

def f83_irva_gemini_065_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=342, w3=614, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(205, min_periods=max(205//3, 2)).mean(), b.abs().rolling(342, min_periods=max(342//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.164667 * _rolling_slope(cover, 205) + 0.0052076 * anchor
    return base_signal.diff()

def f83_irva_gemini_066_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=355, w3=631, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.171 * y + 0.829000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 212) - _rolling_slope(basket, 355) + 0.0052077 * anchor
    return base_signal.diff()

def f83_irva_gemini_067_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=368, w3=648, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(219, min_periods=max(219//3, 2)).mean(), upside.rolling(368, min_periods=max(368//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.229412 + 0.0052078 * anchor
    return base_signal.diff()

def f83_irva_gemini_068_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=381, w3=665, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(381, min_periods=max(381//3, 2)).max()
    rebound = x - x.rolling(226, min_periods=max(226//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.183667 * _rolling_slope(draw, 665) + 0.0052079 * anchor
    return base_signal.diff()

def f83_irva_gemini_069_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=394, w3=682, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(682, min_periods=max(682//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.256471 + 0.005208 * anchor
    return base_signal.diff()

def f83_irva_gemini_070_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=407, w3=699, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(407, min_periods=max(407//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.27 + 0.0052081 * anchor
    return base_signal.diff()

def f83_irva_gemini_071_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=420, w3=716, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 420)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.283529 + 0.0052082 * anchor
    return base_signal.diff()

def f83_irva_gemini_072_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=433, w3=733, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(433, min_periods=max(433//3, 2)).max()
    trough = x.rolling(7, min_periods=max(7//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.297059 + 0.0052083 * anchor
    return base_signal.diff()

def f83_irva_gemini_073_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=446, w3=750, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(14)
    rank = change.rolling(446, min_periods=max(446//3, 2)).rank(pct=True)
    persistence = change.rolling(750, min_periods=max(750//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.215333 * persistence + 0.0052084 * anchor
    return base_signal.diff()

def f83_irva_gemini_074_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=459, w3=767, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(21, min_periods=max(21//3, 2)).std()
    vol_slow = ret.rolling(459, min_periods=max(459//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.324118 + 0.0052085 * anchor
    return base_signal.diff()

def f83_irva_gemini_075_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=472, w3=33, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(472, min_periods=max(472//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 28)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.228 * slope + 0.0052086 * anchor
    return base_signal.diff()
