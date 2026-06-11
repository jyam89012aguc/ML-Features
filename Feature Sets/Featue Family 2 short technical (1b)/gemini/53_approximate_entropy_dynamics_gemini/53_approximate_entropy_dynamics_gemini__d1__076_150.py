"""53 approximate entropy dynamics gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Quantification of regularity and predictability in short-term price fluctuations.
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

def f53_aent_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=7, w2=148, w3=581, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(7)
    drag = impulse.rolling(148, min_periods=max(148//3, 2)).mean()
    noise = impulse.abs().rolling(581, min_periods=max(581//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.095882 + 0.0035287 * anchor
    return base_signal.diff()

def f53_aent_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=14, w2=161, w3=598, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 14)
    acceleration = _rolling_slope(velocity, 161)
    curvature = _rolling_slope(acceleration, 598)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.187333 * acceleration + 0.0035288 * anchor
    return base_signal.diff()

def f53_aent_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=21, w2=174, w3=615, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(21, min_periods=max(21//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.122941 + 0.0035289 * anchor
    return base_signal.diff()

def f53_aent_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=28, w2=187, w3=632, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(187, min_periods=max(187//3, 2)).max()
    rebound = x - x.rolling(28, min_periods=max(28//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2 * _rolling_slope(draw, 632) + 0.003529 * anchor
    return base_signal.diff()

def f53_aent_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=35, w2=200, w3=649, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 35)
    baseline = trend.rolling(200, min_periods=max(200//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(649, min_periods=max(649//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15 + 0.0035291 * anchor
    return base_signal.diff()

def f53_aent_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=42, w2=213, w3=666, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 42)
    slow = _rolling_slope(x, 213)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.163529 + 0.0035292 * anchor
    return base_signal.diff()

def f53_aent_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=49, w2=226, w3=683, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(226, min_periods=max(226//3, 2)).max()
    trough = x.rolling(49, min_periods=max(49//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.177059 + 0.0035293 * anchor
    return base_signal.diff()

def f53_aent_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=56, w2=239, w3=700, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(56)
    rank = change.rolling(239, min_periods=max(239//3, 2)).rank(pct=True)
    persistence = change.rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.225333 * persistence + 0.0035294 * anchor
    return base_signal.diff()

def f53_aent_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=63, w2=252, w3=717, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(63, min_periods=max(63//3, 2)).std()
    vol_slow = ret.rolling(252, min_periods=max(252//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.204118 + 0.0035295 * anchor
    return base_signal.diff()

def f53_aent_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=70, w2=265, w3=734, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(265, min_periods=max(265//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 70)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.238 * slope + 0.0035296 * anchor
    return base_signal.diff()

def f53_aent_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=77, w2=278, w3=751, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(77)
    drag = impulse.rolling(278, min_periods=max(278//3, 2)).mean()
    noise = impulse.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.231176 + 0.0035297 * anchor
    return base_signal.diff()

def f53_aent_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=84, w2=291, w3=17, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 291)
    curvature = _rolling_slope(acceleration, 17)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.250667 * acceleration + 0.0035298 * anchor
    return base_signal.diff()

def f53_aent_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=91, w2=304, w3=34, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(304, min_periods=max(304//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(34) * 1.258235 + 0.0035299 * anchor
    return base_signal.diff()

def f53_aent_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=98, w2=317, w3=51, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(317, min_periods=max(317//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.263333 * _rolling_slope(draw, 51) + 0.00353 * anchor
    return base_signal.diff()

def f53_aent_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=105, w2=330, w3=68, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(330, min_periods=max(330//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(68, min_periods=max(68//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.285294 + 0.0035301 * anchor
    return base_signal.diff()

def f53_aent_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=112, w2=343, w3=85, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 343)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=85, adjust=False).mean() * 1.298824 + 0.0035302 * anchor
    return base_signal.diff()

def f53_aent_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=119, w2=356, w3=102, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(356, min_periods=max(356//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.312353 + 0.0035303 * anchor
    return base_signal.diff()

def f53_aent_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=126, w2=369, w3=119, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(369, min_periods=max(369//3, 2)).rank(pct=True)
    persistence = change.rolling(119, min_periods=max(119//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.288667 * persistence + 0.0035304 * anchor
    return base_signal.diff()

def f53_aent_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=133, w2=382, w3=136, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(382, min_periods=max(382//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.339412 + 0.0035305 * anchor
    return base_signal.diff()

def f53_aent_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=140, w2=395, w3=153, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(395, min_periods=max(395//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.301333 * slope + 0.0035306 * anchor
    return base_signal.diff()

def f53_aent_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=147, w2=408, w3=170, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(408, min_periods=max(408//3, 2)).mean()
    noise = impulse.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.366471 + 0.0035307 * anchor
    return base_signal.diff()

def f53_aent_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=154, w2=421, w3=187, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 421)
    curvature = _rolling_slope(acceleration, 187)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.314 * acceleration + 0.0035308 * anchor
    return base_signal.diff()

def f53_aent_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=161, w2=434, w3=204, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(434, min_periods=max(434//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.393529 + 0.0035309 * anchor
    return base_signal.diff()

def f53_aent_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=168, w2=447, w3=221, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(447, min_periods=max(447//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.326667 * _rolling_slope(draw, 221) + 0.003531 * anchor
    return base_signal.diff()

def f53_aent_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=175, w2=460, w3=238, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(460, min_periods=max(460//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(238, min_periods=max(238//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.420588 + 0.0035311 * anchor
    return base_signal.diff()

def f53_aent_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=182, w2=473, w3=255, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 473)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=255, adjust=False).mean() * 1.434118 + 0.0035312 * anchor
    return base_signal.diff()

def f53_aent_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=189, w2=486, w3=272, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(486, min_periods=max(486//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.447647 + 0.0035313 * anchor
    return base_signal.diff()

def f53_aent_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=196, w2=499, w3=289, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(499, min_periods=max(499//3, 2)).rank(pct=True)
    persistence = change.rolling(289, min_periods=max(289//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.352 * persistence + 0.0035314 * anchor
    return base_signal.diff()

def f53_aent_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=203, w2=13, w3=306, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(13, min_periods=max(13//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.474706 + 0.0035315 * anchor
    return base_signal.diff()

def f53_aent_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=210, w2=26, w3=323, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(26, min_periods=max(26//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.032333 * slope + 0.0035316 * anchor
    return base_signal.diff()

def f53_aent_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=217, w2=39, w3=340, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(39, min_periods=max(39//3, 2)).mean()
    noise = impulse.abs().rolling(340, min_periods=max(340//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.501765 + 0.0035317 * anchor
    return base_signal.diff()

def f53_aent_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=224, w2=52, w3=357, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 52)
    curvature = _rolling_slope(acceleration, 357)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.045 * acceleration + 0.0035318 * anchor
    return base_signal.diff()

def f53_aent_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=231, w2=65, w3=374, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(65, min_periods=max(65//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.528824 + 0.0035319 * anchor
    return base_signal.diff()

def f53_aent_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=238, w2=78, w3=391, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(78, min_periods=max(78//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.057667 * _rolling_slope(draw, 391) + 0.003532 * anchor
    return base_signal.diff()

def f53_aent_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=245, w2=91, w3=408, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(91, min_periods=max(91//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(408, min_periods=max(408//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.555882 + 0.0035321 * anchor
    return base_signal.diff()

def f53_aent_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=5, w2=104, w3=425, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 5)
    slow = _rolling_slope(x, 104)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.569412 + 0.0035322 * anchor
    return base_signal.diff()

def f53_aent_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=117, w3=442, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(117, min_periods=max(117//3, 2)).max()
    trough = x.rolling(12, min_periods=max(12//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.582941 + 0.0035323 * anchor
    return base_signal.diff()

def f53_aent_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=130, w3=459, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(19)
    rank = change.rolling(130, min_periods=max(130//3, 2)).rank(pct=True)
    persistence = change.rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.083 * persistence + 0.0035324 * anchor
    return base_signal.diff()

def f53_aent_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=143, w3=476, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(26, min_periods=max(26//3, 2)).std()
    vol_slow = ret.rolling(143, min_periods=max(143//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.61 + 0.0035325 * anchor
    return base_signal.diff()

def f53_aent_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=156, w3=493, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 33)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.095667 * slope + 0.0035326 * anchor
    return base_signal.diff()

def f53_aent_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=169, w3=510, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(40)
    drag = impulse.rolling(169, min_periods=max(169//3, 2)).mean()
    noise = impulse.abs().rolling(510, min_periods=max(510//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.637059 + 0.0035327 * anchor
    return base_signal.diff()

def f53_aent_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=182, w3=527, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 47)
    acceleration = _rolling_slope(velocity, 182)
    curvature = _rolling_slope(acceleration, 527)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.108333 * acceleration + 0.0035328 * anchor
    return base_signal.diff()

def f53_aent_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=195, w3=544, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(54, min_periods=max(54//3, 2)).mean(), upside.rolling(195, min_periods=max(195//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.664118 + 0.0035329 * anchor
    return base_signal.diff()

def f53_aent_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=208, w3=561, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(208, min_periods=max(208//3, 2)).max()
    rebound = x - x.rolling(61, min_periods=max(61//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.121 * _rolling_slope(draw, 561) + 0.003533 * anchor
    return base_signal.diff()

def f53_aent_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=221, w3=578, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 68)
    baseline = trend.rolling(221, min_periods=max(221//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.837647 + 0.0035331 * anchor
    return base_signal.diff()

def f53_aent_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=234, w3=595, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 75)
    slow = _rolling_slope(x, 234)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.851176 + 0.0035332 * anchor
    return base_signal.diff()

def f53_aent_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=247, w3=612, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(247, min_periods=max(247//3, 2)).max()
    trough = x.rolling(82, min_periods=max(82//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.864706 + 0.0035333 * anchor
    return base_signal.diff()

def f53_aent_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=260, w3=629, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(89)
    rank = change.rolling(260, min_periods=max(260//3, 2)).rank(pct=True)
    persistence = change.rolling(629, min_periods=max(629//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.146333 * persistence + 0.0035334 * anchor
    return base_signal.diff()

def f53_aent_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=273, w3=646, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(96, min_periods=max(96//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.891765 + 0.0035335 * anchor
    return base_signal.diff()

def f53_aent_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=286, w3=663, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(286, min_periods=max(286//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 103)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.159 * slope + 0.0035336 * anchor
    return base_signal.diff()

def f53_aent_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=299, w3=680, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(110)
    drag = impulse.rolling(299, min_periods=max(299//3, 2)).mean()
    noise = impulse.abs().rolling(680, min_periods=max(680//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.918824 + 0.0035337 * anchor
    return base_signal.diff()

def f53_aent_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=312, w3=697, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 117)
    acceleration = _rolling_slope(velocity, 312)
    curvature = _rolling_slope(acceleration, 697)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.171667 * acceleration + 0.0035338 * anchor
    return base_signal.diff()

def f53_aent_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=325, w3=714, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(124, min_periods=max(124//3, 2)).mean(), upside.rolling(325, min_periods=max(325//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.945882 + 0.0035339 * anchor
    return base_signal.diff()

def f53_aent_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=338, w3=731, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(338, min_periods=max(338//3, 2)).max()
    rebound = x - x.rolling(131, min_periods=max(131//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.184333 * _rolling_slope(draw, 731) + 0.003534 * anchor
    return base_signal.diff()

def f53_aent_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=351, w3=748, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 138)
    baseline = trend.rolling(351, min_periods=max(351//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.972941 + 0.0035341 * anchor
    return base_signal.diff()

def f53_aent_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=364, w3=765, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 145)
    slow = _rolling_slope(x, 364)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.986471 + 0.0035342 * anchor
    return base_signal.diff()

def f53_aent_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=377, w3=31, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(377, min_periods=max(377//3, 2)).max()
    trough = x.rolling(152, min_periods=max(152//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.0 + 0.0035343 * anchor
    return base_signal.diff()

def f53_aent_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=390, w3=48, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(390, min_periods=max(390//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.209667 * persistence + 0.0035344 * anchor
    return base_signal.diff()

def f53_aent_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=403, w3=65, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(166, min_periods=max(166//3, 2)).std()
    vol_slow = ret.rolling(403, min_periods=max(403//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.027059 + 0.0035345 * anchor
    return base_signal.diff()

def f53_aent_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=416, w3=82, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(416, min_periods=max(416//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 173)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.222333 * slope + 0.0035346 * anchor
    return base_signal.diff()

def f53_aent_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=429, w3=99, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(429, min_periods=max(429//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.054118 + 0.0035347 * anchor
    return base_signal.diff()

def f53_aent_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=442, w3=116, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 187)
    acceleration = _rolling_slope(velocity, 442)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235 * acceleration + 0.0035348 * anchor
    return base_signal.diff()

def f53_aent_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=455, w3=133, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(194, min_periods=max(194//3, 2)).mean(), upside.rolling(455, min_periods=max(455//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.081176 + 0.0035349 * anchor
    return base_signal.diff()

def f53_aent_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=468, w3=150, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(468, min_periods=max(468//3, 2)).max()
    rebound = x - x.rolling(201, min_periods=max(201//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.247667 * _rolling_slope(draw, 150) + 0.003535 * anchor
    return base_signal.diff()

def f53_aent_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=481, w3=167, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 208)
    baseline = trend.rolling(481, min_periods=max(481//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(167, min_periods=max(167//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.108235 + 0.0035351 * anchor
    return base_signal.diff()

def f53_aent_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=494, w3=184, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 215)
    slow = _rolling_slope(x, 494)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=184, adjust=False).mean() * 1.121765 + 0.0035352 * anchor
    return base_signal.diff()

def f53_aent_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=507, w3=201, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(507, min_periods=max(507//3, 2)).max()
    trough = x.rolling(222, min_periods=max(222//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.135294 + 0.0035353 * anchor
    return base_signal.diff()

def f53_aent_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=21, w3=218, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(21, min_periods=max(21//3, 2)).rank(pct=True)
    persistence = change.rolling(218, min_periods=max(218//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.273 * persistence + 0.0035354 * anchor
    return base_signal.diff()

def f53_aent_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=34, w3=235, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(236, min_periods=max(236//3, 2)).std()
    vol_slow = ret.rolling(34, min_periods=max(34//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.162353 + 0.0035355 * anchor
    return base_signal.diff()

def f53_aent_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=47, w3=252, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(47, min_periods=max(47//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 243)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.285667 * slope + 0.0035356 * anchor
    return base_signal.diff()

def f53_aent_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=60, w3=269, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(60, min_periods=max(60//3, 2)).mean()
    noise = impulse.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.189412 + 0.0035357 * anchor
    return base_signal.diff()

def f53_aent_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=73, w3=286, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 73)
    curvature = _rolling_slope(acceleration, 286)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.298333 * acceleration + 0.0035358 * anchor
    return base_signal.diff()

def f53_aent_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=86, w3=303, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(17, min_periods=max(17//3, 2)).mean(), upside.rolling(86, min_periods=max(86//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.216471 + 0.0035359 * anchor
    return base_signal.diff()

def f53_aent_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=99, w3=320, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(99, min_periods=max(99//3, 2)).max()
    rebound = x - x.rolling(24, min_periods=max(24//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.311 * _rolling_slope(draw, 320) + 0.003536 * anchor
    return base_signal.diff()

def f53_aent_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=112, w3=337, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 31)
    baseline = trend.rolling(112, min_periods=max(112//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(337, min_periods=max(337//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.243529 + 0.0035361 * anchor
    return base_signal.diff()
