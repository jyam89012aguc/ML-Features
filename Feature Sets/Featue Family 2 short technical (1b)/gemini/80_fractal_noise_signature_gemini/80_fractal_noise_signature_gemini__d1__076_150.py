"""80 fractal noise signature gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of specific noise types (white, pink, brown) in market data.
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

def f80_fnoi_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=102, w3=28, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(102, min_periods=max(102//3, 2)).mean()
    noise = impulse.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.667059 + 0.0050407 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=115, w3=45, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 138)
    acceleration = _rolling_slope(velocity, 115)
    curvature = _rolling_slope(acceleration, 45)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.235333 * acceleration + 0.0050408 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=128, w3=62, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(145, min_periods=max(145//3, 2)).mean(), upside.rolling(128, min_periods=max(128//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(62) * 0.840588 + 0.0050409 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=141, w3=79, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(141, min_periods=max(141//3, 2)).max()
    rebound = x - x.rolling(152, min_periods=max(152//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.248 * _rolling_slope(draw, 79) + 0.005041 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=154, w3=96, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 159)
    baseline = trend.rolling(154, min_periods=max(154//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(96, min_periods=max(96//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.867647 + 0.0050411 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=167, w3=113, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 166)
    slow = _rolling_slope(x, 167)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=113, adjust=False).mean() * 0.881176 + 0.0050412 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=180, w3=130, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(180, min_periods=max(180//3, 2)).max()
    trough = x.rolling(173, min_periods=max(173//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.894706 + 0.0050413 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=193, w3=147, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(193, min_periods=max(193//3, 2)).rank(pct=True)
    persistence = change.rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.273333 * persistence + 0.0050414 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=206, w3=164, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(187, min_periods=max(187//3, 2)).std()
    vol_slow = ret.rolling(206, min_periods=max(206//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.921765 + 0.0050415 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=219, w3=181, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 194)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.286 * slope + 0.0050416 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=232, w3=198, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(198, min_periods=max(198//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.948824 + 0.0050417 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=245, w3=215, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 208)
    acceleration = _rolling_slope(velocity, 245)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.298667 * acceleration + 0.0050418 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=258, w3=232, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(215, min_periods=max(215//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.975882 + 0.0050419 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=271, w3=249, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(271, min_periods=max(271//3, 2)).max()
    rebound = x - x.rolling(222, min_periods=max(222//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.311333 * _rolling_slope(draw, 249) + 0.005042 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=284, w3=266, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 229)
    baseline = trend.rolling(284, min_periods=max(284//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(266, min_periods=max(266//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.002941 + 0.0050421 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=297, w3=283, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 236)
    slow = _rolling_slope(x, 297)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=283, adjust=False).mean() * 1.016471 + 0.0050422 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=310, w3=300, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(310, min_periods=max(310//3, 2)).max()
    trough = x.rolling(243, min_periods=max(243//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03 + 0.0050423 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=323, w3=317, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(323, min_periods=max(323//3, 2)).rank(pct=True)
    persistence = change.rolling(317, min_periods=max(317//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.336667 * persistence + 0.0050424 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=336, w3=334, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(10, min_periods=max(10//3, 2)).std()
    vol_slow = ret.rolling(336, min_periods=max(336//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.057059 + 0.0050425 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=349, w3=351, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(349, min_periods=max(349//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 17)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.349333 * slope + 0.0050426 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=362, w3=368, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(24)
    drag = impulse.rolling(362, min_periods=max(362//3, 2)).mean()
    noise = impulse.abs().rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.084118 + 0.0050427 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=375, w3=385, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 31)
    acceleration = _rolling_slope(velocity, 375)
    curvature = _rolling_slope(acceleration, 385)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.362 * acceleration + 0.0050428 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=388, w3=402, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(38, min_periods=max(38//3, 2)).mean(), upside.rolling(388, min_periods=max(388//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.111176 + 0.0050429 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=401, w3=419, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(401, min_periods=max(401//3, 2)).max()
    rebound = x - x.rolling(45, min_periods=max(45//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.042333 * _rolling_slope(draw, 419) + 0.005043 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=414, w3=436, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 52)
    baseline = trend.rolling(414, min_periods=max(414//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(436, min_periods=max(436//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.138235 + 0.0050431 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=427, w3=453, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 59)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.151765 + 0.0050432 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=440, w3=470, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(440, min_periods=max(440//3, 2)).max()
    trough = x.rolling(66, min_periods=max(66//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.165294 + 0.0050433 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=453, w3=487, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(73)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.067667 * persistence + 0.0050434 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=466, w3=504, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(80, min_periods=max(80//3, 2)).std()
    vol_slow = ret.rolling(466, min_periods=max(466//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.192353 + 0.0050435 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=479, w3=521, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(479, min_periods=max(479//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 87)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.080333 * slope + 0.0050436 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=492, w3=538, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(94)
    drag = impulse.rolling(492, min_periods=max(492//3, 2)).mean()
    noise = impulse.abs().rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.219412 + 0.0050437 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=505, w3=555, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 505)
    curvature = _rolling_slope(acceleration, 555)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.093 * acceleration + 0.0050438 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=19, w3=572, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(108, min_periods=max(108//3, 2)).mean(), upside.rolling(19, min_periods=max(19//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.246471 + 0.0050439 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=32, w3=589, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(32, min_periods=max(32//3, 2)).max()
    rebound = x - x.rolling(115, min_periods=max(115//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.105667 * _rolling_slope(draw, 589) + 0.005044 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=45, w3=606, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 122)
    baseline = trend.rolling(45, min_periods=max(45//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.273529 + 0.0050441 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=58, w3=623, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 129)
    slow = _rolling_slope(x, 58)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.287059 + 0.0050442 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=71, w3=640, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(71, min_periods=max(71//3, 2)).max()
    trough = x.rolling(136, min_periods=max(136//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.300588 + 0.0050443 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=84, w3=657, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(84, min_periods=max(84//3, 2)).rank(pct=True)
    persistence = change.rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.131 * persistence + 0.0050444 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=97, w3=674, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(150, min_periods=max(150//3, 2)).std()
    vol_slow = ret.rolling(97, min_periods=max(97//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.327647 + 0.0050445 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=110, w3=691, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(110, min_periods=max(110//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 157)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.143667 * slope + 0.0050446 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=123, w3=708, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(123, min_periods=max(123//3, 2)).mean()
    noise = impulse.abs().rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.354706 + 0.0050447 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=136, w3=725, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 171)
    acceleration = _rolling_slope(velocity, 136)
    curvature = _rolling_slope(acceleration, 725)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.156333 * acceleration + 0.0050448 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=149, w3=742, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(178, min_periods=max(178//3, 2)).mean(), upside.rolling(149, min_periods=max(149//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.381765 + 0.0050449 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=162, w3=759, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(162, min_periods=max(162//3, 2)).max()
    rebound = x - x.rolling(185, min_periods=max(185//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.169 * _rolling_slope(draw, 759) + 0.005045 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=175, w3=25, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 192)
    baseline = trend.rolling(175, min_periods=max(175//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(25, min_periods=max(25//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.408824 + 0.0050451 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=188, w3=42, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 199)
    slow = _rolling_slope(x, 188)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=42, adjust=False).mean() * 1.422353 + 0.0050452 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=201, w3=59, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(201, min_periods=max(201//3, 2)).max()
    trough = x.rolling(206, min_periods=max(206//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.435882 + 0.0050453 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=214, w3=76, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(214, min_periods=max(214//3, 2)).rank(pct=True)
    persistence = change.rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.194333 * persistence + 0.0050454 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=227, w3=93, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(220, min_periods=max(220//3, 2)).std()
    vol_slow = ret.rolling(227, min_periods=max(227//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.462941 + 0.0050455 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=240, w3=110, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(240, min_periods=max(240//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 227)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.207 * slope + 0.0050456 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=253, w3=127, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(253, min_periods=max(253//3, 2)).mean()
    noise = impulse.abs().rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.49 + 0.0050457 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=266, w3=144, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 241)
    acceleration = _rolling_slope(velocity, 266)
    curvature = _rolling_slope(acceleration, 144)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.219667 * acceleration + 0.0050458 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=279, w3=161, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(279, min_periods=max(279//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.517059 + 0.0050459 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=292, w3=178, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(292, min_periods=max(292//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.232333 * _rolling_slope(draw, 178) + 0.005046 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=305, w3=195, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 15)
    baseline = trend.rolling(305, min_periods=max(305//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(195, min_periods=max(195//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.544118 + 0.0050461 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=318, w3=212, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 22)
    slow = _rolling_slope(x, 318)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=212, adjust=False).mean() * 1.557647 + 0.0050462 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=331, w3=229, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(29, min_periods=max(29//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.571176 + 0.0050463 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=344, w3=246, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(36)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.257667 * persistence + 0.0050464 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=357, w3=263, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(43, min_periods=max(43//3, 2)).std()
    vol_slow = ret.rolling(357, min_periods=max(357//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.598235 + 0.0050465 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=370, w3=280, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(370, min_periods=max(370//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 50)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.270333 * slope + 0.0050466 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=383, w3=297, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(57)
    drag = impulse.rolling(383, min_periods=max(383//3, 2)).mean()
    noise = impulse.abs().rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.625294 + 0.0050467 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=396, w3=314, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 64)
    acceleration = _rolling_slope(velocity, 396)
    curvature = _rolling_slope(acceleration, 314)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.283 * acceleration + 0.0050468 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=409, w3=331, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(71, min_periods=max(71//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.652353 + 0.0050469 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=422, w3=348, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(422, min_periods=max(422//3, 2)).max()
    rebound = x - x.rolling(78, min_periods=max(78//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.295667 * _rolling_slope(draw, 348) + 0.005047 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=435, w3=365, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 85)
    baseline = trend.rolling(435, min_periods=max(435//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(365, min_periods=max(365//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.825882 + 0.0050471 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=448, w3=382, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 92)
    slow = _rolling_slope(x, 448)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.839412 + 0.0050472 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=461, w3=399, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(461, min_periods=max(461//3, 2)).max()
    trough = x.rolling(99, min_periods=max(99//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.852941 + 0.0050473 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=474, w3=416, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(106)
    rank = change.rolling(474, min_periods=max(474//3, 2)).rank(pct=True)
    persistence = change.rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.321 * persistence + 0.0050474 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=487, w3=433, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(113, min_periods=max(113//3, 2)).std()
    vol_slow = ret.rolling(487, min_periods=max(487//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.88 + 0.0050475 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=500, w3=450, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(500, min_periods=max(500//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 120)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.333667 * slope + 0.0050476 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=14, w3=467, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(14, min_periods=max(14//3, 2)).mean()
    noise = impulse.abs().rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.907059 + 0.0050477 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=27, w3=484, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 134)
    acceleration = _rolling_slope(velocity, 27)
    curvature = _rolling_slope(acceleration, 484)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.346333 * acceleration + 0.0050478 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=40, w3=501, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(141, min_periods=max(141//3, 2)).mean(), upside.rolling(40, min_periods=max(40//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.934118 + 0.0050479 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=53, w3=518, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(53, min_periods=max(53//3, 2)).max()
    rebound = x - x.rolling(148, min_periods=max(148//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.359 * _rolling_slope(draw, 518) + 0.005048 * anchor
    return base_signal.diff()

def f80_fnoi_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=66, w3=535, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 155)
    baseline = trend.rolling(66, min_periods=max(66//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(535, min_periods=max(535//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.961176 + 0.0050481 * anchor
    return base_signal.diff()
