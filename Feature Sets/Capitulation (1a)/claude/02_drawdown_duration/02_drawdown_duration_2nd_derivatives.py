"""
02_drawdown_duration — 2nd Derivatives (001-025)
Domain: rate-of-change of base duration features; captures acceleration of decline
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


# ── 2nd Derivative Feature functions (001–025) ────────────────────────────────

def ddur_drv2_001_dsh_252d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of days-since-252d-high (diff of base feature ddur_004)."""
    return _days_since_rolling_high(close, _TD_YEAR).diff(5)


def ddur_drv2_002_dsh_ath_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of days-since-ATH (diff of base feature ddur_008)."""
    return _days_since_expanding_high(close).diff(5)


def ddur_drv2_003_dsh_252d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day velocity of days-since-252d-high."""
    return _days_since_rolling_high(close, _TD_YEAR).diff(_TD_MO)


def ddur_drv2_004_dsh_ath_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day velocity of days-since-ATH."""
    return _days_since_expanding_high(close).diff(_TD_MO)


def ddur_drv2_005_consec_under_252d_high_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in consecutive-days-below-252d-high streak (acceleration)."""
    streak = _consec_streak(_underwater_flag(close, _TD_YEAR))
    return streak.diff(5)


def ddur_drv2_006_consec_under_ath_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in consecutive-days-below-ATH streak."""
    streak = _consec_streak(_underwater_expanding_flag(close))
    return streak.diff(5)


def ddur_drv2_007_pct_time_under_252d_high_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in fraction-of-time-below-252d-high (acceleration of persistence)."""
    frac = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    return frac.diff(_TD_MO)


def ddur_drv2_008_pct_time_under_ath_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in fraction-of-time-below-ATH."""
    frac = _rolling_mean(_underwater_expanding_flag(close), _TD_YEAR)
    return frac.diff(_TD_MO)


def ddur_drv2_009_composite_age_index_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in composite drawdown age index (21/63/252d average)."""
    d1 = _days_since_rolling_high(close, _TD_MO)
    d2 = _days_since_rolling_high(close, _TD_QTR)
    d3 = _days_since_rolling_high(close, _TD_YEAR)
    idx = (d1 + d2 + d3) / 3.0
    return idx.diff(5)


def ddur_drv2_010_composite_age_index_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in composite drawdown age index (21/63/252d average)."""
    d1 = _days_since_rolling_high(close, _TD_MO)
    d2 = _days_since_rolling_high(close, _TD_QTR)
    d3 = _days_since_rolling_high(close, _TD_YEAR)
    idx = (d1 + d2 + d3) / 3.0
    return idx.diff(_TD_MO)


def ddur_drv2_011_days_since_new_low_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of days-since-252d-low."""
    dsl = _days_since_rolling_low(close, _TD_YEAR)
    return dsl.diff(5)


def ddur_drv2_012_new_low_freq_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in new-252d-low frequency (acceleration of new-low rate)."""
    is_low = (close == _rolling_min(close, _TD_YEAR)).astype(float)
    freq = _rolling_sum(is_low, _TD_YEAR)
    return freq.diff(_TD_MO)


def ddur_drv2_013_dsh_252d_norm_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of normalized days-since-252d-high (dsh/252)."""
    norm = _days_since_rolling_high(close, _TD_YEAR) / _TD_YEAR
    return norm.diff(5)


def ddur_drv2_014_exp_decay_dsh_252d_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of exp-decay of days-since-252d-high (acceleration of decay reversal)."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    decay = np.exp(-dsh / _TD_QTR)
    return decay.diff(5)


def ddur_drv2_015_exp_decay_dsh_ath_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day velocity of exp-decay of days-since-ATH."""
    dsh = _days_since_expanding_high(close)
    decay = np.exp(-dsh / _TD_YEAR)
    return decay.diff(_TD_MO)


def ddur_drv2_016_dsh_252d_zscore_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of z-score of days-since-252d-high."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    mu = _rolling_mean(dsh, _TD_YEAR)
    sigma = _rolling_std(dsh, _TD_YEAR)
    zscore = _safe_div(dsh - mu, sigma)
    return zscore.diff(5)


def ddur_drv2_017_days_under_20pct_from_252d_high_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in count of days-under-20%-from-252d-high."""
    h = _rolling_max(close, _TD_YEAR)
    days = _rolling_sum((close < h * 0.80).astype(float), _TD_YEAR)
    return days.diff(_TD_MO)


def ddur_drv2_018_consec_below_sma200_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day change in consecutive-days-below-200-SMA streak."""
    sma200 = _rolling_mean(close, 200)
    streak = _consec_streak((close < sma200).astype(float))
    return streak.diff(5)


def ddur_drv2_019_vol_wtd_dsh_252d_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day velocity of volume-weighted days-since-252d-high."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    num = _rolling_sum(dsh * volume, _TD_YEAR)
    den = _rolling_sum(volume, _TD_YEAR)
    vwtd = _safe_div(num, den)
    return vwtd.diff(_TD_MO)


def ddur_drv2_020_days_near_252d_low_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in days-spent-within-5%-of-252d-low count."""
    lo = _rolling_min(close, _TD_YEAR)
    days = _rolling_sum((close <= lo * 1.05).astype(float), _TD_YEAR)
    return days.diff(_TD_MO)


