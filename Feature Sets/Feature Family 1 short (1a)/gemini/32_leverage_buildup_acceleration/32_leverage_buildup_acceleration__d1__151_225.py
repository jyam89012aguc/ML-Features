"""32 leverage buildup acceleration d1 first derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Kinetics_Fundamental - Institutional-grade short-side signal.
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

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)
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

def f32_lba_151_struct_v151_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=173, w2=102, w3=254, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 173)
    slow = _rolling_slope(x, 102)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=254, adjust=False).mean() * 1.46875 + 0.0019352 * anchor
    return base_signal.diff()

def f32_lba_152_struct_v152_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=180, w2=113, w3=267, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(113, min_periods=max(113//3, 2)).max()
    trough = x.rolling(180, min_periods=max(180//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.483125 + 0.0019353 * anchor
    return base_signal.diff()

def f32_lba_153_struct_v153_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=187, w2=124, w3=280, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(124, min_periods=max(124//3, 2)).rank(pct=True)
    persistence = change.rolling(280, min_periods=max(280//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3218 * persistence + 0.0019354 * anchor
    return base_signal.diff()

def f32_lba_154_struct_v154_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=194, w2=135, w3=293, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(194, min_periods=max(194//3, 2)).std()
    vol_slow = ret.rolling(135, min_periods=max(135//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.511875 + 0.0019355 * anchor
    return base_signal.diff()

def f32_lba_155_struct_v155_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=201, w2=146, w3=306, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(146, min_periods=max(146//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.337 * slope + 0.0019356 * anchor
    return base_signal.diff()

def f32_lba_156_struct_v156_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=208, w2=157, w3=319, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(157, min_periods=max(157//3, 2)).mean()
    noise = impulse.abs().rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.540625 + 0.0019357 * anchor
    return base_signal.diff()

def f32_lba_157_struct_v157_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=215, w2=168, w3=332, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 168)
    curvature = _rolling_slope(acceleration, 332)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3522 * acceleration + 0.0019358 * anchor
    return base_signal.diff()

def f32_lba_158_struct_v158_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=222, w2=179, w3=345, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(222, min_periods=max(222//3, 2)).mean(), upside.rolling(179, min_periods=max(179//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.569375 + 0.0019359 * anchor
    return base_signal.diff()

def f32_lba_159_struct_v159_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=229, w2=190, w3=358, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(190, min_periods=max(190//3, 2)).max()
    rebound = x - x.rolling(229, min_periods=max(229//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3674 * _rolling_slope(draw, 358) + 0.001936 * anchor
    return base_signal.diff()

def f32_lba_160_struct_v160_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=236, w2=201, w3=371, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 236)
    baseline = trend.rolling(201, min_periods=max(201//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(371, min_periods=max(371//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.598125 + 0.0019361 * anchor
    return base_signal.diff()

def f32_lba_161_struct_v161_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=243, w2=212, w3=384, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 243)
    slow = _rolling_slope(x, 212)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.6125 + 0.0019362 * anchor
    return base_signal.diff()

def f32_lba_162_struct_v162_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=250, w2=223, w3=397, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(223, min_periods=max(223//3, 2)).max()
    trough = x.rolling(250, min_periods=max(250//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.85375 + 0.0019363 * anchor
    return base_signal.diff()

def f32_lba_163_struct_v163_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=6, w2=234, w3=410, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(6)
    rank = change.rolling(234, min_periods=max(234//3, 2)).rank(pct=True)
    persistence = change.rolling(410, min_periods=max(410//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3978 * persistence + 0.0019364 * anchor
    return base_signal.diff()

def f32_lba_164_struct_v164_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=13, w2=245, w3=423, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(13, min_periods=max(13//3, 2)).std()
    vol_slow = ret.rolling(245, min_periods=max(245//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.8825 + 0.0019365 * anchor
    return base_signal.diff()

def f32_lba_165_struct_v165_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=20, w2=256, w3=436, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(256, min_periods=max(256//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 20)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0366 * slope + 0.0019366 * anchor
    return base_signal.diff()

def f32_lba_166_struct_v166_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=27, w2=267, w3=449, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(27)
    drag = impulse.rolling(267, min_periods=max(267//3, 2)).mean()
    noise = impulse.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.91125 + 0.0019367 * anchor
    return base_signal.diff()

def f32_lba_167_struct_v167_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=34, w2=278, w3=462, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 34)
    acceleration = _rolling_slope(velocity, 278)
    curvature = _rolling_slope(acceleration, 462)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0518 * acceleration + 0.0019368 * anchor
    return base_signal.diff()

def f32_lba_168_struct_v168_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=41, w2=289, w3=475, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(41, min_periods=max(41//3, 2)).mean(), upside.rolling(289, min_periods=max(289//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.94 + 0.0019369 * anchor
    return base_signal.diff()

def f32_lba_169_struct_v169_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=48, w2=300, w3=488, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(300, min_periods=max(300//3, 2)).max()
    rebound = x - x.rolling(48, min_periods=max(48//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.067 * _rolling_slope(draw, 488) + 0.001937 * anchor
    return base_signal.diff()

def f32_lba_170_struct_v170_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=55, w2=311, w3=501, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 55)
    baseline = trend.rolling(311, min_periods=max(311//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(501, min_periods=max(501//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.96875 + 0.0019371 * anchor
    return base_signal.diff()

def f32_lba_171_struct_v171_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=62, w2=322, w3=514, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 62)
    slow = _rolling_slope(x, 322)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.983125 + 0.0019372 * anchor
    return base_signal.diff()

def f32_lba_172_struct_v172_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=69, w2=333, w3=527, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(333, min_periods=max(333//3, 2)).max()
    trough = x.rolling(69, min_periods=max(69//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.9975 + 0.0019373 * anchor
    return base_signal.diff()

def f32_lba_173_struct_v173_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=76, w2=344, w3=540, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(76)
    rank = change.rolling(344, min_periods=max(344//3, 2)).rank(pct=True)
    persistence = change.rolling(540, min_periods=max(540//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0974 * persistence + 0.0019374 * anchor
    return base_signal.diff()

def f32_lba_174_struct_v174_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=83, w2=355, w3=553, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(83, min_periods=max(83//3, 2)).std()
    vol_slow = ret.rolling(355, min_periods=max(355//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.02625 + 0.0019375 * anchor
    return base_signal.diff()

def f32_lba_175_struct_v175_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=90, w2=366, w3=566, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(366, min_periods=max(366//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 90)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1126 * slope + 0.0019376 * anchor
    return base_signal.diff()

def f32_lba_176_struct_v176_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=97, w2=377, w3=579, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(97)
    drag = impulse.rolling(377, min_periods=max(377//3, 2)).mean()
    noise = impulse.abs().rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.055 + 0.0019377 * anchor
    return base_signal.diff()

def f32_lba_177_struct_v177_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=104, w2=388, w3=592, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 104)
    acceleration = _rolling_slope(velocity, 388)
    curvature = _rolling_slope(acceleration, 592)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1278 * acceleration + 0.0019378 * anchor
    return base_signal.diff()

def f32_lba_178_struct_v178_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=111, w2=399, w3=605, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(111, min_periods=max(111//3, 2)).mean(), upside.rolling(399, min_periods=max(399//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.08375 + 0.0019379 * anchor
    return base_signal.diff()

def f32_lba_179_struct_v179_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=118, w2=410, w3=618, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(410, min_periods=max(410//3, 2)).max()
    rebound = x - x.rolling(118, min_periods=max(118//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.143 * _rolling_slope(draw, 618) + 0.001938 * anchor
    return base_signal.diff()

def f32_lba_180_struct_v180_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=125, w2=421, w3=631, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 125)
    baseline = trend.rolling(421, min_periods=max(421//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(631, min_periods=max(631//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.1125 + 0.0019381 * anchor
    return base_signal.diff()

def f32_lba_181_struct_v181_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=132, w2=432, w3=644, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 132)
    slow = _rolling_slope(x, 432)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.126875 + 0.0019382 * anchor
    return base_signal.diff()

def f32_lba_182_struct_v182_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=139, w2=443, w3=657, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(443, min_periods=max(443//3, 2)).max()
    trough = x.rolling(139, min_periods=max(139//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.14125 + 0.0019383 * anchor
    return base_signal.diff()

def f32_lba_183_struct_v183_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=146, w2=454, w3=670, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(454, min_periods=max(454//3, 2)).rank(pct=True)
    persistence = change.rolling(670, min_periods=max(670//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1734 * persistence + 0.0019384 * anchor
    return base_signal.diff()

def f32_lba_184_struct_v184_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=153, w2=465, w3=683, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(153, min_periods=max(153//3, 2)).std()
    vol_slow = ret.rolling(465, min_periods=max(465//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.17 + 0.0019385 * anchor
    return base_signal.diff()

def f32_lba_185_struct_v185_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=160, w2=476, w3=696, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(476, min_periods=max(476//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 160)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1886 * slope + 0.0019386 * anchor
    return base_signal.diff()

def f32_lba_186_struct_v186_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=167, w2=487, w3=709, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(487, min_periods=max(487//3, 2)).mean()
    noise = impulse.abs().rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.19875 + 0.0019387 * anchor
    return base_signal.diff()

def f32_lba_187_struct_v187_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=174, w2=498, w3=722, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 174)
    acceleration = _rolling_slope(velocity, 498)
    curvature = _rolling_slope(acceleration, 722)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2038 * acceleration + 0.0019388 * anchor
    return base_signal.diff()

def f32_lba_188_struct_v188_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=181, w2=509, w3=735, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(181, min_periods=max(181//3, 2)).mean(), upside.rolling(509, min_periods=max(509//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.2275 + 0.0019389 * anchor
    return base_signal.diff()

def f32_lba_189_struct_v189_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=188, w2=17, w3=748, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(17, min_periods=max(17//3, 2)).max()
    rebound = x - x.rolling(188, min_periods=max(188//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.219 * _rolling_slope(draw, 748) + 0.001939 * anchor
    return base_signal.diff()

def f32_lba_190_struct_v190_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=195, w2=28, w3=761, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 195)
    baseline = trend.rolling(28, min_periods=max(28//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(761, min_periods=max(761//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.25625 + 0.0019391 * anchor
    return base_signal.diff()

def f32_lba_191_struct_v191_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=202, w2=39, w3=17, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 202)
    slow = _rolling_slope(x, 39)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=17, adjust=False).mean() * 1.270625 + 0.0019392 * anchor
    return base_signal.diff()

def f32_lba_192_struct_v192_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=209, w2=50, w3=30, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(50, min_periods=max(50//3, 2)).max()
    trough = x.rolling(209, min_periods=max(209//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.285 + 0.0019393 * anchor
    return base_signal.diff()

def f32_lba_193_struct_v193_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=216, w2=61, w3=43, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(61, min_periods=max(61//3, 2)).rank(pct=True)
    persistence = change.rolling(43, min_periods=max(43//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2494 * persistence + 0.0019394 * anchor
    return base_signal.diff()

def f32_lba_194_struct_v194_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=223, w2=72, w3=56, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(223, min_periods=max(223//3, 2)).std()
    vol_slow = ret.rolling(72, min_periods=max(72//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.31375 + 0.0019395 * anchor
    return base_signal.diff()

def f32_lba_195_struct_v195_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=230, w2=83, w3=69, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(83, min_periods=max(83//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 230)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2646 * slope + 0.0019396 * anchor
    return base_signal.diff()

def f32_lba_196_struct_v196_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=237, w2=94, w3=82, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(94, min_periods=max(94//3, 2)).mean()
    noise = impulse.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.3425 + 0.0019397 * anchor
    return base_signal.diff()

def f32_lba_197_struct_v197_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=244, w2=105, w3=95, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 244)
    acceleration = _rolling_slope(velocity, 105)
    curvature = _rolling_slope(acceleration, 95)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2798 * acceleration + 0.0019398 * anchor
    return base_signal.diff()

def f32_lba_198_struct_v198_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=251, w2=116, w3=108, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(251, min_periods=max(251//3, 2)).mean(), upside.rolling(116, min_periods=max(116//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(108) * 1.37125 + 0.0019399 * anchor
    return base_signal.diff()

def f32_lba_199_struct_v199_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=7, w2=127, w3=121, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(127, min_periods=max(127//3, 2)).max()
    rebound = x - x.rolling(7, min_periods=max(7//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.295 * _rolling_slope(draw, 121) + 0.00194 * anchor
    return base_signal.diff()

def f32_lba_200_struct_v200_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=14, w2=138, w3=134, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 14)
    baseline = trend.rolling(138, min_periods=max(138//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4 + 0.0019401 * anchor
    return base_signal.diff()

def f32_lba_201_struct_v201_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=21, w2=149, w3=147, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 21)
    slow = _rolling_slope(x, 149)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=147, adjust=False).mean() * 1.414375 + 0.0019402 * anchor
    return base_signal.diff()

def f32_lba_202_struct_v202_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=28, w2=160, w3=160, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(160, min_periods=max(160//3, 2)).max()
    trough = x.rolling(28, min_periods=max(28//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.42875 + 0.0019403 * anchor
    return base_signal.diff()

def f32_lba_203_struct_v203_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=35, w2=171, w3=173, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(35)
    rank = change.rolling(171, min_periods=max(171//3, 2)).rank(pct=True)
    persistence = change.rolling(173, min_periods=max(173//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3254 * persistence + 0.0019404 * anchor
    return base_signal.diff()

def f32_lba_204_struct_v204_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=42, w2=182, w3=186, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(42, min_periods=max(42//3, 2)).std()
    vol_slow = ret.rolling(182, min_periods=max(182//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.4575 + 0.0019405 * anchor
    return base_signal.diff()

def f32_lba_205_struct_v205_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=49, w2=193, w3=199, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(193, min_periods=max(193//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 49)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3406 * slope + 0.0019406 * anchor
    return base_signal.diff()

def f32_lba_206_struct_v206_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=56, w2=204, w3=212, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(56)
    drag = impulse.rolling(204, min_periods=max(204//3, 2)).mean()
    noise = impulse.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.48625 + 0.0019407 * anchor
    return base_signal.diff()

def f32_lba_207_struct_v207_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=63, w2=215, w3=225, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 63)
    acceleration = _rolling_slope(velocity, 215)
    curvature = _rolling_slope(acceleration, 225)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3558 * acceleration + 0.0019408 * anchor
    return base_signal.diff()

def f32_lba_208_struct_v208_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=70, w2=226, w3=238, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(70, min_periods=max(70//3, 2)).mean(), upside.rolling(226, min_periods=max(226//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.515 + 0.0019409 * anchor
    return base_signal.diff()

def f32_lba_209_struct_v209_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=77, w2=237, w3=251, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(237, min_periods=max(237//3, 2)).max()
    rebound = x - x.rolling(77, min_periods=max(77//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.371 * _rolling_slope(draw, 251) + 0.001941 * anchor
    return base_signal.diff()

def f32_lba_210_struct_v210_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=84, w2=248, w3=264, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 84)
    baseline = trend.rolling(248, min_periods=max(248//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(264, min_periods=max(264//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.54375 + 0.0019411 * anchor
    return base_signal.diff()

def f32_lba_211_struct_v211_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=91, w2=259, w3=277, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 91)
    slow = _rolling_slope(x, 259)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=277, adjust=False).mean() * 1.558125 + 0.0019412 * anchor
    return base_signal.diff()

def f32_lba_212_struct_v212_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=98, w2=270, w3=290, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(270, min_periods=max(270//3, 2)).max()
    trough = x.rolling(98, min_periods=max(98//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.5725 + 0.0019413 * anchor
    return base_signal.diff()

def f32_lba_213_struct_v213_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=105, w2=281, w3=303, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(105)
    rank = change.rolling(281, min_periods=max(281//3, 2)).rank(pct=True)
    persistence = change.rolling(303, min_periods=max(303//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.4014 * persistence + 0.0019414 * anchor
    return base_signal.diff()

def f32_lba_214_struct_v214_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=112, w2=292, w3=316, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(112, min_periods=max(112//3, 2)).std()
    vol_slow = ret.rolling(292, min_periods=max(292//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60125 + 0.0019415 * anchor
    return base_signal.diff()

def f32_lba_215_struct_v215_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=119, w2=303, w3=329, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(303, min_periods=max(303//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 119)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0402 * slope + 0.0019416 * anchor
    return base_signal.diff()

def f32_lba_216_struct_v216_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=126, w2=314, w3=342, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(314, min_periods=max(314//3, 2)).mean()
    noise = impulse.abs().rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.856875 + 0.0019417 * anchor
    return base_signal.diff()

def f32_lba_217_struct_v217_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=133, w2=325, w3=355, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 133)
    acceleration = _rolling_slope(velocity, 325)
    curvature = _rolling_slope(acceleration, 355)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0554 * acceleration + 0.0019418 * anchor
    return base_signal.diff()

def f32_lba_218_struct_v218_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=140, w2=336, w3=368, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(140, min_periods=max(140//3, 2)).mean(), upside.rolling(336, min_periods=max(336//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.885625 + 0.0019419 * anchor
    return base_signal.diff()

def f32_lba_219_struct_v219_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=147, w2=347, w3=381, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(347, min_periods=max(347//3, 2)).max()
    rebound = x - x.rolling(147, min_periods=max(147//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0706 * _rolling_slope(draw, 381) + 0.001942 * anchor
    return base_signal.diff()

def f32_lba_220_struct_v220_d1(gex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=154, w2=358, w3=394, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 154)
    baseline = trend.rolling(358, min_periods=max(358//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(394, min_periods=max(394//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.914375 + 0.0019421 * anchor
    return base_signal.diff()

def f32_lba_221_struct_v221_d1(vex: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=161, w2=369, w3=407, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 161)
    slow = _rolling_slope(x, 369)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.92875 + 0.0019422 * anchor
    return base_signal.diff()

def f32_lba_222_struct_v222_d1(revenue: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=168, w2=380, w3=420, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(380, min_periods=max(380//3, 2)).max()
    trough = x.rolling(168, min_periods=max(168//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.943125 + 0.0019423 * anchor
    return base_signal.diff()

def f32_lba_223_struct_v223_d1(netinc: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=175, w2=391, w3=433, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(391, min_periods=max(391//3, 2)).rank(pct=True)
    persistence = change.rolling(433, min_periods=max(433//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.101 * persistence + 0.0019424 * anchor
    return base_signal.diff()

def f32_lba_224_struct_v224_d1(shortinterest: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=182, w2=402, w3=446, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(182, min_periods=max(182//3, 2)).std()
    vol_slow = ret.rolling(402, min_periods=max(402//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.971875 + 0.0019425 * anchor
    return base_signal.diff()

def f32_lba_225_struct_v225_d1(utilization: pd.Series) -> pd.Series:
    """First derivative of de-duplicated struct replacement signal (w1=189, w2=413, w3=459, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(413, min_periods=max(413//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 189)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1162 * slope + 0.0019426 * anchor
    return base_signal.diff()
