"""
35_capitulation_thrust — 3rd Derivatives (Features drv3_001-025)
Domain: rate-of-change of 2nd-derivative thrust concepts — acceleration of velocity
        Double-diffs and slope-of-slope applied to 2nd-derivative thrust signals.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff / slope applied to a 2nd-derivative concept.

def cth_drv3_001_min_return_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of worst-5d-return (acceleration of thrust-depth velocity)."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    worst = _rolling_min(cum5, _TD_MON)
    vel   = worst.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_002_min_return_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day-velocity of worst-21d return (jerk in monthly thrust)."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    worst = _rolling_min(cum21, _TD_QTR)
    vel21 = worst.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cth_drv3_003_single_day_zscore_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of daily z-score (acceleration of sigma-move velocity)."""
    lr  = _log_ret(close)
    mn  = _rolling_mean(lr, _TD_YEAR)
    sd  = _rolling_std(lr, _TD_YEAR)
    z   = _safe_div(lr - mn, sd)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_004_drawdown_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day drawdown (acceleration of drawdown deepening)."""
    pk  = _rolling_max(close, _TD_MON)
    dd  = _log_safe(close) - _log_safe(pk)
    vel = dd.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_005_drawdown_63d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day drawdown (jerk in quarterly drawdown)."""
    pk   = _rolling_max(close, _TD_QTR)
    dd   = _log_safe(close) - _log_safe(pk)
    vel21 = dd.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cth_drv3_006_thrust_intensity_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day thrust intensity (jerk in per-day loss rate)."""
    cum5      = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    intensity = cum5.clip(upper=0) / _TD_WEEK
    vel       = intensity.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_007_log_slope_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day log-slope (acceleration of descent-rate change)."""
    slp = _linslope(_log_safe(close), _TD_WEEK)
    vel = slp.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_008_log_slope_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-day log-slope velocity (slope of slope change)."""
    slp   = _linslope(_log_safe(close), _TD_MON)
    vel21 = slp.diff(_TD_MON)
    return _linslope(vel21, _TD_MON)


def cth_drv3_009_sigma_burst_5d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day sigma-burst count (jerk in shock-cluster rate)."""
    lr   = _log_ret(close)
    mn   = _rolling_mean(lr, _TD_YEAR)
    sd   = _rolling_std(lr, _TD_YEAR)
    z    = _safe_div(lr - mn, sd)
    cnt  = (z < -1.5).astype(float).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).sum()
    vel  = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_010_sigma_burst_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day sigma-burst count."""
    lr   = _log_ret(close)
    mn   = _rolling_mean(lr, _TD_YEAR)
    sd   = _rolling_std(lr, _TD_YEAR)
    z    = _safe_div(lr - mn, sd)
    cnt  = (z < -2.0).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cth_drv3_011_panic_composite_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in dual-horizon panic composite."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    z5    = _safe_div(cum5  - _rolling_mean(cum5,  _TD_YEAR), _rolling_std(cum5,  _TD_YEAR))
    z21   = _safe_div(cum21 - _rolling_mean(cum21, _TD_YEAR), _rolling_std(cum21, _TD_YEAR))
    comp  = (z5 + z21) / 2.0
    vel21 = comp.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cth_drv3_012_vol_thrust_score_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day volume-weighted thrust score."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    score   = (lr * vol_n).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).sum()
    vel     = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_013_vol_down_up_ratio_5d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day down/up volume ratio."""
    lr     = _log_ret(close)
    down_v = volume.where(lr < 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    up_v   = volume.where(lr > 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    ratio  = _safe_div(down_v, up_v)
    vel    = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_014_thrust_persist_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day thrust persistence (acceleration of down-day piling)."""
    lr   = _log_ret(close)
    pers = (lr < 0).astype(float).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean()
    vel  = pers.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_015_return_skew_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day return skewness."""
    lr   = _log_ret(close)
    skew = lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).skew()
    vel  = skew.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_016_drawdown_21d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the OLS slope of 21-day drawdown (rate of drawdown-slope change)."""
    pk  = _rolling_max(close, _TD_MON)
    dd  = _log_safe(close) - _log_safe(pk)
    slp = _linslope(dd, _TD_MON)
    return slp.diff(_TD_WEEK)


def cth_drv3_017_atr_norm_5d_5d_diff_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-day normalized ATR (jerk in range-expansion rate)."""
    tr   = pd.concat([high - low,
                      (high - close.shift(1)).abs(),
                      (low  - close.shift(1)).abs()], axis=1).max(axis=1)
    atr5 = tr.rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean() / close.clip(lower=_EPS)
    vel  = atr5.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_018_thrust_intensity_5d_slope_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 21-day OLS slope of 5-day thrust intensity."""
    cum5      = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    intensity = cum5.clip(upper=0) / _TD_WEEK
    slp       = _linslope(intensity, _TD_MON)
    return slp.diff(_TD_WEEK)


def cth_drv3_019_panic_score_sigma_21d_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day sigma-exceedance score."""
    lr  = _log_ret(close)
    mn  = _rolling_mean(lr, _TD_YEAR)
    sd  = _rolling_std(lr, _TD_YEAR)
    z   = _safe_div(lr - mn, sd)
    exc = (-z - 2.0).clip(lower=0).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vel = exc.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_020_waterfall_freq_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in waterfall frequency (jerk in cascade rate)."""
    l1   = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))) < 0
    l2   = (_log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(2 * _TD_WEEK))) < 0
    l3   = (_log_safe(close.shift(2 * _TD_WEEK)) - _log_safe(close.shift(3 * _TD_WEEK))) < 0
    freq = (l1 & l2 & l3).astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    vel21 = freq.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cth_drv3_021_horizon_rank_5d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """Second 5-day diff of 252d pct-rank of 5d return (acceleration of rank velocity)."""
    c5   = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    rank = c5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    vel  = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def cth_drv3_022_bear_body_frac_5d_diff_slope(close: pd.Series, open: pd.Series,
                                               high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5-day diff of bear-body fraction."""
    body  = (open - close).clip(lower=0)
    rng   = (high - low).clip(lower=_EPS)
    frac  = (body / rng).rolling(_TD_WEEK, min_periods=max(1, _TD_WEEK // 2)).mean()
    vel   = frac.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def cth_drv3_023_close_near_low_21d_5d_diff_slope(close: pd.Series, high: pd.Series,
                                                    low: pd.Series) -> pd.Series:
    """OLS slope over 21d of the 5-day diff of 21d close-near-low count."""
    pos  = _safe_div(close - low, high - low + _EPS)
    cnt  = (pos < 0.20).astype(float).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vel  = cnt.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def cth_drv3_024_vol_thrust_21d_diff_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day volume-weighted thrust score."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    score   = (lr * vol_n).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    vel21   = score.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def cth_drv3_025_thrust_intensity_21d_21d_diff_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day thrust intensity (jerk in monthly leg speed)."""
    cum21     = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    intensity = cum21.clip(upper=0) / _TD_MON
    vel21     = intensity.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITULATION_THRUST_REGISTRY_3RD_DERIVATIVES = {
    "cth_drv3_001_min_return_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_001_min_return_5d_5d_diff_5d_diff},
    "cth_drv3_002_min_return_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_002_min_return_21d_21d_diff_5d_diff},
    "cth_drv3_003_single_day_zscore_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_003_single_day_zscore_5d_diff_5d_diff},
    "cth_drv3_004_drawdown_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_004_drawdown_21d_5d_diff_5d_diff},
    "cth_drv3_005_drawdown_63d_21d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_005_drawdown_63d_21d_diff_5d_diff},
    "cth_drv3_006_thrust_intensity_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_006_thrust_intensity_5d_5d_diff_5d_diff},
    "cth_drv3_007_log_slope_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_007_log_slope_5d_5d_diff_5d_diff},
    "cth_drv3_008_log_slope_21d_slope_21d": {"inputs": ["close"], "func": cth_drv3_008_log_slope_21d_slope_21d},
    "cth_drv3_009_sigma_burst_5d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_009_sigma_burst_5d_5d_diff_5d_diff},
    "cth_drv3_010_sigma_burst_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_010_sigma_burst_21d_21d_diff_5d_diff},
    "cth_drv3_011_panic_composite_21d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_011_panic_composite_21d_diff_5d_diff},
    "cth_drv3_012_vol_thrust_score_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": cth_drv3_012_vol_thrust_score_5d_diff_5d_diff},
    "cth_drv3_013_vol_down_up_ratio_5d_diff_5d_diff": {"inputs": ["close", "volume"], "func": cth_drv3_013_vol_down_up_ratio_5d_diff_5d_diff},
    "cth_drv3_014_thrust_persist_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_014_thrust_persist_5d_diff_5d_diff},
    "cth_drv3_015_return_skew_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_015_return_skew_21d_5d_diff_5d_diff},
    "cth_drv3_016_drawdown_21d_slope_5d_diff": {"inputs": ["close"], "func": cth_drv3_016_drawdown_21d_slope_5d_diff},
    "cth_drv3_017_atr_norm_5d_5d_diff_5d_diff": {"inputs": ["close", "high", "low"], "func": cth_drv3_017_atr_norm_5d_5d_diff_5d_diff},
    "cth_drv3_018_thrust_intensity_5d_slope_5d_diff": {"inputs": ["close"], "func": cth_drv3_018_thrust_intensity_5d_slope_5d_diff},
    "cth_drv3_019_panic_score_sigma_21d_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_019_panic_score_sigma_21d_5d_diff_5d_diff},
    "cth_drv3_020_waterfall_freq_21d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_020_waterfall_freq_21d_diff_5d_diff},
    "cth_drv3_021_horizon_rank_5d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_021_horizon_rank_5d_diff_5d_diff},
    "cth_drv3_022_bear_body_frac_5d_diff_slope": {"inputs": ["close", "open", "high", "low"], "func": cth_drv3_022_bear_body_frac_5d_diff_slope},
    "cth_drv3_023_close_near_low_21d_5d_diff_slope": {"inputs": ["close", "high", "low"], "func": cth_drv3_023_close_near_low_21d_5d_diff_slope},
    "cth_drv3_024_vol_thrust_21d_diff_5d_diff": {"inputs": ["close", "volume"], "func": cth_drv3_024_vol_thrust_21d_diff_5d_diff},
    "cth_drv3_025_thrust_intensity_21d_21d_diff_5d_diff": {"inputs": ["close"], "func": cth_drv3_025_thrust_intensity_21d_21d_diff_5d_diff},
}
