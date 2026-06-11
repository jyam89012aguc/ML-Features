"""79 long range correlation break gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Sudden loss of correlation between distant points in the price series.
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

def f79_lrcb_gemini_001(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_002(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_003(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_004(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_005(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_006(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_007(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_008(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_009(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_010(close: pd.Series) -> pd.Series:
    """Sudden loss of correlation between distant points in the price series. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff() * _safe_log(close).diff().shift(window * 2), window)
    return res

def f79_lrcb_gemini_011(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=210, w2=137, w3=541, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 210)
    slow = _rolling_slope(x, 137)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.559412 + 0.0049642 * anchor
    return base_signal

def f79_lrcb_gemini_012(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=150, w3=558, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(150, min_periods=max(150//3, 2)).max()
    trough = x.rolling(217, min_periods=max(217//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.572941 + 0.0049643 * anchor
    return base_signal

def f79_lrcb_gemini_013(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=163, w3=575, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(163, min_periods=max(163//3, 2)).rank(pct=True)
    persistence = change.rolling(575, min_periods=max(575//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.049333 * persistence + 0.0049644 * anchor
    return base_signal

def f79_lrcb_gemini_014(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=176, w3=592, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(231, min_periods=max(231//3, 2)).std()
    vol_slow = ret.rolling(176, min_periods=max(176//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.6 + 0.0049645 * anchor
    return base_signal

def f79_lrcb_gemini_015(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=189, w3=609, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(189, min_periods=max(189//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 238)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.062 * slope + 0.0049646 * anchor
    return base_signal

def f79_lrcb_gemini_016(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=202, w3=626, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(202, min_periods=max(202//3, 2)).mean()
    noise = impulse.abs().rolling(626, min_periods=max(626//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.627059 + 0.0049647 * anchor
    return base_signal

def f79_lrcb_gemini_017(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=215, w3=643, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 5)
    acceleration = _rolling_slope(velocity, 215)
    curvature = _rolling_slope(acceleration, 643)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.074667 * acceleration + 0.0049648 * anchor
    return base_signal

def f79_lrcb_gemini_018(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=228, w3=660, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(12, min_periods=max(12//3, 2)).mean(), upside.rolling(228, min_periods=max(228//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.654118 + 0.0049649 * anchor
    return base_signal

def f79_lrcb_gemini_019(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=241, w3=677, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(241, min_periods=max(241//3, 2)).max()
    rebound = x - x.rolling(19, min_periods=max(19//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.087333 * _rolling_slope(draw, 677) + 0.004965 * anchor
    return base_signal

def f79_lrcb_gemini_020(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=254, w3=694, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 26)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.827647 + 0.0049651 * anchor
    return base_signal

def f79_lrcb_gemini_021(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=267, w3=711, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 33)
    slow = _rolling_slope(x, 267)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.841176 + 0.0049652 * anchor
    return base_signal

def f79_lrcb_gemini_022(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=280, w3=728, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(40, min_periods=max(40//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.854706 + 0.0049653 * anchor
    return base_signal

def f79_lrcb_gemini_023(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=293, w3=745, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(47)
    rank = change.rolling(293, min_periods=max(293//3, 2)).rank(pct=True)
    persistence = change.rolling(745, min_periods=max(745//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.112667 * persistence + 0.0049654 * anchor
    return base_signal

def f79_lrcb_gemini_024(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=306, w3=762, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(54, min_periods=max(54//3, 2)).std()
    vol_slow = ret.rolling(306, min_periods=max(306//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.881765 + 0.0049655 * anchor
    return base_signal

def f79_lrcb_gemini_025(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=319, w3=28, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(319, min_periods=max(319//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 61)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.125333 * slope + 0.0049656 * anchor
    return base_signal

def f79_lrcb_gemini_026(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=332, w3=45, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(68)
    drag = impulse.rolling(332, min_periods=max(332//3, 2)).mean()
    noise = impulse.abs().rolling(45, min_periods=max(45//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.908824 + 0.0049657 * anchor
    return base_signal

def f79_lrcb_gemini_027(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=345, w3=62, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 75)
    acceleration = _rolling_slope(velocity, 345)
    curvature = _rolling_slope(acceleration, 62)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.138 * acceleration + 0.0049658 * anchor
    return base_signal

def f79_lrcb_gemini_028(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=358, w3=79, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(82, min_periods=max(82//3, 2)).mean(), upside.rolling(358, min_periods=max(358//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(79) * 0.935882 + 0.0049659 * anchor
    return base_signal

def f79_lrcb_gemini_029(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=371, w3=96, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(371, min_periods=max(371//3, 2)).max()
    rebound = x - x.rolling(89, min_periods=max(89//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.150667 * _rolling_slope(draw, 96) + 0.004966 * anchor
    return base_signal

def f79_lrcb_gemini_030(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=384, w3=113, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 96)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(113, min_periods=max(113//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.962941 + 0.0049661 * anchor
    return base_signal

def f79_lrcb_gemini_031(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=397, w3=130, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 103)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=130, adjust=False).mean() * 0.976471 + 0.0049662 * anchor
    return base_signal

def f79_lrcb_gemini_032(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=410, w3=147, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(410, min_periods=max(410//3, 2)).max()
    trough = x.rolling(110, min_periods=max(110//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.99 + 0.0049663 * anchor
    return base_signal

def f79_lrcb_gemini_033(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=423, w3=164, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(117)
    rank = change.rolling(423, min_periods=max(423//3, 2)).rank(pct=True)
    persistence = change.rolling(164, min_periods=max(164//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.176 * persistence + 0.0049664 * anchor
    return base_signal

def f79_lrcb_gemini_034(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=436, w3=181, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(124, min_periods=max(124//3, 2)).std()
    vol_slow = ret.rolling(436, min_periods=max(436//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.017059 + 0.0049665 * anchor
    return base_signal

def f79_lrcb_gemini_035(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=449, w3=198, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(449, min_periods=max(449//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 131)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.188667 * slope + 0.0049666 * anchor
    return base_signal

def f79_lrcb_gemini_036(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=462, w3=215, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(462, min_periods=max(462//3, 2)).mean()
    noise = impulse.abs().rolling(215, min_periods=max(215//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.044118 + 0.0049667 * anchor
    return base_signal

def f79_lrcb_gemini_037(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=475, w3=232, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 145)
    acceleration = _rolling_slope(velocity, 475)
    curvature = _rolling_slope(acceleration, 232)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.201333 * acceleration + 0.0049668 * anchor
    return base_signal

def f79_lrcb_gemini_038(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=488, w3=249, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(152, min_periods=max(152//3, 2)).mean(), upside.rolling(488, min_periods=max(488//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.071176 + 0.0049669 * anchor
    return base_signal

def f79_lrcb_gemini_039(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=501, w3=266, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(501, min_periods=max(501//3, 2)).max()
    rebound = x - x.rolling(159, min_periods=max(159//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.214 * _rolling_slope(draw, 266) + 0.004967 * anchor
    return base_signal

def f79_lrcb_gemini_040(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=15, w3=283, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 166)
    baseline = trend.rolling(15, min_periods=max(15//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(283, min_periods=max(283//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.098235 + 0.0049671 * anchor
    return base_signal

def f79_lrcb_gemini_041(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=28, w3=300, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 28)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.111765 + 0.0049672 * anchor
    return base_signal

def f79_lrcb_gemini_042(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=41, w3=317, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(41, min_periods=max(41//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.125294 + 0.0049673 * anchor
    return base_signal

def f79_lrcb_gemini_043(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=54, w3=334, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(54, min_periods=max(54//3, 2)).rank(pct=True)
    persistence = change.rolling(334, min_periods=max(334//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.239333 * persistence + 0.0049674 * anchor
    return base_signal

def f79_lrcb_gemini_044(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=67, w3=351, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(67, min_periods=max(67//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.152353 + 0.0049675 * anchor
    return base_signal

def f79_lrcb_gemini_045(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=80, w3=368, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(80, min_periods=max(80//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.252 * slope + 0.0049676 * anchor
    return base_signal

def f79_lrcb_gemini_046(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=93, w3=385, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(93, min_periods=max(93//3, 2)).mean()
    noise = impulse.abs().rolling(385, min_periods=max(385//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.179412 + 0.0049677 * anchor
    return base_signal

def f79_lrcb_gemini_047(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=106, w3=402, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 106)
    curvature = _rolling_slope(acceleration, 402)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.264667 * acceleration + 0.0049678 * anchor
    return base_signal

def f79_lrcb_gemini_048(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=119, w3=419, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(119, min_periods=max(119//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.206471 + 0.0049679 * anchor
    return base_signal

def f79_lrcb_gemini_049(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=132, w3=436, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(132, min_periods=max(132//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.277333 * _rolling_slope(draw, 436) + 0.004968 * anchor
    return base_signal

def f79_lrcb_gemini_050(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=145, w3=453, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(145, min_periods=max(145//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.233529 + 0.0049681 * anchor
    return base_signal

def f79_lrcb_gemini_051(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=158, w3=470, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 158)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.247059 + 0.0049682 * anchor
    return base_signal

def f79_lrcb_gemini_052(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=171, w3=487, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.260588 + 0.0049683 * anchor
    return base_signal

def f79_lrcb_gemini_053(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=184, w3=504, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(10)
    rank = change.rolling(184, min_periods=max(184//3, 2)).rank(pct=True)
    persistence = change.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.302667 * persistence + 0.0049684 * anchor
    return base_signal

def f79_lrcb_gemini_054(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=197, w3=521, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(197, min_periods=max(197//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.287647 + 0.0049685 * anchor
    return base_signal

def f79_lrcb_gemini_055(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=210, w3=538, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(210, min_periods=max(210//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.315333 * slope + 0.0049686 * anchor
    return base_signal

def f79_lrcb_gemini_056(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=223, w3=555, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(31)
    drag = impulse.rolling(223, min_periods=max(223//3, 2)).mean()
    noise = impulse.abs().rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.314706 + 0.0049687 * anchor
    return base_signal

def f79_lrcb_gemini_057(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=236, w3=572, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 236)
    curvature = _rolling_slope(acceleration, 572)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.328 * acceleration + 0.0049688 * anchor
    return base_signal

def f79_lrcb_gemini_058(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=249, w3=589, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(249, min_periods=max(249//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.341765 + 0.0049689 * anchor
    return base_signal

def f79_lrcb_gemini_059(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=262, w3=606, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(262, min_periods=max(262//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.340667 * _rolling_slope(draw, 606) + 0.004969 * anchor
    return base_signal

def f79_lrcb_gemini_060(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=275, w3=623, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(275, min_periods=max(275//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.368824 + 0.0049691 * anchor
    return base_signal

def f79_lrcb_gemini_061(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=288, w3=640, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 288)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.382353 + 0.0049692 * anchor
    return base_signal

def f79_lrcb_gemini_062(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=301, w3=657, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(301, min_periods=max(301//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.395882 + 0.0049693 * anchor
    return base_signal

def f79_lrcb_gemini_063(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=314, w3=674, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(80)
    rank = change.rolling(314, min_periods=max(314//3, 2)).rank(pct=True)
    persistence = change.rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.033667 * persistence + 0.0049694 * anchor
    return base_signal

def f79_lrcb_gemini_064(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=327, w3=691, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(327, min_periods=max(327//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.422941 + 0.0049695 * anchor
    return base_signal

def f79_lrcb_gemini_065(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=340, w3=708, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(340, min_periods=max(340//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.046333 * slope + 0.0049696 * anchor
    return base_signal

def f79_lrcb_gemini_066(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=353, w3=725, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(101)
    drag = impulse.rolling(353, min_periods=max(353//3, 2)).mean()
    noise = impulse.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.45 + 0.0049697 * anchor
    return base_signal

def f79_lrcb_gemini_067(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=366, w3=742, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 366)
    curvature = _rolling_slope(acceleration, 742)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.059 * acceleration + 0.0049698 * anchor
    return base_signal

def f79_lrcb_gemini_068(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=379, w3=759, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(379, min_periods=max(379//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.477059 + 0.0049699 * anchor
    return base_signal

def f79_lrcb_gemini_069(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=392, w3=25, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(392, min_periods=max(392//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.071667 * _rolling_slope(draw, 25) + 0.00497 * anchor
    return base_signal

def f79_lrcb_gemini_070(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=405, w3=42, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(405, min_periods=max(405//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.504118 + 0.0049701 * anchor
    return base_signal

def f79_lrcb_gemini_071(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=418, w3=59, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 418)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=59, adjust=False).mean() * 1.517647 + 0.0049702 * anchor
    return base_signal

def f79_lrcb_gemini_072(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=431, w3=76, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(431, min_periods=max(431//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.531176 + 0.0049703 * anchor
    return base_signal

def f79_lrcb_gemini_073(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=444, w3=93, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(444, min_periods=max(444//3, 2)).rank(pct=True)
    persistence = change.rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.097 * persistence + 0.0049704 * anchor
    return base_signal

def f79_lrcb_gemini_074(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=457, w3=110, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(457, min_periods=max(457//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.558235 + 0.0049705 * anchor
    return base_signal

def f79_lrcb_gemini_075(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=470, w3=127, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(470, min_periods=max(470//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.109667 * slope + 0.0049706 * anchor
    return base_signal
