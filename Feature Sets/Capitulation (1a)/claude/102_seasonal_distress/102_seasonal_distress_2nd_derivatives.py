"""
102_seasonal_distress — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base seasonal-distress features — captures the pace
        of entering the tax-loss window and the acceleration of seasonally-
        gated drawdown / volume distress.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
        Calendar attributes are derived from the close Series' DatetimeIndex.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


# ── Calendar helpers ─────────────────────────────────────────────────────────

def _dtidx(s: pd.Series) -> pd.DatetimeIndex:
    idx = s.index
    if not isinstance(idx, pd.DatetimeIndex):
        idx = pd.DatetimeIndex(pd.to_datetime(idx, errors="coerce"))
    return idx


def _ser(values, s: pd.Series) -> pd.Series:
    return pd.Series(np.asarray(values, dtype=float), index=s.index)


def _days_to_year_end(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    ye = pd.PeriodIndex(idx, freq="Y").end_time.normalize()
    return _ser((ye - idx).days, s)


def _days_from_year_start(s: pd.Series) -> pd.Series:
    idx = _dtidx(s)
    ys = pd.PeriodIndex(idx, freq="Y").start_time.normalize()
    return _ser((idx - ys).days, s)


def _tax_loss_intensity(s: pd.Series) -> pd.Series:
    m = _dtidx(s).month
    in_window = np.isin(m, [10, 11, 12])
    ramp = (1.0 - _days_to_year_end(s) / 92.0).clip(lower=0, upper=1)
    return ramp * _ser(in_window.astype(float), s)


def _tax_loss_window(s: pd.Series) -> pd.Series:
    return _ser(np.isin(_dtidx(s).month, [11, 12]).astype(float), s)


def _q4_flag(s: pd.Series) -> pd.Series:
    return _ser((_dtidx(s).quarter == 4).astype(float), s)


def _turn_of_year_proximity(s: pd.Series) -> pd.Series:
    dte = _days_to_year_end(s)
    dys = _days_from_year_start(s)
    nearest = pd.concat([dte, dys], axis=1).min(axis=1)
    return (1.0 - nearest / 30.0).clip(lower=0)


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def szd_drv2_001_tax_loss_intensity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of tax-loss-window intensity (pace of entering the window)."""
    return _tax_loss_intensity(close).diff(5)


def szd_drv2_002_dd_in_tax_loss_window_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 252d drawdown gated to the tax-loss window."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return (dd * _tax_loss_window(close)).diff(5)


def szd_drv2_003_seasonal_distress_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the seasonal distress score (dd x intensity x proximity)."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    score = dd * _tax_loss_intensity(close) * _turn_of_year_proximity(close)
    return score.diff(5)


def szd_drv2_004_tax_loss_candidate_score_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the tax-loss candidate score (loss x intensity)."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return (loss * _tax_loss_intensity(close)).diff(5)


def szd_drv2_005_turn_of_year_proximity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of turn-of-year proximity (ramp toward / away from year-end)."""
    return _turn_of_year_proximity(close).diff(5)


def szd_drv2_006_ytd_return_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the approximate year-to-date return."""
    elapsed = (_days_from_year_start(close) * 0.69).round().clip(lower=1, upper=_TD_YEAR)
    n = len(close)
    vals = np.full(n, np.nan)
    cv = close.values
    ev = elapsed.values.astype(int)
    for i in range(n):
        j = i - ev[i]
        if j >= 0 and cv[j] != 0:
            vals[i] = cv[i] / cv[j] - 1.0
    return pd.Series(vals, index=close.index).diff(5)


