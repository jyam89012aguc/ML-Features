"""
02_drawdown_duration — Base Features 076-150
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


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


# ── Feature functions 076–150 ─────────────────────────────────────────────────

# --- Group P: drawdown persistence / frequency of new highs ---

def ddur_076_new_high_frequency_63d(close: pd.Series) -> pd.Series:
    """Count of new 63d highs per day over last 63 days (inverse of drawdown persistence)."""
    is_high = (close == _rolling_max(close, _TD_QTR)).astype(float)
    return _rolling_sum(is_high, _TD_QTR)


def ddur_077_new_high_frequency_252d(close: pd.Series) -> pd.Series:
    """Count of new 252d highs per day over last 252 days."""
    is_high = (close == _rolling_max(close, _TD_YEAR)).astype(float)
    return _rolling_sum(is_high, _TD_YEAR)


def ddur_078_days_since_last_new_252d_high(close: pd.Series) -> pd.Series:
    """Days since close last set a new 252-day high."""
    is_high = (close == _rolling_max(close, _TD_YEAR))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(is_high).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_079_days_since_last_new_63d_high(close: pd.Series) -> pd.Series:
    """Days since close last set a new 63-day high."""
    is_high = (close == _rolling_max(close, _TD_QTR))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(is_high).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_080_days_since_last_new_21d_high(close: pd.Series) -> pd.Series:
    """Days since close last set a new 21-day high."""
    is_high = (close == _rolling_max(close, _TD_MO))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(is_high).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_081_no_new_high_streak_over_252d_flag(close: pd.Series) -> pd.Series:
    """1 if no new 252d high has been made in the last 252 days."""
    days_since = ddur_078_days_since_last_new_252d_high(close)
    return (days_since >= _TD_YEAR).astype(float)


def ddur_082_no_new_high_streak_over_504d_flag(close: pd.Series) -> pd.Series:
    """1 if no new 252d high has been made in the last 504 days."""
    days_since = ddur_078_days_since_last_new_252d_high(close)
    return (days_since >= 504).astype(float)


# --- Group Q: longest underwater streak in window ---

def ddur_083_longest_underwater_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of days below 252d high within trailing 252d."""
    flag = _underwater_flag(close, _TD_YEAR)
    streak = _consec_streak(flag)
    return streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).max()


def ddur_084_longest_underwater_streak_504d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of days below 252d high within trailing 504d."""
    flag = _underwater_flag(close, _TD_YEAR)
    streak = _consec_streak(flag)
    return streak.rolling(504, min_periods=max(1, 126)).max()


def ddur_085_longest_below_sma200_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of days below SMA200 within trailing 252d."""
    sma200 = _rolling_mean(close, 200)
    flag = (close < sma200).astype(float)
    streak = _consec_streak(flag)
    return streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).max()


def ddur_086_longest_down_close_streak_252d(close: pd.Series) -> pd.Series:
    """Longest consecutive run of down-close days in trailing 252d."""
    flag = (close < close.shift(1)).astype(float)
    streak = _consec_streak(flag)
    return streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).max()


# --- Group R: VWAP-based duration ---

