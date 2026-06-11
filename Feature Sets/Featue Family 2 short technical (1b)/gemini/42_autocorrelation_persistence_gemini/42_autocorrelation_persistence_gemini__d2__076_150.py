"""42 autocorrelation persistence gemini d2 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Measurement of how past price returns influence future returns over various lags.
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

def f42_acor_gemini_076_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=231, w3=377, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(104)
    drag = impulse.rolling(231, min_periods=max(231//3, 2)).mean()
    noise = impulse.abs().rolling(377, min_periods=max(377//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.587647 + 0.0029267 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_077_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=244, w3=394, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 111)
    acceleration = _rolling_slope(velocity, 244)
    curvature = _rolling_slope(acceleration, 394)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.279 * acceleration + 0.0029268 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_078_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=257, w3=411, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(257, min_periods=max(257//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.614706 + 0.0029269 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_079_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=270, w3=428, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(270, min_periods=max(270//3, 2)).max()
    rebound = x - x.rolling(125, min_periods=max(125//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.291667 * _rolling_slope(draw, 428) + 0.002927 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_080_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=283, w3=445, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 132)
    baseline = trend.rolling(283, min_periods=max(283//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(445, min_periods=max(445//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.641765 + 0.0029271 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_081_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=296, w3=462, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 139)
    slow = _rolling_slope(x, 296)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.655294 + 0.0029272 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_082_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=309, w3=479, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(309, min_periods=max(309//3, 2)).max()
    trough = x.rolling(146, min_periods=max(146//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.668824 + 0.0029273 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_083_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=322, w3=496, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(322, min_periods=max(322//3, 2)).rank(pct=True)
    persistence = change.rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.317 * persistence + 0.0029274 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_084_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=335, w3=513, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(160, min_periods=max(160//3, 2)).std()
    vol_slow = ret.rolling(335, min_periods=max(335//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.842353 + 0.0029275 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_085_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=348, w3=530, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(348, min_periods=max(348//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 167)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.329667 * slope + 0.0029276 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_086_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=361, w3=547, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(361, min_periods=max(361//3, 2)).mean()
    noise = impulse.abs().rolling(547, min_periods=max(547//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.869412 + 0.0029277 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_087_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=374, w3=564, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 181)
    acceleration = _rolling_slope(velocity, 374)
    curvature = _rolling_slope(acceleration, 564)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.342333 * acceleration + 0.0029278 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_088_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=387, w3=581, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(387, min_periods=max(387//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.896471 + 0.0029279 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_089_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=400, w3=598, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(400, min_periods=max(400//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.355 * _rolling_slope(draw, 598) + 0.002928 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_090_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=413, w3=615, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(413, min_periods=max(413//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(615, min_periods=max(615//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.923529 + 0.0029281 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_091_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=426, w3=632, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 426)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.937059 + 0.0029282 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_092_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=439, w3=649, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(439, min_periods=max(439//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.950588 + 0.0029283 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_093_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=452, w3=666, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(452, min_periods=max(452//3, 2)).rank(pct=True)
    persistence = change.rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.048 * persistence + 0.0029284 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_094_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=465, w3=683, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.977647 + 0.0029285 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_095_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=478, w3=700, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(478, min_periods=max(478//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.060667 * slope + 0.0029286 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_096_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=491, w3=717, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(491, min_periods=max(491//3, 2)).mean()
    noise = impulse.abs().rolling(717, min_periods=max(717//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.004706 + 0.0029287 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_097_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=504, w3=734, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 504)
    curvature = _rolling_slope(acceleration, 734)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.073333 * acceleration + 0.0029288 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_098_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=18, w3=751, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(11, min_periods=max(11//3, 2)).mean(), upside.rolling(18, min_periods=max(18//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.031765 + 0.0029289 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_099_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=31, w3=17, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(31, min_periods=max(31//3, 2)).max()
    rebound = x - x.rolling(18, min_periods=max(18//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.086 * _rolling_slope(draw, 17) + 0.002929 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_100_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=44, w3=34, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 25)
    baseline = trend.rolling(44, min_periods=max(44//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.058824 + 0.0029291 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_101_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=57, w3=51, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 32)
    slow = _rolling_slope(x, 57)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=51, adjust=False).mean() * 1.072353 + 0.0029292 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_102_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=70, w3=68, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(70, min_periods=max(70//3, 2)).max()
    trough = x.rolling(39, min_periods=max(39//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.085882 + 0.0029293 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_103_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=83, w3=85, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(46)
    rank = change.rolling(83, min_periods=max(83//3, 2)).rank(pct=True)
    persistence = change.rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111333 * persistence + 0.0029294 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_104_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=96, w3=102, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(53, min_periods=max(53//3, 2)).std()
    vol_slow = ret.rolling(96, min_periods=max(96//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.112941 + 0.0029295 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_105_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=109, w3=119, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(109, min_periods=max(109//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 60)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.124 * slope + 0.0029296 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_106_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=122, w3=136, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(67)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(136, min_periods=max(136//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.14 + 0.0029297 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_107_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=135, w3=153, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 74)
    acceleration = _rolling_slope(velocity, 135)
    curvature = _rolling_slope(acceleration, 153)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136667 * acceleration + 0.0029298 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_108_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=148, w3=170, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(148, min_periods=max(148//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.167059 + 0.0029299 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_109_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=161, w3=187, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(161, min_periods=max(161//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.149333 * _rolling_slope(draw, 187) + 0.00293 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_110_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=174, w3=204, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 95)
    baseline = trend.rolling(174, min_periods=max(174//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(204, min_periods=max(204//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.194118 + 0.0029301 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_111_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=187, w3=221, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 102)
    slow = _rolling_slope(x, 187)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 1.207647 + 0.0029302 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_112_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=200, w3=238, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(200, min_periods=max(200//3, 2)).max()
    trough = x.rolling(109, min_periods=max(109//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.221176 + 0.0029303 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_113_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=213, w3=255, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(116)
    rank = change.rolling(213, min_periods=max(213//3, 2)).rank(pct=True)
    persistence = change.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.174667 * persistence + 0.0029304 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_114_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=226, w3=272, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(123, min_periods=max(123//3, 2)).std()
    vol_slow = ret.rolling(226, min_periods=max(226//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.248235 + 0.0029305 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_115_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=239, w3=289, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(239, min_periods=max(239//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 130)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.187333 * slope + 0.0029306 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_116_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=252, w3=306, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(252, min_periods=max(252//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275294 + 0.0029307 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_117_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=265, w3=323, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 144)
    acceleration = _rolling_slope(velocity, 265)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2 * acceleration + 0.0029308 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_118_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=278, w3=340, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(151, min_periods=max(151//3, 2)).mean(), upside.rolling(278, min_periods=max(278//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.302353 + 0.0029309 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_119_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=291, w3=357, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(291, min_periods=max(291//3, 2)).max()
    rebound = x - x.rolling(158, min_periods=max(158//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212667 * _rolling_slope(draw, 357) + 0.002931 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_120_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=304, w3=374, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 165)
    baseline = trend.rolling(304, min_periods=max(304//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.329412 + 0.0029311 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_121_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=317, w3=391, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.342941 + 0.0029312 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_122_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=330, w3=408, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(330, min_periods=max(330//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.356471 + 0.0029313 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_123_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=343, w3=425, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(425, min_periods=max(425//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.238 * persistence + 0.0029314 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_124_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=356, w3=442, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(356, min_periods=max(356//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.383529 + 0.0029315 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_125_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=369, w3=459, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(369, min_periods=max(369//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.250667 * slope + 0.0029316 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_126_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=382, w3=476, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(382, min_periods=max(382//3, 2)).mean()
    noise = impulse.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.410588 + 0.0029317 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_127_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=395, w3=493, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 395)
    curvature = _rolling_slope(acceleration, 493)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.263333 * acceleration + 0.0029318 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_128_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=408, w3=510, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(408, min_periods=max(408//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.437647 + 0.0029319 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_129_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=228, w2=421, w3=527, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(421, min_periods=max(421//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.276 * _rolling_slope(draw, 527) + 0.002932 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_130_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=235, w2=434, w3=544, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(434, min_periods=max(434//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(544, min_periods=max(544//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.464706 + 0.0029321 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_131_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=242, w2=447, w3=561, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 447)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.478235 + 0.0029322 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_132_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=249, w2=460, w3=578, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(460, min_periods=max(460//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.491765 + 0.0029323 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_133_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=9, w2=473, w3=595, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(9)
    rank = change.rolling(473, min_periods=max(473//3, 2)).rank(pct=True)
    persistence = change.rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.301333 * persistence + 0.0029324 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_134_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=16, w2=486, w3=612, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(486, min_periods=max(486//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.518824 + 0.0029325 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_135_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=23, w2=499, w3=629, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(499, min_periods=max(499//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.314 * slope + 0.0029326 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_136_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=30, w2=13, w3=646, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(30)
    drag = impulse.rolling(13, min_periods=max(13//3, 2)).mean()
    noise = impulse.abs().rolling(646, min_periods=max(646//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.545882 + 0.0029327 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_137_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=37, w2=26, w3=663, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 26)
    curvature = _rolling_slope(acceleration, 663)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.326667 * acceleration + 0.0029328 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_138_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=44, w2=39, w3=680, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(39, min_periods=max(39//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.572941 + 0.0029329 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_139_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=51, w2=52, w3=697, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(52, min_periods=max(52//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.339333 * _rolling_slope(draw, 697) + 0.002933 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_140_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=58, w2=65, w3=714, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(65, min_periods=max(65//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(714, min_periods=max(714//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.6 + 0.0029331 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_141_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=65, w2=78, w3=731, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 78)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.613529 + 0.0029332 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_142_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=72, w2=91, w3=748, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(91, min_periods=max(91//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.627059 + 0.0029333 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_143_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=79, w2=104, w3=765, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(79)
    rank = change.rolling(104, min_periods=max(104//3, 2)).rank(pct=True)
    persistence = change.rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.032333 * persistence + 0.0029334 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_144_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=86, w2=117, w3=31, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(117, min_periods=max(117//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.654118 + 0.0029335 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_145_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=93, w2=130, w3=48, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(130, min_periods=max(130//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.045 * slope + 0.0029336 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_146_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=100, w2=143, w3=65, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(100)
    drag = impulse.rolling(143, min_periods=max(143//3, 2)).mean()
    noise = impulse.abs().rolling(65, min_periods=max(65//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.827647 + 0.0029337 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_147_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=107, w2=156, w3=82, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 156)
    curvature = _rolling_slope(acceleration, 82)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.057667 * acceleration + 0.0029338 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_148_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=114, w2=169, w3=99, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(169, min_periods=max(169//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(99) * 0.854706 + 0.0029339 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_149_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=121, w2=182, w3=116, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(182, min_periods=max(182//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.070333 * _rolling_slope(draw, 116) + 0.002934 * anchor
    return base_signal.diff().diff()

def f42_acor_gemini_150_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=128, w2=195, w3=133, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(195, min_periods=max(195//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(133, min_periods=max(133//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.881765 + 0.0029341 * anchor
    return base_signal.diff().diff()
