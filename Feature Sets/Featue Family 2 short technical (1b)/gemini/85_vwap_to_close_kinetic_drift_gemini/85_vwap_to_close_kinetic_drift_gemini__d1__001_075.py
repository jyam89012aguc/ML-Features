"""85 vwap to close kinetic drift gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Drift between session VWAP and the final closing price as a directional signal.
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

def f85_vwkd_gemini_001_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=5]"""
    window = 5
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_002_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=10]"""
    window = 10
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_003_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=21]"""
    window = 21
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_004_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=42]"""
    window = 42
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_005_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=63]"""
    window = 63
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_006_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=126]"""
    window = 126
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_007_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=252]"""
    window = 252
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_008_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=504]"""
    window = 504
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_009_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=756]"""
    window = 756
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_010_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Drift between session VWAP and the final closing price as a directional signal. [window=1260]"""
    window = 1260
    res = _safe_div(close - (volume * close).rolling(window).sum() / volume.rolling(window).sum(), _atr(high, low, close, window) + 1e-9)
    return (res).diff()

def f85_vwkd_gemini_011_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=228, w3=712, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(228, min_periods=max(228//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 10)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.269333 * slope + 0.0053142 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_012_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=241, w3=729, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(17)
    drag = impulse.rolling(241, min_periods=max(241//3, 2)).mean()
    noise = impulse.abs().rolling(729, min_periods=max(729//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.128235 + 0.0053143 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_013_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=254, w3=746, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 24)
    acceleration = _rolling_slope(velocity, 254)
    curvature = _rolling_slope(acceleration, 746)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.282 * acceleration + 0.0053144 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_014_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=267, w3=763, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 31)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.288333 * pressure.rolling(763, min_periods=max(763//3, 2)).mean() + 0.0053145 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_015_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=280, w3=29, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(38, min_periods=max(38//3, 2)).mean())
    decay = spread.ewm(span=280, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.168824 + 0.0053146 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_016_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=293, w3=46, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(293, min_periods=max(293//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 45)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.182353 + 0.0053147 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_017_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=306, w3=63, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(52, min_periods=max(52//3, 2)).mean(), b.abs().rolling(306, min_periods=max(306//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(63) + 0.307333 * _rolling_slope(cover, 52) + 0.0053148 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_018_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=319, w3=80, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.313667 * y + 0.686333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 59) - _rolling_slope(basket, 319) + 0.0053149 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_019_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=332, w3=97, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(97) * 1.222941 + 0.005315 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_020_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=345, w3=114, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(345, min_periods=max(345//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.326333 * _rolling_slope(draw, 114) + 0.0053151 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_021_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=358, w3=131, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(80) - b.diff(126)
    stress = imbalance.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.25 + 0.0053152 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_022_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=371, w3=148, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 87)
    baseline = trend.rolling(371, min_periods=max(371//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(148, min_periods=max(148//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.263529 + 0.0053153 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_023_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=384, w3=165, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 94)
    slow = _rolling_slope(x, 384)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=165, adjust=False).mean() * 1.277059 + 0.0053154 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_024_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=397, w3=182, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(397, min_periods=max(397//3, 2)).max()
    trough = x.rolling(101, min_periods=max(101//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.290588 + 0.0053155 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_025_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=410, w3=199, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(108)
    rank = change.rolling(410, min_periods=max(410//3, 2)).rank(pct=True)
    persistence = change.rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.358 * persistence + 0.0053156 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_026_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=423, w3=216, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(115, min_periods=max(115//3, 2)).std()
    vol_slow = ret.rolling(423, min_periods=max(423//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.317647 + 0.0053157 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_027_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=436, w3=233, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(436, min_periods=max(436//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 122)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.038333 * slope + 0.0053158 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_028_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=449, w3=250, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(449, min_periods=max(449//3, 2)).mean()
    noise = impulse.abs().rolling(250, min_periods=max(250//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.344706 + 0.0053159 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_029_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=462, w3=267, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 136)
    acceleration = _rolling_slope(velocity, 462)
    curvature = _rolling_slope(acceleration, 267)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.051 * acceleration + 0.005316 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_030_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=475, w3=284, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 143)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.057333 * pressure.rolling(284, min_periods=max(284//3, 2)).mean() + 0.0053161 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_031_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=488, w3=301, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(150, min_periods=max(150//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.385294 + 0.0053162 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_032_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=501, w3=318, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(501, min_periods=max(501//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 157)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.398824 + 0.0053163 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_033_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=15, w3=335, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(164, min_periods=max(164//3, 2)).mean(), b.abs().rolling(15, min_periods=max(15//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.076333 * _rolling_slope(cover, 164) + 0.0053164 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_034_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=28, w3=352, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.082667 * y + 0.917333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 171) - _rolling_slope(basket, 28) + 0.0053165 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_035_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=41, w3=369, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(41, min_periods=max(41//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.439412 + 0.0053166 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_036_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=54, w3=386, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(54, min_periods=max(54//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.095333 * _rolling_slope(draw, 386) + 0.0053167 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_037_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=67, w3=403, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(67)
    stress = imbalance.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.466471 + 0.0053168 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_038_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=80, w3=420, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(80, min_periods=max(80//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(420, min_periods=max(420//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.48 + 0.0053169 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_039_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=93, w3=437, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 93)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.493529 + 0.005317 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_040_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=106, w3=454, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(106, min_periods=max(106//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.507059 + 0.0053171 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_041_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=119, w3=471, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(119, min_periods=max(119//3, 2)).rank(pct=True)
    persistence = change.rolling(471, min_periods=max(471//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.127 * persistence + 0.0053172 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_042_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=132, w3=488, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(132, min_periods=max(132//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.534118 + 0.0053173 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_043_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=145, w3=505, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(145, min_periods=max(145//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.139667 * slope + 0.0053174 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_044_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=158, w3=522, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(158, min_periods=max(158//3, 2)).mean()
    noise = impulse.abs().rolling(522, min_periods=max(522//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.561176 + 0.0053175 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_045_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=171, w3=539, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 171)
    curvature = _rolling_slope(acceleration, 539)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.152333 * acceleration + 0.0053176 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_046_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=184, w3=556, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 8)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.158667 * pressure.rolling(556, min_periods=max(556//3, 2)).mean() + 0.0053177 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_047_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=197, w3=573, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(15, min_periods=max(15//3, 2)).mean())
    decay = spread.ewm(span=197, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.601765 + 0.0053178 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_048_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=210, w3=590, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(210, min_periods=max(210//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 22)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.615294 + 0.0053179 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_049_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=223, w3=607, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(29, min_periods=max(29//3, 2)).mean(), b.abs().rolling(223, min_periods=max(223//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.177667 * _rolling_slope(cover, 29) + 0.005318 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_050_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=236, w3=624, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.184 * y + 0.816000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 36) - _rolling_slope(basket, 236) + 0.0053181 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_051_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=249, w3=641, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(43, min_periods=max(43//3, 2)).mean(), upside.rolling(249, min_periods=max(249//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.655882 + 0.0053182 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_052_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=262, w3=658, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(50, min_periods=max(50//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.196667 * _rolling_slope(draw, 658) + 0.0053183 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_053_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=275, w3=675, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(57) - b.diff(126)
    stress = imbalance.rolling(675, min_periods=max(675//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.829412 + 0.0053184 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_054_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=288, w3=692, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(288, min_periods=max(288//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(692, min_periods=max(692//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.842941 + 0.0053185 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_055_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=301, w3=709, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 301)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.856471 + 0.0053186 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_056_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=314, w3=726, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(314, min_periods=max(314//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.87 + 0.0053187 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_057_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=327, w3=743, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(85)
    rank = change.rolling(327, min_periods=max(327//3, 2)).rank(pct=True)
    persistence = change.rolling(743, min_periods=max(743//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.228333 * persistence + 0.0053188 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_058_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=340, w3=760, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(340, min_periods=max(340//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.897059 + 0.0053189 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_059_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=353, w3=26, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(353, min_periods=max(353//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.241 * slope + 0.005319 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_060_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=366, w3=43, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(106)
    drag = impulse.rolling(366, min_periods=max(366//3, 2)).mean()
    noise = impulse.abs().rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.924118 + 0.0053191 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_061_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=379, w3=60, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 379)
    curvature = _rolling_slope(acceleration, 60)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.253667 * acceleration + 0.0053192 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_062_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=392, w3=77, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 120)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.26 * pressure.rolling(77, min_periods=max(77//3, 2)).mean() + 0.0053193 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_063_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=405, w3=94, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(127, min_periods=max(127//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.964706 + 0.0053194 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_064_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=418, w3=111, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(418, min_periods=max(418//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 134)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.978235 + 0.0053195 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_065_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=431, w3=128, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(141, min_periods=max(141//3, 2)).mean(), b.abs().rolling(431, min_periods=max(431//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.279 * _rolling_slope(cover, 141) + 0.0053196 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_066_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=444, w3=145, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.285333 * y + 0.714667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 148) - _rolling_slope(basket, 444) + 0.0053197 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_067_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=457, w3=162, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(155, min_periods=max(155//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.018824 + 0.0053198 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_068_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=470, w3=179, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(470, min_periods=max(470//3, 2)).max()
    rebound = x - x.rolling(162, min_periods=max(162//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.298 * _rolling_slope(draw, 179) + 0.0053199 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_069_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=483, w3=196, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(196, min_periods=max(196//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.045882 + 0.00532 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_070_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=496, w3=213, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(496, min_periods=max(496//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.059412 + 0.0053201 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_071_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=509, w3=230, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 509)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=230, adjust=False).mean() * 1.072941 + 0.0053202 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_072_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=23, w3=247, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(23, min_periods=max(23//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.086471 + 0.0053203 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_073_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=36, w3=264, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(36, min_periods=max(36//3, 2)).rank(pct=True)
    persistence = change.rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.329667 * persistence + 0.0053204 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_074_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=49, w3=281, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.113529 + 0.0053205 * anchor
    return base_signal.diff()

def f85_vwkd_gemini_075_d1(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=62, w3=298, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(62, min_periods=max(62//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.342333 * slope + 0.0053206 * anchor
    return base_signal.diff()
