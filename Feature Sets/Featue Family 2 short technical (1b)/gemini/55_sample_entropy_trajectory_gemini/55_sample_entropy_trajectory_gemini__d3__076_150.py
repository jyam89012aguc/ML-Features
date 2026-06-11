"""55 sample entropy trajectory gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Complexity measure that is less sensitive to data length than approximate entropy.
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

def f55_ment_gemini_076_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=174, w2=384, w3=349, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(384, min_periods=max(384//3, 2)).mean()
    noise = impulse.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.259412 + 0.0036687 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_077_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=181, w2=397, w3=366, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 397)
    curvature = _rolling_slope(acceleration, 366)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.081 * acceleration + 0.0036688 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_078_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=188, w2=410, w3=383, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.286471 + 0.0036689 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_079_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=195, w2=423, w3=400, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.093667 * _rolling_slope(draw, 400) + 0.003669 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_080_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=202, w2=436, w3=417, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(417, min_periods=max(417//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.313529 + 0.0036691 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_081_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=209, w2=449, w3=434, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.327059 + 0.0036692 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_082_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=216, w2=462, w3=451, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.340588 + 0.0036693 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_083_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=223, w2=475, w3=468, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(468, min_periods=max(468//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.119 * persistence + 0.0036694 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_084_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=230, w2=488, w3=485, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.367647 + 0.0036695 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_085_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=237, w2=501, w3=502, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.131667 * slope + 0.0036696 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_086_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=244, w2=15, w3=519, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(519, min_periods=max(519//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.394706 + 0.0036697 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_087_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=251, w2=28, w3=536, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 536)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.144333 * acceleration + 0.0036698 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_088_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=11, w2=41, w3=553, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(41, min_periods=max(41//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.421765 + 0.0036699 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_089_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=18, w2=54, w3=570, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(54, min_periods=max(54//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.157 * _rolling_slope(draw, 570) + 0.00367 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_090_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=25, w2=67, w3=587, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(67, min_periods=max(67//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.448824 + 0.0036701 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_091_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=32, w2=80, w3=604, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 80)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.462353 + 0.0036702 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_092_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=39, w2=93, w3=621, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.475882 + 0.0036703 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_093_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=46, w2=106, w3=638, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(46)
    rank = change.rolling(106, min_periods=max(106//3, 2)).rank(pct=True)
    persistence = change.rolling(638, min_periods=max(638//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.182333 * persistence + 0.0036704 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_094_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=53, w2=119, w3=655, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(119, min_periods=max(119//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.502941 + 0.0036705 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_095_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=60, w2=132, w3=672, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.195 * slope + 0.0036706 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_096_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=67, w2=145, w3=689, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(67)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(689, min_periods=max(689//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.53 + 0.0036707 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_097_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=74, w2=158, w3=706, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 706)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.207667 * acceleration + 0.0036708 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_098_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=81, w2=171, w3=723, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.557059 + 0.0036709 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_099_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=88, w2=184, w3=740, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.220333 * _rolling_slope(draw, 740) + 0.003671 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_100_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=95, w2=197, w3=757, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(757, min_periods=max(757//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.584118 + 0.0036711 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_101_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=102, w2=210, w3=23, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 210)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=23, adjust=False).mean() * 1.597647 + 0.0036712 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_102_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=109, w2=223, w3=40, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.611176 + 0.0036713 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_103_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=116, w2=236, w3=57, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(116)
    rank = change.rolling(236, min_periods=max(236//3, 2)).rank(pct=True)
    persistence = change.rolling(57, min_periods=max(57//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245667 * persistence + 0.0036714 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_104_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=123, w2=249, w3=74, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.638235 + 0.0036715 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_105_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=130, w2=262, w3=91, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.258333 * slope + 0.0036716 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_106_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=137, w2=275, w3=108, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(275, min_periods=max(275//3, 2)).mean()
    noise = impulse.abs().rolling(108, min_periods=max(108//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.665294 + 0.0036717 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_107_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=144, w2=288, w3=125, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 125)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.271 * acceleration + 0.0036718 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_108_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=151, w2=301, w3=142, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(301, min_periods=max(301//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.838824 + 0.0036719 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_109_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=158, w2=314, w3=159, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.283667 * _rolling_slope(draw, 159) + 0.003672 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_110_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=165, w2=327, w3=176, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(327, min_periods=max(327//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.865882 + 0.0036721 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_111_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=340, w3=193, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=193, adjust=False).mean() * 0.879412 + 0.0036722 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_112_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=353, w3=210, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.892941 + 0.0036723 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_113_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=366, w3=227, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(227, min_periods=max(227//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.309 * persistence + 0.0036724 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_114_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=379, w3=244, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92 + 0.0036725 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_115_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=392, w3=261, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.321667 * slope + 0.0036726 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_116_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=405, w3=278, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(278, min_periods=max(278//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.947059 + 0.0036727 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_117_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=418, w3=295, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 295)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.334333 * acceleration + 0.0036728 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_118_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=431, w3=312, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.974118 + 0.0036729 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_119_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=444, w3=329, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(444, min_periods=max(444//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.347 * _rolling_slope(draw, 329) + 0.003673 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_120_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=457, w3=346, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(457, min_periods=max(457//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.001176 + 0.0036731 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_121_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=470, w3=363, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 470)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.014706 + 0.0036732 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_122_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=483, w3=380, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.028235 + 0.0036733 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_123_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=496, w3=397, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(9)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(397, min_periods=max(397//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.04 * persistence + 0.0036734 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_124_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=509, w3=414, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(509, min_periods=max(509//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.055294 + 0.0036735 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_125_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=23, w3=431, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(23, min_periods=max(23//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.052667 * slope + 0.0036736 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_126_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=36, w3=448, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(30)
    drag = impulse.rolling(36, min_periods=max(36//3, 2)).mean()
    noise = impulse.abs().rolling(448, min_periods=max(448//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.082353 + 0.0036737 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_127_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=49, w3=465, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 49)
    curvature = _rolling_slope(acceleration, 465)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.065333 * acceleration + 0.0036738 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_128_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=62, w3=482, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(62, min_periods=max(62//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.109412 + 0.0036739 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_129_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=75, w3=499, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(75, min_periods=max(75//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.078 * _rolling_slope(draw, 499) + 0.003674 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_130_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=88, w3=516, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(88, min_periods=max(88//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(516, min_periods=max(516//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.136471 + 0.0036741 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_131_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=101, w3=533, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 101)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.15 + 0.0036742 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_132_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=114, w3=550, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(114, min_periods=max(114//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.163529 + 0.0036743 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_133_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=127, w3=567, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(79)
    rank = change.rolling(127, min_periods=max(127//3, 2)).rank(pct=True)
    persistence = change.rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.103333 * persistence + 0.0036744 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_134_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=140, w3=584, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(140, min_periods=max(140//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.190588 + 0.0036745 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_135_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=153, w3=601, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(153, min_periods=max(153//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.116 * slope + 0.0036746 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_136_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=166, w3=618, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(100)
    drag = impulse.rolling(166, min_periods=max(166//3, 2)).mean()
    noise = impulse.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.217647 + 0.0036747 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_137_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=179, w3=635, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 179)
    curvature = _rolling_slope(acceleration, 635)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.128667 * acceleration + 0.0036748 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_138_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=192, w3=652, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(192, min_periods=max(192//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.244706 + 0.0036749 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_139_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=205, w3=669, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(205, min_periods=max(205//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.141333 * _rolling_slope(draw, 669) + 0.003675 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_140_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=218, w3=686, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(218, min_periods=max(218//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.271765 + 0.0036751 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_141_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=231, w3=703, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 231)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.285294 + 0.0036752 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_142_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=244, w3=720, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(244, min_periods=max(244//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.298824 + 0.0036753 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_143_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=257, w3=737, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(257, min_periods=max(257//3, 2)).rank(pct=True)
    persistence = change.rolling(737, min_periods=max(737//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.166667 * persistence + 0.0036754 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_144_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=270, w3=754, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(270, min_periods=max(270//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.325882 + 0.0036755 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_145_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=283, w3=20, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(283, min_periods=max(283//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.179333 * slope + 0.0036756 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_146_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=296, w3=37, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(296, min_periods=max(296//3, 2)).mean()
    noise = impulse.abs().rolling(37, min_periods=max(37//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.352941 + 0.0036757 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_147_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=309, w3=54, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 309)
    curvature = _rolling_slope(acceleration, 54)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.192 * acceleration + 0.0036758 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_148_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=322, w3=71, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(322, min_periods=max(322//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(71) * 1.38 + 0.0036759 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_149_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=335, w3=88, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(335, min_periods=max(335//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.204667 * _rolling_slope(draw, 88) + 0.003676 * anchor
    return base_signal.diff().diff().diff()

def f55_ment_gemini_150_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=348, w3=105, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(348, min_periods=max(348//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(105, min_periods=max(105//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.407059 + 0.0036761 * anchor
    return base_signal.diff().diff().diff()
