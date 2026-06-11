"""82 days sales inventory acceleration d3 third derivative features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Operating_Efficiency - Institutional-grade short-side signal.
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

def f82_dsia_151_struct_v151_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=154, w2=164, w3=504, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 154)
    slow = _rolling_slope(x, 164)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.93125 + 0.0039752 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_152_struct_v152_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=161, w2=175, w3=517, lag=0)."""
    x = shortinterest.shift(0)
    peak = x.rolling(175, min_periods=max(175//3, 2)).max()
    trough = x.rolling(161, min_periods=max(161//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.945625 + 0.0039753 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_153_struct_v153_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=168, w2=186, w3=530, lag=1)."""
    x = utilization.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(186, min_periods=max(186//3, 2)).rank(pct=True)
    persistence = change.rolling(530, min_periods=max(530//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.285 * persistence + 0.0039754 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_154_struct_v154_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=175, w2=197, w3=543, lag=2)."""
    x = _safe_log(gex.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(175, min_periods=max(175//3, 2)).std()
    vol_slow = ret.rolling(197, min_periods=max(197//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.974375 + 0.0039755 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_155_struct_v155_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=182, w2=208, w3=556, lag=5)."""
    x = vex.shift(5)
    ma = x.rolling(208, min_periods=max(208//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 182)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3002 * slope + 0.0039756 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_156_struct_v156_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=189, w2=219, w3=569, lag=10)."""
    x = revenue.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(219, min_periods=max(219//3, 2)).mean()
    noise = impulse.abs().rolling(569, min_periods=max(569//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.003125 + 0.0039757 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_157_struct_v157_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=196, w2=230, w3=582, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 196)
    acceleration = _rolling_slope(velocity, 230)
    curvature = _rolling_slope(acceleration, 582)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3154 * acceleration + 0.0039758 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_158_struct_v158_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=203, w2=241, w3=595, lag=42)."""
    x = shortinterest.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(241, min_periods=max(241//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.031875 + 0.0039759 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_159_struct_v159_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=210, w2=252, w3=608, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    draw = x - x.rolling(252, min_periods=max(252//3, 2)).max()
    rebound = x - x.rolling(210, min_periods=max(210//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3306 * _rolling_slope(draw, 608) + 0.003976 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_160_struct_v160_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=217, w2=263, w3=621, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 217)
    baseline = trend.rolling(263, min_periods=max(263//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(621, min_periods=max(621//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.060625 + 0.0039761 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_161_struct_v161_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=224, w2=274, w3=634, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 224)
    slow = _rolling_slope(x, 274)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.075 + 0.0039762 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_162_struct_v162_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=231, w2=285, w3=647, lag=2)."""
    x = revenue.shift(2)
    peak = x.rolling(285, min_periods=max(285//3, 2)).max()
    trough = x.rolling(231, min_periods=max(231//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.089375 + 0.0039763 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_163_struct_v163_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=238, w2=296, w3=660, lag=5)."""
    x = netinc.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(296, min_periods=max(296//3, 2)).rank(pct=True)
    persistence = change.rolling(660, min_periods=max(660//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.361 * persistence + 0.0039764 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_164_struct_v164_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=245, w2=307, w3=673, lag=10)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(245, min_periods=max(245//3, 2)).std()
    vol_slow = ret.rolling(307, min_periods=max(307//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.118125 + 0.0039765 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_165_struct_v165_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=252, w2=318, w3=686, lag=21)."""
    x = utilization.shift(21)
    ma = x.rolling(318, min_periods=max(318//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 252)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3762 * slope + 0.0039766 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_166_struct_v166_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=8, w2=329, w3=699, lag=42)."""
    x = gex.shift(42)
    impulse = x.diff(8)
    drag = impulse.rolling(329, min_periods=max(329//3, 2)).mean()
    noise = impulse.abs().rolling(699, min_periods=max(699//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.146875 + 0.0039767 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_167_struct_v167_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=15, w2=340, w3=712, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 15)
    acceleration = _rolling_slope(velocity, 340)
    curvature = _rolling_slope(acceleration, 712)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3914 * acceleration + 0.0039768 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_168_struct_v168_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=22, w2=351, w3=725, lag=0)."""
    x = revenue.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(22, min_periods=max(22//3, 2)).mean(), upside.rolling(351, min_periods=max(351//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.175625 + 0.0039769 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_169_struct_v169_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=29, w2=362, w3=738, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    draw = x - x.rolling(362, min_periods=max(362//3, 2)).max()
    rebound = x - x.rolling(29, min_periods=max(29//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4066 * _rolling_slope(draw, 738) + 0.003977 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_170_struct_v170_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=36, w2=373, w3=751, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 36)
    baseline = trend.rolling(373, min_periods=max(373//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(751, min_periods=max(751//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.204375 + 0.0039771 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_171_struct_v171_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=43, w2=384, w3=764, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 43)
    slow = _rolling_slope(x, 384)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.21875 + 0.0039772 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_172_struct_v172_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=50, w2=395, w3=20, lag=10)."""
    x = gex.shift(10)
    peak = x.rolling(395, min_periods=max(395//3, 2)).max()
    trough = x.rolling(50, min_periods=max(50//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.233125 + 0.0039773 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_173_struct_v173_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=57, w2=406, w3=33, lag=21)."""
    x = vex.shift(21)
    change = x.pct_change(57)
    rank = change.rolling(406, min_periods=max(406//3, 2)).rank(pct=True)
    persistence = change.rolling(33, min_periods=max(33//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0606 * persistence + 0.0039774 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_174_struct_v174_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=64, w2=417, w3=46, lag=42)."""
    x = _safe_log(revenue.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(64, min_periods=max(64//3, 2)).std()
    vol_slow = ret.rolling(417, min_periods=max(417//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.261875 + 0.0039775 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_175_struct_v175_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=71, w2=428, w3=59, lag=63)."""
    x = netinc.shift(63)
    ma = x.rolling(428, min_periods=max(428//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 71)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0758 * slope + 0.0039776 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_176_struct_v176_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=78, w2=439, w3=72, lag=0)."""
    x = shortinterest.shift(0)
    impulse = x.diff(78)
    drag = impulse.rolling(439, min_periods=max(439//3, 2)).mean()
    noise = impulse.abs().rolling(72, min_periods=max(72//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.290625 + 0.0039777 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_177_struct_v177_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=85, w2=450, w3=85, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 85)
    acceleration = _rolling_slope(velocity, 450)
    curvature = _rolling_slope(acceleration, 85)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.091 * acceleration + 0.0039778 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_178_struct_v178_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=92, w2=461, w3=98, lag=2)."""
    x = gex.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(92, min_periods=max(92//3, 2)).mean(), upside.rolling(461, min_periods=max(461//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(98) * 1.319375 + 0.0039779 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_179_struct_v179_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=99, w2=472, w3=111, lag=5)."""
    x = _safe_log(vex.abs() + 1.0).shift(5)
    draw = x - x.rolling(472, min_periods=max(472//3, 2)).max()
    rebound = x - x.rolling(99, min_periods=max(99//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1062 * _rolling_slope(draw, 111) + 0.003978 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_180_struct_v180_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=106, w2=483, w3=124, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 106)
    baseline = trend.rolling(483, min_periods=max(483//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(124, min_periods=max(124//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.348125 + 0.0039781 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_181_struct_v181_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=113, w2=494, w3=137, lag=21)."""
    x = _safe_log(netinc.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 113)
    slow = _rolling_slope(x, 494)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=137, adjust=False).mean() * 1.3625 + 0.0039782 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_182_struct_v182_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=120, w2=505, w3=150, lag=42)."""
    x = shortinterest.shift(42)
    peak = x.rolling(505, min_periods=max(505//3, 2)).max()
    trough = x.rolling(120, min_periods=max(120//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.376875 + 0.0039783 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_183_struct_v183_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=127, w2=13, w3=163, lag=63)."""
    x = utilization.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(13, min_periods=max(13//3, 2)).rank(pct=True)
    persistence = change.rolling(163, min_periods=max(163//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1366 * persistence + 0.0039784 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_184_struct_v184_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=134, w2=24, w3=176, lag=0)."""
    x = _safe_log(gex.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(134, min_periods=max(134//3, 2)).std()
    vol_slow = ret.rolling(24, min_periods=max(24//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.405625 + 0.0039785 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_185_struct_v185_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=141, w2=35, w3=189, lag=1)."""
    x = vex.shift(1)
    ma = x.rolling(35, min_periods=max(35//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 141)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1518 * slope + 0.0039786 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_186_struct_v186_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=148, w2=46, w3=202, lag=2)."""
    x = revenue.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(46, min_periods=max(46//3, 2)).mean()
    noise = impulse.abs().rolling(202, min_periods=max(202//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.434375 + 0.0039787 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_187_struct_v187_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=155, w2=57, w3=215, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 155)
    acceleration = _rolling_slope(velocity, 57)
    curvature = _rolling_slope(acceleration, 215)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.167 * acceleration + 0.0039788 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_188_struct_v188_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=162, w2=68, w3=228, lag=10)."""
    x = shortinterest.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(162, min_periods=max(162//3, 2)).mean(), upside.rolling(68, min_periods=max(68//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.463125 + 0.0039789 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_189_struct_v189_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=169, w2=79, w3=241, lag=21)."""
    x = _safe_log(utilization.abs() + 1.0).shift(21)
    draw = x - x.rolling(79, min_periods=max(79//3, 2)).max()
    rebound = x - x.rolling(169, min_periods=max(169//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1822 * _rolling_slope(draw, 241) + 0.003979 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_190_struct_v190_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=176, w2=90, w3=254, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 176)
    baseline = trend.rolling(90, min_periods=max(90//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(254, min_periods=max(254//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.491875 + 0.0039791 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_191_struct_v191_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=183, w2=101, w3=267, lag=63)."""
    x = _safe_log(vex.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 183)
    slow = _rolling_slope(x, 101)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=267, adjust=False).mean() * 1.50625 + 0.0039792 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_192_struct_v192_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=190, w2=112, w3=280, lag=0)."""
    x = revenue.shift(0)
    peak = x.rolling(112, min_periods=max(112//3, 2)).max()
    trough = x.rolling(190, min_periods=max(190//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.520625 + 0.0039793 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_193_struct_v193_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=197, w2=123, w3=293, lag=1)."""
    x = netinc.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(123, min_periods=max(123//3, 2)).rank(pct=True)
    persistence = change.rolling(293, min_periods=max(293//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2126 * persistence + 0.0039794 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_194_struct_v194_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=204, w2=134, w3=306, lag=2)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(204, min_periods=max(204//3, 2)).std()
    vol_slow = ret.rolling(134, min_periods=max(134//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.549375 + 0.0039795 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_195_struct_v195_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=211, w2=145, w3=319, lag=5)."""
    x = utilization.shift(5)
    ma = x.rolling(145, min_periods=max(145//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 211)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2278 * slope + 0.0039796 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_196_struct_v196_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=218, w2=156, w3=332, lag=10)."""
    x = gex.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(156, min_periods=max(156//3, 2)).mean()
    noise = impulse.abs().rolling(332, min_periods=max(332//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.578125 + 0.0039797 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_197_struct_v197_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=225, w2=167, w3=345, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 225)
    acceleration = _rolling_slope(velocity, 167)
    curvature = _rolling_slope(acceleration, 345)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.243 * acceleration + 0.0039798 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_198_struct_v198_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=232, w2=178, w3=358, lag=42)."""
    x = revenue.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(232, min_periods=max(232//3, 2)).mean(), upside.rolling(178, min_periods=max(178//3, 2)).mean().abs())
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.606875 + 0.0039799 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_199_struct_v199_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=239, w2=189, w3=371, lag=63)."""
    x = _safe_log(netinc.abs() + 1.0).shift(63)
    draw = x - x.rolling(189, min_periods=max(189//3, 2)).max()
    rebound = x - x.rolling(239, min_periods=max(239//3, 2)).min()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2582 * _rolling_slope(draw, 371) + 0.00398 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_200_struct_v200_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=246, w2=200, w3=384, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 246)
    baseline = trend.rolling(200, min_periods=max(200//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(384, min_periods=max(384//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.8625 + 0.0039801 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_201_struct_v201_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=253, w2=211, w3=397, lag=1)."""
    x = _safe_log(utilization.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 253)
    slow = _rolling_slope(x, 211)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.876875 + 0.0039802 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_202_struct_v202_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=9, w2=222, w3=410, lag=2)."""
    x = gex.shift(2)
    peak = x.rolling(222, min_periods=max(222//3, 2)).max()
    trough = x.rolling(9, min_periods=max(9//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.89125 + 0.0039803 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_203_struct_v203_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=16, w2=233, w3=423, lag=5)."""
    x = vex.shift(5)
    change = x.pct_change(16)
    rank = change.rolling(233, min_periods=max(233//3, 2)).rank(pct=True)
    persistence = change.rolling(423, min_periods=max(423//3, 2)).mean()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.2886 * persistence + 0.0039804 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_204_struct_v204_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=23, w2=244, w3=436, lag=10)."""
    x = _safe_log(revenue.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(23, min_periods=max(23//3, 2)).std()
    vol_slow = ret.rolling(244, min_periods=max(244//3, 2)).std()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.92 + 0.0039805 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_205_struct_v205_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=30, w2=255, w3=449, lag=21)."""
    x = netinc.shift(21)
    ma = x.rolling(255, min_periods=max(255//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 30)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3038 * slope + 0.0039806 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_206_struct_v206_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=37, w2=266, w3=462, lag=42)."""
    x = shortinterest.shift(42)
    impulse = x.diff(37)
    drag = impulse.rolling(266, min_periods=max(266//3, 2)).mean()
    noise = impulse.abs().rolling(462, min_periods=max(462//3, 2)).mean()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.94875 + 0.0039807 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_207_struct_v207_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=44, w2=277, w3=475, lag=63)."""
    x = _safe_log(utilization.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 44)
    acceleration = _rolling_slope(velocity, 277)
    curvature = _rolling_slope(acceleration, 475)
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.319 * acceleration + 0.0039808 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_208_struct_v208_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=51, w2=288, w3=488, lag=0)."""
    x = gex.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(51, min_periods=max(51//3, 2)).mean(), upside.rolling(288, min_periods=max(288//3, 2)).mean().abs())
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9775 + 0.0039809 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_209_struct_v209_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=58, w2=299, w3=501, lag=1)."""
    x = _safe_log(vex.abs() + 1.0).shift(1)
    draw = x - x.rolling(299, min_periods=max(299//3, 2)).max()
    rebound = x - x.rolling(58, min_periods=max(58//3, 2)).min()
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3342 * _rolling_slope(draw, 501) + 0.003981 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_210_struct_v210_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=65, w2=310, w3=514, lag=2)."""
    x = _safe_log(revenue.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 65)
    baseline = trend.rolling(310, min_periods=max(310//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(514, min_periods=max(514//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.00625 + 0.0039811 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_211_struct_v211_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=72, w2=321, w3=527, lag=5)."""
    x = _safe_log(netinc.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 72)
    slow = _rolling_slope(x, 321)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.020625 + 0.0039812 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_212_struct_v212_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=79, w2=332, w3=540, lag=10)."""
    x = shortinterest.shift(10)
    peak = x.rolling(332, min_periods=max(332//3, 2)).max()
    trough = x.rolling(79, min_periods=max(79//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.035 + 0.0039813 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_213_struct_v213_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=86, w2=343, w3=553, lag=21)."""
    x = utilization.shift(21)
    change = x.pct_change(86)
    rank = change.rolling(343, min_periods=max(343//3, 2)).rank(pct=True)
    persistence = change.rolling(553, min_periods=max(553//3, 2)).mean()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3646 * persistence + 0.0039814 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_214_struct_v214_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=93, w2=354, w3=566, lag=42)."""
    x = _safe_log(gex.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(93, min_periods=max(93//3, 2)).std()
    vol_slow = ret.rolling(354, min_periods=max(354//3, 2)).std()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.06375 + 0.0039815 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_215_struct_v215_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=100, w2=365, w3=579, lag=63)."""
    x = vex.shift(63)
    ma = x.rolling(365, min_periods=max(365//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 100)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3798 * slope + 0.0039816 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_216_struct_v216_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=107, w2=376, w3=592, lag=0)."""
    x = revenue.shift(0)
    impulse = x.diff(107)
    drag = impulse.rolling(376, min_periods=max(376//3, 2)).mean()
    noise = impulse.abs().rolling(592, min_periods=max(592//3, 2)).mean()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0925 + 0.0039817 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_217_struct_v217_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=114, w2=387, w3=605, lag=1)."""
    x = _safe_log(netinc.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 114)
    acceleration = _rolling_slope(velocity, 387)
    curvature = _rolling_slope(acceleration, 605)
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.395 * acceleration + 0.0039818 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_218_struct_v218_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=121, w2=398, w3=618, lag=2)."""
    x = shortinterest.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(121, min_periods=max(121//3, 2)).mean(), upside.rolling(398, min_periods=max(398//3, 2)).mean().abs())
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.12125 + 0.0039819 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_219_struct_v219_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=128, w2=409, w3=631, lag=5)."""
    x = _safe_log(utilization.abs() + 1.0).shift(5)
    draw = x - x.rolling(409, min_periods=max(409//3, 2)).max()
    rebound = x - x.rolling(128, min_periods=max(128//3, 2)).min()
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.4102 * _rolling_slope(draw, 631) + 0.003982 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_220_struct_v220_d3(gex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=135, w2=420, w3=644, lag=10)."""
    x = _safe_log(gex.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 135)
    baseline = trend.rolling(420, min_periods=max(420//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(644, min_periods=max(644//3, 2)).mean()
    anchor = _safe_log(gex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.15 + 0.0039821 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_221_struct_v221_d3(vex: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=142, w2=431, w3=657, lag=21)."""
    x = _safe_log(vex.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 431)
    anchor = _safe_log(vex.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.164375 + 0.0039822 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_222_struct_v222_d3(revenue: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=149, w2=442, w3=670, lag=42)."""
    x = revenue.shift(42)
    peak = x.rolling(442, min_periods=max(442//3, 2)).max()
    trough = x.rolling(149, min_periods=max(149//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(revenue.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.17875 + 0.0039823 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_223_struct_v223_d3(netinc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=156, w2=453, w3=683, lag=63)."""
    x = netinc.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(453, min_periods=max(453//3, 2)).rank(pct=True)
    persistence = change.rolling(683, min_periods=max(683//3, 2)).mean()
    anchor = _safe_log(netinc.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0642 * persistence + 0.0039824 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_224_struct_v224_d3(shortinterest: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=163, w2=464, w3=696, lag=0)."""
    x = _safe_log(shortinterest.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(163, min_periods=max(163//3, 2)).std()
    vol_slow = ret.rolling(464, min_periods=max(464//3, 2)).std()
    anchor = _safe_log(shortinterest.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.2075 + 0.0039825 * anchor
    return base_signal.diff().diff().diff()

def f82_dsia_225_struct_v225_d3(utilization: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated struct replacement signal (w1=170, w2=475, w3=709, lag=1)."""
    x = utilization.shift(1)
    ma = x.rolling(475, min_periods=max(475//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(utilization.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.0794 * slope + 0.0039826 * anchor
    return base_signal.diff().diff().diff()
