"""
115_volatility_term_structure — Base Features 076-150
Domain: term structure of realized volatility — rolling vol-ratio momentum, EWM-based
        term structure, vol-of-vol across horizons, inversion counts in windows,
        normalized spreads, Parkinson/Garman-Klass/Yang-Zhang multi-horizon term structure,
        high-low range-based vol term structure, open-close vol term structure.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _realized_vol(close: pd.Series, w: int) -> pd.Series:
    """Annualized realized volatility (std of log-returns) over w days."""
    lr = np.log(close / close.shift(1))
    rv = lr.rolling(w, min_periods=max(2, w // 2)).std()
    return rv * np.sqrt(_TD_YEAR)


def _parkinson_vol(high: pd.Series, low: pd.Series, w: int) -> pd.Series:
    """Parkinson high-low range estimator, annualized, over w days."""
    hl2 = np.log(high / low.clip(lower=_EPS)) ** 2
    pk = np.sqrt(hl2.rolling(w, min_periods=max(2, w // 2)).mean() / (4.0 * np.log(2.0)))
    return pk * np.sqrt(_TD_YEAR)


def _garman_klass_vol(open_: pd.Series, high: pd.Series,
                      low: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Garman-Klass OHLC estimator, annualized."""
    hl2 = 0.5 * np.log(high / low.clip(lower=_EPS)) ** 2
    co2 = (2.0 * np.log(2.0) - 1.0) * np.log(close / open_.clip(lower=_EPS)) ** 2
    gk = np.sqrt((hl2 - co2).rolling(w, min_periods=max(2, w // 2)).mean())
    return gk * np.sqrt(_TD_YEAR)


def _oc_vol(open_: pd.Series, close: pd.Series, w: int) -> pd.Series:
    """Open-to-close log-return volatility, annualized."""
    oc = np.log(close / open_.clip(lower=_EPS))
    return oc.rolling(w, min_periods=max(2, w // 2)).std() * np.sqrt(_TD_YEAR)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): EWM-based vol term structure ---

def vts_076_ewm_rv5_span5(close: pd.Series) -> pd.Series:
    """EWM (span=5) of daily squared log-returns, annualized (ultra-short EWM vol)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    return np.sqrt(_ewm_mean(lr2, _TD_WEEK)) * np.sqrt(_TD_YEAR)


def vts_077_ewm_rv5_span21(close: pd.Series) -> pd.Series:
    """EWM (span=21) of daily squared log-returns, annualized (monthly EWM vol)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    return np.sqrt(_ewm_mean(lr2, _TD_MON)) * np.sqrt(_TD_YEAR)


def vts_078_ewm_rv5_span63(close: pd.Series) -> pd.Series:
    """EWM (span=63) of daily squared log-returns, annualized (quarterly EWM vol)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    return np.sqrt(_ewm_mean(lr2, _TD_QTR)) * np.sqrt(_TD_YEAR)


def vts_079_ewm_rv5_span252(close: pd.Series) -> pd.Series:
    """EWM (span=252) of daily squared log-returns, annualized (annual EWM vol)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    return np.sqrt(_ewm_mean(lr2, _TD_YEAR)) * np.sqrt(_TD_YEAR)


def vts_080_ewm_vol_span5_span21_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-vol(span=5) to EWM-vol(span=21) — EWM term structure short/mid."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK)) + _EPS
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON)) + _EPS
    return s5 / s21


def vts_081_ewm_vol_span5_span63_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-vol(span=5) to EWM-vol(span=63)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK)) + _EPS
    s63 = np.sqrt(_ewm_mean(lr2, _TD_QTR)) + _EPS
    return s5 / s63


def vts_082_ewm_vol_span21_span63_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-vol(span=21) to EWM-vol(span=63) — EWM monthly/quarterly."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON)) + _EPS
    s63 = np.sqrt(_ewm_mean(lr2, _TD_QTR)) + _EPS
    return s21 / s63


def vts_083_ewm_vol_span63_span252_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-vol(span=63) to EWM-vol(span=252)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s63 = np.sqrt(_ewm_mean(lr2, _TD_QTR)) + _EPS
    s252 = np.sqrt(_ewm_mean(lr2, _TD_YEAR)) + _EPS
    return s63 / s252


def vts_084_ewm_vol_span5_span252_ratio(close: pd.Series) -> pd.Series:
    """Ratio of EWM-vol(span=5) to EWM-vol(span=252) — widest EWM term spread."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK)) + _EPS
    s252 = np.sqrt(_ewm_mean(lr2, _TD_YEAR)) + _EPS
    return s5 / s252


def vts_085_ewm_vol_inversion_5_21_flag(close: pd.Series) -> pd.Series:
    """Binary flag: EWM-vol(span=5) > EWM-vol(span=21)."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK))
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON))
    return (s5 > s21).astype(float)