def szd_drv2_007_days_to_year_end_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-to-year-end (spikes at the year boundary)."""
    return _days_to_year_end(close).diff(5)


def szd_drv2_008_q4_capitulation_score_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the Q4-gated capitulation score."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return (dd * (1.0 + vr) * _q4_flag(close)).diff(5)


def szd_drv2_009_seasonal_distress_composite_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the seasonal distress composite."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return (dd * _tax_loss_intensity(close) * (1.0 + vr)).diff(5)


def szd_drv2_010_tax_loss_volume_ratio_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the tax-loss-window-gated volume ratio."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR))
    return (ratio * _tax_loss_intensity(close)).diff(5)


def szd_drv2_011_dd_x_year_end_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of drawdown weighted by turn-of-year proximity."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return (dd * _turn_of_year_proximity(close)).diff(5)


def szd_drv2_012_underwater_in_window_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the tax-loss-window-gated underwater fraction."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    uw = _rolling_mean((dd < 0).astype(float), _TD_YEAR)
    return (uw * _tax_loss_intensity(close)).diff(5)


def szd_drv2_013_seasonal_distress_intensity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 126d-drawdown seasonal distress intensity."""
    dd = _safe_div(_rolling_max(close, _TD_HALF) - close, _rolling_max(close, _TD_HALF))
    return (dd * _tax_loss_intensity(close)).diff(5)


def szd_drv2_014_calendar_distress_composite_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the calendar distress composite (dd x Q4 x year-end)."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    toy = (1.0 - _days_to_year_end(close) / 60.0).clip(lower=0)
    return (dd * _q4_flag(close) * (1.0 + toy)).diff(5)


def szd_drv2_015_tax_loss_pressure_ramp_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the tax-loss pressure ramp (loss x intensity x volume)."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    vr = _safe_div(volume, _rolling_median(volume, _TD_YEAR)).clip(upper=5)
    return (loss * _tax_loss_intensity(close) * vr).diff(5)


def szd_drv2_016_q4_decline_streak_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the Q4-gated consecutive down-day streak."""
    f = (_daily_ret(close) < 0).astype(float)
    streak = f.groupby((f == 0).cumsum()).cumsum()
    return (streak * _q4_flag(close)).diff(5)


def szd_drv2_017_tax_loss_window_volatility_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the tax-loss-window-gated 21d realized volatility."""
    vol = _rolling_std(_daily_ret(close), _TD_MON)
    return (vol * _tax_loss_intensity(close)).diff(5)


def szd_drv2_018_master_index_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the master seasonal-distress index."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    intensity = _tax_loss_intensity(close)
    toy = (1.0 - _days_to_year_end(close) / 45.0).clip(lower=0)
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    idx = (dd * (1.0 + intensity + toy) * (1.0 + vr)) / 3.0
    return idx.diff(5)


def szd_drv2_019_tax_loss_intensity_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of tax-loss-window intensity (monthly seasonal ramp)."""
    return _tax_loss_intensity(close).diff(_TD_MON)


def szd_drv2_020_seasonal_distress_score_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of the seasonal distress score."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    score = dd * _tax_loss_intensity(close) * _turn_of_year_proximity(close)
    return score.diff(_TD_MON)


def szd_drv2_021_days_into_window_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of days-into-tax-loss-window."""
    idx = _dtidx(close)
    in_window = np.isin(idx.month, [11, 12])
    days = (92.0 - _days_to_year_end(close)).clip(lower=0)
    return (days * _ser(in_window.astype(float), close)).diff(5)


def szd_drv2_022_down_fraction_q4_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the Q4-gated down-day fraction over 63 days."""
    down = (_daily_ret(close) < 0).astype(float)
    q4 = _q4_flag(close)
    frac = _safe_div(_rolling_sum(down * q4, _TD_QTR), _rolling_sum(down, _TD_QTR))
    return frac.diff(5)


def szd_drv2_023_tax_loss_dd_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the tax-loss-window-gated drawdown z-score."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    z = _safe_div(dd - _rolling_mean(dd, _TD_YEAR), _rolling_std(dd, _TD_YEAR))
    return (z * _tax_loss_window(close)).diff(5)


def szd_drv2_024_year_end_low_proximity_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the year-end low-proximity score."""
    prox_low = _safe_div(_rolling_min(close, _TD_YEAR), close)
    return (prox_low * _turn_of_year_proximity(close)).diff(5)


def szd_drv2_025_seasonal_volume_distress_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the seasonal volume-distress feature."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    z = _safe_div(dv - _rolling_mean(dv, _TD_YEAR), _rolling_std(dv, _TD_YEAR))
    return (z * _tax_loss_intensity(close)).diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

