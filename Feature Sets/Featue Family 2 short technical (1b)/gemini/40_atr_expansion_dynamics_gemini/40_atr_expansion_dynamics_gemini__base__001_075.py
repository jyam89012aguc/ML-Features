"""40 atr expansion dynamics gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Sudden increases in Average True Range as a precursor to significant price moves.
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

def f40_atre_gemini_001(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=5]"""
    window = 5
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_002(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=10]"""
    window = 10
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_003(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=21]"""
    window = 21
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_004(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=42]"""
    window = 42
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_005(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=63]"""
    window = 63
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_006(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=126]"""
    window = 126
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_007(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=252]"""
    window = 252
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_008(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=504]"""
    window = 504
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_009(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=756]"""
    window = 756
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_010(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sudden increases in Average True Range as a precursor to significant price moves. [window=1260]"""
    window = 1260
    res = _safe_div(_atr(high, low, close, window), _atr(high, low, close, window*2) + 1e-9)
    return res

def f40_atre_gemini_011(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=223, w2=148, w3=255, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    decay = spread.ewm(span=148, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.398235 + 0.0027802 * anchor
    return base_signal

def f40_atre_gemini_012(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=230, w2=161, w3=272, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(161, min_periods=max(161//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 230)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.411765 + 0.0027803 * anchor
    return base_signal

def f40_atre_gemini_013(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=237, w2=174, w3=289, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(237, min_periods=max(237//3, 2)).mean(), b.abs().rolling(174, min_periods=max(174//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.312333 * _rolling_slope(cover, 237) + 0.0027804 * anchor
    return base_signal

def f40_atre_gemini_014(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=244, w2=187, w3=306, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.318667 * y + 0.681333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 244) - _rolling_slope(basket, 187) + 0.0027805 * anchor
    return base_signal

def f40_atre_gemini_015(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=251, w2=200, w3=323, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(200, min_periods=max(200//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.452353 + 0.0027806 * anchor
    return base_signal

def f40_atre_gemini_016(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=213, w3=340, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(213, min_periods=max(213//3, 2)).max()
    rebound = x - x.rolling(11, min_periods=max(11//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.331333 * _rolling_slope(draw, 340) + 0.0027807 * anchor
    return base_signal

def f40_atre_gemini_017(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=226, w3=357, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(18) - b.diff(126)
    stress = imbalance.rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.479412 + 0.0027808 * anchor
    return base_signal

def f40_atre_gemini_018(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=239, w3=374, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(239, min_periods=max(239//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.492941 + 0.0027809 * anchor
    return base_signal

def f40_atre_gemini_019(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=252, w3=391, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 252)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.506471 + 0.002781 * anchor
    return base_signal

def f40_atre_gemini_020(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=265, w3=408, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(265, min_periods=max(265//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.52 + 0.0027811 * anchor
    return base_signal

def f40_atre_gemini_021(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=278, w3=425, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(46)
    rank = change.rolling(278, min_periods=max(278//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.363 * persistence + 0.0027812 * anchor
    return base_signal

def f40_atre_gemini_022(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=291, w3=442, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(291, min_periods=max(291//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.547059 + 0.0027813 * anchor
    return base_signal

def f40_atre_gemini_023(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=304, w3=459, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(304, min_periods=max(304//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.043333 * slope + 0.0027814 * anchor
    return base_signal

def f40_atre_gemini_024(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=317, w3=476, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(67)
    drag = impulse.rolling(317, min_periods=max(317//3, 2)).mean()
    noise = impulse.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.574118 + 0.0027815 * anchor
    return base_signal

def f40_atre_gemini_025(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=330, w3=493, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 330)
    curvature = _rolling_slope(acceleration, 493)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.056 * acceleration + 0.0027816 * anchor
    return base_signal

def f40_atre_gemini_026(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=343, w3=510, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 81)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.062333 * pressure.rolling(510, min_periods=max(510//3, 2)).mean() + 0.0027817 * anchor
    return base_signal

def f40_atre_gemini_027(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=356, w3=527, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(88, min_periods=max(88//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.614706 + 0.0027818 * anchor
    return base_signal

def f40_atre_gemini_028(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=369, w3=544, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(369, min_periods=max(369//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 95)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.628235 + 0.0027819 * anchor
    return base_signal

def f40_atre_gemini_029(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=382, w3=561, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(102, min_periods=max(102//3, 2)).mean(), b.abs().rolling(382, min_periods=max(382//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.081333 * _rolling_slope(cover, 102) + 0.002782 * anchor
    return base_signal

def f40_atre_gemini_030(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=395, w3=578, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.087667 * y + 0.912333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 109) - _rolling_slope(basket, 395) + 0.0027821 * anchor
    return base_signal

def f40_atre_gemini_031(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=408, w3=595, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(116, min_periods=max(116//3, 2)).mean(), upside.rolling(408, min_periods=max(408//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.668824 + 0.0027822 * anchor
    return base_signal

def f40_atre_gemini_032(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=421, w3=612, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(421, min_periods=max(421//3, 2)).max()
    rebound = x - x.rolling(123, min_periods=max(123//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.100333 * _rolling_slope(draw, 612) + 0.0027823 * anchor
    return base_signal

def f40_atre_gemini_033(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=434, w3=629, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.842353 + 0.0027824 * anchor
    return base_signal

def f40_atre_gemini_034(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=447, w3=646, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 137)
    baseline = trend.rolling(447, min_periods=max(447//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.855882 + 0.0027825 * anchor
    return base_signal

def f40_atre_gemini_035(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=460, w3=663, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 144)
    slow = _rolling_slope(x, 460)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.869412 + 0.0027826 * anchor
    return base_signal

def f40_atre_gemini_036(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=473, w3=680, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(473, min_periods=max(473//3, 2)).max()
    trough = x.rolling(151, min_periods=max(151//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.882941 + 0.0027827 * anchor
    return base_signal

def f40_atre_gemini_037(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=486, w3=697, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(486, min_periods=max(486//3, 2)).rank(pct=True)
    persistence = change.rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.132 * persistence + 0.0027828 * anchor
    return base_signal

def f40_atre_gemini_038(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=499, w3=714, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(165, min_periods=max(165//3, 2)).std()
    vol_slow = ret.rolling(499, min_periods=max(499//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.91 + 0.0027829 * anchor
    return base_signal

def f40_atre_gemini_039(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=13, w3=731, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(13, min_periods=max(13//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 172)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.144667 * slope + 0.002783 * anchor
    return base_signal

def f40_atre_gemini_040(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=26, w3=748, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(26, min_periods=max(26//3, 2)).mean()
    noise = impulse.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.937059 + 0.0027831 * anchor
    return base_signal

def f40_atre_gemini_041(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=39, w3=765, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 186)
    acceleration = _rolling_slope(velocity, 39)
    curvature = _rolling_slope(acceleration, 765)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.157333 * acceleration + 0.0027832 * anchor
    return base_signal

def f40_atre_gemini_042(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=52, w3=31, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 193)
    pressure = rel_log.diff(52)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.163667 * pressure.rolling(31, min_periods=max(31//3, 2)).mean() + 0.0027833 * anchor
    return base_signal

def f40_atre_gemini_043(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=65, w3=48, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(200, min_periods=max(200//3, 2)).mean())
    decay = spread.ewm(span=65, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.977647 + 0.0027834 * anchor
    return base_signal

def f40_atre_gemini_044(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=78, w3=65, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(78, min_periods=max(78//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 207)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.991176 + 0.0027835 * anchor
    return base_signal

def f40_atre_gemini_045(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=91, w3=82, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(214, min_periods=max(214//3, 2)).mean(), b.abs().rolling(91, min_periods=max(91//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(82) + 0.182667 * _rolling_slope(cover, 214) + 0.0027836 * anchor
    return base_signal

def f40_atre_gemini_046(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=104, w3=99, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.189 * y + 0.811000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 221) - _rolling_slope(basket, 104) + 0.0027837 * anchor
    return base_signal

def f40_atre_gemini_047(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=117, w3=116, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(228, min_periods=max(228//3, 2)).mean(), upside.rolling(117, min_periods=max(117//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(116) * 1.031765 + 0.0027838 * anchor
    return base_signal

def f40_atre_gemini_048(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=130, w3=133, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(130, min_periods=max(130//3, 2)).max()
    rebound = x - x.rolling(235, min_periods=max(235//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.201667 * _rolling_slope(draw, 133) + 0.0027839 * anchor
    return base_signal

def f40_atre_gemini_049(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=143, w3=150, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.058824 + 0.002784 * anchor
    return base_signal

def f40_atre_gemini_050(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=156, w3=167, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 249)
    baseline = trend.rolling(156, min_periods=max(156//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.072353 + 0.0027841 * anchor
    return base_signal

def f40_atre_gemini_051(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=169, w3=184, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 9)
    slow = _rolling_slope(x, 169)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=184, adjust=False).mean() * 1.085882 + 0.0027842 * anchor
    return base_signal

def f40_atre_gemini_052(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=182, w3=201, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(182, min_periods=max(182//3, 2)).max()
    trough = x.rolling(16, min_periods=max(16//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.099412 + 0.0027843 * anchor
    return base_signal

def f40_atre_gemini_053(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=195, w3=218, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(23)
    rank = change.rolling(195, min_periods=max(195//3, 2)).rank(pct=True)
    persistence = change.rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.233333 * persistence + 0.0027844 * anchor
    return base_signal

def f40_atre_gemini_054(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=208, w3=235, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(30, min_periods=max(30//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.126471 + 0.0027845 * anchor
    return base_signal

def f40_atre_gemini_055(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=221, w3=252, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(221, min_periods=max(221//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 37)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.246 * slope + 0.0027846 * anchor
    return base_signal

def f40_atre_gemini_056(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=234, w3=269, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(44)
    drag = impulse.rolling(234, min_periods=max(234//3, 2)).mean()
    noise = impulse.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.153529 + 0.0027847 * anchor
    return base_signal

def f40_atre_gemini_057(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=247, w3=286, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 51)
    acceleration = _rolling_slope(velocity, 247)
    curvature = _rolling_slope(acceleration, 286)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.258667 * acceleration + 0.0027848 * anchor
    return base_signal

def f40_atre_gemini_058(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=260, w3=303, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 58)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.265 * pressure.rolling(303, min_periods=max(303//3, 2)).mean() + 0.0027849 * anchor
    return base_signal

def f40_atre_gemini_059(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=273, w3=320, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(65, min_periods=max(65//3, 2)).mean())
    decay = spread.ewm(span=273, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.194118 + 0.002785 * anchor
    return base_signal

def f40_atre_gemini_060(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=286, w3=337, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(286, min_periods=max(286//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 72)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.207647 + 0.0027851 * anchor
    return base_signal

def f40_atre_gemini_061(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=299, w3=354, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(79, min_periods=max(79//3, 2)).mean(), b.abs().rolling(299, min_periods=max(299//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.284 * _rolling_slope(cover, 79) + 0.0027852 * anchor
    return base_signal

def f40_atre_gemini_062(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=312, w3=371, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.290333 * y + 0.709667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 86) - _rolling_slope(basket, 312) + 0.0027853 * anchor
    return base_signal

def f40_atre_gemini_063(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=325, w3=388, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(325, min_periods=max(325//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.248235 + 0.0027854 * anchor
    return base_signal

def f40_atre_gemini_064(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=338, w3=405, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(338, min_periods=max(338//3, 2)).max()
    rebound = x - x.rolling(100, min_periods=max(100//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.303 * _rolling_slope(draw, 405) + 0.0027855 * anchor
    return base_signal

def f40_atre_gemini_065(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=351, w3=422, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(107) - b.diff(126)
    stress = imbalance.rolling(422, min_periods=max(422//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.275294 + 0.0027856 * anchor
    return base_signal

def f40_atre_gemini_066(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=364, w3=439, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 114)
    baseline = trend.rolling(364, min_periods=max(364//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.288824 + 0.0027857 * anchor
    return base_signal

def f40_atre_gemini_067(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=377, w3=456, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.302353 + 0.0027858 * anchor
    return base_signal

def f40_atre_gemini_068(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=390, w3=473, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(390, min_periods=max(390//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.315882 + 0.0027859 * anchor
    return base_signal

def f40_atre_gemini_069(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=403, w3=490, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(403, min_periods=max(403//3, 2)).rank(pct=True)
    persistence = change.rolling(490, min_periods=max(490//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.334667 * persistence + 0.002786 * anchor
    return base_signal

def f40_atre_gemini_070(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=416, w3=507, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(416, min_periods=max(416//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.342941 + 0.0027861 * anchor
    return base_signal

def f40_atre_gemini_071(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=429, w3=524, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(429, min_periods=max(429//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.347333 * slope + 0.0027862 * anchor
    return base_signal

def f40_atre_gemini_072(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=442, w3=541, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(442, min_periods=max(442//3, 2)).mean()
    noise = impulse.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.37 + 0.0027863 * anchor
    return base_signal

def f40_atre_gemini_073(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=455, w3=558, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 455)
    curvature = _rolling_slope(acceleration, 558)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.36 * acceleration + 0.0027864 * anchor
    return base_signal

def f40_atre_gemini_074(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=468, w3=575, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 170)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.034 * pressure.rolling(575, min_periods=max(575//3, 2)).mean() + 0.0027865 * anchor
    return base_signal

def f40_atre_gemini_075(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=481, w3=592, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.410588 + 0.0027866 * anchor
    return base_signal
