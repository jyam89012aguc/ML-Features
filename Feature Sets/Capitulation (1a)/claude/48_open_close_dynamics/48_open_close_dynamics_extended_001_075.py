"""
48_open_close_dynamics — Extended Features 001-075
Domain: open-to-close vs close-to-open session return decomposition — extended variants
        covering new window sizes, cumulative session paths, intraday/overnight return
        ratios and correlations, weak-open / weak-close streaks, percentile ranks,
        z-scores over additional horizons, regime flags, and volume-session interactions.
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


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _rolling_max_streak(cond: pd.Series, w: int) -> pd.Series:
    """Maximum consecutive-True run length over trailing w periods."""
    def _max_run(arr):
        mx = 0
        cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(w, min_periods=max(1, w // 2)).apply(_max_run, raw=True)


def _intraday_ret(open: pd.Series, close: pd.Series) -> pd.Series:
    """Log return from open to close (intraday session)."""
    return _log_safe(close) - _log_safe(open)


def _overnight_ret(close: pd.Series, open: pd.Series) -> pd.Series:
    """Log return from prior close to today's open (overnight session)."""
    return _log_safe(open) - _log_safe(close.shift(1))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (normalized by period length)."""
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

# --- Group A (001-010): New intraday-return window variants ---

def ocd_ext_001_intraday_ret_ewm63(open: pd.Series, close: pd.Series) -> pd.Series:
    """63-day EWM of intraday log return (quarterly smoothed intraday drift)."""
    return _ewm_mean(_intraday_ret(open, close), _TD_QTR)


def ocd_ext_002_overnight_ret_ewm63(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day EWM of overnight log return (quarterly smoothed overnight drift)."""
    return _ewm_mean(_overnight_ret(close, open), _TD_QTR)


def ocd_ext_003_intraday_ret_zscore_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday return vs trailing 21-day distribution."""
    r = _intraday_ret(open, close)
    return _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))


def ocd_ext_004_overnight_ret_zscore_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight return vs trailing 21-day distribution."""
    r = _overnight_ret(close, open)
    return _safe_div(r - _rolling_mean(r, _TD_MON), _rolling_std(r, _TD_MON))


def ocd_ext_005_intraday_ret_zscore_126d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of intraday return vs trailing 126-day (half-year) distribution."""
    r = _intraday_ret(open, close)
    return _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))


def ocd_ext_006_overnight_ret_zscore_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of overnight return vs trailing 126-day distribution."""
    r = _overnight_ret(close, open)
    return _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))


def ocd_ext_007_intraday_ret_pct_rank_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of intraday return in trailing 21-day window."""
    r = _intraday_ret(open, close)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def ocd_ext_008_overnight_ret_pct_rank_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of overnight return in trailing 21-day window."""
    r = _overnight_ret(close, open)
    return r.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def ocd_ext_009_intraday_ret_pct_rank_126d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of intraday return in trailing 126-day window."""
    r = _intraday_ret(open, close)
    return r.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def ocd_ext_010_overnight_ret_pct_rank_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank of overnight return in trailing 126-day window."""
    r = _overnight_ret(close, open)
    return r.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


# --- Group B (011-020): Expanding percentile ranks and z-scores ---

