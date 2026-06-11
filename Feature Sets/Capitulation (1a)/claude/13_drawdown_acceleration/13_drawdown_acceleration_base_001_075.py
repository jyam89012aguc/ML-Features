"""
13_drawdown_acceleration — Base Features 001-100
Domain: drawdown acceleration — whether a price decline is speeding up; 2nd-order behavior
of the drawdown path: gap to trailing highs widening at increasing rate, successive declines
steeper, slope of the underwater curve steepening.
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
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
    """Rolling maximum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling minimum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling standard deviation over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    """Rolling median over w periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponentially-weighted mean with given span."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped to _EPS to avoid log(0)."""
    return np.log(s.clip(lower=_EPS))


def _drawdown(close: pd.Series, w: int) -> pd.Series:
    """Drawdown from rolling w-period high: (close - roll_high) / roll_high."""
    roll_high = _rolling_max(close, w)
    return _safe_div(close - roll_high, roll_high)


def _log_drawdown(close: pd.Series, w: int) -> pd.Series:
    """Log drawdown: log(close) - log(rolling w-period high)."""
    return _log_safe(close) - _log_safe(_rolling_max(close, w))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Raw drawdown depth from rolling highs ---

def dacc_001_drawdown_from_21d_high(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 21-day rolling high (fraction)."""
    return _drawdown(close, _TD_MON)


def dacc_002_drawdown_from_63d_high(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 63-day rolling high (fraction)."""
    return _drawdown(close, _TD_QTR)


def dacc_003_drawdown_from_126d_high(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 126-day rolling high (fraction)."""
    return _drawdown(close, _TD_HALF)


def dacc_004_drawdown_from_252d_high(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 252-day rolling high (fraction)."""
    return _drawdown(close, _TD_YEAR)


def dacc_005_drawdown_from_504d_high(close: pd.Series) -> pd.Series:
    """Drawdown of close from its 504-day rolling high (fraction)."""
    return _drawdown(close, 504)


def dacc_006_log_drawdown_from_21d_high(close: pd.Series) -> pd.Series:
    """Log drawdown from 21-day rolling high."""
    return _log_drawdown(close, _TD_MON)


def dacc_007_log_drawdown_from_63d_high(close: pd.Series) -> pd.Series:
    """Log drawdown from 63-day rolling high."""
    return _log_drawdown(close, _TD_QTR)


def dacc_008_log_drawdown_from_252d_high(close: pd.Series) -> pd.Series:
    """Log drawdown from 252-day rolling high."""
    return _log_drawdown(close, _TD_YEAR)


def dacc_009_drawdown_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day drawdown to 252-day drawdown (recent vs long-term severity)."""
    dd21 = _drawdown(close, _TD_MON)
    dd252 = _drawdown(close, _TD_YEAR)
    return _safe_div(dd21, dd252.replace(0, np.nan))


def dacc_010_drawdown_63d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day drawdown to 252-day drawdown."""
    dd63 = _drawdown(close, _TD_QTR)
    dd252 = _drawdown(close, _TD_YEAR)
    return _safe_div(dd63, dd252.replace(0, np.nan))


# --- Group B (011-020): 5-day change in drawdown (velocity = 1st derivative) ---

def dacc_011_drawdown_21d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 21-day drawdown (how fast the underwater gap is growing)."""
    return _drawdown(close, _TD_MON).diff(_TD_WEEK)


def dacc_012_drawdown_63d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 63-day drawdown."""
    return _drawdown(close, _TD_QTR).diff(_TD_WEEK)


def dacc_013_drawdown_252d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 252-day drawdown."""
    return _drawdown(close, _TD_YEAR).diff(_TD_WEEK)


def dacc_014_drawdown_21d_1d_chg(close: pd.Series) -> pd.Series:
    """1-day change in 21-day drawdown (single-day deepening of underwater curve)."""
    return _drawdown(close, _TD_MON).diff(1)


def dacc_015_drawdown_63d_1d_chg(close: pd.Series) -> pd.Series:
    """1-day change in 63-day drawdown."""
    return _drawdown(close, _TD_QTR).diff(1)


def dacc_016_drawdown_252d_1d_chg(close: pd.Series) -> pd.Series:
    """1-day change in 252-day drawdown."""
    return _drawdown(close, _TD_YEAR).diff(1)


def dacc_017_drawdown_21d_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in 21-day drawdown (monthly deterioration)."""
    return _drawdown(close, _TD_MON).diff(_TD_MON)


def dacc_018_drawdown_63d_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in 63-day drawdown."""
    return _drawdown(close, _TD_QTR).diff(_TD_MON)


def dacc_019_drawdown_252d_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in 252-day drawdown."""
    return _drawdown(close, _TD_YEAR).diff(_TD_MON)


def dacc_020_log_drawdown_252d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in log drawdown from 252-day high."""
    return _log_drawdown(close, _TD_YEAR).diff(_TD_WEEK)


# --- Group C (021-030): Acceleration (2nd derivative) of drawdown depth ---

def dacc_021_drawdown_21d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day drawdown velocity (21-day window): drawdown acceleration."""
    vel = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_022_drawdown_63d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day drawdown velocity (63-day window): drawdown acceleration."""
    vel = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_023_drawdown_252d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day drawdown velocity (252-day window): drawdown acceleration."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_024_drawdown_21d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day drawdown velocity (21-day window)."""
    vel = _drawdown(close, _TD_MON).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_025_drawdown_63d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day drawdown velocity (63-day window)."""
    vel = _drawdown(close, _TD_QTR).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_026_drawdown_252d_accel_21d(close: pd.Series) -> pd.Series:
    """21-day diff of 5-day drawdown velocity (252-day window)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_MON)


def dacc_027_log_drawdown_252d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day log-drawdown velocity."""
    vel = _log_drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_028_drawdown_21d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day drawdown series over the last 21 days."""
    return _linslope(_drawdown(close, _TD_MON), _TD_MON)


def dacc_029_drawdown_63d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day drawdown series over the last 21 days."""
    return _linslope(_drawdown(close, _TD_QTR), _TD_MON)


def dacc_030_drawdown_252d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 252-day drawdown series over the last 63 days."""
    return _linslope(_drawdown(close, _TD_YEAR), _TD_QTR)


# --- Group D (031-040): Drawdown depth rolling statistics ---

def dacc_031_drawdown_252d_rolling_mean_21d(close: pd.Series) -> pd.Series:
    """21-day rolling mean of 252-day drawdown (average recent underwater depth)."""
    return _rolling_mean(_drawdown(close, _TD_YEAR), _TD_MON)


def dacc_032_drawdown_252d_rolling_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of 252-day drawdown."""
    return _rolling_mean(_drawdown(close, _TD_YEAR), _TD_QTR)


def dacc_033_drawdown_252d_rolling_std_21d(close: pd.Series) -> pd.Series:
    """21-day rolling std of 252-day drawdown (volatility of underwater curve)."""
    return _rolling_std(_drawdown(close, _TD_YEAR), _TD_MON)


def dacc_034_drawdown_252d_rolling_std_63d(close: pd.Series) -> pd.Series:
    """63-day rolling std of 252-day drawdown."""
    return _rolling_std(_drawdown(close, _TD_YEAR), _TD_QTR)


def dacc_035_drawdown_252d_min_21d(close: pd.Series) -> pd.Series:
    """21-day minimum of 252-day drawdown (worst depth in recent month)."""
    return _rolling_min(_drawdown(close, _TD_YEAR), _TD_MON)


def dacc_036_drawdown_252d_min_63d(close: pd.Series) -> pd.Series:
    """63-day minimum of 252-day drawdown (worst depth in recent quarter)."""
    return _rolling_min(_drawdown(close, _TD_YEAR), _TD_QTR)


def dacc_037_drawdown_252d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 252-day drawdown within trailing 252-day distribution."""
    dd = _drawdown(close, _TD_YEAR)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_038_drawdown_21d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding all-time minimum of 21-day drawdown (historical worst underwater)."""
    return _drawdown(close, _TD_MON).expanding(min_periods=1).min()


def dacc_039_drawdown_252d_expanding_min(close: pd.Series) -> pd.Series:
    """Expanding all-time minimum of 252-day drawdown."""
    return _drawdown(close, _TD_YEAR).expanding(min_periods=1).min()


def dacc_040_drawdown_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day drawdown relative to 252-day distribution."""
    dd = _drawdown(close, _TD_MON)
    m = _rolling_mean(dd, _TD_YEAR)
    s = _rolling_std(dd, _TD_YEAR)
    return _safe_div(dd - m, s)


# --- Group E (041-050): Successive decline steepness (step-change in drawdown) ---

def dacc_041_successive_decline_5d_vs_prior_5d(close: pd.Series) -> pd.Series:
    """5-day return minus prior 5-day return: steeper decline than prior period."""
    ret5 = close.pct_change(_TD_WEEK)
    return ret5 - ret5.shift(_TD_WEEK)


def dacc_042_successive_decline_21d_vs_prior_21d(close: pd.Series) -> pd.Series:
    """21-day return minus prior 21-day return: monthly decline steepening."""
    ret21 = close.pct_change(_TD_MON)
    return ret21 - ret21.shift(_TD_MON)


def dacc_043_successive_decline_63d_vs_prior_63d(close: pd.Series) -> pd.Series:
    """63-day return minus prior 63-day return: quarterly decline steepening."""
    ret63 = close.pct_change(_TD_QTR)
    return ret63 - ret63.shift(_TD_QTR)


def dacc_044_decline_acceleration_5d_count_21d(close: pd.Series) -> pd.Series:
    """Count of 5-day periods in past 21 days where decline steepened vs prior period."""
    ret5 = close.pct_change(_TD_WEEK)
    steeper = (ret5 < ret5.shift(_TD_WEEK)).astype(float)
    return _rolling_sum(steeper, _TD_MON)


def dacc_045_log_ret_5d_accel_flag(close: pd.Series) -> pd.Series:
    """Flag: today's log-return is worse than 5-day average log-return (steepening)."""
    lr = _log_safe(close).diff(1)
    avg5 = _rolling_mean(lr, _TD_WEEK)
    return (lr < avg5).astype(float)


def dacc_046_successive_wkly_loss_steeper_count_63d(close: pd.Series) -> pd.Series:
    """Count of weeks in past 63 days where weekly loss was worse than prior week."""
    ret5 = close.pct_change(_TD_WEEK)
    steeper = ((ret5 < 0) & (ret5 < ret5.shift(_TD_WEEK))).astype(float)
    return _rolling_sum(steeper, _TD_QTR)


def dacc_047_drawdown_1d_chg_momentum_5d(close: pd.Series) -> pd.Series:
    """5-day rolling mean of 1-day drawdown changes (trend in daily deepening)."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    return _rolling_mean(dd_chg, _TD_WEEK)


def dacc_048_drawdown_depth_increment_21d(close: pd.Series) -> pd.Series:
    """Sum of positive drawdown increments over 21 days (total deepening magnitude)."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deepening = dd_chg.where(dd_chg < 0, 0.0)
    return _rolling_sum(deepening, _TD_MON)


def dacc_049_drawdown_depth_increment_63d(close: pd.Series) -> pd.Series:
    """Sum of positive drawdown increments over 63 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    deepening = dd_chg.where(dd_chg < 0, 0.0)
    return _rolling_sum(deepening, _TD_QTR)


def dacc_050_accel_days_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of days in past 21 days where drawdown deepened more than prior day."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    accel = (dd_chg < dd_chg.shift(1)).astype(float)
    return _rolling_mean(accel, _TD_MON)


# --- Group F (051-060): Slope of underwater curve (OLS over varying windows) ---

def dacc_051_drawdown_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of 252-day drawdown series over the last 5 days."""
    return _linslope(_drawdown(close, _TD_YEAR), _TD_WEEK)


def dacc_052_drawdown_slope_10d(close: pd.Series) -> pd.Series:
    """OLS slope of 252-day drawdown series over the last 10 days."""
    return _linslope(_drawdown(close, _TD_YEAR), 10)


def dacc_053_drawdown_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 252-day drawdown series over the last 63 days."""
    return _linslope(_drawdown(close, _TD_YEAR), _TD_QTR)


def dacc_054_drawdown_63d_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day drawdown series over the last 5 days."""
    return _linslope(_drawdown(close, _TD_QTR), _TD_WEEK)


def dacc_055_drawdown_21d_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day drawdown series over the last 5 days."""
    return _linslope(_drawdown(close, _TD_MON), _TD_WEEK)


def dacc_056_log_drawdown_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of log 252-day drawdown series over the last 21 days."""
    return _linslope(_log_drawdown(close, _TD_YEAR), _TD_MON)


def dacc_057_drawdown_slope_steepening_5d(close: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 252-day drawdown (slope is steepening indicator)."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return slp.diff(_TD_WEEK)


def dacc_058_drawdown_slope_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day OLS slope of 252-day drawdown within 252-day distribution."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    m = _rolling_mean(slp, _TD_YEAR)
    s = _rolling_std(slp, _TD_YEAR)
    return _safe_div(slp - m, s)


def dacc_059_drawdown_slope_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day drawdown slope in trailing 252-day distribution."""
    slp = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    return slp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_060_drawdown_ewm_slope_21d(close: pd.Series) -> pd.Series:
    """21-day EWM of daily drawdown changes (exponentially-weighted deepening trend)."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    return _ewm_mean(dd_chg, _TD_MON)


# --- Group G (061-075): Drawdown acceleration: intraday, volume-weighted, cross-window ---

def dacc_061_intraday_drawdown_from_high_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Drawdown of close from rolling 21-day intraday high (uses daily high)."""
    roll_high = _rolling_max(high, _TD_MON)
    return _safe_div(close - roll_high, roll_high)


def dacc_062_intraday_drawdown_from_high_252d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Drawdown of close from rolling 252-day intraday high."""
    roll_high = _rolling_max(high, _TD_YEAR)
    return _safe_div(close - roll_high, roll_high)


def dacc_063_intraday_drawdown_5d_chg(close: pd.Series, high: pd.Series) -> pd.Series:
    """5-day change in intraday 252-day drawdown."""
    dd = _safe_div(close - _rolling_max(high, _TD_YEAR), _rolling_max(high, _TD_YEAR))
    return dd.diff(_TD_WEEK)


def dacc_064_low_drawdown_from_252d_high(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of intraday low from 252-day rolling high (maximum intraday depth)."""
    roll_high = _rolling_max(high, _TD_YEAR)
    return _safe_div(low - roll_high, roll_high)


def dacc_065_low_drawdown_5d_chg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day change in intraday-low drawdown from 252-day high."""
    roll_high = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(low - roll_high, roll_high)
    return dd.diff(_TD_WEEK)


def dacc_066_volume_weighted_drawdown_21d(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 21-day drawdown depth (high-volume dips weighted more)."""
    roll_high = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - roll_high, roll_high)
    vw_dd = dd * volume
    vw_sum = _rolling_sum(vw_dd, _TD_MON)
    vol_sum = _rolling_sum(volume, _TD_MON)
    return _safe_div(vw_sum, vol_sum)


def dacc_067_volume_weighted_drawdown_63d(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 63-day drawdown depth."""
    roll_high = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - roll_high, roll_high)
    vw_dd = dd * volume
    vw_sum = _rolling_sum(vw_dd, _TD_QTR)
    vol_sum = _rolling_sum(volume, _TD_QTR)
    return _safe_div(vw_sum, vol_sum)


def dacc_068_vw_drawdown_5d_chg(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day change in volume-weighted 21-day drawdown."""
    roll_high = _rolling_max(high, _TD_YEAR)
    dd = _safe_div(close - roll_high, roll_high)
    vw_dd = dd * volume
    vw_sum = _rolling_sum(vw_dd, _TD_MON)
    vol_sum = _rolling_sum(volume, _TD_MON)
    vw = _safe_div(vw_sum, vol_sum)
    return vw.diff(_TD_WEEK)


def dacc_069_drawdown_252d_vs_expanding_min_ratio(close: pd.Series) -> pd.Series:
    """Current 252-day drawdown as fraction of all-time expanding min drawdown."""
    dd = _drawdown(close, _TD_YEAR)
    exp_min = dd.expanding(min_periods=1).min()
    return _safe_div(dd, exp_min.replace(0, np.nan))


def dacc_070_drawdown_acceleration_score_21d(close: pd.Series) -> pd.Series:
    """Composite acceleration score: mean of 1d/5d/21d changes in 252-day drawdown."""
    dd = _drawdown(close, _TD_YEAR)
    c1 = dd.diff(1)
    c5 = dd.diff(_TD_WEEK)
    c21 = dd.diff(_TD_MON)
    return (c1 + c5 + c21) / 3.0


def dacc_071_drawdown_cross_window_accel(close: pd.Series) -> pd.Series:
    """Drawdown steepening: 21-day window depth minus 63-day window depth (short > long = worsening)."""
    return _drawdown(close, _TD_MON) - _drawdown(close, _TD_QTR)


def dacc_072_drawdown_63d_minus_252d(close: pd.Series) -> pd.Series:
    """63-day drawdown minus 252-day drawdown (quarter-horizon vs year-horizon depth gap)."""
    return _drawdown(close, _TD_QTR) - _drawdown(close, _TD_YEAR)


def dacc_073_drawdown_atr_normalized_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day drawdown depth normalized by 21-day ATR."""
    dd = _drawdown(close, _TD_YEAR) * close
    atr21 = _rolling_mean(_tr(close, high, low), _TD_MON)
    return _safe_div(dd, atr21)


def dacc_074_drawdown_atr_normalized_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252-day drawdown depth normalized by 63-day ATR."""
    dd = _drawdown(close, _TD_YEAR) * close
    atr63 = _rolling_mean(_tr(close, high, low), _TD_QTR)
    return _safe_div(dd, atr63)


def dacc_075_drawdown_slope_accel_flag(close: pd.Series) -> pd.Series:
    """Flag: 21-day slope of 252-day drawdown is more negative than its 63-day average slope."""
    slp21 = _linslope(_drawdown(close, _TD_YEAR), _TD_MON)
    avg_slp = _rolling_mean(slp21, _TD_QTR)
    return (slp21 < avg_slp).astype(float)


# --- Group P (151-160): Drawdown from open, close spread and body measures ---

def dacc_151_drawdown_body_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where candle body (close-open) was negative (closing down)."""
    body_neg = (close < open).astype(float)
    return _rolling_mean(body_neg, _TD_MON)


def dacc_152_drawdown_body_size_on_deep_days_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean candle body size on drawdown-deepening days over 21 days."""
    dd_chg = _drawdown(close, _TD_YEAR).diff(1)
    body = (close - open).abs()
    body_deep = body.where(dd_chg < 0, np.nan)
    return body_deep.rolling(_TD_MON, min_periods=1).mean()


def dacc_153_drawdown_504d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 504-day drawdown (velocity at very long horizon)."""
    return _drawdown(close, 504).diff(_TD_WEEK)


def dacc_154_drawdown_504d_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in 504-day drawdown (monthly worsening at 2-year horizon)."""
    return _drawdown(close, 504).diff(_TD_MON)


def dacc_155_drawdown_126d_5d_chg(close: pd.Series) -> pd.Series:
    """5-day change in 126-day drawdown (half-year horizon velocity)."""
    return _drawdown(close, _TD_HALF).diff(_TD_WEEK)


def dacc_156_drawdown_126d_21d_chg(close: pd.Series) -> pd.Series:
    """21-day change in 126-day drawdown (monthly velocity at half-year horizon)."""
    return _drawdown(close, _TD_HALF).diff(_TD_MON)


def dacc_157_drawdown_126d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 126-day drawdown (acceleration at half-year)."""
    vel = _drawdown(close, _TD_HALF).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_158_drawdown_504d_accel_5d(close: pd.Series) -> pd.Series:
    """5-day diff of 5-day velocity of 504-day drawdown (acceleration at 2-year horizon)."""
    vel = _drawdown(close, 504).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def dacc_159_drawdown_126d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 126-day drawdown series over the last 21 days."""
    return _linslope(_drawdown(close, _TD_HALF), _TD_MON)


def dacc_160_drawdown_504d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 504-day drawdown series over the last 21 days."""
    return _linslope(_drawdown(close, 504), _TD_MON)


# --- Group Q (161-170): Drawdown depth relative to low and range ---

def dacc_161_low_to_high_range_drawdown_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 21-day high-low range expressed as drawdown fraction."""
    rng_high = _rolling_max(high, _TD_MON)
    rng_low = _rolling_min(low, _TD_MON)
    return _safe_div(close - rng_high, rng_high - rng_low)


def dacc_162_low_to_high_range_drawdown_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 63-day high-low range expressed as drawdown fraction."""
    rng_high = _rolling_max(high, _TD_QTR)
    rng_low = _rolling_min(low, _TD_QTR)
    return _safe_div(close - rng_high, rng_high - rng_low)


def dacc_163_low_to_high_range_drawdown_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close position within 252-day high-low range expressed as drawdown fraction."""
    rng_high = _rolling_max(high, _TD_YEAR)
    rng_low = _rolling_min(low, _TD_YEAR)
    return _safe_div(close - rng_high, rng_high - rng_low)


def dacc_164_close_to_252d_low_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Close relative to 252-day rolling low: (close - low252) / low252."""
    low252 = _rolling_min(low, _TD_YEAR)
    return _safe_div(close - low252, low252)


def dacc_165_close_to_21d_low_drawdown(close: pd.Series, low: pd.Series) -> pd.Series:
    """Drawdown of close from 21-day rolling close-low (using low series)."""
    low21 = _rolling_min(low, _TD_MON)
    return _safe_div(close - _rolling_max(close, _TD_MON), _rolling_max(close, _TD_MON))


def dacc_166_drawdown_range_contraction_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day rolling (high-low) range normalized by close as contraction measure."""
    rng = high - low
    return _safe_div(_rolling_mean(rng, _TD_MON), close)


def dacc_167_drawdown_range_contraction_5d_chg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day change in 21-day normalized range (range tightening during decline)."""
    rng = high - low
    rng_norm = _safe_div(_rolling_mean(rng, _TD_MON), close)
    return rng_norm.diff(_TD_WEEK)


def dacc_168_drawdown_low_252d_5d_chg(close: pd.Series, low: pd.Series) -> pd.Series:
    """5-day change in close-to-252d-low ratio (approaching multi-year lows faster)."""
    low252 = _rolling_min(low, _TD_YEAR)
    ratio = _safe_div(close - low252, low252)
    return ratio.diff(_TD_WEEK)


def dacc_169_drawdown_63d_vs_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 63-day drawdown to 504-day drawdown (near vs very-long horizon severity)."""
    dd63 = _drawdown(close, _TD_QTR)
    dd504 = _drawdown(close, 504)
    return _safe_div(dd63, dd504.replace(0, np.nan))


def dacc_170_drawdown_126d_vs_504d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 126-day drawdown to 504-day drawdown (half-year vs 2-year severity)."""
    dd126 = _drawdown(close, _TD_HALF)
    dd504 = _drawdown(close, 504)
    return _safe_div(dd126, dd504.replace(0, np.nan))


# --- Group R (171-175): EWM and percentile drawdown extensions ---

def dacc_171_drawdown_252d_ewm5_velocity(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-5 smoothed 252-day drawdown (fast EWM velocity)."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_WEEK)
    return dd_ewm.diff(_TD_WEEK)


def dacc_172_drawdown_252d_ewm63_velocity(close: pd.Series) -> pd.Series:
    """5-day diff of EWM-63 smoothed 252-day drawdown (slow EWM velocity)."""
    dd_ewm = _ewm_mean(_drawdown(close, _TD_YEAR), _TD_QTR)
    return dd_ewm.diff(_TD_WEEK)


def dacc_173_drawdown_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day drawdown within its trailing 252-day distribution."""
    dd = _drawdown(close, _TD_MON)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_174_drawdown_63d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day drawdown within its trailing 252-day distribution."""
    dd = _drawdown(close, _TD_QTR)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dacc_175_drawdown_velocity_ewm_63d(close: pd.Series) -> pd.Series:
    """EWM-63 of 5-day drawdown velocity (very smooth deterioration trend)."""
    vel = _drawdown(close, _TD_YEAR).diff(_TD_WEEK)
    return _ewm_mean(vel, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_ACCELERATION_REGISTRY_001_075 = {
    "dacc_001_drawdown_from_21d_high": {"inputs": ["close"], "func": dacc_001_drawdown_from_21d_high},
    "dacc_002_drawdown_from_63d_high": {"inputs": ["close"], "func": dacc_002_drawdown_from_63d_high},
    "dacc_003_drawdown_from_126d_high": {"inputs": ["close"], "func": dacc_003_drawdown_from_126d_high},
    "dacc_004_drawdown_from_252d_high": {"inputs": ["close"], "func": dacc_004_drawdown_from_252d_high},
    "dacc_005_drawdown_from_504d_high": {"inputs": ["close"], "func": dacc_005_drawdown_from_504d_high},
    "dacc_006_log_drawdown_from_21d_high": {"inputs": ["close"], "func": dacc_006_log_drawdown_from_21d_high},
    "dacc_007_log_drawdown_from_63d_high": {"inputs": ["close"], "func": dacc_007_log_drawdown_from_63d_high},
    "dacc_008_log_drawdown_from_252d_high": {"inputs": ["close"], "func": dacc_008_log_drawdown_from_252d_high},
    "dacc_009_drawdown_21d_vs_252d_ratio": {"inputs": ["close"], "func": dacc_009_drawdown_21d_vs_252d_ratio},
    "dacc_010_drawdown_63d_vs_252d_ratio": {"inputs": ["close"], "func": dacc_010_drawdown_63d_vs_252d_ratio},
    "dacc_011_drawdown_21d_5d_chg": {"inputs": ["close"], "func": dacc_011_drawdown_21d_5d_chg},
    "dacc_012_drawdown_63d_5d_chg": {"inputs": ["close"], "func": dacc_012_drawdown_63d_5d_chg},
    "dacc_013_drawdown_252d_5d_chg": {"inputs": ["close"], "func": dacc_013_drawdown_252d_5d_chg},
    "dacc_014_drawdown_21d_1d_chg": {"inputs": ["close"], "func": dacc_014_drawdown_21d_1d_chg},
    "dacc_015_drawdown_63d_1d_chg": {"inputs": ["close"], "func": dacc_015_drawdown_63d_1d_chg},
    "dacc_016_drawdown_252d_1d_chg": {"inputs": ["close"], "func": dacc_016_drawdown_252d_1d_chg},
    "dacc_017_drawdown_21d_21d_chg": {"inputs": ["close"], "func": dacc_017_drawdown_21d_21d_chg},
    "dacc_018_drawdown_63d_21d_chg": {"inputs": ["close"], "func": dacc_018_drawdown_63d_21d_chg},
    "dacc_019_drawdown_252d_21d_chg": {"inputs": ["close"], "func": dacc_019_drawdown_252d_21d_chg},
    "dacc_020_log_drawdown_252d_5d_chg": {"inputs": ["close"], "func": dacc_020_log_drawdown_252d_5d_chg},
    "dacc_021_drawdown_21d_accel_5d": {"inputs": ["close"], "func": dacc_021_drawdown_21d_accel_5d},
    "dacc_022_drawdown_63d_accel_5d": {"inputs": ["close"], "func": dacc_022_drawdown_63d_accel_5d},
    "dacc_023_drawdown_252d_accel_5d": {"inputs": ["close"], "func": dacc_023_drawdown_252d_accel_5d},
    "dacc_024_drawdown_21d_accel_21d": {"inputs": ["close"], "func": dacc_024_drawdown_21d_accel_21d},
    "dacc_025_drawdown_63d_accel_21d": {"inputs": ["close"], "func": dacc_025_drawdown_63d_accel_21d},
    "dacc_026_drawdown_252d_accel_21d": {"inputs": ["close"], "func": dacc_026_drawdown_252d_accel_21d},
    "dacc_027_log_drawdown_252d_accel_5d": {"inputs": ["close"], "func": dacc_027_log_drawdown_252d_accel_5d},
    "dacc_028_drawdown_21d_slope_21d": {"inputs": ["close"], "func": dacc_028_drawdown_21d_slope_21d},
    "dacc_029_drawdown_63d_slope_21d": {"inputs": ["close"], "func": dacc_029_drawdown_63d_slope_21d},
    "dacc_030_drawdown_252d_slope_63d": {"inputs": ["close"], "func": dacc_030_drawdown_252d_slope_63d},
    "dacc_031_drawdown_252d_rolling_mean_21d": {"inputs": ["close"], "func": dacc_031_drawdown_252d_rolling_mean_21d},
    "dacc_032_drawdown_252d_rolling_mean_63d": {"inputs": ["close"], "func": dacc_032_drawdown_252d_rolling_mean_63d},
    "dacc_033_drawdown_252d_rolling_std_21d": {"inputs": ["close"], "func": dacc_033_drawdown_252d_rolling_std_21d},
    "dacc_034_drawdown_252d_rolling_std_63d": {"inputs": ["close"], "func": dacc_034_drawdown_252d_rolling_std_63d},
    "dacc_035_drawdown_252d_min_21d": {"inputs": ["close"], "func": dacc_035_drawdown_252d_min_21d},
    "dacc_036_drawdown_252d_min_63d": {"inputs": ["close"], "func": dacc_036_drawdown_252d_min_63d},
    "dacc_037_drawdown_252d_pct_rank_252d": {"inputs": ["close"], "func": dacc_037_drawdown_252d_pct_rank_252d},
    "dacc_038_drawdown_21d_expanding_min": {"inputs": ["close"], "func": dacc_038_drawdown_21d_expanding_min},
    "dacc_039_drawdown_252d_expanding_min": {"inputs": ["close"], "func": dacc_039_drawdown_252d_expanding_min},
    "dacc_040_drawdown_21d_zscore_252d": {"inputs": ["close"], "func": dacc_040_drawdown_21d_zscore_252d},
    "dacc_041_successive_decline_5d_vs_prior_5d": {"inputs": ["close"], "func": dacc_041_successive_decline_5d_vs_prior_5d},
    "dacc_042_successive_decline_21d_vs_prior_21d": {"inputs": ["close"], "func": dacc_042_successive_decline_21d_vs_prior_21d},
    "dacc_043_successive_decline_63d_vs_prior_63d": {"inputs": ["close"], "func": dacc_043_successive_decline_63d_vs_prior_63d},
    "dacc_044_decline_acceleration_5d_count_21d": {"inputs": ["close"], "func": dacc_044_decline_acceleration_5d_count_21d},
    "dacc_045_log_ret_5d_accel_flag": {"inputs": ["close"], "func": dacc_045_log_ret_5d_accel_flag},
    "dacc_046_successive_wkly_loss_steeper_count_63d": {"inputs": ["close"], "func": dacc_046_successive_wkly_loss_steeper_count_63d},
    "dacc_047_drawdown_1d_chg_momentum_5d": {"inputs": ["close"], "func": dacc_047_drawdown_1d_chg_momentum_5d},
    "dacc_048_drawdown_depth_increment_21d": {"inputs": ["close"], "func": dacc_048_drawdown_depth_increment_21d},
    "dacc_049_drawdown_depth_increment_63d": {"inputs": ["close"], "func": dacc_049_drawdown_depth_increment_63d},
    "dacc_050_accel_days_fraction_21d": {"inputs": ["close"], "func": dacc_050_accel_days_fraction_21d},
    "dacc_051_drawdown_slope_5d": {"inputs": ["close"], "func": dacc_051_drawdown_slope_5d},
    "dacc_052_drawdown_slope_10d": {"inputs": ["close"], "func": dacc_052_drawdown_slope_10d},
    "dacc_053_drawdown_slope_63d": {"inputs": ["close"], "func": dacc_053_drawdown_slope_63d},
    "dacc_054_drawdown_63d_slope_5d": {"inputs": ["close"], "func": dacc_054_drawdown_63d_slope_5d},
    "dacc_055_drawdown_21d_slope_5d": {"inputs": ["close"], "func": dacc_055_drawdown_21d_slope_5d},
    "dacc_056_log_drawdown_slope_21d": {"inputs": ["close"], "func": dacc_056_log_drawdown_slope_21d},
    "dacc_057_drawdown_slope_steepening_5d": {"inputs": ["close"], "func": dacc_057_drawdown_slope_steepening_5d},
    "dacc_058_drawdown_slope_21d_zscore_252d": {"inputs": ["close"], "func": dacc_058_drawdown_slope_21d_zscore_252d},
    "dacc_059_drawdown_slope_pct_rank_252d": {"inputs": ["close"], "func": dacc_059_drawdown_slope_pct_rank_252d},
    "dacc_060_drawdown_ewm_slope_21d": {"inputs": ["close"], "func": dacc_060_drawdown_ewm_slope_21d},
    "dacc_061_intraday_drawdown_from_high_21d": {"inputs": ["close", "high"], "func": dacc_061_intraday_drawdown_from_high_21d},
    "dacc_062_intraday_drawdown_from_high_252d": {"inputs": ["close", "high"], "func": dacc_062_intraday_drawdown_from_high_252d},
    "dacc_063_intraday_drawdown_5d_chg": {"inputs": ["close", "high"], "func": dacc_063_intraday_drawdown_5d_chg},
    "dacc_064_low_drawdown_from_252d_high": {"inputs": ["close", "high", "low"], "func": dacc_064_low_drawdown_from_252d_high},
    "dacc_065_low_drawdown_5d_chg": {"inputs": ["close", "high", "low"], "func": dacc_065_low_drawdown_5d_chg},
    "dacc_066_volume_weighted_drawdown_21d": {"inputs": ["close", "high", "volume"], "func": dacc_066_volume_weighted_drawdown_21d},
    "dacc_067_volume_weighted_drawdown_63d": {"inputs": ["close", "high", "volume"], "func": dacc_067_volume_weighted_drawdown_63d},
    "dacc_068_vw_drawdown_5d_chg": {"inputs": ["close", "high", "volume"], "func": dacc_068_vw_drawdown_5d_chg},
    "dacc_069_drawdown_252d_vs_expanding_min_ratio": {"inputs": ["close"], "func": dacc_069_drawdown_252d_vs_expanding_min_ratio},
    "dacc_070_drawdown_acceleration_score_21d": {"inputs": ["close"], "func": dacc_070_drawdown_acceleration_score_21d},
    "dacc_071_drawdown_cross_window_accel": {"inputs": ["close"], "func": dacc_071_drawdown_cross_window_accel},
    "dacc_072_drawdown_63d_minus_252d": {"inputs": ["close"], "func": dacc_072_drawdown_63d_minus_252d},
    "dacc_073_drawdown_atr_normalized_21d": {"inputs": ["close", "high", "low"], "func": dacc_073_drawdown_atr_normalized_21d},
    "dacc_074_drawdown_atr_normalized_63d": {"inputs": ["close", "high", "low"], "func": dacc_074_drawdown_atr_normalized_63d},
    "dacc_075_drawdown_slope_accel_flag": {"inputs": ["close"], "func": dacc_075_drawdown_slope_accel_flag},
    "dacc_151_drawdown_body_fraction_21d": {"inputs": ["close", "open"], "func": dacc_151_drawdown_body_fraction_21d},
    "dacc_152_drawdown_body_size_on_deep_days_21d": {"inputs": ["close", "open"], "func": dacc_152_drawdown_body_size_on_deep_days_21d},
    "dacc_153_drawdown_504d_5d_chg": {"inputs": ["close"], "func": dacc_153_drawdown_504d_5d_chg},
    "dacc_154_drawdown_504d_21d_chg": {"inputs": ["close"], "func": dacc_154_drawdown_504d_21d_chg},
    "dacc_155_drawdown_126d_5d_chg": {"inputs": ["close"], "func": dacc_155_drawdown_126d_5d_chg},
    "dacc_156_drawdown_126d_21d_chg": {"inputs": ["close"], "func": dacc_156_drawdown_126d_21d_chg},
    "dacc_157_drawdown_126d_accel_5d": {"inputs": ["close"], "func": dacc_157_drawdown_126d_accel_5d},
    "dacc_158_drawdown_504d_accel_5d": {"inputs": ["close"], "func": dacc_158_drawdown_504d_accel_5d},
    "dacc_159_drawdown_126d_slope_21d": {"inputs": ["close"], "func": dacc_159_drawdown_126d_slope_21d},
    "dacc_160_drawdown_504d_slope_21d": {"inputs": ["close"], "func": dacc_160_drawdown_504d_slope_21d},
    "dacc_161_low_to_high_range_drawdown_21d": {"inputs": ["close", "high", "low"], "func": dacc_161_low_to_high_range_drawdown_21d},
    "dacc_162_low_to_high_range_drawdown_63d": {"inputs": ["close", "high", "low"], "func": dacc_162_low_to_high_range_drawdown_63d},
    "dacc_163_low_to_high_range_drawdown_252d": {"inputs": ["close", "high", "low"], "func": dacc_163_low_to_high_range_drawdown_252d},
    "dacc_164_close_to_252d_low_ratio": {"inputs": ["close", "low"], "func": dacc_164_close_to_252d_low_ratio},
    "dacc_165_close_to_21d_low_drawdown": {"inputs": ["close", "low"], "func": dacc_165_close_to_21d_low_drawdown},
    "dacc_166_drawdown_range_contraction_21d": {"inputs": ["close", "high", "low"], "func": dacc_166_drawdown_range_contraction_21d},
    "dacc_167_drawdown_range_contraction_5d_chg": {"inputs": ["close", "high", "low"], "func": dacc_167_drawdown_range_contraction_5d_chg},
    "dacc_168_drawdown_low_252d_5d_chg": {"inputs": ["close", "low"], "func": dacc_168_drawdown_low_252d_5d_chg},
    "dacc_169_drawdown_63d_vs_504d_ratio": {"inputs": ["close"], "func": dacc_169_drawdown_63d_vs_504d_ratio},
    "dacc_170_drawdown_126d_vs_504d_ratio": {"inputs": ["close"], "func": dacc_170_drawdown_126d_vs_504d_ratio},
    "dacc_171_drawdown_252d_ewm5_velocity": {"inputs": ["close"], "func": dacc_171_drawdown_252d_ewm5_velocity},
    "dacc_172_drawdown_252d_ewm63_velocity": {"inputs": ["close"], "func": dacc_172_drawdown_252d_ewm63_velocity},
    "dacc_173_drawdown_21d_pct_rank_252d": {"inputs": ["close"], "func": dacc_173_drawdown_21d_pct_rank_252d},
    "dacc_174_drawdown_63d_pct_rank_252d": {"inputs": ["close"], "func": dacc_174_drawdown_63d_pct_rank_252d},
    "dacc_175_drawdown_velocity_ewm_63d": {"inputs": ["close"], "func": dacc_175_drawdown_velocity_ewm_63d},
}
