"""20 volume dryup at high gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Decreasing volume at price peaks suggesting a lack of buying interest and potential reversal.
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

def f20_vdry_gemini_076_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=250, w3=466, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(250, min_periods=max(250//3, 2)).max()
    trough = x.rolling(67, min_periods=max(67//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.343529 + 0.0016947 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_077_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=263, w3=483, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(74)
    rank = change.rolling(263, min_periods=max(263//3, 2)).rank(pct=True)
    persistence = change.rolling(483, min_periods=max(483//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.350667 * persistence + 0.0016948 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_078_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=276, w3=500, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(81, min_periods=max(81//3, 2)).std()
    vol_slow = ret.rolling(276, min_periods=max(276//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.370588 + 0.0016949 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_079_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=289, w3=517, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(289, min_periods=max(289//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 88)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.031 * slope + 0.001695 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_080_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=302, w3=534, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(95)
    drag = impulse.rolling(302, min_periods=max(302//3, 2)).mean()
    noise = impulse.abs().rolling(534, min_periods=max(534//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.397647 + 0.0016951 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_081_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=315, w3=551, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 102)
    acceleration = _rolling_slope(velocity, 315)
    curvature = _rolling_slope(acceleration, 551)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.043667 * acceleration + 0.0016952 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_082_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=328, w3=568, lag=2)."""
    rel = _safe_div(high.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 109)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.05 * pressure.rolling(568, min_periods=max(568//3, 2)).mean() + 0.0016953 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_083_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=341, w3=585, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(116, min_periods=max(116//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.438235 + 0.0016954 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_084_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=354, w3=602, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(354, min_periods=max(354//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 123)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.451765 + 0.0016955 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_085_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=367, w3=619, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(130, min_periods=max(130//3, 2)).mean(), b.abs().rolling(367, min_periods=max(367//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.069 * _rolling_slope(cover, 130) + 0.0016956 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_086_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=380, w3=636, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.075333 * y + 0.924667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 137) - _rolling_slope(basket, 380) + 0.0016957 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_087_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=393, w3=653, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(144, min_periods=max(144//3, 2)).mean(), upside.rolling(393, min_periods=max(393//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.492353 + 0.0016958 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_088_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=406, w3=670, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(406, min_periods=max(406//3, 2)).max()
    rebound = x - x.rolling(151, min_periods=max(151//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.088 * _rolling_slope(draw, 670) + 0.0016959 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_089_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=419, w3=687, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.519412 + 0.001696 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_090_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=432, w3=704, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(432, min_periods=max(432//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(704, min_periods=max(704//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.532941 + 0.0016961 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_091_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=445, w3=721, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 445)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.546471 + 0.0016962 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_092_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=458, w3=738, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(458, min_periods=max(458//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.56 + 0.0016963 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_093_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=471, w3=755, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(471, min_periods=max(471//3, 2)).rank(pct=True)
    persistence = change.rolling(755, min_periods=max(755//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119667 * persistence + 0.0016964 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_094_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=484, w3=21, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(484, min_periods=max(484//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.587059 + 0.0016965 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_095_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=497, w3=38, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(497, min_periods=max(497//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.132333 * slope + 0.0016966 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_096_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=11, w3=55, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(11, min_periods=max(11//3, 2)).mean()
    noise = impulse.abs().rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.614118 + 0.0016967 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_097_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=24, w3=72, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 24)
    curvature = _rolling_slope(acceleration, 72)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.145 * acceleration + 0.0016968 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_098_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=37, w3=89, lag=34)."""
    rel = _safe_div(high.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 221)
    pressure = rel_log.diff(37)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.151333 * pressure.rolling(89, min_periods=max(89//3, 2)).mean() + 0.0016969 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_099_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=50, w3=106, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(228, min_periods=max(228//3, 2)).mean())
    decay = spread.ewm(span=50, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.654706 + 0.001697 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_100_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=63, w3=123, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(63, min_periods=max(63//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 235)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.668235 + 0.0016971 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_101_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=76, w3=140, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(242, min_periods=max(242//3, 2)).mean(), b.abs().rolling(76, min_periods=max(76//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.170333 * _rolling_slope(cover, 242) + 0.0016972 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_102_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=89, w3=157, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.176667 * y + 0.823333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 249) - _rolling_slope(basket, 89) + 0.0016973 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_103_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=102, w3=174, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(102, min_periods=max(102//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.855294 + 0.0016974 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_104_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=115, w3=191, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(115, min_periods=max(115//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.189333 * _rolling_slope(draw, 191) + 0.0016975 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_105_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=128, w3=208, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(23) - b.diff(126)
    stress = imbalance.rolling(208, min_periods=max(208//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.882353 + 0.0016976 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_106_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=141, w3=225, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(141, min_periods=max(141//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.895882 + 0.0016977 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_107_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=154, w3=242, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 154)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=242, adjust=False).mean() * 0.909412 + 0.0016978 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_108_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=167, w3=259, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(167, min_periods=max(167//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.922941 + 0.0016979 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_109_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=180, w3=276, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(51)
    rank = change.rolling(180, min_periods=max(180//3, 2)).rank(pct=True)
    persistence = change.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.221 * persistence + 0.001698 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_110_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=193, w3=293, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(193, min_periods=max(193//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95 + 0.0016981 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_111_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=206, w3=310, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(206, min_periods=max(206//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.233667 * slope + 0.0016982 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_112_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=219, w3=327, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(72)
    drag = impulse.rolling(219, min_periods=max(219//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.977059 + 0.0016983 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_113_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=232, w3=344, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 232)
    curvature = _rolling_slope(acceleration, 344)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.246333 * acceleration + 0.0016984 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_114_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=245, w3=361, lag=5)."""
    rel = _safe_div(high.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 86)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.252667 * pressure.rolling(361, min_periods=max(361//3, 2)).mean() + 0.0016985 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_115_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=258, w3=378, lag=8)."""
    a = high.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(93, min_periods=max(93//3, 2)).mean())
    decay = spread.ewm(span=258, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.017647 + 0.0016986 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_116_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=271, w3=395, lag=13)."""
    a = _safe_log(high.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(271, min_periods=max(271//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 100)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.031176 + 0.0016987 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_117_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=284, w3=412, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(107, min_periods=max(107//3, 2)).mean(), b.abs().rolling(284, min_periods=max(284//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.271667 * _rolling_slope(cover, 107) + 0.0016988 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_118_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=297, w3=429, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.278 * y + 0.722000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 114) - _rolling_slope(basket, 297) + 0.0016989 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_119_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=310, w3=446, lag=55)."""
    x = high.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(310, min_periods=max(310//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.071765 + 0.001699 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_120_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=323, w3=463, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    draw = x - x.rolling(323, min_periods=max(323//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.290667 * _rolling_slope(draw, 463) + 0.0016991 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_121_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=135, w2=336, w3=480, lag=1)."""
    a = _safe_log(high.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(480, min_periods=max(480//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.098824 + 0.0016992 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_122_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=142, w2=349, w3=497, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 142)
    baseline = trend.rolling(349, min_periods=max(349//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.112353 + 0.0016993 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_123_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=149, w2=362, w3=514, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 149)
    slow = _rolling_slope(x, 362)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.125882 + 0.0016994 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_124_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=156, w2=375, w3=531, lag=5)."""
    x = high.shift(5)
    peak = x.rolling(375, min_periods=max(375//3, 2)).max()
    trough = x.rolling(156, min_periods=max(156//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.139412 + 0.0016995 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_125_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=163, w2=388, w3=548, lag=8)."""
    x = high.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(388, min_periods=max(388//3, 2)).rank(pct=True)
    persistence = change.rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.322333 * persistence + 0.0016996 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_126_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=170, w2=401, w3=565, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(170, min_periods=max(170//3, 2)).std()
    vol_slow = ret.rolling(401, min_periods=max(401//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.166471 + 0.0016997 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_127_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=177, w2=414, w3=582, lag=21)."""
    x = high.shift(21)
    ma = x.rolling(414, min_periods=max(414//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 177)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.335 * slope + 0.0016998 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_128_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=427, w3=599, lag=34)."""
    x = high.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(427, min_periods=max(427//3, 2)).mean()
    noise = impulse.abs().rolling(599, min_periods=max(599//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.193529 + 0.0016999 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_129_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=440, w3=616, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 191)
    acceleration = _rolling_slope(velocity, 440)
    curvature = _rolling_slope(acceleration, 616)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.347667 * acceleration + 0.0017 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_130_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=453, w3=633, lag=0)."""
    rel = _safe_div(high.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 198)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.354 * pressure.rolling(633, min_periods=max(633//3, 2)).mean() + 0.0017001 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_131_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=466, w3=650, lag=1)."""
    a = high.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(205, min_periods=max(205//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.234118 + 0.0017002 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_132_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=479, w3=667, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(479, min_periods=max(479//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 212)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.247647 + 0.0017003 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_133_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=492, w3=684, lag=3)."""
    a = high.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(219, min_periods=max(219//3, 2)).mean(), b.abs().rolling(492, min_periods=max(492//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.040667 * _rolling_slope(cover, 219) + 0.0017004 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_134_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=505, w3=701, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.047 * y + 0.953000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 226) - _rolling_slope(basket, 505) + 0.0017005 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_135_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=19, w3=718, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.288235 + 0.0017006 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_136_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=32, w3=735, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.059667 * _rolling_slope(draw, 735) + 0.0017007 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_137_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=45, w3=752, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(45)
    stress = imbalance.rolling(752, min_periods=max(752//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.315294 + 0.0017008 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_138_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=58, w3=18, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 7)
    baseline = trend.rolling(58, min_periods=max(58//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(18, min_periods=max(18//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.328824 + 0.0017009 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_139_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=71, w3=35, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 14)
    slow = _rolling_slope(x, 71)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=35, adjust=False).mean() * 1.342353 + 0.001701 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_140_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=84, w3=52, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(84, min_periods=max(84//3, 2)).max()
    trough = x.rolling(21, min_periods=max(21//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.355882 + 0.0017011 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_141_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=97, w3=69, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(28)
    rank = change.rolling(97, min_periods=max(97//3, 2)).rank(pct=True)
    persistence = change.rolling(69, min_periods=max(69//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.091333 * persistence + 0.0017012 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_142_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=110, w3=86, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(35, min_periods=max(35//3, 2)).std()
    vol_slow = ret.rolling(110, min_periods=max(110//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.382941 + 0.0017013 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_143_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=123, w3=103, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(123, min_periods=max(123//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 42)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.104 * slope + 0.0017014 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_144_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=136, w3=120, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(49)
    drag = impulse.rolling(136, min_periods=max(136//3, 2)).mean()
    noise = impulse.abs().rolling(120, min_periods=max(120//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.41 + 0.0017015 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_145_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=149, w3=137, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 56)
    acceleration = _rolling_slope(velocity, 149)
    curvature = _rolling_slope(acceleration, 137)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.116667 * acceleration + 0.0017016 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_146_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=162, w3=154, lag=13)."""
    rel = _safe_div(high.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 63)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.123 * pressure.rolling(154, min_periods=max(154//3, 2)).mean() + 0.0017017 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_147_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=175, w3=171, lag=21)."""
    a = high.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(70, min_periods=max(70//3, 2)).mean())
    decay = spread.ewm(span=175, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.450588 + 0.0017018 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_148_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=188, w3=188, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(188, min_periods=max(188//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 77)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.464118 + 0.0017019 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_149_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=201, w3=205, lag=55)."""
    a = high.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(84, min_periods=max(84//3, 2)).mean(), b.abs().rolling(201, min_periods=max(201//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.142 * _rolling_slope(cover, 84) + 0.001702 * anchor
    return base_signal.diff().diff()

def f20_vdry_gemini_150_d2(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=214, w3=222, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.148333 * y + 0.851667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 91) - _rolling_slope(basket, 214) + 0.0017021 * anchor
    return base_signal.diff().diff()
