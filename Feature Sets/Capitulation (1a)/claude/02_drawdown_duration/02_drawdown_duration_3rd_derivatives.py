"""
02_drawdown_duration — 3rd Derivatives (001-025)
Domain: rate-of-change of 2nd-derivative features; captures exhaustion/inflection of decline
Asset class: US equities | Daily OHLCV only (SEP folder — no fundamental inputs)
Target: capitulation features at/near multi-year absolute low
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MO = 21
_TD_WK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _days_since_rolling_high(s: pd.Series, w: int) -> pd.Series:
    """Number of bars since the rolling-window maximum occurred."""
    return s.rolling(w, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True
    )


def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    """Number of bars since the all-time (expanding) maximum occurred."""
    cummax = s.cummax()
    is_new_high = (s >= cummax)
    pos = pd.Series(np.arange(len(s)), index=s.index)
    last_high_pos = pos.where(is_new_high).ffill().fillna(0)
    return pos - last_high_pos


def _days_since_rolling_low(s: pd.Series, w: int) -> pd.Series:
    """Number of bars since the rolling-window minimum occurred."""
    return s.rolling(w, min_periods=1).apply(
        lambda x: len(x) - 1 - int(np.argmin(x)), raw=True
    )


def _days_since_expanding_low(s: pd.Series) -> pd.Series:
    """Number of bars since the all-time (expanding) minimum occurred."""
    cummin = s.cummin()
    is_new_low = (s <= cummin)
    pos = pd.Series(np.arange(len(s)), index=s.index)
    last_low_pos = pos.where(is_new_low).ffill().fillna(0)
    return pos - last_low_pos


def _underwater_flag(s: pd.Series, w: int) -> pd.Series:
    return (s < _rolling_max(s, w)).astype(float)


def _underwater_expanding_flag(s: pd.Series) -> pd.Series:
    return (s < s.cummax()).astype(float)


def _consec_streak(flag: pd.Series) -> pd.Series:
    groups = (flag == 0).cumsum()
    return flag.groupby(groups).cumsum()


# ── 3rd Derivative Feature functions (001–025) ────────────────────────────────
# Each feature applies a further diff/slope to a 2nd-derivative concept,
# capturing the exhaustion or inflection of the acceleration.

def ddur_drv3_001_dsh_252d_acceleration_of_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day velocity of days-since-252d-high (3rd order)."""
    velocity = _days_since_rolling_high(close, _TD_YEAR).diff(5)
    return velocity.diff(5)


def ddur_drv3_002_dsh_ath_acceleration_of_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day velocity of days-since-ATH (3rd order)."""
    velocity = _days_since_expanding_high(close).diff(5)
    return velocity.diff(5)


def ddur_drv3_003_dsh_252d_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of days-since-252d-high (jerk)."""
    velocity = _days_since_rolling_high(close, _TD_YEAR).diff(5)
    return velocity.diff(_TD_MO)


def ddur_drv3_004_dsh_ath_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day velocity of days-since-ATH (jerk)."""
    velocity = _days_since_expanding_high(close).diff(5)
    return velocity.diff(_TD_MO)


def ddur_drv3_005_consec_under_252d_high_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day change of consecutive-days-below-252d-high (3rd order)."""
    streak = _consec_streak(_underwater_flag(close, _TD_YEAR))
    velocity = streak.diff(5)
    return velocity.diff(5)


