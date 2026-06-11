"""
25_momentum_decay — Extended Features 001-075
Domain: Rate-of-Change (ROC) oscillator family — ROC term structure, decay shape,
        momentum half-life from ROC curve, risk-adjusted momentum, log-return ROC variants.
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


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    """Log return over n periods."""
    return np.log(s.clip(lower=_EPS)) - np.log(s.shift(n).clip(lower=_EPS))


def _roc(s: pd.Series, n: int) -> pd.Series:
    """Rate of Change: (close / close.shift(n) - 1) * 100."""
    return _safe_div(s, s.shift(n).replace(0, np.nan)) * 100.0 - 100.0


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

# --- Group A (001-006): Raw ROC oscillator at canonical horizons ---

def mdc_ext_001_roc_5d(close: pd.Series) -> pd.Series:
    """ROC oscillator: (close / close[5d ago] - 1) * 100. Pure 5-day price ROC."""
    return _roc(close, _TD_WEEK)


def mdc_ext_002_roc_10d(close: pd.Series) -> pd.Series:
    """ROC oscillator at 10-day horizon (2-week price rate of change)."""
    return _roc(close, 10)


def mdc_ext_003_roc_21d(close: pd.Series) -> pd.Series:
    """ROC oscillator at 21-day horizon (monthly price rate of change)."""
    return _roc(close, _TD_MON)


def mdc_ext_004_roc_63d(close: pd.Series) -> pd.Series:
    """ROC oscillator at 63-day horizon (quarterly price rate of change)."""
    return _roc(close, _TD_QTR)


def mdc_ext_005_roc_126d(close: pd.Series) -> pd.Series:
    """ROC oscillator at 126-day horizon (half-year price rate of change)."""
    return _roc(close, _TD_HALF)


def mdc_ext_006_roc_252d(close: pd.Series) -> pd.Series:
    """ROC oscillator at 252-day horizon (annual price rate of change)."""
    return _roc(close, _TD_YEAR)


# --- Group B (007-012): Smoothed ROC (EWM of raw ROC) ---

def mdc_ext_007_roc_5d_ewm_span21(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) 5-day ROC: captures the trend in short-term ROC."""
    return _ewm_mean(_roc(close, _TD_WEEK), _TD_MON)


def mdc_ext_008_roc_10d_ewm_span21(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=21) 10-day ROC."""
    return _ewm_mean(_roc(close, 10), _TD_MON)


def mdc_ext_009_roc_21d_ewm_span63(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=63) 21-day ROC: smoothed monthly ROC signal."""
    return _ewm_mean(_roc(close, _TD_MON), _TD_QTR)


def mdc_ext_010_roc_63d_ewm_span126(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=126) 63-day ROC: smoothed quarterly ROC."""
    return _ewm_mean(_roc(close, _TD_QTR), _TD_HALF)


def mdc_ext_011_roc_126d_ewm_span252(close: pd.Series) -> pd.Series:
    """EWM-smoothed (span=252) 126-day ROC: long-run smoothed half-year ROC."""
    return _ewm_mean(_roc(close, _TD_HALF), _TD_YEAR)


def mdc_ext_012_roc_5d_rolling_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of 5-day ROC (persistent short-term ROC level)."""
    return _rolling_mean(_roc(close, _TD_WEEK), _TD_QTR)


# --- Group C (013-018): ROC z-score vs trailing distribution ---

def mdc_ext_013_roc_5d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day ROC vs its trailing 252-day distribution."""
    r = _roc(close, _TD_WEEK)
    return _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))


def mdc_ext_014_roc_10d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 10-day ROC vs its trailing 252-day distribution."""
    r = _roc(close, 10)
    return _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))


def mdc_ext_015_roc_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 21-day ROC vs its trailing 252-day distribution."""
    r = _roc(close, _TD_MON)
    return _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))


def mdc_ext_016_roc_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63-day ROC vs its trailing 252-day distribution."""
    r = _roc(close, _TD_QTR)
    return _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))