def ddur_drv2_021_dsh_504d_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day velocity of days-since-504d-high."""
    return _days_since_rolling_high(close, 504).diff(_TD_MO)


def ddur_drv2_022_pct_days_bottom_decile_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in fraction-of-days-in-bottom-decile of 252d price range."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    threshold = lo + 0.10 * (hi - lo)
    frac = _rolling_mean((close <= threshold).astype(float), _TD_YEAR)
    return frac.diff(_TD_MO)


def ddur_drv2_023_cross_horizon_persistence_velocity_21d(close: pd.Series) -> pd.Series:
    """21-day change in cross-horizon underwater persistence index."""
    f21 = _rolling_mean(_underwater_flag(close, _TD_MO), _TD_YEAR)
    f63 = _rolling_mean(_underwater_flag(close, _TD_QTR), _TD_YEAR)
    f252 = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    f504 = _rolling_mean(_underwater_flag(close, 504), _TD_YEAR)
    idx = (f21 + f63 + f252 + f504) / 4.0
    return idx.diff(_TD_MO)


def ddur_drv2_024_dsh_ath_vs_252d_spread_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day velocity of the spread (days-since-ATH minus days-since-252d-high)."""
    spread = _days_since_expanding_high(close) - _days_since_rolling_high(close, _TD_YEAR)
    return spread.diff(5)


def ddur_drv2_025_dsh_intraday_high_252d_velocity_5d(high: pd.Series) -> pd.Series:
    """5-day velocity of days-since-252d-intraday-high."""
    return _days_since_rolling_high(high, _TD_YEAR).diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DURATION_REGISTRY_2ND_DERIVATIVES = {
    "ddur_drv2_001_dsh_252d_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_001_dsh_252d_velocity_5d},
    "ddur_drv2_002_dsh_ath_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_002_dsh_ath_velocity_5d},
    "ddur_drv2_003_dsh_252d_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_003_dsh_252d_velocity_21d},
    "ddur_drv2_004_dsh_ath_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_004_dsh_ath_velocity_21d},
    "ddur_drv2_005_consec_under_252d_high_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_005_consec_under_252d_high_velocity_5d},
    "ddur_drv2_006_consec_under_ath_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_006_consec_under_ath_velocity_5d},
    "ddur_drv2_007_pct_time_under_252d_high_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_007_pct_time_under_252d_high_velocity_21d},
    "ddur_drv2_008_pct_time_under_ath_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_008_pct_time_under_ath_velocity_21d},
    "ddur_drv2_009_composite_age_index_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_009_composite_age_index_velocity_5d},
    "ddur_drv2_010_composite_age_index_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_010_composite_age_index_velocity_21d},
    "ddur_drv2_011_days_since_new_low_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_011_days_since_new_low_velocity_5d},
    "ddur_drv2_012_new_low_freq_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_012_new_low_freq_velocity_21d},
    "ddur_drv2_013_dsh_252d_norm_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_013_dsh_252d_norm_velocity_5d},
    "ddur_drv2_014_exp_decay_dsh_252d_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_014_exp_decay_dsh_252d_velocity_5d},
    "ddur_drv2_015_exp_decay_dsh_ath_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_015_exp_decay_dsh_ath_velocity_21d},
    "ddur_drv2_016_dsh_252d_zscore_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_016_dsh_252d_zscore_velocity_5d},
    "ddur_drv2_017_days_under_20pct_from_252d_high_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_017_days_under_20pct_from_252d_high_velocity_21d},
    "ddur_drv2_018_consec_below_sma200_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_018_consec_below_sma200_velocity_5d},
    "ddur_drv2_019_vol_wtd_dsh_252d_velocity_21d": {"inputs": ["close", "volume"], "func": ddur_drv2_019_vol_wtd_dsh_252d_velocity_21d},
    "ddur_drv2_020_days_near_252d_low_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_020_days_near_252d_low_velocity_21d},
    "ddur_drv2_021_dsh_504d_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_021_dsh_504d_velocity_21d},
    "ddur_drv2_022_pct_days_bottom_decile_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_022_pct_days_bottom_decile_velocity_21d},
    "ddur_drv2_023_cross_horizon_persistence_velocity_21d": {"inputs": ["close"], "func": ddur_drv2_023_cross_horizon_persistence_velocity_21d},
    "ddur_drv2_024_dsh_ath_vs_252d_spread_velocity_5d": {"inputs": ["close"], "func": ddur_drv2_024_dsh_ath_vs_252d_spread_velocity_5d},
    "ddur_drv2_025_dsh_intraday_high_252d_velocity_5d": {"inputs": ["high"], "func": ddur_drv2_025_dsh_intraday_high_252d_velocity_5d},
}