def vts_086_ewm_vol_spread_5_21(close: pd.Series) -> pd.Series:
    """EWM-vol(span=5) minus EWM-vol(span=21), annualized."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK)) * np.sqrt(_TD_YEAR)
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON)) * np.sqrt(_TD_YEAR)
    return s5 - s21


def vts_087_ewm_vol_spread_5_63(close: pd.Series) -> pd.Series:
    """EWM-vol(span=5) minus EWM-vol(span=63), annualized."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK)) * np.sqrt(_TD_YEAR)
    s63 = np.sqrt(_ewm_mean(lr2, _TD_QTR)) * np.sqrt(_TD_YEAR)
    return s5 - s63


def vts_088_ewm_vol_spread_21_252(close: pd.Series) -> pd.Series:
    """EWM-vol(span=21) minus EWM-vol(span=252), annualized."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON)) * np.sqrt(_TD_YEAR)
    s252 = np.sqrt(_ewm_mean(lr2, _TD_YEAR)) * np.sqrt(_TD_YEAR)
    return s21 - s252


def vts_089_ewm_vol_span21_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of EWM-vol(span=21) over 252 trading days."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s21 = np.sqrt(_ewm_mean(lr2, _TD_MON))
    return s21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_090_ewm_vol_span5_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of EWM-vol(span=5) vs its 252-day distribution."""
    lr2 = np.log(close / close.shift(1)) ** 2
    s5 = np.sqrt(_ewm_mean(lr2, _TD_WEEK))
    return _safe_div(s5 - _rolling_mean(s5, _TD_YEAR), _rolling_std(s5, _TD_YEAR))


# --- Group I (091-105): Parkinson and Garman-Klass multi-horizon term structure ---

def vts_091_pk_rv5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 5-day realized vol, annualized."""
    return _parkinson_vol(high, low, _TD_WEEK)


def vts_092_pk_rv21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 21-day realized vol, annualized."""
    return _parkinson_vol(high, low, _TD_MON)


def vts_093_pk_rv63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 63-day realized vol, annualized."""
    return _parkinson_vol(high, low, _TD_QTR)


def vts_094_pk_rv252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 252-day realized vol, annualized."""
    return _parkinson_vol(high, low, _TD_YEAR)


def vts_095_pk_rv5d_rv21d_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of Parkinson 5d to 21d vol (HL-based term structure short/mid)."""
    return _safe_div(_parkinson_vol(high, low, _TD_WEEK),
                     _parkinson_vol(high, low, _TD_MON))


def vts_096_pk_rv21d_rv63d_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of Parkinson 21d to 63d vol."""
    return _safe_div(_parkinson_vol(high, low, _TD_MON),
                     _parkinson_vol(high, low, _TD_QTR))


def vts_097_pk_rv63d_rv252d_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of Parkinson 63d to 252d vol."""
    return _safe_div(_parkinson_vol(high, low, _TD_QTR),
                     _parkinson_vol(high, low, _TD_YEAR))


def vts_098_pk_ts_inversion_5d21d_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: Parkinson 5d vol > 21d vol (HL-based inversion)."""
    return (_parkinson_vol(high, low, _TD_WEEK)
            > _parkinson_vol(high, low, _TD_MON)).astype(float)


def vts_099_pk_ts_inversion_full_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary flag: Parkinson full term-structure inversion (5d>21d>63d>252d)."""
    p5 = _parkinson_vol(high, low, _TD_WEEK)
    p21 = _parkinson_vol(high, low, _TD_MON)
    p63 = _parkinson_vol(high, low, _TD_QTR)
    p252 = _parkinson_vol(high, low, _TD_YEAR)
    return ((p5 > p21) & (p21 > p63) & (p63 > p252)).astype(float)


def vts_100_gk_rv5d(open_: pd.Series, high: pd.Series,
                    low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass 5-day realized vol, annualized."""
    return _garman_klass_vol(open_, high, low, close, _TD_WEEK)


