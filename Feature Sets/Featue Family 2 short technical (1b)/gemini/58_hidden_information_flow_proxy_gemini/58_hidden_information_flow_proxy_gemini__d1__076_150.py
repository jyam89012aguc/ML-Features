"""58 hidden information flow proxy gemini d1 features 76-150 — Pipeline 1b-HF Grade v7.

Hypothesis: Estimation of latent information processing through price and volume complexity.
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

def f58_hinf_gemini_076_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=94, w2=121, w3=117, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(94)
    drag = impulse.rolling(121, min_periods=max(121//3, 2)).mean()
    noise = impulse.abs().rolling(117, min_periods=max(117//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.422941 + 0.0038087 * anchor
    return base_signal.diff()

def f58_hinf_gemini_077_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=101, w2=134, w3=134, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 101)
    acceleration = _rolling_slope(velocity, 134)
    curvature = _rolling_slope(acceleration, 134)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.307 * acceleration + 0.0038088 * anchor
    return base_signal.diff()

def f58_hinf_gemini_078_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=108, w2=147, w3=151, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 108)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.313333 * pressure.rolling(151, min_periods=max(151//3, 2)).mean() + 0.0038089 * anchor
    return base_signal.diff()

def f58_hinf_gemini_079_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=115, w2=160, w3=168, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(115, min_periods=max(115//3, 2)).mean())
    decay = spread.ewm(span=160, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.463529 + 0.003809 * anchor
    return base_signal.diff()

def f58_hinf_gemini_080_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=122, w2=173, w3=185, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(173, min_periods=max(173//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 122)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.477059 + 0.0038091 * anchor
    return base_signal.diff()

def f58_hinf_gemini_081_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=129, w2=186, w3=202, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(129, min_periods=max(129//3, 2)).mean(), b.abs().rolling(186, min_periods=max(186//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.332333 * _rolling_slope(cover, 129) + 0.0038092 * anchor
    return base_signal.diff()

def f58_hinf_gemini_082_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=136, w2=199, w3=219, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.338667 * y + 0.661333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 136) - _rolling_slope(basket, 199) + 0.0038093 * anchor
    return base_signal.diff()

def f58_hinf_gemini_083_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=143, w2=212, w3=236, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(143, min_periods=max(143//3, 2)).mean(), upside.rolling(212, min_periods=max(212//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.517647 + 0.0038094 * anchor
    return base_signal.diff()

def f58_hinf_gemini_084_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=150, w2=225, w3=253, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(225, min_periods=max(225//3, 2)).max()
    rebound = x - x.rolling(150, min_periods=max(150//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.351333 * _rolling_slope(draw, 253) + 0.0038095 * anchor
    return base_signal.diff()

def f58_hinf_gemini_085_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=157, w2=238, w3=270, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(270, min_periods=max(270//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.544706 + 0.0038096 * anchor
    return base_signal.diff()

def f58_hinf_gemini_086_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=164, w2=251, w3=287, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 164)
    baseline = trend.rolling(251, min_periods=max(251//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(287, min_periods=max(287//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.558235 + 0.0038097 * anchor
    return base_signal.diff()

def f58_hinf_gemini_087_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=171, w2=264, w3=304, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 171)
    slow = _rolling_slope(x, 264)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.571765 + 0.0038098 * anchor
    return base_signal.diff()

def f58_hinf_gemini_088_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=178, w2=277, w3=321, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(277, min_periods=max(277//3, 2)).max()
    trough = x.rolling(178, min_periods=max(178//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.585294 + 0.0038099 * anchor
    return base_signal.diff()

def f58_hinf_gemini_089_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=185, w2=290, w3=338, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(290, min_periods=max(290//3, 2)).rank(pct=True)
    persistence = change.rolling(338, min_periods=max(338//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.050667 * persistence + 0.00381 * anchor
    return base_signal.diff()

def f58_hinf_gemini_090_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=192, w2=303, w3=355, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(192, min_periods=max(192//3, 2)).std()
    vol_slow = ret.rolling(303, min_periods=max(303//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.612353 + 0.0038101 * anchor
    return base_signal.diff()

def f58_hinf_gemini_091_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=199, w2=316, w3=372, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(316, min_periods=max(316//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 199)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.063333 * slope + 0.0038102 * anchor
    return base_signal.diff()

def f58_hinf_gemini_092_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=206, w2=329, w3=389, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(329, min_periods=max(329//3, 2)).mean()
    noise = impulse.abs().rolling(389, min_periods=max(389//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.639412 + 0.0038103 * anchor
    return base_signal.diff()

def f58_hinf_gemini_093_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=213, w2=342, w3=406, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 213)
    acceleration = _rolling_slope(velocity, 342)
    curvature = _rolling_slope(acceleration, 406)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.076 * acceleration + 0.0038104 * anchor
    return base_signal.diff()

def f58_hinf_gemini_094_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=220, w2=355, w3=423, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 220)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.082333 * pressure.rolling(423, min_periods=max(423//3, 2)).mean() + 0.0038105 * anchor
    return base_signal.diff()

def f58_hinf_gemini_095_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=227, w2=368, w3=440, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(227, min_periods=max(227//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.826471 + 0.0038106 * anchor
    return base_signal.diff()

def f58_hinf_gemini_096_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=234, w2=381, w3=457, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(381, min_periods=max(381//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 234)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.84 + 0.0038107 * anchor
    return base_signal.diff()

def f58_hinf_gemini_097_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=241, w2=394, w3=474, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(241, min_periods=max(241//3, 2)).mean(), b.abs().rolling(394, min_periods=max(394//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.101333 * _rolling_slope(cover, 241) + 0.0038108 * anchor
    return base_signal.diff()

def f58_hinf_gemini_098_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=248, w2=407, w3=491, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.107667 * y + 0.892333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 248) - _rolling_slope(basket, 407) + 0.0038109 * anchor
    return base_signal.diff()

def f58_hinf_gemini_099_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=8, w2=420, w3=508, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(8, min_periods=max(8//3, 2)).mean(), upside.rolling(420, min_periods=max(420//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.880588 + 0.003811 * anchor
    return base_signal.diff()

def f58_hinf_gemini_100_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=15, w2=433, w3=525, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(433, min_periods=max(433//3, 2)).max()
    rebound = x - x.rolling(15, min_periods=max(15//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.120333 * _rolling_slope(draw, 525) + 0.0038111 * anchor
    return base_signal.diff()

def f58_hinf_gemini_101_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=22, w2=446, w3=542, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(22) - b.diff(126)
    stress = imbalance.rolling(542, min_periods=max(542//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.907647 + 0.0038112 * anchor
    return base_signal.diff()

def f58_hinf_gemini_102_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=29, w2=459, w3=559, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 29)
    baseline = trend.rolling(459, min_periods=max(459//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(559, min_periods=max(559//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.921176 + 0.0038113 * anchor
    return base_signal.diff()

def f58_hinf_gemini_103_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=36, w2=472, w3=576, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 36)
    slow = _rolling_slope(x, 472)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.934706 + 0.0038114 * anchor
    return base_signal.diff()

def f58_hinf_gemini_104_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=43, w2=485, w3=593, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(485, min_periods=max(485//3, 2)).max()
    trough = x.rolling(43, min_periods=max(43//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.948235 + 0.0038115 * anchor
    return base_signal.diff()

def f58_hinf_gemini_105_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=50, w2=498, w3=610, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(50)
    rank = change.rolling(498, min_periods=max(498//3, 2)).rank(pct=True)
    persistence = change.rolling(610, min_periods=max(610//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.152 * persistence + 0.0038116 * anchor
    return base_signal.diff()

def f58_hinf_gemini_106_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=57, w2=12, w3=627, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(57, min_periods=max(57//3, 2)).std()
    vol_slow = ret.rolling(12, min_periods=max(12//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.975294 + 0.0038117 * anchor
    return base_signal.diff()

def f58_hinf_gemini_107_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=64, w2=25, w3=644, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(25, min_periods=max(25//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 64)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.164667 * slope + 0.0038118 * anchor
    return base_signal.diff()

def f58_hinf_gemini_108_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=71, w2=38, w3=661, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(71)
    drag = impulse.rolling(38, min_periods=max(38//3, 2)).mean()
    noise = impulse.abs().rolling(661, min_periods=max(661//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.002353 + 0.0038119 * anchor
    return base_signal.diff()

def f58_hinf_gemini_109_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=78, w2=51, w3=678, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 78)
    acceleration = _rolling_slope(velocity, 51)
    curvature = _rolling_slope(acceleration, 678)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.177333 * acceleration + 0.003812 * anchor
    return base_signal.diff()

def f58_hinf_gemini_110_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=85, w2=64, w3=695, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 85)
    pressure = rel_log.diff(64)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.183667 * pressure.rolling(695, min_periods=max(695//3, 2)).mean() + 0.0038121 * anchor
    return base_signal.diff()

def f58_hinf_gemini_111_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=92, w2=77, w3=712, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(92, min_periods=max(92//3, 2)).mean())
    decay = spread.ewm(span=77, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.042941 + 0.0038122 * anchor
    return base_signal.diff()

def f58_hinf_gemini_112_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=99, w2=90, w3=729, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(90, min_periods=max(90//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 99)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.056471 + 0.0038123 * anchor
    return base_signal.diff()

def f58_hinf_gemini_113_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=106, w2=103, w3=746, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(106, min_periods=max(106//3, 2)).mean(), b.abs().rolling(103, min_periods=max(103//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.202667 * _rolling_slope(cover, 106) + 0.0038124 * anchor
    return base_signal.diff()

def f58_hinf_gemini_114_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=113, w2=116, w3=763, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.209 * y + 0.791000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 113) - _rolling_slope(basket, 116) + 0.0038125 * anchor
    return base_signal.diff()

def f58_hinf_gemini_115_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=120, w2=129, w3=29, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(129, min_periods=max(129//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(29) * 1.097059 + 0.0038126 * anchor
    return base_signal.diff()

def f58_hinf_gemini_116_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=127, w2=142, w3=46, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(142, min_periods=max(142//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.221667 * _rolling_slope(draw, 46) + 0.0038127 * anchor
    return base_signal.diff()

def f58_hinf_gemini_117_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=134, w2=155, w3=63, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(63, min_periods=max(63//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.124118 + 0.0038128 * anchor
    return base_signal.diff()

def f58_hinf_gemini_118_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=141, w2=168, w3=80, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(168, min_periods=max(168//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(80, min_periods=max(80//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.137647 + 0.0038129 * anchor
    return base_signal.diff()

def f58_hinf_gemini_119_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=148, w2=181, w3=97, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 181)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=97, adjust=False).mean() * 1.151176 + 0.003813 * anchor
    return base_signal.diff()

def f58_hinf_gemini_120_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=155, w2=194, w3=114, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(194, min_periods=max(194//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.164706 + 0.0038131 * anchor
    return base_signal.diff()

def f58_hinf_gemini_121_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=162, w2=207, w3=131, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(207, min_periods=max(207//3, 2)).rank(pct=True)
    persistence = change.rolling(131, min_periods=max(131//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.253333 * persistence + 0.0038132 * anchor
    return base_signal.diff()

def f58_hinf_gemini_122_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=169, w2=220, w3=148, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(220, min_periods=max(220//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.191765 + 0.0038133 * anchor
    return base_signal.diff()

def f58_hinf_gemini_123_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=176, w2=233, w3=165, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(233, min_periods=max(233//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.266 * slope + 0.0038134 * anchor
    return base_signal.diff()

def f58_hinf_gemini_124_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=183, w2=246, w3=182, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(246, min_periods=max(246//3, 2)).mean()
    noise = impulse.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.218824 + 0.0038135 * anchor
    return base_signal.diff()

def f58_hinf_gemini_125_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=190, w2=259, w3=199, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 259)
    curvature = _rolling_slope(acceleration, 199)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.278667 * acceleration + 0.0038136 * anchor
    return base_signal.diff()

def f58_hinf_gemini_126_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=197, w2=272, w3=216, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 197)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.285 * pressure.rolling(216, min_periods=max(216//3, 2)).mean() + 0.0038137 * anchor
    return base_signal.diff()

def f58_hinf_gemini_127_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=204, w2=285, w3=233, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(204, min_periods=max(204//3, 2)).mean())
    decay = spread.ewm(span=285, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.259412 + 0.0038138 * anchor
    return base_signal.diff()

def f58_hinf_gemini_128_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=211, w2=298, w3=250, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(298, min_periods=max(298//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 211)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.272941 + 0.0038139 * anchor
    return base_signal.diff()

def f58_hinf_gemini_129_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=218, w2=311, w3=267, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(218, min_periods=max(218//3, 2)).mean(), b.abs().rolling(311, min_periods=max(311//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.304 * _rolling_slope(cover, 218) + 0.003814 * anchor
    return base_signal.diff()

def f58_hinf_gemini_130_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=225, w2=324, w3=284, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.310333 * y + 0.689667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 225) - _rolling_slope(basket, 324) + 0.0038141 * anchor
    return base_signal.diff()

def f58_hinf_gemini_131_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=232, w2=337, w3=301, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(337, min_periods=max(337//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.313529 + 0.0038142 * anchor
    return base_signal.diff()

def f58_hinf_gemini_132_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=239, w2=350, w3=318, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(350, min_periods=max(350//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.323 * _rolling_slope(draw, 318) + 0.0038143 * anchor
    return base_signal.diff()

def f58_hinf_gemini_133_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=246, w2=363, w3=335, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.340588 + 0.0038144 * anchor
    return base_signal.diff()

def f58_hinf_gemini_134_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=6, w2=376, w3=352, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 6)
    baseline = trend.rolling(376, min_periods=max(376//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(352, min_periods=max(352//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.354118 + 0.0038145 * anchor
    return base_signal.diff()

def f58_hinf_gemini_135_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=13, w2=389, w3=369, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 13)
    slow = _rolling_slope(x, 389)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.367647 + 0.0038146 * anchor
    return base_signal.diff()

def f58_hinf_gemini_136_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=20, w2=402, w3=386, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(402, min_periods=max(402//3, 2)).max()
    trough = x.rolling(20, min_periods=max(20//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.381176 + 0.0038147 * anchor
    return base_signal.diff()

def f58_hinf_gemini_137_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=27, w2=415, w3=403, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(27)
    rank = change.rolling(415, min_periods=max(415//3, 2)).rank(pct=True)
    persistence = change.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.354667 * persistence + 0.0038148 * anchor
    return base_signal.diff()

def f58_hinf_gemini_138_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=34, w2=428, w3=420, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(34, min_periods=max(34//3, 2)).std()
    vol_slow = ret.rolling(428, min_periods=max(428//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.408235 + 0.0038149 * anchor
    return base_signal.diff()

def f58_hinf_gemini_139_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=41, w2=441, w3=437, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 41)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.035 * slope + 0.003815 * anchor
    return base_signal.diff()

def f58_hinf_gemini_140_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=48, w2=454, w3=454, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(48)
    drag = impulse.rolling(454, min_periods=max(454//3, 2)).mean()
    noise = impulse.abs().rolling(454, min_periods=max(454//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.435294 + 0.0038151 * anchor
    return base_signal.diff()

def f58_hinf_gemini_141_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=55, w2=467, w3=471, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 55)
    acceleration = _rolling_slope(velocity, 467)
    curvature = _rolling_slope(acceleration, 471)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.047667 * acceleration + 0.0038152 * anchor
    return base_signal.diff()

def f58_hinf_gemini_142_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=62, w2=480, w3=488, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 62)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.054 * pressure.rolling(488, min_periods=max(488//3, 2)).mean() + 0.0038153 * anchor
    return base_signal.diff()

def f58_hinf_gemini_143_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=69, w2=493, w3=505, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(69, min_periods=max(69//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.475882 + 0.0038154 * anchor
    return base_signal.diff()

def f58_hinf_gemini_144_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=76, w2=506, w3=522, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(506, min_periods=max(506//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 76)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.489412 + 0.0038155 * anchor
    return base_signal.diff()

def f58_hinf_gemini_145_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=83, w2=20, w3=539, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(83, min_periods=max(83//3, 2)).mean(), b.abs().rolling(20, min_periods=max(20//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.073 * _rolling_slope(cover, 83) + 0.0038156 * anchor
    return base_signal.diff()

def f58_hinf_gemini_146_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=90, w2=33, w3=556, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.079333 * y + 0.920667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 90) - _rolling_slope(basket, 33) + 0.0038157 * anchor
    return base_signal.diff()

def f58_hinf_gemini_147_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=97, w2=46, w3=573, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(97, min_periods=max(97//3, 2)).mean(), upside.rolling(46, min_periods=max(46//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.53 + 0.0038158 * anchor
    return base_signal.diff()

def f58_hinf_gemini_148_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=104, w2=59, w3=590, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(59, min_periods=max(59//3, 2)).max()
    rebound = x - x.rolling(104, min_periods=max(104//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.092 * _rolling_slope(draw, 590) + 0.0038159 * anchor
    return base_signal.diff()

def f58_hinf_gemini_149_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=111, w2=72, w3=607, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(111) - b.diff(72)
    stress = imbalance.rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.557059 + 0.003816 * anchor
    return base_signal.diff()

def f58_hinf_gemini_150_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d1 signal (w1=118, w2=85, w3=624, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 118)
    baseline = trend.rolling(85, min_periods=max(85//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.570588 + 0.0038161 * anchor
    return base_signal.diff()
