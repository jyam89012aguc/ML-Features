"""
58_trading_intensity — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base trading-intensity features — velocity of activity
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def tin_drv2_001_active_frac_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day active-day fraction (velocity of activity change)."""
    act = _active_day(close, high, low)
    f21 = _rolling_sum(act, _TD_MON) / _TD_MON
    return f21.diff(_TD_WEEK)


def tin_drv2_002_active_frac_21d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 21-day active-day fraction (monthly velocity)."""
    act = _active_day(close, high, low)
    f21 = _rolling_sum(act, _TD_MON) / _TD_MON
    return f21.diff(_TD_MON)


def tin_drv2_003_vol_per_range_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day vol/range intensity."""
    rng  = (high - low).replace(0, np.nan)
    vpr  = _safe_div(volume, rng)
    m21  = _rolling_mean(vpr, _TD_MON)
    return m21.diff(_TD_WEEK)


def tin_drv2_004_vol_per_range_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day vol/range intensity."""
    rng = (high - low).replace(0, np.nan)
    vpr = _safe_div(volume, rng)
    m63 = _rolling_mean(vpr, _TD_QTR)
    return m63.diff(_TD_MON)


def tin_drv2_005_high_vol_frac_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day high-vol-day fraction."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = (volume > avg252).astype(float)
    f21    = _rolling_sum(cond, _TD_MON) / _TD_MON
    return f21.diff(_TD_WEEK)


def tin_drv2_006_burst_lull_ratio_21d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day burst/lull ratio."""
    avg  = _rolling_mean(volume, _TD_MON)
    high = _rolling_sum((volume > avg).astype(float), _TD_MON)
    low  = _rolling_sum((volume < avg).astype(float), _TD_MON)
    r21  = _safe_div(high, low.replace(0, np.nan))
    return r21.diff(_TD_MON)


def tin_drv2_007_vxr_21d_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day VxR (volume times range) intensity."""
    rng  = high - low
    vxr  = volume * rng
    m21  = _rolling_mean(vxr, _TD_MON)
    return m21.diff(_TD_WEEK)


def tin_drv2_008_vxr_63d_21d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day VxR intensity."""
    rng = high - low
    vxr = volume * rng
    m63 = _rolling_mean(vxr, _TD_QTR)
    return m63.diff(_TD_MON)


def tin_drv2_009_range_expansion_frac_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day range-expansion fraction."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    f21   = _rolling_sum(cond, _TD_MON) / _TD_MON
    return f21.diff(_TD_WEEK)


def tin_drv2_010_discovery_events_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day price-discovery event count."""
    rng    = high - low
    med_r  = _rolling_median(rng, _TD_QTR)
    events = ((close != close.shift(1)) & (rng > med_r)).astype(float)
    c21    = _rolling_sum(events, _TD_MON)
    return c21.diff(_TD_WEEK)


def tin_drv2_011_active_frac_5d_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 5-day active-day fraction over trailing 21 days."""
    act = _active_day(close, high, low)
    f5  = _rolling_sum(act, _TD_WEEK) / _TD_WEEK
    return _linslope(f5, _TD_MON)


def tin_drv2_012_vol_trend_slope_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-volume OLS slope."""
    log_v = _log_safe(volume)
    slp21 = _linslope(log_v, _TD_MON)
    return slp21.diff(_TD_WEEK)


def tin_drv2_013_range_trend_slope_21d_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day range OLS slope."""
    rng   = high - low
    slp21 = _linslope(rng, _TD_MON)
    return slp21.diff(_TD_WEEK)


def tin_drv2_014_lull_frac_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day lull-regime fraction."""
    avg  = _rolling_mean(volume, _TD_MON)
    lull = ((_active_day(close, high, low) == 0) | (volume < 0.5 * avg)).astype(float)
    f21  = _rolling_sum(lull, _TD_MON) / _TD_MON
    return f21.diff(_TD_WEEK)


def tin_drv2_015_regime_transition_count_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day active/lull regime-transition count."""
    avg    = _rolling_mean(volume, _TD_MON)
    regime = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(int)
    trans  = (regime != regime.shift(1)).astype(float)
    c21    = _rolling_sum(trans, _TD_MON)
    return c21.diff(_TD_WEEK)


