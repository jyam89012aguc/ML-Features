"""
42_volatility_of_volatility — Extended Features 001-075
Domain: instability of the volatility series itself (vol-of-vol) — extended variants
Measures: Parkinson vol-of-vol, Garman-Klass vol-of-vol, Rogers-Satchell vol-of-vol,
          vol-of-vol on volume-weighted vols, vol stability/instability flags,
          vol regime classification, cross-estimator vov spreads, vov on intraday
          vs close-to-close, vol entropy proxies, conditional vov, vov on
          normalized price series, vov streaks, tail-frequency measures.
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
_SQRT252 = 252 ** 0.5

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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).std()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS) / s.shift(1).clip(lower=_EPS))


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized close-to-close realized volatility over w-day rolling window."""
    lr = _log_ret(close)
    return lr.rolling(w, min_periods=max(2, w // 2)).std() * _SQRT252


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Parkinson (1980) high-low range volatility estimator, annualized."""
    hl2 = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS)) ** 2
    factor = 1.0 / (4.0 * np.log(2.0))
    daily_var = factor * hl2
    return (daily_var.rolling(w, min_periods=max(2, w // 2)).mean() * _TD_YEAR) ** 0.5


def _garman_klass_vol(close: pd.Series, high: pd.Series, low: pd.Series,
                      open_: pd.Series, w: int) -> pd.Series:
    """Garman-Klass (1980) OHLC volatility estimator, annualized."""
    log_hl = np.log(high.clip(lower=_EPS) / low.clip(lower=_EPS))
    log_co = np.log(close.clip(lower=_EPS) / open_.clip(lower=_EPS))
    gk = 0.5 * log_hl ** 2 - (2.0 * np.log(2.0) - 1.0) * log_co ** 2
    return (gk.rolling(w, min_periods=max(2, w // 2)).mean() * _TD_YEAR) ** 0.5


def _rogers_satchell_vol(close: pd.Series, high: pd.Series, low: pd.Series,
                         open_: pd.Series, w: int) -> pd.Series:
    """Rogers-Satchell (1991) volatility estimator, annualized."""
    lhc = np.log(high.clip(lower=_EPS) / close.clip(lower=_EPS))
    llc = np.log(low.clip(lower=_EPS) / close.clip(lower=_EPS))
    lho = np.log(high.clip(lower=_EPS) / open_.clip(lower=_EPS))
    llo = np.log(low.clip(lower=_EPS) / open_.clip(lower=_EPS))
    rs = lhc * lho + llc * llo
    return (rs.clip(lower=0).rolling(w, min_periods=max(2, w // 2)).mean() * _TD_YEAR) ** 0.5


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


def _atr(close: pd.Series, high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Average True Range over w-day window."""
    return _rolling_mean(_tr(close, high, low), w)


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

# --- Group A (001-015): Parkinson vol-of-vol (std/CV/range of Parkinson vol) ---

def vov_ext_001_std_park_vol21_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of 21-day Parkinson vol over trailing 63 days (Parkinson vov)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return _rolling_std(pv, _TD_QTR)


def vov_ext_002_std_park_vol21_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of 21-day Parkinson vol over trailing 252 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return _rolling_std(pv, _TD_YEAR)


def vov_ext_003_cv_park_vol21_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of 21-day Parkinson vol over trailing 63 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return _safe_div(_rolling_std(pv, _TD_QTR), _rolling_mean(pv, _TD_QTR).clip(lower=_EPS))


def vov_ext_004_cv_park_vol21_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of 21-day Parkinson vol over trailing 252 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return _safe_div(_rolling_std(pv, _TD_YEAR), _rolling_mean(pv, _TD_YEAR).clip(lower=_EPS))


def vov_ext_005_range_park_vol21_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range (max-min) of 21-day Parkinson vol over 63 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return _rolling_max(pv, _TD_QTR) - _rolling_min(pv, _TD_QTR)


def vov_ext_006_range_park_vol21_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Range of 21-day Parkinson vol over 252 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return _rolling_max(pv, _TD_YEAR) - _rolling_min(pv, _TD_YEAR)


def vov_ext_007_mac_park_vol21_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21-day Parkinson vol over 63 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return pv.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_ext_008_zscore_park_vol21_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of current 21-day Parkinson vol within trailing 252-day distribution."""
    pv = _parkinson_vol(high, low, _TD_MON)
    m = _rolling_mean(pv, _TD_YEAR)
    s = _rolling_std(pv, _TD_YEAR)
    return _safe_div(pv - m, s.clip(lower=_EPS))


def vov_ext_009_pct_rank_park_vol21_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Parkinson vol within trailing 252 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    return pv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_010_std_park_vol5_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Std of 5-day Parkinson vol over trailing 63 days."""
    pv = _parkinson_vol(high, low, _TD_WEEK)
    return _rolling_std(pv, _TD_QTR)


def vov_ext_011_cv_park_vol5_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """CV of 5-day Parkinson vol over trailing 63 days."""
    pv = _parkinson_vol(high, low, _TD_WEEK)
    return _safe_div(_rolling_std(pv, _TD_QTR), _rolling_mean(pv, _TD_QTR).clip(lower=_EPS))


def vov_ext_012_park_vs_cc_vov_ratio_63d(close: pd.Series, high: pd.Series,
                                          low: pd.Series) -> pd.Series:
    """Ratio of Parkinson vov (63d std of park_vol21) to close-to-close vov (63d std of rvol21)."""
    pv_vov = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    cc_vov = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    return _safe_div(pv_vov, cc_vov.clip(lower=_EPS))


def vov_ext_013_park_vov_above_cc_vov_flag(close: pd.Series, high: pd.Series,
                                            low: pd.Series) -> pd.Series:
    """Binary flag: 63-day Parkinson vov exceeds close-to-close vov."""
    pv_vov = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    cc_vov = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    return (pv_vov > cc_vov).astype(float)


def vov_ext_014_park_vol21_iqr_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """IQR (75th-25th pct) of 21-day Parkinson vol over trailing 63 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    q75 = pv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = pv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def vov_ext_015_park_vol21_reversal_freq_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Direction-reversal frequency of 21-day Parkinson vol over 63 days."""
    pv = _parkinson_vol(high, low, _TD_MON)
    d = pv.diff(1)
    rev = ((d > 0) & (d.shift(1) < 0)) | ((d < 0) & (d.shift(1) > 0))
    return rev.astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


# --- Group B (016-030): Garman-Klass vol-of-vol ---

def vov_ext_016_std_gk_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                  open: pd.Series) -> pd.Series:
    """Std of 21-day Garman-Klass vol over trailing 63 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return _rolling_std(gk, _TD_QTR)


def vov_ext_017_std_gk_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                   open: pd.Series) -> pd.Series:
    """Std of 21-day Garman-Klass vol over trailing 252 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return _rolling_std(gk, _TD_YEAR)


def vov_ext_018_cv_gk_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                 open: pd.Series) -> pd.Series:
    """CV of 21-day Garman-Klass vol over trailing 63 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return _safe_div(_rolling_std(gk, _TD_QTR), _rolling_mean(gk, _TD_QTR).clip(lower=_EPS))


def vov_ext_019_cv_gk_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                  open: pd.Series) -> pd.Series:
    """CV of 21-day Garman-Klass vol over trailing 252 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return _safe_div(_rolling_std(gk, _TD_YEAR), _rolling_mean(gk, _TD_YEAR).clip(lower=_EPS))


