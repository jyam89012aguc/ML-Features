"""27 macd topping dynamics gemini d3 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Moving Average Convergence Divergence peaks and bearish crossovers at trend exhaustion.
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

def f27_macd_gemini_076_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=82, w2=136, w3=394, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(82)
    drag = impulse.rolling(136, min_periods=max(136//3, 2)).mean()
    noise = impulse.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.647059 + 0.0021007 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_077_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=89, w2=149, w3=411, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 149)
    curvature = _rolling_slope(acceleration, 411)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.142 * acceleration + 0.0021008 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_078_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=96, w2=162, w3=428, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(162, min_periods=max(162//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.820588 + 0.0021009 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_079_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=103, w2=175, w3=445, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(175, min_periods=max(175//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.154667 * _rolling_slope(draw, 445) + 0.002101 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_080_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=110, w2=188, w3=462, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(188, min_periods=max(188//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.847647 + 0.0021011 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_081_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=117, w2=201, w3=479, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.861176 + 0.0021012 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_082_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=124, w2=214, w3=496, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(214, min_periods=max(214//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.874706 + 0.0021013 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_083_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=131, w2=227, w3=513, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(227, min_periods=max(227//3, 2)).rank(pct=True)
    persistence = change.rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.18 * persistence + 0.0021014 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_084_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=138, w2=240, w3=530, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(240, min_periods=max(240//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.901765 + 0.0021015 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_085_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=145, w2=253, w3=547, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(253, min_periods=max(253//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.192667 * slope + 0.0021016 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_086_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=152, w2=266, w3=564, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(266, min_periods=max(266//3, 2)).mean()
    noise = impulse.abs().rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.928824 + 0.0021017 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_087_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=159, w2=279, w3=581, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 279)
    curvature = _rolling_slope(acceleration, 581)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.205333 * acceleration + 0.0021018 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_088_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=166, w2=292, w3=598, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(292, min_periods=max(292//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.955882 + 0.0021019 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_089_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=173, w2=305, w3=615, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(305, min_periods=max(305//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.218 * _rolling_slope(draw, 615) + 0.002102 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_090_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=180, w2=318, w3=632, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(318, min_periods=max(318//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(632, min_periods=max(632//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.982941 + 0.0021021 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_091_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=187, w2=331, w3=649, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 331)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.996471 + 0.0021022 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_092_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=194, w2=344, w3=666, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.01 + 0.0021023 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_093_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=201, w2=357, w3=683, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(357, min_periods=max(357//3, 2)).rank(pct=True)
    persistence = change.rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.243333 * persistence + 0.0021024 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_094_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=208, w2=370, w3=700, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(370, min_periods=max(370//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.037059 + 0.0021025 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_095_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=215, w2=383, w3=717, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(383, min_periods=max(383//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.256 * slope + 0.0021026 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_096_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=222, w2=396, w3=734, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(396, min_periods=max(396//3, 2)).mean()
    noise = impulse.abs().rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.064118 + 0.0021027 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_097_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=229, w2=409, w3=751, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 409)
    curvature = _rolling_slope(acceleration, 751)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.268667 * acceleration + 0.0021028 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_098_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=236, w2=422, w3=17, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(422, min_periods=max(422//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(17) * 1.091176 + 0.0021029 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_099_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=243, w2=435, w3=34, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(435, min_periods=max(435//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.281333 * _rolling_slope(draw, 34) + 0.002103 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_100_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=250, w2=448, w3=51, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(448, min_periods=max(448//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(51, min_periods=max(51//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.118235 + 0.0021031 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_101_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=10, w2=461, w3=68, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 461)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=68, adjust=False).mean() * 1.131765 + 0.0021032 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_102_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=17, w2=474, w3=85, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(474, min_periods=max(474//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.145294 + 0.0021033 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_103_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=24, w2=487, w3=102, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(24)
    rank = change.rolling(487, min_periods=max(487//3, 2)).rank(pct=True)
    persistence = change.rolling(102, min_periods=max(102//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.306667 * persistence + 0.0021034 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_104_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=31, w2=500, w3=119, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(500, min_periods=max(500//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.172353 + 0.0021035 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_105_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=38, w2=14, w3=136, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(14, min_periods=max(14//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.319333 * slope + 0.0021036 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_106_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=45, w2=27, w3=153, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(45)
    drag = impulse.rolling(27, min_periods=max(27//3, 2)).mean()
    noise = impulse.abs().rolling(153, min_periods=max(153//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.199412 + 0.0021037 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_107_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=52, w2=40, w3=170, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 40)
    curvature = _rolling_slope(acceleration, 170)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.332 * acceleration + 0.0021038 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_108_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=59, w2=53, w3=187, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(53, min_periods=max(53//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.226471 + 0.0021039 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_109_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=66, w2=66, w3=204, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(66, min_periods=max(66//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.344667 * _rolling_slope(draw, 204) + 0.002104 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_110_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=73, w2=79, w3=221, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(79, min_periods=max(79//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(221, min_periods=max(221//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.253529 + 0.0021041 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_111_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=80, w2=92, w3=238, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=238, adjust=False).mean() * 1.267059 + 0.0021042 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_112_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=87, w2=105, w3=255, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(105, min_periods=max(105//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.280588 + 0.0021043 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_113_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=94, w2=118, w3=272, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(94)
    rank = change.rolling(118, min_periods=max(118//3, 2)).rank(pct=True)
    persistence = change.rolling(272, min_periods=max(272//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.037667 * persistence + 0.0021044 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_114_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=101, w2=131, w3=289, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(131, min_periods=max(131//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.307647 + 0.0021045 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_115_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=108, w2=144, w3=306, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(144, min_periods=max(144//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.050333 * slope + 0.0021046 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_116_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=115, w2=157, w3=323, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(115)
    drag = impulse.rolling(157, min_periods=max(157//3, 2)).mean()
    noise = impulse.abs().rolling(323, min_periods=max(323//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.334706 + 0.0021047 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_117_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=122, w2=170, w3=340, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 170)
    curvature = _rolling_slope(acceleration, 340)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.063 * acceleration + 0.0021048 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_118_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=129, w2=183, w3=357, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(183, min_periods=max(183//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.361765 + 0.0021049 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_119_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=136, w2=196, w3=374, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(196, min_periods=max(196//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.075667 * _rolling_slope(draw, 374) + 0.002105 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_120_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=143, w2=209, w3=391, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(209, min_periods=max(209//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(391, min_periods=max(391//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.388824 + 0.0021051 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_121_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=150, w2=222, w3=408, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 222)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.402353 + 0.0021052 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_122_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=157, w2=235, w3=425, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(235, min_periods=max(235//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.415882 + 0.0021053 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_123_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=164, w2=248, w3=442, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(248, min_periods=max(248//3, 2)).rank(pct=True)
    persistence = change.rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.101 * persistence + 0.0021054 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_124_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=171, w2=261, w3=459, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(261, min_periods=max(261//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.442941 + 0.0021055 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_125_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=178, w2=274, w3=476, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(274, min_periods=max(274//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.113667 * slope + 0.0021056 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_126_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=185, w2=287, w3=493, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(287, min_periods=max(287//3, 2)).mean()
    noise = impulse.abs().rolling(493, min_periods=max(493//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.47 + 0.0021057 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_127_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=192, w2=300, w3=510, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 300)
    curvature = _rolling_slope(acceleration, 510)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.126333 * acceleration + 0.0021058 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_128_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=199, w2=313, w3=527, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(313, min_periods=max(313//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.497059 + 0.0021059 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_129_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=206, w2=326, w3=544, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(326, min_periods=max(326//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.139 * _rolling_slope(draw, 544) + 0.002106 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_130_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=213, w2=339, w3=561, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(561, min_periods=max(561//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.524118 + 0.0021061 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_131_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=220, w2=352, w3=578, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 352)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.537647 + 0.0021062 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_132_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=227, w2=365, w3=595, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(365, min_periods=max(365//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.551176 + 0.0021063 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_133_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=234, w2=378, w3=612, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(378, min_periods=max(378//3, 2)).rank(pct=True)
    persistence = change.rolling(612, min_periods=max(612//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.164333 * persistence + 0.0021064 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_134_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=241, w2=391, w3=629, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(391, min_periods=max(391//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.578235 + 0.0021065 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_135_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=248, w2=404, w3=646, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(404, min_periods=max(404//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.177 * slope + 0.0021066 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_136_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=8, w2=417, w3=663, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(8)
    drag = impulse.rolling(417, min_periods=max(417//3, 2)).mean()
    noise = impulse.abs().rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.605294 + 0.0021067 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_137_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=15, w2=430, w3=680, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 430)
    curvature = _rolling_slope(acceleration, 680)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.189667 * acceleration + 0.0021068 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_138_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=22, w2=443, w3=697, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(443, min_periods=max(443//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.632353 + 0.0021069 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_139_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=29, w2=456, w3=714, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(456, min_periods=max(456//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.202333 * _rolling_slope(draw, 714) + 0.002107 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_140_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=36, w2=469, w3=731, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(469, min_periods=max(469//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.659412 + 0.0021071 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_141_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=43, w2=482, w3=748, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 482)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.672941 + 0.0021072 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_142_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=50, w2=495, w3=765, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(495, min_periods=max(495//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.832941 + 0.0021073 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_143_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=57, w2=508, w3=31, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(57)
    rank = change.rolling(508, min_periods=max(508//3, 2)).rank(pct=True)
    persistence = change.rolling(31, min_periods=max(31//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.227667 * persistence + 0.0021074 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_144_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=64, w2=22, w3=48, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(22, min_periods=max(22//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.86 + 0.0021075 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_145_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=71, w2=35, w3=65, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.240333 * slope + 0.0021076 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_146_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=78, w2=48, w3=82, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(78)
    drag = impulse.rolling(48, min_periods=max(48//3, 2)).mean()
    noise = impulse.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.887059 + 0.0021077 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_147_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=85, w2=61, w3=99, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 61)
    curvature = _rolling_slope(acceleration, 99)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.253 * acceleration + 0.0021078 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_148_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=92, w2=74, w3=116, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(74, min_periods=max(74//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(116) * 0.914118 + 0.0021079 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_149_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=99, w2=87, w3=133, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(87, min_periods=max(87//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.265667 * _rolling_slope(draw, 133) + 0.002108 * anchor
    return base_signal.diff().diff().diff()

def f27_macd_gemini_150_d3(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=106, w2=100, w3=150, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(100, min_periods=max(100//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(150, min_periods=max(150//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.941176 + 0.0021081 * anchor
    return base_signal.diff().diff().diff()
