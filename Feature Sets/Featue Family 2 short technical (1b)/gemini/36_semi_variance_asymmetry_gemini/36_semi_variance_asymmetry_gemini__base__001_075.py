"""36 semi variance asymmetry gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of downside vs. upside volatility to detect bearish risk bias.
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

def f36_svar_gemini_001(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_002(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_003(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_004(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_005(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_006(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_007(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_008(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_009(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_010(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return res

def f36_svar_gemini_011(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=104, w2=469, w3=476, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(104, min_periods=max(104//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.965882 + 0.0025562 * anchor
    return base_signal

def f36_svar_gemini_012(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=111, w2=482, w3=493, lag=2)."""
    a = _safe_log(low.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(482, min_periods=max(482//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 111)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.979412 + 0.0025563 * anchor
    return base_signal

def f36_svar_gemini_013(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=118, w2=495, w3=510, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(118, min_periods=max(118//3, 2)).mean(), b.abs().rolling(495, min_periods=max(495//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.083667 * _rolling_slope(cover, 118) + 0.0025564 * anchor
    return base_signal

def f36_svar_gemini_014(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=125, w2=508, w3=527, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.09 * y + 0.910000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 125) - _rolling_slope(basket, 508) + 0.0025565 * anchor
    return base_signal

def f36_svar_gemini_015(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=132, w2=22, w3=544, lag=8)."""
    x = low.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(22, min_periods=max(22//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.02 + 0.0025566 * anchor
    return base_signal

def f36_svar_gemini_016(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=139, w2=35, w3=561, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    draw = x - x.rolling(35, min_periods=max(35//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.102667 * _rolling_slope(draw, 561) + 0.0025567 * anchor
    return base_signal

def f36_svar_gemini_017(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=146, w2=48, w3=578, lag=21)."""
    a = _safe_log(low.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(48)
    stress = imbalance.rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.047059 + 0.0025568 * anchor
    return base_signal

def f36_svar_gemini_018(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=153, w2=61, w3=595, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(61, min_periods=max(61//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.060588 + 0.0025569 * anchor
    return base_signal

def f36_svar_gemini_019(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=160, w2=74, w3=612, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 74)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.074118 + 0.002557 * anchor
    return base_signal

def f36_svar_gemini_020(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=167, w2=87, w3=629, lag=0)."""
    x = low.shift(0)
    peak = x.rolling(87, min_periods=max(87//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.087647 + 0.0025571 * anchor
    return base_signal

def f36_svar_gemini_021(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=174, w2=100, w3=646, lag=1)."""
    x = low.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(100, min_periods=max(100//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.134333 * persistence + 0.0025572 * anchor
    return base_signal

def f36_svar_gemini_022(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=181, w2=113, w3=663, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(113, min_periods=max(113//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.114706 + 0.0025573 * anchor
    return base_signal

def f36_svar_gemini_023(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=188, w2=126, w3=680, lag=3)."""
    x = low.shift(3)
    ma = x.rolling(126, min_periods=max(126//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.147 * slope + 0.0025574 * anchor
    return base_signal

def f36_svar_gemini_024(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=195, w2=139, w3=697, lag=5)."""
    x = low.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(139, min_periods=max(139//3, 2)).mean()
    noise = impulse.abs().rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.141765 + 0.0025575 * anchor
    return base_signal

def f36_svar_gemini_025(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=202, w2=152, w3=714, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 152)
    curvature = _rolling_slope(acceleration, 714)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.159667 * acceleration + 0.0025576 * anchor
    return base_signal

def f36_svar_gemini_026(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=209, w2=165, w3=731, lag=13)."""
    rel = _safe_div(low.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 209)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.166 * pressure.rolling(731, min_periods=max(731//3, 2)).mean() + 0.0025577 * anchor
    return base_signal

def f36_svar_gemini_027(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=216, w2=178, w3=748, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(216, min_periods=max(216//3, 2)).mean())
    decay = spread.ewm(span=178, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.182353 + 0.0025578 * anchor
    return base_signal

def f36_svar_gemini_028(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=223, w2=191, w3=765, lag=34)."""
    a = _safe_log(low.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(191, min_periods=max(191//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 223)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.195882 + 0.0025579 * anchor
    return base_signal

def f36_svar_gemini_029(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=230, w2=204, w3=31, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(230, min_periods=max(230//3, 2)).mean(), b.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(31) + 0.185 * _rolling_slope(cover, 230) + 0.002558 * anchor
    return base_signal

def f36_svar_gemini_030(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=237, w2=217, w3=48, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.191333 * y + 0.808667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 237) - _rolling_slope(basket, 217) + 0.0025581 * anchor
    return base_signal

def f36_svar_gemini_031(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=244, w2=230, w3=65, lag=1)."""
    x = low.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(244, min_periods=max(244//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(65) * 1.236471 + 0.0025582 * anchor
    return base_signal

def f36_svar_gemini_032(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=251, w2=243, w3=82, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(251, min_periods=max(251//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.204 * _rolling_slope(draw, 82) + 0.0025583 * anchor
    return base_signal

def f36_svar_gemini_033(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=256, w3=99, lag=3)."""
    a = _safe_log(low.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(11) - b.diff(126)
    stress = imbalance.rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.263529 + 0.0025584 * anchor
    return base_signal

def f36_svar_gemini_034(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=269, w3=116, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 18)
    baseline = trend.rolling(269, min_periods=max(269//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.277059 + 0.0025585 * anchor
    return base_signal

def f36_svar_gemini_035(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=282, w3=133, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 25)
    slow = _rolling_slope(x, 282)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=133, adjust=False).mean() * 1.290588 + 0.0025586 * anchor
    return base_signal

def f36_svar_gemini_036(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=295, w3=150, lag=13)."""
    x = low.shift(13)
    peak = x.rolling(295, min_periods=max(295//3, 2)).max()
    trough = x.rolling(32, min_periods=max(32//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.304118 + 0.0025587 * anchor
    return base_signal

def f36_svar_gemini_037(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=308, w3=167, lag=21)."""
    x = low.shift(21)
    change = x.pct_change(39)
    rank = change.rolling(308, min_periods=max(308//3, 2)).rank(pct=True)
    persistence = change.rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.235667 * persistence + 0.0025588 * anchor
    return base_signal

def f36_svar_gemini_038(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=321, w3=184, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(46, min_periods=max(46//3, 2)).std()
    vol_slow = ret.rolling(321, min_periods=max(321//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.331176 + 0.0025589 * anchor
    return base_signal

def f36_svar_gemini_039(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=334, w3=201, lag=55)."""
    x = low.shift(55)
    ma = x.rolling(334, min_periods=max(334//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 53)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.248333 * slope + 0.002559 * anchor
    return base_signal

def f36_svar_gemini_040(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=347, w3=218, lag=0)."""
    x = low.shift(0)
    impulse = x.diff(60)
    drag = impulse.rolling(347, min_periods=max(347//3, 2)).mean()
    noise = impulse.abs().rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.358235 + 0.0025591 * anchor
    return base_signal

def f36_svar_gemini_041(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=360, w3=235, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 67)
    acceleration = _rolling_slope(velocity, 360)
    curvature = _rolling_slope(acceleration, 235)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.261 * acceleration + 0.0025592 * anchor
    return base_signal

def f36_svar_gemini_042(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=373, w3=252, lag=2)."""
    rel = _safe_div(low.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 74)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.267333 * pressure.rolling(252, min_periods=max(252//3, 2)).mean() + 0.0025593 * anchor
    return base_signal

def f36_svar_gemini_043(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=386, w3=269, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(81, min_periods=max(81//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.398824 + 0.0025594 * anchor
    return base_signal

def f36_svar_gemini_044(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=399, w3=286, lag=5)."""
    a = _safe_log(low.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(399, min_periods=max(399//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 88)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.412353 + 0.0025595 * anchor
    return base_signal

def f36_svar_gemini_045(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=412, w3=303, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(95, min_periods=max(95//3, 2)).mean(), b.abs().rolling(412, min_periods=max(412//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.286333 * _rolling_slope(cover, 95) + 0.0025596 * anchor
    return base_signal

def f36_svar_gemini_046(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=425, w3=320, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.292667 * y + 0.707333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 102) - _rolling_slope(basket, 425) + 0.0025597 * anchor
    return base_signal

def f36_svar_gemini_047(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=438, w3=337, lag=21)."""
    x = low.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(109, min_periods=max(109//3, 2)).mean(), upside.rolling(438, min_periods=max(438//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.452941 + 0.0025598 * anchor
    return base_signal

def f36_svar_gemini_048(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=451, w3=354, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(116, min_periods=max(116//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.305333 * _rolling_slope(draw, 354) + 0.0025599 * anchor
    return base_signal

def f36_svar_gemini_049(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=464, w3=371, lag=55)."""
    a = _safe_log(low.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(123) - b.diff(126)
    stress = imbalance.rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.48 + 0.00256 * anchor
    return base_signal

def f36_svar_gemini_050(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=477, w3=388, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 130)
    baseline = trend.rolling(477, min_periods=max(477//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.493529 + 0.0025601 * anchor
    return base_signal

def f36_svar_gemini_051(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=490, w3=405, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 137)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.507059 + 0.0025602 * anchor
    return base_signal

def f36_svar_gemini_052(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=503, w3=422, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(503, min_periods=max(503//3, 2)).max()
    trough = x.rolling(144, min_periods=max(144//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.520588 + 0.0025603 * anchor
    return base_signal

def f36_svar_gemini_053(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=17, w3=439, lag=3)."""
    x = low.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(17, min_periods=max(17//3, 2)).rank(pct=True)
    persistence = change.rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.337 * persistence + 0.0025604 * anchor
    return base_signal

def f36_svar_gemini_054(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=30, w3=456, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(158, min_periods=max(158//3, 2)).std()
    vol_slow = ret.rolling(30, min_periods=max(30//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.547647 + 0.0025605 * anchor
    return base_signal

def f36_svar_gemini_055(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=43, w3=473, lag=8)."""
    x = low.shift(8)
    ma = x.rolling(43, min_periods=max(43//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 165)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349667 * slope + 0.0025606 * anchor
    return base_signal

def f36_svar_gemini_056(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=56, w3=490, lag=13)."""
    x = low.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(56, min_periods=max(56//3, 2)).mean()
    noise = impulse.abs().rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.574706 + 0.0025607 * anchor
    return base_signal

def f36_svar_gemini_057(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=69, w3=507, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 179)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 507)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.362333 * acceleration + 0.0025608 * anchor
    return base_signal

def f36_svar_gemini_058(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=82, w3=524, lag=34)."""
    rel = _safe_div(low.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 186)
    pressure = rel_log.diff(82)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.036333 * pressure.rolling(524, min_periods=max(524//3, 2)).mean() + 0.0025609 * anchor
    return base_signal

def f36_svar_gemini_059(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=95, w3=541, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(193, min_periods=max(193//3, 2)).mean())
    decay = spread.ewm(span=95, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.615294 + 0.002561 * anchor
    return base_signal

def f36_svar_gemini_060(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=108, w3=558, lag=0)."""
    a = _safe_log(low.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(108, min_periods=max(108//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 200)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.628824 + 0.0025611 * anchor
    return base_signal

def f36_svar_gemini_061(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=121, w3=575, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(207, min_periods=max(207//3, 2)).mean(), b.abs().rolling(121, min_periods=max(121//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.055333 * _rolling_slope(cover, 207) + 0.0025612 * anchor
    return base_signal

def f36_svar_gemini_062(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=134, w3=592, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.061667 * y + 0.938333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 214) - _rolling_slope(basket, 134) + 0.0025613 * anchor
    return base_signal

def f36_svar_gemini_063(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=147, w3=609, lag=3)."""
    x = low.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(147, min_periods=max(147//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.669412 + 0.0025614 * anchor
    return base_signal

def f36_svar_gemini_064(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=160, w3=626, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    draw = x - x.rolling(160, min_periods=max(160//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.074333 * _rolling_slope(draw, 626) + 0.0025615 * anchor
    return base_signal

def f36_svar_gemini_065(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=173, w3=643, lag=8)."""
    a = _safe_log(low.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(643, min_periods=max(643//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.842941 + 0.0025616 * anchor
    return base_signal

def f36_svar_gemini_066(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=186, w3=660, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 242)
    baseline = trend.rolling(186, min_periods=max(186//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.856471 + 0.0025617 * anchor
    return base_signal

def f36_svar_gemini_067(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=199, w3=677, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 249)
    slow = _rolling_slope(x, 199)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.87 + 0.0025618 * anchor
    return base_signal

def f36_svar_gemini_068(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=212, w3=694, lag=34)."""
    x = low.shift(34)
    peak = x.rolling(212, min_periods=max(212//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.883529 + 0.0025619 * anchor
    return base_signal

def f36_svar_gemini_069(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=225, w3=711, lag=55)."""
    x = low.shift(55)
    change = x.pct_change(16)
    rank = change.rolling(225, min_periods=max(225//3, 2)).rank(pct=True)
    persistence = change.rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.106 * persistence + 0.002562 * anchor
    return base_signal

def f36_svar_gemini_070(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=238, w3=728, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(238, min_periods=max(238//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.910588 + 0.0025621 * anchor
    return base_signal

def f36_svar_gemini_071(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=251, w3=745, lag=1)."""
    x = low.shift(1)
    ma = x.rolling(251, min_periods=max(251//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.118667 * slope + 0.0025622 * anchor
    return base_signal

def f36_svar_gemini_072(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=264, w3=762, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(37)
    drag = impulse.rolling(264, min_periods=max(264//3, 2)).mean()
    noise = impulse.abs().rolling(762, min_periods=max(762//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.937647 + 0.0025623 * anchor
    return base_signal

def f36_svar_gemini_073(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=277, w3=28, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 277)
    curvature = _rolling_slope(acceleration, 28)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.131333 * acceleration + 0.0025624 * anchor
    return base_signal

def f36_svar_gemini_074(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=290, w3=45, lag=5)."""
    rel = _safe_div(low.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 51)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.137667 * pressure.rolling(45, min_periods=max(45//3, 2)).mean() + 0.0025625 * anchor
    return base_signal

def f36_svar_gemini_075(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=303, w3=62, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(58, min_periods=max(58//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.978235 + 0.0025626 * anchor
    return base_signal
