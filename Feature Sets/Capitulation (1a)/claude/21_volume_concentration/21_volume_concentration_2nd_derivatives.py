"""
21_volume_concentration — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base volume-concentration features — velocity of concentration shifts
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _topn_share(arr: np.ndarray, n: int) -> float:
    """Share of total held by top-n values."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    top = np.partition(arr, -min(n, len(arr)))[-min(n, len(arr)):]
    return float(top.sum() / total)


def _herfindahl(arr: np.ndarray) -> float:
    """Herfindahl index of volume shares."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    shares = arr / total
    return float((shares ** 2).sum())


def _gini(arr: np.ndarray) -> float:
    """Gini coefficient of volume distribution."""
    n = len(arr)
    if n < 2:
        return np.nan
    s = arr.sum()
    if s <= 0:
        return np.nan
    sorted_a = np.sort(arr)
    idx = np.arange(1, n + 1)
    return float((2 * (idx * sorted_a).sum() - (n + 1) * s) / (n * s))


def _entropy(arr: np.ndarray) -> float:
    """Shannon entropy (nats) of volume shares."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    shares = arr / total
    shares = shares[shares > 0]
    return float(-(shares * np.log(shares)).sum())


def _cv(arr: np.ndarray) -> float:
    """Coefficient of variation of arr."""
    m = arr.mean()
    if m <= 0:
        return np.nan
    return float(arr.std() / m)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vcc_drv2_001_hhi_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day HHI (velocity of short-run concentration change)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return hhi.diff(_TD_WEEK)


def vcc_drv2_002_hhi_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day HHI (monthly velocity of concentration)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return hhi.diff(_TD_MON)


def vcc_drv2_003_hhi_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day HHI (monthly change in medium-run concentration)."""
    hhi = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _herfindahl, raw=True)
    return hhi.diff(_TD_MON)


def vcc_drv2_004_gini_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day Gini coefficient."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return g.diff(_TD_WEEK)


def vcc_drv2_005_gini_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day Gini (monthly change in volume inequality)."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return g.diff(_TD_MON)


def vcc_drv2_006_gini_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day Gini (monthly change in medium-run inequality)."""
    g = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)
    return g.diff(_TD_MON)


def vcc_drv2_007_entropy_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day entropy (velocity of diversification change)."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    return ent.diff(_TD_WEEK)


def vcc_drv2_008_entropy_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day entropy (monthly change in medium-run entropy)."""
    ent = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy, raw=True)
    return ent.diff(_TD_MON)


def vcc_drv2_009_top1_share_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day top-1 volume share."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return r.diff(_TD_WEEK)


def vcc_drv2_010_top3_share_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day top-3 volume share."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    return r.diff(_TD_MON)


def vcc_drv2_011_top5_share_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day top-5 volume share."""
    r = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    return r.diff(_TD_MON)


def vcc_drv2_012_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day coefficient of variation."""
    cv = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)
    return cv.diff(_TD_WEEK)


def vcc_drv2_013_cv_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day coefficient of variation."""
    cv = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _cv, raw=True)
    return cv.diff(_TD_MON)


def vcc_drv2_014_down_day_vol_share_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down-day volume share (velocity of selling concentration)."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    return s.diff(_TD_WEEK)


def vcc_drv2_015_down_day_vol_share_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day down-day volume share."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    return s.diff(_TD_MON)


def vcc_drv2_016_hhi_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day HHI over trailing 21 days."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return _linslope(hhi, _TD_MON)


def vcc_drv2_017_hhi_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day HHI over trailing 63 days."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return _linslope(hhi, _TD_QTR)


def vcc_drv2_018_gini_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day Gini over trailing 21 days."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return _linslope(g, _TD_MON)


def vcc_drv2_019_entropy_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day entropy over trailing 21 days."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    return _linslope(ent, _TD_MON)


def vcc_drv2_020_top1_share_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day top-1 share over trailing 63 days."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return _linslope(r, _TD_QTR)


def vcc_drv2_021_concentration_index_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day concentration composite (HHI+Gini+top3 avg)."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    ci = (h * _TD_MON + g + t) / 3.0
    return ci.diff(_TD_WEEK)


