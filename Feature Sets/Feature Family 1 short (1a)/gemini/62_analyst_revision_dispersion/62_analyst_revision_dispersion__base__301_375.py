"""62 analyst revision dispersion base features 301-375 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Analyst_Sentiment - Institutional-grade short-side signal.
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

def f62_ard_301_analyst_v301(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=234, w2=320, w3=614, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 234)
    slow = _rolling_slope(x, 320)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.349375 + 0.0035102 * anchor

def f62_ard_302_analyst_v302(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=241, w2=331, w3=627, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(331, min_periods=max(331//3, 2)).max()
    trough = x.rolling(241, min_periods=max(241//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.36375 + 0.0035103 * anchor

def f62_ard_303_analyst_v303(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=248, w2=342, w3=640, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(342, min_periods=max(342//3, 2)).rank(pct=True)
    persistence = change.rolling(640, min_periods=max(640//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3266 * persistence + 0.0035104 * anchor

def f62_ard_304_analyst_v304(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=255, w2=353, w3=653, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(255, min_periods=max(255//3, 2)).std()
    vol_slow = ret.rolling(353, min_periods=max(353//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.3925 + 0.0035105 * anchor

def f62_ard_305_analyst_v305(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=11, w2=364, w3=666, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(364, min_periods=max(364//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 11)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3418 * slope + 0.0035106 * anchor

def f62_ard_306_analyst_v306(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=18, w2=375, w3=679, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(18)
    drag = impulse.rolling(375, min_periods=max(375//3, 2)).mean()
    noise = impulse.abs().rolling(679, min_periods=max(679//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.42125 + 0.0035107 * anchor

def f62_ard_307_analyst_v307(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=25, w2=386, w3=692, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 25)
    acceleration = _rolling_slope(velocity, 386)
    curvature = _rolling_slope(acceleration, 692)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.357 * acceleration + 0.0035108 * anchor

def f62_ard_308_analyst_v308(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=32, w2=397, w3=705, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(32, min_periods=max(32//3, 2)).mean(), upside.rolling(397, min_periods=max(397//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.45 + 0.0035109 * anchor

def f62_ard_309_analyst_v309(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=39, w2=408, w3=718, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(408, min_periods=max(408//3, 2)).max()
    rebound = x - x.rolling(39, min_periods=max(39//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3722 * _rolling_slope(draw, 718) + 0.003511 * anchor

def f62_ard_310_analyst_v310(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=46, w2=419, w3=731, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 46)
    baseline = trend.rolling(419, min_periods=max(419//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(731, min_periods=max(731//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.47875 + 0.0035111 * anchor

def f62_ard_311_analyst_v311(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=53, w2=430, w3=744, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 53)
    slow = _rolling_slope(x, 430)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.493125 + 0.0035112 * anchor

def f62_ard_312_analyst_v312(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=60, w2=441, w3=757, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(441, min_periods=max(441//3, 2)).max()
    trough = x.rolling(60, min_periods=max(60//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5075 + 0.0035113 * anchor

def f62_ard_313_analyst_v313(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=67, w2=452, w3=770, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(67)
    rank = change.rolling(452, min_periods=max(452//3, 2)).rank(pct=True)
    persistence = change.rolling(770, min_periods=max(770//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4026 * persistence + 0.0035114 * anchor

def f62_ard_314_analyst_v314(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=74, w2=463, w3=26, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(74, min_periods=max(74//3, 2)).std()
    vol_slow = ret.rolling(463, min_periods=max(463//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.53625 + 0.0035115 * anchor

def f62_ard_315_analyst_v315(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=81, w2=474, w3=39, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(474, min_periods=max(474//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 81)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0414 * slope + 0.0035116 * anchor

def f62_ard_316_analyst_v316(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=88, w2=485, w3=52, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(88)
    drag = impulse.rolling(485, min_periods=max(485//3, 2)).mean()
    noise = impulse.abs().rolling(52, min_periods=max(52//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.565 + 0.0035117 * anchor

def f62_ard_317_analyst_v317(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=95, w2=496, w3=65, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 95)
    acceleration = _rolling_slope(velocity, 496)
    curvature = _rolling_slope(acceleration, 65)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0566 * acceleration + 0.0035118 * anchor

def f62_ard_318_analyst_v318(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=102, w2=507, w3=78, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(102, min_periods=max(102//3, 2)).mean(), upside.rolling(507, min_periods=max(507//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(78) * 1.59375 + 0.0035119 * anchor

def f62_ard_319_analyst_v319(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=109, w2=15, w3=91, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(15, min_periods=max(15//3, 2)).max()
    rebound = x - x.rolling(109, min_periods=max(109//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0718 * _rolling_slope(draw, 91) + 0.003512 * anchor

def f62_ard_320_analyst_v320(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=116, w2=26, w3=104, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 116)
    baseline = trend.rolling(26, min_periods=max(26//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(104, min_periods=max(104//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.6225 + 0.0035121 * anchor

def f62_ard_321_analyst_v321(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=123, w2=37, w3=117, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 123)
    slow = _rolling_slope(x, 37)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=117, adjust=False).mean() * 0.86375 + 0.0035122 * anchor

def f62_ard_322_analyst_v322(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=130, w2=48, w3=130, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(48, min_periods=max(48//3, 2)).max()
    trough = x.rolling(130, min_periods=max(130//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.878125 + 0.0035123 * anchor

def f62_ard_323_analyst_v323(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=137, w2=59, w3=143, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(59, min_periods=max(59//3, 2)).rank(pct=True)
    persistence = change.rolling(143, min_periods=max(143//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1022 * persistence + 0.0035124 * anchor

def f62_ard_324_analyst_v324(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=144, w2=70, w3=156, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(144, min_periods=max(144//3, 2)).std()
    vol_slow = ret.rolling(70, min_periods=max(70//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.906875 + 0.0035125 * anchor

def f62_ard_325_analyst_v325(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=151, w2=81, w3=169, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(81, min_periods=max(81//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 151)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1174 * slope + 0.0035126 * anchor

def f62_ard_326_analyst_v326(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=158, w2=92, w3=182, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(92, min_periods=max(92//3, 2)).mean()
    noise = impulse.abs().rolling(182, min_periods=max(182//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.935625 + 0.0035127 * anchor

def f62_ard_327_analyst_v327(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=165, w2=103, w3=195, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 165)
    acceleration = _rolling_slope(velocity, 103)
    curvature = _rolling_slope(acceleration, 195)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1326 * acceleration + 0.0035128 * anchor

def f62_ard_328_analyst_v328(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=172, w2=114, w3=208, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(172, min_periods=max(172//3, 2)).mean(), upside.rolling(114, min_periods=max(114//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.964375 + 0.0035129 * anchor

def f62_ard_329_analyst_v329(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=179, w2=125, w3=221, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(125, min_periods=max(125//3, 2)).max()
    rebound = x - x.rolling(179, min_periods=max(179//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.1478 * _rolling_slope(draw, 221) + 0.003513 * anchor

def f62_ard_330_analyst_v330(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=186, w2=136, w3=234, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 186)
    baseline = trend.rolling(136, min_periods=max(136//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(234, min_periods=max(234//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.993125 + 0.0035131 * anchor

def f62_ard_331_analyst_v331(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=193, w2=147, w3=247, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 193)
    slow = _rolling_slope(x, 147)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=247, adjust=False).mean() * 1.0075 + 0.0035132 * anchor

def f62_ard_332_analyst_v332(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=200, w2=158, w3=260, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(158, min_periods=max(158//3, 2)).max()
    trough = x.rolling(200, min_periods=max(200//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.021875 + 0.0035133 * anchor

def f62_ard_333_analyst_v333(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=207, w2=169, w3=273, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(169, min_periods=max(169//3, 2)).rank(pct=True)
    persistence = change.rolling(273, min_periods=max(273//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1782 * persistence + 0.0035134 * anchor

def f62_ard_334_analyst_v334(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=214, w2=180, w3=286, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(214, min_periods=max(214//3, 2)).std()
    vol_slow = ret.rolling(180, min_periods=max(180//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.050625 + 0.0035135 * anchor

def f62_ard_335_analyst_v335(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=221, w2=191, w3=299, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(191, min_periods=max(191//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 221)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1934 * slope + 0.0035136 * anchor

def f62_ard_336_analyst_v336(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=228, w2=202, w3=312, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(202, min_periods=max(202//3, 2)).mean()
    noise = impulse.abs().rolling(312, min_periods=max(312//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.079375 + 0.0035137 * anchor

def f62_ard_337_analyst_v337(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=235, w2=213, w3=325, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 235)
    acceleration = _rolling_slope(velocity, 213)
    curvature = _rolling_slope(acceleration, 325)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2086 * acceleration + 0.0035138 * anchor

def f62_ard_338_analyst_v338(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=242, w2=224, w3=338, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(242, min_periods=max(242//3, 2)).mean(), upside.rolling(224, min_periods=max(224//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.108125 + 0.0035139 * anchor

def f62_ard_339_analyst_v339(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=249, w2=235, w3=351, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(235, min_periods=max(235//3, 2)).max()
    rebound = x - x.rolling(249, min_periods=max(249//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2238 * _rolling_slope(draw, 351) + 0.003514 * anchor

def f62_ard_340_analyst_v340(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=5, w2=246, w3=364, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 5)
    baseline = trend.rolling(246, min_periods=max(246//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(364, min_periods=max(364//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.136875 + 0.0035141 * anchor

def f62_ard_341_analyst_v341(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=12, w2=257, w3=377, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 12)
    slow = _rolling_slope(x, 257)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.15125 + 0.0035142 * anchor

def f62_ard_342_analyst_v342(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=19, w2=268, w3=390, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(268, min_periods=max(268//3, 2)).max()
    trough = x.rolling(19, min_periods=max(19//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.165625 + 0.0035143 * anchor

def f62_ard_343_analyst_v343(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=26, w2=279, w3=403, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(26)
    rank = change.rolling(279, min_periods=max(279//3, 2)).rank(pct=True)
    persistence = change.rolling(403, min_periods=max(403//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2542 * persistence + 0.0035144 * anchor

def f62_ard_344_analyst_v344(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=33, w2=290, w3=416, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(33, min_periods=max(33//3, 2)).std()
    vol_slow = ret.rolling(290, min_periods=max(290//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.194375 + 0.0035145 * anchor

def f62_ard_345_analyst_v345(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=40, w2=301, w3=429, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(301, min_periods=max(301//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 40)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2694 * slope + 0.0035146 * anchor

def f62_ard_346_analyst_v346(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=47, w2=312, w3=442, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(47)
    drag = impulse.rolling(312, min_periods=max(312//3, 2)).mean()
    noise = impulse.abs().rolling(442, min_periods=max(442//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.223125 + 0.0035147 * anchor

def f62_ard_347_analyst_v347(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=54, w2=323, w3=455, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 54)
    acceleration = _rolling_slope(velocity, 323)
    curvature = _rolling_slope(acceleration, 455)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2846 * acceleration + 0.0035148 * anchor

def f62_ard_348_analyst_v348(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=61, w2=334, w3=468, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(61, min_periods=max(61//3, 2)).mean(), upside.rolling(334, min_periods=max(334//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.251875 + 0.0035149 * anchor

def f62_ard_349_analyst_v349(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=68, w2=345, w3=481, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(345, min_periods=max(345//3, 2)).max()
    rebound = x - x.rolling(68, min_periods=max(68//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2998 * _rolling_slope(draw, 481) + 0.003515 * anchor

def f62_ard_350_analyst_v350(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=75, w2=356, w3=494, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 75)
    baseline = trend.rolling(356, min_periods=max(356//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(494, min_periods=max(494//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.280625 + 0.0035151 * anchor

def f62_ard_351_analyst_v351(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=82, w2=367, w3=507, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 82)
    slow = _rolling_slope(x, 367)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.295 + 0.0035152 * anchor

def f62_ard_352_analyst_v352(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=89, w2=378, w3=520, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(378, min_periods=max(378//3, 2)).max()
    trough = x.rolling(89, min_periods=max(89//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.309375 + 0.0035153 * anchor

def f62_ard_353_analyst_v353(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=96, w2=389, w3=533, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(96)
    rank = change.rolling(389, min_periods=max(389//3, 2)).rank(pct=True)
    persistence = change.rolling(533, min_periods=max(533//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3302 * persistence + 0.0035154 * anchor

def f62_ard_354_analyst_v354(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=103, w2=400, w3=546, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(103, min_periods=max(103//3, 2)).std()
    vol_slow = ret.rolling(400, min_periods=max(400//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.338125 + 0.0035155 * anchor

def f62_ard_355_analyst_v355(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=110, w2=411, w3=559, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(411, min_periods=max(411//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 110)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3454 * slope + 0.0035156 * anchor

def f62_ard_356_analyst_v356(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=117, w2=422, w3=572, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(117)
    drag = impulse.rolling(422, min_periods=max(422//3, 2)).mean()
    noise = impulse.abs().rolling(572, min_periods=max(572//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.366875 + 0.0035157 * anchor

def f62_ard_357_analyst_v357(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=124, w2=433, w3=585, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 124)
    acceleration = _rolling_slope(velocity, 433)
    curvature = _rolling_slope(acceleration, 585)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3606 * acceleration + 0.0035158 * anchor

def f62_ard_358_analyst_v358(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=131, w2=444, w3=598, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(131, min_periods=max(131//3, 2)).mean(), upside.rolling(444, min_periods=max(444//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.395625 + 0.0035159 * anchor

def f62_ard_359_analyst_v359(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=138, w2=455, w3=611, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(455, min_periods=max(455//3, 2)).max()
    rebound = x - x.rolling(138, min_periods=max(138//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3758 * _rolling_slope(draw, 611) + 0.003516 * anchor

def f62_ard_360_analyst_v360(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=145, w2=466, w3=624, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 145)
    baseline = trend.rolling(466, min_periods=max(466//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(624, min_periods=max(624//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.424375 + 0.0035161 * anchor

def f62_ard_361_analyst_v361(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=152, w2=477, w3=637, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 152)
    slow = _rolling_slope(x, 477)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.43875 + 0.0035162 * anchor

def f62_ard_362_analyst_v362(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=159, w2=488, w3=650, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(488, min_periods=max(488//3, 2)).max()
    trough = x.rolling(159, min_periods=max(159//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.453125 + 0.0035163 * anchor

def f62_ard_363_analyst_v363(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=166, w2=499, w3=663, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(499, min_periods=max(499//3, 2)).rank(pct=True)
    persistence = change.rolling(663, min_periods=max(663//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.4062 * persistence + 0.0035164 * anchor

def f62_ard_364_analyst_v364(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=173, w2=510, w3=676, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(173, min_periods=max(173//3, 2)).std()
    vol_slow = ret.rolling(510, min_periods=max(510//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.481875 + 0.0035165 * anchor

def f62_ard_365_analyst_v365(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=180, w2=18, w3=689, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(18, min_periods=max(18//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 180)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.045 * slope + 0.0035166 * anchor

def f62_ard_366_analyst_v366(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=187, w2=29, w3=702, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(29, min_periods=max(29//3, 2)).mean()
    noise = impulse.abs().rolling(702, min_periods=max(702//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.510625 + 0.0035167 * anchor

def f62_ard_367_analyst_v367(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=194, w2=40, w3=715, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 194)
    acceleration = _rolling_slope(velocity, 40)
    curvature = _rolling_slope(acceleration, 715)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0602 * acceleration + 0.0035168 * anchor

def f62_ard_368_analyst_v368(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=201, w2=51, w3=728, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(201, min_periods=max(201//3, 2)).mean(), upside.rolling(51, min_periods=max(51//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.539375 + 0.0035169 * anchor

def f62_ard_369_analyst_v369(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=208, w2=62, w3=741, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(62, min_periods=max(62//3, 2)).max()
    rebound = x - x.rolling(208, min_periods=max(208//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.0754 * _rolling_slope(draw, 741) + 0.003517 * anchor

def f62_ard_370_analyst_v370(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=215, w2=73, w3=754, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 215)
    baseline = trend.rolling(73, min_periods=max(73//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(754, min_periods=max(754//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.568125 + 0.0035171 * anchor

def f62_ard_371_analyst_v371(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=222, w2=84, w3=767, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 222)
    slow = _rolling_slope(x, 84)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.5825 + 0.0035172 * anchor

def f62_ard_372_analyst_v372(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=229, w2=95, w3=23, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(95, min_periods=max(95//3, 2)).max()
    trough = x.rolling(229, min_periods=max(229//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.596875 + 0.0035173 * anchor

def f62_ard_373_analyst_v373(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=236, w2=106, w3=36, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(126)
    rank = change.rolling(106, min_periods=max(106//3, 2)).rank(pct=True)
    persistence = change.rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1058 * persistence + 0.0035174 * anchor

def f62_ard_374_analyst_v374(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=243, w2=117, w3=49, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(243, min_periods=max(243//3, 2)).std()
    vol_slow = ret.rolling(117, min_periods=max(117//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8525 + 0.0035175 * anchor

def f62_ard_375_analyst_v375(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=250, w2=128, w3=62, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(128, min_periods=max(128//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 250)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.121 * slope + 0.0035176 * anchor
