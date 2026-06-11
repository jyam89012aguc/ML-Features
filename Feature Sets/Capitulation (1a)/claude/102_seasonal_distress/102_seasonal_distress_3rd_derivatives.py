"""
102_seasonal_distress — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of the 2nd-derivative seasonal features — captures the
        inflection of seasonally-gated distress (turning into / out of the
        tax-loss window, exhaustion of seasonal selling pressure).
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


def _accel(s: pd.Series, n: int = 5) -> pd.Series:
    """Second difference: rate of change of the n-day rate of change."""
    return s.diff(n).diff(n)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def szd_drv3_001_tax_loss_intensity_accel(close: pd.Series) -> pd.Series:
    """Acceleration of tax-loss-window intensity."""
    return _accel(_tax_loss_intensity(close))


def szd_drv3_002_dd_in_tax_loss_window_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss-window-gated 252d drawdown."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _accel(dd * _tax_loss_window(close))


def szd_drv3_003_seasonal_distress_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the seasonal distress score."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    score = dd * _tax_loss_intensity(close) * _turn_of_year_proximity(close)
    return _accel(score)


def szd_drv3_004_tax_loss_candidate_score_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss candidate score."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    return _accel(loss * _tax_loss_intensity(close))


def szd_drv3_005_turn_of_year_proximity_accel(close: pd.Series) -> pd.Series:
    """Acceleration of turn-of-year proximity."""
    return _accel(_turn_of_year_proximity(close))


def szd_drv3_006_ytd_return_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the approximate year-to-date return."""
    elapsed = (_days_from_year_start(close) * 0.69).round().clip(lower=1, upper=_TD_YEAR)
    n = len(close)
    vals = np.full(n, np.nan)
    cv = close.values
    ev = elapsed.values.astype(int)
    for i in range(n):
        j = i - ev[i]
        if j >= 0 and cv[j] != 0:
            vals[i] = cv[i] / cv[j] - 1.0
    return _accel(pd.Series(vals, index=close.index))


def szd_drv3_007_days_to_year_end_accel(close: pd.Series) -> pd.Series:
    """Acceleration of days-to-year-end (year-boundary inflection)."""
    return _accel(_days_to_year_end(close))


def szd_drv3_008_q4_capitulation_score_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the Q4-gated capitulation score."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return _accel(dd * (1.0 + vr) * _q4_flag(close))


def szd_drv3_009_seasonal_distress_composite_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the seasonal distress composite."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    return _accel(dd * _tax_loss_intensity(close) * (1.0 + vr))


def szd_drv3_010_tax_loss_volume_ratio_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss-window-gated volume ratio."""
    ratio = _safe_div(volume, _rolling_median(volume, _TD_YEAR))
    return _accel(ratio * _tax_loss_intensity(close))


def szd_drv3_011_dd_x_year_end_accel(close: pd.Series) -> pd.Series:
    """Acceleration of drawdown weighted by turn-of-year proximity."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    return _accel(dd * _turn_of_year_proximity(close))


def szd_drv3_012_underwater_in_window_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss-window-gated underwater fraction."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    uw = _rolling_mean((dd < 0).astype(float), _TD_YEAR)
    return _accel(uw * _tax_loss_intensity(close))


def szd_drv3_013_seasonal_distress_intensity_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the 126d-drawdown seasonal distress intensity."""
    dd = _safe_div(_rolling_max(close, _TD_HALF) - close, _rolling_max(close, _TD_HALF))
    return _accel(dd * _tax_loss_intensity(close))


def szd_drv3_014_calendar_distress_composite_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the calendar distress composite."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    toy = (1.0 - _days_to_year_end(close) / 60.0).clip(lower=0)
    return _accel(dd * _q4_flag(close) * (1.0 + toy))


def szd_drv3_015_tax_loss_pressure_ramp_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss pressure ramp."""
    loss = (-close.pct_change(_TD_YEAR)).clip(lower=0)
    vr = _safe_div(volume, _rolling_median(volume, _TD_YEAR)).clip(upper=5)
    return _accel(loss * _tax_loss_intensity(close) * vr)


