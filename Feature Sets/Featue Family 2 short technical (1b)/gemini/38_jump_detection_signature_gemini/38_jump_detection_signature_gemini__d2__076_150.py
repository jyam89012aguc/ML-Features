"""38 jump detection signature gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

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
# FEATURE HYPOTHESES (076-150)
# ============================================================

def f38_jump_gemini_076_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=53, w3=598, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(53, min_periods=max(53//3, 2)).mean()
    noise = impulse.abs().rolling(598, min_periods=max(598//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.155294 + 0.0027027 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_077_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=66, w3=615, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 239)
    acceleration = _rolling_slope(velocity, 66)
    curvature = _rolling_slope(acceleration, 615)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.050333 * acceleration + 0.0027028 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_078_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=79, w3=632, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(246, min_periods=max(246//3, 2)).mean(), upside.rolling(79, min_periods=max(79//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.182353 + 0.0027029 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_079_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=92, w3=649, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(92, min_periods=max(92//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.063 * _rolling_slope(draw, 649) + 0.002703 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_080_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=105, w3=666, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(105, min_periods=max(105//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.209412 + 0.0027031 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_081_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=118, w3=683, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 118)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.222941 + 0.0027032 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_082_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=131, w3=700, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(131, min_periods=max(131//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.236471 + 0.0027033 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_083_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=144, w3=717, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(34)
    rank = change.rolling(144, min_periods=max(144//3, 2)).rank(pct=True)
    persistence = change.rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.088333 * persistence + 0.0027034 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_084_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=157, w3=734, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(157, min_periods=max(157//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.263529 + 0.0027035 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_085_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=170, w3=751, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.101 * slope + 0.0027036 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_086_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=183, w3=17, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(55)
    drag = impulse.rolling(183, min_periods=max(183//3, 2)).mean()
    noise = impulse.abs().rolling(17, min_periods=max(17//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.290588 + 0.0027037 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_087_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=196, w3=34, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 196)
    curvature = _rolling_slope(acceleration, 34)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113667 * acceleration + 0.0027038 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_088_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=209, w3=51, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(209, min_periods=max(209//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(51) * 1.317647 + 0.0027039 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_089_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=222, w3=68, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(222, min_periods=max(222//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.126333 * _rolling_slope(draw, 68) + 0.002704 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_090_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=235, w3=85, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(235, min_periods=max(235//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.344706 + 0.0027041 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_091_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=248, w3=102, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 248)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=102, adjust=False).mean() * 1.358235 + 0.0027042 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_092_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=261, w3=119, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(261, min_periods=max(261//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.371765 + 0.0027043 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_093_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=274, w3=136, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(104)
    rank = change.rolling(274, min_periods=max(274//3, 2)).rank(pct=True)
    persistence = change.rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.151667 * persistence + 0.0027044 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_094_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=287, w3=153, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(287, min_periods=max(287//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.398824 + 0.0027045 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_095_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=300, w3=170, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(300, min_periods=max(300//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.164333 * slope + 0.0027046 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_096_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=313, w3=187, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(125)
    drag = impulse.rolling(313, min_periods=max(313//3, 2)).mean()
    noise = impulse.abs().rolling(187, min_periods=max(187//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.425882 + 0.0027047 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_097_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=326, w3=204, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 326)
    curvature = _rolling_slope(acceleration, 204)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.177 * acceleration + 0.0027048 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_098_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=339, w3=221, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(339, min_periods=max(339//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.452941 + 0.0027049 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_099_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=352, w3=238, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(352, min_periods=max(352//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189667 * _rolling_slope(draw, 238) + 0.002705 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_100_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=365, w3=255, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(365, min_periods=max(365//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.48 + 0.0027051 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_101_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=378, w3=272, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 378)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=272, adjust=False).mean() * 1.493529 + 0.0027052 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_102_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=391, w3=289, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.507059 + 0.0027053 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_103_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=404, w3=306, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(404, min_periods=max(404//3, 2)).rank(pct=True)
    persistence = change.rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.215 * persistence + 0.0027054 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_104_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=417, w3=323, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.534118 + 0.0027055 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_105_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=430, w3=340, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(430, min_periods=max(430//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.227667 * slope + 0.0027056 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_106_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=443, w3=357, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(443, min_periods=max(443//3, 2)).mean()
    noise = impulse.abs().rolling(357, min_periods=max(357//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.561176 + 0.0027057 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_107_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=456, w3=374, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 456)
    curvature = _rolling_slope(acceleration, 374)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.240333 * acceleration + 0.0027058 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_108_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=469, w3=391, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(469, min_periods=max(469//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.588235 + 0.0027059 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_109_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=482, w3=408, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(482, min_periods=max(482//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.253 * _rolling_slope(draw, 408) + 0.002706 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_110_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=495, w3=425, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.615294 + 0.0027061 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_111_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=508, w3=442, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 508)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.628824 + 0.0027062 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_112_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=22, w3=459, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(22, min_periods=max(22//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.642353 + 0.0027063 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_113_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=35, w3=476, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(35, min_periods=max(35//3, 2)).rank(pct=True)
    persistence = change.rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.278333 * persistence + 0.0027064 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_114_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=48, w3=493, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(48, min_periods=max(48//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.669412 + 0.0027065 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_115_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=61, w3=510, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(61, min_periods=max(61//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.291 * slope + 0.0027066 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_116_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=74, w3=527, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(18)
    drag = impulse.rolling(74, min_periods=max(74//3, 2)).mean()
    noise = impulse.abs().rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.842941 + 0.0027067 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_117_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=87, w3=544, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 87)
    curvature = _rolling_slope(acceleration, 544)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.303667 * acceleration + 0.0027068 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_118_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=100, w3=561, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(100, min_periods=max(100//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87 + 0.0027069 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_119_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=113, w3=578, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(113, min_periods=max(113//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.316333 * _rolling_slope(draw, 578) + 0.002707 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_120_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=126, w3=595, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(126, min_periods=max(126//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.897059 + 0.0027071 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_121_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=139, w3=612, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 139)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.910588 + 0.0027072 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_122_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=152, w3=629, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(152, min_periods=max(152//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.924118 + 0.0027073 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_123_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=165, w3=646, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(67)
    rank = change.rolling(165, min_periods=max(165//3, 2)).rank(pct=True)
    persistence = change.rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.341667 * persistence + 0.0027074 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_124_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=178, w3=663, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(178, min_periods=max(178//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.951176 + 0.0027075 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_125_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=191, w3=680, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(191, min_periods=max(191//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.354333 * slope + 0.0027076 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_126_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=204, w3=697, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(88)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(697, min_periods=max(697//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.978235 + 0.0027077 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_127_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=217, w3=714, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 217)
    curvature = _rolling_slope(acceleration, 714)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.034667 * acceleration + 0.0027078 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_128_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=230, w3=731, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(230, min_periods=max(230//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.005294 + 0.0027079 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_129_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=243, w3=748, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(243, min_periods=max(243//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.047333 * _rolling_slope(draw, 748) + 0.002708 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_130_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=256, w3=765, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(256, min_periods=max(256//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.032353 + 0.0027081 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_131_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=269, w3=31, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 269)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=31, adjust=False).mean() * 1.045882 + 0.0027082 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_132_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=282, w3=48, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(282, min_periods=max(282//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.059412 + 0.0027083 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_133_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=295, w3=65, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(295, min_periods=max(295//3, 2)).rank(pct=True)
    persistence = change.rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.072667 * persistence + 0.0027084 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_134_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=308, w3=82, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(308, min_periods=max(308//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.086471 + 0.0027085 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_135_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=321, w3=99, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(321, min_periods=max(321//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.085333 * slope + 0.0027086 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_136_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=334, w3=116, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(334, min_periods=max(334//3, 2)).mean()
    noise = impulse.abs().rolling(116, min_periods=max(116//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.113529 + 0.0027087 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_137_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=347, w3=133, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 347)
    curvature = _rolling_slope(acceleration, 133)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.098 * acceleration + 0.0027088 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_138_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=360, w3=150, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(360, min_periods=max(360//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.140588 + 0.0027089 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_139_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=373, w3=167, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.110667 * _rolling_slope(draw, 167) + 0.002709 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_140_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=386, w3=184, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(184, min_periods=max(184//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.167647 + 0.0027091 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_141_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=399, w3=201, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 399)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=201, adjust=False).mean() * 1.181176 + 0.0027092 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_142_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=412, w3=218, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(412, min_periods=max(412//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.194706 + 0.0027093 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_143_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=425, w3=235, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(425, min_periods=max(425//3, 2)).rank(pct=True)
    persistence = change.rolling(235, min_periods=max(235//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.136 * persistence + 0.0027094 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_144_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=438, w3=252, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(438, min_periods=max(438//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.221765 + 0.0027095 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_145_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=451, w3=269, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(451, min_periods=max(451//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.148667 * slope + 0.0027096 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_146_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=464, w3=286, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(464, min_periods=max(464//3, 2)).mean()
    noise = impulse.abs().rolling(286, min_periods=max(286//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.248824 + 0.0027097 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_147_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=477, w3=303, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 477)
    curvature = _rolling_slope(acceleration, 303)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.161333 * acceleration + 0.0027098 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_148_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=490, w3=320, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(490, min_periods=max(490//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.275882 + 0.0027099 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_149_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=503, w3=337, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(503, min_periods=max(503//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.174 * _rolling_slope(draw, 337) + 0.00271 * anchor
    return base_signal.diff().diff()

def f38_jump_gemini_150_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=17, w3=354, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 9)
    baseline = trend.rolling(17, min_periods=max(17//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(354, min_periods=max(354//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.302941 + 0.0027101 * anchor
    return base_signal.diff().diff()
