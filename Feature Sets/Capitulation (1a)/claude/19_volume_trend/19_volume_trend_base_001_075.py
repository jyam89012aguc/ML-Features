"""
19_volume_trend — Base Features 001-100
Domain: directional drift/slope/trend of volume over multi-week and multi-month windows
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
    """Rolling mean with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    """Rolling std with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    """Rolling sum with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    """Rolling min with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    """Rolling max with half-window min_periods."""
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    """Exponential weighted mean."""
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    """Log of series clipped at EPS."""
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope of s over w periods (unnormalized)."""
    def _slope(x):
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
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _linslope_rsq(s: pd.Series, w: int) -> pd.Series:
    """Rolling R-squared of OLS line fit of s over w periods."""
    def _rsq(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        ss_tot = ((x - x_m) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        slope = num / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        ss_res = (resid ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_rsq, raw=False)


def _count_rising(s: pd.Series, w: int) -> pd.Series:
    """Count of periods where s > s.shift(1) within rolling window w."""
    rising = (s > s.shift(1)).astype(float)
    return rising.rolling(w, min_periods=max(1, w // 2)).sum()


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): OLS slope of raw volume over multiple windows ---

def vtr_001_vol_ols_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over trailing 21-day window."""
    return _linslope(volume, _TD_MON)


def vtr_002_vol_ols_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over trailing 63-day window."""
    return _linslope(volume, _TD_QTR)


def vtr_003_vol_ols_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over trailing 126-day window."""
    return _linslope(volume, _TD_HALF)


def vtr_004_vol_ols_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over trailing 252-day window."""
    return _linslope(volume, _TD_YEAR)


def vtr_005_vol_ols_slope_21d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 21-day OLS volume slope (+1 rising, -1 falling, 0 flat)."""
    return np.sign(vtr_001_vol_ols_slope_21d(volume))


def vtr_006_vol_ols_slope_63d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 63-day OLS volume slope."""
    return np.sign(vtr_002_vol_ols_slope_63d(volume))


def vtr_007_vol_ols_slope_126d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 126-day OLS volume slope."""
    return np.sign(vtr_003_vol_ols_slope_126d(volume))


def vtr_008_vol_ols_slope_252d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 252-day OLS volume slope."""
    return np.sign(vtr_004_vol_ols_slope_252d(volume))


def vtr_009_vol_ols_slope_21d_norm(volume: pd.Series) -> pd.Series:
    """21-day OLS slope normalized by 21-day mean volume (scale-free)."""
    slope = _linslope(volume, _TD_MON)
    avg = _rolling_mean(volume, _TD_MON)
    return _safe_div(slope, avg)


def vtr_010_vol_ols_slope_63d_norm(volume: pd.Series) -> pd.Series:
    """63-day OLS slope normalized by 63-day mean volume."""
    slope = _linslope(volume, _TD_QTR)
    avg = _rolling_mean(volume, _TD_QTR)
    return _safe_div(slope, avg)


def vtr_011_vol_ols_slope_126d_norm(volume: pd.Series) -> pd.Series:
    """126-day OLS slope normalized by 126-day mean volume."""
    slope = _linslope(volume, _TD_HALF)
    avg = _rolling_mean(volume, _TD_HALF)
    return _safe_div(slope, avg)


def vtr_012_vol_ols_slope_252d_norm(volume: pd.Series) -> pd.Series:
    """252-day OLS slope normalized by 252-day mean volume."""
    slope = _linslope(volume, _TD_YEAR)
    avg = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(slope, avg)


# --- Group B (013-024): OLS slope of log-volume over multiple windows ---

def vtr_013_logvol_ols_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 21-day window."""
    return _linslope(_log_safe(volume), _TD_MON)


def vtr_014_logvol_ols_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 63-day window."""
    return _linslope(_log_safe(volume), _TD_QTR)


def vtr_015_logvol_ols_slope_126d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 126-day window."""
    return _linslope(_log_safe(volume), _TD_HALF)


def vtr_016_logvol_ols_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 252-day window."""
    return _linslope(_log_safe(volume), _TD_YEAR)


def vtr_017_logvol_ols_slope_21d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 21-day log-volume OLS slope."""
    return np.sign(vtr_013_logvol_ols_slope_21d(volume))


def vtr_018_logvol_ols_slope_63d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 63-day log-volume OLS slope."""
    return np.sign(vtr_014_logvol_ols_slope_63d(volume))


def vtr_019_logvol_ols_slope_126d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 126-day log-volume OLS slope."""
    return np.sign(vtr_015_logvol_ols_slope_126d(volume))


def vtr_020_logvol_ols_slope_252d_sign(volume: pd.Series) -> pd.Series:
    """Sign of 252-day log-volume OLS slope."""
    return np.sign(vtr_016_logvol_ols_slope_252d(volume))


def vtr_021_logvol_slope_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 21-day log-vol slope within trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_022_logvol_slope_63d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 63-day log-vol slope within trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_QTR)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_023_logvol_slope_126d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 126-day log-vol slope within trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_HALF)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_024_logvol_slope_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day log-vol slope relative to 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_MON)
    m = _rolling_mean(slope, _TD_YEAR)
    s = _rolling_std(slope, _TD_YEAR)
    return _safe_div(slope - m, s)


# --- Group C (025-036): EMA fast-vs-slow crossover ratios ---

def vtr_025_vol_ema5_vs_ema21_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA volume to 21-day EMA volume (fast vs slow trend)."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_MON))


def vtr_026_vol_ema5_vs_ema63_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day EMA volume to 63-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_WEEK), _ewm_mean(volume, _TD_QTR))


def vtr_027_vol_ema21_vs_ema63_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day EMA volume to 63-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_QTR))


def vtr_028_vol_ema21_vs_ema126_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day EMA volume to 126-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_MON), _ewm_mean(volume, _TD_HALF))


def vtr_029_vol_ema63_vs_ema252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day EMA volume to 252-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_QTR), _ewm_mean(volume, _TD_YEAR))


def vtr_030_vol_ema5_vs_ema21_diff(volume: pd.Series) -> pd.Series:
    """Difference (fast minus slow EMA) of volume: EMA5 minus EMA21."""
    return _ewm_mean(volume, _TD_WEEK) - _ewm_mean(volume, _TD_MON)


def vtr_031_vol_ema21_vs_ema63_diff(volume: pd.Series) -> pd.Series:
    """Difference of volume EMA21 minus EMA63."""
    return _ewm_mean(volume, _TD_MON) - _ewm_mean(volume, _TD_QTR)


def vtr_032_vol_ema21_vs_ema63_sign(volume: pd.Series) -> pd.Series:
    """Sign of EMA21-vs-EMA63 volume crossover (+1 = short-term above long-term)."""
    return np.sign(_ewm_mean(volume, _TD_MON) - _ewm_mean(volume, _TD_QTR))


def vtr_033_vol_ema63_vs_ema252_sign(volume: pd.Series) -> pd.Series:
    """Sign of EMA63-vs-EMA252 volume crossover."""
    return np.sign(_ewm_mean(volume, _TD_QTR) - _ewm_mean(volume, _TD_YEAR))


def vtr_034_vol_ema5_above_ema63_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA5 volume > EMA63 volume (short-term vol spike above medium trend)."""
    return (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_QTR)).astype(float)


def vtr_035_vol_ema21_above_ema252_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA21 volume > EMA252 volume (recent activity exceeds annual average)."""
    return (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_YEAR)).astype(float)


def vtr_036_vol_ema_crossover_score(volume: pd.Series) -> pd.Series:
    """Sum of three EMA crossover signs: E5>E21 + E21>E63 + E63>E252 (0-3 scale)."""
    s1 = (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_MON)).astype(float)
    s2 = (_ewm_mean(volume, _TD_MON) > _ewm_mean(volume, _TD_QTR)).astype(float)
    s3 = (_ewm_mean(volume, _TD_QTR) > _ewm_mean(volume, _TD_YEAR)).astype(float)
    return s1 + s2 + s3


# --- Group D (037-048): SMA-based volume moving-average ratios ---

def vtr_037_vol_sma5_vs_sma21_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day SMA volume to 21-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_MON))


def vtr_038_vol_sma21_vs_sma63_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day SMA volume to 63-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_QTR))


def vtr_039_vol_sma21_vs_sma126_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day SMA volume to 126-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_HALF))


def vtr_040_vol_sma21_vs_sma252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day SMA volume to 252-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_MON), _rolling_mean(volume, _TD_YEAR))


def vtr_041_vol_sma63_vs_sma252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day SMA volume to 252-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_mean(volume, _TD_YEAR))


def vtr_042_vol_sma5_vs_sma252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day SMA volume to 252-day SMA volume (shortest vs longest)."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_YEAR))


def vtr_043_vol_sma21_vs_sma63_diff_norm(volume: pd.Series) -> pd.Series:
    """Normalized difference: (SMA21 - SMA63) / SMA63."""
    s21 = _rolling_mean(volume, _TD_MON)
    s63 = _rolling_mean(volume, _TD_QTR)
    return _safe_div(s21 - s63, s63)


def vtr_044_vol_sma21_vs_sma252_diff_norm(volume: pd.Series) -> pd.Series:
    """Normalized difference: (SMA21 - SMA252) / SMA252."""
    s21 = _rolling_mean(volume, _TD_MON)
    s252 = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(s21 - s252, s252)


def vtr_045_vol_sma63_vs_sma252_diff_norm(volume: pd.Series) -> pd.Series:
    """Normalized difference: (SMA63 - SMA252) / SMA252."""
    s63 = _rolling_mean(volume, _TD_QTR)
    s252 = _rolling_mean(volume, _TD_YEAR)
    return _safe_div(s63 - s252, s252)


def vtr_046_vol_sma21_above_sma63_flag(volume: pd.Series) -> pd.Series:
    """Flag: SMA21 volume > SMA63 volume (short-term trend above medium)."""
    return (_rolling_mean(volume, _TD_MON) > _rolling_mean(volume, _TD_QTR)).astype(float)


def vtr_047_vol_sma63_above_sma252_flag(volume: pd.Series) -> pd.Series:
    """Flag: SMA63 volume > SMA252 volume (medium trend above annual)."""
    return (_rolling_mean(volume, _TD_QTR) > _rolling_mean(volume, _TD_YEAR)).astype(float)


def vtr_048_vol_sma_alignment_score(volume: pd.Series) -> pd.Series:
    """Count of aligned SMA ordering signals: SMA5>SMA21, SMA21>SMA63, SMA63>SMA252."""
    s5 = _rolling_mean(volume, _TD_WEEK)
    s21 = _rolling_mean(volume, _TD_MON)
    s63 = _rolling_mean(volume, _TD_QTR)
    s252 = _rolling_mean(volume, _TD_YEAR)
    return ((s5 > s21).astype(float) + (s21 > s63).astype(float)
            + (s63 > s252).astype(float))


# --- Group E (049-060): R-squared of volume trend (trend quality) ---

def vtr_049_vol_rsq_21d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 21 days."""
    return _linslope_rsq(volume, _TD_MON)


def vtr_050_vol_rsq_63d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 63 days."""
    return _linslope_rsq(volume, _TD_QTR)


def vtr_051_vol_rsq_126d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 126 days."""
    return _linslope_rsq(volume, _TD_HALF)


def vtr_052_vol_rsq_252d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 252 days."""
    return _linslope_rsq(volume, _TD_YEAR)


def vtr_053_logvol_rsq_21d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to log-volume over trailing 21 days."""
    return _linslope_rsq(_log_safe(volume), _TD_MON)


def vtr_054_logvol_rsq_63d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to log-volume over trailing 63 days."""
    return _linslope_rsq(_log_safe(volume), _TD_QTR)


def vtr_055_logvol_rsq_126d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to log-volume over trailing 126 days."""
    return _linslope_rsq(_log_safe(volume), _TD_HALF)


def vtr_056_logvol_rsq_252d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to log-volume over trailing 252 days."""
    return _linslope_rsq(_log_safe(volume), _TD_YEAR)


def vtr_057_vol_rsq_21d_signed(volume: pd.Series) -> pd.Series:
    """R-squared of 21-day volume trend, signed by slope direction."""
    rsq = _linslope_rsq(volume, _TD_MON)
    sgn = np.sign(_linslope(volume, _TD_MON))
    return rsq * sgn


def vtr_058_vol_rsq_63d_signed(volume: pd.Series) -> pd.Series:
    """R-squared of 63-day volume trend, signed by slope direction."""
    rsq = _linslope_rsq(volume, _TD_QTR)
    sgn = np.sign(_linslope(volume, _TD_QTR))
    return rsq * sgn


def vtr_059_logvol_rsq_21d_signed(volume: pd.Series) -> pd.Series:
    """Signed R-squared of 21-day log-volume trend."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_MON)
    sgn = np.sign(_linslope(_log_safe(volume), _TD_MON))
    return rsq * sgn


def vtr_060_logvol_rsq_63d_signed(volume: pd.Series) -> pd.Series:
    """Signed R-squared of 63-day log-volume trend."""
    rsq = _linslope_rsq(_log_safe(volume), _TD_QTR)
    sgn = np.sign(_linslope(_log_safe(volume), _TD_QTR))
    return rsq * sgn


# --- Group F (061-075): Rising-week share and drift consistency ---

def vtr_061_vol_rising_weeks_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of weeks with rising volume in trailing 63 days."""
    weekly_vol = volume.pct_change(_TD_WEEK)
    rising = (weekly_vol > 0).astype(float)
    return _rolling_mean(rising, _TD_QTR)


def vtr_062_vol_rising_weeks_frac_126d(volume: pd.Series) -> pd.Series:
    """Fraction of weeks with rising volume in trailing 126 days."""
    weekly_vol = volume.pct_change(_TD_WEEK)
    rising = (weekly_vol > 0).astype(float)
    return _rolling_mean(rising, _TD_HALF)


def vtr_063_vol_rising_weeks_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of weeks with rising volume in trailing 252 days."""
    weekly_vol = volume.pct_change(_TD_WEEK)
    rising = (weekly_vol > 0).astype(float)
    return _rolling_mean(rising, _TD_YEAR)


def vtr_064_vol_rising_days_frac_21d(volume: pd.Series) -> pd.Series:
    """Fraction of days with rising volume in trailing 21 days."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_mean(rising, _TD_MON)


def vtr_065_vol_rising_days_frac_63d(volume: pd.Series) -> pd.Series:
    """Fraction of days with rising volume in trailing 63 days."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_mean(rising, _TD_QTR)


def vtr_066_vol_rising_days_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of days with rising volume in trailing 252 days."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_mean(rising, _TD_YEAR)


def vtr_067_vol_rising_months_frac_252d(volume: pd.Series) -> pd.Series:
    """Fraction of 21-day periods with rising cumulative volume over 252 days."""
    monthly_vol = volume.pct_change(_TD_MON)
    rising = (monthly_vol > 0).astype(float)
    return _rolling_mean(rising, _TD_YEAR)


def vtr_068_vol_trend_consistency_21d(volume: pd.Series) -> pd.Series:
    """Consistency of daily volume changes: abs(sum_of_signs) / 21 (1=pure trend)."""
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum()
    return total_sign.abs() / _TD_MON


def vtr_069_vol_trend_consistency_63d(volume: pd.Series) -> pd.Series:
    """Consistency of daily volume changes over trailing 63 days."""
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()
    return total_sign.abs() / _TD_QTR


def vtr_070_vol_trend_consistency_252d(volume: pd.Series) -> pd.Series:
    """Consistency of daily volume changes over trailing 252 days."""
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).sum()
    return total_sign.abs() / _TD_YEAR


def vtr_071_vol_net_drift_21d(volume: pd.Series) -> pd.Series:
    """Net volume drift: (end - start) / start over trailing 21-day window."""
    start = volume.shift(_TD_MON - 1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return _safe_div(volume - start, start.clip(lower=_EPS))


def vtr_072_vol_net_drift_63d(volume: pd.Series) -> pd.Series:
    """Net volume drift over trailing 63-day window (end vs window open)."""
    vol63_ago = volume.shift(_TD_QTR)
    return _safe_div(volume - vol63_ago, vol63_ago.clip(lower=_EPS))


def vtr_073_vol_net_drift_126d(volume: pd.Series) -> pd.Series:
    """Net volume drift over trailing 126-day window."""
    vol126_ago = volume.shift(_TD_HALF)
    return _safe_div(volume - vol126_ago, vol126_ago.clip(lower=_EPS))


def vtr_074_vol_net_drift_252d(volume: pd.Series) -> pd.Series:
    """Net volume drift over trailing 252-day window."""
    vol252_ago = volume.shift(_TD_YEAR)
    return _safe_div(volume - vol252_ago, vol252_ago.clip(lower=_EPS))


def vtr_075_vol_trend_slope_vs_price_slope_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 21-day volume OLS slope (norm) to 21-day price OLS slope (norm)."""
    vslope = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    pslope = _safe_div(_linslope(close, _TD_MON), _rolling_mean(close, _TD_MON).clip(lower=_EPS))
    return _safe_div(vslope, pslope.replace(0, np.nan))


# --- Group G (151-175): Additional windows, transforms, and cross-asset signals ---

def vtr_151_vol_ols_slope_10d_norm(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over trailing 10-day window, normalized by 10-day mean."""
    slope = _linslope(volume, 10)
    avg = _rolling_mean(volume, 10)
    return _safe_div(slope, avg)


def vtr_152_vol_ols_slope_42d_norm(volume: pd.Series) -> pd.Series:
    """OLS slope of raw volume over trailing 42-day window, normalized by 42-day mean."""
    slope = _linslope(volume, 42)
    avg = _rolling_mean(volume, 42)
    return _safe_div(slope, avg)


def vtr_153_logvol_slope_10d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 10-day window."""
    return _linslope(_log_safe(volume), 10)


def vtr_154_logvol_slope_42d(volume: pd.Series) -> pd.Series:
    """OLS slope of log-volume over trailing 42-day window."""
    return _linslope(_log_safe(volume), 42)


def vtr_155_vol_ema10_vs_ema42_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 10-day EMA volume to 42-day EMA volume."""
    return _safe_div(_ewm_mean(volume, 10), _ewm_mean(volume, 42))


def vtr_156_vol_sma10_vs_sma42_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 10-day SMA volume to 42-day SMA volume."""
    return _safe_div(_rolling_mean(volume, 10), _rolling_mean(volume, 42))


def vtr_157_vol_ema126_vs_ema252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 126-day EMA volume to 252-day EMA volume."""
    return _safe_div(_ewm_mean(volume, _TD_HALF), _ewm_mean(volume, _TD_YEAR))


def vtr_158_vol_sma10_vs_sma252_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 10-day SMA volume to 252-day SMA volume (ultra-short vs annual)."""
    return _safe_div(_rolling_mean(volume, 10), _rolling_mean(volume, _TD_YEAR))


def vtr_159_vol_rising_days_frac_10d(volume: pd.Series) -> pd.Series:
    """Fraction of days with rising volume in trailing 10 days."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_mean(rising, 10)


def vtr_160_vol_rising_days_frac_42d(volume: pd.Series) -> pd.Series:
    """Fraction of days with rising volume in trailing 42 days."""
    rising = (volume > volume.shift(1)).astype(float)
    return _rolling_mean(rising, 42)


def vtr_161_vol_trend_consistency_42d(volume: pd.Series) -> pd.Series:
    """Consistency of daily volume changes over trailing 42 days (|sum_signs|/42)."""
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(42, min_periods=21).sum()
    return total_sign.abs() / 42


def vtr_162_vol_trend_consistency_126d(volume: pd.Series) -> pd.Series:
    """Consistency of daily volume changes over trailing 126 days."""
    sign_chg = np.sign(volume - volume.shift(1))
    total_sign = sign_chg.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).sum()
    return total_sign.abs() / _TD_HALF


def vtr_163_vol_net_drift_10d(volume: pd.Series) -> pd.Series:
    """Net volume drift over trailing 10-day window."""
    vol10_ago = volume.shift(10)
    return _safe_div(volume - vol10_ago, vol10_ago.clip(lower=_EPS))


def vtr_164_vol_net_drift_42d(volume: pd.Series) -> pd.Series:
    """Net volume drift over trailing 42-day window."""
    vol42_ago = volume.shift(42)
    return _safe_div(volume - vol42_ago, vol42_ago.clip(lower=_EPS))


def vtr_165_vol_rsq_10d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 10 days."""
    return _linslope_rsq(volume, 10)


def vtr_166_vol_rsq_42d(volume: pd.Series) -> pd.Series:
    """R-squared of OLS fit to raw volume over trailing 42 days."""
    return _linslope_rsq(volume, 42)


def vtr_167_logvol_rsq_10d_signed(volume: pd.Series) -> pd.Series:
    """Signed R-squared of 10-day log-volume OLS trend."""
    rsq = _linslope_rsq(_log_safe(volume), 10)
    sgn = np.sign(_linslope(_log_safe(volume), 10))
    return rsq * sgn


def vtr_168_vol_ols_slope_21d_vs_63d_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of normalized 21-day to normalized 63-day raw-volume slope."""
    s21 = _safe_div(_linslope(volume, _TD_MON), _rolling_mean(volume, _TD_MON).clip(lower=_EPS))
    s63 = _safe_div(_linslope(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    return _safe_div(s21, s63.replace(0, np.nan))


def vtr_169_vol_ema5_above_ema252_flag(volume: pd.Series) -> pd.Series:
    """Flag: EMA5 volume > EMA252 volume (immediate activity above annual baseline)."""
    return (_ewm_mean(volume, _TD_WEEK) > _ewm_mean(volume, _TD_YEAR)).astype(float)


def vtr_170_vol_sma5_above_sma126_flag(volume: pd.Series) -> pd.Series:
    """Flag: SMA5 volume > SMA126 volume (weekly pace above half-year average)."""
    return (_rolling_mean(volume, _TD_WEEK) > _rolling_mean(volume, _TD_HALF)).astype(float)


def vtr_171_vol_logslope_126d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of 126-day log-vol slope within trailing 252-day distribution."""
    slope = _linslope(_log_safe(volume), _TD_HALF)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vtr_172_vol_slope_10d_zscore_63d(volume: pd.Series) -> pd.Series:
    """Z-score of 10-day raw-volume slope relative to trailing 63-day distribution."""
    slope = _linslope(volume, 10)
    m = _rolling_mean(slope, _TD_QTR)
    s = _rolling_std(slope, _TD_QTR)
    return _safe_div(slope - m, s)


def vtr_173_vol_sma5_vs_sma63_ratio(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day SMA volume to 63-day SMA volume."""
    return _safe_div(_rolling_mean(volume, _TD_WEEK), _rolling_mean(volume, _TD_QTR))


def vtr_174_vol_trend_slope_vs_price_slope_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of 63-day volume OLS slope (norm) to 63-day price OLS slope (norm)."""
    vslope = _safe_div(_linslope(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR).clip(lower=_EPS))
    pslope = _safe_div(_linslope(close, _TD_QTR), _rolling_mean(close, _TD_QTR).clip(lower=_EPS))
    return _safe_div(vslope, pslope.replace(0, np.nan))


def vtr_175_vol_rsq_signed_composite_3window(volume: pd.Series) -> pd.Series:
    """Average of signed R-squared across 10d, 42d, 126d volume trend windows."""
    def _srq(w):
        rsq = _linslope_rsq(volume, w)
        sgn = np.sign(_linslope(volume, w))
        return rsq * sgn
    return (_srq(10) + _srq(42) + _srq(_TD_HALF)) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_TREND_REGISTRY_001_075 = {
    "vtr_001_vol_ols_slope_21d": {"inputs": ["volume"], "func": vtr_001_vol_ols_slope_21d},
    "vtr_002_vol_ols_slope_63d": {"inputs": ["volume"], "func": vtr_002_vol_ols_slope_63d},
    "vtr_003_vol_ols_slope_126d": {"inputs": ["volume"], "func": vtr_003_vol_ols_slope_126d},
    "vtr_004_vol_ols_slope_252d": {"inputs": ["volume"], "func": vtr_004_vol_ols_slope_252d},
    "vtr_005_vol_ols_slope_21d_sign": {"inputs": ["volume"], "func": vtr_005_vol_ols_slope_21d_sign},
    "vtr_006_vol_ols_slope_63d_sign": {"inputs": ["volume"], "func": vtr_006_vol_ols_slope_63d_sign},
    "vtr_007_vol_ols_slope_126d_sign": {"inputs": ["volume"], "func": vtr_007_vol_ols_slope_126d_sign},
    "vtr_008_vol_ols_slope_252d_sign": {"inputs": ["volume"], "func": vtr_008_vol_ols_slope_252d_sign},
    "vtr_009_vol_ols_slope_21d_norm": {"inputs": ["volume"], "func": vtr_009_vol_ols_slope_21d_norm},
    "vtr_010_vol_ols_slope_63d_norm": {"inputs": ["volume"], "func": vtr_010_vol_ols_slope_63d_norm},
    "vtr_011_vol_ols_slope_126d_norm": {"inputs": ["volume"], "func": vtr_011_vol_ols_slope_126d_norm},
    "vtr_012_vol_ols_slope_252d_norm": {"inputs": ["volume"], "func": vtr_012_vol_ols_slope_252d_norm},
    "vtr_013_logvol_ols_slope_21d": {"inputs": ["volume"], "func": vtr_013_logvol_ols_slope_21d},
    "vtr_014_logvol_ols_slope_63d": {"inputs": ["volume"], "func": vtr_014_logvol_ols_slope_63d},
    "vtr_015_logvol_ols_slope_126d": {"inputs": ["volume"], "func": vtr_015_logvol_ols_slope_126d},
    "vtr_016_logvol_ols_slope_252d": {"inputs": ["volume"], "func": vtr_016_logvol_ols_slope_252d},
    "vtr_017_logvol_ols_slope_21d_sign": {"inputs": ["volume"], "func": vtr_017_logvol_ols_slope_21d_sign},
    "vtr_018_logvol_ols_slope_63d_sign": {"inputs": ["volume"], "func": vtr_018_logvol_ols_slope_63d_sign},
    "vtr_019_logvol_ols_slope_126d_sign": {"inputs": ["volume"], "func": vtr_019_logvol_ols_slope_126d_sign},
    "vtr_020_logvol_ols_slope_252d_sign": {"inputs": ["volume"], "func": vtr_020_logvol_ols_slope_252d_sign},
    "vtr_021_logvol_slope_21d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_021_logvol_slope_21d_pct_rank_252d},
    "vtr_022_logvol_slope_63d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_022_logvol_slope_63d_pct_rank_252d},
    "vtr_023_logvol_slope_126d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_023_logvol_slope_126d_pct_rank_252d},
    "vtr_024_logvol_slope_21d_zscore_252d": {"inputs": ["volume"], "func": vtr_024_logvol_slope_21d_zscore_252d},
    "vtr_025_vol_ema5_vs_ema21_ratio": {"inputs": ["volume"], "func": vtr_025_vol_ema5_vs_ema21_ratio},
    "vtr_026_vol_ema5_vs_ema63_ratio": {"inputs": ["volume"], "func": vtr_026_vol_ema5_vs_ema63_ratio},
    "vtr_027_vol_ema21_vs_ema63_ratio": {"inputs": ["volume"], "func": vtr_027_vol_ema21_vs_ema63_ratio},
    "vtr_028_vol_ema21_vs_ema126_ratio": {"inputs": ["volume"], "func": vtr_028_vol_ema21_vs_ema126_ratio},
    "vtr_029_vol_ema63_vs_ema252_ratio": {"inputs": ["volume"], "func": vtr_029_vol_ema63_vs_ema252_ratio},
    "vtr_030_vol_ema5_vs_ema21_diff": {"inputs": ["volume"], "func": vtr_030_vol_ema5_vs_ema21_diff},
    "vtr_031_vol_ema21_vs_ema63_diff": {"inputs": ["volume"], "func": vtr_031_vol_ema21_vs_ema63_diff},
    "vtr_032_vol_ema21_vs_ema63_sign": {"inputs": ["volume"], "func": vtr_032_vol_ema21_vs_ema63_sign},
    "vtr_033_vol_ema63_vs_ema252_sign": {"inputs": ["volume"], "func": vtr_033_vol_ema63_vs_ema252_sign},
    "vtr_034_vol_ema5_above_ema63_flag": {"inputs": ["volume"], "func": vtr_034_vol_ema5_above_ema63_flag},
    "vtr_035_vol_ema21_above_ema252_flag": {"inputs": ["volume"], "func": vtr_035_vol_ema21_above_ema252_flag},
    "vtr_036_vol_ema_crossover_score": {"inputs": ["volume"], "func": vtr_036_vol_ema_crossover_score},
    "vtr_037_vol_sma5_vs_sma21_ratio": {"inputs": ["volume"], "func": vtr_037_vol_sma5_vs_sma21_ratio},
    "vtr_038_vol_sma21_vs_sma63_ratio": {"inputs": ["volume"], "func": vtr_038_vol_sma21_vs_sma63_ratio},
    "vtr_039_vol_sma21_vs_sma126_ratio": {"inputs": ["volume"], "func": vtr_039_vol_sma21_vs_sma126_ratio},
    "vtr_040_vol_sma21_vs_sma252_ratio": {"inputs": ["volume"], "func": vtr_040_vol_sma21_vs_sma252_ratio},
    "vtr_041_vol_sma63_vs_sma252_ratio": {"inputs": ["volume"], "func": vtr_041_vol_sma63_vs_sma252_ratio},
    "vtr_042_vol_sma5_vs_sma252_ratio": {"inputs": ["volume"], "func": vtr_042_vol_sma5_vs_sma252_ratio},
    "vtr_043_vol_sma21_vs_sma63_diff_norm": {"inputs": ["volume"], "func": vtr_043_vol_sma21_vs_sma63_diff_norm},
    "vtr_044_vol_sma21_vs_sma252_diff_norm": {"inputs": ["volume"], "func": vtr_044_vol_sma21_vs_sma252_diff_norm},
    "vtr_045_vol_sma63_vs_sma252_diff_norm": {"inputs": ["volume"], "func": vtr_045_vol_sma63_vs_sma252_diff_norm},
    "vtr_046_vol_sma21_above_sma63_flag": {"inputs": ["volume"], "func": vtr_046_vol_sma21_above_sma63_flag},
    "vtr_047_vol_sma63_above_sma252_flag": {"inputs": ["volume"], "func": vtr_047_vol_sma63_above_sma252_flag},
    "vtr_048_vol_sma_alignment_score": {"inputs": ["volume"], "func": vtr_048_vol_sma_alignment_score},
    "vtr_049_vol_rsq_21d": {"inputs": ["volume"], "func": vtr_049_vol_rsq_21d},
    "vtr_050_vol_rsq_63d": {"inputs": ["volume"], "func": vtr_050_vol_rsq_63d},
    "vtr_051_vol_rsq_126d": {"inputs": ["volume"], "func": vtr_051_vol_rsq_126d},
    "vtr_052_vol_rsq_252d": {"inputs": ["volume"], "func": vtr_052_vol_rsq_252d},
    "vtr_053_logvol_rsq_21d": {"inputs": ["volume"], "func": vtr_053_logvol_rsq_21d},
    "vtr_054_logvol_rsq_63d": {"inputs": ["volume"], "func": vtr_054_logvol_rsq_63d},
    "vtr_055_logvol_rsq_126d": {"inputs": ["volume"], "func": vtr_055_logvol_rsq_126d},
    "vtr_056_logvol_rsq_252d": {"inputs": ["volume"], "func": vtr_056_logvol_rsq_252d},
    "vtr_057_vol_rsq_21d_signed": {"inputs": ["volume"], "func": vtr_057_vol_rsq_21d_signed},
    "vtr_058_vol_rsq_63d_signed": {"inputs": ["volume"], "func": vtr_058_vol_rsq_63d_signed},
    "vtr_059_logvol_rsq_21d_signed": {"inputs": ["volume"], "func": vtr_059_logvol_rsq_21d_signed},
    "vtr_060_logvol_rsq_63d_signed": {"inputs": ["volume"], "func": vtr_060_logvol_rsq_63d_signed},
    "vtr_061_vol_rising_weeks_frac_63d": {"inputs": ["volume"], "func": vtr_061_vol_rising_weeks_frac_63d},
    "vtr_062_vol_rising_weeks_frac_126d": {"inputs": ["volume"], "func": vtr_062_vol_rising_weeks_frac_126d},
    "vtr_063_vol_rising_weeks_frac_252d": {"inputs": ["volume"], "func": vtr_063_vol_rising_weeks_frac_252d},
    "vtr_064_vol_rising_days_frac_21d": {"inputs": ["volume"], "func": vtr_064_vol_rising_days_frac_21d},
    "vtr_065_vol_rising_days_frac_63d": {"inputs": ["volume"], "func": vtr_065_vol_rising_days_frac_63d},
    "vtr_066_vol_rising_days_frac_252d": {"inputs": ["volume"], "func": vtr_066_vol_rising_days_frac_252d},
    "vtr_067_vol_rising_months_frac_252d": {"inputs": ["volume"], "func": vtr_067_vol_rising_months_frac_252d},
    "vtr_068_vol_trend_consistency_21d": {"inputs": ["volume"], "func": vtr_068_vol_trend_consistency_21d},
    "vtr_069_vol_trend_consistency_63d": {"inputs": ["volume"], "func": vtr_069_vol_trend_consistency_63d},
    "vtr_070_vol_trend_consistency_252d": {"inputs": ["volume"], "func": vtr_070_vol_trend_consistency_252d},
    "vtr_071_vol_net_drift_21d": {"inputs": ["volume"], "func": vtr_071_vol_net_drift_21d},
    "vtr_072_vol_net_drift_63d": {"inputs": ["volume"], "func": vtr_072_vol_net_drift_63d},
    "vtr_073_vol_net_drift_126d": {"inputs": ["volume"], "func": vtr_073_vol_net_drift_126d},
    "vtr_074_vol_net_drift_252d": {"inputs": ["volume"], "func": vtr_074_vol_net_drift_252d},
    "vtr_075_vol_trend_slope_vs_price_slope_ratio_21d": {"inputs": ["close", "volume"], "func": vtr_075_vol_trend_slope_vs_price_slope_ratio_21d},
    "vtr_151_vol_ols_slope_10d_norm": {"inputs": ["volume"], "func": vtr_151_vol_ols_slope_10d_norm},
    "vtr_152_vol_ols_slope_42d_norm": {"inputs": ["volume"], "func": vtr_152_vol_ols_slope_42d_norm},
    "vtr_153_logvol_slope_10d": {"inputs": ["volume"], "func": vtr_153_logvol_slope_10d},
    "vtr_154_logvol_slope_42d": {"inputs": ["volume"], "func": vtr_154_logvol_slope_42d},
    "vtr_155_vol_ema10_vs_ema42_ratio": {"inputs": ["volume"], "func": vtr_155_vol_ema10_vs_ema42_ratio},
    "vtr_156_vol_sma10_vs_sma42_ratio": {"inputs": ["volume"], "func": vtr_156_vol_sma10_vs_sma42_ratio},
    "vtr_157_vol_ema126_vs_ema252_ratio": {"inputs": ["volume"], "func": vtr_157_vol_ema126_vs_ema252_ratio},
    "vtr_158_vol_sma10_vs_sma252_ratio": {"inputs": ["volume"], "func": vtr_158_vol_sma10_vs_sma252_ratio},
    "vtr_159_vol_rising_days_frac_10d": {"inputs": ["volume"], "func": vtr_159_vol_rising_days_frac_10d},
    "vtr_160_vol_rising_days_frac_42d": {"inputs": ["volume"], "func": vtr_160_vol_rising_days_frac_42d},
    "vtr_161_vol_trend_consistency_42d": {"inputs": ["volume"], "func": vtr_161_vol_trend_consistency_42d},
    "vtr_162_vol_trend_consistency_126d": {"inputs": ["volume"], "func": vtr_162_vol_trend_consistency_126d},
    "vtr_163_vol_net_drift_10d": {"inputs": ["volume"], "func": vtr_163_vol_net_drift_10d},
    "vtr_164_vol_net_drift_42d": {"inputs": ["volume"], "func": vtr_164_vol_net_drift_42d},
    "vtr_165_vol_rsq_10d": {"inputs": ["volume"], "func": vtr_165_vol_rsq_10d},
    "vtr_166_vol_rsq_42d": {"inputs": ["volume"], "func": vtr_166_vol_rsq_42d},
    "vtr_167_logvol_rsq_10d_signed": {"inputs": ["volume"], "func": vtr_167_logvol_rsq_10d_signed},
    "vtr_168_vol_ols_slope_21d_vs_63d_ratio": {"inputs": ["volume"], "func": vtr_168_vol_ols_slope_21d_vs_63d_ratio},
    "vtr_169_vol_ema5_above_ema252_flag": {"inputs": ["volume"], "func": vtr_169_vol_ema5_above_ema252_flag},
    "vtr_170_vol_sma5_above_sma126_flag": {"inputs": ["volume"], "func": vtr_170_vol_sma5_above_sma126_flag},
    "vtr_171_vol_logslope_126d_pct_rank_252d": {"inputs": ["volume"], "func": vtr_171_vol_logslope_126d_pct_rank_252d},
    "vtr_172_vol_slope_10d_zscore_63d": {"inputs": ["volume"], "func": vtr_172_vol_slope_10d_zscore_63d},
    "vtr_173_vol_sma5_vs_sma63_ratio": {"inputs": ["volume"], "func": vtr_173_vol_sma5_vs_sma63_ratio},
    "vtr_174_vol_trend_slope_vs_price_slope_ratio_63d": {"inputs": ["close", "volume"], "func": vtr_174_vol_trend_slope_vs_price_slope_ratio_63d},
    "vtr_175_vol_rsq_signed_composite_3window": {"inputs": ["volume"], "func": vtr_175_vol_rsq_signed_composite_3window},
}
