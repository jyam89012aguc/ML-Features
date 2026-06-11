"""
24_volume_distribution — Base Features 076-150
Domain: shape of the volume distribution — skewness, kurtosis, dispersion, quantile spreads,
        mean-vs-median gap, fat-tailedness, normalized rank dispersion of volume.
        Statistical moments and distributional shape of trailing volume only.
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(3, w // 2)).skew()


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(4, w // 2)).kurt()


def _rolling_quantile(s: pd.Series, w: int, q: float) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).quantile(q)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


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

# --- Group H (076-085): EWM-based distributional shape (exponential weighting) ---

def vds_076_vol_ewm_cv_21d(volume: pd.Series) -> pd.Series:
    """EWM coefficient of variation (ewm-std / ewm-mean) with span=21."""
    return _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))


def vds_077_vol_ewm_cv_63d(volume: pd.Series) -> pd.Series:
    """EWM coefficient of variation with span=63."""
    return _safe_div(_ewm_std(volume, _TD_QTR), _ewm_mean(volume, _TD_QTR))


def vds_078_vol_ewm_cv_126d(volume: pd.Series) -> pd.Series:
    """EWM coefficient of variation with span=126."""
    return _safe_div(_ewm_std(volume, _TD_HALF), _ewm_mean(volume, _TD_HALF))


def vds_079_vol_ewm_vs_sma_cv_ratio_21d(volume: pd.Series) -> pd.Series:
    """Ratio of EWM-CV to rolling-CV over 21 days (recency-weighted vs equal-weighted)."""
    ewm_cv = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    sma_cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return _safe_div(ewm_cv, sma_cv)


def vds_080_vol_ewm_mean_to_median_ratio_63d(volume: pd.Series) -> pd.Series:
    """EWM mean (span=63) divided by rolling median (63d) — asymmetry via weighting."""
    return _safe_div(_ewm_mean(volume, _TD_QTR), _rolling_median(volume, _TD_QTR))


def vds_081_vol_log_ewm_std_21d(volume: pd.Series) -> pd.Series:
    """EWM std of log-volume with span=21 (exponentially weighted log dispersion)."""
    lv = np.log(volume.clip(lower=_EPS))
    return _ewm_std(lv, _TD_MON)


def vds_082_vol_log_ewm_std_63d(volume: pd.Series) -> pd.Series:
    """EWM std of log-volume with span=63."""
    lv = np.log(volume.clip(lower=_EPS))
    return _ewm_std(lv, _TD_QTR)


def vds_083_vol_ewm_cv_21d_pct_rank_252d(volume: pd.Series) -> pd.Series:
    """Percentile rank of EWM-CV(21) within trailing 252-day distribution."""
    cv = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    return cv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vds_084_vol_ewm_cv_ratio_21d_vs_126d(volume: pd.Series) -> pd.Series:
    """Ratio of EWM-CV(21) to EWM-CV(126) — short vs long dispersion comparison."""
    cv21 = _safe_div(_ewm_std(volume, _TD_MON), _ewm_mean(volume, _TD_MON))
    cv126 = _safe_div(_ewm_std(volume, _TD_HALF), _ewm_mean(volume, _TD_HALF))
    return _safe_div(cv21, cv126)


def vds_085_vol_ewm_std_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of EWM-std(21) vs its own 252-day rolling distribution."""
    s21 = _ewm_std(volume, _TD_MON)
    m = _rolling_mean(s21, _TD_YEAR)
    s = _rolling_std(s21, _TD_YEAR)
    return _safe_div(s21 - m, s)


# --- Group I (086-095): Standardized/z-score forms of skew and kurtosis ---

def vds_086_vol_skew_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day skew vs its own 252-day mean/std."""
    sk = _rolling_skew(volume, _TD_MON)
    m = _rolling_mean(sk, _TD_YEAR)
    s = _rolling_std(sk, _TD_YEAR)
    return _safe_div(sk - m, s)


def vds_087_vol_kurt_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day kurtosis vs its own 252-day mean/std."""
    k = _rolling_kurt(volume, _TD_MON)
    m = _rolling_mean(k, _TD_YEAR)
    s = _rolling_std(k, _TD_YEAR)
    return _safe_div(k - m, s)


def vds_088_vol_skew_126d_zscore_expanding(volume: pd.Series) -> pd.Series:
    """Expanding z-score of 126-day skew (extremity vs all-history)."""
    sk = _rolling_skew(volume, _TD_HALF)
    m = sk.expanding(min_periods=5).mean()
    s = sk.expanding(min_periods=5).std()
    return _safe_div(sk - m, s)


def vds_089_vol_kurt_126d_zscore_expanding(volume: pd.Series) -> pd.Series:
    """Expanding z-score of 126-day kurtosis (extremity vs all-history)."""
    k = _rolling_kurt(volume, _TD_HALF)
    m = k.expanding(min_periods=5).mean()
    s = k.expanding(min_periods=5).std()
    return _safe_div(k - m, s)


def vds_090_vol_cv_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day CV vs its 252-day rolling distribution."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s)


def vds_091_vol_iqr_norm_21d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day normalized IQR vs its 252-day distribution."""
    q75 = _rolling_quantile(volume, _TD_MON, 0.75)
    q25 = _rolling_quantile(volume, _TD_MON, 0.25)
    med = _rolling_median(volume, _TD_MON)
    iqr_n = _safe_div(q75 - q25, med)
    m = _rolling_mean(iqr_n, _TD_YEAR)
    s = _rolling_std(iqr_n, _TD_YEAR)
    return _safe_div(iqr_n - m, s)


def vds_092_vol_90_10_spread_norm_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 63-day 90-10 spread (normalized by median) vs 252-day distribution."""
    q90 = _rolling_quantile(volume, _TD_QTR, 0.90)
    q10 = _rolling_quantile(volume, _TD_QTR, 0.10)
    med = _rolling_median(volume, _TD_QTR)
    spread_n = _safe_div(q90 - q10, med)
    m = _rolling_mean(spread_n, _TD_YEAR)
    s = _rolling_std(spread_n, _TD_YEAR)
    return _safe_div(spread_n - m, s)


