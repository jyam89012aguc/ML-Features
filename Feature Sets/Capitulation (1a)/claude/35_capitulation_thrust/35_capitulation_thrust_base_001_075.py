"""
35_capitulation_thrust — Base Features 001-075
Domain: sharp final-leg-down thrust signatures — violent terminal acceleration of decline
        Steepest N-day collapses, multi-sigma down-moves, thrust magnitude, thrust intensity,
        waterfall/cascade patterns, final-leg slope vs earlier legs, panic-thrust composites.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (backward-looking)."""
    def _slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): Steepest N-day return (minimum rolling return) ---

def cth_001_min_return_5d(close: pd.Series) -> pd.Series:
    """Minimum (most negative) 5-day log-return in trailing 5-day window."""
    lr = _log_ret(close)
    return _rolling_min(lr.rolling(_TD_WEEK, min_periods=1).sum(), _TD_WEEK)


def cth_002_min_return_10d(close: pd.Series) -> pd.Series:
    """Steepest 10-day cumulative log-return within trailing 21-day window."""
    cum10 = _log_safe(close) - _log_safe(close.shift(10))
    return _rolling_min(cum10, _TD_MON)


def cth_003_min_return_21d(close: pd.Series) -> pd.Series:
    """Steepest 21-day cumulative log-return within trailing 63-day window."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return _rolling_min(cum21, _TD_QTR)


def cth_004_min_return_63d(close: pd.Series) -> pd.Series:
    """Steepest 63-day cumulative log-return within trailing 126-day window."""
    cum63 = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    return _rolling_min(cum63, _TD_HALF)


def cth_005_min_return_5d_vs_252d_mean(close: pd.Series) -> pd.Series:
    """Steepest 5-day return standardized by 252-day mean 5-day return."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    mn   = _rolling_mean(cum5, _TD_YEAR)
    return _rolling_min(cum5, _TD_MON) - mn


def cth_006_min_return_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of worst 5-day thrust vs 252-day distribution of 5-day returns."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    mn   = _rolling_mean(cum5, _TD_YEAR)
    sd   = _rolling_std(cum5, _TD_YEAR)
    worst = _rolling_min(cum5, _TD_MON)
    return _safe_div(worst - mn, sd)


def cth_007_min_return_10d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of worst 10-day cumulative return vs 252-day distribution."""
    cum10 = _log_safe(close) - _log_safe(close.shift(10))
    mn    = _rolling_mean(cum10, _TD_YEAR)
    sd    = _rolling_std(cum10, _TD_YEAR)
    worst = _rolling_min(cum10, _TD_MON)
    return _safe_div(worst - mn, sd)


def cth_008_min_return_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of worst 21-day cumulative return vs 252-day distribution."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    mn    = _rolling_mean(cum21, _TD_YEAR)
    sd    = _rolling_std(cum21, _TD_YEAR)
    worst = _rolling_min(cum21, _TD_QTR)
    return _safe_div(worst - mn, sd)


def cth_009_min_return_5d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of worst recent 5-day return in 252-day history."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    worst = _rolling_min(cum5, _TD_MON)
    return worst.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_010_min_return_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of worst recent 21-day return in 252-day history."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    worst = _rolling_min(cum21, _TD_QTR)
    return worst.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): Single-day multi-sigma down-moves ---

def cth_011_single_day_ret_zscore_63d(close: pd.Series) -> pd.Series:
    """Today's 1-day log-return z-scored against trailing 63-day distribution."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_QTR)
    sd = _rolling_std(lr, _TD_QTR)
    return _safe_div(lr - mn, sd)