def ocd_ext_011_intraday_ret_expanding_zscore(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history z-score of intraday log return."""
    r = _intraday_ret(open, close)
    m = r.expanding(min_periods=5).mean()
    s = r.expanding(min_periods=5).std()
    return _safe_div(r - m, s)


def ocd_ext_012_overnight_ret_expanding_zscore(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-history z-score of overnight log return."""
    r = _overnight_ret(close, open)
    m = r.expanding(min_periods=5).mean()
    s = r.expanding(min_periods=5).std()
    return _safe_div(r - m, s)


def ocd_ext_013_intraday_ret_expanding_pct_rank(open: pd.Series, close: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of intraday log return."""
    r = _intraday_ret(open, close)
    return r.expanding(min_periods=5).rank(pct=True)


def ocd_ext_014_overnight_ret_expanding_pct_rank(close: pd.Series, open: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of overnight log return."""
    r = _overnight_ret(close, open)
    return r.expanding(min_periods=5).rank(pct=True)


def ocd_ext_015_intraday_mean_126d_zscore_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of 126-day mean intraday return within 252-day distribution."""
    r = _intraday_ret(open, close)
    mean126 = _rolling_mean(r, _TD_HALF)
    return _safe_div(mean126 - _rolling_mean(mean126, _TD_YEAR),
                     _rolling_std(mean126, _TD_YEAR))


def ocd_ext_016_overnight_mean_126d_zscore_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of 126-day mean overnight return within 252-day distribution."""
    r = _overnight_ret(close, open)
    mean126 = _rolling_mean(r, _TD_HALF)
    return _safe_div(mean126 - _rolling_mean(mean126, _TD_YEAR),
                     _rolling_std(mean126, _TD_YEAR))


def ocd_ext_017_intraday_vol_126d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 126-day (half-year) standard deviation of intraday returns."""
    return _rolling_std(_intraday_ret(open, close), _TD_HALF)


def ocd_ext_018_overnight_vol_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 126-day standard deviation of overnight returns."""
    return _rolling_std(_overnight_ret(close, open), _TD_HALF)


def ocd_ext_019_intraday_vol_252d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 252-day (annual) standard deviation of intraday returns."""
    return _rolling_std(_intraday_ret(open, close), _TD_YEAR)


def ocd_ext_020_overnight_vol_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 252-day standard deviation of overnight returns."""
    return _rolling_std(_overnight_ret(close, open), _TD_YEAR)


# --- Group C (021-030): Intraday/overnight ratio and spread — new windows ---

def ocd_ext_021_intraday_vs_overnight_vol_ratio_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of intraday std to overnight std over trailing 126 days."""
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_HALF)
    over_std = _rolling_std(_overnight_ret(close, open), _TD_HALF)
    return _safe_div(intra_std, over_std + _EPS)


def ocd_ext_022_overnight_vs_intraday_vol_ratio_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of overnight std to intraday std over trailing 252 days."""
    over_std = _rolling_std(_overnight_ret(close, open), _TD_YEAR)
    intra_std = _rolling_std(_intraday_ret(open, close), _TD_YEAR)
    return _safe_div(over_std, intra_std + _EPS)


def ocd_ext_023_session_mean_diff_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day mean intraday return minus 63-day mean overnight return."""
    intra_mean = _rolling_mean(_intraday_ret(open, close), _TD_QTR)
    over_mean = _rolling_mean(_overnight_ret(close, open), _TD_QTR)
    return intra_mean - over_mean


def ocd_ext_024_session_mean_diff_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """126-day mean intraday minus 126-day mean overnight (half-year drift divergence)."""
    intra_mean = _rolling_mean(_intraday_ret(open, close), _TD_HALF)
    over_mean = _rolling_mean(_overnight_ret(close, open), _TD_HALF)
    return intra_mean - over_mean


def ocd_ext_025_intraday_overnight_corr_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 126-day correlation between intraday and overnight returns."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return intra.rolling(_TD_HALF, min_periods=max(5, _TD_HALF // 2)).corr(over)


def ocd_ext_026_intraday_overnight_corr_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 252-day correlation between intraday and overnight returns."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return intra.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).corr(over)


def ocd_ext_027_intraday_loss_fraction_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 days where intraday return was negative."""
    r = _intraday_ret(open, close)
    return _rolling_count_true(r < 0, _TD_QTR) / _TD_QTR


def ocd_ext_028_overnight_loss_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days where overnight return was negative."""
    r = _overnight_ret(close, open)
    return _rolling_count_true(r < 0, _TD_QTR) / _TD_QTR


def ocd_ext_029_both_sessions_negative_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days where both intraday and overnight sessions were negative."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    return _rolling_count_true((intra < 0) & (over < 0), _TD_QTR) / _TD_QTR


def ocd_ext_030_session_sign_agreement_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days where intraday and overnight sessions had same sign."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    same_sign = np.sign(intra) == np.sign(over)
    return _rolling_count_true(same_sign, _TD_QTR) / _TD_QTR


# --- Group D (031-040): Weak-open and weak-close streak metrics ---

def ocd_ext_031_weak_open_flag(open: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 if open is below previous close (gap-down open = weak open)."""
    return (open < close.shift(1)).astype(float)


def ocd_ext_032_weak_open_fraction_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 21 days with a weak open (open < prior close)."""
    flag = (open < close.shift(1)).astype(float)
    return _rolling_count_true(flag.astype(bool), _TD_MON) / _TD_MON


def ocd_ext_033_weak_open_fraction_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of last 63 days with a weak open (open < prior close)."""
    flag = (open < close.shift(1)).astype(float)
    return _rolling_count_true(flag.astype(bool), _TD_QTR) / _TD_QTR


def ocd_ext_034_consec_weak_opens(open: pd.Series, close: pd.Series) -> pd.Series:
    """Current consecutive days with weak open (gap-down opens)."""
    return _consec_streak(open < close.shift(1))


def ocd_ext_035_max_weak_open_streak_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Maximum consecutive weak-open streak in trailing 63 days."""
    return _rolling_max_streak(open < close.shift(1), _TD_QTR)


def ocd_ext_036_weak_close_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if close is below open and below prior close (doubly weak close)."""
    return ((close < open) & (close < close.shift(1))).astype(float)


def ocd_ext_037_weak_close_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days with doubly weak close (below open AND prior close)."""
    cond = (close < open) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_MON) / _TD_MON


def ocd_ext_038_weak_close_fraction_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days with doubly weak close."""
    cond = (close < open) & (close < close.shift(1))
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def ocd_ext_039_consec_weak_closes(close: pd.Series, open: pd.Series) -> pd.Series:
    """Current consecutive days with doubly weak close."""
    return _consec_streak((close < open) & (close < close.shift(1)))


def ocd_ext_040_weak_open_and_close_fraction_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days with both weak open AND weak close (full bearish structure)."""
    weak_open = open < close.shift(1)
    weak_close = close < open
    return _rolling_count_true(weak_open & weak_close, _TD_MON) / _TD_MON


# --- Group E (041-050): Cumulative intraday vs overnight return paths ---

def ocd_ext_041_cum_intraday_ret_126d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative sum of intraday log returns over trailing 126 days."""
    return _rolling_sum(_intraday_ret(open, close), _TD_HALF)


def ocd_ext_042_cum_overnight_ret_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative sum of overnight log returns over trailing 126 days."""
    return _rolling_sum(_overnight_ret(close, open), _TD_HALF)


def ocd_ext_043_intraday_minus_overnight_cum_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """126-day cumulative intraday minus cumulative overnight (half-year session imbalance)."""
    return _rolling_sum(_intraday_ret(open, close), _TD_HALF) - _rolling_sum(_overnight_ret(close, open), _TD_HALF)


def ocd_ext_044_intraday_fraction_of_cum_loss_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday loss share of total 21-day cumulative loss (intraday vs overnight loss attribution)."""
    intra_loss = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    over_loss = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    total_loss = intra_loss + over_loss
    return _safe_div(intra_loss, total_loss - _EPS)


def ocd_ext_045_overnight_fraction_of_cum_loss_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight loss share of total 21-day cumulative loss."""
    intra_loss = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_MON)
    over_loss = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_MON)
    total_loss = intra_loss + over_loss
    return _safe_div(over_loss, total_loss - _EPS)


def ocd_ext_046_intraday_fraction_of_cum_loss_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Intraday loss share of total 63-day cumulative loss."""
    intra_loss = _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_QTR)
    over_loss = _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_QTR)
    total_loss = intra_loss + over_loss
    return _safe_div(intra_loss, total_loss - _EPS)


