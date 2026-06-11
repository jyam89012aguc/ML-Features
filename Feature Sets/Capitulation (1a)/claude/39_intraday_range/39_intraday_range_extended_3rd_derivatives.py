"""
39_intraday_range — Extended 3rd Derivatives (Features extdrv3_001-025)
Domain: rate of change of extended 2nd-derivative intraday-range concepts — acceleration
        of Parkinson/GK velocity, close-position-in-range velocity, range z-score on new
        windows, range-volume product velocity, distribution shape velocity, and
        capitulation-composite velocity from the extended feature layer.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _hl_range_over_close(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return _safe_div(high - low, close)


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Parkinson volatility over window w."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    return np.sqrt(_rolling_mean(log_hl ** 2, w) / (4.0 * np.log(2.0) + _EPS))


def _close_position_in_range(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Close position within day's range: (close - low) / (high - low)."""
    return _safe_div(close - low, (high - low).replace(0, np.nan))


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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each = diff or slope applied to a 2nd-derivative concept from the extended layer

def idr_extdrv3_001_parkinson_vol_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Parkinson volatility (acceleration of range-vol velocity)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vel = pv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_002_parkinson_vol_21d_21d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 21-day Parkinson vol (jerk of monthly vol velocity)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vel21 = pv.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_extdrv3_003_parkinson_vol_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day Parkinson volatility."""
    pv = _parkinson_vol(high, low, _TD_QTR)
    vel = pv.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_004_gk_vol_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day Garman-Klass vol (GK vol acceleration)."""
    log_hl = np.log((high / low.replace(0, np.nan)).clip(lower=_EPS))
    log_co = np.log((close / open.replace(0, np.nan)).clip(lower=_EPS))
    gk_daily = 0.5 * log_hl ** 2 - (2.0 * np.log(2.0) - 1.0) * log_co ** 2
    gk21 = np.sqrt(_rolling_mean(gk_daily.clip(lower=0), _TD_MON))
    vel = gk21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_005_close_pos_in_range_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of close position in range (acceleration of intraday close bias)."""
    pos = _close_position_in_range(high, low, close)
    vel = pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_006_avg_close_pos_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day average close position in range."""
    pos = _close_position_in_range(high, low, close)
    avg_pos = _rolling_mean(pos, _TD_MON)
    vel = avg_pos.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_007_range_zscore_126d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day range z-score (acceleration of half-year extremity)."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_008_range_zscore_126d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 126-day range z-score."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_extdrv3_009_range_vol_product_zscore_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day z-score of range × volume product."""
    rv = _hl_range_over_close(high, low, close) * volume
    z = _safe_div(rv - _rolling_mean(rv, _TD_QTR), _rolling_std(rv, _TD_QTR))
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_010_vol_weighted_range_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day volume-weighted average range."""
    r = _hl_range_over_close(high, low, close)
    vol_sum = _rolling_sum(volume, _TD_MON).replace(0, np.nan)
    vwr = _safe_div(_rolling_sum(r * volume, _TD_MON), vol_sum)
    vel = vwr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_011_range_iqr_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day IQR of normalized range (IQR acceleration)."""
    r = _hl_range_over_close(high, low, close)
    q75 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = r.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    iqr = q75 - q25
    vel = iqr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_012_range_skew_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day skewness of range (skewness jerk)."""
    r = _hl_range_over_close(high, low, close)
    skew = r.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    vel21 = skew.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_extdrv3_013_range_kurt_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day kurtosis of range."""
    r = _hl_range_over_close(high, low, close)
    kurt = r.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()
    vel21 = kurt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_extdrv3_014_range_pct_rank_126d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 126-day percentile rank of range (rank acceleration)."""
    r = _hl_range_over_close(high, low, close)
    rank = r.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)
    vel = rank.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_015_parkinson_vol_ratio_5d_diff_5d_diff(high: pd.Series, low: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/63d Parkinson vol ratio (vol-ratio acceleration)."""
    pv21 = _parkinson_vol(high, low, _TD_MON)
    pv63 = _parkinson_vol(high, low, _TD_QTR)
    ratio = _safe_div(pv21, pv63)
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_016_range_ewm_zscore_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of EWM(21) range z-score vs 63-day baseline."""
    r_ewm = _ewm_mean(_hl_range_over_close(high, low, close), _TD_MON)
    m = _rolling_mean(r_ewm, _TD_QTR)
    s = _rolling_std(r_ewm, _TD_QTR)
    z = _safe_div(r_ewm - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_017_avg_range_ewm_126d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in EWM(126) normalized range."""
    ewm = _ewm_mean(_hl_range_over_close(high, low, close), _TD_HALF)
    vel21 = ewm.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_extdrv3_018_range_median_zscore_63d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of 63-day robust median z-score of range."""
    r = _hl_range_over_close(high, low, close)
    med = _rolling_median(r, _TD_QTR)
    mad = (r - med).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).median()
    mz = _safe_div(r - med, mad * 1.4826 + _EPS)
    vel = mz.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_019_close_near_low_flag_21d_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Second 5-day diff of count of close-near-low days in 21d (bearish-close acceleration)."""
    rng = (high - low).replace(0, np.nan)
    pos = _safe_div(close - low, rng)
    cnt = _rolling_sum((pos < 0.25).astype(float), _TD_MON)
    vel = cnt.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_020_range_capitulation_score_5d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Second 5-day diff of range capitulation score (acceleration of score velocity)."""
    r = _hl_range_over_close(high, low, close)
    m = _rolling_mean(r, _TD_YEAR)
    s = _rolling_std(r, _TD_YEAR)
    z252 = _safe_div(r - m, s).clip(lower=0)
    p252 = r.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).rank(pct=True)
    is_dn = (close < close.shift(1)).astype(float)
    dn_frac = _rolling_mean(is_dn, _TD_MON)
    score = z252 * p252 * dn_frac
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def idr_extdrv3_021_parkinson_vol_21d_5d_diff_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 21-day Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vel = pv.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_extdrv3_022_range_zscore_126d_5d_diff_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of 126-day range z-score."""
    r = _hl_range_over_close(high, low, close)
    z = _safe_div(r - _rolling_mean(r, _TD_HALF), _rolling_std(r, _TD_HALF))
    vel = z.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_extdrv3_023_avg_close_pos_21d_5d_diff_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day velocity of avg close position in range."""
    pos = _close_position_in_range(high, low, close)
    avg_pos = _rolling_mean(pos, _TD_MON)
    vel = avg_pos.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def idr_extdrv3_024_log_range_mean_63d_21d_diff_5d_diff(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day mean of log(normalized range)."""
    r = _hl_range_over_close(high, low, close).clip(lower=_EPS)
    log_r_mean = _rolling_mean(np.log(r), _TD_QTR)
    vel21 = log_r_mean.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def idr_extdrv3_025_parkinson_vol_63d_5d_diff_slope_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope over 63 days of the 5-day velocity of 63-day Parkinson vol."""
    pv = _parkinson_vol(high, low, _TD_QTR)
    vel = pv.diff(_TD_WEEK)
    return _linslope(vel, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

INTRADAY_RANGE_EXTENDED_REGISTRY_3RD_DERIVATIVES = {
    "idr_extdrv3_001_parkinson_vol_21d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": idr_extdrv3_001_parkinson_vol_21d_5d_diff_5d_diff},
    "idr_extdrv3_002_parkinson_vol_21d_21d_diff_5d_diff": {"inputs": ["high", "low"], "func": idr_extdrv3_002_parkinson_vol_21d_21d_diff_5d_diff},
    "idr_extdrv3_003_parkinson_vol_63d_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": idr_extdrv3_003_parkinson_vol_63d_5d_diff_5d_diff},
    "idr_extdrv3_004_gk_vol_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "open"], "func": idr_extdrv3_004_gk_vol_21d_5d_diff_5d_diff},
    "idr_extdrv3_005_close_pos_in_range_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_005_close_pos_in_range_5d_diff_5d_diff},
    "idr_extdrv3_006_avg_close_pos_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_006_avg_close_pos_21d_5d_diff_5d_diff},
    "idr_extdrv3_007_range_zscore_126d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_007_range_zscore_126d_5d_diff_5d_diff},
    "idr_extdrv3_008_range_zscore_126d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_008_range_zscore_126d_21d_diff_5d_diff},
    "idr_extdrv3_009_range_vol_product_zscore_63d_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": idr_extdrv3_009_range_vol_product_zscore_63d_5d_diff_5d_diff},
    "idr_extdrv3_010_vol_weighted_range_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": idr_extdrv3_010_vol_weighted_range_21d_5d_diff_5d_diff},
    "idr_extdrv3_011_range_iqr_63d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_011_range_iqr_63d_5d_diff_5d_diff},
    "idr_extdrv3_012_range_skew_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_012_range_skew_63d_21d_diff_5d_diff},
    "idr_extdrv3_013_range_kurt_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_013_range_kurt_63d_21d_diff_5d_diff},
    "idr_extdrv3_014_range_pct_rank_126d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_014_range_pct_rank_126d_5d_diff_5d_diff},
    "idr_extdrv3_015_parkinson_vol_ratio_5d_diff_5d_diff": {"inputs": ["high", "low"], "func": idr_extdrv3_015_parkinson_vol_ratio_5d_diff_5d_diff},
    "idr_extdrv3_016_range_ewm_zscore_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_016_range_ewm_zscore_21d_5d_diff_5d_diff},
    "idr_extdrv3_017_avg_range_ewm_126d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_017_avg_range_ewm_126d_21d_diff_5d_diff},
    "idr_extdrv3_018_range_median_zscore_63d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_018_range_median_zscore_63d_5d_diff_5d_diff},
    "idr_extdrv3_019_close_near_low_flag_21d_5d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_019_close_near_low_flag_21d_5d_diff_5d_diff},
    "idr_extdrv3_020_range_capitulation_score_5d_diff_5d_diff": {"inputs": ["high", "low", "close", "volume"], "func": idr_extdrv3_020_range_capitulation_score_5d_diff_5d_diff},
    "idr_extdrv3_021_parkinson_vol_21d_5d_diff_slope_21d": {"inputs": ["high", "low"], "func": idr_extdrv3_021_parkinson_vol_21d_5d_diff_slope_21d},
    "idr_extdrv3_022_range_zscore_126d_5d_diff_slope_21d": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_022_range_zscore_126d_5d_diff_slope_21d},
    "idr_extdrv3_023_avg_close_pos_21d_5d_diff_slope_21d": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_023_avg_close_pos_21d_5d_diff_slope_21d},
    "idr_extdrv3_024_log_range_mean_63d_21d_diff_5d_diff": {"inputs": ["high", "low", "close"], "func": idr_extdrv3_024_log_range_mean_63d_21d_diff_5d_diff},
    "idr_extdrv3_025_parkinson_vol_63d_5d_diff_slope_63d": {"inputs": ["high", "low"], "func": idr_extdrv3_025_parkinson_vol_63d_5d_diff_slope_63d},
}
