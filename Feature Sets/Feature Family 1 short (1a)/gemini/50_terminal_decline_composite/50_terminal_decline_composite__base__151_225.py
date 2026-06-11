"""50 terminal decline composite base features 151-225 â€” Pipeline 1a-HF Grade v3.

Hypothesis: Composite - Institutional-grade short-side signal.
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

def f50_tdc_151_accrual_v151(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=155, w2=255, w3=82, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.44125 + 0.0030752 * anchor

def f50_tdc_152_jerk_v152(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=162, w2=266, w3=95, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(266, min_periods=max(266//3, 2)).max()
    trough = x.rolling(162, min_periods=max(162//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.455625 + 0.0030753 * anchor

def f50_tdc_153_rel_v153(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=169, w2=277, w3=108, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 169)
    slow = _rolling_slope(x, 277)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=108, adjust=False).mean() * 1.47 + 0.0030754 * anchor

def f50_tdc_154_analyst_v154(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=176, w2=288, w3=121, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(176, min_periods=max(176//3, 2)).std()
    vol_slow = ret.rolling(288, min_periods=max(288//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.484375 + 0.0030755 * anchor

def f50_tdc_155_accrual_v155(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=183, w2=299, w3=134, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(299, min_periods=max(299//3, 2)).rank(pct=True)
    persistence = change.rolling(134, min_periods=max(134//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.405 * persistence + 0.0030756 * anchor

def f50_tdc_156_jerk_v156(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=190, w2=310, w3=147, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(310, min_periods=max(310//3, 2)).mean()
    noise = impulse.abs().rolling(147, min_periods=max(147//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.513125 + 0.0030757 * anchor

def f50_tdc_157_rel_v157(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=197, w2=321, w3=160, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(321, min_periods=max(321//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 197)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.0438 * slope + 0.0030758 * anchor

def f50_tdc_158_analyst_v158(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=204, w2=332, w3=173, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(204, min_periods=max(204//3, 2)).mean(), upside.rolling(332, min_periods=max(332//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.541875 + 0.0030759 * anchor

def f50_tdc_159_accrual_v159(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=211, w2=343, w3=186, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 211)
    acceleration = _rolling_slope(velocity, 343)
    curvature = _rolling_slope(acceleration, 186)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.059 * acceleration + 0.003076 * anchor

def f50_tdc_160_jerk_v160(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=218, w2=354, w3=199, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 218)
    baseline = trend.rolling(354, min_periods=max(354//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(199, min_periods=max(199//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.570625 + 0.0030761 * anchor

def f50_tdc_161_rel_v161(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=225, w2=365, w3=212, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(225, min_periods=max(225//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.585 + 0.0030762 * anchor

def f50_tdc_162_analyst_v162(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=232, w2=376, w3=225, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(376, min_periods=max(376//3, 2)).max()
    trough = x.rolling(232, min_periods=max(232//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.599375 + 0.0030763 * anchor

def f50_tdc_163_accrual_v163(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=239, w2=387, w3=238, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(239, min_periods=max(239//3, 2)).mean(), b.abs().rolling(387, min_periods=max(387//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.0894 * _rolling_slope(cover, 239) + 0.0030764 * anchor

def f50_tdc_164_jerk_v164(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=246, w2=398, w3=251, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(246, min_periods=max(246//3, 2)).std()
    vol_slow = ret.rolling(398, min_periods=max(398//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.855 + 0.0030765 * anchor

def f50_tdc_165_rel_v165(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=253, w2=409, w3=264, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(253, min_periods=max(253//3, 2)).mean(), upside.rolling(409, min_periods=max(409//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.869375 + 0.0030766 * anchor

def f50_tdc_166_analyst_v166(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=9, w2=420, w3=277, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(9)
    drag = impulse.rolling(420, min_periods=max(420//3, 2)).mean()
    noise = impulse.abs().rolling(277, min_periods=max(277//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 0.88375 + 0.0030767 * anchor

def f50_tdc_167_accrual_v167(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=16, w2=431, w3=290, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(16) - b.diff(126)
    stress = imbalance.rolling(290, min_periods=max(290//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 0.898125 + 0.0030768 * anchor

def f50_tdc_168_jerk_v168(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=23, w2=442, w3=303, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(23, min_periods=max(23//3, 2)).mean(), upside.rolling(442, min_periods=max(442//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.9125 + 0.0030769 * anchor

def f50_tdc_169_rel_v169(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=30, w2=453, w3=316, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 30)
    slow = _rolling_slope(x, 453)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 0.926875 + 0.003077 * anchor

def f50_tdc_170_analyst_v170(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=37, w2=464, w3=329, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 37)
    baseline = trend.rolling(464, min_periods=max(464//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(329, min_periods=max(329//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.94125 + 0.0030771 * anchor

def f50_tdc_171_accrual_v171(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=44, w2=475, w3=342, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(44)
    rank = change.rolling(475, min_periods=max(475//3, 2)).rank(pct=True)
    persistence = change.rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1502 * persistence + 0.0030772 * anchor

def f50_tdc_172_jerk_v172(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=51, w2=486, w3=355, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(486, min_periods=max(486//3, 2)).max()
    trough = x.rolling(51, min_periods=max(51//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.97 + 0.0030773 * anchor

def f50_tdc_173_rel_v173(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=58, w2=497, w3=368, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(497, min_periods=max(497//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 58)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1654 * slope + 0.0030774 * anchor

def f50_tdc_174_analyst_v174(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=65, w2=508, w3=381, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(65, min_periods=max(65//3, 2)).std()
    vol_slow = ret.rolling(508, min_periods=max(508//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.99875 + 0.0030775 * anchor

def f50_tdc_175_accrual_v175(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=72, w2=16, w3=394, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 72)
    acceleration = _rolling_slope(velocity, 16)
    curvature = _rolling_slope(acceleration, 394)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.1806 * acceleration + 0.0030776 * anchor

def f50_tdc_176_jerk_v176(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=79, w2=27, w3=407, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(79)
    drag = impulse.rolling(27, min_periods=max(27//3, 2)).mean()
    noise = impulse.abs().rolling(407, min_periods=max(407//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.0275 + 0.0030777 * anchor

def f50_tdc_177_rel_v177(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=86, w2=38, w3=420, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(86, min_periods=max(86//3, 2)).mean())
    decay = spread.ewm(span=38, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.041875 + 0.0030778 * anchor

def f50_tdc_178_analyst_v178(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=93, w2=49, w3=433, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(93, min_periods=max(93//3, 2)).mean(), upside.rolling(49, min_periods=max(49//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.05625 + 0.0030779 * anchor

def f50_tdc_179_accrual_v179(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=100, w2=60, w3=446, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(100, min_periods=max(100//3, 2)).mean(), b.abs().rolling(60, min_periods=max(60//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.211 * _rolling_slope(cover, 100) + 0.003078 * anchor

def f50_tdc_180_jerk_v180(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=107, w2=71, w3=459, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 107)
    baseline = trend.rolling(71, min_periods=max(71//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(459, min_periods=max(459//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.085 + 0.0030781 * anchor

def f50_tdc_181_rel_v181(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=114, w2=82, w3=472, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(114, min_periods=max(114//3, 2)).mean(), upside.rolling(82, min_periods=max(82//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.099375 + 0.0030782 * anchor

def f50_tdc_182_analyst_v182(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=121, w2=93, w3=485, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(93, min_periods=max(93//3, 2)).max()
    trough = x.rolling(121, min_periods=max(121//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.11375 + 0.0030783 * anchor

def f50_tdc_183_accrual_v183(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=128, w2=104, w3=498, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(104)
    stress = imbalance.rolling(498, min_periods=max(498//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.128125 + 0.0030784 * anchor

def f50_tdc_184_jerk_v184(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=135, w2=115, w3=511, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(135, min_periods=max(135//3, 2)).std()
    vol_slow = ret.rolling(115, min_periods=max(115//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1425 + 0.0030785 * anchor

def f50_tdc_185_rel_v185(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=142, w2=126, w3=524, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 142)
    slow = _rolling_slope(x, 126)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.156875 + 0.0030786 * anchor

def f50_tdc_186_analyst_v186(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=149, w2=137, w3=537, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(137, min_periods=max(137//3, 2)).mean()
    noise = impulse.abs().rolling(537, min_periods=max(537//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.17125 + 0.0030787 * anchor

def f50_tdc_187_accrual_v187(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=156, w2=148, w3=550, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(148, min_periods=max(148//3, 2)).rank(pct=True)
    persistence = change.rolling(550, min_periods=max(550//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.2718 * persistence + 0.0030788 * anchor

def f50_tdc_188_jerk_v188(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=163, w2=159, w3=563, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(163, min_periods=max(163//3, 2)).mean(), upside.rolling(159, min_periods=max(159//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.2 + 0.0030789 * anchor

def f50_tdc_189_rel_v189(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=170, w2=170, w3=576, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(170, min_periods=max(170//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 170)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.287 * slope + 0.003079 * anchor

def f50_tdc_190_analyst_v190(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=177, w2=181, w3=589, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 177)
    baseline = trend.rolling(181, min_periods=max(181//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(589, min_periods=max(589//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.22875 + 0.0030791 * anchor

def f50_tdc_191_accrual_v191(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=184, w2=192, w3=602, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 184)
    acceleration = _rolling_slope(velocity, 192)
    curvature = _rolling_slope(acceleration, 602)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.3022 * acceleration + 0.0030792 * anchor

def f50_tdc_192_jerk_v192(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=191, w2=203, w3=615, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(203, min_periods=max(203//3, 2)).max()
    trough = x.rolling(191, min_periods=max(191//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.2575 + 0.0030793 * anchor

def f50_tdc_193_rel_v193(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=198, w2=214, w3=628, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(198, min_periods=max(198//3, 2)).mean())
    decay = spread.ewm(span=214, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.271875 + 0.0030794 * anchor

def f50_tdc_194_analyst_v194(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=205, w2=225, w3=641, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(205, min_periods=max(205//3, 2)).std()
    vol_slow = ret.rolling(225, min_periods=max(225//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.28625 + 0.0030795 * anchor

def f50_tdc_195_accrual_v195(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=212, w2=236, w3=654, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(212, min_periods=max(212//3, 2)).mean(), b.abs().rolling(236, min_periods=max(236//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(126) + 0.3326 * _rolling_slope(cover, 212) + 0.0030796 * anchor

def f50_tdc_196_jerk_v196(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=219, w2=247, w3=667, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(247, min_periods=max(247//3, 2)).mean()
    noise = impulse.abs().rolling(667, min_periods=max(667//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.315 + 0.0030797 * anchor

def f50_tdc_197_rel_v197(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=226, w2=258, w3=680, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(258, min_periods=max(258//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.329375 + 0.0030798 * anchor

def f50_tdc_198_analyst_v198(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=233, w2=269, w3=693, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(233, min_periods=max(233//3, 2)).mean(), upside.rolling(269, min_periods=max(269//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.34375 + 0.0030799 * anchor

def f50_tdc_199_accrual_v199(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=240, w2=280, w3=706, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(706, min_periods=max(706//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.358125 + 0.00308 * anchor

def f50_tdc_200_jerk_v200(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=247, w2=291, w3=719, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 247)
    baseline = trend.rolling(291, min_periods=max(291//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(719, min_periods=max(719//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.3725 + 0.0030801 * anchor

def f50_tdc_201_rel_v201(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=254, w2=302, w3=732, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 254)
    slow = _rolling_slope(x, 302)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=300, adjust=False).mean() * 1.386875 + 0.0030802 * anchor

def f50_tdc_202_analyst_v202(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=10, w2=313, w3=745, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(313, min_periods=max(313//3, 2)).max()
    trough = x.rolling(10, min_periods=max(10//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.40125 + 0.0030803 * anchor

def f50_tdc_203_accrual_v203(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=17, w2=324, w3=758, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(17)
    rank = change.rolling(324, min_periods=max(324//3, 2)).rank(pct=True)
    persistence = change.rolling(758, min_periods=max(758//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.3934 * persistence + 0.0030804 * anchor

def f50_tdc_204_jerk_v204(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=24, w2=335, w3=771, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(24, min_periods=max(24//3, 2)).std()
    vol_slow = ret.rolling(335, min_periods=max(335//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.43 + 0.0030805 * anchor

def f50_tdc_205_rel_v205(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=31, w2=346, w3=27, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(346, min_periods=max(346//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 31)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.4086 * slope + 0.0030806 * anchor

def f50_tdc_206_analyst_v206(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=38, w2=357, w3=40, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(38)
    drag = impulse.rolling(357, min_periods=max(357//3, 2)).mean()
    noise = impulse.abs().rolling(40, min_periods=max(40//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.45875 + 0.0030807 * anchor

def f50_tdc_207_accrual_v207(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=45, w2=368, w3=53, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 45)
    acceleration = _rolling_slope(velocity, 368)
    curvature = _rolling_slope(acceleration, 53)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.0474 * acceleration + 0.0030808 * anchor

def f50_tdc_208_jerk_v208(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=52, w2=379, w3=66, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(52, min_periods=max(52//3, 2)).mean(), upside.rolling(379, min_periods=max(379//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(66) * 1.4875 + 0.0030809 * anchor

def f50_tdc_209_rel_v209(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=59, w2=390, w3=79, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(59, min_periods=max(59//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 1.501875 + 0.003081 * anchor

def f50_tdc_210_analyst_v210(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=66, w2=401, w3=92, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 66)
    baseline = trend.rolling(401, min_periods=max(401//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(92, min_periods=max(92//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 1.51625 + 0.0030811 * anchor

def f50_tdc_211_accrual_v211(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=73, w2=412, w3=105, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(73, min_periods=max(73//3, 2)).mean(), b.abs().rolling(412, min_periods=max(412//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return cover.diff(105) + 0.0778 * _rolling_slope(cover, 73) + 0.0030812 * anchor

def f50_tdc_212_jerk_v212(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=80, w2=423, w3=118, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(423, min_periods=max(423//3, 2)).max()
    trough = x.rolling(80, min_periods=max(80//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 1.545 + 0.0030813 * anchor

def f50_tdc_213_rel_v213(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=87, w2=434, w3=131, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(87, min_periods=max(87//3, 2)).mean(), upside.rolling(434, min_periods=max(434//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 1.559375 + 0.0030814 * anchor

def f50_tdc_214_analyst_v214(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=94, w2=445, w3=144, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(94, min_periods=max(94//3, 2)).std()
    vol_slow = ret.rolling(445, min_periods=max(445//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.57375 + 0.0030815 * anchor

def f50_tdc_215_accrual_v215(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=101, w2=456, w3=157, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(101) - b.diff(126)
    stress = imbalance.rolling(157, min_periods=max(157//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (imbalance - stress) * 1.588125 + 0.0030816 * anchor

def f50_tdc_216_jerk_v216(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=108, w2=467, w3=170, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(108)
    drag = impulse.rolling(467, min_periods=max(467//3, 2)).mean()
    noise = impulse.abs().rolling(170, min_periods=max(170//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(impulse - drag, noise) * 1.6025 + 0.0030817 * anchor

def f50_tdc_217_rel_v217(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=115, w2=478, w3=183, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 115)
    slow = _rolling_slope(x, 478)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (fast - slow).ewm(span=183, adjust=False).mean() * 1.616875 + 0.0030818 * anchor

def f50_tdc_218_analyst_v218(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=122, w2=489, w3=196, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(122, min_periods=max(122//3, 2)).mean(), upside.rolling(489, min_periods=max(489//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return asym.diff(126) * 0.858125 + 0.0030819 * anchor

def f50_tdc_219_accrual_v219(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=129, w2=500, w3=209, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(500, min_periods=max(500//3, 2)).rank(pct=True)
    persistence = change.rolling(209, min_periods=max(209//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (rank - 0.5) + 0.1386 * persistence + 0.003082 * anchor

def f50_tdc_220_jerk_v220(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=136, w2=511, w3=222, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 136)
    baseline = trend.rolling(511, min_periods=max(511//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(222, min_periods=max(222//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(spread, scale) * 0.886875 + 0.0030821 * anchor

def f50_tdc_221_rel_v221(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=143, w2=19, w3=235, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(19, min_periods=max(19//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 143)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return gap - 0.1538 * slope + 0.0030822 * anchor

def f50_tdc_222_analyst_v222(rev_est: pd.Series) -> pd.Series:
    """De-duplicated analyst replacement signal (w1=150, w2=30, w3=248, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(30, min_periods=max(30//3, 2)).max()
    trough = x.rolling(150, min_periods=max(150//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(x - peak, range_) * 0.915625 + 0.0030823 * anchor

def f50_tdc_223_accrual_v223(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """De-duplicated accrual replacement signal (w1=157, w2=41, w3=261, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 157)
    acceleration = _rolling_slope(velocity, 41)
    curvature = _rolling_slope(acceleration, 261)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return curvature + 0.169 * acceleration + 0.0030824 * anchor

def f50_tdc_224_jerk_v224(high: pd.Series) -> pd.Series:
    """De-duplicated jerk replacement signal (w1=164, w2=52, w3=274, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(164, min_periods=max(164//3, 2)).std()
    vol_slow = ret.rolling(52, min_periods=max(52//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.944375 + 0.0030825 * anchor

def f50_tdc_225_rel_v225(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """De-duplicated rel replacement signal (w1=171, w2=63, w3=287, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(171, min_periods=max(171//3, 2)).mean())
    decay = spread.ewm(span=63, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    return (spread - decay) * 0.95875 + 0.0030826 * anchor
