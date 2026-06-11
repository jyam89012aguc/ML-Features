"""
88_insider_transaction_freq — 2nd-Derivative Features 001-075
Domain: rate of change of base insider-transaction-frequency features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Series Contract
--------------------------------------
Inputs are daily-frequency pandas Series derived from Sharadar SF2 insider
transaction filings, aggregated to one row per (ticker, date).  Most days
carry ZERO — the series are event-driven and are NOT forward-filled.
The 2nd-derivative series produced here are typically very sparse on the
daily index because the underlying activity is episodic — this is correct
and expected.  Rolling sums/counts are used so that the base concepts
have continuous coverage; diffs/slopes of those rolling quantities then
measure how rapidly activity is changing.

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
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _ols_slope(arr: np.ndarray) -> float:
    """OLS slope of arr vs index; returns NaN if n < 2."""
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


# ── Base-concept helpers (self-contained; no cross-file imports) ──────────────

def _total(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return buy + sell


def _cnt21(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_sum(_total(buy, sell), _TD_MO)


def _cnt63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_sum(_total(buy, sell), _TD_QTR)


def _cnt252(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_sum(_total(buy, sell), _TD_YEAR)


def _buy_cnt21(buy: pd.Series) -> pd.Series:
    return _rolling_sum(buy, _TD_MO)


def _buy_cnt63(buy: pd.Series) -> pd.Series:
    return _rolling_sum(buy, _TD_QTR)


def _buy_cnt252(buy: pd.Series) -> pd.Series:
    return _rolling_sum(buy, _TD_YEAR)


def _active_day_density_63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_mean((_total(buy, sell) > 0).astype(float), _TD_QTR)


def _active_day_density_252(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_mean((_total(buy, sell) > 0).astype(float), _TD_YEAR)


def _txn_accel_21v252(buy: pd.Series, sell: pd.Series) -> pd.Series:
    t = _total(buy, sell)
    return _rolling_sum(t, _TD_MO) / _TD_MO - _rolling_sum(t, _TD_YEAR) / _TD_YEAR


def _buy_accel_21v252(buy: pd.Series) -> pd.Series:
    return _rolling_sum(buy, _TD_MO) / _TD_MO - _rolling_sum(buy, _TD_YEAR) / _TD_YEAR


def _buyers_63(buyers: pd.Series) -> pd.Series:
    return _rolling_sum(buyers, _TD_QTR)


def _buyers_252(buyers: pd.Series) -> pd.Series:
    return _rolling_sum(buyers, _TD_YEAR)


def _officer_cnt63(officer_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_count, _TD_QTR)


def _director_cnt63(director_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_count, _TD_QTR)


# ── 2nd-derivative feature functions ─────────────────────────────────────────

def itf_drv2_001_cnt21_diff_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 21-day transaction count lagged 21 days (change in monthly count)."""
    base = _cnt21(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_MO)


