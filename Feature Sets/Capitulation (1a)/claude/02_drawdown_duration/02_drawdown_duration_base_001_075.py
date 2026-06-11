"""
02_drawdown_duration — Base Features 001-075
Domain: time in drawdown, days since high, persistence and age of the decline
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
    """1 if below rolling-window high, 0 otherwise."""
    return (s < _rolling_max(s, w)).astype(float)


def _underwater_expanding_flag(s: pd.Series) -> pd.Series:
    """1 if below all-time high, 0 otherwise."""
    return (s < s.cummax()).astype(float)


def _consec_streak(flag: pd.Series) -> pd.Series:
    """Current consecutive run length of flag==1."""
    groups = (flag == 0).cumsum()
    return flag.groupby(groups).cumsum()


# ── Feature functions 001–075 ─────────────────────────────────────────────────

# --- Group A: days since rolling high (close) ---

def ddur_001_days_since_21d_close_high(close: pd.Series) -> pd.Series:
    """Days since 21-day rolling close high."""
    return _days_since_rolling_high(close, _TD_MO)


def ddur_002_days_since_63d_close_high(close: pd.Series) -> pd.Series:
    """Days since 63-day rolling close high."""
    return _days_since_rolling_high(close, _TD_QTR)


def ddur_003_days_since_126d_close_high(close: pd.Series) -> pd.Series:
    """Days since 126-day rolling close high."""
    return _days_since_rolling_high(close, _TD_HALF)


def ddur_004_days_since_252d_close_high(close: pd.Series) -> pd.Series:
    """Days since 252-day rolling close high."""
    return _days_since_rolling_high(close, _TD_YEAR)


def ddur_005_days_since_504d_close_high(close: pd.Series) -> pd.Series:
    """Days since 504-day rolling close high."""
    return _days_since_rolling_high(close, 504)


def ddur_006_days_since_756d_close_high(close: pd.Series) -> pd.Series:
    """Days since 756-day rolling close high."""
    return _days_since_rolling_high(close, 756)


def ddur_007_days_since_1260d_close_high(close: pd.Series) -> pd.Series:
    """Days since 1260-day rolling close high."""
    return _days_since_rolling_high(close, 1260)


def ddur_008_days_since_ath_close(close: pd.Series) -> pd.Series:
    """Days since all-time (expanding) close high."""
    return _days_since_expanding_high(close)


# --- Group B: days since rolling high (high price) ---

def ddur_009_days_since_21d_intraday_high(high: pd.Series) -> pd.Series:
    """Days since 21-day rolling intraday high."""
    return _days_since_rolling_high(high, _TD_MO)


def ddur_010_days_since_63d_intraday_high(high: pd.Series) -> pd.Series:
    """Days since 63-day rolling intraday high."""
    return _days_since_rolling_high(high, _TD_QTR)


def ddur_011_days_since_252d_intraday_high(high: pd.Series) -> pd.Series:
    """Days since 252-day rolling intraday high."""
    return _days_since_rolling_high(high, _TD_YEAR)


def ddur_012_days_since_504d_intraday_high(high: pd.Series) -> pd.Series:
    """Days since 504-day rolling intraday high."""
    return _days_since_rolling_high(high, 504)


def ddur_013_days_since_ath_intraday_high(high: pd.Series) -> pd.Series:
    """Days since all-time (expanding) intraday high."""
    return _days_since_expanding_high(high)


# --- Group C: normalized days-since-high (fraction of window) ---

def ddur_014_days_since_252d_high_norm(close: pd.Series) -> pd.Series:
    """Days since 252d high as fraction of 252."""
    return _days_since_rolling_high(close, _TD_YEAR) / _TD_YEAR


def ddur_015_days_since_504d_high_norm(close: pd.Series) -> pd.Series:
    """Days since 504d high as fraction of 504."""
    return _days_since_rolling_high(close, 504) / 504.0


def ddur_016_days_since_1260d_high_norm(close: pd.Series) -> pd.Series:
    """Days since 1260d high as fraction of 1260."""
    return _days_since_rolling_high(close, 1260) / 1260.0


def ddur_017_days_since_ath_norm_by_age(close: pd.Series) -> pd.Series:
    """Days since ATH divided by total bars elapsed (fraction of life)."""
    pos = pd.Series(np.arange(len(close)), index=close.index).replace(0, np.nan)
    return _safe_div(_days_since_expanding_high(close), pos)


# --- Group D: consecutive days under rolling/expanding high ---

def ddur_018_consec_days_under_21d_high(close: pd.Series) -> pd.Series:
    """Consecutive days price has stayed below its 21-day high."""
    return _consec_streak(_underwater_flag(close, _TD_MO))


def ddur_019_consec_days_under_63d_high(close: pd.Series) -> pd.Series:
    """Consecutive days price has stayed below its 63-day high."""
    return _consec_streak(_underwater_flag(close, _TD_QTR))


def ddur_020_consec_days_under_252d_high(close: pd.Series) -> pd.Series:
    """Consecutive days price has stayed below its 252-day high."""
    return _consec_streak(_underwater_flag(close, _TD_YEAR))


def ddur_021_consec_days_under_504d_high(close: pd.Series) -> pd.Series:
    """Consecutive days price has stayed below its 504-day high."""
    return _consec_streak(_underwater_flag(close, 504))


def ddur_022_consec_days_under_ath(close: pd.Series) -> pd.Series:
    """Consecutive days price has stayed below all-time high."""
    return _consec_streak(_underwater_expanding_flag(close))


# --- Group E: fraction of window spent below high ---

def ddur_023_pct_days_under_21d_high_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days spent below 21d rolling high."""
    flag = _underwater_flag(close, _TD_MO)
    return _rolling_mean(flag, _TD_QTR)


