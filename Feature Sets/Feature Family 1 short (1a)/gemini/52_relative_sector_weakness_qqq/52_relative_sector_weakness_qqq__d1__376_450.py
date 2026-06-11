"""52 relative sector weakness qqq d1 first derivative features 376-450 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Relative_Strength - Institutional-grade short-side signal.
Version: 3.0 (Strict De-duplication)
PIT-clean: right-anchored rolling, explicit min_periods.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

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

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if not valid.all():
            x = x[valid]; w = w[valid]
        xm, wm = x.mean(), w.mean()
        num = ((x - xm) * (w - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f52_rsw_q_376_rel_v376_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=90, w2=337, w3=439, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 90)
    baseline = trend.rolling(337, min_periods=max(337//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(439, min_periods=max(439//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.05125 + 0.0032177 * anchor
    return base_signal.diff()

def f52_rsw_q_377_rel_v377_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=97, w2=348, w3=452, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 97)
    slow = _rolling_slope(x, 348)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.065625 + 0.0032178 * anchor
    return base_signal.diff()

def f52_rsw_q_378_rel_v378_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=104, w2=359, w3=465, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(359, min_periods=max(359//3, 2)).max()
    trough = x.rolling(104, min_periods=max(104//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.08 + 0.0032179 * anchor
    return base_signal.diff()

def f52_rsw_q_379_rel_v379_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=111, w2=370, w3=478, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(111)
    rank = change.rolling(370, min_periods=max(370//3, 2)).rank(pct=True)
    persistence = change.rolling(478, min_periods=max(478//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3118 * persistence + 0.003218 * anchor
    return base_signal.diff()

def f52_rsw_q_380_rel_v380_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=118, w2=381, w3=491, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(118, min_periods=max(118//3, 2)).std()
    vol_slow = ret.rolling(381, min_periods=max(381//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.10875 + 0.0032181 * anchor
    return base_signal.diff()

def f52_rsw_q_381_rel_v381_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=125, w2=392, w3=504, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(392, min_periods=max(392//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 125)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.327 * slope + 0.0032182 * anchor
    return base_signal.diff()

def f52_rsw_q_382_rel_v382_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=132, w2=403, w3=517, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(403, min_periods=max(403//3, 2)).mean()
    noise = impulse.abs().rolling(517, min_periods=max(517//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.1375 + 0.0032183 * anchor
    return base_signal.diff()

def f52_rsw_q_383_rel_v383_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=139, w2=414, w3=530, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 139)
    acceleration = _rolling_slope(velocity, 414)
    curvature = _rolling_slope(acceleration, 530)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3422 * acceleration + 0.0032184 * anchor
    return base_signal.diff()

def f52_rsw_q_384_rel_v384_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=146, w2=425, w3=543, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 146)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3498 * pressure.rolling(543, min_periods=max(543//3, 2)).mean() + 0.0032185 * anchor
    return base_signal.diff()

def f52_rsw_q_385_rel_v385_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=153, w2=436, w3=556, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(153, min_periods=max(153//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.180625 + 0.0032186 * anchor
    return base_signal.diff()

def f52_rsw_q_386_rel_v386_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=160, w2=447, w3=569, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(447, min_periods=max(447//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 160)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.195 + 0.0032187 * anchor
    return base_signal.diff()

def f52_rsw_q_387_rel_v387_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=167, w2=458, w3=582, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(167, min_periods=max(167//3, 2)).mean(), b.abs().rolling(458, min_periods=max(458//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.3726 * _rolling_slope(cover, 167) + 0.0032188 * anchor
    return base_signal.diff()

def f52_rsw_q_388_rel_v388_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=174, w2=469, w3=595, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3802 * y + 0.619800 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 174) - _rolling_slope(basket, 469) + 0.0032189 * anchor
    return base_signal.diff()

def f52_rsw_q_389_rel_v389_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=181, w2=480, w3=608, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(480, min_periods=max(480//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.238125 + 0.003219 * anchor
    return base_signal.diff()

def f52_rsw_q_390_rel_v390_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=188, w2=491, w3=621, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(491, min_periods=max(491//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3954 * _rolling_slope(draw, 621) + 0.0032191 * anchor
    return base_signal.diff()

def f52_rsw_q_391_rel_v391_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=195, w2=502, w3=634, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.266875 + 0.0032192 * anchor
    return base_signal.diff()

def f52_rsw_q_392_rel_v392_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=202, w2=10, w3=647, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 202)
    baseline = trend.rolling(10, min_periods=max(10//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(647, min_periods=max(647//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28125 + 0.0032193 * anchor
    return base_signal.diff()

def f52_rsw_q_393_rel_v393_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=209, w2=21, w3=660, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 209)
    slow = _rolling_slope(x, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.295625 + 0.0032194 * anchor
    return base_signal.diff()

def f52_rsw_q_394_rel_v394_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=216, w2=32, w3=673, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(32, min_periods=max(32//3, 2)).max()
    trough = x.rolling(216, min_periods=max(216//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.31 + 0.0032195 * anchor
    return base_signal.diff()

def f52_rsw_q_395_rel_v395_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=223, w2=43, w3=686, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(43, min_periods=max(43//3, 2)).rank(pct=True)
    persistence = change.rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.057 * persistence + 0.0032196 * anchor
    return base_signal.diff()

def f52_rsw_q_396_rel_v396_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=230, w2=54, w3=699, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(230, min_periods=max(230//3, 2)).std()
    vol_slow = ret.rolling(54, min_periods=max(54//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.33875 + 0.0032197 * anchor
    return base_signal.diff()

def f52_rsw_q_397_rel_v397_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=237, w2=65, w3=712, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(65, min_periods=max(65//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 237)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0722 * slope + 0.0032198 * anchor
    return base_signal.diff()

def f52_rsw_q_398_rel_v398_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=244, w2=76, w3=725, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(76, min_periods=max(76//3, 2)).mean()
    noise = impulse.abs().rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3675 + 0.0032199 * anchor
    return base_signal.diff()

def f52_rsw_q_399_rel_v399_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=251, w2=87, w3=738, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 251)
    acceleration = _rolling_slope(velocity, 87)
    curvature = _rolling_slope(acceleration, 738)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0874 * acceleration + 0.00322 * anchor
    return base_signal.diff()

def f52_rsw_q_400_rel_v400_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=7, w2=98, w3=751, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 7)
    pressure = rel_log.diff(98)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.095 * pressure.rolling(751, min_periods=max(751//3, 2)).mean() + 0.0032201 * anchor
    return base_signal.diff()

def f52_rsw_q_401_rel_v401_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=14, w2=109, w3=764, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(14, min_periods=max(14//3, 2)).mean())
    decay = spread.ewm(span=109, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.410625 + 0.0032202 * anchor
    return base_signal.diff()

def f52_rsw_q_402_rel_v402_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=21, w2=120, w3=20, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(120, min_periods=max(120//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 21)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.425 + 0.0032203 * anchor
    return base_signal.diff()

def f52_rsw_q_403_rel_v403_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=28, w2=131, w3=33, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(28, min_periods=max(28//3, 2)).mean(), b.abs().rolling(131, min_periods=max(131//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(33) + 0.1178 * _rolling_slope(cover, 28) + 0.0032204 * anchor
    return base_signal.diff()

def f52_rsw_q_404_rel_v404_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=35, w2=142, w3=46, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.1254 * y + 0.874600 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 35) - _rolling_slope(basket, 142) + 0.0032205 * anchor
    return base_signal.diff()

def f52_rsw_q_405_rel_v405_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=42, w2=153, w3=59, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(42, min_periods=max(42//3, 2)).mean(), upside.rolling(153, min_periods=max(153//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(59) * 1.468125 + 0.0032206 * anchor
    return base_signal.diff()

def f52_rsw_q_406_rel_v406_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=49, w2=164, w3=72, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(164, min_periods=max(164//3, 2)).max()
    rebound = x - x.rolling(49, min_periods=max(49//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1406 * _rolling_slope(draw, 72) + 0.0032207 * anchor
    return base_signal.diff()

def f52_rsw_q_407_rel_v407_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=56, w2=175, w3=85, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(56) - b.diff(126)
    stress = imbalance.rolling(85, min_periods=max(85//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.496875 + 0.0032208 * anchor
    return base_signal.diff()

def f52_rsw_q_408_rel_v408_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=63, w2=186, w3=98, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 63)
    baseline = trend.rolling(186, min_periods=max(186//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.51125 + 0.0032209 * anchor
    return base_signal.diff()

def f52_rsw_q_409_rel_v409_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=70, w2=197, w3=111, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 70)
    slow = _rolling_slope(x, 197)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=111, adjust=False).mean() * 1.525625 + 0.003221 * anchor
    return base_signal.diff()

def f52_rsw_q_410_rel_v410_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=77, w2=208, w3=124, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(208, min_periods=max(208//3, 2)).max()
    trough = x.rolling(77, min_periods=max(77//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.54 + 0.0032211 * anchor
    return base_signal.diff()

def f52_rsw_q_411_rel_v411_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=84, w2=219, w3=137, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(84)
    rank = change.rolling(219, min_periods=max(219//3, 2)).rank(pct=True)
    persistence = change.rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1786 * persistence + 0.0032212 * anchor
    return base_signal.diff()

def f52_rsw_q_412_rel_v412_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=91, w2=230, w3=150, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(91, min_periods=max(91//3, 2)).std()
    vol_slow = ret.rolling(230, min_periods=max(230//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.56875 + 0.0032213 * anchor
    return base_signal.diff()

def f52_rsw_q_413_rel_v413_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=98, w2=241, w3=163, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(241, min_periods=max(241//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 98)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1938 * slope + 0.0032214 * anchor
    return base_signal.diff()

def f52_rsw_q_414_rel_v414_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=105, w2=252, w3=176, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(105)
    drag = impulse.rolling(252, min_periods=max(252//3, 2)).mean()
    noise = impulse.abs().rolling(176, min_periods=max(176//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.5975 + 0.0032215 * anchor
    return base_signal.diff()

def f52_rsw_q_415_rel_v415_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=112, w2=263, w3=189, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 112)
    acceleration = _rolling_slope(velocity, 263)
    curvature = _rolling_slope(acceleration, 189)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.209 * acceleration + 0.0032216 * anchor
    return base_signal.diff()

def f52_rsw_q_416_rel_v416_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=119, w2=274, w3=202, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 119)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.2166 * pressure.rolling(202, min_periods=max(202//3, 2)).mean() + 0.0032217 * anchor
    return base_signal.diff()

def f52_rsw_q_417_rel_v417_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=126, w2=285, w3=215, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(126, min_periods=max(126//3, 2)).mean())
    decay = spread.ewm(span=285, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 0.8675 + 0.0032218 * anchor
    return base_signal.diff()

def f52_rsw_q_418_rel_v418_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=133, w2=296, w3=228, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(296, min_periods=max(296//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 133)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 0.881875 + 0.0032219 * anchor
    return base_signal.diff()

def f52_rsw_q_419_rel_v419_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=140, w2=307, w3=241, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(140, min_periods=max(140//3, 2)).mean(), b.abs().rolling(307, min_periods=max(307//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2394 * _rolling_slope(cover, 140) + 0.003222 * anchor
    return base_signal.diff()

def f52_rsw_q_420_rel_v420_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=147, w2=318, w3=254, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.247 * y + 0.753000 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 147) - _rolling_slope(basket, 318) + 0.0032221 * anchor
    return base_signal.diff()

def f52_rsw_q_421_rel_v421_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=154, w2=329, w3=267, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(154, min_periods=max(154//3, 2)).mean(), upside.rolling(329, min_periods=max(329//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.925 + 0.0032222 * anchor
    return base_signal.diff()

def f52_rsw_q_422_rel_v422_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=161, w2=340, w3=280, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(340, min_periods=max(340//3, 2)).max()
    rebound = x - x.rolling(161, min_periods=max(161//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2622 * _rolling_slope(draw, 280) + 0.0032223 * anchor
    return base_signal.diff()

def f52_rsw_q_423_rel_v423_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=168, w2=351, w3=293, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.95375 + 0.0032224 * anchor
    return base_signal.diff()

def f52_rsw_q_424_rel_v424_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=175, w2=362, w3=306, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(362, min_periods=max(362//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(306, min_periods=max(306//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.968125 + 0.0032225 * anchor
    return base_signal.diff()

def f52_rsw_q_425_rel_v425_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=182, w2=373, w3=319, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 373)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.9825 + 0.0032226 * anchor
    return base_signal.diff()

def f52_rsw_q_426_rel_v426_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=189, w2=384, w3=332, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(384, min_periods=max(384//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.996875 + 0.0032227 * anchor
    return base_signal.diff()

def f52_rsw_q_427_rel_v427_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=196, w2=395, w3=345, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(395, min_periods=max(395//3, 2)).rank(pct=True)
    persistence = change.rolling(345, min_periods=max(345//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3002 * persistence + 0.0032228 * anchor
    return base_signal.diff()

def f52_rsw_q_428_rel_v428_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=203, w2=406, w3=358, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(406, min_periods=max(406//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.025625 + 0.0032229 * anchor
    return base_signal.diff()

def f52_rsw_q_429_rel_v429_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=210, w2=417, w3=371, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(417, min_periods=max(417//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3154 * slope + 0.003223 * anchor
    return base_signal.diff()

def f52_rsw_q_430_rel_v430_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=217, w2=428, w3=384, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(428, min_periods=max(428//3, 2)).mean()
    noise = impulse.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.054375 + 0.0032231 * anchor
    return base_signal.diff()

def f52_rsw_q_431_rel_v431_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=224, w2=439, w3=397, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 439)
    curvature = _rolling_slope(acceleration, 397)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3306 * acceleration + 0.0032232 * anchor
    return base_signal.diff()

def f52_rsw_q_432_rel_v432_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=231, w2=450, w3=410, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 231)
    pressure = rel_log.diff(126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.3382 * pressure.rolling(410, min_periods=max(410//3, 2)).mean() + 0.0032233 * anchor
    return base_signal.diff()

def f52_rsw_q_433_rel_v433_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=238, w2=461, w3=423, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(238, min_periods=max(238//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.0975 + 0.0032234 * anchor
    return base_signal.diff()

def f52_rsw_q_434_rel_v434_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=245, w2=472, w3=436, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(472, min_periods=max(472//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 245)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.111875 + 0.0032235 * anchor
    return base_signal.diff()

def f52_rsw_q_435_rel_v435_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=252, w2=483, w3=449, lag=5)."""
    a = close.shift(5)
    b = sector_close.shift(5)
    cover = _safe_div(a.rolling(252, min_periods=max(252//3, 2)).mean(), b.abs().rolling(483, min_periods=max(483//3, 2)).mean())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.361 * _rolling_slope(cover, 252) + 0.0032236 * anchor
    return base_signal.diff()

def f52_rsw_q_436_rel_v436_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=8, w2=494, w3=462, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    y = _safe_log(sector_close.abs() + 1.0).shift(10)
    z = _safe_log(sector_close.abs() + 1.0).shift(10)
    basket = x - 0.3686 * y + 0.631400 * z
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _rolling_slope(basket, 8) - _rolling_slope(basket, 494) + 0.0032237 * anchor
    return base_signal.diff()

def f52_rsw_q_437_rel_v437_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=15, w2=505, w3=475, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(15, min_periods=max(15//3, 2)).mean(), upside.rolling(505, min_periods=max(505//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.155 + 0.0032238 * anchor
    return base_signal.diff()

def f52_rsw_q_438_rel_v438_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=22, w2=13, w3=488, lag=42)."""
    x = _safe_log(close.abs() + 1.0).shift(42)
    draw = x - x.rolling(13, min_periods=max(13//3, 2)).max()
    rebound = x - x.rolling(22, min_periods=max(22//3, 2)).min()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3838 * _rolling_slope(draw, 488) + 0.0032239 * anchor
    return base_signal.diff()

def f52_rsw_q_439_rel_v439_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=29, w2=24, w3=501, lag=63)."""
    a = _safe_log(close.abs() + 1.0).shift(63)
    b = _safe_log(sector_close.abs() + 1.0).shift(63)
    imbalance = a.diff(29) - b.diff(24)
    stress = imbalance.rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.18375 + 0.003224 * anchor
    return base_signal.diff()

def f52_rsw_q_440_rel_v440_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=36, w2=35, w3=514, lag=0)."""
    x = _safe_log(close.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(35, min_periods=max(35//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.198125 + 0.0032241 * anchor
    return base_signal.diff()

def f52_rsw_q_441_rel_v441_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=43, w2=46, w3=527, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 46)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2125 + 0.0032242 * anchor
    return base_signal.diff()

def f52_rsw_q_442_rel_v442_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=50, w2=57, w3=540, lag=2)."""
    x = close.shift(2)
    peak = x.rolling(57, min_periods=max(57//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.226875 + 0.0032243 * anchor
    return base_signal.diff()

def f52_rsw_q_443_rel_v443_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=57, w2=68, w3=553, lag=5)."""
    x = close.shift(5)
    change = x.pct_change(57)
    rank = change.rolling(68, min_periods=max(68//3, 2)).rank(pct=True)
    persistence = change.rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0454 * persistence + 0.0032244 * anchor
    return base_signal.diff()

def f52_rsw_q_444_rel_v444_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=64, w2=79, w3=566, lag=10)."""
    x = _safe_log(close.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(79, min_periods=max(79//3, 2)).std()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.255625 + 0.0032245 * anchor
    return base_signal.diff()

def f52_rsw_q_445_rel_v445_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=71, w2=90, w3=579, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(90, min_periods=max(90//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0606 * slope + 0.0032246 * anchor
    return base_signal.diff()

def f52_rsw_q_446_rel_v446_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=78, w2=101, w3=592, lag=42)."""
    x = close.shift(42)
    impulse = x.diff(78)
    drag = impulse.rolling(101, min_periods=max(101//3, 2)).mean()
    noise = impulse.abs().rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.284375 + 0.0032247 * anchor
    return base_signal.diff()

def f52_rsw_q_447_rel_v447_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=85, w2=112, w3=605, lag=63)."""
    x = _safe_log(close.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 112)
    curvature = _rolling_slope(acceleration, 605)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0758 * acceleration + 0.0032248 * anchor
    return base_signal.diff()

def f52_rsw_q_448_rel_v448_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=92, w2=123, w3=618, lag=0)."""
    rel = _safe_div(close.shift(0), sector_close.shift(0).abs() + 1e-12)
    rel_log = _safe_log(rel.abs() + 1.0)
    trend = _rolling_slope(rel_log, 92)
    pressure = rel_log.diff(123)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = trend + 0.0834 * pressure.rolling(618, min_periods=max(618//3, 2)).mean() + 0.0032249 * anchor
    return base_signal.diff()

def f52_rsw_q_449_rel_v449_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=99, w2=134, w3=631, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(99, min_periods=max(99//3, 2)).mean())
    decay = spread.ewm(span=134, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.3275 + 0.003225 * anchor
    return base_signal.diff()

def f52_rsw_q_450_rel_v450_d1(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """First derivative of de-duplicated rel replacement signal (w1=106, w2=145, w3=644, lag=2)."""
    a = _safe_log(close.abs() + 1.0).shift(2)
    b = _safe_log(sector_close.abs() + 1.0).shift(2)
    corr = a.rolling(145, min_periods=max(145//3, 3)).corr(b)
    slope = _rolling_slope(a - b, 106)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = slope * (1.0 - corr) * 1.341875 + 0.0032251 * anchor
    return base_signal.diff()