def ocd_ext_047_intraday_gain_vs_total_gain_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21-day cumulative gain attributable to intraday session."""
    intra_gain = _rolling_sum(_intraday_ret(open, close).clip(lower=0.0), _TD_MON)
    over_gain = _rolling_sum(_overnight_ret(close, open).clip(lower=0.0), _TD_MON)
    total_gain = intra_gain + over_gain
    return _safe_div(intra_gain, total_gain + _EPS)


def ocd_ext_048_overnight_gain_vs_total_gain_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21-day cumulative gain attributable to overnight session."""
    intra_gain = _rolling_sum(_intraday_ret(open, close).clip(lower=0.0), _TD_MON)
    over_gain = _rolling_sum(_overnight_ret(close, open).clip(lower=0.0), _TD_MON)
    total_gain = intra_gain + over_gain
    return _safe_div(over_gain, total_gain + _EPS)


def ocd_ext_049_cum_intraday_loss_126d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Cumulative sum of intraday losses only over trailing 126 days."""
    return _rolling_sum(_intraday_ret(open, close).clip(upper=0.0), _TD_HALF)


def ocd_ext_050_cum_overnight_loss_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative sum of overnight losses only over trailing 126 days."""
    return _rolling_sum(_overnight_ret(close, open).clip(upper=0.0), _TD_HALF)