def vds_093_vol_mean_median_gap_norm_21d_zscore(volume: pd.Series) -> pd.Series:
    """Z-score of 21-day (mean-median)/std vs its 252-day distribution."""
    mn = _rolling_mean(volume, _TD_MON)
    med = _rolling_median(volume, _TD_MON)
    std = _rolling_std(volume, _TD_MON)
    gap = _safe_div(mn - med, std)
    m = _rolling_mean(gap, _TD_YEAR)
    s = _rolling_std(gap, _TD_YEAR)
    return _safe_div(gap - m, s)


def vds_094_vol_skew_kurt_product_21d(volume: pd.Series) -> pd.Series:
    """Product of 21-day skew and excess kurtosis (joint non-normality measure)."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    return sk * k


def vds_095_vol_skew_kurt_product_63d(volume: pd.Series) -> pd.Series:
    """Product of 63-day skew and excess kurtosis."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    return sk * k


# --- Group J (096-105): Multi-window dispersion comparisons and regimes ---

def vds_096_vol_cv_ratio_63d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 63-day CV to 252-day CV (recent vs long-term dispersion)."""
    cv63 = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    cv252 = _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    return _safe_div(cv63, cv252)


def vds_097_vol_iqr_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day IQR to 252-day IQR (short vs long spread regime)."""
    iqr21 = _rolling_quantile(volume, _TD_MON, 0.75) - _rolling_quantile(volume, _TD_MON, 0.25)
    iqr252 = _rolling_quantile(volume, _TD_YEAR, 0.75) - _rolling_quantile(volume, _TD_YEAR, 0.25)
    return _safe_div(iqr21, iqr252)


def vds_098_vol_skew_ratio_21d_vs_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day skew to 63-day skew (short vs medium skew comparison)."""
    return _safe_div(_rolling_skew(volume, _TD_MON), _rolling_skew(volume, _TD_QTR))


def vds_099_vol_kurt_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day kurtosis to 252-day kurtosis (short vs long fat-tailedness)."""
    return _safe_div(_rolling_kurt(volume, _TD_MON), _rolling_kurt(volume, _TD_YEAR))


def vds_100_vol_std_ratio_5d_vs_63d(volume: pd.Series) -> pd.Series:
    """Ratio of 5-day std to 63-day std of volume (very short vs medium dispersion)."""
    return _safe_div(_rolling_std(volume, _TD_WEEK), _rolling_std(volume, _TD_QTR))


def vds_101_vol_std_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day std to 252-day std of volume (short vs long std)."""
    return _safe_div(_rolling_std(volume, _TD_MON), _rolling_std(volume, _TD_YEAR))


def vds_102_vol_high_dispersion_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day CV exceeds its own 252-day 75th percentile."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    q75 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    return (cv > q75).astype(float)


def vds_103_vol_low_dispersion_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day CV is below its own 252-day 25th percentile (compressed volume)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    q25 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return (cv < q25).astype(float)


def vds_104_vol_dispersion_regime_score_21d(volume: pd.Series) -> pd.Series:
    """Signed regime: +1 high dispersion, -1 low dispersion, 0 neutral (21-day CV)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    q75 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = cv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    result = pd.Series(0.0, index=volume.index)
    result[cv > q75] = 1.0
    result[cv < q25] = -1.0
    return result


def vds_105_vol_log_std_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """Ratio of 21-day log-vol std to 252-day log-vol std."""
    lv = np.log(volume.clip(lower=_EPS))
    return _safe_div(_rolling_std(lv, _TD_MON), _rolling_std(lv, _TD_YEAR))


# --- Group K (106-115): Distributional shape on conditioned subsets ---

def vds_106_vol_skew_up_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of volume on up-price days only, 63-day window."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    return vol_up.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vds_107_vol_skew_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of volume on down-price days only, 63-day window."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    return vol_dn.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()


