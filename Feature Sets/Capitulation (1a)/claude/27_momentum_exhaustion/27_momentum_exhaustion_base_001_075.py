"""
27_momentum_exhaustion — Base Features 001-075
Domain: loss of downside momentum — deceleration / exhaustion of the decline
Measures the decline running out of force: slowing down-day magnitude, fading
velocity of the fall, deceleration of cumulative loss, smaller new-low increments,
contraction of negative-return magnitude, ratio of recent to earlier down-move size.
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


def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change(1)


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _down_rets(close: pd.Series) -> pd.Series:
    """Daily log-returns on down days only; NaN on up/flat days."""
    r = _log_ret(close)
    return r.where(r < 0, np.nan)


def _down_ret_abs(close: pd.Series) -> pd.Series:
    """Absolute value of daily log-return on down days; NaN otherwise."""
    r = _log_ret(close)
    return r.abs().where(r < 0, np.nan)


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


def _roc(close: pd.Series, n: int) -> pd.Series:
    """Rate of Change: (close / close.shift(n) - 1) * 100."""
    return _safe_div(close, close.shift(n).replace(0, np.nan)) * 100.0 - 100.0


def _kaufman_er(close: pd.Series, n: int) -> pd.Series:
    """Kaufman Efficiency Ratio over n periods (0=choppy, 1=trending)."""
    direction = (close - close.shift(n)).abs()
    volatility = close.diff(1).abs().rolling(n, min_periods=max(2, n // 2)).sum()
    return _safe_div(direction, volatility)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Magnitude of down-day returns shrinking (recent vs earlier) ---

def mex_001_down_ret_mag_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day mean down-return magnitude to 21-day mean: <1 = shrinking."""
    abs_dn = _down_ret_abs(close)
    m5 = abs_dn.rolling(_TD_WEEK, min_periods=1).mean()
    m21 = abs_dn.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(m5, m21)


def mex_002_down_ret_mag_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day mean down-return magnitude to 63-day mean."""
    abs_dn = _down_ret_abs(close)
    m5 = abs_dn.rolling(_TD_WEEK, min_periods=1).mean()
    m63 = abs_dn.rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(m5, m63)


def mex_003_down_ret_mag_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day mean down-return magnitude to 63-day mean."""
    abs_dn = _down_ret_abs(close)
    m21 = abs_dn.rolling(_TD_MON, min_periods=1).mean()
    m63 = abs_dn.rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(m21, m63)


def mex_004_down_ret_mag_ratio_21d_vs_126d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day mean down-return magnitude to 126-day mean."""
    abs_dn = _down_ret_abs(close)
    m21 = abs_dn.rolling(_TD_MON, min_periods=1).mean()
    m126 = abs_dn.rolling(_TD_HALF, min_periods=1).mean()
    return _safe_div(m21, m126)


def mex_005_down_ret_mag_ratio_63d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 63-day mean down-return magnitude to 252-day mean."""
    abs_dn = _down_ret_abs(close)
    m63 = abs_dn.rolling(_TD_QTR, min_periods=1).mean()
    m252 = abs_dn.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()
    return _safe_div(m63, m252)


def mex_006_down_ret_mag_ema5_vs_ema21(close: pd.Series) -> pd.Series:
    """EMA-5 of down-return magnitude divided by EMA-21 (fast vs slow)."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    e5 = _ewm_mean(abs_dn, _TD_WEEK)
    e21 = _ewm_mean(abs_dn, _TD_MON)
    return _safe_div(e5, e21)


def mex_007_down_ret_mag_ema10_vs_ema63(close: pd.Series) -> pd.Series:
    """EMA-10 of down-return magnitude divided by EMA-63."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    e10 = _ewm_mean(abs_dn, 10)
    e63 = _ewm_mean(abs_dn, _TD_QTR)
    return _safe_div(e10, e63)


def mex_008_down_ret_mag_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of absolute down-return magnitude over trailing 21 days (negative = shrinking)."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    return _linslope(abs_dn, _TD_MON)


def mex_009_down_ret_mag_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of absolute down-return magnitude over trailing 63 days."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    return _linslope(abs_dn, _TD_QTR)