def vcc_drv2_022_concentration_index_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day concentration composite."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    ci = (h * _TD_MON + g + t) / 3.0
    return ci.diff(_TD_MON)


def vcc_drv2_023_high_vol_share_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day high-volume-day share (>2x mean fraction of total)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    high_vol = volume.where(volume > 2.0 * mean21, 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    s = _safe_div(_rolling_sum(high_vol, _TD_MON), tot)
    return s.diff(_TD_WEEK)


def vcc_drv2_024_max_day_ratio_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day max-day-to-total-volume ratio."""
    mx = _rolling_max(volume, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    r = _safe_div(mx, tot)
    return r.diff(_TD_WEEK)


def vcc_drv2_025_down_day_hhi_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-day HHI (velocity of panic concentration)."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    hhi = down_vol.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)
    return hhi.diff(_TD_MON)


# --- 2nd Derivatives drv2_026-075 ---

def vcc_drv2_026_hhi_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day HHI (monthly velocity of long-run concentration)."""
    hhi = volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _herfindahl, raw=True)
    return hhi.diff(_TD_MON)


def vcc_drv2_027_hhi_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day HHI (monthly velocity of annual concentration)."""
    hhi = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _herfindahl, raw=True)
    return hhi.diff(_TD_MON)


def vcc_drv2_028_gini_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day Gini (weekly velocity of medium-run inequality)."""
    g = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)
    return g.diff(_TD_WEEK)


def vcc_drv2_029_gini_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day Gini (monthly change in long-run inequality)."""
    g = volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _gini, raw=True)
    return g.diff(_TD_MON)


def vcc_drv2_030_entropy_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day entropy (monthly change in short-run entropy)."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    return ent.diff(_TD_MON)


def vcc_drv2_031_entropy_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day entropy (monthly change in long-run diversity)."""
    ent = volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _entropy, raw=True)
    return ent.diff(_TD_MON)


def vcc_drv2_032_top1_share_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day top-1 share (monthly velocity of medium-run spike)."""
    r = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return r.diff(_TD_MON)


def vcc_drv2_033_top5_share_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day top-5 share (weekly velocity of short-run concentration)."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    return r.diff(_TD_WEEK)


def vcc_drv2_034_cv_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day CV (monthly change in long-run dispersion)."""
    cv = volume.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).apply(
        _cv, raw=True)
    return cv.diff(_TD_MON)


def vcc_drv2_035_max_day_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day max-day-to-total ratio (monthly change in spike dominance)."""
    mx = _rolling_max(volume, _TD_QTR)
    tot = _rolling_sum(volume, _TD_QTR)
    r = _safe_div(mx, tot)
    return r.diff(_TD_MON)


def vcc_drv2_036_max_day_ratio_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day max-day-to-total ratio."""
    mx = _rolling_max(volume, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    r = _safe_div(mx, tot)
    return r.diff(_TD_MON)


def vcc_drv2_037_down_day_vol_share_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day down-day volume share (medium-run selling concentration velocity)."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_QTR)
    dn_tot = _rolling_sum(down_vol, _TD_QTR)
    s = _safe_div(dn_tot, tot)
    return s.diff(_TD_MON)


def vcc_drv2_038_up_day_vol_share_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day up-day volume share (velocity of buying concentration)."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    up_tot = _rolling_sum(up_vol, _TD_MON)
    s = _safe_div(up_tot, tot)
    return s.diff(_TD_WEEK)


def vcc_drv2_039_hhi_21d_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day HHI over trailing 126 days (long-run concentration trend)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return _linslope(hhi, _TD_HALF)


def vcc_drv2_040_gini_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day Gini over trailing 63 days."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return _linslope(g, _TD_QTR)


def vcc_drv2_041_entropy_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day entropy over trailing 63 days."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    return _linslope(ent, _TD_QTR)


def vcc_drv2_042_top3_share_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day top-3 share over trailing 21 days."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    return _linslope(r, _TD_MON)


def vcc_drv2_043_cv_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day CV over trailing 21 days."""
    cv = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)
    return _linslope(cv, _TD_MON)


def vcc_drv2_044_cv_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day CV over trailing 63 days."""
    cv = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)
    return _linslope(cv, _TD_QTR)