def vds_108_vol_kurt_up_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling kurtosis of volume on up-price days only, 63-day window."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    return vol_up.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vds_109_vol_kurt_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling kurtosis of volume on down-price days only, 63-day window."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    return vol_dn.rolling(_TD_QTR, min_periods=max(4, _TD_QTR // 2)).kurt()


def vds_110_vol_cv_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of volume on down-price days over trailing 63 days."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    m = vol_dn.rolling(_TD_QTR, min_periods=1).mean()
    s = vol_dn.rolling(_TD_QTR, min_periods=1).std()
    return _safe_div(s, m)


def vds_111_vol_cv_up_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of volume on up-price days over trailing 63 days."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    m = vol_up.rolling(_TD_QTR, min_periods=1).mean()
    s = vol_up.rolling(_TD_QTR, min_periods=1).std()
    return _safe_div(s, m)


def vds_112_vol_cv_down_vs_up_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of down-day CV to up-day CV of volume over 63 days."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    vol_up = volume.where(ret > 0, np.nan)
    cv_dn = _safe_div(vol_dn.rolling(_TD_QTR, min_periods=1).std(),
                      vol_dn.rolling(_TD_QTR, min_periods=1).mean())
    cv_up = _safe_div(vol_up.rolling(_TD_QTR, min_periods=1).std(),
                      vol_up.rolling(_TD_QTR, min_periods=1).mean())
    return _safe_div(cv_dn, cv_up)


def vds_113_vol_skew_down_vs_up_diff_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Difference in skewness: down-day vol skew minus up-day vol skew over 63 days."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    vol_up = volume.where(ret > 0, np.nan)
    sk_dn = vol_dn.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    sk_up = vol_up.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).skew()
    return sk_dn - sk_up


def vds_114_vol_iqr_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """IQR of volume on down-price days over trailing 63 days."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    q75 = vol_dn.rolling(_TD_QTR, min_periods=1).quantile(0.75)
    q25 = vol_dn.rolling(_TD_QTR, min_periods=1).quantile(0.25)
    return q75 - q25


def vds_115_vol_mean_median_gap_down_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(Mean - median) of down-day volume normalized by median over 63 days."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    m = vol_dn.rolling(_TD_QTR, min_periods=1).mean()
    med = vol_dn.rolling(_TD_QTR, min_periods=1).median()
    return _safe_div(m - med, med)


# --- Group L (116-125): Log-return-of-volume based distributional shape ---

def vds_116_vol_chg_skew_21d(volume: pd.Series) -> pd.Series:
    """Skewness of daily volume changes (volume.pct_change) over 21 days."""
    vc = volume.pct_change(1)
    return _rolling_skew(vc, _TD_MON)


def vds_117_vol_chg_skew_63d(volume: pd.Series) -> pd.Series:
    """Skewness of daily volume changes over 63 days."""
    vc = volume.pct_change(1)
    return _rolling_skew(vc, _TD_QTR)


def vds_118_vol_chg_kurt_21d(volume: pd.Series) -> pd.Series:
    """Kurtosis of daily volume changes over 21 days."""
    vc = volume.pct_change(1)
    return _rolling_kurt(vc, _TD_MON)


def vds_119_vol_chg_kurt_63d(volume: pd.Series) -> pd.Series:
    """Kurtosis of daily volume changes over 63 days."""
    vc = volume.pct_change(1)
    return _rolling_kurt(vc, _TD_QTR)


def vds_120_vol_chg_cv_21d(volume: pd.Series) -> pd.Series:
    """CV of daily volume changes (std/|mean|) over 21 days."""
    vc = volume.pct_change(1)
    m = _rolling_mean(vc.abs(), _TD_MON)
    s = _rolling_std(vc, _TD_MON)
    return _safe_div(s, m)


def vds_121_vol_chg_cv_63d(volume: pd.Series) -> pd.Series:
    """CV of daily volume changes over 63 days."""
    vc = volume.pct_change(1)
    m = _rolling_mean(vc.abs(), _TD_QTR)
    s = _rolling_std(vc, _TD_QTR)
    return _safe_div(s, m)


def vds_122_vol_log_chg_skew_21d(volume: pd.Series) -> pd.Series:
    """Skewness of log-volume daily changes over 21 days."""
    lvc = np.log(volume.clip(lower=_EPS)).diff(1)
    return _rolling_skew(lvc, _TD_MON)


def vds_123_vol_log_chg_skew_63d(volume: pd.Series) -> pd.Series:
    """Skewness of log-volume daily changes over 63 days."""
    lvc = np.log(volume.clip(lower=_EPS)).diff(1)
    return _rolling_skew(lvc, _TD_QTR)


def vds_124_vol_log_chg_kurt_63d(volume: pd.Series) -> pd.Series:
    """Kurtosis of log-volume daily changes over 63 days."""
    lvc = np.log(volume.clip(lower=_EPS)).diff(1)
    return _rolling_kurt(lvc, _TD_QTR)


def vds_125_vol_chg_iqr_norm_63d(volume: pd.Series) -> pd.Series:
    """Normalized IQR of daily volume pct-changes over 63 days."""
    vc = volume.pct_change(1)
    q75 = _rolling_quantile(vc, _TD_QTR, 0.75)
    q25 = _rolling_quantile(vc, _TD_QTR, 0.25)
    med = _rolling_median(vc, _TD_QTR)
    return _safe_div(q75 - q25, med.abs().clip(lower=_EPS))


# --- Group M (126-135): Distributional shape relative to longer baseline ---

def vds_126_vol_skew_21d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference: 21-day skew minus 252-day skew (short vs long skew gap)."""
    return _rolling_skew(volume, _TD_MON) - _rolling_skew(volume, _TD_YEAR)


def vds_127_vol_kurt_21d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference: 21-day kurtosis minus 252-day kurtosis."""
    return _rolling_kurt(volume, _TD_MON) - _rolling_kurt(volume, _TD_YEAR)


def vds_128_vol_skew_63d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference: 63-day skew minus 252-day skew."""
    return _rolling_skew(volume, _TD_QTR) - _rolling_skew(volume, _TD_YEAR)


def vds_129_vol_kurt_63d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference: 63-day kurtosis minus 252-day kurtosis."""
    return _rolling_kurt(volume, _TD_QTR) - _rolling_kurt(volume, _TD_YEAR)


def vds_130_vol_cv_21d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference: 21-day CV minus 252-day CV."""
    cv21 = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    cv252 = _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    return cv21 - cv252


def vds_131_vol_iqr_norm_63d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference in normalized IQR: 63-day minus 252-day."""
    iqr63n = _safe_div(
        _rolling_quantile(volume, _TD_QTR, 0.75) - _rolling_quantile(volume, _TD_QTR, 0.25),
        _rolling_median(volume, _TD_QTR))
    iqr252n = _safe_div(
        _rolling_quantile(volume, _TD_YEAR, 0.75) - _rolling_quantile(volume, _TD_YEAR, 0.25),
        _rolling_median(volume, _TD_YEAR))
    return iqr63n - iqr252n


def vds_132_vol_mean_median_ratio_21d_vs_252d_diff(volume: pd.Series) -> pd.Series:
    """Difference in mean/median ratio: 21-day minus 252-day."""
    r21 = _safe_div(_rolling_mean(volume, _TD_MON), _rolling_median(volume, _TD_MON))
    r252 = _safe_div(_rolling_mean(volume, _TD_YEAR), _rolling_median(volume, _TD_YEAR))
    return r21 - r252


def vds_133_vol_skew_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day volume skew (all-history extremity)."""
    sk = _rolling_skew(volume, _TD_MON)
    return sk.expanding(min_periods=5).rank(pct=True)


def vds_134_vol_kurt_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day volume kurtosis."""
    k = _rolling_kurt(volume, _TD_MON)
    return k.expanding(min_periods=5).rank(pct=True)


def vds_135_vol_cv_21d_expanding_rank(volume: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day CV (all-history dispersion rank)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return cv.expanding(min_periods=5).rank(pct=True)


# --- Group N (136-145): Composite distributional shape scores ---

def vds_136_vol_shape_composite_21d(volume: pd.Series) -> pd.Series:
    """Composite: avg of normalized skew, kurtosis, and CV over 21 days."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    return (sk_z + k_z + cv_z) / 3.0


def vds_137_vol_shape_composite_63d(volume: pd.Series) -> pd.Series:
    """Composite: avg of normalized skew, kurtosis, and CV over 63 days."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    cv = _safe_div(_rolling_std(volume, _TD_QTR), _rolling_mean(volume, _TD_QTR))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    return (sk_z + k_z + cv_z) / 3.0


def vds_138_vol_dispersion_breadth_21d(volume: pd.Series) -> pd.Series:
    """Breadth of dispersion: (std + IQR/1.35 + log-std) averaged over 21 days."""
    std21 = _rolling_std(volume, _TD_MON)
    iqr21 = _rolling_quantile(volume, _TD_MON, 0.75) - _rolling_quantile(volume, _TD_MON, 0.25)
    lv = np.log(volume.clip(lower=_EPS))
    lstd21 = _rolling_std(lv, _TD_MON)
    mean21 = _rolling_mean(volume, _TD_MON).clip(lower=_EPS)
    return _safe_div(std21 + iqr21 / 1.35 + lstd21 * mean21, 3.0 * mean21)


def vds_139_vol_skew_positive_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day volume skew is positive (right-skewed distribution)."""
    return (_rolling_skew(volume, _TD_MON) > 0).astype(float)


def vds_140_vol_extreme_skew_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: |21-day skew| > 2 (highly asymmetric volume distribution)."""
    return (_rolling_skew(volume, _TD_MON).abs() > 2).astype(float)


def vds_141_vol_extreme_kurt_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: 21-day excess kurtosis > 5 (very fat-tailed volume)."""
    return (_rolling_kurt(volume, _TD_MON) > 5).astype(float)


def vds_142_vol_low_skew_high_kurt_flag_21d(volume: pd.Series) -> pd.Series:
    """Flag: |21-day skew| < 0.5 AND excess kurtosis > 3 (symmetric fat tails)."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    return ((sk.abs() < 0.5) & (k > 3)).astype(float)


def vds_143_vol_skew_trend_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day skew over trailing 63 days (trend in skew)."""
    sk = _rolling_skew(volume, _TD_MON)
    return _linslope(sk, _TD_QTR)


def vds_144_vol_cv_trend_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day CV over trailing 63 days (trend in dispersion)."""
    cv = _safe_div(_rolling_std(volume, _TD_MON), _rolling_mean(volume, _TD_MON))
    return _linslope(cv, _TD_QTR)


def vds_145_vol_kurt_trend_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day kurtosis over trailing 63 days."""
    k = _rolling_kurt(volume, _TD_MON)
    return _linslope(k, _TD_QTR)


# --- Group O (146-150): Miscellaneous shape and spread measures ---

def vds_146_vol_mad_21d(volume: pd.Series) -> pd.Series:
    """Mean absolute deviation of volume over 21 days (robust dispersion)."""
    m = _rolling_mean(volume, _TD_MON)
    return (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()


def vds_147_vol_mad_63d(volume: pd.Series) -> pd.Series:
    """Mean absolute deviation of volume over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    return (volume - m).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vds_148_vol_mad_norm_21d(volume: pd.Series) -> pd.Series:
    """MAD normalized by mean over 21 days (relative mean absolute deviation)."""
    m = _rolling_mean(volume, _TD_MON)
    mad = (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    return _safe_div(mad, m)


def vds_149_vol_mad_norm_63d(volume: pd.Series) -> pd.Series:
    """MAD normalized by mean over 63 days."""
    m = _rolling_mean(volume, _TD_QTR)
    mad = (volume - m).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return _safe_div(mad, m)


def vds_150_vol_bimodality_coefficient_63d(volume: pd.Series) -> pd.Series:
    """Bimodality coefficient (skew^2+1)/kurtosis over 63 days; >5/9 suggests bimodality."""
    sk = _rolling_skew(volume, _TD_QTR)
    k = _rolling_kurt(volume, _TD_QTR)
    return _safe_div(sk ** 2 + 1, k.clip(lower=_EPS))


# --- Group P (176-200): Conditioned subsets extended, change-skew extended, composites ---

def vds_176_vol_skew_up_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of volume on up-price days only, 252-day window."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    return vol_up.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


def vds_177_vol_skew_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling skewness of volume on down-price days only, 252-day window."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    return vol_dn.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).skew()


def vds_178_vol_cv_up_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of volume on up-price days over trailing 252 days."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    m = vol_up.rolling(_TD_YEAR, min_periods=1).mean()
    s = vol_up.rolling(_TD_YEAR, min_periods=1).std()
    return _safe_div(s, m)


def vds_179_vol_cv_down_days_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of volume on down-price days over trailing 252 days."""
    ret = close.pct_change(1)
    vol_dn = volume.where(ret < 0, np.nan)
    m = vol_dn.rolling(_TD_YEAR, min_periods=1).mean()
    s = vol_dn.rolling(_TD_YEAR, min_periods=1).std()
    return _safe_div(s, m)


def vds_180_vol_iqr_up_days_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """IQR of volume on up-price days over trailing 63 days."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    q75 = vol_up.rolling(_TD_QTR, min_periods=1).quantile(0.75)
    q25 = vol_up.rolling(_TD_QTR, min_periods=1).quantile(0.25)
    return q75 - q25


def vds_181_vol_iqr_up_vs_down_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of up-day IQR to down-day IQR of volume over 63 days."""
    ret = close.pct_change(1)
    vol_up = volume.where(ret > 0, np.nan)
    vol_dn = volume.where(ret < 0, np.nan)
    iqr_up = vol_up.rolling(_TD_QTR, min_periods=1).quantile(0.75) - vol_up.rolling(_TD_QTR, min_periods=1).quantile(0.25)
    iqr_dn = vol_dn.rolling(_TD_QTR, min_periods=1).quantile(0.75) - vol_dn.rolling(_TD_QTR, min_periods=1).quantile(0.25)
    return _safe_div(iqr_up, iqr_dn)


def vds_182_vol_chg_skew_126d(volume: pd.Series) -> pd.Series:
    """Skewness of daily volume pct-changes over 126 days."""
    vc = volume.pct_change(1)
    return _rolling_skew(vc, _TD_HALF)


def vds_183_vol_chg_kurt_126d(volume: pd.Series) -> pd.Series:
    """Kurtosis of daily volume pct-changes over 126 days."""
    vc = volume.pct_change(1)
    return _rolling_kurt(vc, _TD_HALF)


def vds_184_vol_log_chg_kurt_21d(volume: pd.Series) -> pd.Series:
    """Kurtosis of log-volume daily changes over 21 days."""
    lvc = np.log(volume.clip(lower=_EPS)).diff(1)
    return _rolling_kurt(lvc, _TD_MON)


def vds_185_vol_chg_iqr_norm_21d(volume: pd.Series) -> pd.Series:
    """Normalized IQR of daily volume pct-changes over 21 days."""
    vc = volume.pct_change(1)
    q75 = _rolling_quantile(vc, _TD_MON, 0.75)
    q25 = _rolling_quantile(vc, _TD_MON, 0.25)
    med = _rolling_median(vc, _TD_MON)
    return _safe_div(q75 - q25, med.abs().clip(lower=_EPS))


def vds_186_vol_chg_90_10_spread_63d(volume: pd.Series) -> pd.Series:
    """90th-10th percentile spread of daily volume pct-changes over 63 days."""
    vc = volume.pct_change(1)
    q90 = _rolling_quantile(vc, _TD_QTR, 0.90)
    q10 = _rolling_quantile(vc, _TD_QTR, 0.10)
    return q90 - q10


def vds_187_vol_chg_mean_median_gap_norm_21d(volume: pd.Series) -> pd.Series:
    """(Mean-median)/std of daily volume pct-changes over 21 days."""
    vc = volume.pct_change(1)
    m = _rolling_mean(vc, _TD_MON)
    med = _rolling_median(vc, _TD_MON)
    s = _rolling_std(vc, _TD_MON)
    return _safe_div(m - med, s)


def vds_188_vol_bimodality_coefficient_21d(volume: pd.Series) -> pd.Series:
    """Bimodality coefficient (skew^2+1)/kurtosis over 21 days."""
    sk = _rolling_skew(volume, _TD_MON)
    k = _rolling_kurt(volume, _TD_MON)
    return _safe_div(sk ** 2 + 1, k.clip(lower=_EPS))


def vds_189_vol_bimodality_coefficient_252d(volume: pd.Series) -> pd.Series:
    """Bimodality coefficient (skew^2+1)/kurtosis over 252 days."""
    sk = _rolling_skew(volume, _TD_YEAR)
    k = _rolling_kurt(volume, _TD_YEAR)
    return _safe_div(sk ** 2 + 1, k.clip(lower=_EPS))


def vds_190_vol_mad_norm_252d(volume: pd.Series) -> pd.Series:
    """MAD normalized by mean over 252 days (long-run relative mean absolute deviation)."""
    m = _rolling_mean(volume, _TD_YEAR)
    mad = (volume - m).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()
    return _safe_div(mad, m)


def vds_191_vol_mad_252d(volume: pd.Series) -> pd.Series:
    """Mean absolute deviation of volume over 252 days (raw long-run MAD)."""
    m = _rolling_mean(volume, _TD_YEAR)
    return (volume - m).abs().rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).mean()


def vds_192_vol_skew_trend_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day volume skew over trailing 252 days."""
    sk = _rolling_skew(volume, _TD_QTR)
    return _linslope(sk, _TD_YEAR)


def vds_193_vol_kurt_trend_63d_slope_252d(volume: pd.Series) -> pd.Series:
    """OLS slope of 63-day volume kurtosis over trailing 252 days."""
    k = _rolling_kurt(volume, _TD_QTR)
    return _linslope(k, _TD_YEAR)


def vds_194_vol_mad_trend_21d_slope_63d(volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day MAD (normalized) over trailing 63 days."""
    m = _rolling_mean(volume, _TD_MON)
    mad = (volume - m).abs().rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).mean()
    mad_n = _safe_div(mad, m)
    return _linslope(mad_n, _TD_QTR)


