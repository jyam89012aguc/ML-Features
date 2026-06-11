"""
24_volume_distribution — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base volume-distribution shape features — velocity of skew,
        kurtosis, CV, IQR, and mean-vs-median gap changes over time.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vds_drv2_001_vol_skew_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume skew (velocity of skewness change)."""
    return _rolling_skew(volume, _TD_MON).diff(_TD_WEEK)


def vds_drv2_002_vol_skew_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day volume skew (monthly velocity of skewness)."""
    return _rolling_skew(volume, _TD_MON).diff(_TD_MON)


def vds_drv2_003_vol_skew_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume skew."""
    return _rolling_skew(volume, _TD_QTR).diff(_TD_MON)


def vds_drv2_004_vol_kurt_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume kurtosis (velocity of fat-tail change)."""
    return _rolling_kurt(volume, _TD_MON).diff(_TD_WEEK)


def vds_drv2_005_vol_kurt_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day volume kurtosis."""
    return _rolling_kurt(volume, _TD_QTR).diff(_TD_MON)


def vds_drv2_006_vol_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day coefficient of variation of volume."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_WEEK)


def vds_drv2_007_vol_cv_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day CV of volume (monthly change in dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_MON)


def vds_drv2_008_vol_cv_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day CV of volume."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return cv.diff(_TD_MON)


def vds_drv2_009_vol_iqr_norm_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of normalized IQR over 21 days."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr_n = _safe_div(q75 - q25, med)
    return iqr_n.diff(_TD_WEEK)


def vds_drv2_010_vol_iqr_norm_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of normalized IQR over 63 days."""
    q75 = _rolling_quantile(volume, _TD_QTR, 0.75)
    q25 = _rolling_quantile(volume, _TD_QTR, 0.25)
    med = _rolling_median(volume, _TD_QTR)
    iqr_n = _safe_div(q75 - q25, med)
    return iqr_n.diff(_TD_MON)


def vds_drv2_011_vol_mean_median_ratio_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of mean/median ratio over 21 days."""
    r = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    return r.diff(_TD_WEEK)


def vds_drv2_012_vol_mean_median_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of mean/median ratio over 63 days."""
    r = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    return r.diff(_TD_MON)


def vds_drv2_013_vol_90_10_spread_norm_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of normalized 90-10 spread over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    med = _rolling_median(volume, _TD_QTR)
    spread_n = _safe_div(q90 - q10, med)
    return spread_n.diff(_TD_MON)


def vds_drv2_014_vol_skew_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day volume skew over trailing 63 days."""
    return _linslope(_rolling_skew(volume, _TD_MON), _TD_QTR)


def vds_drv2_015_vol_kurt_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day kurtosis over trailing 63 days."""
    return _linslope(_rolling_kurt(volume, _TD_MON), _TD_QTR)


def vds_drv2_016_vol_cv_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day CV over trailing 63 days."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return _linslope(cv, _TD_QTR)


def vds_drv2_017_vol_skew_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day skew over trailing 252 days (long-run skew trend)."""
    return _linslope(_rolling_skew(volume, _TD_QTR), _TD_YEAR)


def vds_drv2_018_vol_cv_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day CV over trailing 252 days."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return _linslope(cv, _TD_YEAR)


def vds_drv2_019_vol_log_std_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day log-volume std (velocity of log-space dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_MON).diff(_TD_WEEK)


def vds_drv2_020_vol_log_std_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 63-day log-volume std."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_QTR).diff(_TD_MON)