def mdc_ext_017_roc_126d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 126-day ROC vs its trailing 252-day distribution."""
    r = _roc(close, _TD_HALF)
    return _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))


def mdc_ext_018_roc_252d_zscore_expanding(close: pd.Series) -> pd.Series:
    """Expanding-window z-score of 252-day ROC (all-time extremity of annual ROC)."""
    r = _roc(close, _TD_YEAR)
    m = r.expanding(min_periods=_TD_YEAR).mean()
    s = r.expanding(min_periods=_TD_YEAR).std()
    return _safe_div(r - m, s)


# --- Group D (019-024): ROC percentile rank vs trailing window ---

def mdc_ext_019_roc_5d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day ROC within trailing 252-day distribution."""
    return _roc(close, _TD_WEEK).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_ext_020_roc_10d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 10-day ROC within trailing 252-day distribution."""
    return _roc(close, 10).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_ext_021_roc_21d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ROC within trailing 252-day distribution."""
    return _roc(close, _TD_MON).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_ext_022_roc_63d_pctrank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63-day ROC within trailing 252-day distribution."""
    return _roc(close, _TD_QTR).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def mdc_ext_023_roc_5d_pctrank_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day ROC within trailing 63-day distribution."""
    return _roc(close, _TD_WEEK).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def mdc_ext_024_roc_21d_pctrank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day ROC within trailing 126-day distribution."""
    return _roc(close, _TD_MON).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


# --- Group E (025-030): ROC depth below zero and magnitude measures ---

def mdc_ext_025_roc_5d_depth_below_zero(close: pd.Series) -> pd.Series:
    """Depth of 5-day ROC below zero; zero when ROC >= 0."""
    r = _roc(close, _TD_WEEK)
    return r.clip(upper=0.0)


def mdc_ext_026_roc_21d_depth_below_zero(close: pd.Series) -> pd.Series:
    """Depth of 21-day ROC below zero; zero when ROC >= 0."""
    r = _roc(close, _TD_MON)
    return r.clip(upper=0.0)


def mdc_ext_027_roc_63d_depth_below_zero(close: pd.Series) -> pd.Series:
    """Depth of 63-day ROC below zero; zero when ROC >= 0."""
    r = _roc(close, _TD_QTR)
    return r.clip(upper=0.0)


def mdc_ext_028_roc_5d_rolling_min_63d(close: pd.Series) -> pd.Series:
    """Trailing 63-day minimum of 5-day ROC (worst ROC reading in the quarter)."""
    return _rolling_min(_roc(close, _TD_WEEK), _TD_QTR)


def mdc_ext_029_roc_21d_rolling_min_252d(close: pd.Series) -> pd.Series:
    """Trailing 252-day minimum of 21-day ROC (worst monthly ROC in the year)."""
    return _rolling_min(_roc(close, _TD_MON), _TD_YEAR)


def mdc_ext_030_roc_5d_vs_trailing_range_63d(close: pd.Series) -> pd.Series:
    """5-day ROC relative to its 63-day range: (ROC - min) / (max - min)."""
    r = _roc(close, _TD_WEEK)
    mn = _rolling_min(r, _TD_QTR)
    mx = _rolling_max(r, _TD_QTR)
    return _safe_div(r - mn, mx - mn)


# --- Group F (031-036): ROC slope (rate of change of ROC) ---

def mdc_ext_031_roc_5d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 5-day ROC series over trailing 21 days (momentum of 5d ROC)."""
    return _linslope(_roc(close, _TD_WEEK), _TD_MON)


def mdc_ext_032_roc_10d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope of 10-day ROC series over trailing 21 days."""
    return _linslope(_roc(close, 10), _TD_MON)


def mdc_ext_033_roc_21d_slope_63d(close: pd.Series) -> pd.Series:
    """OLS slope of 21-day ROC series over trailing 63 days."""
    return _linslope(_roc(close, _TD_MON), _TD_QTR)


def mdc_ext_034_roc_63d_slope_126d(close: pd.Series) -> pd.Series:
    """OLS slope of 63-day ROC series over trailing 126 days."""
    return _linslope(_roc(close, _TD_QTR), _TD_HALF)


def mdc_ext_035_roc_5d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day first difference of 5-day ROC (velocity / rate of change of ROC)."""
    return _roc(close, _TD_WEEK).diff(_TD_WEEK)


