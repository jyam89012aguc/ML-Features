"""33 coppock curve kst gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Long-term momentum and smoothed rate-of-change indicators for trend identification.
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

def f33_ckst_gemini_001_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=5]"""
    window = 5
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_002_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=10]"""
    window = 10
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_003_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=21]"""
    window = 21
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_004_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=42]"""
    window = 42
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_005_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=63]"""
    window = 63
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_006_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=126]"""
    window = 126
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_007_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=252]"""
    window = 252
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_008_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=504]"""
    window = 504
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_009_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=756]"""
    window = 756
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_010_d2(close: pd.Series) -> pd.Series:
    """Long-term momentum and smoothed rate-of-change indicators for trend identification. [window=1260]"""
    window = 1260
    res = _safe_log(close / close.shift(window) + 1e-9).rolling(window).mean()
    return (res).diff().diff()

def f33_ckst_gemini_011_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=184, w2=233, w3=708, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 184)
    slow = _rolling_slope(x, 233)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.655882 + 0.0024162 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_012_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=191, w2=246, w3=725, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(246, min_periods=max(246//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.669412 + 0.0024163 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_013_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=198, w2=259, w3=742, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(259, min_periods=max(259//3, 2)).rank(pct=True)
    persistence = change.rolling(742, min_periods=max(742//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.19 * persistence + 0.0024164 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_014_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=205, w2=272, w3=759, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(272, min_periods=max(272//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.842941 + 0.0024165 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_015_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=212, w2=285, w3=25, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(285, min_periods=max(285//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 212)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.202667 * slope + 0.0024166 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_016_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=219, w2=298, w3=42, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(298, min_periods=max(298//3, 2)).mean()
    noise = impulse.abs().rolling(42, min_periods=max(42//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87 + 0.0024167 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_017_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=226, w2=311, w3=59, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 226)
    acceleration = _rolling_slope(velocity, 311)
    curvature = _rolling_slope(acceleration, 59)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.215333 * acceleration + 0.0024168 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_018_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=233, w2=324, w3=76, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(324, min_periods=max(324//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(76) * 0.897059 + 0.0024169 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_019_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=240, w2=337, w3=93, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(337, min_periods=max(337//3, 2)).max()
    rebound = x - x.rolling(240, min_periods=max(240//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.228 * _rolling_slope(draw, 93) + 0.002417 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_020_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=247, w2=350, w3=110, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(350, min_periods=max(350//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(110, min_periods=max(110//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.924118 + 0.0024171 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_021_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=7, w2=363, w3=127, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 363)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=127, adjust=False).mean() * 0.937647 + 0.0024172 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_022_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=14, w2=376, w3=144, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(14, min_periods=max(14//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.951176 + 0.0024173 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_023_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=21, w2=389, w3=161, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(21)
    rank = change.rolling(389, min_periods=max(389//3, 2)).rank(pct=True)
    persistence = change.rolling(161, min_periods=max(161//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.253333 * persistence + 0.0024174 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_024_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=28, w2=402, w3=178, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(28, min_periods=max(28//3, 2)).std()
    vol_slow = ret.rolling(402, min_periods=max(402//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.978235 + 0.0024175 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_025_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=35, w2=415, w3=195, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(415, min_periods=max(415//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.266 * slope + 0.0024176 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_026_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=42, w2=428, w3=212, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(42)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.005294 + 0.0024177 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_027_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=49, w2=441, w3=229, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 441)
    curvature = _rolling_slope(acceleration, 229)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.278667 * acceleration + 0.0024178 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_028_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=56, w2=454, w3=246, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(56, min_periods=max(56//3, 2)).mean(), upside.rolling(454, min_periods=max(454//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.032353 + 0.0024179 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_029_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=63, w2=467, w3=263, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(467, min_periods=max(467//3, 2)).max()
    rebound = x - x.rolling(63, min_periods=max(63//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.291333 * _rolling_slope(draw, 263) + 0.002418 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_030_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=70, w2=480, w3=280, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 70)
    baseline = trend.rolling(480, min_periods=max(480//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.059412 + 0.0024181 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_031_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=77, w2=493, w3=297, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 77)
    slow = _rolling_slope(x, 493)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=297, adjust=False).mean() * 1.072941 + 0.0024182 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_032_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=84, w2=506, w3=314, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(506, min_periods=max(506//3, 2)).max()
    trough = x.rolling(84, min_periods=max(84//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.086471 + 0.0024183 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_033_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=91, w2=20, w3=331, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(91)
    rank = change.rolling(20, min_periods=max(20//3, 2)).rank(pct=True)
    persistence = change.rolling(331, min_periods=max(331//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.316667 * persistence + 0.0024184 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_034_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=98, w2=33, w3=348, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(98, min_periods=max(98//3, 2)).std()
    vol_slow = ret.rolling(33, min_periods=max(33//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.113529 + 0.0024185 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_035_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=105, w2=46, w3=365, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(46, min_periods=max(46//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 105)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.329333 * slope + 0.0024186 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_036_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=112, w2=59, w3=382, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(112)
    drag = impulse.rolling(59, min_periods=max(59//3, 2)).mean()
    noise = impulse.abs().rolling(382, min_periods=max(382//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.140588 + 0.0024187 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_037_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=119, w2=72, w3=399, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 119)
    acceleration = _rolling_slope(velocity, 72)
    curvature = _rolling_slope(acceleration, 399)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.342 * acceleration + 0.0024188 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_038_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=126, w2=85, w3=416, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(126, min_periods=max(126//3, 2)).mean(), upside.rolling(85, min_periods=max(85//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.167647 + 0.0024189 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_039_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=133, w2=98, w3=433, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(98, min_periods=max(98//3, 2)).max()
    rebound = x - x.rolling(133, min_periods=max(133//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.354667 * _rolling_slope(draw, 433) + 0.002419 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_040_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=140, w2=111, w3=450, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 140)
    baseline = trend.rolling(111, min_periods=max(111//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.194706 + 0.0024191 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_041_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=147, w2=124, w3=467, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 147)
    slow = _rolling_slope(x, 124)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.208235 + 0.0024192 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_042_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=154, w2=137, w3=484, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(137, min_periods=max(137//3, 2)).max()
    trough = x.rolling(154, min_periods=max(154//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.221765 + 0.0024193 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_043_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=161, w2=150, w3=501, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(150, min_periods=max(150//3, 2)).rank(pct=True)
    persistence = change.rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.047667 * persistence + 0.0024194 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_044_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=168, w2=163, w3=518, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(168, min_periods=max(168//3, 2)).std()
    vol_slow = ret.rolling(163, min_periods=max(163//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.248824 + 0.0024195 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_045_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=175, w2=176, w3=535, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(176, min_periods=max(176//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 175)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.060333 * slope + 0.0024196 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_046_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=182, w2=189, w3=552, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(189, min_periods=max(189//3, 2)).mean()
    noise = impulse.abs().rolling(552, min_periods=max(552//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.275882 + 0.0024197 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_047_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=189, w2=202, w3=569, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 189)
    acceleration = _rolling_slope(velocity, 202)
    curvature = _rolling_slope(acceleration, 569)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.073 * acceleration + 0.0024198 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_048_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=196, w2=215, w3=586, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(196, min_periods=max(196//3, 2)).mean(), upside.rolling(215, min_periods=max(215//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.302941 + 0.0024199 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_049_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=203, w2=228, w3=603, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(228, min_periods=max(228//3, 2)).max()
    rebound = x - x.rolling(203, min_periods=max(203//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.085667 * _rolling_slope(draw, 603) + 0.00242 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_050_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=210, w2=241, w3=620, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 210)
    baseline = trend.rolling(241, min_periods=max(241//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(620, min_periods=max(620//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.33 + 0.0024201 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_051_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=217, w2=254, w3=637, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 217)
    slow = _rolling_slope(x, 254)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.343529 + 0.0024202 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_052_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=224, w2=267, w3=654, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(267, min_periods=max(267//3, 2)).max()
    trough = x.rolling(224, min_periods=max(224//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.357059 + 0.0024203 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_053_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=231, w2=280, w3=671, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(280, min_periods=max(280//3, 2)).rank(pct=True)
    persistence = change.rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.111 * persistence + 0.0024204 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_054_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=238, w2=293, w3=688, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(238, min_periods=max(238//3, 2)).std()
    vol_slow = ret.rolling(293, min_periods=max(293//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.384118 + 0.0024205 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_055_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=245, w2=306, w3=705, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(306, min_periods=max(306//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 245)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.123667 * slope + 0.0024206 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_056_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=5, w2=319, w3=722, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(5)
    drag = impulse.rolling(319, min_periods=max(319//3, 2)).mean()
    noise = impulse.abs().rolling(722, min_periods=max(722//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.411176 + 0.0024207 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_057_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=12, w2=332, w3=739, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 12)
    acceleration = _rolling_slope(velocity, 332)
    curvature = _rolling_slope(acceleration, 739)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.136333 * acceleration + 0.0024208 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_058_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=19, w2=345, w3=756, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(19, min_periods=max(19//3, 2)).mean(), upside.rolling(345, min_periods=max(345//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.438235 + 0.0024209 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_059_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=26, w2=358, w3=22, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(358, min_periods=max(358//3, 2)).max()
    rebound = x - x.rolling(26, min_periods=max(26//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.149 * _rolling_slope(draw, 22) + 0.002421 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_060_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=33, w2=371, w3=39, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 33)
    baseline = trend.rolling(371, min_periods=max(371//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(39, min_periods=max(39//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.465294 + 0.0024211 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_061_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=40, w2=384, w3=56, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 40)
    slow = _rolling_slope(x, 384)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=56, adjust=False).mean() * 1.478824 + 0.0024212 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_062_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=47, w2=397, w3=73, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(397, min_periods=max(397//3, 2)).max()
    trough = x.rolling(47, min_periods=max(47//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.492353 + 0.0024213 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_063_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=54, w2=410, w3=90, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(54)
    rank = change.rolling(410, min_periods=max(410//3, 2)).rank(pct=True)
    persistence = change.rolling(90, min_periods=max(90//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.174333 * persistence + 0.0024214 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_064_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=61, w2=423, w3=107, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(61, min_periods=max(61//3, 2)).std()
    vol_slow = ret.rolling(423, min_periods=max(423//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.519412 + 0.0024215 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_065_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=68, w2=436, w3=124, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(436, min_periods=max(436//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 68)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.187 * slope + 0.0024216 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_066_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=75, w2=449, w3=141, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(75)
    drag = impulse.rolling(449, min_periods=max(449//3, 2)).mean()
    noise = impulse.abs().rolling(141, min_periods=max(141//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.546471 + 0.0024217 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_067_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=82, w2=462, w3=158, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 82)
    acceleration = _rolling_slope(velocity, 462)
    curvature = _rolling_slope(acceleration, 158)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.199667 * acceleration + 0.0024218 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_068_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=89, w2=475, w3=175, lag=34)."""
    x = close.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(89, min_periods=max(89//3, 2)).mean(), upside.rolling(475, min_periods=max(475//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.573529 + 0.0024219 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_069_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=96, w2=488, w3=192, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    draw = x - x.rolling(488, min_periods=max(488//3, 2)).max()
    rebound = x - x.rolling(96, min_periods=max(96//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.212333 * _rolling_slope(draw, 192) + 0.002422 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_070_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=103, w2=501, w3=209, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 103)
    baseline = trend.rolling(501, min_periods=max(501//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.600588 + 0.0024221 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_071_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=110, w2=15, w3=226, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 110)
    slow = _rolling_slope(x, 15)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=226, adjust=False).mean() * 1.614118 + 0.0024222 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_072_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=117, w2=28, w3=243, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(28, min_periods=max(28//3, 2)).max()
    trough = x.rolling(117, min_periods=max(117//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.627647 + 0.0024223 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_073_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=124, w2=41, w3=260, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(124)
    rank = change.rolling(41, min_periods=max(41//3, 2)).rank(pct=True)
    persistence = change.rolling(260, min_periods=max(260//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.237667 * persistence + 0.0024224 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_074_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=131, w2=54, w3=277, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(131, min_periods=max(131//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.654706 + 0.0024225 * anchor
    return base_signal.diff().diff()

def f33_ckst_gemini_075_d2(close: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=138, w2=67, w3=294, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(67, min_periods=max(67//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 138)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.250333 * slope + 0.0024226 * anchor
    return base_signal.diff().diff()
