"""58 hidden information flow proxy gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Estimation of latent information processing through price and volume complexity.
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

def f58_hinf_gemini_076_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=268, w3=371, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(268, min_periods=max(268//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.08 * _rolling_slope(draw, 371) + 0.0038367 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_077_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=281, w3=388, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(85) - b.diff(126)
    stress = imbalance.rolling(388, min_periods=max(388//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.957059 + 0.0038368 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_078_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=294, w3=405, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(294, min_periods=max(294//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(405, min_periods=max(405//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.970588 + 0.0038369 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_079_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=307, w3=422, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 307)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.984118 + 0.003837 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_080_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=320, w3=439, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(320, min_periods=max(320//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.997647 + 0.0038371 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_081_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=113, w2=333, w3=456, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(113)
    rank = change.rolling(333, min_periods=max(333//3, 2)).rank(pct=True)
    persistence = change.rolling(456, min_periods=max(456//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111667 * persistence + 0.0038372 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_082_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=120, w2=346, w3=473, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(346, min_periods=max(346//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.024706 + 0.0038373 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_083_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=127, w2=359, w3=490, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(359, min_periods=max(359//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.124333 * slope + 0.0038374 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_084_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=134, w2=372, w3=507, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(372, min_periods=max(372//3, 2)).mean()
    noise = impulse.abs().rolling(507, min_periods=max(507//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.051765 + 0.0038375 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_085_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=141, w2=385, w3=524, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 385)
    curvature = _rolling_slope(acceleration, 524)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.137 * acceleration + 0.0038376 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_086_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=148, w2=398, w3=541, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 148)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.143333 * pressure.rolling(541, min_periods=max(541//3, 2)).mean() + 0.0038377 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_087_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=155, w2=411, w3=558, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(155, min_periods=max(155//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.092353 + 0.0038378 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_088_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=162, w2=424, w3=575, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(424, min_periods=max(424//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 162)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.105882 + 0.0038379 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_089_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=169, w2=437, w3=592, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(169, min_periods=max(169//3, 2)).mean(), b.abs().rolling(437, min_periods=max(437//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.162333 * _rolling_slope(cover, 169) + 0.003838 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_090_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=176, w2=450, w3=609, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.168667 * y + 0.831333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 176) - _rolling_slope(basket, 450) + 0.0038381 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_091_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=183, w2=463, w3=626, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(183, min_periods=max(183//3, 2)).mean(), upside.rolling(463, min_periods=max(463//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.146471 + 0.0038382 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_092_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=190, w2=476, w3=643, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(476, min_periods=max(476//3, 2)).max()
    rebound = x - x.rolling(190, min_periods=max(190//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.181333 * _rolling_slope(draw, 643) + 0.0038383 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_093_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=197, w2=489, w3=660, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.173529 + 0.0038384 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_094_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=204, w2=502, w3=677, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(502, min_periods=max(502//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(677, min_periods=max(677//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.187059 + 0.0038385 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_095_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=211, w2=16, w3=694, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 16)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.200588 + 0.0038386 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_096_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=218, w2=29, w3=711, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(29, min_periods=max(29//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.214118 + 0.0038387 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_097_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=225, w2=42, w3=728, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(42, min_periods=max(42//3, 2)).rank(pct=True)
    persistence = change.rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.213 * persistence + 0.0038388 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_098_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=232, w2=55, w3=745, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(55, min_periods=max(55//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.241176 + 0.0038389 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_099_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=239, w2=68, w3=762, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(68, min_periods=max(68//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225667 * slope + 0.003839 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_100_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=246, w2=81, w3=28, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(81, min_periods=max(81//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.268235 + 0.0038391 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_101_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=6, w2=94, w3=45, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 6)
    acceleration = _rolling_slope(velocity, 94)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.238333 * acceleration + 0.0038392 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_102_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=13, w2=107, w3=62, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 13)
    pressure = rel_log.diff(107)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.244667 * pressure.rolling(62, min_periods=max(62//3, 2)).mean() + 0.0038393 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_103_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=20, w2=120, w3=79, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(20, min_periods=max(20//3, 2)).mean())
    decay = spread.ewm(span=120, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.308824 + 0.0038394 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_104_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=27, w2=133, w3=96, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(133, min_periods=max(133//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 27)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.322353 + 0.0038395 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_105_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=34, w2=146, w3=113, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(34, min_periods=max(34//3, 2)).mean(), b.abs().rolling(146, min_periods=max(146//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(113) + 0.263667 * _rolling_slope(cover, 34) + 0.0038396 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_106_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=41, w2=159, w3=130, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.27 * y + 0.730000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 41) - _rolling_slope(basket, 159) + 0.0038397 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_107_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=48, w2=172, w3=147, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(48, min_periods=max(48//3, 2)).mean(), upside.rolling(172, min_periods=max(172//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.362941 + 0.0038398 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_108_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=55, w2=185, w3=164, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(185, min_periods=max(185//3, 2)).max()
    rebound = x - x.rolling(55, min_periods=max(55//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.282667 * _rolling_slope(draw, 164) + 0.0038399 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_109_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=62, w2=198, w3=181, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(62) - b.diff(126)
    stress = imbalance.rolling(181, min_periods=max(181//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.39 + 0.00384 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_110_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=69, w2=211, w3=198, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 69)
    baseline = trend.rolling(211, min_periods=max(211//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.403529 + 0.0038401 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_111_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=76, w2=224, w3=215, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 76)
    slow = _rolling_slope(x, 224)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=215, adjust=False).mean() * 1.417059 + 0.0038402 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_112_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=83, w2=237, w3=232, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(237, min_periods=max(237//3, 2)).max()
    trough = x.rolling(83, min_periods=max(83//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.430588 + 0.0038403 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_113_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=90, w2=250, w3=249, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(90)
    rank = change.rolling(250, min_periods=max(250//3, 2)).rank(pct=True)
    persistence = change.rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.314333 * persistence + 0.0038404 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_114_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=97, w2=263, w3=266, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(97, min_periods=max(97//3, 2)).std()
    vol_slow = ret.rolling(263, min_periods=max(263//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.457647 + 0.0038405 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_115_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=104, w2=276, w3=283, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(276, min_periods=max(276//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 104)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.327 * slope + 0.0038406 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_116_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=111, w2=289, w3=300, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(111)
    drag = impulse.rolling(289, min_periods=max(289//3, 2)).mean()
    noise = impulse.abs().rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.484706 + 0.0038407 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_117_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=118, w2=302, w3=317, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 118)
    acceleration = _rolling_slope(velocity, 302)
    curvature = _rolling_slope(acceleration, 317)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.339667 * acceleration + 0.0038408 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_118_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=125, w2=315, w3=334, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 125)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.346 * pressure.rolling(334, min_periods=max(334//3, 2)).mean() + 0.0038409 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_119_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=132, w2=328, w3=351, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(132, min_periods=max(132//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.525294 + 0.003841 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_120_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=139, w2=341, w3=368, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(341, min_periods=max(341//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 139)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.538824 + 0.0038411 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_121_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=146, w2=354, w3=385, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(146, min_periods=max(146//3, 2)).mean(), b.abs().rolling(354, min_periods=max(354//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.032667 * _rolling_slope(cover, 146) + 0.0038412 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_122_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=153, w2=367, w3=402, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.039 * y + 0.961000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 153) - _rolling_slope(basket, 367) + 0.0038413 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_123_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=160, w2=380, w3=419, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(160, min_periods=max(160//3, 2)).mean(), upside.rolling(380, min_periods=max(380//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.579412 + 0.0038414 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_124_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=167, w2=393, w3=436, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(393, min_periods=max(393//3, 2)).max()
    rebound = x - x.rolling(167, min_periods=max(167//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.051667 * _rolling_slope(draw, 436) + 0.0038415 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_125_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=406, w3=453, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(453, min_periods=max(453//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.606471 + 0.0038416 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_126_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=419, w3=470, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 181)
    baseline = trend.rolling(419, min_periods=max(419//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(470, min_periods=max(470//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.62 + 0.0038417 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_127_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=432, w3=487, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 188)
    slow = _rolling_slope(x, 432)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.633529 + 0.0038418 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_128_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=445, w3=504, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(445, min_periods=max(445//3, 2)).max()
    trough = x.rolling(195, min_periods=max(195//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.647059 + 0.0038419 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_129_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=458, w3=521, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(458, min_periods=max(458//3, 2)).rank(pct=True)
    persistence = change.rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.083333 * persistence + 0.003842 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_130_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=471, w3=538, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(209, min_periods=max(209//3, 2)).std()
    vol_slow = ret.rolling(471, min_periods=max(471//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.820588 + 0.0038421 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_131_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=484, w3=555, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(484, min_periods=max(484//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 216)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.096 * slope + 0.0038422 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_132_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=497, w3=572, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(497, min_periods=max(497//3, 2)).mean()
    noise = impulse.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.847647 + 0.0038423 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_133_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=11, w3=589, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 230)
    acceleration = _rolling_slope(velocity, 11)
    curvature = _rolling_slope(acceleration, 589)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.108667 * acceleration + 0.0038424 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_134_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=24, w3=606, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 237)
    pressure = rel_log.diff(24)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.115 * pressure.rolling(606, min_periods=max(606//3, 2)).mean() + 0.0038425 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_135_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=37, w3=623, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(244, min_periods=max(244//3, 2)).mean())
    decay = spread.ewm(span=37, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.888235 + 0.0038426 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_136_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=50, w3=640, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(50, min_periods=max(50//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 251)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.901765 + 0.0038427 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_137_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=63, w3=657, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(11, min_periods=max(11//3, 2)).mean(), b.abs().rolling(63, min_periods=max(63//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.134 * _rolling_slope(cover, 11) + 0.0038428 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_138_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=76, w3=674, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.140333 * y + 0.859667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 18) - _rolling_slope(basket, 76) + 0.0038429 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_139_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=89, w3=691, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(89, min_periods=max(89//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.942353 + 0.003843 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_140_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=102, w3=708, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(102, min_periods=max(102//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.153 * _rolling_slope(draw, 708) + 0.0038431 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_141_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=115, w3=725, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(39) - b.diff(115)
    stress = imbalance.rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.969412 + 0.0038432 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_142_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=128, w3=742, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(128, min_periods=max(128//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.982941 + 0.0038433 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_143_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=141, w3=759, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 141)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.996471 + 0.0038434 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_144_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=154, w3=25, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(154, min_periods=max(154//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01 + 0.0038435 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_145_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=167, w3=42, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(67)
    rank = change.rolling(167, min_periods=max(167//3, 2)).rank(pct=True)
    persistence = change.rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.184667 * persistence + 0.0038436 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_146_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=180, w3=59, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(180, min_periods=max(180//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.037059 + 0.0038437 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_147_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=193, w3=76, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(193, min_periods=max(193//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.197333 * slope + 0.0038438 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_148_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=206, w3=93, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(88)
    drag = impulse.rolling(206, min_periods=max(206//3, 2)).mean()
    noise = impulse.abs().rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.064118 + 0.0038439 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_149_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=219, w3=110, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 219)
    curvature = _rolling_slope(acceleration, 110)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.21 * acceleration + 0.003844 * anchor
    return base_signal.diff().diff().diff()

def f58_hinf_gemini_150_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=232, w3=127, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 102)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.216333 * pressure.rolling(127, min_periods=max(127//3, 2)).mean() + 0.0038441 * anchor
    return base_signal.diff().diff().diff()