# --- Group F (051-060): Regime flags and structural distress signals ---

def ocd_ext_051_intraday_bear_regime_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Binary: 1 if intraday return has been negative for at least 14 of last 21 days."""
    r = _intraday_ret(open, close)
    return (_rolling_count_true(r < 0, _TD_MON) >= 14).astype(float)


def ocd_ext_052_overnight_bear_regime_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if overnight return has been negative for at least 14 of last 21 days."""
    r = _overnight_ret(close, open)
    return (_rolling_count_true(r < 0, _TD_MON) >= 14).astype(float)


def ocd_ext_053_dual_session_bear_regime_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Binary: 1 if both intraday AND overnight bear regimes are active simultaneously."""
    intra_bear = (_rolling_count_true(_intraday_ret(open, close) < 0, _TD_MON) >= 14)
    over_bear = (_rolling_count_true(_overnight_ret(close, open) < 0, _TD_MON) >= 14)
    return (intra_bear & over_bear).astype(float)


def ocd_ext_054_open_is_high_fraction_63d(open: pd.Series, high: pd.Series) -> pd.Series:
    """Fraction of last 63 days where open was the high (structural bearish)."""
    return _rolling_count_true(open >= high, _TD_QTR) / _TD_QTR


def ocd_ext_055_close_is_low_fraction_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 63 days where close was the low (selling-into-close frequency)."""
    return _rolling_count_true(close <= low, _TD_QTR) / _TD_QTR


def ocd_ext_056_consec_open_is_high(open: pd.Series, high: pd.Series) -> pd.Series:
    """Current consecutive days where open equals the daily high."""
    return _consec_streak(open >= high)


def ocd_ext_057_consec_close_is_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive days where close equals the daily low."""
    return _consec_streak(close <= low)


def ocd_ext_058_max_open_is_high_streak_21d(open: pd.Series, high: pd.Series) -> pd.Series:
    """Maximum consecutive open=high streak in trailing 21 days."""
    return _rolling_max_streak(open >= high, _TD_MON)


def ocd_ext_059_max_close_is_low_streak_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum consecutive close=low streak in trailing 21 days."""
    return _rolling_max_streak(close <= low, _TD_MON)


def ocd_ext_060_full_bearish_day_fraction_126d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 126 days with a fully bearish candle (open=high, close=low)."""
    flag = ((open >= high) & (close <= low)).astype(float)
    return _rolling_sum(flag, _TD_HALF) / _TD_HALF


# --- Group G (061-070): Median-based and skew measures ---

def ocd_ext_061_intraday_ret_median_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day median of intraday log returns."""
    return _rolling_median(_intraday_ret(open, close), _TD_MON)


def ocd_ext_062_overnight_ret_median_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day median of overnight log returns."""
    return _rolling_median(_overnight_ret(close, open), _TD_MON)


def ocd_ext_063_intraday_ret_median_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63-day median of intraday log returns."""
    return _rolling_median(_intraday_ret(open, close), _TD_QTR)


def ocd_ext_064_overnight_ret_median_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day median of overnight log returns."""
    return _rolling_median(_overnight_ret(close, open), _TD_QTR)


def ocd_ext_065_intraday_mean_minus_median_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday return mean minus median over 21 days (skew proxy — negative = left-skewed)."""
    r = _intraday_ret(open, close)
    return _rolling_mean(r, _TD_MON) - _rolling_median(r, _TD_MON)