def tin_drv2_016_vxr_zscore_5d_diff(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of daily VxR z-score."""
    rng = high - low
    vxr = volume * rng
    m   = _rolling_mean(vxr, _TD_YEAR)
    s   = _rolling_std(vxr, _TD_YEAR)
    z   = _safe_div(vxr - m, s)
    return z.diff(_TD_WEEK)


def tin_drv2_017_vol_roc_5d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 5-day volume ROC."""
    roc5 = _safe_div(volume - volume.shift(_TD_WEEK), volume.shift(_TD_WEEK).replace(0, np.nan))
    return roc5.diff(_TD_MON)


def tin_drv2_018_active_regime_frac_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day active-regime fraction."""
    avg = _rolling_mean(volume, _TD_MON)
    act = ((_active_day(close, high, low) > 0) & (volume > avg)).astype(float)
    f63 = _rolling_sum(act, _TD_QTR) / _TD_QTR
    return f63.diff(_TD_MON)


def tin_drv2_019_vol_spike_count_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume-spike count."""
    avg  = _rolling_mean(volume, _TD_MON)
    cond = (volume > 2.0 * avg).astype(float)
    c21  = _rolling_sum(cond, _TD_MON)
    return c21.diff(_TD_WEEK)


def tin_drv2_020_body_vs_range_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day mean body/range ratio (velocity of directional commitment)."""
    body  = (close - open).abs()
    rng   = (high - low).replace(0, np.nan)
    ratio = _safe_div(body, rng)
    m21   = _rolling_mean(ratio, _TD_MON)
    return m21.diff(_TD_WEEK)


def tin_drv2_021_active_frac_ewm21_63d_slope(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of EMA21 of active-day indicator over trailing 63 days."""
    act = _active_day(close, high, low)
    e21 = _ewm_mean(act, _TD_MON)
    return _linslope(e21, _TD_QTR)


def tin_drv2_022_high_vol_frac_63d_21d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day high-vol-day fraction."""
    avg252 = _rolling_mean(volume, _TD_YEAR)
    cond   = (volume > avg252).astype(float)
    f63    = _rolling_sum(cond, _TD_QTR) / _TD_QTR
    return f63.diff(_TD_MON)


def tin_drv2_023_range_expansion_frac_63d_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day diff of 63-day range-expansion fraction."""
    rng   = high - low
    med63 = _rolling_median(rng, _TD_QTR)
    cond  = (rng > med63).astype(float)
    f63   = _rolling_sum(cond, _TD_QTR) / _TD_QTR
    return f63.diff(_TD_MON)


def tin_drv2_024_activity_composite_score_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the composite activity score (active-frac + vol/range + high-vol-frac)."""
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
    return composite.diff(_TD_WEEK)


def tin_drv2_025_activity_composite_score_21d_diff(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of the composite activity score."""
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
    return composite.diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

TRADING_INTENSITY_REGISTRY_2ND_DERIVATIVES = {
    "tin_drv2_001_active_frac_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv2_001_active_frac_21d_5d_diff},
    "tin_drv2_002_active_frac_21d_21d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv2_002_active_frac_21d_21d_diff},
    "tin_drv2_003_vol_per_range_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_003_vol_per_range_21d_5d_diff},
    "tin_drv2_004_vol_per_range_63d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_004_vol_per_range_63d_21d_diff},
    "tin_drv2_005_high_vol_frac_21d_5d_diff": {"inputs": ["close", "volume"], "func": tin_drv2_005_high_vol_frac_21d_5d_diff},
    "tin_drv2_006_burst_lull_ratio_21d_21d_diff": {"inputs": ["close", "volume"], "func": tin_drv2_006_burst_lull_ratio_21d_21d_diff},
    "tin_drv2_007_vxr_21d_5d_diff": {"inputs": ["high", "low", "volume"], "func": tin_drv2_007_vxr_21d_5d_diff},
    "tin_drv2_008_vxr_63d_21d_diff": {"inputs": ["high", "low", "volume"], "func": tin_drv2_008_vxr_63d_21d_diff},
    "tin_drv2_009_range_expansion_frac_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv2_009_range_expansion_frac_21d_5d_diff},
    "tin_drv2_010_discovery_events_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv2_010_discovery_events_21d_5d_diff},
    "tin_drv2_011_active_frac_5d_slope_21d": {"inputs": ["close", "high", "low"], "func": tin_drv2_011_active_frac_5d_slope_21d},
    "tin_drv2_012_vol_trend_slope_21d_5d_diff": {"inputs": ["volume"], "func": tin_drv2_012_vol_trend_slope_21d_5d_diff},
    "tin_drv2_013_range_trend_slope_21d_5d_diff": {"inputs": ["high", "low"], "func": tin_drv2_013_range_trend_slope_21d_5d_diff},
    "tin_drv2_014_lull_frac_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_014_lull_frac_21d_5d_diff},
    "tin_drv2_015_regime_transition_count_21d_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_015_regime_transition_count_21d_5d_diff},
    "tin_drv2_016_vxr_zscore_5d_diff": {"inputs": ["high", "low", "volume"], "func": tin_drv2_016_vxr_zscore_5d_diff},
    "tin_drv2_017_vol_roc_5d_21d_diff": {"inputs": ["volume"], "func": tin_drv2_017_vol_roc_5d_21d_diff},
    "tin_drv2_018_active_regime_frac_63d_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_018_active_regime_frac_63d_21d_diff},
    "tin_drv2_019_vol_spike_count_21d_5d_diff": {"inputs": ["volume"], "func": tin_drv2_019_vol_spike_count_21d_5d_diff},
    "tin_drv2_020_body_vs_range_21d_5d_diff": {"inputs": ["close", "high", "low", "open"], "func": tin_drv2_020_body_vs_range_21d_5d_diff},
    "tin_drv2_021_active_frac_ewm21_63d_slope": {"inputs": ["close", "high", "low"], "func": tin_drv2_021_active_frac_ewm21_63d_slope},
    "tin_drv2_022_high_vol_frac_63d_21d_diff": {"inputs": ["close", "volume"], "func": tin_drv2_022_high_vol_frac_63d_21d_diff},
    "tin_drv2_023_range_expansion_frac_63d_21d_diff": {"inputs": ["close", "high", "low"], "func": tin_drv2_023_range_expansion_frac_63d_21d_diff},
    "tin_drv2_024_activity_composite_score_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_024_activity_composite_score_5d_diff},
    "tin_drv2_025_activity_composite_score_21d_diff": {"inputs": ["close", "high", "low", "volume"], "func": tin_drv2_025_activity_composite_score_21d_diff},
}
