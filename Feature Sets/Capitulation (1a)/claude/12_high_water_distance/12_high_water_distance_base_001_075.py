"""
12_high_water_distance — Base Features 001-075
Domain: distance, time, and regain-multiple relative to prior all-time / expanding-window
        high-water mark (HWM). Anchors on the running peak price; emphasizes staleness,
        time-since-peak, recovery multiples, new-HWM recency, and history-fraction-below-HWM.
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
    """Element-wise division; replaces zero denominator with NaN."""
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _expanding_hwm(s: pd.Series) -> pd.Series:
    """Expanding (all-time) high-water mark."""
    return s.expanding(min_periods=1).max()


def _days_since_expanding_max(s: pd.Series) -> pd.Series:
    """Number of bars elapsed since the expanding-window maximum was last set."""
    hwm = _expanding_hwm(s)
    at_peak = (s >= hwm).astype(float)
    # For each row: how many bars back was the last at_peak == 1?
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _days_since_rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Number of bars elapsed since the rolling-w maximum was last set."""
    roll_max = _rolling_max(s, w)
    at_peak = (s >= roll_max).astype(float)
    result = pd.Series(np.nan, index=s.index)
    last_peak = -1
    for i, val in enumerate(at_peak):
        if val == 1.0:
            last_peak = i
        if last_peak >= 0:
            result.iloc[i] = i - last_peak
    return result


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Multiplicative / ratio distance from expanding HWM ---

def hwd_001_hwm_pct_below_ath(close: pd.Series) -> pd.Series:
    """Percent below expanding all-time HWM: (close - ATH) / ATH."""
    hwm = _expanding_hwm(close)
    return _safe_div(close - hwm, hwm)


def hwd_002_hwm_log_dist_ath(close: pd.Series) -> pd.Series:
    """Log distance below expanding ATH HWM: log(ATH) - log(close)."""
    hwm = _expanding_hwm(close)
    return _log_safe(hwm) - _log_safe(close)


def hwd_003_hwm_regain_multiple_ath(close: pd.Series) -> pd.Series:
    """Multiple of current price needed to regain ATH: ATH / close."""
    hwm = _expanding_hwm(close)
    return _safe_div(hwm, close)


def hwd_004_hwm_log_regain_multiple_ath(close: pd.Series) -> pd.Series:
    """Log regain multiple for ATH: log(ATH / close)."""
    hwm = _expanding_hwm(close)
    return _log_safe(_safe_div(hwm, close))


def hwd_005_hwm_pct_below_1y(close: pd.Series) -> pd.Series:
    """Percent below 1-year rolling HWM: (close - max_252d) / max_252d."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(close - hwm, hwm)


def hwd_006_hwm_pct_below_2y(close: pd.Series) -> pd.Series:
    """Percent below 2-year rolling HWM: (close - max_504d) / max_504d."""
    hwm = _rolling_max(close, 504)
    return _safe_div(close - hwm, hwm)


def hwd_007_hwm_pct_below_3y(close: pd.Series) -> pd.Series:
    """Percent below 3-year rolling HWM: (close - max_756d) / max_756d."""
    hwm = _rolling_max(close, 756)
    return _safe_div(close - hwm, hwm)


def hwd_008_hwm_pct_below_5y(close: pd.Series) -> pd.Series:
    """Percent below 5-year rolling HWM: (close - max_1260d) / max_1260d."""
    hwm = _rolling_max(close, 1260)
    return _safe_div(close - hwm, hwm)


def hwd_009_hwm_log_dist_1y(close: pd.Series) -> pd.Series:
    """Log distance below 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _log_safe(hwm) - _log_safe(close)


def hwd_010_hwm_log_dist_2y(close: pd.Series) -> pd.Series:
    """Log distance below 2-year rolling HWM."""
    hwm = _rolling_max(close, 504)
    return _log_safe(hwm) - _log_safe(close)


def hwd_011_hwm_log_dist_3y(close: pd.Series) -> pd.Series:
    """Log distance below 3-year rolling HWM."""
    hwm = _rolling_max(close, 756)
    return _log_safe(hwm) - _log_safe(close)


