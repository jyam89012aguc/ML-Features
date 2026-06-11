"""
23_dollar_volume_shock — Base Features 076-150
Domain: dollar-volume spikes and turnover extremes — dollar volume shock
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
Dollar volume = close * volume (price-weighted traded value).
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _dv(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume: close * volume."""
    return close * volume


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Dollar-volume shock with high/low price inputs ---

def dvs_076_dv_high_close_ratio(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume scaled by close/high ratio (shock near daily top = supply)."""
    dv = _dv(close, volume)
    ratio = _safe_div(close, high)
    return dv * ratio


def dvs_077_dv_low_close_ratio(close: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume scaled by close/low ratio (close near low = bearish dv)."""
    dv = _dv(close, volume)
    ratio = _safe_div(low, close.clip(lower=_EPS))
    return dv * (2.0 - ratio)


def dvs_078_dv_intraday_range_norm(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume divided by intraday high-low range (DV per unit range)."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    return _safe_div(dv, rng)


def dvs_079_dv_range_norm_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of range-normalized dollar volume over 63 days."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    dv_rng = _safe_div(dv, rng)
    m = _rolling_mean(dv_rng, _TD_QTR)
    s = _rolling_std(dv_rng, _TD_QTR)
    return _safe_div(dv_rng - m, s)


def dvs_080_dv_open_gap_interaction(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume times magnitude of open gap (gap-driven dollar shock)."""
    dv = _dv(close, volume)
    gap = (open - close.shift(1)).abs() / close.shift(1).clip(lower=_EPS)
    return dv * gap


def dvs_081_dv_open_gap_interaction_zscore_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of gap-times-dv interaction over 63 days."""
    dv = _dv(close, volume)
    gap = (open - close.shift(1)).abs() / close.shift(1).clip(lower=_EPS)
    combo = dv * gap
    m = _rolling_mean(combo, _TD_QTR)
    s = _rolling_std(combo, _TD_QTR)
    return _safe_div(combo - m, s)


def dvs_082_dv_close_near_low_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """DV z-score filtered to days when close is in bottom 25% of daily range."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    return z.where(pos <= 0.25, 0.0)


def dvs_083_dv_close_near_high_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """DV z-score filtered to days when close is in top 25% of daily range."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    return z.where(pos >= 0.75, 0.0)


def dvs_084_dv_high_volume_range_product_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21d mean of (dollar_volume * intraday_range_pct) — combined panic signal."""
    dv = _dv(close, volume)
    rng_pct = (high - low) / close.shift(1).clip(lower=_EPS)
    return _rolling_mean(dv * rng_pct, _TD_MON)


def dvs_085_dv_high_volume_range_product_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d mean (dv * range_pct) over trailing 252 days."""
    dv = _dv(close, volume)
    rng_pct = (high - low) / close.shift(1).clip(lower=_EPS)
    combo21 = _rolling_mean(dv * rng_pct, _TD_MON)
    m = _rolling_mean(combo21, _TD_YEAR)
    s = _rolling_std(combo21, _TD_YEAR)
    return _safe_div(combo21 - m, s)


# --- Group I (086-095): Dollar-volume EWM signals and trend ---

def dvs_086_dv_ewm21_vs_ewm63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day EWM to 63-day EWM of dollar volume (DV momentum)."""
    dv = _dv(close, volume)
    return _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, _TD_QTR))


def dvs_087_dv_ewm21_vs_ewm126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day EWM to 126-day EWM of dollar volume."""
    dv = _dv(close, volume)
    return _safe_div(_ewm_mean(dv, _TD_MON), _ewm_mean(dv, _TD_HALF))


def dvs_088_dv_ewm5_vs_ewm21(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EWM to 21-day EWM of dollar volume (very short-term burst)."""
    dv = _dv(close, volume)
    return _safe_div(_ewm_mean(dv, _TD_WEEK), _ewm_mean(dv, _TD_MON))


def dvs_089_dv_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar volume over trailing 21 days (DV trend)."""
    dv = _dv(close, volume)
    return _linslope(dv, _TD_MON)


def dvs_090_dv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar volume over trailing 63 days."""
    dv = _dv(close, volume)
    return _linslope(dv, _TD_QTR)


def dvs_091_dv_slope_norm_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar volume / 21d mean DV (normalized slope)."""
    dv = _dv(close, volume)
    norm = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    return _linslope(norm, _TD_MON)


def dvs_092_dv_log_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of log-dollar-volume over trailing 21 days."""
    dv = _log_safe(_dv(close, volume))
    return _linslope(dv, _TD_MON)


def dvs_093_dv_log_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of log-dollar-volume over trailing 63 days."""
    dv = _log_safe(_dv(close, volume))
    return _linslope(dv, _TD_QTR)


def dvs_094_dv_above_ewm21_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days where dollar volume > its 21-day EWM."""
    dv = _dv(close, volume)
    ewm = _ewm_mean(dv, _TD_MON)
    cond = dv > ewm
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dvs_095_dv_below_ewm21_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days where dollar volume < its 21-day EWM (drying up)."""
    dv = _dv(close, volume)
    ewm = _ewm_mean(dv, _TD_MON)
    cond = dv < ewm
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


# --- Group J (096-105): Dollar-volume shock with open price ---

def dvs_096_dv_gap_down_sum_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on gap-down open days over trailing 21 days."""
    dv = _dv(close, volume)
    gap_down = open < close.shift(1)
    dv_gd = dv.where(gap_down, 0.0)
    return _rolling_sum(dv_gd, _TD_MON)


def dvs_097_dv_gap_down_sum_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on gap-down open days over trailing 63 days."""
    dv = _dv(close, volume)
    gap_down = open < close.shift(1)
    dv_gd = dv.where(gap_down, 0.0)
    return _rolling_sum(dv_gd, _TD_QTR)


def dvs_098_dv_gap_down_fraction_dv_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21-day total dollar volume traded on gap-down days."""
    dv = _dv(close, volume)
    gap_down = open < close.shift(1)
    dv_gd = dv.where(gap_down, 0.0)
    total = _rolling_sum(dv, _TD_MON)
    return _safe_div(_rolling_sum(dv_gd, _TD_MON), total)


def dvs_099_dv_gap_down_fraction_dv_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63-day total dollar volume traded on gap-down days."""
    dv = _dv(close, volume)
    gap_down = open < close.shift(1)
    dv_gd = dv.where(gap_down, 0.0)
    total = _rolling_sum(dv, _TD_QTR)
    return _safe_div(_rolling_sum(dv_gd, _TD_QTR), total)


def dvs_100_dv_gap_down_spike_count_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 2x-dv spike days that also had a gap-down open, trailing 63 days."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    gap_down = open < close.shift(1)
    cond = ((dv > 2.0 * baseline) & gap_down).astype(float)
    return _rolling_sum(cond, _TD_QTR)


def dvs_101_dv_open_to_close_signed_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of DV * sign(close-open) over 21 days (net directional dollar flow)."""
    dv = _dv(close, volume)
    sign = np.sign(close - open)
    return _rolling_sum(dv * sign, _TD_MON)


def dvs_102_dv_open_to_close_signed_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of DV * sign(close-open) over 63 days."""
    dv = _dv(close, volume)
    sign = np.sign(close - open)
    return _rolling_sum(dv * sign, _TD_QTR)


def dvs_103_dv_bear_candle_sum_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on bear-candle days (close < open) over 21 days."""
    dv = _dv(close, volume)
    bear = close < open
    dv_bear = dv.where(bear, 0.0)
    return _rolling_sum(dv_bear, _TD_MON)


def dvs_104_dv_bear_candle_fraction_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 21d total DV on bear-candle (close<open) days."""
    dv = _dv(close, volume)
    bear = close < open
    dv_bear = dv.where(bear, 0.0)
    total = _rolling_sum(dv, _TD_MON)
    return _safe_div(_rolling_sum(dv_bear, _TD_MON), total)


def dvs_105_dv_bear_candle_fraction_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d total DV on bear-candle days."""
    dv = _dv(close, volume)
    bear = close < open
    dv_bear = dv.where(bear, 0.0)
    total = _rolling_sum(dv, _TD_QTR)
    return _safe_div(_rolling_sum(dv_bear, _TD_QTR), total)


# --- Group K (106-115): Dollar-volume at price extremes ---

def dvs_106_dv_at_new_low_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on new 63-day low closes over trailing 63 days."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    return _rolling_sum(dv_nl, _TD_QTR)


def dvs_107_dv_at_new_low_sum_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on new 252-day low closes over trailing 252 days."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    return _rolling_sum(dv_nl, _TD_YEAR)


def dvs_108_dv_at_new_low_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d total DV that occurred on new-63d-low days."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    total = _rolling_sum(dv, _TD_QTR)
    return _safe_div(_rolling_sum(dv_nl, _TD_QTR), total)


def dvs_109_dv_at_new_low_fraction_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252d total DV that occurred on new-252d-low days."""
    dv = _dv(close, volume)
    roll_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_HALF).min()
    new_low = close < roll_min
    dv_nl = dv.where(new_low, 0.0)
    total = _rolling_sum(dv, _TD_YEAR)
    return _safe_div(_rolling_sum(dv_nl, _TD_YEAR), total)


def dvs_110_dv_bottom_decile_price_sum_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of DV on days when close is in bottom 10th percentile of 252d close range."""
    dv = _dv(close, volume)
    roll_min = _rolling_min(close, _TD_YEAR)
    roll_max = _rolling_max(close, _TD_YEAR)
    pct_pos = _safe_div(close - roll_min, roll_max - roll_min)
    at_bottom = pct_pos <= 0.10
    return _rolling_sum(dv.where(at_bottom, 0.0), _TD_QTR)


def dvs_111_dv_bottom_quartile_price_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d DV traded when close is in bottom 25% of 252d range."""
    dv = _dv(close, volume)
    roll_min = _rolling_min(close, _TD_YEAR)
    roll_max = _rolling_max(close, _TD_YEAR)
    pct_pos = _safe_div(close - roll_min, roll_max - roll_min)
    at_bottom = pct_pos <= 0.25
    total = _rolling_sum(dv, _TD_QTR)
    return _safe_div(_rolling_sum(dv.where(at_bottom, 0.0), _TD_QTR), total)


def dvs_112_dv_acceleration_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day percent change in 21-day average dollar volume (DV acceleration)."""
    dv = _dv(close, volume)
    avg21 = _rolling_mean(dv, _TD_MON)
    return avg21.pct_change(_TD_WEEK)


def dvs_113_dv_acceleration_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day percent change in 63-day average dollar volume."""
    dv = _dv(close, volume)
    avg63 = _rolling_mean(dv, _TD_QTR)
    return avg63.pct_change(_TD_MON)


def dvs_114_dv_std_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling standard deviation of dollar volume (dispersion)."""
    dv = _dv(close, volume)
    return _rolling_std(dv, _TD_MON)


def dvs_115_dv_std_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day rolling standard deviation of dollar volume."""
    dv = _dv(close, volume)
    return _rolling_std(dv, _TD_QTR)


# --- Group L (116-125): Relative dollar-volume ratios across windows ---

def dvs_116_dv_ratio_5d_vs_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day mean DV divided by 21-day mean DV (very recent vs monthly)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_WEEK), _rolling_mean(dv, _TD_MON))


def dvs_117_dv_ratio_21d_vs_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean DV divided by 126-day mean DV."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_MON), _rolling_mean(dv, _TD_HALF))


def dvs_118_dv_ratio_21d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day mean DV divided by 252-day mean DV."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_MON), _rolling_mean(dv, _TD_YEAR))


def dvs_119_dv_ratio_63d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63-day mean DV divided by 252-day mean DV (medium vs long baseline)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_QTR), _rolling_mean(dv, _TD_YEAR))


