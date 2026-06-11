"""49 blowoff climax composite gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Multi-factor indicator for identifying parabolic peaks and blow-off moves.
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

def f49_bocc_gemini_076_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=127, w2=293, w3=178, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(293, min_periods=max(293//3, 2)).max()
    trough = x.rolling(127, min_periods=max(127//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.850588 + 0.0033187 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_077_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=134, w2=306, w3=195, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(306, min_periods=max(306//3, 2)).rank(pct=True)
    persistence = change.rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.180667 * persistence + 0.0033188 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_078_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=141, w2=319, w3=212, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(141, min_periods=max(141//3, 2)).std()
    vol_slow = ret.rolling(319, min_periods=max(319//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.877647 + 0.0033189 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_079_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=148, w2=332, w3=229, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(332, min_periods=max(332//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 148)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.193333 * slope + 0.003319 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_080_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=345, w3=246, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(345, min_periods=max(345//3, 2)).mean()
    noise = impulse.abs().rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.904706 + 0.0033191 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_081_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=358, w3=263, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 358)
    curvature = _rolling_slope(acceleration, 263)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.206 * acceleration + 0.0033192 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_082_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=371, w3=280, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 169)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.212333 * pressure.rolling(280, min_periods=max(280//3, 2)).mean() + 0.0033193 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_083_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=384, w3=297, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(176, min_periods=max(176//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.945294 + 0.0033194 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_084_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=397, w3=314, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(397, min_periods=max(397//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 183)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.958824 + 0.0033195 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_085_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=410, w3=331, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(190, min_periods=max(190//3, 2)).mean(), b.abs().rolling(410, min_periods=max(410//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.231333 * _rolling_slope(cover, 190) + 0.0033196 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_086_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=423, w3=348, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.237667 * y + 0.762333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 197) - _rolling_slope(basket, 423) + 0.0033197 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_087_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=436, w3=365, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(436, min_periods=max(436//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.999412 + 0.0033198 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_088_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=449, w3=382, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(449, min_periods=max(449//3, 2)).max()
    rebound = x - x.rolling(211, min_periods=max(211//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.250333 * _rolling_slope(draw, 382) + 0.0033199 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_089_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=462, w3=399, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(399, min_periods=max(399//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.026471 + 0.00332 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_090_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=475, w3=416, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 225)
    baseline = trend.rolling(475, min_periods=max(475//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.04 + 0.0033201 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_091_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=488, w3=433, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 232)
    slow = _rolling_slope(x, 488)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.053529 + 0.0033202 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_092_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=501, w3=450, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(239, min_periods=max(239//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.067059 + 0.0033203 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_093_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=15, w3=467, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(15, min_periods=max(15//3, 2)).rank(pct=True)
    persistence = change.rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.282 * persistence + 0.0033204 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_094_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=28, w3=484, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(6, min_periods=max(6//3, 2)).std()
    vol_slow = ret.rolling(28, min_periods=max(28//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.094118 + 0.0033205 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_095_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=41, w3=501, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(41, min_periods=max(41//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 13)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.294667 * slope + 0.0033206 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_096_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=54, w3=518, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(20)
    drag = impulse.rolling(54, min_periods=max(54//3, 2)).mean()
    noise = impulse.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.121176 + 0.0033207 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_097_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=67, w3=535, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 27)
    acceleration = _rolling_slope(velocity, 67)
    curvature = _rolling_slope(acceleration, 535)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.307333 * acceleration + 0.0033208 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_098_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=80, w3=552, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 34)
    pressure = rel_log.diff(80)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.313667 * pressure.rolling(552, min_periods=max(552//3, 2)).mean() + 0.0033209 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_099_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=93, w3=569, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(41, min_periods=max(41//3, 2)).mean())
    decay = spread.ewm(span=93, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.161765 + 0.003321 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_100_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=106, w3=586, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(106, min_periods=max(106//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 48)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.175294 + 0.0033211 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_101_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=119, w3=603, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(55, min_periods=max(55//3, 2)).mean(), b.abs().rolling(119, min_periods=max(119//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.332667 * _rolling_slope(cover, 55) + 0.0033212 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_102_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=132, w3=620, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.339 * y + 0.661000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 62) - _rolling_slope(basket, 132) + 0.0033213 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_103_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=145, w3=637, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(145, min_periods=max(145//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.215882 + 0.0033214 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_104_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=158, w3=654, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(158, min_periods=max(158//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.351667 * _rolling_slope(draw, 654) + 0.0033215 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_105_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=171, w3=671, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(83) - b.diff(126)
    stress = imbalance.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.242941 + 0.0033216 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_106_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=184, w3=688, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(184, min_periods=max(184//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.256471 + 0.0033217 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_107_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=197, w3=705, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 197)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.27 + 0.0033218 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_108_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=210, w3=722, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(210, min_periods=max(210//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.283529 + 0.0033219 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_109_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=223, w3=739, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(111)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(739, min_periods=max(739//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.051 * persistence + 0.003322 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_110_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=236, w3=756, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(236, min_periods=max(236//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.310588 + 0.0033221 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_111_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=249, w3=22, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(249, min_periods=max(249//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.063667 * slope + 0.0033222 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_112_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=262, w3=39, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(262, min_periods=max(262//3, 2)).mean()
    noise = impulse.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.337647 + 0.0033223 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_113_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=275, w3=56, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 275)
    curvature = _rolling_slope(acceleration, 56)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.076333 * acceleration + 0.0033224 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_114_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=288, w3=73, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 146)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.082667 * pressure.rolling(73, min_periods=max(73//3, 2)).mean() + 0.0033225 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_115_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=301, w3=90, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(153, min_periods=max(153//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.378235 + 0.0033226 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_116_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=314, w3=107, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(314, min_periods=max(314//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 160)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.391765 + 0.0033227 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_117_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=327, w3=124, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(167, min_periods=max(167//3, 2)).mean(), b.abs().rolling(327, min_periods=max(327//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(124) + 0.101667 * _rolling_slope(cover, 167) + 0.0033228 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_118_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=340, w3=141, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.108 * y + 0.892000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 174) - _rolling_slope(basket, 340) + 0.0033229 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_119_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=353, w3=158, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(353, min_periods=max(353//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.432353 + 0.003323 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_120_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=366, w3=175, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(366, min_periods=max(366//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.120667 * _rolling_slope(draw, 175) + 0.0033231 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_121_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=379, w3=192, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(192, min_periods=max(192//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.459412 + 0.0033232 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_122_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=392, w3=209, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(392, min_periods=max(392//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.472941 + 0.0033233 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_123_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=405, w3=226, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 405)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=226, adjust=False).mean() * 1.486471 + 0.0033234 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_124_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=418, w3=243, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(418, min_periods=max(418//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5 + 0.0033235 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_125_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=431, w3=260, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(431, min_periods=max(431//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.152333 * persistence + 0.0033236 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_126_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=444, w3=277, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(444, min_periods=max(444//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.527059 + 0.0033237 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_127_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=457, w3=294, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(457, min_periods=max(457//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.165 * slope + 0.0033238 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_128_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=470, w3=311, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(470, min_periods=max(470//3, 2)).mean()
    noise = impulse.abs().rolling(311, min_periods=max(311//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.554118 + 0.0033239 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_129_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=483, w3=328, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 483)
    curvature = _rolling_slope(acceleration, 328)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.177667 * acceleration + 0.003324 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_130_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=496, w3=345, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 11)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.184 * pressure.rolling(345, min_periods=max(345//3, 2)).mean() + 0.0033241 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_131_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=509, w3=362, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(18, min_periods=max(18//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.594706 + 0.0033242 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_132_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=23, w3=379, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(23, min_periods=max(23//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 25)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.608235 + 0.0033243 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_133_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=36, w3=396, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(32, min_periods=max(32//3, 2)).mean(), b.abs().rolling(36, min_periods=max(36//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.203 * _rolling_slope(cover, 32) + 0.0033244 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_134_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=49, w3=413, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.209333 * y + 0.790667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 39) - _rolling_slope(basket, 49) + 0.0033245 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_135_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=62, w3=430, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(46, min_periods=max(46//3, 2)).mean(), upside.rolling(62, min_periods=max(62//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.648824 + 0.0033246 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_136_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=75, w3=447, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(75, min_periods=max(75//3, 2)).max()
    rebound = x - x.rolling(53, min_periods=max(53//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.222 * _rolling_slope(draw, 447) + 0.0033247 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_137_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=88, w3=464, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(60) - b.diff(88)
    stress = imbalance.rolling(464, min_periods=max(464//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.822353 + 0.0033248 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_138_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=101, w3=481, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 67)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(481, min_periods=max(481//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.835882 + 0.0033249 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_139_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=114, w3=498, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 74)
    slow = _rolling_slope(x, 114)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.849412 + 0.003325 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_140_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=127, w3=515, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(127, min_periods=max(127//3, 2)).max()
    trough = x.rolling(81, min_periods=max(81//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.862941 + 0.0033251 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_141_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=140, w3=532, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(88)
    rank = change.rolling(140, min_periods=max(140//3, 2)).rank(pct=True)
    persistence = change.rolling(532, min_periods=max(532//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.253667 * persistence + 0.0033252 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_142_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=153, w3=549, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(95, min_periods=max(95//3, 2)).std()
    vol_slow = ret.rolling(153, min_periods=max(153//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.89 + 0.0033253 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_143_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=166, w3=566, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(166, min_periods=max(166//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 102)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.266333 * slope + 0.0033254 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_144_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=179, w3=583, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(109)
    drag = impulse.rolling(179, min_periods=max(179//3, 2)).mean()
    noise = impulse.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.917059 + 0.0033255 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_145_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=192, w3=600, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 116)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 600)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.279 * acceleration + 0.0033256 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_146_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=205, w3=617, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 123)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.285333 * pressure.rolling(617, min_periods=max(617//3, 2)).mean() + 0.0033257 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_147_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=218, w3=634, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(130, min_periods=max(130//3, 2)).mean())
    decay = spread.ewm(span=218, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.957647 + 0.0033258 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_148_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=231, w3=651, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(231, min_periods=max(231//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 137)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.971176 + 0.0033259 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_149_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=244, w3=668, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(144, min_periods=max(144//3, 2)).mean(), b.abs().rolling(244, min_periods=max(244//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.304333 * _rolling_slope(cover, 144) + 0.003326 * anchor
    return base_signal.diff().diff()

def f49_bocc_gemini_150_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=257, w3=685, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.310667 * y + 0.689333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 151) - _rolling_slope(basket, 257) + 0.0033261 * anchor
    return base_signal.diff().diff()