def cth_012_single_day_ret_zscore_252d(close: pd.Series) -> pd.Series:
    """Today's 1-day log-return z-scored against trailing 252-day distribution."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    return _safe_div(lr - mn, sd)


def cth_013_worst_single_day_21d(close: pd.Series) -> pd.Series:
    """Minimum (worst) single-day log-return in trailing 21 days."""
    lr = _log_ret(close)
    return _rolling_min(lr, _TD_MON)


def cth_014_worst_single_day_63d(close: pd.Series) -> pd.Series:
    """Minimum single-day log-return in trailing 63 days."""
    lr = _log_ret(close)
    return _rolling_min(lr, _TD_QTR)


def cth_015_worst_single_day_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of worst single-day return in trailing 21d vs 63d distribution."""
    lr   = _log_ret(close)
    mn   = _rolling_mean(lr, _TD_QTR)
    sd   = _rolling_std(lr, _TD_QTR)
    worst = _rolling_min(lr, _TD_MON)
    return _safe_div(worst - mn, sd)


def cth_016_days_below_2sigma_21d(close: pd.Series) -> pd.Series:
    """Count of days with 1-day return below 2-sigma threshold in trailing 21 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    threshold = mn - 2.0 * sd
    flag = (lr < threshold).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_017_days_below_3sigma_63d(close: pd.Series) -> pd.Series:
    """Count of days with 1-day return below 3-sigma threshold in trailing 63 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    threshold = mn - 3.0 * sd
    flag = (lr < threshold).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def cth_018_days_below_1p5sigma_21d(close: pd.Series) -> pd.Series:
    """Count of days with return below 1.5-sigma threshold in trailing 21 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    threshold = mn - 1.5 * sd
    flag = (lr < threshold).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_019_max_sigma_hit_21d(close: pd.Series) -> pd.Series:
    """Maximum (most negative) sigma-score of any single day in trailing 21 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    return _rolling_min(z, _TD_MON)


def cth_020_frac_days_below_2sigma_252d(close: pd.Series) -> pd.Series:
    """Fraction of last 252 days with return below 2-sigma (tail-event density)."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    flag = (lr < (mn - 2.0 * sd)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


# --- Group C (021-030): Thrust magnitude — size of the most recent down-leg ---

def cth_021_drawdown_from_recent_peak_21d(close: pd.Series) -> pd.Series:
    """Log-return from 21-day rolling max to today's close (thrust depth)."""
    pk = _rolling_max(close, _TD_MON)
    return _log_safe(close) - _log_safe(pk)


def cth_022_drawdown_from_recent_peak_63d(close: pd.Series) -> pd.Series:
    """Log-return from 63-day rolling max to today's close."""
    pk = _rolling_max(close, _TD_QTR)
    return _log_safe(close) - _log_safe(pk)


def cth_023_drawdown_from_recent_peak_126d(close: pd.Series) -> pd.Series:
    """Log-return from 126-day rolling max to today's close."""
    pk = _rolling_max(close, _TD_HALF)
    return _log_safe(close) - _log_safe(pk)


def cth_024_drawdown_from_recent_peak_252d(close: pd.Series) -> pd.Series:
    """Log-return from 252-day rolling max to today's close."""
    pk = _rolling_max(close, _TD_YEAR)
    return _log_safe(close) - _log_safe(pk)


def cth_025_thrust_last5d_vs_dd21d(close: pd.Series) -> pd.Series:
    """Fraction of 21-day drawdown that occurred in the last 5 days (recency of thrust)."""
    dd21 = cth_021_drawdown_from_recent_peak_21d(close)
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return _safe_div(cum5, dd21.abs())


def cth_026_thrust_last10d_vs_dd63d(close: pd.Series) -> pd.Series:
    """Fraction of 63-day drawdown concentrated in the last 10 days."""
    dd63 = cth_022_drawdown_from_recent_peak_63d(close)
    cum10 = _log_safe(close) - _log_safe(close.shift(10))
    return _safe_div(cum10, dd63.abs())


def cth_027_thrust_magnitude_abs_5d(close: pd.Series) -> pd.Series:
    """Absolute 5-day log-return (magnitude of recent thrust, sign dropped)."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return cum5.clip(upper=0).abs()


def cth_028_thrust_magnitude_abs_21d(close: pd.Series) -> pd.Series:
    """Absolute 21-day log-return clipped to only capture losses."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return cum21.clip(upper=0).abs()


