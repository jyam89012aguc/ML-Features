"""
34_velocity_inflection — Base Features 001-075
Domain: sign change in price velocity — inflection points where smoothed price velocity
(1st derivative) changes sign, days since last velocity sign-flip, curvature/2nd-derivative
of price crossing zero, count of inflections in a window, magnitude of velocity at most
recent inflection, alternating up/down velocity regimes, zero-crossings of momentum,
smoothed-slope sign reversals.
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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _velocity(close: pd.Series, span: int) -> pd.Series:
    """EMA-smoothed 1-day log-return (price velocity)."""
    lr = _log_safe(close).diff(1)
    return _ewm_mean(lr, span)


def _sign_flip(s: pd.Series) -> pd.Series:
    """Binary: 1 where sign of s differs from prior row (i.e. velocity sign-change)."""
    sg = np.sign(s)
    return ((sg != sg.shift(1)) & sg.notna() & sg.shift(1).notna()).astype(float)


def _days_since_flip(flip: pd.Series) -> pd.Series:
    """Bars elapsed since last 1 in binary flip series (backward-looking counter)."""
    idx = np.arange(len(flip))
    last = pd.Series(np.nan, index=flip.index)
    cum = flip.cumsum()
    # for each row, find when the most recent flip occurred
    # use cumsum trick: within a "no flip" run the cumsum is constant
    # days_since = current_index - index_of_last_flip
    last_flip_idx = pd.Series(np.where(flip.values == 1, idx, np.nan))
    last_flip_idx = last_flip_idx.ffill()
    result = pd.Series(idx, index=flip.index, dtype=float) - last_flip_idx.values
    result[last_flip_idx.isna().values] = np.nan
    return result


def _rolling_count(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


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

# --- Group A (001-015): Velocity sign-flip detection across smoothing spans ---

def vif_001_vel_flip_ema5_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EMA-5 velocity changed sign today vs yesterday."""
    v = _velocity(close, 5)
    return _sign_flip(v)


def vif_002_vel_flip_ema10_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EMA-10 velocity sign flip today."""
    v = _velocity(close, 10)
    return _sign_flip(v)


def vif_003_vel_flip_ema21_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EMA-21 velocity sign flip today."""
    v = _velocity(close, _TD_MON)
    return _sign_flip(v)


def vif_004_vel_flip_ema63_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EMA-63 velocity sign flip today."""
    v = _velocity(close, _TD_QTR)
    return _sign_flip(v)


def vif_005_vel_flip_raw1d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: raw 1-day log-return sign changed from prior day."""
    lr = _log_safe(close).diff(1)
    return _sign_flip(lr)


def vif_006_vel_flip_sma5_slope_flag(close: pd.Series) -> pd.Series:
    """Binary flag: sign flip in the 1-day diff of the 5-day SMA (SMA slope)."""
    slope = _rolling_mean(close, _TD_WEEK).diff(1)
    return _sign_flip(slope)


def vif_007_vel_flip_sma21_slope_flag(close: pd.Series) -> pd.Series:
    """Binary flag: sign flip in 1-day diff of 21-day SMA slope."""
    slope = _rolling_mean(close, _TD_MON).diff(1)
    return _sign_flip(slope)


def vif_008_vel_flip_sma63_slope_flag(close: pd.Series) -> pd.Series:
    """Binary flag: sign flip in 1-day diff of 63-day SMA slope."""
    slope = _rolling_mean(close, _TD_QTR).diff(1)
    return _sign_flip(slope)


def vif_009_vel_flip_ema5_to_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity flipped from positive to negative (bearish inflection)."""
    v = _velocity(close, 5)
    sg = np.sign(v)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_010_vel_flip_ema5_to_pos_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity flipped from negative to positive (bullish inflection)."""
    v = _velocity(close, 5)
    sg = np.sign(v)
    return ((sg > 0) & (sg.shift(1) < 0)).astype(float)


def vif_011_vel_flip_ema21_to_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-21 velocity flipped negative (bearish inflection on monthly smoothing)."""
    v = _velocity(close, _TD_MON)
    sg = np.sign(v)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_012_vel_flip_ema21_to_pos_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-21 velocity flipped positive (bullish inflection on monthly smoothing)."""
    v = _velocity(close, _TD_MON)
    sg = np.sign(v)
    return ((sg > 0) & (sg.shift(1) < 0)).astype(float)