def mdc_ext_036_roc_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day first difference of 21-day ROC (monthly velocity of monthly ROC)."""
    return _roc(close, _TD_MON).diff(_TD_MON)


# --- Group G (037-043): ROC of ROC (second-order momentum) ---

def mdc_ext_037_roc_of_roc_5d_5d(close: pd.Series) -> pd.Series:
    """ROC of the 5-day ROC over 5 days: (roc5[t] / roc5[t-5] - 1)*100."""
    r5 = _roc(close, _TD_WEEK)
    return _safe_div(r5, r5.shift(_TD_WEEK).replace(0, np.nan)) * 100.0 - 100.0


def mdc_ext_038_roc_of_roc_21d_21d(close: pd.Series) -> pd.Series:
    """ROC of the 21-day ROC over 21 days: second-order monthly momentum."""
    r21 = _roc(close, _TD_MON)
    return _safe_div(r21, r21.shift(_TD_MON).replace(0, np.nan)) * 100.0 - 100.0


def mdc_ext_039_roc_of_roc_63d_63d(close: pd.Series) -> pd.Series:
    """ROC of the 63-day ROC over 63 days: second-order quarterly momentum."""
    r63 = _roc(close, _TD_QTR)
    return _safe_div(r63, r63.shift(_TD_QTR).replace(0, np.nan)) * 100.0 - 100.0


def mdc_ext_040_roc_5d_zscore_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of the 5-day ROC z-score (velocity of ROC extremity)."""
    r = _roc(close, _TD_WEEK)
    z = _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))
    return z.diff(_TD_WEEK)


def mdc_ext_041_roc_21d_zscore_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day ROC z-score (monthly velocity of ROC extremity)."""
    r = _roc(close, _TD_MON)
    z = _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))
    return z.diff(_TD_MON)


def mdc_ext_042_roc_5d_ewm_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21d of EWM(span=21)-smoothed 5d ROC (trend in smooth ROC)."""
    return _linslope(_ewm_mean(_roc(close, _TD_WEEK), _TD_MON), _TD_MON)


def mdc_ext_043_roc_5d_acceleration_5d(close: pd.Series) -> pd.Series:
    """5d diff of the 5d-diff of 5d ROC: second-order ROC acceleration."""
    vel = _roc(close, _TD_WEEK).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- Group H (044-049): ROC sign streaks ---

def mdc_ext_044_roc_5d_neg_streak_count(close: pd.Series) -> pd.Series:
    """Count of consecutive recent days where 5-day ROC is negative (sign streak)."""
    neg = (_roc(close, _TD_WEEK) < 0).astype(float)
    # Streak: cumulative sum reset on sign flip
    streak = neg * (neg.groupby((neg != neg.shift()).cumsum()).cumcount() + 1)
    return streak


def mdc_ext_045_roc_21d_neg_streak_count(close: pd.Series) -> pd.Series:
    """Count of consecutive recent days where 21-day ROC is negative."""
    neg = (_roc(close, _TD_MON) < 0).astype(float)
    streak = neg * (neg.groupby((neg != neg.shift()).cumsum()).cumcount() + 1)
    return streak


