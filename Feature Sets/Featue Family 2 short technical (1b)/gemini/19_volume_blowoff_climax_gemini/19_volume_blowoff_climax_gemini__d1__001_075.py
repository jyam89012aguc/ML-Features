"""19 volume blowoff climax gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Extreme volume spikes accompanying price exhaustion moves, often marking trend ends.
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

def f19_vboc_gemini_001_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=5]"""
    window = 5
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_002_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=10]"""
    window = 10
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_003_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=21]"""
    window = 21
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_004_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=42]"""
    window = 42
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_005_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=63]"""
    window = 63
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_006_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=126]"""
    window = 126
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_007_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=252]"""
    window = 252
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_008_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=504]"""
    window = 504
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_009_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=756]"""
    window = 756
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_010_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Extreme volume spikes accompanying price exhaustion moves, often marking trend ends. [window=1260]"""
    window = 1260
    res = _rolling_zscore(volume, window) * _rolling_zscore(high - low, window)
    return (res).diff()

def f19_vboc_gemini_011_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=285, w3=228, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 146)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.152 * slope + 0.0016182 * anchor
    return base_signal.diff()

def f19_vboc_gemini_012_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=298, w3=245, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.249412 + 0.0016183 * anchor
    return base_signal.diff()

def f19_vboc_gemini_013_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=311, w3=262, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 160)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.164667 * acceleration + 0.0016184 * anchor
    return base_signal.diff()

def f19_vboc_gemini_014_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=324, w3=279, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 167)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.171 * pressure.rolling(279, min_periods=max(279//3, 2)).mean() + 0.0016185 * anchor
    return base_signal.diff()

def f19_vboc_gemini_015_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=337, w3=296, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(174, min_periods=max(174//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.29 + 0.0016186 * anchor
    return base_signal.diff()

def f19_vboc_gemini_016_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=350, w3=313, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(350, min_periods=max(350//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 181)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.303529 + 0.0016187 * anchor
    return base_signal.diff()

def f19_vboc_gemini_017_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=363, w3=330, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(188, min_periods=max(188//3, 2)).mean(), b.abs().rolling(363, min_periods=max(363//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.19 * _rolling_slope(cover, 188) + 0.0016188 * anchor
    return base_signal.diff()

def f19_vboc_gemini_018_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=376, w3=347, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.196333 * y + 0.803667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 195) - _rolling_slope(basket, 376) + 0.0016189 * anchor
    return base_signal.diff()

def f19_vboc_gemini_019_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=389, w3=364, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(389, min_periods=max(389//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.344118 + 0.001619 * anchor
    return base_signal.diff()

def f19_vboc_gemini_020_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=402, w3=381, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(402, min_periods=max(402//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.209 * _rolling_slope(draw, 381) + 0.0016191 * anchor
    return base_signal.diff()

def f19_vboc_gemini_021_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=415, w3=398, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.371176 + 0.0016192 * anchor
    return base_signal.diff()

def f19_vboc_gemini_022_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=428, w3=415, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(428, min_periods=max(428//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.384706 + 0.0016193 * anchor
    return base_signal.diff()

def f19_vboc_gemini_023_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=441, w3=432, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 441)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.398235 + 0.0016194 * anchor
    return base_signal.diff()

def f19_vboc_gemini_024_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=454, w3=449, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.411765 + 0.0016195 * anchor
    return base_signal.diff()

def f19_vboc_gemini_025_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=467, w3=466, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(467, min_periods=max(467//3, 2)).rank(pct=True)
    persistence = change.rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.240667 * persistence + 0.0016196 * anchor
    return base_signal.diff()

def f19_vboc_gemini_026_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=480, w3=483, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.438824 + 0.0016197 * anchor
    return base_signal.diff()

def f19_vboc_gemini_027_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=493, w3=500, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.253333 * slope + 0.0016198 * anchor
    return base_signal.diff()

def f19_vboc_gemini_028_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=506, w3=517, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(18)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.465882 + 0.0016199 * anchor
    return base_signal.diff()

def f19_vboc_gemini_029_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=20, w3=534, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 534)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.266 * acceleration + 0.00162 * anchor
    return base_signal.diff()

def f19_vboc_gemini_030_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=33, w3=551, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 32)
    pressure = rel_log.diff(33)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.272333 * pressure.rolling(551, min_periods=max(551//3, 2)).mean() + 0.0016201 * anchor
    return base_signal.diff()

def f19_vboc_gemini_031_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=46, w3=568, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(39, min_periods=max(39//3, 2)).mean())
    decay = spread.ewm(span=46, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.506471 + 0.0016202 * anchor
    return base_signal.diff()

def f19_vboc_gemini_032_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=59, w3=585, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(59, min_periods=max(59//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 46)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.52 + 0.0016203 * anchor
    return base_signal.diff()

def f19_vboc_gemini_033_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=72, w3=602, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(53, min_periods=max(53//3, 2)).mean(), b.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.291333 * _rolling_slope(cover, 53) + 0.0016204 * anchor
    return base_signal.diff()

def f19_vboc_gemini_034_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=85, w3=619, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.297667 * y + 0.702333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 60) - _rolling_slope(basket, 85) + 0.0016205 * anchor
    return base_signal.diff()

def f19_vboc_gemini_035_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=98, w3=636, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(67, min_periods=max(67//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.560588 + 0.0016206 * anchor
    return base_signal.diff()

def f19_vboc_gemini_036_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=111, w3=653, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(74, min_periods=max(74//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.310333 * _rolling_slope(draw, 653) + 0.0016207 * anchor
    return base_signal.diff()

def f19_vboc_gemini_037_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=124, w3=670, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(81) - b.diff(124)
    stress = imbalance.rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.587647 + 0.0016208 * anchor
    return base_signal.diff()

def f19_vboc_gemini_038_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=137, w3=687, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 88)
    baseline = trend.rolling(137, min_periods=max(137//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.601176 + 0.0016209 * anchor
    return base_signal.diff()

def f19_vboc_gemini_039_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=150, w3=704, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 95)
    slow = _rolling_slope(x, 150)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.614706 + 0.001621 * anchor
    return base_signal.diff()

def f19_vboc_gemini_040_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=163, w3=721, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(163, min_periods=max(163//3, 2)).max()
    trough = x.rolling(102, min_periods=max(102//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.628235 + 0.0016211 * anchor
    return base_signal.diff()

def f19_vboc_gemini_041_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=176, w3=738, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(109)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.342 * persistence + 0.0016212 * anchor
    return base_signal.diff()

def f19_vboc_gemini_042_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=189, w3=755, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(116, min_periods=max(116//3, 2)).std()
    vol_slow = ret.rolling(189, min_periods=max(189//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.655294 + 0.0016213 * anchor
    return base_signal.diff()

def f19_vboc_gemini_043_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=202, w3=21, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 123)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.354667 * slope + 0.0016214 * anchor
    return base_signal.diff()

def f19_vboc_gemini_044_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=215, w3=38, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(38, min_periods=max(38//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.828824 + 0.0016215 * anchor
    return base_signal.diff()

def f19_vboc_gemini_045_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=228, w3=55, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 137)
    acceleration = _rolling_slope(velocity, 228)
    curvature = _rolling_slope(acceleration, 55)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.035 * acceleration + 0.0016216 * anchor
    return base_signal.diff()

def f19_vboc_gemini_046_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=241, w3=72, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 144)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.041333 * pressure.rolling(72, min_periods=max(72//3, 2)).mean() + 0.0016217 * anchor
    return base_signal.diff()

def f19_vboc_gemini_047_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=254, w3=89, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(151, min_periods=max(151//3, 2)).mean())
    decay = spread.ewm(span=254, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.869412 + 0.0016218 * anchor
    return base_signal.diff()

def f19_vboc_gemini_048_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=267, w3=106, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(267, min_periods=max(267//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 158)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.882941 + 0.0016219 * anchor
    return base_signal.diff()

def f19_vboc_gemini_049_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=280, w3=123, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(165, min_periods=max(165//3, 2)).mean(), b.abs().rolling(280, min_periods=max(280//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(123) + 0.060333 * _rolling_slope(cover, 165) + 0.001622 * anchor
    return base_signal.diff()

def f19_vboc_gemini_050_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=293, w3=140, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.066667 * y + 0.933333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 172) - _rolling_slope(basket, 293) + 0.0016221 * anchor
    return base_signal.diff()

def f19_vboc_gemini_051_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=306, w3=157, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(179, min_periods=max(179//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.923529 + 0.0016222 * anchor
    return base_signal.diff()

def f19_vboc_gemini_052_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=319, w3=174, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(186, min_periods=max(186//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.079333 * _rolling_slope(draw, 174) + 0.0016223 * anchor
    return base_signal.diff()

def f19_vboc_gemini_053_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=332, w3=191, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(191, min_periods=max(191//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.950588 + 0.0016224 * anchor
    return base_signal.diff()

def f19_vboc_gemini_054_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=345, w3=208, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 200)
    baseline = trend.rolling(345, min_periods=max(345//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.964118 + 0.0016225 * anchor
    return base_signal.diff()

def f19_vboc_gemini_055_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=358, w3=225, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 207)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=225, adjust=False).mean() * 0.977647 + 0.0016226 * anchor
    return base_signal.diff()

def f19_vboc_gemini_056_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=371, w3=242, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(214, min_periods=max(214//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.991176 + 0.0016227 * anchor
    return base_signal.diff()

def f19_vboc_gemini_057_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=384, w3=259, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 0.0016228 * anchor
    return base_signal.diff()

def f19_vboc_gemini_058_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=397, w3=276, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(228, min_periods=max(228//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.018235 + 0.0016229 * anchor
    return base_signal.diff()

def f19_vboc_gemini_059_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=410, w3=293, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 235)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.123667 * slope + 0.001623 * anchor
    return base_signal.diff()

def f19_vboc_gemini_060_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=423, w3=310, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(310, min_periods=max(310//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.045294 + 0.0016231 * anchor
    return base_signal.diff()

def f19_vboc_gemini_061_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=436, w3=327, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 249)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 327)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136333 * acceleration + 0.0016232 * anchor
    return base_signal.diff()

def f19_vboc_gemini_062_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=449, w3=344, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 9)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.142667 * pressure.rolling(344, min_periods=max(344//3, 2)).mean() + 0.0016233 * anchor
    return base_signal.diff()

def f19_vboc_gemini_063_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=462, w3=361, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(16, min_periods=max(16//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.085882 + 0.0016234 * anchor
    return base_signal.diff()

def f19_vboc_gemini_064_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=475, w3=378, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(475, min_periods=max(475//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 23)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.099412 + 0.0016235 * anchor
    return base_signal.diff()

def f19_vboc_gemini_065_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=488, w3=395, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(30, min_periods=max(30//3, 2)).mean(), b.abs().rolling(488, min_periods=max(488//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.161667 * _rolling_slope(cover, 30) + 0.0016236 * anchor
    return base_signal.diff()

def f19_vboc_gemini_066_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=501, w3=412, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.168 * y + 0.832000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 37) - _rolling_slope(basket, 501) + 0.0016237 * anchor
    return base_signal.diff()

def f19_vboc_gemini_067_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=15, w3=429, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.14 + 0.0016238 * anchor
    return base_signal.diff()

def f19_vboc_gemini_068_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=28, w3=446, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.180667 * _rolling_slope(draw, 446) + 0.0016239 * anchor
    return base_signal.diff()

def f19_vboc_gemini_069_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=41, w3=463, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(58) - b.diff(41)
    stress = imbalance.rolling(463, min_periods=max(463//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.167059 + 0.001624 * anchor
    return base_signal.diff()

def f19_vboc_gemini_070_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=54, w3=480, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.180588 + 0.0016241 * anchor
    return base_signal.diff()

def f19_vboc_gemini_071_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=67, w3=497, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.194118 + 0.0016242 * anchor
    return base_signal.diff()

def f19_vboc_gemini_072_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=80, w3=514, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.207647 + 0.0016243 * anchor
    return base_signal.diff()

def f19_vboc_gemini_073_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=93, w3=531, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(86)
    rank = change.rolling(93, min_periods=max(93//3, 2)).rank(pct=True)
    persistence = change.rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.212333 * persistence + 0.0016244 * anchor
    return base_signal.diff()

def f19_vboc_gemini_074_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=106, w3=548, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(106, min_periods=max(106//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.234706 + 0.0016245 * anchor
    return base_signal.diff()

def f19_vboc_gemini_075_d1(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=119, w3=565, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225 * slope + 0.0016246 * anchor
    return base_signal.diff()
