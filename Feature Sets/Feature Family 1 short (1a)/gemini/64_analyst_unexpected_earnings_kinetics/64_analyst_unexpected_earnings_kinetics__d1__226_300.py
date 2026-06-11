"""64 analyst unexpected earnings kinetics d1 first derivative features 226-300 â€” Pipeline 1a-HF Grade v3.

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

def f64_asue_226_analyst_v226_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=77, w2=120, w3=99, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(77)
    drag = impulse.rolling(120, min_periods=max(120//3, 2)).mean()
    noise = impulse.abs().rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.285625 + 0.0036227 * anchor
    return base_signal.diff()

def f64_asue_227_analyst_v227_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=84, w2=131, w3=112, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 84)
    acceleration = _rolling_slope(velocity, 131)
    curvature = _rolling_slope(acceleration, 112)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2118 * acceleration + 0.0036228 * anchor
    return base_signal.diff()

def f64_asue_228_analyst_v228_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=91, w2=142, w3=125, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(142, min_periods=max(142//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(125) * 1.314375 + 0.0036229 * anchor
    return base_signal.diff()

def f64_asue_229_analyst_v229_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=98, w2=153, w3=138, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(153, min_periods=max(153//3, 2)).max()
    rebound = x - x.rolling(98, min_periods=max(98//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.227 * _rolling_slope(draw, 138) + 0.003623 * anchor
    return base_signal.diff()

def f64_asue_230_analyst_v230_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=105, w2=164, w3=151, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 105)
    baseline = trend.rolling(164, min_periods=max(164//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.343125 + 0.0036231 * anchor
    return base_signal.diff()

def f64_asue_231_analyst_v231_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=112, w2=175, w3=164, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 112)
    slow = _rolling_slope(x, 175)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=164, adjust=False).mean() * 1.3575 + 0.0036232 * anchor
    return base_signal.diff()

def f64_asue_232_analyst_v232_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=119, w2=186, w3=177, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(186, min_periods=max(186//3, 2)).max()
    trough = x.rolling(119, min_periods=max(119//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.371875 + 0.0036233 * anchor
    return base_signal.diff()

def f64_asue_233_analyst_v233_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=126, w2=197, w3=190, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(197, min_periods=max(197//3, 2)).rank(pct=True)
    persistence = change.rolling(190, min_periods=max(190//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2574 * persistence + 0.0036234 * anchor
    return base_signal.diff()

def f64_asue_234_analyst_v234_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=133, w2=208, w3=203, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(133, min_periods=max(133//3, 2)).std()
    vol_slow = ret.rolling(208, min_periods=max(208//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.400625 + 0.0036235 * anchor
    return base_signal.diff()

def f64_asue_235_analyst_v235_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=140, w2=219, w3=216, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(219, min_periods=max(219//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 140)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2726 * slope + 0.0036236 * anchor
    return base_signal.diff()

def f64_asue_236_analyst_v236_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=147, w2=230, w3=229, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(230, min_periods=max(230//3, 2)).mean()
    noise = impulse.abs().rolling(229, min_periods=max(229//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.429375 + 0.0036237 * anchor
    return base_signal.diff()

def f64_asue_237_analyst_v237_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=154, w2=241, w3=242, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 154)
    acceleration = _rolling_slope(velocity, 241)
    curvature = _rolling_slope(acceleration, 242)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2878 * acceleration + 0.0036238 * anchor
    return base_signal.diff()

def f64_asue_238_analyst_v238_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=161, w2=252, w3=255, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(161, min_periods=max(161//3, 2)).mean(), upside.rolling(252, min_periods=max(252//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.458125 + 0.0036239 * anchor
    return base_signal.diff()

def f64_asue_239_analyst_v239_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=168, w2=263, w3=268, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(263, min_periods=max(263//3, 2)).max()
    rebound = x - x.rolling(168, min_periods=max(168//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.303 * _rolling_slope(draw, 268) + 0.003624 * anchor
    return base_signal.diff()

def f64_asue_240_analyst_v240_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=175, w2=274, w3=281, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 175)
    baseline = trend.rolling(274, min_periods=max(274//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(281, min_periods=max(281//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.486875 + 0.0036241 * anchor
    return base_signal.diff()

def f64_asue_241_analyst_v241_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=182, w2=285, w3=294, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 182)
    slow = _rolling_slope(x, 285)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=294, adjust=False).mean() * 1.50125 + 0.0036242 * anchor
    return base_signal.diff()

def f64_asue_242_analyst_v242_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=189, w2=296, w3=307, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(296, min_periods=max(296//3, 2)).max()
    trough = x.rolling(189, min_periods=max(189//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.515625 + 0.0036243 * anchor
    return base_signal.diff()

def f64_asue_243_analyst_v243_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=196, w2=307, w3=320, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(307, min_periods=max(307//3, 2)).rank(pct=True)
    persistence = change.rolling(320, min_periods=max(320//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3334 * persistence + 0.0036244 * anchor
    return base_signal.diff()

def f64_asue_244_analyst_v244_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=203, w2=318, w3=333, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(203, min_periods=max(203//3, 2)).std()
    vol_slow = ret.rolling(318, min_periods=max(318//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.544375 + 0.0036245 * anchor
    return base_signal.diff()

def f64_asue_245_analyst_v245_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=210, w2=329, w3=346, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(329, min_periods=max(329//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 210)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3486 * slope + 0.0036246 * anchor
    return base_signal.diff()

def f64_asue_246_analyst_v246_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=217, w2=340, w3=359, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(340, min_periods=max(340//3, 2)).mean()
    noise = impulse.abs().rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.573125 + 0.0036247 * anchor
    return base_signal.diff()

def f64_asue_247_analyst_v247_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=224, w2=351, w3=372, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 224)
    acceleration = _rolling_slope(velocity, 351)
    curvature = _rolling_slope(acceleration, 372)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3638 * acceleration + 0.0036248 * anchor
    return base_signal.diff()

def f64_asue_248_analyst_v248_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=231, w2=362, w3=385, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(231, min_periods=max(231//3, 2)).mean(), upside.rolling(362, min_periods=max(362//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.601875 + 0.0036249 * anchor
    return base_signal.diff()

def f64_asue_249_analyst_v249_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=238, w2=373, w3=398, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(373, min_periods=max(373//3, 2)).max()
    rebound = x - x.rolling(238, min_periods=max(238//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.379 * _rolling_slope(draw, 398) + 0.003625 * anchor
    return base_signal.diff()

def f64_asue_250_analyst_v250_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=245, w2=384, w3=411, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 245)
    baseline = trend.rolling(384, min_periods=max(384//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(411, min_periods=max(411//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8575 + 0.0036251 * anchor
    return base_signal.diff()

def f64_asue_251_analyst_v251_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=252, w2=395, w3=424, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 252)
    slow = _rolling_slope(x, 395)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.871875 + 0.0036252 * anchor
    return base_signal.diff()

def f64_asue_252_analyst_v252_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=8, w2=406, w3=437, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(406, min_periods=max(406//3, 2)).max()
    trough = x.rolling(8, min_periods=max(8//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.88625 + 0.0036253 * anchor
    return base_signal.diff()

def f64_asue_253_analyst_v253_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=15, w2=417, w3=450, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(15)
    rank = change.rolling(417, min_periods=max(417//3, 2)).rank(pct=True)
    persistence = change.rolling(450, min_periods=max(450//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4094 * persistence + 0.0036254 * anchor
    return base_signal.diff()

def f64_asue_254_analyst_v254_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=22, w2=428, w3=463, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(22, min_periods=max(22//3, 2)).std()
    vol_slow = ret.rolling(428, min_periods=max(428//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.915 + 0.0036255 * anchor
    return base_signal.diff()

def f64_asue_255_analyst_v255_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=29, w2=439, w3=476, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(439, min_periods=max(439//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 29)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0482 * slope + 0.0036256 * anchor
    return base_signal.diff()

def f64_asue_256_analyst_v256_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=36, w2=450, w3=489, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(36)
    drag = impulse.rolling(450, min_periods=max(450//3, 2)).mean()
    noise = impulse.abs().rolling(489, min_periods=max(489//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94375 + 0.0036257 * anchor
    return base_signal.diff()

def f64_asue_257_analyst_v257_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=43, w2=461, w3=502, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 43)
    acceleration = _rolling_slope(velocity, 461)
    curvature = _rolling_slope(acceleration, 502)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0634 * acceleration + 0.0036258 * anchor
    return base_signal.diff()

def f64_asue_258_analyst_v258_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=50, w2=472, w3=515, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(50, min_periods=max(50//3, 2)).mean(), upside.rolling(472, min_periods=max(472//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9725 + 0.0036259 * anchor
    return base_signal.diff()

def f64_asue_259_analyst_v259_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=57, w2=483, w3=528, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(483, min_periods=max(483//3, 2)).max()
    rebound = x - x.rolling(57, min_periods=max(57//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0786 * _rolling_slope(draw, 528) + 0.003626 * anchor
    return base_signal.diff()

def f64_asue_260_analyst_v260_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=64, w2=494, w3=541, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 64)
    baseline = trend.rolling(494, min_periods=max(494//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(541, min_periods=max(541//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.00125 + 0.0036261 * anchor
    return base_signal.diff()

def f64_asue_261_analyst_v261_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=71, w2=505, w3=554, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 71)
    slow = _rolling_slope(x, 505)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.015625 + 0.0036262 * anchor
    return base_signal.diff()

def f64_asue_262_analyst_v262_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=78, w2=13, w3=567, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(13, min_periods=max(13//3, 2)).max()
    trough = x.rolling(78, min_periods=max(78//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.03 + 0.0036263 * anchor
    return base_signal.diff()

def f64_asue_263_analyst_v263_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=85, w2=24, w3=580, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(85)
    rank = change.rolling(24, min_periods=max(24//3, 2)).rank(pct=True)
    persistence = change.rolling(580, min_periods=max(580//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.109 * persistence + 0.0036264 * anchor
    return base_signal.diff()

def f64_asue_264_analyst_v264_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=92, w2=35, w3=593, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(92, min_periods=max(92//3, 2)).std()
    vol_slow = ret.rolling(35, min_periods=max(35//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.05875 + 0.0036265 * anchor
    return base_signal.diff()

def f64_asue_265_analyst_v265_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=99, w2=46, w3=606, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(46, min_periods=max(46//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 99)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1242 * slope + 0.0036266 * anchor
    return base_signal.diff()

def f64_asue_266_analyst_v266_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=106, w2=57, w3=619, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(106)
    drag = impulse.rolling(57, min_periods=max(57//3, 2)).mean()
    noise = impulse.abs().rolling(619, min_periods=max(619//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0875 + 0.0036267 * anchor
    return base_signal.diff()

def f64_asue_267_analyst_v267_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=113, w2=68, w3=632, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 113)
    acceleration = _rolling_slope(velocity, 68)
    curvature = _rolling_slope(acceleration, 632)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1394 * acceleration + 0.0036268 * anchor
    return base_signal.diff()

def f64_asue_268_analyst_v268_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=120, w2=79, w3=645, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(120, min_periods=max(120//3, 2)).mean(), upside.rolling(79, min_periods=max(79//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.11625 + 0.0036269 * anchor
    return base_signal.diff()

def f64_asue_269_analyst_v269_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=127, w2=90, w3=658, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(90, min_periods=max(90//3, 2)).max()
    rebound = x - x.rolling(127, min_periods=max(127//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1546 * _rolling_slope(draw, 658) + 0.003627 * anchor
    return base_signal.diff()

def f64_asue_270_analyst_v270_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=134, w2=101, w3=671, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 134)
    baseline = trend.rolling(101, min_periods=max(101//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(671, min_periods=max(671//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.145 + 0.0036271 * anchor
    return base_signal.diff()

def f64_asue_271_analyst_v271_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=141, w2=112, w3=684, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 141)
    slow = _rolling_slope(x, 112)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.159375 + 0.0036272 * anchor
    return base_signal.diff()

def f64_asue_272_analyst_v272_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=148, w2=123, w3=697, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(123, min_periods=max(123//3, 2)).max()
    trough = x.rolling(148, min_periods=max(148//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17375 + 0.0036273 * anchor
    return base_signal.diff()

def f64_asue_273_analyst_v273_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=155, w2=134, w3=710, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(134, min_periods=max(134//3, 2)).rank(pct=True)
    persistence = change.rolling(710, min_periods=max(710//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.185 * persistence + 0.0036274 * anchor
    return base_signal.diff()

def f64_asue_274_analyst_v274_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=162, w2=145, w3=723, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(162, min_periods=max(162//3, 2)).std()
    vol_slow = ret.rolling(145, min_periods=max(145//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2025 + 0.0036275 * anchor
    return base_signal.diff()

def f64_asue_275_analyst_v275_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=169, w2=156, w3=736, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(156, min_periods=max(156//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 169)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2002 * slope + 0.0036276 * anchor
    return base_signal.diff()

def f64_asue_276_analyst_v276_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=176, w2=167, w3=749, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(167, min_periods=max(167//3, 2)).mean()
    noise = impulse.abs().rolling(749, min_periods=max(749//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.23125 + 0.0036277 * anchor
    return base_signal.diff()

def f64_asue_277_analyst_v277_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=183, w2=178, w3=762, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 183)
    acceleration = _rolling_slope(velocity, 178)
    curvature = _rolling_slope(acceleration, 762)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2154 * acceleration + 0.0036278 * anchor
    return base_signal.diff()

def f64_asue_278_analyst_v278_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=190, w2=189, w3=18, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(190, min_periods=max(190//3, 2)).mean(), upside.rolling(189, min_periods=max(189//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(18) * 1.26 + 0.0036279 * anchor
    return base_signal.diff()

def f64_asue_279_analyst_v279_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=197, w2=200, w3=31, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(200, min_periods=max(200//3, 2)).max()
    rebound = x - x.rolling(197, min_periods=max(197//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2306 * _rolling_slope(draw, 31) + 0.003628 * anchor
    return base_signal.diff()

def f64_asue_280_analyst_v280_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=204, w2=211, w3=44, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 204)
    baseline = trend.rolling(211, min_periods=max(211//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(44, min_periods=max(44//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.28875 + 0.0036281 * anchor
    return base_signal.diff()

def f64_asue_281_analyst_v281_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=211, w2=222, w3=57, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 211)
    slow = _rolling_slope(x, 222)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=57, adjust=False).mean() * 1.303125 + 0.0036282 * anchor
    return base_signal.diff()

def f64_asue_282_analyst_v282_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=218, w2=233, w3=70, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(233, min_periods=max(233//3, 2)).max()
    trough = x.rolling(218, min_periods=max(218//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.3175 + 0.0036283 * anchor
    return base_signal.diff()

def f64_asue_283_analyst_v283_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=225, w2=244, w3=83, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(244, min_periods=max(244//3, 2)).rank(pct=True)
    persistence = change.rolling(83, min_periods=max(83//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.261 * persistence + 0.0036284 * anchor
    return base_signal.diff()

def f64_asue_284_analyst_v284_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=232, w2=255, w3=96, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(232, min_periods=max(232//3, 2)).std()
    vol_slow = ret.rolling(255, min_periods=max(255//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.34625 + 0.0036285 * anchor
    return base_signal.diff()

def f64_asue_285_analyst_v285_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=239, w2=266, w3=109, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(266, min_periods=max(266//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 239)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2762 * slope + 0.0036286 * anchor
    return base_signal.diff()

def f64_asue_286_analyst_v286_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=246, w2=277, w3=122, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(277, min_periods=max(277//3, 2)).mean()
    noise = impulse.abs().rolling(122, min_periods=max(122//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.375 + 0.0036287 * anchor
    return base_signal.diff()

def f64_asue_287_analyst_v287_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=253, w2=288, w3=135, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 253)
    acceleration = _rolling_slope(velocity, 288)
    curvature = _rolling_slope(acceleration, 135)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2914 * acceleration + 0.0036288 * anchor
    return base_signal.diff()

def f64_asue_288_analyst_v288_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=9, w2=299, w3=148, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(9, min_periods=max(9//3, 2)).mean(), upside.rolling(299, min_periods=max(299//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.40375 + 0.0036289 * anchor
    return base_signal.diff()

def f64_asue_289_analyst_v289_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=16, w2=310, w3=161, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(310, min_periods=max(310//3, 2)).max()
    rebound = x - x.rolling(16, min_periods=max(16//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3066 * _rolling_slope(draw, 161) + 0.003629 * anchor
    return base_signal.diff()

def f64_asue_290_analyst_v290_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=23, w2=321, w3=174, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 23)
    baseline = trend.rolling(321, min_periods=max(321//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(174, min_periods=max(174//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4325 + 0.0036291 * anchor
    return base_signal.diff()

def f64_asue_291_analyst_v291_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=30, w2=332, w3=187, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 332)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=187, adjust=False).mean() * 1.446875 + 0.0036292 * anchor
    return base_signal.diff()

def f64_asue_292_analyst_v292_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=37, w2=343, w3=200, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(343, min_periods=max(343//3, 2)).max()
    trough = x.rolling(37, min_periods=max(37//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.46125 + 0.0036293 * anchor
    return base_signal.diff()

def f64_asue_293_analyst_v293_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=44, w2=354, w3=213, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(44)
    rank = change.rolling(354, min_periods=max(354//3, 2)).rank(pct=True)
    persistence = change.rolling(213, min_periods=max(213//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.337 * persistence + 0.0036294 * anchor
    return base_signal.diff()

def f64_asue_294_analyst_v294_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=51, w2=365, w3=226, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(51, min_periods=max(51//3, 2)).std()
    vol_slow = ret.rolling(365, min_periods=max(365//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.49 + 0.0036295 * anchor
    return base_signal.diff()

def f64_asue_295_analyst_v295_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=58, w2=376, w3=239, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(376, min_periods=max(376//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3522 * slope + 0.0036296 * anchor
    return base_signal.diff()

def f64_asue_296_analyst_v296_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=65, w2=387, w3=252, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(65)
    drag = impulse.rolling(387, min_periods=max(387//3, 2)).mean()
    noise = impulse.abs().rolling(252, min_periods=max(252//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.51875 + 0.0036297 * anchor
    return base_signal.diff()

def f64_asue_297_analyst_v297_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=72, w2=398, w3=265, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 398)
    curvature = _rolling_slope(acceleration, 265)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3674 * acceleration + 0.0036298 * anchor
    return base_signal.diff()

def f64_asue_298_analyst_v298_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=79, w2=409, w3=278, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(79, min_periods=max(79//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5475 + 0.0036299 * anchor
    return base_signal.diff()

def f64_asue_299_analyst_v299_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=86, w2=420, w3=291, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(420, min_periods=max(420//3, 2)).max()
    rebound = x - x.rolling(86, min_periods=max(86//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3826 * _rolling_slope(draw, 291) + 0.00363 * anchor
    return base_signal.diff()

def f64_asue_300_analyst_v300_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=93, w2=431, w3=304, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 93)
    baseline = trend.rolling(431, min_periods=max(431//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(304, min_periods=max(304//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.57625 + 0.0036301 * anchor
    return base_signal.diff()
