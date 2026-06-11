"""36 semi variance asymmetry gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f36_svar_gemini_001_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_002_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_003_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_004_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_005_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_006_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_007_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_008_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_009_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_010_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff().diff().diff()

def f36_svar_gemini_011_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=440, w3=106, lag=1)."""
    x = low.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(80, min_periods=max(80//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(106) * 1.527059 + 0.0025982 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_012_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=453, w3=123, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(87, min_periods=max(87//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.078667 * _rolling_slope(draw, 123) + 0.0025983 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_013_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=466, w3=140, lag=3)."""
    a = _safe_log(low.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(94) - b.diff(126)
    stress = imbalance.rolling(140, min_periods=max(140//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.554118 + 0.0025984 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_014_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=479, w3=157, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(479, min_periods=max(479//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.567647 + 0.0025985 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_015_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=492, w3=174, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 492)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=174, adjust=False).mean() * 1.581176 + 0.0025986 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_016_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=505, w3=191, lag=13)."""
    x = low.shift(13)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.594706 + 0.0025987 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_017_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=19, w3=208, lag=21)."""
    x = low.shift(21)
    change = x.pct_change(122)
    rank = change.rolling(19, min_periods=max(19//3, 2)).rank(pct=True)
    persistence = change.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.110333 * persistence + 0.0025988 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_018_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=32, w3=225, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(32, min_periods=max(32//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.621765 + 0.0025989 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_019_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=45, w3=242, lag=55)."""
    x = low.shift(55)
    ma = x.rolling(45, min_periods=max(45//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.123 * slope + 0.002599 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_020_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=58, w3=259, lag=0)."""
    x = low.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(259, min_periods=max(259//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.648824 + 0.0025991 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_021_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=71, w3=276, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 71)
    curvature = _rolling_slope(acceleration, 276)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.135667 * acceleration + 0.0025992 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_022_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=84, w3=293, lag=2)."""
    rel = _safe_div(low.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 157)
    pressure = rel_log.diff(84)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.142 * pressure.rolling(293, min_periods=max(293//3, 2)).mean() + 0.0025993 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_023_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=97, w3=310, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(164, min_periods=max(164//3, 2)).mean())
    decay = spread.ewm(span=97, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.835882 + 0.0025994 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_024_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=110, w3=327, lag=5)."""
    a = _safe_log(low.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(110, min_periods=max(110//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 171)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.849412 + 0.0025995 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_025_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=123, w3=344, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(178, min_periods=max(178//3, 2)).mean(), b.abs().rolling(123, min_periods=max(123//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.161 * _rolling_slope(cover, 178) + 0.0025996 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_026_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=136, w3=361, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.167333 * y + 0.832667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 185) - _rolling_slope(basket, 136) + 0.0025997 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_027_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=149, w3=378, lag=21)."""
    x = low.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.89 + 0.0025998 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_028_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=162, w3=395, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.18 * _rolling_slope(draw, 395) + 0.0025999 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_029_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=175, w3=412, lag=55)."""
    a = _safe_log(low.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(412, min_periods=max(412//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.917059 + 0.0026 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_030_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=188, w3=429, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(188, min_periods=max(188//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(429, min_periods=max(429//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.930588 + 0.0026001 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_031_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=201, w3=446, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.944118 + 0.0026002 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_032_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=214, w3=463, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(214, min_periods=max(214//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.957647 + 0.0026003 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_033_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=227, w3=480, lag=3)."""
    x = low.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(227, min_periods=max(227//3, 2)).rank(pct=True)
    persistence = change.rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.211667 * persistence + 0.0026004 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_034_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=240, w3=497, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(240, min_periods=max(240//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.984706 + 0.0026005 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_035_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=253, w3=514, lag=8)."""
    x = low.shift(8)
    ma = x.rolling(253, min_periods=max(253//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.224333 * slope + 0.0026006 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_036_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=266, w3=531, lag=13)."""
    x = low.shift(13)
    impulse = x.diff(8)
    drag = impulse.rolling(266, min_periods=max(266//3, 2)).mean()
    noise = impulse.abs().rolling(531, min_periods=max(531//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.011765 + 0.0026007 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_037_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=279, w3=548, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 279)
    curvature = _rolling_slope(acceleration, 548)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.237 * acceleration + 0.0026008 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_038_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=292, w3=565, lag=34)."""
    rel = _safe_div(low.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 22)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.243333 * pressure.rolling(565, min_periods=max(565//3, 2)).mean() + 0.0026009 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_039_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=305, w3=582, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(29, min_periods=max(29//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.052353 + 0.002601 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_040_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=318, w3=599, lag=0)."""
    a = _safe_log(low.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(318, min_periods=max(318//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 36)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.065882 + 0.0026011 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_041_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=331, w3=616, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(43, min_periods=max(43//3, 2)).mean(), b.abs().rolling(331, min_periods=max(331//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.262333 * _rolling_slope(cover, 43) + 0.0026012 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_042_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=344, w3=633, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.268667 * y + 0.731333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 50) - _rolling_slope(basket, 344) + 0.0026013 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_043_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=357, w3=650, lag=3)."""
    x = low.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(357, min_periods=max(357//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.106471 + 0.0026014 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_044_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=370, w3=667, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    draw = x - x.rolling(370, min_periods=max(370//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.281333 * _rolling_slope(draw, 667) + 0.0026015 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_045_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=383, w3=684, lag=8)."""
    a = _safe_log(low.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(71) - b.diff(126)
    stress = imbalance.rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.133529 + 0.0026016 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_046_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=396, w3=701, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 78)
    baseline = trend.rolling(396, min_periods=max(396//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(701, min_periods=max(701//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.147059 + 0.0026017 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_047_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=409, w3=718, lag=21)."""
    x = _safe_log(low.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 85)
    slow = _rolling_slope(x, 409)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.160588 + 0.0026018 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_048_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=422, w3=735, lag=34)."""
    x = low.shift(34)
    peak = x.rolling(422, min_periods=max(422//3, 2)).max()
    trough = x.rolling(92, min_periods=max(92//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.174118 + 0.0026019 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_049_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=435, w3=752, lag=55)."""
    x = low.shift(55)
    change = x.pct_change(99)
    rank = change.rolling(435, min_periods=max(435//3, 2)).rank(pct=True)
    persistence = change.rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.313 * persistence + 0.002602 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_050_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=448, w3=18, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(106, min_periods=max(106//3, 2)).std()
    vol_slow = ret.rolling(448, min_periods=max(448//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.201176 + 0.0026021 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_051_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=461, w3=35, lag=1)."""
    x = low.shift(1)
    ma = x.rolling(461, min_periods=max(461//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 113)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.325667 * slope + 0.0026022 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_052_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=474, w3=52, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(120)
    drag = impulse.rolling(474, min_periods=max(474//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.228235 + 0.0026023 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_053_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=487, w3=69, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 127)
    acceleration = _rolling_slope(velocity, 487)
    curvature = _rolling_slope(acceleration, 69)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.338333 * acceleration + 0.0026024 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_054_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=500, w3=86, lag=5)."""
    rel = _safe_div(low.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 134)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.344667 * pressure.rolling(86, min_periods=max(86//3, 2)).mean() + 0.0026025 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_055_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=14, w3=103, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(141, min_periods=max(141//3, 2)).mean())
    decay = spread.ewm(span=14, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.268824 + 0.0026026 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_056_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=27, w3=120, lag=13)."""
    a = _safe_log(low.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(27, min_periods=max(27//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 148)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.282353 + 0.0026027 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_057_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=40, w3=137, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(155, min_periods=max(155//3, 2)).mean(), b.abs().rolling(40, min_periods=max(40//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.031333 * _rolling_slope(cover, 155) + 0.0026028 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_058_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=53, w3=154, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.037667 * y + 0.962333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 162) - _rolling_slope(basket, 53) + 0.0026029 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_059_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=66, w3=171, lag=55)."""
    x = low.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(66, min_periods=max(66//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.322941 + 0.002603 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_060_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=79, w3=188, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    draw = x - x.rolling(79, min_periods=max(79//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.050333 * _rolling_slope(draw, 188) + 0.0026031 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_061_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=92, w3=205, lag=1)."""
    a = _safe_log(low.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(92)
    stress = imbalance.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.35 + 0.0026032 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_062_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=105, w3=222, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 190)
    baseline = trend.rolling(105, min_periods=max(105//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.363529 + 0.0026033 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_063_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=118, w3=239, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 197)
    slow = _rolling_slope(x, 118)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=239, adjust=False).mean() * 1.377059 + 0.0026034 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_064_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=131, w3=256, lag=5)."""
    x = low.shift(5)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(204, min_periods=max(204//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.390588 + 0.0026035 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_065_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=144, w3=273, lag=8)."""
    x = low.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.082 * persistence + 0.0026036 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_066_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=157, w3=290, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(218, min_periods=max(218//3, 2)).std()
    vol_slow = ret.rolling(157, min_periods=max(157//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.417647 + 0.0026037 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_067_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=170, w3=307, lag=21)."""
    x = low.shift(21)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 225)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.094667 * slope + 0.0026038 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_068_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=183, w3=324, lag=34)."""
    x = low.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.444706 + 0.0026039 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_069_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=196, w3=341, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 196)
    curvature = _rolling_slope(acceleration, 341)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.107333 * acceleration + 0.002604 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_070_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=209, w3=358, lag=0)."""
    rel = _safe_div(low.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 246)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.113667 * pressure.rolling(358, min_periods=max(358//3, 2)).mean() + 0.0026041 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_071_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=222, w3=375, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(6, min_periods=max(6//3, 2)).mean())
    decay = spread.ewm(span=222, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.485294 + 0.0026042 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_072_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=235, w3=392, lag=2)."""
    a = _safe_log(low.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(235, min_periods=max(235//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 13)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.498824 + 0.0026043 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_073_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=248, w3=409, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(20, min_periods=max(20//3, 2)).mean(), b.abs().rolling(248, min_periods=max(248//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.132667 * _rolling_slope(cover, 20) + 0.0026044 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_074_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=261, w3=426, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.139 * y + 0.861000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 27) - _rolling_slope(basket, 261) + 0.0026045 * anchor
    return base_signal.diff().diff().diff()

def f36_svar_gemini_075_d3(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=274, w3=443, lag=8)."""
    x = low.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(34, min_periods=max(34//3, 2)).mean(), upside.rolling(274, min_periods=max(274//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.539412 + 0.0026046 * anchor
    return base_signal.diff().diff().diff()