def vov_ext_020_range_gk_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                    open: pd.Series) -> pd.Series:
    """Range of 21-day Garman-Klass vol over trailing 63 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return _rolling_max(gk, _TD_QTR) - _rolling_min(gk, _TD_QTR)


def vov_ext_021_mac_gk_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                  open: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21-day Garman-Klass vol over 63 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return gk.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_ext_022_zscore_gk_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                      open: pd.Series) -> pd.Series:
    """Z-score of 21-day Garman-Klass vol within its trailing 252-day distribution."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    m = _rolling_mean(gk, _TD_YEAR)
    s = _rolling_std(gk, _TD_YEAR)
    return _safe_div(gk - m, s.clip(lower=_EPS))


def vov_ext_023_pct_rank_gk_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                        open: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Garman-Klass vol within trailing 252 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return gk.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_024_gk_vs_park_vov_spread_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                           open: pd.Series) -> pd.Series:
    """Spread: 63-day std of GK vol minus std of Parkinson vol (estimator divergence)."""
    gk_vov = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    pk_vov = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    return gk_vov - pk_vov


def vov_ext_025_gk_vol5_std_21d(close: pd.Series, high: pd.Series, low: pd.Series,
                                 open: pd.Series) -> pd.Series:
    """Std of 5-day Garman-Klass vol over trailing 21 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_WEEK)
    return _rolling_std(gk, _TD_MON)


def vov_ext_026_gk_vol21_iqr_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                  open: pd.Series) -> pd.Series:
    """IQR of 21-day Garman-Klass vol over trailing 63 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    q75 = gk.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75)
    q25 = gk.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25)
    return q75 - q25


def vov_ext_027_gk_vol21_reversal_freq_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                            open: pd.Series) -> pd.Series:
    """Direction-reversal frequency of 21-day Garman-Klass vol over 63 days."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    d = gk.diff(1)
    rev = ((d > 0) & (d.shift(1) < 0)) | ((d < 0) & (d.shift(1) > 0))
    return rev.astype(float).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).sum()


def vov_ext_028_gk_vov_above_longrun_flag(close: pd.Series, high: pd.Series, low: pd.Series,
                                           open: pd.Series) -> pd.Series:
    """Flag: 63-day GK vov exceeds its 252-day average."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv63 = _rolling_std(gk, _TD_QTR)
    avg252 = _rolling_mean(vv63, _TD_YEAR)
    return (vv63 > avg252).astype(float)