def vds_195_vol_dispersion_breadth_63d(volume: pd.Series) -> pd.Series:
    """Breadth of dispersion: (std + IQR/1.35 + log-std) averaged over 63 days."""
    std63 = _rolling_std(volume, _TD_QTR)
    iqr63 = _rolling_quantile(volume, _TD_QTR, 0.75) - _rolling_quantile(volume, _TD_QTR, 0.25)
    lv = np.log(volume.clip(lower=_EPS))
    lstd63 = _rolling_std(lv, _TD_QTR)
    mean63 = _rolling_mean(volume, _TD_QTR).clip(lower=_EPS)
    return _safe_div(std63 + iqr63 / 1.35 + lstd63 * mean63, 3.0 * mean63)


def vds_196_vol_shape_composite_252d(volume: pd.Series) -> pd.Series:
    """Composite: avg of z-normalized skew, kurtosis, and CV over 252 days."""
    sk = _rolling_skew(volume, _TD_YEAR)
    k = _rolling_kurt(volume, _TD_YEAR)
    cv = _safe_div(_rolling_std(volume, _TD_YEAR), _rolling_mean(volume, _TD_YEAR))
    sk_z = _safe_div(sk - _rolling_mean(sk, _TD_YEAR), _rolling_std(sk, _TD_YEAR))
    k_z = _safe_div(k - _rolling_mean(k, _TD_YEAR), _rolling_std(k, _TD_YEAR))
    cv_z = _safe_div(cv - _rolling_mean(cv, _TD_YEAR), _rolling_std(cv, _TD_YEAR))
    return (sk_z + k_z + cv_z) / 3.0