def ddur_087_days_since_vwap_21d_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since 21-day VWAP reached its 252d high."""
    vwap = _safe_div(
        _rolling_sum(close * volume, _TD_MO),
        _rolling_sum(volume, _TD_MO)
    )
    return _days_since_rolling_high(vwap, _TD_YEAR)


def ddur_088_days_since_vwap_63d_high(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since 63-day VWAP reached its 252d high."""
    vwap = _safe_div(
        _rolling_sum(close * volume, _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    return _days_since_rolling_high(vwap, _TD_YEAR)


def ddur_089_consec_days_close_below_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days close has stayed below 21-day VWAP."""
    vwap = _safe_div(
        _rolling_sum(close * volume, _TD_MO),
        _rolling_sum(volume, _TD_MO)
    )
    flag = (close < vwap).astype(float)
    return _consec_streak(flag)


def ddur_090_pct_days_close_below_vwap_63d_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days close has stayed below 63-day VWAP."""
    vwap = _safe_div(
        _rolling_sum(close * volume, _TD_QTR),
        _rolling_sum(volume, _TD_QTR)
    )
    flag = (close < vwap).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group S: high-price-only duration features ---

def ddur_091_pct_days_high_below_prior_high_in_252d(high: pd.Series) -> pd.Series:
    """Fraction of last 252 days intraday high is below prior-day intraday high (lower-highs)."""
    flag = (high < high.shift(1)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_092_consec_lower_highs(high: pd.Series) -> pd.Series:
    """Consecutive days of lower intraday highs (lower-high streak)."""
    flag = (high < high.shift(1)).astype(float)
    return _consec_streak(flag)


def ddur_093_consec_lower_lows(low: pd.Series) -> pd.Series:
    """Consecutive days of lower intraday lows (lower-low streak)."""
    flag = (low < low.shift(1)).astype(float)
    return _consec_streak(flag)


def ddur_094_days_since_252d_intraday_low_low(low: pd.Series) -> pd.Series:
    """Days since rolling 252d intraday low was set."""
    return _days_since_rolling_low(low, _TD_YEAR)


def ddur_095_days_since_atl_intraday_low_expanding(low: pd.Series) -> pd.Series:
    """Days since all-time intraday low was set (expanding)."""
    return _days_since_expanding_low(low)


# --- Group T: range-compression duration ---

def ddur_096_days_since_252d_range_high(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since 252d high of (high-low) daily range."""
    rng = high - low
    return _days_since_rolling_high(rng, _TD_YEAR)


def ddur_097_consec_days_range_below_252d_mean(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days the intraday range is below its 252-day mean (compression)."""
    rng = high - low
    avg_rng = _rolling_mean(rng, _TD_YEAR)
    flag = (rng < avg_rng).astype(float)
    return _consec_streak(flag)


def ddur_098_pct_days_hl_range_compressed_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 252 days range is in bottom 25th percentile of its own 252d history."""
    rng = high - low
    pct25 = rng.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).quantile(0.25)
    flag = (rng <= pct25).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group U: drawdown cohort duration (compare windows) ---

def ddur_099_dsh_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of days-since-21d-high to days-since-252d-high."""
    d21 = _days_since_rolling_high(close, _TD_MO)
    d252 = _days_since_rolling_high(close, _TD_YEAR)
    return _safe_div(d21, d252)


def ddur_100_dsh_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of days-since-63d-high to days-since-252d-high."""
    d63 = _days_since_rolling_high(close, _TD_QTR)
    d252 = _days_since_rolling_high(close, _TD_YEAR)
    return _safe_div(d63, d252)


def ddur_101_dsh_126d_vs_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of days-since-126d-high to days-since-504d-high."""
    d126 = _days_since_rolling_high(close, _TD_HALF)
    d504 = _days_since_rolling_high(close, 504)
    return _safe_div(d126, d504)


def ddur_102_dsl_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of days-since-63d-low to days-since-252d-low."""
    d63 = _days_since_rolling_low(close, _TD_QTR)
    d252 = _days_since_rolling_low(close, _TD_YEAR)
    return _safe_div(d63, d252)


def ddur_103_dsh_vs_dsl_252d(close: pd.Series) -> pd.Series:
    """Ratio of days-since-252d-high to days-since-252d-low."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    dsl = _days_since_rolling_low(close, _TD_YEAR)
    return _safe_div(dsh, dsl)


# --- Group V: new-low frequency / recency ---

def ddur_104_new_low_frequency_252d(close: pd.Series) -> pd.Series:
    """Count of new 252d lows in the last 252 days."""
    is_low = (close == _rolling_min(close, _TD_YEAR)).astype(float)
    return _rolling_sum(is_low, _TD_YEAR)


def ddur_105_new_low_frequency_504d(close: pd.Series) -> pd.Series:
    """Count of new 504d lows in the last 504 days."""
    is_low = (close == _rolling_min(close, 504)).astype(float)
    return _rolling_sum(is_low, 504)


def ddur_106_days_since_last_new_252d_low(close: pd.Series) -> pd.Series:
    """Days since close last set a new 252-day low."""
    is_low = (close == _rolling_min(close, _TD_YEAR))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(is_low).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_107_days_since_last_new_atl(close: pd.Series) -> pd.Series:
    """Days since close last set an all-time low."""
    return _days_since_expanding_low(close)


def ddur_108_avg_interval_between_252d_lows(close: pd.Series) -> pd.Series:
    """Average days between new 252d lows over trailing 504-day window."""
    is_low = (close == _rolling_min(close, _TD_YEAR)).astype(float)
    count = _rolling_sum(is_low, 504)
    return _safe_div(pd.Series(504.0, index=close.index), count)


# --- Group W: duration normalized by volatility ---

def ddur_109_dsh_252d_vol_scaled(close: pd.Series) -> pd.Series:
    """Days-since-252d-high scaled by 21-day realized vol (annualized)."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    vol = close.pct_change().rolling(_TD_MO, min_periods=5).std() * np.sqrt(_TD_YEAR)
    return dsh * vol.fillna(vol.expanding().mean())


def ddur_110_dsh_ath_vol_scaled(close: pd.Series) -> pd.Series:
    """Days-since-ATH scaled by 63-day realized vol (annualized)."""
    dsh = _days_since_expanding_high(close)
    vol = close.pct_change().rolling(_TD_QTR, min_periods=10).std() * np.sqrt(_TD_YEAR)
    return dsh * vol.fillna(vol.expanding().mean())


def ddur_111_dsh_252d_per_unit_vol(close: pd.Series) -> pd.Series:
    """Days-since-252d-high divided by 63-day vol (time-per-vol-unit)."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    vol = close.pct_change().rolling(_TD_QTR, min_periods=10).std() * np.sqrt(_TD_YEAR)
    return _safe_div(dsh, vol)


def ddur_112_vol_regime_adjusted_dsh(close: pd.Series) -> pd.Series:
    """Days-since-252d-high minus its 252d mean, scaled by its 252d std."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    mu = _rolling_mean(dsh, _TD_YEAR)
    sigma = _rolling_std(dsh, _TD_YEAR)
    return _safe_div(dsh - mu, sigma)


# --- Group X: price-range underwater flags ---

def ddur_113_pct_days_close_in_bottom_decile_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days close was in bottom 10% of its 252d range."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    rng = hi - lo
    threshold = lo + 0.10 * rng
    flag = (close <= threshold).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_114_pct_days_close_in_bottom_quartile_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days close was in bottom 25% of its 252d range."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    rng = hi - lo
    threshold = lo + 0.25 * rng
    flag = (close <= threshold).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_115_consec_days_in_bottom_quartile_252d(close: pd.Series) -> pd.Series:
    """Consecutive days close is in the bottom 25% of its 252d price range."""
    lo = _rolling_min(close, _TD_YEAR)
    hi = _rolling_max(close, _TD_YEAR)
    rng = hi - lo
    threshold = lo + 0.25 * rng
    flag = (close <= threshold).astype(float)
    return _consec_streak(flag)


def ddur_116_pct_days_close_in_bottom_decile_504d(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days close was in bottom 10% of its 504d range."""
    lo = _rolling_min(close, 504)
    hi = _rolling_max(close, 504)
    rng = hi - lo
    threshold = lo + 0.10 * rng
    flag = (close <= threshold).astype(float)
    return _rolling_mean(flag, 504)


# --- Group Y: SMA slope duration ---

def ddur_117_days_since_sma50_turned_negative_slope(close: pd.Series) -> pd.Series:
    """Days since 50-day SMA slope (1-day diff) turned negative."""
    sma = _rolling_mean(close, 50)
    neg_slope = (sma.diff(1) < 0)
    cross = neg_slope & (~neg_slope.shift(1).fillna(False))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(cross).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_118_days_since_sma200_turned_negative_slope(close: pd.Series) -> pd.Series:
    """Days since 200-day SMA slope (1-day diff) turned negative."""
    sma = _rolling_mean(close, 200)
    neg_slope = (sma.diff(1) < 0)
    cross = neg_slope & (~neg_slope.shift(1).fillna(False))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(cross).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_119_consec_days_sma50_slope_negative(close: pd.Series) -> pd.Series:
    """Consecutive days the 50-day SMA slope has been negative."""
    sma = _rolling_mean(close, 50)
    flag = (sma.diff(1) < 0).astype(float)
    return _consec_streak(flag)


def ddur_120_consec_days_sma200_slope_negative(close: pd.Series) -> pd.Series:
    """Consecutive days the 200-day SMA slope has been negative."""
    sma = _rolling_mean(close, 200)
    flag = (sma.diff(1) < 0).astype(float)
    return _consec_streak(flag)


# --- Group Z: combined high+volume duration ---

def ddur_121_days_since_last_close_high_on_high_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last day that was simultaneously a 63d close high and above-avg volume."""
    is_high = (close == _rolling_max(close, _TD_QTR))
    avg_vol = _rolling_mean(volume, _TD_QTR)
    event = (is_high & (volume > avg_vol))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(event).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_122_days_since_last_close_low_on_high_vol(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last day that was simultaneously a 63d close low and above-avg volume."""
    is_low = (close == _rolling_min(close, _TD_QTR))
    avg_vol = _rolling_mean(volume, _TD_QTR)
    event = (is_low & (volume > avg_vol))
    pos = pd.Series(np.arange(len(close)), index=close.index)
    last_pos = pos.where(event).ffill()
    return (pos - last_pos).fillna(pos)


def ddur_123_pct_days_ath_underwater_high_vol_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 days that are both below ATH and high-volume (>1.5x avg)."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    underwater = _underwater_expanding_flag(close)
    hi_vol = (volume > avg_vol * 1.5).astype(float)
    return _rolling_mean(underwater * hi_vol, _TD_YEAR)


# --- Group AA: momentum duration (streaks of return sign) ---

def ddur_124_consec_days_negative_return(close: pd.Series) -> pd.Series:
    """Consecutive days of negative daily returns."""
    ret = close.pct_change()
    flag = (ret < 0).astype(float)
    return _consec_streak(flag)


def ddur_125_consec_weeks_negative_return(close: pd.Series) -> pd.Series:
    """Consecutive 5-day periods with negative cumulative return."""
    ret5 = close.pct_change(5)
    flag = (ret5 < 0).astype(float)
    return _consec_streak(flag)


def ddur_126_consec_months_negative_return(close: pd.Series) -> pd.Series:
    """Consecutive 21-day periods with negative cumulative return."""
    ret21 = close.pct_change(_TD_MO)
    flag = (ret21 < 0).astype(float)
    return _consec_streak(flag)


def ddur_127_pct_negative_return_days_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days with negative daily return."""
    ret = close.pct_change()
    flag = (ret < 0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def ddur_128_pct_negative_return_weeks_in_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 bars where the 5-day return is negative."""
    ret5 = close.pct_change(5)
    flag = (ret5 < 0).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Group AB: drawdown age indexed to volatility regime ---

def ddur_129_dsh_to_half_vol_life(close: pd.Series) -> pd.Series:
    """Days-since-252d-high normalized by vol half-life (63 days * vol)."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    vol = close.pct_change().rolling(_TD_QTR, min_periods=10).std()
    half_life = _TD_QTR * vol.fillna(vol.expanding().mean())
    return _safe_div(dsh, half_life)


def ddur_130_underwater_duration_score(close: pd.Series) -> pd.Series:
    """Composite: days-since-ATH / (1 + 252d vol), penalizing longer underwater stays."""
    dsh = _days_since_expanding_high(close)
    vol = close.pct_change().rolling(_TD_YEAR, min_periods=50).std() * np.sqrt(_TD_YEAR)
    return _safe_div(dsh, 1.0 + vol.fillna(vol.expanding().mean()))


# --- Group AC: cross-horizon persistence of underwater state ---

def ddur_131_persistence_ratio_21d_vs_252d_underwater(close: pd.Series) -> pd.Series:
    """Ratio: fraction-under-21d-high / fraction-under-252d-high, over 252d."""
    f21 = _rolling_mean(_underwater_flag(close, _TD_MO), _TD_YEAR)
    f252 = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    return _safe_div(f21, f252)


def ddur_132_persistence_ratio_63d_vs_504d_underwater(close: pd.Series) -> pd.Series:
    """Ratio: fraction-under-63d-high / fraction-under-504d-high, over 252d."""
    f63 = _rolling_mean(_underwater_flag(close, _TD_QTR), _TD_YEAR)
    f504 = _rolling_mean(_underwater_flag(close, 504), _TD_YEAR)
    return _safe_div(f63, f504)


def ddur_133_cross_horizon_persistence_index(close: pd.Series) -> pd.Series:
    """Average of fraction-underwater across 21/63/252/504d horizons."""
    f21 = _rolling_mean(_underwater_flag(close, _TD_MO), _TD_YEAR)
    f63 = _rolling_mean(_underwater_flag(close, _TD_QTR), _TD_YEAR)
    f252 = _rolling_mean(_underwater_flag(close, _TD_YEAR), _TD_YEAR)
    f504 = _rolling_mean(_underwater_flag(close, 504), _TD_YEAR)
    return (f21 + f63 + f252 + f504) / 4.0


# --- Group AD: time-since-high acceleration (higher-order) ---

def ddur_134_dsh_252d_acceleration_5d(close: pd.Series) -> pd.Series:
    """5-day change in days-since-252d-high (acceleration of drawdown age)."""
    return _days_since_rolling_high(close, _TD_YEAR).diff(5)


def ddur_135_dsh_ath_acceleration_21d(close: pd.Series) -> pd.Series:
    """21-day change in days-since-ATH."""
    return _days_since_expanding_high(close).diff(_TD_MO)


def ddur_136_dsh_ath_acceleration_63d(close: pd.Series) -> pd.Series:
    """63-day change in days-since-ATH."""
    return _days_since_expanding_high(close).diff(_TD_QTR)


# --- Group AE: OHLC-blend duration ---

def ddur_137_days_since_252d_high_typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since 252d high of typical price (H+L+C)/3."""
    tp = (high + low + close) / 3.0
    return _days_since_rolling_high(tp, _TD_YEAR)


def ddur_138_days_since_ath_typical_price(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since ATH of typical price (H+L+C)/3."""
    tp = (high + low + close) / 3.0
    return _days_since_expanding_high(tp)


def ddur_139_days_since_252d_high_weighted_close(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Days since 252d high of weighted close (H+L+2C)/4."""
    wc = (high + low + 2.0 * close) / 4.0
    return _days_since_rolling_high(wc, _TD_YEAR)


def ddur_140_consec_days_tp_below_sma200(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days typical price is below 200-day SMA of typical price."""
    tp = (high + low + close) / 3.0
    sma_tp = _rolling_mean(tp, 200)
    flag = (tp < sma_tp).astype(float)
    return _consec_streak(flag)


# --- Group AF: volume-time interaction ---

def ddur_141_vol_above_avg_while_underwater_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 252 underwater days (vs 252d high) that had above-avg volume."""
    underwater = _underwater_flag(close, _TD_YEAR)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    hi_vol = (volume > avg_vol).astype(float)
    num = _rolling_sum(underwater * hi_vol, _TD_YEAR)
    den = _rolling_sum(underwater, _TD_YEAR)
    return _safe_div(num, den)


def ddur_142_vol_trend_during_drawdown_duration(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of volume during underwater period: rolling corr of position vs volume."""
    underwater = _underwater_flag(close, _TD_YEAR)
    t = pd.Series(np.arange(len(close), dtype=float), index=close.index)
    vol_underwater = volume * underwater
    return vol_underwater.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).corr(t)


def ddur_143_avg_volume_on_new_low_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on days that set a new 252d closing low."""
    is_low = (close == _rolling_min(close, _TD_YEAR)).astype(float)
    vol_on_low = volume * is_low
    num = _rolling_sum(vol_on_low, _TD_YEAR)
    den = _rolling_sum(is_low, _TD_YEAR)
    return _safe_div(num, den)


# --- Group AG: percentile-rank of key time metrics ---

def ddur_144_pctrank_consec_days_under_252d_high_in_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of current consecutive-days-under-252d-high in trailing 504d."""
    streak = _consec_streak(_underwater_flag(close, _TD_YEAR))
    return streak.rolling(504, min_periods=max(1, 126)).rank(pct=True)


def ddur_145_pctrank_days_since_new_low_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of days-since-252d-low in trailing 252d."""
    dsl = _days_since_rolling_low(close, _TD_YEAR)
    return dsl.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).rank(pct=True)


def ddur_146_pctrank_longest_streak_under_ath_in_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of longest-ever streak below ATH in trailing 504d."""
    streak = _consec_streak(_underwater_expanding_flag(close))
    max_streak = streak.rolling(504, min_periods=max(1, 126)).max()
    return max_streak.rolling(504, min_periods=max(1, 126)).rank(pct=True)


# --- Group AH: multi-asset / volume-proxy synthetic features ---

def ddur_147_dollar_vol_wtd_days_since_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar-volume-weighted days-since-ATH over last 252 days."""
    dsh = _days_since_expanding_high(close)
    dollar_vol = close * volume
    num = _rolling_sum(dsh * dollar_vol, _TD_YEAR)
    den = _rolling_sum(dollar_vol, _TD_YEAR)
    return _safe_div(num, den)


def ddur_148_avg_dsh_252d_high_per_vol_decile(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days-since-252d-high on days when volume > 90th percentile of trailing 252d volume."""
    dsh = _days_since_rolling_high(close, _TD_YEAR)
    q90 = volume.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).quantile(0.90)
    hi_vol = (volume >= q90).astype(float)
    num = _rolling_sum(dsh * hi_vol, _TD_YEAR)
    den = _rolling_sum(hi_vol, _TD_YEAR)
    return _safe_div(num, den)


def ddur_149_time_in_drawdown_entropy_252d(close: pd.Series) -> pd.Series:
    """Entropy of daily underwater flag (binary) over 252d — measures persistence vs noise."""
    flag = _underwater_flag(close, _TD_YEAR)
    p = _rolling_mean(flag, _TD_YEAR).clip(_EPS, 1 - _EPS)
    return -(p * np.log(p) + (1 - p) * np.log(1 - p))


def ddur_150_time_in_drawdown_hurst_proxy_252d(close: pd.Series) -> pd.Series:
    """Hurst-proxy for time-in-drawdown: ratio of 252d max streak to expected random streak."""
    flag = _underwater_flag(close, _TD_YEAR)
    streak = _consec_streak(flag)
    max_streak = streak.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).max()
    p = _rolling_mean(flag, _TD_YEAR).clip(_EPS, 1 - _EPS)
    expected = _safe_div(pd.Series(1.0, index=close.index), 1.0 - p)
    return _safe_div(max_streak, expected)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_DURATION_REGISTRY_076_150 = {
    "ddur_076_new_high_frequency_63d": {"inputs": ["close"], "func": ddur_076_new_high_frequency_63d},
    "ddur_077_new_high_frequency_252d": {"inputs": ["close"], "func": ddur_077_new_high_frequency_252d},
    "ddur_078_days_since_last_new_252d_high": {"inputs": ["close"], "func": ddur_078_days_since_last_new_252d_high},
    "ddur_079_days_since_last_new_63d_high": {"inputs": ["close"], "func": ddur_079_days_since_last_new_63d_high},
    "ddur_080_days_since_last_new_21d_high": {"inputs": ["close"], "func": ddur_080_days_since_last_new_21d_high},
    "ddur_081_no_new_high_streak_over_252d_flag": {"inputs": ["close"], "func": ddur_081_no_new_high_streak_over_252d_flag},
    "ddur_082_no_new_high_streak_over_504d_flag": {"inputs": ["close"], "func": ddur_082_no_new_high_streak_over_504d_flag},
    "ddur_083_longest_underwater_streak_252d": {"inputs": ["close"], "func": ddur_083_longest_underwater_streak_252d},
    "ddur_084_longest_underwater_streak_504d": {"inputs": ["close"], "func": ddur_084_longest_underwater_streak_504d},
    "ddur_085_longest_below_sma200_streak_252d": {"inputs": ["close"], "func": ddur_085_longest_below_sma200_streak_252d},
    "ddur_086_longest_down_close_streak_252d": {"inputs": ["close"], "func": ddur_086_longest_down_close_streak_252d},
    "ddur_087_days_since_vwap_21d_high": {"inputs": ["close", "volume"], "func": ddur_087_days_since_vwap_21d_high},
    "ddur_088_days_since_vwap_63d_high": {"inputs": ["close", "volume"], "func": ddur_088_days_since_vwap_63d_high},
    "ddur_089_consec_days_close_below_vwap_21d": {"inputs": ["close", "volume"], "func": ddur_089_consec_days_close_below_vwap_21d},
    "ddur_090_pct_days_close_below_vwap_63d_in_252d": {"inputs": ["close", "volume"], "func": ddur_090_pct_days_close_below_vwap_63d_in_252d},
    "ddur_091_pct_days_high_below_prior_high_in_252d": {"inputs": ["high"], "func": ddur_091_pct_days_high_below_prior_high_in_252d},
    "ddur_092_consec_lower_highs": {"inputs": ["high"], "func": ddur_092_consec_lower_highs},
    "ddur_093_consec_lower_lows": {"inputs": ["low"], "func": ddur_093_consec_lower_lows},
    "ddur_094_days_since_252d_intraday_low_low": {"inputs": ["low"], "func": ddur_094_days_since_252d_intraday_low_low},
    "ddur_095_days_since_atl_intraday_low_expanding": {"inputs": ["low"], "func": ddur_095_days_since_atl_intraday_low_expanding},
    "ddur_096_days_since_252d_range_high": {"inputs": ["close", "high", "low"], "func": ddur_096_days_since_252d_range_high},
    "ddur_097_consec_days_range_below_252d_mean": {"inputs": ["close", "high", "low"], "func": ddur_097_consec_days_range_below_252d_mean},
    "ddur_098_pct_days_hl_range_compressed_252d": {"inputs": ["high", "low"], "func": ddur_098_pct_days_hl_range_compressed_252d},
    "ddur_099_dsh_21d_vs_252d_ratio": {"inputs": ["close"], "func": ddur_099_dsh_21d_vs_252d_ratio},
    "ddur_100_dsh_63d_vs_252d_ratio": {"inputs": ["close"], "func": ddur_100_dsh_63d_vs_252d_ratio},
    "ddur_101_dsh_126d_vs_504d_ratio": {"inputs": ["close"], "func": ddur_101_dsh_126d_vs_504d_ratio},
    "ddur_102_dsl_63d_vs_252d_ratio": {"inputs": ["close"], "func": ddur_102_dsl_63d_vs_252d_ratio},
    "ddur_103_dsh_vs_dsl_252d": {"inputs": ["close"], "func": ddur_103_dsh_vs_dsl_252d},
    "ddur_104_new_low_frequency_252d": {"inputs": ["close"], "func": ddur_104_new_low_frequency_252d},
    "ddur_105_new_low_frequency_504d": {"inputs": ["close"], "func": ddur_105_new_low_frequency_504d},
    "ddur_106_days_since_last_new_252d_low": {"inputs": ["close"], "func": ddur_106_days_since_last_new_252d_low},
    "ddur_107_days_since_last_new_atl": {"inputs": ["close"], "func": ddur_107_days_since_last_new_atl},
    "ddur_108_avg_interval_between_252d_lows": {"inputs": ["close"], "func": ddur_108_avg_interval_between_252d_lows},
    "ddur_109_dsh_252d_vol_scaled": {"inputs": ["close"], "func": ddur_109_dsh_252d_vol_scaled},
    "ddur_110_dsh_ath_vol_scaled": {"inputs": ["close"], "func": ddur_110_dsh_ath_vol_scaled},
    "ddur_111_dsh_252d_per_unit_vol": {"inputs": ["close"], "func": ddur_111_dsh_252d_per_unit_vol},
    "ddur_112_vol_regime_adjusted_dsh": {"inputs": ["close"], "func": ddur_112_vol_regime_adjusted_dsh},
    "ddur_113_pct_days_close_in_bottom_decile_252d": {"inputs": ["close"], "func": ddur_113_pct_days_close_in_bottom_decile_252d},
    "ddur_114_pct_days_close_in_bottom_quartile_252d": {"inputs": ["close"], "func": ddur_114_pct_days_close_in_bottom_quartile_252d},
    "ddur_115_consec_days_in_bottom_quartile_252d": {"inputs": ["close"], "func": ddur_115_consec_days_in_bottom_quartile_252d},
    "ddur_116_pct_days_close_in_bottom_decile_504d": {"inputs": ["close"], "func": ddur_116_pct_days_close_in_bottom_decile_504d},
    "ddur_117_days_since_sma50_turned_negative_slope": {"inputs": ["close"], "func": ddur_117_days_since_sma50_turned_negative_slope},
    "ddur_118_days_since_sma200_turned_negative_slope": {"inputs": ["close"], "func": ddur_118_days_since_sma200_turned_negative_slope},
    "ddur_119_consec_days_sma50_slope_negative": {"inputs": ["close"], "func": ddur_119_consec_days_sma50_slope_negative},
    "ddur_120_consec_days_sma200_slope_negative": {"inputs": ["close"], "func": ddur_120_consec_days_sma200_slope_negative},
    "ddur_121_days_since_last_close_high_on_high_vol": {"inputs": ["close", "volume"], "func": ddur_121_days_since_last_close_high_on_high_vol},
    "ddur_122_days_since_last_close_low_on_high_vol": {"inputs": ["close", "volume"], "func": ddur_122_days_since_last_close_low_on_high_vol},
    "ddur_123_pct_days_ath_underwater_high_vol_in_252d": {"inputs": ["close", "volume"], "func": ddur_123_pct_days_ath_underwater_high_vol_in_252d},
    "ddur_124_consec_days_negative_return": {"inputs": ["close"], "func": ddur_124_consec_days_negative_return},
    "ddur_125_consec_weeks_negative_return": {"inputs": ["close"], "func": ddur_125_consec_weeks_negative_return},
    "ddur_126_consec_months_negative_return": {"inputs": ["close"], "func": ddur_126_consec_months_negative_return},
    "ddur_127_pct_negative_return_days_in_252d": {"inputs": ["close"], "func": ddur_127_pct_negative_return_days_in_252d},
    "ddur_128_pct_negative_return_weeks_in_252d": {"inputs": ["close"], "func": ddur_128_pct_negative_return_weeks_in_252d},
    "ddur_129_dsh_to_half_vol_life": {"inputs": ["close"], "func": ddur_129_dsh_to_half_vol_life},
    "ddur_130_underwater_duration_score": {"inputs": ["close"], "func": ddur_130_underwater_duration_score},
    "ddur_131_persistence_ratio_21d_vs_252d_underwater": {"inputs": ["close"], "func": ddur_131_persistence_ratio_21d_vs_252d_underwater},
    "ddur_132_persistence_ratio_63d_vs_504d_underwater": {"inputs": ["close"], "func": ddur_132_persistence_ratio_63d_vs_504d_underwater},
    "ddur_133_cross_horizon_persistence_index": {"inputs": ["close"], "func": ddur_133_cross_horizon_persistence_index},
    "ddur_134_dsh_252d_acceleration_5d": {"inputs": ["close"], "func": ddur_134_dsh_252d_acceleration_5d},
    "ddur_135_dsh_ath_acceleration_21d": {"inputs": ["close"], "func": ddur_135_dsh_ath_acceleration_21d},
    "ddur_136_dsh_ath_acceleration_63d": {"inputs": ["close"], "func": ddur_136_dsh_ath_acceleration_63d},
    "ddur_137_days_since_252d_high_typical_price": {"inputs": ["close", "high", "low"], "func": ddur_137_days_since_252d_high_typical_price},
    "ddur_138_days_since_ath_typical_price": {"inputs": ["close", "high", "low"], "func": ddur_138_days_since_ath_typical_price},
    "ddur_139_days_since_252d_high_weighted_close": {"inputs": ["close", "high", "low"], "func": ddur_139_days_since_252d_high_weighted_close},
    "ddur_140_consec_days_tp_below_sma200": {"inputs": ["close", "high", "low"], "func": ddur_140_consec_days_tp_below_sma200},
    "ddur_141_vol_above_avg_while_underwater_252d": {"inputs": ["close", "volume"], "func": ddur_141_vol_above_avg_while_underwater_252d},
    "ddur_142_vol_trend_during_drawdown_duration": {"inputs": ["close", "volume"], "func": ddur_142_vol_trend_during_drawdown_duration},
    "ddur_143_avg_volume_on_new_low_days_252d": {"inputs": ["close", "volume"], "func": ddur_143_avg_volume_on_new_low_days_252d},
    "ddur_144_pctrank_consec_days_under_252d_high_in_504d": {"inputs": ["close"], "func": ddur_144_pctrank_consec_days_under_252d_high_in_504d},
    "ddur_145_pctrank_days_since_new_low_in_252d": {"inputs": ["close"], "func": ddur_145_pctrank_days_since_new_low_in_252d},
    "ddur_146_pctrank_longest_streak_under_ath_in_504d": {"inputs": ["close"], "func": ddur_146_pctrank_longest_streak_under_ath_in_504d},
    "ddur_147_dollar_vol_wtd_days_since_ath": {"inputs": ["close", "volume"], "func": ddur_147_dollar_vol_wtd_days_since_ath},
    "ddur_148_avg_dsh_252d_high_per_vol_decile": {"inputs": ["close", "volume"], "func": ddur_148_avg_dsh_252d_high_per_vol_decile},
    "ddur_149_time_in_drawdown_entropy_252d": {"inputs": ["close"], "func": ddur_149_time_in_drawdown_entropy_252d},
    "ddur_150_time_in_drawdown_hurst_proxy_252d": {"inputs": ["close"], "func": ddur_150_time_in_drawdown_hurst_proxy_252d},
}