def vif_013_vel_flip_ema63_to_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-63 velocity turned negative (bearish quarterly-smooth inflection)."""
    v = _velocity(close, _TD_QTR)
    sg = np.sign(v)
    return ((sg < 0) & (sg.shift(1) > 0)).astype(float)


def vif_014_vel_flip_macd_zero_cross_neg(close: pd.Series) -> pd.Series:
    """Binary: MACD (EMA12-EMA26) crossed below zero (negative velocity inflection)."""
    macd = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return ((macd < 0) & (macd.shift(1) >= 0)).astype(float)


def vif_015_vel_flip_macd_zero_cross_pos(close: pd.Series) -> pd.Series:
    """Binary: MACD crossed above zero (positive velocity inflection)."""
    macd = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return ((macd > 0) & (macd.shift(1) <= 0)).astype(float)


# --- Group B (016-030): Days since last velocity sign-flip ---

def vif_016_days_since_ema5_vel_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-5 velocity sign-flip (staleness of inflection)."""
    flip = _sign_flip(_velocity(close, 5))
    return _days_since_flip(flip)


def vif_017_days_since_ema10_vel_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-10 velocity sign-flip."""
    flip = _sign_flip(_velocity(close, 10))
    return _days_since_flip(flip)


def vif_018_days_since_ema21_vel_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-21 velocity sign-flip."""
    flip = _sign_flip(_velocity(close, _TD_MON))
    return _days_since_flip(flip)