def mex_010_down_ret_mag_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day mean down magnitude within 252-day history."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    m5 = abs_dn.rolling(_TD_WEEK, min_periods=1).mean()
    return m5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): Cumulative loss deceleration ---

def mex_011_cum_loss_5d_vs_prior_5d(close: pd.Series) -> pd.Series:
    """Ratio of most-recent 5-day cumulative loss to prior 5-day cumulative loss."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum5 = _rolling_sum(dn, _TD_WEEK)
    return _safe_div(sum5, sum5.shift(_TD_WEEK))


def mex_012_cum_loss_21d_vs_prior_21d(close: pd.Series) -> pd.Series:
    """Ratio of most-recent 21-day cumulative loss to prior 21-day cumulative loss."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum21 = _rolling_sum(dn, _TD_MON)
    return _safe_div(sum21, sum21.shift(_TD_MON))


def mex_013_cum_loss_5d_vs_63d_avg(close: pd.Series) -> pd.Series:
    """5-day cumulative loss divided by 63-day rolling average of 5-day loss."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum5 = _rolling_sum(dn, _TD_WEEK)
    avg63 = _rolling_mean(sum5, _TD_QTR)
    return _safe_div(sum5, avg63)


def mex_014_cum_loss_decel_index_21d(close: pd.Series) -> pd.Series:
    """Difference between first-half and second-half 21-day loss sums (positive = decel)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    first_half = dn.shift(_TD_MON // 2).rolling(_TD_MON // 2, min_periods=1).sum()
    second_half = _rolling_sum(dn, _TD_MON // 2)
    return first_half - second_half


def mex_015_cum_loss_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of daily cumulative-loss series over trailing 21 days (flattening = exhaustion)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    cum_dn = _rolling_sum(dn, _TD_MON)
    return _linslope(cum_dn, _TD_MON)


def mex_016_cum_loss_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day cumulative-loss over trailing 63 days."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    cum21 = _rolling_sum(dn, _TD_MON)
    return _linslope(cum21, _TD_QTR)


def mex_017_loss_pace_ratio_half_windows_63d(close: pd.Series) -> pd.Series:
    """Loss in first 32d of trailing 63d vs last 31d (>1 means recent loss slower)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    recent = _rolling_sum(dn, 31)
    older = _rolling_sum(dn.shift(32), 32)
    return _safe_div(older.abs(), recent.abs().replace(0, np.nan))


def mex_018_cum_loss_21d_ewm_ratio(close: pd.Series) -> pd.Series:
    """EMA-10 of daily down-rets divided by EMA-42 (short vs long loss pace)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    e10 = _ewm_mean(dn, 10)
    e42 = _ewm_mean(dn, 42)
    return _safe_div(e10, e42)


def mex_019_loss_acceleration_5d_diff_of_sum5(close: pd.Series) -> pd.Series:
    """5-day change in 5-day cumulative loss (negative-to-less-negative = exhaustion)."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum5 = _rolling_sum(dn, _TD_WEEK)
    return sum5.diff(_TD_WEEK)


def mex_020_loss_acceleration_21d_diff_of_sum21(close: pd.Series) -> pd.Series:
    """21-day change in 21-day cumulative loss."""
    r = _log_ret(close)
    dn = r.where(r < 0, 0.0)
    sum21 = _rolling_sum(dn, _TD_MON)
    return sum21.diff(_TD_MON)


# --- Group C (021-030): New-low increment shrinkage ---

def mex_021_new_low_increment_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day avg new-low increment to 21-day avg: <1 = smaller drops."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    increment = (rl_min - close).clip(lower=0.0)
    m5 = _rolling_mean(increment, _TD_WEEK)
    m21 = _rolling_mean(increment, _TD_MON)
    return _safe_div(m5, m21)


def mex_022_new_low_increment_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day avg new-low increment to 63-day avg."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    increment = (rl_min - close).clip(lower=0.0)
    m21 = _rolling_mean(increment, _TD_MON)
    m63 = _rolling_mean(increment, _TD_QTR)
    return _safe_div(m21, m63)


def mex_023_new_low_increment_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of new-21d-low increment series over 21 days (negative = shrinking drops)."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    increment = (rl_min - close).clip(lower=0.0)
    return _linslope(increment, _TD_MON)


def mex_024_new_low_52wk_increment_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day avg 52wk-new-low increment to 21-day avg."""
    rl_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).min()
    increment = (rl_min - close).clip(lower=0.0)
    m5 = _rolling_mean(increment, _TD_WEEK)
    m21 = _rolling_mean(increment, _TD_MON)
    return _safe_div(m5, m21)


def mex_025_new_low_52wk_increment_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 52wk-new-low increment over trailing 63 days."""
    rl_min = close.shift(1).rolling(_TD_YEAR, min_periods=_TD_QTR).min()
    increment = (rl_min - close).clip(lower=0.0)
    return _linslope(increment, _TD_QTR)


def mex_026_intraday_low_increment_ratio_5d_vs_21d(low: pd.Series) -> pd.Series:
    """Ratio of 5-day avg lower-low increment (intraday) to 21-day avg."""
    prev_low = low.shift(1)
    drop = (prev_low - low).clip(lower=0.0)
    m5 = _rolling_mean(drop, _TD_WEEK)
    m21 = _rolling_mean(drop, _TD_MON)
    return _safe_div(m5, m21)


def mex_027_intraday_low_increment_slope_21d(low: pd.Series) -> pd.Series:
    """OLS slope of daily lower-low drop size over 21 days."""
    prev_low = low.shift(1)
    drop = (prev_low - low).clip(lower=0.0)
    return _linslope(drop, _TD_MON)


def mex_028_new_low_pct_increment_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5d avg pct new-low increment to 21d avg (magnitude-normalized)."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    pct_inc = _safe_div((rl_min - close).clip(lower=0.0), rl_min.replace(0, np.nan))
    m5 = _rolling_mean(pct_inc, _TD_WEEK)
    m21 = _rolling_mean(pct_inc, _TD_MON)
    return _safe_div(m5, m21)


def mex_029_new_low_count_decay_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Count of new-21d-low days in last 21d vs last 63d (rate of new-low production)."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    is_new_low = (close < rl_min).astype(float)
    cnt21 = _rolling_sum(is_new_low, _TD_MON)
    cnt63 = _rolling_sum(is_new_low, _TD_QTR)
    return _safe_div(cnt21 / _TD_MON, cnt63 / _TD_QTR)


def mex_030_new_low_count_decay_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of new-21d-low count rate in last 5d vs last 21d."""
    rl_min = close.shift(1).rolling(_TD_MON, min_periods=1).min()
    is_new_low = (close < rl_min).astype(float)
    cnt5 = _rolling_sum(is_new_low, _TD_WEEK)
    cnt21 = _rolling_sum(is_new_low, _TD_MON)
    return _safe_div(cnt5 / _TD_WEEK, cnt21 / _TD_MON)


# --- Group D (031-040): Downside velocity (speed of price fall) deceleration ---

def mex_031_price_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day price change divided by 5 (average daily velocity of decline)."""
    return close.diff(_TD_WEEK) / _TD_WEEK


def mex_032_price_velocity_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day decline velocity to 21-day decline velocity."""
    v5 = close.diff(_TD_WEEK) / _TD_WEEK
    v21 = close.diff(_TD_MON) / _TD_MON
    return _safe_div(v5, v21)


def mex_033_price_velocity_ratio_5d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day decline velocity to 63-day decline velocity."""
    v5 = close.diff(_TD_WEEK) / _TD_WEEK
    v63 = close.diff(_TD_QTR) / _TD_QTR
    return _safe_div(v5, v63)


def mex_034_price_velocity_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day velocity series over 21 days (velocity decelerating)."""
    v5 = close.diff(_TD_WEEK) / _TD_WEEK
    return _linslope(v5, _TD_MON)


def mex_035_price_velocity_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day velocity series over 63 days."""
    v5 = close.diff(_TD_WEEK) / _TD_WEEK
    return _linslope(v5, _TD_QTR)


def mex_036_log_velocity_5d(close: pd.Series) -> pd.Series:
    """5-day log-return divided by 5 (log velocity; negative = falling)."""
    return _log_safe(close).diff(_TD_WEEK) / _TD_WEEK


def mex_037_log_velocity_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day log-velocity to 21-day log-velocity."""
    lc = _log_safe(close)
    v5 = lc.diff(_TD_WEEK) / _TD_WEEK
    v21 = lc.diff(_TD_MON) / _TD_MON
    return _safe_div(v5, v21)


def mex_038_log_velocity_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day log-velocity to 63-day log-velocity."""
    lc = _log_safe(close)
    v21 = lc.diff(_TD_MON) / _TD_MON
    v63 = lc.diff(_TD_QTR) / _TD_QTR
    return _safe_div(v21, v63)


def mex_039_velocity_ewm_ratio_10d_vs_42d(close: pd.Series) -> pd.Series:
    """EMA-10 of daily log-return divided by EMA-42 (short vs long velocity)."""
    r = _log_ret(close)
    e10 = _ewm_mean(r, 10)
    e42 = _ewm_mean(r, 42)
    return _safe_div(e10, e42)


def mex_040_velocity_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 5-day log-velocity in trailing 252-day distribution."""
    lc = _log_safe(close)
    v5 = lc.diff(_TD_WEEK) / _TD_WEEK
    return v5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (041-050): Down-move range contraction ---

def mex_041_down_range_ratio_5d_vs_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean high-low range on down days: 5-day vs 21-day ratio."""
    ret = _daily_ret(close)
    rng = (high - low)
    dn_rng = rng.where(ret < 0, np.nan)
    m5 = dn_rng.rolling(_TD_WEEK, min_periods=1).mean()
    m21 = dn_rng.rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(m5, m21)


def mex_042_down_range_ratio_21d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean down-day high-low range: 21-day vs 63-day ratio."""
    ret = _daily_ret(close)
    rng = (high - low)
    dn_rng = rng.where(ret < 0, np.nan)
    m21 = dn_rng.rolling(_TD_MON, min_periods=1).mean()
    m63 = dn_rng.rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(m21, m63)


def mex_043_down_range_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily high-low range on down days over 21 days."""
    ret = _daily_ret(close)
    rng = (high - low)
    dn_rng = rng.where(ret < 0, 0.0)
    return _linslope(dn_rng, _TD_MON)


def mex_044_atr_ratio_5d_vs_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR to 21-day ATR (contracting = exhaustion)."""
    tr = _tr(close, high, low)
    atr5 = _rolling_mean(tr, _TD_WEEK)
    atr21 = _rolling_mean(tr, _TD_MON)
    return _safe_div(atr5, atr21)


def mex_045_atr_ratio_21d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21-day ATR to 63-day ATR."""
    tr = _tr(close, high, low)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    return _safe_div(atr21, atr63)


def mex_046_atr_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily TR over 21 days (negative = range shrinking)."""
    tr = _tr(close, high, low)
    return _linslope(tr, _TD_MON)


def mex_047_atr_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily TR over 63 days."""
    tr = _tr(close, high, low)
    return _linslope(tr, _TD_QTR)


def mex_048_close_to_low_pct_decay_5d_vs_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day avg (close-low)/close to 21-day avg (lower tail = fading selling)."""
    cl_low = _safe_div(close - low, close.replace(0, np.nan))
    m5 = _rolling_mean(cl_low, _TD_WEEK)
    m21 = _rolling_mean(cl_low, _TD_MON)
    return _safe_div(m5, m21)


def mex_049_high_low_spread_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily (high-low) spread over 21 days."""
    spread = high - low
    return _linslope(spread, _TD_MON)


def mex_050_intraday_downside_tail_ratio_5d_vs_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day avg lower shadow (prev_close-low)/prev_close to 21-day avg."""
    prev_c = close.shift(1)
    lower_shadow = (prev_c - low).clip(lower=0.0)
    pct_shadow = _safe_div(lower_shadow, prev_c.replace(0, np.nan))
    m5 = _rolling_mean(pct_shadow, _TD_WEEK)
    m21 = _rolling_mean(pct_shadow, _TD_MON)
    return _safe_div(m5, m21)


# --- Group F (051-060): Down-day return volatility deceleration ---

def mex_051_down_ret_std_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day std of down-returns to 21-day std (volatility contracting)."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    s5 = _rolling_std(abs_dn, _TD_WEEK)
    s21 = _rolling_std(abs_dn, _TD_MON)
    return _safe_div(s5, s21)


def mex_052_down_ret_std_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day std of down-returns to 63-day std."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    s21 = _rolling_std(abs_dn, _TD_MON)
    s63 = _rolling_std(abs_dn, _TD_QTR)
    return _safe_div(s21, s63)


def mex_053_down_ret_std_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day std of down-returns over trailing 21 days."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    s5 = _rolling_std(abs_dn, _TD_WEEK)
    return _linslope(s5, _TD_MON)


def mex_054_all_ret_std_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of total return volatility: 5-day std vs 21-day std."""
    r = _log_ret(close)
    s5 = r.rolling(_TD_WEEK, min_periods=1).std()
    s21 = r.rolling(_TD_MON, min_periods=1).std()
    return _safe_div(s5, s21)


def mex_055_all_ret_std_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day return std to 63-day std."""
    r = _log_ret(close)
    s21 = r.rolling(_TD_MON, min_periods=1).std()
    s63 = r.rolling(_TD_QTR, min_periods=1).std()
    return _safe_div(s21, s63)


def mex_056_all_ret_std_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of rolling 5-day return std over 21 days."""
    r = _log_ret(close)
    s5 = r.rolling(_TD_WEEK, min_periods=2).std()
    return _linslope(s5, _TD_MON)


def mex_057_down_ret_ewmstd_ratio_5_vs_21(close: pd.Series) -> pd.Series:
    """EWM std (span=5) of down-returns divided by EWM std (span=21)."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    es5 = abs_dn.ewm(span=_TD_WEEK, min_periods=2).std()
    es21 = abs_dn.ewm(span=_TD_MON, min_periods=2).std()
    return _safe_div(es5, es21)


def mex_058_down_ret_max_ratio_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Ratio of max down-return in last 5d to max in last 21d (peak-loss shrinking)."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    mx5 = _rolling_max(abs_dn, _TD_WEEK)
    mx21 = _rolling_max(abs_dn, _TD_MON)
    return _safe_div(mx5, mx21)


def mex_059_down_ret_max_ratio_21d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of max down-return in last 21d to max in last 63d."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    mx21 = _rolling_max(abs_dn, _TD_MON)
    mx63 = _rolling_max(abs_dn, _TD_QTR)
    return _safe_div(mx21, mx63)


def mex_060_down_ret_max_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of rolling 5-day max down-return over 63 days."""
    abs_dn = _down_ret_abs(close).fillna(0.0)
    mx5 = _rolling_max(abs_dn, _TD_WEEK)
    return _linslope(mx5, _TD_QTR)


# --- Group G (061-075): ROC oscillator + Kaufman ER + volume/momentum exhaustion ---

def mex_061_roc_5d(close: pd.Series) -> pd.Series:
    """Rate of Change 5-day: (close/close.shift(5)-1)*100; negative = falling."""
    return _roc(close, _TD_WEEK)


def mex_062_roc_10d(close: pd.Series) -> pd.Series:
    """Rate of Change 10-day."""
    return _roc(close, 10)


def mex_063_roc_21d(close: pd.Series) -> pd.Series:
    """Rate of Change 21-day."""
    return _roc(close, _TD_MON)


def mex_064_roc_63d(close: pd.Series) -> pd.Series:
    """Rate of Change 63-day (quarterly)."""
    return _roc(close, _TD_QTR)


def mex_065_roc_126d(close: pd.Series) -> pd.Series:
    """Rate of Change 126-day (semi-annual)."""
    return _roc(close, _TD_HALF)


def mex_066_roc_252d(close: pd.Series) -> pd.Series:
    """Rate of Change 252-day (annual)."""
    return _roc(close, _TD_YEAR)


def mex_067_roc_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day ROC over 21 days: rising toward zero = deceleration of fall."""
    roc5 = _roc(close, _TD_WEEK)
    return _linslope(roc5, _TD_MON)


def mex_068_roc_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day ROC over 63 days: momentum deceleration signal."""
    roc21 = _roc(close, _TD_MON)
    return _linslope(roc21, _TD_QTR)


def mex_069_roc_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 5-day ROC to 21-day ROC (recent vs quarter momentum)."""
    roc5 = _roc(close, _TD_WEEK)
    roc21 = _roc(close, _TD_MON)
    return _safe_div(roc5, roc21.replace(0, np.nan))


def mex_070_roc_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day ROC to 63-day ROC."""
    roc21 = _roc(close, _TD_MON)
    roc63 = _roc(close, _TD_QTR)
    return _safe_div(roc21, roc63.replace(0, np.nan))


def mex_071_roc_5d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day ROC within trailing 63-day distribution."""
    roc5 = _roc(close, _TD_WEEK)
    m = _rolling_mean(roc5, _TD_QTR)
    s = _rolling_std(roc5, _TD_QTR)
    return _safe_div(roc5 - m, s)


def mex_072_roc_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ROC in trailing 252-day distribution."""
    roc21 = _roc(close, _TD_MON)
    return roc21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mex_073_roc_5d_range_position_63d(close: pd.Series) -> pd.Series:
    """Position of 5-day ROC within its 63-day min-max range (0=at min, 1=at max)."""
    roc5 = _roc(close, _TD_WEEK)
    rmin = _rolling_min(roc5, _TD_QTR)
    rmax = _rolling_max(roc5, _TD_QTR)
    return _safe_div(roc5 - rmin, (rmax - rmin).replace(0, np.nan))


def mex_074_kaufman_er_10d(close: pd.Series) -> pd.Series:
    """Kaufman Efficiency Ratio 10-day: low value = choppy/stalling = momentum exhaustion."""
    return _kaufman_er(close, 10)


def mex_075_kaufman_er_21d(close: pd.Series) -> pd.Series:
    """Kaufman Efficiency Ratio 21-day."""
    return _kaufman_er(close, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_EXHAUSTION_REGISTRY_001_075 = {
    "mex_001_down_ret_mag_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_001_down_ret_mag_ratio_5d_vs_21d},
    "mex_002_down_ret_mag_ratio_5d_vs_63d": {"inputs": ["close"], "func": mex_002_down_ret_mag_ratio_5d_vs_63d},
    "mex_003_down_ret_mag_ratio_21d_vs_63d": {"inputs": ["close"], "func": mex_003_down_ret_mag_ratio_21d_vs_63d},
    "mex_004_down_ret_mag_ratio_21d_vs_126d": {"inputs": ["close"], "func": mex_004_down_ret_mag_ratio_21d_vs_126d},
    "mex_005_down_ret_mag_ratio_63d_vs_252d": {"inputs": ["close"], "func": mex_005_down_ret_mag_ratio_63d_vs_252d},
    "mex_006_down_ret_mag_ema5_vs_ema21": {"inputs": ["close"], "func": mex_006_down_ret_mag_ema5_vs_ema21},
    "mex_007_down_ret_mag_ema10_vs_ema63": {"inputs": ["close"], "func": mex_007_down_ret_mag_ema10_vs_ema63},
    "mex_008_down_ret_mag_slope_21d": {"inputs": ["close"], "func": mex_008_down_ret_mag_slope_21d},
    "mex_009_down_ret_mag_slope_63d": {"inputs": ["close"], "func": mex_009_down_ret_mag_slope_63d},
    "mex_010_down_ret_mag_pct_rank_252d": {"inputs": ["close"], "func": mex_010_down_ret_mag_pct_rank_252d},
    "mex_011_cum_loss_5d_vs_prior_5d": {"inputs": ["close"], "func": mex_011_cum_loss_5d_vs_prior_5d},
    "mex_012_cum_loss_21d_vs_prior_21d": {"inputs": ["close"], "func": mex_012_cum_loss_21d_vs_prior_21d},
    "mex_013_cum_loss_5d_vs_63d_avg": {"inputs": ["close"], "func": mex_013_cum_loss_5d_vs_63d_avg},
    "mex_014_cum_loss_decel_index_21d": {"inputs": ["close"], "func": mex_014_cum_loss_decel_index_21d},
    "mex_015_cum_loss_slope_21d": {"inputs": ["close"], "func": mex_015_cum_loss_slope_21d},
    "mex_016_cum_loss_slope_63d": {"inputs": ["close"], "func": mex_016_cum_loss_slope_63d},
    "mex_017_loss_pace_ratio_half_windows_63d": {"inputs": ["close"], "func": mex_017_loss_pace_ratio_half_windows_63d},
    "mex_018_cum_loss_21d_ewm_ratio": {"inputs": ["close"], "func": mex_018_cum_loss_21d_ewm_ratio},
    "mex_019_loss_acceleration_5d_diff_of_sum5": {"inputs": ["close"], "func": mex_019_loss_acceleration_5d_diff_of_sum5},
    "mex_020_loss_acceleration_21d_diff_of_sum21": {"inputs": ["close"], "func": mex_020_loss_acceleration_21d_diff_of_sum21},
    "mex_021_new_low_increment_5d_vs_21d": {"inputs": ["close"], "func": mex_021_new_low_increment_5d_vs_21d},
    "mex_022_new_low_increment_21d_vs_63d": {"inputs": ["close"], "func": mex_022_new_low_increment_21d_vs_63d},
    "mex_023_new_low_increment_slope_21d": {"inputs": ["close"], "func": mex_023_new_low_increment_slope_21d},
    "mex_024_new_low_52wk_increment_5d_vs_21d": {"inputs": ["close"], "func": mex_024_new_low_52wk_increment_5d_vs_21d},
    "mex_025_new_low_52wk_increment_slope_63d": {"inputs": ["close"], "func": mex_025_new_low_52wk_increment_slope_63d},
    "mex_026_intraday_low_increment_ratio_5d_vs_21d": {"inputs": ["low"], "func": mex_026_intraday_low_increment_ratio_5d_vs_21d},
    "mex_027_intraday_low_increment_slope_21d": {"inputs": ["low"], "func": mex_027_intraday_low_increment_slope_21d},
    "mex_028_new_low_pct_increment_5d_vs_21d": {"inputs": ["close"], "func": mex_028_new_low_pct_increment_5d_vs_21d},
    "mex_029_new_low_count_decay_21d_vs_63d": {"inputs": ["close"], "func": mex_029_new_low_count_decay_21d_vs_63d},
    "mex_030_new_low_count_decay_5d_vs_21d": {"inputs": ["close"], "func": mex_030_new_low_count_decay_5d_vs_21d},
    "mex_031_price_velocity_5d": {"inputs": ["close"], "func": mex_031_price_velocity_5d},
    "mex_032_price_velocity_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_032_price_velocity_ratio_5d_vs_21d},
    "mex_033_price_velocity_ratio_5d_vs_63d": {"inputs": ["close"], "func": mex_033_price_velocity_ratio_5d_vs_63d},
    "mex_034_price_velocity_slope_21d": {"inputs": ["close"], "func": mex_034_price_velocity_slope_21d},
    "mex_035_price_velocity_slope_63d": {"inputs": ["close"], "func": mex_035_price_velocity_slope_63d},
    "mex_036_log_velocity_5d": {"inputs": ["close"], "func": mex_036_log_velocity_5d},
    "mex_037_log_velocity_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_037_log_velocity_ratio_5d_vs_21d},
    "mex_038_log_velocity_ratio_21d_vs_63d": {"inputs": ["close"], "func": mex_038_log_velocity_ratio_21d_vs_63d},
    "mex_039_velocity_ewm_ratio_10d_vs_42d": {"inputs": ["close"], "func": mex_039_velocity_ewm_ratio_10d_vs_42d},
    "mex_040_velocity_pct_rank_252d": {"inputs": ["close"], "func": mex_040_velocity_pct_rank_252d},
    "mex_041_down_range_ratio_5d_vs_21d": {"inputs": ["close", "high", "low"], "func": mex_041_down_range_ratio_5d_vs_21d},
    "mex_042_down_range_ratio_21d_vs_63d": {"inputs": ["close", "high", "low"], "func": mex_042_down_range_ratio_21d_vs_63d},
    "mex_043_down_range_slope_21d": {"inputs": ["close", "high", "low"], "func": mex_043_down_range_slope_21d},
    "mex_044_atr_ratio_5d_vs_21d": {"inputs": ["close", "high", "low"], "func": mex_044_atr_ratio_5d_vs_21d},
    "mex_045_atr_ratio_21d_vs_63d": {"inputs": ["close", "high", "low"], "func": mex_045_atr_ratio_21d_vs_63d},
    "mex_046_atr_slope_21d": {"inputs": ["close", "high", "low"], "func": mex_046_atr_slope_21d},
    "mex_047_atr_slope_63d": {"inputs": ["close", "high", "low"], "func": mex_047_atr_slope_63d},
    "mex_048_close_to_low_pct_decay_5d_vs_21d": {"inputs": ["close", "low"], "func": mex_048_close_to_low_pct_decay_5d_vs_21d},
    "mex_049_high_low_spread_slope_21d": {"inputs": ["high", "low"], "func": mex_049_high_low_spread_slope_21d},
    "mex_050_intraday_downside_tail_ratio_5d_vs_21d": {"inputs": ["close", "low"], "func": mex_050_intraday_downside_tail_ratio_5d_vs_21d},
    "mex_051_down_ret_std_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_051_down_ret_std_ratio_5d_vs_21d},
    "mex_052_down_ret_std_ratio_21d_vs_63d": {"inputs": ["close"], "func": mex_052_down_ret_std_ratio_21d_vs_63d},
    "mex_053_down_ret_std_slope_21d": {"inputs": ["close"], "func": mex_053_down_ret_std_slope_21d},
    "mex_054_all_ret_std_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_054_all_ret_std_ratio_5d_vs_21d},
    "mex_055_all_ret_std_ratio_21d_vs_63d": {"inputs": ["close"], "func": mex_055_all_ret_std_ratio_21d_vs_63d},
    "mex_056_all_ret_std_slope_21d": {"inputs": ["close"], "func": mex_056_all_ret_std_slope_21d},
    "mex_057_down_ret_ewmstd_ratio_5_vs_21": {"inputs": ["close"], "func": mex_057_down_ret_ewmstd_ratio_5_vs_21},
    "mex_058_down_ret_max_ratio_5d_vs_21d": {"inputs": ["close"], "func": mex_058_down_ret_max_ratio_5d_vs_21d},
    "mex_059_down_ret_max_ratio_21d_vs_63d": {"inputs": ["close"], "func": mex_059_down_ret_max_ratio_21d_vs_63d},
    "mex_060_down_ret_max_slope_63d": {"inputs": ["close"], "func": mex_060_down_ret_max_slope_63d},
    "mex_061_roc_5d": {"inputs": ["close"], "func": mex_061_roc_5d},
    "mex_062_roc_10d": {"inputs": ["close"], "func": mex_062_roc_10d},
    "mex_063_roc_21d": {"inputs": ["close"], "func": mex_063_roc_21d},
    "mex_064_roc_63d": {"inputs": ["close"], "func": mex_064_roc_63d},
    "mex_065_roc_126d": {"inputs": ["close"], "func": mex_065_roc_126d},
    "mex_066_roc_252d": {"inputs": ["close"], "func": mex_066_roc_252d},
    "mex_067_roc_5d_slope_21d": {"inputs": ["close"], "func": mex_067_roc_5d_slope_21d},
    "mex_068_roc_21d_slope_63d": {"inputs": ["close"], "func": mex_068_roc_21d_slope_63d},
    "mex_069_roc_5d_vs_21d_ratio": {"inputs": ["close"], "func": mex_069_roc_5d_vs_21d_ratio},
    "mex_070_roc_21d_vs_63d_ratio": {"inputs": ["close"], "func": mex_070_roc_21d_vs_63d_ratio},
    "mex_071_roc_5d_zscore_63d": {"inputs": ["close"], "func": mex_071_roc_5d_zscore_63d},
    "mex_072_roc_21d_pct_rank_252d": {"inputs": ["close"], "func": mex_072_roc_21d_pct_rank_252d},
    "mex_073_roc_5d_range_position_63d": {"inputs": ["close"], "func": mex_073_roc_5d_range_position_63d},
    "mex_074_kaufman_er_10d": {"inputs": ["close"], "func": mex_074_kaufman_er_10d},
    "mex_075_kaufman_er_21d": {"inputs": ["close"], "func": mex_075_kaufman_er_21d},
}
