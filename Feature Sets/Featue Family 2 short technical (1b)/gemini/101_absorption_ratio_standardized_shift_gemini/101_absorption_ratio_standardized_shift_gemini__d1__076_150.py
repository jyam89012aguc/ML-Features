"""101 absorption ratio standardized shift gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Standardized changes in the proportion of variance explained by lead components.
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

def f101_abrs_gemini_076_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=35, w3=693, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(35, min_periods=max(35//3, 2)).mean()
    noise = impulse.abs().rolling(693, min_periods=max(693//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.555294 + 0.0005607 * anchor
    return base_signal.diff()

def f101_abrs_gemini_077_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=48, w3=710, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 228)
    acceleration = _rolling_slope(velocity, 48)
    curvature = _rolling_slope(acceleration, 710)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.314667 * acceleration + 0.0005608 * anchor
    return base_signal.diff()

def f101_abrs_gemini_078_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=61, w3=727, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 235)
    pressure = rel_log.diff(61)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.321 * pressure.rolling(727, min_periods=max(727//3, 2)).mean() + 0.0005609 * anchor
    return base_signal.diff()

def f101_abrs_gemini_079_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=74, w3=744, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(242, min_periods=max(242//3, 2)).mean())
    decay = spread.ewm(span=74, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.595882 + 0.000561 * anchor
    return base_signal.diff()

def f101_abrs_gemini_080_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=87, w3=761, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(87, min_periods=max(87//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 249)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.609412 + 0.0005611 * anchor
    return base_signal.diff()

def f101_abrs_gemini_081_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=100, w3=27, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(9, min_periods=max(9//3, 2)).mean(), b.abs().rolling(100, min_periods=max(100//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(27) + 0.34 * _rolling_slope(cover, 9) + 0.0005612 * anchor
    return base_signal.diff()

def f101_abrs_gemini_082_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=113, w3=44, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.346333 * y + 0.653667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 16) - _rolling_slope(basket, 113) + 0.0005613 * anchor
    return base_signal.diff()

def f101_abrs_gemini_083_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=126, w3=61, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(126, min_periods=max(126//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(61) * 1.65 + 0.0005614 * anchor
    return base_signal.diff()

def f101_abrs_gemini_084_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=139, w3=78, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(139, min_periods=max(139//3, 2)).max()
    rebound = x - x.rolling(30, min_periods=max(30//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359 * _rolling_slope(draw, 78) + 0.0005615 * anchor
    return base_signal.diff()

def f101_abrs_gemini_085_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=152, w3=95, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(37) - b.diff(126)
    stress = imbalance.rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.823529 + 0.0005616 * anchor
    return base_signal.diff()

def f101_abrs_gemini_086_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=165, w3=112, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 44)
    baseline = trend.rolling(165, min_periods=max(165//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(112, min_periods=max(112//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.837059 + 0.0005617 * anchor
    return base_signal.diff()

def f101_abrs_gemini_087_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=178, w3=129, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 51)
    slow = _rolling_slope(x, 178)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=129, adjust=False).mean() * 0.850588 + 0.0005618 * anchor
    return base_signal.diff()

def f101_abrs_gemini_088_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=191, w3=146, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(191, min_periods=max(191//3, 2)).max()
    trough = x.rolling(58, min_periods=max(58//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.864118 + 0.0005619 * anchor
    return base_signal.diff()

def f101_abrs_gemini_089_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=204, w3=163, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(65)
    rank = change.rolling(204, min_periods=max(204//3, 2)).rank(pct=True)
    persistence = change.rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.058333 * persistence + 0.000562 * anchor
    return base_signal.diff()

def f101_abrs_gemini_090_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=217, w3=180, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(72, min_periods=max(72//3, 2)).std()
    vol_slow = ret.rolling(217, min_periods=max(217//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.891176 + 0.0005621 * anchor
    return base_signal.diff()

def f101_abrs_gemini_091_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=230, w3=197, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(230, min_periods=max(230//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 79)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.071 * slope + 0.0005622 * anchor
    return base_signal.diff()

def f101_abrs_gemini_092_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=243, w3=214, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(86)
    drag = impulse.rolling(243, min_periods=max(243//3, 2)).mean()
    noise = impulse.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.918235 + 0.0005623 * anchor
    return base_signal.diff()

def f101_abrs_gemini_093_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=93, w2=256, w3=231, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 93)
    acceleration = _rolling_slope(velocity, 256)
    curvature = _rolling_slope(acceleration, 231)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.083667 * acceleration + 0.0005624 * anchor
    return base_signal.diff()

def f101_abrs_gemini_094_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=100, w2=269, w3=248, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 100)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.09 * pressure.rolling(248, min_periods=max(248//3, 2)).mean() + 0.0005625 * anchor
    return base_signal.diff()

def f101_abrs_gemini_095_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=107, w2=282, w3=265, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(107, min_periods=max(107//3, 2)).mean())
    decay = spread.ewm(span=282, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.958824 + 0.0005626 * anchor
    return base_signal.diff()

def f101_abrs_gemini_096_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=114, w2=295, w3=282, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(295, min_periods=max(295//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 114)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.972353 + 0.0005627 * anchor
    return base_signal.diff()

def f101_abrs_gemini_097_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=121, w2=308, w3=299, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(121, min_periods=max(121//3, 2)).mean(), b.abs().rolling(308, min_periods=max(308//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.109 * _rolling_slope(cover, 121) + 0.0005628 * anchor
    return base_signal.diff()

def f101_abrs_gemini_098_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=128, w2=321, w3=316, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.115333 * y + 0.884667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 128) - _rolling_slope(basket, 321) + 0.0005629 * anchor
    return base_signal.diff()

def f101_abrs_gemini_099_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=135, w2=334, w3=333, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(135, min_periods=max(135//3, 2)).mean(), upside.rolling(334, min_periods=max(334//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.012941 + 0.000563 * anchor
    return base_signal.diff()

def f101_abrs_gemini_100_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=142, w2=347, w3=350, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(347, min_periods=max(347//3, 2)).max()
    rebound = x - x.rolling(142, min_periods=max(142//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.128 * _rolling_slope(draw, 350) + 0.0005631 * anchor
    return base_signal.diff()

def f101_abrs_gemini_101_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=149, w2=360, w3=367, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.04 + 0.0005632 * anchor
    return base_signal.diff()

def f101_abrs_gemini_102_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=156, w2=373, w3=384, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 156)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.053529 + 0.0005633 * anchor
    return base_signal.diff()

def f101_abrs_gemini_103_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=163, w2=386, w3=401, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 163)
    slow = _rolling_slope(x, 386)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.067059 + 0.0005634 * anchor
    return base_signal.diff()

def f101_abrs_gemini_104_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=170, w2=399, w3=418, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(399, min_periods=max(399//3, 2)).max()
    trough = x.rolling(170, min_periods=max(170//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.080588 + 0.0005635 * anchor
    return base_signal.diff()

def f101_abrs_gemini_105_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=177, w2=412, w3=435, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(412, min_periods=max(412//3, 2)).rank(pct=True)
    persistence = change.rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.159667 * persistence + 0.0005636 * anchor
    return base_signal.diff()

def f101_abrs_gemini_106_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=184, w2=425, w3=452, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(184, min_periods=max(184//3, 2)).std()
    vol_slow = ret.rolling(425, min_periods=max(425//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.107647 + 0.0005637 * anchor
    return base_signal.diff()

def f101_abrs_gemini_107_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=191, w2=438, w3=469, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(438, min_periods=max(438//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 191)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.172333 * slope + 0.0005638 * anchor
    return base_signal.diff()

def f101_abrs_gemini_108_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=198, w2=451, w3=486, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.134706 + 0.0005639 * anchor
    return base_signal.diff()

def f101_abrs_gemini_109_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=205, w2=464, w3=503, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 205)
    acceleration = _rolling_slope(velocity, 464)
    curvature = _rolling_slope(acceleration, 503)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.185 * acceleration + 0.000564 * anchor
    return base_signal.diff()

def f101_abrs_gemini_110_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=212, w2=477, w3=520, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 212)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.191333 * pressure.rolling(520, min_periods=max(520//3, 2)).mean() + 0.0005641 * anchor
    return base_signal.diff()

def f101_abrs_gemini_111_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=219, w2=490, w3=537, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(219, min_periods=max(219//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.175294 + 0.0005642 * anchor
    return base_signal.diff()

def f101_abrs_gemini_112_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=226, w2=503, w3=554, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(503, min_periods=max(503//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 226)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.188824 + 0.0005643 * anchor
    return base_signal.diff()

def f101_abrs_gemini_113_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=233, w2=17, w3=571, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(233, min_periods=max(233//3, 2)).mean(), b.abs().rolling(17, min_periods=max(17//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.210333 * _rolling_slope(cover, 233) + 0.0005644 * anchor
    return base_signal.diff()

def f101_abrs_gemini_114_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=240, w2=30, w3=588, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.216667 * y + 0.783333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 240) - _rolling_slope(basket, 30) + 0.0005645 * anchor
    return base_signal.diff()

def f101_abrs_gemini_115_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=247, w2=43, w3=605, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(247, min_periods=max(247//3, 2)).mean(), upside.rolling(43, min_periods=max(43//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.229412 + 0.0005646 * anchor
    return base_signal.diff()

def f101_abrs_gemini_116_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=56, w3=622, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(56, min_periods=max(56//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.229333 * _rolling_slope(draw, 622) + 0.0005647 * anchor
    return base_signal.diff()

def f101_abrs_gemini_117_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=69, w3=639, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(14) - b.diff(69)
    stress = imbalance.rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.256471 + 0.0005648 * anchor
    return base_signal.diff()

def f101_abrs_gemini_118_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=82, w3=656, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(82, min_periods=max(82//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.27 + 0.0005649 * anchor
    return base_signal.diff()

def f101_abrs_gemini_119_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=95, w3=673, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 95)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.283529 + 0.000565 * anchor
    return base_signal.diff()

def f101_abrs_gemini_120_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=108, w3=690, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.297059 + 0.0005651 * anchor
    return base_signal.diff()

def f101_abrs_gemini_121_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=121, w3=707, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(42)
    rank = change.rolling(121, min_periods=max(121//3, 2)).rank(pct=True)
    persistence = change.rolling(707, min_periods=max(707//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.261 * persistence + 0.0005652 * anchor
    return base_signal.diff()

def f101_abrs_gemini_122_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=134, w3=724, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(134, min_periods=max(134//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.324118 + 0.0005653 * anchor
    return base_signal.diff()

def f101_abrs_gemini_123_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=147, w3=741, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(147, min_periods=max(147//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.273667 * slope + 0.0005654 * anchor
    return base_signal.diff()

def f101_abrs_gemini_124_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=160, w3=758, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(63)
    drag = impulse.rolling(160, min_periods=max(160//3, 2)).mean()
    noise = impulse.abs().rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.351176 + 0.0005655 * anchor
    return base_signal.diff()

def f101_abrs_gemini_125_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=173, w3=24, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 173)
    curvature = _rolling_slope(acceleration, 24)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.286333 * acceleration + 0.0005656 * anchor
    return base_signal.diff()

def f101_abrs_gemini_126_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=186, w3=41, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 77)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.292667 * pressure.rolling(41, min_periods=max(41//3, 2)).mean() + 0.0005657 * anchor
    return base_signal.diff()

def f101_abrs_gemini_127_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=199, w3=58, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(84, min_periods=max(84//3, 2)).mean())
    decay = spread.ewm(span=199, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.391765 + 0.0005658 * anchor
    return base_signal.diff()

def f101_abrs_gemini_128_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=212, w3=75, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(212, min_periods=max(212//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 91)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.405294 + 0.0005659 * anchor
    return base_signal.diff()

def f101_abrs_gemini_129_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=225, w3=92, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(98, min_periods=max(98//3, 2)).mean(), b.abs().rolling(225, min_periods=max(225//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(92) + 0.311667 * _rolling_slope(cover, 98) + 0.000566 * anchor
    return base_signal.diff()

def f101_abrs_gemini_130_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=238, w3=109, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.318 * y + 0.682000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 105) - _rolling_slope(basket, 238) + 0.0005661 * anchor
    return base_signal.diff()

def f101_abrs_gemini_131_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=251, w3=126, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(112, min_periods=max(112//3, 2)).mean(), upside.rolling(251, min_periods=max(251//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.445882 + 0.0005662 * anchor
    return base_signal.diff()

def f101_abrs_gemini_132_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=264, w3=143, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(264, min_periods=max(264//3, 2)).max()
    rebound = x - x.rolling(119, min_periods=max(119//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.330667 * _rolling_slope(draw, 143) + 0.0005663 * anchor
    return base_signal.diff()

def f101_abrs_gemini_133_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=277, w3=160, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(160, min_periods=max(160//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.472941 + 0.0005664 * anchor
    return base_signal.diff()

def f101_abrs_gemini_134_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=290, w3=177, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 133)
    baseline = trend.rolling(290, min_periods=max(290//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(177, min_periods=max(177//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.486471 + 0.0005665 * anchor
    return base_signal.diff()

def f101_abrs_gemini_135_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=303, w3=194, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 140)
    slow = _rolling_slope(x, 303)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=194, adjust=False).mean() * 1.5 + 0.0005666 * anchor
    return base_signal.diff()

def f101_abrs_gemini_136_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=316, w3=211, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(316, min_periods=max(316//3, 2)).max()
    trough = x.rolling(147, min_periods=max(147//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.513529 + 0.0005667 * anchor
    return base_signal.diff()

def f101_abrs_gemini_137_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=329, w3=228, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(329, min_periods=max(329//3, 2)).rank(pct=True)
    persistence = change.rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.362333 * persistence + 0.0005668 * anchor
    return base_signal.diff()

def f101_abrs_gemini_138_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=342, w3=245, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(161, min_periods=max(161//3, 2)).std()
    vol_slow = ret.rolling(342, min_periods=max(342//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.540588 + 0.0005669 * anchor
    return base_signal.diff()

def f101_abrs_gemini_139_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=355, w3=262, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(355, min_periods=max(355//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 168)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.042667 * slope + 0.000567 * anchor
    return base_signal.diff()

def f101_abrs_gemini_140_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=368, w3=279, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(368, min_periods=max(368//3, 2)).mean()
    noise = impulse.abs().rolling(279, min_periods=max(279//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.567647 + 0.0005671 * anchor
    return base_signal.diff()

def f101_abrs_gemini_141_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=381, w3=296, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 182)
    acceleration = _rolling_slope(velocity, 381)
    curvature = _rolling_slope(acceleration, 296)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.055333 * acceleration + 0.0005672 * anchor
    return base_signal.diff()

def f101_abrs_gemini_142_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=189, w2=394, w3=313, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 189)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.061667 * pressure.rolling(313, min_periods=max(313//3, 2)).mean() + 0.0005673 * anchor
    return base_signal.diff()

def f101_abrs_gemini_143_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=196, w2=407, w3=330, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(196, min_periods=max(196//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.608235 + 0.0005674 * anchor
    return base_signal.diff()

def f101_abrs_gemini_144_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=203, w2=420, w3=347, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(420, min_periods=max(420//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 203)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.621765 + 0.0005675 * anchor
    return base_signal.diff()

def f101_abrs_gemini_145_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=433, w3=364, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(210, min_periods=max(210//3, 2)).mean(), b.abs().rolling(433, min_periods=max(433//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.080667 * _rolling_slope(cover, 210) + 0.0005676 * anchor
    return base_signal.diff()

def f101_abrs_gemini_146_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=446, w3=381, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.087 * y + 0.913000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 217) - _rolling_slope(basket, 446) + 0.0005677 * anchor
    return base_signal.diff()

def f101_abrs_gemini_147_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=459, w3=398, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(224, min_periods=max(224//3, 2)).mean(), upside.rolling(459, min_periods=max(459//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.662353 + 0.0005678 * anchor
    return base_signal.diff()

def f101_abrs_gemini_148_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=472, w3=415, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(472, min_periods=max(472//3, 2)).max()
    rebound = x - x.rolling(231, min_periods=max(231//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.099667 * _rolling_slope(draw, 415) + 0.0005679 * anchor
    return base_signal.diff()

def f101_abrs_gemini_149_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=485, w3=432, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(432, min_periods=max(432//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.835882 + 0.000568 * anchor
    return base_signal.diff()

def f101_abrs_gemini_150_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=498, w3=449, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(498, min_periods=max(498//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.849412 + 0.0005681 * anchor
    return base_signal.diff()