def vif_019_days_since_ema63_vel_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last EMA-63 velocity sign-flip."""
    flip = _sign_flip(_velocity(close, _TD_QTR))
    return _days_since_flip(flip)


def vif_020_days_since_raw_vel_flip(close: pd.Series) -> pd.Series:
    """Days elapsed since last raw 1-day log-return sign-flip."""
    lr = _log_safe(close).diff(1)
    flip = _sign_flip(lr)
    return _days_since_flip(flip)


def vif_021_days_since_sma5_slope_flip(close: pd.Series) -> pd.Series:
    """Days since last sign-flip in the 1-day diff of the 5-day SMA."""
    slope = _rolling_mean(close, _TD_WEEK).diff(1)
    flip = _sign_flip(slope)
    return _days_since_flip(flip)


def vif_022_days_since_sma21_slope_flip(close: pd.Series) -> pd.Series:
    """Days since last sign-flip in the 1-day diff of the 21-day SMA."""
    slope = _rolling_mean(close, _TD_MON).diff(1)
    flip = _sign_flip(slope)
    return _days_since_flip(flip)


def vif_023_days_since_sma63_slope_flip(close: pd.Series) -> pd.Series:
    """Days since last sign-flip in the 1-day diff of the 63-day SMA."""
    slope = _rolling_mean(close, _TD_QTR).diff(1)
    flip = _sign_flip(slope)
    return _days_since_flip(flip)


def vif_024_days_since_macd_zero_cross(close: pd.Series) -> pd.Series:
    """Days since last MACD zero-crossing (either direction)."""
    macd = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    flip = _sign_flip(macd)
    return _days_since_flip(flip)


def vif_025_days_since_neg_vel_flip(close: pd.Series) -> pd.Series:
    """Days since last bearish EMA-21 velocity flip (positive-to-negative only)."""
    flip = vif_011_vel_flip_ema21_to_neg_flag(close)
    return _days_since_flip(flip)


def vif_026_days_since_pos_vel_flip(close: pd.Series) -> pd.Series:
    """Days since last bullish EMA-21 velocity flip (negative-to-positive only)."""
    flip = vif_012_vel_flip_ema21_to_pos_flag(close)
    return _days_since_flip(flip)


def vif_027_days_since_ema5_neg_flip_log(close: pd.Series) -> pd.Series:
    """Log1p of days since last bearish EMA-5 velocity flip."""
    d = _days_since_flip(vif_009_vel_flip_ema5_to_neg_flag(close))
    return np.log1p(d.clip(lower=0))


def vif_028_days_since_ema21_neg_flip_norm(close: pd.Series) -> pd.Series:
    """Days since last bearish EMA-21 flip normalized by 252-day avg."""
    d = _days_since_flip(vif_011_vel_flip_ema21_to_neg_flag(close))
    avg = _rolling_mean(d, _TD_YEAR)
    return _safe_div(d, avg)


def vif_029_days_since_sma5_flip_norm_252d(close: pd.Series) -> pd.Series:
    """Days since last SMA-5 slope flip, normalized by 252-day average."""
    slope = _rolling_mean(close, _TD_WEEK).diff(1)
    d = _days_since_flip(_sign_flip(slope))
    avg = _rolling_mean(d, _TD_YEAR)
    return _safe_div(d, avg)


def vif_030_days_since_macd_neg_cross(close: pd.Series) -> pd.Series:
    """Days since last bearish MACD zero-cross (MACD crossed below zero)."""
    flip = vif_014_vel_flip_macd_zero_cross_neg(close)
    return _days_since_flip(flip)


# --- Group C (031-045): Count of inflections in rolling windows ---

def vif_031_inflection_count_ema5_21d(close: pd.Series) -> pd.Series:
    """Count of EMA-5 velocity sign-flips in trailing 21 days."""
    return _rolling_count(vif_001_vel_flip_ema5_flag(close), _TD_MON)


def vif_032_inflection_count_ema5_63d(close: pd.Series) -> pd.Series:
    """Count of EMA-5 velocity sign-flips in trailing 63 days."""
    return _rolling_count(vif_001_vel_flip_ema5_flag(close), _TD_QTR)


def vif_033_inflection_count_ema5_252d(close: pd.Series) -> pd.Series:
    """Count of EMA-5 velocity sign-flips in trailing 252 days."""
    return _rolling_count(vif_001_vel_flip_ema5_flag(close), _TD_YEAR)


def vif_034_inflection_count_ema21_63d(close: pd.Series) -> pd.Series:
    """Count of EMA-21 velocity sign-flips in trailing 63 days."""
    return _rolling_count(vif_003_vel_flip_ema21_flag(close), _TD_QTR)


def vif_035_inflection_count_ema21_252d(close: pd.Series) -> pd.Series:
    """Count of EMA-21 velocity sign-flips in trailing 252 days."""
    return _rolling_count(vif_003_vel_flip_ema21_flag(close), _TD_YEAR)


def vif_036_inflection_count_raw_21d(close: pd.Series) -> pd.Series:
    """Count of raw 1-day return sign-flips in trailing 21 days."""
    lr = _log_safe(close).diff(1)
    return _rolling_count(_sign_flip(lr), _TD_MON)


def vif_037_inflection_count_sma5_slope_21d(close: pd.Series) -> pd.Series:
    """Count of SMA-5 slope sign-flips in trailing 21 days."""
    return _rolling_count(vif_006_vel_flip_sma5_slope_flag(close), _TD_MON)


def vif_038_inflection_count_sma21_slope_63d(close: pd.Series) -> pd.Series:
    """Count of SMA-21 slope sign-flips in trailing 63 days."""
    return _rolling_count(vif_007_vel_flip_sma21_slope_flag(close), _TD_QTR)


def vif_039_inflection_count_macd_252d(close: pd.Series) -> pd.Series:
    """Count of MACD zero-crossings (either direction) in trailing 252 days."""
    macd = _ewm_mean(close, 12) - _ewm_mean(close, 26)
    return _rolling_count(_sign_flip(macd), _TD_YEAR)


def vif_040_neg_inflection_count_ema21_252d(close: pd.Series) -> pd.Series:
    """Count of bearish EMA-21 velocity flips in trailing 252 days."""
    return _rolling_count(vif_011_vel_flip_ema21_to_neg_flag(close), _TD_YEAR)


def vif_041_pos_inflection_count_ema21_252d(close: pd.Series) -> pd.Series:
    """Count of bullish EMA-21 velocity flips in trailing 252 days."""
    return _rolling_count(vif_012_vel_flip_ema21_to_pos_flag(close), _TD_YEAR)


def vif_042_neg_vs_pos_inflection_ratio_252d(close: pd.Series) -> pd.Series:
    """Ratio of bearish to bullish EMA-21 inflections over 252 days."""
    neg = _rolling_count(vif_011_vel_flip_ema21_to_neg_flag(close), _TD_YEAR)
    pos = _rolling_count(vif_012_vel_flip_ema21_to_pos_flag(close), _TD_YEAR)
    return _safe_div(neg, pos)


def vif_043_inflection_count_ema5_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day EMA-5 inflection count within trailing 252 days."""
    cnt = _rolling_count(vif_001_vel_flip_ema5_flag(close), _TD_MON)
    return cnt.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vif_044_inflection_count_sma5_252d(close: pd.Series) -> pd.Series:
    """Count of SMA-5 slope sign-flips in trailing 252 days."""
    return _rolling_count(vif_006_vel_flip_sma5_slope_flag(close), _TD_YEAR)


