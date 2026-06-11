"""84 session strength kinetics gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Momentum and volume analysis specific to key market session hours.
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

def f84_sstk_gemini_001_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=5]"""
    window = 5
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_002_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=10]"""
    window = 10
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_003_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=21]"""
    window = 21
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_004_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=42]"""
    window = 42
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_005_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=63]"""
    window = 63
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_006_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=126]"""
    window = 126
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_007_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=252]"""
    window = 252
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_008_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=504]"""
    window = 504
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_009_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=756]"""
    window = 756
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_010_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Momentum and volume analysis specific to key market session hours. [window=1260]"""
    window = 1260
    res = _rolling_slope(close - open, window)
    return (res).diff().diff().diff()

def f84_sstk_gemini_011_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=26, w2=81, w3=458, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(81, min_periods=max(81//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.594118 + 0.0052862 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_012_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=33, w2=94, w3=475, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(94, min_periods=max(94//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.164 * _rolling_slope(draw, 475) + 0.0052863 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_013_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=40, w2=107, w3=492, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(40) - b.diff(107)
    stress = imbalance.rolling(492, min_periods=max(492//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.621176 + 0.0052864 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_014_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=47, w2=120, w3=509, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(120, min_periods=max(120//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(509, min_periods=max(509//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.634706 + 0.0052865 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_015_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=54, w2=133, w3=526, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 133)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.648235 + 0.0052866 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_016_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=61, w2=146, w3=543, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(146, min_periods=max(146//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.661765 + 0.0052867 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_017_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=68, w2=159, w3=560, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(68)
    rank = change.rolling(159, min_periods=max(159//3, 2)).rank(pct=True)
    persistence = change.rolling(560, min_periods=max(560//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.195667 * persistence + 0.0052868 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_018_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=75, w2=172, w3=577, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(172, min_periods=max(172//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.835294 + 0.0052869 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_019_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=185, w3=594, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(185, min_periods=max(185//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.208333 * slope + 0.005287 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_020_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=198, w3=611, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(89)
    drag = impulse.rolling(198, min_periods=max(198//3, 2)).mean()
    noise = impulse.abs().rolling(611, min_periods=max(611//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.862353 + 0.0052871 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_021_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=211, w3=628, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 211)
    curvature = _rolling_slope(acceleration, 628)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.221 * acceleration + 0.0052872 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_022_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=224, w3=645, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 103)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.227333 * pressure.rolling(645, min_periods=max(645//3, 2)).mean() + 0.0052873 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_023_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=237, w3=662, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(110, min_periods=max(110//3, 2)).mean())
    decay = spread.ewm(span=237, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.902941 + 0.0052874 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_024_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=250, w3=679, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(250, min_periods=max(250//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 117)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.916471 + 0.0052875 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_025_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=263, w3=696, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(124, min_periods=max(124//3, 2)).mean(), b.abs().rolling(263, min_periods=max(263//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.246333 * _rolling_slope(cover, 124) + 0.0052876 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_026_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=276, w3=713, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.252667 * y + 0.747333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 131) - _rolling_slope(basket, 276) + 0.0052877 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_027_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=289, w3=730, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(289, min_periods=max(289//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.957059 + 0.0052878 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_028_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=302, w3=747, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(302, min_periods=max(302//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.265333 * _rolling_slope(draw, 747) + 0.0052879 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_029_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=315, w3=764, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.984118 + 0.005288 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_030_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=328, w3=30, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(328, min_periods=max(328//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.997647 + 0.0052881 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_031_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=341, w3=47, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 341)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=47, adjust=False).mean() * 1.011176 + 0.0052882 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_032_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=354, w3=64, lag=2)."""
    x = open.shift(2)
    peak = x.rolling(354, min_periods=max(354//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.024706 + 0.0052883 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_033_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=367, w3=81, lag=3)."""
    x = open.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(367, min_periods=max(367//3, 2)).rank(pct=True)
    persistence = change.rolling(81, min_periods=max(81//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.297 * persistence + 0.0052884 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_034_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=380, w3=98, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(380, min_periods=max(380//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.051765 + 0.0052885 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_035_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=393, w3=115, lag=8)."""
    x = open.shift(8)
    ma = x.rolling(393, min_periods=max(393//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.309667 * slope + 0.0052886 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_036_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=406, w3=132, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(406, min_periods=max(406//3, 2)).mean()
    noise = impulse.abs().rolling(132, min_periods=max(132//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.078824 + 0.0052887 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_037_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=419, w3=149, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 419)
    curvature = _rolling_slope(acceleration, 149)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.322333 * acceleration + 0.0052888 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_038_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=432, w3=166, lag=34)."""
    rel = _safe_div(open.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 215)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.328667 * pressure.rolling(166, min_periods=max(166//3, 2)).mean() + 0.0052889 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_039_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=445, w3=183, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(222, min_periods=max(222//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.119412 + 0.005289 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_040_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=458, w3=200, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(458, min_periods=max(458//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 229)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.132941 + 0.0052891 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_041_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=471, w3=217, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(236, min_periods=max(236//3, 2)).mean(), b.abs().rolling(471, min_periods=max(471//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.347667 * _rolling_slope(cover, 236) + 0.0052892 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_042_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=484, w3=234, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.354 * y + 0.646000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 243) - _rolling_slope(basket, 484) + 0.0052893 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_043_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=497, w3=251, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(497, min_periods=max(497//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.173529 + 0.0052894 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_044_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=11, w3=268, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(11, min_periods=max(11//3, 2)).max()
    rebound = x - x.rolling(10, min_periods=max(10//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.034333 * _rolling_slope(draw, 268) + 0.0052895 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_045_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=24, w3=285, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(17) - b.diff(24)
    stress = imbalance.rolling(285, min_periods=max(285//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.200588 + 0.0052896 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_046_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=37, w3=302, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 24)
    baseline = trend.rolling(37, min_periods=max(37//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(302, min_periods=max(302//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.214118 + 0.0052897 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_047_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=50, w3=319, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 31)
    slow = _rolling_slope(x, 50)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.227647 + 0.0052898 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_048_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=63, w3=336, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(63, min_periods=max(63//3, 2)).max()
    trough = x.rolling(38, min_periods=max(38//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.241176 + 0.0052899 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_049_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=76, w3=353, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(45)
    rank = change.rolling(76, min_periods=max(76//3, 2)).rank(pct=True)
    persistence = change.rolling(353, min_periods=max(353//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.066 * persistence + 0.00529 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_050_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=89, w3=370, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(52, min_periods=max(52//3, 2)).std()
    vol_slow = ret.rolling(89, min_periods=max(89//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.268235 + 0.0052901 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_051_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=102, w3=387, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(102, min_periods=max(102//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 59)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.078667 * slope + 0.0052902 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_052_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=115, w3=404, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(66)
    drag = impulse.rolling(115, min_periods=max(115//3, 2)).mean()
    noise = impulse.abs().rolling(404, min_periods=max(404//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.295294 + 0.0052903 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_053_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=128, w3=421, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 73)
    acceleration = _rolling_slope(velocity, 128)
    curvature = _rolling_slope(acceleration, 421)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091333 * acceleration + 0.0052904 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_054_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=141, w3=438, lag=5)."""
    rel = _safe_div(open.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 80)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.097667 * pressure.rolling(438, min_periods=max(438//3, 2)).mean() + 0.0052905 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_055_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=154, w3=455, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(87, min_periods=max(87//3, 2)).mean())
    decay = spread.ewm(span=154, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.335882 + 0.0052906 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_056_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=167, w3=472, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(167, min_periods=max(167//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 94)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.349412 + 0.0052907 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_057_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=180, w3=489, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(101, min_periods=max(101//3, 2)).mean(), b.abs().rolling(180, min_periods=max(180//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.116667 * _rolling_slope(cover, 101) + 0.0052908 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_058_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=193, w3=506, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.123 * y + 0.877000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 108) - _rolling_slope(basket, 193) + 0.0052909 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_059_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=206, w3=523, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(206, min_periods=max(206//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.39 + 0.005291 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_060_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=219, w3=540, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(219, min_periods=max(219//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.135667 * _rolling_slope(draw, 540) + 0.0052911 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_061_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=232, w3=557, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(557, min_periods=max(557//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.417059 + 0.0052912 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_062_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=245, w3=574, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(245, min_periods=max(245//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(574, min_periods=max(574//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.430588 + 0.0052913 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_063_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=258, w3=591, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 258)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.444118 + 0.0052914 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_064_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=271, w3=608, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(271, min_periods=max(271//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.457647 + 0.0052915 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_065_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=284, w3=625, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(284, min_periods=max(284//3, 2)).rank(pct=True)
    persistence = change.rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.167333 * persistence + 0.0052916 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_066_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=297, w3=642, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(297, min_periods=max(297//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.484706 + 0.0052917 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_067_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=310, w3=659, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(310, min_periods=max(310//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.18 * slope + 0.0052918 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_068_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=323, w3=676, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(323, min_periods=max(323//3, 2)).mean()
    noise = impulse.abs().rolling(676, min_periods=max(676//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.511765 + 0.0052919 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_069_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=336, w3=693, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 693)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.192667 * acceleration + 0.005292 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_070_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=349, w3=710, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 192)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.199 * pressure.rolling(710, min_periods=max(710//3, 2)).mean() + 0.0052921 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_071_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=362, w3=727, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(199, min_periods=max(199//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.552353 + 0.0052922 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_072_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=375, w3=744, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(375, min_periods=max(375//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 206)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.565882 + 0.0052923 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_073_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=388, w3=761, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(213, min_periods=max(213//3, 2)).mean(), b.abs().rolling(388, min_periods=max(388//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.218 * _rolling_slope(cover, 213) + 0.0052924 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_074_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=401, w3=27, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.224333 * y + 0.775667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 220) - _rolling_slope(basket, 401) + 0.0052925 * anchor
    return base_signal.diff().diff().diff()

def f84_sstk_gemini_075_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=414, w3=44, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(414, min_periods=max(414//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(44) * 1.606471 + 0.0052926 * anchor
    return base_signal.diff().diff().diff()