def cth_029_drawdown_21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of today's 21-day drawdown in 252-day history (extremity)."""
    dd = cth_021_drawdown_from_recent_peak_21d(close)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_030_drawdown_63d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of the 63-day drawdown depth."""
    dd = cth_022_drawdown_from_recent_peak_63d(close)
    return dd.expanding(min_periods=_TD_QTR).rank(pct=True)


# --- Group D (031-040): Thrust intensity — cumulative loss per day in sharpest leg ---

def cth_031_thrust_intensity_5d(close: pd.Series) -> pd.Series:
    """5-day cumulative log-loss divided by 5 (avg daily loss intensity in thrust leg)."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return cum5.clip(upper=0) / _TD_WEEK


def cth_032_thrust_intensity_10d(close: pd.Series) -> pd.Series:
    """10-day cumulative log-loss per day (avg intensity of 10-day thrust leg)."""
    cum10 = _log_safe(close) - _log_safe(close.shift(10))
    return cum10.clip(upper=0) / 10.0


def cth_033_thrust_intensity_21d(close: pd.Series) -> pd.Series:
    """21-day cumulative log-loss per day."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return cum21.clip(upper=0) / _TD_MON


def cth_034_worst_intensity_5d_in_63d(close: pd.Series) -> pd.Series:
    """Most intense 5-day thrust (min avg daily log-loss) in trailing 63 days."""
    intensity = cth_031_thrust_intensity_5d(close)
    return _rolling_min(intensity, _TD_QTR)


def cth_035_worst_intensity_10d_in_126d(close: pd.Series) -> pd.Series:
    """Most intense 10-day thrust in trailing 126-day window."""
    intensity = cth_032_thrust_intensity_10d(close)
    return _rolling_min(intensity, _TD_HALF)


def cth_036_worst_intensity_21d_in_252d(close: pd.Series) -> pd.Series:
    """Most intense 21-day thrust in trailing 252-day window."""
    intensity = cth_033_thrust_intensity_21d(close)
    return _rolling_min(intensity, _TD_YEAR)


def cth_037_intensity_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 5-day thrust intensity vs 252-day distribution."""
    intensity = cth_031_thrust_intensity_5d(close)
    mn = _rolling_mean(intensity, _TD_YEAR)
    sd = _rolling_std(intensity, _TD_YEAR)
    return _safe_div(intensity - mn, sd)


