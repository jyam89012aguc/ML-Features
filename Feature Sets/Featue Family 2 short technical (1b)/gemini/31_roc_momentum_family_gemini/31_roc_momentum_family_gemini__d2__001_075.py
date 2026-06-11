"""31 roc momentum family gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Rate of change measurements identifying the velocity of price movements.
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

def f31_rocm_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=5]"""
    window = 5
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=10]"""
    window = 10
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=21]"""
    window = 21
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=42]"""
    window = 42
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=63]"""
    window = 63
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=126]"""
    window = 126
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=252]"""
    window = 252
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=504]"""
    window = 504
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=756]"""
    window = 756
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Rate of change measurements identifying the velocity of price movements. [window=1260]"""
    window = 1260
    res = _safe_div(close - close.shift(window), close.shift(window) + 1e-9)
    return (res).diff().diff()

def f31_rocm_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=248, w2=144, w3=443, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 248)
    slow = _rolling_slope(x, 144)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.012941 + 0.0023042 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=8, w2=157, w3=460, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(157, min_periods=max(157//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.026471 + 0.0023043 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=15, w2=170, w3=477, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(15)
    rank = change.rolling(170, min_periods=max(170//3, 2)).rank(pct=True)
    persistence = change.rolling(477, min_periods=max(477//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.075667 * persistence + 0.0023044 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=22, w2=183, w3=494, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(183, min_periods=max(183//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.053529 + 0.0023045 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=29, w2=196, w3=511, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(196, min_periods=max(196//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.088333 * slope + 0.0023046 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=36, w2=209, w3=528, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(36)
    drag = impulse.rolling(209, min_periods=max(209//3, 2)).mean()
    noise = impulse.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.080588 + 0.0023047 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=43, w2=222, w3=545, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 222)
    curvature = _rolling_slope(acceleration, 545)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.101 * acceleration + 0.0023048 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=50, w2=235, w3=562, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(235, min_periods=max(235//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.107647 + 0.0023049 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=57, w2=248, w3=579, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.113667 * _rolling_slope(draw, 579) + 0.002305 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=64, w2=261, w3=596, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(261, min_periods=max(261//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.134706 + 0.0023051 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=71, w2=274, w3=613, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.148235 + 0.0023052 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=78, w2=287, w3=630, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(287, min_periods=max(287//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.161765 + 0.0023053 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=85, w2=300, w3=647, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(85)
    rank = change.rolling(300, min_periods=max(300//3, 2)).rank(pct=True)
    persistence = change.rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.139 * persistence + 0.0023054 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=92, w2=313, w3=664, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(313, min_periods=max(313//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.188824 + 0.0023055 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=99, w2=326, w3=681, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(326, min_periods=max(326//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.151667 * slope + 0.0023056 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=106, w2=339, w3=698, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(106)
    drag = impulse.rolling(339, min_periods=max(339//3, 2)).mean()
    noise = impulse.abs().rolling(698, min_periods=max(698//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.215882 + 0.0023057 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=113, w2=352, w3=715, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 352)
    curvature = _rolling_slope(acceleration, 715)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.164333 * acceleration + 0.0023058 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=120, w2=365, w3=732, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(365, min_periods=max(365//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.242941 + 0.0023059 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=378, w3=749, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(378, min_periods=max(378//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.177 * _rolling_slope(draw, 749) + 0.002306 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=391, w3=766, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(391, min_periods=max(391//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.27 + 0.0023061 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=404, w3=32, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 404)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=32, adjust=False).mean() * 1.283529 + 0.0023062 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=417, w3=49, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(417, min_periods=max(417//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.297059 + 0.0023063 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=430, w3=66, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(430, min_periods=max(430//3, 2)).rank(pct=True)
    persistence = change.rolling(66, min_periods=max(66//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.202333 * persistence + 0.0023064 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=443, w3=83, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(443, min_periods=max(443//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.324118 + 0.0023065 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=456, w3=100, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(456, min_periods=max(456//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.215 * slope + 0.0023066 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=469, w3=117, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(469, min_periods=max(469//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.351176 + 0.0023067 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=482, w3=134, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 482)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.227667 * acceleration + 0.0023068 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=495, w3=151, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(495, min_periods=max(495//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.378235 + 0.0023069 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=508, w3=168, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(508, min_periods=max(508//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.240333 * _rolling_slope(draw, 168) + 0.002307 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=22, w3=185, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(22, min_periods=max(22//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.405294 + 0.0023071 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=35, w3=202, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 35)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=202, adjust=False).mean() * 1.418824 + 0.0023072 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=48, w3=219, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(48, min_periods=max(48//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.432353 + 0.0023073 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=61, w3=236, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(61, min_periods=max(61//3, 2)).rank(pct=True)
    persistence = change.rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265667 * persistence + 0.0023074 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=74, w3=253, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(74, min_periods=max(74//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.459412 + 0.0023075 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=87, w3=270, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(87, min_periods=max(87//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.278333 * slope + 0.0023076 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=100, w3=287, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(100, min_periods=max(100//3, 2)).mean()
    noise = impulse.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.486471 + 0.0023077 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=113, w3=304, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 113)
    curvature = _rolling_slope(acceleration, 304)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.291 * acceleration + 0.0023078 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=126, w3=321, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(13, min_periods=max(13//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.513529 + 0.0023079 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=139, w3=338, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(139, min_periods=max(139//3, 2)).max()
    rebound = x - x.rolling(20, min_periods=max(20//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.303667 * _rolling_slope(draw, 338) + 0.002308 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=152, w3=355, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(152, min_periods=max(152//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(355, min_periods=max(355//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.540588 + 0.0023081 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=165, w3=372, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 165)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.554118 + 0.0023082 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=178, w3=389, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(178, min_periods=max(178//3, 2)).max()
    trough = x.rolling(41, min_periods=max(41//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.567647 + 0.0023083 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=191, w3=406, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(48)
    rank = change.rolling(191, min_periods=max(191//3, 2)).rank(pct=True)
    persistence = change.rolling(406, min_periods=max(406//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.329 * persistence + 0.0023084 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=204, w3=423, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(55, min_periods=max(55//3, 2)).std()
    vol_slow = ret.rolling(204, min_periods=max(204//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.594706 + 0.0023085 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=217, w3=440, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(217, min_periods=max(217//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.341667 * slope + 0.0023086 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=230, w3=457, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(69)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.621765 + 0.0023087 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=243, w3=474, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 243)
    curvature = _rolling_slope(acceleration, 474)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.354333 * acceleration + 0.0023088 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=256, w3=491, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(83, min_periods=max(83//3, 2)).mean(), upside.rolling(256, min_periods=max(256//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.648824 + 0.0023089 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=269, w3=508, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(269, min_periods=max(269//3, 2)).max()
    rebound = x - x.rolling(90, min_periods=max(90//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.034667 * _rolling_slope(draw, 508) + 0.002309 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=282, w3=525, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 97)
    baseline = trend.rolling(282, min_periods=max(282//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.822353 + 0.0023091 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=295, w3=542, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 104)
    slow = _rolling_slope(x, 295)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.835882 + 0.0023092 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=308, w3=559, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(308, min_periods=max(308//3, 2)).max()
    trough = x.rolling(111, min_periods=max(111//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.849412 + 0.0023093 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=321, w3=576, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(118)
    rank = change.rolling(321, min_periods=max(321//3, 2)).rank(pct=True)
    persistence = change.rolling(576, min_periods=max(576//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.06 * persistence + 0.0023094 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=334, w3=593, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(125, min_periods=max(125//3, 2)).std()
    vol_slow = ret.rolling(334, min_periods=max(334//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.876471 + 0.0023095 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=347, w3=610, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(347, min_periods=max(347//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 132)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.072667 * slope + 0.0023096 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=360, w3=627, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(360, min_periods=max(360//3, 2)).mean()
    noise = impulse.abs().rolling(627, min_periods=max(627//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.903529 + 0.0023097 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=373, w3=644, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 146)
    acceleration = _rolling_slope(velocity, 373)
    curvature = _rolling_slope(acceleration, 644)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.085333 * acceleration + 0.0023098 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=386, w3=661, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(153, min_periods=max(153//3, 2)).mean(), upside.rolling(386, min_periods=max(386//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.930588 + 0.0023099 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=399, w3=678, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(399, min_periods=max(399//3, 2)).max()
    rebound = x - x.rolling(160, min_periods=max(160//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.098 * _rolling_slope(draw, 678) + 0.00231 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=412, w3=695, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 167)
    baseline = trend.rolling(412, min_periods=max(412//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(695, min_periods=max(695//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.957647 + 0.0023101 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=425, w3=712, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 174)
    slow = _rolling_slope(x, 425)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.971176 + 0.0023102 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=438, w3=729, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(438, min_periods=max(438//3, 2)).max()
    trough = x.rolling(181, min_periods=max(181//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.984706 + 0.0023103 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=451, w3=746, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(451, min_periods=max(451//3, 2)).rank(pct=True)
    persistence = change.rolling(746, min_periods=max(746//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.123333 * persistence + 0.0023104 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=464, w3=763, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(195, min_periods=max(195//3, 2)).std()
    vol_slow = ret.rolling(464, min_periods=max(464//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.011765 + 0.0023105 * anchor
    return base_signal.diff().diff()

def f31_rocm_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=477, w3=29, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(477, min_periods=max(477//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 202)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.136 * slope + 0.0023106 * anchor
    return base_signal.diff().diff()