def vts_101_gk_rv21d(open_: pd.Series, high: pd.Series,
                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass 21-day realized vol, annualized."""
    return _garman_klass_vol(open_, high, low, close, _TD_MON)


def vts_102_gk_rv63d(open_: pd.Series, high: pd.Series,
                     low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass 63-day realized vol, annualized."""
    return _garman_klass_vol(open_, high, low, close, _TD_QTR)


def vts_103_gk_rv252d(open_: pd.Series, high: pd.Series,
                      low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass 252-day realized vol, annualized."""
    return _garman_klass_vol(open_, high, low, close, _TD_YEAR)


def vts_104_gk_rv5d_rv21d_ratio(open_: pd.Series, high: pd.Series,
                                 low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of GK 5d to GK 21d vol (OHLC-based term structure)."""
    return _safe_div(_garman_klass_vol(open_, high, low, close, _TD_WEEK),
                     _garman_klass_vol(open_, high, low, close, _TD_MON))


def vts_105_gk_rv21d_rv63d_ratio(open_: pd.Series, high: pd.Series,
                                  low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of GK 21d to GK 63d vol."""
    return _safe_div(_garman_klass_vol(open_, high, low, close, _TD_MON),
                     _garman_klass_vol(open_, high, low, close, _TD_QTR))


# --- Group J (106-120): Open-close vol term structure & rolling inversion counts ---

def vts_106_oc_rv5d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Open-to-close 5-day vol, annualized."""
    return _oc_vol(open_, close, _TD_WEEK)


def vts_107_oc_rv21d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Open-to-close 21-day vol, annualized."""
    return _oc_vol(open_, close, _TD_MON)


def vts_108_oc_rv63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Open-to-close 63-day vol, annualized."""
    return _oc_vol(open_, close, _TD_QTR)


def vts_109_oc_rv252d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Open-to-close 252-day vol, annualized."""
    return _oc_vol(open_, close, _TD_YEAR)


def vts_110_oc_rv5d_rv21d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of OC 5d to OC 21d vol (open-close term structure short/mid)."""
    return _safe_div(_oc_vol(open_, close, _TD_WEEK),
                     _oc_vol(open_, close, _TD_MON))


def vts_111_oc_rv21d_rv63d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of OC 21d to OC 63d vol."""
    return _safe_div(_oc_vol(open_, close, _TD_MON),
                     _oc_vol(open_, close, _TD_QTR))


def vts_112_oc_rv5d_rv63d_ratio(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of OC 5d to OC 63d vol (wide open-close term spread)."""
    return _safe_div(_oc_vol(open_, close, _TD_WEEK),
                     _oc_vol(open_, close, _TD_QTR))


def vts_113_days_5d21d_inverted_in_63d(close: pd.Series) -> pd.Series:
    """Count of days 5d>21d RV inversion occurred in trailing 63 days."""
    inv = (_realized_vol(close, _TD_WEEK) > _realized_vol(close, _TD_MON)).astype(float)
    return _rolling_sum(inv, _TD_QTR)


def vts_114_days_21d63d_inverted_in_252d(close: pd.Series) -> pd.Series:
    """Count of days 21d>63d RV inversion in trailing 252 days."""
    inv = (_realized_vol(close, _TD_MON) > _realized_vol(close, _TD_QTR)).astype(float)
    return _rolling_sum(inv, _TD_YEAR)


def vts_115_days_full_inverted_in_252d(close: pd.Series) -> pd.Series:
    """Count of days full term-structure inversion in trailing 252 days."""
    r5 = _realized_vol(close, _TD_WEEK)
    r21 = _realized_vol(close, _TD_MON)
    r63 = _realized_vol(close, _TD_QTR)
    r252 = _realized_vol(close, _TD_YEAR)
    inv = ((r5 > r21) & (r21 > r63) & (r63 > r252)).astype(float)
    return _rolling_sum(inv, _TD_YEAR)


def vts_116_fraction_5d21d_inverted_252d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where 5d RV > 21d RV."""
    inv = (_realized_vol(close, _TD_WEEK) > _realized_vol(close, _TD_MON)).astype(float)
    return _rolling_sum(inv, _TD_YEAR) / _TD_YEAR


def vts_117_fraction_21d63d_inverted_63d(close: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where 21d RV > 63d RV."""
    inv = (_realized_vol(close, _TD_MON) > _realized_vol(close, _TD_QTR)).astype(float)
    return _rolling_sum(inv, _TD_QTR) / _TD_QTR


def vts_118_rv5d_rv21d_ratio_rolling_mean_21d(close: pd.Series) -> pd.Series:
    """21-day rolling mean of the 5d/21d vol ratio (smoothed term structure tilt)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return _rolling_mean(ratio, _TD_MON)


def vts_119_rv21d_rv63d_ratio_rolling_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of the 21d/63d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_MON), _realized_vol(close, _TD_QTR))
    return _rolling_mean(ratio, _TD_QTR)


def vts_120_rv5d_rv252d_ratio_rolling_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of the 5d/252d vol ratio (sustained inversion context)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_YEAR))
    return _rolling_mean(ratio, _TD_QTR)


# --- Group K (121-135): Vol-of-vol across horizons ---

def vts_121_vov_rv5d_21d(close: pd.Series) -> pd.Series:
    """Vol-of-vol: 21-day std of daily 5d RV (short-horizon vol variability)."""
    return _rolling_std(_realized_vol(close, _TD_WEEK), _TD_MON)


def vts_122_vov_rv21d_63d(close: pd.Series) -> pd.Series:
    """Vol-of-vol: 63-day std of daily 21d RV."""
    return _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)


def vts_123_vov_rv63d_252d(close: pd.Series) -> pd.Series:
    """Vol-of-vol: 252-day std of daily 63d RV."""
    return _rolling_std(_realized_vol(close, _TD_QTR), _TD_YEAR)


def vts_124_vov_rv5d_63d(close: pd.Series) -> pd.Series:
    """Vol-of-vol: 63-day std of daily 5d RV."""
    return _rolling_std(_realized_vol(close, _TD_WEEK), _TD_QTR)


def vts_125_vov_rv252d_expanding(close: pd.Series) -> pd.Series:
    """Expanding std of 252d RV (all-time volatility of long-horizon vol)."""
    return _realized_vol(close, _TD_YEAR).expanding(min_periods=_TD_YEAR).std()


def vts_126_vov_ratio_rv5d_rv21d_21d(close: pd.Series) -> pd.Series:
    """21-day std of the 5d/21d vol ratio (instability of short-end term structure)."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return _rolling_std(ratio, _TD_MON)


def vts_127_vov_ratio_rv5d_rv21d_63d(close: pd.Series) -> pd.Series:
    """63-day std of the 5d/21d vol ratio."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return _rolling_std(ratio, _TD_QTR)


def vts_128_rv5d_vov_zscore(close: pd.Series) -> pd.Series:
    """Z-score of vov(rv5d,21d) vs its 252-day distribution."""
    vov = _rolling_std(_realized_vol(close, _TD_WEEK), _TD_MON)
    return _safe_div(vov - _rolling_mean(vov, _TD_YEAR), _rolling_std(vov, _TD_YEAR))


def vts_129_vov_spread_rv5d_rv252d(close: pd.Series) -> pd.Series:
    """Difference: vov(rv5d,21d) minus vov(rv252d,252d) — cross-horizon vol stability."""
    vov_short = _rolling_std(_realized_vol(close, _TD_WEEK), _TD_MON)
    vov_long = _rolling_std(_realized_vol(close, _TD_YEAR), _TD_YEAR)
    return vov_short - vov_long


def vts_130_vov_rv21d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of vov(rv21d,63d) within 252-day distribution."""
    vov = _rolling_std(_realized_vol(close, _TD_MON), _TD_QTR)
    return vov.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group L (131-150): Normalized spreads, vol term slope rolling stats ---

def vts_131_rv5d_rv21d_spread_norm(close: pd.Series) -> pd.Series:
    """(5d RV - 21d RV) normalized by 252d RV (scale-invariant short spread)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return (rv5 - rv21) / rv252


def vts_132_rv21d_rv63d_spread_norm(close: pd.Series) -> pd.Series:
    """(21d RV - 63d RV) normalized by 252d RV."""
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return (rv21 - rv63) / rv252


def vts_133_rv63d_rv252d_spread_norm(close: pd.Series) -> pd.Series:
    """(63d RV - 252d RV) normalized by 252d RV."""
    rv63 = _realized_vol(close, _TD_QTR)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return (rv63 - rv252) / rv252


def vts_134_rv5d_rv252d_spread_norm(close: pd.Series) -> pd.Series:
    """(5d RV - 252d RV) normalized by 252d RV (widest spread, standardized)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    return (rv5 - rv252) / rv252


def vts_135_rv5d_rv21d_spread_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (5d-21d) spread vs its own 252-day distribution."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    return _safe_div(spread - _rolling_mean(spread, _TD_YEAR),
                     _rolling_std(spread, _TD_YEAR))


def vts_136_rv21d_rv63d_spread_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of (21d-63d) spread vs its 252-day distribution."""
    spread = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)
    return _safe_div(spread - _rolling_mean(spread, _TD_YEAR),
                     _rolling_std(spread, _TD_YEAR))


def vts_137_vol_curve_slope_rolling_mean_63d(close: pd.Series) -> pd.Series:
    """63-day rolling mean of log-linear vol curve slope (5d to 252d)."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    return _rolling_mean(slope, _TD_QTR)


def vts_138_vol_curve_slope_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of log-linear vol curve slope vs its 252-day distribution."""
    rv5 = _realized_vol(close, _TD_WEEK).clip(lower=_EPS)
    rv252 = _realized_vol(close, _TD_YEAR).clip(lower=_EPS)
    slope = np.log(rv252 / rv5) / np.log(_TD_YEAR / _TD_WEEK)
    return _safe_div(slope - _rolling_mean(slope, _TD_YEAR),
                     _rolling_std(slope, _TD_YEAR))


def vts_139_rv5d_rv21d_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 5d/21d vol ratio vs its 252-day distribution."""
    ratio = _safe_div(_realized_vol(close, _TD_WEEK), _realized_vol(close, _TD_MON))
    return _safe_div(ratio - _rolling_mean(ratio, _TD_YEAR),
                     _rolling_std(ratio, _TD_YEAR))


def vts_140_rv63d_rv252d_ratio_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d/252d vol ratio vs its 252-day distribution."""
    ratio = _safe_div(_realized_vol(close, _TD_QTR), _realized_vol(close, _TD_YEAR))
    return _safe_div(ratio - _rolling_mean(ratio, _TD_YEAR),
                     _rolling_std(ratio, _TD_YEAR))


def vts_141_rv5d_rv21d_spread_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of (5d-21d) RV spread within 252-day history."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_MON)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_142_rv21d_rv63d_spread_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of (21d-63d) RV spread within 252-day history."""
    spread = _realized_vol(close, _TD_MON) - _realized_vol(close, _TD_QTR)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_143_rv5d_rv252d_spread_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of (5d-252d) RV spread (widest spread) within 252-day history."""
    spread = _realized_vol(close, _TD_WEEK) - _realized_vol(close, _TD_YEAR)
    return spread.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def vts_144_rv5d_expanding_max_ratio(close: pd.Series) -> pd.Series:
    """5d RV as fraction of its all-time expanding maximum (extreme spike indicator)."""
    rv = _realized_vol(close, _TD_WEEK)
    exp_max = rv.expanding(min_periods=_TD_WEEK).max().clip(lower=_EPS)
    return rv / exp_max


def vts_145_rv252d_relative_to_5yr_mean(close: pd.Series) -> pd.Series:
    """252d RV divided by its 5-year (1260-day) rolling mean."""
    rv = _realized_vol(close, _TD_YEAR)
    mean_5y = _rolling_mean(rv, 5 * _TD_YEAR)
    return _safe_div(rv, mean_5y.clip(lower=_EPS))


def vts_146_rv5d_rv21d_rv63d_composite(close: pd.Series) -> pd.Series:
    """Equal-weight composite of 5d, 21d, 63d RV (short-to-mid term vol average)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    return (rv5 + rv21 + rv63) / 3.0


def vts_147_rv_all_horizon_composite(close: pd.Series) -> pd.Series:
    """Equal-weight composite of 5d, 21d, 63d, 126d, 252d RV (full curve mean)."""
    rv5 = _realized_vol(close, _TD_WEEK)
    rv21 = _realized_vol(close, _TD_MON)
    rv63 = _realized_vol(close, _TD_QTR)
    rv126 = _realized_vol(close, _TD_HALF)
    rv252 = _realized_vol(close, _TD_YEAR)
    return (rv5 + rv21 + rv63 + rv126 + rv252) / 5.0


def vts_148_rv_composite_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of full-curve composite vs 252-day distribution."""
    comp = ((_realized_vol(close, _TD_WEEK) + _realized_vol(close, _TD_MON)
             + _realized_vol(close, _TD_QTR) + _realized_vol(close, _TD_HALF)
             + _realized_vol(close, _TD_YEAR)) / 5.0)
    return _safe_div(comp - _rolling_mean(comp, _TD_YEAR), _rolling_std(comp, _TD_YEAR))


def vts_149_pk_rv5d_rv252d_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson 5d/252d vol ratio (wide-horizon HL term spread)."""
    return _safe_div(_parkinson_vol(high, low, _TD_WEEK),
                     _parkinson_vol(high, low, _TD_YEAR))


def vts_150_gk_ts_inversion_full_flag(open_: pd.Series, high: pd.Series,
                                      low: pd.Series, close: pd.Series) -> pd.Series:
    """GK full term-structure inversion flag (5d>21d>63d>252d, OHLC-based)."""
    g5 = _garman_klass_vol(open_, high, low, close, _TD_WEEK)
    g21 = _garman_klass_vol(open_, high, low, close, _TD_MON)
    g63 = _garman_klass_vol(open_, high, low, close, _TD_QTR)
    g252 = _garman_klass_vol(open_, high, low, close, _TD_YEAR)
    return ((g5 > g21) & (g21 > g63) & (g63 > g252)).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

VOLATILITY_TERM_STRUCTURE_REGISTRY_076_150 = {
    "vts_076_ewm_rv5_span5": {"inputs": ["close"], "func": vts_076_ewm_rv5_span5},
    "vts_077_ewm_rv5_span21": {"inputs": ["close"], "func": vts_077_ewm_rv5_span21},
    "vts_078_ewm_rv5_span63": {"inputs": ["close"], "func": vts_078_ewm_rv5_span63},
    "vts_079_ewm_rv5_span252": {"inputs": ["close"], "func": vts_079_ewm_rv5_span252},
    "vts_080_ewm_vol_span5_span21_ratio": {"inputs": ["close"], "func": vts_080_ewm_vol_span5_span21_ratio},
    "vts_081_ewm_vol_span5_span63_ratio": {"inputs": ["close"], "func": vts_081_ewm_vol_span5_span63_ratio},
    "vts_082_ewm_vol_span21_span63_ratio": {"inputs": ["close"], "func": vts_082_ewm_vol_span21_span63_ratio},
    "vts_083_ewm_vol_span63_span252_ratio": {"inputs": ["close"], "func": vts_083_ewm_vol_span63_span252_ratio},
    "vts_084_ewm_vol_span5_span252_ratio": {"inputs": ["close"], "func": vts_084_ewm_vol_span5_span252_ratio},
    "vts_085_ewm_vol_inversion_5_21_flag": {"inputs": ["close"], "func": vts_085_ewm_vol_inversion_5_21_flag},
    "vts_086_ewm_vol_spread_5_21": {"inputs": ["close"], "func": vts_086_ewm_vol_spread_5_21},
    "vts_087_ewm_vol_spread_5_63": {"inputs": ["close"], "func": vts_087_ewm_vol_spread_5_63},
    "vts_088_ewm_vol_spread_21_252": {"inputs": ["close"], "func": vts_088_ewm_vol_spread_21_252},
    "vts_089_ewm_vol_span21_pct_rank_252d": {"inputs": ["close"], "func": vts_089_ewm_vol_span21_pct_rank_252d},
    "vts_090_ewm_vol_span5_zscore_252d": {"inputs": ["close"], "func": vts_090_ewm_vol_span5_zscore_252d},
    "vts_091_pk_rv5d": {"inputs": ["high", "low"], "func": vts_091_pk_rv5d},
    "vts_092_pk_rv21d": {"inputs": ["high", "low"], "func": vts_092_pk_rv21d},
    "vts_093_pk_rv63d": {"inputs": ["high", "low"], "func": vts_093_pk_rv63d},
    "vts_094_pk_rv252d": {"inputs": ["high", "low"], "func": vts_094_pk_rv252d},
    "vts_095_pk_rv5d_rv21d_ratio": {"inputs": ["high", "low"], "func": vts_095_pk_rv5d_rv21d_ratio},
    "vts_096_pk_rv21d_rv63d_ratio": {"inputs": ["high", "low"], "func": vts_096_pk_rv21d_rv63d_ratio},
    "vts_097_pk_rv63d_rv252d_ratio": {"inputs": ["high", "low"], "func": vts_097_pk_rv63d_rv252d_ratio},
    "vts_098_pk_ts_inversion_5d21d_flag": {"inputs": ["high", "low"], "func": vts_098_pk_ts_inversion_5d21d_flag},
    "vts_099_pk_ts_inversion_full_flag": {"inputs": ["high", "low"], "func": vts_099_pk_ts_inversion_full_flag},
    "vts_100_gk_rv5d": {"inputs": ["open", "high", "low", "close"], "func": vts_100_gk_rv5d},
    "vts_101_gk_rv21d": {"inputs": ["open", "high", "low", "close"], "func": vts_101_gk_rv21d},
    "vts_102_gk_rv63d": {"inputs": ["open", "high", "low", "close"], "func": vts_102_gk_rv63d},
    "vts_103_gk_rv252d": {"inputs": ["open", "high", "low", "close"], "func": vts_103_gk_rv252d},
    "vts_104_gk_rv5d_rv21d_ratio": {"inputs": ["open", "high", "low", "close"], "func": vts_104_gk_rv5d_rv21d_ratio},
    "vts_105_gk_rv21d_rv63d_ratio": {"inputs": ["open", "high", "low", "close"], "func": vts_105_gk_rv21d_rv63d_ratio},
    "vts_106_oc_rv5d": {"inputs": ["open", "close"], "func": vts_106_oc_rv5d},
    "vts_107_oc_rv21d": {"inputs": ["open", "close"], "func": vts_107_oc_rv21d},
    "vts_108_oc_rv63d": {"inputs": ["open", "close"], "func": vts_108_oc_rv63d},
    "vts_109_oc_rv252d": {"inputs": ["open", "close"], "func": vts_109_oc_rv252d},
    "vts_110_oc_rv5d_rv21d_ratio": {"inputs": ["open", "close"], "func": vts_110_oc_rv5d_rv21d_ratio},
    "vts_111_oc_rv21d_rv63d_ratio": {"inputs": ["open", "close"], "func": vts_111_oc_rv21d_rv63d_ratio},
    "vts_112_oc_rv5d_rv63d_ratio": {"inputs": ["open", "close"], "func": vts_112_oc_rv5d_rv63d_ratio},
    "vts_113_days_5d21d_inverted_in_63d": {"inputs": ["close"], "func": vts_113_days_5d21d_inverted_in_63d},
    "vts_114_days_21d63d_inverted_in_252d": {"inputs": ["close"], "func": vts_114_days_21d63d_inverted_in_252d},
    "vts_115_days_full_inverted_in_252d": {"inputs": ["close"], "func": vts_115_days_full_inverted_in_252d},
    "vts_116_fraction_5d21d_inverted_252d": {"inputs": ["close"], "func": vts_116_fraction_5d21d_inverted_252d},
    "vts_117_fraction_21d63d_inverted_63d": {"inputs": ["close"], "func": vts_117_fraction_21d63d_inverted_63d},
    "vts_118_rv5d_rv21d_ratio_rolling_mean_21d": {"inputs": ["close"], "func": vts_118_rv5d_rv21d_ratio_rolling_mean_21d},
    "vts_119_rv21d_rv63d_ratio_rolling_mean_63d": {"inputs": ["close"], "func": vts_119_rv21d_rv63d_ratio_rolling_mean_63d},
    "vts_120_rv5d_rv252d_ratio_rolling_mean_63d": {"inputs": ["close"], "func": vts_120_rv5d_rv252d_ratio_rolling_mean_63d},
    "vts_121_vov_rv5d_21d": {"inputs": ["close"], "func": vts_121_vov_rv5d_21d},
    "vts_122_vov_rv21d_63d": {"inputs": ["close"], "func": vts_122_vov_rv21d_63d},
    "vts_123_vov_rv63d_252d": {"inputs": ["close"], "func": vts_123_vov_rv63d_252d},
    "vts_124_vov_rv5d_63d": {"inputs": ["close"], "func": vts_124_vov_rv5d_63d},
    "vts_125_vov_rv252d_expanding": {"inputs": ["close"], "func": vts_125_vov_rv252d_expanding},
    "vts_126_vov_ratio_rv5d_rv21d_21d": {"inputs": ["close"], "func": vts_126_vov_ratio_rv5d_rv21d_21d},
    "vts_127_vov_ratio_rv5d_rv21d_63d": {"inputs": ["close"], "func": vts_127_vov_ratio_rv5d_rv21d_63d},
    "vts_128_rv5d_vov_zscore": {"inputs": ["close"], "func": vts_128_rv5d_vov_zscore},
    "vts_129_vov_spread_rv5d_rv252d": {"inputs": ["close"], "func": vts_129_vov_spread_rv5d_rv252d},
    "vts_130_vov_rv21d_pct_rank_252d": {"inputs": ["close"], "func": vts_130_vov_rv21d_pct_rank_252d},
    "vts_131_rv5d_rv21d_spread_norm": {"inputs": ["close"], "func": vts_131_rv5d_rv21d_spread_norm},
    "vts_132_rv21d_rv63d_spread_norm": {"inputs": ["close"], "func": vts_132_rv21d_rv63d_spread_norm},
    "vts_133_rv63d_rv252d_spread_norm": {"inputs": ["close"], "func": vts_133_rv63d_rv252d_spread_norm},
    "vts_134_rv5d_rv252d_spread_norm": {"inputs": ["close"], "func": vts_134_rv5d_rv252d_spread_norm},
    "vts_135_rv5d_rv21d_spread_zscore_252d": {"inputs": ["close"], "func": vts_135_rv5d_rv21d_spread_zscore_252d},
    "vts_136_rv21d_rv63d_spread_zscore_252d": {"inputs": ["close"], "func": vts_136_rv21d_rv63d_spread_zscore_252d},
    "vts_137_vol_curve_slope_rolling_mean_63d": {"inputs": ["close"], "func": vts_137_vol_curve_slope_rolling_mean_63d},
    "vts_138_vol_curve_slope_zscore_252d": {"inputs": ["close"], "func": vts_138_vol_curve_slope_zscore_252d},
    "vts_139_rv5d_rv21d_ratio_zscore_252d": {"inputs": ["close"], "func": vts_139_rv5d_rv21d_ratio_zscore_252d},
    "vts_140_rv63d_rv252d_ratio_zscore_252d": {"inputs": ["close"], "func": vts_140_rv63d_rv252d_ratio_zscore_252d},
    "vts_141_rv5d_rv21d_spread_pct_rank_252d": {"inputs": ["close"], "func": vts_141_rv5d_rv21d_spread_pct_rank_252d},
    "vts_142_rv21d_rv63d_spread_pct_rank_252d": {"inputs": ["close"], "func": vts_142_rv21d_rv63d_spread_pct_rank_252d},
    "vts_143_rv5d_rv252d_spread_pct_rank_252d": {"inputs": ["close"], "func": vts_143_rv5d_rv252d_spread_pct_rank_252d},
    "vts_144_rv5d_expanding_max_ratio": {"inputs": ["close"], "func": vts_144_rv5d_expanding_max_ratio},
    "vts_145_rv252d_relative_to_5yr_mean": {"inputs": ["close"], "func": vts_145_rv252d_relative_to_5yr_mean},
    "vts_146_rv5d_rv21d_rv63d_composite": {"inputs": ["close"], "func": vts_146_rv5d_rv21d_rv63d_composite},
    "vts_147_rv_all_horizon_composite": {"inputs": ["close"], "func": vts_147_rv_all_horizon_composite},
    "vts_148_rv_composite_zscore_252d": {"inputs": ["close"], "func": vts_148_rv_composite_zscore_252d},
    "vts_149_pk_rv5d_rv252d_ratio": {"inputs": ["high", "low"], "func": vts_149_pk_rv5d_rv252d_ratio},
    "vts_150_gk_ts_inversion_full_flag": {"inputs": ["open", "high", "low", "close"], "func": vts_150_gk_ts_inversion_full_flag},
}