def ddur_drv3_006_consec_under_ath_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day change of consecutive-days-below-ATH (3rd order)."""
    streak = _consec_streak(_underwater_expanding_flag(close))
    velocity = streak.diff(5)
    return velocity.diff(5)


def ddur_drv3_007_pct_time_under_252d_high_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day change of fraction-of-time-below-252d-high."""
    frac = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    velocity = frac.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_008_composite_age_index_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of composite drawdown age index."""
    d1 = _days_since_rolling_high(close, _TD_MO)
    d2 = _days_since_rolling_high(close, _TD_QTR)
    d3 = _days_since_rolling_high(close, _TD_YEAR)
    idx = (d1 + d2 + d3) / 3.0
    velocity = idx.diff(5)
    return velocity.diff(5)


def ddur_drv3_009_composite_age_index_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of composite drawdown age index."""
    d1 = _days_since_rolling_high(close, _TD_MO)
    d2 = _days_since_rolling_high(close, _TD_QTR)
    d3 = _days_since_rolling_high(close, _TD_YEAR)
    idx = (d1 + d2 + d3) / 3.0
    velocity = idx.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_010_days_since_new_low_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of days-since-252d-low."""
    dsl = _days_since_rolling_low(close, _TD_YEAR)
    velocity = dsl.diff(5)
    return velocity.diff(5)


def ddur_drv3_011_new_low_freq_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day change of new-252d-low frequency."""
    is_low = (close == _rolling_min(close, _TD_YEAR)).astype(float)
    freq = _rolling_sum(is_low, _TD_YEAR)
    velocity = freq.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_012_exp_decay_dsh_252d_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of exp-decay of days-since-252d-high."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    decay = np.exp(-dsh / _TD_QTR)
    velocity = decay.diff(5)
    return velocity.diff(5)


def ddur_drv3_013_exp_decay_dsh_ath_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of exp-decay of days-since-ATH."""
    dsh = _days_since_expanding_high(close)
    decay = np.exp(-dsh / _TD_YEAR)
    velocity = decay.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_014_dsh_252d_zscore_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of z-score of days-since-252d-high."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    mu = _rolling_mean(dsh, _TD_YEAR)
    sigma = _rolling_std(dsh, _TD_YEAR)
    zscore = _safe_div(dsh - mu, sigma)
    velocity = zscore.diff(5)
    return velocity.diff(5)


def ddur_drv3_015_days_under_20pct_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day change of days-under-20%-from-252d-high count."""
    h = _rolling_max(close, _TD_YEAR)
    days = _rolling_sum((close < h * 0.80).astype(float), _TD_YEAR)
    velocity = days.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_016_consec_below_sma200_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day change of consecutive-days-below-200-SMA streak."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak((close < sma200).astype(float))
    velocity = streak.diff(5)
    return velocity.diff(5)


def ddur_drv3_017_pct_time_under_ath_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day change of fraction-of-time-below-ATH."""
    frac = _rolling_mean(_underwater_expanding_flag(close), _TD_YEAR)
    velocity = frac.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_018_dsh_252d_norm_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of normalized days-since-252d-high."""
    norm = _days_since_rolling_high(close, _TD_YEAR) / _TD_YEAR
    velocity = norm.diff(5)
    return velocity.diff(5)


def ddur_drv3_019_vol_wtd_dsh_jerk_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of volume-weighted days-since-252d-high."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    num = _rolling_sum(dsh * volume, _TD_YEAR)
    den = _rolling_sum(volume, _TD_YEAR)
    vwtd = _safe_div(num, den)
    velocity = vwtd.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_020_days_near_252d_low_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of days-spent-near-252d-low count."""
    lo = _rolling_min(close, _TD_YEAR)
    days = _rolling_sum((close <= lo * 1.05).astype(float), _TD_YEAR)
    velocity = days.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_021_cross_horizon_persistence_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day change of cross-horizon persistence index."""
    f21 = _rolling_mean(_underwater_flag(close, _TD_MO), _TD_YEAR)
    f63 = _rolling_mean(_underwater_flag(close, _TD_QTR), _TD_YEAR)
    f252 = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    f504 = _rolling_mean(_underwater_flag(close, 504), _TD_YEAR)
    idx = (f21 + f63 + f252 + f504) / 4.0
    velocity = idx.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_022_dsh_504d_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of days-since-504d-high."""
    velocity = _days_since_rolling_high(close, 504).diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_023_pct_days_bottom_decile_jerk_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day velocity of fraction-in-bottom-decile feature."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    threshold = lo + 0.10 * (hi - lo)
    frac = _rolling_mean((close <= threshold).astype(float), _TD_YEAR)
    velocity = frac.diff(_TD_MO)
    return velocity.diff(_TD_MO)


def ddur_drv3_024_dsh_ath_vs_252d_spread_jerk_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of (days-since-ATH minus days-since-252d-high)."""
    spread = _days_since_expanding_high(close) - _days_since_rolling_high(close, _TD_YEAR)
    velocity = spread.diff(5)
    return velocity.diff(5)


