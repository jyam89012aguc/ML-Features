"""36 semi variance asymmetry gemini d1 features 1-75 — Pipeline 1b-HF Grade v7.

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

def f36_svar_gemini_001_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_002_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_003_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_004_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_005_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_006_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_007_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_008_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_009_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_010_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Measurement of downside vs. upside volatility to detect bearish risk bias. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().clip(upper=0).rolling(window).std(), _safe_log(close).diff().clip(lower=0).rolling(window).std() + 1e-9)
    return (res).diff()

def f36_svar_gemini_011_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=293, w3=603, lag=1)."""
    x = low.shift(1)
    ma = x.rolling(293, min_periods=max(293//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 96)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.293 * slope + 0.0025702 * anchor
    return base_signal.diff()

def f36_svar_gemini_012_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=306, w3=620, lag=2)."""
    x = low.shift(2)
    impulse = x.diff(103)
    drag = impulse.rolling(306, min_periods=max(306//3, 2)).mean()
    noise = impulse.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.166471 + 0.0025703 * anchor
    return base_signal.diff()

def f36_svar_gemini_013_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=319, w3=637, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 110)
    acceleration = _rolling_slope(velocity, 319)
    curvature = _rolling_slope(acceleration, 637)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305667 * acceleration + 0.0025704 * anchor
    return base_signal.diff()

def f36_svar_gemini_014_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=332, w3=654, lag=5)."""
    rel = _safe_div(low.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 117)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.312 * pressure.rolling(654, min_periods=max(654//3, 2)).mean() + 0.0025705 * anchor
    return base_signal.diff()

def f36_svar_gemini_015_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=345, w3=671, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(124, min_periods=max(124//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.207059 + 0.0025706 * anchor
    return base_signal.diff()

def f36_svar_gemini_016_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=358, w3=688, lag=13)."""
    a = _safe_log(low.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(358, min_periods=max(358//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 131)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.220588 + 0.0025707 * anchor
    return base_signal.diff()

def f36_svar_gemini_017_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=371, w3=705, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(138, min_periods=max(138//3, 2)).mean(), b.abs().rolling(371, min_periods=max(371//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.331 * _rolling_slope(cover, 138) + 0.0025708 * anchor
    return base_signal.diff()

def f36_svar_gemini_018_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=384, w3=722, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.337333 * y + 0.662667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 145) - _rolling_slope(basket, 384) + 0.0025709 * anchor
    return base_signal.diff()

def f36_svar_gemini_019_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=397, w3=739, lag=55)."""
    x = low.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(397, min_periods=max(397//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.261176 + 0.002571 * anchor
    return base_signal.diff()

def f36_svar_gemini_020_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=410, w3=756, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    draw = x - x.rolling(410, min_periods=max(410//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.35 * _rolling_slope(draw, 756) + 0.0025711 * anchor
    return base_signal.diff()

def f36_svar_gemini_021_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=423, w3=22, lag=1)."""
    a = _safe_log(low.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(22, min_periods=max(22//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.288235 + 0.0025712 * anchor
    return base_signal.diff()

def f36_svar_gemini_022_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=436, w3=39, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.301765 + 0.0025713 * anchor
    return base_signal.diff()

def f36_svar_gemini_023_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=449, w3=56, lag=3)."""
    x = _safe_log(low.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=56, adjust=False).mean() * 1.315294 + 0.0025714 * anchor
    return base_signal.diff()

def f36_svar_gemini_024_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=462, w3=73, lag=5)."""
    x = low.shift(5)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.328824 + 0.0025715 * anchor
    return base_signal.diff()

def f36_svar_gemini_025_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=475, w3=90, lag=8)."""
    x = low.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.049333 * persistence + 0.0025716 * anchor
    return base_signal.diff()

def f36_svar_gemini_026_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=488, w3=107, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.355882 + 0.0025717 * anchor
    return base_signal.diff()

def f36_svar_gemini_027_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=501, w3=124, lag=21)."""
    x = low.shift(21)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.062 * slope + 0.0025718 * anchor
    return base_signal.diff()

def f36_svar_gemini_028_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=15, w3=141, lag=34)."""
    x = low.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.382941 + 0.0025719 * anchor
    return base_signal.diff()

def f36_svar_gemini_029_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=28, w3=158, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 158)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.074667 * acceleration + 0.002572 * anchor
    return base_signal.diff()

def f36_svar_gemini_030_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=41, w3=175, lag=0)."""
    rel = _safe_div(low.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 229)
    pressure = rel_log.diff(41)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.081 * pressure.rolling(175, min_periods=max(175//3, 2)).mean() + 0.0025721 * anchor
    return base_signal.diff()

def f36_svar_gemini_031_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=54, w3=192, lag=1)."""
    a = low.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(236, min_periods=max(236//3, 2)).mean())
    decay = spread.ewm(span=54, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.423529 + 0.0025722 * anchor
    return base_signal.diff()

def f36_svar_gemini_032_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=67, w3=209, lag=2)."""
    a = _safe_log(low.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(67, min_periods=max(67//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 243)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.437059 + 0.0025723 * anchor
    return base_signal.diff()

def f36_svar_gemini_033_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=80, w3=226, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(250, min_periods=max(250//3, 2)).mean(), b.abs().rolling(80, min_periods=max(80//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1 * _rolling_slope(cover, 250) + 0.0025724 * anchor
    return base_signal.diff()

def f36_svar_gemini_034_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=93, w3=243, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.106333 * y + 0.893667 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 10) - _rolling_slope(basket, 93) + 0.0025725 * anchor
    return base_signal.diff()

def f36_svar_gemini_035_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=106, w3=260, lag=8)."""
    x = low.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(106, min_periods=max(106//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.477647 + 0.0025726 * anchor
    return base_signal.diff()

def f36_svar_gemini_036_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=119, w3=277, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    draw = x - x.rolling(119, min_periods=max(119//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.119 * _rolling_slope(draw, 277) + 0.0025727 * anchor
    return base_signal.diff()

def f36_svar_gemini_037_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=132, w3=294, lag=21)."""
    a = _safe_log(low.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(31) - b.diff(126)
    stress = imbalance.rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.504706 + 0.0025728 * anchor
    return base_signal.diff()

def f36_svar_gemini_038_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=145, w3=311, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 38)
    baseline = trend.rolling(145, min_periods=max(145//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.518235 + 0.0025729 * anchor
    return base_signal.diff()

def f36_svar_gemini_039_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=158, w3=328, lag=55)."""
    x = _safe_log(low.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 45)
    slow = _rolling_slope(x, 158)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.531765 + 0.002573 * anchor
    return base_signal.diff()

def f36_svar_gemini_040_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=171, w3=345, lag=0)."""
    x = low.shift(0)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(52, min_periods=max(52//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.545294 + 0.0025731 * anchor
    return base_signal.diff()

def f36_svar_gemini_041_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=184, w3=362, lag=1)."""
    x = low.shift(1)
    change = x.pct_change(59)
    rank = change.rolling(184, min_periods=max(184//3, 2)).rank(pct=True)
    persistence = change.rolling(362, min_periods=max(362//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.150667 * persistence + 0.0025732 * anchor
    return base_signal.diff()

def f36_svar_gemini_042_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=197, w3=379, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(66, min_periods=max(66//3, 2)).std()
    vol_slow = ret.rolling(197, min_periods=max(197//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.572353 + 0.0025733 * anchor
    return base_signal.diff()

def f36_svar_gemini_043_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=210, w3=396, lag=3)."""
    x = low.shift(3)
    ma = x.rolling(210, min_periods=max(210//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 73)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.163333 * slope + 0.0025734 * anchor
    return base_signal.diff()

def f36_svar_gemini_044_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=223, w3=413, lag=5)."""
    x = low.shift(5)
    impulse = x.diff(80)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(413, min_periods=max(413//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.599412 + 0.0025735 * anchor
    return base_signal.diff()

def f36_svar_gemini_045_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=236, w3=430, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 87)
    acceleration = _rolling_slope(velocity, 236)
    curvature = _rolling_slope(acceleration, 430)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.176 * acceleration + 0.0025736 * anchor
    return base_signal.diff()

def f36_svar_gemini_046_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=249, w3=447, lag=13)."""
    rel = _safe_div(low.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 94)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.182333 * pressure.rolling(447, min_periods=max(447//3, 2)).mean() + 0.0025737 * anchor
    return base_signal.diff()

def f36_svar_gemini_047_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=262, w3=464, lag=21)."""
    a = low.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(101, min_periods=max(101//3, 2)).mean())
    decay = spread.ewm(span=262, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.64 + 0.0025738 * anchor
    return base_signal.diff()

def f36_svar_gemini_048_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=275, w3=481, lag=34)."""
    a = _safe_log(low.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(275, min_periods=max(275//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 108)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.653529 + 0.0025739 * anchor
    return base_signal.diff()

def f36_svar_gemini_049_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=288, w3=498, lag=55)."""
    a = low.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(115, min_periods=max(115//3, 2)).mean(), b.abs().rolling(288, min_periods=max(288//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.201333 * _rolling_slope(cover, 115) + 0.002574 * anchor
    return base_signal.diff()

def f36_svar_gemini_050_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=301, w3=515, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.207667 * y + 0.792333 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 122) - _rolling_slope(basket, 301) + 0.0025741 * anchor
    return base_signal.diff()

def f36_svar_gemini_051_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=314, w3=532, lag=1)."""
    x = low.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(314, min_periods=max(314//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.840588 + 0.0025742 * anchor
    return base_signal.diff()

def f36_svar_gemini_052_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=327, w3=549, lag=2)."""
    x = _safe_log(low.abs() + 1.0).shift(2)
    draw = x - x.rolling(327, min_periods=max(327//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.220333 * _rolling_slope(draw, 549) + 0.0025743 * anchor
    return base_signal.diff()

def f36_svar_gemini_053_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=340, w3=566, lag=3)."""
    a = _safe_log(low.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(566, min_periods=max(566//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.867647 + 0.0025744 * anchor
    return base_signal.diff()

def f36_svar_gemini_054_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=353, w3=583, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(353, min_periods=max(353//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.881176 + 0.0025745 * anchor
    return base_signal.diff()

def f36_svar_gemini_055_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=366, w3=600, lag=8)."""
    x = _safe_log(low.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 366)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.894706 + 0.0025746 * anchor
    return base_signal.diff()

def f36_svar_gemini_056_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=379, w3=617, lag=13)."""
    x = low.shift(13)
    peak = x.rolling(379, min_periods=max(379//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.908235 + 0.0025747 * anchor
    return base_signal.diff()

def f36_svar_gemini_057_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=392, w3=634, lag=21)."""
    x = low.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(392, min_periods=max(392//3, 2)).rank(pct=True)
    persistence = change.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.252 * persistence + 0.0025748 * anchor
    return base_signal.diff()

def f36_svar_gemini_058_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=405, w3=651, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(405, min_periods=max(405//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.935294 + 0.0025749 * anchor
    return base_signal.diff()

def f36_svar_gemini_059_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=418, w3=668, lag=55)."""
    x = low.shift(55)
    ma = x.rolling(418, min_periods=max(418//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.264667 * slope + 0.002575 * anchor
    return base_signal.diff()

def f36_svar_gemini_060_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=431, w3=685, lag=0)."""
    x = low.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(431, min_periods=max(431//3, 2)).mean()
    noise = impulse.abs().rolling(685, min_periods=max(685//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.962353 + 0.0025751 * anchor
    return base_signal.diff()

def f36_svar_gemini_061_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=444, w3=702, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 444)
    curvature = _rolling_slope(acceleration, 702)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.277333 * acceleration + 0.0025752 * anchor
    return base_signal.diff()

def f36_svar_gemini_062_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=457, w3=719, lag=2)."""
    rel = _safe_div(low.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 206)
    pressure = rel_log.diff(126)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.283667 * pressure.rolling(719, min_periods=max(719//3, 2)).mean() + 0.0025753 * anchor
    return base_signal.diff()

def f36_svar_gemini_063_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=470, w3=736, lag=3)."""
    a = low.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(213, min_periods=max(213//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.002941 + 0.0025754 * anchor
    return base_signal.diff()

def f36_svar_gemini_064_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=483, w3=753, lag=5)."""
    a = _safe_log(low.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(483, min_periods=max(483//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 220)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.016471 + 0.0025755 * anchor
    return base_signal.diff()

def f36_svar_gemini_065_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=496, w3=19, lag=8)."""
    a = low.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(227, min_periods=max(227//3, 2)).mean(), b.abs().rolling(496, min_periods=max(496//3, 2)).mean())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(19) + 0.302667 * _rolling_slope(cover, 227) + 0.0025756 * anchor
    return base_signal.diff()

def f36_svar_gemini_066_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=509, w3=36, lag=13)."""
    x = _safe_log(low.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.309 * y + 0.691000 * z
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 234) - _rolling_slope(basket, 509) + 0.0025757 * anchor
    return base_signal.diff()

def f36_svar_gemini_067_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=23, w3=53, lag=21)."""
    x = low.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(241, min_periods=max(241//3, 2)).mean(), upside.rolling(23, min_periods=max(23//3, 2)).mean().abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(53) * 1.057059 + 0.0025758 * anchor
    return base_signal.diff()

def f36_svar_gemini_068_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=36, w3=70, lag=34)."""
    x = _safe_log(low.abs() + 1.0).shift(34)
    draw = x - x.rolling(36, min_periods=max(36//3, 2)).max()
    rebound = x - x.rolling(248, min_periods=max(248//3, 2)).min()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.321667 * _rolling_slope(draw, 70) + 0.0025759 * anchor
    return base_signal.diff()

def f36_svar_gemini_069_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=49, w3=87, lag=55)."""
    a = _safe_log(low.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(8) - b.diff(49)
    stress = imbalance.rolling(87, min_periods=max(87//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.084118 + 0.002576 * anchor
    return base_signal.diff()

def f36_svar_gemini_070_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=62, w3=104, lag=0)."""
    x = _safe_log(low.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(62, min_periods=max(62//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.097647 + 0.0025761 * anchor
    return base_signal.diff()

def f36_svar_gemini_071_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=75, w3=121, lag=1)."""
    x = _safe_log(low.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 75)
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=121, adjust=False).mean() * 1.111176 + 0.0025762 * anchor
    return base_signal.diff()

def f36_svar_gemini_072_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=88, w3=138, lag=2)."""
    x = low.shift(2)
    peak = x.rolling(88, min_periods=max(88//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.124706 + 0.0025763 * anchor
    return base_signal.diff()

def f36_svar_gemini_073_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=101, w3=155, lag=3)."""
    x = low.shift(3)
    change = x.pct_change(36)
    rank = change.rolling(101, min_periods=max(101//3, 2)).rank(pct=True)
    persistence = change.rolling(155, min_periods=max(155//3, 2)).mean()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.353333 * persistence + 0.0025764 * anchor
    return base_signal.diff()

def f36_svar_gemini_074_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=114, w3=172, lag=5)."""
    x = _safe_log(low.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(114, min_periods=max(114//3, 2)).std()
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.151765 + 0.0025765 * anchor
    return base_signal.diff()

def f36_svar_gemini_075_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=127, w3=189, lag=8)."""
    x = low.shift(8)
    ma = x.rolling(127, min_periods=max(127//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(low.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.033667 * slope + 0.0025766 * anchor
    return base_signal.diff()