def cth_038_intensity_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of current 21-day thrust intensity vs 252-day distribution."""
    intensity = cth_033_thrust_intensity_21d(close)
    mn = _rolling_mean(intensity, _TD_YEAR)
    sd = _rolling_std(intensity, _TD_YEAR)
    return _safe_div(intensity - mn, sd)


def cth_039_intensity_vs_hist_max_252d(close: pd.Series) -> pd.Series:
    """Current 5-day intensity as fraction of worst 252-day intensity on record."""
    intensity = cth_031_thrust_intensity_5d(close)
    worst252  = _rolling_min(intensity, _TD_YEAR)
    return _safe_div(intensity, worst252)


def cth_040_intensity_acceleration_5d(close: pd.Series) -> pd.Series:
    """Change in 5-day thrust intensity over last 5 days (intensity acceleration)."""
    intensity = cth_031_thrust_intensity_5d(close)
    return intensity.diff(_TD_WEEK)


# --- Group E (041-050): Waterfall / cascade patterns ---

def cth_041_waterfall_3leg_loss(close: pd.Series) -> pd.Series:
    """Sum of three successive 5-day losses forming a waterfall (legs 1+2+3 ago)."""
    l1 = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))).clip(upper=0)
    l2 = (_log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(2 * _TD_WEEK))).clip(upper=0)
    l3 = (_log_safe(close.shift(2 * _TD_WEEK)) - _log_safe(close.shift(3 * _TD_WEEK))).clip(upper=0)
    return l1 + l2 + l3


def cth_042_waterfall_3leg_each_negative(close: pd.Series) -> pd.Series:
    """Flag: all three successive 5-day legs are negative (cascade)."""
    l1 = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))) < 0
    l2 = (_log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(2 * _TD_WEEK))) < 0
    l3 = (_log_safe(close.shift(2 * _TD_WEEK)) - _log_safe(close.shift(3 * _TD_WEEK))) < 0
    return (l1 & l2 & l3).astype(float)


def cth_043_waterfall_accelerating_loss(close: pd.Series) -> pd.Series:
    """Flag: each successive 5-day leg is worse than the prior (accelerating cascade)."""
    l1 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    l2 = _log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(2 * _TD_WEEK))
    l3 = _log_safe(close.shift(2 * _TD_WEEK)) - _log_safe(close.shift(3 * _TD_WEEK))
    return ((l1 < l2) & (l2 < l3)).astype(float)


def cth_044_cascade_down_days_in_10d(close: pd.Series) -> pd.Series:
    """Number of down-days in rolling 10-day window (cascade density)."""
    lr   = _log_ret(close)
    down = (lr < 0).astype(float)
    return down.rolling(10, min_periods=5).sum()


def cth_045_cascade_loss_ratio_last5_vs_prior10(close: pd.Series) -> pd.Series:
    """Ratio of last-5d loss to prior-10d loss (last leg dominance in waterfall)."""
    last5  = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))).clip(upper=0).abs()
    prior10 = (_log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(_TD_WEEK + 10))).clip(upper=0).abs()
    return _safe_div(last5, prior10 + _EPS)


def cth_046_waterfall_freq_63d(close: pd.Series) -> pd.Series:
    """Count of 3-consecutive-down-5d-leg events in trailing 63 days."""
    flag = cth_042_waterfall_3leg_each_negative(close)
    return _rolling_sum(flag, _TD_QTR)


def cth_047_waterfall_freq_252d(close: pd.Series) -> pd.Series:
    """Count of 3-consecutive-down-5d-leg events in trailing 252 days."""
    flag = cth_042_waterfall_3leg_each_negative(close)
    return _rolling_sum(flag, _TD_YEAR)


def cth_048_gap_cluster_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down opens (open < prior close) in trailing 5 days."""
    gap_down = (open < close.shift(1)).astype(float)
    return _rolling_sum(gap_down, _TD_WEEK)


def cth_049_gap_cluster_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of gap-down opens in trailing 21 days."""
    gap_down = (open < close.shift(1)).astype(float)
    return _rolling_sum(gap_down, _TD_MON)


def cth_050_gap_cluster_magnitude_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Sum of negative gap magnitudes (log) over trailing 5 days."""
    gap = (_log_safe(open) - _log_safe(close.shift(1))).clip(upper=0)
    return _rolling_sum(gap, _TD_WEEK)


# --- Group F (051-060): Final-leg slope vs earlier legs ---

def cth_051_final_leg_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of close over trailing 5 days (steepness of final thrust leg)."""
    return _linslope(close, _TD_WEEK)


def cth_052_final_leg_slope_10d(close: pd.Series) -> pd.Series:
    """OLS slope of close over trailing 10 days."""
    return _linslope(close, 10)


def cth_053_final_leg_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of close over trailing 21 days."""
    return _linslope(close, _TD_MON)


def cth_054_slope_5d_vs_slope_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day slope to 21-day slope (final leg steeper than recent trend)."""
    s5  = _linslope(close, _TD_WEEK)
    s21 = _linslope(close, _TD_MON)
    return _safe_div(s5, s21.abs() + _EPS)


def cth_055_slope_5d_vs_slope_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day slope to 63-day slope (final thrust vs quarterly trend)."""
    s5  = _linslope(close, _TD_WEEK)
    s63 = _linslope(close, _TD_QTR)
    return _safe_div(s5, s63.abs() + _EPS)


def cth_056_log_slope_5d(close: pd.Series) -> pd.Series:
    """OLS slope of log-close over trailing 5 days (relative rate of descent)."""
    return _linslope(_log_safe(close), _TD_WEEK)


def cth_057_log_slope_10d(close: pd.Series) -> pd.Series:
    """OLS slope of log-close over trailing 10 days."""
    return _linslope(_log_safe(close), 10)


