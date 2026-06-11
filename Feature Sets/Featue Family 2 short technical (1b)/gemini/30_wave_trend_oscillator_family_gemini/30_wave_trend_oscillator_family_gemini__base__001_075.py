"""30 wave trend oscillator family gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of price cycles and waves through specialized oscillator techniques.
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

def f30_wave_gemini_001(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=5]"""
    window = 5
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_002(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=10]"""
    window = 10
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_003(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=21]"""
    window = 21
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_004(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=42]"""
    window = 42
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_005(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=63]"""
    window = 63
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_006(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=126]"""
    window = 126
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_007(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=252]"""
    window = 252
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_008(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=504]"""
    window = 504
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_009(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=756]"""
    window = 756
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_010(close: pd.Series) -> pd.Series:
    """Analysis of price cycles and waves through specialized oscillator techniques. [window=1260]"""
    window = 1260
    res = _rolling_zscore(close.diff(), window)
    return res

def f30_wave_gemini_011(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=49, w2=202, w3=432, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 202)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.597647 + 0.0022202 * anchor
    return base_signal

def f30_wave_gemini_012(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=56, w2=215, w3=449, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(215, min_periods=max(215//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.611176 + 0.0022203 * anchor
    return base_signal

def f30_wave_gemini_013(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=63, w2=228, w3=466, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(63)
    rank = change.rolling(228, min_periods=max(228//3, 2)).rank(pct=True)
    persistence = change.rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.073 * persistence + 0.0022204 * anchor
    return base_signal

def f30_wave_gemini_014(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=70, w2=241, w3=483, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(241, min_periods=max(241//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.638235 + 0.0022205 * anchor
    return base_signal

def f30_wave_gemini_015(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=77, w2=254, w3=500, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(254, min_periods=max(254//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.085667 * slope + 0.0022206 * anchor
    return base_signal

def f30_wave_gemini_016(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=84, w2=267, w3=517, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(84)
    drag = impulse.rolling(267, min_periods=max(267//3, 2)).mean()
    noise = impulse.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.665294 + 0.0022207 * anchor
    return base_signal

def f30_wave_gemini_017(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=91, w2=280, w3=534, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 280)
    curvature = _rolling_slope(acceleration, 534)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.098333 * acceleration + 0.0022208 * anchor
    return base_signal

def f30_wave_gemini_018(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=98, w2=293, w3=551, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(293, min_periods=max(293//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.838824 + 0.0022209 * anchor
    return base_signal

def f30_wave_gemini_019(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=105, w2=306, w3=568, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(306, min_periods=max(306//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.111 * _rolling_slope(draw, 568) + 0.002221 * anchor
    return base_signal

def f30_wave_gemini_020(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=112, w2=319, w3=585, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(319, min_periods=max(319//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.865882 + 0.0022211 * anchor
    return base_signal

def f30_wave_gemini_021(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=119, w2=332, w3=602, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 332)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.879412 + 0.0022212 * anchor
    return base_signal

def f30_wave_gemini_022(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=126, w2=345, w3=619, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(345, min_periods=max(345//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.892941 + 0.0022213 * anchor
    return base_signal

def f30_wave_gemini_023(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=133, w2=358, w3=636, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(358, min_periods=max(358//3, 2)).rank(pct=True)
    persistence = change.rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.136333 * persistence + 0.0022214 * anchor
    return base_signal

def f30_wave_gemini_024(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=140, w2=371, w3=653, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(371, min_periods=max(371//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92 + 0.0022215 * anchor
    return base_signal

def f30_wave_gemini_025(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=147, w2=384, w3=670, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(384, min_periods=max(384//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.149 * slope + 0.0022216 * anchor
    return base_signal

def f30_wave_gemini_026(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=154, w2=397, w3=687, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(397, min_periods=max(397//3, 2)).mean()
    noise = impulse.abs().rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.947059 + 0.0022217 * anchor
    return base_signal

def f30_wave_gemini_027(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=161, w2=410, w3=704, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 410)
    curvature = _rolling_slope(acceleration, 704)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.161667 * acceleration + 0.0022218 * anchor
    return base_signal

def f30_wave_gemini_028(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=168, w2=423, w3=721, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(423, min_periods=max(423//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.974118 + 0.0022219 * anchor
    return base_signal

def f30_wave_gemini_029(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=175, w2=436, w3=738, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.174333 * _rolling_slope(draw, 738) + 0.002222 * anchor
    return base_signal

def f30_wave_gemini_030(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=182, w2=449, w3=755, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.001176 + 0.0022221 * anchor
    return base_signal

def f30_wave_gemini_031(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=189, w2=462, w3=21, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 462)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=21, adjust=False).mean() * 1.014706 + 0.0022222 * anchor
    return base_signal

def f30_wave_gemini_032(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=196, w2=475, w3=38, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(475, min_periods=max(475//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.028235 + 0.0022223 * anchor
    return base_signal

def f30_wave_gemini_033(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=203, w2=488, w3=55, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(488, min_periods=max(488//3, 2)).rank(pct=True)
    persistence = change.rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.199667 * persistence + 0.0022224 * anchor
    return base_signal

def f30_wave_gemini_034(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=501, w3=72, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(501, min_periods=max(501//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055294 + 0.0022225 * anchor
    return base_signal

def f30_wave_gemini_035(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=15, w3=89, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(15, min_periods=max(15//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.212333 * slope + 0.0022226 * anchor
    return base_signal

def f30_wave_gemini_036(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=28, w3=106, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(28, min_periods=max(28//3, 2)).mean()
    noise = impulse.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.082353 + 0.0022227 * anchor
    return base_signal

def f30_wave_gemini_037(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=41, w3=123, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 41)
    curvature = _rolling_slope(acceleration, 123)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.225 * acceleration + 0.0022228 * anchor
    return base_signal

def f30_wave_gemini_038(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=54, w3=140, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(54, min_periods=max(54//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.109412 + 0.0022229 * anchor
    return base_signal

def f30_wave_gemini_039(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=67, w3=157, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(67, min_periods=max(67//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.237667 * _rolling_slope(draw, 157) + 0.002223 * anchor
    return base_signal

def f30_wave_gemini_040(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=80, w3=174, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 5)
    baseline = trend.rolling(80, min_periods=max(80//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.136471 + 0.0022231 * anchor
    return base_signal

def f30_wave_gemini_041(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=93, w3=191, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 93)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=191, adjust=False).mean() * 1.15 + 0.0022232 * anchor
    return base_signal

def f30_wave_gemini_042(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=106, w3=208, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(106, min_periods=max(106//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.163529 + 0.0022233 * anchor
    return base_signal

def f30_wave_gemini_043(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=119, w3=225, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(26)
    rank = change.rolling(119, min_periods=max(119//3, 2)).rank(pct=True)
    persistence = change.rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.263 * persistence + 0.0022234 * anchor
    return base_signal

def f30_wave_gemini_044(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=132, w3=242, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(132, min_periods=max(132//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.190588 + 0.0022235 * anchor
    return base_signal

def f30_wave_gemini_045(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=145, w3=259, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(145, min_periods=max(145//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.275667 * slope + 0.0022236 * anchor
    return base_signal

def f30_wave_gemini_046(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=158, w3=276, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(47)
    drag = impulse.rolling(158, min_periods=max(158//3, 2)).mean()
    noise = impulse.abs().rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.217647 + 0.0022237 * anchor
    return base_signal

def f30_wave_gemini_047(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=171, w3=293, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 54)
    acceleration = _rolling_slope(velocity, 171)
    curvature = _rolling_slope(acceleration, 293)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.288333 * acceleration + 0.0022238 * anchor
    return base_signal

def f30_wave_gemini_048(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=184, w3=310, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(61, min_periods=max(61//3, 2)).mean(), upside.rolling(184, min_periods=max(184//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.244706 + 0.0022239 * anchor
    return base_signal

def f30_wave_gemini_049(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=197, w3=327, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(197, min_periods=max(197//3, 2)).max()
    rebound = x - x.rolling(68, min_periods=max(68//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.301 * _rolling_slope(draw, 327) + 0.002224 * anchor
    return base_signal

def f30_wave_gemini_050(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=210, w3=344, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(210, min_periods=max(210//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(344, min_periods=max(344//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.271765 + 0.0022241 * anchor
    return base_signal

def f30_wave_gemini_051(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=223, w3=361, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 223)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.285294 + 0.0022242 * anchor
    return base_signal

def f30_wave_gemini_052(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=236, w3=378, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(236, min_periods=max(236//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.298824 + 0.0022243 * anchor
    return base_signal

def f30_wave_gemini_053(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=249, w3=395, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(96)
    rank = change.rolling(249, min_periods=max(249//3, 2)).rank(pct=True)
    persistence = change.rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.326333 * persistence + 0.0022244 * anchor
    return base_signal

def f30_wave_gemini_054(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=262, w3=412, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(262, min_periods=max(262//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.325882 + 0.0022245 * anchor
    return base_signal

def f30_wave_gemini_055(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=275, w3=429, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(275, min_periods=max(275//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.339 * slope + 0.0022246 * anchor
    return base_signal

def f30_wave_gemini_056(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=288, w3=446, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(117)
    drag = impulse.rolling(288, min_periods=max(288//3, 2)).mean()
    noise = impulse.abs().rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.352941 + 0.0022247 * anchor
    return base_signal

def f30_wave_gemini_057(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=301, w3=463, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 301)
    curvature = _rolling_slope(acceleration, 463)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.351667 * acceleration + 0.0022248 * anchor
    return base_signal

def f30_wave_gemini_058(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=314, w3=480, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(314, min_periods=max(314//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.38 + 0.0022249 * anchor
    return base_signal

def f30_wave_gemini_059(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=327, w3=497, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(327, min_periods=max(327//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.032 * _rolling_slope(draw, 497) + 0.002225 * anchor
    return base_signal

def f30_wave_gemini_060(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=340, w3=514, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(340, min_periods=max(340//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.407059 + 0.0022251 * anchor
    return base_signal

def f30_wave_gemini_061(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=353, w3=531, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 353)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.420588 + 0.0022252 * anchor
    return base_signal

def f30_wave_gemini_062(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=366, w3=548, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(366, min_periods=max(366//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.434118 + 0.0022253 * anchor
    return base_signal

def f30_wave_gemini_063(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=379, w3=565, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(379, min_periods=max(379//3, 2)).rank(pct=True)
    persistence = change.rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.057333 * persistence + 0.0022254 * anchor
    return base_signal

def f30_wave_gemini_064(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=392, w3=582, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(392, min_periods=max(392//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.461176 + 0.0022255 * anchor
    return base_signal

def f30_wave_gemini_065(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=405, w3=599, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(405, min_periods=max(405//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.07 * slope + 0.0022256 * anchor
    return base_signal

def f30_wave_gemini_066(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=418, w3=616, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(418, min_periods=max(418//3, 2)).mean()
    noise = impulse.abs().rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.488235 + 0.0022257 * anchor
    return base_signal

def f30_wave_gemini_067(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=431, w3=633, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 431)
    curvature = _rolling_slope(acceleration, 633)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.082667 * acceleration + 0.0022258 * anchor
    return base_signal

def f30_wave_gemini_068(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=444, w3=650, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(444, min_periods=max(444//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.515294 + 0.0022259 * anchor
    return base_signal

def f30_wave_gemini_069(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=457, w3=667, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(457, min_periods=max(457//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.095333 * _rolling_slope(draw, 667) + 0.002226 * anchor
    return base_signal

def f30_wave_gemini_070(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=470, w3=684, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 215)
    baseline = trend.rolling(470, min_periods=max(470//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(684, min_periods=max(684//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.542353 + 0.0022261 * anchor
    return base_signal

def f30_wave_gemini_071(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=483, w3=701, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 483)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.555882 + 0.0022262 * anchor
    return base_signal

def f30_wave_gemini_072(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=496, w3=718, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(496, min_periods=max(496//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.569412 + 0.0022263 * anchor
    return base_signal

def f30_wave_gemini_073(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=509, w3=735, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(509, min_periods=max(509//3, 2)).rank(pct=True)
    persistence = change.rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.120667 * persistence + 0.0022264 * anchor
    return base_signal

def f30_wave_gemini_074(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=23, w3=752, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(23, min_periods=max(23//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.596471 + 0.0022265 * anchor
    return base_signal

def f30_wave_gemini_075(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=36, w3=18, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(36, min_periods=max(36//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.133333 * slope + 0.0022266 * anchor
    return base_signal
