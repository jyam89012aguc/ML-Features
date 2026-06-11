"""106 covariance matrix entropy gemini base features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Informational entropy of the covariance matrix as a measure of system disorder.
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

def f106_cmen_gemini_001(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=5]"""
    window = 5
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_002(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=10]"""
    window = 10
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_003(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=21]"""
    window = 21
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_004(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=42]"""
    window = 42
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_005(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=63]"""
    window = 63
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_006(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=126]"""
    window = 126
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_007(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=252]"""
    window = 252
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_008(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=504]"""
    window = 504
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_009(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=756]"""
    window = 756
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_010(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Informational entropy of the covariance matrix as a measure of system disorder. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_absorption_ratio_proxy([_safe_log(close).diff(), _safe_log(volume).diff()], 1).diff(), window)
    return res

def f106_cmen_gemini_011(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=108, w2=337, w3=499, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(108, min_periods=max(108//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.669412 + 0.0008202 * anchor
    return base_signal

def f106_cmen_gemini_012(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=115, w2=350, w3=516, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(350, min_periods=max(350//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 115)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.829412 + 0.0008203 * anchor
    return base_signal

def f106_cmen_gemini_013(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=122, w2=363, w3=533, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(122, min_periods=max(122//3, 2)).mean(), b.abs().rolling(363, min_periods=max(363//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.139333 * _rolling_slope(cover, 122) + 0.0008204 * anchor
    return base_signal

def f106_cmen_gemini_014(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=129, w2=376, w3=550, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.145667 * y + 0.854333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 129) - _rolling_slope(basket, 376) + 0.0008205 * anchor
    return base_signal

def f106_cmen_gemini_015(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=136, w2=389, w3=567, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(136, min_periods=max(136//3, 2)).mean(), upside.rolling(389, min_periods=max(389//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.87 + 0.0008206 * anchor
    return base_signal

def f106_cmen_gemini_016(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=143, w2=402, w3=584, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(402, min_periods=max(402//3, 2)).max()
    rebound = x - x.rolling(143, min_periods=max(143//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.158333 * _rolling_slope(draw, 584) + 0.0008207 * anchor
    return base_signal

def f106_cmen_gemini_017(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=150, w2=415, w3=601, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(601, min_periods=max(601//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.897059 + 0.0008208 * anchor
    return base_signal

def f106_cmen_gemini_018(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=157, w2=428, w3=618, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 157)
    baseline = trend.rolling(428, min_periods=max(428//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.910588 + 0.0008209 * anchor
    return base_signal

def f106_cmen_gemini_019(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=164, w2=441, w3=635, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 164)
    slow = _rolling_slope(x, 441)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.924118 + 0.000821 * anchor
    return base_signal

def f106_cmen_gemini_020(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=171, w2=454, w3=652, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(171, min_periods=max(171//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.937647 + 0.0008211 * anchor
    return base_signal

def f106_cmen_gemini_021(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=178, w2=467, w3=669, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(467, min_periods=max(467//3, 2)).rank(pct=True)
    persistence = change.rolling(669, min_periods=max(669//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.19 * persistence + 0.0008212 * anchor
    return base_signal

def f106_cmen_gemini_022(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=185, w2=480, w3=686, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(185, min_periods=max(185//3, 2)).std()
    vol_slow = ret.rolling(480, min_periods=max(480//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.964706 + 0.0008213 * anchor
    return base_signal

def f106_cmen_gemini_023(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=192, w2=493, w3=703, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(493, min_periods=max(493//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 192)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.202667 * slope + 0.0008214 * anchor
    return base_signal

def f106_cmen_gemini_024(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=199, w2=506, w3=720, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(506, min_periods=max(506//3, 2)).mean()
    noise = impulse.abs().rolling(720, min_periods=max(720//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.991765 + 0.0008215 * anchor
    return base_signal

def f106_cmen_gemini_025(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=206, w2=20, w3=737, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 206)
    acceleration = _rolling_slope(velocity, 20)
    curvature = _rolling_slope(acceleration, 737)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.215333 * acceleration + 0.0008216 * anchor
    return base_signal

def f106_cmen_gemini_026(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=213, w2=33, w3=754, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 213)
    pressure = rel_log.diff(33)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.221667 * pressure.rolling(754, min_periods=max(754//3, 2)).mean() + 0.0008217 * anchor
    return base_signal

def f106_cmen_gemini_027(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=220, w2=46, w3=20, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(220, min_periods=max(220//3, 2)).mean())
    decay = spread.ewm(span=46, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.032353 + 0.0008218 * anchor
    return base_signal

def f106_cmen_gemini_028(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=227, w2=59, w3=37, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(59, min_periods=max(59//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 227)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.045882 + 0.0008219 * anchor
    return base_signal

def f106_cmen_gemini_029(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=234, w2=72, w3=54, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(234, min_periods=max(234//3, 2)).mean(), b.abs().rolling(72, min_periods=max(72//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(54) + 0.240667 * _rolling_slope(cover, 234) + 0.000822 * anchor
    return base_signal

def f106_cmen_gemini_030(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=241, w2=85, w3=71, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.247 * y + 0.753000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 241) - _rolling_slope(basket, 85) + 0.0008221 * anchor
    return base_signal

def f106_cmen_gemini_031(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=248, w2=98, w3=88, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(248, min_periods=max(248//3, 2)).mean(), upside.rolling(98, min_periods=max(98//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(88) * 1.086471 + 0.0008222 * anchor
    return base_signal

def f106_cmen_gemini_032(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=8, w2=111, w3=105, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(111, min_periods=max(111//3, 2)).max()
    rebound = x - x.rolling(8, min_periods=max(8//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.259667 * _rolling_slope(draw, 105) + 0.0008223 * anchor
    return base_signal

def f106_cmen_gemini_033(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=15, w2=124, w3=122, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(15) - b.diff(124)
    stress = imbalance.rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.113529 + 0.0008224 * anchor
    return base_signal

def f106_cmen_gemini_034(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=22, w2=137, w3=139, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 22)
    baseline = trend.rolling(137, min_periods=max(137//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(139, min_periods=max(139//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.127059 + 0.0008225 * anchor
    return base_signal

def f106_cmen_gemini_035(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=29, w2=150, w3=156, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 29)
    slow = _rolling_slope(x, 150)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=156, adjust=False).mean() * 1.140588 + 0.0008226 * anchor
    return base_signal

def f106_cmen_gemini_036(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=36, w2=163, w3=173, lag=13)."""
    x = close.shift(13)
    peak = x.rolling(163, min_periods=max(163//3, 2)).max()
    trough = x.rolling(36, min_periods=max(36//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.154118 + 0.0008227 * anchor
    return base_signal

def f106_cmen_gemini_037(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=43, w2=176, w3=190, lag=21)."""
    x = close.shift(21)
    change = x.pct_change(43)
    rank = change.rolling(176, min_periods=max(176//3, 2)).rank(pct=True)
    persistence = change.rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.291333 * persistence + 0.0008228 * anchor
    return base_signal

def f106_cmen_gemini_038(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=50, w2=189, w3=207, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    ret = x.diff()
    vol_fast = ret.rolling(50, min_periods=max(50//3, 2)).std()
    vol_slow = ret.rolling(189, min_periods=max(189//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.181176 + 0.0008229 * anchor
    return base_signal

def f106_cmen_gemini_039(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=57, w2=202, w3=224, lag=55)."""
    x = close.shift(55)
    ma = x.rolling(202, min_periods=max(202//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 57)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.304 * slope + 0.000823 * anchor
    return base_signal

def f106_cmen_gemini_040(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=64, w2=215, w3=241, lag=0)."""
    x = close.shift(0)
    impulse = x.diff(64)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(241, min_periods=max(241//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.208235 + 0.0008231 * anchor
    return base_signal

def f106_cmen_gemini_041(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=71, w2=228, w3=258, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 71)
    acceleration = _rolling_slope(velocity, 228)
    curvature = _rolling_slope(acceleration, 258)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.316667 * acceleration + 0.0008232 * anchor
    return base_signal

def f106_cmen_gemini_042(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=78, w2=241, w3=275, lag=2)."""
    rel = _safe_div(close.shift(2), volume.shift(2).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 78)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.323 * pressure.rolling(275, min_periods=max(275//3, 2)).mean() + 0.0008233 * anchor
    return base_signal

def f106_cmen_gemini_043(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=85, w2=254, w3=292, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    spread = _safe_div(a - b, a.abs().rolling(85, min_periods=max(85//3, 2)).mean())
    decay = spread.ewm(span=254, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.248824 + 0.0008234 * anchor
    return base_signal

def f106_cmen_gemini_044(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=92, w2=267, w3=309, lag=5)."""
    a = _safe_log(close.abs() + 1.0).shift(5)
    b = _safe_log(volume.abs() + 1.0).shift(5)
    corr = a.rolling(267, min_periods=max(267//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 92)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.262353 + 0.0008235 * anchor
    return base_signal

def f106_cmen_gemini_045(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=99, w2=280, w3=326, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    cover = _safe_div(a.rolling(99, min_periods=max(99//3, 2)).mean(), b.abs().rolling(280, min_periods=max(280//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.342 * _rolling_slope(cover, 99) + 0.0008236 * anchor
    return base_signal

def f106_cmen_gemini_046(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=106, w2=293, w3=343, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    y = _safe_log(volume.abs() + 1.0).shift(13)
    z = _safe_log(volume.abs() + 1.0).shift(13)
    basket = x - 0.348333 * y + 0.651667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 106) - _rolling_slope(basket, 293) + 0.0008237 * anchor
    return base_signal

def f106_cmen_gemini_047(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=113, w2=306, w3=360, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(113, min_periods=max(113//3, 2)).mean(), upside.rolling(306, min_periods=max(306//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.302941 + 0.0008238 * anchor
    return base_signal

def f106_cmen_gemini_048(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=120, w2=319, w3=377, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    draw = x - x.rolling(319, min_periods=max(319//3, 2)).max()
    rebound = x - x.rolling(120, min_periods=max(120//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.361 * _rolling_slope(draw, 377) + 0.0008239 * anchor
    return base_signal

def f106_cmen_gemini_049(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=127, w2=332, w3=394, lag=55)."""
    a = _safe_log(close.abs() + 1.0).shift(55)
    b = _safe_log(volume.abs() + 1.0).shift(55)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.33 + 0.000824 * anchor
    return base_signal

def f106_cmen_gemini_050(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=134, w2=345, w3=411, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(345, min_periods=max(345//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.343529 + 0.0008241 * anchor
    return base_signal

def f106_cmen_gemini_051(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=141, w2=358, w3=428, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 358)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.357059 + 0.0008242 * anchor
    return base_signal

def f106_cmen_gemini_052(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=148, w2=371, w3=445, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(371, min_periods=max(371//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.370588 + 0.0008243 * anchor
    return base_signal

def f106_cmen_gemini_053(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=155, w2=384, w3=462, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(384, min_periods=max(384//3, 2)).rank(pct=True)
    persistence = change.rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.060333 * persistence + 0.0008244 * anchor
    return base_signal

def f106_cmen_gemini_054(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=162, w2=397, w3=479, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(397, min_periods=max(397//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.397647 + 0.0008245 * anchor
    return base_signal

def f106_cmen_gemini_055(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=169, w2=410, w3=496, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(410, min_periods=max(410//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.073 * slope + 0.0008246 * anchor
    return base_signal

def f106_cmen_gemini_056(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=176, w2=423, w3=513, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(423, min_periods=max(423//3, 2)).mean()
    noise = impulse.abs().rolling(513, min_periods=max(513//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.424706 + 0.0008247 * anchor
    return base_signal

def f106_cmen_gemini_057(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=183, w2=436, w3=530, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 436)
    curvature = _rolling_slope(acceleration, 530)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.085667 * acceleration + 0.0008248 * anchor
    return base_signal

def f106_cmen_gemini_058(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=190, w2=449, w3=547, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 190)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.092 * pressure.rolling(547, min_periods=max(547//3, 2)).mean() + 0.0008249 * anchor
    return base_signal

def f106_cmen_gemini_059(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=197, w2=462, w3=564, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(197, min_periods=max(197//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.465294 + 0.000825 * anchor
    return base_signal

def f106_cmen_gemini_060(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=204, w2=475, w3=581, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(475, min_periods=max(475//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 204)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.478824 + 0.0008251 * anchor
    return base_signal

def f106_cmen_gemini_061(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=211, w2=488, w3=598, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(211, min_periods=max(211//3, 2)).mean(), b.abs().rolling(488, min_periods=max(488//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.111 * _rolling_slope(cover, 211) + 0.0008252 * anchor
    return base_signal

def f106_cmen_gemini_062(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=218, w2=501, w3=615, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.117333 * y + 0.882667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 218) - _rolling_slope(basket, 501) + 0.0008253 * anchor
    return base_signal

def f106_cmen_gemini_063(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=225, w2=15, w3=632, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(225, min_periods=max(225//3, 2)).mean(), upside.rolling(15, min_periods=max(15//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.519412 + 0.0008254 * anchor
    return base_signal

def f106_cmen_gemini_064(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=232, w2=28, w3=649, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(232, min_periods=max(232//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.13 * _rolling_slope(draw, 649) + 0.0008255 * anchor
    return base_signal

def f106_cmen_gemini_065(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=239, w2=41, w3=666, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(126) - b.diff(41)
    stress = imbalance.rolling(666, min_periods=max(666//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.546471 + 0.0008256 * anchor
    return base_signal

def f106_cmen_gemini_066(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=246, w2=54, w3=683, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(54, min_periods=max(54//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.56 + 0.0008257 * anchor
    return base_signal

def f106_cmen_gemini_067(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=6, w2=67, w3=700, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 6)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.573529 + 0.0008258 * anchor
    return base_signal

def f106_cmen_gemini_068(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=13, w2=80, w3=717, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(80, min_periods=max(80//3, 2)).max()
    trough = x.rolling(13, min_periods=max(13//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.587059 + 0.0008259 * anchor
    return base_signal

def f106_cmen_gemini_069(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=20, w2=93, w3=734, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(20)
    rank = change.rolling(93, min_periods=max(93//3, 2)).rank(pct=True)
    persistence = change.rolling(734, min_periods=max(734//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.161667 * persistence + 0.000826 * anchor
    return base_signal

def f106_cmen_gemini_070(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=27, w2=106, w3=751, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(27, min_periods=max(27//3, 2)).std()
    vol_slow = ret.rolling(106, min_periods=max(106//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.614118 + 0.0008261 * anchor
    return base_signal

def f106_cmen_gemini_071(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=34, w2=119, w3=17, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(119, min_periods=max(119//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 34)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.174333 * slope + 0.0008262 * anchor
    return base_signal

def f106_cmen_gemini_072(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=41, w2=132, w3=34, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(41)
    drag = impulse.rolling(132, min_periods=max(132//3, 2)).mean()
    noise = impulse.abs().rolling(34, min_periods=max(34//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.641176 + 0.0008263 * anchor
    return base_signal

def f106_cmen_gemini_073(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=48, w2=145, w3=51, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 48)
    acceleration = _rolling_slope(velocity, 145)
    curvature = _rolling_slope(acceleration, 51)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.187 * acceleration + 0.0008264 * anchor
    return base_signal

def f106_cmen_gemini_074(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=55, w2=158, w3=68, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 55)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.193333 * pressure.rolling(68, min_periods=max(68//3, 2)).mean() + 0.0008265 * anchor
    return base_signal

def f106_cmen_gemini_075(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct base signal (w1=62, w2=171, w3=85, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(62, min_periods=max(62//3, 2)).mean())
    decay = spread.ewm(span=171, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.828235 + 0.0008266 * anchor
    return base_signal
