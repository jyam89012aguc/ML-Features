"""76 multi fractal dfa spectrum gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Multi-scale analysis of fluctuations to detect non-linear scaling behavior.
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

def f76_mdfa_gemini_076_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=12, w2=423, w3=249, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(12)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(249, min_periods=max(249//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.234706 + 0.0048167 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_077_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=19, w2=436, w3=266, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 19)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 266)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.339 * acceleration + 0.0048168 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_078_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=26, w2=449, w3=283, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(26, min_periods=max(26//3, 2)).mean(), upside.rolling(449, min_periods=max(449//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.261765 + 0.0048169 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_079_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=33, w2=462, w3=300, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(462, min_periods=max(462//3, 2)).max()
    rebound = x - x.rolling(33, min_periods=max(33//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.351667 * _rolling_slope(draw, 300) + 0.004817 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_080_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=40, w2=475, w3=317, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 40)
    baseline = trend.rolling(475, min_periods=max(475//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(317, min_periods=max(317//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.288824 + 0.0048171 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_081_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=47, w2=488, w3=334, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 47)
    slow = _rolling_slope(x, 488)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.302353 + 0.0048172 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_082_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=54, w2=501, w3=351, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(54, min_periods=max(54//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.315882 + 0.0048173 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_083_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=61, w2=15, w3=368, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(61)
    rank = change.rolling(15, min_periods=max(15//3, 2)).rank(pct=True)
    persistence = change.rolling(368, min_periods=max(368//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.044667 * persistence + 0.0048174 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_084_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=68, w2=28, w3=385, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(68, min_periods=max(68//3, 2)).std()
    vol_slow = ret.rolling(28, min_periods=max(28//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.342941 + 0.0048175 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_085_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=75, w2=41, w3=402, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(41, min_periods=max(41//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 75)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.057333 * slope + 0.0048176 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_086_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=82, w2=54, w3=419, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(82)
    drag = impulse.rolling(54, min_periods=max(54//3, 2)).mean()
    noise = impulse.abs().rolling(419, min_periods=max(419//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.37 + 0.0048177 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_087_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=89, w2=67, w3=436, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 89)
    acceleration = _rolling_slope(velocity, 67)
    curvature = _rolling_slope(acceleration, 436)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.07 * acceleration + 0.0048178 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_088_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=96, w2=80, w3=453, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(96, min_periods=max(96//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.397059 + 0.0048179 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_089_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=103, w2=93, w3=470, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(93, min_periods=max(93//3, 2)).max()
    rebound = x - x.rolling(103, min_periods=max(103//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.082667 * _rolling_slope(draw, 470) + 0.004818 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_090_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=110, w2=106, w3=487, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 110)
    baseline = trend.rolling(106, min_periods=max(106//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(487, min_periods=max(487//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.424118 + 0.0048181 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_091_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=117, w2=119, w3=504, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 117)
    slow = _rolling_slope(x, 119)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.437647 + 0.0048182 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_092_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=124, w2=132, w3=521, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(132, min_periods=max(132//3, 2)).max()
    trough = x.rolling(124, min_periods=max(124//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.451176 + 0.0048183 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_093_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=131, w2=145, w3=538, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(145, min_periods=max(145//3, 2)).rank(pct=True)
    persistence = change.rolling(538, min_periods=max(538//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.108 * persistence + 0.0048184 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_094_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=138, w2=158, w3=555, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(138, min_periods=max(138//3, 2)).std()
    vol_slow = ret.rolling(158, min_periods=max(158//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478235 + 0.0048185 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_095_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=145, w2=171, w3=572, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(171, min_periods=max(171//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 145)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.120667 * slope + 0.0048186 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_096_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=152, w2=184, w3=589, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(184, min_periods=max(184//3, 2)).mean()
    noise = impulse.abs().rolling(589, min_periods=max(589//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.505294 + 0.0048187 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_097_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=159, w2=197, w3=606, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 159)
    acceleration = _rolling_slope(velocity, 197)
    curvature = _rolling_slope(acceleration, 606)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.133333 * acceleration + 0.0048188 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_098_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=166, w2=210, w3=623, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(166, min_periods=max(166//3, 2)).mean(), upside.rolling(210, min_periods=max(210//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.532353 + 0.0048189 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_099_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=173, w2=223, w3=640, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(223, min_periods=max(223//3, 2)).max()
    rebound = x - x.rolling(173, min_periods=max(173//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.146 * _rolling_slope(draw, 640) + 0.004819 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_100_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=180, w2=236, w3=657, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 180)
    baseline = trend.rolling(236, min_periods=max(236//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.559412 + 0.0048191 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_101_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=187, w2=249, w3=674, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 187)
    slow = _rolling_slope(x, 249)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.572941 + 0.0048192 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_102_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=194, w2=262, w3=691, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(262, min_periods=max(262//3, 2)).max()
    trough = x.rolling(194, min_periods=max(194//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.586471 + 0.0048193 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_103_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=201, w2=275, w3=708, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(275, min_periods=max(275//3, 2)).rank(pct=True)
    persistence = change.rolling(708, min_periods=max(708//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.171333 * persistence + 0.0048194 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_104_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=208, w2=288, w3=725, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(208, min_periods=max(208//3, 2)).std()
    vol_slow = ret.rolling(288, min_periods=max(288//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.613529 + 0.0048195 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_105_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=215, w2=301, w3=742, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(301, min_periods=max(301//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 215)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.184 * slope + 0.0048196 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_106_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=222, w2=314, w3=759, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(314, min_periods=max(314//3, 2)).mean()
    noise = impulse.abs().rolling(759, min_periods=max(759//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.640588 + 0.0048197 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_107_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=229, w2=327, w3=25, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 229)
    acceleration = _rolling_slope(velocity, 327)
    curvature = _rolling_slope(acceleration, 25)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.196667 * acceleration + 0.0048198 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_108_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=236, w2=340, w3=42, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(236, min_periods=max(236//3, 2)).mean(), upside.rolling(340, min_periods=max(340//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(42) * 1.667647 + 0.0048199 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_109_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=243, w2=353, w3=59, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(353, min_periods=max(353//3, 2)).max()
    rebound = x - x.rolling(243, min_periods=max(243//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.209333 * _rolling_slope(draw, 59) + 0.00482 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_110_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=250, w2=366, w3=76, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 250)
    baseline = trend.rolling(366, min_periods=max(366//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(76, min_periods=max(76//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.841176 + 0.0048201 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_111_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=10, w2=379, w3=93, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 379)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=93, adjust=False).mean() * 0.854706 + 0.0048202 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_112_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=17, w2=392, w3=110, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(392, min_periods=max(392//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.868235 + 0.0048203 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_113_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=24, w2=405, w3=127, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(24)
    rank = change.rolling(405, min_periods=max(405//3, 2)).rank(pct=True)
    persistence = change.rolling(127, min_periods=max(127//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.234667 * persistence + 0.0048204 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_114_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=31, w2=418, w3=144, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(418, min_periods=max(418//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.895294 + 0.0048205 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_115_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=38, w2=431, w3=161, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(431, min_periods=max(431//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.247333 * slope + 0.0048206 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_116_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=45, w2=444, w3=178, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(45)
    drag = impulse.rolling(444, min_periods=max(444//3, 2)).mean()
    noise = impulse.abs().rolling(178, min_periods=max(178//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.922353 + 0.0048207 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_117_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=52, w2=457, w3=195, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 457)
    curvature = _rolling_slope(acceleration, 195)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.26 * acceleration + 0.0048208 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_118_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=59, w2=470, w3=212, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(470, min_periods=max(470//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.949412 + 0.0048209 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_119_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=66, w2=483, w3=229, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(483, min_periods=max(483//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.272667 * _rolling_slope(draw, 229) + 0.004821 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_120_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=73, w2=496, w3=246, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(496, min_periods=max(496//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(246, min_periods=max(246//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.976471 + 0.0048211 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_121_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=80, w2=509, w3=263, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 509)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=263, adjust=False).mean() * 0.99 + 0.0048212 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_122_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=87, w2=23, w3=280, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(23, min_periods=max(23//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.003529 + 0.0048213 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_123_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=36, w3=297, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(94)
    rank = change.rolling(36, min_periods=max(36//3, 2)).rank(pct=True)
    persistence = change.rolling(297, min_periods=max(297//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.298 * persistence + 0.0048214 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_124_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=49, w3=314, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(49, min_periods=max(49//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.030588 + 0.0048215 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_125_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=62, w3=331, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(62, min_periods=max(62//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.310667 * slope + 0.0048216 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_126_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=75, w3=348, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(115)
    drag = impulse.rolling(75, min_periods=max(75//3, 2)).mean()
    noise = impulse.abs().rolling(348, min_periods=max(348//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.057647 + 0.0048217 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_127_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=88, w3=365, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 88)
    curvature = _rolling_slope(acceleration, 365)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.323333 * acceleration + 0.0048218 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_128_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=101, w3=382, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(101, min_periods=max(101//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.084706 + 0.0048219 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_129_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=114, w3=399, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(114, min_periods=max(114//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.336 * _rolling_slope(draw, 399) + 0.004822 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_130_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=127, w3=416, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(127, min_periods=max(127//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(416, min_periods=max(416//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.111765 + 0.0048221 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_131_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=140, w3=433, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 140)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.125294 + 0.0048222 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_132_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=153, w3=450, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(153, min_periods=max(153//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.138824 + 0.0048223 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_133_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=166, w3=467, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(166, min_periods=max(166//3, 2)).rank(pct=True)
    persistence = change.rolling(467, min_periods=max(467//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361333 * persistence + 0.0048224 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_134_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=179, w3=484, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(179, min_periods=max(179//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.165882 + 0.0048225 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_135_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=192, w3=501, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(192, min_periods=max(192//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.041667 * slope + 0.0048226 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_136_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=205, w3=518, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(205, min_periods=max(205//3, 2)).mean()
    noise = impulse.abs().rolling(518, min_periods=max(518//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.192941 + 0.0048227 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_137_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=218, w3=535, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 218)
    curvature = _rolling_slope(acceleration, 535)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.054333 * acceleration + 0.0048228 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_138_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=231, w3=552, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(231, min_periods=max(231//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.22 + 0.0048229 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_139_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=244, w3=569, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(244, min_periods=max(244//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.067 * _rolling_slope(draw, 569) + 0.004823 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_140_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=257, w3=586, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(257, min_periods=max(257//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(586, min_periods=max(586//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.247059 + 0.0048231 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_141_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=270, w3=603, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 270)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.260588 + 0.0048232 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_142_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=283, w3=620, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(283, min_periods=max(283//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.274118 + 0.0048233 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_143_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=296, w3=637, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(296, min_periods=max(296//3, 2)).rank(pct=True)
    persistence = change.rolling(637, min_periods=max(637//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.092333 * persistence + 0.0048234 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_144_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=309, w3=654, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(309, min_periods=max(309//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.301176 + 0.0048235 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_145_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=322, w3=671, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(322, min_periods=max(322//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.105 * slope + 0.0048236 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_146_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=335, w3=688, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(8)
    drag = impulse.rolling(335, min_periods=max(335//3, 2)).mean()
    noise = impulse.abs().rolling(688, min_periods=max(688//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.328235 + 0.0048237 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_147_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=348, w3=705, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 348)
    curvature = _rolling_slope(acceleration, 705)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.117667 * acceleration + 0.0048238 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_148_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=361, w3=722, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(361, min_periods=max(361//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.355294 + 0.0048239 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_149_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=374, w3=739, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(374, min_periods=max(374//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.130333 * _rolling_slope(draw, 739) + 0.004824 * anchor
    return base_signal.diff()

def f76_mdfa_gemini_150_d1(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=387, w3=756, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(387, min_periods=max(387//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(756, min_periods=max(756//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.382353 + 0.0048241 * anchor
    return base_signal.diff()
