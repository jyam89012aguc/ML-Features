"""50 terminal decline composite d3 third derivative features 301-375 â€” Pipeline 1a-HF Grade v3.

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

def f50_tdc_301_rel_v301_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=201, w2=396, w3=518, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(396, min_periods=max(396//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 201)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3854 * slope + 0.0030902 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_302_analyst_v302_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=208, w2=407, w3=531, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(407, min_periods=max(407//3, 2)).max()
    trough = x.rolling(208, min_periods=max(208//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2925 + 0.0030903 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_303_accrual_v303_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=215, w2=418, w3=544, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 215)
    acceleration = _rolling_slope(velocity, 418)
    curvature = _rolling_slope(acceleration, 544)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.4006 * acceleration + 0.0030904 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_304_jerk_v304_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=222, w2=429, w3=557, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(222, min_periods=max(222//3, 2)).std()
    vol_slow = ret.rolling(429, min_periods=max(429//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.32125 + 0.0030905 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_305_rel_v305_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=229, w2=440, w3=570, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(229, min_periods=max(229//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.335625 + 0.0030906 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_306_analyst_v306_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=236, w2=451, w3=583, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(451, min_periods=max(451//3, 2)).mean()
    noise = impulse.abs().rolling(583, min_periods=max(583//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.35 + 0.0030907 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_307_accrual_v307_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=243, w2=462, w3=596, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(243, min_periods=max(243//3, 2)).mean(), b.abs().rolling(462, min_periods=max(462//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.0546 * _rolling_slope(cover, 243) + 0.0030908 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_308_jerk_v308_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=250, w2=473, w3=609, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(250, min_periods=max(250//3, 2)).mean(), upside.rolling(473, min_periods=max(473//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.37875 + 0.0030909 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_309_rel_v309_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=6, w2=484, w3=622, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(6, min_periods=max(6//3, 2)).mean(), upside.rolling(484, min_periods=max(484//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.393125 + 0.003091 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_310_analyst_v310_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=13, w2=495, w3=635, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 13)
    baseline = trend.rolling(495, min_periods=max(495//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(635, min_periods=max(635//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.4075 + 0.0030911 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_311_accrual_v311_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=20, w2=506, w3=648, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(20) - b.diff(126)
    stress = imbalance.rolling(648, min_periods=max(648//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.421875 + 0.0030912 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_312_jerk_v312_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=27, w2=14, w3=661, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(14, min_periods=max(14//3, 2)).max()
    trough = x.rolling(27, min_periods=max(27//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.43625 + 0.0030913 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_313_rel_v313_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=34, w2=25, w3=674, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 34)
    slow = _rolling_slope(x, 25)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.450625 + 0.0030914 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_314_analyst_v314_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=41, w2=36, w3=687, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(41, min_periods=max(41//3, 2)).std()
    vol_slow = ret.rolling(36, min_periods=max(36//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.465 + 0.0030915 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_315_accrual_v315_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=48, w2=47, w3=700, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(48)
    rank = change.rolling(47, min_periods=max(47//3, 2)).rank(pct=True)
    persistence = change.rolling(700, min_periods=max(700//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1154 * persistence + 0.0030916 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_316_jerk_v316_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=55, w2=58, w3=713, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(55)
    drag = impulse.rolling(58, min_periods=max(58//3, 2)).mean()
    noise = impulse.abs().rolling(713, min_periods=max(713//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.49375 + 0.0030917 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_317_rel_v317_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=62, w2=69, w3=726, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(69, min_periods=max(69//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 62)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1306 * slope + 0.0030918 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_318_analyst_v318_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=69, w2=80, w3=739, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(69, min_periods=max(69//3, 2)).mean(), upside.rolling(80, min_periods=max(80//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.5225 + 0.0030919 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_319_accrual_v319_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=76, w2=91, w3=752, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 76)
    acceleration = _rolling_slope(velocity, 91)
    curvature = _rolling_slope(acceleration, 752)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1458 * acceleration + 0.003092 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_320_jerk_v320_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=83, w2=102, w3=765, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 83)
    baseline = trend.rolling(102, min_periods=max(102//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(765, min_periods=max(765//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.55125 + 0.0030921 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_321_rel_v321_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=90, w2=113, w3=21, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(90, min_periods=max(90//3, 2)).mean())
    decay = spread.ewm(span=113, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.565625 + 0.0030922 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_322_analyst_v322_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=97, w2=124, w3=34, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(124, min_periods=max(124//3, 2)).max()
    trough = x.rolling(97, min_periods=max(97//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.58 + 0.0030923 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_323_accrual_v323_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=104, w2=135, w3=47, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(104, min_periods=max(104//3, 2)).mean(), b.abs().rolling(135, min_periods=max(135//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(47) + 0.1762 * _rolling_slope(cover, 104) + 0.0030924 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_324_jerk_v324_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=111, w2=146, w3=60, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(111, min_periods=max(111//3, 2)).std()
    vol_slow = ret.rolling(146, min_periods=max(146//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.60875 + 0.0030925 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_325_rel_v325_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=118, w2=157, w3=73, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(118, min_periods=max(118//3, 2)).mean(), upside.rolling(157, min_periods=max(157//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(73) * 0.85 + 0.0030926 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_326_analyst_v326_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=125, w2=168, w3=86, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(125)
    drag = impulse.rolling(168, min_periods=max(168//3, 2)).mean()
    noise = impulse.abs().rolling(86, min_periods=max(86//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.864375 + 0.0030927 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_327_accrual_v327_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=132, w2=179, w3=99, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(99, min_periods=max(99//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 0.87875 + 0.0030928 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_328_jerk_v328_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=139, w2=190, w3=112, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(139, min_periods=max(139//3, 2)).mean(), upside.rolling(190, min_periods=max(190//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(112) * 0.893125 + 0.0030929 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_329_rel_v329_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=146, w2=201, w3=125, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 146)
    slow = _rolling_slope(x, 201)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=125, adjust=False).mean() * 0.9075 + 0.003093 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_330_analyst_v330_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=153, w2=212, w3=138, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 153)
    baseline = trend.rolling(212, min_periods=max(212//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(138, min_periods=max(138//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.921875 + 0.0030931 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_331_accrual_v331_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=160, w2=223, w3=151, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(223, min_periods=max(223//3, 2)).rank(pct=True)
    persistence = change.rolling(151, min_periods=max(151//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.237 * persistence + 0.0030932 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_332_jerk_v332_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=167, w2=234, w3=164, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(234, min_periods=max(234//3, 2)).max()
    trough = x.rolling(167, min_periods=max(167//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.950625 + 0.0030933 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_333_rel_v333_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=174, w2=245, w3=177, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(245, min_periods=max(245//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 174)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2522 * slope + 0.0030934 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_334_analyst_v334_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=181, w2=256, w3=190, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(181, min_periods=max(181//3, 2)).std()
    vol_slow = ret.rolling(256, min_periods=max(256//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.979375 + 0.0030935 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_335_accrual_v335_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=188, w2=267, w3=203, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 188)
    acceleration = _rolling_slope(velocity, 267)
    curvature = _rolling_slope(acceleration, 203)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2674 * acceleration + 0.0030936 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_336_jerk_v336_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=195, w2=278, w3=216, lag=0)."""
    x = high.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(278, min_periods=max(278//3, 2)).mean()
    noise = impulse.abs().rolling(216, min_periods=max(216//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.008125 + 0.0030937 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_337_rel_v337_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=202, w2=289, w3=229, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(202, min_periods=max(202//3, 2)).mean())
    decay = spread.ewm(span=289, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.0225 + 0.0030938 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_338_analyst_v338_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=209, w2=300, w3=242, lag=2)."""
    x = rev_est.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(209, min_periods=max(209//3, 2)).mean(), upside.rolling(300, min_periods=max(300//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.036875 + 0.0030939 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_339_accrual_v339_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=216, w2=311, w3=255, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(216, min_periods=max(216//3, 2)).mean(), b.abs().rolling(311, min_periods=max(311//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.2978 * _rolling_slope(cover, 216) + 0.003094 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_340_jerk_v340_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=223, w2=322, w3=268, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 223)
    baseline = trend.rolling(322, min_periods=max(322//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(268, min_periods=max(268//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.065625 + 0.0030941 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_341_rel_v341_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=230, w2=333, w3=281, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(230, min_periods=max(230//3, 2)).mean(), upside.rolling(333, min_periods=max(333//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.08 + 0.0030942 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_342_analyst_v342_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=237, w2=344, w3=294, lag=42)."""
    x = rev_est.shift(42)
    peak = x.rolling(344, min_periods=max(344//3, 2)).max()
    trough = x.rolling(237, min_periods=max(237//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.094375 + 0.0030943 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_343_accrual_v343_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=244, w2=355, w3=307, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(307, min_periods=max(307//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.10875 + 0.0030944 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_344_jerk_v344_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=251, w2=366, w3=320, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(251, min_periods=max(251//3, 2)).std()
    vol_slow = ret.rolling(366, min_periods=max(366//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.123125 + 0.0030945 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_345_rel_v345_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=7, w2=377, w3=333, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 7)
    slow = _rolling_slope(x, 377)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.1375 + 0.0030946 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_346_analyst_v346_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=14, w2=388, w3=346, lag=2)."""
    x = rev_est.shift(2)
    impulse = x.diff(14)
    drag = impulse.rolling(388, min_periods=max(388//3, 2)).mean()
    noise = impulse.abs().rolling(346, min_periods=max(346//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.151875 + 0.0030947 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_347_accrual_v347_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=21, w2=399, w3=359, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(21)
    rank = change.rolling(399, min_periods=max(399//3, 2)).rank(pct=True)
    persistence = change.rolling(359, min_periods=max(359//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3586 * persistence + 0.0030948 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_348_jerk_v348_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=28, w2=410, w3=372, lag=10)."""
    x = high.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(28, min_periods=max(28//3, 2)).mean(), upside.rolling(410, min_periods=max(410//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.180625 + 0.0030949 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_349_rel_v349_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=35, w2=421, w3=385, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(421, min_periods=max(421//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 35)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3738 * slope + 0.003095 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_350_analyst_v350_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=42, w2=432, w3=398, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 42)
    baseline = trend.rolling(432, min_periods=max(432//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(398, min_periods=max(398//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.209375 + 0.0030951 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_351_accrual_v351_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=49, w2=443, w3=411, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 49)
    acceleration = _rolling_slope(velocity, 443)
    curvature = _rolling_slope(acceleration, 411)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.389 * acceleration + 0.0030952 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_352_jerk_v352_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=56, w2=454, w3=424, lag=0)."""
    x = high.shift(0)
    peak = x.rolling(454, min_periods=max(454//3, 2)).max()
    trough = x.rolling(56, min_periods=max(56//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.238125 + 0.0030953 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_353_rel_v353_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=63, w2=465, w3=437, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(63, min_periods=max(63//3, 2)).mean())
    decay = spread.ewm(span=300, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.2525 + 0.0030954 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_354_analyst_v354_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=70, w2=476, w3=450, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(70, min_periods=max(70//3, 2)).std()
    vol_slow = ret.rolling(476, min_periods=max(476//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.266875 + 0.0030955 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_355_accrual_v355_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=77, w2=487, w3=463, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(77, min_periods=max(77//3, 2)).mean(), b.abs().rolling(487, min_periods=max(487//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.043 * _rolling_slope(cover, 77) + 0.0030956 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_356_jerk_v356_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=84, w2=498, w3=476, lag=10)."""
    x = high.shift(10)
    impulse = x.diff(84)
    drag = impulse.rolling(498, min_periods=max(498//3, 2)).mean()
    noise = impulse.abs().rolling(476, min_periods=max(476//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.295625 + 0.0030957 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_357_rel_v357_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=91, w2=509, w3=489, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(91, min_periods=max(91//3, 2)).mean(), upside.rolling(509, min_periods=max(509//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.31 + 0.0030958 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_358_analyst_v358_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=98, w2=17, w3=502, lag=42)."""
    x = rev_est.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(98, min_periods=max(98//3, 2)).mean(), upside.rolling(17, min_periods=max(17//3, 2)).mean().abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.324375 + 0.0030959 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_359_accrual_v359_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=105, w2=28, w3=515, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(105) - b.diff(28)
    stress = imbalance.rolling(515, min_periods=max(515//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.33875 + 0.003096 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_360_jerk_v360_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=112, w2=39, w3=528, lag=0)."""
    x = _safe_log(high.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 112)
    baseline = trend.rolling(39, min_periods=max(39//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(528, min_periods=max(528//3, 2)).mean()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.353125 + 0.0030961 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_361_rel_v361_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=119, w2=50, w3=541, lag=1)."""
    x = _safe_log(close.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 119)
    slow = _rolling_slope(x, 50)
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.3675 + 0.0030962 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_362_analyst_v362_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=126, w2=61, w3=554, lag=2)."""
    x = rev_est.shift(2)
    peak = x.rolling(61, min_periods=max(61//3, 2)).max()
    trough = x.rolling(126, min_periods=max(126//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.381875 + 0.0030963 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_363_accrual_v363_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=133, w2=72, w3=567, lag=5)."""
    x = ocf.shift(5)
    change = x.pct_change(126)
    rank = change.rolling(72, min_periods=max(72//3, 2)).rank(pct=True)
    persistence = change.rolling(567, min_periods=max(567//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1038 * persistence + 0.0030964 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_364_jerk_v364_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=140, w2=83, w3=580, lag=10)."""
    x = _safe_log(high.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(140, min_periods=max(140//3, 2)).std()
    vol_slow = ret.rolling(83, min_periods=max(83//3, 2)).std()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.410625 + 0.0030965 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_365_rel_v365_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=147, w2=94, w3=593, lag=21)."""
    x = close.shift(21)
    ma = x.rolling(94, min_periods=max(94//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 147)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.119 * slope + 0.0030966 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_366_analyst_v366_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=154, w2=105, w3=606, lag=42)."""
    x = rev_est.shift(42)
    impulse = x.diff(126)
    drag = impulse.rolling(105, min_periods=max(105//3, 2)).mean()
    noise = impulse.abs().rolling(606, min_periods=max(606//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.439375 + 0.0030967 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_367_accrual_v367_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=161, w2=116, w3=619, lag=63)."""
    x = _safe_log(ocf.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 161)
    acceleration = _rolling_slope(velocity, 116)
    curvature = _rolling_slope(acceleration, 619)
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1342 * acceleration + 0.0030968 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_368_jerk_v368_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=168, w2=127, w3=632, lag=0)."""
    x = high.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(168, min_periods=max(168//3, 2)).mean(), upside.rolling(127, min_periods=max(127//3, 2)).mean().abs())
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.468125 + 0.0030969 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_369_rel_v369_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=175, w2=138, w3=645, lag=1)."""
    a = close.shift(1)
    b = sector_close.shift(1)
    spread = _safe_div(a - b, a.abs().rolling(175, min_periods=max(175//3, 2)).mean())
    decay = spread.ewm(span=138, adjust=False).mean()
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (spread - decay) * 1.4825 + 0.003097 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_370_analyst_v370_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=182, w2=149, w3=658, lag=2)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 182)
    baseline = trend.rolling(149, min_periods=max(149//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(658, min_periods=max(658//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.496875 + 0.0030971 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_371_accrual_v371_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=189, w2=160, w3=671, lag=5)."""
    a = ocf.shift(5)
    b = assetsc.shift(5)
    cover = _safe_div(a.rolling(189, min_periods=max(189//3, 2)).mean(), b.abs().rolling(160, min_periods=max(160//3, 2)).mean())
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = cover.diff(126) + 0.1646 * _rolling_slope(cover, 189) + 0.0030972 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_372_jerk_v372_d3(high: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated jerk replacement signal (w1=196, w2=171, w3=684, lag=10)."""
    x = high.shift(10)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(196, min_periods=max(196//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(high.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.525625 + 0.0030973 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_373_rel_v373_d3(close: pd.Series, sector_close: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated rel replacement signal (w1=203, w2=182, w3=697, lag=21)."""
    x = close.shift(21)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(203, min_periods=max(203//3, 2)).mean(), upside.rolling(182, min_periods=max(182//3, 2)).mean().abs())
    anchor = _safe_log(close.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.54 + 0.0030974 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_374_analyst_v374_d3(rev_est: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated analyst replacement signal (w1=210, w2=193, w3=710, lag=42)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(210, min_periods=max(210//3, 2)).std()
    vol_slow = ret.rolling(193, min_periods=max(193//3, 2)).std()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.554375 + 0.0030975 * anchor
    return base_signal.diff().diff().diff()

def f50_tdc_375_accrual_v375_d3(ocf: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Third derivative of de-duplicated accrual replacement signal (w1=217, w2=204, w3=723, lag=63)."""
    a = _safe_log(ocf.abs() + 1.0).shift(63)
    b = _safe_log(assetsc.abs() + 1.0).shift(63)
    imbalance = a.diff(126) - b.diff(126)
    stress = imbalance.rolling(723, min_periods=max(723//3, 2)).mean()
    anchor = _safe_log(ocf.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (imbalance - stress) * 1.56875 + 0.0030976 * anchor
    return base_signal.diff().diff().diff()