def vif_045_inflection_freq_21d_vs_252d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of 21-day EMA-5 flip count to 252-day avg (recent vs historical freq)."""
    cnt21 = _rolling_count(vif_001_vel_flip_ema5_flag(close), _TD_MON)
    avg = _rolling_mean(cnt21, _TD_YEAR)
    return _safe_div(cnt21, avg)


# --- Group D (046-060): Velocity magnitude at/around inflection points ---

def vif_046_vel_mag_at_ema5_flip(close: pd.Series) -> pd.Series:
    """Absolute EMA-5 velocity magnitude on the day of a sign-flip, else NaN forward-filled."""
    v = _velocity(close, 5)
    flip = _sign_flip(v)
    mag = v.abs().where(flip == 1, np.nan)
    return mag.ffill()


def vif_047_vel_mag_at_ema21_flip(close: pd.Series) -> pd.Series:
    """Absolute EMA-21 velocity magnitude on sign-flip day, forward-filled."""
    v = _velocity(close, _TD_MON)
    flip = _sign_flip(v)
    mag = v.abs().where(flip == 1, np.nan)
    return mag.ffill()


def vif_048_vel_at_last_neg_flip_ema5(close: pd.Series) -> pd.Series:
    """EMA-5 velocity level on the most recent bearish flip, forward-filled."""
    v = _velocity(close, 5)
    flip = vif_009_vel_flip_ema5_to_neg_flag(close)
    val = v.where(flip == 1, np.nan)
    return val.ffill()


def vif_049_vel_at_last_pos_flip_ema5(close: pd.Series) -> pd.Series:
    """EMA-5 velocity level on the most recent bullish flip, forward-filled."""
    v = _velocity(close, 5)
    flip = vif_010_vel_flip_ema5_to_pos_flag(close)
    val = v.where(flip == 1, np.nan)
    return val.ffill()


def vif_050_vel_at_last_neg_flip_ema21(close: pd.Series) -> pd.Series:
    """EMA-21 velocity level on the most recent bearish flip, forward-filled."""
    v = _velocity(close, _TD_MON)
    flip = vif_011_vel_flip_ema21_to_neg_flag(close)
    val = v.where(flip == 1, np.nan)
    return val.ffill()


def vif_051_avg_vel_mag_at_flip_ema5_63d(close: pd.Series) -> pd.Series:
    """Average absolute EMA-5 velocity at flip points over trailing 63 days."""
    v = _velocity(close, 5)
    flip = _sign_flip(v)
    mag_on_flip = v.abs().where(flip == 1, np.nan)
    return mag_on_flip.rolling(_TD_QTR, min_periods=1).mean()


def vif_052_avg_vel_mag_at_flip_ema21_252d(close: pd.Series) -> pd.Series:
    """Average absolute EMA-21 velocity at flip points over trailing 252 days."""
    v = _velocity(close, _TD_MON)
    flip = _sign_flip(v)
    mag_on_flip = v.abs().where(flip == 1, np.nan)
    return mag_on_flip.rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def vif_053_vel_at_flip_vs_current_ema5(close: pd.Series) -> pd.Series:
    """Current EMA-5 velocity vs velocity at last flip (measures drift since inflection)."""
    v = _velocity(close, 5)
    flip = _sign_flip(v)
    at_flip = v.where(flip == 1, np.nan).ffill()
    return v - at_flip


def vif_054_vel_at_flip_vs_current_ema21(close: pd.Series) -> pd.Series:
    """Current EMA-21 velocity vs velocity at last flip."""
    v = _velocity(close, _TD_MON)
    flip = _sign_flip(v)
    at_flip = v.where(flip == 1, np.nan).ffill()
    return v - at_flip


def vif_055_vel_mag_at_neg_flip_ema5_norm(close: pd.Series) -> pd.Series:
    """Last-bearish-flip EMA-5 velocity magnitude normalized by 252-day avg magnitude."""
    v = _velocity(close, 5)
    flip = vif_009_vel_flip_ema5_to_neg_flag(close)
    mag = v.abs().where(flip == 1, np.nan).ffill()
    avg = _rolling_mean(v.abs(), _TD_YEAR)
    return _safe_div(mag, avg)


def vif_056_curvature_at_last_ema5_flip(close: pd.Series) -> pd.Series:
    """2nd derivative of EMA-5 velocity on last flip day, forward-filled."""
    v = _velocity(close, 5)
    curv = v.diff(1)
    flip = _sign_flip(v)
    curv_at_flip = curv.where(flip == 1, np.nan).ffill()
    return curv_at_flip


def vif_057_curvature_at_last_ema21_flip(close: pd.Series) -> pd.Series:
    """2nd derivative of EMA-21 velocity on last flip day, forward-filled."""
    v = _velocity(close, _TD_MON)
    curv = v.diff(1)
    flip = _sign_flip(v)
    curv_at_flip = curv.where(flip == 1, np.nan).ffill()
    return curv_at_flip


def vif_058_max_neg_vel_since_last_pos_flip(close: pd.Series) -> pd.Series:
    """Minimum (most negative) EMA-21 velocity since last bullish flip (depth of bear regime)."""
    v = _velocity(close, _TD_MON)
    pos_flip = vif_012_vel_flip_ema21_to_pos_flag(close)
    group = pos_flip.cumsum()
    return v.groupby(group).cummin()


def vif_059_max_pos_vel_since_last_neg_flip(close: pd.Series) -> pd.Series:
    """Maximum EMA-21 velocity since last bearish flip (strength of remaining bulls)."""
    v = _velocity(close, _TD_MON)
    neg_flip = vif_011_vel_flip_ema21_to_neg_flag(close)
    group = neg_flip.cumsum()
    return v.groupby(group).cummax()


def vif_060_vel_ema5_abs_at_flip_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of last-flip EMA-5 magnitude within trailing 252-day flip magnitudes."""
    v = _velocity(close, 5)
    flip = _sign_flip(v)
    mag = v.abs().where(flip == 1, np.nan).ffill()
    return mag.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group E (061-075): Alternating velocity regimes and curvature zero-crossings ---

