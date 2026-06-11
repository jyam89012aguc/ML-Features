"""59 structural randomness trapping gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of market phases where noise overwhelms signal, trapping traders.
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

def f59_sran_gemini_076_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=415, w3=625, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(62)
    drag = impulse.rolling(415, min_periods=max(415//3, 2)).mean()
    noise = impulse.abs().rolling(625, min_periods=max(625//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.317647 + 0.0038647 * anchor
    return base_signal.diff()

def f59_sran_gemini_077_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=428, w3=642, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 69)
    acceleration = _rolling_slope(velocity, 428)
    curvature = _rolling_slope(acceleration, 642)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.198 * acceleration + 0.0038648 * anchor
    return base_signal.diff()

def f59_sran_gemini_078_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=441, w3=659, lag=34)."""
    rel = _safe_div(open.shift(34), high.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 76)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.204333 * pressure.rolling(659, min_periods=max(659//3, 2)).mean() + 0.0038649 * anchor
    return base_signal.diff()

def f59_sran_gemini_079_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=454, w3=676, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(83, min_periods=max(83//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.358235 + 0.003865 * anchor
    return base_signal.diff()

def f59_sran_gemini_080_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=467, w3=693, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(high.abs() + 1.0).shift(0)
    corr = a.rolling(467, min_periods=max(467//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 90)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.371765 + 0.0038651 * anchor
    return base_signal.diff()

def f59_sran_gemini_081_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=480, w3=710, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    cover = _safe_div(a.rolling(97, min_periods=max(97//3, 2)).mean(), b.abs().rolling(480, min_periods=max(480//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.223333 * _rolling_slope(cover, 97) + 0.0038652 * anchor
    return base_signal.diff()

def f59_sran_gemini_082_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=493, w3=727, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(high.abs() + 1.0).shift(2)
    z = _safe_log(low.abs() + 1.0).shift(2)
    basket = x - 0.229667 * y + 0.770333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 104) - _rolling_slope(basket, 493) + 0.0038653 * anchor
    return base_signal.diff()

def f59_sran_gemini_083_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=506, w3=744, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(506, min_periods=max(506//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.412353 + 0.0038654 * anchor
    return base_signal.diff()

def f59_sran_gemini_084_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=20, w3=761, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(20, min_periods=max(20//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.242333 * _rolling_slope(draw, 761) + 0.0038655 * anchor
    return base_signal.diff()

def f59_sran_gemini_085_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=125, w2=33, w3=27, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(high.abs() + 1.0).shift(8)
    imbalance = a.diff(125) - b.diff(33)
    stress = imbalance.rolling(27, min_periods=max(27//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.439412 + 0.0038656 * anchor
    return base_signal.diff()

def f59_sran_gemini_086_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=132, w2=46, w3=44, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(46, min_periods=max(46//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.452941 + 0.0038657 * anchor
    return base_signal.diff()

def f59_sran_gemini_087_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=139, w2=59, w3=61, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 59)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=61, adjust=False).mean() * 1.466471 + 0.0038658 * anchor
    return base_signal.diff()

def f59_sran_gemini_088_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=146, w2=72, w3=78, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(72, min_periods=max(72//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.48 + 0.0038659 * anchor
    return base_signal.diff()

def f59_sran_gemini_089_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=153, w2=85, w3=95, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(85, min_periods=max(85//3, 2)).rank(pct=True)
    persistence = change.rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.274 * persistence + 0.003866 * anchor
    return base_signal.diff()

def f59_sran_gemini_090_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=160, w2=98, w3=112, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(98, min_periods=max(98//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.507059 + 0.0038661 * anchor
    return base_signal.diff()

def f59_sran_gemini_091_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=167, w2=111, w3=129, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.286667 * slope + 0.0038662 * anchor
    return base_signal.diff()

def f59_sran_gemini_092_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=174, w2=124, w3=146, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(124, min_periods=max(124//3, 2)).mean()
    noise = impulse.abs().rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.534118 + 0.0038663 * anchor
    return base_signal.diff()

def f59_sran_gemini_093_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=181, w2=137, w3=163, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 137)
    curvature = _rolling_slope(acceleration, 163)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.299333 * acceleration + 0.0038664 * anchor
    return base_signal.diff()

def f59_sran_gemini_094_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=188, w2=150, w3=180, lag=5)."""
    rel = _safe_div(open.shift(5), high.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 188)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.305667 * pressure.rolling(180, min_periods=max(180//3, 2)).mean() + 0.0038665 * anchor
    return base_signal.diff()

def f59_sran_gemini_095_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=195, w2=163, w3=197, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(195, min_periods=max(195//3, 2)).mean())
    decay = spread.ewm(span=163, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.574706 + 0.0038666 * anchor
    return base_signal.diff()

def f59_sran_gemini_096_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=202, w2=176, w3=214, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(high.abs() + 1.0).shift(13)
    corr = a.rolling(176, min_periods=max(176//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 202)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.588235 + 0.0038667 * anchor
    return base_signal.diff()

def f59_sran_gemini_097_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=209, w2=189, w3=231, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    cover = _safe_div(a.rolling(209, min_periods=max(209//3, 2)).mean(), b.abs().rolling(189, min_periods=max(189//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.324667 * _rolling_slope(cover, 209) + 0.0038668 * anchor
    return base_signal.diff()

def f59_sran_gemini_098_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=216, w2=202, w3=248, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(high.abs() + 1.0).shift(34)
    z = _safe_log(low.abs() + 1.0).shift(34)
    basket = x - 0.331 * y + 0.669000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 216) - _rolling_slope(basket, 202) + 0.0038669 * anchor
    return base_signal.diff()

def f59_sran_gemini_099_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=223, w2=215, w3=265, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(223, min_periods=max(223//3, 2)).mean(), upside.rolling(215, min_periods=max(215//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.628824 + 0.003867 * anchor
    return base_signal.diff()

def f59_sran_gemini_100_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=230, w2=228, w3=282, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(228, min_periods=max(228//3, 2)).max()
    rebound = x - x.rolling(230, min_periods=max(230//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.343667 * _rolling_slope(draw, 282) + 0.0038671 * anchor
    return base_signal.diff()

def f59_sran_gemini_101_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=237, w2=241, w3=299, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(high.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(299, min_periods=max(299//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.655882 + 0.0038672 * anchor
    return base_signal.diff()

def f59_sran_gemini_102_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=244, w2=254, w3=316, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 244)
    baseline = trend.rolling(254, min_periods=max(254//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.669412 + 0.0038673 * anchor
    return base_signal.diff()

def f59_sran_gemini_103_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=251, w2=267, w3=333, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 251)
    slow = _rolling_slope(x, 267)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.829412 + 0.0038674 * anchor
    return base_signal.diff()

def f59_sran_gemini_104_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=11, w2=280, w3=350, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(280, min_periods=max(280//3, 2)).max()
    trough = x.rolling(11, min_periods=max(11//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.842941 + 0.0038675 * anchor
    return base_signal.diff()

def f59_sran_gemini_105_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=18, w2=293, w3=367, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(18)
    rank = change.rolling(293, min_periods=max(293//3, 2)).rank(pct=True)
    persistence = change.rolling(367, min_periods=max(367//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.043 * persistence + 0.0038676 * anchor
    return base_signal.diff()

def f59_sran_gemini_106_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=25, w2=306, w3=384, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(25, min_periods=max(25//3, 2)).std()
    vol_slow = ret.rolling(306, min_periods=max(306//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.87 + 0.0038677 * anchor
    return base_signal.diff()

def f59_sran_gemini_107_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=32, w2=319, w3=401, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(319, min_periods=max(319//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 32)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.055667 * slope + 0.0038678 * anchor
    return base_signal.diff()

def f59_sran_gemini_108_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=39, w2=332, w3=418, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(39)
    drag = impulse.rolling(332, min_periods=max(332//3, 2)).mean()
    noise = impulse.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.897059 + 0.0038679 * anchor
    return base_signal.diff()

def f59_sran_gemini_109_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=46, w2=345, w3=435, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 46)
    acceleration = _rolling_slope(velocity, 345)
    curvature = _rolling_slope(acceleration, 435)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.068333 * acceleration + 0.003868 * anchor
    return base_signal.diff()

def f59_sran_gemini_110_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=53, w2=358, w3=452, lag=0)."""
    rel = _safe_div(open.shift(0), high.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 53)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.074667 * pressure.rolling(452, min_periods=max(452//3, 2)).mean() + 0.0038681 * anchor
    return base_signal.diff()

def f59_sran_gemini_111_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=60, w2=371, w3=469, lag=1)."""
    a = open.shift(1)
    b = high.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(60, min_periods=max(60//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.937647 + 0.0038682 * anchor
    return base_signal.diff()

def f59_sran_gemini_112_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=67, w2=384, w3=486, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(high.abs() + 1.0).shift(2)
    corr = a.rolling(384, min_periods=max(384//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 67)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.951176 + 0.0038683 * anchor
    return base_signal.diff()

def f59_sran_gemini_113_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=74, w2=397, w3=503, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    cover = _safe_div(a.rolling(74, min_periods=max(74//3, 2)).mean(), b.abs().rolling(397, min_periods=max(397//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.093667 * _rolling_slope(cover, 74) + 0.0038684 * anchor
    return base_signal.diff()

def f59_sran_gemini_114_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=81, w2=410, w3=520, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(high.abs() + 1.0).shift(5)
    z = _safe_log(low.abs() + 1.0).shift(5)
    basket = x - 0.1 * y + 0.900000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 81) - _rolling_slope(basket, 410) + 0.0038685 * anchor
    return base_signal.diff()

def f59_sran_gemini_115_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=88, w2=423, w3=537, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(423, min_periods=max(423//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.991765 + 0.0038686 * anchor
    return base_signal.diff()

def f59_sran_gemini_116_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=95, w2=436, w3=554, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(436, min_periods=max(436//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.112667 * _rolling_slope(draw, 554) + 0.0038687 * anchor
    return base_signal.diff()

def f59_sran_gemini_117_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=102, w2=449, w3=571, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(high.abs() + 1.0).shift(21)
    imbalance = a.diff(102) - b.diff(126)
    stress = imbalance.rolling(571, min_periods=max(571//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.018824 + 0.0038688 * anchor
    return base_signal.diff()

def f59_sran_gemini_118_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=109, w2=462, w3=588, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(462, min_periods=max(462//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(588, min_periods=max(588//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.032353 + 0.0038689 * anchor
    return base_signal.diff()

def f59_sran_gemini_119_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=116, w2=475, w3=605, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 475)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.045882 + 0.003869 * anchor
    return base_signal.diff()

def f59_sran_gemini_120_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=123, w2=488, w3=622, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(488, min_periods=max(488//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.059412 + 0.0038691 * anchor
    return base_signal.diff()

def f59_sran_gemini_121_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=130, w2=501, w3=639, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(501, min_periods=max(501//3, 2)).rank(pct=True)
    persistence = change.rolling(639, min_periods=max(639//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.144333 * persistence + 0.0038692 * anchor
    return base_signal.diff()

def f59_sran_gemini_122_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=137, w2=15, w3=656, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(15, min_periods=max(15//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.086471 + 0.0038693 * anchor
    return base_signal.diff()

def f59_sran_gemini_123_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=144, w2=28, w3=673, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(28, min_periods=max(28//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.157 * slope + 0.0038694 * anchor
    return base_signal.diff()

def f59_sran_gemini_124_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=151, w2=41, w3=690, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(41, min_periods=max(41//3, 2)).mean()
    noise = impulse.abs().rolling(690, min_periods=max(690//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.113529 + 0.0038695 * anchor
    return base_signal.diff()

def f59_sran_gemini_125_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=158, w2=54, w3=707, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 54)
    curvature = _rolling_slope(acceleration, 707)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.169667 * acceleration + 0.0038696 * anchor
    return base_signal.diff()

def f59_sran_gemini_126_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=165, w2=67, w3=724, lag=13)."""
    rel = _safe_div(open.shift(13), high.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 165)
    pressure = rel_log.diff(67)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.176 * pressure.rolling(724, min_periods=max(724//3, 2)).mean() + 0.0038697 * anchor
    return base_signal.diff()

def f59_sran_gemini_127_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=172, w2=80, w3=741, lag=21)."""
    a = open.shift(21)
    b = high.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(172, min_periods=max(172//3, 2)).mean())
    decay = spread.ewm(span=80, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.154118 + 0.0038698 * anchor
    return base_signal.diff()

def f59_sran_gemini_128_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=179, w2=93, w3=758, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(high.abs() + 1.0).shift(34)
    corr = a.rolling(93, min_periods=max(93//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 179)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.167647 + 0.0038699 * anchor
    return base_signal.diff()

def f59_sran_gemini_129_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=186, w2=106, w3=24, lag=55)."""
    a = open.shift(55)
    b = high.shift(55)
    cover = _safe_div(a.rolling(186, min_periods=max(186//3, 2)).mean(), b.abs().rolling(106, min_periods=max(106//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(24) + 0.195 * _rolling_slope(cover, 186) + 0.00387 * anchor
    return base_signal.diff()

def f59_sran_gemini_130_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=193, w2=119, w3=41, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(high.abs() + 1.0).shift(0)
    z = _safe_log(low.abs() + 1.0).shift(0)
    basket = x - 0.201333 * y + 0.798667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 193) - _rolling_slope(basket, 119) + 0.0038701 * anchor
    return base_signal.diff()

def f59_sran_gemini_131_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=200, w2=132, w3=58, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(200, min_periods=max(200//3, 2)).mean(), upside.rolling(132, min_periods=max(132//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(58) * 1.208235 + 0.0038702 * anchor
    return base_signal.diff()

def f59_sran_gemini_132_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=207, w2=145, w3=75, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(145, min_periods=max(145//3, 2)).max()
    rebound = x - x.rolling(207, min_periods=max(207//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.214 * _rolling_slope(draw, 75) + 0.0038703 * anchor
    return base_signal.diff()

def f59_sran_gemini_133_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=214, w2=158, w3=92, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(high.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.235294 + 0.0038704 * anchor
    return base_signal.diff()

def f59_sran_gemini_134_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=221, w2=171, w3=109, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 221)
    baseline = trend.rolling(171, min_periods=max(171//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(109, min_periods=max(109//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.248824 + 0.0038705 * anchor
    return base_signal.diff()

def f59_sran_gemini_135_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=228, w2=184, w3=126, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 228)
    slow = _rolling_slope(x, 184)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=126, adjust=False).mean() * 1.262353 + 0.0038706 * anchor
    return base_signal.diff()

def f59_sran_gemini_136_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=235, w2=197, w3=143, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(197, min_periods=max(197//3, 2)).max()
    trough = x.rolling(235, min_periods=max(235//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.275882 + 0.0038707 * anchor
    return base_signal.diff()

def f59_sran_gemini_137_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=242, w2=210, w3=160, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(210, min_periods=max(210//3, 2)).rank(pct=True)
    persistence = change.rolling(160, min_periods=max(160//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.245667 * persistence + 0.0038708 * anchor
    return base_signal.diff()

def f59_sran_gemini_138_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=249, w2=223, w3=177, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(249, min_periods=max(249//3, 2)).std()
    vol_slow = ret.rolling(223, min_periods=max(223//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.302941 + 0.0038709 * anchor
    return base_signal.diff()

def f59_sran_gemini_139_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=9, w2=236, w3=194, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(236, min_periods=max(236//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 9)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.258333 * slope + 0.003871 * anchor
    return base_signal.diff()

def f59_sran_gemini_140_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=16, w2=249, w3=211, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(16)
    drag = impulse.rolling(249, min_periods=max(249//3, 2)).mean()
    noise = impulse.abs().rolling(211, min_periods=max(211//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.33 + 0.0038711 * anchor
    return base_signal.diff()

def f59_sran_gemini_141_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=23, w2=262, w3=228, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 23)
    acceleration = _rolling_slope(velocity, 262)
    curvature = _rolling_slope(acceleration, 228)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.271 * acceleration + 0.0038712 * anchor
    return base_signal.diff()

def f59_sran_gemini_142_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=30, w2=275, w3=245, lag=2)."""
    rel = _safe_div(open.shift(2), high.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 30)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.277333 * pressure.rolling(245, min_periods=max(245//3, 2)).mean() + 0.0038713 * anchor
    return base_signal.diff()

def f59_sran_gemini_143_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=37, w2=288, w3=262, lag=3)."""
    a = open.shift(3)
    b = high.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(37, min_periods=max(37//3, 2)).mean())
    decay = spread.ewm(span=288, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.370588 + 0.0038714 * anchor
    return base_signal.diff()

def f59_sran_gemini_144_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=44, w2=301, w3=279, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(high.abs() + 1.0).shift(5)
    corr = a.rolling(301, min_periods=max(301//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 44)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.384118 + 0.0038715 * anchor
    return base_signal.diff()

def f59_sran_gemini_145_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=51, w2=314, w3=296, lag=8)."""
    a = open.shift(8)
    b = high.shift(8)
    cover = _safe_div(a.rolling(51, min_periods=max(51//3, 2)).mean(), b.abs().rolling(314, min_periods=max(314//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.296333 * _rolling_slope(cover, 51) + 0.0038716 * anchor
    return base_signal.diff()

def f59_sran_gemini_146_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=58, w2=327, w3=313, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(high.abs() + 1.0).shift(13)
    z = _safe_log(low.abs() + 1.0).shift(13)
    basket = x - 0.302667 * y + 0.697333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 58) - _rolling_slope(basket, 327) + 0.0038717 * anchor
    return base_signal.diff()

def f59_sran_gemini_147_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=65, w2=340, w3=330, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(65, min_periods=max(65//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.424706 + 0.0038718 * anchor
    return base_signal.diff()

def f59_sran_gemini_148_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=72, w2=353, w3=347, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(72, min_periods=max(72//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315333 * _rolling_slope(draw, 347) + 0.0038719 * anchor
    return base_signal.diff()

def f59_sran_gemini_149_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=79, w2=366, w3=364, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(high.abs() + 1.0).shift(55)
    imbalance = a.diff(79) - b.diff(126)
    stress = imbalance.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.451765 + 0.003872 * anchor
    return base_signal.diff()

def f59_sran_gemini_150_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=86, w2=379, w3=381, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 86)
    baseline = trend.rolling(379, min_periods=max(379//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.465294 + 0.0038721 * anchor
    return base_signal.diff()