def vov_ext_029_gk_vov_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                    open: pd.Series) -> pd.Series:
    """Z-score of 63-day GK vov within its trailing 252-day distribution."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv63 = _rolling_std(gk, _TD_QTR)
    m = _rolling_mean(vv63, _TD_YEAR)
    s = _rolling_std(vv63, _TD_YEAR)
    return _safe_div(vv63 - m, s.clip(lower=_EPS))


def vov_ext_030_gk_vol21_expanding_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series,
                                             open: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of 21-day Garman-Klass vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    return gk.expanding(min_periods=_TD_MON).rank(pct=True)


# --- Group C (031-045): Rogers-Satchell vol-of-vol ---

def vov_ext_031_std_rs_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                  open: pd.Series) -> pd.Series:
    """Std of 21-day Rogers-Satchell vol over trailing 63 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    return _rolling_std(rs, _TD_QTR)


def vov_ext_032_std_rs_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                   open: pd.Series) -> pd.Series:
    """Std of 21-day Rogers-Satchell vol over trailing 252 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    return _rolling_std(rs, _TD_YEAR)


def vov_ext_033_cv_rs_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                 open: pd.Series) -> pd.Series:
    """CV of 21-day Rogers-Satchell vol over trailing 63 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    return _safe_div(_rolling_std(rs, _TD_QTR), _rolling_mean(rs, _TD_QTR).clip(lower=_EPS))


def vov_ext_034_range_rs_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                    open: pd.Series) -> pd.Series:
    """Range of 21-day Rogers-Satchell vol over trailing 63 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    return _rolling_max(rs, _TD_QTR) - _rolling_min(rs, _TD_QTR)


def vov_ext_035_zscore_rs_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                      open: pd.Series) -> pd.Series:
    """Z-score of 21-day Rogers-Satchell vol within its 252-day distribution."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    m = _rolling_mean(rs, _TD_YEAR)
    s = _rolling_std(rs, _TD_YEAR)
    return _safe_div(rs - m, s.clip(lower=_EPS))


def vov_ext_036_pct_rank_rs_vol21_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                        open: pd.Series) -> pd.Series:
    """Percentile rank of 21-day Rogers-Satchell vol within trailing 252 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    return rs.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_037_mac_rs_vol21_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                  open: pd.Series) -> pd.Series:
    """Mean absolute daily change of 21-day Rogers-Satchell vol over 63 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    return rs.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()


def vov_ext_038_rs_vs_cc_spread_vov_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                         open: pd.Series) -> pd.Series:
    """Spread of Rogers-Satchell vov over close-to-close vov (both 63d std of 21d vol)."""
    rs_vov = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    cc_vov = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    return rs_vov - cc_vov


def vov_ext_039_rs_vov_above_cc_vov_flag(close: pd.Series, high: pd.Series, low: pd.Series,
                                          open: pd.Series) -> pd.Series:
    """Flag: 63-day Rogers-Satchell vov exceeds close-to-close vov."""
    rs_vov = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    cc_vov = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    return (rs_vov > cc_vov).astype(float)


def vov_ext_040_rs_vol5_std_21d(close: pd.Series, high: pd.Series, low: pd.Series,
                                 open: pd.Series) -> pd.Series:
    """Std of 5-day Rogers-Satchell vol over trailing 21 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_WEEK)
    return _rolling_std(rs, _TD_MON)


def vov_ext_041_rs_vol21_iqr_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                   open: pd.Series) -> pd.Series:
    """IQR (75th-25th) of 21-day Rogers-Satchell vol over trailing 252 days."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    q75 = rs.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = rs.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def vov_ext_042_rs_vov_zscore_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                    open: pd.Series) -> pd.Series:
    """Z-score of 63-day RS vov within its trailing 252-day distribution."""
    rs = _rogers_satchell_vol(close, high, low, open, _TD_MON)
    vv63 = _rolling_std(rs, _TD_QTR)
    m = _rolling_mean(vv63, _TD_YEAR)
    s = _rolling_std(vv63, _TD_YEAR)
    return _safe_div(vv63 - m, s.clip(lower=_EPS))


def vov_ext_043_cross_estimator_vov_composite(close: pd.Series, high: pd.Series, low: pd.Series,
                                               open: pd.Series) -> pd.Series:
    """Mean of CC vov, Parkinson vov, GK vov, and RS vov (all 63d std of 21d vol)."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    return (cc + pk + gk + rs) / 4.0


def vov_ext_044_max_cross_estimator_vov_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                             open: pd.Series) -> pd.Series:
    """Maximum of CC, Parkinson, GK, RS vov (63d std of 21d) — worst-case vov."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    return pd.concat([cc, pk, gk, rs], axis=1).max(axis=1)


def vov_ext_045_cross_estimator_vov_dispersion(close: pd.Series, high: pd.Series, low: pd.Series,
                                                open: pd.Series) -> pd.Series:
    """Std across CC/Parkinson/GK/RS vov estimates (dispersion of estimator estimates)."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    return pd.concat([cc, pk, gk, rs], axis=1).std(axis=1)


# --- Group D (046-060): Volume-weighted vol instability and tail-frequency ---

def vov_ext_046_vwap_vol21_std_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of 21-day realized vol of VWAP-proxy (volume-weighted close) over 63 days."""
    vwap = _safe_div(
        (close * volume).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum(),
        volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum().clip(lower=_EPS)
    )
    rv = _realized_vol(vwap, _TD_MON)
    return _rolling_std(rv, _TD_QTR)