SEASONAL_DISTRESS_REGISTRY_2ND_DERIVATIVES = {
    "szd_drv2_001_tax_loss_intensity_5d_diff": {"inputs": ["close"], "func": szd_drv2_001_tax_loss_intensity_5d_diff},
    "szd_drv2_002_dd_in_tax_loss_window_5d_diff": {"inputs": ["close"], "func": szd_drv2_002_dd_in_tax_loss_window_5d_diff},
    "szd_drv2_003_seasonal_distress_score_5d_diff": {"inputs": ["close"], "func": szd_drv2_003_seasonal_distress_score_5d_diff},
    "szd_drv2_004_tax_loss_candidate_score_5d_diff": {"inputs": ["close"], "func": szd_drv2_004_tax_loss_candidate_score_5d_diff},
    "szd_drv2_005_turn_of_year_proximity_5d_diff": {"inputs": ["close"], "func": szd_drv2_005_turn_of_year_proximity_5d_diff},
    "szd_drv2_006_ytd_return_5d_diff": {"inputs": ["close"], "func": szd_drv2_006_ytd_return_5d_diff},
    "szd_drv2_007_days_to_year_end_5d_diff": {"inputs": ["close"], "func": szd_drv2_007_days_to_year_end_5d_diff},
    "szd_drv2_008_q4_capitulation_score_5d_diff": {"inputs": ["close", "volume"], "func": szd_drv2_008_q4_capitulation_score_5d_diff},
    "szd_drv2_009_seasonal_distress_composite_5d_diff": {"inputs": ["close", "volume"], "func": szd_drv2_009_seasonal_distress_composite_5d_diff},
    "szd_drv2_010_tax_loss_volume_ratio_5d_diff": {"inputs": ["close", "volume"], "func": szd_drv2_010_tax_loss_volume_ratio_5d_diff},
    "szd_drv2_011_dd_x_year_end_5d_diff": {"inputs": ["close"], "func": szd_drv2_011_dd_x_year_end_5d_diff},
    "szd_drv2_012_underwater_in_window_5d_diff": {"inputs": ["close"], "func": szd_drv2_012_underwater_in_window_5d_diff},
    "szd_drv2_013_seasonal_distress_intensity_5d_diff": {"inputs": ["close"], "func": szd_drv2_013_seasonal_distress_intensity_5d_diff},
    "szd_drv2_014_calendar_distress_composite_5d_diff": {"inputs": ["close"], "func": szd_drv2_014_calendar_distress_composite_5d_diff},
    "szd_drv2_015_tax_loss_pressure_ramp_5d_diff": {"inputs": ["close", "volume"], "func": szd_drv2_015_tax_loss_pressure_ramp_5d_diff},
    "szd_drv2_016_q4_decline_streak_5d_diff": {"inputs": ["close"], "func": szd_drv2_016_q4_decline_streak_5d_diff},
    "szd_drv2_017_tax_loss_window_volatility_5d_diff": {"inputs": ["close"], "func": szd_drv2_017_tax_loss_window_volatility_5d_diff},
    "szd_drv2_018_master_index_5d_diff": {"inputs": ["close", "volume"], "func": szd_drv2_018_master_index_5d_diff},
    "szd_drv2_019_tax_loss_intensity_21d_diff": {"inputs": ["close"], "func": szd_drv2_019_tax_loss_intensity_21d_diff},
    "szd_drv2_020_seasonal_distress_score_21d_diff": {"inputs": ["close"], "func": szd_drv2_020_seasonal_distress_score_21d_diff},
    "szd_drv2_021_days_into_window_5d_diff": {"inputs": ["close"], "func": szd_drv2_021_days_into_window_5d_diff},
    "szd_drv2_022_down_fraction_q4_5d_diff": {"inputs": ["close"], "func": szd_drv2_022_down_fraction_q4_5d_diff},
    "szd_drv2_023_tax_loss_dd_zscore_5d_diff": {"inputs": ["close"], "func": szd_drv2_023_tax_loss_dd_zscore_5d_diff},
    "szd_drv2_024_year_end_low_proximity_5d_diff": {"inputs": ["close"], "func": szd_drv2_024_year_end_low_proximity_5d_diff},
    "szd_drv2_025_seasonal_volume_distress_5d_diff": {"inputs": ["close", "volume"], "func": szd_drv2_025_seasonal_volume_distress_5d_diff},
}
