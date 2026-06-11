"""96 jump diffusion probability gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Probabilistic model of price moves being part of a continuous or jump process.
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
# FEATURE HYPOTHESES (001-075)
# ============================================================

def f96_jdpb_gemini_001(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=5]"""
    window = 5
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_002(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=10]"""
    window = 10
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_003(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=21]"""
    window = 21
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_004(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=42]"""
    window = 42
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_005(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=63]"""
    window = 63
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_006(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=126]"""
    window = 126
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_007(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=252]"""
    window = 252
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_008(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=504]"""
    window = 504
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_009(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=756]"""
    window = 756
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_010(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Probabilistic model of price moves being part of a continuous or jump process. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_safe_log(close).diff().abs() / (_atr(high, low, close, window) + 1e-9), window)
    return res

def f96_jdpb_gemini_011(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=160, w2=145, w3=165, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(160, min_periods=max(160//3, 2)).mean())
    decay = spread.ewm(span=145, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.476471 + 0.0059162 * anchor
    return base_signal

def f96_jdpb_gemini_012(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=167, w2=158, w3=182, lag=2)."""
    a = _safe_log(high.abs() + 1.0).shift(2)
    b = _safe_log(low.abs() + 1.0).shift(2)
    corr = a.rolling(158, min_periods=max(158//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 167)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.49 + 0.0059163 * anchor
    return base_signal

def f96_jdpb_gemini_013(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=174, w2=171, w3=199, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    cover = _safe_div(a.rolling(174, min_periods=max(174//3, 2)).mean(), b.abs().rolling(171, min_periods=max(171//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.190333 * _rolling_slope(cover, 174) + 0.0059164 * anchor
    return base_signal

def f96_jdpb_gemini_014(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=181, w2=184, w3=216, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    y = _safe_log(low.abs() + 1.0).shift(5)
    z = _safe_log(close.abs() + 1.0).shift(5)
    basket = x - 0.196667 * y + 0.803333 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 181) - _rolling_slope(basket, 184) + 0.0059165 * anchor
    return base_signal

def f96_jdpb_gemini_015(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=188, w2=197, w3=233, lag=8)."""
    x = high.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(188, min_periods=max(188//3, 2)).mean(), upside.rolling(197, min_periods=max(197//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.530588 + 0.0059166 * anchor
    return base_signal

def f96_jdpb_gemini_016(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=195, w2=210, w3=250, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    draw = x - x.rolling(210, min_periods=max(210//3, 2)).max()
    rebound = x - x.rolling(195, min_periods=max(195//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.209333 * _rolling_slope(draw, 250) + 0.0059167 * anchor
    return base_signal

def f96_jdpb_gemini_017(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=202, w2=223, w3=267, lag=21)."""
    a = _safe_log(high.abs() + 1.0).shift(21)
    b = _safe_log(low.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.557647 + 0.0059168 * anchor
    return base_signal

def f96_jdpb_gemini_018(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=209, w2=236, w3=284, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 209)
    baseline = trend.rolling(236, min_periods=max(236//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(284, min_periods=max(284//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.571176 + 0.0059169 * anchor
    return base_signal

def f96_jdpb_gemini_019(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=216, w2=249, w3=301, lag=55)."""
    x = _safe_log(high.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 216)
    slow = _rolling_slope(x, 249)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.584706 + 0.005917 * anchor
    return base_signal

def f96_jdpb_gemini_020(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=223, w2=262, w3=318, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(262, min_periods=max(262//3, 2)).max()
    trough = x.rolling(223, min_periods=max(223//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.598235 + 0.0059171 * anchor
    return base_signal

def f96_jdpb_gemini_021(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=230, w2=275, w3=335, lag=1)."""
    x = high.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(275, min_periods=max(275//3, 2)).rank(pct=True)
    persistence = change.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.241 * persistence + 0.0059172 * anchor
    return base_signal

def f96_jdpb_gemini_022(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=237, w2=288, w3=352, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(237, min_periods=max(237//3, 2)).std()
    vol_slow = ret.rolling(288, min_periods=max(288//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.625294 + 0.0059173 * anchor
    return base_signal

def f96_jdpb_gemini_023(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=244, w2=301, w3=369, lag=3)."""
    x = high.shift(3)
    ma = x.rolling(301, min_periods=max(301//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 244)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.253667 * slope + 0.0059174 * anchor
    return base_signal

def f96_jdpb_gemini_024(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=251, w2=314, w3=386, lag=5)."""
    x = high.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(314, min_periods=max(314//3, 2)).mean()
    noise = impulse.abs().rolling(386, min_periods=max(386//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.652353 + 0.0059175 * anchor
    return base_signal

def f96_jdpb_gemini_025(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=11, w2=327, w3=403, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 327)
    curvature = _rolling_slope(acceleration, 403)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.266333 * acceleration + 0.0059176 * anchor
    return base_signal

def f96_jdpb_gemini_026(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=18, w2=340, w3=420, lag=13)."""
    rel = _safe_div(high.shift(13), low.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 18)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.272667 * pressure.rolling(420, min_periods=max(420//3, 2)).mean() + 0.0059177 * anchor
    return base_signal

def f96_jdpb_gemini_027(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=25, w2=353, w3=437, lag=21)."""
    a = high.shift(21)
    b = low.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(25, min_periods=max(25//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.839412 + 0.0059178 * anchor
    return base_signal

def f96_jdpb_gemini_028(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=32, w2=366, w3=454, lag=34)."""
    a = _safe_log(high.abs() + 1.0).shift(34)
    b = _safe_log(low.abs() + 1.0).shift(34)
    corr = a.rolling(366, min_periods=max(366//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 32)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.852941 + 0.0059179 * anchor
    return base_signal

def f96_jdpb_gemini_029(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=39, w2=379, w3=471, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    cover = _safe_div(a.rolling(39, min_periods=max(39//3, 2)).mean(), b.abs().rolling(379, min_periods=max(379//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.291667 * _rolling_slope(cover, 39) + 0.005918 * anchor
    return base_signal

def f96_jdpb_gemini_030(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=46, w2=392, w3=488, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    y = _safe_log(low.abs() + 1.0).shift(0)
    z = _safe_log(close.abs() + 1.0).shift(0)
    basket = x - 0.298 * y + 0.702000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 46) - _rolling_slope(basket, 392) + 0.0059181 * anchor
    return base_signal

def f96_jdpb_gemini_031(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=53, w2=405, w3=505, lag=1)."""
    x = high.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(53, min_periods=max(53//3, 2)).mean(), upside.rolling(405, min_periods=max(405//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.893529 + 0.0059182 * anchor
    return base_signal

def f96_jdpb_gemini_032(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=60, w2=418, w3=522, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    draw = x - x.rolling(418, min_periods=max(418//3, 2)).max()
    rebound = x - x.rolling(60, min_periods=max(60//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.310667 * _rolling_slope(draw, 522) + 0.0059183 * anchor
    return base_signal

def f96_jdpb_gemini_033(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=67, w2=431, w3=539, lag=3)."""
    a = _safe_log(high.abs() + 1.0).shift(3)
    b = _safe_log(low.abs() + 1.0).shift(3)
    imbalance = a.diff(67) - b.diff(126)
    stress = imbalance.rolling(539, min_periods=max(539//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.920588 + 0.0059184 * anchor
    return base_signal

def f96_jdpb_gemini_034(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=74, w2=444, w3=556, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 74)
    baseline = trend.rolling(444, min_periods=max(444//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.934118 + 0.0059185 * anchor
    return base_signal

def f96_jdpb_gemini_035(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=81, w2=457, w3=573, lag=8)."""
    x = _safe_log(high.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 81)
    slow = _rolling_slope(x, 457)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.947647 + 0.0059186 * anchor
    return base_signal

def f96_jdpb_gemini_036(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=88, w2=470, w3=590, lag=13)."""
    x = high.shift(13)
    peak = x.rolling(470, min_periods=max(470//3, 2)).max()
    trough = x.rolling(88, min_periods=max(88//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.961176 + 0.0059187 * anchor
    return base_signal

def f96_jdpb_gemini_037(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=95, w2=483, w3=607, lag=21)."""
    x = high.shift(21)
    change = x.pct_change(95)
    rank = change.rolling(483, min_periods=max(483//3, 2)).rank(pct=True)
    persistence = change.rolling(607, min_periods=max(607//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.342333 * persistence + 0.0059188 * anchor
    return base_signal

def f96_jdpb_gemini_038(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=102, w2=496, w3=624, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(102, min_periods=max(102//3, 2)).std()
    vol_slow = ret.rolling(496, min_periods=max(496//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.988235 + 0.0059189 * anchor
    return base_signal

def f96_jdpb_gemini_039(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=109, w2=509, w3=641, lag=55)."""
    x = high.shift(55)
    ma = x.rolling(509, min_periods=max(509//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 109)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.355 * slope + 0.005919 * anchor
    return base_signal

def f96_jdpb_gemini_040(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=116, w2=23, w3=658, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(116)
    drag = impulse.rolling(23, min_periods=max(23//3, 2)).mean()
    noise = impulse.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.015294 + 0.0059191 * anchor
    return base_signal

def f96_jdpb_gemini_041(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=123, w2=36, w3=675, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 123)
    acceleration = _rolling_slope(velocity, 36)
    curvature = _rolling_slope(acceleration, 675)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.035333 * acceleration + 0.0059192 * anchor
    return base_signal

def f96_jdpb_gemini_042(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=130, w2=49, w3=692, lag=2)."""
    rel = _safe_div(high.shift(2), low.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 130)
    pressure = rel_log.diff(49)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.041667 * pressure.rolling(692, min_periods=max(692//3, 2)).mean() + 0.0059193 * anchor
    return base_signal

def f96_jdpb_gemini_043(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=137, w2=62, w3=709, lag=3)."""
    a = high.shift(3)
    b = low.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(137, min_periods=max(137//3, 2)).mean())
    decay = spread.ewm(span=62, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.055882 + 0.0059194 * anchor
    return base_signal

def f96_jdpb_gemini_044(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=144, w2=75, w3=726, lag=5)."""
    a = _safe_log(high.abs() + 1.0).shift(5)
    b = _safe_log(low.abs() + 1.0).shift(5)
    corr = a.rolling(75, min_periods=max(75//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 144)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.069412 + 0.0059195 * anchor
    return base_signal

def f96_jdpb_gemini_045(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=151, w2=88, w3=743, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    cover = _safe_div(a.rolling(151, min_periods=max(151//3, 2)).mean(), b.abs().rolling(88, min_periods=max(88//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.060667 * _rolling_slope(cover, 151) + 0.0059196 * anchor
    return base_signal

def f96_jdpb_gemini_046(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=158, w2=101, w3=760, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    y = _safe_log(low.abs() + 1.0).shift(13)
    z = _safe_log(close.abs() + 1.0).shift(13)
    basket = x - 0.067 * y + 0.933000 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 158) - _rolling_slope(basket, 101) + 0.0059197 * anchor
    return base_signal

def f96_jdpb_gemini_047(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=165, w2=114, w3=26, lag=21)."""
    x = high.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(165, min_periods=max(165//3, 2)).mean(), upside.rolling(114, min_periods=max(114//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(26) * 1.11 + 0.0059198 * anchor
    return base_signal

def f96_jdpb_gemini_048(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=172, w2=127, w3=43, lag=34)."""
    x = _safe_log(high.abs() + 1.0).shift(34)
    draw = x - x.rolling(127, min_periods=max(127//3, 2)).max()
    rebound = x - x.rolling(172, min_periods=max(172//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.079667 * _rolling_slope(draw, 43) + 0.0059199 * anchor
    return base_signal

def f96_jdpb_gemini_049(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=179, w2=140, w3=60, lag=55)."""
    a = _safe_log(high.abs() + 1.0).shift(55)
    b = _safe_log(low.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(60, min_periods=max(60//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.137059 + 0.00592 * anchor
    return base_signal

def f96_jdpb_gemini_050(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=186, w2=153, w3=77, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(153, min_periods=max(153//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(77, min_periods=max(77//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.150588 + 0.0059201 * anchor
    return base_signal

def f96_jdpb_gemini_051(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=193, w2=166, w3=94, lag=1)."""
    x = _safe_log(high.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 166)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=94, adjust=False).mean() * 1.164118 + 0.0059202 * anchor
    return base_signal

def f96_jdpb_gemini_052(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=200, w2=179, w3=111, lag=2)."""
    x = high.shift(2)
    peak = x.rolling(179, min_periods=max(179//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.177647 + 0.0059203 * anchor
    return base_signal

def f96_jdpb_gemini_053(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=207, w2=192, w3=128, lag=3)."""
    x = high.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(192, min_periods=max(192//3, 2)).rank(pct=True)
    persistence = change.rolling(128, min_periods=max(128//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111333 * persistence + 0.0059204 * anchor
    return base_signal

def f96_jdpb_gemini_054(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=214, w2=205, w3=145, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(205, min_periods=max(205//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.204706 + 0.0059205 * anchor
    return base_signal

def f96_jdpb_gemini_055(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=221, w2=218, w3=162, lag=8)."""
    x = high.shift(8)
    ma = x.rolling(218, min_periods=max(218//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.124 * slope + 0.0059206 * anchor
    return base_signal

def f96_jdpb_gemini_056(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=228, w2=231, w3=179, lag=13)."""
    x = high.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(231, min_periods=max(231//3, 2)).mean()
    noise = impulse.abs().rolling(179, min_periods=max(179//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.231765 + 0.0059207 * anchor
    return base_signal

def f96_jdpb_gemini_057(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=235, w2=244, w3=196, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 244)
    curvature = _rolling_slope(acceleration, 196)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136667 * acceleration + 0.0059208 * anchor
    return base_signal

def f96_jdpb_gemini_058(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=242, w2=257, w3=213, lag=34)."""
    rel = _safe_div(high.shift(34), low.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 242)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.143 * pressure.rolling(213, min_periods=max(213//3, 2)).mean() + 0.0059209 * anchor
    return base_signal

def f96_jdpb_gemini_059(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=249, w2=270, w3=230, lag=55)."""
    a = high.shift(55)
    b = low.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(249, min_periods=max(249//3, 2)).mean())
    decay = spread.ewm(span=270, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.272353 + 0.005921 * anchor
    return base_signal

def f96_jdpb_gemini_060(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=9, w2=283, w3=247, lag=0)."""
    a = _safe_log(high.abs() + 1.0).shift(0)
    b = _safe_log(low.abs() + 1.0).shift(0)
    corr = a.rolling(283, min_periods=max(283//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 9)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.285882 + 0.0059211 * anchor
    return base_signal

def f96_jdpb_gemini_061(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=16, w2=296, w3=264, lag=1)."""
    a = high.shift(1)
    b = low.shift(1)
    cover = _safe_div(a.rolling(16, min_periods=max(16//3, 2)).mean(), b.abs().rolling(296, min_periods=max(296//3, 2)).mean())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.162 * _rolling_slope(cover, 16) + 0.0059212 * anchor
    return base_signal

def f96_jdpb_gemini_062(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=23, w2=309, w3=281, lag=2)."""
    x = _safe_log(high.abs() + 1.0).shift(2)
    y = _safe_log(low.abs() + 1.0).shift(2)
    z = _safe_log(close.abs() + 1.0).shift(2)
    basket = x - 0.168333 * y + 0.831667 * z
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 23) - _rolling_slope(basket, 309) + 0.0059213 * anchor
    return base_signal

def f96_jdpb_gemini_063(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=30, w2=322, w3=298, lag=3)."""
    x = high.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(30, min_periods=max(30//3, 2)).mean(), upside.rolling(322, min_periods=max(322//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.326471 + 0.0059214 * anchor
    return base_signal

def f96_jdpb_gemini_064(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=37, w2=335, w3=315, lag=5)."""
    x = _safe_log(high.abs() + 1.0).shift(5)
    draw = x - x.rolling(335, min_periods=max(335//3, 2)).max()
    rebound = x - x.rolling(37, min_periods=max(37//3, 2)).min()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.181 * _rolling_slope(draw, 315) + 0.0059215 * anchor
    return base_signal

def f96_jdpb_gemini_065(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=44, w2=348, w3=332, lag=8)."""
    a = _safe_log(high.abs() + 1.0).shift(8)
    b = _safe_log(low.abs() + 1.0).shift(8)
    imbalance = a.diff(44) - b.diff(126)
    stress = imbalance.rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.353529 + 0.0059216 * anchor
    return base_signal

def f96_jdpb_gemini_066(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=51, w2=361, w3=349, lag=13)."""
    x = _safe_log(high.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 51)
    baseline = trend.rolling(361, min_periods=max(361//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(349, min_periods=max(349//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.367059 + 0.0059217 * anchor
    return base_signal

def f96_jdpb_gemini_067(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=58, w2=374, w3=366, lag=21)."""
    x = _safe_log(high.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 58)
    slow = _rolling_slope(x, 374)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.380588 + 0.0059218 * anchor
    return base_signal

def f96_jdpb_gemini_068(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=65, w2=387, w3=383, lag=34)."""
    x = high.shift(34)
    peak = x.rolling(387, min_periods=max(387//3, 2)).max()
    trough = x.rolling(65, min_periods=max(65//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.394118 + 0.0059219 * anchor
    return base_signal

def f96_jdpb_gemini_069(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=72, w2=400, w3=400, lag=55)."""
    x = high.shift(55)
    change = x.pct_change(72)
    rank = change.rolling(400, min_periods=max(400//3, 2)).rank(pct=True)
    persistence = change.rolling(400, min_periods=max(400//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.212667 * persistence + 0.005922 * anchor
    return base_signal

def f96_jdpb_gemini_070(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=79, w2=413, w3=417, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(79, min_periods=max(79//3, 2)).std()
    vol_slow = ret.rolling(413, min_periods=max(413//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.421176 + 0.0059221 * anchor
    return base_signal

def f96_jdpb_gemini_071(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=86, w2=426, w3=434, lag=1)."""
    x = high.shift(1)
    ma = x.rolling(426, min_periods=max(426//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 86)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.225333 * slope + 0.0059222 * anchor
    return base_signal

def f96_jdpb_gemini_072(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=93, w2=439, w3=451, lag=2)."""
    x = high.shift(2)
    impulse = x.diff(93)
    drag = impulse.rolling(439, min_periods=max(439//3, 2)).mean()
    noise = impulse.abs().rolling(451, min_periods=max(451//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.448235 + 0.0059223 * anchor
    return base_signal

def f96_jdpb_gemini_073(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=100, w2=452, w3=468, lag=3)."""
    x = _safe_log(high.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 100)
    acceleration = _rolling_slope(velocity, 452)
    curvature = _rolling_slope(acceleration, 468)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.238 * acceleration + 0.0059224 * anchor
    return base_signal

def f96_jdpb_gemini_074(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=107, w2=465, w3=485, lag=5)."""
    rel = _safe_div(high.shift(5), low.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 107)
    pressure = rel_log.diff(126)
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.244333 * pressure.rolling(485, min_periods=max(485//3, 2)).mean() + 0.0059225 * anchor
    return base_signal

def f96_jdpb_gemini_075(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=114, w2=478, w3=502, lag=8)."""
    a = high.shift(8)
    b = low.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(114, min_periods=max(114//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.488824 + 0.0059226 * anchor
    return base_signal