def vds_197_vol_skew_kurt_product_252d(volume: pd.Series) -> pd.Series:
    """Product of 252-day skew and excess kurtosis (long-run joint non-normality)."""
    sk = _rolling_skew(volume, _TD_YEAR)
    k = _rolling_kurt(volume, _TD_YEAR)
    return sk * k


def vds_198_vol_cv_126d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 126-day CV vs its 252-day rolling distribution."""
    cv = _safe_div(_rolling_std(volume, _TD_HALF), _rolling_mean(volume, _TD_HALF))
    m = _rolling_mean(cv, _TD_YEAR)
    s = _rolling_std(cv, _TD_YEAR)
    return _safe_div(cv - m, s)


def vds_199_vol_iqr_norm_126d_zscore_252d(volume: pd.Series) -> pd.Series:
    """Z-score of 126-day normalized IQR vs its 252-day distribution."""
    q75 = _rolling_quantile(volume, _TD_HALF, 0.75)
    q25 = _rolling_quantile(volume, _TD_HALF, 0.25)
    med = _rolling_median(volume, _TD_HALF)
    iqr_n = _safe_div(q75 - q25, med)
    m = _rolling_mean(iqr_n, _TD_YEAR)
    s = _rolling_std(iqr_n, _TD_YEAR)
    return _safe_div(iqr_n - m, s)


def vds_200_vol_extreme_skew_flag_63d(volume: pd.Series) -> pd.Series:
    """Flag: |63-day skew| > 2 (highly asymmetric volume distribution)."""
    return (_rolling_skew(volume, _TD_QTR).abs() > 2).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLUME_DISTRIBUTION_REGISTRY_076_150 = {
    "vds_076_vol_ewm_cv_21d": {"inputs": ["volume"], "func": vds_076_vol_ewm_cv_21d},
    "vds_077_vol_ewm_cv_63d": {"inputs": ["volume"], "func": vds_077_vol_ewm_cv_63d},
    "vds_078_vol_ewm_cv_126d": {"inputs": ["volume"], "func": vds_078_vol_ewm_cv_126d},
    "vds_079_vol_ewm_vs_sma_cv_ratio_21d": {"inputs": ["volume"], "func": vds_079_vol_ewm_vs_sma_cv_ratio_21d},
    "vds_080_vol_ewm_mean_to_median_ratio_63d": {"inputs": ["volume"], "func": vds_080_vol_ewm_mean_to_median_ratio_63d},
    "vds_081_vol_log_ewm_std_21d": {"inputs": ["volume"], "func": vds_081_vol_log_ewm_std_21d},
    "vds_082_vol_log_ewm_std_63d": {"inputs": ["volume"], "func": vds_082_vol_log_ewm_std_63d},
    "vds_083_vol_ewm_cv_21d_pct_rank_252d": {"inputs": ["volume"], "func": vds_083_vol_ewm_cv_21d_pct_rank_252d},
    "vds_084_vol_ewm_cv_ratio_21d_vs_126d": {"inputs": ["volume"], "func": vds_084_vol_ewm_cv_ratio_21d_vs_126d},
    "vds_085_vol_ewm_std_zscore_252d": {"inputs": ["volume"], "func": vds_085_vol_ewm_std_zscore_252d},
    "vds_086_vol_skew_21d_zscore_252d": {"inputs": ["volume"], "func": vds_086_vol_skew_21d_zscore_252d},
    "vds_087_vol_kurt_21d_zscore_252d": {"inputs": ["volume"], "func": vds_087_vol_kurt_21d_zscore_252d},
    "vds_088_vol_skew_126d_zscore_expanding": {"inputs": ["volume"], "func": vds_088_vol_skew_126d_zscore_expanding},
    "vds_089_vol_kurt_126d_zscore_expanding": {"inputs": ["volume"], "func": vds_089_vol_kurt_126d_zscore_expanding},
    "vds_090_vol_cv_21d_zscore_252d": {"inputs": ["volume"], "func": vds_090_vol_cv_21d_zscore_252d},
    "vds_091_vol_iqr_norm_21d_zscore_252d": {"inputs": ["volume"], "func": vds_091_vol_iqr_norm_21d_zscore_252d},
    "vds_092_vol_90_10_spread_norm_zscore_252d": {"inputs": ["volume"], "func": vds_092_vol_90_10_spread_norm_zscore_252d},
    "vds_093_vol_mean_median_gap_norm_21d_zscore": {"inputs": ["volume"], "func": vds_093_vol_mean_median_gap_norm_21d_zscore},
    "vds_094_vol_skew_kurt_product_21d": {"inputs": ["volume"], "func": vds_094_vol_skew_kurt_product_21d},
    "vds_095_vol_skew_kurt_product_63d": {"inputs": ["volume"], "func": vds_095_vol_skew_kurt_product_63d},
    "vds_096_vol_cv_ratio_63d_vs_252d": {"inputs": ["volume"], "func": vds_096_vol_cv_ratio_63d_vs_252d},
    "vds_097_vol_iqr_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vds_097_vol_iqr_ratio_21d_vs_252d},
    "vds_098_vol_skew_ratio_21d_vs_63d": {"inputs": ["volume"], "func": vds_098_vol_skew_ratio_21d_vs_63d},
    "vds_099_vol_kurt_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vds_099_vol_kurt_ratio_21d_vs_252d},
    "vds_100_vol_std_ratio_5d_vs_63d": {"inputs": ["volume"], "func": vds_100_vol_std_ratio_5d_vs_63d},
    "vds_101_vol_std_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vds_101_vol_std_ratio_21d_vs_252d},
    "vds_102_vol_high_dispersion_flag_21d": {"inputs": ["volume"], "func": vds_102_vol_high_dispersion_flag_21d},
    "vds_103_vol_low_dispersion_flag_21d": {"inputs": ["volume"], "func": vds_103_vol_low_dispersion_flag_21d},
    "vds_104_vol_dispersion_regime_score_21d": {"inputs": ["volume"], "func": vds_104_vol_dispersion_regime_score_21d},
    "vds_105_vol_log_std_ratio_21d_vs_252d": {"inputs": ["volume"], "func": vds_105_vol_log_std_ratio_21d_vs_252d},
    "vds_106_vol_skew_up_days_63d": {"inputs": ["close", "volume"], "func": vds_106_vol_skew_up_days_63d},
    "vds_107_vol_skew_down_days_63d": {"inputs": ["close", "volume"], "func": vds_107_vol_skew_down_days_63d},
    "vds_108_vol_kurt_up_days_63d": {"inputs": ["close", "volume"], "func": vds_108_vol_kurt_up_days_63d},
    "vds_109_vol_kurt_down_days_63d": {"inputs": ["close", "volume"], "func": vds_109_vol_kurt_down_days_63d},
    "vds_110_vol_cv_down_days_63d": {"inputs": ["close", "volume"], "func": vds_110_vol_cv_down_days_63d},
    "vds_111_vol_cv_up_days_63d": {"inputs": ["close", "volume"], "func": vds_111_vol_cv_up_days_63d},
    "vds_112_vol_cv_down_vs_up_ratio_63d": {"inputs": ["close", "volume"], "func": vds_112_vol_cv_down_vs_up_ratio_63d},
    "vds_113_vol_skew_down_vs_up_diff_63d": {"inputs": ["close", "volume"], "func": vds_113_vol_skew_down_vs_up_diff_63d},
    "vds_114_vol_iqr_down_days_63d": {"inputs": ["close", "volume"], "func": vds_114_vol_iqr_down_days_63d},
    "vds_115_vol_mean_median_gap_down_days_63d": {"inputs": ["close", "volume"], "func": vds_115_vol_mean_median_gap_down_days_63d},
    "vds_116_vol_chg_skew_21d": {"inputs": ["volume"], "func": vds_116_vol_chg_skew_21d},
    "vds_117_vol_chg_skew_63d": {"inputs": ["volume"], "func": vds_117_vol_chg_skew_63d},
    "vds_118_vol_chg_kurt_21d": {"inputs": ["volume"], "func": vds_118_vol_chg_kurt_21d},
    "vds_119_vol_chg_kurt_63d": {"inputs": ["volume"], "func": vds_119_vol_chg_kurt_63d},
    "vds_120_vol_chg_cv_21d": {"inputs": ["volume"], "func": vds_120_vol_chg_cv_21d},
    "vds_121_vol_chg_cv_63d": {"inputs": ["volume"], "func": vds_121_vol_chg_cv_63d},
    "vds_122_vol_log_chg_skew_21d": {"inputs": ["volume"], "func": vds_122_vol_log_chg_skew_21d},
    "vds_123_vol_log_chg_skew_63d": {"inputs": ["volume"], "func": vds_123_vol_log_chg_skew_63d},
    "vds_124_vol_log_chg_kurt_63d": {"inputs": ["volume"], "func": vds_124_vol_log_chg_kurt_63d},
    "vds_125_vol_chg_iqr_norm_63d": {"inputs": ["volume"], "func": vds_125_vol_chg_iqr_norm_63d},
    "vds_126_vol_skew_21d_vs_252d_diff": {"inputs": ["volume"], "func": vds_126_vol_skew_21d_vs_252d_diff},
    "vds_127_vol_kurt_21d_vs_252d_diff": {"inputs": ["volume"], "func": vds_127_vol_kurt_21d_vs_252d_diff},
    "vds_128_vol_skew_63d_vs_252d_diff": {"inputs": ["volume"], "func": vds_128_vol_skew_63d_vs_252d_diff},
    "vds_129_vol_kurt_63d_vs_252d_diff": {"inputs": ["volume"], "func": vds_129_vol_kurt_63d_vs_252d_diff},
    "vds_130_vol_cv_21d_vs_252d_diff": {"inputs": ["volume"], "func": vds_130_vol_cv_21d_vs_252d_diff},
    "vds_131_vol_iqr_norm_63d_vs_252d_diff": {"inputs": ["volume"], "func": vds_131_vol_iqr_norm_63d_vs_252d_diff},
    "vds_132_vol_mean_median_ratio_21d_vs_252d_diff": {"inputs": ["volume"], "func": vds_132_vol_mean_median_ratio_21d_vs_252d_diff},
    "vds_133_vol_skew_21d_expanding_rank": {"inputs": ["volume"], "func": vds_133_vol_skew_21d_expanding_rank},
    "vds_134_vol_kurt_21d_expanding_rank": {"inputs": ["volume"], "func": vds_134_vol_kurt_21d_expanding_rank},
    "vds_135_vol_cv_21d_expanding_rank": {"inputs": ["volume"], "func": vds_135_vol_cv_21d_expanding_rank},
    "vds_136_vol_shape_composite_21d": {"inputs": ["volume"], "func": vds_136_vol_shape_composite_21d},
    "vds_137_vol_shape_composite_63d": {"inputs": ["volume"], "func": vds_137_vol_shape_composite_63d},
    "vds_138_vol_dispersion_breadth_21d": {"inputs": ["volume"], "func": vds_138_vol_dispersion_breadth_21d},
    "vds_139_vol_skew_positive_flag_21d": {"inputs": ["volume"], "func": vds_139_vol_skew_positive_flag_21d},
    "vds_140_vol_extreme_skew_flag_21d": {"inputs": ["volume"], "func": vds_140_vol_extreme_skew_flag_21d},
    "vds_141_vol_extreme_kurt_flag_21d": {"inputs": ["volume"], "func": vds_141_vol_extreme_kurt_flag_21d},
    "vds_142_vol_low_skew_high_kurt_flag_21d": {"inputs": ["volume"], "func": vds_142_vol_low_skew_high_kurt_flag_21d},
    "vds_143_vol_skew_trend_21d_slope_63d": {"inputs": ["volume"], "func": vds_143_vol_skew_trend_21d_slope_63d},
    "vds_144_vol_cv_trend_21d_slope_63d": {"inputs": ["volume"], "func": vds_144_vol_cv_trend_21d_slope_63d},
    "vds_145_vol_kurt_trend_21d_slope_63d": {"inputs": ["volume"], "func": vds_145_vol_kurt_trend_21d_slope_63d},
    "vds_146_vol_mad_21d": {"inputs": ["volume"], "func": vds_146_vol_mad_21d},
    "vds_147_vol_mad_63d": {"inputs": ["volume"], "func": vds_147_vol_mad_63d},
    "vds_148_vol_mad_norm_21d": {"inputs": ["volume"], "func": vds_148_vol_mad_norm_21d},
    "vds_149_vol_mad_norm_63d": {"inputs": ["volume"], "func": vds_149_vol_mad_norm_63d},
    "vds_150_vol_bimodality_coefficient_63d": {"inputs": ["volume"], "func": vds_150_vol_bimodality_coefficient_63d},
    # --- New features 176-200 ---
    "vds_176_vol_skew_up_days_252d": {"inputs": ["close", "volume"], "func": vds_176_vol_skew_up_days_252d},
    "vds_177_vol_skew_down_days_252d": {"inputs": ["close", "volume"], "func": vds_177_vol_skew_down_days_252d},
    "vds_178_vol_cv_up_days_252d": {"inputs": ["close", "volume"], "func": vds_178_vol_cv_up_days_252d},
    "vds_179_vol_cv_down_days_252d": {"inputs": ["close", "volume"], "func": vds_179_vol_cv_down_days_252d},
    "vds_180_vol_iqr_up_days_63d": {"inputs": ["close", "volume"], "func": vds_180_vol_iqr_up_days_63d},
    "vds_181_vol_iqr_up_vs_down_ratio_63d": {"inputs": ["close", "volume"], "func": vds_181_vol_iqr_up_vs_down_ratio_63d},
    "vds_182_vol_chg_skew_126d": {"inputs": ["volume"], "func": vds_182_vol_chg_skew_126d},
    "vds_183_vol_chg_kurt_126d": {"inputs": ["volume"], "func": vds_183_vol_chg_kurt_126d},
    "vds_184_vol_log_chg_kurt_21d": {"inputs": ["volume"], "func": vds_184_vol_log_chg_kurt_21d},
    "vds_185_vol_chg_iqr_norm_21d": {"inputs": ["volume"], "func": vds_185_vol_chg_iqr_norm_21d},
    "vds_186_vol_chg_90_10_spread_63d": {"inputs": ["volume"], "func": vds_186_vol_chg_90_10_spread_63d},
    "vds_187_vol_chg_mean_median_gap_norm_21d": {"inputs": ["volume"], "func": vds_187_vol_chg_mean_median_gap_norm_21d},
    "vds_188_vol_bimodality_coefficient_21d": {"inputs": ["volume"], "func": vds_188_vol_bimodality_coefficient_21d},
    "vds_189_vol_bimodality_coefficient_252d": {"inputs": ["volume"], "func": vds_189_vol_bimodality_coefficient_252d},
    "vds_190_vol_mad_norm_252d": {"inputs": ["volume"], "func": vds_190_vol_mad_norm_252d},
    "vds_191_vol_mad_252d": {"inputs": ["volume"], "func": vds_191_vol_mad_252d},
    "vds_192_vol_skew_trend_63d_slope_252d": {"inputs": ["volume"], "func": vds_192_vol_skew_trend_63d_slope_252d},
    "vds_193_vol_kurt_trend_63d_slope_252d": {"inputs": ["volume"], "func": vds_193_vol_kurt_trend_63d_slope_252d},
    "vds_194_vol_mad_trend_21d_slope_63d": {"inputs": ["volume"], "func": vds_194_vol_mad_trend_21d_slope_63d},
    "vds_195_vol_dispersion_breadth_63d": {"inputs": ["volume"], "func": vds_195_vol_dispersion_breadth_63d},
    "vds_196_vol_shape_composite_252d": {"inputs": ["volume"], "func": vds_196_vol_shape_composite_252d},
    "vds_197_vol_skew_kurt_product_252d": {"inputs": ["volume"], "func": vds_197_vol_skew_kurt_product_252d},
    "vds_198_vol_cv_126d_zscore_252d": {"inputs": ["volume"], "func": vds_198_vol_cv_126d_zscore_252d},
    "vds_199_vol_iqr_norm_126d_zscore_252d": {"inputs": ["volume"], "func": vds_199_vol_iqr_norm_126d_zscore_252d},
    "vds_200_vol_extreme_skew_flag_63d": {"inputs": ["volume"], "func": vds_200_vol_extreme_skew_flag_63d},
}