def vcc_drv2_045_concentration_index_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21d concentration composite over trailing 63 days."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    ci = (h * _TD_MON + g + t) / 3.0
    return _linslope(ci, _TD_QTR)


def vcc_drv2_046_hhi_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day HHI (quarterly velocity of short-run concentration)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    return hhi.diff(_TD_QTR)


def vcc_drv2_047_gini_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day Gini (quarterly change in short-run inequality)."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    return g.diff(_TD_QTR)


def vcc_drv2_048_entropy_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day entropy (quarterly change in diversity)."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    return ent.diff(_TD_QTR)


def vcc_drv2_049_top1_share_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day top-1 share (quarterly change in daily spike dominance)."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    return r.diff(_TD_QTR)


def vcc_drv2_050_cv_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day CV (quarterly change in short-run dispersion)."""
    cv = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)
    return cv.diff(_TD_QTR)


def vcc_drv2_051_down_day_vol_share_21d_63d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day down-day volume share."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    return s.diff(_TD_QTR)


def vcc_drv2_052_high_vol_share_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d high-vol-day share (>2x mean) — monthly velocity."""
    mean21 = _rolling_mean(volume, _TD_MON)
    high_vol = volume.where(volume > 2.0 * mean21, 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    s = _safe_div(_rolling_sum(high_vol, _TD_MON), tot)
    return s.diff(_TD_MON)


def vcc_drv2_053_max_day_ratio_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day max-day ratio over trailing 21 days."""
    mx = _rolling_max(volume, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    r = _safe_div(mx, tot)
    return _linslope(r, _TD_MON)


def vcc_drv2_054_max_day_ratio_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day max-day ratio over trailing 63 days."""
    mx = _rolling_max(volume, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    r = _safe_div(mx, tot)
    return _linslope(r, _TD_QTR)


def vcc_drv2_055_down_day_vol_share_21d_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-day vol share over trailing 21 days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    return _linslope(s, _TD_MON)


def vcc_drv2_056_down_day_vol_share_21d_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day down-day vol share over trailing 63 days."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    return _linslope(s, _TD_QTR)


def vcc_drv2_057_hhi_21d_ewm_diff_21d(volume: pd.Series) -> pd.Series:
    """21-day diff of EWM(span=21) of 21-day HHI (smoothed velocity)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    ewm_hhi = hhi.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return ewm_hhi.diff(_TD_MON)


def vcc_drv2_058_gini_21d_ewm_diff_21d(volume: pd.Series) -> pd.Series:
    """21-day diff of EWM(span=21) of 21-day Gini."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    ewm_g = g.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return ewm_g.diff(_TD_MON)


def vcc_drv2_059_top5_share_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day top-5 share (weekly velocity of medium-run concentration)."""
    r = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    return r.diff(_TD_WEEK)


def vcc_drv2_060_pareto_top20pct_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21d top-20%-share (weekly velocity of Pareto concentration)."""
    def _par20(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        k = max(1, int(np.ceil(n * 0.20)))
        top = np.partition(arr, -k)[-k:]
        total = arr.sum()
        if total <= 0:
            return np.nan
        return float(top.sum() / total)
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_par20, raw=True)
    return r.diff(_TD_WEEK)


def vcc_drv2_061_pareto_top20pct_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21d top-20%-share (monthly velocity of Pareto concentration)."""
    def _par20(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        k = max(1, int(np.ceil(n * 0.20)))
        top = np.partition(arr, -k)[-k:]
        total = arr.sum()
        if total <= 0:
            return np.nan
        return float(top.sum() / total)
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_par20, raw=True)
    return r.diff(_TD_MON)


def vcc_drv2_062_hhi_21d_vs_252d_ratio_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of ratio of 21-day to 252-day HHI (velocity of relative concentration)."""
    hhi21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    hhi252 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _herfindahl, raw=True)
    r = _safe_div(hhi21, hhi252)
    return r.diff(_TD_WEEK)


def vcc_drv2_063_gini_21d_vs_252d_ratio_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of ratio of 21-day Gini to 252-day Gini."""
    g21 = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    g252 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(
        _gini, raw=True)
    r = _safe_div(g21, g252)
    return r.diff(_TD_MON)


def vcc_drv2_064_entropy_deficit_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day entropy deficit (velocity of lost diversity)."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    deficit = np.log(_TD_MON) - ent
    return deficit.diff(_TD_WEEK)


def vcc_drv2_065_entropy_deficit_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day entropy deficit."""
    ent = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy, raw=True)
    deficit = np.log(_TD_QTR) - ent
    return deficit.diff(_TD_MON)