def cth_058_log_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of log-close over trailing 21 days."""
    return _linslope(_log_safe(close), _TD_MON)


def cth_059_log_slope_5d_vs_63d(close: pd.Series) -> pd.Series:
    """Ratio of 5-day log-slope to 63-day log-slope (final descent acceleration)."""
    s5  = _linslope(_log_safe(close), _TD_WEEK)
    s63 = _linslope(_log_safe(close), _TD_QTR)
    return _safe_div(s5, s63.abs() + _EPS)


def cth_060_slope_convexity_21d(close: pd.Series) -> pd.Series:
    """Difference of 10-day slope from 21-day slope (late-period steepening)."""
    s10 = _linslope(close, 10)
    s21 = _linslope(close, _TD_MON)
    return s10 - s21


# --- Group G (061-075): Panic-thrust composite scores ---

def cth_061_panic_composite_5d_21d(close: pd.Series) -> pd.Series:
    """Composite: z-scored 5d return + z-scored 21d return (dual-horizon thrust)."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    z5  = _safe_div(cum5  - _rolling_mean(cum5, _TD_YEAR),  _rolling_std(cum5,  _TD_YEAR))
    z21 = _safe_div(cum21 - _rolling_mean(cum21, _TD_YEAR), _rolling_std(cum21, _TD_YEAR))
    return (z5 + z21) / 2.0


def cth_062_panic_steepness_persistence(close: pd.Series) -> pd.Series:
    """Composite: z-score of 5d return * fraction of down days in 21d (steepness * persistence)."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    z5    = _safe_div(cum5 - _rolling_mean(cum5, _TD_YEAR), _rolling_std(cum5, _TD_YEAR))
    lr    = _log_ret(close)
    pers  = _rolling_sum((lr < 0).astype(float), _TD_MON) / _TD_MON
    return z5 * pers


def cth_063_panic_volume_weighted_thrust(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 5-day log-return (panic thrust weighted by trading activity)."""
    lr   = _log_ret(close)
    vw   = (lr * volume).rolling(_TD_WEEK, min_periods=1).sum()
    vsum = _rolling_sum(volume, _TD_WEEK)
    return _safe_div(vw, vsum)


def cth_064_panic_score_sigma_days_21d(close: pd.Series) -> pd.Series:
    """Sum of sigma-exceedances (how much each down-day exceeded -2sigma) in 21 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    excess = (-z - 2.0).clip(lower=0)
    return _rolling_sum(excess, _TD_MON)


def cth_065_panic_score_sigma_days_63d(close: pd.Series) -> pd.Series:
    """Sum of sigma-exceedances beyond -2sigma in trailing 63 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    excess = (-z - 2.0).clip(lower=0)
    return _rolling_sum(excess, _TD_QTR)


def cth_066_thrust_range_ratio_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average daily (high-low)/close range in trailing 5 days (intraday thrust width)."""
    rng = (high - low) / close.clip(lower=_EPS)
    return _rolling_mean(rng, _TD_WEEK)


def cth_067_thrust_range_ratio_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average daily (high-low)/close in trailing 21 days."""
    rng = (high - low) / close.clip(lower=_EPS)
    return _rolling_mean(rng, _TD_MON)


def cth_068_atr_normalized_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day mean ATR normalized by close (normalized true-range burst)."""
    atr = _tr(close, high, low)
    return _rolling_mean(atr, _TD_WEEK) / close.clip(lower=_EPS)


def cth_069_atr_normalized_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day mean ATR normalized by close."""
    atr = _tr(close, high, low)
    return _rolling_mean(atr, _TD_MON) / close.clip(lower=_EPS)


def cth_070_atr_5d_vs_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR to 252-day ATR (thrust volatility relative to history)."""
    atr  = _tr(close, high, low) / close.clip(lower=_EPS)
    r5   = _rolling_mean(atr, _TD_WEEK)
    r252 = _rolling_mean(atr, _TD_YEAR)
    return _safe_div(r5, r252)


def cth_071_panic_composite_return_vol(close: pd.Series) -> pd.Series:
    """Composite: 21d return divided by 21d realized vol (Sharpe-like thrust signal)."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    vol21 = _rolling_std(_log_ret(close), _TD_MON)
    return _safe_div(cum21, vol21 * np.sqrt(_TD_MON))


