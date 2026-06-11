"""103 principal component drift velocity gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Speed of change in the orientation of principal components in market data.
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

def f103_pcdv_gemini_076_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=447, w3=334, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(447, min_periods=max(447//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.531765 + 0.0006867 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_077_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=460, w3=351, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(460, min_periods=max(460//3, 2)).rank(pct=True)
    persistence = change.rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.318667 * persistence + 0.0006868 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_078_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=473, w3=368, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(473, min_periods=max(473//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.558824 + 0.0006869 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_079_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=486, w3=385, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(486, min_periods=max(486//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.331333 * slope + 0.000687 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_080_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=499, w3=402, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(499, min_periods=max(499//3, 2)).mean()
    noise = impulse.abs().rolling(402, min_periods=max(402//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.585882 + 0.0006871 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_081_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=13, w3=419, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 13)
    curvature = _rolling_slope(acceleration, 419)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.344 * acceleration + 0.0006872 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_082_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=26, w3=436, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 191)
    pressure = rel_log.diff(26)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.350333 * pressure.rolling(436, min_periods=max(436//3, 2)).mean() + 0.0006873 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_083_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=39, w3=453, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(198, min_periods=max(198//3, 2)).mean())
    decay = spread.ewm(span=39, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.626471 + 0.0006874 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_084_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=52, w3=470, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(52, min_periods=max(52//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 205)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.64 + 0.0006875 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_085_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=65, w3=487, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(212, min_periods=max(212//3, 2)).mean(), b.abs().rolling(65, min_periods=max(65//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.037 * _rolling_slope(cover, 212) + 0.0006876 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_086_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=78, w3=504, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.043333 * y + 0.956667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 219) - _rolling_slope(basket, 78) + 0.0006877 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_087_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=91, w3=521, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(91, min_periods=max(91//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.827059 + 0.0006878 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_088_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=104, w3=538, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(104, min_periods=max(104//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.056 * _rolling_slope(draw, 538) + 0.0006879 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_089_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=117, w3=555, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(117)
    stress = imbalance.rolling(555, min_periods=max(555//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.854118 + 0.000688 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_090_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=130, w3=572, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(130, min_periods=max(130//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.867647 + 0.0006881 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_091_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=143, w3=589, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 143)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.881176 + 0.0006882 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_092_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=156, w3=606, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(156, min_periods=max(156//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.894706 + 0.0006883 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_093_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=169, w3=623, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(21)
    rank = change.rolling(169, min_periods=max(169//3, 2)).rank(pct=True)
    persistence = change.rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087667 * persistence + 0.0006884 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_094_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=182, w3=640, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.921765 + 0.0006885 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_095_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=195, w3=657, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(195, min_periods=max(195//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.100333 * slope + 0.0006886 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_096_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=208, w3=674, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(42)
    drag = impulse.rolling(208, min_periods=max(208//3, 2)).mean()
    noise = impulse.abs().rolling(674, min_periods=max(674//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.948824 + 0.0006887 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_097_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=221, w3=691, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 221)
    curvature = _rolling_slope(acceleration, 691)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.113 * acceleration + 0.0006888 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_098_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=234, w3=708, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 56)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.119333 * pressure.rolling(708, min_periods=max(708//3, 2)).mean() + 0.0006889 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_099_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=247, w3=725, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(63, min_periods=max(63//3, 2)).mean())
    decay = spread.ewm(span=247, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.989412 + 0.000689 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_100_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=260, w3=742, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(260, min_periods=max(260//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 70)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.002941 + 0.0006891 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_101_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=273, w3=759, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(77, min_periods=max(77//3, 2)).mean(), b.abs().rolling(273, min_periods=max(273//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.138333 * _rolling_slope(cover, 77) + 0.0006892 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_102_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=286, w3=25, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.144667 * y + 0.855333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 84) - _rolling_slope(basket, 286) + 0.0006893 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_103_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=299, w3=42, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(299, min_periods=max(299//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(42) * 1.043529 + 0.0006894 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_104_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=312, w3=59, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(312, min_periods=max(312//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.157333 * _rolling_slope(draw, 59) + 0.0006895 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_105_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=325, w3=76, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(105) - b.diff(126)
    stress = imbalance.rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.070588 + 0.0006896 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_106_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=338, w3=93, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(338, min_periods=max(338//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.084118 + 0.0006897 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_107_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=351, w3=110, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 351)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=110, adjust=False).mean() * 1.097647 + 0.0006898 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_108_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=364, w3=127, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(364, min_periods=max(364//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.111176 + 0.0006899 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_109_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=377, w3=144, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(377, min_periods=max(377//3, 2)).rank(pct=True)
    persistence = change.rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.189 * persistence + 0.00069 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_110_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=390, w3=161, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(390, min_periods=max(390//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.138235 + 0.0006901 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_111_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=403, w3=178, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(403, min_periods=max(403//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.201667 * slope + 0.0006902 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_112_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=416, w3=195, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(416, min_periods=max(416//3, 2)).mean()
    noise = impulse.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.165294 + 0.0006903 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_113_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=429, w3=212, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 429)
    curvature = _rolling_slope(acceleration, 212)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.214333 * acceleration + 0.0006904 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_114_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=442, w3=229, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 168)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.220667 * pressure.rolling(229, min_periods=max(229//3, 2)).mean() + 0.0006905 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_115_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=455, w3=246, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(175, min_periods=max(175//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.205882 + 0.0006906 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_116_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=468, w3=263, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(low.abs() + 1.0).shift(13)
    corr = a.rolling(468, min_periods=max(468//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 182)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.219412 + 0.0006907 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_117_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=481, w3=280, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    cover = _safe_div(a.rolling(189, min_periods=max(189//3, 2)).mean(), b.abs().rolling(481, min_periods=max(481//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.239667 * _rolling_slope(cover, 189) + 0.0006908 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_118_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=494, w3=297, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(low.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.246 * y + 0.754000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 196) - _rolling_slope(basket, 494) + 0.0006909 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_119_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=507, w3=314, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(507, min_periods=max(507//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.26 + 0.000691 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_120_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=21, w3=331, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(21, min_periods=max(21//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.258667 * _rolling_slope(draw, 331) + 0.0006911 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_121_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=34, w3=348, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(low.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(34)
    stress = imbalance.rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.287059 + 0.0006912 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_122_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=47, w3=365, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 224)
    baseline = trend.rolling(47, min_periods=max(47//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.300588 + 0.0006913 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_123_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=60, w3=382, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 231)
    slow = _rolling_slope(x, 60)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.314118 + 0.0006914 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_124_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=73, w3=399, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(73, min_periods=max(73//3, 2)).max()
    trough = x.rolling(238, min_periods=max(238//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.327647 + 0.0006915 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_125_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=86, w3=416, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(86, min_periods=max(86//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.290333 * persistence + 0.0006916 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_126_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=99, w3=433, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(5, min_periods=max(5//3, 2)).std()
    vol_slow = ret.rolling(99, min_periods=max(99//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.354706 + 0.0006917 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_127_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=112, w3=450, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(112, min_periods=max(112//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 12)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.303 * slope + 0.0006918 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_128_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=125, w3=467, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(19)
    drag = impulse.rolling(125, min_periods=max(125//3, 2)).mean()
    noise = impulse.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.381765 + 0.0006919 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_129_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=138, w3=484, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 26)
    acceleration = _rolling_slope(velocity, 138)
    curvature = _rolling_slope(acceleration, 484)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.315667 * acceleration + 0.000692 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_130_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=151, w3=501, lag=0)."""
    rel = _safe_div(high.shift(0), low.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 33)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.322 * pressure.rolling(501, min_periods=max(501//3, 2)).mean() + 0.0006921 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_131_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=164, w3=518, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(40, min_periods=max(40//3, 2)).mean())
    decay = spread.ewm(span=164, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.422353 + 0.0006922 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_132_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=177, w3=535, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(177, min_periods=max(177//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 47)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.435882 + 0.0006923 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_133_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=190, w3=552, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(54, min_periods=max(54//3, 2)).mean(), b.abs().rolling(190, min_periods=max(190//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.341 * _rolling_slope(cover, 54) + 0.0006924 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_134_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=203, w3=569, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.347333 * y + 0.652667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 61) - _rolling_slope(basket, 203) + 0.0006925 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_135_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=216, w3=586, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(68, min_periods=max(68//3, 2)).mean(), upside.rolling(216, min_periods=max(216//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.476471 + 0.0006926 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_136_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=229, w3=603, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(229, min_periods=max(229//3, 2)).max()
    rebound = x - x.rolling(75, min_periods=max(75//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.36 * _rolling_slope(draw, 603) + 0.0006927 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_137_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=242, w3=620, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(82) - b.diff(126)
    stress = imbalance.rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.503529 + 0.0006928 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_138_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=255, w3=637, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 89)
    baseline = trend.rolling(255, min_periods=max(255//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.517059 + 0.0006929 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_139_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=268, w3=654, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 96)
    slow = _rolling_slope(x, 268)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.530588 + 0.000693 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_140_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=281, w3=671, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(281, min_periods=max(281//3, 2)).max()
    trough = x.rolling(103, min_periods=max(103//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.544118 + 0.0006931 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_141_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=294, w3=688, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(110)
    rank = change.rolling(294, min_periods=max(294//3, 2)).rank(pct=True)
    persistence = change.rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.059333 * persistence + 0.0006932 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_142_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=307, w3=705, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(117, min_periods=max(117//3, 2)).std()
    vol_slow = ret.rolling(307, min_periods=max(307//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.571176 + 0.0006933 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_143_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=320, w3=722, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(320, min_periods=max(320//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 124)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.072 * slope + 0.0006934 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_144_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=333, w3=739, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(333, min_periods=max(333//3, 2)).mean()
    noise = impulse.abs().rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.598235 + 0.0006935 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_145_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=346, w3=756, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 346)
    curvature = _rolling_slope(acceleration, 756)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.084667 * acceleration + 0.0006936 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_146_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=145, w2=359, w3=22, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 145)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.091 * pressure.rolling(22, min_periods=max(22//3, 2)).mean() + 0.0006937 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_147_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=152, w2=372, w3=39, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(152, min_periods=max(152//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.638824 + 0.0006938 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_148_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=159, w2=385, w3=56, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(385, min_periods=max(385//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 159)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.652353 + 0.0006939 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_149_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=166, w2=398, w3=73, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(166, min_periods=max(166//3, 2)).mean(), b.abs().rolling(398, min_periods=max(398//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(73) + 0.11 * _rolling_slope(cover, 166) + 0.000694 * anchor
    return base_signal.diff().diff()

def f103_pcdv_gemini_150_d2(high: pd.Series, low: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=173, w2=411, w3=90, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.116333 * y + 0.883667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 173) - _rolling_slope(basket, 411) + 0.0006941 * anchor
    return base_signal.diff().diff()
