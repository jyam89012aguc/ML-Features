"""
58_trading_intensity — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative activity features — acceleration of velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — active vs lull regimes, price-discovery intensity
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _active_day(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True when the day moved: close != prior close OR high != low."""
    moved_close = close != close.shift(1)
    has_range   = (high - low) > 0
    return (moved_close | has_range).astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative (velocity) concept

def tin_drv3_001_active_frac_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day active-day fraction (acceleration of activity)."""
    act = _active_day(close, high, low)
    f21 = _rolling_sum(act, _TD_MON) / _TD_MON
    vel = f21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_002_active_frac_21d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of active-day fraction (jerk)."""
    act   = _active_day(close, high, low)
    f21   = _rolling_sum(act, _TD_MON) / _TD_MON
    vel21 = f21.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_003_vol_per_range_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day vol/range intensity (acceleration)."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    m21 = _rolling_mean(vpr, _TD_MON)
    vel = m21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_004_vxr_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day VxR intensity (acceleration of tape intensity)."""
    rng = high - low
    vxr = volume * rng
    m21 = _rolling_mean(vxr, _TD_MON)
    vel = m21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_005_high_vol_frac_21d_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day high-vol-day fraction."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = (volume > avg252).astype(float)
    f21    = _rolling_sum(cond, _TD_MON) / _TD_MON
    vel    = f21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_006_burst_lull_ratio_21d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in burst/lull ratio (jerk)."""
    avg  = _rolling_mean(volume, _TD_MON)
    high = _rolling_sum((volume > avg).astype(float), _TD_MON)
    low  = _rolling_sum((volume < avg).astype(float), _TD_MON)
    r21  = _safe_div(high, low.replace(0, np.nan))
    vel  = r21.diff(_TD_MON)
    return vel.diff(_TD_WEEK)


