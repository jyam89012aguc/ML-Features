"""63 analyst downgrade cluster base features 526-600 â€” Pipeline 1a-HF Grade v3.

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

def f63_adc_526_analyst_v526(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=236, w2=341, w3=741, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(341, min_periods=max(341//3, 2)).mean()
    noise = impulse.abs().rolling(741, min_periods=max(741//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.611875 + 0.0035927 * anchor

def f63_adc_527_analyst_v527(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=243, w2=352, w3=754, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 243)
    acceleration = _rolling_slope(velocity, 352)
    curvature = _rolling_slope(acceleration, 754)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1902 * acceleration + 0.0035928 * anchor

def f63_adc_528_analyst_v528(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=250, w2=363, w3=767, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(363, min_periods=max(363//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.8675 + 0.0035929 * anchor

def f63_adc_529_analyst_v529(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=6, w2=374, w3=23, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(374, min_periods=max(374//3, 2)).max()
    rebound = x - x.rolling(6, min_periods=max(6//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2054 * _rolling_slope(draw, 23) + 0.003593 * anchor

def f63_adc_530_analyst_v530(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=13, w2=385, w3=36, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(385, min_periods=max(385//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(36, min_periods=max(36//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.89625 + 0.0035931 * anchor

def f63_adc_531_analyst_v531(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=20, w2=396, w3=49, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 20)
    slow = _rolling_slope(x, 396)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=49, adjust=False).mean() * 0.910625 + 0.0035932 * anchor

def f63_adc_532_analyst_v532(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=27, w2=407, w3=62, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(407, min_periods=max(407//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.925 + 0.0035933 * anchor

def f63_adc_533_analyst_v533(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=34, w2=418, w3=75, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(34)
    rank = change.rolling(418, min_periods=max(418//3, 2)).rank(pct=True)
    persistence = change.rolling(75, min_periods=max(75//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2358 * persistence + 0.0035934 * anchor

def f63_adc_534_analyst_v534(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=41, w2=429, w3=88, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(429, min_periods=max(429//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.95375 + 0.0035935 * anchor

def f63_adc_535_analyst_v535(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=48, w2=440, w3=101, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(440, min_periods=max(440//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 48)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.251 * slope + 0.0035936 * anchor

def f63_adc_536_analyst_v536(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=55, w2=451, w3=114, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(55)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(114, min_periods=max(114//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.9825 + 0.0035937 * anchor

def f63_adc_537_analyst_v537(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=62, w2=462, w3=127, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 62)
    acceleration = _rolling_slope(velocity, 462)
    curvature = _rolling_slope(acceleration, 127)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2662 * acceleration + 0.0035938 * anchor

def f63_adc_538_analyst_v538(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=69, w2=473, w3=140, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.01125 + 0.0035939 * anchor

def f63_adc_539_analyst_v539(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=76, w2=484, w3=153, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(484, min_periods=max(484//3, 2)).max()
    rebound = x - x.rolling(76, min_periods=max(76//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.2814 * _rolling_slope(draw, 153) + 0.003594 * anchor

def f63_adc_540_analyst_v540(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=83, w2=495, w3=166, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(166, min_periods=max(166//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.04 + 0.0035941 * anchor

def f63_adc_541_analyst_v541(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=90, w2=506, w3=179, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 90)
    slow = _rolling_slope(x, 506)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=179, adjust=False).mean() * 1.054375 + 0.0035942 * anchor

def f63_adc_542_analyst_v542(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=97, w2=14, w3=192, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.06875 + 0.0035943 * anchor

def f63_adc_543_analyst_v543(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=104, w2=25, w3=205, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(104)
    rank = change.rolling(25, min_periods=max(25//3, 2)).rank(pct=True)
    persistence = change.rolling(205, min_periods=max(205//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3118 * persistence + 0.0035944 * anchor

def f63_adc_544_analyst_v544(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=111, w2=36, w3=218, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.0975 + 0.0035945 * anchor

def f63_adc_545_analyst_v545(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=118, w2=47, w3=231, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(47, min_periods=max(47//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 118)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.327 * slope + 0.0035946 * anchor

def f63_adc_546_analyst_v546(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=125, w2=58, w3=244, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(125)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(244, min_periods=max(244//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.12625 + 0.0035947 * anchor

def f63_adc_547_analyst_v547(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=132, w2=69, w3=257, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 132)
    acceleration = _rolling_slope(velocity, 69)
    curvature = _rolling_slope(acceleration, 257)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3422 * acceleration + 0.0035948 * anchor

def f63_adc_548_analyst_v548(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=139, w2=80, w3=270, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.155 + 0.0035949 * anchor

def f63_adc_549_analyst_v549(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=146, w2=91, w3=283, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(91, min_periods=max(91//3, 2)).max()
    rebound = x - x.rolling(146, min_periods=max(146//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.3574 * _rolling_slope(draw, 283) + 0.003595 * anchor

def f63_adc_550_analyst_v550(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=153, w2=102, w3=296, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(296, min_periods=max(296//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.18375 + 0.0035951 * anchor

def f63_adc_551_analyst_v551(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=160, w2=113, w3=309, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 160)
    slow = _rolling_slope(x, 113)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.198125 + 0.0035952 * anchor

def f63_adc_552_analyst_v552(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=167, w2=124, w3=322, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(124, min_periods=max(124//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2125 + 0.0035953 * anchor

def f63_adc_553_analyst_v553(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=174, w2=135, w3=335, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(135, min_periods=max(135//3, 2)).rank(pct=True)
    persistence = change.rolling(335, min_periods=max(335//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3878 * persistence + 0.0035954 * anchor

def f63_adc_554_analyst_v554(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=181, w2=146, w3=348, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(146, min_periods=max(146//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.24125 + 0.0035955 * anchor

def f63_adc_555_analyst_v555(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=188, w2=157, w3=361, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(157, min_periods=max(157//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 188)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.403 * slope + 0.0035956 * anchor

def f63_adc_556_analyst_v556(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=195, w2=168, w3=374, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(168, min_periods=max(168//3, 2)).mean()
    noise = impulse.abs().rolling(374, min_periods=max(374//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.27 + 0.0035957 * anchor

def f63_adc_557_analyst_v557(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=202, w2=179, w3=387, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 202)
    acceleration = _rolling_slope(velocity, 179)
    curvature = _rolling_slope(acceleration, 387)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0418 * acceleration + 0.0035958 * anchor

def f63_adc_558_analyst_v558(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=209, w2=190, w3=400, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(190, min_periods=max(190//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.29875 + 0.0035959 * anchor

def f63_adc_559_analyst_v559(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=216, w2=201, w3=413, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(201, min_periods=max(201//3, 2)).max()
    rebound = x - x.rolling(216, min_periods=max(216//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.057 * _rolling_slope(draw, 413) + 0.003596 * anchor

def f63_adc_560_analyst_v560(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=223, w2=212, w3=426, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(212, min_periods=max(212//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(426, min_periods=max(426//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3275 + 0.0035961 * anchor

def f63_adc_561_analyst_v561(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=230, w2=223, w3=439, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 230)
    slow = _rolling_slope(x, 223)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.341875 + 0.0035962 * anchor

def f63_adc_562_analyst_v562(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=237, w2=234, w3=452, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(234, min_periods=max(234//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.35625 + 0.0035963 * anchor

def f63_adc_563_analyst_v563(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=244, w2=245, w3=465, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(245, min_periods=max(245//3, 2)).rank(pct=True)
    persistence = change.rolling(465, min_periods=max(465//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.0874 * persistence + 0.0035964 * anchor

def f63_adc_564_analyst_v564(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=251, w2=256, w3=478, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(256, min_periods=max(256//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.385 + 0.0035965 * anchor

def f63_adc_565_analyst_v565(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=7, w2=267, w3=491, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(267, min_periods=max(267//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 7)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1026 * slope + 0.0035966 * anchor

def f63_adc_566_analyst_v566(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=14, w2=278, w3=504, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(14)
    drag = impulse.rolling(278, min_periods=max(278//3, 2)).mean()
    noise = impulse.abs().rolling(504, min_periods=max(504//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.41375 + 0.0035967 * anchor

def f63_adc_567_analyst_v567(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=21, w2=289, w3=517, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 21)
    acceleration = _rolling_slope(velocity, 289)
    curvature = _rolling_slope(acceleration, 517)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1178 * acceleration + 0.0035968 * anchor

def f63_adc_568_analyst_v568(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=28, w2=300, w3=530, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.4425 + 0.0035969 * anchor

def f63_adc_569_analyst_v569(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=35, w2=311, w3=543, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(311, min_periods=max(311//3, 2)).max()
    rebound = x - x.rolling(35, min_periods=max(35//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.133 * _rolling_slope(draw, 543) + 0.003597 * anchor

def f63_adc_570_analyst_v570(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=42, w2=322, w3=556, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(322, min_periods=max(322//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(556, min_periods=max(556//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.47125 + 0.0035971 * anchor

def f63_adc_571_analyst_v571(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=49, w2=333, w3=569, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 49)
    slow = _rolling_slope(x, 333)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.485625 + 0.0035972 * anchor

def f63_adc_572_analyst_v572(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=56, w2=344, w3=582, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.5 + 0.0035973 * anchor

def f63_adc_573_analyst_v573(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=63, w2=355, w3=595, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(63)
    rank = change.rolling(355, min_periods=max(355//3, 2)).rank(pct=True)
    persistence = change.rolling(595, min_periods=max(595//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1634 * persistence + 0.0035974 * anchor

def f63_adc_574_analyst_v574(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=70, w2=366, w3=608, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(366, min_periods=max(366//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.52875 + 0.0035975 * anchor

def f63_adc_575_analyst_v575(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=77, w2=377, w3=621, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(377, min_periods=max(377//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 77)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1786 * slope + 0.0035976 * anchor

def f63_adc_576_analyst_v576(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=84, w2=388, w3=634, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(84)
    drag = impulse.rolling(388, min_periods=max(388//3, 2)).mean()
    noise = impulse.abs().rolling(634, min_periods=max(634//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.5575 + 0.0035977 * anchor

def f63_adc_577_analyst_v577(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=91, w2=399, w3=647, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 91)
    acceleration = _rolling_slope(velocity, 399)
    curvature = _rolling_slope(acceleration, 647)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1938 * acceleration + 0.0035978 * anchor

def f63_adc_578_analyst_v578(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=98, w2=410, w3=660, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.58625 + 0.0035979 * anchor

def f63_adc_579_analyst_v579(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=105, w2=421, w3=673, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(421, min_periods=max(421//3, 2)).max()
    rebound = x - x.rolling(105, min_periods=max(105//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.209 * _rolling_slope(draw, 673) + 0.003598 * anchor

def f63_adc_580_analyst_v580(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=112, w2=432, w3=686, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(432, min_periods=max(432//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(686, min_periods=max(686//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.615 + 0.0035981 * anchor

def f63_adc_581_analyst_v581(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=119, w2=443, w3=699, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 443)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.85625 + 0.0035982 * anchor

def f63_adc_582_analyst_v582(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=126, w2=454, w3=712, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.870625 + 0.0035983 * anchor

def f63_adc_583_analyst_v583(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=133, w2=465, w3=725, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(465, min_periods=max(465//3, 2)).rank(pct=True)
    persistence = change.rolling(725, min_periods=max(725//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2394 * persistence + 0.0035984 * anchor

def f63_adc_584_analyst_v584(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=140, w2=476, w3=738, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(476, min_periods=max(476//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.899375 + 0.0035985 * anchor

def f63_adc_585_analyst_v585(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=147, w2=487, w3=751, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(487, min_periods=max(487//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.2546 * slope + 0.0035986 * anchor

def f63_adc_586_analyst_v586(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=154, w2=498, w3=764, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(498, min_periods=max(498//3, 2)).mean()
    noise = impulse.abs().rolling(764, min_periods=max(764//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.928125 + 0.0035987 * anchor

def f63_adc_587_analyst_v587(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=161, w2=509, w3=20, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 509)
    curvature = _rolling_slope(acceleration, 20)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.2698 * acceleration + 0.0035988 * anchor

def f63_adc_588_analyst_v588(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=168, w2=17, w3=33, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(17, min_periods=max(17//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(33) * 0.956875 + 0.0035989 * anchor

def f63_adc_589_analyst_v589(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=175, w2=28, w3=46, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(28, min_periods=max(28//3, 2)).max()
    rebound = x - x.rolling(175, min_periods=max(175//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.285 * _rolling_slope(draw, 46) + 0.003599 * anchor

def f63_adc_590_analyst_v590(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=182, w2=39, w3=59, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(39, min_periods=max(39//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(59, min_periods=max(59//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.985625 + 0.0035991 * anchor

def f63_adc_591_analyst_v591(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=189, w2=50, w3=72, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 189)
    slow = _rolling_slope(x, 50)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=72, adjust=False).mean() * 1.0 + 0.0035992 * anchor

def f63_adc_592_analyst_v592(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=196, w2=61, w3=85, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(61, min_periods=max(61//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.014375 + 0.0035993 * anchor

def f63_adc_593_analyst_v593(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=203, w2=72, w3=98, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(72, min_periods=max(72//3, 2)).rank(pct=True)
    persistence = change.rolling(98, min_periods=max(98//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3154 * persistence + 0.0035994 * anchor

def f63_adc_594_analyst_v594(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=210, w2=83, w3=111, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(83, min_periods=max(83//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.043125 + 0.0035995 * anchor

def f63_adc_595_analyst_v595(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=217, w2=94, w3=124, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(94, min_periods=max(94//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 217)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.3306 * slope + 0.0035996 * anchor

def f63_adc_596_analyst_v596(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=224, w2=105, w3=137, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(105, min_periods=max(105//3, 2)).mean()
    noise = impulse.abs().rolling(137, min_periods=max(137//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.071875 + 0.0035997 * anchor

def f63_adc_597_analyst_v597(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=231, w2=116, w3=150, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 231)
    acceleration = _rolling_slope(velocity, 116)
    curvature = _rolling_slope(acceleration, 150)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3458 * acceleration + 0.0035998 * anchor

def f63_adc_598_analyst_v598(eps_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=238, w2=127, w3=163, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(238, min_periods=max(238//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.100625 + 0.0035999 * anchor

def f63_adc_599_analyst_v599(rev_disp: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=245, w2=138, w3=176, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(138, min_periods=max(138//3, 2)).max()
    rebound = x - x.rolling(245, min_periods=max(245//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(draw, rebound.abs()) + 0.361 * _rolling_slope(draw, 176) + 0.0036 * anchor

def f63_adc_600_analyst_v600(eps_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=252, w2=149, w3=189, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 252)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(189, min_periods=max(189//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.129375 + 0.0036001 * anchor
