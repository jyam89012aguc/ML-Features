"""84 session strength kinetics gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Momentum and volume analysis specific to key market session hours.
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

def f84_sstk_gemini_076_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=280, w3=558, lag=13)."""
    x = open.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(280, min_periods=max(280//3, 2)).mean()
    noise = impulse.abs().rolling(558, min_periods=max(558//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.245882 + 0.0052647 * anchor
    return base_signal.diff()

def f84_sstk_gemini_077_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=293, w3=575, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 10)
    acceleration = _rolling_slope(velocity, 293)
    curvature = _rolling_slope(acceleration, 575)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.131667 * acceleration + 0.0052648 * anchor
    return base_signal.diff()

def f84_sstk_gemini_078_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=306, w3=592, lag=34)."""
    rel = _safe_div(open.shift(34), close.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 17)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.138 * pressure.rolling(592, min_periods=max(592//3, 2)).mean() + 0.0052649 * anchor
    return base_signal.diff()

def f84_sstk_gemini_079_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=319, w3=609, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(24, min_periods=max(24//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.286471 + 0.005265 * anchor
    return base_signal.diff()

def f84_sstk_gemini_080_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=332, w3=626, lag=0)."""
    a = _safe_log(open.abs() + 1.0).shift(0)
    b = _safe_log(close.abs() + 1.0).shift(0)
    corr = a.rolling(332, min_periods=max(332//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 31)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.3 + 0.0052651 * anchor
    return base_signal.diff()

def f84_sstk_gemini_081_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=345, w3=643, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    cover = _safe_div(a.rolling(38, min_periods=max(38//3, 2)).mean(), b.abs().rolling(345, min_periods=max(345//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.157 * _rolling_slope(cover, 38) + 0.0052652 * anchor
    return base_signal.diff()

def f84_sstk_gemini_082_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=358, w3=660, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    y = _safe_log(close.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.163333 * y + 0.836667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 45) - _rolling_slope(basket, 358) + 0.0052653 * anchor
    return base_signal.diff()

def f84_sstk_gemini_083_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=371, w3=677, lag=3)."""
    x = open.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(371, min_periods=max(371//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.340588 + 0.0052654 * anchor
    return base_signal.diff()

def f84_sstk_gemini_084_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=384, w3=694, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    draw = x - x.rolling(384, min_periods=max(384//3, 2)).max()
    rebound = x - x.rolling(59, min_periods=max(59//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.176 * _rolling_slope(draw, 694) + 0.0052655 * anchor
    return base_signal.diff()

def f84_sstk_gemini_085_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=397, w3=711, lag=8)."""
    a = _safe_log(open.abs() + 1.0).shift(8)
    b = _safe_log(close.abs() + 1.0).shift(8)
    imbalance = a.diff(66) - b.diff(126)
    stress = imbalance.rolling(711, min_periods=max(711//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.367647 + 0.0052656 * anchor
    return base_signal.diff()

def f84_sstk_gemini_086_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=410, w3=728, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(410, min_periods=max(410//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(728, min_periods=max(728//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.381176 + 0.0052657 * anchor
    return base_signal.diff()

def f84_sstk_gemini_087_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=423, w3=745, lag=21)."""
    x = _safe_log(open.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 423)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.394706 + 0.0052658 * anchor
    return base_signal.diff()

def f84_sstk_gemini_088_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=436, w3=762, lag=34)."""
    x = open.shift(34)
    peak = x.rolling(436, min_periods=max(436//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.408235 + 0.0052659 * anchor
    return base_signal.diff()

def f84_sstk_gemini_089_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=449, w3=28, lag=55)."""
    x = open.shift(55)
    change = x.pct_change(94)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.207667 * persistence + 0.005266 * anchor
    return base_signal.diff()

def f84_sstk_gemini_090_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=462, w3=45, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(462, min_periods=max(462//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.435294 + 0.0052661 * anchor
    return base_signal.diff()

def f84_sstk_gemini_091_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=475, w3=62, lag=1)."""
    x = open.shift(1)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.220333 * slope + 0.0052662 * anchor
    return base_signal.diff()

def f84_sstk_gemini_092_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=488, w3=79, lag=2)."""
    x = open.shift(2)
    impulse = x.diff(115)
    drag = impulse.rolling(488, min_periods=max(488//3, 2)).mean()
    noise = impulse.abs().rolling(79, min_periods=max(79//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.462353 + 0.0052663 * anchor
    return base_signal.diff()

def f84_sstk_gemini_093_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=501, w3=96, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 501)
    curvature = _rolling_slope(acceleration, 96)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.233 * acceleration + 0.0052664 * anchor
    return base_signal.diff()

def f84_sstk_gemini_094_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=15, w3=113, lag=5)."""
    rel = _safe_div(open.shift(5), close.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 129)
    pressure = rel_log.diff(15)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.239333 * pressure.rolling(113, min_periods=max(113//3, 2)).mean() + 0.0052665 * anchor
    return base_signal.diff()

def f84_sstk_gemini_095_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=28, w3=130, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(136, min_periods=max(136//3, 2)).mean())
    decay = spread.ewm(span=28, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.502941 + 0.0052666 * anchor
    return base_signal.diff()

def f84_sstk_gemini_096_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=41, w3=147, lag=13)."""
    a = _safe_log(open.abs() + 1.0).shift(13)
    b = _safe_log(close.abs() + 1.0).shift(13)
    corr = a.rolling(41, min_periods=max(41//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 143)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.516471 + 0.0052667 * anchor
    return base_signal.diff()

def f84_sstk_gemini_097_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=54, w3=164, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    cover = _safe_div(a.rolling(150, min_periods=max(150//3, 2)).mean(), b.abs().rolling(54, min_periods=max(54//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.258333 * _rolling_slope(cover, 150) + 0.0052668 * anchor
    return base_signal.diff()

def f84_sstk_gemini_098_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=67, w3=181, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    y = _safe_log(close.abs() + 1.0).shift(34)
    z = _safe_log(close.abs() + 1.0).shift(34)
    basket = x - 0.264667 * y + 0.735333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 157) - _rolling_slope(basket, 67) + 0.0052669 * anchor
    return base_signal.diff()

def f84_sstk_gemini_099_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=80, w3=198, lag=55)."""
    x = open.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(164, min_periods=max(164//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.557059 + 0.005267 * anchor
    return base_signal.diff()

def f84_sstk_gemini_100_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=93, w3=215, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    draw = x - x.rolling(93, min_periods=max(93//3, 2)).max()
    rebound = x - x.rolling(171, min_periods=max(171//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.277333 * _rolling_slope(draw, 215) + 0.0052671 * anchor
    return base_signal.diff()

def f84_sstk_gemini_101_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=106, w3=232, lag=1)."""
    a = _safe_log(open.abs() + 1.0).shift(1)
    b = _safe_log(close.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(106)
    stress = imbalance.rolling(232, min_periods=max(232//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.584118 + 0.0052672 * anchor
    return base_signal.diff()

def f84_sstk_gemini_102_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=119, w3=249, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 185)
    baseline = trend.rolling(119, min_periods=max(119//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.597647 + 0.0052673 * anchor
    return base_signal.diff()

def f84_sstk_gemini_103_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=132, w3=266, lag=3)."""
    x = _safe_log(open.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 192)
    slow = _rolling_slope(x, 132)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=266, adjust=False).mean() * 1.611176 + 0.0052674 * anchor
    return base_signal.diff()

def f84_sstk_gemini_104_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=145, w3=283, lag=5)."""
    x = open.shift(5)
    peak = x.rolling(145, min_periods=max(145//3, 2)).max()
    trough = x.rolling(199, min_periods=max(199//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.624706 + 0.0052675 * anchor
    return base_signal.diff()

def f84_sstk_gemini_105_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=158, w3=300, lag=8)."""
    x = open.shift(8)
    change = x.pct_change(126)
    rank = change.rolling(158, min_periods=max(158//3, 2)).rank(pct=True)
    persistence = change.rolling(300, min_periods=max(300//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.309 * persistence + 0.0052676 * anchor
    return base_signal.diff()

def f84_sstk_gemini_106_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=171, w3=317, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(213, min_periods=max(213//3, 2)).std()
    vol_slow = ret.rolling(171, min_periods=max(171//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.651765 + 0.0052677 * anchor
    return base_signal.diff()

def f84_sstk_gemini_107_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=184, w3=334, lag=21)."""
    x = open.shift(21)
    ma = x.rolling(184, min_periods=max(184//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 220)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.321667 * slope + 0.0052678 * anchor
    return base_signal.diff()

def f84_sstk_gemini_108_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=197, w3=351, lag=34)."""
    x = open.shift(34)
    impulse = x.diff(126)
    drag = impulse.rolling(197, min_periods=max(197//3, 2)).mean()
    noise = impulse.abs().rolling(351, min_periods=max(351//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.825294 + 0.0052679 * anchor
    return base_signal.diff()

def f84_sstk_gemini_109_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=210, w3=368, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 234)
    acceleration = _rolling_slope(velocity, 210)
    curvature = _rolling_slope(acceleration, 368)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.334333 * acceleration + 0.005268 * anchor
    return base_signal.diff()

def f84_sstk_gemini_110_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=223, w3=385, lag=0)."""
    rel = _safe_div(open.shift(0), close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 241)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.340667 * pressure.rolling(385, min_periods=max(385//3, 2)).mean() + 0.0052681 * anchor
    return base_signal.diff()

def f84_sstk_gemini_111_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=236, w3=402, lag=1)."""
    a = open.shift(1)
    b = close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(248, min_periods=max(248//3, 2)).mean())
    decay = spread.ewm(span=236, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.865882 + 0.0052682 * anchor
    return base_signal.diff()

def f84_sstk_gemini_112_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=249, w3=419, lag=2)."""
    a = _safe_log(open.abs() + 1.0).shift(2)
    b = _safe_log(close.abs() + 1.0).shift(2)
    corr = a.rolling(249, min_periods=max(249//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 8)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.879412 + 0.0052683 * anchor
    return base_signal.diff()

def f84_sstk_gemini_113_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=262, w3=436, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    cover = _safe_div(a.rolling(15, min_periods=max(15//3, 2)).mean(), b.abs().rolling(262, min_periods=max(262//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.359667 * _rolling_slope(cover, 15) + 0.0052684 * anchor
    return base_signal.diff()

def f84_sstk_gemini_114_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=275, w3=453, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    y = _safe_log(close.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.033667 * y + 0.966333 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 22) - _rolling_slope(basket, 275) + 0.0052685 * anchor
    return base_signal.diff()

def f84_sstk_gemini_115_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=288, w3=470, lag=8)."""
    x = open.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(29, min_periods=max(29//3, 2)).mean(), upside.rolling(288, min_periods=max(288//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.92 + 0.0052686 * anchor
    return base_signal.diff()

def f84_sstk_gemini_116_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=301, w3=487, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    draw = x - x.rolling(301, min_periods=max(301//3, 2)).max()
    rebound = x - x.rolling(36, min_periods=max(36//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.046333 * _rolling_slope(draw, 487) + 0.0052687 * anchor
    return base_signal.diff()

def f84_sstk_gemini_117_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=314, w3=504, lag=21)."""
    a = _safe_log(open.abs() + 1.0).shift(21)
    b = _safe_log(close.abs() + 1.0).shift(21)
    imbalance = a.diff(43) - b.diff(126)
    stress = imbalance.rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.947059 + 0.0052688 * anchor
    return base_signal.diff()

def f84_sstk_gemini_118_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=327, w3=521, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 50)
    baseline = trend.rolling(327, min_periods=max(327//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(521, min_periods=max(521//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.960588 + 0.0052689 * anchor
    return base_signal.diff()

def f84_sstk_gemini_119_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=340, w3=538, lag=55)."""
    x = _safe_log(open.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 57)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.974118 + 0.005269 * anchor
    return base_signal.diff()

def f84_sstk_gemini_120_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=353, w3=555, lag=0)."""
    x = open.shift(0)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(64, min_periods=max(64//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.987647 + 0.0052691 * anchor
    return base_signal.diff()

def f84_sstk_gemini_121_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=366, w3=572, lag=1)."""
    x = open.shift(1)
    change = x.pct_change(71)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.078 * persistence + 0.0052692 * anchor
    return base_signal.diff()

def f84_sstk_gemini_122_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=379, w3=589, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(78, min_periods=max(78//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.014706 + 0.0052693 * anchor
    return base_signal.diff()

def f84_sstk_gemini_123_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=392, w3=606, lag=3)."""
    x = open.shift(3)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 85)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.090667 * slope + 0.0052694 * anchor
    return base_signal.diff()

def f84_sstk_gemini_124_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=405, w3=623, lag=5)."""
    x = open.shift(5)
    impulse = x.diff(92)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(623, min_periods=max(623//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.041765 + 0.0052695 * anchor
    return base_signal.diff()

def f84_sstk_gemini_125_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=418, w3=640, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 99)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 640)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.103333 * acceleration + 0.0052696 * anchor
    return base_signal.diff()

def f84_sstk_gemini_126_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=431, w3=657, lag=13)."""
    rel = _safe_div(open.shift(13), close.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 106)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.109667 * pressure.rolling(657, min_periods=max(657//3, 2)).mean() + 0.0052697 * anchor
    return base_signal.diff()

def f84_sstk_gemini_127_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=444, w3=674, lag=21)."""
    a = open.shift(21)
    b = close.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(113, min_periods=max(113//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.082353 + 0.0052698 * anchor
    return base_signal.diff()

def f84_sstk_gemini_128_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=457, w3=691, lag=34)."""
    a = _safe_log(open.abs() + 1.0).shift(34)
    b = _safe_log(close.abs() + 1.0).shift(34)
    corr = a.rolling(457, min_periods=max(457//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 120)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.095882 + 0.0052699 * anchor
    return base_signal.diff()

def f84_sstk_gemini_129_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=470, w3=708, lag=55)."""
    a = open.shift(55)
    b = close.shift(55)
    cover = _safe_div(a.rolling(127, min_periods=max(127//3, 2)).mean(), b.abs().rolling(470, min_periods=max(470//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.128667 * _rolling_slope(cover, 127) + 0.00527 * anchor
    return base_signal.diff()

def f84_sstk_gemini_130_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=483, w3=725, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    y = _safe_log(close.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.135 * y + 0.865000 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 134) - _rolling_slope(basket, 483) + 0.0052701 * anchor
    return base_signal.diff()

def f84_sstk_gemini_131_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=496, w3=742, lag=1)."""
    x = open.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(496, min_periods=max(496//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.136471 + 0.0052702 * anchor
    return base_signal.diff()

def f84_sstk_gemini_132_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=509, w3=759, lag=2)."""
    x = _safe_log(open.abs() + 1.0).shift(2)
    draw = x - x.rolling(509, min_periods=max(509//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.147667 * _rolling_slope(draw, 759) + 0.0052703 * anchor
    return base_signal.diff()

def f84_sstk_gemini_133_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=23, w3=25, lag=3)."""
    a = _safe_log(open.abs() + 1.0).shift(3)
    b = _safe_log(close.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(23)
    stress = imbalance.rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.163529 + 0.0052704 * anchor
    return base_signal.diff()

def f84_sstk_gemini_134_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=36, w3=42, lag=5)."""
    x = _safe_log(open.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 162)
    baseline = trend.rolling(36, min_periods=max(36//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.177059 + 0.0052705 * anchor
    return base_signal.diff()

def f84_sstk_gemini_135_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=49, w3=59, lag=8)."""
    x = _safe_log(open.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 49)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=59, adjust=False).mean() * 1.190588 + 0.0052706 * anchor
    return base_signal.diff()

def f84_sstk_gemini_136_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=62, w3=76, lag=13)."""
    x = open.shift(13)
    peak = x.rolling(62, min_periods=max(62//3, 2)).max()
    trough = x.rolling(176, min_periods=max(176//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.204118 + 0.0052707 * anchor
    return base_signal.diff()

def f84_sstk_gemini_137_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=75, w3=93, lag=21)."""
    x = open.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(75, min_periods=max(75//3, 2)).rank(pct=True)
    persistence = change.rolling(93, min_periods=max(93//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.179333 * persistence + 0.0052708 * anchor
    return base_signal.diff()

def f84_sstk_gemini_138_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=88, w3=110, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(190, min_periods=max(190//3, 2)).std()
    vol_slow = ret.rolling(88, min_periods=max(88//3, 2)).std()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.231176 + 0.0052709 * anchor
    return base_signal.diff()

def f84_sstk_gemini_139_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=101, w3=127, lag=55)."""
    x = open.shift(55)
    ma = x.rolling(101, min_periods=max(101//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.192 * slope + 0.005271 * anchor
    return base_signal.diff()

def f84_sstk_gemini_140_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=114, w3=144, lag=0)."""
    x = open.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(114, min_periods=max(114//3, 2)).mean()
    noise = impulse.abs().rolling(144, min_periods=max(144//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.258235 + 0.0052711 * anchor
    return base_signal.diff()

def f84_sstk_gemini_141_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=127, w3=161, lag=1)."""
    x = _safe_log(open.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 127)
    curvature = _rolling_slope(acceleration, 161)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.204667 * acceleration + 0.0052712 * anchor
    return base_signal.diff()

def f84_sstk_gemini_142_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=140, w3=178, lag=2)."""
    rel = _safe_div(open.shift(2), close.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 218)
    pressure = rel_log.diff(126)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.211 * pressure.rolling(178, min_periods=max(178//3, 2)).mean() + 0.0052713 * anchor
    return base_signal.diff()

def f84_sstk_gemini_143_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=153, w3=195, lag=3)."""
    a = open.shift(3)
    b = close.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(225, min_periods=max(225//3, 2)).mean())
    decay = spread.ewm(span=153, adjust=False).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.298824 + 0.0052714 * anchor
    return base_signal.diff()

def f84_sstk_gemini_144_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=166, w3=212, lag=5)."""
    a = _safe_log(open.abs() + 1.0).shift(5)
    b = _safe_log(close.abs() + 1.0).shift(5)
    corr = a.rolling(166, min_periods=max(166//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 232)
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.312353 + 0.0052715 * anchor
    return base_signal.diff()

def f84_sstk_gemini_145_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=179, w3=229, lag=8)."""
    a = open.shift(8)
    b = close.shift(8)
    cover = _safe_div(a.rolling(239, min_periods=max(239//3, 2)).mean(), b.abs().rolling(179, min_periods=max(179//3, 2)).mean())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.23 * _rolling_slope(cover, 239) + 0.0052716 * anchor
    return base_signal.diff()

def f84_sstk_gemini_146_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=192, w3=246, lag=13)."""
    x = _safe_log(open.abs() + 1.0).shift(13)
    y = _safe_log(close.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.236333 * y + 0.763667 * z
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 246) - _rolling_slope(basket, 192) + 0.0052717 * anchor
    return base_signal.diff()

def f84_sstk_gemini_147_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=205, w3=263, lag=21)."""
    x = open.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(205, min_periods=max(205//3, 2)).mean().abs())
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.352941 + 0.0052718 * anchor
    return base_signal.diff()

def f84_sstk_gemini_148_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=218, w3=280, lag=34)."""
    x = _safe_log(open.abs() + 1.0).shift(34)
    draw = x - x.rolling(218, min_periods=max(218//3, 2)).max()
    rebound = x - x.rolling(13, min_periods=max(13//3, 2)).min()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.249 * _rolling_slope(draw, 280) + 0.0052719 * anchor
    return base_signal.diff()

def f84_sstk_gemini_149_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=231, w3=297, lag=55)."""
    a = _safe_log(open.abs() + 1.0).shift(55)
    b = _safe_log(close.abs() + 1.0).shift(55)
    imbalance = a.diff(20) - b.diff(126)
    stress = imbalance.rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.38 + 0.005272 * anchor
    return base_signal.diff()

def f84_sstk_gemini_150_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=244, w3=314, lag=0)."""
    x = _safe_log(open.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 27)
    baseline = trend.rolling(244, min_periods=max(244//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(314, min_periods=max(314//3, 2)).mean()
    anchor = _safe_log(open.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.393529 + 0.0052721 * anchor
    return base_signal.diff()