def hwd_012_hwm_log_dist_5y(close: pd.Series) -> pd.Series:
    """Log distance below 5-year rolling HWM."""
    hwm = _rolling_max(close, 1260)
    return _log_safe(hwm) - _log_safe(close)


# --- Group B (013-022): Time since ATH / rolling HWM was set ---

def hwd_013_days_since_ath(close: pd.Series) -> pd.Series:
    """Days elapsed since the expanding ATH was last set."""
    return _days_since_expanding_max(close)


def hwd_014_days_since_1y_hwm(close: pd.Series) -> pd.Series:
    """Days elapsed since the 1-year rolling HWM was last set."""
    return _days_since_rolling_max(close, _TD_YEAR)


def hwd_015_days_since_2y_hwm(close: pd.Series) -> pd.Series:
    """Days elapsed since the 2-year rolling HWM was last set."""
    return _days_since_rolling_max(close, 504)


def hwd_016_days_since_3y_hwm(close: pd.Series) -> pd.Series:
    """Days elapsed since the 3-year rolling HWM was last set."""
    return _days_since_rolling_max(close, 756)


def hwd_017_months_since_ath(close: pd.Series) -> pd.Series:
    """Months (trading) elapsed since ATH: days_since_ath / 21."""
    return _safe_div(hwd_013_days_since_ath(close), pd.Series(_TD_MON, index=close.index))


def hwd_018_years_since_ath(close: pd.Series) -> pd.Series:
    """Years (trading) elapsed since ATH: days_since_ath / 252."""
    return _safe_div(hwd_013_days_since_ath(close), pd.Series(_TD_YEAR, index=close.index))


def hwd_019_time_since_ath_frac_history(close: pd.Series) -> pd.Series:
    """Fraction of total trading history spent since ATH was set."""
    days = hwd_013_days_since_ath(close)
    total = pd.Series(np.arange(1, len(close) + 1), index=close.index, dtype=float)
    return _safe_div(days, total)


def hwd_020_days_since_ath_log(close: pd.Series) -> pd.Series:
    """Log of (days since ATH + 1) — compresses extreme staleness."""
    d = hwd_013_days_since_ath(close).fillna(0)
    return np.log1p(d)


def hwd_021_days_since_1y_hwm_log(close: pd.Series) -> pd.Series:
    """Log of (days since 1y HWM + 1)."""
    d = hwd_014_days_since_1y_hwm(close).fillna(0)
    return np.log1p(d)


def hwd_022_days_since_ath_sqrt(close: pd.Series) -> pd.Series:
    """Square root of days since ATH (moderate scale compression)."""
    d = hwd_013_days_since_ath(close).fillna(0)
    return np.sqrt(d)


# --- Group C (023-034): Fraction of history spent below HWM ---

def hwd_023_frac_history_below_ath(close: pd.Series) -> pd.Series:
    """Fraction of all trading days where close was below expanding ATH."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    return below.expanding(min_periods=1).mean()


def hwd_024_frac_252d_below_ath(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below expanding ATH."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def hwd_025_frac_504d_below_ath(close: pd.Series) -> pd.Series:
    """Fraction of last 504 days where close was below expanding ATH."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, 504)


def hwd_026_frac_1260d_below_ath(close: pd.Series) -> pd.Series:
    """Fraction of last 1260 days where close was below expanding ATH."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, 1260)


def hwd_027_frac_252d_below_1y_hwm(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where close was below 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def hwd_028_frac_history_below_1y_hwm(close: pd.Series) -> pd.Series:
    """Fraction of all history where close was below 1-year rolling HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    below = (close < hwm).astype(float)
    return below.expanding(min_periods=1).mean()


def hwd_029_consecutive_below_ath(close: pd.Series) -> pd.Series:
    """Current consecutive-day streak below expanding ATH (resets when new ATH made)."""
    hwm = _expanding_hwm(close)
    below = (close < hwm).astype(float)
    result = pd.Series(0.0, index=close.index)
    streak = 0
    for i, b in enumerate(below):
        if b == 1.0:
            streak += 1
        else:
            streak = 0
        result.iloc[i] = streak
    return result