def ocd_ext_066_overnight_mean_minus_median_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Overnight return mean minus median over 21 days (skew proxy)."""
    r = _overnight_ret(close, open)
    return _rolling_mean(r, _TD_MON) - _rolling_median(r, _TD_MON)


def ocd_ext_067_intraday_negative_vol_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 21-day std of intraday returns on loss days only (downside volatility)."""
    r = _intraday_ret(open, close)
    loss_r = r.where(r < 0, np.nan)
    return loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()


def ocd_ext_068_overnight_negative_vol_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 21-day std of overnight returns on loss days only (downside overnight vol)."""
    r = _overnight_ret(close, open)
    loss_r = r.where(r < 0, np.nan)
    return loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()


def ocd_ext_069_intraday_sortino_proxy_21d(open: pd.Series, close: pd.Series) -> pd.Series:
    """21-day Sortino-style ratio: intraday mean return / downside vol (intraday)."""
    r = _intraday_ret(open, close)
    mean_r = _rolling_mean(r, _TD_MON)
    loss_r = r.where(r < 0, np.nan)
    down_std = loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    return _safe_div(mean_r, down_std + _EPS)


def ocd_ext_070_overnight_sortino_proxy_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day Sortino-style ratio: overnight mean return / downside overnight vol."""
    r = _overnight_ret(close, open)
    mean_r = _rolling_mean(r, _TD_MON)
    loss_r = r.where(r < 0, np.nan)
    down_std = loss_r.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).std()
    return _safe_div(mean_r, down_std + _EPS)


# --- Group H (071-075): Volume-session extended interactions ---

def ocd_ext_071_vol_weighted_intraday_ret_126d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean intraday return over 126 days."""
    r = _intraday_ret(open, close)
    return _safe_div(_rolling_sum(r * volume, _TD_HALF), _rolling_sum(volume, _TD_HALF))


def ocd_ext_072_vol_weighted_overnight_ret_126d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted mean overnight return over 126 days."""
    r = _overnight_ret(close, open)
    return _safe_div(_rolling_sum(r * volume, _TD_HALF), _rolling_sum(volume, _TD_HALF))


