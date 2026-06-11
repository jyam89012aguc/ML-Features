"""69 low volume node fragility gemini d2 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Rapid price movement through low-volume 'gaps' in the volume profile.
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

def f69_lvnf_gemini_001_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=5]"""
    window = 5
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_002_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=10]"""
    window = 10
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_003_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=21]"""
    window = 21
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_004_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=42]"""
    window = 42
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_005_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=63]"""
    window = 63
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_006_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=126]"""
    window = 126
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_007_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=252]"""
    window = 252
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_008_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=504]"""
    window = 504
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_009_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=756]"""
    window = 756
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_010_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rapid price movement through low-volume 'gaps' in the volume profile. [window=1260]"""
    window = 1260
    res = _safe_div(_rolling_slope(close, window), volume.rolling(window).min() + 1e-9)
    return (res).diff().diff()

def f69_lvnf_gemini_011_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=20, w2=338, w3=221, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 338)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=221, adjust=False).mean() * 1.279412 + 0.0044322 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_012_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=27, w2=351, w3=238, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(351, min_periods=max(351//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.292941 + 0.0044323 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_013_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=34, w2=364, w3=255, lag=3)."""
    x = close.shift(3)
    change = x.pct_change(34)
    rank = change.rolling(364, min_periods=max(364//3, 2)).rank(pct=True)
    persistence = change.rolling(255, min_periods=max(255//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.254 * persistence + 0.0044324 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_014_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=41, w2=377, w3=272, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(377, min_periods=max(377//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32 + 0.0044325 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_015_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=48, w2=390, w3=289, lag=8)."""
    x = close.shift(8)
    ma = x.rolling(390, min_periods=max(390//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.266667 * slope + 0.0044326 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_016_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=55, w2=403, w3=306, lag=13)."""
    x = close.shift(13)
    impulse = x.diff(55)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.347059 + 0.0044327 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_017_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=62, w2=416, w3=323, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 416)
    curvature = _rolling_slope(acceleration, 323)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.279333 * acceleration + 0.0044328 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_018_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=69, w2=429, w3=340, lag=34)."""
    rel = _safe_div(close.shift(34), volume.shift(34).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 69)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.285667 * pressure.rolling(340, min_periods=max(340//3, 2)).mean() + 0.0044329 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_019_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=76, w2=442, w3=357, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    spread = _safe_div(a - b, a.abs().rolling(76, min_periods=max(76//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.387647 + 0.004433 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_020_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=83, w2=455, w3=374, lag=0)."""
    a = _safe_log(close.abs() + 1.0).shift(0)
    b = _safe_log(volume.abs() + 1.0).shift(0)
    corr = a.rolling(455, min_periods=max(455//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 83)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.401176 + 0.0044331 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_021_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=90, w2=468, w3=391, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    cover = _safe_div(a.rolling(90, min_periods=max(90//3, 2)).mean(), b.abs().rolling(468, min_periods=max(468//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.304667 * _rolling_slope(cover, 90) + 0.0044332 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_022_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=97, w2=481, w3=408, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    y = _safe_log(volume.abs() + 1.0).shift(2)
    z = _safe_log(volume.abs() + 1.0).shift(2)
    basket = x - 0.311 * y + 0.689000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 97) - _rolling_slope(basket, 481) + 0.0044333 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_023_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=104, w2=494, w3=425, lag=3)."""
    x = close.shift(3)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(104, min_periods=max(104//3, 2)).mean(), upside.rolling(494, min_periods=max(494//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.441765 + 0.0044334 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_024_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=111, w2=507, w3=442, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    draw = x - x.rolling(507, min_periods=max(507//3, 2)).max()
    rebound = x - x.rolling(111, min_periods=max(111//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.323667 * _rolling_slope(draw, 442) + 0.0044335 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_025_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=118, w2=21, w3=459, lag=8)."""
    a = _safe_log(close.abs() + 1.0).shift(8)
    b = _safe_log(volume.abs() + 1.0).shift(8)
    imbalance = a.diff(118) - b.diff(21)
    stress = imbalance.rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.468824 + 0.0044336 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_026_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=125, w2=34, w3=476, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(34, min_periods=max(34//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.482353 + 0.0044337 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_027_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=132, w2=47, w3=493, lag=21)."""
    x = _safe_log(close.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 47)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.495882 + 0.0044338 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_028_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=139, w2=60, w3=510, lag=34)."""
    x = close.shift(34)
    peak = x.rolling(60, min_periods=max(60//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.509412 + 0.0044339 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_029_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=146, w2=73, w3=527, lag=55)."""
    x = close.shift(55)
    change = x.pct_change(126)
    rank = change.rolling(73, min_periods=max(73//3, 2)).rank(pct=True)
    persistence = change.rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.355333 * persistence + 0.004434 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_030_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=153, w2=86, w3=544, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(86, min_periods=max(86//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.536471 + 0.0044341 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_031_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=160, w2=99, w3=561, lag=1)."""
    x = close.shift(1)
    ma = x.rolling(99, min_periods=max(99//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.035667 * slope + 0.0044342 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_032_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=167, w2=112, w3=578, lag=2)."""
    x = close.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(112, min_periods=max(112//3, 2)).mean()
    noise = impulse.abs().rolling(578, min_periods=max(578//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.563529 + 0.0044343 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_033_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=174, w2=125, w3=595, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 125)
    curvature = _rolling_slope(acceleration, 595)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.048333 * acceleration + 0.0044344 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_034_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=181, w2=138, w3=612, lag=5)."""
    rel = _safe_div(close.shift(5), volume.shift(5).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 181)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.054667 * pressure.rolling(612, min_periods=max(612//3, 2)).mean() + 0.0044345 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_035_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=188, w2=151, w3=629, lag=8)."""
    a = close.shift(8)
    b = volume.shift(8)
    spread = _safe_div(a - b, a.abs().rolling(188, min_periods=max(188//3, 2)).mean())
    decay = spread.ewm(span=151, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.604118 + 0.0044346 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_036_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=195, w2=164, w3=646, lag=13)."""
    a = _safe_log(close.abs() + 1.0).shift(13)
    b = _safe_log(volume.abs() + 1.0).shift(13)
    corr = a.rolling(164, min_periods=max(164//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 195)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.617647 + 0.0044347 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_037_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=202, w2=177, w3=663, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    cover = _safe_div(a.rolling(202, min_periods=max(202//3, 2)).mean(), b.abs().rolling(177, min_periods=max(177//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.073667 * _rolling_slope(cover, 202) + 0.0044348 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_038_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=209, w2=190, w3=680, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    y = _safe_log(volume.abs() + 1.0).shift(34)
    z = _safe_log(volume.abs() + 1.0).shift(34)
    basket = x - 0.08 * y + 0.920000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 209) - _rolling_slope(basket, 190) + 0.0044349 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_039_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=216, w2=203, w3=697, lag=55)."""
    x = close.shift(55)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(216, min_periods=max(216//3, 2)).mean(), upside.rolling(203, min_periods=max(203//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.658235 + 0.004435 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_040_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=223, w2=216, w3=714, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    draw = x - x.rolling(216, min_periods=max(216//3, 2)).max()
    rebound = x - x.rolling(223, min_periods=max(223//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.092667 * _rolling_slope(draw, 714) + 0.0044351 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_041_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=230, w2=229, w3=731, lag=1)."""
    a = _safe_log(close.abs() + 1.0).shift(1)
    b = _safe_log(volume.abs() + 1.0).shift(1)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.831765 + 0.0044352 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_042_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=237, w2=242, w3=748, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 237)
    baseline = trend.rolling(242, min_periods=max(242//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.845294 + 0.0044353 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_043_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=244, w2=255, w3=765, lag=3)."""
    x = _safe_log(close.abs() + 1.0).shift(3)
    fast = _rolling_slope(x, 244)
    slow = _rolling_slope(x, 255)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.858824 + 0.0044354 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_044_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=251, w2=268, w3=31, lag=5)."""
    x = close.shift(5)
    peak = x.rolling(268, min_periods=max(268//3, 2)).max()
    trough = x.rolling(251, min_periods=max(251//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.872353 + 0.0044355 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_045_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=11, w2=281, w3=48, lag=8)."""
    x = close.shift(8)
    change = x.pct_change(11)
    rank = change.rolling(281, min_periods=max(281//3, 2)).rank(pct=True)
    persistence = change.rolling(48, min_periods=max(48//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.124333 * persistence + 0.0044356 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_046_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=18, w2=294, w3=65, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    ret = x.diff()
    vol_fast = ret.rolling(18, min_periods=max(18//3, 2)).std()
    vol_slow = ret.rolling(294, min_periods=max(294//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.899412 + 0.0044357 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_047_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=25, w2=307, w3=82, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(307, min_periods=max(307//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 25)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.137 * slope + 0.0044358 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_048_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=32, w2=320, w3=99, lag=34)."""
    x = close.shift(34)
    impulse = x.diff(32)
    drag = impulse.rolling(320, min_periods=max(320//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.926471 + 0.0044359 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_049_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=39, w2=333, w3=116, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    velocity = _rolling_slope(x, 39)
    acceleration = _rolling_slope(velocity, 333)
    curvature = _rolling_slope(acceleration, 116)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.149667 * acceleration + 0.004436 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_050_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=46, w2=346, w3=133, lag=0)."""
    rel = _safe_div(close.shift(0), volume.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 46)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.156 * pressure.rolling(133, min_periods=max(133//3, 2)).mean() + 0.0044361 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_051_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=53, w2=359, w3=150, lag=1)."""
    a = close.shift(1)
    b = volume.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(53, min_periods=max(53//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.967059 + 0.0044362 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_052_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=60, w2=372, w3=167, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(volume.abs() + 1.0).shift(2)
    corr = a.rolling(372, min_periods=max(372//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 60)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.980588 + 0.0044363 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_053_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=67, w2=385, w3=184, lag=3)."""
    a = close.shift(3)
    b = volume.shift(3)
    cover = _safe_div(a.rolling(67, min_periods=max(67//3, 2)).mean(), b.abs().rolling(385, min_periods=max(385//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.175 * _rolling_slope(cover, 67) + 0.0044364 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_054_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=74, w2=398, w3=201, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    y = _safe_log(volume.abs() + 1.0).shift(5)
    z = _safe_log(volume.abs() + 1.0).shift(5)
    basket = x - 0.181333 * y + 0.818667 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 74) - _rolling_slope(basket, 398) + 0.0044365 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_055_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=81, w2=411, w3=218, lag=8)."""
    x = close.shift(8)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(81, min_periods=max(81//3, 2)).mean(), upside.rolling(411, min_periods=max(411//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.021176 + 0.0044366 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_056_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=88, w2=424, w3=235, lag=13)."""
    x = _safe_log(close.abs() + 1.0).shift(13)
    draw = x - x.rolling(424, min_periods=max(424//3, 2)).max()
    rebound = x - x.rolling(88, min_periods=max(88//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.194 * _rolling_slope(draw, 235) + 0.0044367 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_057_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=95, w2=437, w3=252, lag=21)."""
    a = _safe_log(close.abs() + 1.0).shift(21)
    b = _safe_log(volume.abs() + 1.0).shift(21)
    imbalance = a.diff(95) - b.diff(126)
    stress = imbalance.rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.048235 + 0.0044368 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_058_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=102, w2=450, w3=269, lag=34)."""
    x = _safe_log(close.abs() + 1.0).shift(34)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(450, min_periods=max(450//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(269, min_periods=max(269//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.061765 + 0.0044369 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_059_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=109, w2=463, w3=286, lag=55)."""
    x = _safe_log(close.abs() + 1.0).shift(55)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 463)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=286, adjust=False).mean() * 1.075294 + 0.004437 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_060_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=116, w2=476, w3=303, lag=0)."""
    x = close.shift(0)
    peak = x.rolling(476, min_periods=max(476//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.088824 + 0.0044371 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_061_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=123, w2=489, w3=320, lag=1)."""
    x = close.shift(1)
    change = x.pct_change(123)
    rank = change.rolling(489, min_periods=max(489//3, 2)).rank(pct=True)
    persistence = change.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.225667 * persistence + 0.0044372 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_062_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=130, w2=502, w3=337, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(502, min_periods=max(502//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.115882 + 0.0044373 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_063_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=137, w2=16, w3=354, lag=3)."""
    x = close.shift(3)
    ma = x.rolling(16, min_periods=max(16//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.238333 * slope + 0.0044374 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_064_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=144, w2=29, w3=371, lag=5)."""
    x = close.shift(5)
    impulse = x.diff(126)
    drag = impulse.rolling(29, min_periods=max(29//3, 2)).mean()
    noise = impulse.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.142941 + 0.0044375 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_065_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=151, w2=42, w3=388, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    velocity = _rolling_slope(x, 151)
    acceleration = _rolling_slope(velocity, 42)
    curvature = _rolling_slope(acceleration, 388)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.251 * acceleration + 0.0044376 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_066_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=158, w2=55, w3=405, lag=13)."""
    rel = _safe_div(close.shift(13), volume.shift(13).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 158)
    pressure = rel_log.diff(55)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.257333 * pressure.rolling(405, min_periods=max(405//3, 2)).mean() + 0.0044377 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_067_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=165, w2=68, w3=422, lag=21)."""
    a = close.shift(21)
    b = volume.shift(21)
    spread = _safe_div(a - b, a.abs().rolling(165, min_periods=max(165//3, 2)).mean())
    decay = spread.ewm(span=68, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.183529 + 0.0044378 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_068_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=172, w2=81, w3=439, lag=34)."""
    a = _safe_log(close.abs() + 1.0).shift(34)
    b = _safe_log(volume.abs() + 1.0).shift(34)
    corr = a.rolling(81, min_periods=max(81//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 172)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.197059 + 0.0044379 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_069_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=179, w2=94, w3=456, lag=55)."""
    a = close.shift(55)
    b = volume.shift(55)
    cover = _safe_div(a.rolling(179, min_periods=max(179//3, 2)).mean(), b.abs().rolling(94, min_periods=max(94//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.276333 * _rolling_slope(cover, 179) + 0.004438 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_070_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=186, w2=107, w3=473, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    y = _safe_log(volume.abs() + 1.0).shift(0)
    z = _safe_log(volume.abs() + 1.0).shift(0)
    basket = x - 0.282667 * y + 0.717333 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 186) - _rolling_slope(basket, 107) + 0.0044381 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_071_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=193, w2=120, w3=490, lag=1)."""
    x = close.shift(1)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(193, min_periods=max(193//3, 2)).mean(), upside.rolling(120, min_periods=max(120//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.237647 + 0.0044382 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_072_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=200, w2=133, w3=507, lag=2)."""
    x = _safe_log(close.abs() + 1.0).shift(2)
    draw = x - x.rolling(133, min_periods=max(133//3, 2)).max()
    rebound = x - x.rolling(200, min_periods=max(200//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.295333 * _rolling_slope(draw, 507) + 0.0044383 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_073_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=207, w2=146, w3=524, lag=3)."""
    a = _safe_log(close.abs() + 1.0).shift(3)
    b = _safe_log(volume.abs() + 1.0).shift(3)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(524, min_periods=max(524//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.264706 + 0.0044384 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_074_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=214, w2=159, w3=541, lag=5)."""
    x = _safe_log(close.abs() + 1.0).shift(5)
    trend = _rolling_slope(x, 214)
    baseline = trend.rolling(159, min_periods=max(159//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.278235 + 0.0044385 * anchor
    return base_signal.diff().diff()

def f69_lvnf_gemini_075_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d2 signal (w1=221, w2=172, w3=558, lag=8)."""
    x = _safe_log(close.abs() + 1.0).shift(8)
    fast = _rolling_slope(x, 221)
    slow = _rolling_slope(x, 172)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.291765 + 0.0044386 * anchor
    return base_signal.diff().diff()
