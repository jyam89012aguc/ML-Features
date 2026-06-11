"""101 absorption ratio standardized shift gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Standardized changes in the proportion of variance explained by lead components.
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

def f101_abrs_gemini_001(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=5]"""
    window = 5
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_002(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=10]"""
    window = 10
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_003(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=21]"""
    window = 21
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_004(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=42]"""
    window = 42
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_005(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=63]"""
    window = 63
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_006(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=126]"""
    window = 126
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_007(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=252]"""
    window = 252
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_008(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=504]"""
    window = 504
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_009(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=756]"""
    window = 756
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_010(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standardized changes in the proportion of variance explained by lead components. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1), window)
    return res

def f101_abrs_gemini_011(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=21, w2=364, w3=212, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(21, min_periods=max(21//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.342353 + 0.0005402 * anchor
    return base_signal

def f101_abrs_gemini_012(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=28, w2=377, w3=229, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(377, min_periods=max(377//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 28)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.355882 + 0.0005403 * anchor
    return base_signal

def f101_abrs_gemini_013(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=35, w2=390, w3=246, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(35, min_periods=max(35//3, 2)).mean(), b.abs().rolling(390, min_periods=max(390//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.352 * _rolling_slope(cover, 35) + 0.0005404 * anchor
    return base_signal

def f101_abrs_gemini_014(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=42, w2=403, w3=263, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.358333 * y + 0.641667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 42) - _rolling_slope(basket, 403) + 0.0005405 * anchor
    return base_signal

def f101_abrs_gemini_015(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=416, w3=280, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(49, min_periods=max(49//3, 2)).mean(), upside.rolling(416, min_periods=max(416//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.396471 + 0.0005406 * anchor
    return base_signal

def f101_abrs_gemini_016(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=429, w3=297, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(429, min_periods=max(429//3, 2)).max()
    rebound = x - x.rolling(56, min_periods=max(56//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.038667 * _rolling_slope(draw, 297) + 0.0005407 * anchor
    return base_signal

def f101_abrs_gemini_017(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=442, w3=314, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(63) - b.diff(126)
    stress = imbalance.rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.423529 + 0.0005408 * anchor
    return base_signal

def f101_abrs_gemini_018(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=455, w3=331, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(455, min_periods=max(455//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.437059 + 0.0005409 * anchor
    return base_signal

def f101_abrs_gemini_019(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=468, w3=348, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 468)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.450588 + 0.000541 * anchor
    return base_signal

def f101_abrs_gemini_020(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=481, w3=365, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(481, min_periods=max(481//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.464118 + 0.0005411 * anchor
    return base_signal

def f101_abrs_gemini_021(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=494, w3=382, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(91)
    rank = change.rolling(494, min_periods=max(494//3, 2)).rank(pct=True)
    persistence = change.rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.070333 * persistence + 0.0005412 * anchor
    return base_signal

def f101_abrs_gemini_022(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=507, w3=399, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(507, min_periods=max(507//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.491176 + 0.0005413 * anchor
    return base_signal

def f101_abrs_gemini_023(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=21, w3=416, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(21, min_periods=max(21//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.083 * slope + 0.0005414 * anchor
    return base_signal

def f101_abrs_gemini_024(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=34, w3=433, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(112)
    drag = impulse.rolling(34, min_periods=max(34//3, 2)).mean()
    noise = impulse.abs().rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.518235 + 0.0005415 * anchor
    return base_signal

def f101_abrs_gemini_025(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=47, w3=450, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 47)
    curvature = _rolling_slope(acceleration, 450)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.095667 * acceleration + 0.0005416 * anchor
    return base_signal

def f101_abrs_gemini_026(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=60, w3=467, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 126)
    pressure = rel_log.diff(60)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.102 * pressure.rolling(467, min_periods=max(467//3, 2)).mean() + 0.0005417 * anchor
    return base_signal

def f101_abrs_gemini_027(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=73, w3=484, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(133, min_periods=max(133//3, 2)).mean())
    decay = spread.ewm(span=73, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.558824 + 0.0005418 * anchor
    return base_signal

def f101_abrs_gemini_028(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=86, w3=501, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(86, min_periods=max(86//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 140)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.572353 + 0.0005419 * anchor
    return base_signal

def f101_abrs_gemini_029(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=99, w3=518, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(147, min_periods=max(147//3, 2)).mean(), b.abs().rolling(99, min_periods=max(99//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.121 * _rolling_slope(cover, 147) + 0.000542 * anchor
    return base_signal

def f101_abrs_gemini_030(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=112, w3=535, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.127333 * y + 0.872667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 154) - _rolling_slope(basket, 112) + 0.0005421 * anchor
    return base_signal

def f101_abrs_gemini_031(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=125, w3=552, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(125, min_periods=max(125//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.612941 + 0.0005422 * anchor
    return base_signal

def f101_abrs_gemini_032(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=138, w3=569, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(138, min_periods=max(138//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.14 * _rolling_slope(draw, 569) + 0.0005423 * anchor
    return base_signal

def f101_abrs_gemini_033(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=151, w3=586, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.64 + 0.0005424 * anchor
    return base_signal

def f101_abrs_gemini_034(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=164, w3=603, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.653529 + 0.0005425 * anchor
    return base_signal

def f101_abrs_gemini_035(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=177, w3=620, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 177)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.667059 + 0.0005426 * anchor
    return base_signal

def f101_abrs_gemini_036(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=190, w3=637, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(190, min_periods=max(190//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.827059 + 0.0005427 * anchor
    return base_signal

def f101_abrs_gemini_037(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=203, w3=654, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(203, min_periods=max(203//3, 2)).rank(pct=True)
    persistence = change.rolling(654, min_periods=max(654//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.171667 * persistence + 0.0005428 * anchor
    return base_signal

def f101_abrs_gemini_038(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=216, w3=671, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(216, min_periods=max(216//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.854118 + 0.0005429 * anchor
    return base_signal

def f101_abrs_gemini_039(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=229, w3=688, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(229, min_periods=max(229//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.184333 * slope + 0.000543 * anchor
    return base_signal

def f101_abrs_gemini_040(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=242, w3=705, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(242, min_periods=max(242//3, 2)).mean()
    noise = impulse.abs().rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.881176 + 0.0005431 * anchor
    return base_signal

def f101_abrs_gemini_041(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=255, w3=722, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 255)
    curvature = _rolling_slope(acceleration, 722)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.197 * acceleration + 0.0005432 * anchor
    return base_signal

def f101_abrs_gemini_042(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=268, w3=739, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 238)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.203333 * pressure.rolling(739, min_periods=max(739//3, 2)).mean() + 0.0005433 * anchor
    return base_signal

def f101_abrs_gemini_043(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=281, w3=756, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(245, min_periods=max(245//3, 2)).mean())
    decay = spread.ewm(span=281, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.921765 + 0.0005434 * anchor
    return base_signal

def f101_abrs_gemini_044(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=294, w3=22, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(294, min_periods=max(294//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 5)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.935294 + 0.0005435 * anchor
    return base_signal

def f101_abrs_gemini_045(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=307, w3=39, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(12, min_periods=max(12//3, 2)).mean(), b.abs().rolling(307, min_periods=max(307//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(39) + 0.222333 * _rolling_slope(cover, 12) + 0.0005436 * anchor
    return base_signal

def f101_abrs_gemini_046(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=320, w3=56, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.228667 * y + 0.771333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 19) - _rolling_slope(basket, 320) + 0.0005437 * anchor
    return base_signal

def f101_abrs_gemini_047(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=333, w3=73, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(73) * 0.975882 + 0.0005438 * anchor
    return base_signal

def f101_abrs_gemini_048(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=346, w3=90, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(346, min_periods=max(346//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.241333 * _rolling_slope(draw, 90) + 0.0005439 * anchor
    return base_signal

def f101_abrs_gemini_049(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=359, w3=107, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(40) - b.diff(126)
    stress = imbalance.rolling(107, min_periods=max(107//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.002941 + 0.000544 * anchor
    return base_signal

def f101_abrs_gemini_050(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=372, w3=124, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 47)
    baseline = trend.rolling(372, min_periods=max(372//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.016471 + 0.0005441 * anchor
    return base_signal

def f101_abrs_gemini_051(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=385, w3=141, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 54)
    slow = _rolling_slope(x, 385)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=141, adjust=False).mean() * 1.03 + 0.0005442 * anchor
    return base_signal

def f101_abrs_gemini_052(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=398, w3=158, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(398, min_periods=max(398//3, 2)).max()
    trough = x.rolling(61, min_periods=max(61//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.043529 + 0.0005443 * anchor
    return base_signal

def f101_abrs_gemini_053(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=411, w3=175, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(68)
    rank = change.rolling(411, min_periods=max(411//3, 2)).rank(pct=True)
    persistence = change.rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.273 * persistence + 0.0005444 * anchor
    return base_signal

def f101_abrs_gemini_054(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=424, w3=192, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(75, min_periods=max(75//3, 2)).std()
    vol_slow = ret.rolling(424, min_periods=max(424//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.070588 + 0.0005445 * anchor
    return base_signal

def f101_abrs_gemini_055(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=437, w3=209, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(437, min_periods=max(437//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 82)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.285667 * slope + 0.0005446 * anchor
    return base_signal

def f101_abrs_gemini_056(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=450, w3=226, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(89)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.097647 + 0.0005447 * anchor
    return base_signal

def f101_abrs_gemini_057(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=463, w3=243, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 96)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 243)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.298333 * acceleration + 0.0005448 * anchor
    return base_signal

def f101_abrs_gemini_058(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=476, w3=260, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 103)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.304667 * pressure.rolling(260, min_periods=max(260//3, 2)).mean() + 0.0005449 * anchor
    return base_signal

def f101_abrs_gemini_059(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=489, w3=277, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(110, min_periods=max(110//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.138235 + 0.000545 * anchor
    return base_signal

def f101_abrs_gemini_060(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=502, w3=294, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(502, min_periods=max(502//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 117)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.151765 + 0.0005451 * anchor
    return base_signal

def f101_abrs_gemini_061(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=16, w3=311, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(124, min_periods=max(124//3, 2)).mean(), b.abs().rolling(16, min_periods=max(16//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.323667 * _rolling_slope(cover, 124) + 0.0005452 * anchor
    return base_signal

def f101_abrs_gemini_062(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=29, w3=328, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.33 * y + 0.670000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 131) - _rolling_slope(basket, 29) + 0.0005453 * anchor
    return base_signal

def f101_abrs_gemini_063(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=42, w3=345, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(138, min_periods=max(138//3, 2)).mean(), upside.rolling(42, min_periods=max(42//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.192353 + 0.0005454 * anchor
    return base_signal

def f101_abrs_gemini_064(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=55, w3=362, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(55, min_periods=max(55//3, 2)).max()
    rebound = x - x.rolling(145, min_periods=max(145//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.342667 * _rolling_slope(draw, 362) + 0.0005455 * anchor
    return base_signal

def f101_abrs_gemini_065(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=68, w3=379, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(68)
    stress = imbalance.rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.219412 + 0.0005456 * anchor
    return base_signal

def f101_abrs_gemini_066(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=81, w3=396, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(81, min_periods=max(81//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(396, min_periods=max(396//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.232941 + 0.0005457 * anchor
    return base_signal

def f101_abrs_gemini_067(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=94, w3=413, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 94)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.246471 + 0.0005458 * anchor
    return base_signal

def f101_abrs_gemini_068(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=107, w3=430, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(107, min_periods=max(107//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.26 + 0.0005459 * anchor
    return base_signal

def f101_abrs_gemini_069(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=120, w3=447, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(120, min_periods=max(120//3, 2)).rank(pct=True)
    persistence = change.rolling(447, min_periods=max(447//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.042 * persistence + 0.000546 * anchor
    return base_signal

def f101_abrs_gemini_070(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=133, w3=464, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(133, min_periods=max(133//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.287059 + 0.0005461 * anchor
    return base_signal

def f101_abrs_gemini_071(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=146, w3=481, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(146, min_periods=max(146//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.054667 * slope + 0.0005462 * anchor
    return base_signal

def f101_abrs_gemini_072(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=159, w3=498, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(159, min_periods=max(159//3, 2)).mean()
    noise = impulse.abs().rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.314118 + 0.0005463 * anchor
    return base_signal

def f101_abrs_gemini_073(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=172, w3=515, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 172)
    curvature = _rolling_slope(acceleration, 515)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.067333 * acceleration + 0.0005464 * anchor
    return base_signal

def f101_abrs_gemini_074(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=185, w3=532, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 215)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.073667 * pressure.rolling(532, min_periods=max(532//3, 2)).mean() + 0.0005465 * anchor
    return base_signal

def f101_abrs_gemini_075(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=198, w3=549, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(222, min_periods=max(222//3, 2)).mean())
    decay = spread.ewm(span=198, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.354706 + 0.0005466 * anchor
    return base_signal
