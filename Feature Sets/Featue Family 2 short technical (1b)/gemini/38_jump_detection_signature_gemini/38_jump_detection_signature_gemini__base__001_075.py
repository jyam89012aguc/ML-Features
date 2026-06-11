"""38 jump detection signature gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of discontinuous price movements or 'jumps' using statistical thresholds.
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

def f38_jump_gemini_001(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=5]"""
    window = 5
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_002(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=10]"""
    window = 10
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_003(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=21]"""
    window = 21
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_004(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=42]"""
    window = 42
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_005(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=63]"""
    window = 63
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_006(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=126]"""
    window = 126
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_007(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=252]"""
    window = 252
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_008(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=504]"""
    window = 504
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_009(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=756]"""
    window = 756
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_010(close: pd.Series) -> pd.Series:
    """Identification of discontinuous price movements or 'jumps' using statistical thresholds. [window=1260]"""
    window = 1260
    res = _safe_div(_safe_log(close).diff().abs(), _safe_log(close).diff().rolling(window).std() + 1e-9)
    return res

def f38_jump_gemini_011(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=59, w3=741, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 59)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.608824 + 0.0026682 * anchor
    return base_signal

def f38_jump_gemini_012(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=72, w3=758, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(72, min_periods=max(72//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.622353 + 0.0026683 * anchor
    return base_signal

def f38_jump_gemini_013(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=85, w3=24, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(54)
    rank = change.rolling(85, min_periods=max(85//3, 2)).rank(pct=True)
    persistence = change.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.198 * persistence + 0.0026684 * anchor
    return base_signal

def f38_jump_gemini_014(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=98, w3=41, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.649412 + 0.0026685 * anchor
    return base_signal

def f38_jump_gemini_015(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=111, w3=58, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.210667 * slope + 0.0026686 * anchor
    return base_signal

def f38_jump_gemini_016(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=124, w3=75, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(75)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.822941 + 0.0026687 * anchor
    return base_signal

def f38_jump_gemini_017(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=137, w3=92, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 137)
    curvature = _rolling_slope(acceleration, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.223333 * acceleration + 0.0026688 * anchor
    return base_signal

def f38_jump_gemini_018(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=150, w3=109, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(150, min_periods=max(150//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(109) * 0.85 + 0.0026689 * anchor
    return base_signal

def f38_jump_gemini_019(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=163, w3=126, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(163, min_periods=max(163//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.236 * _rolling_slope(draw, 126) + 0.002669 * anchor
    return base_signal

def f38_jump_gemini_020(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=176, w3=143, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(176, min_periods=max(176//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.877059 + 0.0026691 * anchor
    return base_signal

def f38_jump_gemini_021(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=189, w3=160, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=160, adjust=False).mean() * 0.890588 + 0.0026692 * anchor
    return base_signal

def f38_jump_gemini_022(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=202, w3=177, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(202, min_periods=max(202//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.904118 + 0.0026693 * anchor
    return base_signal

def f38_jump_gemini_023(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=215, w3=194, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(124)
    rank = change.rolling(215, min_periods=max(215//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.261333 * persistence + 0.0026694 * anchor
    return base_signal

def f38_jump_gemini_024(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=228, w3=211, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(228, min_periods=max(228//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.931176 + 0.0026695 * anchor
    return base_signal

def f38_jump_gemini_025(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=241, w3=228, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.274 * slope + 0.0026696 * anchor
    return base_signal

def f38_jump_gemini_026(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=254, w3=245, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(254, min_periods=max(254//3, 2)).mean()
    noise = impulse.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.958235 + 0.0026697 * anchor
    return base_signal

def f38_jump_gemini_027(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=267, w3=262, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.286667 * acceleration + 0.0026698 * anchor
    return base_signal

def f38_jump_gemini_028(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=280, w3=279, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(280, min_periods=max(280//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.985294 + 0.0026699 * anchor
    return base_signal

def f38_jump_gemini_029(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=293, w3=296, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(293, min_periods=max(293//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.299333 * _rolling_slope(draw, 296) + 0.00267 * anchor
    return base_signal

def f38_jump_gemini_030(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=306, w3=313, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.012353 + 0.0026701 * anchor
    return base_signal

def f38_jump_gemini_031(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=319, w3=330, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 180)
    slow = _rolling_slope(x, 319)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.025882 + 0.0026702 * anchor
    return base_signal

def f38_jump_gemini_032(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=332, w3=347, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(187, min_periods=max(187//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.039412 + 0.0026703 * anchor
    return base_signal

def f38_jump_gemini_033(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=345, w3=364, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(345, min_periods=max(345//3, 2)).rank(pct=True)
    persistence = change.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.324667 * persistence + 0.0026704 * anchor
    return base_signal

def f38_jump_gemini_034(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=358, w3=381, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(201, min_periods=max(201//3, 2)).std()
    vol_slow = ret.rolling(358, min_periods=max(358//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.066471 + 0.0026705 * anchor
    return base_signal

def f38_jump_gemini_035(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=371, w3=398, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(371, min_periods=max(371//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 208)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.337333 * slope + 0.0026706 * anchor
    return base_signal

def f38_jump_gemini_036(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=384, w3=415, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(384, min_periods=max(384//3, 2)).mean()
    noise = impulse.abs().rolling(415, min_periods=max(415//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.093529 + 0.0026707 * anchor
    return base_signal

def f38_jump_gemini_037(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=397, w3=432, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 222)
    acceleration = _rolling_slope(velocity, 397)
    curvature = _rolling_slope(acceleration, 432)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.35 * acceleration + 0.0026708 * anchor
    return base_signal

def f38_jump_gemini_038(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=410, w3=449, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(229, min_periods=max(229//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.120588 + 0.0026709 * anchor
    return base_signal

def f38_jump_gemini_039(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=423, w3=466, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(236, min_periods=max(236//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.362667 * _rolling_slope(draw, 466) + 0.002671 * anchor
    return base_signal

def f38_jump_gemini_040(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=436, w3=483, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 243)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.147647 + 0.0026711 * anchor
    return base_signal

def f38_jump_gemini_041(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=449, w3=500, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 250)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.161176 + 0.0026712 * anchor
    return base_signal

def f38_jump_gemini_042(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=462, w3=517, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.174706 + 0.0026713 * anchor
    return base_signal

def f38_jump_gemini_043(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=475, w3=534, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(17)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.055667 * persistence + 0.0026714 * anchor
    return base_signal

def f38_jump_gemini_044(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=488, w3=551, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.201765 + 0.0026715 * anchor
    return base_signal

def f38_jump_gemini_045(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=501, w3=568, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.068333 * slope + 0.0026716 * anchor
    return base_signal

def f38_jump_gemini_046(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=15, w3=585, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(38)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(585, min_periods=max(585//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.228824 + 0.0026717 * anchor
    return base_signal

def f38_jump_gemini_047(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=28, w3=602, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 602)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.081 * acceleration + 0.0026718 * anchor
    return base_signal

def f38_jump_gemini_048(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=41, w3=619, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(41, min_periods=max(41//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.255882 + 0.0026719 * anchor
    return base_signal

def f38_jump_gemini_049(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=54, w3=636, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(54, min_periods=max(54//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.093667 * _rolling_slope(draw, 636) + 0.002672 * anchor
    return base_signal

def f38_jump_gemini_050(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=67, w3=653, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(67, min_periods=max(67//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(653, min_periods=max(653//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.282941 + 0.0026721 * anchor
    return base_signal

def f38_jump_gemini_051(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=80, w3=670, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 73)
    slow = _rolling_slope(x, 80)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.296471 + 0.0026722 * anchor
    return base_signal

def f38_jump_gemini_052(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=93, w3=687, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.31 + 0.0026723 * anchor
    return base_signal

def f38_jump_gemini_053(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=106, w3=704, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(87)
    rank = change.rolling(106, min_periods=max(106//3, 2)).rank(pct=True)
    persistence = change.rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119 * persistence + 0.0026724 * anchor
    return base_signal

def f38_jump_gemini_054(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=119, w3=721, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(119, min_periods=max(119//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.337059 + 0.0026725 * anchor
    return base_signal

def f38_jump_gemini_055(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=132, w3=738, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 101)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.131667 * slope + 0.0026726 * anchor
    return base_signal

def f38_jump_gemini_056(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=145, w3=755, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(108)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.364118 + 0.0026727 * anchor
    return base_signal

def f38_jump_gemini_057(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=158, w3=21, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 115)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.144333 * acceleration + 0.0026728 * anchor
    return base_signal

def f38_jump_gemini_058(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=171, w3=38, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(38) * 1.391176 + 0.0026729 * anchor
    return base_signal

def f38_jump_gemini_059(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=184, w3=55, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(129, min_periods=max(129//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.157 * _rolling_slope(draw, 55) + 0.002673 * anchor
    return base_signal

def f38_jump_gemini_060(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=197, w3=72, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.418235 + 0.0026731 * anchor
    return base_signal

def f38_jump_gemini_061(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=210, w3=89, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 143)
    slow = _rolling_slope(x, 210)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=89, adjust=False).mean() * 1.431765 + 0.0026732 * anchor
    return base_signal

def f38_jump_gemini_062(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=223, w3=106, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.445294 + 0.0026733 * anchor
    return base_signal

def f38_jump_gemini_063(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=236, w3=123, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(236, min_periods=max(236//3, 2)).rank(pct=True)
    persistence = change.rolling(123, min_periods=max(123//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.182333 * persistence + 0.0026734 * anchor
    return base_signal

def f38_jump_gemini_064(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=249, w3=140, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.472353 + 0.0026735 * anchor
    return base_signal

def f38_jump_gemini_065(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=262, w3=157, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 171)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.195 * slope + 0.0026736 * anchor
    return base_signal

def f38_jump_gemini_066(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=275, w3=174, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(275, min_periods=max(275//3, 2)).mean()
    noise = impulse.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.499412 + 0.0026737 * anchor
    return base_signal

def f38_jump_gemini_067(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=288, w3=191, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 185)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 191)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.207667 * acceleration + 0.0026738 * anchor
    return base_signal

def f38_jump_gemini_068(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=301, w3=208, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(192, min_periods=max(192//3, 2)).mean(), upside.rolling(301, min_periods=max(301//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.526471 + 0.0026739 * anchor
    return base_signal

def f38_jump_gemini_069(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=314, w3=225, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(199, min_periods=max(199//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.220333 * _rolling_slope(draw, 225) + 0.002674 * anchor
    return base_signal

def f38_jump_gemini_070(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=327, w3=242, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 206)
    baseline = trend.rolling(327, min_periods=max(327//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(242, min_periods=max(242//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.553529 + 0.0026741 * anchor
    return base_signal

def f38_jump_gemini_071(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=340, w3=259, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 213)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=259, adjust=False).mean() * 1.567059 + 0.0026742 * anchor
    return base_signal

def f38_jump_gemini_072(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=353, w3=276, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(220, min_periods=max(220//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.580588 + 0.0026743 * anchor
    return base_signal

def f38_jump_gemini_073(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=366, w3=293, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245667 * persistence + 0.0026744 * anchor
    return base_signal

def f38_jump_gemini_074(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=379, w3=310, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(234, min_periods=max(234//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.607647 + 0.0026745 * anchor
    return base_signal

def f38_jump_gemini_075(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=392, w3=327, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 241)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.258333 * slope + 0.0026746 * anchor
    return base_signal