def hwd_030_consec_below_ath_log(close: pd.Series) -> pd.Series:
    """Log of (consecutive days below ATH + 1)."""
    return np.log1p(hwd_029_consecutive_below_ath(close))


def hwd_031_frac_history_at_new_hwm(close: pd.Series) -> pd.Series:
    """Fraction of history where close was setting a new expanding ATH."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return at_peak.expanding(min_periods=1).mean()


def hwd_032_frac_252d_at_new_hwm(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days where a new ATH was set."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return _rolling_mean(at_peak, _TD_YEAR)


def hwd_033_frac_1260d_at_new_hwm(close: pd.Series) -> pd.Series:
    """Fraction of last 1260 days where a new ATH was set."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return _rolling_mean(at_peak, 1260)


def hwd_034_time_ratio_peak_to_history(close: pd.Series) -> pd.Series:
    """Ratio of days-since-ATH to length of price history (staleness ratio)."""
    d = hwd_013_days_since_ath(close)
    total = pd.Series(np.arange(1, len(close) + 1), index=close.index, dtype=float)
    return _safe_div(d, total)


# --- Group D (035-046): HWM level vs current price (absolute and relative) ---

def hwd_035_hwm_ath_level_to_close_ratio(close: pd.Series) -> pd.Series:
    """ATH price level divided by current close (raw regain multiple)."""
    hwm = _expanding_hwm(close)
    return _safe_div(hwm, close)


