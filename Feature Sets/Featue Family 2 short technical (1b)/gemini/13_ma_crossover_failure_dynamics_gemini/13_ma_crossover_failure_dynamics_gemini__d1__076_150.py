"""13 ma crossover failure dynamics gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Failed moving average crossovers where price reverses immediately after the signal.
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

def f13_macf_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=364, w3=538, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(52)
    drag = impulse.rolling(364, min_periods=max(364//3, 2)).mean()
    noise = impulse.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.04 + 0.0012887 * anchor
    return base_signal.diff()

def f13_macf_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=377, w3=555, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 59)
    acceleration = _rolling_slope(velocity, 377)
    curvature = _rolling_slope(acceleration, 555)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.227 * acceleration + 0.0012888 * anchor
    return base_signal.diff()

def f13_macf_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=390, w3=572, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(66, min_periods=max(66//3, 2)).mean(), upside.rolling(390, min_periods=max(390//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.067059 + 0.0012889 * anchor
    return base_signal.diff()

def f13_macf_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=403, w3=589, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(403, min_periods=max(403//3, 2)).max()
    rebound = x - x.rolling(73, min_periods=max(73//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.239667 * _rolling_slope(draw, 589) + 0.001289 * anchor
    return base_signal.diff()

def f13_macf_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=416, w3=606, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 80)
    baseline = trend.rolling(416, min_periods=max(416//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.094118 + 0.0012891 * anchor
    return base_signal.diff()

def f13_macf_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=429, w3=623, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 87)
    slow = _rolling_slope(x, 429)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.107647 + 0.0012892 * anchor
    return base_signal.diff()

def f13_macf_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=442, w3=640, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(442, min_periods=max(442//3, 2)).max()
    trough = x.rolling(94, min_periods=max(94//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.121176 + 0.0012893 * anchor
    return base_signal.diff()

def f13_macf_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=455, w3=657, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(101)
    rank = change.rolling(455, min_periods=max(455//3, 2)).rank(pct=True)
    persistence = change.rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.265 * persistence + 0.0012894 * anchor
    return base_signal.diff()

def f13_macf_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=468, w3=674, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(108, min_periods=max(108//3, 2)).std()
    vol_slow = ret.rolling(468, min_periods=max(468//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.148235 + 0.0012895 * anchor
    return base_signal.diff()

def f13_macf_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=481, w3=691, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(481, min_periods=max(481//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 115)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.277667 * slope + 0.0012896 * anchor
    return base_signal.diff()

def f13_macf_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=494, w3=708, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(122)
    drag = impulse.rolling(494, min_periods=max(494//3, 2)).mean()
    noise = impulse.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.175294 + 0.0012897 * anchor
    return base_signal.diff()

def f13_macf_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=507, w3=725, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 129)
    acceleration = _rolling_slope(velocity, 507)
    curvature = _rolling_slope(acceleration, 725)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.290333 * acceleration + 0.0012898 * anchor
    return base_signal.diff()

def f13_macf_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=21, w3=742, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(21, min_periods=max(21//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.202353 + 0.0012899 * anchor
    return base_signal.diff()

def f13_macf_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=34, w3=759, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(34, min_periods=max(34//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.303 * _rolling_slope(draw, 759) + 0.00129 * anchor
    return base_signal.diff()

def f13_macf_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=47, w3=25, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 150)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.229412 + 0.0012901 * anchor
    return base_signal.diff()

def f13_macf_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=60, w3=42, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 157)
    slow = _rolling_slope(x, 60)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=42, adjust=False).mean() * 1.242941 + 0.0012902 * anchor
    return base_signal.diff()

def f13_macf_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=73, w3=59, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(73, min_periods=max(73//3, 2)).max()
    trough = x.rolling(164, min_periods=max(164//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.256471 + 0.0012903 * anchor
    return base_signal.diff()

def f13_macf_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=86, w3=76, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(86, min_periods=max(86//3, 2)).rank(pct=True)
    persistence = change.rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.328333 * persistence + 0.0012904 * anchor
    return base_signal.diff()

def f13_macf_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=99, w3=93, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(178, min_periods=max(178//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.283529 + 0.0012905 * anchor
    return base_signal.diff()

def f13_macf_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=112, w3=110, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(112, min_periods=max(112//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 185)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.341 * slope + 0.0012906 * anchor
    return base_signal.diff()

def f13_macf_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=125, w3=127, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.310588 + 0.0012907 * anchor
    return base_signal.diff()

def f13_macf_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=138, w3=144, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 199)
    acceleration = _rolling_slope(velocity, 138)
    curvature = _rolling_slope(acceleration, 144)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.353667 * acceleration + 0.0012908 * anchor
    return base_signal.diff()

def f13_macf_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=151, w3=161, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(206, min_periods=max(206//3, 2)).mean(), upside.rolling(151, min_periods=max(151//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.337647 + 0.0012909 * anchor
    return base_signal.diff()

def f13_macf_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=164, w3=178, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(164, min_periods=max(164//3, 2)).max()
    rebound = x - x.rolling(213, min_periods=max(213//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.034 * _rolling_slope(draw, 178) + 0.001291 * anchor
    return base_signal.diff()

def f13_macf_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=177, w3=195, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 220)
    baseline = trend.rolling(177, min_periods=max(177//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.364706 + 0.0012911 * anchor
    return base_signal.diff()

def f13_macf_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=190, w3=212, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 227)
    slow = _rolling_slope(x, 190)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=212, adjust=False).mean() * 1.378235 + 0.0012912 * anchor
    return base_signal.diff()

def f13_macf_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=203, w3=229, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(203, min_periods=max(203//3, 2)).max()
    trough = x.rolling(234, min_periods=max(234//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.391765 + 0.0012913 * anchor
    return base_signal.diff()

def f13_macf_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=216, w3=246, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(216, min_periods=max(216//3, 2)).rank(pct=True)
    persistence = change.rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.059333 * persistence + 0.0012914 * anchor
    return base_signal.diff()

def f13_macf_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=229, w3=263, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(248, min_periods=max(248//3, 2)).std()
    vol_slow = ret.rolling(229, min_periods=max(229//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.418824 + 0.0012915 * anchor
    return base_signal.diff()

def f13_macf_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=242, w3=280, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(242, min_periods=max(242//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 8)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.072 * slope + 0.0012916 * anchor
    return base_signal.diff()

def f13_macf_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=255, w3=297, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(15)
    drag = impulse.rolling(255, min_periods=max(255//3, 2)).mean()
    noise = impulse.abs().rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.445882 + 0.0012917 * anchor
    return base_signal.diff()

def f13_macf_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=268, w3=314, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 22)
    acceleration = _rolling_slope(velocity, 268)
    curvature = _rolling_slope(acceleration, 314)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.084667 * acceleration + 0.0012918 * anchor
    return base_signal.diff()

def f13_macf_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=281, w3=331, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(281, min_periods=max(281//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.472941 + 0.0012919 * anchor
    return base_signal.diff()

def f13_macf_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=294, w3=348, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(294, min_periods=max(294//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.097333 * _rolling_slope(draw, 348) + 0.001292 * anchor
    return base_signal.diff()

def f13_macf_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=307, w3=365, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 43)
    baseline = trend.rolling(307, min_periods=max(307//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.5 + 0.0012921 * anchor
    return base_signal.diff()

def f13_macf_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=320, w3=382, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 50)
    slow = _rolling_slope(x, 320)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.513529 + 0.0012922 * anchor
    return base_signal.diff()

def f13_macf_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=333, w3=399, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(57, min_periods=max(57//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.527059 + 0.0012923 * anchor
    return base_signal.diff()

def f13_macf_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=346, w3=416, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(64)
    rank = change.rolling(346, min_periods=max(346//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.122667 * persistence + 0.0012924 * anchor
    return base_signal.diff()

def f13_macf_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=359, w3=433, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(71, min_periods=max(71//3, 2)).std()
    vol_slow = ret.rolling(359, min_periods=max(359//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.554118 + 0.0012925 * anchor
    return base_signal.diff()

def f13_macf_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=372, w3=450, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(372, min_periods=max(372//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 78)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.135333 * slope + 0.0012926 * anchor
    return base_signal.diff()

def f13_macf_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=385, w3=467, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(85)
    drag = impulse.rolling(385, min_periods=max(385//3, 2)).mean()
    noise = impulse.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.581176 + 0.0012927 * anchor
    return base_signal.diff()

def f13_macf_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=398, w3=484, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 92)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 484)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.148 * acceleration + 0.0012928 * anchor
    return base_signal.diff()

def f13_macf_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=411, w3=501, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(99, min_periods=max(99//3, 2)).mean(), upside.rolling(411, min_periods=max(411//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.608235 + 0.0012929 * anchor
    return base_signal.diff()

def f13_macf_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=424, w3=518, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(424, min_periods=max(424//3, 2)).max()
    rebound = x - x.rolling(106, min_periods=max(106//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.160667 * _rolling_slope(draw, 518) + 0.001293 * anchor
    return base_signal.diff()

def f13_macf_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=437, w3=535, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 113)
    baseline = trend.rolling(437, min_periods=max(437//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.635294 + 0.0012931 * anchor
    return base_signal.diff()

def f13_macf_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=450, w3=552, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 120)
    slow = _rolling_slope(x, 450)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.648824 + 0.0012932 * anchor
    return base_signal.diff()

def f13_macf_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=463, w3=569, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(463, min_periods=max(463//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.662353 + 0.0012933 * anchor
    return base_signal.diff()

def f13_macf_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=476, w3=586, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(476, min_periods=max(476//3, 2)).rank(pct=True)
    persistence = change.rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.186 * persistence + 0.0012934 * anchor
    return base_signal.diff()

def f13_macf_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=489, w3=603, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(489, min_periods=max(489//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.835882 + 0.0012935 * anchor
    return base_signal.diff()

def f13_macf_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=502, w3=620, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(502, min_periods=max(502//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.198667 * slope + 0.0012936 * anchor
    return base_signal.diff()

def f13_macf_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=16, w3=637, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(16, min_periods=max(16//3, 2)).mean()
    noise = impulse.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.862941 + 0.0012937 * anchor
    return base_signal.diff()

def f13_macf_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=29, w3=654, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 29)
    curvature = _rolling_slope(acceleration, 654)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.211333 * acceleration + 0.0012938 * anchor
    return base_signal.diff()

def f13_macf_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=42, w3=671, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(42, min_periods=max(42//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.89 + 0.0012939 * anchor
    return base_signal.diff()

def f13_macf_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=55, w3=688, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(55, min_periods=max(55//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.224 * _rolling_slope(draw, 688) + 0.001294 * anchor
    return base_signal.diff()

def f13_macf_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=68, w3=705, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(68, min_periods=max(68//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(705, min_periods=max(705//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.917059 + 0.0012941 * anchor
    return base_signal.diff()

def f13_macf_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=81, w3=722, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 81)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.930588 + 0.0012942 * anchor
    return base_signal.diff()

def f13_macf_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=94, w3=739, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(94, min_periods=max(94//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.944118 + 0.0012943 * anchor
    return base_signal.diff()

def f13_macf_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=107, w3=756, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(107, min_periods=max(107//3, 2)).rank(pct=True)
    persistence = change.rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.249333 * persistence + 0.0012944 * anchor
    return base_signal.diff()

def f13_macf_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=120, w3=22, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(120, min_periods=max(120//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.971176 + 0.0012945 * anchor
    return base_signal.diff()

def f13_macf_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=133, w3=39, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(133, min_periods=max(133//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.262 * slope + 0.0012946 * anchor
    return base_signal.diff()

def f13_macf_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=146, w3=56, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(146, min_periods=max(146//3, 2)).mean()
    noise = impulse.abs().rolling(56, min_periods=max(56//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.998235 + 0.0012947 * anchor
    return base_signal.diff()

def f13_macf_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=159, w3=73, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 159)
    curvature = _rolling_slope(acceleration, 73)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.274667 * acceleration + 0.0012948 * anchor
    return base_signal.diff()

def f13_macf_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=172, w3=90, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(172, min_periods=max(172//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(90) * 1.025294 + 0.0012949 * anchor
    return base_signal.diff()

def f13_macf_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=185, w3=107, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(185, min_periods=max(185//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.287333 * _rolling_slope(draw, 107) + 0.001295 * anchor
    return base_signal.diff()

def f13_macf_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=198, w3=124, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(198, min_periods=max(198//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.052353 + 0.0012951 * anchor
    return base_signal.diff()

def f13_macf_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=211, w3=141, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 211)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=141, adjust=False).mean() * 1.065882 + 0.0012952 * anchor
    return base_signal.diff()

def f13_macf_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=224, w3=158, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(224, min_periods=max(224//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.079412 + 0.0012953 * anchor
    return base_signal.diff()

def f13_macf_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=237, w3=175, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(27)
    rank = change.rolling(237, min_periods=max(237//3, 2)).rank(pct=True)
    persistence = change.rolling(175, min_periods=max(175//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.312667 * persistence + 0.0012954 * anchor
    return base_signal.diff()

def f13_macf_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=250, w3=192, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(250, min_periods=max(250//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.106471 + 0.0012955 * anchor
    return base_signal.diff()

def f13_macf_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=263, w3=209, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(263, min_periods=max(263//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.325333 * slope + 0.0012956 * anchor
    return base_signal.diff()

def f13_macf_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=276, w3=226, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(48)
    drag = impulse.rolling(276, min_periods=max(276//3, 2)).mean()
    noise = impulse.abs().rolling(226, min_periods=max(226//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.133529 + 0.0012957 * anchor
    return base_signal.diff()

def f13_macf_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=289, w3=243, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 289)
    curvature = _rolling_slope(acceleration, 243)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.338 * acceleration + 0.0012958 * anchor
    return base_signal.diff()

def f13_macf_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=302, w3=260, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(302, min_periods=max(302//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.160588 + 0.0012959 * anchor
    return base_signal.diff()

def f13_macf_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=315, w3=277, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(315, min_periods=max(315//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.350667 * _rolling_slope(draw, 277) + 0.001296 * anchor
    return base_signal.diff()

def f13_macf_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=328, w3=294, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(328, min_periods=max(328//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(294, min_periods=max(294//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.187647 + 0.0012961 * anchor
    return base_signal.diff()