def cth_072_panic_composite_3factor(close: pd.Series, volume: pd.Series) -> pd.Series:
    """3-factor composite: z(5d ret) + z(vol ratio) + z(down-day fraction) in 21d."""
    cum5    = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    z5      = _safe_div(cum5 - _rolling_mean(cum5, _TD_YEAR), _rolling_std(cum5, _TD_YEAR))
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_r   = _safe_div(volume, avg_vol)
    zvol    = _safe_div(vol_r - _rolling_mean(vol_r, _TD_YEAR), _rolling_std(vol_r, _TD_YEAR))
    lr      = _log_ret(close)
    frac    = _rolling_sum((lr < 0).astype(float), _TD_MON) / _TD_MON
    zfrac   = _safe_div(frac - _rolling_mean(frac, _TD_YEAR), _rolling_std(frac, _TD_YEAR))
    return (z5 + zvol + zfrac) / 3.0


def cth_073_max_intraday_down_thrust_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum intraday drawdown (high-to-low / high) over trailing 5 days."""
    intraday_dd = (high - low) / high.clip(lower=_EPS)
    return _rolling_max(intraday_dd, _TD_WEEK)


def cth_074_max_intraday_down_thrust_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Maximum intraday drawdown (high-to-low / high) over trailing 21 days."""
    intraday_dd = (high - low) / high.clip(lower=_EPS)
    return _rolling_max(intraday_dd, _TD_MON)