def szd_drv3_016_q4_decline_streak_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the Q4-gated consecutive down-day streak."""
    f = (_daily_ret(close) < 0).astype(float)
    streak = f.groupby((f == 0).cumsum()).cumsum()
    return _accel(streak * _q4_flag(close))


def szd_drv3_017_tax_loss_window_volatility_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss-window-gated 21d realized volatility."""
    vol = _rolling_std(_daily_ret(close), _TD_MON)
    return _accel(vol * _tax_loss_intensity(close))


def szd_drv3_018_master_index_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the master seasonal-distress index."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    intensity = _tax_loss_intensity(close)
    toy = (1.0 - _days_to_year_end(close) / 45.0).clip(lower=0)
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    vr = _safe_div(dv, _rolling_median(volume, _TD_YEAR)).clip(upper=5) / 5.0
    idx = (dd * (1.0 + intensity + toy) * (1.0 + vr)) / 3.0
    return _accel(idx)


def szd_drv3_019_tax_loss_intensity_21d_accel(close: pd.Series) -> pd.Series:
    """21-day-horizon acceleration of tax-loss-window intensity."""
    return _accel(_tax_loss_intensity(close), _TD_MON)


def szd_drv3_020_seasonal_distress_score_21d_accel(close: pd.Series) -> pd.Series:
    """21-day-horizon acceleration of the seasonal distress score."""
    dd = _safe_div(_rolling_max(close, _TD_YEAR) - close, _rolling_max(close, _TD_YEAR))
    score = dd * _tax_loss_intensity(close) * _turn_of_year_proximity(close)
    return _accel(score, _TD_MON)


def szd_drv3_021_days_into_window_accel(close: pd.Series) -> pd.Series:
    """Acceleration of days-into-tax-loss-window."""
    idx = _dtidx(close)
    in_window = np.isin(idx.month, [11, 12])
    days = (92.0 - _days_to_year_end(close)).clip(lower=0)
    return _accel(days * _ser(in_window.astype(float), close))


def szd_drv3_022_down_fraction_q4_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the Q4-gated down-day fraction."""
    down = (_daily_ret(close) < 0).astype(float)
    q4 = _q4_flag(close)
    frac = _safe_div(_rolling_sum(down * q4, _TD_QTR), _rolling_sum(down, _TD_QTR))
    return _accel(frac)


def szd_drv3_023_tax_loss_dd_zscore_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the tax-loss-window-gated drawdown z-score."""
    dd = _safe_div(close - _rolling_max(close, _TD_YEAR), _rolling_max(close, _TD_YEAR))
    z = _safe_div(dd - _rolling_mean(dd, _TD_YEAR), _rolling_std(dd, _TD_YEAR))
    return _accel(z * _tax_loss_window(close))


def szd_drv3_024_year_end_low_proximity_accel(close: pd.Series) -> pd.Series:
    """Acceleration of the year-end low-proximity score."""
    prox_low = _safe_div(_rolling_min(close, _TD_YEAR), close)
    return _accel(prox_low * _turn_of_year_proximity(close))