def mdc_ext_046_roc_5d_neg_count_in_63d(close: pd.Series) -> pd.Series:
    """Count of days in the last 63d where 5-day ROC was negative."""
    return (_roc(close, _TD_WEEK) < 0).astype(float).rolling(
        _TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def mdc_ext_047_roc_21d_neg_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of days in the last 252d where 21-day ROC was negative."""
    return (_roc(close, _TD_MON) < 0).astype(float).rolling(
        _TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def mdc_ext_048_roc_63d_neg_count_in_252d(close: pd.Series) -> pd.Series:
    """Count of days in the last 252d where 63-day ROC was negative."""
    return (_roc(close, _TD_QTR) < 0).astype(float).rolling(
        _TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()


def mdc_ext_049_roc_all_horizons_negative_flag(close: pd.Series) -> pd.Series:
    """Flag: 5d, 21d, 63d, 126d, 252d ROC all negative simultaneously."""
    return ((_roc(close, _TD_WEEK) < 0) & (_roc(close, _TD_MON) < 0) &
            (_roc(close, _TD_QTR) < 0) & (_roc(close, _TD_HALF) < 0) &
            (_roc(close, _TD_YEAR) < 0)).astype(float)


# --- Group I (050-056): ROC term structure decay shape (short vs long ROC spread) ---

def mdc_ext_050_roc_5d_minus_63d(close: pd.Series) -> pd.Series:
    """Short-horizon ROC (5d) minus long-horizon ROC (63d): ROC term structure decay."""
    return _roc(close, _TD_WEEK) - _roc(close, _TD_QTR)


def mdc_ext_051_roc_5d_minus_252d(close: pd.Series) -> pd.Series:
    """5-day ROC minus 252-day ROC: extreme short-vs-annual ROC decay shape."""
    return _roc(close, _TD_WEEK) - _roc(close, _TD_YEAR)


def mdc_ext_052_roc_21d_minus_126d(close: pd.Series) -> pd.Series:
    """21-day ROC minus 126-day ROC: monthly vs half-year decay shape."""
    return _roc(close, _TD_MON) - _roc(close, _TD_HALF)


def mdc_ext_053_roc_21d_minus_252d(close: pd.Series) -> pd.Series:
    """21-day ROC minus 252-day ROC: monthly vs annual ROC decay spread."""
    return _roc(close, _TD_MON) - _roc(close, _TD_YEAR)


def mdc_ext_054_roc_63d_minus_252d(close: pd.Series) -> pd.Series:
    """63-day ROC minus 252-day ROC: quarterly vs annual decay shape."""
    return _roc(close, _TD_QTR) - _roc(close, _TD_YEAR)


def mdc_ext_055_roc_term_structure_slope(close: pd.Series) -> pd.Series:
    """OLS slope of ROC on log(horizon) across 5/21/63/126/252d (ROC term slope)."""
    r5 = _roc(close, _TD_WEEK)
    r21 = _roc(close, _TD_MON)
    r63 = _roc(close, _TD_QTR)
    r126 = _roc(close, _TD_HALF)
    r252 = _roc(close, _TD_YEAR)
    horizons = np.log(np.array([_TD_WEEK, _TD_MON, _TD_QTR, _TD_HALF, _TD_YEAR], dtype=float))
    horizons = horizons - horizons.mean()
    def ts_slope(row):
        vals = np.array(row, dtype=float)
        if np.any(np.isnan(vals)):
            return np.nan
        vals_m = vals.mean()
        num = (horizons * (vals - vals_m)).sum()
        den = (horizons ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    df = pd.concat([r5, r21, r63, r126, r252], axis=1)
    return df.apply(ts_slope, axis=1)


def mdc_ext_056_roc_short_minus_long_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (5d ROC - 252d ROC) spread vs its 252-day distribution."""
    spread = _roc(close, _TD_WEEK) - _roc(close, _TD_YEAR)
    return _safe_div(spread - _rolling_mean(spread, _TD_YEAR), _rolling_std(spread, _TD_YEAR))


# --- Group J (057-061): Momentum half-life estimated from ROC curve ---

def mdc_ext_057_roc_halflife_proxy_126_252(close: pd.Series) -> pd.Series:
    """ROC half-life proxy: 126d ROC / 252d ROC; <50 signals momentum halved mid-year."""
    return _safe_div(_roc(close, _TD_HALF), _roc(close, _TD_YEAR).replace(0, np.nan))


def mdc_ext_058_roc_halflife_proxy_63_126(close: pd.Series) -> pd.Series:
    """ROC half-life proxy at quarterly scale: 63d ROC / 126d ROC."""
    return _safe_div(_roc(close, _TD_QTR), _roc(close, _TD_HALF).replace(0, np.nan))


def mdc_ext_059_roc_halflife_decay_speed(close: pd.Series) -> pd.Series:
    """Speed of ROC decay: (5d ROC - 252d ROC) / |252d ROC| — relative short-end drop."""
    r5 = _roc(close, _TD_WEEK)
    r252 = _roc(close, _TD_YEAR)
    return _safe_div(r5 - r252, r252.abs() + _EPS)


def mdc_ext_060_roc_curve_convexity(close: pd.Series) -> pd.Series:
    """ROC curve convexity: (ROC_5 + ROC_252) / 2 - ROC_126 (bowing of term structure)."""
    return (_roc(close, _TD_WEEK) + _roc(close, _TD_YEAR)) / 2.0 - _roc(close, _TD_HALF)


def mdc_ext_061_roc_negative_horizon_count(close: pd.Series) -> pd.Series:
    """Count of negative ROC across 5/21/63/126/252d horizons (0-5)."""
    return ((_roc(close, _TD_WEEK) < 0).astype(float) +
            (_roc(close, _TD_MON) < 0).astype(float) +
            (_roc(close, _TD_QTR) < 0).astype(float) +
            (_roc(close, _TD_HALF) < 0).astype(float) +
            (_roc(close, _TD_YEAR) < 0).astype(float))


# --- Group K (062-066): Multi-window low momentum detection ---

def mdc_ext_062_roc_5d_at_252d_low_flag(close: pd.Series) -> pd.Series:
    """Flag: current 5-day ROC equals its 252-day rolling minimum (at momentum low)."""
    r = _roc(close, _TD_WEEK)
    return (r <= _rolling_min(r, _TD_YEAR)).astype(float)


def mdc_ext_063_roc_21d_at_252d_low_flag(close: pd.Series) -> pd.Series:
    """Flag: current 21-day ROC equals its 252-day rolling minimum."""
    r = _roc(close, _TD_MON)
    return (r <= _rolling_min(r, _TD_YEAR)).astype(float)


def mdc_ext_064_roc_5d_pct_from_252d_low(close: pd.Series) -> pd.Series:
    """Distance of 5-day ROC from its 252-day minimum, as pct of the range."""
    r = _roc(close, _TD_WEEK)
    mn = _rolling_min(r, _TD_YEAR)
    mx = _rolling_max(r, _TD_YEAR)
    return _safe_div(r - mn, mx - mn)


def mdc_ext_065_roc_21d_pct_from_252d_low(close: pd.Series) -> pd.Series:
    """Distance of 21-day ROC from its 252-day minimum, as pct of the range."""
    r = _roc(close, _TD_MON)
    mn = _rolling_min(r, _TD_YEAR)
    mx = _rolling_max(r, _TD_YEAR)
    return _safe_div(r - mn, mx - mn)


def mdc_ext_066_roc_dispersion_across_horizons(close: pd.Series) -> pd.Series:
    """Std dev of ROC values across 5/21/63/126/252d (spread of ROC term structure)."""
    df = pd.concat([
        _roc(close, _TD_WEEK),
        _roc(close, _TD_MON),
        _roc(close, _TD_QTR),
        _roc(close, _TD_HALF),
        _roc(close, _TD_YEAR)
    ], axis=1)
    return df.std(axis=1)


# --- Group L (067-069): Momentum acceleration / deceleration ---

def mdc_ext_067_roc_5d_accel_vs_21d_roc(close: pd.Series) -> pd.Series:
    """ROC acceleration: current 5d ROC minus prior 5d ROC, normalized by 21d ROC."""
    r5 = _roc(close, _TD_WEEK)
    r5_lag = r5.shift(_TD_WEEK)
    r21 = _roc(close, _TD_MON)
    return _safe_div(r5 - r5_lag, r21.abs() + _EPS)


def mdc_ext_068_roc_21d_decel_vs_63d_roc(close: pd.Series) -> pd.Series:
    """ROC deceleration: current 21d ROC minus prior 21d ROC, normalized by 63d ROC."""
    r21 = _roc(close, _TD_MON)
    r21_lag = r21.shift(_TD_MON)
    r63 = _roc(close, _TD_QTR)
    return _safe_div(r21 - r21_lag, r63.abs() + _EPS)


def mdc_ext_069_roc_momentum_acceleration_sign(close: pd.Series) -> pd.Series:
    """Sign-composite of ROC acceleration: sign(roc5-roc5_lag) + sign(roc21-roc21_lag)."""
    r5 = _roc(close, _TD_WEEK)
    r21 = _roc(close, _TD_MON)
    acc5 = np.sign(r5 - r5.shift(_TD_WEEK))
    acc21 = np.sign(r21 - r21.shift(_TD_MON))
    return (acc5 + acc21) / 2.0


# --- Group M (070-072): Log-return momentum variants (ROC complement) ---

def mdc_ext_070_log_roc_5d(close: pd.Series) -> pd.Series:
    """Log-based ROC: log(close / close[5d]) * 100 — continuous compounding ROC."""
    return _log_ret(close, _TD_WEEK) * 100.0


def mdc_ext_071_log_roc_63d(close: pd.Series) -> pd.Series:
    """Log-based ROC at 63d: log(close / close[63d]) * 100."""
    return _log_ret(close, _TD_QTR) * 100.0


def mdc_ext_072_log_roc_5d_minus_252d(close: pd.Series) -> pd.Series:
    """Log-ROC decay spread: log_roc_5d minus log_roc_252d (log-domain term decay)."""
    return (_log_ret(close, _TD_WEEK) - _log_ret(close, _TD_YEAR)) * 100.0


# --- Group N (073-075): Risk-adjusted momentum (ROC / volatility) ---

def mdc_ext_073_roc_5d_risk_adjusted_21d(close: pd.Series) -> pd.Series:
    """Risk-adjusted 5d ROC: 5d ROC divided by 21-day rolling std of 1d returns * 100."""
    r = _roc(close, _TD_WEEK)
    vol = _rolling_std(_log_ret(close, 1), _TD_MON) * 100.0
    return _safe_div(r, vol + _EPS)


def mdc_ext_074_roc_21d_risk_adjusted_63d(close: pd.Series) -> pd.Series:
    """Risk-adjusted 21d ROC: 21d ROC divided by 63-day rolling std of 1d returns * 100."""
    r = _roc(close, _TD_MON)
    vol = _rolling_std(_log_ret(close, 1), _TD_QTR) * 100.0
    return _safe_div(r, vol + _EPS)


def mdc_ext_075_roc_composite_decay_score(close: pd.Series) -> pd.Series:
    """Composite ROC decay score: avg z-score of 5d/21d/63d ROC vs 252d distributions."""
    def _rz(n):
        r = _roc(close, n)
        return _safe_div(r - _rolling_mean(r, _TD_YEAR), _rolling_std(r, _TD_YEAR))
    return (_rz(_TD_WEEK) + _rz(_TD_MON) + _rz(_TD_QTR)) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

MOMENTUM_DECAY_EXTENDED_REGISTRY_001_075 = {
    "mdc_ext_001_roc_5d": {"inputs": ["close"], "func": mdc_ext_001_roc_5d},
    "mdc_ext_002_roc_10d": {"inputs": ["close"], "func": mdc_ext_002_roc_10d},
    "mdc_ext_003_roc_21d": {"inputs": ["close"], "func": mdc_ext_003_roc_21d},
    "mdc_ext_004_roc_63d": {"inputs": ["close"], "func": mdc_ext_004_roc_63d},
    "mdc_ext_005_roc_126d": {"inputs": ["close"], "func": mdc_ext_005_roc_126d},
    "mdc_ext_006_roc_252d": {"inputs": ["close"], "func": mdc_ext_006_roc_252d},
    "mdc_ext_007_roc_5d_ewm_span21": {"inputs": ["close"], "func": mdc_ext_007_roc_5d_ewm_span21},
    "mdc_ext_008_roc_10d_ewm_span21": {"inputs": ["close"], "func": mdc_ext_008_roc_10d_ewm_span21},
    "mdc_ext_009_roc_21d_ewm_span63": {"inputs": ["close"], "func": mdc_ext_009_roc_21d_ewm_span63},
    "mdc_ext_010_roc_63d_ewm_span126": {"inputs": ["close"], "func": mdc_ext_010_roc_63d_ewm_span126},
    "mdc_ext_011_roc_126d_ewm_span252": {"inputs": ["close"], "func": mdc_ext_011_roc_126d_ewm_span252},
    "mdc_ext_012_roc_5d_rolling_mean_63d": {"inputs": ["close"], "func": mdc_ext_012_roc_5d_rolling_mean_63d},
    "mdc_ext_013_roc_5d_zscore_252d": {"inputs": ["close"], "func": mdc_ext_013_roc_5d_zscore_252d},
    "mdc_ext_014_roc_10d_zscore_252d": {"inputs": ["close"], "func": mdc_ext_014_roc_10d_zscore_252d},
    "mdc_ext_015_roc_21d_zscore_252d": {"inputs": ["close"], "func": mdc_ext_015_roc_21d_zscore_252d},
    "mdc_ext_016_roc_63d_zscore_252d": {"inputs": ["close"], "func": mdc_ext_016_roc_63d_zscore_252d},
    "mdc_ext_017_roc_126d_zscore_252d": {"inputs": ["close"], "func": mdc_ext_017_roc_126d_zscore_252d},
    "mdc_ext_018_roc_252d_zscore_expanding": {"inputs": ["close"], "func": mdc_ext_018_roc_252d_zscore_expanding},
    "mdc_ext_019_roc_5d_pctrank_252d": {"inputs": ["close"], "func": mdc_ext_019_roc_5d_pctrank_252d},
    "mdc_ext_020_roc_10d_pctrank_252d": {"inputs": ["close"], "func": mdc_ext_020_roc_10d_pctrank_252d},
    "mdc_ext_021_roc_21d_pctrank_252d": {"inputs": ["close"], "func": mdc_ext_021_roc_21d_pctrank_252d},
    "mdc_ext_022_roc_63d_pctrank_252d": {"inputs": ["close"], "func": mdc_ext_022_roc_63d_pctrank_252d},
    "mdc_ext_023_roc_5d_pctrank_63d": {"inputs": ["close"], "func": mdc_ext_023_roc_5d_pctrank_63d},
    "mdc_ext_024_roc_21d_pctrank_126d": {"inputs": ["close"], "func": mdc_ext_024_roc_21d_pctrank_126d},
    "mdc_ext_025_roc_5d_depth_below_zero": {"inputs": ["close"], "func": mdc_ext_025_roc_5d_depth_below_zero},
    "mdc_ext_026_roc_21d_depth_below_zero": {"inputs": ["close"], "func": mdc_ext_026_roc_21d_depth_below_zero},
    "mdc_ext_027_roc_63d_depth_below_zero": {"inputs": ["close"], "func": mdc_ext_027_roc_63d_depth_below_zero},
    "mdc_ext_028_roc_5d_rolling_min_63d": {"inputs": ["close"], "func": mdc_ext_028_roc_5d_rolling_min_63d},
    "mdc_ext_029_roc_21d_rolling_min_252d": {"inputs": ["close"], "func": mdc_ext_029_roc_21d_rolling_min_252d},
    "mdc_ext_030_roc_5d_vs_trailing_range_63d": {"inputs": ["close"], "func": mdc_ext_030_roc_5d_vs_trailing_range_63d},
    "mdc_ext_031_roc_5d_slope_21d": {"inputs": ["close"], "func": mdc_ext_031_roc_5d_slope_21d},
    "mdc_ext_032_roc_10d_slope_21d": {"inputs": ["close"], "func": mdc_ext_032_roc_10d_slope_21d},
    "mdc_ext_033_roc_21d_slope_63d": {"inputs": ["close"], "func": mdc_ext_033_roc_21d_slope_63d},
    "mdc_ext_034_roc_63d_slope_126d": {"inputs": ["close"], "func": mdc_ext_034_roc_63d_slope_126d},
    "mdc_ext_035_roc_5d_5d_diff": {"inputs": ["close"], "func": mdc_ext_035_roc_5d_5d_diff},
    "mdc_ext_036_roc_21d_21d_diff": {"inputs": ["close"], "func": mdc_ext_036_roc_21d_21d_diff},
    "mdc_ext_037_roc_of_roc_5d_5d": {"inputs": ["close"], "func": mdc_ext_037_roc_of_roc_5d_5d},
    "mdc_ext_038_roc_of_roc_21d_21d": {"inputs": ["close"], "func": mdc_ext_038_roc_of_roc_21d_21d},
    "mdc_ext_039_roc_of_roc_63d_63d": {"inputs": ["close"], "func": mdc_ext_039_roc_of_roc_63d_63d},
    "mdc_ext_040_roc_5d_zscore_5d_diff": {"inputs": ["close"], "func": mdc_ext_040_roc_5d_zscore_5d_diff},
    "mdc_ext_041_roc_21d_zscore_21d_diff": {"inputs": ["close"], "func": mdc_ext_041_roc_21d_zscore_21d_diff},
    "mdc_ext_042_roc_5d_ewm_slope_21d": {"inputs": ["close"], "func": mdc_ext_042_roc_5d_ewm_slope_21d},
    "mdc_ext_043_roc_5d_acceleration_5d": {"inputs": ["close"], "func": mdc_ext_043_roc_5d_acceleration_5d},
    "mdc_ext_044_roc_5d_neg_streak_count": {"inputs": ["close"], "func": mdc_ext_044_roc_5d_neg_streak_count},
    "mdc_ext_045_roc_21d_neg_streak_count": {"inputs": ["close"], "func": mdc_ext_045_roc_21d_neg_streak_count},
    "mdc_ext_046_roc_5d_neg_count_in_63d": {"inputs": ["close"], "func": mdc_ext_046_roc_5d_neg_count_in_63d},
    "mdc_ext_047_roc_21d_neg_count_in_252d": {"inputs": ["close"], "func": mdc_ext_047_roc_21d_neg_count_in_252d},
    "mdc_ext_048_roc_63d_neg_count_in_252d": {"inputs": ["close"], "func": mdc_ext_048_roc_63d_neg_count_in_252d},
    "mdc_ext_049_roc_all_horizons_negative_flag": {"inputs": ["close"], "func": mdc_ext_049_roc_all_horizons_negative_flag},
    "mdc_ext_050_roc_5d_minus_63d": {"inputs": ["close"], "func": mdc_ext_050_roc_5d_minus_63d},
    "mdc_ext_051_roc_5d_minus_252d": {"inputs": ["close"], "func": mdc_ext_051_roc_5d_minus_252d},
    "mdc_ext_052_roc_21d_minus_126d": {"inputs": ["close"], "func": mdc_ext_052_roc_21d_minus_126d},
    "mdc_ext_053_roc_21d_minus_252d": {"inputs": ["close"], "func": mdc_ext_053_roc_21d_minus_252d},
    "mdc_ext_054_roc_63d_minus_252d": {"inputs": ["close"], "func": mdc_ext_054_roc_63d_minus_252d},
    "mdc_ext_055_roc_term_structure_slope": {"inputs": ["close"], "func": mdc_ext_055_roc_term_structure_slope},
    "mdc_ext_056_roc_short_minus_long_zscore_252d": {"inputs": ["close"], "func": mdc_ext_056_roc_short_minus_long_zscore_252d},
    "mdc_ext_057_roc_halflife_proxy_126_252": {"inputs": ["close"], "func": mdc_ext_057_roc_halflife_proxy_126_252},
    "mdc_ext_058_roc_halflife_proxy_63_126": {"inputs": ["close"], "func": mdc_ext_058_roc_halflife_proxy_63_126},
    "mdc_ext_059_roc_halflife_decay_speed": {"inputs": ["close"], "func": mdc_ext_059_roc_halflife_decay_speed},
    "mdc_ext_060_roc_curve_convexity": {"inputs": ["close"], "func": mdc_ext_060_roc_curve_convexity},
    "mdc_ext_061_roc_negative_horizon_count": {"inputs": ["close"], "func": mdc_ext_061_roc_negative_horizon_count},
    "mdc_ext_062_roc_5d_at_252d_low_flag": {"inputs": ["close"], "func": mdc_ext_062_roc_5d_at_252d_low_flag},
    "mdc_ext_063_roc_21d_at_252d_low_flag": {"inputs": ["close"], "func": mdc_ext_063_roc_21d_at_252d_low_flag},
    "mdc_ext_064_roc_5d_pct_from_252d_low": {"inputs": ["close"], "func": mdc_ext_064_roc_5d_pct_from_252d_low},
    "mdc_ext_065_roc_21d_pct_from_252d_low": {"inputs": ["close"], "func": mdc_ext_065_roc_21d_pct_from_252d_low},
    "mdc_ext_066_roc_dispersion_across_horizons": {"inputs": ["close"], "func": mdc_ext_066_roc_dispersion_across_horizons},
    "mdc_ext_067_roc_5d_accel_vs_21d_roc": {"inputs": ["close"], "func": mdc_ext_067_roc_5d_accel_vs_21d_roc},
    "mdc_ext_068_roc_21d_decel_vs_63d_roc": {"inputs": ["close"], "func": mdc_ext_068_roc_21d_decel_vs_63d_roc},
    "mdc_ext_069_roc_momentum_acceleration_sign": {"inputs": ["close"], "func": mdc_ext_069_roc_momentum_acceleration_sign},
    "mdc_ext_070_log_roc_5d": {"inputs": ["close"], "func": mdc_ext_070_log_roc_5d},
    "mdc_ext_071_log_roc_63d": {"inputs": ["close"], "func": mdc_ext_071_log_roc_63d},
    "mdc_ext_072_log_roc_5d_minus_252d": {"inputs": ["close"], "func": mdc_ext_072_log_roc_5d_minus_252d},
    "mdc_ext_073_roc_5d_risk_adjusted_21d": {"inputs": ["close"], "func": mdc_ext_073_roc_5d_risk_adjusted_21d},
    "mdc_ext_074_roc_21d_risk_adjusted_63d": {"inputs": ["close"], "func": mdc_ext_074_roc_21d_risk_adjusted_63d},
    "mdc_ext_075_roc_composite_decay_score": {"inputs": ["close"], "func": mdc_ext_075_roc_composite_decay_score},
}