def vcc_drv2_066_up_day_vol_share_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day up-day volume share."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    up_tot = _rolling_sum(up_vol, _TD_MON)
    s = _safe_div(up_tot, tot)
    return s.diff(_TD_MON)


def vcc_drv2_067_down_vs_up_vol_ratio_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day down/up volume share ratio."""
    dn = volume.where(close < close.shift(1), 0.0)
    up = volume.where(close > close.shift(1), 0.0)
    dn_tot = _rolling_sum(dn, _TD_MON)
    up_tot = _rolling_sum(up, _TD_MON)
    r = _safe_div(dn_tot, up_tot)
    return r.diff(_TD_WEEK)


def vcc_drv2_068_concentration_index_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day concentration composite (monthly velocity)."""
    h = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    ci = (h * _TD_QTR + g + t) / 3.0
    return ci.diff(_TD_MON)


def vcc_drv2_069_concentration_index_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day concentration composite."""
    h = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        lambda a: _topn_share(a, 5), raw=True)
    ci = (h * _TD_QTR + g + t) / 3.0
    return ci.diff(_TD_WEEK)


def vcc_drv2_070_hhi_21d_5d_diff_ewm21(volume: pd.Series) -> pd.Series:
    """EWM(span=21) of 5-day diff of 21-day HHI (smoothed velocity of concentration)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    vel = hhi.diff(_TD_WEEK)
    return vel.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vcc_drv2_071_gini_21d_5d_diff_ewm21(volume: pd.Series) -> pd.Series:
    """EWM(span=21) of 5-day diff of 21-day Gini (smoothed inequality velocity)."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    vel = g.diff(_TD_WEEK)
    return vel.ewm(span=_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vcc_drv2_072_top3_share_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day top-3 share over trailing 63 days."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    return _linslope(r, _TD_QTR)


def vcc_drv2_073_down_day_gini_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day down-day Gini (monthly change in panic inequality)."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    g = down_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _gini(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)
    return g.diff(_TD_MON)


def vcc_drv2_074_up_day_hhi_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day up-day HHI (velocity of buying concentration)."""
    up_vol = volume.where(close > close.shift(1), 0.0)
    hhi = up_vol.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _herfindahl(a[a > 0]) if (a > 0).sum() > 1 else np.nan, raw=True)
    return hhi.diff(_TD_MON)