def itf_drv2_002_cnt63_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day transaction count lagged 63 days (change in quarterly count)."""
    base = _cnt63(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_003_cnt252_diff_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 252-day transaction count lagged 252 days (YoY change in annual count)."""
    base = _cnt252(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_004_buy_cnt63_diff_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of 63-day buy count lagged 63 days."""
    base = _buy_cnt63(insider_buy_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_005_buy_cnt252_diff_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of 252-day buy count lagged 252 days."""
    base = _buy_cnt252(insider_buy_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_006_active_density_63d_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day active-day density lagged 63 days."""
    base = _active_day_density_63(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_007_active_density_252d_diff_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 252-day active-day density lagged 252 days."""
    base = _active_day_density_252(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_008_txn_accel_21v252_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of txn_accel_21v252 lagged 63 days (change in acceleration signal)."""
    base = _txn_accel_21v252(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_009_buy_accel_21v252_diff_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of buy_accel_21v252 lagged 63 days."""
    base = _buy_accel_21v252(insider_buy_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_010_buyers_63d_diff_63d(insider_buyers: pd.Series) -> pd.Series:
    """Diff of 63-day buyer sum lagged 63 days."""
    base = _buyers_63(insider_buyers)
    return base - base.shift(_TD_QTR)


def itf_drv2_011_buyers_252d_diff_252d(insider_buyers: pd.Series) -> pd.Series:
    """Diff of 252-day buyer sum lagged 252 days."""
    base = _buyers_252(insider_buyers)
    return base - base.shift(_TD_YEAR)


def itf_drv2_012_cnt21_pct_change_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of 21-day count vs prior 21-day count, then diff of that pct change."""
    total   = _total(insider_buy_count, insider_sell_count)
    cnt     = _rolling_sum(total, _TD_MO)
    prior   = cnt.shift(_TD_MO)
    pct_chg = _safe_div(cnt - prior, prior)
    return pct_chg - pct_chg.shift(_TD_MO)


def itf_drv2_013_cnt63_pct_change_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of 63-day count vs prior 63-day count, then diff of that pct change."""
    cnt     = _cnt63(insider_buy_count, insider_sell_count)
    prior   = cnt.shift(_TD_QTR)
    pct_chg = _safe_div(cnt - prior, prior)
    return pct_chg - pct_chg.shift(_TD_QTR)


def itf_drv2_014_officer_cnt63_diff_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Diff of 63-day officer buy count lagged 63 days."""
    base = _officer_cnt63(officer_buy_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_015_director_cnt63_diff_63d(director_buy_count: pd.Series) -> pd.Series:
    """Diff of 63-day director buy count lagged 63 days."""
    base = _director_cnt63(director_buy_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_016_cnt63_slope_252d_diff_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Diff of (OLS slope of 63-day count over 252d window) lagged 252 days.
    Captures acceleration in the trend of quarterly activity.
    """
    cnt63 = _cnt63(insider_buy_count, insider_sell_count)
    slope = cnt63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)
    return slope - slope.shift(_TD_YEAR)


def itf_drv2_017_buy_cnt63_slope_252d_diff_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of (OLS slope of 63-day buy count over 252d window) lagged 252 days."""
    cnt63 = _buy_cnt63(insider_buy_count)
    slope = cnt63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)
    return slope - slope.shift(_TD_YEAR)


def itf_drv2_018_active_density_63d_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day active-day density over 252-day window (trend in regularity)."""
    dens = _active_day_density_63(insider_buy_count, insider_sell_count)
    return dens.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_019_cnt21_ewm_diff_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) of 21-day count minus its own 63-day EWM (MACD of monthly counts)."""
    base    = _cnt21(insider_buy_count, insider_sell_count)
    fast    = _ewm_mean(base, _TD_MO)
    slow    = _ewm_mean(base, _TD_QTR)
    return fast - slow


def itf_drv2_020_buyers_63d_zscore_diff_63d(insider_buyers: pd.Series) -> pd.Series:
    """
    Diff of z-score(buyers_63d within 252d window) lagged 63 days.
    Measures how quickly the relative buyer-count is shifting.
    """
    base  = _buyers_63(insider_buyers)
    m     = _rolling_mean(base, _TD_YEAR)
    sd    = _rolling_std(base, _TD_YEAR)
    z     = _safe_div(base - m, sd)
    return z - z.shift(_TD_QTR)


def itf_drv2_021_txn_accel_21v63_diff_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of txn_accel_21v63 lagged 21 days (change in short acceleration)."""
    total   = _total(insider_buy_count, insider_sell_count)
    r21     = _rolling_sum(total, _TD_MO) / _TD_MO
    r63     = _rolling_sum(total, _TD_QTR) / _TD_QTR
    accel   = r21 - r63
    return accel - accel.shift(_TD_MO)


def itf_drv2_022_surge_ratio_21v252_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Diff of (21d-rate / 252d-rate) lagged 63 days.
    Captures change in how "surgy" recent activity is vs its baseline.
    """
    total    = _total(insider_buy_count, insider_sell_count)
    rate_21  = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_252 = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    ratio    = _safe_div(rate_21, rate_252)
    return ratio - ratio.shift(_TD_QTR)


def itf_drv2_023_buy_cnt21_second_diff(insider_buy_count: pd.Series) -> pd.Series:
    """
    Second finite difference of 21-day buy count (diff of diff, both lagged 21d).
    Measures acceleration / deceleration of buy-count momentum.
    """
    base = _buy_cnt21(insider_buy_count)
    d1   = base - base.shift(_TD_MO)
    d2   = d1 - d1.shift(_TD_MO)
    return d2


def itf_drv2_024_total_cnt63_second_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Second finite difference of 63-day total transaction count (diff of diff, lagged 63d).
    Captures curvature in the quarterly activity trend.
    """
    base = _cnt63(insider_buy_count, insider_sell_count)
    d1   = base - base.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2


def itf_drv2_025_activity_accel_composite_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Diff of the composite-acceleration score (itf_150 concept) lagged 63 days.
    = change in the activity-acceleration composite over the past quarter.
    """
    total     = _total(insider_buy_count, insider_sell_count)
    rate_21   = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_252  = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    accel_txn = rate_21 - rate_252

    brate_21  = _rolling_sum(insider_buyers, _TD_MO) / _TD_MO
    brate_252 = _rolling_sum(insider_buyers, _TD_YEAR) / _TD_YEAR
    accel_buy = brate_21 - brate_252

    any_txn  = (total > 0).astype(float)
    dens_21  = _rolling_mean(any_txn, _TD_MO)
    dens_252 = _rolling_mean(any_txn, _TD_YEAR)
    accel_den = dens_21 - dens_252

    def _z(s: pd.Series) -> pd.Series:
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    composite = (_z(accel_txn) + _z(accel_buy) + _z(accel_den)) / 3.0
    return composite - composite.shift(_TD_QTR)


# ── 2nd-derivative feature functions 026-075 ──────────────────────────────────

# --- Additional base-concept helpers ---

def _sell_cnt63(sell: pd.Series) -> pd.Series:
    return _rolling_sum(sell, _TD_QTR)


def _sell_cnt252(sell: pd.Series) -> pd.Series:
    return _rolling_sum(sell, _TD_YEAR)


def _buy_cnt5(buy: pd.Series) -> pd.Series:
    return _rolling_sum(buy, _TD_WK)


def _cnt5(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_sum(buy + sell, _TD_WK)


def _active_density_21(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_mean(((buy + sell) > 0).astype(float), _TD_MO)


def _burst_intensity_63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    total  = buy + sell
    cnt_63 = _rolling_sum(total, _TD_QTR)
    act_63 = _rolling_sum((total > 0).astype(float), _TD_QTR)
    return cnt_63 / act_63.replace(0, np.nan)


def _officer_cnt252(officer_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(officer_buy_count, _TD_YEAR)


def _director_cnt252(director_buy_count: pd.Series) -> pd.Series:
    return _rolling_sum(director_buy_count, _TD_YEAR)


def _sellers_63(sellers: pd.Series) -> pd.Series:
    return _rolling_sum(sellers, _TD_QTR)


def _net_txn_63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_sum(buy - sell, _TD_QTR)


def _buy_to_sell_ratio_63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return _rolling_sum(buy, _TD_QTR) / _rolling_sum(sell, _TD_QTR).replace(0, np.nan)


def _surge_ratio_5v252(buy: pd.Series, sell: pd.Series) -> pd.Series:
    t = buy + sell
    return (_rolling_sum(t, _TD_WK) / _TD_WK) / (_rolling_sum(t, _TD_YEAR) / _TD_YEAR).replace(0, np.nan)


# --- Group: 2nd derivatives 026-040 (new windows / lag combos for existing concepts) ---

def itf_drv2_026_cnt5_diff_5d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 5-day transaction count lagged 5 days."""
    base = _cnt5(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_WK)


def itf_drv2_027_buy_cnt5_diff_5d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of 5-day buy count lagged 5 days."""
    base = _buy_cnt5(insider_buy_count)
    return base - base.shift(_TD_WK)


def itf_drv2_028_cnt21_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 21-day transaction count lagged 63 days (cross-lag: monthly vs quarterly)."""
    base = _cnt21(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_029_buy_cnt21_diff_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of 21-day buy count lagged 63 days."""
    base = _buy_cnt21(insider_buy_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_030_cnt63_diff_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day transaction count lagged 252 days (QoY change)."""
    base = _cnt63(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_031_sell_cnt63_diff_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day sell count lagged 63 days."""
    base = _sell_cnt63(insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_032_sell_cnt252_diff_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 252-day sell count lagged 252 days."""
    base = _sell_cnt252(insider_sell_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_033_net_txn63_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day net transactions (buys minus sells) lagged 63 days."""
    base = _net_txn_63(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_034_buy_to_sell_ratio_63d_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day buy-to-sell ratio lagged 63 days."""
    base = _buy_to_sell_ratio_63(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_035_active_density_21d_diff_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 21-day active-day density lagged 21 days."""
    base = _active_density_21(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_MO)


def itf_drv2_036_active_density_21d_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 21-day active-day density lagged 63 days."""
    base = _active_density_21(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_037_burst_intensity_63d_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day burst-intensity lagged 63 days."""
    base = _burst_intensity_63(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_QTR)


def itf_drv2_038_officer_cnt252_diff_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Diff of 252-day officer buy count lagged 252 days."""
    base = _officer_cnt252(officer_buy_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_039_director_cnt252_diff_252d(director_buy_count: pd.Series) -> pd.Series:
    """Diff of 252-day director buy count lagged 252 days."""
    base = _director_cnt252(director_buy_count)
    return base - base.shift(_TD_YEAR)


def itf_drv2_040_sellers_63d_diff_63d(insider_sellers: pd.Series) -> pd.Series:
    """Diff of 63-day seller sum lagged 63 days."""
    base = _sellers_63(insider_sellers)
    return base - base.shift(_TD_QTR)


# --- Group: 2nd derivatives 041-055 (rolling slopes of new base concepts) ---

def itf_drv2_041_cnt5_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 5-day transaction count over 63-day window."""
    cnt5 = _cnt5(insider_buy_count, insider_sell_count)
    return cnt5.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_042_buy_cnt5_slope_63d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 5-day buy count over 63-day window."""
    cnt5 = _buy_cnt5(insider_buy_count)
    return cnt5.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_043_sell_cnt63_slope_252d(insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day sell count over 252-day window."""
    cnt63 = _sell_cnt63(insider_sell_count)
    return cnt63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_044_net_txn63_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day net-transaction count over 252-day window."""
    net63 = _net_txn_63(insider_buy_count, insider_sell_count)
    return net63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_045_active_density_21d_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 21-day active-day density over 252-day window."""
    dens = _active_density_21(insider_buy_count, insider_sell_count)
    return dens.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_046_sellers_63d_slope_252d(insider_sellers: pd.Series) -> pd.Series:
    """OLS slope of 63-day seller sum over 252-day window."""
    s63 = _sellers_63(insider_sellers)
    return s63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_047_officer_cnt63_slope_252d(officer_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day officer buy count over 252-day window."""
    cnt63 = _officer_cnt63(officer_buy_count)
    return cnt63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_048_director_cnt63_slope_252d(director_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day director buy count over 252-day window."""
    cnt63 = _director_cnt63(director_buy_count)
    return cnt63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_049_buyers_252d_diff_252d(insider_buyers: pd.Series) -> pd.Series:
    """Diff of 252-day buyer sum lagged 252 days (2-year buyer momentum)."""
    base = _buyers_252(insider_buyers)
    return base - base.shift(_TD_YEAR)


def itf_drv2_050_cnt252_diff_504d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 252-day transaction count lagged 504 days (2-year-over-2-year)."""
    base = _cnt252(insider_buy_count, insider_sell_count)
    return base - base.shift(_TD_2Y)


def itf_drv2_051_active_density_252d_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of 252-day active-day density over 252-day window."""
    dens = _active_day_density_252(insider_buy_count, insider_sell_count)
    return dens.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_052_buy_accel_21v63_diff_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of (buy_rate_21 - buy_rate_63) lagged 63 days."""
    r21  = _rolling_sum(insider_buy_count, _TD_MO) / _TD_MO
    r63  = _rolling_sum(insider_buy_count, _TD_QTR) / _TD_QTR
    base = r21 - r63
    return base - base.shift(_TD_QTR)


def itf_drv2_053_surge_ratio_5v252_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of (5d-rate / 252d-rate) lagged 63 days."""
    ratio = _surge_ratio_5v252(insider_buy_count, insider_sell_count)
    return ratio - ratio.shift(_TD_QTR)


def itf_drv2_054_buyers_63d_slope_252d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of 63-day buyer sum over 252-day window."""
    s63 = _buyers_63(insider_buyers)
    return s63.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_055_txn_cv_63d_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of 63-day CV (std/mean) lagged 63 days (change in burstiness)."""
    total = insider_buy_count + insider_sell_count
    m  = _rolling_mean(total, _TD_QTR)
    s  = _rolling_std(total, _TD_QTR)
    cv = s / m.replace(0, np.nan)
    return cv - cv.shift(_TD_QTR)


# --- Group: 2nd derivatives 056-075 (EWM diffs, pct-change, zscore dynamics) ---

def itf_drv2_056_cnt21_ewm_minus_ewm252_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of (EWM21-EWM252 of total txns) lagged 63 days."""
    total = insider_buy_count + insider_sell_count
    base  = _ewm_mean(total, _TD_MO) - _ewm_mean(total, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def itf_drv2_057_buy_ewm21_minus_ewm63_diff_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of (EWM21-EWM63 of buy count) lagged 21 days."""
    base = _ewm_mean(insider_buy_count, _TD_MO) - _ewm_mean(insider_buy_count, _TD_QTR)
    return base - base.shift(_TD_MO)


def itf_drv2_058_sell_cnt63_pct_change_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of 63-day sell count vs prior 63-day window, then diff."""
    cnt    = _sell_cnt63(insider_sell_count)
    prior  = cnt.shift(_TD_QTR)
    pct    = cnt / prior.replace(0, np.nan) - 1.0
    return pct - pct.shift(_TD_QTR)


def itf_drv2_059_net_txn63_pct_change_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of 63-day net transactions vs prior 63-day window."""
    base  = _net_txn_63(insider_buy_count, insider_sell_count)
    prior = base.shift(_TD_QTR)
    return (base - prior) / prior.abs().replace(0, np.nan)


def itf_drv2_060_active_density_63d_ewm_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(21) of 63-day active-density minus EWM(63) of same (MACD of regularity)."""
    dens = _active_day_density_63(insider_buy_count, insider_sell_count)
    return _ewm_mean(dens, _TD_MO) - _ewm_mean(dens, _TD_QTR)


def itf_drv2_061_buyers_63d_pct_change_252d(insider_buyers: pd.Series) -> pd.Series:
    """Pct change of 63-day buyer sum vs prior 252 days ago."""
    s63   = _buyers_63(insider_buyers)
    prior = s63.shift(_TD_YEAR)
    return (s63 - prior) / prior.replace(0, np.nan)


def itf_drv2_062_cnt63_zscore_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of z-score(63d-count within 252d) lagged 63 days."""
    cnt  = _cnt63(insider_buy_count, insider_sell_count)
    m    = _rolling_mean(cnt, _TD_YEAR)
    sd   = _rolling_std(cnt, _TD_YEAR)
    z    = (cnt - m) / sd.replace(0, np.nan)
    return z - z.shift(_TD_QTR)


def itf_drv2_063_buy_cnt252_diff_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of 252-day buy count lagged 504 days."""
    base = _buy_cnt252(insider_buy_count)
    return base - base.shift(_TD_2Y)


def itf_drv2_064_officer_cnt63_pct_change_252d(officer_buy_count: pd.Series) -> pd.Series:
    """Pct change of 63-day officer buy count vs prior 252 days ago."""
    cnt   = _officer_cnt63(officer_buy_count)
    prior = cnt.shift(_TD_YEAR)
    return (cnt - prior) / prior.replace(0, np.nan)


def itf_drv2_065_director_cnt63_pct_change_252d(director_buy_count: pd.Series) -> pd.Series:
    """Pct change of 63-day director buy count vs prior 252 days ago."""
    cnt   = _director_cnt63(director_buy_count)
    prior = cnt.shift(_TD_YEAR)
    return (cnt - prior) / prior.replace(0, np.nan)


def itf_drv2_066_cnt21_slope_63d_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of (OLS slope of 21-day count over 63d window) lagged 63 days."""
    cnt21 = _cnt21(insider_buy_count, insider_sell_count)
    slope = cnt21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def itf_drv2_067_buy_cnt21_slope_63d_diff_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of (OLS slope of 21-day buy count over 63d window) lagged 63 days."""
    cnt21 = _buy_cnt21(insider_buy_count)
    slope = cnt21.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)
    return slope - slope.shift(_TD_QTR)


def itf_drv2_068_active_density_63d_zscore_diff_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of z-score(63d active-density within 252d) lagged 252 days."""
    dens = _active_day_density_63(insider_buy_count, insider_sell_count)
    m    = _rolling_mean(dens, _TD_YEAR)
    sd   = _rolling_std(dens, _TD_YEAR)
    z    = (dens - m) / sd.replace(0, np.nan)
    return z - z.shift(_TD_YEAR)


def itf_drv2_069_sellers_63d_pct_change_252d(insider_sellers: pd.Series) -> pd.Series:
    """Pct change of 63-day seller sum vs prior 252 days ago."""
    s63   = _sellers_63(insider_sellers)
    prior = s63.shift(_TD_YEAR)
    return (s63 - prior) / prior.replace(0, np.nan)


def itf_drv2_070_txn_accel_21v252_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of txn_accel_21v252 series over 252-day window."""
    accel = _txn_accel_21v252(insider_buy_count, insider_sell_count)
    return accel.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_071_buy_accel_21v252_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of buy_accel_21v252 series over 252-day window."""
    accel = _buy_accel_21v252(insider_buy_count)
    return accel.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv2_072_buyers_63d_diff_252d(insider_buyers: pd.Series) -> pd.Series:
    """Diff of 63-day buyer sum lagged 252 days (year-over-year buyer shift)."""
    base = _buyers_63(insider_buyers)
    return base - base.shift(_TD_YEAR)


def itf_drv2_073_cnt21_second_diff_ewm21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) of second finite difference of 21-day total count."""
    base = _cnt21(insider_buy_count, insider_sell_count)
    d1   = base - base.shift(_TD_MO)
    d2   = d1 - d1.shift(_TD_MO)
    return _ewm_mean(d2, _TD_MO)


def itf_drv2_074_officer_director_cnt63_diff_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Diff of 63-day combined officer+director buy count lagged 63 days."""
    combo = _rolling_sum(officer_buy_count + director_buy_count, _TD_QTR)
    return combo - combo.shift(_TD_QTR)


def itf_drv2_075_composite_accel_diff_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Diff of composite-acceleration score lagged 252 days (YoY change in acceleration).
    """
    total     = insider_buy_count + insider_sell_count
    rate_21   = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_252  = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    accel_txn = rate_21 - rate_252
    brate_21  = _rolling_sum(insider_buyers, _TD_MO) / _TD_MO
    brate_252 = _rolling_sum(insider_buyers, _TD_YEAR) / _TD_YEAR
    accel_buy = brate_21 - brate_252
    any_txn   = (total > 0).astype(float)
    accel_den = _rolling_mean(any_txn, _TD_MO) - _rolling_mean(any_txn, _TD_YEAR)

    def _z(s: pd.Series) -> pd.Series:
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return (s - m) / sd.replace(0, np.nan)

    composite = (_z(accel_txn) + _z(accel_buy) + _z(accel_den)) / 3.0
    return composite - composite.shift(_TD_YEAR)


# ── Registry 2nd Derivatives ──────────────────────────────────────────────────

INSIDER_TRANSACTION_FREQ_REGISTRY_2ND_DERIVATIVES = {
    "itf_drv2_001_cnt21_diff_21d":                   {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_001_cnt21_diff_21d},
    "itf_drv2_002_cnt63_diff_63d":                   {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_002_cnt63_diff_63d},
    "itf_drv2_003_cnt252_diff_252d":                 {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_003_cnt252_diff_252d},
    "itf_drv2_004_buy_cnt63_diff_63d":               {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_004_buy_cnt63_diff_63d},
    "itf_drv2_005_buy_cnt252_diff_252d":             {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_005_buy_cnt252_diff_252d},
    "itf_drv2_006_active_density_63d_diff_63d":      {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_006_active_density_63d_diff_63d},
    "itf_drv2_007_active_density_252d_diff_252d":    {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_007_active_density_252d_diff_252d},
    "itf_drv2_008_txn_accel_21v252_diff_63d":        {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_008_txn_accel_21v252_diff_63d},
    "itf_drv2_009_buy_accel_21v252_diff_63d":        {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_009_buy_accel_21v252_diff_63d},
    "itf_drv2_010_buyers_63d_diff_63d":              {"inputs": ["insider_buyers"],                                               "func": itf_drv2_010_buyers_63d_diff_63d},
    "itf_drv2_011_buyers_252d_diff_252d":            {"inputs": ["insider_buyers"],                                               "func": itf_drv2_011_buyers_252d_diff_252d},
    "itf_drv2_012_cnt21_pct_change_21d":             {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_012_cnt21_pct_change_21d},
    "itf_drv2_013_cnt63_pct_change_63d":             {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_013_cnt63_pct_change_63d},
    "itf_drv2_014_officer_cnt63_diff_63d":           {"inputs": ["officer_buy_count"],                                            "func": itf_drv2_014_officer_cnt63_diff_63d},
    "itf_drv2_015_director_cnt63_diff_63d":          {"inputs": ["director_buy_count"],                                           "func": itf_drv2_015_director_cnt63_diff_63d},
    "itf_drv2_016_cnt63_slope_252d_diff_252d":       {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_016_cnt63_slope_252d_diff_252d},
    "itf_drv2_017_buy_cnt63_slope_252d_diff_252d":   {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_017_buy_cnt63_slope_252d_diff_252d},
    "itf_drv2_018_active_density_63d_slope_252d":    {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_018_active_density_63d_slope_252d},
    "itf_drv2_019_cnt21_ewm_diff_21d":               {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_019_cnt21_ewm_diff_21d},
    "itf_drv2_020_buyers_63d_zscore_diff_63d":       {"inputs": ["insider_buyers"],                                               "func": itf_drv2_020_buyers_63d_zscore_diff_63d},
    "itf_drv2_021_txn_accel_21v63_diff_21d":         {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_021_txn_accel_21v63_diff_21d},
    "itf_drv2_022_surge_ratio_21v252_diff_63d":      {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_022_surge_ratio_21v252_diff_63d},
    "itf_drv2_023_buy_cnt21_second_diff":            {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_023_buy_cnt21_second_diff},
    "itf_drv2_024_total_cnt63_second_diff":          {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_024_total_cnt63_second_diff},
    "itf_drv2_025_activity_accel_composite_diff_63d":{"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"],    "func": itf_drv2_025_activity_accel_composite_diff_63d},
    "itf_drv2_026_cnt5_diff_5d":                      {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_026_cnt5_diff_5d},
    "itf_drv2_027_buy_cnt5_diff_5d":                  {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_027_buy_cnt5_diff_5d},
    "itf_drv2_028_cnt21_diff_63d":                    {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_028_cnt21_diff_63d},
    "itf_drv2_029_buy_cnt21_diff_63d":                {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_029_buy_cnt21_diff_63d},
    "itf_drv2_030_cnt63_diff_252d":                   {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_030_cnt63_diff_252d},
    "itf_drv2_031_sell_cnt63_diff_63d":               {"inputs": ["insider_sell_count"],                                           "func": itf_drv2_031_sell_cnt63_diff_63d},
    "itf_drv2_032_sell_cnt252_diff_252d":             {"inputs": ["insider_sell_count"],                                           "func": itf_drv2_032_sell_cnt252_diff_252d},
    "itf_drv2_033_net_txn63_diff_63d":                {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_033_net_txn63_diff_63d},
    "itf_drv2_034_buy_to_sell_ratio_63d_diff_63d":    {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_034_buy_to_sell_ratio_63d_diff_63d},
    "itf_drv2_035_active_density_21d_diff_21d":       {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_035_active_density_21d_diff_21d},
    "itf_drv2_036_active_density_21d_diff_63d":       {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_036_active_density_21d_diff_63d},
    "itf_drv2_037_burst_intensity_63d_diff_63d":      {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_037_burst_intensity_63d_diff_63d},
    "itf_drv2_038_officer_cnt252_diff_252d":          {"inputs": ["officer_buy_count"],                                            "func": itf_drv2_038_officer_cnt252_diff_252d},
    "itf_drv2_039_director_cnt252_diff_252d":         {"inputs": ["director_buy_count"],                                           "func": itf_drv2_039_director_cnt252_diff_252d},
    "itf_drv2_040_sellers_63d_diff_63d":              {"inputs": ["insider_sellers"],                                              "func": itf_drv2_040_sellers_63d_diff_63d},
    "itf_drv2_041_cnt5_slope_63d":                    {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_041_cnt5_slope_63d},
    "itf_drv2_042_buy_cnt5_slope_63d":                {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_042_buy_cnt5_slope_63d},
    "itf_drv2_043_sell_cnt63_slope_252d":             {"inputs": ["insider_sell_count"],                                           "func": itf_drv2_043_sell_cnt63_slope_252d},
    "itf_drv2_044_net_txn63_slope_252d":              {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_044_net_txn63_slope_252d},
    "itf_drv2_045_active_density_21d_slope_252d":     {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_045_active_density_21d_slope_252d},
    "itf_drv2_046_sellers_63d_slope_252d":            {"inputs": ["insider_sellers"],                                              "func": itf_drv2_046_sellers_63d_slope_252d},
    "itf_drv2_047_officer_cnt63_slope_252d":          {"inputs": ["officer_buy_count"],                                            "func": itf_drv2_047_officer_cnt63_slope_252d},
    "itf_drv2_048_director_cnt63_slope_252d":         {"inputs": ["director_buy_count"],                                           "func": itf_drv2_048_director_cnt63_slope_252d},
    "itf_drv2_049_buyers_252d_diff_252d":             {"inputs": ["insider_buyers"],                                               "func": itf_drv2_049_buyers_252d_diff_252d},
    "itf_drv2_050_cnt252_diff_504d":                  {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_050_cnt252_diff_504d},
    "itf_drv2_051_active_density_252d_slope_252d":    {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_051_active_density_252d_slope_252d},
    "itf_drv2_052_buy_accel_21v63_diff_63d":          {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_052_buy_accel_21v63_diff_63d},
    "itf_drv2_053_surge_ratio_5v252_diff_63d":        {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_053_surge_ratio_5v252_diff_63d},
    "itf_drv2_054_buyers_63d_slope_252d":             {"inputs": ["insider_buyers"],                                               "func": itf_drv2_054_buyers_63d_slope_252d},
    "itf_drv2_055_txn_cv_63d_diff_63d":               {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_055_txn_cv_63d_diff_63d},
    "itf_drv2_056_cnt21_ewm_minus_ewm252_diff_63d":   {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_056_cnt21_ewm_minus_ewm252_diff_63d},
    "itf_drv2_057_buy_ewm21_minus_ewm63_diff_21d":    {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_057_buy_ewm21_minus_ewm63_diff_21d},
    "itf_drv2_058_sell_cnt63_pct_change_63d":         {"inputs": ["insider_sell_count"],                                           "func": itf_drv2_058_sell_cnt63_pct_change_63d},
    "itf_drv2_059_net_txn63_pct_change_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_059_net_txn63_pct_change_63d},
    "itf_drv2_060_active_density_63d_ewm_diff":       {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_060_active_density_63d_ewm_diff},
    "itf_drv2_061_buyers_63d_pct_change_252d":        {"inputs": ["insider_buyers"],                                               "func": itf_drv2_061_buyers_63d_pct_change_252d},
    "itf_drv2_062_cnt63_zscore_diff_63d":             {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_062_cnt63_zscore_diff_63d},
    "itf_drv2_063_buy_cnt252_diff_504d":              {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_063_buy_cnt252_diff_504d},
    "itf_drv2_064_officer_cnt63_pct_change_252d":     {"inputs": ["officer_buy_count"],                                            "func": itf_drv2_064_officer_cnt63_pct_change_252d},
    "itf_drv2_065_director_cnt63_pct_change_252d":    {"inputs": ["director_buy_count"],                                           "func": itf_drv2_065_director_cnt63_pct_change_252d},
    "itf_drv2_066_cnt21_slope_63d_diff_63d":          {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_066_cnt21_slope_63d_diff_63d},
    "itf_drv2_067_buy_cnt21_slope_63d_diff_63d":      {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_067_buy_cnt21_slope_63d_diff_63d},
    "itf_drv2_068_active_density_63d_zscore_diff_252d":{"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv2_068_active_density_63d_zscore_diff_252d},
    "itf_drv2_069_sellers_63d_pct_change_252d":       {"inputs": ["insider_sellers"],                                              "func": itf_drv2_069_sellers_63d_pct_change_252d},
    "itf_drv2_070_txn_accel_21v252_slope_252d":       {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_070_txn_accel_21v252_slope_252d},
    "itf_drv2_071_buy_accel_21v252_slope_252d":       {"inputs": ["insider_buy_count"],                                            "func": itf_drv2_071_buy_accel_21v252_slope_252d},
    "itf_drv2_072_buyers_63d_diff_252d":              {"inputs": ["insider_buyers"],                                               "func": itf_drv2_072_buyers_63d_diff_252d},
    "itf_drv2_073_cnt21_second_diff_ewm21":           {"inputs": ["insider_buy_count", "insider_sell_count"],                      "func": itf_drv2_073_cnt21_second_diff_ewm21},
    "itf_drv2_074_officer_director_cnt63_diff_63d":   {"inputs": ["officer_buy_count", "director_buy_count"],                      "func": itf_drv2_074_officer_director_cnt63_diff_63d},
    "itf_drv2_075_composite_accel_diff_252d":         {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"],    "func": itf_drv2_075_composite_accel_diff_252d},
}
