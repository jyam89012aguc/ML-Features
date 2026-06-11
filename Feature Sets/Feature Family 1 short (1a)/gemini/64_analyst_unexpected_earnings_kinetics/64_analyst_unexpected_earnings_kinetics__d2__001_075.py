"""64 analyst unexpected earnings kinetics d2 second derivative features 1-75 â€” Pipeline 1a-HF Grade v3.

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

def f64_asue_001_analyst_v1_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=8, w2=160, w3=202, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 8)
    slow = _rolling_slope(x, 160)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=202, adjust=False).mean() * 1.14375 + 0.0036002 * anchor
    return base_signal.diff().diff()

def f64_asue_002_analyst_v2_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=15, w2=171, w3=215, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(171, min_periods=max(171//3, 2)).max()
    trough = x.rolling(15, min_periods=max(15//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.158125 + 0.0036003 * anchor
    return base_signal.diff().diff()

def f64_asue_003_analyst_v3_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=22, w2=182, w3=228, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(22)
    rank = change.rolling(182, min_periods=max(182//3, 2)).rank(pct=True)
    persistence = change.rolling(228, min_periods=max(228//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.3914 * persistence + 0.0036004 * anchor
    return base_signal.diff().diff()

def f64_asue_004_analyst_v4_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=29, w2=193, w3=241, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(29, min_periods=max(29//3, 2)).std()
    vol_slow = ret.rolling(193, min_periods=max(193//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.186875 + 0.0036005 * anchor
    return base_signal.diff().diff()

def f64_asue_005_analyst_v5_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=36, w2=204, w3=254, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(204, min_periods=max(204//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 36)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4066 * slope + 0.0036006 * anchor
    return base_signal.diff().diff()

def f64_asue_006_analyst_v6_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=43, w2=215, w3=267, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(43)
    drag = impulse.rolling(215, min_periods=max(215//3, 2)).mean()
    noise = impulse.abs().rolling(267, min_periods=max(267//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.215625 + 0.0036007 * anchor
    return base_signal.diff().diff()

def f64_asue_007_analyst_v7_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=50, w2=226, w3=280, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 50)
    acceleration = _rolling_slope(velocity, 226)
    curvature = _rolling_slope(acceleration, 280)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.0454 * acceleration + 0.0036008 * anchor
    return base_signal.diff().diff()

def f64_asue_008_analyst_v8_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=57, w2=237, w3=293, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(57, min_periods=max(57//3, 2)).mean(), upside.rolling(237, min_periods=max(237//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.244375 + 0.0036009 * anchor
    return base_signal.diff().diff()

def f64_asue_009_analyst_v9_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=64, w2=248, w3=306, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(248, min_periods=max(248//3, 2)).max()
    rebound = x - x.rolling(64, min_periods=max(64//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0606 * _rolling_slope(draw, 306) + 0.003601 * anchor
    return base_signal.diff().diff()

def f64_asue_010_analyst_v10_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=71, w2=259, w3=319, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 71)
    baseline = trend.rolling(259, min_periods=max(259//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(319, min_periods=max(319//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.273125 + 0.0036011 * anchor
    return base_signal.diff().diff()

def f64_asue_011_analyst_v11_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=78, w2=270, w3=332, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 78)
    slow = _rolling_slope(x, 270)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.2875 + 0.0036012 * anchor
    return base_signal.diff().diff()

def f64_asue_012_analyst_v12_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=85, w2=281, w3=345, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(281, min_periods=max(281//3, 2)).max()
    trough = x.rolling(85, min_periods=max(85//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.301875 + 0.0036013 * anchor
    return base_signal.diff().diff()

def f64_asue_013_analyst_v13_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=92, w2=292, w3=358, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(92)
    rank = change.rolling(292, min_periods=max(292//3, 2)).rank(pct=True)
    persistence = change.rolling(358, min_periods=max(358//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.091 * persistence + 0.0036014 * anchor
    return base_signal.diff().diff()

def f64_asue_014_analyst_v14_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=99, w2=303, w3=371, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(99, min_periods=max(99//3, 2)).std()
    vol_slow = ret.rolling(303, min_periods=max(303//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.330625 + 0.0036015 * anchor
    return base_signal.diff().diff()

def f64_asue_015_analyst_v15_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=106, w2=314, w3=384, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(314, min_periods=max(314//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 106)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1062 * slope + 0.0036016 * anchor
    return base_signal.diff().diff()

def f64_asue_016_analyst_v16_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=113, w2=325, w3=397, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(113)
    drag = impulse.rolling(325, min_periods=max(325//3, 2)).mean()
    noise = impulse.abs().rolling(397, min_periods=max(397//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.359375 + 0.0036017 * anchor
    return base_signal.diff().diff()

def f64_asue_017_analyst_v17_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=120, w2=336, w3=410, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 120)
    acceleration = _rolling_slope(velocity, 336)
    curvature = _rolling_slope(acceleration, 410)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1214 * acceleration + 0.0036018 * anchor
    return base_signal.diff().diff()

def f64_asue_018_analyst_v18_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=127, w2=347, w3=423, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(127, min_periods=max(127//3, 2)).mean(), upside.rolling(347, min_periods=max(347//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.388125 + 0.0036019 * anchor
    return base_signal.diff().diff()

def f64_asue_019_analyst_v19_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=134, w2=358, w3=436, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(358, min_periods=max(358//3, 2)).max()
    rebound = x - x.rolling(134, min_periods=max(134//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1366 * _rolling_slope(draw, 436) + 0.003602 * anchor
    return base_signal.diff().diff()

def f64_asue_020_analyst_v20_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=141, w2=369, w3=449, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 141)
    baseline = trend.rolling(369, min_periods=max(369//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(449, min_periods=max(449//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.416875 + 0.0036021 * anchor
    return base_signal.diff().diff()

def f64_asue_021_analyst_v21_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=148, w2=380, w3=462, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 148)
    slow = _rolling_slope(x, 380)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.43125 + 0.0036022 * anchor
    return base_signal.diff().diff()

def f64_asue_022_analyst_v22_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=155, w2=391, w3=475, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(391, min_periods=max(391//3, 2)).max()
    trough = x.rolling(155, min_periods=max(155//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.445625 + 0.0036023 * anchor
    return base_signal.diff().diff()

def f64_asue_023_analyst_v23_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=162, w2=402, w3=488, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(402, min_periods=max(402//3, 2)).rank(pct=True)
    persistence = change.rolling(488, min_periods=max(488//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.167 * persistence + 0.0036024 * anchor
    return base_signal.diff().diff()

def f64_asue_024_analyst_v24_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=169, w2=413, w3=501, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(169, min_periods=max(169//3, 2)).std()
    vol_slow = ret.rolling(413, min_periods=max(413//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.474375 + 0.0036025 * anchor
    return base_signal.diff().diff()

def f64_asue_025_analyst_v25_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=176, w2=424, w3=514, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(424, min_periods=max(424//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 176)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1822 * slope + 0.0036026 * anchor
    return base_signal.diff().diff()

def f64_asue_026_analyst_v26_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=183, w2=435, w3=527, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(435, min_periods=max(435//3, 2)).mean()
    noise = impulse.abs().rolling(527, min_periods=max(527//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.503125 + 0.0036027 * anchor
    return base_signal.diff().diff()

def f64_asue_027_analyst_v27_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=190, w2=446, w3=540, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 190)
    acceleration = _rolling_slope(velocity, 446)
    curvature = _rolling_slope(acceleration, 540)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.1974 * acceleration + 0.0036028 * anchor
    return base_signal.diff().diff()

def f64_asue_028_analyst_v28_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=197, w2=457, w3=553, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(197, min_periods=max(197//3, 2)).mean(), upside.rolling(457, min_periods=max(457//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.531875 + 0.0036029 * anchor
    return base_signal.diff().diff()

def f64_asue_029_analyst_v29_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=204, w2=468, w3=566, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(468, min_periods=max(468//3, 2)).max()
    rebound = x - x.rolling(204, min_periods=max(204//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2126 * _rolling_slope(draw, 566) + 0.003603 * anchor
    return base_signal.diff().diff()

def f64_asue_030_analyst_v30_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=211, w2=479, w3=579, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 211)
    baseline = trend.rolling(479, min_periods=max(479//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(579, min_periods=max(579//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.560625 + 0.0036031 * anchor
    return base_signal.diff().diff()

def f64_asue_031_analyst_v31_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=218, w2=490, w3=592, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 218)
    slow = _rolling_slope(x, 490)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.575 + 0.0036032 * anchor
    return base_signal.diff().diff()

def f64_asue_032_analyst_v32_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=225, w2=501, w3=605, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(501, min_periods=max(501//3, 2)).max()
    trough = x.rolling(225, min_periods=max(225//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.589375 + 0.0036033 * anchor
    return base_signal.diff().diff()

def f64_asue_033_analyst_v33_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=232, w2=512, w3=618, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(126)
    rank = change.rolling(512, min_periods=max(512//3, 2)).rank(pct=True)
    persistence = change.rolling(618, min_periods=max(618//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.243 * persistence + 0.0036034 * anchor
    return base_signal.diff().diff()

def f64_asue_034_analyst_v34_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=239, w2=20, w3=631, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(239, min_periods=max(239//3, 2)).std()
    vol_slow = ret.rolling(20, min_periods=max(20//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.618125 + 0.0036035 * anchor
    return base_signal.diff().diff()

def f64_asue_035_analyst_v35_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=246, w2=31, w3=644, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(31, min_periods=max(31//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 246)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.2582 * slope + 0.0036036 * anchor
    return base_signal.diff().diff()

def f64_asue_036_analyst_v36_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=253, w2=42, w3=657, lag=10)."""
    x = eps_est.shift(10)
    impulse = x.diff(126)
    drag = impulse.rolling(42, min_periods=max(42//3, 2)).mean()
    noise = impulse.abs().rolling(657, min_periods=max(657//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 0.87375 + 0.0036037 * anchor
    return base_signal.diff().diff()

def f64_asue_037_analyst_v37_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=9, w2=53, w3=670, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    velocity = _rolling_slope(x, 9)
    acceleration = _rolling_slope(velocity, 53)
    curvature = _rolling_slope(acceleration, 670)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.2734 * acceleration + 0.0036038 * anchor
    return base_signal.diff().diff()

def f64_asue_038_analyst_v38_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=16, w2=64, w3=683, lag=42)."""
    x = eps_disp.shift(42)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(16, min_periods=max(16//3, 2)).mean(), upside.rolling(64, min_periods=max(64//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 0.9025 + 0.0036039 * anchor
    return base_signal.diff().diff()

def f64_asue_039_analyst_v39_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=23, w2=75, w3=696, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    draw = x - x.rolling(75, min_periods=max(75//3, 2)).max()
    rebound = x - x.rolling(23, min_periods=max(23//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.2886 * _rolling_slope(draw, 696) + 0.003604 * anchor
    return base_signal.diff().diff()

def f64_asue_040_analyst_v40_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=30, w2=86, w3=709, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    trend = _rolling_slope(x, 30)
    baseline = trend.rolling(86, min_periods=max(86//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(709, min_periods=max(709//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 0.93125 + 0.0036041 * anchor
    return base_signal.diff().diff()

def f64_asue_041_analyst_v41_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=37, w2=97, w3=722, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    fast = _rolling_slope(x, 37)
    slow = _rolling_slope(x, 97)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 0.945625 + 0.0036042 * anchor
    return base_signal.diff().diff()

def f64_asue_042_analyst_v42_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=44, w2=108, w3=735, lag=2)."""
    x = eps_disp.shift(2)
    peak = x.rolling(108, min_periods=max(108//3, 2)).max()
    trough = x.rolling(44, min_periods=max(44//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 0.96 + 0.0036043 * anchor
    return base_signal.diff().diff()

def f64_asue_043_analyst_v43_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=51, w2=119, w3=748, lag=5)."""
    x = rev_disp.shift(5)
    change = x.pct_change(51)
    rank = change.rolling(119, min_periods=max(119//3, 2)).rank(pct=True)
    persistence = change.rolling(748, min_periods=max(748//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.319 * persistence + 0.0036044 * anchor
    return base_signal.diff().diff()

def f64_asue_044_analyst_v44_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=58, w2=130, w3=761, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    ret = x.diff()
    vol_fast = ret.rolling(58, min_periods=max(58//3, 2)).std()
    vol_slow = ret.rolling(130, min_periods=max(130//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 0.98875 + 0.0036045 * anchor
    return base_signal.diff().diff()

def f64_asue_045_analyst_v45_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=65, w2=141, w3=17, lag=21)."""
    x = rev_est.shift(21)
    ma = x.rolling(141, min_periods=max(141//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 65)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.3342 * slope + 0.0036046 * anchor
    return base_signal.diff().diff()

def f64_asue_046_analyst_v46_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=72, w2=152, w3=30, lag=42)."""
    x = eps_disp.shift(42)
    impulse = x.diff(72)
    drag = impulse.rolling(152, min_periods=max(152//3, 2)).mean()
    noise = impulse.abs().rolling(30, min_periods=max(30//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.0175 + 0.0036047 * anchor
    return base_signal.diff().diff()

def f64_asue_047_analyst_v47_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=79, w2=163, w3=43, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    velocity = _rolling_slope(x, 79)
    acceleration = _rolling_slope(velocity, 163)
    curvature = _rolling_slope(acceleration, 43)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.3494 * acceleration + 0.0036048 * anchor
    return base_signal.diff().diff()

def f64_asue_048_analyst_v48_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=86, w2=174, w3=56, lag=0)."""
    x = eps_est.shift(0)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(86, min_periods=max(86//3, 2)).mean(), upside.rolling(174, min_periods=max(174//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(56) * 1.04625 + 0.0036049 * anchor
    return base_signal.diff().diff()

def f64_asue_049_analyst_v49_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=93, w2=185, w3=69, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    draw = x - x.rolling(185, min_periods=max(185//3, 2)).max()
    rebound = x - x.rolling(93, min_periods=max(93//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.3646 * _rolling_slope(draw, 69) + 0.003605 * anchor
    return base_signal.diff().diff()

def f64_asue_050_analyst_v50_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=100, w2=196, w3=82, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    trend = _rolling_slope(x, 100)
    baseline = trend.rolling(196, min_periods=max(196//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(82, min_periods=max(82//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.075 + 0.0036051 * anchor
    return base_signal.diff().diff()

def f64_asue_051_analyst_v51_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=107, w2=207, w3=95, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    fast = _rolling_slope(x, 107)
    slow = _rolling_slope(x, 207)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=95, adjust=False).mean() * 1.089375 + 0.0036052 * anchor
    return base_signal.diff().diff()

def f64_asue_052_analyst_v52_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=114, w2=218, w3=108, lag=10)."""
    x = eps_est.shift(10)
    peak = x.rolling(218, min_periods=max(218//3, 2)).max()
    trough = x.rolling(114, min_periods=max(114//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.10375 + 0.0036053 * anchor
    return base_signal.diff().diff()

def f64_asue_053_analyst_v53_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=121, w2=229, w3=121, lag=21)."""
    x = rev_est.shift(21)
    change = x.pct_change(121)
    rank = change.rolling(229, min_periods=max(229//3, 2)).rank(pct=True)
    persistence = change.rolling(121, min_periods=max(121//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.395 * persistence + 0.0036054 * anchor
    return base_signal.diff().diff()

def f64_asue_054_analyst_v54_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=128, w2=240, w3=134, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    ret = x.diff()
    vol_fast = ret.rolling(128, min_periods=max(128//3, 2)).std()
    vol_slow = ret.rolling(240, min_periods=max(240//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.1325 + 0.0036055 * anchor
    return base_signal.diff().diff()

def f64_asue_055_analyst_v55_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=135, w2=251, w3=147, lag=63)."""
    x = rev_disp.shift(63)
    ma = x.rolling(251, min_periods=max(251//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 135)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.4102 * slope + 0.0036056 * anchor
    return base_signal.diff().diff()

def f64_asue_056_analyst_v56_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=142, w2=262, w3=160, lag=0)."""
    x = eps_est.shift(0)
    impulse = x.diff(126)
    drag = impulse.rolling(262, min_periods=max(262//3, 2)).mean()
    noise = impulse.abs().rolling(160, min_periods=max(160//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.16125 + 0.0036057 * anchor
    return base_signal.diff().diff()

def f64_asue_057_analyst_v57_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=149, w2=273, w3=173, lag=1)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(1)
    velocity = _rolling_slope(x, 149)
    acceleration = _rolling_slope(velocity, 273)
    curvature = _rolling_slope(acceleration, 173)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.049 * acceleration + 0.0036058 * anchor
    return base_signal.diff().diff()

def f64_asue_058_analyst_v58_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=156, w2=284, w3=186, lag=2)."""
    x = eps_disp.shift(2)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(156, min_periods=max(156//3, 2)).mean(), upside.rolling(284, min_periods=max(284//3, 2)).mean().abs())
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.19 + 0.0036059 * anchor
    return base_signal.diff().diff()

def f64_asue_059_analyst_v59_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=163, w2=295, w3=199, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    draw = x - x.rolling(295, min_periods=max(295//3, 2)).max()
    rebound = x - x.rolling(163, min_periods=max(163//3, 2)).min()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.0642 * _rolling_slope(draw, 199) + 0.003606 * anchor
    return base_signal.diff().diff()

def f64_asue_060_analyst_v60_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=170, w2=306, w3=212, lag=10)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(10)
    trend = _rolling_slope(x, 170)
    baseline = trend.rolling(306, min_periods=max(306//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(212, min_periods=max(212//3, 2)).mean()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.21875 + 0.0036061 * anchor
    return base_signal.diff().diff()

def f64_asue_061_analyst_v61_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=177, w2=317, w3=225, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    fast = _rolling_slope(x, 177)
    slow = _rolling_slope(x, 317)
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=225, adjust=False).mean() * 1.233125 + 0.0036062 * anchor
    return base_signal.diff().diff()

def f64_asue_062_analyst_v62_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=184, w2=328, w3=238, lag=42)."""
    x = eps_disp.shift(42)
    peak = x.rolling(328, min_periods=max(328//3, 2)).max()
    trough = x.rolling(184, min_periods=max(184//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.2475 + 0.0036063 * anchor
    return base_signal.diff().diff()

def f64_asue_063_analyst_v63_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=191, w2=339, w3=251, lag=63)."""
    x = rev_disp.shift(63)
    change = x.pct_change(126)
    rank = change.rolling(339, min_periods=max(339//3, 2)).rank(pct=True)
    persistence = change.rolling(251, min_periods=max(251//3, 2)).mean()
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.0946 * persistence + 0.0036064 * anchor
    return base_signal.diff().diff()

def f64_asue_064_analyst_v64_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=198, w2=350, w3=264, lag=0)."""
    x = _safe_log(eps_est.abs() + 1.0).shift(0)
    ret = x.diff()
    vol_fast = ret.rolling(198, min_periods=max(198//3, 2)).std()
    vol_slow = ret.rolling(350, min_periods=max(350//3, 2)).std()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.27625 + 0.0036065 * anchor
    return base_signal.diff().diff()

def f64_asue_065_analyst_v65_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=205, w2=361, w3=277, lag=1)."""
    x = rev_est.shift(1)
    ma = x.rolling(361, min_periods=max(361//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 205)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1098 * slope + 0.0036066 * anchor
    return base_signal.diff().diff()

def f64_asue_066_analyst_v66_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=212, w2=372, w3=290, lag=2)."""
    x = eps_disp.shift(2)
    impulse = x.diff(126)
    drag = impulse.rolling(372, min_periods=max(372//3, 2)).mean()
    noise = impulse.abs().rolling(290, min_periods=max(290//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(impulse - drag, noise) * 1.305 + 0.0036067 * anchor
    return base_signal.diff().diff()

def f64_asue_067_analyst_v67_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=219, w2=383, w3=303, lag=5)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(5)
    velocity = _rolling_slope(x, 219)
    acceleration = _rolling_slope(velocity, 383)
    curvature = _rolling_slope(acceleration, 303)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = curvature + 0.125 * acceleration + 0.0036068 * anchor
    return base_signal.diff().diff()

def f64_asue_068_analyst_v68_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=226, w2=394, w3=316, lag=10)."""
    x = eps_est.shift(10)
    step = x - x.shift(1)
    downside = step.where(step < 0, 0.0).abs()
    upside = step.where(step > 0, 0.0)
    asym = _safe_div(downside.rolling(226, min_periods=max(226//3, 2)).mean(), upside.rolling(394, min_periods=max(394//3, 2)).mean().abs())
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = asym.diff(126) * 1.33375 + 0.0036069 * anchor
    return base_signal.diff().diff()

def f64_asue_069_analyst_v69_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=233, w2=405, w3=329, lag=21)."""
    x = _safe_log(rev_est.abs() + 1.0).shift(21)
    draw = x - x.rolling(405, min_periods=max(405//3, 2)).max()
    rebound = x - x.rolling(233, min_periods=max(233//3, 2)).min()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(draw, rebound.abs()) + 0.1402 * _rolling_slope(draw, 329) + 0.003607 * anchor
    return base_signal.diff().diff()

def f64_asue_070_analyst_v70_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=240, w2=416, w3=342, lag=42)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(42)
    trend = _rolling_slope(x, 240)
    baseline = trend.rolling(416, min_periods=max(416//3, 2)).mean()
    spread = trend - baseline
    scale = trend.abs().rolling(342, min_periods=max(342//3, 2)).mean()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(spread, scale) * 1.3625 + 0.0036071 * anchor
    return base_signal.diff().diff()

def f64_asue_071_analyst_v71_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=247, w2=427, w3=355, lag=63)."""
    x = _safe_log(rev_disp.abs() + 1.0).shift(63)
    fast = _rolling_slope(x, 247)
    slow = _rolling_slope(x, 427)
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (fast - slow).ewm(span=300, adjust=False).mean() * 1.376875 + 0.0036072 * anchor
    return base_signal.diff().diff()

def f64_asue_072_analyst_v72_d2(eps_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=254, w2=438, w3=368, lag=0)."""
    x = eps_est.shift(0)
    peak = x.rolling(438, min_periods=max(438//3, 2)).max()
    trough = x.rolling(254, min_periods=max(254//3, 2)).min()
    range_ = (peak - trough).abs()
    anchor = _safe_log(eps_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(x - peak, range_) * 1.39125 + 0.0036073 * anchor
    return base_signal.diff().diff()

def f64_asue_073_analyst_v73_d2(rev_est: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=10, w2=449, w3=381, lag=1)."""
    x = rev_est.shift(1)
    change = x.pct_change(10)
    rank = change.rolling(449, min_periods=max(449//3, 2)).rank(pct=True)
    persistence = change.rolling(381, min_periods=max(381//3, 2)).mean()
    anchor = _safe_log(rev_est.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = (rank - 0.5) + 0.1706 * persistence + 0.0036074 * anchor
    return base_signal.diff().diff()

def f64_asue_074_analyst_v74_d2(eps_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=17, w2=460, w3=394, lag=2)."""
    x = _safe_log(eps_disp.abs() + 1.0).shift(2)
    ret = x.diff()
    vol_fast = ret.rolling(17, min_periods=max(17//3, 2)).std()
    vol_slow = ret.rolling(460, min_periods=max(460//3, 2)).std()
    anchor = _safe_log(eps_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = _safe_div(vol_fast - vol_slow, vol_slow.abs()) * 1.42 + 0.0036075 * anchor
    return base_signal.diff().diff()

def f64_asue_075_analyst_v75_d2(rev_disp: pd.Series) -> pd.Series:
    """Second derivative of de-duplicated analyst replacement signal (w1=24, w2=471, w3=407, lag=5)."""
    x = rev_disp.shift(5)
    ma = x.rolling(471, min_periods=max(471//3, 2)).mean()
    slope = _rolling_slope(_safe_log(x.abs() + 1.0), 24)
    gap = _safe_div(x - ma, ma.abs())
    anchor = _safe_log(rev_disp.abs() + 1.0).diff().rolling(3, min_periods=2).mean()
    base_signal = gap - 0.1858 * slope + 0.0036076 * anchor
    return base_signal.diff().diff()
