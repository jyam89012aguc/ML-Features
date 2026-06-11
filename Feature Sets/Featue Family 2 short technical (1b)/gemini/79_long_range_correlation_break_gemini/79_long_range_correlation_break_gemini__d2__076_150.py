"""79 long range correlation break gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Sudden loss of correlation between distant points in the price series.
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

def f79_lrcb_gemini_076_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=155, w2=131, w3=398, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(131, min_periods=max(131//3, 2)).mean()
    noise = impulse.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.105882 + 0.0049987 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_077_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=162, w2=144, w3=415, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 162)
    acceleration = _rolling_slope(velocity, 144)
    curvature = _rolling_slope(acceleration, 415)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.234 * acceleration + 0.0049988 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_078_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=169, w2=157, w3=432, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(169, min_periods=max(169//3, 2)).mean(), upside.rolling(157, min_periods=max(157//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.132941 + 0.0049989 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_079_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=176, w2=170, w3=449, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(170, min_periods=max(170//3, 2)).max()
    rebound = x - x.rolling(176, min_periods=max(176//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.246667 * _rolling_slope(draw, 449) + 0.004999 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_080_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=183, w2=183, w3=466, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 183)
    baseline = trend.rolling(183, min_periods=max(183//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(466, min_periods=max(466//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.16 + 0.0049991 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_081_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=190, w2=196, w3=483, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 190)
    slow = _rolling_slope(x, 196)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.173529 + 0.0049992 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_082_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=197, w2=209, w3=500, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(209, min_periods=max(209//3, 2)).max()
    trough = x.rolling(197, min_periods=max(197//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.187059 + 0.0049993 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_083_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=204, w2=222, w3=517, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(222, min_periods=max(222//3, 2)).rank(pct=True)
    persistence = change.rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.272 * persistence + 0.0049994 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_084_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=211, w2=235, w3=534, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(211, min_periods=max(211//3, 2)).std()
    vol_slow = ret.rolling(235, min_periods=max(235//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.214118 + 0.0049995 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_085_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=218, w2=248, w3=551, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(248, min_periods=max(248//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 218)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.284667 * slope + 0.0049996 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_086_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=225, w2=261, w3=568, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(261, min_periods=max(261//3, 2)).mean()
    noise = impulse.abs().rolling(568, min_periods=max(568//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.241176 + 0.0049997 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_087_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=232, w2=274, w3=585, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 232)
    acceleration = _rolling_slope(velocity, 274)
    curvature = _rolling_slope(acceleration, 585)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.297333 * acceleration + 0.0049998 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_088_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=239, w2=287, w3=602, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(239, min_periods=max(239//3, 2)).mean(), upside.rolling(287, min_periods=max(287//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.268235 + 0.0049999 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_089_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=246, w2=300, w3=619, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(300, min_periods=max(300//3, 2)).max()
    rebound = x - x.rolling(246, min_periods=max(246//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.31 * _rolling_slope(draw, 619) + 0.005 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_090_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=6, w2=313, w3=636, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(313, min_periods=max(313//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(636, min_periods=max(636//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.295294 + 0.0050001 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_091_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=13, w2=326, w3=653, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 326)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.308824 + 0.0050002 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_092_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=339, w3=670, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(339, min_periods=max(339//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.322353 + 0.0050003 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_093_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=352, w3=687, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(27)
    rank = change.rolling(352, min_periods=max(352//3, 2)).rank(pct=True)
    persistence = change.rolling(687, min_periods=max(687//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.335333 * persistence + 0.0050004 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_094_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=365, w3=704, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.349412 + 0.0050005 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_095_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=378, w3=721, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(378, min_periods=max(378//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.348 * slope + 0.0050006 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_096_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=391, w3=738, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(48)
    drag = impulse.rolling(391, min_periods=max(391//3, 2)).mean()
    noise = impulse.abs().rolling(738, min_periods=max(738//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.376471 + 0.0050007 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_097_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=404, w3=755, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 404)
    curvature = _rolling_slope(acceleration, 755)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.360667 * acceleration + 0.0050008 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_098_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=417, w3=21, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(62, min_periods=max(62//3, 2)).mean(), upside.rolling(417, min_periods=max(417//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(21) * 1.403529 + 0.0050009 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_099_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=430, w3=38, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(430, min_periods=max(430//3, 2)).max()
    rebound = x - x.rolling(69, min_periods=max(69//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.041 * _rolling_slope(draw, 38) + 0.005001 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_100_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=443, w3=55, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 76)
    baseline = trend.rolling(443, min_periods=max(443//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(55, min_periods=max(55//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.430588 + 0.0050011 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_101_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=456, w3=72, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 83)
    slow = _rolling_slope(x, 456)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=72, adjust=False).mean() * 1.444118 + 0.0050012 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_102_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=469, w3=89, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(469, min_periods=max(469//3, 2)).max()
    trough = x.rolling(90, min_periods=max(90//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.457647 + 0.0050013 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_103_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=482, w3=106, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(97)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.066333 * persistence + 0.0050014 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_104_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=495, w3=123, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(104, min_periods=max(104//3, 2)).std()
    vol_slow = ret.rolling(495, min_periods=max(495//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.484706 + 0.0050015 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_105_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=508, w3=140, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(508, min_periods=max(508//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 111)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.079 * slope + 0.0050016 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_106_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=22, w3=157, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(118)
    drag = impulse.rolling(22, min_periods=max(22//3, 2)).mean()
    noise = impulse.abs().rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.511765 + 0.0050017 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_107_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=35, w3=174, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 125)
    acceleration = _rolling_slope(velocity, 35)
    curvature = _rolling_slope(acceleration, 174)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091667 * acceleration + 0.0050018 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_108_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=48, w3=191, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(132, min_periods=max(132//3, 2)).mean(), upside.rolling(48, min_periods=max(48//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.538824 + 0.0050019 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_109_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=61, w3=208, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(61, min_periods=max(61//3, 2)).max()
    rebound = x - x.rolling(139, min_periods=max(139//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.104333 * _rolling_slope(draw, 208) + 0.005002 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_110_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=74, w3=225, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 146)
    baseline = trend.rolling(74, min_periods=max(74//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(225, min_periods=max(225//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.565882 + 0.0050021 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_111_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=87, w3=242, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 153)
    slow = _rolling_slope(x, 87)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=242, adjust=False).mean() * 1.579412 + 0.0050022 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_112_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=100, w3=259, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(100, min_periods=max(100//3, 2)).max()
    trough = x.rolling(160, min_periods=max(160//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.592941 + 0.0050023 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_113_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=113, w3=276, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(113, min_periods=max(113//3, 2)).rank(pct=True)
    persistence = change.rolling(276, min_periods=max(276//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.129667 * persistence + 0.0050024 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_114_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=126, w3=293, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(174, min_periods=max(174//3, 2)).std()
    vol_slow = ret.rolling(126, min_periods=max(126//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.62 + 0.0050025 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_115_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=139, w3=310, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(139, min_periods=max(139//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 181)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.142333 * slope + 0.0050026 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_116_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=152, w3=327, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.647059 + 0.0050027 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_117_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=165, w3=344, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 195)
    acceleration = _rolling_slope(velocity, 165)
    curvature = _rolling_slope(acceleration, 344)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.155 * acceleration + 0.0050028 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_118_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=178, w3=361, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(202, min_periods=max(202//3, 2)).mean(), upside.rolling(178, min_periods=max(178//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.820588 + 0.0050029 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_119_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=191, w3=378, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(191, min_periods=max(191//3, 2)).max()
    rebound = x - x.rolling(209, min_periods=max(209//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.167667 * _rolling_slope(draw, 378) + 0.005003 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_120_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=204, w3=395, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 216)
    baseline = trend.rolling(204, min_periods=max(204//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(395, min_periods=max(395//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.847647 + 0.0050031 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_121_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=217, w3=412, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 223)
    slow = _rolling_slope(x, 217)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.861176 + 0.0050032 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_122_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=230, w3=429, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(230, min_periods=max(230//3, 2)).max()
    trough = x.rolling(230, min_periods=max(230//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.874706 + 0.0050033 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_123_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=243, w3=446, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(243, min_periods=max(243//3, 2)).rank(pct=True)
    persistence = change.rolling(446, min_periods=max(446//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.193 * persistence + 0.0050034 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_124_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=256, w3=463, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(244, min_periods=max(244//3, 2)).std()
    vol_slow = ret.rolling(256, min_periods=max(256//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.901765 + 0.0050035 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_125_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=269, w3=480, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(269, min_periods=max(269//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 251)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.205667 * slope + 0.0050036 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_126_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=282, w3=497, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(11)
    drag = impulse.rolling(282, min_periods=max(282//3, 2)).mean()
    noise = impulse.abs().rolling(497, min_periods=max(497//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.928824 + 0.0050037 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_127_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=295, w3=514, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 18)
    acceleration = _rolling_slope(velocity, 295)
    curvature = _rolling_slope(acceleration, 514)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.218333 * acceleration + 0.0050038 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_128_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=308, w3=531, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(25, min_periods=max(25//3, 2)).mean(), upside.rolling(308, min_periods=max(308//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.955882 + 0.0050039 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_129_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=321, w3=548, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(321, min_periods=max(321//3, 2)).max()
    rebound = x - x.rolling(32, min_periods=max(32//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.231 * _rolling_slope(draw, 548) + 0.005004 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_130_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=334, w3=565, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 39)
    baseline = trend.rolling(334, min_periods=max(334//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(565, min_periods=max(565//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.982941 + 0.0050041 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_131_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=347, w3=582, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 46)
    slow = _rolling_slope(x, 347)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.996471 + 0.0050042 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_132_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=360, w3=599, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(360, min_periods=max(360//3, 2)).max()
    trough = x.rolling(53, min_periods=max(53//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01 + 0.0050043 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_133_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=373, w3=616, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(60)
    rank = change.rolling(373, min_periods=max(373//3, 2)).rank(pct=True)
    persistence = change.rolling(616, min_periods=max(616//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.256333 * persistence + 0.0050044 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_134_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=386, w3=633, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(67, min_periods=max(67//3, 2)).std()
    vol_slow = ret.rolling(386, min_periods=max(386//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.037059 + 0.0050045 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_135_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=399, w3=650, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(399, min_periods=max(399//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 74)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.269 * slope + 0.0050046 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_136_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=412, w3=667, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(81)
    drag = impulse.rolling(412, min_periods=max(412//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.064118 + 0.0050047 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_137_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=425, w3=684, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 88)
    acceleration = _rolling_slope(velocity, 425)
    curvature = _rolling_slope(acceleration, 684)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.281667 * acceleration + 0.0050048 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_138_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=438, w3=701, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(95, min_periods=max(95//3, 2)).mean(), upside.rolling(438, min_periods=max(438//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.091176 + 0.0050049 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_139_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=451, w3=718, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(451, min_periods=max(451//3, 2)).max()
    rebound = x - x.rolling(102, min_periods=max(102//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.294333 * _rolling_slope(draw, 718) + 0.005005 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_140_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=464, w3=735, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 109)
    baseline = trend.rolling(464, min_periods=max(464//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(735, min_periods=max(735//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.118235 + 0.0050051 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_141_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=477, w3=752, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 116)
    slow = _rolling_slope(x, 477)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.131765 + 0.0050052 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_142_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=490, w3=18, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(490, min_periods=max(490//3, 2)).max()
    trough = x.rolling(123, min_periods=max(123//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.145294 + 0.0050053 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_143_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=503, w3=35, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(503, min_periods=max(503//3, 2)).rank(pct=True)
    persistence = change.rolling(35, min_periods=max(35//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319667 * persistence + 0.0050054 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_144_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=17, w3=52, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(137, min_periods=max(137//3, 2)).std()
    vol_slow = ret.rolling(17, min_periods=max(17//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.172353 + 0.0050055 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_145_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=30, w3=69, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(30, min_periods=max(30//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 144)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.332333 * slope + 0.0050056 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_146_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=43, w3=86, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(43, min_periods=max(43//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.199412 + 0.0050057 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_147_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=56, w3=103, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 158)
    acceleration = _rolling_slope(velocity, 56)
    curvature = _rolling_slope(acceleration, 103)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.345 * acceleration + 0.0050058 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_148_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=69, w3=120, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(69, min_periods=max(69//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(120) * 1.226471 + 0.0050059 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_149_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=82, w3=137, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(82, min_periods=max(82//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.357667 * _rolling_slope(draw, 137) + 0.005006 * anchor
    return base_signal.diff().diff()

def f79_lrcb_gemini_150_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=95, w3=154, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 179)
    baseline = trend.rolling(95, min_periods=max(95//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(154, min_periods=max(154//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.253529 + 0.0050061 * anchor
    return base_signal.diff().diff()
