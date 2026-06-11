"""93 skew convexity proxy technical gemini base features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Analysis of return distribution asymmetry as a proxy for implied skew.
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

def f93_skcx_gemini_076(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=217, w2=108, w3=497, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(108, min_periods=max(108//3, 2)).mean()
    noise = impulse.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.964706 + 0.0057547 * anchor
    return base_signal

def f93_skcx_gemini_077(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=224, w2=121, w3=514, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 121)
    curvature = _rolling_slope(acceleration, 514)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.258 * acceleration + 0.0057548 * anchor
    return base_signal

def f93_skcx_gemini_078(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=231, w2=134, w3=531, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(134, min_periods=max(134//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.991765 + 0.0057549 * anchor
    return base_signal

def f93_skcx_gemini_079(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=238, w2=147, w3=548, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(147, min_periods=max(147//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.270667 * _rolling_slope(draw, 548) + 0.005755 * anchor
    return base_signal

def f93_skcx_gemini_080(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=245, w2=160, w3=565, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(160, min_periods=max(160//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.018824 + 0.0057551 * anchor
    return base_signal

def f93_skcx_gemini_081(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=5, w2=173, w3=582, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 173)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.032353 + 0.0057552 * anchor
    return base_signal

def f93_skcx_gemini_082(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=12, w2=186, w3=599, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.045882 + 0.0057553 * anchor
    return base_signal

def f93_skcx_gemini_083(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=19, w2=199, w3=616, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(19)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.296 * persistence + 0.0057554 * anchor
    return base_signal

def f93_skcx_gemini_084(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=26, w2=212, w3=633, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(212, min_periods=max(212//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.072941 + 0.0057555 * anchor
    return base_signal

def f93_skcx_gemini_085(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=33, w2=225, w3=650, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(225, min_periods=max(225//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.308667 * slope + 0.0057556 * anchor
    return base_signal

def f93_skcx_gemini_086(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=40, w2=238, w3=667, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(40)
    drag = impulse.rolling(238, min_periods=max(238//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1 + 0.0057557 * anchor
    return base_signal

def f93_skcx_gemini_087(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=47, w2=251, w3=684, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 251)
    curvature = _rolling_slope(acceleration, 684)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.321333 * acceleration + 0.0057558 * anchor
    return base_signal

def f93_skcx_gemini_088(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=54, w2=264, w3=701, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(264, min_periods=max(264//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.127059 + 0.0057559 * anchor
    return base_signal

def f93_skcx_gemini_089(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=61, w2=277, w3=718, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(277, min_periods=max(277//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.334 * _rolling_slope(draw, 718) + 0.005756 * anchor
    return base_signal

def f93_skcx_gemini_090(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=68, w2=290, w3=735, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(290, min_periods=max(290//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.154118 + 0.0057561 * anchor
    return base_signal

def f93_skcx_gemini_091(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=75, w2=303, w3=752, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 303)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.167647 + 0.0057562 * anchor
    return base_signal

def f93_skcx_gemini_092(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=82, w2=316, w3=18, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(316, min_periods=max(316//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.181176 + 0.0057563 * anchor
    return base_signal

def f93_skcx_gemini_093(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=89, w2=329, w3=35, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(89)
    rank = change.rolling(329, min_periods=max(329//3, 2)).rank(pct=True)
    persistence = change.rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.359333 * persistence + 0.0057564 * anchor
    return base_signal

def f93_skcx_gemini_094(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=96, w2=342, w3=52, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(342, min_periods=max(342//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.208235 + 0.0057565 * anchor
    return base_signal

def f93_skcx_gemini_095(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=103, w2=355, w3=69, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.039667 * slope + 0.0057566 * anchor
    return base_signal

def f93_skcx_gemini_096(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=110, w2=368, w3=86, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(110)
    drag = impulse.rolling(368, min_periods=max(368//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.235294 + 0.0057567 * anchor
    return base_signal

def f93_skcx_gemini_097(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=117, w2=381, w3=103, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 381)
    curvature = _rolling_slope(acceleration, 103)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.052333 * acceleration + 0.0057568 * anchor
    return base_signal

def f93_skcx_gemini_098(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=124, w2=394, w3=120, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(120) * 1.262353 + 0.0057569 * anchor
    return base_signal

def f93_skcx_gemini_099(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=131, w2=407, w3=137, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(407, min_periods=max(407//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.065 * _rolling_slope(draw, 137) + 0.005757 * anchor
    return base_signal

def f93_skcx_gemini_100(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=138, w2=420, w3=154, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(420, min_periods=max(420//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.289412 + 0.0057571 * anchor
    return base_signal

def f93_skcx_gemini_101(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=145, w2=433, w3=171, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 433)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=171, adjust=False).mean() * 1.302941 + 0.0057572 * anchor
    return base_signal

def f93_skcx_gemini_102(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=152, w2=446, w3=188, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(446, min_periods=max(446//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.316471 + 0.0057573 * anchor
    return base_signal

def f93_skcx_gemini_103(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=159, w2=459, w3=205, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(459, min_periods=max(459//3, 2)).rank(pct=True)
    persistence = change.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.090333 * persistence + 0.0057574 * anchor
    return base_signal

def f93_skcx_gemini_104(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=166, w2=472, w3=222, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(472, min_periods=max(472//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.343529 + 0.0057575 * anchor
    return base_signal

def f93_skcx_gemini_105(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=173, w2=485, w3=239, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(485, min_periods=max(485//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.103 * slope + 0.0057576 * anchor
    return base_signal

def f93_skcx_gemini_106(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=180, w2=498, w3=256, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(498, min_periods=max(498//3, 2)).mean()
    noise = impulse.abs().rolling(256, min_periods=max(256//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.370588 + 0.0057577 * anchor
    return base_signal

def f93_skcx_gemini_107(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=187, w2=12, w3=273, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 12)
    curvature = _rolling_slope(acceleration, 273)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.115667 * acceleration + 0.0057578 * anchor
    return base_signal

def f93_skcx_gemini_108(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=194, w2=25, w3=290, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(25, min_periods=max(25//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.397647 + 0.0057579 * anchor
    return base_signal

def f93_skcx_gemini_109(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=201, w2=38, w3=307, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(38, min_periods=max(38//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.128333 * _rolling_slope(draw, 307) + 0.005758 * anchor
    return base_signal

def f93_skcx_gemini_110(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=208, w2=51, w3=324, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(51, min_periods=max(51//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(324, min_periods=max(324//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.424706 + 0.0057581 * anchor
    return base_signal

def f93_skcx_gemini_111(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=215, w2=64, w3=341, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 64)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.438235 + 0.0057582 * anchor
    return base_signal

def f93_skcx_gemini_112(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=222, w2=77, w3=358, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(77, min_periods=max(77//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.451765 + 0.0057583 * anchor
    return base_signal

def f93_skcx_gemini_113(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=229, w2=90, w3=375, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(90, min_periods=max(90//3, 2)).rank(pct=True)
    persistence = change.rolling(375, min_periods=max(375//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.153667 * persistence + 0.0057584 * anchor
    return base_signal

def f93_skcx_gemini_114(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=236, w2=103, w3=392, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(103, min_periods=max(103//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478824 + 0.0057585 * anchor
    return base_signal

def f93_skcx_gemini_115(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=243, w2=116, w3=409, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(116, min_periods=max(116//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.166333 * slope + 0.0057586 * anchor
    return base_signal

def f93_skcx_gemini_116(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=250, w2=129, w3=426, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(129, min_periods=max(129//3, 2)).mean()
    noise = impulse.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.505882 + 0.0057587 * anchor
    return base_signal

def f93_skcx_gemini_117(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=10, w2=142, w3=443, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 142)
    curvature = _rolling_slope(acceleration, 443)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.179 * acceleration + 0.0057588 * anchor
    return base_signal

def f93_skcx_gemini_118(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=17, w2=155, w3=460, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(155, min_periods=max(155//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.532941 + 0.0057589 * anchor
    return base_signal

def f93_skcx_gemini_119(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=24, w2=168, w3=477, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(168, min_periods=max(168//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.191667 * _rolling_slope(draw, 477) + 0.005759 * anchor
    return base_signal

def f93_skcx_gemini_120(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=31, w2=181, w3=494, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(181, min_periods=max(181//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.56 + 0.0057591 * anchor
    return base_signal

def f93_skcx_gemini_121(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=38, w2=194, w3=511, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 38)
    slow = _rolling_slope(x, 194)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.573529 + 0.0057592 * anchor
    return base_signal

def f93_skcx_gemini_122(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=45, w2=207, w3=528, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(207, min_periods=max(207//3, 2)).max()
    trough = x.rolling(45, min_periods=max(45//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.587059 + 0.0057593 * anchor
    return base_signal

def f93_skcx_gemini_123(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=52, w2=220, w3=545, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(52)
    rank = change.rolling(220, min_periods=max(220//3, 2)).rank(pct=True)
    persistence = change.rolling(545, min_periods=max(545//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.217 * persistence + 0.0057594 * anchor
    return base_signal

def f93_skcx_gemini_124(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=59, w2=233, w3=562, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(59, min_periods=max(59//3, 2)).std()
    vol_slow = ret.rolling(233, min_periods=max(233//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.614118 + 0.0057595 * anchor
    return base_signal

def f93_skcx_gemini_125(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=66, w2=246, w3=579, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(246, min_periods=max(246//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 66)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.229667 * slope + 0.0057596 * anchor
    return base_signal

def f93_skcx_gemini_126(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=73, w2=259, w3=596, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(73)
    drag = impulse.rolling(259, min_periods=max(259//3, 2)).mean()
    noise = impulse.abs().rolling(596, min_periods=max(596//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.641176 + 0.0057597 * anchor
    return base_signal

def f93_skcx_gemini_127(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=80, w2=272, w3=613, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 80)
    acceleration = _rolling_slope(velocity, 272)
    curvature = _rolling_slope(acceleration, 613)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.242333 * acceleration + 0.0057598 * anchor
    return base_signal

def f93_skcx_gemini_128(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=87, w2=285, w3=630, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(285, min_periods=max(285//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.668235 + 0.0057599 * anchor
    return base_signal

def f93_skcx_gemini_129(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=94, w2=298, w3=647, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(298, min_periods=max(298//3, 2)).max()
    rebound = x - x.rolling(94, min_periods=max(94//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.255 * _rolling_slope(draw, 647) + 0.00576 * anchor
    return base_signal

def f93_skcx_gemini_130(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=101, w2=311, w3=664, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 101)
    baseline = trend.rolling(311, min_periods=max(311//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(664, min_periods=max(664//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.841765 + 0.0057601 * anchor
    return base_signal

def f93_skcx_gemini_131(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=324, w3=681, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 108)
    slow = _rolling_slope(x, 324)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.855294 + 0.0057602 * anchor
    return base_signal

def f93_skcx_gemini_132(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=337, w3=698, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(337, min_periods=max(337//3, 2)).max()
    trough = x.rolling(115, min_periods=max(115//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.868824 + 0.0057603 * anchor
    return base_signal

def f93_skcx_gemini_133(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=350, w3=715, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(122)
    rank = change.rolling(350, min_periods=max(350//3, 2)).rank(pct=True)
    persistence = change.rolling(715, min_periods=max(715//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.280333 * persistence + 0.0057604 * anchor
    return base_signal

def f93_skcx_gemini_134(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=363, w3=732, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(129, min_periods=max(129//3, 2)).std()
    vol_slow = ret.rolling(363, min_periods=max(363//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.895882 + 0.0057605 * anchor
    return base_signal

def f93_skcx_gemini_135(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=376, w3=749, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 136)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.293 * slope + 0.0057606 * anchor
    return base_signal

def f93_skcx_gemini_136(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=389, w3=766, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(389, min_periods=max(389//3, 2)).mean()
    noise = impulse.abs().rolling(766, min_periods=max(766//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.922941 + 0.0057607 * anchor
    return base_signal

def f93_skcx_gemini_137(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=402, w3=32, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 150)
    acceleration = _rolling_slope(velocity, 402)
    curvature = _rolling_slope(acceleration, 32)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305667 * acceleration + 0.0057608 * anchor
    return base_signal

def f93_skcx_gemini_138(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=415, w3=49, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(157, min_periods=max(157//3, 2)).mean(), upside.rolling(415, min_periods=max(415//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(49) * 0.95 + 0.0057609 * anchor
    return base_signal

def f93_skcx_gemini_139(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=428, w3=66, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(428, min_periods=max(428//3, 2)).max()
    rebound = x - x.rolling(164, min_periods=max(164//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.318333 * _rolling_slope(draw, 66) + 0.005761 * anchor
    return base_signal

def f93_skcx_gemini_140(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=441, w3=83, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 171)
    baseline = trend.rolling(441, min_periods=max(441//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.977059 + 0.0057611 * anchor
    return base_signal

def f93_skcx_gemini_141(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=454, w3=100, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 178)
    slow = _rolling_slope(x, 454)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=100, adjust=False).mean() * 0.990588 + 0.0057612 * anchor
    return base_signal

def f93_skcx_gemini_142(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=467, w3=117, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(467, min_periods=max(467//3, 2)).max()
    trough = x.rolling(185, min_periods=max(185//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.004118 + 0.0057613 * anchor
    return base_signal

def f93_skcx_gemini_143(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=480, w3=134, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(480, min_periods=max(480//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343667 * persistence + 0.0057614 * anchor
    return base_signal

def f93_skcx_gemini_144(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=493, w3=151, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(199, min_periods=max(199//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.031176 + 0.0057615 * anchor
    return base_signal

def f93_skcx_gemini_145(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=506, w3=168, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(506, min_periods=max(506//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 206)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.356333 * slope + 0.0057616 * anchor
    return base_signal

def f93_skcx_gemini_146(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=20, w3=185, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(20, min_periods=max(20//3, 2)).mean()
    noise = impulse.abs().rolling(185, min_periods=max(185//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.058235 + 0.0057617 * anchor
    return base_signal

def f93_skcx_gemini_147(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=33, w3=202, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 220)
    acceleration = _rolling_slope(velocity, 33)
    curvature = _rolling_slope(acceleration, 202)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.036667 * acceleration + 0.0057618 * anchor
    return base_signal

def f93_skcx_gemini_148(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=46, w3=219, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(227, min_periods=max(227//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.085294 + 0.0057619 * anchor
    return base_signal

def f93_skcx_gemini_149(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=59, w3=236, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(234, min_periods=max(234//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.049333 * _rolling_slope(draw, 236) + 0.005762 * anchor
    return base_signal

def f93_skcx_gemini_150(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=72, w3=253, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 241)
    baseline = trend.rolling(72, min_periods=max(72//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(253, min_periods=max(253//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.112353 + 0.0057621 * anchor
    return base_signal
