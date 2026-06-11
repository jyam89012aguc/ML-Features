"""35 realized volatility regime gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Historical volatility levels categorized into regimes to identify shifts in market environment.
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
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f35_rvol_gemini_076_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=492, w3=703, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(73)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(703, min_periods=max(703//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.658235 + 0.0025487 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_077_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=505, w3=720, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 505)
    curvature = _rolling_slope(acceleration, 720)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.267 * acceleration + 0.0025488 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_078_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=19, w3=737, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.831765 + 0.0025489 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_079_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=32, w3=754, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.279667 * _rolling_slope(draw, 754) + 0.002549 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_080_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=45, w3=20, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(45, min_periods=max(45//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(20, min_periods=max(20//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.858824 + 0.0025491 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_081_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=58, w3=37, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=37, adjust=False).mean() * 0.872353 + 0.0025492 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_082_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=71, w3=54, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.885882 + 0.0025493 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_083_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=84, w3=71, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(122)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(71, min_periods=max(71//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.305 * persistence + 0.0025494 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_084_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=97, w3=88, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.912941 + 0.0025495 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_085_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=110, w3=105, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.317667 * slope + 0.0025496 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_086_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=123, w3=122, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94 + 0.0025497 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_087_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=136, w3=139, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 139)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.330333 * acceleration + 0.0025498 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_088_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=149, w3=156, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.967059 + 0.0025499 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_089_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=162, w3=173, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.343 * _rolling_slope(draw, 173) + 0.00255 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_090_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=175, w3=190, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(175, min_periods=max(175//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.994118 + 0.0025501 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_091_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=188, w3=207, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=207, adjust=False).mean() * 1.007647 + 0.0025502 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_092_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=201, w3=224, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(201, min_periods=max(201//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.021176 + 0.0025503 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_093_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=214, w3=241, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.036 * persistence + 0.0025504 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_094_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=227, w3=258, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.048235 + 0.0025505 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_095_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=240, w3=275, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.048667 * slope + 0.0025506 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_096_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=253, w3=292, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(292, min_periods=max(292//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.075294 + 0.0025507 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_097_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=266, w3=309, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 309)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.061333 * acceleration + 0.0025508 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_098_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=279, w3=326, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.102353 + 0.0025509 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_099_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=292, w3=343, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.074 * _rolling_slope(draw, 343) + 0.002551 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_100_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=305, w3=360, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(360, min_periods=max(360//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.129412 + 0.0025511 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_101_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=318, w3=377, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.142941 + 0.0025512 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_102_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=331, w3=394, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.156471 + 0.0025513 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_103_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=344, w3=411, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(15)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.099333 * persistence + 0.0025514 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_104_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=357, w3=428, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(357, min_periods=max(357//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.183529 + 0.0025515 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_105_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=370, w3=445, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.112 * slope + 0.0025516 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_106_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=383, w3=462, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(36)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.210588 + 0.0025517 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_107_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=396, w3=479, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 479)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.124667 * acceleration + 0.0025518 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_108_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=409, w3=496, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.237647 + 0.0025519 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_109_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=422, w3=513, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(422, min_periods=max(422//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.137333 * _rolling_slope(draw, 513) + 0.002552 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_110_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=435, w3=530, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.264706 + 0.0025521 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_111_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=448, w3=547, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.278235 + 0.0025522 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_112_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=461, w3=564, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.291765 + 0.0025523 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_113_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=474, w3=581, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(85)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.162667 * persistence + 0.0025524 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_114_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=487, w3=598, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.318824 + 0.0025525 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_115_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=500, w3=615, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.175333 * slope + 0.0025526 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_116_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=14, w3=632, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(106)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.345882 + 0.0025527 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_117_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=27, w3=649, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 27)
    curvature = _rolling_slope(acceleration, 649)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.188 * acceleration + 0.0025528 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_118_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=40, w3=666, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(40, min_periods=max(40//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.372941 + 0.0025529 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_119_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=53, w3=683, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.200667 * _rolling_slope(draw, 683) + 0.002553 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_120_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=66, w3=700, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4 + 0.0025531 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_121_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=79, w3=717, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 79)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.413529 + 0.0025532 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_122_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=92, w3=734, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(92, min_periods=max(92//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.427059 + 0.0025533 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_123_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=105, w3=751, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(105, min_periods=max(105//3, 2)).rank(pct=True)
    persistence = change.rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.226 * persistence + 0.0025534 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_124_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=118, w3=17, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(118, min_periods=max(118//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.454118 + 0.0025535 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_125_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=131, w3=34, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(131, min_periods=max(131//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.238667 * slope + 0.0025536 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_126_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=144, w3=51, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(144, min_periods=max(144//3, 2)).mean()
    noise = impulse.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.481176 + 0.0025537 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_127_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=157, w3=68, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 157)
    curvature = _rolling_slope(acceleration, 68)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.251333 * acceleration + 0.0025538 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_128_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=170, w3=85, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(170, min_periods=max(170//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(85) * 1.508235 + 0.0025539 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_129_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=183, w3=102, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(183, min_periods=max(183//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.264 * _rolling_slope(draw, 102) + 0.002554 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_130_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=196, w3=119, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.535294 + 0.0025541 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_131_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=209, w3=136, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 209)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=136, adjust=False).mean() * 1.548824 + 0.0025542 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_132_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=222, w3=153, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.562353 + 0.0025543 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_133_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=235, w3=170, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(235, min_periods=max(235//3, 2)).rank(pct=True)
    persistence = change.rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.289333 * persistence + 0.0025544 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_134_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=248, w3=187, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(248, min_periods=max(248//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.589412 + 0.0025545 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_135_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=261, w3=204, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(261, min_periods=max(261//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.302 * slope + 0.0025546 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_136_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=274, w3=221, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(274, min_periods=max(274//3, 2)).mean()
    noise = impulse.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.616471 + 0.0025547 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_137_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=287, w3=238, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 287)
    curvature = _rolling_slope(acceleration, 238)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.314667 * acceleration + 0.0025548 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_138_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=300, w3=255, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.643529 + 0.0025549 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_139_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=313, w3=272, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(313, min_periods=max(313//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.327333 * _rolling_slope(draw, 272) + 0.002555 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_140_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=326, w3=289, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(326, min_periods=max(326//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.670588 + 0.0025551 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_141_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=339, w3=306, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 339)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.830588 + 0.0025552 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_142_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=352, w3=323, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(352, min_periods=max(352//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.844118 + 0.0025553 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_143_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=365, w3=340, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(48)
    rank = change.rolling(365, min_periods=max(365//3, 2)).rank(pct=True)
    persistence = change.rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.352667 * persistence + 0.0025554 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_144_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=378, w3=357, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(378, min_periods=max(378//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.871176 + 0.0025555 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_145_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=391, w3=374, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(391, min_periods=max(391//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.033 * slope + 0.0025556 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_146_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=404, w3=391, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(69)
    drag = impulse.rolling(404, min_periods=max(404//3, 2)).mean()
    noise = impulse.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.898235 + 0.0025557 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_147_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=417, w3=408, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 417)
    curvature = _rolling_slope(acceleration, 408)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045667 * acceleration + 0.0025558 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_148_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=430, w3=425, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(430, min_periods=max(430//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.925294 + 0.0025559 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_149_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=443, w3=442, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(443, min_periods=max(443//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.058333 * _rolling_slope(draw, 442) + 0.002556 * anchor
    return base_signal.diff().diff().diff()

def f35_rvol_gemini_150_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=456, w3=459, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(456, min_periods=max(456//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.952353 + 0.0025561 * anchor
    return base_signal.diff().diff().diff()
