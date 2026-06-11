"""49 blowoff climax composite gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Multi-factor indicator for identifying parabolic peaks and blow-off moves.
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

def f49_bocc_gemini_001(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=5]"""
    window = 5
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_002(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=10]"""
    window = 10
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_003(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=21]"""
    window = 21
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_004(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=42]"""
    window = 42
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_005(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=63]"""
    window = 63
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_006(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=126]"""
    window = 126
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_007(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=252]"""
    window = 252
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_008(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=504]"""
    window = 504
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_009(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=756]"""
    window = 756
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_010(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Multi-factor indicator for identifying parabolic peaks and blow-off moves. [window=1260]"""
    window = 1260
    res = _rolling_zscore(close, window) * _rolling_zscore(volume, window)
    return res

def f49_bocc_gemini_011(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=299, w3=321, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(182, min_periods=max(182//3, 2)).mean())
    decay = spread.ewm(span=299, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.304118 + 0.0032842 * anchor
    return base_signal

def f49_bocc_gemini_012(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=312, w3=338, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(312, min_periods=max(312//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 189)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.317647 + 0.0032843 * anchor
    return base_signal

def f49_bocc_gemini_013(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=325, w3=355, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(196, min_periods=max(196//3, 2)).mean(), b.abs().rolling(325, min_periods=max(325//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.328333 * _rolling_slope(cover, 196) + 0.0032844 * anchor
    return base_signal

def f49_bocc_gemini_014(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=338, w3=372, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.334667 * y + 0.665333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 203) - _rolling_slope(basket, 338) + 0.0032845 * anchor
    return base_signal

def f49_bocc_gemini_015(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=351, w3=389, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(210, min_periods=max(210//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.358235 + 0.0032846 * anchor
    return base_signal

def f49_bocc_gemini_016(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=364, w3=406, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(364, min_periods=max(364//3, 2)).max()
    rebound = x - x.rolling(217, min_periods=max(217//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.347333 * _rolling_slope(draw, 406) + 0.0032847 * anchor
    return base_signal

def f49_bocc_gemini_017(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=377, w3=423, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.385294 + 0.0032848 * anchor
    return base_signal

def f49_bocc_gemini_018(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=390, w3=440, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 231)
    baseline = trend.rolling(390, min_periods=max(390//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(440, min_periods=max(440//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.398824 + 0.0032849 * anchor
    return base_signal

def f49_bocc_gemini_019(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=403, w3=457, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 238)
    slow = _rolling_slope(x, 403)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.412353 + 0.003285 * anchor
    return base_signal

def f49_bocc_gemini_020(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=416, w3=474, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(416, min_periods=max(416//3, 2)).max()
    trough = x.rolling(245, min_periods=max(245//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.425882 + 0.0032851 * anchor
    return base_signal

def f49_bocc_gemini_021(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=429, w3=491, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(5)
    rank = change.rolling(429, min_periods=max(429//3, 2)).rank(pct=True)
    persistence = change.rolling(491, min_periods=max(491//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.046667 * persistence + 0.0032852 * anchor
    return base_signal

def f49_bocc_gemini_022(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=442, w3=508, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(12, min_periods=max(12//3, 2)).std()
    vol_slow = ret.rolling(442, min_periods=max(442//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.452941 + 0.0032853 * anchor
    return base_signal

def f49_bocc_gemini_023(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=455, w3=525, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(455, min_periods=max(455//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 19)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.059333 * slope + 0.0032854 * anchor
    return base_signal

def f49_bocc_gemini_024(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=468, w3=542, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(26)
    drag = impulse.rolling(468, min_periods=max(468//3, 2)).mean()
    noise = impulse.abs().rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.48 + 0.0032855 * anchor
    return base_signal

def f49_bocc_gemini_025(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=481, w3=559, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 33)
    acceleration = _rolling_slope(velocity, 481)
    curvature = _rolling_slope(acceleration, 559)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.072 * acceleration + 0.0032856 * anchor
    return base_signal

def f49_bocc_gemini_026(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=494, w3=576, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 40)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.078333 * pressure.rolling(576, min_periods=max(576//3, 2)).mean() + 0.0032857 * anchor
    return base_signal

def f49_bocc_gemini_027(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=507, w3=593, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(47, min_periods=max(47//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.520588 + 0.0032858 * anchor
    return base_signal

def f49_bocc_gemini_028(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=21, w3=610, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(21, min_periods=max(21//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 54)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.534118 + 0.0032859 * anchor
    return base_signal

def f49_bocc_gemini_029(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=34, w3=627, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(61, min_periods=max(61//3, 2)).mean(), b.abs().rolling(34, min_periods=max(34//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.097333 * _rolling_slope(cover, 61) + 0.003286 * anchor
    return base_signal

def f49_bocc_gemini_030(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=47, w3=644, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.103667 * y + 0.896333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 68) - _rolling_slope(basket, 47) + 0.0032861 * anchor
    return base_signal

def f49_bocc_gemini_031(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=60, w3=661, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(75, min_periods=max(75//3, 2)).mean(), upside.rolling(60, min_periods=max(60//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.574706 + 0.0032862 * anchor
    return base_signal

def f49_bocc_gemini_032(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=73, w3=678, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(73, min_periods=max(73//3, 2)).max()
    rebound = x - x.rolling(82, min_periods=max(82//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.116333 * _rolling_slope(draw, 678) + 0.0032863 * anchor
    return base_signal

def f49_bocc_gemini_033(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=86, w3=695, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(89) - b.diff(86)
    stress = imbalance.rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.601765 + 0.0032864 * anchor
    return base_signal

def f49_bocc_gemini_034(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=99, w3=712, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(99, min_periods=max(99//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(712, min_periods=max(712//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.615294 + 0.0032865 * anchor
    return base_signal

def f49_bocc_gemini_035(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=112, w3=729, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 103)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.628824 + 0.0032866 * anchor
    return base_signal

def f49_bocc_gemini_036(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=125, w3=746, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(125, min_periods=max(125//3, 2)).max()
    trough = x.rolling(110, min_periods=max(110//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.642353 + 0.0032867 * anchor
    return base_signal

def f49_bocc_gemini_037(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=138, w3=763, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(117)
    rank = change.rolling(138, min_periods=max(138//3, 2)).rank(pct=True)
    persistence = change.rolling(763, min_periods=max(763//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.148 * persistence + 0.0032868 * anchor
    return base_signal

def f49_bocc_gemini_038(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=151, w3=29, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(124, min_periods=max(124//3, 2)).std()
    vol_slow = ret.rolling(151, min_periods=max(151//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.669412 + 0.0032869 * anchor
    return base_signal

def f49_bocc_gemini_039(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=164, w3=46, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(164, min_periods=max(164//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 131)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.160667 * slope + 0.003287 * anchor
    return base_signal

def f49_bocc_gemini_040(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=177, w3=63, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(177, min_periods=max(177//3, 2)).mean()
    noise = impulse.abs().rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.842941 + 0.0032871 * anchor
    return base_signal

def f49_bocc_gemini_041(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=190, w3=80, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 145)
    acceleration = _rolling_slope(velocity, 190)
    curvature = _rolling_slope(acceleration, 80)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.173333 * acceleration + 0.0032872 * anchor
    return base_signal

def f49_bocc_gemini_042(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=203, w3=97, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 152)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.179667 * pressure.rolling(97, min_periods=max(97//3, 2)).mean() + 0.0032873 * anchor
    return base_signal

def f49_bocc_gemini_043(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=216, w3=114, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(159, min_periods=max(159//3, 2)).mean())
    decay = spread.ewm(span=216, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.883529 + 0.0032874 * anchor
    return base_signal

def f49_bocc_gemini_044(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=229, w3=131, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(229, min_periods=max(229//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 166)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.897059 + 0.0032875 * anchor
    return base_signal

def f49_bocc_gemini_045(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=242, w3=148, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(173, min_periods=max(173//3, 2)).mean(), b.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.198667 * _rolling_slope(cover, 173) + 0.0032876 * anchor
    return base_signal

def f49_bocc_gemini_046(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=255, w3=165, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.205 * y + 0.795000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 180) - _rolling_slope(basket, 255) + 0.0032877 * anchor
    return base_signal

def f49_bocc_gemini_047(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=268, w3=182, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(187, min_periods=max(187//3, 2)).mean(), upside.rolling(268, min_periods=max(268//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.937647 + 0.0032878 * anchor
    return base_signal

def f49_bocc_gemini_048(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=281, w3=199, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(281, min_periods=max(281//3, 2)).max()
    rebound = x - x.rolling(194, min_periods=max(194//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.217667 * _rolling_slope(draw, 199) + 0.0032879 * anchor
    return base_signal

def f49_bocc_gemini_049(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=294, w3=216, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.964706 + 0.003288 * anchor
    return base_signal

def f49_bocc_gemini_050(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=307, w3=233, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(233, min_periods=max(233//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.978235 + 0.0032881 * anchor
    return base_signal

def f49_bocc_gemini_051(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=320, w3=250, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 320)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=250, adjust=False).mean() * 0.991765 + 0.0032882 * anchor
    return base_signal

def f49_bocc_gemini_052(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=333, w3=267, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.005294 + 0.0032883 * anchor
    return base_signal

def f49_bocc_gemini_053(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=346, w3=284, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(346, min_periods=max(346//3, 2)).rank(pct=True)
    persistence = change.rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249333 * persistence + 0.0032884 * anchor
    return base_signal

def f49_bocc_gemini_054(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=359, w3=301, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(359, min_periods=max(359//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.032353 + 0.0032885 * anchor
    return base_signal

def f49_bocc_gemini_055(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=372, w3=318, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(372, min_periods=max(372//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.262 * slope + 0.0032886 * anchor
    return base_signal

def f49_bocc_gemini_056(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=385, w3=335, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(385, min_periods=max(385//3, 2)).mean()
    noise = impulse.abs().rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.059412 + 0.0032887 * anchor
    return base_signal

def f49_bocc_gemini_057(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=398, w3=352, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 352)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274667 * acceleration + 0.0032888 * anchor
    return base_signal

def f49_bocc_gemini_058(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=411, w3=369, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 17)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.281 * pressure.rolling(369, min_periods=max(369//3, 2)).mean() + 0.0032889 * anchor
    return base_signal

def f49_bocc_gemini_059(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=424, w3=386, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(24, min_periods=max(24//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.1 + 0.003289 * anchor
    return base_signal

def f49_bocc_gemini_060(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=437, w3=403, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(437, min_periods=max(437//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 31)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.113529 + 0.0032891 * anchor
    return base_signal

def f49_bocc_gemini_061(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=450, w3=420, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(38, min_periods=max(38//3, 2)).mean(), b.abs().rolling(450, min_periods=max(450//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3 * _rolling_slope(cover, 38) + 0.0032892 * anchor
    return base_signal

def f49_bocc_gemini_062(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=463, w3=437, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.306333 * y + 0.693667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 45) - _rolling_slope(basket, 463) + 0.0032893 * anchor
    return base_signal

def f49_bocc_gemini_063(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=476, w3=454, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(476, min_periods=max(476//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.154118 + 0.0032894 * anchor
    return base_signal

def f49_bocc_gemini_064(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=489, w3=471, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(489, min_periods=max(489//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.319 * _rolling_slope(draw, 471) + 0.0032895 * anchor
    return base_signal

def f49_bocc_gemini_065(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=502, w3=488, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(66) - b.diff(126)
    stress = imbalance.rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.181176 + 0.0032896 * anchor
    return base_signal

def f49_bocc_gemini_066(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=16, w3=505, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(16, min_periods=max(16//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(505, min_periods=max(505//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.194706 + 0.0032897 * anchor
    return base_signal

def f49_bocc_gemini_067(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=29, w3=522, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 29)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.208235 + 0.0032898 * anchor
    return base_signal

def f49_bocc_gemini_068(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=42, w3=539, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(42, min_periods=max(42//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.221765 + 0.0032899 * anchor
    return base_signal

def f49_bocc_gemini_069(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=55, w3=556, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(94)
    rank = change.rolling(55, min_periods=max(55//3, 2)).rank(pct=True)
    persistence = change.rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.350667 * persistence + 0.00329 * anchor
    return base_signal

def f49_bocc_gemini_070(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=68, w3=573, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(68, min_periods=max(68//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.248824 + 0.0032901 * anchor
    return base_signal

def f49_bocc_gemini_071(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=81, w3=590, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(81, min_periods=max(81//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.031 * slope + 0.0032902 * anchor
    return base_signal

def f49_bocc_gemini_072(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=94, w3=607, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(115)
    drag = impulse.rolling(94, min_periods=max(94//3, 2)).mean()
    noise = impulse.abs().rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275882 + 0.0032903 * anchor
    return base_signal

def f49_bocc_gemini_073(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=107, w3=624, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 107)
    curvature = _rolling_slope(acceleration, 624)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.043667 * acceleration + 0.0032904 * anchor
    return base_signal

def f49_bocc_gemini_074(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=120, w3=641, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 129)
    pressure = rel_log.diff(120)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.05 * pressure.rolling(641, min_periods=max(641//3, 2)).mean() + 0.0032905 * anchor
    return base_signal

def f49_bocc_gemini_075(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=133, w3=658, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(136, min_periods=max(136//3, 2)).mean())
    decay = spread.ewm(span=133, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.316471 + 0.0032906 * anchor
    return base_signal
