"""
88_insider_transaction_freq — Base Features 076-200
Domain: frequency, rate, and acceleration of insider trading ACTIVITY
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Series Contract
--------------------------------------
Inputs are daily-frequency pandas Series derived from Sharadar SF2 insider
transaction filings, aggregated to one row per (ticker, date).  Most days
carry ZERO — the series are event-driven and are NOT forward-filled.  A
positive value appears only on days when a filing was recorded.  Feature
functions aggregate over trailing rolling windows using rolling SUMS and
COUNTS; they do NOT forward-fill gaps.  Trading-day conventions used:
  5 trading days  = 1 week
  21 trading days = 1 month
  63 trading days = 1 quarter
  126 trading days = 2 quarters
  252 trading days = 1 year
  504 trading days = 2 years

All functions look strictly backward via .shift(positive_int), .rolling(),
or .expanding().  No negative shifts, no iloc[i+n], no .diff(negative).
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WK    = 5
_TD_MO    = 21
_TD_QTR   = 63
_TD_2Q    = 126
_TD_YEAR  = 252
_TD_2Y    = 504
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _active_days(s: pd.Series, w: int) -> pd.Series:
    """Count of days with nonzero values in a rolling window."""
    return _rolling_sum((s > 0).astype(float), w)


def _days_since_last_nonzero(s: pd.Series) -> pd.Series:
    """
    Backward-only helper: number of trading days since the most recent day
    with a nonzero (>0) value.  Returns NaN if no nonzero has ever appeared.
    On an all-zero series, returns NaN throughout.
    """
    n = len(s)
    arr = s.values
    out = np.full(n, np.nan)
    last = -1
    for i in range(n):
        if arr[i] > 0:
            last = i
        if last >= 0:
            out[i] = float(i - last)
    return pd.Series(out, index=s.index)


def _ols_slope(arr: np.ndarray) -> float:
    """OLS slope of arr vs [0,1,...,n-1]; returns NaN if n < 2."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = ((x - xm) ** 2).sum()
    if denom == 0.0:
        return np.nan
    return float(((x - xm) * (arr - ym)).sum() / denom)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-090): Peak / min of rolling transaction counts ---

def itf_076_txn_count_63d_vs_252d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Current 63-day transaction count minus its 252-day rolling peak.
    Negative means recent activity is below its own annual high.
    """
    total = insider_buy_count + insider_sell_count
    cnt_63 = _rolling_sum(total, _TD_QTR)
    peak   = _rolling_max(cnt_63, _TD_YEAR)
    return cnt_63 - peak


def itf_077_txn_count_63d_pct_of_252d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Current 63-day transaction count as a fraction of its 252-day peak."""
    total  = insider_buy_count + insider_sell_count
    cnt_63 = _rolling_sum(total, _TD_QTR)
    peak   = _rolling_max(cnt_63, _TD_YEAR)
    return _safe_div(cnt_63, peak)


def itf_078_buy_count_21d_vs_252d_peak(insider_buy_count: pd.Series) -> pd.Series:
    """21-day buy count minus its own 252-day rolling peak."""
    cnt_21 = _rolling_sum(insider_buy_count, _TD_MO)
    peak   = _rolling_max(cnt_21, _TD_YEAR)
    return cnt_21 - peak


def itf_079_buy_count_21d_pct_of_252d_peak(insider_buy_count: pd.Series) -> pd.Series:
    """21-day buy count as fraction of its 252-day rolling peak."""
    cnt_21 = _rolling_sum(insider_buy_count, _TD_MO)
    peak   = _rolling_max(cnt_21, _TD_YEAR)
    return _safe_div(cnt_21, peak)


def itf_080_txn_count_21d_vs_expanding_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day transaction count vs its all-history expanding maximum."""
    total  = insider_buy_count + insider_sell_count
    cnt_21 = _rolling_sum(total, _TD_MO)
    epeak  = cnt_21.expanding(min_periods=1).max()
    return cnt_21 - epeak


def itf_081_buy_count_63d_expanding_zscore(insider_buy_count: pd.Series) -> pd.Series:
    """Expanding z-score of 63-day buy count (how extreme vs all history)."""
    cnt_63 = _rolling_sum(insider_buy_count, _TD_QTR)
    m  = cnt_63.expanding(min_periods=2).mean()
    sd = cnt_63.expanding(min_periods=2).std()
    return _safe_div(cnt_63 - m, sd)


def itf_082_active_days_63d_vs_252d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day active-day count vs its 252-day rolling peak."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    ad_63   = _rolling_sum(any_txn, _TD_QTR)
    peak    = _rolling_max(ad_63, _TD_YEAR)
    return ad_63 - peak


def itf_083_active_days_density_21v252_ratio(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 21-day active-day density to 252-day active-day density."""
    any_txn  = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    dens_21  = _rolling_mean(any_txn, _TD_MO)
    dens_252 = _rolling_mean(any_txn, _TD_YEAR)
    return _safe_div(dens_21, dens_252)


def itf_084_txn_count_5d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Total insider transactions over trailing 5-day (1-week) window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_sum(total, _TD_WK)


def itf_085_buy_count_5d(insider_buy_count: pd.Series) -> pd.Series:
    """Insider buy count over trailing 5-day window."""
    return _rolling_sum(insider_buy_count, _TD_WK)