def ddur_drv3_025_dsh_intraday_high_252d_jerk_5d(high: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of days-since-252d-intraday-high."""
    velocity = _days_since_rolling_high(high, _TD_YEAR).diff(5)
    return velocity.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DURATION_REGISTRY_3RD_DERIVATIVES = {
    "ddur_drv3_001_dsh_252d_acceleration_of_velocity_5d": {"inputs": ["close"], "func": ddur_drv3_001_dsh_252d_acceleration_of_velocity_5d},
    "ddur_drv3_002_dsh_ath_acceleration_of_velocity_5d": {"inputs": ["close"], "func": ddur_drv3_002_dsh_ath_acceleration_of_velocity_5d},
    "ddur_drv3_003_dsh_252d_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_003_dsh_252d_jerk_21d},
    "ddur_drv3_004_dsh_ath_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_004_dsh_ath_jerk_21d},
    "ddur_drv3_005_consec_under_252d_high_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_005_consec_under_252d_high_jerk_5d},
    "ddur_drv3_006_consec_under_ath_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_006_consec_under_ath_jerk_5d},
    "ddur_drv3_007_pct_time_under_252d_high_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_007_pct_time_under_252d_high_jerk_21d},
    "ddur_drv3_008_composite_age_index_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_008_composite_age_index_jerk_5d},
    "ddur_drv3_009_composite_age_index_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_009_composite_age_index_jerk_21d},
    "ddur_drv3_010_days_since_new_low_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_010_days_since_new_low_jerk_5d},
    "ddur_drv3_011_new_low_freq_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_011_new_low_freq_jerk_21d},
    "ddur_drv3_012_exp_decay_dsh_252d_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_012_exp_decay_dsh_252d_jerk_5d},
    "ddur_drv3_013_exp_decay_dsh_ath_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_013_exp_decay_dsh_ath_jerk_21d},
    "ddur_drv3_014_dsh_252d_zscore_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_014_dsh_252d_zscore_jerk_5d},
    "ddur_drv3_015_days_under_20pct_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_015_days_under_20pct_jerk_21d},
    "ddur_drv3_016_consec_below_sma200_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_016_consec_below_sma200_jerk_5d},
    "ddur_drv3_017_pct_time_under_ath_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_017_pct_time_under_ath_jerk_21d},
    "ddur_drv3_018_dsh_252d_norm_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_018_dsh_252d_norm_jerk_5d},
    "ddur_drv3_019_vol_wtd_dsh_jerk_21d": {"inputs": ["close", "volume"], "func": ddur_drv3_019_vol_wtd_dsh_jerk_21d},
    "ddur_drv3_020_days_near_252d_low_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_020_days_near_252d_low_jerk_21d},
    "ddur_drv3_021_cross_horizon_persistence_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_021_cross_horizon_persistence_jerk_21d},
    "ddur_drv3_022_dsh_504d_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_022_dsh_504d_jerk_21d},
    "ddur_drv3_023_pct_days_bottom_decile_jerk_21d": {"inputs": ["close"], "func": ddur_drv3_023_pct_days_bottom_decile_jerk_21d},
    "ddur_drv3_024_dsh_ath_vs_252d_spread_jerk_5d": {"inputs": ["close"], "func": ddur_drv3_024_dsh_ath_vs_252d_spread_jerk_5d},
    "ddur_drv3_025_dsh_intraday_high_252d_jerk_5d": {"inputs": ["high"], "func": ddur_drv3_025_dsh_intraday_high_252d_jerk_5d},
}