def vif_061_cur_vel_sign_ema5(close: pd.Series) -> pd.Series:
    """Sign (+1/-1/0) of current EMA-5 velocity (current velocity regime)."""
    return np.sign(_velocity(close, 5)).astype(float)


def vif_062_cur_vel_sign_ema21(close: pd.Series) -> pd.Series:
    """Sign of current EMA-21 velocity (monthly velocity regime)."""
    return np.sign(_velocity(close, _TD_MON)).astype(float)


def vif_063_cur_vel_sign_ema63(close: pd.Series) -> pd.Series:
    """Sign of current EMA-63 velocity (quarterly velocity regime)."""
    return np.sign(_velocity(close, _TD_QTR)).astype(float)


def vif_064_vel_regime_ema5_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: currently in negative EMA-5 velocity regime."""
    return (np.sign(_velocity(close, 5)) < 0).astype(float)


def vif_065_vel_regime_ema21_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: currently in negative EMA-21 velocity regime."""
    return (np.sign(_velocity(close, _TD_MON)) < 0).astype(float)


def vif_066_vel_regime_ema63_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: currently in negative EMA-63 velocity regime."""
    return (np.sign(_velocity(close, _TD_QTR)) < 0).astype(float)


def vif_067_all_vel_regimes_neg_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-5, EMA-21, and EMA-63 velocities all negative simultaneously."""
    v5 = _velocity(close, 5)
    v21 = _velocity(close, _TD_MON)
    v63 = _velocity(close, _TD_QTR)
    return ((v5 < 0) & (v21 < 0) & (v63 < 0)).astype(float)


def vif_068_curvature_ema5_sign(close: pd.Series) -> pd.Series:
    """Sign of EMA-5 velocity 1-day change (curvature direction)."""
    v = _velocity(close, 5)
    return np.sign(v.diff(1)).astype(float)