def cth_075_open_to_close_thrust_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Mean negative open-to-close log-return (body thrust) over trailing 5 days."""
    body = (_log_safe(close) - _log_safe(open)).clip(upper=0)
    return _rolling_mean(body, _TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITULATION_THRUST_REGISTRY_001_075 = {
    "cth_001_min_return_5d": {"inputs": ["close"], "func": cth_001_min_return_5d},
    "cth_002_min_return_10d": {"inputs": ["close"], "func": cth_002_min_return_10d},
    "cth_003_min_return_21d": {"inputs": ["close"], "func": cth_003_min_return_21d},
    "cth_004_min_return_63d": {"inputs": ["close"], "func": cth_004_min_return_63d},
    "cth_005_min_return_5d_vs_252d_mean": {"inputs": ["close"], "func": cth_005_min_return_5d_vs_252d_mean},
    "cth_006_min_return_5d_zscore_252d": {"inputs": ["close"], "func": cth_006_min_return_5d_zscore_252d},
    "cth_007_min_return_10d_zscore_252d": {"inputs": ["close"], "func": cth_007_min_return_10d_zscore_252d},
    "cth_008_min_return_21d_zscore_252d": {"inputs": ["close"], "func": cth_008_min_return_21d_zscore_252d},
    "cth_009_min_return_5d_pct_rank_252d": {"inputs": ["close"], "func": cth_009_min_return_5d_pct_rank_252d},
    "cth_010_min_return_21d_pct_rank_252d": {"inputs": ["close"], "func": cth_010_min_return_21d_pct_rank_252d},
    "cth_011_single_day_ret_zscore_63d": {"inputs": ["close"], "func": cth_011_single_day_ret_zscore_63d},
    "cth_012_single_day_ret_zscore_252d": {"inputs": ["close"], "func": cth_012_single_day_ret_zscore_252d},
    "cth_013_worst_single_day_21d": {"inputs": ["close"], "func": cth_013_worst_single_day_21d},
    "cth_014_worst_single_day_63d": {"inputs": ["close"], "func": cth_014_worst_single_day_63d},
    "cth_015_worst_single_day_zscore_63d": {"inputs": ["close"], "func": cth_015_worst_single_day_zscore_63d},
    "cth_016_days_below_2sigma_21d": {"inputs": ["close"], "func": cth_016_days_below_2sigma_21d},
    "cth_017_days_below_3sigma_63d": {"inputs": ["close"], "func": cth_017_days_below_3sigma_63d},
    "cth_018_days_below_1p5sigma_21d": {"inputs": ["close"], "func": cth_018_days_below_1p5sigma_21d},
    "cth_019_max_sigma_hit_21d": {"inputs": ["close"], "func": cth_019_max_sigma_hit_21d},
    "cth_020_frac_days_below_2sigma_252d": {"inputs": ["close"], "func": cth_020_frac_days_below_2sigma_252d},
    "cth_021_drawdown_from_recent_peak_21d": {"inputs": ["close"], "func": cth_021_drawdown_from_recent_peak_21d},
    "cth_022_drawdown_from_recent_peak_63d": {"inputs": ["close"], "func": cth_022_drawdown_from_recent_peak_63d},
    "cth_023_drawdown_from_recent_peak_126d": {"inputs": ["close"], "func": cth_023_drawdown_from_recent_peak_126d},
    "cth_024_drawdown_from_recent_peak_252d": {"inputs": ["close"], "func": cth_024_drawdown_from_recent_peak_252d},
    "cth_025_thrust_last5d_vs_dd21d": {"inputs": ["close"], "func": cth_025_thrust_last5d_vs_dd21d},
    "cth_026_thrust_last10d_vs_dd63d": {"inputs": ["close"], "func": cth_026_thrust_last10d_vs_dd63d},
    "cth_027_thrust_magnitude_abs_5d": {"inputs": ["close"], "func": cth_027_thrust_magnitude_abs_5d},
    "cth_028_thrust_magnitude_abs_21d": {"inputs": ["close"], "func": cth_028_thrust_magnitude_abs_21d},
    "cth_029_drawdown_21d_pct_rank_252d": {"inputs": ["close"], "func": cth_029_drawdown_21d_pct_rank_252d},
    "cth_030_drawdown_63d_expanding_rank": {"inputs": ["close"], "func": cth_030_drawdown_63d_expanding_rank},
    "cth_031_thrust_intensity_5d": {"inputs": ["close"], "func": cth_031_thrust_intensity_5d},
    "cth_032_thrust_intensity_10d": {"inputs": ["close"], "func": cth_032_thrust_intensity_10d},
    "cth_033_thrust_intensity_21d": {"inputs": ["close"], "func": cth_033_thrust_intensity_21d},
    "cth_034_worst_intensity_5d_in_63d": {"inputs": ["close"], "func": cth_034_worst_intensity_5d_in_63d},
    "cth_035_worst_intensity_10d_in_126d": {"inputs": ["close"], "func": cth_035_worst_intensity_10d_in_126d},
    "cth_036_worst_intensity_21d_in_252d": {"inputs": ["close"], "func": cth_036_worst_intensity_21d_in_252d},
    "cth_037_intensity_5d_zscore_252d": {"inputs": ["close"], "func": cth_037_intensity_5d_zscore_252d},
    "cth_038_intensity_21d_zscore_252d": {"inputs": ["close"], "func": cth_038_intensity_21d_zscore_252d},
    "cth_039_intensity_vs_hist_max_252d": {"inputs": ["close"], "func": cth_039_intensity_vs_hist_max_252d},
    "cth_040_intensity_acceleration_5d": {"inputs": ["close"], "func": cth_040_intensity_acceleration_5d},
    "cth_041_waterfall_3leg_loss": {"inputs": ["close"], "func": cth_041_waterfall_3leg_loss},
    "cth_042_waterfall_3leg_each_negative": {"inputs": ["close"], "func": cth_042_waterfall_3leg_each_negative},
    "cth_043_waterfall_accelerating_loss": {"inputs": ["close"], "func": cth_043_waterfall_accelerating_loss},
    "cth_044_cascade_down_days_in_10d": {"inputs": ["close"], "func": cth_044_cascade_down_days_in_10d},
    "cth_045_cascade_loss_ratio_last5_vs_prior10": {"inputs": ["close"], "func": cth_045_cascade_loss_ratio_last5_vs_prior10},
    "cth_046_waterfall_freq_63d": {"inputs": ["close"], "func": cth_046_waterfall_freq_63d},
    "cth_047_waterfall_freq_252d": {"inputs": ["close"], "func": cth_047_waterfall_freq_252d},
    "cth_048_gap_cluster_5d": {"inputs": ["close", "open"], "func": cth_048_gap_cluster_5d},
    "cth_049_gap_cluster_21d": {"inputs": ["close", "open"], "func": cth_049_gap_cluster_21d},
    "cth_050_gap_cluster_magnitude_5d": {"inputs": ["close", "open"], "func": cth_050_gap_cluster_magnitude_5d},
    "cth_051_final_leg_slope_5d": {"inputs": ["close"], "func": cth_051_final_leg_slope_5d},
    "cth_052_final_leg_slope_10d": {"inputs": ["close"], "func": cth_052_final_leg_slope_10d},
    "cth_053_final_leg_slope_21d": {"inputs": ["close"], "func": cth_053_final_leg_slope_21d},
    "cth_054_slope_5d_vs_slope_21d": {"inputs": ["close"], "func": cth_054_slope_5d_vs_slope_21d},
    "cth_055_slope_5d_vs_slope_63d": {"inputs": ["close"], "func": cth_055_slope_5d_vs_slope_63d},
    "cth_056_log_slope_5d": {"inputs": ["close"], "func": cth_056_log_slope_5d},
    "cth_057_log_slope_10d": {"inputs": ["close"], "func": cth_057_log_slope_10d},
    "cth_058_log_slope_21d": {"inputs": ["close"], "func": cth_058_log_slope_21d},
    "cth_059_log_slope_5d_vs_63d": {"inputs": ["close"], "func": cth_059_log_slope_5d_vs_63d},
    "cth_060_slope_convexity_21d": {"inputs": ["close"], "func": cth_060_slope_convexity_21d},
    "cth_061_panic_composite_5d_21d": {"inputs": ["close"], "func": cth_061_panic_composite_5d_21d},
    "cth_062_panic_steepness_persistence": {"inputs": ["close"], "func": cth_062_panic_steepness_persistence},
    "cth_063_panic_volume_weighted_thrust": {"inputs": ["close", "volume"], "func": cth_063_panic_volume_weighted_thrust},
    "cth_064_panic_score_sigma_days_21d": {"inputs": ["close"], "func": cth_064_panic_score_sigma_days_21d},
    "cth_065_panic_score_sigma_days_63d": {"inputs": ["close"], "func": cth_065_panic_score_sigma_days_63d},
    "cth_066_thrust_range_ratio_5d": {"inputs": ["close", "high", "low"], "func": cth_066_thrust_range_ratio_5d},
    "cth_067_thrust_range_ratio_21d": {"inputs": ["close", "high", "low"], "func": cth_067_thrust_range_ratio_21d},
    "cth_068_atr_normalized_5d": {"inputs": ["close", "high", "low"], "func": cth_068_atr_normalized_5d},
    "cth_069_atr_normalized_21d": {"inputs": ["close", "high", "low"], "func": cth_069_atr_normalized_21d},
    "cth_070_atr_5d_vs_252d": {"inputs": ["close", "high", "low"], "func": cth_070_atr_5d_vs_252d},
    "cth_071_panic_composite_return_vol": {"inputs": ["close"], "func": cth_071_panic_composite_return_vol},
    "cth_072_panic_composite_3factor": {"inputs": ["close", "volume"], "func": cth_072_panic_composite_3factor},
    "cth_073_max_intraday_down_thrust_5d": {"inputs": ["close", "high", "low"], "func": cth_073_max_intraday_down_thrust_5d},
    "cth_074_max_intraday_down_thrust_21d": {"inputs": ["close", "high", "low"], "func": cth_074_max_intraday_down_thrust_21d},
    "cth_075_open_to_close_thrust_5d": {"inputs": ["close", "open"], "func": cth_075_open_to_close_thrust_5d},
}
