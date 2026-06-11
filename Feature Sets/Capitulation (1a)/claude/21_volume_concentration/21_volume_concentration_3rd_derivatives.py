"""
21_volume_concentration — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative concentration features — acceleration of velocity
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


def _topn_share(arr: np.ndarray, n: int) -> float:
    """Share of total held by top-n values."""
    total = arr.sum()
    if total <= 0:
        return np.nan
    top = np.partition(arr, -min(n, len(arr)))[-min(n, len(arr)):]
    return float(top.sum() / total)


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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept

def vcc_drv3_001_hhi_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day HHI (acceleration of concentration velocity)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    vel = hhi.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_002_hhi_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21-day HHI."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    vel = hhi.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_003_gini_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Gini (acceleration of inequality velocity)."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    vel = g.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_004_gini_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 21-day Gini."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    vel = g.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_005_entropy_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day entropy (acceleration of entropy change)."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    vel = ent.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_006_top1_share_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day top-1 share."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_007_top3_share_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day top-3 share."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    vel = r.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_008_cv_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day CV (acceleration of dispersion velocity)."""
    cv = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)
    vel = cv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_009_hhi_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day HHI (rate of slope change)."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    slp = _linslope(hhi, _TD_MON)
    return slp.diff(_TD_WEEK)


def vcc_drv3_010_gini_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day Gini."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    slp = _linslope(g, _TD_MON)
    return slp.diff(_TD_WEEK)


def vcc_drv3_011_entropy_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day entropy."""
    ent = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _entropy, raw=True)
    slp = _linslope(ent, _TD_MON)
    return slp.diff(_TD_WEEK)


def vcc_drv3_012_down_day_vol_share_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down-day volume share."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_013_concentration_index_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day concentration composite."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    ci = (h * _TD_MON + g + t) / 3.0
    vel = ci.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_014_concentration_index_21d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in concentration composite."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    ci = (h * _TD_MON + g + t) / 3.0
    vel = ci.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_015_hhi_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day HHI."""
    hhi = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _herfindahl, raw=True)
    vel = hhi.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_016_gini_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day Gini."""
    g = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _gini, raw=True)
    vel = g.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_017_entropy_63d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day entropy."""
    ent = volume.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(
        _entropy, raw=True)
    vel = ent.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def vcc_drv3_018_high_vol_share_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day high-vol-day share (>2x mean of total)."""
    mean21 = _rolling_mean(volume, _TD_MON)
    high_vol = volume.where(volume > 2.0 * mean21, 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    s = _safe_div(_rolling_sum(high_vol, _TD_MON), tot)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_019_max_day_ratio_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day max-day-to-total ratio."""
    mx = _rolling_max(volume, _TD_MON)
    tot = _rolling_sum(volume, _TD_MON)
    r = _safe_div(mx, tot)
    vel = r.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def vcc_drv3_020_top1_share_21d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day top-1 share over 63-day window."""
    r = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 1), raw=True)
    slp = _linslope(r, _TD_QTR)
    return slp.diff(_TD_WEEK)


def vcc_drv3_021_cv_21d_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day CV over trailing 21 days."""
    cv = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _cv, raw=True)
    slp = _linslope(cv, _TD_MON)
    return slp.diff(_TD_WEEK)


def vcc_drv3_022_hhi_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day HHI."""
    hhi = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    vel = hhi.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcc_drv3_023_gini_21d_5d_diff_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day Gini."""
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    vel = g.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def vcc_drv3_024_down_day_vol_share_21d_diff_slope(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day-velocity of down-day vol share."""
    down_vol = volume.where(close < close.shift(1), 0.0)
    tot = _rolling_sum(volume, _TD_MON)
    dn_tot = _rolling_sum(down_vol, _TD_MON)
    s = _safe_div(dn_tot, tot)
    vel = s.diff(_TD_MON)
    return _linslope(vel, _TD_MON)


def vcc_drv3_025_concentration_index_21d_slope_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21d concentration composite over 21 days."""
    h = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _herfindahl, raw=True)
    g = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        _gini, raw=True)
    t = volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(
        lambda a: _topn_share(a, 3), raw=True)
    ci = (h * _TD_MON + g + t) / 3.0
    slp = _linslope(ci, _TD_MON)
    return slp.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_CONCENTRATION_REGISTRY_3RD_DERIVATIVES = {
    "vcc_drv3_001_hhi_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_001_hhi_21d_5d_diff_5d_diff},
    "vcc_drv3_002_hhi_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_002_hhi_21d_21d_diff_5d_diff},
    "vcc_drv3_003_gini_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_003_gini_21d_5d_diff_5d_diff},
    "vcc_drv3_004_gini_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_004_gini_21d_21d_diff_5d_diff},
    "vcc_drv3_005_entropy_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_005_entropy_21d_5d_diff_5d_diff},
    "vcc_drv3_006_top1_share_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_006_top1_share_21d_5d_diff_5d_diff},
    "vcc_drv3_007_top3_share_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_007_top3_share_21d_21d_diff_5d_diff},
    "vcc_drv3_008_cv_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_008_cv_21d_5d_diff_5d_diff},
    "vcc_drv3_009_hhi_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_009_hhi_21d_slope_21d_5d_diff},
    "vcc_drv3_010_gini_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_010_gini_21d_slope_21d_5d_diff},
    "vcc_drv3_011_entropy_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_011_entropy_21d_slope_21d_5d_diff},
    "vcc_drv3_012_down_day_vol_share_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": vcc_drv3_012_down_day_vol_share_5d_diff_5d_diff},
    "vcc_drv3_013_concentration_index_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_013_concentration_index_21d_5d_diff_5d_diff},
    "vcc_drv3_014_concentration_index_21d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_014_concentration_index_21d_21d_diff_5d_diff},
    "vcc_drv3_015_hhi_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_015_hhi_63d_21d_diff_5d_diff},
    "vcc_drv3_016_gini_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_016_gini_63d_21d_diff_5d_diff},
    "vcc_drv3_017_entropy_63d_21d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_017_entropy_63d_21d_diff_5d_diff},
    "vcc_drv3_018_high_vol_share_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_018_high_vol_share_21d_5d_diff_5d_diff},
    "vcc_drv3_019_max_day_ratio_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_019_max_day_ratio_21d_5d_diff_5d_diff},
    "vcc_drv3_020_top1_share_21d_slope_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_020_top1_share_21d_slope_5d_diff},
    "vcc_drv3_021_cv_21d_slope_21d_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_021_cv_21d_slope_21d_5d_diff},
    "vcc_drv3_022_hhi_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vcc_drv3_022_hhi_21d_5d_diff_slope_21d},
    "vcc_drv3_023_gini_21d_5d_diff_slope_21d": {"inputs": ["volume"], "func": vcc_drv3_023_gini_21d_5d_diff_slope_21d},
    "vcc_drv3_024_down_day_vol_share_21d_diff_slope": {"inputs": ["close", "volume"], "func": vcc_drv3_024_down_day_vol_share_21d_diff_slope},
    "vcc_drv3_025_concentration_index_21d_slope_5d_diff": {"inputs": ["volume"], "func": vcc_drv3_025_concentration_index_21d_slope_5d_diff},
}