def ddur_024_pct_days_under_63d_high_in_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63 days spent below 63d rolling high."""
    flag = _underwater_flag(close, _TD_QTR)
    return _rolling_mean(flag, _TD_QTR)


def ddur_025_pct_days_under_252d_high_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days spent below 252d rolling high."""
    flag = _underwater_flag(close, _TD_YEAR)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_026_pct_days_under_504d_high_in_504d(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days spent below 504d rolling high."""
    flag = _underwater_flag(close, 504)
    return _rolling_mean(flag, 504)


def ddur_027_pct_days_under_ath_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days spent below all-time high."""
    flag = _underwater_expanding_flag(close)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_028_pct_days_under_ath_in_504d(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days spent below all-time high."""
    flag = _underwater_expanding_flag(close)
    return _rolling_mean(flag, 504)


# --- Group F: days since rolling / expanding low (new-low recency) ---

def ddur_029_days_since_63d_close_low(close: pd.Series) -> pd.Series:
    """Days since 63-day rolling close low."""
    return _days_since_rolling_low(close, _TD_QTR)


def ddur_030_days_since_252d_close_low(close: pd.Series) -> pd.Series:
    """Days since 252-day rolling close low."""
    return _days_since_rolling_low(close, _TD_YEAR)


def ddur_031_days_since_504d_close_low(close: pd.Series) -> pd.Series:
    """Days since 504-day rolling close low."""
    return _days_since_rolling_low(close, 504)


def ddur_032_days_since_1260d_close_low(close: pd.Series) -> pd.Series:
    """Days since 1260-day rolling close low."""
    return _days_since_rolling_low(close, 1260)


def ddur_033_days_since_atl_close(close: pd.Series) -> pd.Series:
    """Days since all-time (expanding) close low."""
    return _days_since_expanding_low(close)


# --- Group G: depth-bucket duration (time spent in loss zones) ---

def ddur_034_days_under_5pct_from_252d_high_in_252d(close: pd.Series) -> pd.Series:
    """Days in last 252 spent more than 5% below 252d high."""
    h = _rolling_max(close, _TD_YEAR)
    return _rolling_sum((close < h * 0.95).astype(float), _TD_YEAR)


def ddur_035_days_under_10pct_from_252d_high_in_252d(close: pd.Series) -> pd.Series:
    """Days in last 252 spent more than 10% below 252d high."""
    h = _rolling_max(close, _TD_YEAR)
    return _rolling_sum((close < h * 0.90).astype(float), _TD_YEAR)


def ddur_036_days_under_20pct_from_252d_high_in_252d(close: pd.Series) -> pd.Series:
    """Days in last 252 spent more than 20% below 252d high."""
    h = _rolling_max(close, _TD_YEAR)
    return _rolling_sum((close < h * 0.80).astype(float), _TD_YEAR)


def ddur_037_days_under_30pct_from_504d_high_in_504d(close: pd.Series) -> pd.Series:
    """Days in last 504 spent more than 30% below 504d high."""
    h = _rolling_max(close, 504)
    return _rolling_sum((close < h * 0.70).astype(float), 504)


def ddur_038_days_under_50pct_from_ath_expanding(close: pd.Series) -> pd.Series:
    """Cumulative days spent more than 50% below all-time high."""
    h = close.cummax()
    return (close < h * 0.50).astype(float).expanding().sum()


def ddur_039_days_under_70pct_from_ath_expanding(close: pd.Series) -> pd.Series:
    """Cumulative days spent more than 70% below all-time high."""
    h = close.cummax()
    return (close < h * 0.30).astype(float).expanding().sum()


def ddur_040_days_near_252d_low_in_252d(close: pd.Series) -> pd.Series:
    """Days in last 252 within 5% above the 252d rolling low."""
    lo = _rolling_min(close, _TD_YEAR)
    return _rolling_sum((close <= lo * 1.05).astype(float), _TD_YEAR)


# --- Group H: multi-window composite age indices ---

def ddur_041_composite_age_index_3w(close: pd.Series) -> pd.Series:
    """Unweighted average of days-since-high across 21/63/252d."""
    d1 = _days_since_rolling_high(close, _TD_MO)
    d2 = _days_since_rolling_high(close, _TD_QTR)
    d3 = _days_since_rolling_high(close, _TD_YEAR)
    return (d1 + d2 + d3) / 3.0


def ddur_042_composite_age_index_5w(close: pd.Series) -> pd.Series:
    """Unweighted average of days-since-high across 21/63/126/252/504d."""
    d1 = _days_since_rolling_high(close, _TD_MO)
    d2 = _days_since_rolling_high(close, _TD_QTR)
    d3 = _days_since_rolling_high(close, _TD_HALF)
    d4 = _days_since_rolling_high(close, _TD_YEAR)
    d5 = _days_since_rolling_high(close, 504)
    return (d1 + d2 + d3 + d4 + d5) / 5.0


def ddur_043_weighted_age_index_ath_heavy(close: pd.Series) -> pd.Series:
    """Days-since-high weighted toward ATH (longer-horizon)."""
    d252 = _days_since_rolling_high(close, _TD_YEAR)
    dath = _days_since_expanding_high(close)
    return 0.3 * d252 + 0.7 * dath


def ddur_044_age_index_spread_ath_minus_252d(close: pd.Series) -> pd.Series:
    """Difference: days-since-ATH minus days-since-252d-high."""
    return _days_since_expanding_high(close) - _days_since_rolling_high(close, _TD_YEAR)


def ddur_045_age_index_ratio_ath_to_252d(close: pd.Series) -> pd.Series:
    """Ratio: days-since-ATH / days-since-252d-high."""
    return _safe_div(_days_since_expanding_high(close),
                     _days_since_rolling_high(close, _TD_YEAR))


# --- Group I: z-score / rank of duration features ---

def ddur_046_days_since_252d_high_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-252d-high over trailing 252-day window."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    return _safe_div(dsh - _rolling_mean(dsh, _TD_YEAR), _rolling_std(dsh, _TD_YEAR))


def ddur_047_days_since_ath_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 504-day window."""
    dsh = _days_since_expanding_high(close)
    return _safe_div(dsh - _rolling_mean(dsh, 504), _rolling_std(dsh, 504))


def ddur_048_days_since_252d_high_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-252d-high in own trailing 252d history."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    return dsh.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).rank(pct=True)


def ddur_049_days_since_ath_pctrank_expanding(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of days-since-ATH."""
    dsh = _days_since_expanding_high(close)
    return dsh.expanding(min_periods=1).rank(pct=True)


def ddur_050_pct_time_under_252d_high_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of fraction-of-time-below-252d-high over last 252 days."""
    frac = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    return _safe_div(frac - _rolling_mean(frac, _TD_YEAR), _rolling_std(frac, _TD_YEAR))


# --- Group J: time-since-high rolling statistics ---

def ddur_051_rolling_max_days_since_252d_high_in_504d(close: pd.Series) -> pd.Series:
    """Max of days-since-252d-high over trailing 504-day window."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    return dsh.rolling(504, min_periods=max(1, 126)).max()


def ddur_052_rolling_mean_days_since_63d_high_in_252d(close: pd.Series) -> pd.Series:
    """Mean of days-since-63d-high over trailing 252-day window."""
    dsh = _days_since_rolling_high(close, _TD_QTR)
    return _rolling_mean(dsh, _TD_YEAR)


def ddur_053_rolling_std_days_since_252d_high_in_252d(close: pd.Series) -> pd.Series:
    """Std dev of days-since-252d-high over trailing 252-day window."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    return _rolling_std(dsh, _TD_YEAR)


def ddur_054_rolling_max_days_since_ath_in_252d(close: pd.Series) -> pd.Series:
    """Max of days-since-ATH observed in the trailing 252-day window."""
    dsh = _days_since_expanding_high(close)
    return _rolling_mean(dsh, _TD_YEAR)


# --- Group K: volume-weighted / volume-conditioned duration ---

def ddur_055_vol_wtd_days_since_252d_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average days-since-252d-high over last 252 days."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    num = _rolling_sum(dsh * volume, _TD_YEAR)
    den = _rolling_sum(volume, _TD_YEAR)
    return _safe_div(num, den)


def ddur_056_high_vol_day_underwater_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of high-volume days (above 1.5x mean vol) that are below 252d high."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    hi_vol = (volume > avg_vol * 1.5).astype(float)
    underwater = _underwater_flag(close, _TD_YEAR)
    num = _rolling_sum(hi_vol * underwater, _TD_YEAR)
    den = _rolling_sum(hi_vol, _TD_YEAR)
    return _safe_div(num, den)


def ddur_057_low_vol_day_underwater_ratio_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of low-volume days (below 0.5x mean vol) that are below 252d high."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    lo_vol = (volume < avg_vol * 0.5).astype(float)
    underwater = _underwater_flag(close, _TD_YEAR)
    num = _rolling_sum(lo_vol * underwater, _TD_YEAR)
    den = _rolling_sum(lo_vol, _TD_YEAR)
    return _safe_div(num, den)


def ddur_058_days_since_vol_spike_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since the most recent day that was both a 63d close high and a volume spike (>2x avg)."""
    avg_vol = _rolling_mean(volume, _TD_QTR)
    is_close_high = (close == _rolling_max(close, _TD_QTR))
    vol_spike = (volume > avg_vol * 2.0)
    event = (is_close_high & vol_spike)
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(event).ffill()
    return (pos - last_pos).fillna(pos)


# --- Group L: SMA / EMA-anchored duration ---

def ddur_059_days_since_sma50_high(close: pd.Series) -> pd.Series:
    """Days since the 50-day SMA reached its 252-day high."""
    sma = _rolling_mean(close, 50)
    return _days_since_rolling_high(sma, _TD_YEAR)


def ddur_060_days_since_sma200_high(close: pd.Series) -> pd.Series:
    """Days since the 200-day SMA reached its 252-day high."""
    sma = _rolling_mean(close, 200)
    return _days_since_rolling_high(sma, _TD_YEAR)


def ddur_061_consec_days_below_sma50(close: pd.Series) -> pd.Series:
    """Consecutive days close has stayed below 50-day SMA."""
    sma = _rolling_mean(close, 50)
    flag = (close < sma).astype(float)
    return _consec_streak(flag)


def ddur_062_consec_days_below_sma200(close: pd.Series) -> pd.Series:
    """Consecutive days close has stayed below 200-day SMA."""
    sma = _rolling_mean(close, 200)
    flag = (close < sma).astype(float)
    return _consec_streak(flag)


def ddur_063_pct_days_below_sma200_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days spent below 200-day SMA."""
    sma = _rolling_mean(close, 200)
    flag = (close < sma).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_064_days_since_last_sma50_cross_below_sma200(close: pd.Series) -> pd.Series:
    """Days since 50-SMA crossed below 200-SMA (death cross)."""
    sma50 = _rolling_mean(close, 50)
    sma200 = _rolling_mean(close, 200)
    cross = ((sma50 < sma200) & (sma50.shift(1) >= sma200.shift(1)))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(cross).ffill()
    return (pos - last_pos).fillna(pos)


# --- Group M: decay / half-life functions ---

def ddur_065_exp_decay_days_since_252d_high(close: pd.Series) -> pd.Series:
    """Exponential decay of days-since-252d-high (half-life = 63 days)."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    return np.exp(-dsh / _TD_QTR)


def ddur_066_exp_decay_days_since_ath(close: pd.Series) -> pd.Series:
    """Exponential decay of days-since-ATH (half-life = 252 days)."""
    dsh = _days_since_expanding_high(close)
    return np.exp(-dsh / _TD_YEAR)


def ddur_067_linear_decay_days_since_252d_high(close: pd.Series) -> pd.Series:
    """Linear decay weight: 1 - (dsh/252), clipped to [0,1]."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    return (1.0 - dsh / _TD_YEAR).clip(0.0, 1.0)


# --- Group N: OHLC spread duration features ---

def ddur_068_days_since_252d_high_open(open: pd.Series) -> pd.Series:
    """Days since 252-day rolling open high."""
    return _days_since_rolling_high(open, _TD_YEAR)


def ddur_069_days_since_252d_low_low(low: pd.Series) -> pd.Series:
    """Days since 252-day rolling intraday low."""
    return _days_since_rolling_low(low, _TD_YEAR)


def ddur_070_days_since_atl_intraday_low(low: pd.Series) -> pd.Series:
    """Days since all-time (expanding) intraday low."""
    return _days_since_expanding_low(low)


def ddur_071_consec_days_low_below_prior_low_21d(low: pd.Series) -> pd.Series:
    """Consecutive days the intraday low is below the 21-day rolling min (prior close)."""
    roll_low = _rolling_min(low, _TD_MO)
    flag = (low <= roll_low).astype(float)
    return _consec_streak(flag)


def ddur_072_pct_days_close_below_open_in_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close < open (down-close days)."""
    flag = (close < open).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group O: volume-duration combined ---

def ddur_073_days_since_252d_high_volume(volume: pd.Series) -> pd.Series:
    """Days since peak volume over last 252 days."""
    return _days_since_rolling_high(volume, _TD_YEAR)


def ddur_074_days_since_ath_volume(volume: pd.Series) -> pd.Series:
    """Days since all-time (expanding) peak volume."""
    return _days_since_expanding_high(volume)


def ddur_075_pct_days_volume_below_252d_mean_in_252d(volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days where volume is below its 252-day mean (drying up)."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    flag = (volume < avg_vol).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DURATION_REGISTRY_001_075 = {
    "ddur_001_days_since_21d_close_high": {"inputs": ["close"], "func": ddur_001_days_since_21d_close_high},
    "ddur_002_days_since_63d_close_high": {"inputs": ["close"], "func": ddur_002_days_since_63d_close_high},
    "ddur_003_days_since_126d_close_high": {"inputs": ["close"], "func": ddur_003_days_since_126d_close_high},
    "ddur_004_days_since_252d_close_high": {"inputs": ["close"], "func": ddur_004_days_since_252d_close_high},
    "ddur_005_days_since_504d_close_high": {"inputs": ["close"], "func": ddur_005_days_since_504d_close_high},
    "ddur_006_days_since_756d_close_high": {"inputs": ["close"], "func": ddur_006_days_since_756d_close_high},
    "ddur_007_days_since_1260d_close_high": {"inputs": ["close"], "func": ddur_007_days_since_1260d_close_high},
    "ddur_008_days_since_ath_close": {"inputs": ["close"], "func": ddur_008_days_since_ath_close},
    "ddur_009_days_since_21d_intraday_high": {"inputs": ["high"], "func": ddur_009_days_since_21d_intraday_high},
    "ddur_010_days_since_63d_intraday_high": {"inputs": ["high"], "func": ddur_010_days_since_63d_intraday_high},
    "ddur_011_days_since_252d_intraday_high": {"inputs": ["high"], "func": ddur_011_days_since_252d_intraday_high},
    "ddur_012_days_since_504d_intraday_high": {"inputs": ["high"], "func": ddur_012_days_since_504d_intraday_high},
    "ddur_013_days_since_ath_intraday_high": {"inputs": ["high"], "func": ddur_013_days_since_ath_intraday_high},
    "ddur_014_days_since_252d_high_norm": {"inputs": ["close"], "func": ddur_014_days_since_252d_high_norm},
    "ddur_015_days_since_504d_high_norm": {"inputs": ["close"], "func": ddur_015_days_since_504d_high_norm},
    "ddur_016_days_since_1260d_high_norm": {"inputs": ["close"], "func": ddur_016_days_since_1260d_high_norm},
    "ddur_017_days_since_ath_norm_by_age": {"inputs": ["close"], "func": ddur_017_days_since_ath_norm_by_age},
    "ddur_018_consec_days_under_21d_high": {"inputs": ["close"], "func": ddur_018_consec_days_under_21d_high},
    "ddur_019_consec_days_under_63d_high": {"inputs": ["close"], "func": ddur_019_consec_days_under_63d_high},
    "ddur_020_consec_days_under_252d_high": {"inputs": ["close"], "func": ddur_020_consec_days_under_252d_high},
    "ddur_021_consec_days_under_504d_high": {"inputs": ["close"], "func": ddur_021_consec_days_under_504d_high},
    "ddur_022_consec_days_under_ath": {"inputs": ["close"], "func": ddur_022_consec_days_under_ath},
    "ddur_023_pct_days_under_21d_high_in_63d": {"inputs": ["close"], "func": ddur_023_pct_days_under_21d_high_in_63d},
    "ddur_024_pct_days_under_63d_high_in_63d": {"inputs": ["close"], "func": ddur_024_pct_days_under_63d_high_in_63d},
    "ddur_025_pct_days_under_252d_high_in_252d": {"inputs": ["close"], "func": ddur_025_pct_days_under_252d_high_in_252d},
    "ddur_026_pct_days_under_504d_high_in_504d": {"inputs": ["close"], "func": ddur_026_pct_days_under_504d_high_in_504d},
    "ddur_027_pct_days_under_ath_in_252d": {"inputs": ["close"], "func": ddur_027_pct_days_under_ath_in_252d},
    "ddur_028_pct_days_under_ath_in_504d": {"inputs": ["close"], "func": ddur_028_pct_days_under_ath_in_504d},
    "ddur_029_days_since_63d_close_low": {"inputs": ["close"], "func": ddur_029_days_since_63d_close_low},
    "ddur_030_days_since_252d_close_low": {"inputs": ["close"], "func": ddur_030_days_since_252d_close_low},
    "ddur_031_days_since_504d_close_low": {"inputs": ["close"], "func": ddur_031_days_since_504d_close_low},
    "ddur_032_days_since_1260d_close_low": {"inputs": ["close"], "func": ddur_032_days_since_1260d_close_low},
    "ddur_033_days_since_atl_close": {"inputs": ["close"], "func": ddur_033_days_since_atl_close},
    "ddur_034_days_under_5pct_from_252d_high_in_252d": {"inputs": ["close"], "func": ddur_034_days_under_5pct_from_252d_high_in_252d},
    "ddur_035_days_under_10pct_from_252d_high_in_252d": {"inputs": ["close"], "func": ddur_035_days_under_10pct_from_252d_high_in_252d},
    "ddur_036_days_under_20pct_from_252d_high_in_252d": {"inputs": ["close"], "func": ddur_036_days_under_20pct_from_252d_high_in_252d},
    "ddur_037_days_under_30pct_from_504d_high_in_504d": {"inputs": ["close"], "func": ddur_037_days_under_30pct_from_504d_high_in_504d},
    "ddur_038_days_under_50pct_from_ath_expanding": {"inputs": ["close"], "func": ddur_038_days_under_50pct_from_ath_expanding},
    "ddur_039_days_under_70pct_from_ath_expanding": {"inputs": ["close"], "func": ddur_039_days_under_70pct_from_ath_expanding},
    "ddur_040_days_near_252d_low_in_252d": {"inputs": ["close"], "func": ddur_040_days_near_252d_low_in_252d},
    "ddur_041_composite_age_index_3w": {"inputs": ["close"], "func": ddur_041_composite_age_index_3w},
    "ddur_042_composite_age_index_5w": {"inputs": ["close"], "func": ddur_042_composite_age_index_5w},
    "ddur_043_weighted_age_index_ath_heavy": {"inputs": ["close"], "func": ddur_043_weighted_age_index_ath_heavy},
    "ddur_044_age_index_spread_ath_minus_252d": {"inputs": ["close"], "func": ddur_044_age_index_spread_ath_minus_252d},
    "ddur_045_age_index_ratio_ath_to_252d": {"inputs": ["close"], "func": ddur_045_age_index_ratio_ath_to_252d},
    "ddur_046_days_since_252d_high_zscore_252d": {"inputs": ["close"], "func": ddur_046_days_since_252d_high_zscore_252d},
    "ddur_047_days_since_ath_zscore_504d": {"inputs": ["close"], "func": ddur_047_days_since_ath_zscore_504d},
    "ddur_048_days_since_252d_high_pctrank_252d": {"inputs": ["close"], "func": ddur_048_days_since_252d_high_pctrank_252d},
    "ddur_049_days_since_ath_pctrank_expanding": {"inputs": ["close"], "func": ddur_049_days_since_ath_pctrank_expanding},
    "ddur_050_pct_time_under_252d_high_zscore_252d": {"inputs": ["close"], "func": ddur_050_pct_time_under_252d_high_zscore_252d},
    "ddur_051_rolling_max_days_since_252d_high_in_504d": {"inputs": ["close"], "func": ddur_051_rolling_max_days_since_252d_high_in_504d},
    "ddur_052_rolling_mean_days_since_63d_high_in_252d": {"inputs": ["close"], "func": ddur_052_rolling_mean_days_since_63d_high_in_252d},
    "ddur_053_rolling_std_days_since_252d_high_in_252d": {"inputs": ["close"], "func": ddur_053_rolling_std_days_since_252d_high_in_252d},
    "ddur_054_rolling_max_days_since_ath_in_252d": {"inputs": ["close"], "func": ddur_054_rolling_max_days_since_ath_in_252d},
    "ddur_055_vol_wtd_days_since_252d_high": {"inputs": ["close", "volume"], "func": ddur_055_vol_wtd_days_since_252d_high},
    "ddur_056_high_vol_day_underwater_ratio_252d": {"inputs": ["close", "volume"], "func": ddur_056_high_vol_day_underwater_ratio_252d},
    "ddur_057_low_vol_day_underwater_ratio_252d": {"inputs": ["close", "volume"], "func": ddur_057_low_vol_day_underwater_ratio_252d},
    "ddur_058_days_since_vol_spike_high": {"inputs": ["close", "volume"], "func": ddur_058_days_since_vol_spike_high},
    "ddur_059_days_since_sma50_high": {"inputs": ["close"], "func": ddur_059_days_since_sma50_high},
    "ddur_060_days_since_sma200_high": {"inputs": ["close"], "func": ddur_060_days_since_sma200_high},
    "ddur_061_consec_days_below_sma50": {"inputs": ["close"], "func": ddur_061_consec_days_below_sma50},
    "ddur_062_consec_days_below_sma200": {"inputs": ["close"], "func": ddur_062_consec_days_below_sma200},
    "ddur_063_pct_days_below_sma200_in_252d": {"inputs": ["close"], "func": ddur_063_pct_days_below_sma200_in_252d},
    "ddur_064_days_since_last_sma50_cross_below_sma200": {"inputs": ["close"], "func": ddur_064_days_since_last_sma50_cross_below_sma200},
    "ddur_065_exp_decay_days_since_252d_high": {"inputs": ["close"], "func": ddur_065_exp_decay_days_since_252d_high},
    "ddur_066_exp_decay_days_since_ath": {"inputs": ["close"], "func": ddur_066_exp_decay_days_since_ath},
    "ddur_067_linear_decay_days_since_252d_high": {"inputs": ["close"], "func": ddur_067_linear_decay_days_since_252d_high},
    "ddur_068_days_since_252d_high_open": {"inputs": ["open"], "func": ddur_068_days_since_252d_high_open},
    "ddur_069_days_since_252d_low_low": {"inputs": ["low"], "func": ddur_069_days_since_252d_low_low},
    "ddur_070_days_since_atl_intraday_low": {"inputs": ["low"], "func": ddur_070_days_since_atl_intraday_low},
    "ddur_071_consec_days_low_below_prior_low_21d": {"inputs": ["low"], "func": ddur_071_consec_days_low_below_prior_low_21d},
    "ddur_072_pct_days_close_below_open_in_252d": {"inputs": ["close", "open"], "func": ddur_072_pct_days_close_below_open_in_252d},
    "ddur_073_days_since_252d_high_volume": {"inputs": ["volume"], "func": ddur_073_days_since_252d_high_volume},
    "ddur_074_days_since_ath_volume": {"inputs": ["volume"], "func": ddur_074_days_since_ath_volume},
    "ddur_075_pct_days_volume_below_252d_mean_in_252d": {"inputs": ["volume"], "func": ddur_075_pct_days_volume_below_252d_mean_in_252d},
}
