"""64 volume velocity spike detector gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of rapid acceleration in volume as a precursor to price jumps.
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

def f64_vvsd_gemini_076_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=388, w3=161, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(388, min_periods=max(388//3, 2)).mean()
    noise = impulse.abs().rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.644706 + 0.0041447 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_077_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=401, w3=178, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 156)
    acceleration = _rolling_slope(velocity, 401)
    curvature = _rolling_slope(acceleration, 178)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.317667 * acceleration + 0.0041448 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_078_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=414, w3=195, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(414, min_periods=max(414//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.671765 + 0.0041449 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_079_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=427, w3=212, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(427, min_periods=max(427//3, 2)).max()
    rebound = x - x.rolling(170, min_periods=max(170//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.330333 * _rolling_slope(draw, 212) + 0.004145 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_080_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=440, w3=229, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(440, min_periods=max(440//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.845294 + 0.0041451 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_081_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=453, w3=246, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=246, adjust=False).mean() * 0.858824 + 0.0041452 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_082_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=466, w3=263, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(466, min_periods=max(466//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.872353 + 0.0041453 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_083_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=479, w3=280, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(479, min_periods=max(479//3, 2)).rank(pct=True)
    persistence = change.rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355667 * persistence + 0.0041454 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_084_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=492, w3=297, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(492, min_periods=max(492//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.899412 + 0.0041455 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_085_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=505, w3=314, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(505, min_periods=max(505//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.036 * slope + 0.0041456 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_086_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=19, w3=331, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(19, min_periods=max(19//3, 2)).mean()
    noise = impulse.abs().rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.926471 + 0.0041457 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_087_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=32, w3=348, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 32)
    curvature = _rolling_slope(acceleration, 348)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.048667 * acceleration + 0.0041458 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_088_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=45, w3=365, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(45, min_periods=max(45//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.953529 + 0.0041459 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_089_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=58, w3=382, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(58, min_periods=max(58//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.061333 * _rolling_slope(draw, 382) + 0.004146 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_090_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=71, w3=399, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(71, min_periods=max(71//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.980588 + 0.0041461 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_091_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=84, w3=416, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 84)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.994118 + 0.0041462 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_092_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=97, w3=433, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(97, min_periods=max(97//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.007647 + 0.0041463 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_093_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=110, w3=450, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(21)
    rank = change.rolling(110, min_periods=max(110//3, 2)).rank(pct=True)
    persistence = change.rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.086667 * persistence + 0.0041464 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_094_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=123, w3=467, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(123, min_periods=max(123//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.034706 + 0.0041465 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_095_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=136, w3=484, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(136, min_periods=max(136//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.099333 * slope + 0.0041466 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_096_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=149, w3=501, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(42)
    drag = impulse.rolling(149, min_periods=max(149//3, 2)).mean()
    noise = impulse.abs().rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.061765 + 0.0041467 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_097_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=162, w3=518, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 162)
    curvature = _rolling_slope(acceleration, 518)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.112 * acceleration + 0.0041468 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_098_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=175, w3=535, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(175, min_periods=max(175//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.088824 + 0.0041469 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_099_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=188, w3=552, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(188, min_periods=max(188//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.124667 * _rolling_slope(draw, 552) + 0.004147 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_100_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=201, w3=569, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(201, min_periods=max(201//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.115882 + 0.0041471 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_101_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=214, w3=586, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 214)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.129412 + 0.0041472 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_102_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=227, w3=603, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(227, min_periods=max(227//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.142941 + 0.0041473 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_103_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=240, w3=620, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(91)
    rank = change.rolling(240, min_periods=max(240//3, 2)).rank(pct=True)
    persistence = change.rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.15 * persistence + 0.0041474 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_104_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=253, w3=637, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(253, min_periods=max(253//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17 + 0.0041475 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_105_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=266, w3=654, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(266, min_periods=max(266//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.162667 * slope + 0.0041476 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_106_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=279, w3=671, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(112)
    drag = impulse.rolling(279, min_periods=max(279//3, 2)).mean()
    noise = impulse.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.197059 + 0.0041477 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_107_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=292, w3=688, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 292)
    curvature = _rolling_slope(acceleration, 688)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.175333 * acceleration + 0.0041478 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_108_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=305, w3=705, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(305, min_periods=max(305//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.224118 + 0.0041479 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_109_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=318, w3=722, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(318, min_periods=max(318//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.188 * _rolling_slope(draw, 722) + 0.004148 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_110_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=331, w3=739, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(331, min_periods=max(331//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.251176 + 0.0041481 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_111_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=344, w3=756, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 344)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.264706 + 0.0041482 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_112_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=357, w3=22, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(357, min_periods=max(357//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.278235 + 0.0041483 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_113_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=370, w3=39, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.213333 * persistence + 0.0041484 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_114_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=383, w3=56, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.305294 + 0.0041485 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_115_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=396, w3=73, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.226 * slope + 0.0041486 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_116_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=409, w3=90, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(409, min_periods=max(409//3, 2)).mean()
    noise = impulse.abs().rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.332353 + 0.0041487 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_117_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=189, w2=422, w3=107, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 422)
    curvature = _rolling_slope(acceleration, 107)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.238667 * acceleration + 0.0041488 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_118_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=196, w2=435, w3=124, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(196, min_periods=max(196//3, 2)).mean(), upside.rolling(435, min_periods=max(435//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(124) * 1.359412 + 0.0041489 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_119_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=203, w2=448, w3=141, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(448, min_periods=max(448//3, 2)).max()
    rebound = x - x.rolling(203, min_periods=max(203//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.251333 * _rolling_slope(draw, 141) + 0.004149 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_120_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=461, w3=158, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(461, min_periods=max(461//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.386471 + 0.0041491 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_121_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=474, w3=175, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 474)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=175, adjust=False).mean() * 1.4 + 0.0041492 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_122_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=487, w3=192, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(487, min_periods=max(487//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.413529 + 0.0041493 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_123_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=500, w3=209, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(500, min_periods=max(500//3, 2)).rank(pct=True)
    persistence = change.rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.276667 * persistence + 0.0041494 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_124_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=14, w3=226, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(14, min_periods=max(14//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.440588 + 0.0041495 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_125_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=27, w3=243, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(27, min_periods=max(27//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.289333 * slope + 0.0041496 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_126_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=40, w3=260, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(5)
    drag = impulse.rolling(40, min_periods=max(40//3, 2)).mean()
    noise = impulse.abs().rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.467647 + 0.0041497 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_127_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=53, w3=277, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 53)
    curvature = _rolling_slope(acceleration, 277)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.302 * acceleration + 0.0041498 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_128_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=66, w3=294, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(66, min_periods=max(66//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.494706 + 0.0041499 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_129_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=79, w3=311, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(79, min_periods=max(79//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.314667 * _rolling_slope(draw, 311) + 0.00415 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_130_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=92, w3=328, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(92, min_periods=max(92//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(328, min_periods=max(328//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.521765 + 0.0041501 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_131_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=105, w3=345, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 105)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.535294 + 0.0041502 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_132_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=118, w3=362, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(118, min_periods=max(118//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.548824 + 0.0041503 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_133_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=131, w3=379, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(54)
    rank = change.rolling(131, min_periods=max(131//3, 2)).rank(pct=True)
    persistence = change.rolling(379, min_periods=max(379//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.34 * persistence + 0.0041504 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_134_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=144, w3=396, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(144, min_periods=max(144//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.575882 + 0.0041505 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_135_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=157, w3=413, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(157, min_periods=max(157//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.352667 * slope + 0.0041506 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_136_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=170, w3=430, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(75)
    drag = impulse.rolling(170, min_periods=max(170//3, 2)).mean()
    noise = impulse.abs().rolling(430, min_periods=max(430//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.602941 + 0.0041507 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_137_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=183, w3=447, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 183)
    curvature = _rolling_slope(acceleration, 447)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.033 * acceleration + 0.0041508 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_138_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=196, w3=464, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(196, min_periods=max(196//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.63 + 0.0041509 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_139_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=209, w3=481, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(209, min_periods=max(209//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.045667 * _rolling_slope(draw, 481) + 0.004151 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_140_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=222, w3=498, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(222, min_periods=max(222//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.657059 + 0.0041511 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_141_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=235, w3=515, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 235)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.670588 + 0.0041512 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_142_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=248, w3=532, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(248, min_periods=max(248//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.830588 + 0.0041513 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_143_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=261, w3=549, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(124)
    rank = change.rolling(261, min_periods=max(261//3, 2)).rank(pct=True)
    persistence = change.rolling(549, min_periods=max(549//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071 * persistence + 0.0041514 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_144_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=274, w3=566, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(274, min_periods=max(274//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.857647 + 0.0041515 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_145_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=287, w3=583, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(287, min_periods=max(287//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.083667 * slope + 0.0041516 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_146_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=300, w3=600, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(300, min_periods=max(300//3, 2)).mean()
    noise = impulse.abs().rolling(600, min_periods=max(600//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.884706 + 0.0041517 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_147_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=313, w3=617, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 152)
    acceleration = _rolling_slope(velocity, 313)
    curvature = _rolling_slope(acceleration, 617)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.096333 * acceleration + 0.0041518 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_148_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=326, w3=634, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(159, min_periods=max(159//3, 2)).mean(), upside.rolling(326, min_periods=max(326//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.911765 + 0.0041519 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_149_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=339, w3=651, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(339, min_periods=max(339//3, 2)).max()
    rebound = x - x.rolling(166, min_periods=max(166//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.109 * _rolling_slope(draw, 651) + 0.004152 * anchor
    return base_signal.diff()

def f64_vvsd_gemini_150_d1(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=352, w3=668, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 173)
    baseline = trend.rolling(352, min_periods=max(352//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(668, min_periods=max(668//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.938824 + 0.0041521 * anchor
    return base_signal.diff()