def tin_drv3_007_range_expansion_frac_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range-expansion fraction."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    f21   = _rolling_sum(cond, _TD_MON) / _TD_MON
    vel   = f21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_008_discovery_events_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day price-discovery event count."""
    rng    = high - low
    med_r  = _rolling_median(rng, _TD_QTR)
    events = ((close != close.shift(1)) & (rng > med_r)).astype(float)
    c21    = _rolling_sum(events, _TD_MON)
    vel    = c21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_009_vol_trend_slope_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day log-volume OLS slope."""
    log_v = _log_safe(volume)
    slp21 = _linslope(log_v, _TD_MON)
    vel   = slp21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_010_lull_frac_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day lull-regime fraction."""
    avg  = _rolling_mean(volume, _TD_MON)
    lull = ((_active_day(close, high, low) == 0) | (volume < 0.5 * avg)).astype(float)
    f21  = _rolling_sum(lull, _TD_MON) / _TD_MON
    vel  = f21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_011_vxr_zscore_5d_diff_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of VxR z-score (jerk in intensity extremity)."""
    rng = high - low
    vxr = volume * rng
    m   = _rolling_mean(vxr, _TD_YEAR)
    s   = _rolling_std(vxr, _TD_YEAR)
    z   = _safe_div(vxr - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_012_active_frac_5d_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 5-day active-day fraction over 21 days."""
    act = _active_day(close, high, low)
    f5  = _rolling_sum(act, _TD_WEEK) / _TD_WEEK
    slp = _linslope(f5, _TD_MON)
    return slp.diff(_TD_WEEK)


def tin_drv3_013_regime_transition_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day regime-transition count."""
    avg    = _rolling_mean(volume, _TD_MON)
    regime = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(int)
    trans  = (regime != regime.shift(1)).astype(float)
    c21    = _rolling_sum(trans, _TD_MON)
    vel    = c21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_014_vol_roc_5d_21d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 5-day volume ROC (jerk in vol acceleration)."""
    roc5  = _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))
    vel21 = roc5.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_015_active_regime_frac_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day active-regime fraction."""
    avg   = _rolling_mean(volume, _TD_MON)
    act   = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(float)
    f63   = _rolling_sum(act, _TD_QTR) / _TD_QTR
    vel21 = f63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_016_vol_spike_count_21d_5d_diff_5d_diff(volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume-spike count."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > 2.0 * avg).astype(float)
    c21  = _rolling_sum(cond, _TD_MON)
    vel  = c21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_017_range_trend_slope_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day range OLS slope (acceleration of range trend)."""
    rng  = high - low
    slp  = _linslope(rng, _TD_MON)
    vel  = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_018_body_vs_range_21d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day body/range ratio (acceleration of commitment)."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    m21   = _rolling_mean(ratio, _TD_MON)
    vel   = m21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_019_active_frac_ewm21_slope_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of EMA21 of active-day indicator over 63 days."""
    act = _active_day(close, high, low)
    e21 = _ewm_mean(act, _TD_MON)
    slp = _linslope(e21, _TD_QTR)
    return slp.diff(_TD_WEEK)


def tin_drv3_020_vxr_21d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 21-day VxR intensity."""
    rng   = high - low
    vxr   = volume * rng
    m21   = _rolling_mean(vxr, _TD_MON)
    vel21 = m21.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_021_vol_per_range_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day change in 63-day vol/range intensity."""
    rng   = (high - low).replace(0, np.nan)
    vpr   = _safe_div(volume, rng)
    m63   = _rolling_mean(vpr, _TD_QTR)
    vel21 = m63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_022_high_vol_frac_63d_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day high-vol-day fraction."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = (volume > avg252).astype(float)
    f63    = _rolling_sum(cond, _TD_QTR) / _TD_QTR
    vel21  = f63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_023_range_expansion_frac_63d_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day range-expansion fraction."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    f63   = _rolling_sum(cond, _TD_QTR) / _TD_QTR
    vel21 = f63.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def tin_drv3_024_activity_composite_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of composite activity score (acceleration of activity signal)."""
    act    = _active_day(close, high, low)
    f21    = _rolling_mean(act, _TD_MON)
    f21_z  = _safe_div(f21 - _rolling_mean(f21, _TD_YEAR), _rolling_std(f21, _TD_YEAR))

    rng    = (high - low).replace(0, np.nan)
    vpr    = _safe_div(volume, rng)
    vpr21  = _rolling_mean(vpr, _TD_MON)
    vpr_z  = _safe_div(vpr21 - _rolling_mean(vpr21, _TD_YEAR), _rolling_std(vpr21, _TD_YEAR))

    avg252 = _rolling_mean(volume, _TD_YEAR)
    hvf21  = _rolling_sum((volume > avg252).astype(float), _TD_MON) / _TD_MON
    hvf_z  = _safe_div(hvf21 - _rolling_mean(hvf21, _TD_YEAR), _rolling_std(hvf21, _TD_YEAR))

    composite = (f21_z + vpr_z + hvf_z) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def tin_drv3_025_activity_composite_21d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of composite activity score."""
    act    = _active_day(close, high, low)
    f21    = _rolling_mean(act, _TD_MON)
    f21_z  = _safe_div(f21 - _rolling_mean(f21, _TD_YEAR), _rolling_std(f21, _TD_YEAR))

    rng    = (high - low).replace(0, np.nan)
    vpr    = _safe_div(volume, rng)
    vpr21  = _rolling_mean(vpr, _TD_MON)
    vpr_z  = _safe_div(vpr21 - _rolling_mean(vpr21, _TD_YEAR), _rolling_std(vpr21, _TD_YEAR))

    avg252 = _rolling_mean(volume, _TD_YEAR)
    hvf21  = _rolling_sum((volume > avg252).astype(float), _TD_MON) / _TD_MON
    hvf_z  = _safe_div(hvf21 - _rolling_mean(hvf21, _TD_YEAR), _rolling_std(hvf21, _TD_YEAR))

    composite = (f21_z + vpr_z + hvf_z) / 3.0
    vel21 = composite.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

TRADING_INTENSITY_REGISTRY_3RD_DERIVATIVES = {
    "tin_drv3_001_active_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_001_active_frac_21d_5d_diff_5d_diff},
    "tin_drv3_002_active_frac_21d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_002_active_frac_21d_21d_diff_5d_diff},
    "tin_drv3_003_vol_per_range_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_003_vol_per_range_21d_5d_diff_5d_diff},
    "tin_drv3_004_vxr_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "volume"], "func": tin_drv3_004_vxr_21d_5d_diff_5d_diff},
    "tin_drv3_005_high_vol_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tin_drv3_005_high_vol_frac_21d_5d_diff_5d_diff},
    "tin_drv3_006_burst_lull_ratio_21d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tin_drv3_006_burst_lull_ratio_21d_21d_diff_5d_diff},
    "tin_drv3_007_range_expansion_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_007_range_expansion_frac_21d_5d_diff_5d_diff},
    "tin_drv3_008_discovery_events_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_008_discovery_events_21d_5d_diff_5d_diff},
    "tin_drv3_009_vol_trend_slope_5d_diff_5d_diff": {"inputs": ["volume"], "func": tin_drv3_009_vol_trend_slope_5d_diff_5d_diff},
    "tin_drv3_010_lull_frac_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_010_lull_frac_21d_5d_diff_5d_diff},
    "tin_drv3_011_vxr_zscore_5d_diff_5d_diff": {"inputs": ["high", "low", "volume"], "func": tin_drv3_011_vxr_zscore_5d_diff_5d_diff},
    "tin_drv3_012_active_frac_5d_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_012_active_frac_5d_slope_5d_diff},
    "tin_drv3_013_regime_transition_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_013_regime_transition_21d_5d_diff_5d_diff},
    "tin_drv3_014_vol_roc_5d_21d_diff_5d_diff": {"inputs": ["volume"], "func": tin_drv3_014_vol_roc_5d_21d_diff_5d_diff},
    "tin_drv3_015_active_regime_frac_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_015_active_regime_frac_63d_21d_diff_5d_diff},
    "tin_drv3_016_vol_spike_count_21d_5d_diff_5d_diff": {"inputs": ["volume"], "func": tin_drv3_016_vol_spike_count_21d_5d_diff_5d_diff},
    "tin_drv3_017_range_trend_slope_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": tin_drv3_017_range_trend_slope_5d_diff_5d_diff},
    "tin_drv3_018_body_vs_range_21d_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": tin_drv3_018_body_vs_range_21d_5d_diff_5d_diff},
    "tin_drv3_019_active_frac_ewm21_slope_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_019_active_frac_ewm21_slope_5d_diff},
    "tin_drv3_020_vxr_21d_21d_diff_5d_diff": {"inputs": ["high", "low", "volume"], "func": tin_drv3_020_vxr_21d_21d_diff_5d_diff},
    "tin_drv3_021_vol_per_range_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_021_vol_per_range_63d_21d_diff_5d_diff},
    "tin_drv3_022_high_vol_frac_63d_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": tin_drv3_022_high_vol_frac_63d_21d_diff_5d_diff},
    "tin_drv3_023_range_expansion_frac_63d_21d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv3_023_range_expansion_frac_63d_21d_diff_5d_diff},
    "tin_drv3_024_activity_composite_5d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_024_activity_composite_5d_diff_5d_diff},
    "tin_drv3_025_activity_composite_21d_diff_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv3_025_activity_composite_21d_diff_5d_diff},
}