def vov_ext_047_vwap_vol21_cv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV of 21-day VWAP-proxy realized vol over 63 days."""
    vwap = _safe_div(
        (close * volume).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum(),
        volume.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).sum().clip(lower=_EPS)
    )
    rv = _realized_vol(vwap, _TD_MON)
    return _safe_div(_rolling_std(rv, _TD_QTR), _rolling_mean(rv, _TD_QTR).clip(lower=_EPS))


def vov_ext_048_vol_tail_freq_above_2std_63d(close: pd.Series) -> pd.Series:
    """Frequency of days where 21d rvol exceeds mean+2*std (252d) over trailing 63d."""
    rv = _realized_vol(close, _TD_MON)
    m = _rolling_mean(rv, _TD_YEAR)
    s = _rolling_std(rv, _TD_YEAR)
    tail = (rv > m + 2.0 * s).astype(float)
    return _rolling_sum(tail, _TD_QTR)


def vov_ext_049_vol_tail_freq_above_2std_252d(close: pd.Series) -> pd.Series:
    """Frequency of days where 21d rvol exceeds mean+2*std over full 252-day window."""
    rv = _realized_vol(close, _TD_MON)
    m = rv.expanding(min_periods=_TD_QTR).mean()
    s = rv.expanding(min_periods=_TD_QTR).std()
    tail = (rv > m + 2.0 * s).astype(float)
    return _rolling_sum(tail, _TD_YEAR)


def vov_ext_050_vol_tail_freq_above_3std_252d(close: pd.Series) -> pd.Series:
    """Frequency of days where 21d rvol exceeds mean+3*std (expanding) over 252 days."""
    rv = _realized_vol(close, _TD_MON)
    m = rv.expanding(min_periods=_TD_QTR).mean()
    s = rv.expanding(min_periods=_TD_QTR).std()
    tail = (rv > m + 3.0 * s).astype(float)
    return _rolling_sum(tail, _TD_YEAR)


def vov_ext_051_vol_below_10th_pct_freq_63d(close: pd.Series) -> pd.Series:
    """Frequency of days where 21d rvol is below its 252-day 10th percentile over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    q10 = rv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    calm = (rv < q10).astype(float)
    return _rolling_sum(calm, _TD_QTR)


def vov_ext_052_vol_above_90th_pct_freq_63d(close: pd.Series) -> pd.Series:
    """Frequency of days where 21d rvol is above its 252-day 90th percentile over 63 days."""
    rv = _realized_vol(close, _TD_MON)
    q90 = rv.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    extreme = (rv > q90).astype(float)
    return _rolling_sum(extreme, _TD_QTR)


def vov_ext_053_vol_regime_switch_freq_63d(close: pd.Series) -> pd.Series:
    """Frequency of switches between high/low vol regimes (above/below median) over 63d."""
    rv = _realized_vol(close, _TD_MON)
    med = _rolling_median(rv, _TD_YEAR)
    high_regime = (rv > med).astype(int)
    switch = high_regime.diff(1).abs()
    return _rolling_sum(switch, _TD_QTR)


def vov_ext_054_vol_consec_high_regime_max_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive days where 21d rvol > 252d median, measured over trailing 63d."""
    rv = _realized_vol(close, _TD_MON)
    med = _rolling_median(rv, _TD_YEAR)
    cond = rv > med
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum().astype(float)
    return _rolling_max(streak, _TD_QTR)


def vov_ext_055_vol_frac_above_longrun_mean_63d(close: pd.Series) -> pd.Series:
    """Fraction of days in 63-day window where 21d rvol > its 252d rolling mean."""
    rv = _realized_vol(close, _TD_MON)
    avg = _rolling_mean(rv, _TD_YEAR)
    above = (rv > avg).astype(float)
    return _rolling_mean(above, _TD_QTR)


def vov_ext_056_vol_frac_above_longrun_mean_252d(close: pd.Series) -> pd.Series:
    """Fraction of days in 252-day window where 21d rvol > its expanding mean."""
    rv = _realized_vol(close, _TD_MON)
    avg = rv.expanding(min_periods=_TD_QTR).mean()
    above = (rv > avg).astype(float)
    return _rolling_mean(above, _TD_YEAR)


def vov_ext_057_intraday_vs_overnight_vov_ratio(close: pd.Series, high: pd.Series,
                                                  low: pd.Series) -> pd.Series:
    """Ratio of intraday HL-range vov to overnight gap vov over 63-day window.
    Intraday vov = std of (H-L)/prev_close; overnight vov = std of log(open/prev_close)
    approximated using log(close/prev_close) vs HL-range."""
    hl_pct = (high - low) / close.shift(1).clip(lower=_EPS)
    overnight = _log_ret(close).abs()
    std_hl = _rolling_std(hl_pct, _TD_QTR)
    std_ov = _rolling_std(overnight, _TD_QTR)
    return _safe_div(std_hl, std_ov.clip(lower=_EPS))


def vov_ext_058_hl_range_normalized_vov_63d(close: pd.Series, high: pd.Series,
                                             low: pd.Series) -> pd.Series:
    """Std of normalized HL range (HL/close) over trailing 63 days."""
    hl_norm = (high - low) / close.clip(lower=_EPS)
    return _rolling_std(hl_norm, _TD_QTR)


def vov_ext_059_hl_range_normalized_cv_252d(close: pd.Series, high: pd.Series,
                                             low: pd.Series) -> pd.Series:
    """CV of normalized HL range (HL/close) over trailing 252 days."""
    hl_norm = (high - low) / close.clip(lower=_EPS)
    return _safe_div(_rolling_std(hl_norm, _TD_YEAR), _rolling_mean(hl_norm, _TD_YEAR).clip(lower=_EPS))


def vov_ext_060_close_open_gap_vov_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Std of daily log(open/prev_close) gaps over trailing 63 days (overnight vov)."""
    gap = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    return _rolling_std(gap, _TD_QTR)