def dvs_120_dv_ratio_5d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day mean DV divided by 252-day mean DV (weekly shock vs annual)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_WEEK), _rolling_mean(dv, _TD_YEAR))


def dvs_121_dv_min_21d_vs_mean_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day minimum DV divided by 252-day mean (drying-up signal)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_min(dv, _TD_MON), _rolling_mean(dv, _TD_YEAR))


def dvs_122_dv_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of dollar volume over 21 days (normalized volatility)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))


def dvs_123_dv_cv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of dollar volume over 63 days."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_std(dv, _TD_QTR), _rolling_mean(dv, _TD_QTR))


def dvs_124_dv_cv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of dollar volume over 252 days."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_std(dv, _TD_YEAR), _rolling_mean(dv, _TD_YEAR))


def dvs_125_dv_log_cv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of log-dollar-volume over 63 days (log-space dispersion)."""
    dv = _log_safe(_dv(close, volume))
    return _safe_div(_rolling_std(dv, _TD_QTR), _rolling_mean(dv, _TD_QTR))


# --- Group M (126-135): Dollar-volume decay and persistence ---

def dvs_126_dv_autocorr_lag1_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day lag-1 autocorrelation of dollar volume."""
    dv = _dv(close, volume)
    def _ac1(x):
        if len(x) < 4:
            return np.nan
        s = pd.Series(x)
        c = s.autocorr(lag=1)
        return c if not np.isnan(c) else 0.0
    return dv.rolling(_TD_MON, min_periods=max(4, _TD_MON // 2)).apply(_ac1, raw=True)


def dvs_127_dv_autocorr_lag1_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63-day lag-1 autocorrelation of dollar volume."""
    dv = _dv(close, volume)
    def _ac1(x):
        if len(x) < 4:
            return np.nan
        s = pd.Series(x)
        c = s.autocorr(lag=1)
        return c if not np.isnan(c) else 0.0
    return dv.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).apply(_ac1, raw=True)


def dvs_128_dv_persistence_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days where DV exceeded prior-day DV (consecutive surge check)."""
    dv = _dv(close, volume)
    above = (dv > dv.shift(1)).astype(float)
    return _rolling_sum(above, _TD_MON) / _TD_MON


def dvs_129_dv_persistence_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days where DV exceeded prior-day DV."""
    dv = _dv(close, volume)
    above = (dv > dv.shift(1)).astype(float)
    return _rolling_sum(above, _TD_QTR) / _TD_QTR


def dvs_130_dv_decay_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of last-5d mean DV to prior-16d mean DV within 21d (has the spike faded?)."""
    dv = _dv(close, volume)
    recent = _rolling_mean(dv, _TD_WEEK)
    prior = dv.shift(_TD_WEEK).rolling(_TD_MON - _TD_WEEK, min_periods=max(1, (_TD_MON - _TD_WEEK) // 2)).mean()
    return _safe_div(recent, prior)


def dvs_131_dv_spike_flag_1d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's DV > 2x its 63-day mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    return (dv > 2.0 * baseline).astype(float)


def dvs_132_dv_spike_flag_3x_1d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's DV > 3x its 63-day mean."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    return (dv > 3.0 * baseline).astype(float)


def dvs_133_dv_spike_flag_5x_1d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Binary flag: today's DV > 5x its 63-day mean (extreme capitulation event)."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    return (dv > 5.0 * baseline).astype(float)


def dvs_134_dv_spike_since_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Days since last 2x-DV spike (recency of most recent capitulation event)."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(int)
    idx = np.arange(len(spike))
    last_spike = spike.cumsum()
    result = pd.Series(np.nan, index=spike.index)
    for i in range(len(spike)):
        cum = last_spike.iloc[i]
        if cum > 0:
            arr = np.where(spike.iloc[:i+1].values == 1)[0]
            if len(arr) > 0:
                result.iloc[i] = float(i - arr[-1])
    return result


def dvs_135_dv_spike_recency_decay_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Exponentially decayed presence of 2x-DV spikes, half-life 5 days, 63d window."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    return spike.ewm(halflife=5, min_periods=1).mean()


# --- Group N (136-145): Dollar-volume composite and distress indices ---

def dvs_136_dv_distress_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DV ratio-21d times fraction of down-price days in 21d (intensity * direction)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_MON, min_periods=1).sum() / _TD_MON
    return ratio * dn_frac


def dvs_137_dv_distress_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DV z-score-63d times fraction of down-price days in 63d."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_QTR, min_periods=1).sum() / _TD_QTR
    return z * dn_frac


def dvs_138_dv_composite_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of DV ratio-21d and DV pct-rank-21d (blended spike signal)."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    rank = dv.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    return (ratio + rank) / 2.0


def dvs_139_dv_composite_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Average of DV ratio-63d and DV pct-rank-63d."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    rank = dv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (ratio + rank) / 2.0


def dvs_140_dv_above_sma21_streak(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Current consecutive days where dollar volume > its 21-day SMA."""
    dv = _dv(close, volume)
    sma = _rolling_mean(dv, _TD_MON)
    cond = dv > sma
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def dvs_141_dv_5d_sum_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 5-day sum of DV vs 252-day distribution of 5d sums."""
    dv = _dv(close, volume)
    sum5 = _rolling_sum(dv, _TD_WEEK)
    m = _rolling_mean(sum5, _TD_YEAR)
    s = _rolling_std(sum5, _TD_YEAR)
    return _safe_div(sum5 - m, s)


def dvs_142_dv_1d_vs_5d_avg_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Today's DV divided by 5-day mean DV (single-day concentration in recent week)."""
    dv = _dv(close, volume)
    return _safe_div(dv, _rolling_mean(dv, _TD_WEEK))


def dvs_143_dv_1d_vs_21d_avg_log_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log of today's DV divided by 21-day mean DV."""
    dv = _dv(close, volume)
    return _log_safe(dv) - _log_safe(_rolling_mean(dv, _TD_MON))


def dvs_144_dv_expanding_zscore_on_down_days(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Expanding z-score of DV, zeroed out on up-price days."""
    dv = _dv(close, volume)
    m = dv.expanding(min_periods=5).mean()
    s = dv.expanding(min_periods=5).std()
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    return z.where(ret < 0, 0.0)


def dvs_145_dv_spike_count_21d_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d spike count vs 252-day distribution of 21d spike counts."""
    dv = _dv(close, volume)
    baseline = _rolling_mean(dv, _TD_QTR)
    spike = (dv > 2.0 * baseline).astype(float)
    count21 = _rolling_sum(spike, _TD_MON)
    m = _rolling_mean(count21, _TD_YEAR)
    s = _rolling_std(count21, _TD_YEAR)
    return _safe_div(count21 - m, s)


# --- Group O (146-150): DV shock with full OHLCV composite ---

def dvs_146_dv_intraday_net_flow_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21d mean of DV * (close-open)/(high-low) — signed net intraday DV flow."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    net = _safe_div(close - open, rng)
    return _rolling_mean(dv * net, _TD_MON)


def dvs_147_dv_intraday_net_flow_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """63d mean of DV * (close-open)/(high-low) — signed net intraday DV flow."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    net = _safe_div(close - open, rng)
    return _rolling_mean(dv * net, _TD_QTR)


def dvs_148_dv_tail_risk_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of 21d DV ratio and 21d DV cv — spike magnitude times instability."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_MON))
    cv = _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))
    return ratio * cv


def dvs_149_dv_high_low_dv_range_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(21d max DV - 21d min DV) / 21d mean DV — range of DV spike relative to mean."""
    dv = _dv(close, volume)
    mx = _rolling_max(dv, _TD_MON)
    mn = _rolling_min(dv, _TD_MON)
    mean = _rolling_mean(dv, _TD_MON)
    return _safe_div(mx - mn, mean)


def dvs_150_dv_capitulation_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: DV zscore-63d * down-day-fraction-21d * (1 + dv-pct-rank-252d)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_QTR)
    s = _rolling_std(dv, _TD_QTR)
    z63 = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_MON, min_periods=1).sum() / _TD_MON
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.0)
    return z63 * dn_frac * (1.0 + rank)


# --- Group P (176-200): Additional OHLCV-composite and turnover features ---

def dvs_176_dv_range_norm_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of range-normalized dollar volume over 21 days."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    dv_rng = _safe_div(dv, rng)
    m = _rolling_mean(dv_rng, _TD_MON)
    s = _rolling_std(dv_rng, _TD_MON)
    return _safe_div(dv_rng - m, s)


def dvs_177_dv_range_norm_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of range-normalized dollar volume over 252 days."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    dv_rng = _safe_div(dv, rng)
    m = _rolling_mean(dv_rng, _TD_YEAR)
    s = _rolling_std(dv_rng, _TD_YEAR)
    return _safe_div(dv_rng - m, s)


def dvs_178_dv_close_near_low_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """DV z-score filtered to days when close is in bottom 25% of 21d daily range."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    m = _rolling_mean(dv, _TD_MON)
    s = _rolling_std(dv, _TD_MON)
    z = _safe_div(dv - m, s)
    return z.where(pos <= 0.25, 0.0)


def dvs_179_dv_close_near_low_sum_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of DV on days when close is in bottom 25% of intraday range, 63d window."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    dv_near_low = dv.where(pos <= 0.25, 0.0)
    return _rolling_sum(dv_near_low, _TD_QTR)


def dvs_180_dv_open_gap_sum_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of DV * open-gap magnitude over 21 days (cumulative gap-shock value)."""
    dv = _dv(close, volume)
    gap = (open - close.shift(1)).abs() / close.shift(1).clip(lower=_EPS)
    return _rolling_sum(dv * gap, _TD_MON)


def dvs_181_dv_gap_up_sum_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on gap-up open days over trailing 21 days."""
    dv = _dv(close, volume)
    gap_up = open > close.shift(1)
    return _rolling_sum(dv.where(gap_up, 0.0), _TD_MON)


def dvs_182_dv_gap_up_sum_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on gap-up open days over trailing 63 days."""
    dv = _dv(close, volume)
    gap_up = open > close.shift(1)
    return _rolling_sum(dv.where(gap_up, 0.0), _TD_QTR)


def dvs_183_dv_gap_down_vs_gap_up_ratio_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of gap-down DV to gap-up DV over 63 days (bearish gap dominance)."""
    dv = _dv(close, volume)
    gap_down = open < close.shift(1)
    gap_up = open > close.shift(1)
    dv_gd = _rolling_sum(dv.where(gap_down, 0.0), _TD_QTR)
    dv_gu = _rolling_sum(dv.where(gap_up, 0.0), _TD_QTR)
    return _safe_div(dv_gd, dv_gu)


def dvs_184_dv_bear_candle_sum_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of dollar volume on bear-candle days (close < open) over 63 days."""
    dv = _dv(close, volume)
    bear = close < open
    return _rolling_sum(dv.where(bear, 0.0), _TD_QTR)


def dvs_185_dv_bear_candle_fraction_252d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 252d total DV on bear-candle (close<open) days."""
    dv = _dv(close, volume)
    bear = close < open
    total = _rolling_sum(dv, _TD_YEAR)
    return _safe_div(_rolling_sum(dv.where(bear, 0.0), _TD_YEAR), total)


def dvs_186_dv_intraday_net_flow_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """252d mean of DV * (close-open)/(high-low) — long-run net intraday DV flow."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    net = _safe_div(close - open, rng)
    return _rolling_mean(dv * net, _TD_YEAR)


def dvs_187_dv_intraday_net_flow_zscore_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d-mean intraday net DV flow over 252-day distribution."""
    dv = _dv(close, volume)
    rng = (high - low).replace(0, np.nan)
    net = _safe_div(close - open, rng)
    flow21 = _rolling_mean(dv * net, _TD_MON)
    m = _rolling_mean(flow21, _TD_YEAR)
    s = _rolling_std(flow21, _TD_YEAR)
    return _safe_div(flow21 - m, s)


def dvs_188_dv_std_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """252-day rolling standard deviation of dollar volume."""
    dv = _dv(close, volume)
    return _rolling_std(dv, _TD_YEAR)


def dvs_189_dv_cv_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of dollar volume over 5 days (weekly instability)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_std(dv, _TD_WEEK), _rolling_mean(dv, _TD_WEEK))


def dvs_190_dv_log_cv_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of log-dollar-volume over 21 days (log-space short-term dispersion)."""
    dv = _log_safe(_dv(close, volume))
    return _safe_div(_rolling_std(dv, _TD_MON), _rolling_mean(dv, _TD_MON))


def dvs_191_dv_log_cv_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of log-dollar-volume over 252 days (log-space annual dispersion)."""
    dv = _log_safe(_dv(close, volume))
    return _safe_div(_rolling_std(dv, _TD_YEAR), _rolling_mean(dv, _TD_YEAR))


def dvs_192_dv_ratio_5d_vs_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day mean DV divided by 63-day mean DV (weekly vs quarterly baseline)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_WEEK), _rolling_mean(dv, _TD_QTR))


def dvs_193_dv_ratio_126d_vs_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day mean DV divided by 252-day mean DV (half-year vs full-year)."""
    dv = _dv(close, volume)
    return _safe_div(_rolling_mean(dv, _TD_HALF), _rolling_mean(dv, _TD_YEAR))


def dvs_194_dv_ewm5_vs_ewm126(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EWM to 126-day EWM of dollar volume (burst vs half-year trend)."""
    dv = _dv(close, volume)
    return _safe_div(_ewm_mean(dv, _TD_WEEK), _ewm_mean(dv, _TD_HALF))


def dvs_195_dv_log_slope_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of log-dollar-volume over trailing 252 days."""
    dv = _log_safe(_dv(close, volume))
    return _linslope(dv, _TD_YEAR)


def dvs_196_dv_slope_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of dollar volume over trailing 5 days (very short-term DV trend)."""
    dv = _dv(close, volume)
    return _linslope(dv, _TD_WEEK)


def dvs_197_dv_distress_index_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """DV z-score-252d times fraction of down-price days in 252d (annual distress)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_YEAR, min_periods=1).sum() / _TD_YEAR
    return z * dn_frac


def dvs_198_dv_tail_risk_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Product of 63d DV ratio and 63d DV cv — quarterly spike intensity times instability."""
    dv = _dv(close, volume)
    ratio = _safe_div(dv, _rolling_mean(dv, _TD_QTR))
    cv = _safe_div(_rolling_std(dv, _TD_QTR), _rolling_mean(dv, _TD_QTR))
    return ratio * cv


def dvs_199_dv_high_low_dv_range_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(63d max DV - 63d min DV) / 63d mean DV — quarterly DV range relative to mean."""
    dv = _dv(close, volume)
    mx = _rolling_max(dv, _TD_QTR)
    mn = _rolling_min(dv, _TD_QTR)
    mean = _rolling_mean(dv, _TD_QTR)
    return _safe_div(mx - mn, mean)


def dvs_200_dv_capitulation_composite_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: DV zscore-252d * down-day-fraction-63d * (1 + dv-pct-rank-252d)."""
    dv = _dv(close, volume)
    m = _rolling_mean(dv, _TD_YEAR)
    s = _rolling_std(dv, _TD_YEAR)
    z252 = _safe_div(dv - m, s)
    ret = close.pct_change(1)
    dn_frac = (ret < 0).astype(float).rolling(_TD_QTR, min_periods=1).sum() / _TD_QTR
    rank = dv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True).fillna(0.0)
    return z252 * dn_frac * (1.0 + rank)


# ── Registry ──────────────────────────────────────────────────────────────────

DOLLAR_VOLUME_SHOCK_REGISTRY_076_150 = {
    "dvs_076_dv_high_close_ratio": {"inputs": ["close", "high", "volume"], "func": dvs_076_dv_high_close_ratio},
    "dvs_077_dv_low_close_ratio": {"inputs": ["close", "low", "volume"], "func": dvs_077_dv_low_close_ratio},
    "dvs_078_dv_intraday_range_norm": {"inputs": ["close", "high", "low", "volume"], "func": dvs_078_dv_intraday_range_norm},
    "dvs_079_dv_range_norm_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_079_dv_range_norm_zscore_63d},
    "dvs_080_dv_open_gap_interaction": {"inputs": ["close", "open", "volume"], "func": dvs_080_dv_open_gap_interaction},
    "dvs_081_dv_open_gap_interaction_zscore_63d": {"inputs": ["close", "open", "volume"], "func": dvs_081_dv_open_gap_interaction_zscore_63d},
    "dvs_082_dv_close_near_low_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_082_dv_close_near_low_zscore_63d},
    "dvs_083_dv_close_near_high_zscore_63d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_083_dv_close_near_high_zscore_63d},
    "dvs_084_dv_high_volume_range_product_21d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_084_dv_high_volume_range_product_21d},
    "dvs_085_dv_high_volume_range_product_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_085_dv_high_volume_range_product_zscore_252d},
    "dvs_086_dv_ewm21_vs_ewm63": {"inputs": ["close", "volume"], "func": dvs_086_dv_ewm21_vs_ewm63},
    "dvs_087_dv_ewm21_vs_ewm126": {"inputs": ["close", "volume"], "func": dvs_087_dv_ewm21_vs_ewm126},
    "dvs_088_dv_ewm5_vs_ewm21": {"inputs": ["close", "volume"], "func": dvs_088_dv_ewm5_vs_ewm21},
    "dvs_089_dv_slope_21d": {"inputs": ["close", "volume"], "func": dvs_089_dv_slope_21d},
    "dvs_090_dv_slope_63d": {"inputs": ["close", "volume"], "func": dvs_090_dv_slope_63d},
    "dvs_091_dv_slope_norm_21d": {"inputs": ["close", "volume"], "func": dvs_091_dv_slope_norm_21d},
    "dvs_092_dv_log_slope_21d": {"inputs": ["close", "volume"], "func": dvs_092_dv_log_slope_21d},
    "dvs_093_dv_log_slope_63d": {"inputs": ["close", "volume"], "func": dvs_093_dv_log_slope_63d},
    "dvs_094_dv_above_ewm21_streak": {"inputs": ["close", "volume"], "func": dvs_094_dv_above_ewm21_streak},
    "dvs_095_dv_below_ewm21_streak": {"inputs": ["close", "volume"], "func": dvs_095_dv_below_ewm21_streak},
    "dvs_096_dv_gap_down_sum_21d": {"inputs": ["close", "open", "volume"], "func": dvs_096_dv_gap_down_sum_21d},
    "dvs_097_dv_gap_down_sum_63d": {"inputs": ["close", "open", "volume"], "func": dvs_097_dv_gap_down_sum_63d},
    "dvs_098_dv_gap_down_fraction_dv_21d": {"inputs": ["close", "open", "volume"], "func": dvs_098_dv_gap_down_fraction_dv_21d},
    "dvs_099_dv_gap_down_fraction_dv_63d": {"inputs": ["close", "open", "volume"], "func": dvs_099_dv_gap_down_fraction_dv_63d},
    "dvs_100_dv_gap_down_spike_count_63d": {"inputs": ["close", "open", "volume"], "func": dvs_100_dv_gap_down_spike_count_63d},
    "dvs_101_dv_open_to_close_signed_21d": {"inputs": ["close", "open", "volume"], "func": dvs_101_dv_open_to_close_signed_21d},
    "dvs_102_dv_open_to_close_signed_63d": {"inputs": ["close", "open", "volume"], "func": dvs_102_dv_open_to_close_signed_63d},
    "dvs_103_dv_bear_candle_sum_21d": {"inputs": ["close", "open", "volume"], "func": dvs_103_dv_bear_candle_sum_21d},
    "dvs_104_dv_bear_candle_fraction_21d": {"inputs": ["close", "open", "volume"], "func": dvs_104_dv_bear_candle_fraction_21d},
    "dvs_105_dv_bear_candle_fraction_63d": {"inputs": ["close", "open", "volume"], "func": dvs_105_dv_bear_candle_fraction_63d},
    "dvs_106_dv_at_new_low_sum_63d": {"inputs": ["close", "volume"], "func": dvs_106_dv_at_new_low_sum_63d},
    "dvs_107_dv_at_new_low_sum_252d": {"inputs": ["close", "volume"], "func": dvs_107_dv_at_new_low_sum_252d},
    "dvs_108_dv_at_new_low_fraction_63d": {"inputs": ["close", "volume"], "func": dvs_108_dv_at_new_low_fraction_63d},
    "dvs_109_dv_at_new_low_fraction_252d": {"inputs": ["close", "volume"], "func": dvs_109_dv_at_new_low_fraction_252d},
    "dvs_110_dv_bottom_decile_price_sum_63d": {"inputs": ["close", "volume"], "func": dvs_110_dv_bottom_decile_price_sum_63d},
    "dvs_111_dv_bottom_quartile_price_fraction_63d": {"inputs": ["close", "volume"], "func": dvs_111_dv_bottom_quartile_price_fraction_63d},
    "dvs_112_dv_acceleration_5d": {"inputs": ["close", "volume"], "func": dvs_112_dv_acceleration_5d},
    "dvs_113_dv_acceleration_21d": {"inputs": ["close", "volume"], "func": dvs_113_dv_acceleration_21d},
    "dvs_114_dv_std_21d": {"inputs": ["close", "volume"], "func": dvs_114_dv_std_21d},
    "dvs_115_dv_std_63d": {"inputs": ["close", "volume"], "func": dvs_115_dv_std_63d},
    "dvs_116_dv_ratio_5d_vs_21d": {"inputs": ["close", "volume"], "func": dvs_116_dv_ratio_5d_vs_21d},
    "dvs_117_dv_ratio_21d_vs_126d": {"inputs": ["close", "volume"], "func": dvs_117_dv_ratio_21d_vs_126d},
    "dvs_118_dv_ratio_21d_vs_252d": {"inputs": ["close", "volume"], "func": dvs_118_dv_ratio_21d_vs_252d},
    "dvs_119_dv_ratio_63d_vs_252d": {"inputs": ["close", "volume"], "func": dvs_119_dv_ratio_63d_vs_252d},
    "dvs_120_dv_ratio_5d_vs_252d": {"inputs": ["close", "volume"], "func": dvs_120_dv_ratio_5d_vs_252d},
    "dvs_121_dv_min_21d_vs_mean_252d": {"inputs": ["close", "volume"], "func": dvs_121_dv_min_21d_vs_mean_252d},
    "dvs_122_dv_cv_21d": {"inputs": ["close", "volume"], "func": dvs_122_dv_cv_21d},
    "dvs_123_dv_cv_63d": {"inputs": ["close", "volume"], "func": dvs_123_dv_cv_63d},
    "dvs_124_dv_cv_252d": {"inputs": ["close", "volume"], "func": dvs_124_dv_cv_252d},
    "dvs_125_dv_log_cv_63d": {"inputs": ["close", "volume"], "func": dvs_125_dv_log_cv_63d},
    "dvs_126_dv_autocorr_lag1_21d": {"inputs": ["close", "volume"], "func": dvs_126_dv_autocorr_lag1_21d},
    "dvs_127_dv_autocorr_lag1_63d": {"inputs": ["close", "volume"], "func": dvs_127_dv_autocorr_lag1_63d},
    "dvs_128_dv_persistence_score_21d": {"inputs": ["close", "volume"], "func": dvs_128_dv_persistence_score_21d},
    "dvs_129_dv_persistence_score_63d": {"inputs": ["close", "volume"], "func": dvs_129_dv_persistence_score_63d},
    "dvs_130_dv_decay_ratio_21d": {"inputs": ["close", "volume"], "func": dvs_130_dv_decay_ratio_21d},
    "dvs_131_dv_spike_flag_1d": {"inputs": ["close", "volume"], "func": dvs_131_dv_spike_flag_1d},
    "dvs_132_dv_spike_flag_3x_1d": {"inputs": ["close", "volume"], "func": dvs_132_dv_spike_flag_3x_1d},
    "dvs_133_dv_spike_flag_5x_1d": {"inputs": ["close", "volume"], "func": dvs_133_dv_spike_flag_5x_1d},
    "dvs_134_dv_spike_since_days": {"inputs": ["close", "volume"], "func": dvs_134_dv_spike_since_days},
    "dvs_135_dv_spike_recency_decay_63d": {"inputs": ["close", "volume"], "func": dvs_135_dv_spike_recency_decay_63d},
    "dvs_136_dv_distress_index_21d": {"inputs": ["close", "volume"], "func": dvs_136_dv_distress_index_21d},
    "dvs_137_dv_distress_index_63d": {"inputs": ["close", "volume"], "func": dvs_137_dv_distress_index_63d},
    "dvs_138_dv_composite_score_21d": {"inputs": ["close", "volume"], "func": dvs_138_dv_composite_score_21d},
    "dvs_139_dv_composite_score_63d": {"inputs": ["close", "volume"], "func": dvs_139_dv_composite_score_63d},
    "dvs_140_dv_above_sma21_streak": {"inputs": ["close", "volume"], "func": dvs_140_dv_above_sma21_streak},
    "dvs_141_dv_5d_sum_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_141_dv_5d_sum_zscore_252d},
    "dvs_142_dv_1d_vs_5d_avg_ratio": {"inputs": ["close", "volume"], "func": dvs_142_dv_1d_vs_5d_avg_ratio},
    "dvs_143_dv_1d_vs_21d_avg_log_ratio": {"inputs": ["close", "volume"], "func": dvs_143_dv_1d_vs_21d_avg_log_ratio},
    "dvs_144_dv_expanding_zscore_on_down_days": {"inputs": ["close", "volume"], "func": dvs_144_dv_expanding_zscore_on_down_days},
    "dvs_145_dv_spike_count_21d_zscore_252d": {"inputs": ["close", "volume"], "func": dvs_145_dv_spike_count_21d_zscore_252d},
    "dvs_146_dv_intraday_net_flow_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": dvs_146_dv_intraday_net_flow_21d},
    "dvs_147_dv_intraday_net_flow_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": dvs_147_dv_intraday_net_flow_63d},
    "dvs_148_dv_tail_risk_score_21d": {"inputs": ["close", "volume"], "func": dvs_148_dv_tail_risk_score_21d},
    "dvs_149_dv_high_low_dv_range_ratio_21d": {"inputs": ["close", "volume"], "func": dvs_149_dv_high_low_dv_range_ratio_21d},
    "dvs_150_dv_capitulation_composite": {"inputs": ["close", "volume"], "func": dvs_150_dv_capitulation_composite},
    "dvs_176_dv_range_norm_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_176_dv_range_norm_zscore_21d},
    "dvs_177_dv_range_norm_zscore_252d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_177_dv_range_norm_zscore_252d},
    "dvs_178_dv_close_near_low_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_178_dv_close_near_low_zscore_21d},
    "dvs_179_dv_close_near_low_sum_63d": {"inputs": ["close", "high", "low", "volume"], "func": dvs_179_dv_close_near_low_sum_63d},
    "dvs_180_dv_open_gap_sum_21d": {"inputs": ["close", "open", "volume"], "func": dvs_180_dv_open_gap_sum_21d},
    "dvs_181_dv_gap_up_sum_21d": {"inputs": ["close", "open", "volume"], "func": dvs_181_dv_gap_up_sum_21d},
    "dvs_182_dv_gap_up_sum_63d": {"inputs": ["close", "open", "volume"], "func": dvs_182_dv_gap_up_sum_63d},
    "dvs_183_dv_gap_down_vs_gap_up_ratio_63d": {"inputs": ["close", "open", "volume"], "func": dvs_183_dv_gap_down_vs_gap_up_ratio_63d},
    "dvs_184_dv_bear_candle_sum_63d": {"inputs": ["close", "open", "volume"], "func": dvs_184_dv_bear_candle_sum_63d},
    "dvs_185_dv_bear_candle_fraction_252d": {"inputs": ["close", "open", "volume"], "func": dvs_185_dv_bear_candle_fraction_252d},
    "dvs_186_dv_intraday_net_flow_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": dvs_186_dv_intraday_net_flow_252d},
    "dvs_187_dv_intraday_net_flow_zscore_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": dvs_187_dv_intraday_net_flow_zscore_252d},
    "dvs_188_dv_std_252d": {"inputs": ["close", "volume"], "func": dvs_188_dv_std_252d},
    "dvs_189_dv_cv_5d": {"inputs": ["close", "volume"], "func": dvs_189_dv_cv_5d},
    "dvs_190_dv_log_cv_21d": {"inputs": ["close", "volume"], "func": dvs_190_dv_log_cv_21d},
    "dvs_191_dv_log_cv_252d": {"inputs": ["close", "volume"], "func": dvs_191_dv_log_cv_252d},
    "dvs_192_dv_ratio_5d_vs_63d": {"inputs": ["close", "volume"], "func": dvs_192_dv_ratio_5d_vs_63d},
    "dvs_193_dv_ratio_126d_vs_252d": {"inputs": ["close", "volume"], "func": dvs_193_dv_ratio_126d_vs_252d},
    "dvs_194_dv_ewm5_vs_ewm126": {"inputs": ["close", "volume"], "func": dvs_194_dv_ewm5_vs_ewm126},
    "dvs_195_dv_log_slope_252d": {"inputs": ["close", "volume"], "func": dvs_195_dv_log_slope_252d},
    "dvs_196_dv_slope_5d": {"inputs": ["close", "volume"], "func": dvs_196_dv_slope_5d},
    "dvs_197_dv_distress_index_252d": {"inputs": ["close", "volume"], "func": dvs_197_dv_distress_index_252d},
    "dvs_198_dv_tail_risk_score_63d": {"inputs": ["close", "volume"], "func": dvs_198_dv_tail_risk_score_63d},
    "dvs_199_dv_high_low_dv_range_ratio_63d": {"inputs": ["close", "volume"], "func": dvs_199_dv_high_low_dv_range_ratio_63d},
    "dvs_200_dv_capitulation_composite_252d": {"inputs": ["close", "volume"], "func": dvs_200_dv_capitulation_composite_252d},
}
