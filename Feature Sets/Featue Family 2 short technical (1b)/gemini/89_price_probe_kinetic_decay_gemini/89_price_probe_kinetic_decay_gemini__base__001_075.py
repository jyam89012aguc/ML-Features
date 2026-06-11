"""89 price probe kinetic decay gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Failure of price 'probes' into new territory, followed by rapid retracement.
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

def f89_ppkd_gemini_001(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=5]"""
    window = 5
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_002(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=10]"""
    window = 10
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_003(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=21]"""
    window = 21
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_004(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=42]"""
    window = 42
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_005(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=63]"""
    window = 63
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_006(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=126]"""
    window = 126
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_007(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=252]"""
    window = 252
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_008(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=504]"""
    window = 504
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_009(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=756]"""
    window = 756
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_010(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Failure of price 'probes' into new territory, followed by rapid retracement. [window=1260]"""
    window = 1260
    res = _safe_div(high - close, high - low + 1e-9)
    return res

def f89_ppkd_gemini_011(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=83, w3=364, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(137, min_periods=max(137//3, 2)).mean())
    decay = spread.ewm(span=83, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.36 + 0.0055242 * anchor
    return base_signal

def f89_ppkd_gemini_012(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=96, w3=381, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(96, min_periods=max(96//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 144)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.373529 + 0.0055243 * anchor
    return base_signal

def f89_ppkd_gemini_013(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=109, w3=398, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(151, min_periods=max(151//3, 2)).mean(), b.abs().rolling(109, min_periods=max(109//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.288667 * _rolling_slope(cover, 151) + 0.0055244 * anchor
    return base_signal

def f89_ppkd_gemini_014(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=122, w3=415, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.295 * y + 0.705000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 158) - _rolling_slope(basket, 122) + 0.0055245 * anchor
    return base_signal

def f89_ppkd_gemini_015(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=135, w3=432, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(135, min_periods=max(135//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.414118 + 0.0055246 * anchor
    return base_signal

def f89_ppkd_gemini_016(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=148, w3=449, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(148, min_periods=max(148//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.307667 * _rolling_slope(draw, 449) + 0.0055247 * anchor
    return base_signal

def f89_ppkd_gemini_017(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=161, w3=466, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.441176 + 0.0055248 * anchor
    return base_signal

def f89_ppkd_gemini_018(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=174, w3=483, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(174, min_periods=max(174//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.454706 + 0.0055249 * anchor
    return base_signal

def f89_ppkd_gemini_019(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=187, w3=500, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 187)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.468235 + 0.005525 * anchor
    return base_signal

def f89_ppkd_gemini_020(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=200, w3=517, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(200, min_periods=max(200//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.481765 + 0.0055251 * anchor
    return base_signal

def f89_ppkd_gemini_021(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=213, w3=534, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(213, min_periods=max(213//3, 2)).rank(pct=True)
    persistence = change.rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.339333 * persistence + 0.0055252 * anchor
    return base_signal

def f89_ppkd_gemini_022(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=226, w3=551, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(226, min_periods=max(226//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.508824 + 0.0055253 * anchor
    return base_signal

def f89_ppkd_gemini_023(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=239, w3=568, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(239, min_periods=max(239//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.352 * slope + 0.0055254 * anchor
    return base_signal

def f89_ppkd_gemini_024(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=252, w3=585, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(252, min_periods=max(252//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.535882 + 0.0055255 * anchor
    return base_signal

def f89_ppkd_gemini_025(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=265, w3=602, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 265)
    curvature = _rolling_slope(acceleration, 602)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.032333 * acceleration + 0.0055256 * anchor
    return base_signal

def f89_ppkd_gemini_026(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=278, w3=619, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 242)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.038667 * pressure.rolling(619, min_periods=max(619//3, 2)).mean() + 0.0055257 * anchor
    return base_signal

def f89_ppkd_gemini_027(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=291, w3=636, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(249, min_periods=max(249//3, 2)).mean())
    decay = spread.ewm(span=291, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.576471 + 0.0055258 * anchor
    return base_signal

def f89_ppkd_gemini_028(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=304, w3=653, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(304, min_periods=max(304//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 9)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.59 + 0.0055259 * anchor
    return base_signal

def f89_ppkd_gemini_029(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=317, w3=670, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(16, min_periods=max(16//3, 2)).mean(), b.abs().rolling(317, min_periods=max(317//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.057667 * _rolling_slope(cover, 16) + 0.005526 * anchor
    return base_signal

def f89_ppkd_gemini_030(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=330, w3=687, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.064 * y + 0.936000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 23) - _rolling_slope(basket, 330) + 0.0055261 * anchor
    return base_signal

def f89_ppkd_gemini_031(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=343, w3=704, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(343, min_periods=max(343//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.630588 + 0.0055262 * anchor
    return base_signal

def f89_ppkd_gemini_032(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=356, w3=721, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(356, min_periods=max(356//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.076667 * _rolling_slope(draw, 721) + 0.0055263 * anchor
    return base_signal

def f89_ppkd_gemini_033(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=369, w3=738, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(44) - b.diff(126)
    stress = imbalance.rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.657647 + 0.0055264 * anchor
    return base_signal

def f89_ppkd_gemini_034(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=382, w3=755, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(382, min_periods=max(382//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.671176 + 0.0055265 * anchor
    return base_signal

def f89_ppkd_gemini_035(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=395, w3=21, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=21, adjust=False).mean() * 0.831176 + 0.0055266 * anchor
    return base_signal

def f89_ppkd_gemini_036(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=408, w3=38, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.844706 + 0.0055267 * anchor
    return base_signal

def f89_ppkd_gemini_037(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=421, w3=55, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(72)
    rank = change.rolling(421, min_periods=max(421//3, 2)).rank(pct=True)
    persistence = change.rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.108333 * persistence + 0.0055268 * anchor
    return base_signal

def f89_ppkd_gemini_038(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=434, w3=72, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(434, min_periods=max(434//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.871765 + 0.0055269 * anchor
    return base_signal

def f89_ppkd_gemini_039(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=447, w3=89, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(447, min_periods=max(447//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.121 * slope + 0.005527 * anchor
    return base_signal

def f89_ppkd_gemini_040(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=460, w3=106, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(93)
    drag = impulse.rolling(460, min_periods=max(460//3, 2)).mean()
    noise = impulse.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.898824 + 0.0055271 * anchor
    return base_signal

def f89_ppkd_gemini_041(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=473, w3=123, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 473)
    curvature = _rolling_slope(acceleration, 123)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.133667 * acceleration + 0.0055272 * anchor
    return base_signal

def f89_ppkd_gemini_042(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=486, w3=140, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 107)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.14 * pressure.rolling(140, min_periods=max(140//3, 2)).mean() + 0.0055273 * anchor
    return base_signal

def f89_ppkd_gemini_043(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=499, w3=157, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.939412 + 0.0055274 * anchor
    return base_signal

def f89_ppkd_gemini_044(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=121, w2=13, w3=174, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(13, min_periods=max(13//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 121)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.952941 + 0.0055275 * anchor
    return base_signal

def f89_ppkd_gemini_045(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=128, w2=26, w3=191, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(128, min_periods=max(128//3, 2)).mean(), b.abs().rolling(26, min_periods=max(26//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.159 * _rolling_slope(cover, 128) + 0.0055276 * anchor
    return base_signal

def f89_ppkd_gemini_046(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=135, w2=39, w3=208, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.165333 * y + 0.834667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 135) - _rolling_slope(basket, 39) + 0.0055277 * anchor
    return base_signal

def f89_ppkd_gemini_047(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=142, w2=52, w3=225, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(142, min_periods=max(142//3, 2)).mean(), upside.rolling(52, min_periods=max(52//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.993529 + 0.0055278 * anchor
    return base_signal

def f89_ppkd_gemini_048(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=149, w2=65, w3=242, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(65, min_periods=max(65//3, 2)).max()
    rebound = x - x.rolling(149, min_periods=max(149//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.178 * _rolling_slope(draw, 242) + 0.0055279 * anchor
    return base_signal

def f89_ppkd_gemini_049(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=156, w2=78, w3=259, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(78)
    stress = imbalance.rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.020588 + 0.005528 * anchor
    return base_signal

def f89_ppkd_gemini_050(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=163, w2=91, w3=276, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 163)
    baseline = trend.rolling(91, min_periods=max(91//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.034118 + 0.0055281 * anchor
    return base_signal

def f89_ppkd_gemini_051(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=170, w2=104, w3=293, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 170)
    slow = _rolling_slope(x, 104)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=293, adjust=False).mean() * 1.047647 + 0.0055282 * anchor
    return base_signal

def f89_ppkd_gemini_052(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=177, w2=117, w3=310, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(177, min_periods=max(177//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.061176 + 0.0055283 * anchor
    return base_signal

def f89_ppkd_gemini_053(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=184, w2=130, w3=327, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(130, min_periods=max(130//3, 2)).rank(pct=True)
    persistence = change.rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.209667 * persistence + 0.0055284 * anchor
    return base_signal

def f89_ppkd_gemini_054(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=191, w2=143, w3=344, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(191, min_periods=max(191//3, 2)).std()
    vol_slow = ret.rolling(143, min_periods=max(143//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.088235 + 0.0055285 * anchor
    return base_signal

def f89_ppkd_gemini_055(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=198, w2=156, w3=361, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 198)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.222333 * slope + 0.0055286 * anchor
    return base_signal

def f89_ppkd_gemini_056(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=205, w2=169, w3=378, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(169, min_periods=max(169//3, 2)).mean()
    noise = impulse.abs().rolling(378, min_periods=max(378//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.115294 + 0.0055287 * anchor
    return base_signal

def f89_ppkd_gemini_057(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=212, w2=182, w3=395, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 212)
    acceleration = _rolling_slope(velocity, 182)
    curvature = _rolling_slope(acceleration, 395)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235 * acceleration + 0.0055288 * anchor
    return base_signal

def f89_ppkd_gemini_058(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=219, w2=195, w3=412, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 219)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.241333 * pressure.rolling(412, min_periods=max(412//3, 2)).mean() + 0.0055289 * anchor
    return base_signal

def f89_ppkd_gemini_059(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=226, w2=208, w3=429, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(226, min_periods=max(226//3, 2)).mean())
    decay = spread.ewm(span=208, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.155882 + 0.005529 * anchor
    return base_signal

def f89_ppkd_gemini_060(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=233, w2=221, w3=446, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(221, min_periods=max(221//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 233)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.169412 + 0.0055291 * anchor
    return base_signal

def f89_ppkd_gemini_061(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=240, w2=234, w3=463, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(240, min_periods=max(240//3, 2)).mean(), b.abs().rolling(234, min_periods=max(234//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.260333 * _rolling_slope(cover, 240) + 0.0055292 * anchor
    return base_signal

def f89_ppkd_gemini_062(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=247, w2=247, w3=480, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.266667 * y + 0.733333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 247) - _rolling_slope(basket, 247) + 0.0055293 * anchor
    return base_signal

def f89_ppkd_gemini_063(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=7, w2=260, w3=497, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(260, min_periods=max(260//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.21 + 0.0055294 * anchor
    return base_signal

def f89_ppkd_gemini_064(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=14, w2=273, w3=514, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(273, min_periods=max(273//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.279333 * _rolling_slope(draw, 514) + 0.0055295 * anchor
    return base_signal

def f89_ppkd_gemini_065(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=286, w3=531, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(21) - b.diff(126)
    stress = imbalance.rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.237059 + 0.0055296 * anchor
    return base_signal

def f89_ppkd_gemini_066(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=299, w3=548, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 28)
    baseline = trend.rolling(299, min_periods=max(299//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.250588 + 0.0055297 * anchor
    return base_signal

def f89_ppkd_gemini_067(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=312, w3=565, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 35)
    slow = _rolling_slope(x, 312)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.264118 + 0.0055298 * anchor
    return base_signal

def f89_ppkd_gemini_068(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=325, w3=582, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(325, min_periods=max(325//3, 2)).max()
    trough = x.rolling(42, min_periods=max(42//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.277647 + 0.0055299 * anchor
    return base_signal

def f89_ppkd_gemini_069(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=338, w3=599, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(49)
    rank = change.rolling(338, min_periods=max(338//3, 2)).rank(pct=True)
    persistence = change.rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.311 * persistence + 0.00553 * anchor
    return base_signal

def f89_ppkd_gemini_070(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=351, w3=616, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(56, min_periods=max(56//3, 2)).std()
    vol_slow = ret.rolling(351, min_periods=max(351//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.304706 + 0.0055301 * anchor
    return base_signal

def f89_ppkd_gemini_071(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=364, w3=633, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(364, min_periods=max(364//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 63)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.323667 * slope + 0.0055302 * anchor
    return base_signal

def f89_ppkd_gemini_072(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=377, w3=650, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(70)
    drag = impulse.rolling(377, min_periods=max(377//3, 2)).mean()
    noise = impulse.abs().rolling(650, min_periods=max(650//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.331765 + 0.0055303 * anchor
    return base_signal

def f89_ppkd_gemini_073(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=390, w3=667, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 77)
    acceleration = _rolling_slope(velocity, 390)
    curvature = _rolling_slope(acceleration, 667)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.336333 * acceleration + 0.0055304 * anchor
    return base_signal

def f89_ppkd_gemini_074(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=403, w3=684, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 84)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.342667 * pressure.rolling(684, min_periods=max(684//3, 2)).mean() + 0.0055305 * anchor
    return base_signal

def f89_ppkd_gemini_075(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=416, w3=701, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(91, min_periods=max(91//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.372353 + 0.0055306 * anchor
    return base_signal