def vif_069_curvature_ema21_sign(close: pd.Series) -> pd.Series:
    """Sign of EMA-21 velocity 1-day change (curvature direction)."""
    v = _velocity(close, _TD_MON)
    return np.sign(v.diff(1)).astype(float)


def vif_070_curvature_zero_cross_ema5(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 velocity curvature (2nd deriv) crossed zero today."""
    v = _velocity(close, 5)
    curv = v.diff(1)
    return _sign_flip(curv)


def vif_071_curvature_zero_cross_ema21(close: pd.Series) -> pd.Series:
    """Binary: EMA-21 velocity curvature (2nd deriv) crossed zero today."""
    v = _velocity(close, _TD_MON)
    curv = v.diff(1)
    return _sign_flip(curv)


def vif_072_curvature_count_ema5_21d(close: pd.Series) -> pd.Series:
    """Count of EMA-5 curvature zero-crossings in trailing 21 days."""
    return _rolling_count(vif_070_curvature_zero_cross_ema5(close), _TD_MON)


def vif_073_curvature_count_ema21_63d(close: pd.Series) -> pd.Series:
    """Count of EMA-21 curvature zero-crossings in trailing 63 days."""
    return _rolling_count(vif_071_curvature_zero_cross_ema21(close), _TD_QTR)


def vif_074_vel_regime_disagreement_flag(close: pd.Series) -> pd.Series:
    """Binary: EMA-5 and EMA-63 velocities have opposite signs (short vs long divergence)."""
    v5 = _velocity(close, 5)
    v63 = _velocity(close, _TD_QTR)
    return ((np.sign(v5) != np.sign(v63)) & v5.notna() & v63.notna()).astype(float)


def vif_075_consec_neg_vel_regime_ema21(close: pd.Series) -> pd.Series:
    """Consecutive days in negative EMA-21 velocity regime (current bear-velocity streak)."""
    cond = _velocity(close, _TD_MON) < 0
    c = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

VELOCITY_INFLECTION_REGISTRY_001_075 = {
    "vif_001_vel_flip_ema5_flag": {"inputs": ["close"], "func": vif_001_vel_flip_ema5_flag},
    "vif_002_vel_flip_ema10_flag": {"inputs": ["close"], "func": vif_002_vel_flip_ema10_flag},
    "vif_003_vel_flip_ema21_flag": {"inputs": ["close"], "func": vif_003_vel_flip_ema21_flag},
    "vif_004_vel_flip_ema63_flag": {"inputs": ["close"], "func": vif_004_vel_flip_ema63_flag},
    "vif_005_vel_flip_raw1d_flag": {"inputs": ["close"], "func": vif_005_vel_flip_raw1d_flag},
    "vif_006_vel_flip_sma5_slope_flag": {"inputs": ["close"], "func": vif_006_vel_flip_sma5_slope_flag},
    "vif_007_vel_flip_sma21_slope_flag": {"inputs": ["close"], "func": vif_007_vel_flip_sma21_slope_flag},
    "vif_008_vel_flip_sma63_slope_flag": {"inputs": ["close"], "func": vif_008_vel_flip_sma63_slope_flag},
    "vif_009_vel_flip_ema5_to_neg_flag": {"inputs": ["close"], "func": vif_009_vel_flip_ema5_to_neg_flag},
    "vif_010_vel_flip_ema5_to_pos_flag": {"inputs": ["close"], "func": vif_010_vel_flip_ema5_to_pos_flag},
    "vif_011_vel_flip_ema21_to_neg_flag": {"inputs": ["close"], "func": vif_011_vel_flip_ema21_to_neg_flag},
    "vif_012_vel_flip_ema21_to_pos_flag": {"inputs": ["close"], "func": vif_012_vel_flip_ema21_to_pos_flag},
    "vif_013_vel_flip_ema63_to_neg_flag": {"inputs": ["close"], "func": vif_013_vel_flip_ema63_to_neg_flag},
    "vif_014_vel_flip_macd_zero_cross_neg": {"inputs": ["close"], "func": vif_014_vel_flip_macd_zero_cross_neg},
    "vif_015_vel_flip_macd_zero_cross_pos": {"inputs": ["close"], "func": vif_015_vel_flip_macd_zero_cross_pos},
    "vif_016_days_since_ema5_vel_flip": {"inputs": ["close"], "func": vif_016_days_since_ema5_vel_flip},
    "vif_017_days_since_ema10_vel_flip": {"inputs": ["close"], "func": vif_017_days_since_ema10_vel_flip},
    "vif_018_days_since_ema21_vel_flip": {"inputs": ["close"], "func": vif_018_days_since_ema21_vel_flip},
    "vif_019_days_since_ema63_vel_flip": {"inputs": ["close"], "func": vif_019_days_since_ema63_vel_flip},
    "vif_020_days_since_raw_vel_flip": {"inputs": ["close"], "func": vif_020_days_since_raw_vel_flip},
    "vif_021_days_since_sma5_slope_flip": {"inputs": ["close"], "func": vif_021_days_since_sma5_slope_flip},
    "vif_022_days_since_sma21_slope_flip": {"inputs": ["close"], "func": vif_022_days_since_sma21_slope_flip},
    "vif_023_days_since_sma63_slope_flip": {"inputs": ["close"], "func": vif_023_days_since_sma63_slope_flip},
    "vif_024_days_since_macd_zero_cross": {"inputs": ["close"], "func": vif_024_days_since_macd_zero_cross},
    "vif_025_days_since_neg_vel_flip": {"inputs": ["close"], "func": vif_025_days_since_neg_vel_flip},
    "vif_026_days_since_pos_vel_flip": {"inputs": ["close"], "func": vif_026_days_since_pos_vel_flip},
    "vif_027_days_since_ema5_neg_flip_log": {"inputs": ["close"], "func": vif_027_days_since_ema5_neg_flip_log},
    "vif_028_days_since_ema21_neg_flip_norm": {"inputs": ["close"], "func": vif_028_days_since_ema21_neg_flip_norm},
    "vif_029_days_since_sma5_flip_norm_252d": {"inputs": ["close"], "func": vif_029_days_since_sma5_flip_norm_252d},
    "vif_030_days_since_macd_neg_cross": {"inputs": ["close"], "func": vif_030_days_since_macd_neg_cross},
    "vif_031_inflection_count_ema5_21d": {"inputs": ["close"], "func": vif_031_inflection_count_ema5_21d},
    "vif_032_inflection_count_ema5_63d": {"inputs": ["close"], "func": vif_032_inflection_count_ema5_63d},
    "vif_033_inflection_count_ema5_252d": {"inputs": ["close"], "func": vif_033_inflection_count_ema5_252d},
    "vif_034_inflection_count_ema21_63d": {"inputs": ["close"], "func": vif_034_inflection_count_ema21_63d},
    "vif_035_inflection_count_ema21_252d": {"inputs": ["close"], "func": vif_035_inflection_count_ema21_252d},
    "vif_036_inflection_count_raw_21d": {"inputs": ["close"], "func": vif_036_inflection_count_raw_21d},
    "vif_037_inflection_count_sma5_slope_21d": {"inputs": ["close"], "func": vif_037_inflection_count_sma5_slope_21d},
    "vif_038_inflection_count_sma21_slope_63d": {"inputs": ["close"], "func": vif_038_inflection_count_sma21_slope_63d},
    "vif_039_inflection_count_macd_252d": {"inputs": ["close"], "func": vif_039_inflection_count_macd_252d},
    "vif_040_neg_inflection_count_ema21_252d": {"inputs": ["close"], "func": vif_040_neg_inflection_count_ema21_252d},
    "vif_041_pos_inflection_count_ema21_252d": {"inputs": ["close"], "func": vif_041_pos_inflection_count_ema21_252d},
    "vif_042_neg_vs_pos_inflection_ratio_252d": {"inputs": ["close"], "func": vif_042_neg_vs_pos_inflection_ratio_252d},
    "vif_043_inflection_count_ema5_pct_rank_252d": {"inputs": ["close"], "func": vif_043_inflection_count_ema5_pct_rank_252d},
    "vif_044_inflection_count_sma5_252d": {"inputs": ["close"], "func": vif_044_inflection_count_sma5_252d},
    "vif_045_inflection_freq_21d_vs_252d_ratio": {"inputs": ["close"], "func": vif_045_inflection_freq_21d_vs_252d_ratio},
    "vif_046_vel_mag_at_ema5_flip": {"inputs": ["close"], "func": vif_046_vel_mag_at_ema5_flip},
    "vif_047_vel_mag_at_ema21_flip": {"inputs": ["close"], "func": vif_047_vel_mag_at_ema21_flip},
    "vif_048_vel_at_last_neg_flip_ema5": {"inputs": ["close"], "func": vif_048_vel_at_last_neg_flip_ema5},
    "vif_049_vel_at_last_pos_flip_ema5": {"inputs": ["close"], "func": vif_049_vel_at_last_pos_flip_ema5},
    "vif_050_vel_at_last_neg_flip_ema21": {"inputs": ["close"], "func": vif_050_vel_at_last_neg_flip_ema21},
    "vif_051_avg_vel_mag_at_flip_ema5_63d": {"inputs": ["close"], "func": vif_051_avg_vel_mag_at_flip_ema5_63d},
    "vif_052_avg_vel_mag_at_flip_ema21_252d": {"inputs": ["close"], "func": vif_052_avg_vel_mag_at_flip_ema21_252d},
    "vif_053_vel_at_flip_vs_current_ema5": {"inputs": ["close"], "func": vif_053_vel_at_flip_vs_current_ema5},
    "vif_054_vel_at_flip_vs_current_ema21": {"inputs": ["close"], "func": vif_054_vel_at_flip_vs_current_ema21},
    "vif_055_vel_mag_at_neg_flip_ema5_norm": {"inputs": ["close"], "func": vif_055_vel_mag_at_neg_flip_ema5_norm},
    "vif_056_curvature_at_last_ema5_flip": {"inputs": ["close"], "func": vif_056_curvature_at_last_ema5_flip},
    "vif_057_curvature_at_last_ema21_flip": {"inputs": ["close"], "func": vif_057_curvature_at_last_ema21_flip},
    "vif_058_max_neg_vel_since_last_pos_flip": {"inputs": ["close"], "func": vif_058_max_neg_vel_since_last_pos_flip},
    "vif_059_max_pos_vel_since_last_neg_flip": {"inputs": ["close"], "func": vif_059_max_pos_vel_since_last_neg_flip},
    "vif_060_vel_ema5_abs_at_flip_pct_rank_252d": {"inputs": ["close"], "func": vif_060_vel_ema5_abs_at_flip_pct_rank_252d},
    "vif_061_cur_vel_sign_ema5": {"inputs": ["close"], "func": vif_061_cur_vel_sign_ema5},
    "vif_062_cur_vel_sign_ema21": {"inputs": ["close"], "func": vif_062_cur_vel_sign_ema21},
    "vif_063_cur_vel_sign_ema63": {"inputs": ["close"], "func": vif_063_cur_vel_sign_ema63},
    "vif_064_vel_regime_ema5_neg_flag": {"inputs": ["close"], "func": vif_064_vel_regime_ema5_neg_flag},
    "vif_065_vel_regime_ema21_neg_flag": {"inputs": ["close"], "func": vif_065_vel_regime_ema21_neg_flag},
    "vif_066_vel_regime_ema63_neg_flag": {"inputs": ["close"], "func": vif_066_vel_regime_ema63_neg_flag},
    "vif_067_all_vel_regimes_neg_flag": {"inputs": ["close"], "func": vif_067_all_vel_regimes_neg_flag},
    "vif_068_curvature_ema5_sign": {"inputs": ["close"], "func": vif_068_curvature_ema5_sign},
    "vif_069_curvature_ema21_sign": {"inputs": ["close"], "func": vif_069_curvature_ema21_sign},
    "vif_070_curvature_zero_cross_ema5": {"inputs": ["close"], "func": vif_070_curvature_zero_cross_ema5},
    "vif_071_curvature_zero_cross_ema21": {"inputs": ["close"], "func": vif_071_curvature_zero_cross_ema21},
    "vif_072_curvature_count_ema5_21d": {"inputs": ["close"], "func": vif_072_curvature_count_ema5_21d},
    "vif_073_curvature_count_ema21_63d": {"inputs": ["close"], "func": vif_073_curvature_count_ema21_63d},
    "vif_074_vel_regime_disagreement_flag": {"inputs": ["close"], "func": vif_074_vel_regime_disagreement_flag},
    "vif_075_consec_neg_vel_regime_ema21": {"inputs": ["close"], "func": vif_075_consec_neg_vel_regime_ema21},
}