def vcc_drv2_075_vol_skewness_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume skewness (velocity of distributional skew)."""
    sk = volume.rolling(_TD_MON, min_periods=max(3, _TD_MON // 2)).skew()
    return sk.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CONCENTRATION_REGISTRY_2ND_DERIVATIVES = {
    "vcc_drv2_001_hhi_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_001_hhi_21d_5d_diff},
    "vcc_drv2_002_hhi_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_002_hhi_21d_21d_diff},
    "vcc_drv2_003_hhi_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_003_hhi_63d_21d_diff},
    "vcc_drv2_004_gini_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_004_gini_21d_5d_diff},
    "vcc_drv2_005_gini_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_005_gini_21d_21d_diff},
    "vcc_drv2_006_gini_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_006_gini_63d_21d_diff},
    "vcc_drv2_007_entropy_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_007_entropy_21d_5d_diff},
    "vcc_drv2_008_entropy_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_008_entropy_63d_21d_diff},
    "vcc_drv2_009_top1_share_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_009_top1_share_21d_5d_diff},
    "vcc_drv2_010_top3_share_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_010_top3_share_21d_21d_diff},
    "vcc_drv2_011_top5_share_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_011_top5_share_63d_21d_diff},
    "vcc_drv2_012_cv_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_012_cv_21d_5d_diff},
    "vcc_drv2_013_cv_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_013_cv_63d_21d_diff},
    "vcc_drv2_014_down_day_vol_share_21d_5d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_014_down_day_vol_share_21d_5d_diff},
    "vcc_drv2_015_down_day_vol_share_21d_21d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_015_down_day_vol_share_21d_21d_diff},
    "vcc_drv2_016_hhi_21d_slope_21d": {"inputs": ["volume"], "func": vcc_drv2_016_hhi_21d_slope_21d},
    "vcc_drv2_017_hhi_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_017_hhi_21d_slope_63d},
    "vcc_drv2_018_gini_21d_slope_21d": {"inputs": ["volume"], "func": vcc_drv2_018_gini_21d_slope_21d},
    "vcc_drv2_019_entropy_21d_slope_21d": {"inputs": ["volume"], "func": vcc_drv2_019_entropy_21d_slope_21d},
    "vcc_drv2_020_top1_share_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_020_top1_share_21d_slope_63d},
    "vcc_drv2_021_concentration_index_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_021_concentration_index_21d_5d_diff},
    "vcc_drv2_022_concentration_index_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_022_concentration_index_21d_21d_diff},
    "vcc_drv2_023_high_vol_share_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_023_high_vol_share_21d_5d_diff},
    "vcc_drv2_024_max_day_ratio_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_024_max_day_ratio_21d_5d_diff},
    "vcc_drv2_025_down_day_hhi_63d_21d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_025_down_day_hhi_63d_21d_diff},
    "vcc_drv2_026_hhi_126d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_026_hhi_126d_21d_diff},
    "vcc_drv2_027_hhi_252d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_027_hhi_252d_21d_diff},
    "vcc_drv2_028_gini_63d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_028_gini_63d_5d_diff},
    "vcc_drv2_029_gini_126d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_029_gini_126d_21d_diff},
    "vcc_drv2_030_entropy_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_030_entropy_21d_21d_diff},
    "vcc_drv2_031_entropy_126d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_031_entropy_126d_21d_diff},
    "vcc_drv2_032_top1_share_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_032_top1_share_63d_21d_diff},
    "vcc_drv2_033_top5_share_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_033_top5_share_21d_5d_diff},
    "vcc_drv2_034_cv_126d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_034_cv_126d_21d_diff},
    "vcc_drv2_035_max_day_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_035_max_day_ratio_63d_21d_diff},
    "vcc_drv2_036_max_day_ratio_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_036_max_day_ratio_21d_21d_diff},
    "vcc_drv2_037_down_day_vol_share_63d_21d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_037_down_day_vol_share_63d_21d_diff},
    "vcc_drv2_038_up_day_vol_share_21d_5d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_038_up_day_vol_share_21d_5d_diff},
    "vcc_drv2_039_hhi_21d_slope_126d": {"inputs": ["volume"], "func": vcc_drv2_039_hhi_21d_slope_126d},
    "vcc_drv2_040_gini_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_040_gini_21d_slope_63d},
    "vcc_drv2_041_entropy_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_041_entropy_21d_slope_63d},
    "vcc_drv2_042_top3_share_21d_slope_21d": {"inputs": ["volume"], "func": vcc_drv2_042_top3_share_21d_slope_21d},
    "vcc_drv2_043_cv_21d_slope_21d": {"inputs": ["volume"], "func": vcc_drv2_043_cv_21d_slope_21d},
    "vcc_drv2_044_cv_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_044_cv_21d_slope_63d},
    "vcc_drv2_045_concentration_index_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_045_concentration_index_21d_slope_63d},
    "vcc_drv2_046_hhi_21d_63d_diff": {"inputs": ["volume"], "func": vcc_drv2_046_hhi_21d_63d_diff},
    "vcc_drv2_047_gini_21d_63d_diff": {"inputs": ["volume"], "func": vcc_drv2_047_gini_21d_63d_diff},
    "vcc_drv2_048_entropy_21d_63d_diff": {"inputs": ["volume"], "func": vcc_drv2_048_entropy_21d_63d_diff},
    "vcc_drv2_049_top1_share_21d_63d_diff": {"inputs": ["volume"], "func": vcc_drv2_049_top1_share_21d_63d_diff},
    "vcc_drv2_050_cv_21d_63d_diff": {"inputs": ["volume"], "func": vcc_drv2_050_cv_21d_63d_diff},
    "vcc_drv2_051_down_day_vol_share_21d_63d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_051_down_day_vol_share_21d_63d_diff},
    "vcc_drv2_052_high_vol_share_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_052_high_vol_share_21d_21d_diff},
    "vcc_drv2_053_max_day_ratio_21d_slope_21d": {"inputs": ["volume"], "func": vcc_drv2_053_max_day_ratio_21d_slope_21d},
    "vcc_drv2_054_max_day_ratio_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_054_max_day_ratio_21d_slope_63d},
    "vcc_drv2_055_down_day_vol_share_21d_slope_21d": {"inputs": ["close", "volume"], "func": vcc_drv2_055_down_day_vol_share_21d_slope_21d},
    "vcc_drv2_056_down_day_vol_share_21d_slope_63d": {"inputs": ["close", "volume"], "func": vcc_drv2_056_down_day_vol_share_21d_slope_63d},
    "vcc_drv2_057_hhi_21d_ewm_diff_21d": {"inputs": ["volume"], "func": vcc_drv2_057_hhi_21d_ewm_diff_21d},
    "vcc_drv2_058_gini_21d_ewm_diff_21d": {"inputs": ["volume"], "func": vcc_drv2_058_gini_21d_ewm_diff_21d},
    "vcc_drv2_059_top5_share_63d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_059_top5_share_63d_5d_diff},
    "vcc_drv2_060_pareto_top20pct_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_060_pareto_top20pct_21d_5d_diff},
    "vcc_drv2_061_pareto_top20pct_21d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_061_pareto_top20pct_21d_21d_diff},
    "vcc_drv2_062_hhi_21d_vs_252d_ratio_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_062_hhi_21d_vs_252d_ratio_5d_diff},
    "vcc_drv2_063_gini_21d_vs_252d_ratio_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_063_gini_21d_vs_252d_ratio_21d_diff},
    "vcc_drv2_064_entropy_deficit_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_064_entropy_deficit_21d_5d_diff},
    "vcc_drv2_065_entropy_deficit_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_065_entropy_deficit_63d_21d_diff},
    "vcc_drv2_066_up_day_vol_share_21d_21d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_066_up_day_vol_share_21d_21d_diff},
    "vcc_drv2_067_down_vs_up_vol_ratio_21d_5d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_067_down_vs_up_vol_ratio_21d_5d_diff},
    "vcc_drv2_068_concentration_index_63d_21d_diff": {"inputs": ["volume"], "func": vcc_drv2_068_concentration_index_63d_21d_diff},
    "vcc_drv2_069_concentration_index_63d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_069_concentration_index_63d_5d_diff},
    "vcc_drv2_070_hhi_21d_5d_diff_ewm21": {"inputs": ["volume"], "func": vcc_drv2_070_hhi_21d_5d_diff_ewm21},
    "vcc_drv2_071_gini_21d_5d_diff_ewm21": {"inputs": ["volume"], "func": vcc_drv2_071_gini_21d_5d_diff_ewm21},
    "vcc_drv2_072_top3_share_21d_slope_63d": {"inputs": ["volume"], "func": vcc_drv2_072_top3_share_21d_slope_63d},
    "vcc_drv2_073_down_day_gini_21d_21d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_073_down_day_gini_21d_21d_diff},
    "vcc_drv2_074_up_day_hhi_21d_21d_diff": {"inputs": ["close", "volume"], "func": vcc_drv2_074_up_day_hhi_21d_21d_diff},
    "vcc_drv2_075_vol_skewness_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv2_075_vol_skewness_21d_5d_diff},
}