# --- Group E (061-075): Z-score ranks of extended vov measures, composites, entropy ---

def vov_ext_061_park_vov_pct_rank_expanding(high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63d Parkinson vov (all-history)."""
    pv = _parkinson_vol(high, low, _TD_MON)
    vv = _rolling_std(pv, _TD_QTR)
    return vv.expanding(min_periods=_TD_QTR).rank(pct=True)


def vov_ext_062_gk_vov_pct_rank_expanding(close: pd.Series, high: pd.Series, low: pd.Series,
                                           open: pd.Series) -> pd.Series:
    """Expanding percentile rank of 63d Garman-Klass vov (all-history)."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    vv = _rolling_std(gk, _TD_QTR)
    return vv.expanding(min_periods=_TD_QTR).rank(pct=True)


def vov_ext_063_park_vol21_zscore_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of current 21-day Parkinson vol within its trailing 63-day distribution."""
    pv = _parkinson_vol(high, low, _TD_MON)
    m = _rolling_mean(pv, _TD_QTR)
    s = _rolling_std(pv, _TD_QTR)
    return _safe_div(pv - m, s.clip(lower=_EPS))


def vov_ext_064_gk_vol21_zscore_63d(close: pd.Series, high: pd.Series, low: pd.Series,
                                     open: pd.Series) -> pd.Series:
    """Z-score of current 21-day GK vol within its trailing 63-day distribution."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    m = _rolling_mean(gk, _TD_QTR)
    s = _rolling_std(gk, _TD_QTR)
    return _safe_div(gk - m, s.clip(lower=_EPS))


def vov_ext_065_vol_entropy_proxy_63d(close: pd.Series) -> pd.Series:
    """Entropy proxy of 21d rvol: -sum(p*log(p)) using histogram of 63-day window.
    Implemented as normalized Shannon entropy of 10-bin rolling quantile histogram."""
    rv = _realized_vol(close, _TD_MON)
    n_bins = 10
    def _entropy(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        mn, mx = x.min(), x.max()
        if mx - mn < _EPS:
            return 0.0
        bins = np.linspace(mn, mx, n_bins + 1)
        counts, _ = np.histogram(x, bins=bins)
        probs = counts / counts.sum()
        probs = probs[probs > 0]
        return -np.sum(probs * np.log(probs))
    return rv.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(_entropy, raw=True)


def vov_ext_066_vol_entropy_proxy_252d(close: pd.Series) -> pd.Series:
    """Entropy proxy of 21d rvol over 252-day window (long-run vol distribution entropy)."""
    rv = _realized_vol(close, _TD_MON)
    n_bins = 10
    def _entropy(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        mn, mx = x.min(), x.max()
        if mx - mn < _EPS:
            return 0.0
        bins = np.linspace(mn, mx, n_bins + 1)
        counts, _ = np.histogram(x, bins=bins)
        probs = counts / counts.sum()
        probs = probs[probs > 0]
        return -np.sum(probs * np.log(probs))
    return rv.rolling(_TD_YEAR, min_periods=max(5, _TD_YEAR // 2)).apply(_entropy, raw=True)


def vov_ext_067_vol_entropy_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d vol entropy within trailing 252 days."""
    rv = _realized_vol(close, _TD_MON)
    n_bins = 10
    def _entropy(x):
        x = x[~np.isnan(x)]
        if len(x) < 5:
            return np.nan
        mn, mx = x.min(), x.max()
        if mx - mn < _EPS:
            return 0.0
        bins = np.linspace(mn, mx, n_bins + 1)
        counts, _ = np.histogram(x, bins=bins)
        probs = counts / counts.sum()
        probs = probs[probs > 0]
        return -np.sum(probs * np.log(probs))
    ent = rv.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).apply(_entropy, raw=True)
    return ent.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_068_rvol21_trend_instability_63d(close: pd.Series) -> pd.Series:
    """Residual std of OLS fit to 21d rvol over 63-day window (trend deviations)."""
    rv = _realized_vol(close, _TD_MON)
    def _resid_std(x):
        if len(x) < max(3, len(x) // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den < _EPS:
            return np.nan
        slope = ((xi - xi_m) * (x - x_m)).sum() / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        return resid.std()
    return rv.rolling(_TD_QTR, min_periods=max(3, _TD_QTR // 2)).apply(_resid_std, raw=True)


def vov_ext_069_rvol21_trend_instability_252d(close: pd.Series) -> pd.Series:
    """Residual std of OLS fit to 21d rvol over 252-day window."""
    rv = _realized_vol(close, _TD_MON)
    def _resid_std(x):
        if len(x) < max(3, len(x) // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        den = ((xi - xi_m) ** 2).sum()
        if den < _EPS:
            return np.nan
        slope = ((xi - xi_m) * (x - x_m)).sum() / den
        intercept = x_m - slope * xi_m
        resid = x - (slope * xi + intercept)
        return resid.std()
    return rv.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 2)).apply(_resid_std, raw=True)


def vov_ext_070_park_gk_rs_vov_max_pct_rank_252d(close: pd.Series, high: pd.Series,
                                                   low: pd.Series, open: pd.Series) -> pd.Series:
    """Pct rank (252d) of composite max(Parkinson, GK, RS) vov over 63d."""
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    gk = _rolling_std(_garman_klass_vol(close, high, low, open, _TD_MON), _TD_QTR)
    rs = _rolling_std(_rogers_satchell_vol(close, high, low, open, _TD_MON), _TD_QTR)
    mx = pd.concat([pk, gk, rs], axis=1).max(axis=1)
    return mx.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_071_cc_vov_minus_park_vov_zscore(close: pd.Series, high: pd.Series,
                                              low: pd.Series) -> pd.Series:
    """Z-score of (CC vov - Parkinson vov) spread over 252-day distribution."""
    cc = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    diff = cc - pk
    m = _rolling_mean(diff, _TD_YEAR)
    s = _rolling_std(diff, _TD_YEAR)
    return _safe_div(diff - m, s.clip(lower=_EPS))


def vov_ext_072_gk_vol21_mac_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series,
                                            open: pd.Series) -> pd.Series:
    """Percentile rank (252d) of 63d MAC of 21-day GK vol."""
    gk = _garman_klass_vol(close, high, low, open, _TD_MON)
    mac = gk.diff(1).abs().rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).mean()
    return mac.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_073_close_open_gap_vov_pct_rank_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Percentile rank (252d) of 63d overnight-gap vov."""
    gap = np.log(open.clip(lower=_EPS) / close.shift(1).clip(lower=_EPS))
    gvov = _rolling_std(gap, _TD_QTR)
    return gvov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vov_ext_074_vol_stability_score_composite(close: pd.Series, high: pd.Series,
                                               low: pd.Series) -> pd.Series:
    """Inverse vol-stability composite: mean of (1 - pct_rank) for CC vov, Parkinson vov,
    and IQR-based vov. Higher score = more unstable (capitulation-aligned)."""
    cc_vov = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    pk_vov = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    rv = _realized_vol(close, _TD_MON)
    iqr_vov = (rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.75) -
               rv.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).quantile(0.25))
    cc_rank = cc_vov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    pk_rank = pk_vov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    iqr_rank = iqr_vov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (cc_rank + pk_rank + iqr_rank) / 3.0


def vov_ext_075_vol_distress_composite(close: pd.Series, high: pd.Series,
                                        low: pd.Series) -> pd.Series:
    """Capitulation distress composite: CC vov zscore + Parkinson vov zscore + tail freq.
    Standardized sum — higher = more distressed vol environment."""
    rv = _realized_vol(close, _TD_MON)
    cc_vov = _rolling_std(rv, _TD_QTR)
    pk_vov = _rolling_std(_parkinson_vol(high, low, _TD_MON), _TD_QTR)
    m_cc = _rolling_mean(cc_vov, _TD_YEAR)
    s_cc = _rolling_std(cc_vov, _TD_YEAR)
    z_cc = _safe_div(cc_vov - m_cc, s_cc.clip(lower=_EPS))
    m_pk = _rolling_mean(pk_vov, _TD_YEAR)
    s_pk = _rolling_std(pk_vov, _TD_YEAR)
    z_pk = _safe_div(pk_vov - m_pk, s_pk.clip(lower=_EPS))
    m_rv = _rolling_mean(rv, _TD_YEAR)
    s_rv = _rolling_std(rv, _TD_YEAR)
    tail_flag = (rv > m_rv + 2.0 * s_rv).astype(float)
    tail_freq = _rolling_mean(tail_flag, _TD_QTR)
    return z_cc + z_pk + tail_freq


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_OF_VOLATILITY_EXTENDED_REGISTRY_001_075 = {
    "vov_ext_001_std_park_vol21_63d": {"inputs": ["high", "low"], "func": vov_ext_001_std_park_vol21_63d},
    "vov_ext_002_std_park_vol21_252d": {"inputs": ["high", "low"], "func": vov_ext_002_std_park_vol21_252d},
    "vov_ext_003_cv_park_vol21_63d": {"inputs": ["high", "low"], "func": vov_ext_003_cv_park_vol21_63d},
    "vov_ext_004_cv_park_vol21_252d": {"inputs": ["high", "low"], "func": vov_ext_004_cv_park_vol21_252d},
    "vov_ext_005_range_park_vol21_63d": {"inputs": ["high", "low"], "func": vov_ext_005_range_park_vol21_63d},
    "vov_ext_006_range_park_vol21_252d": {"inputs": ["high", "low"], "func": vov_ext_006_range_park_vol21_252d},
    "vov_ext_007_mac_park_vol21_63d": {"inputs": ["high", "low"], "func": vov_ext_007_mac_park_vol21_63d},
    "vov_ext_008_zscore_park_vol21_252d": {"inputs": ["high", "low"], "func": vov_ext_008_zscore_park_vol21_252d},
    "vov_ext_009_pct_rank_park_vol21_252d": {"inputs": ["high", "low"], "func": vov_ext_009_pct_rank_park_vol21_252d},
    "vov_ext_010_std_park_vol5_63d": {"inputs": ["high", "low"], "func": vov_ext_010_std_park_vol5_63d},
    "vov_ext_011_cv_park_vol5_63d": {"inputs": ["high", "low"], "func": vov_ext_011_cv_park_vol5_63d},
    "vov_ext_012_park_vs_cc_vov_ratio_63d": {"inputs": ["close", "high", "low"], "func": vov_ext_012_park_vs_cc_vov_ratio_63d},
    "vov_ext_013_park_vov_above_cc_vov_flag": {"inputs": ["close", "high", "low"], "func": vov_ext_013_park_vov_above_cc_vov_flag},
    "vov_ext_014_park_vol21_iqr_63d": {"inputs": ["high", "low"], "func": vov_ext_014_park_vol21_iqr_63d},
    "vov_ext_015_park_vol21_reversal_freq_63d": {"inputs": ["high", "low"], "func": vov_ext_015_park_vol21_reversal_freq_63d},
    "vov_ext_016_std_gk_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_016_std_gk_vol21_63d},
    "vov_ext_017_std_gk_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_017_std_gk_vol21_252d},
    "vov_ext_018_cv_gk_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_018_cv_gk_vol21_63d},
    "vov_ext_019_cv_gk_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_019_cv_gk_vol21_252d},
    "vov_ext_020_range_gk_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_020_range_gk_vol21_63d},
    "vov_ext_021_mac_gk_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_021_mac_gk_vol21_63d},
    "vov_ext_022_zscore_gk_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_022_zscore_gk_vol21_252d},
    "vov_ext_023_pct_rank_gk_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_023_pct_rank_gk_vol21_252d},
    "vov_ext_024_gk_vs_park_vov_spread_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_024_gk_vs_park_vov_spread_63d},
    "vov_ext_025_gk_vol5_std_21d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_025_gk_vol5_std_21d},
    "vov_ext_026_gk_vol21_iqr_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_026_gk_vol21_iqr_63d},
    "vov_ext_027_gk_vol21_reversal_freq_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_027_gk_vol21_reversal_freq_63d},
    "vov_ext_028_gk_vov_above_longrun_flag": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_028_gk_vov_above_longrun_flag},
    "vov_ext_029_gk_vov_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_029_gk_vov_zscore_252d},
    "vov_ext_030_gk_vol21_expanding_pct_rank": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_030_gk_vol21_expanding_pct_rank},
    "vov_ext_031_std_rs_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_031_std_rs_vol21_63d},
    "vov_ext_032_std_rs_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_032_std_rs_vol21_252d},
    "vov_ext_033_cv_rs_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_033_cv_rs_vol21_63d},
    "vov_ext_034_range_rs_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_034_range_rs_vol21_63d},
    "vov_ext_035_zscore_rs_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_035_zscore_rs_vol21_252d},
    "vov_ext_036_pct_rank_rs_vol21_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_036_pct_rank_rs_vol21_252d},
    "vov_ext_037_mac_rs_vol21_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_037_mac_rs_vol21_63d},
    "vov_ext_038_rs_vs_cc_spread_vov_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_038_rs_vs_cc_spread_vov_63d},
    "vov_ext_039_rs_vov_above_cc_vov_flag": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_039_rs_vov_above_cc_vov_flag},
    "vov_ext_040_rs_vol5_std_21d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_040_rs_vol5_std_21d},
    "vov_ext_041_rs_vol21_iqr_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_041_rs_vol21_iqr_252d},
    "vov_ext_042_rs_vov_zscore_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_042_rs_vov_zscore_252d},
    "vov_ext_043_cross_estimator_vov_composite": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_043_cross_estimator_vov_composite},
    "vov_ext_044_max_cross_estimator_vov_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_044_max_cross_estimator_vov_63d},
    "vov_ext_045_cross_estimator_vov_dispersion": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_045_cross_estimator_vov_dispersion},
    "vov_ext_046_vwap_vol21_std_63d": {"inputs": ["close", "volume"], "func": vov_ext_046_vwap_vol21_std_63d},
    "vov_ext_047_vwap_vol21_cv_63d": {"inputs": ["close", "volume"], "func": vov_ext_047_vwap_vol21_cv_63d},
    "vov_ext_048_vol_tail_freq_above_2std_63d": {"inputs": ["close"], "func": vov_ext_048_vol_tail_freq_above_2std_63d},
    "vov_ext_049_vol_tail_freq_above_2std_252d": {"inputs": ["close"], "func": vov_ext_049_vol_tail_freq_above_2std_252d},
    "vov_ext_050_vol_tail_freq_above_3std_252d": {"inputs": ["close"], "func": vov_ext_050_vol_tail_freq_above_3std_252d},
    "vov_ext_051_vol_below_10th_pct_freq_63d": {"inputs": ["close"], "func": vov_ext_051_vol_below_10th_pct_freq_63d},
    "vov_ext_052_vol_above_90th_pct_freq_63d": {"inputs": ["close"], "func": vov_ext_052_vol_above_90th_pct_freq_63d},
    "vov_ext_053_vol_regime_switch_freq_63d": {"inputs": ["close"], "func": vov_ext_053_vol_regime_switch_freq_63d},
    "vov_ext_054_vol_consec_high_regime_max_63d": {"inputs": ["close"], "func": vov_ext_054_vol_consec_high_regime_max_63d},
    "vov_ext_055_vol_frac_above_longrun_mean_63d": {"inputs": ["close"], "func": vov_ext_055_vol_frac_above_longrun_mean_63d},
    "vov_ext_056_vol_frac_above_longrun_mean_252d": {"inputs": ["close"], "func": vov_ext_056_vol_frac_above_longrun_mean_252d},
    "vov_ext_057_intraday_vs_overnight_vov_ratio": {"inputs": ["close", "high", "low"], "func": vov_ext_057_intraday_vs_overnight_vov_ratio},
    "vov_ext_058_hl_range_normalized_vov_63d": {"inputs": ["close", "high", "low"], "func": vov_ext_058_hl_range_normalized_vov_63d},
    "vov_ext_059_hl_range_normalized_cv_252d": {"inputs": ["close", "high", "low"], "func": vov_ext_059_hl_range_normalized_cv_252d},
    "vov_ext_060_close_open_gap_vov_63d": {"inputs": ["close", "open"], "func": vov_ext_060_close_open_gap_vov_63d},
    "vov_ext_061_park_vov_pct_rank_expanding": {"inputs": ["high", "low"], "func": vov_ext_061_park_vov_pct_rank_expanding},
    "vov_ext_062_gk_vov_pct_rank_expanding": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_062_gk_vov_pct_rank_expanding},
    "vov_ext_063_park_vol21_zscore_63d": {"inputs": ["high", "low"], "func": vov_ext_063_park_vol21_zscore_63d},
    "vov_ext_064_gk_vol21_zscore_63d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_064_gk_vol21_zscore_63d},
    "vov_ext_065_vol_entropy_proxy_63d": {"inputs": ["close"], "func": vov_ext_065_vol_entropy_proxy_63d},
    "vov_ext_066_vol_entropy_proxy_252d": {"inputs": ["close"], "func": vov_ext_066_vol_entropy_proxy_252d},
    "vov_ext_067_vol_entropy_pct_rank_252d": {"inputs": ["close"], "func": vov_ext_067_vol_entropy_pct_rank_252d},
    "vov_ext_068_rvol21_trend_instability_63d": {"inputs": ["close"], "func": vov_ext_068_rvol21_trend_instability_63d},
    "vov_ext_069_rvol21_trend_instability_252d": {"inputs": ["close"], "func": vov_ext_069_rvol21_trend_instability_252d},
    "vov_ext_070_park_gk_rs_vov_max_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_070_park_gk_rs_vov_max_pct_rank_252d},
    "vov_ext_071_cc_vov_minus_park_vov_zscore": {"inputs": ["close", "high", "low"], "func": vov_ext_071_cc_vov_minus_park_vov_zscore},
    "vov_ext_072_gk_vol21_mac_pct_rank_252d": {"inputs": ["close", "high", "low", "open"], "func": vov_ext_072_gk_vol21_mac_pct_rank_252d},
    "vov_ext_073_close_open_gap_vov_pct_rank_252d": {"inputs": ["close", "open"], "func": vov_ext_073_close_open_gap_vov_pct_rank_252d},
    "vov_ext_074_vol_stability_score_composite": {"inputs": ["close", "high", "low"], "func": vov_ext_074_vol_stability_score_composite},
    "vov_ext_075_vol_distress_composite": {"inputs": ["close", "high", "low"], "func": vov_ext_075_vol_distress_composite},
}