def vds_drv2_021_vol_ewm_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of EWM-CV(21) (velocity of exponentially weighted dispersion)."""
    cv = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    return cv.diff(_TD_WEEK)


def vds_drv2_022_vol_tail_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of Q90/Q50 tail ratio over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    return _safe_div(q90, q50).diff(_TD_MON)


def vds_drv2_023_vol_upper_lower_tail_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (Q90-Q50)/(Q50-Q10) tail asymmetry ratio over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    ratio = _safe_div(q90 - q50, q50 - q10)
    return ratio.diff(_TD_MON)


def vds_drv2_024_vol_shape_composite_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of composite shape score (z-normalized skew+kurt+cv, 21-day)."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    composite = (sk_z + k_z + cv_z) / 3.0
    return composite.diff(_TD_WEEK)


def vds_drv2_025_vol_mad_norm_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of normalized MAD over 21 days (velocity of robust dispersion)."""
    m = _rolling_mean(volume, _TD_MON)
    mad = (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    mad_n = _safe_div(mad, m)
    return mad_n.diff(_TD_WEEK)


# ── New 2nd-Derivative Feature Functions 026-075 ─────────────────────────────

def vds_drv2_026_vol_skew_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day volume skew (quarterly velocity of skewness)."""
    return _rolling_skew(volume, _TD_MON).diff(_TD_QTR)


def vds_drv2_027_vol_kurt_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day kurtosis (quarterly velocity of fat-tail change)."""
    return _rolling_kurt(volume, _TD_MON).diff(_TD_QTR)


def vds_drv2_028_vol_cv_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 21-day CV (quarterly change in short-term dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.diff(_TD_QTR)


def vds_drv2_029_vol_skew_63d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 63-day volume skew (self-referenced quarterly skew velocity)."""
    return _rolling_skew(volume, _TD_QTR).diff(_TD_QTR)


def vds_drv2_030_vol_kurt_63d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 63-day kurtosis."""
    return _rolling_kurt(volume, _TD_QTR).diff(_TD_QTR)


def vds_drv2_031_vol_cv_63d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 63-day CV (quarterly change in medium-term dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    return cv.diff(_TD_QTR)


def vds_drv2_032_vol_iqr_norm_63d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of normalized IQR over 63 days."""
    q75 = _rolling_quantile(volume, _TD_QTR, 0.75)
    q25 = _rolling_quantile(volume, _TD_QTR, 0.25)
    med = _rolling_median(volume, _TD_QTR)
    iqr_n = _safe_div(q75 - q25, med)
    return iqr_n.diff(_TD_QTR)


def vds_drv2_033_vol_90_10_spread_norm_63d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of normalized 90-10 spread over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    med = _rolling_median(volume, _TD_QTR)
    spread_n = _safe_div(q90 - q10, med)
    return spread_n.diff(_TD_QTR)


def vds_drv2_034_vol_mean_median_ratio_21d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of mean/median ratio over 21 days."""
    r = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    return r.diff(_TD_QTR)


def vds_drv2_035_vol_log_std_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day log-volume std (monthly velocity of log-space dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_MON).diff(_TD_MON)


def vds_drv2_036_vol_log_std_63d_63d_diff(volume: pd.Series) -> pd.Series:
    """63-day diff of 63-day log-volume std."""
    lv = np.log(volume.clip(lower=_EPS))
    return _rolling_std(lv, _TD_QTR).diff(_TD_QTR)


def vds_drv2_037_vol_ewm_cv_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EWM-CV(63) (monthly velocity of medium-term ewm dispersion)."""
    cv = _safe_div(_ewm_std(volume, _TD_QTR), _ewm_mean(volume, _TD_QTR))
    return cv.diff(_TD_MON)


def vds_drv2_038_vol_ewm_cv_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of EWM-CV(21) (monthly velocity of ewm short-term dispersion)."""
    cv = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    return cv.diff(_TD_MON)


def vds_drv2_039_vol_tail_ratio_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of Q90/Q50 tail ratio over 21 days."""
    q90 = _rolling_quantile(volume, _TD_MON, 0.90)
    q50 = _rolling_quantile(volume, _TD_MON, 0.50)
    return _safe_div(q90, q50).diff(_TD_WEEK)


def vds_drv2_040_vol_tail_ratio_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of Q90/Q50 tail ratio over 252 days."""
    q90 = _rolling_quantile(volume, _TD_YEAR, 0.90)
    q50 = _rolling_quantile(volume, _TD_YEAR, 0.50)
    return _safe_div(q90, q50).diff(_TD_MON)


def vds_drv2_041_vol_mad_norm_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of normalized MAD over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    mad = (volume - m).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    mad_n = _safe_div(mad, m)
    return mad_n.diff(_TD_MON)


def vds_drv2_042_vol_mad_norm_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of normalized MAD over 21 days (monthly velocity)."""
    m = _rolling_mean(volume, _TD_MON)
    mad = (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    mad_n = _safe_div(mad, m)
    return mad_n.diff(_TD_MON)


def vds_drv2_043_vol_bimodality_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of bimodality coefficient over 63 days."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    bm = _safe_div(sk ** 2 + 1, k.clip(lower=_EPS))
    return bm.diff(_TD_MON)


def vds_drv2_044_vol_skew_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume skew."""
    return _rolling_skew(volume, _TD_HALF).diff(_TD_MON)


def vds_drv2_045_vol_kurt_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day volume kurtosis."""
    return _rolling_kurt(volume, _TD_HALF).diff(_TD_MON)


def vds_drv2_046_vol_cv_126d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 126-day CV."""
    cv = _safe_div(_rolling_std(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))
    return cv.diff(_TD_MON)


def vds_drv2_047_vol_iqr_norm_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of normalized IQR over 21 days (monthly velocity of short IQR)."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr_n = _safe_div(q75 - q25, med)
    return iqr_n.diff(_TD_MON)


def vds_drv2_048_vol_skew_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day volume skew over trailing 21 days (short-run skew trend)."""
    return _linslope(_rolling_skew(volume, _TD_MON), _TD_MON)


def vds_drv2_049_vol_kurt_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day kurtosis over trailing 21 days."""
    return _linslope(_rolling_kurt(volume, _TD_MON), _TD_MON)


def vds_drv2_050_vol_cv_21d_slope_21d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day CV over trailing 21 days."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return _linslope(cv, _TD_MON)


def vds_drv2_051_vol_iqr_norm_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of normalized 21-day IQR over trailing 63 days."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr_n = _safe_div(q75 - q25, med)
    return _linslope(iqr_n, _TD_QTR)


def vds_drv2_052_vol_iqr_norm_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of normalized 63-day IQR over trailing 252 days."""
    q75 = _rolling_quantile(volume, _TD_QTR, 0.75)
    q25 = _rolling_quantile(volume, _TD_QTR, 0.25)
    med = _rolling_median(volume, _TD_QTR)
    iqr_n = _safe_div(q75 - q25, med)
    return _linslope(iqr_n, _TD_YEAR)


def vds_drv2_053_vol_mean_median_ratio_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day mean/median ratio over trailing 63 days."""
    r = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    return _linslope(r, _TD_QTR)


def vds_drv2_054_vol_mean_median_ratio_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day mean/median ratio over trailing 252 days."""
    r = _safe_div(_rolling_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    return _linslope(r, _TD_YEAR)


def vds_drv2_055_vol_log_std_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day log-volume std over trailing 63 days."""
    lv = np.log(volume.clip(lower=_EPS))
    return _linslope(_rolling_std(lv, _TD_MON), _TD_QTR)


def vds_drv2_056_vol_log_std_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day log-volume std over trailing 252 days."""
    lv = np.log(volume.clip(lower=_EPS))
    return _linslope(_rolling_std(lv, _TD_QTR), _TD_YEAR)


def vds_drv2_057_vol_ewm_cv_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of EWM-CV(21) over trailing 63 days."""
    cv = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    return _linslope(cv, _TD_QTR)


def vds_drv2_058_vol_tail_ratio_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of Q90/Q50 tail ratio over 63 days, measured over 252 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    return _linslope(_safe_div(q90, q50), _TD_YEAR)


def vds_drv2_059_vol_mad_norm_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of normalized 21-day MAD over trailing 63 days."""
    m = _rolling_mean(volume, _TD_MON)
    mad = (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    mad_n = _safe_div(mad, m)
    return _linslope(mad_n, _TD_QTR)


def vds_drv2_060_vol_mad_norm_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of normalized 63-day MAD over trailing 252 days."""
    m = _rolling_mean(volume, _TD_QTR)
    mad = (volume - m).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    mad_n = _safe_div(mad, m)
    return _linslope(mad_n, _TD_YEAR)


def vds_drv2_061_vol_upper_lower_tail_ratio_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of (Q90-Q50)/(Q50-Q10) tail asymmetry ratio over 63 days."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q50 = _rolling_quantile(volume, _TD_QTR, 0.50)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    ratio = _safe_div(q90 - q50, q50 - q10)
    return ratio.diff(_TD_WEEK)


def vds_drv2_062_vol_upper_lower_tail_ratio_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of (Q90-Q50)/(Q50-Q10) tail asymmetry ratio over 252 days."""
    q90 = _rolling_quantile(volume, _TD_YEAR, 0.90)
    q50 = _rolling_quantile(volume, _TD_YEAR, 0.50)
    q10 = _rolling_quantile(volume, _TD_YEAR, 0.10)
    ratio = _safe_div(q90 - q50, q50 - q10)
    return ratio.diff(_TD_MON)


def vds_drv2_063_vol_shape_composite_63d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 63-day composite shape score."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    composite = (sk_z + k_z + cv_z) / 3.0
    return composite.diff(_TD_WEEK)


def vds_drv2_064_vol_shape_composite_21d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 21-day composite shape score (monthly velocity of shape)."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    composite = (sk_z + k_z + cv_z) / 3.0
    return composite.diff(_TD_MON)


def vds_drv2_065_vol_skew_kurt_product_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of the skew×kurtosis product over 21 days."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    return (sk * k).diff(_TD_WEEK)


def vds_drv2_066_vol_skew_kurt_product_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of the skew×kurtosis product over 63 days."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    return (sk * k).diff(_TD_MON)


def vds_drv2_067_vol_q75_q25_ratio_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of Q75/Q25 ratio over 21 days (velocity of multiplicative IQR)."""
    ratio = _safe_div(_rolling_quantile(volume, _TD_MON, 0.75), _rolling_quantile(volume, _TD_MON, 0.25))
    return ratio.diff(_TD_WEEK)


def vds_drv2_068_vol_q75_q25_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of Q75/Q25 ratio over 63 days."""
    ratio = _safe_div(_rolling_quantile(volume, _TD_QTR, 0.75), _rolling_quantile(volume, _TD_QTR, 0.25))
    return ratio.diff(_TD_MON)


def vds_drv2_069_vol_max_to_median_ratio_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of max/median ratio over 21 days (velocity of spike dominance)."""
    ratio = _safe_div(_rolling_max(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    return ratio.diff(_TD_WEEK)


def vds_drv2_070_vol_max_to_median_ratio_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of max/median ratio over 63 days."""
    ratio = _safe_div(_rolling_max(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))
    return ratio.diff(_TD_MON)


def vds_drv2_071_vol_cv_5d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of 5-day CV (very short velocity of dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_mean(volume, _TD_WEEK))
    return cv.diff(_TD_WEEK)


def vds_drv2_072_vol_log_cv_21d_5d_diff(volume: pd.Series) -> pd.Series:
    """5-day diff of log-volume CV over 21 days (velocity of log-space dispersion CV)."""
    lv = np.log(volume.clip(lower=_EPS))
    cv = _safe_div(_rolling_std(lv, _TD_MON), _rolling_mean(lv, _TD_MON).abs().clip(lower=_EPS))
    return cv.diff(_TD_WEEK)


def vds_drv2_073_vol_log_cv_63d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of log-volume CV over 63 days."""
    lv = np.log(volume.clip(lower=_EPS))
    cv = _safe_div(_rolling_std(lv, _TD_QTR), _rolling_mean(lv, _TD_QTR).abs().clip(lower=_EPS))
    return cv.diff(_TD_MON)


def vds_drv2_074_vol_bimodality_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of bimodality coefficient (63-day) over 252 days."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    bm = _safe_div(sk ** 2 + 1, k.clip(lower=_EPS))
    return _linslope(bm, _TD_YEAR)


def vds_drv2_075_vol_skew_252d_21d_diff(volume: pd.Series) -> pd.Series:
    """21-day diff of 252-day volume skew (monthly velocity of long-run skewness)."""
    return _rolling_skew(volume, _TD_YEAR).diff(_TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DISTRIBUTION_REGISTRY_2ND_DERIVATIVES = {
    "vds_drv2_001_vol_skew_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_001_vol_skew_21d_5d_diff},
    "vds_drv2_002_vol_skew_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_002_vol_skew_21d_21d_diff},
    "vds_drv2_003_vol_skew_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_003_vol_skew_63d_21d_diff},
    "vds_drv2_004_vol_kurt_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_004_vol_kurt_21d_5d_diff},
    "vds_drv2_005_vol_kurt_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_005_vol_kurt_63d_21d_diff},
    "vds_drv2_006_vol_cv_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_006_vol_cv_21d_5d_diff},
    "vds_drv2_007_vol_cv_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_007_vol_cv_21d_21d_diff},
    "vds_drv2_008_vol_cv_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_008_vol_cv_63d_21d_diff},
    "vds_drv2_009_vol_iqr_norm_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_009_vol_iqr_norm_21d_5d_diff},
    "vds_drv2_010_vol_iqr_norm_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_010_vol_iqr_norm_63d_21d_diff},
    "vds_drv2_011_vol_mean_median_ratio_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_011_vol_mean_median_ratio_21d_5d_diff},
    "vds_drv2_012_vol_mean_median_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_012_vol_mean_median_ratio_63d_21d_diff},
    "vds_drv2_013_vol_90_10_spread_norm_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_013_vol_90_10_spread_norm_63d_21d_diff},
    "vds_drv2_014_vol_skew_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_014_vol_skew_21d_slope_63d},
    "vds_drv2_015_vol_kurt_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_015_vol_kurt_21d_slope_63d},
    "vds_drv2_016_vol_cv_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_016_vol_cv_21d_slope_63d},
    "vds_drv2_017_vol_skew_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_017_vol_skew_63d_slope_252d},
    "vds_drv2_018_vol_cv_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_018_vol_cv_63d_slope_252d},
    "vds_drv2_019_vol_log_std_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_019_vol_log_std_21d_5d_diff},
    "vds_drv2_020_vol_log_std_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_020_vol_log_std_63d_21d_diff},
    "vds_drv2_021_vol_ewm_cv_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_021_vol_ewm_cv_21d_5d_diff},
    "vds_drv2_022_vol_tail_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_022_vol_tail_ratio_63d_21d_diff},
    "vds_drv2_023_vol_upper_lower_tail_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_023_vol_upper_lower_tail_ratio_63d_21d_diff},
    "vds_drv2_024_vol_shape_composite_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_024_vol_shape_composite_21d_5d_diff},
    "vds_drv2_025_vol_mad_norm_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_025_vol_mad_norm_21d_5d_diff},
    # --- New 2nd-derivative features 026-075 ---
    "vds_drv2_026_vol_skew_21d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_026_vol_skew_21d_63d_diff},
    "vds_drv2_027_vol_kurt_21d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_027_vol_kurt_21d_63d_diff},
    "vds_drv2_028_vol_cv_21d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_028_vol_cv_21d_63d_diff},
    "vds_drv2_029_vol_skew_63d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_029_vol_skew_63d_63d_diff},
    "vds_drv2_030_vol_kurt_63d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_030_vol_kurt_63d_63d_diff},
    "vds_drv2_031_vol_cv_63d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_031_vol_cv_63d_63d_diff},
    "vds_drv2_032_vol_iqr_norm_63d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_032_vol_iqr_norm_63d_63d_diff},
    "vds_drv2_033_vol_90_10_spread_norm_63d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_033_vol_90_10_spread_norm_63d_63d_diff},
    "vds_drv2_034_vol_mean_median_ratio_21d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_034_vol_mean_median_ratio_21d_63d_diff},
    "vds_drv2_035_vol_log_std_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_035_vol_log_std_21d_21d_diff},
    "vds_drv2_036_vol_log_std_63d_63d_diff": {"inputs": ["volume"], "func": vds_drv2_036_vol_log_std_63d_63d_diff},
    "vds_drv2_037_vol_ewm_cv_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_037_vol_ewm_cv_63d_21d_diff},
    "vds_drv2_038_vol_ewm_cv_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_038_vol_ewm_cv_21d_21d_diff},
    "vds_drv2_039_vol_tail_ratio_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_039_vol_tail_ratio_21d_5d_diff},
    "vds_drv2_040_vol_tail_ratio_252d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_040_vol_tail_ratio_252d_21d_diff},
    "vds_drv2_041_vol_mad_norm_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_041_vol_mad_norm_63d_21d_diff},
    "vds_drv2_042_vol_mad_norm_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_042_vol_mad_norm_21d_21d_diff},
    "vds_drv2_043_vol_bimodality_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_043_vol_bimodality_63d_21d_diff},
    "vds_drv2_044_vol_skew_126d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_044_vol_skew_126d_21d_diff},
    "vds_drv2_045_vol_kurt_126d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_045_vol_kurt_126d_21d_diff},
    "vds_drv2_046_vol_cv_126d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_046_vol_cv_126d_21d_diff},
    "vds_drv2_047_vol_iqr_norm_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_047_vol_iqr_norm_21d_21d_diff},
    "vds_drv2_048_vol_skew_21d_slope_21d": {"inputs": ["volume"], "func": vds_drv2_048_vol_skew_21d_slope_21d},
    "vds_drv2_049_vol_kurt_21d_slope_21d": {"inputs": ["volume"], "func": vds_drv2_049_vol_kurt_21d_slope_21d},
    "vds_drv2_050_vol_cv_21d_slope_21d": {"inputs": ["volume"], "func": vds_drv2_050_vol_cv_21d_slope_21d},
    "vds_drv2_051_vol_iqr_norm_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_051_vol_iqr_norm_21d_slope_63d},
    "vds_drv2_052_vol_iqr_norm_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_052_vol_iqr_norm_63d_slope_252d},
    "vds_drv2_053_vol_mean_median_ratio_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_053_vol_mean_median_ratio_21d_slope_63d},
    "vds_drv2_054_vol_mean_median_ratio_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_054_vol_mean_median_ratio_63d_slope_252d},
    "vds_drv2_055_vol_log_std_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_055_vol_log_std_21d_slope_63d},
    "vds_drv2_056_vol_log_std_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_056_vol_log_std_63d_slope_252d},
    "vds_drv2_057_vol_ewm_cv_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_057_vol_ewm_cv_21d_slope_63d},
    "vds_drv2_058_vol_tail_ratio_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_058_vol_tail_ratio_63d_slope_252d},
    "vds_drv2_059_vol_mad_norm_21d_slope_63d": {"inputs": ["volume"], "func": vds_drv2_059_vol_mad_norm_21d_slope_63d},
    "vds_drv2_060_vol_mad_norm_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_060_vol_mad_norm_63d_slope_252d},
    "vds_drv2_061_vol_upper_lower_tail_ratio_63d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_061_vol_upper_lower_tail_ratio_63d_5d_diff},
    "vds_drv2_062_vol_upper_lower_tail_ratio_252d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_062_vol_upper_lower_tail_ratio_252d_21d_diff},
    "vds_drv2_063_vol_shape_composite_63d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_063_vol_shape_composite_63d_5d_diff},
    "vds_drv2_064_vol_shape_composite_21d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_064_vol_shape_composite_21d_21d_diff},
    "vds_drv2_065_vol_skew_kurt_product_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_065_vol_skew_kurt_product_21d_5d_diff},
    "vds_drv2_066_vol_skew_kurt_product_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_066_vol_skew_kurt_product_63d_21d_diff},
    "vds_drv2_067_vol_q75_q25_ratio_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_067_vol_q75_q25_ratio_21d_5d_diff},
    "vds_drv2_068_vol_q75_q25_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_068_vol_q75_q25_ratio_63d_21d_diff},
    "vds_drv2_069_vol_max_to_median_ratio_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_069_vol_max_to_median_ratio_21d_5d_diff},
    "vds_drv2_070_vol_max_to_median_ratio_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_070_vol_max_to_median_ratio_63d_21d_diff},
    "vds_drv2_071_vol_cv_5d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_071_vol_cv_5d_5d_diff},
    "vds_drv2_072_vol_log_cv_21d_5d_diff": {"inputs": ["volume"], "func": vds_drv2_072_vol_log_cv_21d_5d_diff},
    "vds_drv2_073_vol_log_cv_63d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_073_vol_log_cv_63d_21d_diff},
    "vds_drv2_074_vol_bimodality_63d_slope_252d": {"inputs": ["volume"], "func": vds_drv2_074_vol_bimodality_63d_slope_252d},
    "vds_drv2_075_vol_skew_252d_21d_diff": {"inputs": ["volume"], "func": vds_drv2_075_vol_skew_252d_21d_diff},
}