def hwd_036_hwm_1y_level_to_close_ratio(close: pd.Series) -> pd.Series:
    """1-year HWM price level divided by current close."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(hwm, close)


def hwd_037_hwm_2y_level_to_close_ratio(close: pd.Series) -> pd.Series:
    """2-year HWM price level divided by current close."""
    hwm = _rolling_max(close, 504)
    return _safe_div(hwm, close)


def hwd_038_hwm_3y_level_to_close_ratio(close: pd.Series) -> pd.Series:
    """3-year HWM price level divided by current close."""
    hwm = _rolling_max(close, 756)
    return _safe_div(hwm, close)


def hwd_039_hwm_5y_level_to_close_ratio(close: pd.Series) -> pd.Series:
    """5-year HWM price level divided by current close."""
    hwm = _rolling_max(close, 1260)
    return _safe_div(hwm, close)


def hwd_040_hwm_ath_vs_sma200_ratio(close: pd.Series) -> pd.Series:
    """Ratio of ATH to 200-day SMA (how elevated was peak vs trend)."""
    hwm = _expanding_hwm(close)
    sma = _rolling_mean(close, 200)
    return _safe_div(hwm, sma)


def hwd_041_hwm_close_pct_of_ath(close: pd.Series) -> pd.Series:
    """Close as a percentage of ATH (complement of pct_below): close / ATH."""
    hwm = _expanding_hwm(close)
    return _safe_div(close, hwm)


def hwd_042_hwm_close_pct_of_1y(close: pd.Series) -> pd.Series:
    """Close as percentage of 1-year HWM."""
    hwm = _rolling_max(close, _TD_YEAR)
    return _safe_div(close, hwm)


def hwd_043_hwm_close_pct_of_2y(close: pd.Series) -> pd.Series:
    """Close as percentage of 2-year HWM."""
    hwm = _rolling_max(close, 504)
    return _safe_div(close, hwm)


def hwd_044_hwm_close_pct_of_5y(close: pd.Series) -> pd.Series:
    """Close as percentage of 5-year HWM."""
    hwm = _rolling_max(close, 1260)
    return _safe_div(close, hwm)


def hwd_045_hwm_ath_dollar_gap(close: pd.Series) -> pd.Series:
    """Absolute dollar gap from ATH: ATH - close."""
    hwm = _expanding_hwm(close)
    return hwm - close


def hwd_046_hwm_ath_dollar_gap_vol_norm(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATH dollar gap normalized by 252-day average daily volume times close."""
    gap = hwd_045_hwm_ath_dollar_gap(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    denom = avg_vol * close
    return _safe_div(gap, denom.replace(0, np.nan))


# --- Group E (047-057): New-HWM recency and count ---

def hwd_047_days_since_last_new_hwm_ath(close: pd.Series) -> pd.Series:
    """Days since the most recent new expanding ATH was set (alias of hwd_013)."""
    return _days_since_expanding_max(close)


def hwd_048_new_hwm_count_252d(close: pd.Series) -> pd.Series:
    """Number of new ATH days in trailing 252-day window."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return _rolling_sum(at_peak, _TD_YEAR)


def hwd_049_new_hwm_count_504d(close: pd.Series) -> pd.Series:
    """Number of new ATH days in trailing 504-day window."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return _rolling_sum(at_peak, 504)


def hwd_050_new_hwm_count_1260d(close: pd.Series) -> pd.Series:
    """Number of new ATH days in trailing 1260-day window."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return _rolling_sum(at_peak, 1260)


def hwd_051_new_hwm_count_all(close: pd.Series) -> pd.Series:
    """Cumulative count of all new ATH days in price history."""
    hwm = _expanding_hwm(close)
    at_peak = (close >= hwm).astype(float)
    return at_peak.expanding(min_periods=1).sum()


def hwd_052_new_hwm_rate_252d(close: pd.Series) -> pd.Series:
    """Rate of new ATH days per trading month over last 252 days."""
    return _safe_div(hwd_048_new_hwm_count_252d(close),
                     pd.Series(_TD_YEAR / _TD_MON, index=close.index))


def hwd_053_new_hwm_rate_1260d(close: pd.Series) -> pd.Series:
    """Rate of new ATH days per trading month over last 1260 days."""
    return _safe_div(hwd_050_new_hwm_count_1260d(close),
                     pd.Series(1260 / _TD_MON, index=close.index))


def hwd_054_new_1y_hwm_count_252d(close: pd.Series) -> pd.Series:
    """Number of new 1-year rolling HWM days in trailing 252-day window."""
    hwm = _rolling_max(close, _TD_YEAR)
    at_peak = (close >= hwm).astype(float)
    return _rolling_sum(at_peak, _TD_YEAR)


def hwd_055_days_since_last_new_1y_hwm(close: pd.Series) -> pd.Series:
    """Days since the most recent new 1-year rolling HWM was set."""
    return _days_since_rolling_max(close, _TD_YEAR)


def hwd_056_days_since_last_new_2y_hwm(close: pd.Series) -> pd.Series:
    """Days since the most recent new 2-year rolling HWM was set."""
    return _days_since_rolling_max(close, 504)


def hwd_057_hwm_new_ath_recency_zscore(close: pd.Series) -> pd.Series:
    """Z-score of days-since-ATH over trailing 252-day window."""
    d = hwd_013_days_since_ath(close)
    return _zscore_rolling(d, _TD_YEAR)


# --- Group F (058-067): Volatility-adjusted and normalized HWM distances ---

def hwd_058_hwm_pct_below_ath_vol_adj(close: pd.Series) -> pd.Series:
    """ATH pct-below divided by 252-day realized volatility."""
    pct = hwd_001_hwm_pct_below_ath(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(pct, vol)


def hwd_059_hwm_log_dist_ath_vol_adj(close: pd.Series) -> pd.Series:
    """Log distance from ATH divided by 252-day realized volatility."""
    ld = hwd_002_hwm_log_dist_ath(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(ld, vol)


def hwd_060_hwm_pct_below_1y_vol_adj(close: pd.Series) -> pd.Series:
    """1-year HWM pct-below divided by 252-day realized volatility."""
    pct = hwd_005_hwm_pct_below_1y(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(pct, vol)


def hwd_061_hwm_pct_below_ath_atr_adj(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """ATH pct-below normalized by 252-day ATR / close (ATR as fraction of price)."""
    pct = hwd_001_hwm_pct_below_ath(close)
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    atr_pct = _safe_div(_rolling_mean(tr, _TD_YEAR), close)
    return _safe_div(pct, atr_pct)


def hwd_062_hwm_log_dist_ath_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of log-distance from ATH over trailing 252-day window."""
    ld = hwd_002_hwm_log_dist_ath(close)
    return _zscore_rolling(ld, _TD_YEAR)


def hwd_063_hwm_log_dist_ath_zscore_1260d(close: pd.Series) -> pd.Series:
    """Z-score of log-distance from ATH over trailing 1260-day window."""
    ld = hwd_002_hwm_log_dist_ath(close)
    return _zscore_rolling(ld, 1260)


def hwd_064_hwm_log_dist_ath_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of log-dist-from-ATH within trailing 252-day window."""
    ld = hwd_002_hwm_log_dist_ath(close)
    return _rolling_rank_pct(ld, _TD_YEAR)


def hwd_065_hwm_log_dist_ath_pct_rank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of log-dist-from-ATH within trailing 1260-day window."""
    ld = hwd_002_hwm_log_dist_ath(close)
    return _rolling_rank_pct(ld, 1260)


def hwd_066_hwm_log_dist_ath_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of log-dist-from-ATH over full history."""
    ld = hwd_002_hwm_log_dist_ath(close)
    return ld.expanding(min_periods=5).rank(pct=True)


def hwd_067_hwm_regain_multiple_vol_adj(close: pd.Series) -> pd.Series:
    """Log regain multiple for ATH divided by 252-day realized vol."""
    lrm = hwd_004_hwm_log_regain_multiple_ath(close)
    vol = _rolling_std(_daily_ret(close), _TD_YEAR)
    return _safe_div(lrm, vol)


# --- Group G (068-075): Multi-window ratios, staleness, and composites ---

def hwd_068_hwm_ratio_1y_to_ath_dist(close: pd.Series) -> pd.Series:
    """Ratio of 1-year HWM distance to ATH distance (recent vs all-time severity)."""
    d1y = hwd_005_hwm_pct_below_1y(close)
    dath = hwd_001_hwm_pct_below_ath(close)
    return _safe_div(d1y, dath)


def hwd_069_hwm_ratio_2y_to_ath_dist(close: pd.Series) -> pd.Series:
    """Ratio of 2-year HWM distance to ATH distance."""
    d2y = hwd_006_hwm_pct_below_2y(close)
    dath = hwd_001_hwm_pct_below_ath(close)
    return _safe_div(d2y, dath)


def hwd_070_hwm_ratio_3y_to_5y_dist(close: pd.Series) -> pd.Series:
    """Ratio of 3-year HWM distance to 5-year HWM distance."""
    d3y = hwd_007_hwm_pct_below_3y(close)
    d5y = hwd_008_hwm_pct_below_5y(close)
    return _safe_div(d3y, d5y)


def hwd_071_hwm_staleness_score(close: pd.Series) -> pd.Series:
    """Staleness: log-dist-from-ATH times log(days_since_ATH + 1)."""
    ld   = hwd_002_hwm_log_dist_ath(close)
    dlog = hwd_020_days_since_ath_log(close)
    return ld * dlog


def hwd_072_hwm_time_weighted_distance(close: pd.Series) -> pd.Series:
    """Time-weighted ATH distance: pct_below * years_since_ATH."""
    pct  = hwd_001_hwm_pct_below_ath(close).abs()
    yrs  = hwd_018_years_since_ath(close)
    return pct * yrs


def hwd_073_hwm_composite_multiscale(close: pd.Series) -> pd.Series:
    """Composite multi-scale HWM distance: 0.4*ATH + 0.3*1y + 0.2*2y + 0.1*5y."""
    dath = hwd_002_hwm_log_dist_ath(close)
    d1y  = hwd_009_hwm_log_dist_1y(close)
    d2y  = hwd_010_hwm_log_dist_2y(close)
    d5y  = hwd_012_hwm_log_dist_5y(close)
    return 0.4 * dath + 0.3 * d1y + 0.2 * d2y + 0.1 * d5y


def hwd_074_hwm_volume_weighted_dist_ath(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted log-distance from ATH (distress weighted by trade activity)."""
    ld    = hwd_002_hwm_log_dist_ath(close)
    v_norm = _safe_div(volume, _rolling_mean(volume, _TD_YEAR))
    return _rolling_mean(ld * v_norm, _TD_YEAR)


def hwd_075_hwm_close_vs_intraday_ath(high: pd.Series, close: pd.Series) -> pd.Series:
    """Log distance from intraday all-time high to current close."""
    hwm = high.expanding(min_periods=1).max()
    return _log_safe(hwm) - _log_safe(close)


# ── Registry ──────────────────────────────────────────────────────────────────

HIGH_WATER_DISTANCE_REGISTRY_001_075 = {
    "hwd_001_hwm_pct_below_ath":            {"inputs": ["close"],                    "func": hwd_001_hwm_pct_below_ath},
    "hwd_002_hwm_log_dist_ath":             {"inputs": ["close"],                    "func": hwd_002_hwm_log_dist_ath},
    "hwd_003_hwm_regain_multiple_ath":      {"inputs": ["close"],                    "func": hwd_003_hwm_regain_multiple_ath},
    "hwd_004_hwm_log_regain_multiple_ath":  {"inputs": ["close"],                    "func": hwd_004_hwm_log_regain_multiple_ath},
    "hwd_005_hwm_pct_below_1y":             {"inputs": ["close"],                    "func": hwd_005_hwm_pct_below_1y},
    "hwd_006_hwm_pct_below_2y":             {"inputs": ["close"],                    "func": hwd_006_hwm_pct_below_2y},
    "hwd_007_hwm_pct_below_3y":             {"inputs": ["close"],                    "func": hwd_007_hwm_pct_below_3y},
    "hwd_008_hwm_pct_below_5y":             {"inputs": ["close"],                    "func": hwd_008_hwm_pct_below_5y},
    "hwd_009_hwm_log_dist_1y":              {"inputs": ["close"],                    "func": hwd_009_hwm_log_dist_1y},
    "hwd_010_hwm_log_dist_2y":              {"inputs": ["close"],                    "func": hwd_010_hwm_log_dist_2y},
    "hwd_011_hwm_log_dist_3y":              {"inputs": ["close"],                    "func": hwd_011_hwm_log_dist_3y},
    "hwd_012_hwm_log_dist_5y":              {"inputs": ["close"],                    "func": hwd_012_hwm_log_dist_5y},
    "hwd_013_days_since_ath":               {"inputs": ["close"],                    "func": hwd_013_days_since_ath},
    "hwd_014_days_since_1y_hwm":            {"inputs": ["close"],                    "func": hwd_014_days_since_1y_hwm},
    "hwd_015_days_since_2y_hwm":            {"inputs": ["close"],                    "func": hwd_015_days_since_2y_hwm},
    "hwd_016_days_since_3y_hwm":            {"inputs": ["close"],                    "func": hwd_016_days_since_3y_hwm},
    "hwd_017_months_since_ath":             {"inputs": ["close"],                    "func": hwd_017_months_since_ath},
    "hwd_018_years_since_ath":              {"inputs": ["close"],                    "func": hwd_018_years_since_ath},
    "hwd_019_time_since_ath_frac_history":  {"inputs": ["close"],                    "func": hwd_019_time_since_ath_frac_history},
    "hwd_020_days_since_ath_log":           {"inputs": ["close"],                    "func": hwd_020_days_since_ath_log},
    "hwd_021_days_since_1y_hwm_log":        {"inputs": ["close"],                    "func": hwd_021_days_since_1y_hwm_log},
    "hwd_022_days_since_ath_sqrt":          {"inputs": ["close"],                    "func": hwd_022_days_since_ath_sqrt},
    "hwd_023_frac_history_below_ath":       {"inputs": ["close"],                    "func": hwd_023_frac_history_below_ath},
    "hwd_024_frac_252d_below_ath":          {"inputs": ["close"],                    "func": hwd_024_frac_252d_below_ath},
    "hwd_025_frac_504d_below_ath":          {"inputs": ["close"],                    "func": hwd_025_frac_504d_below_ath},
    "hwd_026_frac_1260d_below_ath":         {"inputs": ["close"],                    "func": hwd_026_frac_1260d_below_ath},
    "hwd_027_frac_252d_below_1y_hwm":       {"inputs": ["close"],                    "func": hwd_027_frac_252d_below_1y_hwm},
    "hwd_028_frac_history_below_1y_hwm":    {"inputs": ["close"],                    "func": hwd_028_frac_history_below_1y_hwm},
    "hwd_029_consecutive_below_ath":        {"inputs": ["close"],                    "func": hwd_029_consecutive_below_ath},
    "hwd_030_consec_below_ath_log":         {"inputs": ["close"],                    "func": hwd_030_consec_below_ath_log},
    "hwd_031_frac_history_at_new_hwm":      {"inputs": ["close"],                    "func": hwd_031_frac_history_at_new_hwm},
    "hwd_032_frac_252d_at_new_hwm":         {"inputs": ["close"],                    "func": hwd_032_frac_252d_at_new_hwm},
    "hwd_033_frac_1260d_at_new_hwm":        {"inputs": ["close"],                    "func": hwd_033_frac_1260d_at_new_hwm},
    "hwd_034_time_ratio_peak_to_history":   {"inputs": ["close"],                    "func": hwd_034_time_ratio_peak_to_history},
    "hwd_035_hwm_ath_level_to_close_ratio": {"inputs": ["close"],                    "func": hwd_035_hwm_ath_level_to_close_ratio},
    "hwd_036_hwm_1y_level_to_close_ratio":  {"inputs": ["close"],                    "func": hwd_036_hwm_1y_level_to_close_ratio},
    "hwd_037_hwm_2y_level_to_close_ratio":  {"inputs": ["close"],                    "func": hwd_037_hwm_2y_level_to_close_ratio},
    "hwd_038_hwm_3y_level_to_close_ratio":  {"inputs": ["close"],                    "func": hwd_038_hwm_3y_level_to_close_ratio},
    "hwd_039_hwm_5y_level_to_close_ratio":  {"inputs": ["close"],                    "func": hwd_039_hwm_5y_level_to_close_ratio},
    "hwd_040_hwm_ath_vs_sma200_ratio":      {"inputs": ["close"],                    "func": hwd_040_hwm_ath_vs_sma200_ratio},
    "hwd_041_hwm_close_pct_of_ath":         {"inputs": ["close"],                    "func": hwd_041_hwm_close_pct_of_ath},
    "hwd_042_hwm_close_pct_of_1y":          {"inputs": ["close"],                    "func": hwd_042_hwm_close_pct_of_1y},
    "hwd_043_hwm_close_pct_of_2y":          {"inputs": ["close"],                    "func": hwd_043_hwm_close_pct_of_2y},
    "hwd_044_hwm_close_pct_of_5y":          {"inputs": ["close"],                    "func": hwd_044_hwm_close_pct_of_5y},
    "hwd_045_hwm_ath_dollar_gap":           {"inputs": ["close"],                    "func": hwd_045_hwm_ath_dollar_gap},
    "hwd_046_hwm_ath_dollar_gap_vol_norm":  {"inputs": ["close", "volume"],          "func": hwd_046_hwm_ath_dollar_gap_vol_norm},
    "hwd_047_days_since_last_new_hwm_ath":  {"inputs": ["close"],                    "func": hwd_047_days_since_last_new_hwm_ath},
    "hwd_048_new_hwm_count_252d":           {"inputs": ["close"],                    "func": hwd_048_new_hwm_count_252d},
    "hwd_049_new_hwm_count_504d":           {"inputs": ["close"],                    "func": hwd_049_new_hwm_count_504d},
    "hwd_050_new_hwm_count_1260d":          {"inputs": ["close"],                    "func": hwd_050_new_hwm_count_1260d},
    "hwd_051_new_hwm_count_all":            {"inputs": ["close"],                    "func": hwd_051_new_hwm_count_all},
    "hwd_052_new_hwm_rate_252d":            {"inputs": ["close"],                    "func": hwd_052_new_hwm_rate_252d},
    "hwd_053_new_hwm_rate_1260d":           {"inputs": ["close"],                    "func": hwd_053_new_hwm_rate_1260d},
    "hwd_054_new_1y_hwm_count_252d":        {"inputs": ["close"],                    "func": hwd_054_new_1y_hwm_count_252d},
    "hwd_055_days_since_last_new_1y_hwm":   {"inputs": ["close"],                    "func": hwd_055_days_since_last_new_1y_hwm},
    "hwd_056_days_since_last_new_2y_hwm":   {"inputs": ["close"],                    "func": hwd_056_days_since_last_new_2y_hwm},
    "hwd_057_hwm_new_ath_recency_zscore":   {"inputs": ["close"],                    "func": hwd_057_hwm_new_ath_recency_zscore},
    "hwd_058_hwm_pct_below_ath_vol_adj":    {"inputs": ["close"],                    "func": hwd_058_hwm_pct_below_ath_vol_adj},
    "hwd_059_hwm_log_dist_ath_vol_adj":     {"inputs": ["close"],                    "func": hwd_059_hwm_log_dist_ath_vol_adj},
    "hwd_060_hwm_pct_below_1y_vol_adj":     {"inputs": ["close"],                    "func": hwd_060_hwm_pct_below_1y_vol_adj},
    "hwd_061_hwm_pct_below_ath_atr_adj":    {"inputs": ["close", "high", "low"],     "func": hwd_061_hwm_pct_below_ath_atr_adj},
    "hwd_062_hwm_log_dist_ath_zscore_252d": {"inputs": ["close"],                    "func": hwd_062_hwm_log_dist_ath_zscore_252d},
    "hwd_063_hwm_log_dist_ath_zscore_1260d":{"inputs": ["close"],                    "func": hwd_063_hwm_log_dist_ath_zscore_1260d},
    "hwd_064_hwm_log_dist_ath_pct_rank_252d":{"inputs": ["close"],                   "func": hwd_064_hwm_log_dist_ath_pct_rank_252d},
    "hwd_065_hwm_log_dist_ath_pct_rank_1260d":{"inputs": ["close"],                  "func": hwd_065_hwm_log_dist_ath_pct_rank_1260d},
    "hwd_066_hwm_log_dist_ath_expanding_pct_rank":{"inputs": ["close"],              "func": hwd_066_hwm_log_dist_ath_expanding_pct_rank},
    "hwd_067_hwm_regain_multiple_vol_adj":  {"inputs": ["close"],                    "func": hwd_067_hwm_regain_multiple_vol_adj},
    "hwd_068_hwm_ratio_1y_to_ath_dist":     {"inputs": ["close"],                    "func": hwd_068_hwm_ratio_1y_to_ath_dist},
    "hwd_069_hwm_ratio_2y_to_ath_dist":     {"inputs": ["close"],                    "func": hwd_069_hwm_ratio_2y_to_ath_dist},
    "hwd_070_hwm_ratio_3y_to_5y_dist":      {"inputs": ["close"],                    "func": hwd_070_hwm_ratio_3y_to_5y_dist},
    "hwd_071_hwm_staleness_score":          {"inputs": ["close"],                    "func": hwd_071_hwm_staleness_score},
    "hwd_072_hwm_time_weighted_distance":   {"inputs": ["close"],                    "func": hwd_072_hwm_time_weighted_distance},
    "hwd_073_hwm_composite_multiscale":     {"inputs": ["close"],                    "func": hwd_073_hwm_composite_multiscale},
    "hwd_074_hwm_volume_weighted_dist_ath": {"inputs": ["close", "volume"],          "func": hwd_074_hwm_volume_weighted_dist_ath},
    "hwd_075_hwm_close_vs_intraday_ath":    {"inputs": ["high", "close"],            "func": hwd_075_hwm_close_vs_intraday_ath},
}
