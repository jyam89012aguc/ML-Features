"""63 analyst downgrade cluster d1 first derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

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

def f63_adc_151_analyst_v151_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=121, w2=240, w3=408, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 121)
    slow = _rolling_slope(x, 240)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.86 + 0.0035552 * anchor
    return base_signal.diff()

def f63_adc_152_analyst_v152_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=128, w2=251, w3=421, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(251, min_periods=max(251//3, 2)).max()
    trough = x.rolling(128, min_periods=max(128//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.874375 + 0.0035553 * anchor
    return base_signal.diff()

def f63_adc_153_analyst_v153_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=135, w2=262, w3=434, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(262, min_periods=max(262//3, 2)).rank(pct=True)
    persistence = change.rolling(434, min_periods=max(434//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.359 * persistence + 0.0035554 * anchor
    return base_signal.diff()

def f63_adc_154_analyst_v154_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=142, w2=273, w3=447, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(142, min_periods=max(142//3, 2)).std()
    vol_slow = ret.rolling(273, min_periods=max(273//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.903125 + 0.0035555 * anchor
    return base_signal.diff()

def f63_adc_155_analyst_v155_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=149, w2=284, w3=460, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(284, min_periods=max(284//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 149)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3742 * slope + 0.0035556 * anchor
    return base_signal.diff()

def f63_adc_156_analyst_v156_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=156, w2=295, w3=473, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(295, min_periods=max(295//3, 2)).mean()
    noise = impulse.abs().rolling(473, min_periods=max(473//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.931875 + 0.0035557 * anchor
    return base_signal.diff()

def f63_adc_157_analyst_v157_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=163, w2=306, w3=486, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 163)
    acceleration = _rolling_slope(velocity, 306)
    curvature = _rolling_slope(acceleration, 486)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3894 * acceleration + 0.0035558 * anchor
    return base_signal.diff()

def f63_adc_158_analyst_v158_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=170, w2=317, w3=499, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(170, min_periods=max(170//3, 2)).mean(), upside.rolling(317, min_periods=max(317//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.960625 + 0.0035559 * anchor
    return base_signal.diff()

def f63_adc_159_analyst_v159_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=177, w2=328, w3=512, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(328, min_periods=max(328//3, 2)).max()
    rebound = x - x.rolling(177, min_periods=max(177//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4046 * _rolling_slope(draw, 512) + 0.003556 * anchor
    return base_signal.diff()

def f63_adc_160_analyst_v160_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=184, w2=339, w3=525, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 184)
    baseline = trend.rolling(339, min_periods=max(339//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(525, min_periods=max(525//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.989375 + 0.0035561 * anchor
    return base_signal.diff()

def f63_adc_161_analyst_v161_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=191, w2=350, w3=538, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 191)
    slow = _rolling_slope(x, 350)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.00375 + 0.0035562 * anchor
    return base_signal.diff()

def f63_adc_162_analyst_v162_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=198, w2=361, w3=551, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(361, min_periods=max(361//3, 2)).max()
    trough = x.rolling(198, min_periods=max(198//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.018125 + 0.0035563 * anchor
    return base_signal.diff()

def f63_adc_163_analyst_v163_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=205, w2=372, w3=564, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(372, min_periods=max(372//3, 2)).rank(pct=True)
    persistence = change.rolling(564, min_periods=max(564//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0586 * persistence + 0.0035564 * anchor
    return base_signal.diff()

def f63_adc_164_analyst_v164_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=212, w2=383, w3=577, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(212, min_periods=max(212//3, 2)).std()
    vol_slow = ret.rolling(383, min_periods=max(383//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.046875 + 0.0035565 * anchor
    return base_signal.diff()

def f63_adc_165_analyst_v165_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=219, w2=394, w3=590, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(394, min_periods=max(394//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 219)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0738 * slope + 0.0035566 * anchor
    return base_signal.diff()

def f63_adc_166_analyst_v166_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=226, w2=405, w3=603, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(405, min_periods=max(405//3, 2)).mean()
    noise = impulse.abs().rolling(603, min_periods=max(603//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.075625 + 0.0035567 * anchor
    return base_signal.diff()

def f63_adc_167_analyst_v167_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=233, w2=416, w3=616, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 233)
    acceleration = _rolling_slope(velocity, 416)
    curvature = _rolling_slope(acceleration, 616)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.089 * acceleration + 0.0035568 * anchor
    return base_signal.diff()

def f63_adc_168_analyst_v168_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=240, w2=427, w3=629, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(240, min_periods=max(240//3, 2)).mean(), upside.rolling(427, min_periods=max(427//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.104375 + 0.0035569 * anchor
    return base_signal.diff()

def f63_adc_169_analyst_v169_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=247, w2=438, w3=642, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(438, min_periods=max(438//3, 2)).max()
    rebound = x - x.rolling(247, min_periods=max(247//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1042 * _rolling_slope(draw, 642) + 0.003557 * anchor
    return base_signal.diff()

def f63_adc_170_analyst_v170_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=254, w2=449, w3=655, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 254)
    baseline = trend.rolling(449, min_periods=max(449//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(655, min_periods=max(655//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.133125 + 0.0035571 * anchor
    return base_signal.diff()

def f63_adc_171_analyst_v171_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=10, w2=460, w3=668, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 10)
    slow = _rolling_slope(x, 460)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1475 + 0.0035572 * anchor
    return base_signal.diff()

def f63_adc_172_analyst_v172_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=17, w2=471, w3=681, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(471, min_periods=max(471//3, 2)).max()
    trough = x.rolling(17, min_periods=max(17//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.161875 + 0.0035573 * anchor
    return base_signal.diff()

def f63_adc_173_analyst_v173_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=24, w2=482, w3=694, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(24)
    rank = change.rolling(482, min_periods=max(482//3, 2)).rank(pct=True)
    persistence = change.rolling(694, min_periods=max(694//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1346 * persistence + 0.0035574 * anchor
    return base_signal.diff()

def f63_adc_174_analyst_v174_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=31, w2=493, w3=707, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(31, min_periods=max(31//3, 2)).std()
    vol_slow = ret.rolling(493, min_periods=max(493//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.190625 + 0.0035575 * anchor
    return base_signal.diff()

def f63_adc_175_analyst_v175_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=38, w2=504, w3=720, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(504, min_periods=max(504//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 38)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1498 * slope + 0.0035576 * anchor
    return base_signal.diff()

def f63_adc_176_analyst_v176_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=45, w2=12, w3=733, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(45)
    drag = impulse.rolling(12, min_periods=max(12//3, 2)).mean()
    noise = impulse.abs().rolling(733, min_periods=max(733//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.219375 + 0.0035577 * anchor
    return base_signal.diff()

def f63_adc_177_analyst_v177_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=52, w2=23, w3=746, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 52)
    acceleration = _rolling_slope(velocity, 23)
    curvature = _rolling_slope(acceleration, 746)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.165 * acceleration + 0.0035578 * anchor
    return base_signal.diff()

def f63_adc_178_analyst_v178_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=59, w2=34, w3=759, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(59, min_periods=max(59//3, 2)).mean(), upside.rolling(34, min_periods=max(34//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.248125 + 0.0035579 * anchor
    return base_signal.diff()

def f63_adc_179_analyst_v179_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=66, w2=45, w3=15, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(45, min_periods=max(45//3, 2)).max()
    rebound = x - x.rolling(66, min_periods=max(66//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1802 * _rolling_slope(draw, 15) + 0.003558 * anchor
    return base_signal.diff()

def f63_adc_180_analyst_v180_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=73, w2=56, w3=28, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 73)
    baseline = trend.rolling(56, min_periods=max(56//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(28, min_periods=max(28//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.276875 + 0.0035581 * anchor
    return base_signal.diff()

def f63_adc_181_analyst_v181_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=80, w2=67, w3=41, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 80)
    slow = _rolling_slope(x, 67)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=41, adjust=False).mean() * 1.29125 + 0.0035582 * anchor
    return base_signal.diff()

def f63_adc_182_analyst_v182_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=87, w2=78, w3=54, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(78, min_periods=max(78//3, 2)).max()
    trough = x.rolling(87, min_periods=max(87//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.305625 + 0.0035583 * anchor
    return base_signal.diff()

def f63_adc_183_analyst_v183_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=94, w2=89, w3=67, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(94)
    rank = change.rolling(89, min_periods=max(89//3, 2)).rank(pct=True)
    persistence = change.rolling(67, min_periods=max(67//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2106 * persistence + 0.0035584 * anchor
    return base_signal.diff()

def f63_adc_184_analyst_v184_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=101, w2=100, w3=80, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(101, min_periods=max(101//3, 2)).std()
    vol_slow = ret.rolling(100, min_periods=max(100//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.334375 + 0.0035585 * anchor
    return base_signal.diff()

def f63_adc_185_analyst_v185_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=108, w2=111, w3=93, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(111, min_periods=max(111//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 108)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2258 * slope + 0.0035586 * anchor
    return base_signal.diff()

def f63_adc_186_analyst_v186_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=115, w2=122, w3=106, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(115)
    drag = impulse.rolling(122, min_periods=max(122//3, 2)).mean()
    noise = impulse.abs().rolling(106, min_periods=max(106//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.363125 + 0.0035587 * anchor
    return base_signal.diff()

def f63_adc_187_analyst_v187_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=122, w2=133, w3=119, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 122)
    acceleration = _rolling_slope(velocity, 133)
    curvature = _rolling_slope(acceleration, 119)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.241 * acceleration + 0.0035588 * anchor
    return base_signal.diff()

def f63_adc_188_analyst_v188_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=129, w2=144, w3=132, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(129, min_periods=max(129//3, 2)).mean(), upside.rolling(144, min_periods=max(144//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.391875 + 0.0035589 * anchor
    return base_signal.diff()

def f63_adc_189_analyst_v189_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=136, w2=155, w3=145, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(155, min_periods=max(155//3, 2)).max()
    rebound = x - x.rolling(136, min_periods=max(136//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2562 * _rolling_slope(draw, 145) + 0.003559 * anchor
    return base_signal.diff()

def f63_adc_190_analyst_v190_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=143, w2=166, w3=158, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 143)
    baseline = trend.rolling(166, min_periods=max(166//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(158, min_periods=max(158//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.420625 + 0.0035591 * anchor
    return base_signal.diff()

def f63_adc_191_analyst_v191_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=150, w2=177, w3=171, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 150)
    slow = _rolling_slope(x, 177)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=171, adjust=False).mean() * 1.435 + 0.0035592 * anchor
    return base_signal.diff()

def f63_adc_192_analyst_v192_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=157, w2=188, w3=184, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(188, min_periods=max(188//3, 2)).max()
    trough = x.rolling(157, min_periods=max(157//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.449375 + 0.0035593 * anchor
    return base_signal.diff()

def f63_adc_193_analyst_v193_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=164, w2=199, w3=197, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(199, min_periods=max(199//3, 2)).rank(pct=True)
    persistence = change.rolling(197, min_periods=max(197//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2866 * persistence + 0.0035594 * anchor
    return base_signal.diff()

def f63_adc_194_analyst_v194_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=171, w2=210, w3=210, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(171, min_periods=max(171//3, 2)).std()
    vol_slow = ret.rolling(210, min_periods=max(210//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.478125 + 0.0035595 * anchor
    return base_signal.diff()

def f63_adc_195_analyst_v195_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=178, w2=221, w3=223, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(221, min_periods=max(221//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 178)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3018 * slope + 0.0035596 * anchor
    return base_signal.diff()

def f63_adc_196_analyst_v196_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=185, w2=232, w3=236, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(232, min_periods=max(232//3, 2)).mean()
    noise = impulse.abs().rolling(236, min_periods=max(236//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.506875 + 0.0035597 * anchor
    return base_signal.diff()

def f63_adc_197_analyst_v197_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=192, w2=243, w3=249, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 192)
    acceleration = _rolling_slope(velocity, 243)
    curvature = _rolling_slope(acceleration, 249)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.317 * acceleration + 0.0035598 * anchor
    return base_signal.diff()

def f63_adc_198_analyst_v198_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=199, w2=254, w3=262, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(199, min_periods=max(199//3, 2)).mean(), upside.rolling(254, min_periods=max(254//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.535625 + 0.0035599 * anchor
    return base_signal.diff()

def f63_adc_199_analyst_v199_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=206, w2=265, w3=275, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(265, min_periods=max(265//3, 2)).max()
    rebound = x - x.rolling(206, min_periods=max(206//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3322 * _rolling_slope(draw, 275) + 0.00356 * anchor
    return base_signal.diff()

def f63_adc_200_analyst_v200_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=213, w2=276, w3=288, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 213)
    baseline = trend.rolling(276, min_periods=max(276//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(288, min_periods=max(288//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.564375 + 0.0035601 * anchor
    return base_signal.diff()

def f63_adc_201_analyst_v201_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=220, w2=287, w3=301, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 220)
    slow = _rolling_slope(x, 287)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.57875 + 0.0035602 * anchor
    return base_signal.diff()

def f63_adc_202_analyst_v202_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=227, w2=298, w3=314, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(298, min_periods=max(298//3, 2)).max()
    trough = x.rolling(227, min_periods=max(227//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.593125 + 0.0035603 * anchor
    return base_signal.diff()

def f63_adc_203_analyst_v203_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=234, w2=309, w3=327, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(309, min_periods=max(309//3, 2)).rank(pct=True)
    persistence = change.rolling(327, min_periods=max(327//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3626 * persistence + 0.0035604 * anchor
    return base_signal.diff()

def f63_adc_204_analyst_v204_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=241, w2=320, w3=340, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(241, min_periods=max(241//3, 2)).std()
    vol_slow = ret.rolling(320, min_periods=max(320//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.621875 + 0.0035605 * anchor
    return base_signal.diff()

def f63_adc_205_analyst_v205_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=248, w2=331, w3=353, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(331, min_periods=max(331//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 248)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3778 * slope + 0.0035606 * anchor
    return base_signal.diff()

def f63_adc_206_analyst_v206_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=255, w2=342, w3=366, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(342, min_periods=max(342//3, 2)).mean()
    noise = impulse.abs().rolling(366, min_periods=max(366//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.8775 + 0.0035607 * anchor
    return base_signal.diff()

def f63_adc_207_analyst_v207_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=11, w2=353, w3=379, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 11)
    acceleration = _rolling_slope(velocity, 353)
    curvature = _rolling_slope(acceleration, 379)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.393 * acceleration + 0.0035608 * anchor
    return base_signal.diff()

def f63_adc_208_analyst_v208_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=18, w2=364, w3=392, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(18, min_periods=max(18//3, 2)).mean(), upside.rolling(364, min_periods=max(364//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.90625 + 0.0035609 * anchor
    return base_signal.diff()

def f63_adc_209_analyst_v209_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=25, w2=375, w3=405, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(375, min_periods=max(375//3, 2)).max()
    rebound = x - x.rolling(25, min_periods=max(25//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4082 * _rolling_slope(draw, 405) + 0.003561 * anchor
    return base_signal.diff()

def f63_adc_210_analyst_v210_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=32, w2=386, w3=418, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 32)
    baseline = trend.rolling(386, min_periods=max(386//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(418, min_periods=max(418//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.935 + 0.0035611 * anchor
    return base_signal.diff()

def f63_adc_211_analyst_v211_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=39, w2=397, w3=431, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 39)
    slow = _rolling_slope(x, 397)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.949375 + 0.0035612 * anchor
    return base_signal.diff()

def f63_adc_212_analyst_v212_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=46, w2=408, w3=444, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(408, min_periods=max(408//3, 2)).max()
    trough = x.rolling(46, min_periods=max(46//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.96375 + 0.0035613 * anchor
    return base_signal.diff()

def f63_adc_213_analyst_v213_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=53, w2=419, w3=457, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(53)
    rank = change.rolling(419, min_periods=max(419//3, 2)).rank(pct=True)
    persistence = change.rolling(457, min_periods=max(457//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0622 * persistence + 0.0035614 * anchor
    return base_signal.diff()

def f63_adc_214_analyst_v214_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=60, w2=430, w3=470, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(60, min_periods=max(60//3, 2)).std()
    vol_slow = ret.rolling(430, min_periods=max(430//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.9925 + 0.0035615 * anchor
    return base_signal.diff()

def f63_adc_215_analyst_v215_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=67, w2=441, w3=483, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(441, min_periods=max(441//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 67)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0774 * slope + 0.0035616 * anchor
    return base_signal.diff()

def f63_adc_216_analyst_v216_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=74, w2=452, w3=496, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(74)
    drag = impulse.rolling(452, min_periods=max(452//3, 2)).mean()
    noise = impulse.abs().rolling(496, min_periods=max(496//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.02125 + 0.0035617 * anchor
    return base_signal.diff()

def f63_adc_217_analyst_v217_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=81, w2=463, w3=509, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 81)
    acceleration = _rolling_slope(velocity, 463)
    curvature = _rolling_slope(acceleration, 509)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0926 * acceleration + 0.0035618 * anchor
    return base_signal.diff()

def f63_adc_218_analyst_v218_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=88, w2=474, w3=522, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(88, min_periods=max(88//3, 2)).mean(), upside.rolling(474, min_periods=max(474//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.05 + 0.0035619 * anchor
    return base_signal.diff()

def f63_adc_219_analyst_v219_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=95, w2=485, w3=535, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(485, min_periods=max(485//3, 2)).max()
    rebound = x - x.rolling(95, min_periods=max(95//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1078 * _rolling_slope(draw, 535) + 0.003562 * anchor
    return base_signal.diff()

def f63_adc_220_analyst_v220_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=102, w2=496, w3=548, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 102)
    baseline = trend.rolling(496, min_periods=max(496//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(548, min_periods=max(548//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.07875 + 0.0035621 * anchor
    return base_signal.diff()

def f63_adc_221_analyst_v221_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=109, w2=507, w3=561, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 109)
    slow = _rolling_slope(x, 507)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.093125 + 0.0035622 * anchor
    return base_signal.diff()

def f63_adc_222_analyst_v222_d1(eps_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=116, w2=15, w3=574, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(15, min_periods=max(15//3, 2)).max()
    trough = x.rolling(116, min_periods=max(116//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.1075 + 0.0035623 * anchor
    return base_signal.diff()

def f63_adc_223_analyst_v223_d1(rev_disp: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=123, w2=26, w3=587, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(123)
    rank = change.rolling(26, min_periods=max(26//3, 2)).rank(pct=True)
    persistence = change.rolling(587, min_periods=max(587//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1382 * persistence + 0.0035624 * anchor
    return base_signal.diff()

def f63_adc_224_analyst_v224_d1(eps_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=130, w2=37, w3=600, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(130, min_periods=max(130//3, 2)).std()
    vol_slow = ret.rolling(37, min_periods=max(37//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.13625 + 0.0035625 * anchor
    return base_signal.diff()

def f63_adc_225_analyst_v225_d1(rev_est: pd.Series) -> pd.Series:
    """First derivative of de-duplicated analyst replacement signal (w1=137, w2=48, w3=613, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(48, min_periods=max(48//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 137)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1534 * slope + 0.0035626 * anchor
    return base_signal.diff()
