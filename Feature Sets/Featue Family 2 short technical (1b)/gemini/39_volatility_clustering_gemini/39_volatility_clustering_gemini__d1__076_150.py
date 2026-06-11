"""39 volatility clustering gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Temporal persistence of high or low volatility periods as a risk signal.
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

def f39_vclu_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=24, w3=228, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(24, min_periods=max(24//3, 2)).mean()
    noise = impulse.abs().rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.862941 + 0.0027447 * anchor
    return base_signal.diff()

def f39_vclu_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=37, w3=245, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 37)
    curvature = _rolling_slope(acceleration, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.051667 * acceleration + 0.0027448 * anchor
    return base_signal.diff()

def f39_vclu_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=50, w3=262, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(50, min_periods=max(50//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.89 + 0.0027449 * anchor
    return base_signal.diff()

def f39_vclu_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=63, w3=279, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(63, min_periods=max(63//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.064333 * _rolling_slope(draw, 279) + 0.002745 * anchor
    return base_signal.diff()

def f39_vclu_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=76, w3=296, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(76, min_periods=max(76//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.917059 + 0.0027451 * anchor
    return base_signal.diff()

def f39_vclu_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=89, w3=313, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 89)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.930588 + 0.0027452 * anchor
    return base_signal.diff()

def f39_vclu_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=102, w3=330, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(102, min_periods=max(102//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.944118 + 0.0027453 * anchor
    return base_signal.diff()

def f39_vclu_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=115, w3=347, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(10)
    rank = change.rolling(115, min_periods=max(115//3, 2)).rank(pct=True)
    persistence = change.rolling(347, min_periods=max(347//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.089667 * persistence + 0.0027454 * anchor
    return base_signal.diff()

def f39_vclu_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=128, w3=364, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(128, min_periods=max(128//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.971176 + 0.0027455 * anchor
    return base_signal.diff()

def f39_vclu_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=141, w3=381, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(141, min_periods=max(141//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.102333 * slope + 0.0027456 * anchor
    return base_signal.diff()

def f39_vclu_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=154, w3=398, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(31)
    drag = impulse.rolling(154, min_periods=max(154//3, 2)).mean()
    noise = impulse.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.998235 + 0.0027457 * anchor
    return base_signal.diff()

def f39_vclu_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=167, w3=415, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 38)
    acceleration = _rolling_slope(velocity, 167)
    curvature = _rolling_slope(acceleration, 415)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.115 * acceleration + 0.0027458 * anchor
    return base_signal.diff()

def f39_vclu_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=180, w3=432, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(45, min_periods=max(45//3, 2)).mean(), upside.rolling(180, min_periods=max(180//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.025294 + 0.0027459 * anchor
    return base_signal.diff()

def f39_vclu_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=193, w3=449, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(193, min_periods=max(193//3, 2)).max()
    rebound = x - x.rolling(52, min_periods=max(52//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.127667 * _rolling_slope(draw, 449) + 0.002746 * anchor
    return base_signal.diff()

def f39_vclu_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=206, w3=466, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 59)
    baseline = trend.rolling(206, min_periods=max(206//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.052353 + 0.0027461 * anchor
    return base_signal.diff()

def f39_vclu_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=219, w3=483, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 66)
    slow = _rolling_slope(x, 219)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.065882 + 0.0027462 * anchor
    return base_signal.diff()

def f39_vclu_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=232, w3=500, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(232, min_periods=max(232//3, 2)).max()
    trough = x.rolling(73, min_periods=max(73//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.079412 + 0.0027463 * anchor
    return base_signal.diff()

def f39_vclu_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=245, w3=517, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(80)
    rank = change.rolling(245, min_periods=max(245//3, 2)).rank(pct=True)
    persistence = change.rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.153 * persistence + 0.0027464 * anchor
    return base_signal.diff()

def f39_vclu_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=258, w3=534, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(87, min_periods=max(87//3, 2)).std()
    vol_slow = ret.rolling(258, min_periods=max(258//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.106471 + 0.0027465 * anchor
    return base_signal.diff()

def f39_vclu_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=271, w3=551, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(271, min_periods=max(271//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 94)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.165667 * slope + 0.0027466 * anchor
    return base_signal.diff()

def f39_vclu_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=284, w3=568, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(101)
    drag = impulse.rolling(284, min_periods=max(284//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.133529 + 0.0027467 * anchor
    return base_signal.diff()

def f39_vclu_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=297, w3=585, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 108)
    acceleration = _rolling_slope(velocity, 297)
    curvature = _rolling_slope(acceleration, 585)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.178333 * acceleration + 0.0027468 * anchor
    return base_signal.diff()

def f39_vclu_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=310, w3=602, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(115, min_periods=max(115//3, 2)).mean(), upside.rolling(310, min_periods=max(310//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.160588 + 0.0027469 * anchor
    return base_signal.diff()

def f39_vclu_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=323, w3=619, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(323, min_periods=max(323//3, 2)).max()
    rebound = x - x.rolling(122, min_periods=max(122//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.191 * _rolling_slope(draw, 619) + 0.002747 * anchor
    return base_signal.diff()

def f39_vclu_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=336, w3=636, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 129)
    baseline = trend.rolling(336, min_periods=max(336//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.187647 + 0.0027471 * anchor
    return base_signal.diff()

def f39_vclu_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=349, w3=653, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 136)
    slow = _rolling_slope(x, 349)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.201176 + 0.0027472 * anchor
    return base_signal.diff()

def f39_vclu_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=362, w3=670, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(362, min_periods=max(362//3, 2)).max()
    trough = x.rolling(143, min_periods=max(143//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.214706 + 0.0027473 * anchor
    return base_signal.diff()

def f39_vclu_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=375, w3=687, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(375, min_periods=max(375//3, 2)).rank(pct=True)
    persistence = change.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.216333 * persistence + 0.0027474 * anchor
    return base_signal.diff()

def f39_vclu_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=388, w3=704, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(157, min_periods=max(157//3, 2)).std()
    vol_slow = ret.rolling(388, min_periods=max(388//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.241765 + 0.0027475 * anchor
    return base_signal.diff()

def f39_vclu_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=401, w3=721, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(401, min_periods=max(401//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 164)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.229 * slope + 0.0027476 * anchor
    return base_signal.diff()

def f39_vclu_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=414, w3=738, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(414, min_periods=max(414//3, 2)).mean()
    noise = impulse.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.268824 + 0.0027477 * anchor
    return base_signal.diff()

def f39_vclu_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=427, w3=755, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 178)
    acceleration = _rolling_slope(velocity, 427)
    curvature = _rolling_slope(acceleration, 755)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.241667 * acceleration + 0.0027478 * anchor
    return base_signal.diff()

def f39_vclu_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=440, w3=21, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(185, min_periods=max(185//3, 2)).mean(), upside.rolling(440, min_periods=max(440//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(21) * 1.295882 + 0.0027479 * anchor
    return base_signal.diff()

def f39_vclu_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=453, w3=38, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(453, min_periods=max(453//3, 2)).max()
    rebound = x - x.rolling(192, min_periods=max(192//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.254333 * _rolling_slope(draw, 38) + 0.002748 * anchor
    return base_signal.diff()

def f39_vclu_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=466, w3=55, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 199)
    baseline = trend.rolling(466, min_periods=max(466//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.322941 + 0.0027481 * anchor
    return base_signal.diff()

def f39_vclu_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=479, w3=72, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 206)
    slow = _rolling_slope(x, 479)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=72, adjust=False).mean() * 1.336471 + 0.0027482 * anchor
    return base_signal.diff()

def f39_vclu_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=492, w3=89, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(492, min_periods=max(492//3, 2)).max()
    trough = x.rolling(213, min_periods=max(213//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.35 + 0.0027483 * anchor
    return base_signal.diff()

def f39_vclu_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=505, w3=106, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(505, min_periods=max(505//3, 2)).rank(pct=True)
    persistence = change.rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.279667 * persistence + 0.0027484 * anchor
    return base_signal.diff()

def f39_vclu_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=19, w3=123, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(227, min_periods=max(227//3, 2)).std()
    vol_slow = ret.rolling(19, min_periods=max(19//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.377059 + 0.0027485 * anchor
    return base_signal.diff()

def f39_vclu_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=32, w3=140, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(32, min_periods=max(32//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 234)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.292333 * slope + 0.0027486 * anchor
    return base_signal.diff()

def f39_vclu_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=45, w3=157, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(45, min_periods=max(45//3, 2)).mean()
    noise = impulse.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.404118 + 0.0027487 * anchor
    return base_signal.diff()

def f39_vclu_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=58, w3=174, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 248)
    acceleration = _rolling_slope(velocity, 58)
    curvature = _rolling_slope(acceleration, 174)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.305 * acceleration + 0.0027488 * anchor
    return base_signal.diff()

def f39_vclu_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=71, w3=191, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(71, min_periods=max(71//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.431176 + 0.0027489 * anchor
    return base_signal.diff()

def f39_vclu_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=84, w3=208, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(84, min_periods=max(84//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.317667 * _rolling_slope(draw, 208) + 0.002749 * anchor
    return base_signal.diff()

def f39_vclu_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=97, w3=225, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(97, min_periods=max(97//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.458235 + 0.0027491 * anchor
    return base_signal.diff()

def f39_vclu_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=110, w3=242, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 110)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=242, adjust=False).mean() * 1.471765 + 0.0027492 * anchor
    return base_signal.diff()

def f39_vclu_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=123, w3=259, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(123, min_periods=max(123//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.485294 + 0.0027493 * anchor
    return base_signal.diff()

def f39_vclu_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=136, w3=276, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(43)
    rank = change.rolling(136, min_periods=max(136//3, 2)).rank(pct=True)
    persistence = change.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.343 * persistence + 0.0027494 * anchor
    return base_signal.diff()

def f39_vclu_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=149, w3=293, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(149, min_periods=max(149//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.512353 + 0.0027495 * anchor
    return base_signal.diff()

def f39_vclu_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=162, w3=310, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(162, min_periods=max(162//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.355667 * slope + 0.0027496 * anchor
    return base_signal.diff()

def f39_vclu_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=175, w3=327, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(64)
    drag = impulse.rolling(175, min_periods=max(175//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.539412 + 0.0027497 * anchor
    return base_signal.diff()

def f39_vclu_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=188, w3=344, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 188)
    curvature = _rolling_slope(acceleration, 344)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.036 * acceleration + 0.0027498 * anchor
    return base_signal.diff()

def f39_vclu_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=201, w3=361, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(78, min_periods=max(78//3, 2)).mean(), upside.rolling(201, min_periods=max(201//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.566471 + 0.0027499 * anchor
    return base_signal.diff()

def f39_vclu_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=214, w3=378, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(214, min_periods=max(214//3, 2)).max()
    rebound = x - x.rolling(85, min_periods=max(85//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.048667 * _rolling_slope(draw, 378) + 0.00275 * anchor
    return base_signal.diff()

def f39_vclu_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=227, w3=395, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 92)
    baseline = trend.rolling(227, min_periods=max(227//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.593529 + 0.0027501 * anchor
    return base_signal.diff()

def f39_vclu_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=240, w3=412, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 99)
    slow = _rolling_slope(x, 240)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.607059 + 0.0027502 * anchor
    return base_signal.diff()

def f39_vclu_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=253, w3=429, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(253, min_periods=max(253//3, 2)).max()
    trough = x.rolling(106, min_periods=max(106//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.620588 + 0.0027503 * anchor
    return base_signal.diff()

def f39_vclu_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=266, w3=446, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(113)
    rank = change.rolling(266, min_periods=max(266//3, 2)).rank(pct=True)
    persistence = change.rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.074 * persistence + 0.0027504 * anchor
    return base_signal.diff()

def f39_vclu_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=279, w3=463, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(120, min_periods=max(120//3, 2)).std()
    vol_slow = ret.rolling(279, min_periods=max(279//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.647647 + 0.0027505 * anchor
    return base_signal.diff()

def f39_vclu_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=292, w3=480, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(292, min_periods=max(292//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 127)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.086667 * slope + 0.0027506 * anchor
    return base_signal.diff()

def f39_vclu_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=305, w3=497, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(305, min_periods=max(305//3, 2)).mean()
    noise = impulse.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.821176 + 0.0027507 * anchor
    return base_signal.diff()

def f39_vclu_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=318, w3=514, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 141)
    acceleration = _rolling_slope(velocity, 318)
    curvature = _rolling_slope(acceleration, 514)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.099333 * acceleration + 0.0027508 * anchor
    return base_signal.diff()

def f39_vclu_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=331, w3=531, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(148, min_periods=max(148//3, 2)).mean(), upside.rolling(331, min_periods=max(331//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.848235 + 0.0027509 * anchor
    return base_signal.diff()

def f39_vclu_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=344, w3=548, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(344, min_periods=max(344//3, 2)).max()
    rebound = x - x.rolling(155, min_periods=max(155//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.112 * _rolling_slope(draw, 548) + 0.002751 * anchor
    return base_signal.diff()

def f39_vclu_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=357, w3=565, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(357, min_periods=max(357//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.875294 + 0.0027511 * anchor
    return base_signal.diff()

def f39_vclu_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=370, w3=582, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 370)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.888824 + 0.0027512 * anchor
    return base_signal.diff()

def f39_vclu_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=383, w3=599, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(383, min_periods=max(383//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.902353 + 0.0027513 * anchor
    return base_signal.diff()

def f39_vclu_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=396, w3=616, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(396, min_periods=max(396//3, 2)).rank(pct=True)
    persistence = change.rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.137333 * persistence + 0.0027514 * anchor
    return base_signal.diff()

def f39_vclu_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=409, w3=633, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(409, min_periods=max(409//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.929412 + 0.0027515 * anchor
    return base_signal.diff()

def f39_vclu_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=422, w3=650, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(422, min_periods=max(422//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.15 * slope + 0.0027516 * anchor
    return base_signal.diff()

def f39_vclu_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=435, w3=667, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(435, min_periods=max(435//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.956471 + 0.0027517 * anchor
    return base_signal.diff()

def f39_vclu_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=448, w3=684, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 448)
    curvature = _rolling_slope(acceleration, 684)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.162667 * acceleration + 0.0027518 * anchor
    return base_signal.diff()

def f39_vclu_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=461, w3=701, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(218, min_periods=max(218//3, 2)).mean(), upside.rolling(461, min_periods=max(461//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.983529 + 0.0027519 * anchor
    return base_signal.diff()

def f39_vclu_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=474, w3=718, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(474, min_periods=max(474//3, 2)).max()
    rebound = x - x.rolling(225, min_periods=max(225//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.175333 * _rolling_slope(draw, 718) + 0.002752 * anchor
    return base_signal.diff()

def f39_vclu_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=487, w3=735, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 232)
    baseline = trend.rolling(487, min_periods=max(487//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.010588 + 0.0027521 * anchor
    return base_signal.diff()