def ocd_ext_073_intraday_loss_days_vol_fraction_63d(open: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63-day volume that traded on intraday-loss days."""
    r = _intraday_ret(open, close)
    loss_vol = _rolling_sum(volume.where(r < 0, 0.0), _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(loss_vol, total_vol + _EPS)


def ocd_ext_074_overnight_loss_days_vol_fraction_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 63-day volume that traded on overnight-loss days."""
    r = _overnight_ret(close, open)
    loss_vol = _rolling_sum(volume.where(r < 0, 0.0), _TD_QTR)
    total_vol = _rolling_sum(volume, _TD_QTR)
    return _safe_div(loss_vol, total_vol + _EPS)


def ocd_ext_075_capitulation_session_composite(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation composite: normalized combination of dual-session loss frequency,
    intraday loss fraction expanding z-score, and volume-on-loss-days fraction.
    Higher = more extreme distress signature."""
    intra = _intraday_ret(open, close)
    over = _overnight_ret(close, open)
    dual_frac = _rolling_count_true((intra < 0) & (over < 0), _TD_QTR) / _TD_QTR
    df_z = _safe_div(dual_frac - dual_frac.expanding(min_periods=10).mean(),
                     dual_frac.expanding(min_periods=10).std())
    loss_vol = _rolling_sum(volume.where(intra < 0, 0.0), _TD_MON)
    total_vol = _rolling_sum(volume, _TD_MON)
    loss_vol_frac = _safe_div(loss_vol, total_vol + _EPS)
    intra_frac = _rolling_count_true(intra < 0, _TD_MON) / _TD_MON
    return df_z.fillna(0.0) + loss_vol_frac + intra_frac


# ── Registry ──────────────────────────────────────────────────────────────────

OPEN_CLOSE_DYNAMICS_EXTENDED_REGISTRY_001_075 = {
    "ocd_ext_001_intraday_ret_ewm63": {"inputs": ["open", "close"], "func": ocd_ext_001_intraday_ret_ewm63},
    "ocd_ext_002_overnight_ret_ewm63": {"inputs": ["close", "open"], "func": ocd_ext_002_overnight_ret_ewm63},
    "ocd_ext_003_intraday_ret_zscore_21d": {"inputs": ["open", "close"], "func": ocd_ext_003_intraday_ret_zscore_21d},
    "ocd_ext_004_overnight_ret_zscore_21d": {"inputs": ["close", "open"], "func": ocd_ext_004_overnight_ret_zscore_21d},
    "ocd_ext_005_intraday_ret_zscore_126d": {"inputs": ["open", "close"], "func": ocd_ext_005_intraday_ret_zscore_126d},
    "ocd_ext_006_overnight_ret_zscore_126d": {"inputs": ["close", "open"], "func": ocd_ext_006_overnight_ret_zscore_126d},
    "ocd_ext_007_intraday_ret_pct_rank_21d": {"inputs": ["open", "close"], "func": ocd_ext_007_intraday_ret_pct_rank_21d},
    "ocd_ext_008_overnight_ret_pct_rank_21d": {"inputs": ["close", "open"], "func": ocd_ext_008_overnight_ret_pct_rank_21d},
    "ocd_ext_009_intraday_ret_pct_rank_126d": {"inputs": ["open", "close"], "func": ocd_ext_009_intraday_ret_pct_rank_126d},
    "ocd_ext_010_overnight_ret_pct_rank_126d": {"inputs": ["close", "open"], "func": ocd_ext_010_overnight_ret_pct_rank_126d},
    "ocd_ext_011_intraday_ret_expanding_zscore": {"inputs": ["open", "close"], "func": ocd_ext_011_intraday_ret_expanding_zscore},
    "ocd_ext_012_overnight_ret_expanding_zscore": {"inputs": ["close", "open"], "func": ocd_ext_012_overnight_ret_expanding_zscore},
    "ocd_ext_013_intraday_ret_expanding_pct_rank": {"inputs": ["open", "close"], "func": ocd_ext_013_intraday_ret_expanding_pct_rank},
    "ocd_ext_014_overnight_ret_expanding_pct_rank": {"inputs": ["close", "open"], "func": ocd_ext_014_overnight_ret_expanding_pct_rank},
    "ocd_ext_015_intraday_mean_126d_zscore_252d": {"inputs": ["open", "close"], "func": ocd_ext_015_intraday_mean_126d_zscore_252d},
    "ocd_ext_016_overnight_mean_126d_zscore_252d": {"inputs": ["close", "open"], "func": ocd_ext_016_overnight_mean_126d_zscore_252d},
    "ocd_ext_017_intraday_vol_126d": {"inputs": ["open", "close"], "func": ocd_ext_017_intraday_vol_126d},
    "ocd_ext_018_overnight_vol_126d": {"inputs": ["close", "open"], "func": ocd_ext_018_overnight_vol_126d},
    "ocd_ext_019_intraday_vol_252d": {"inputs": ["open", "close"], "func": ocd_ext_019_intraday_vol_252d},
    "ocd_ext_020_overnight_vol_252d": {"inputs": ["close", "open"], "func": ocd_ext_020_overnight_vol_252d},
    "ocd_ext_021_intraday_vs_overnight_vol_ratio_126d": {"inputs": ["close", "open"], "func": ocd_ext_021_intraday_vs_overnight_vol_ratio_126d},
    "ocd_ext_022_overnight_vs_intraday_vol_ratio_252d": {"inputs": ["close", "open"], "func": ocd_ext_022_overnight_vs_intraday_vol_ratio_252d},
    "ocd_ext_023_session_mean_diff_63d": {"inputs": ["close", "open"], "func": ocd_ext_023_session_mean_diff_63d},
    "ocd_ext_024_session_mean_diff_126d": {"inputs": ["close", "open"], "func": ocd_ext_024_session_mean_diff_126d},
    "ocd_ext_025_intraday_overnight_corr_126d": {"inputs": ["close", "open"], "func": ocd_ext_025_intraday_overnight_corr_126d},
    "ocd_ext_026_intraday_overnight_corr_252d": {"inputs": ["close", "open"], "func": ocd_ext_026_intraday_overnight_corr_252d},
    "ocd_ext_027_intraday_loss_fraction_63d": {"inputs": ["open", "close"], "func": ocd_ext_027_intraday_loss_fraction_63d},
    "ocd_ext_028_overnight_loss_fraction_63d": {"inputs": ["close", "open"], "func": ocd_ext_028_overnight_loss_fraction_63d},
    "ocd_ext_029_both_sessions_negative_fraction_63d": {"inputs": ["close", "open"], "func": ocd_ext_029_both_sessions_negative_fraction_63d},
    "ocd_ext_030_session_sign_agreement_fraction_63d": {"inputs": ["close", "open"], "func": ocd_ext_030_session_sign_agreement_fraction_63d},
    "ocd_ext_031_weak_open_flag": {"inputs": ["open", "close"], "func": ocd_ext_031_weak_open_flag},
    "ocd_ext_032_weak_open_fraction_21d": {"inputs": ["open", "close"], "func": ocd_ext_032_weak_open_fraction_21d},
    "ocd_ext_033_weak_open_fraction_63d": {"inputs": ["open", "close"], "func": ocd_ext_033_weak_open_fraction_63d},
    "ocd_ext_034_consec_weak_opens": {"inputs": ["open", "close"], "func": ocd_ext_034_consec_weak_opens},
    "ocd_ext_035_max_weak_open_streak_63d": {"inputs": ["open", "close"], "func": ocd_ext_035_max_weak_open_streak_63d},
    "ocd_ext_036_weak_close_flag": {"inputs": ["close", "open"], "func": ocd_ext_036_weak_close_flag},
    "ocd_ext_037_weak_close_fraction_21d": {"inputs": ["close", "open"], "func": ocd_ext_037_weak_close_fraction_21d},
    "ocd_ext_038_weak_close_fraction_63d": {"inputs": ["close", "open"], "func": ocd_ext_038_weak_close_fraction_63d},
    "ocd_ext_039_consec_weak_closes": {"inputs": ["close", "open"], "func": ocd_ext_039_consec_weak_closes},
    "ocd_ext_040_weak_open_and_close_fraction_21d": {"inputs": ["close", "open"], "func": ocd_ext_040_weak_open_and_close_fraction_21d},
    "ocd_ext_041_cum_intraday_ret_126d": {"inputs": ["open", "close"], "func": ocd_ext_041_cum_intraday_ret_126d},
    "ocd_ext_042_cum_overnight_ret_126d": {"inputs": ["close", "open"], "func": ocd_ext_042_cum_overnight_ret_126d},
    "ocd_ext_043_intraday_minus_overnight_cum_126d": {"inputs": ["close", "open"], "func": ocd_ext_043_intraday_minus_overnight_cum_126d},
    "ocd_ext_044_intraday_fraction_of_cum_loss_21d": {"inputs": ["close", "open"], "func": ocd_ext_044_intraday_fraction_of_cum_loss_21d},
    "ocd_ext_045_overnight_fraction_of_cum_loss_21d": {"inputs": ["close", "open"], "func": ocd_ext_045_overnight_fraction_of_cum_loss_21d},
    "ocd_ext_046_intraday_fraction_of_cum_loss_63d": {"inputs": ["close", "open"], "func": ocd_ext_046_intraday_fraction_of_cum_loss_63d},
    "ocd_ext_047_intraday_gain_vs_total_gain_21d": {"inputs": ["close", "open"], "func": ocd_ext_047_intraday_gain_vs_total_gain_21d},
    "ocd_ext_048_overnight_gain_vs_total_gain_21d": {"inputs": ["close", "open"], "func": ocd_ext_048_overnight_gain_vs_total_gain_21d},
    "ocd_ext_049_cum_intraday_loss_126d": {"inputs": ["open", "close"], "func": ocd_ext_049_cum_intraday_loss_126d},
    "ocd_ext_050_cum_overnight_loss_126d": {"inputs": ["close", "open"], "func": ocd_ext_050_cum_overnight_loss_126d},
    "ocd_ext_051_intraday_bear_regime_21d": {"inputs": ["open", "close"], "func": ocd_ext_051_intraday_bear_regime_21d},
    "ocd_ext_052_overnight_bear_regime_21d": {"inputs": ["close", "open"], "func": ocd_ext_052_overnight_bear_regime_21d},
    "ocd_ext_053_dual_session_bear_regime_21d": {"inputs": ["close", "open"], "func": ocd_ext_053_dual_session_bear_regime_21d},
    "ocd_ext_054_open_is_high_fraction_63d": {"inputs": ["open", "high"], "func": ocd_ext_054_open_is_high_fraction_63d},
    "ocd_ext_055_close_is_low_fraction_63d": {"inputs": ["close", "low"], "func": ocd_ext_055_close_is_low_fraction_63d},
    "ocd_ext_056_consec_open_is_high": {"inputs": ["open", "high"], "func": ocd_ext_056_consec_open_is_high},
    "ocd_ext_057_consec_close_is_low": {"inputs": ["close", "low"], "func": ocd_ext_057_consec_close_is_low},
    "ocd_ext_058_max_open_is_high_streak_21d": {"inputs": ["open", "high"], "func": ocd_ext_058_max_open_is_high_streak_21d},
    "ocd_ext_059_max_close_is_low_streak_21d": {"inputs": ["close", "low"], "func": ocd_ext_059_max_close_is_low_streak_21d},
    "ocd_ext_060_full_bearish_day_fraction_126d": {"inputs": ["close", "open", "high", "low"], "func": ocd_ext_060_full_bearish_day_fraction_126d},
    "ocd_ext_061_intraday_ret_median_21d": {"inputs": ["open", "close"], "func": ocd_ext_061_intraday_ret_median_21d},
    "ocd_ext_062_overnight_ret_median_21d": {"inputs": ["close", "open"], "func": ocd_ext_062_overnight_ret_median_21d},
    "ocd_ext_063_intraday_ret_median_63d": {"inputs": ["open", "close"], "func": ocd_ext_063_intraday_ret_median_63d},
    "ocd_ext_064_overnight_ret_median_63d": {"inputs": ["close", "open"], "func": ocd_ext_064_overnight_ret_median_63d},
    "ocd_ext_065_intraday_mean_minus_median_21d": {"inputs": ["open", "close"], "func": ocd_ext_065_intraday_mean_minus_median_21d},
    "ocd_ext_066_overnight_mean_minus_median_21d": {"inputs": ["close", "open"], "func": ocd_ext_066_overnight_mean_minus_median_21d},
    "ocd_ext_067_intraday_negative_vol_21d": {"inputs": ["open", "close"], "func": ocd_ext_067_intraday_negative_vol_21d},
    "ocd_ext_068_overnight_negative_vol_21d": {"inputs": ["close", "open"], "func": ocd_ext_068_overnight_negative_vol_21d},
    "ocd_ext_069_intraday_sortino_proxy_21d": {"inputs": ["open", "close"], "func": ocd_ext_069_intraday_sortino_proxy_21d},
    "ocd_ext_070_overnight_sortino_proxy_21d": {"inputs": ["close", "open"], "func": ocd_ext_070_overnight_sortino_proxy_21d},
    "ocd_ext_071_vol_weighted_intraday_ret_126d": {"inputs": ["open", "close", "volume"], "func": ocd_ext_071_vol_weighted_intraday_ret_126d},
    "ocd_ext_072_vol_weighted_overnight_ret_126d": {"inputs": ["close", "open", "volume"], "func": ocd_ext_072_vol_weighted_overnight_ret_126d},
    "ocd_ext_073_intraday_loss_days_vol_fraction_63d": {"inputs": ["open", "close", "volume"], "func": ocd_ext_073_intraday_loss_days_vol_fraction_63d},
    "ocd_ext_074_overnight_loss_days_vol_fraction_63d": {"inputs": ["close", "open", "volume"], "func": ocd_ext_074_overnight_loss_days_vol_fraction_63d},
    "ocd_ext_075_capitulation_session_composite": {"inputs": ["close", "open", "volume"], "func": ocd_ext_075_capitulation_session_composite},
}