def itf_086_txn_count_5d_vs_21d_rate(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """5-day transaction rate vs 21-day rate (ultra-recent vs monthly acceleration)."""
    total    = insider_buy_count + insider_sell_count
    rate_5   = _rolling_sum(total, _TD_WK) / _TD_WK
    rate_21  = _rolling_sum(total, _TD_MO) / _TD_MO
    return rate_5 - rate_21


def itf_087_buy_count_5d_vs_63d_rate(insider_buy_count: pd.Series) -> pd.Series:
    """5-day buy rate vs 63-day buy rate."""
    rate_5  = _rolling_sum(insider_buy_count, _TD_WK) / _TD_WK
    rate_63 = _rolling_sum(insider_buy_count, _TD_QTR) / _TD_QTR
    return rate_5 - rate_63


def itf_088_officer_director_buy_count_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy count over 63-day window."""
    return _rolling_sum(officer_buy_count + director_buy_count, _TD_QTR)


def itf_089_officer_director_buy_count_252d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director buy count over 252-day window."""
    return _rolling_sum(officer_buy_count + director_buy_count, _TD_YEAR)


def itf_090_officer_director_buy_accel_21v252(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Ratio of 21-day officer+director buy rate to 252-day rate."""
    combo    = officer_buy_count + director_buy_count
    rate_21  = _rolling_sum(combo, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(combo, _TD_YEAR) / _TD_YEAR
    return _safe_div(rate_21, rate_252)


# --- Group I (091-105): Rolling slope / trend of activity ---

def itf_091_txn_count_21d_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    OLS slope of the 21-day rolling transaction count over a 63-day window.
    Rising slope = accelerating activity trend.
    """
    total  = insider_buy_count + insider_sell_count
    cnt_21 = _rolling_sum(total, _TD_MO)
    return cnt_21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_092_buy_count_21d_slope_63d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 21-day buy count over a 63-day window."""
    cnt_21 = _rolling_sum(insider_buy_count, _TD_MO)
    return cnt_21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_093_active_days_21d_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of the 21-day active-day count over a 63-day window."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    ad_21   = _rolling_sum(any_txn, _TD_MO)
    return ad_21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_094_buyer_count_21d_slope_63d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of the 21-day buyer-sum over a 63-day window."""
    sum_21 = _rolling_sum(insider_buyers, _TD_MO)
    return sum_21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_095_txn_count_63d_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of the 63-day transaction count over a 252-day window."""
    total  = insider_buy_count + insider_sell_count
    cnt_63 = _rolling_sum(total, _TD_QTR)
    return cnt_63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_096_buy_count_63d_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of the 63-day buy count over a 252-day window."""
    cnt_63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return cnt_63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_097_txn_ewm_minus_long_mean(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM (span=21) of total transactions minus 252-day rolling mean (momentum signal)."""
    total   = insider_buy_count + insider_sell_count
    ewm_21  = _ewm_mean(total, _TD_MO)
    mean_252 = _rolling_mean(total, _TD_YEAR)
    return ewm_21 - mean_252


def itf_098_buy_ewm_minus_long_mean(insider_buy_count: pd.Series) -> pd.Series:
    """EWM (span=21) of buy count minus 252-day rolling mean."""
    ewm_21   = _ewm_mean(insider_buy_count, _TD_MO)
    mean_252 = _rolling_mean(insider_buy_count, _TD_YEAR)
    return ewm_21 - mean_252


def itf_099_txn_ewm63_minus_ewm252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=63) minus EWM(span=252) of total transactions (MACD-style)."""
    total = insider_buy_count + insider_sell_count
    return _ewm_mean(total, _TD_QTR) - _ewm_mean(total, _TD_YEAR)


def itf_100_buy_ewm21_minus_ewm63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=63) of buy count."""
    return _ewm_mean(insider_buy_count, _TD_MO) - _ewm_mean(insider_buy_count, _TD_QTR)


def itf_101_active_days_63d_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day active-day count over 252-day window."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    ad_63   = _rolling_sum(any_txn, _TD_QTR)
    return ad_63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_102_txn_pct_change_21d_lag21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of 21-day transaction count vs prior 21-day window (non-overlapping)."""
    total  = insider_buy_count + insider_sell_count
    cnt_21 = _rolling_sum(total, _TD_MO)
    prior  = cnt_21.shift(_TD_MO)
    return _safe_div(cnt_21 - prior, prior)


def itf_103_buy_count_pct_change_63d_lag63(insider_buy_count: pd.Series) -> pd.Series:
    """Pct change of 63-day buy count vs prior 63-day window."""
    cnt_63 = _rolling_sum(insider_buy_count, _TD_QTR)
    prior  = cnt_63.shift(_TD_QTR)
    return _safe_div(cnt_63 - prior, prior)


def itf_104_txn_count_pct_change_63d_lag252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day transaction count now vs 63-day count 252 days ago (YoY comparison)."""
    total  = insider_buy_count + insider_sell_count
    cnt_63 = _rolling_sum(total, _TD_QTR)
    prior  = cnt_63.shift(_TD_YEAR)
    return _safe_div(cnt_63 - prior, prior.abs())


def itf_105_buyer_sum_pct_change_63d_lag63(insider_buyers: pd.Series) -> pd.Series:
    """Pct change of 63-day buyer sum vs prior 63-day window."""
    sum_63 = _rolling_sum(insider_buyers, _TD_QTR)
    prior  = sum_63.shift(_TD_QTR)
    return _safe_div(sum_63 - prior, prior)


# --- Group J (106-120): Cross-window regularity / burstiness metrics ---

def itf_106_txn_cv_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Coefficient of variation of daily total transactions over 63-day window.
    High CV = bursty; low CV = regular activity.
    """
    total = insider_buy_count + insider_sell_count
    m = _rolling_mean(total, _TD_QTR)
    s = _rolling_std(total, _TD_QTR)
    return _safe_div(s, m)


def itf_107_txn_cv_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Coefficient of variation of daily transactions over 252-day window."""
    total = insider_buy_count + insider_sell_count
    m = _rolling_mean(total, _TD_YEAR)
    s = _rolling_std(total, _TD_YEAR)
    return _safe_div(s, m)


def itf_108_buy_cv_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation of daily buy count over 252-day window."""
    m = _rolling_mean(insider_buy_count, _TD_YEAR)
    s = _rolling_std(insider_buy_count, _TD_YEAR)
    return _safe_div(s, m)


def itf_109_txn_max_single_day_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Maximum single-day transaction count in trailing 21-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_max(total, _TD_MO)


def itf_110_txn_max_single_day_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Maximum single-day transaction count in trailing 63-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_max(total, _TD_QTR)


def itf_111_txn_max_single_day_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Maximum single-day transaction count in trailing 252-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_max(total, _TD_YEAR)


def itf_112_buy_max_single_day_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Maximum single-day buy count in trailing 63-day window."""
    return _rolling_max(insider_buy_count, _TD_QTR)


def itf_113_txn_median_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Median daily transaction count over 63-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_median(total, _TD_QTR)


def itf_114_txn_median_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Median daily transaction count over 252-day window."""
    total = insider_buy_count + insider_sell_count
    return _rolling_median(total, _TD_YEAR)


def itf_115_txn_max_to_median_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 21-day max daily count to 21-day median daily count (spike ratio)."""
    total = insider_buy_count + insider_sell_count
    mx  = _rolling_max(total, _TD_MO)
    med = _rolling_median(total, _TD_MO)
    return _safe_div(mx, med)


def itf_116_txn_count_above_mean_days_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Days in trailing 63-day window where daily count exceeds the 252-day mean."""
    total    = insider_buy_count + insider_sell_count
    mean_252 = _rolling_mean(total, _TD_YEAR)
    above    = (total > mean_252).astype(float)
    return _rolling_sum(above, _TD_QTR)


def itf_117_txn_count_above_mean_days_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Days in trailing 252-day window where daily count exceeds the 504-day mean."""
    total    = insider_buy_count + insider_sell_count
    mean_504 = _rolling_mean(total, _TD_2Y)
    above    = (total > mean_504).astype(float)
    return _rolling_sum(above, _TD_YEAR)


def itf_118_txn_expanding_pct_rank(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Expanding percentile rank of daily total transaction count (all-history rank)."""
    total = insider_buy_count + insider_sell_count
    return total.expanding(min_periods=2).rank(pct=True)


def itf_119_buy_expanding_pct_rank(insider_buy_count: pd.Series) -> pd.Series:
    """Expanding percentile rank of daily buy count (all-history rank)."""
    return insider_buy_count.expanding(min_periods=2).rank(pct=True)


def itf_120_txn_count_5d_vs_504d_rate(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of 5-day transaction rate to 504-day rate (ultra-short vs 2-year baseline)."""
    total    = insider_buy_count + insider_sell_count
    rate_5   = _rolling_sum(total, _TD_WK) / _TD_WK
    rate_504 = _rolling_sum(total, _TD_2Y) / _TD_2Y
    return _safe_div(rate_5, rate_504)


# --- Group K (121-135): Officer / director specific frequency features ---

def itf_121_officer_buy_active_days_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with an officer buy in trailing 63-day window."""
    return _active_days(officer_buy_count, _TD_QTR)


def itf_122_director_buy_active_days_63d(director_buy_count: pd.Series) -> pd.Series:
    """Number of distinct days with a director buy in trailing 63-day window."""
    return _active_days(director_buy_count, _TD_QTR)


def itf_123_officer_buy_density_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Fraction of days in 63-day window with an officer buy."""
    return _rolling_mean((officer_buy_count > 0).astype(float), _TD_QTR)


def itf_124_director_buy_density_63d(director_buy_count: pd.Series) -> pd.Series:
    """Fraction of days in 63-day window with a director buy."""
    return _rolling_mean((director_buy_count > 0).astype(float), _TD_QTR)


def itf_125_officer_buy_zscore_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Z-score of daily officer buy count within a 63-day window."""
    return _zscore_rolling(officer_buy_count, _TD_QTR)


def itf_126_director_buy_zscore_252d(director_buy_count: pd.Series) -> pd.Series:
    """Z-score of daily director buy count within a 252-day window."""
    return _zscore_rolling(director_buy_count, _TD_YEAR)


def itf_127_officer_buy_pct_rank_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of daily officer buy count within 252-day window."""
    return _rolling_rank_pct(officer_buy_count, _TD_YEAR)


def itf_128_officer_plus_director_density_252d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Fraction of days in 252-day window with any officer or director buy."""
    any_od = ((officer_buy_count + director_buy_count) > 0).astype(float)
    return _rolling_mean(any_od, _TD_YEAR)


def itf_129_officer_buy_count_5d(officer_buy_count: pd.Series) -> pd.Series:
    """Officer buy transaction count over trailing 5-day window."""
    return _rolling_sum(officer_buy_count, _TD_WK)


def itf_130_officer_buy_count_21d(officer_buy_count: pd.Series) -> pd.Series:
    """Officer buy transaction count over trailing 21-day window."""
    return _rolling_sum(officer_buy_count, _TD_MO)


def itf_131_director_buy_count_21d(director_buy_count: pd.Series) -> pd.Series:
    """Director buy transaction count over trailing 21-day window."""
    return _rolling_sum(director_buy_count, _TD_MO)


def itf_132_officer_buy_accel_63v252(officer_buy_count: pd.Series) -> pd.Series:
    """63-day officer buy rate vs 252-day officer buy rate (acceleration)."""
    rate_63  = _rolling_sum(officer_buy_count, _TD_QTR) / _TD_QTR
    rate_252 = _rolling_sum(officer_buy_count, _TD_YEAR) / _TD_YEAR
    return rate_63 - rate_252


def itf_133_director_buy_accel_63v252(director_buy_count: pd.Series) -> pd.Series:
    """63-day director buy rate vs 252-day director buy rate (acceleration)."""
    rate_63  = _rolling_sum(director_buy_count, _TD_QTR) / _TD_QTR
    rate_252 = _rolling_sum(director_buy_count, _TD_YEAR) / _TD_YEAR
    return rate_63 - rate_252


def itf_134_officer_buy_slope_252d(officer_buy_count: pd.Series) -> pd.Series:
    """OLS slope of daily officer buy count over 252-day window."""
    return officer_buy_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_135_director_buy_slope_252d(director_buy_count: pd.Series) -> pd.Series:
    """OLS slope of daily director buy count over 252-day window."""
    return director_buy_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


# --- Group L (136-150): Inter-window gap dynamics and surge detection ---

def itf_136_burst_count_21d_windows_in_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Number of non-overlapping 21-day windows in the past 252 days that contained
    at least one transaction.  Approximated by summing an indicator of
    activity in each lagged 21-day window (12 windows = 252/21).
    """
    total = insider_buy_count + insider_sell_count
    cnt_21 = _rolling_sum(total, _TD_MO)
    # Check each of 12 prior non-overlapping windows (lag 0,21,42,...,231)
    active = pd.Series(0.0, index=total.index)
    for lag in range(0, _TD_YEAR, _TD_MO):
        active = active + (cnt_21.shift(lag) > 0).astype(float)
    return active


def itf_137_quiet_to_active_transitions_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Count of 0->1 transitions (quiet->active day) in trailing 252-day window.
    Each transition = a new burst of activity beginning.
    """
    total    = insider_buy_count + insider_sell_count
    active   = (total > 0).astype(float)
    was_quiet = (total.shift(1) == 0).astype(float)
    new_burst = (active * was_quiet)
    return _rolling_sum(new_burst, _TD_YEAR)


def itf_138_quiet_to_active_transitions_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Count of 0->1 transitions in trailing 63-day window."""
    total     = insider_buy_count + insider_sell_count
    active    = (total > 0).astype(float)
    was_quiet = (total.shift(1) == 0).astype(float)
    new_burst = active * was_quiet
    return _rolling_sum(new_burst, _TD_QTR)


def itf_139_buy_quiet_to_active_transitions_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Count of 0->1 buy transitions in trailing 252-day window."""
    active    = (insider_buy_count > 0).astype(float)
    was_quiet = (insider_buy_count.shift(1) == 0).astype(float)
    return _rolling_sum(active * was_quiet, _TD_YEAR)


def itf_140_burst_intensity_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Burst intensity: 21-day total transactions divided by number of active
    days in that window.  Measures average transactions per active day.
    """
    total   = insider_buy_count + insider_sell_count
    cnt_21  = _rolling_sum(total, _TD_MO)
    act_21  = _rolling_sum((total > 0).astype(float), _TD_MO)
    return _safe_div(cnt_21, act_21)


def itf_141_burst_intensity_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Burst intensity over 63-day window: total transactions per active day."""
    total  = insider_buy_count + insider_sell_count
    cnt_63 = _rolling_sum(total, _TD_QTR)
    act_63 = _rolling_sum((total > 0).astype(float), _TD_QTR)
    return _safe_div(cnt_63, act_63)


def itf_142_txn_concentration_21in63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of 63-day transactions that occurred in the most recent 21 days."""
    total  = insider_buy_count + insider_sell_count
    cnt_21 = _rolling_sum(total, _TD_MO)
    cnt_63 = _rolling_sum(total, _TD_QTR)
    return _safe_div(cnt_21, cnt_63)


def itf_143_txn_concentration_63in252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of 252-day transactions that occurred in the most recent 63 days."""
    total   = insider_buy_count + insider_sell_count
    cnt_63  = _rolling_sum(total, _TD_QTR)
    cnt_252 = _rolling_sum(total, _TD_YEAR)
    return _safe_div(cnt_63, cnt_252)


def itf_144_buy_concentration_21in63(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 63-day buy count occurring in the most recent 21 days."""
    cnt_21 = _rolling_sum(insider_buy_count, _TD_MO)
    cnt_63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return _safe_div(cnt_21, cnt_63)


def itf_145_surge_flag_21d_3x_252d_rate(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if 21-day transaction rate >= 3x the 252-day baseline rate."""
    total    = insider_buy_count + insider_sell_count
    rate_21  = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    return (rate_21 >= 3.0 * rate_252).astype(float)


def itf_146_surge_flag_21d_5x_504d_rate(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if 21-day rate >= 5x the 504-day baseline rate."""
    total    = insider_buy_count + insider_sell_count
    rate_21  = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_504 = _rolling_sum(total, _TD_2Y) / _TD_2Y
    return (rate_21 >= 5.0 * rate_504).astype(float)


def itf_147_buyers_21d_vs_252d_peak(insider_buyers: pd.Series) -> pd.Series:
    """21-day buyer sum vs its 252-day rolling peak."""
    sum_21 = _rolling_sum(insider_buyers, _TD_MO)
    peak   = _rolling_max(sum_21, _TD_YEAR)
    return sum_21 - peak


def itf_148_total_participants_21d_accel_21v252(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Ratio of 21-day participant rate to 252-day participant rate."""
    combo    = insider_buyers + insider_sellers
    rate_21  = _rolling_sum(combo, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(combo, _TD_YEAR) / _TD_YEAR
    return _safe_div(rate_21, rate_252)


def itf_149_multi_buyer_day_count_252d(insider_buyers: pd.Series) -> pd.Series:
    """Count of days in trailing 252-day window where insider_buyers >= 2."""
    multi = (insider_buyers >= 2).astype(float)
    return _rolling_sum(multi, _TD_YEAR)


def itf_150_activity_acceleration_composite(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Composite acceleration score: equally weighted sum of three acceleration signals:
      (1) txn_accel_21v252 z-score, (2) buyer_accel_21v252 z-score,
      (3) active_day_density_21d vs 252d z-score.
    Higher = stronger recent acceleration in activity.
    """
    total    = insider_buy_count + insider_sell_count
    rate_21  = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    accel_txn = rate_21 - rate_252

    brate_21  = _rolling_sum(insider_buyers, _TD_MO) / _TD_MO
    brate_252 = _rolling_sum(insider_buyers, _TD_YEAR) / _TD_YEAR
    accel_buy = brate_21 - brate_252

    any_txn   = (total > 0).astype(float)
    dens_21   = _rolling_mean(any_txn, _TD_MO)
    dens_252  = _rolling_mean(any_txn, _TD_YEAR)
    accel_den = dens_21 - dens_252

    z1 = _zscore_rolling(accel_txn, _TD_YEAR)
    z2 = _zscore_rolling(accel_buy, _TD_YEAR)
    z3 = _zscore_rolling(accel_den, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


# ── Feature functions 176-200 ─────────────────────────────────────────────────

# --- Group M (176-185): Cross-window peak/trough normalization ---

def itf_176_buy_count_63d_pct_of_504d_peak(insider_buy_count: pd.Series) -> pd.Series:
    """63-day buy count as fraction of its 504-day rolling peak."""
    cnt = _rolling_sum(insider_buy_count, _TD_QTR)
    return _safe_div(cnt, _rolling_max(cnt, _TD_2Y))


def itf_177_txn_count_21d_pct_of_252d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day transaction count as fraction of its 252-day rolling peak."""
    total  = insider_buy_count + insider_sell_count
    cnt_21 = _rolling_sum(total, _TD_MO)
    return _safe_div(cnt_21, _rolling_max(cnt_21, _TD_YEAR))


def itf_178_active_days_21d_pct_of_252d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day active-day count as fraction of its 252-day rolling peak."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    ad_21   = _rolling_sum(any_txn, _TD_MO)
    return _safe_div(ad_21, _rolling_max(ad_21, _TD_YEAR))


def itf_179_buyers_63d_pct_of_252d_peak(insider_buyers: pd.Series) -> pd.Series:
    """63-day buyer sum as fraction of its 252-day rolling peak."""
    s63 = _rolling_sum(insider_buyers, _TD_QTR)
    return _safe_div(s63, _rolling_max(s63, _TD_YEAR))


def itf_180_officer_buy_63d_pct_of_252d_peak(officer_buy_count: pd.Series) -> pd.Series:
    """63-day officer buy count as fraction of its 252-day rolling peak."""
    cnt = _rolling_sum(officer_buy_count, _TD_QTR)
    return _safe_div(cnt, _rolling_max(cnt, _TD_YEAR))


def itf_181_txn_count_63d_expanding_pct_rank(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Expanding percentile rank of the 63-day transaction count (all-history rank)."""
    cnt63 = _rolling_sum(insider_buy_count + insider_sell_count, _TD_QTR)
    return cnt63.expanding(min_periods=2).rank(pct=True)


def itf_182_buy_cnt21_pct_of_504d_peak(insider_buy_count: pd.Series) -> pd.Series:
    """21-day buy count as fraction of its 504-day rolling peak."""
    cnt = _rolling_sum(insider_buy_count, _TD_MO)
    return _safe_div(cnt, _rolling_max(cnt, _TD_2Y))


def itf_183_active_days_126d_pct_of_504d_peak(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """126-day active-day count as fraction of its 504-day rolling peak."""
    any_txn = ((insider_buy_count + insider_sell_count) > 0).astype(float)
    ad_126  = _rolling_sum(any_txn, _TD_2Q)
    return _safe_div(ad_126, _rolling_max(ad_126, _TD_2Y))


def itf_184_director_buy_63d_pct_of_252d_peak(director_buy_count: pd.Series) -> pd.Series:
    """63-day director buy count as fraction of its 252-day rolling peak."""
    cnt = _rolling_sum(director_buy_count, _TD_QTR)
    return _safe_div(cnt, _rolling_max(cnt, _TD_YEAR))


def itf_185_buyers_252d_pct_of_504d_peak(insider_buyers: pd.Series) -> pd.Series:
    """252-day buyer sum as fraction of its 504-day rolling peak."""
    s252 = _rolling_sum(insider_buyers, _TD_YEAR)
    return _safe_div(s252, _rolling_max(s252, _TD_2Y))


# --- Group N (186-193): EWM-based frequency momentum ---

def itf_186_txn_ewm5_minus_ewm21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=5) minus EWM(span=21) of total transactions (ultra-short MACD)."""
    total = insider_buy_count + insider_sell_count
    return _ewm_mean(total, _TD_WK) - _ewm_mean(total, _TD_MO)


def itf_187_buy_ewm5_minus_ewm63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(span=5) minus EWM(span=63) of buy count."""
    return _ewm_mean(insider_buy_count, _TD_WK) - _ewm_mean(insider_buy_count, _TD_QTR)


def itf_188_txn_ewm21_minus_ewm252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=252) of total transactions."""
    total = insider_buy_count + insider_sell_count
    return _ewm_mean(total, _TD_MO) - _ewm_mean(total, _TD_YEAR)


def itf_189_buy_ewm63_minus_ewm252(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(span=63) minus EWM(span=252) of buy count (quarterly vs annual momentum)."""
    return _ewm_mean(insider_buy_count, _TD_QTR) - _ewm_mean(insider_buy_count, _TD_YEAR)


def itf_190_officer_buy_ewm21_minus_ewm252(officer_buy_count: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=252) of officer buy count."""
    return _ewm_mean(officer_buy_count, _TD_MO) - _ewm_mean(officer_buy_count, _TD_YEAR)


def itf_191_buyers_ewm21_minus_ewm252(insider_buyers: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=252) of insider_buyers."""
    return _ewm_mean(insider_buyers, _TD_MO) - _ewm_mean(insider_buyers, _TD_YEAR)


def itf_192_txn_ewm_ratio_21v63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Ratio of EWM(span=21) to EWM(span=63) of total transactions."""
    total = insider_buy_count + insider_sell_count
    return _safe_div(_ewm_mean(total, _TD_MO), _ewm_mean(total, _TD_QTR))


def itf_193_buy_ewm_ratio_21v252(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of EWM(span=21) to EWM(span=252) of buy count."""
    return _safe_div(_ewm_mean(insider_buy_count, _TD_MO),
                     _ewm_mean(insider_buy_count, _TD_YEAR))


# --- Group O (194-200): New surge / concentration / cross-type signals ---

def itf_194_buy_concentration_63in252(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of 252-day buy count occurring in the most recent 63 days."""
    cnt_63  = _rolling_sum(insider_buy_count, _TD_QTR)
    cnt_252 = _rolling_sum(insider_buy_count, _TD_YEAR)
    return _safe_div(cnt_63, cnt_252)


def itf_195_surge_flag_5d_2x_252d_rate(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if 5-day transaction rate >= 2x the 252-day baseline rate."""
    total    = insider_buy_count + insider_sell_count
    rate_5   = _rolling_sum(total, _TD_WK) / _TD_WK
    rate_252 = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    return (rate_5 >= 2.0 * rate_252).astype(float)


def itf_196_buy_surge_flag_21d_2x_504d_rate(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if 21-day buy rate >= 2x the 504-day buy baseline rate."""
    rate_21  = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    rate_504 = _rolling_sum(insider_buy_count, _TD_2Y) / _TD_2Y
    return (rate_21 >= 2.0 * rate_504).astype(float)


def itf_197_txn_count_5d_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of 5-day transaction count within a 252-day rolling window."""
    cnt5 = _rolling_sum(insider_buy_count + insider_sell_count, _TD_WK)
    return _zscore_rolling(cnt5, _TD_YEAR)


def itf_198_buy_count_pct_rank_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of daily buy count within 63-day rolling window."""
    return _rolling_rank_pct(insider_buy_count, _TD_QTR)


def itf_199_officer_director_buy_density_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Fraction of days in 63-day window with any officer or director buy."""
    any_od = ((officer_buy_count + director_buy_count) > 0).astype(float)
    return _rolling_mean(any_od, _TD_QTR)


def itf_200_activity_breadth_score_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """
    Activity breadth score: equally weighted z-score sum of (1) total txn count 252d,
    (2) total participants 252d, (3) active-day density 252d.
    Higher = broader insider participation vs own history.
    """
    total        = insider_buy_count + insider_sell_count
    z_cnt        = _zscore_rolling(_rolling_sum(total, _TD_YEAR), _TD_YEAR)
    z_part       = _zscore_rolling(_rolling_sum(insider_buyers + insider_sellers, _TD_YEAR), _TD_YEAR)
    z_density    = _zscore_rolling(_rolling_mean((total > 0).astype(float), _TD_YEAR), _TD_YEAR)
    return (z_cnt + z_part + z_density) / 3.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INSIDER_TRANSACTION_FREQ_REGISTRY_076_150 = {
    "itf_076_txn_count_63d_vs_252d_peak":           {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_076_txn_count_63d_vs_252d_peak},
    "itf_077_txn_count_63d_pct_of_252d_peak":       {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_077_txn_count_63d_pct_of_252d_peak},
    "itf_078_buy_count_21d_vs_252d_peak":           {"inputs": ["insider_buy_count"],                       "func": itf_078_buy_count_21d_vs_252d_peak},
    "itf_079_buy_count_21d_pct_of_252d_peak":       {"inputs": ["insider_buy_count"],                       "func": itf_079_buy_count_21d_pct_of_252d_peak},
    "itf_080_txn_count_21d_vs_expanding_peak":      {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_080_txn_count_21d_vs_expanding_peak},
    "itf_081_buy_count_63d_expanding_zscore":       {"inputs": ["insider_buy_count"],                       "func": itf_081_buy_count_63d_expanding_zscore},
    "itf_082_active_days_63d_vs_252d_peak":         {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_082_active_days_63d_vs_252d_peak},
    "itf_083_active_days_density_21v252_ratio":     {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_083_active_days_density_21v252_ratio},
    "itf_084_txn_count_5d":                         {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_084_txn_count_5d},
    "itf_085_buy_count_5d":                         {"inputs": ["insider_buy_count"],                       "func": itf_085_buy_count_5d},
    "itf_086_txn_count_5d_vs_21d_rate":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_086_txn_count_5d_vs_21d_rate},
    "itf_087_buy_count_5d_vs_63d_rate":             {"inputs": ["insider_buy_count"],                       "func": itf_087_buy_count_5d_vs_63d_rate},
    "itf_088_officer_director_buy_count_63d":       {"inputs": ["officer_buy_count", "director_buy_count"], "func": itf_088_officer_director_buy_count_63d},
    "itf_089_officer_director_buy_count_252d":      {"inputs": ["officer_buy_count", "director_buy_count"], "func": itf_089_officer_director_buy_count_252d},
    "itf_090_officer_director_buy_accel_21v252":    {"inputs": ["officer_buy_count", "director_buy_count"], "func": itf_090_officer_director_buy_accel_21v252},
    "itf_091_txn_count_21d_slope_63d":              {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_091_txn_count_21d_slope_63d},
    "itf_092_buy_count_21d_slope_63d":              {"inputs": ["insider_buy_count"],                       "func": itf_092_buy_count_21d_slope_63d},
    "itf_093_active_days_21d_slope_63d":            {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_093_active_days_21d_slope_63d},
    "itf_094_buyer_count_21d_slope_63d":            {"inputs": ["insider_buyers"],                          "func": itf_094_buyer_count_21d_slope_63d},
    "itf_095_txn_count_63d_slope_252d":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_095_txn_count_63d_slope_252d},
    "itf_096_buy_count_63d_slope_252d":             {"inputs": ["insider_buy_count"],                       "func": itf_096_buy_count_63d_slope_252d},
    "itf_097_txn_ewm_minus_long_mean":              {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_097_txn_ewm_minus_long_mean},
    "itf_098_buy_ewm_minus_long_mean":              {"inputs": ["insider_buy_count"],                       "func": itf_098_buy_ewm_minus_long_mean},
    "itf_099_txn_ewm63_minus_ewm252":               {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_099_txn_ewm63_minus_ewm252},
    "itf_100_buy_ewm21_minus_ewm63":                {"inputs": ["insider_buy_count"],                       "func": itf_100_buy_ewm21_minus_ewm63},
    "itf_101_active_days_63d_slope_252d":           {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_101_active_days_63d_slope_252d},
    "itf_102_txn_pct_change_21d_lag21":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_102_txn_pct_change_21d_lag21},
    "itf_103_buy_count_pct_change_63d_lag63":       {"inputs": ["insider_buy_count"],                       "func": itf_103_buy_count_pct_change_63d_lag63},
    "itf_104_txn_count_pct_change_63d_lag252":      {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_104_txn_count_pct_change_63d_lag252},
    "itf_105_buyer_sum_pct_change_63d_lag63":       {"inputs": ["insider_buyers"],                          "func": itf_105_buyer_sum_pct_change_63d_lag63},
    "itf_106_txn_cv_63d":                           {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_106_txn_cv_63d},
    "itf_107_txn_cv_252d":                          {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_107_txn_cv_252d},
    "itf_108_buy_cv_252d":                          {"inputs": ["insider_buy_count"],                       "func": itf_108_buy_cv_252d},
    "itf_109_txn_max_single_day_21d":               {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_109_txn_max_single_day_21d},
    "itf_110_txn_max_single_day_63d":               {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_110_txn_max_single_day_63d},
    "itf_111_txn_max_single_day_252d":              {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_111_txn_max_single_day_252d},
    "itf_112_buy_max_single_day_63d":               {"inputs": ["insider_buy_count"],                       "func": itf_112_buy_max_single_day_63d},
    "itf_113_txn_median_63d":                       {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_113_txn_median_63d},
    "itf_114_txn_median_252d":                      {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_114_txn_median_252d},
    "itf_115_txn_max_to_median_21d":                {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_115_txn_max_to_median_21d},
    "itf_116_txn_count_above_mean_days_63d":        {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_116_txn_count_above_mean_days_63d},
    "itf_117_txn_count_above_mean_days_252d":       {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_117_txn_count_above_mean_days_252d},
    "itf_118_txn_expanding_pct_rank":               {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_118_txn_expanding_pct_rank},
    "itf_119_buy_expanding_pct_rank":               {"inputs": ["insider_buy_count"],                       "func": itf_119_buy_expanding_pct_rank},
    "itf_120_txn_count_5d_vs_504d_rate":            {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_120_txn_count_5d_vs_504d_rate},
    "itf_121_officer_buy_active_days_63d":          {"inputs": ["officer_buy_count"],                       "func": itf_121_officer_buy_active_days_63d},
    "itf_122_director_buy_active_days_63d":         {"inputs": ["director_buy_count"],                      "func": itf_122_director_buy_active_days_63d},
    "itf_123_officer_buy_density_63d":              {"inputs": ["officer_buy_count"],                       "func": itf_123_officer_buy_density_63d},
    "itf_124_director_buy_density_63d":             {"inputs": ["director_buy_count"],                      "func": itf_124_director_buy_density_63d},
    "itf_125_officer_buy_zscore_63d":               {"inputs": ["officer_buy_count"],                       "func": itf_125_officer_buy_zscore_63d},
    "itf_126_director_buy_zscore_252d":             {"inputs": ["director_buy_count"],                      "func": itf_126_director_buy_zscore_252d},
    "itf_127_officer_buy_pct_rank_252d":            {"inputs": ["officer_buy_count"],                       "func": itf_127_officer_buy_pct_rank_252d},
    "itf_128_officer_plus_director_density_252d":   {"inputs": ["officer_buy_count", "director_buy_count"], "func": itf_128_officer_plus_director_density_252d},
    "itf_129_officer_buy_count_5d":                 {"inputs": ["officer_buy_count"],                       "func": itf_129_officer_buy_count_5d},
    "itf_130_officer_buy_count_21d":                {"inputs": ["officer_buy_count"],                       "func": itf_130_officer_buy_count_21d},
    "itf_131_director_buy_count_21d":               {"inputs": ["director_buy_count"],                      "func": itf_131_director_buy_count_21d},
    "itf_132_officer_buy_accel_63v252":             {"inputs": ["officer_buy_count"],                       "func": itf_132_officer_buy_accel_63v252},
    "itf_133_director_buy_accel_63v252":            {"inputs": ["director_buy_count"],                      "func": itf_133_director_buy_accel_63v252},
    "itf_134_officer_buy_slope_252d":               {"inputs": ["officer_buy_count"],                       "func": itf_134_officer_buy_slope_252d},
    "itf_135_director_buy_slope_252d":              {"inputs": ["director_buy_count"],                      "func": itf_135_director_buy_slope_252d},
    "itf_136_burst_count_21d_windows_in_252d":      {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_136_burst_count_21d_windows_in_252d},
    "itf_137_quiet_to_active_transitions_252d":     {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_137_quiet_to_active_transitions_252d},
    "itf_138_quiet_to_active_transitions_63d":      {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_138_quiet_to_active_transitions_63d},
    "itf_139_buy_quiet_to_active_transitions_252d": {"inputs": ["insider_buy_count"],                       "func": itf_139_buy_quiet_to_active_transitions_252d},
    "itf_140_burst_intensity_21d":                  {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_140_burst_intensity_21d},
    "itf_141_burst_intensity_63d":                  {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_141_burst_intensity_63d},
    "itf_142_txn_concentration_21in63":             {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_142_txn_concentration_21in63},
    "itf_143_txn_concentration_63in252":            {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_143_txn_concentration_63in252},
    "itf_144_buy_concentration_21in63":             {"inputs": ["insider_buy_count"],                       "func": itf_144_buy_concentration_21in63},
    "itf_145_surge_flag_21d_3x_252d_rate":          {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_145_surge_flag_21d_3x_252d_rate},
    "itf_146_surge_flag_21d_5x_504d_rate":          {"inputs": ["insider_buy_count", "insider_sell_count"], "func": itf_146_surge_flag_21d_5x_504d_rate},
    "itf_147_buyers_21d_vs_252d_peak":              {"inputs": ["insider_buyers"],                          "func": itf_147_buyers_21d_vs_252d_peak},
    "itf_148_total_participants_21d_accel_21v252":  {"inputs": ["insider_buyers", "insider_sellers"],        "func": itf_148_total_participants_21d_accel_21v252},
    "itf_149_multi_buyer_day_count_252d":           {"inputs": ["insider_buyers"],                          "func": itf_149_multi_buyer_day_count_252d},
    "itf_150_activity_acceleration_composite":      {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"], "func": itf_150_activity_acceleration_composite},
    "itf_176_buy_count_63d_pct_of_504d_peak":       {"inputs": ["insider_buy_count"],                                         "func": itf_176_buy_count_63d_pct_of_504d_peak},
    "itf_177_txn_count_21d_pct_of_252d_peak":       {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_177_txn_count_21d_pct_of_252d_peak},
    "itf_178_active_days_21d_pct_of_252d_peak":     {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_178_active_days_21d_pct_of_252d_peak},
    "itf_179_buyers_63d_pct_of_252d_peak":          {"inputs": ["insider_buyers"],                                            "func": itf_179_buyers_63d_pct_of_252d_peak},
    "itf_180_officer_buy_63d_pct_of_252d_peak":     {"inputs": ["officer_buy_count"],                                         "func": itf_180_officer_buy_63d_pct_of_252d_peak},
    "itf_181_txn_count_63d_expanding_pct_rank":     {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_181_txn_count_63d_expanding_pct_rank},
    "itf_182_buy_cnt21_pct_of_504d_peak":           {"inputs": ["insider_buy_count"],                                         "func": itf_182_buy_cnt21_pct_of_504d_peak},
    "itf_183_active_days_126d_pct_of_504d_peak":    {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_183_active_days_126d_pct_of_504d_peak},
    "itf_184_director_buy_63d_pct_of_252d_peak":    {"inputs": ["director_buy_count"],                                        "func": itf_184_director_buy_63d_pct_of_252d_peak},
    "itf_185_buyers_252d_pct_of_504d_peak":         {"inputs": ["insider_buyers"],                                            "func": itf_185_buyers_252d_pct_of_504d_peak},
    "itf_186_txn_ewm5_minus_ewm21":                 {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_186_txn_ewm5_minus_ewm21},
    "itf_187_buy_ewm5_minus_ewm63":                 {"inputs": ["insider_buy_count"],                                         "func": itf_187_buy_ewm5_minus_ewm63},
    "itf_188_txn_ewm21_minus_ewm252":               {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_188_txn_ewm21_minus_ewm252},
    "itf_189_buy_ewm63_minus_ewm252":               {"inputs": ["insider_buy_count"],                                         "func": itf_189_buy_ewm63_minus_ewm252},
    "itf_190_officer_buy_ewm21_minus_ewm252":       {"inputs": ["officer_buy_count"],                                         "func": itf_190_officer_buy_ewm21_minus_ewm252},
    "itf_191_buyers_ewm21_minus_ewm252":            {"inputs": ["insider_buyers"],                                            "func": itf_191_buyers_ewm21_minus_ewm252},
    "itf_192_txn_ewm_ratio_21v63":                  {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_192_txn_ewm_ratio_21v63},
    "itf_193_buy_ewm_ratio_21v252":                 {"inputs": ["insider_buy_count"],                                         "func": itf_193_buy_ewm_ratio_21v252},
    "itf_194_buy_concentration_63in252":            {"inputs": ["insider_buy_count"],                                         "func": itf_194_buy_concentration_63in252},
    "itf_195_surge_flag_5d_2x_252d_rate":           {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_195_surge_flag_5d_2x_252d_rate},
    "itf_196_buy_surge_flag_21d_2x_504d_rate":      {"inputs": ["insider_buy_count"],                                         "func": itf_196_buy_surge_flag_21d_2x_504d_rate},
    "itf_197_txn_count_5d_zscore_252d":             {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_197_txn_count_5d_zscore_252d},
    "itf_198_buy_count_pct_rank_63d":               {"inputs": ["insider_buy_count"],                                         "func": itf_198_buy_count_pct_rank_63d},
    "itf_199_officer_director_buy_density_63d":     {"inputs": ["officer_buy_count", "director_buy_count"],                   "func": itf_199_officer_director_buy_density_63d},
    "itf_200_activity_breadth_score_252d":          {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "insider_sellers"], "func": itf_200_activity_breadth_score_252d},
}
