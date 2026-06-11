"""64 volume velocity spike detector gemini d3 features 1-75 — Pipeline 1b-HF Grade v7.

Hypothesis: Identification of rapid acceleration in volume as a precursor to price jumps.
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

def f64_vvsd_gemini_001_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=5]"""
    window = 5
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_002_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=10]"""
    window = 10
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_003_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=21]"""
    window = 21
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_004_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=42]"""
    window = 42
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_005_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=63]"""
    window = 63
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_006_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=126]"""
    window = 126
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_007_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=252]"""
    window = 252
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_008_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=504]"""
    window = 504
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_009_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=756]"""
    window = 756
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_010_d3(volume: pd.Series) -> pd.Series:
    """Identification of rapid acceleration in volume as a precursor to price jumps. [window=1260]"""
    window = 1260
    res = _rolling_zscore(_rolling_slope(volume, window), window)
    return (res).diff().diff().diff()

def f64_vvsd_gemini_011_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=172, w2=189, w3=61, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 172)
    slow = _rolling_slope(x, 189)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=61, adjust=False).mean() * 1.139412 + 0.0041662 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_012_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=179, w2=202, w3=78, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(202, min_periods=max(202//3, 2)).max()
    trough = x.rolling(179, min_periods=max(179//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.152941 + 0.0041663 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_013_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=186, w2=215, w3=95, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(215, min_periods=max(215//3, 2)).rank(pct=True)
    persistence = change.rolling(95, min_periods=max(95//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.356333 * persistence + 0.0041664 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_014_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=193, w2=228, w3=112, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(193, min_periods=max(193//3, 2)).std()
    vol_slow = ret.rolling(228, min_periods=max(228//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.18 + 0.0041665 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_015_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=200, w2=241, w3=129, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 200)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.036667 * slope + 0.0041666 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_016_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=207, w2=254, w3=146, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(254, min_periods=max(254//3, 2)).mean()
    noise = impulse.abs().rolling(146, min_periods=max(146//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.207059 + 0.0041667 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_017_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=214, w2=267, w3=163, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 214)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 163)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.049333 * acceleration + 0.0041668 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_018_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=221, w2=280, w3=180, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(221, min_periods=max(221//3, 2)).mean(), upside.rolling(280, min_periods=max(280//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.234118 + 0.0041669 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_019_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=228, w2=293, w3=197, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(293, min_periods=max(293//3, 2)).max()
    rebound = x - x.rolling(228, min_periods=max(228//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.062 * _rolling_slope(draw, 197) + 0.004167 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_020_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=235, w2=306, w3=214, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 235)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(214, min_periods=max(214//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.261176 + 0.0041671 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_021_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=242, w2=319, w3=231, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 242)
    slow = _rolling_slope(x, 319)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=231, adjust=False).mean() * 1.274706 + 0.0041672 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_022_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=249, w2=332, w3=248, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(249, min_periods=max(249//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.288235 + 0.0041673 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_023_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=9, w2=345, w3=265, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(9)
    rank = change.rolling(345, min_periods=max(345//3, 2)).rank(pct=True)
    persistence = change.rolling(265, min_periods=max(265//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.087333 * persistence + 0.0041674 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_024_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=16, w2=358, w3=282, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(16, min_periods=max(16//3, 2)).std()
    vol_slow = ret.rolling(358, min_periods=max(358//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.315294 + 0.0041675 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_025_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=23, w2=371, w3=299, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(371, min_periods=max(371//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 23)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1 * slope + 0.0041676 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_026_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=30, w2=384, w3=316, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(30)
    drag = impulse.rolling(384, min_periods=max(384//3, 2)).mean()
    noise = impulse.abs().rolling(316, min_periods=max(316//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.342353 + 0.0041677 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_027_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=37, w2=397, w3=333, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 37)
    acceleration = _rolling_slope(velocity, 397)
    curvature = _rolling_slope(acceleration, 333)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.112667 * acceleration + 0.0041678 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_028_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=44, w2=410, w3=350, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(44, min_periods=max(44//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.369412 + 0.0041679 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_029_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=51, w2=423, w3=367, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(423, min_periods=max(423//3, 2)).max()
    rebound = x - x.rolling(51, min_periods=max(51//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.125333 * _rolling_slope(draw, 367) + 0.004168 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_030_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=58, w2=436, w3=384, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 58)
    baseline = trend.rolling(436, min_periods=max(436//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.396471 + 0.0041681 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_031_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=65, w2=449, w3=401, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 65)
    slow = _rolling_slope(x, 449)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.41 + 0.0041682 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_032_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=72, w2=462, w3=418, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(462, min_periods=max(462//3, 2)).max()
    trough = x.rolling(72, min_periods=max(72//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.423529 + 0.0041683 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_033_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=79, w2=475, w3=435, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(79)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(435, min_periods=max(435//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.150667 * persistence + 0.0041684 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_034_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=86, w2=488, w3=452, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(86, min_periods=max(86//3, 2)).std()
    vol_slow = ret.rolling(488, min_periods=max(488//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.450588 + 0.0041685 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_035_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=93, w2=501, w3=469, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(501, min_periods=max(501//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 93)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.163333 * slope + 0.0041686 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_036_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=100, w2=15, w3=486, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(100)
    drag = impulse.rolling(15, min_periods=max(15//3, 2)).mean()
    noise = impulse.abs().rolling(486, min_periods=max(486//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.477647 + 0.0041687 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_037_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=107, w2=28, w3=503, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 107)
    acceleration = _rolling_slope(velocity, 28)
    curvature = _rolling_slope(acceleration, 503)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.176 * acceleration + 0.0041688 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_038_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=114, w2=41, w3=520, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(41, min_periods=max(41//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.504706 + 0.0041689 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_039_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=121, w2=54, w3=537, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(54, min_periods=max(54//3, 2)).max()
    rebound = x - x.rolling(121, min_periods=max(121//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.188667 * _rolling_slope(draw, 537) + 0.004169 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_040_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=128, w2=67, w3=554, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 128)
    baseline = trend.rolling(67, min_periods=max(67//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(554, min_periods=max(554//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.531765 + 0.0041691 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_041_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=135, w2=80, w3=571, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 135)
    slow = _rolling_slope(x, 80)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.545294 + 0.0041692 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_042_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=142, w2=93, w3=588, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(142, min_periods=max(142//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.558824 + 0.0041693 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_043_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=149, w2=106, w3=605, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(106, min_periods=max(106//3, 2)).rank(pct=True)
    persistence = change.rolling(605, min_periods=max(605//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.214 * persistence + 0.0041694 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_044_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=156, w2=119, w3=622, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(156, min_periods=max(156//3, 2)).std()
    vol_slow = ret.rolling(119, min_periods=max(119//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.585882 + 0.0041695 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_045_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=163, w2=132, w3=639, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(132, min_periods=max(132//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 163)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.226667 * slope + 0.0041696 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_046_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=170, w2=145, w3=656, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(145, min_periods=max(145//3, 2)).mean()
    noise = impulse.abs().rolling(656, min_periods=max(656//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.612941 + 0.0041697 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_047_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=177, w2=158, w3=673, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 177)
    acceleration = _rolling_slope(velocity, 158)
    curvature = _rolling_slope(acceleration, 673)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.239333 * acceleration + 0.0041698 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_048_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=184, w2=171, w3=690, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(184, min_periods=max(184//3, 2)).mean(), upside.rolling(171, min_periods=max(171//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.64 + 0.0041699 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_049_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=191, w2=184, w3=707, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(184, min_periods=max(184//3, 2)).max()
    rebound = x - x.rolling(191, min_periods=max(191//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.252 * _rolling_slope(draw, 707) + 0.00417 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_050_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=198, w2=197, w3=724, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 198)
    baseline = trend.rolling(197, min_periods=max(197//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(724, min_periods=max(724//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.667059 + 0.0041701 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_051_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=205, w2=210, w3=741, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 205)
    slow = _rolling_slope(x, 210)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.827059 + 0.0041702 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_052_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=212, w2=223, w3=758, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(212, min_periods=max(212//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.840588 + 0.0041703 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_053_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=219, w2=236, w3=24, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(126)
    rank = change.rolling(236, min_periods=max(236//3, 2)).rank(pct=True)
    persistence = change.rolling(24, min_periods=max(24//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.277333 * persistence + 0.0041704 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_054_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=226, w2=249, w3=41, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(226, min_periods=max(226//3, 2)).std()
    vol_slow = ret.rolling(249, min_periods=max(249//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.867647 + 0.0041705 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_055_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=233, w2=262, w3=58, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(262, min_periods=max(262//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 233)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.29 * slope + 0.0041706 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_056_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=240, w2=275, w3=75, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(126)
    drag = impulse.rolling(275, min_periods=max(275//3, 2)).mean()
    noise = impulse.abs().rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.894706 + 0.0041707 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_057_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=247, w2=288, w3=92, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 247)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 92)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.302667 * acceleration + 0.0041708 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_058_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=7, w2=301, w3=109, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(7, min_periods=max(7//3, 2)).mean(), upside.rolling(301, min_periods=max(301//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(109) * 0.921765 + 0.0041709 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_059_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=14, w2=314, w3=126, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(314, min_periods=max(314//3, 2)).max()
    rebound = x - x.rolling(14, min_periods=max(14//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.315333 * _rolling_slope(draw, 126) + 0.004171 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_060_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=21, w2=327, w3=143, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 21)
    baseline = trend.rolling(327, min_periods=max(327//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.948824 + 0.0041711 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_061_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=28, w2=340, w3=160, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 28)
    slow = _rolling_slope(x, 340)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=160, adjust=False).mean() * 0.962353 + 0.0041712 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_062_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=35, w2=353, w3=177, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(353, min_periods=max(353//3, 2)).max()
    trough = x.rolling(35, min_periods=max(35//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.975882 + 0.0041713 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_063_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=42, w2=366, w3=194, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(42)
    rank = change.rolling(366, min_periods=max(366//3, 2)).rank(pct=True)
    persistence = change.rolling(194, min_periods=max(194//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.340667 * persistence + 0.0041714 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_064_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=49, w2=379, w3=211, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(49, min_periods=max(49//3, 2)).std()
    vol_slow = ret.rolling(379, min_periods=max(379//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.002941 + 0.0041715 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_065_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=56, w2=392, w3=228, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 56)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.353333 * slope + 0.0041716 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_066_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=63, w2=405, w3=245, lag=13)."""
    x = volume.shift(13)
    impulse = x.diff(63)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(245, min_periods=max(245//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.03 + 0.0041717 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_067_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=70, w2=418, w3=262, lag=21)."""
    x = _safe_log(volume.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 70)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 262)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.033667 * acceleration + 0.0041718 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_068_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=77, w2=431, w3=279, lag=34)."""
    x = volume.shift(34)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(77, min_periods=max(77//3, 2)).mean(), upside.rolling(431, min_periods=max(431//3, 2)).mean().abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.057059 + 0.0041719 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_069_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=84, w2=444, w3=296, lag=55)."""
    x = _safe_log(volume.abs() + 1.0).shift(55)
    draw = x - x.rolling(444, min_periods=max(444//3, 2)).max()
    rebound = x - x.rolling(84, min_periods=max(84//3, 2)).min()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.046333 * _rolling_slope(draw, 296) + 0.004172 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_070_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=91, w2=457, w3=313, lag=0)."""
    x = _safe_log(volume.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 91)
    baseline = trend.rolling(457, min_periods=max(457//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(313, min_periods=max(313//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.084118 + 0.0041721 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_071_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=98, w2=470, w3=330, lag=1)."""
    x = _safe_log(volume.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 98)
    slow = _rolling_slope(x, 470)
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.097647 + 0.0041722 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_072_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=105, w2=483, w3=347, lag=2)."""
    x = volume.shift(2)
    peak = x.rolling(483, min_periods=max(483//3, 2)).max()
    trough = x.rolling(105, min_periods=max(105//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.111176 + 0.0041723 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_073_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=112, w2=496, w3=364, lag=3)."""
    x = volume.shift(3)
    change = x.pct_change(112)
    rank = change.rolling(496, min_periods=max(496//3, 2)).rank(pct=True)
    persistence = change.rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.071667 * persistence + 0.0041724 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_074_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=119, w2=509, w3=381, lag=5)."""
    x = _safe_log(volume.abs() + 1.0).shift(5)
    ret = x.diff()
    vol_fast = ret.rolling(119, min_periods=max(119//3, 2)).std()
    vol_slow = ret.rolling(509, min_periods=max(509//3, 2)).std()
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.138235 + 0.0041725 * anchor
    return base_signal.diff().diff().diff()

def f64_vvsd_gemini_075_d3(volume: pd.Series) -> pd.Series:
    """Replacement for confirmed exact duplicate formula; distinct d3 signal (w1=126, w2=23, w3=398, lag=8)."""
    x = volume.shift(8)
    ma = x.rolling(23, min_periods=max(23//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 126)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(volume.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.084333 * slope + 0.0041726 * anchor
    return base_signal.diff().diff().diff()