def szd_drv3_025_seasonal_volume_distress_accel(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Acceleration of the seasonal volume-distress feature."""
    dv = volume.where(_daily_ret(close) < 0, 0.0)
    z = _safe_div(dv - _rolling_mean(dv, _TD_YEAR), _rolling_std(dv, _TD_YEAR))
    return _accel(z * _tax_loss_intensity(close))


# ── Registry ──────────────────────────────────────────────────────────────────

SEASONAL_DISTRESS_REGISTRY_3RD_DERIVATIVES = {
    "szd_drv3_001_tax_loss_intensity_accel": {"inputs": ["close"], "func": szd_drv3_001_tax_loss_intensity_accel},
    "szd_drv3_002_dd_in_tax_loss_window_accel": {"inputs": ["close"], "func": szd_drv3_002_dd_in_tax_loss_window_accel},
    "szd_drv3_003_seasonal_distress_score_accel": {"inputs": ["close"], "func": szd_drv3_003_seasonal_distress_score_accel},
    "szd_drv3_004_tax_loss_candidate_score_accel": {"inputs": ["close"], "func": szd_drv3_004_tax_loss_candidate_score_accel},
    "szd_drv3_005_turn_of_year_proximity_accel": {"inputs": ["close"], "func": szd_drv3_005_turn_of_year_proximity_accel},
    "szd_drv3_006_ytd_return_accel": {"inputs": ["close"], "func": szd_drv3_006_ytd_return_accel},
    "szd_drv3_007_days_to_year_end_accel": {"inputs": ["close"], "func": szd_drv3_007_days_to_year_end_accel},
    "szd_drv3_008_q4_capitulation_score_accel": {"inputs": ["close", "volume"], "func": szd_drv3_008_q4_capitulation_score_accel},
    "szd_drv3_009_seasonal_distress_composite_accel": {"inputs": ["close", "volume"], "func": szd_drv3_009_seasonal_distress_composite_accel},
    "szd_drv3_010_tax_loss_volume_ratio_accel": {"inputs": ["close", "volume"], "func": szd_drv3_010_tax_loss_volume_ratio_accel},
    "szd_drv3_011_dd_x_year_end_accel": {"inputs": ["close"], "func": szd_drv3_011_dd_x_year_end_accel},
    "szd_drv3_012_underwater_in_window_accel": {"inputs": ["close"], "func": szd_drv3_012_underwater_in_window_accel},
    "szd_drv3_013_seasonal_distress_intensity_accel": {"inputs": ["close"], "func": szd_drv3_013_seasonal_distress_intensity_accel},
    "szd_drv3_014_calendar_distress_composite_accel": {"inputs": ["close"], "func": szd_drv3_014_calendar_distress_composite_accel},
    "szd_drv3_015_tax_loss_pressure_ramp_accel": {"inputs": ["close", "volume"], "func": szd_drv3_015_tax_loss_pressure_ramp_accel},
    "szd_drv3_016_q4_decline_streak_accel": {"inputs": ["close"], "func": szd_drv3_016_q4_decline_streak_accel},
    "szd_drv3_017_tax_loss_window_volatility_accel": {"inputs": ["close"], "func": szd_drv3_017_tax_loss_window_volatility_accel},
    "szd_drv3_018_master_index_accel": {"inputs": ["close", "volume"], "func": szd_drv3_018_master_index_accel},
    "szd_drv3_019_tax_loss_intensity_21d_accel": {"inputs": ["close"], "func": szd_drv3_019_tax_loss_intensity_21d_accel},
    "szd_drv3_020_seasonal_distress_score_21d_accel": {"inputs": ["close"], "func": szd_drv3_020_seasonal_distress_score_21d_accel},
    "szd_drv3_021_days_into_window_accel": {"inputs": ["close"], "func": szd_drv3_021_days_into_window_accel},
    "szd_drv3_022_down_fraction_q4_accel": {"inputs": ["close"], "func": szd_drv3_022_down_fraction_q4_accel},
    "szd_drv3_023_tax_loss_dd_zscore_accel": {"inputs": ["close"], "func": szd_drv3_023_tax_loss_dd_zscore_accel},
    "szd_drv3_024_year_end_low_proximity_accel": {"inputs": ["close"], "func": szd_drv3_024_year_end_low_proximity_accel},
    "szd_drv3_025_seasonal_volume_distress_accel": {"inputs": ["close", "volume"], "func": szd_drv3_025_seasonal_volume_distress_accel},
}
