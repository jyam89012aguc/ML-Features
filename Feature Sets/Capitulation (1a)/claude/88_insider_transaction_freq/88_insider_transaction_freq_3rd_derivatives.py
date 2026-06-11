"""
88_insider_transaction_freq — 3rd-Derivative Features 001-075
Domain: rate of change of 2nd-derivative insider-transaction-frequency features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Series Contract
--------------------------------------
Inputs are daily-frequency pandas Series derived from Sharadar SF2 insider
transaction filings, aggregated to one row per (ticker, date).  Most days
carry ZERO — the series are event-driven and are NOT forward-filled.
3rd-derivative features differentiate or take slopes of the 2nd-derivative
concepts, producing highly sparse signals on the daily index — this is
correct and expected.  These features capture changes in the rate-of-change
of acceleration, i.e. the "jerk" in insider activity dynamics.

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


# ── 2nd-derivative concept helpers (self-contained; no cross-file imports) ────

def _total(buy: pd.Series, sell: pd.Series) -> pd.Series:
    return buy + sell


def _cnt21_diff21(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 21-day count lagged 21 days."""
    base = _rolling_sum(_total(buy, sell), _TD_MO)
    return base - base.shift(_TD_MO)


def _cnt63_diff63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day count lagged 63 days."""
    base = _rolling_sum(_total(buy, sell), _TD_QTR)
    return base - base.shift(_TD_QTR)


def _buy_cnt63_diff63(buy: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day buy count lagged 63 days."""
    base = _rolling_sum(buy, _TD_QTR)
    return base - base.shift(_TD_QTR)


def _active_density_63_diff63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day active-day density lagged 63 days."""
    base = _rolling_mean((_total(buy, sell) > 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_QTR)


def _txn_accel_21v252_diff63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of txn_accel_21v252 lagged 63 days."""
    t   = _total(buy, sell)
    acc = _rolling_sum(t, _TD_MO) / _TD_MO - _rolling_sum(t, _TD_YEAR) / _TD_YEAR
    return acc - acc.shift(_TD_QTR)


def _buy_accel_21v252_diff63(buy: pd.Series) -> pd.Series:
    """2nd-derivative: diff of buy_accel_21v252 lagged 63 days."""
    acc = _rolling_sum(buy, _TD_MO) / _TD_MO - _rolling_sum(buy, _TD_YEAR) / _TD_YEAR
    return acc - acc.shift(_TD_QTR)


def _buyers_63_diff63(buyers: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day buyer sum lagged 63 days."""
    base = _rolling_sum(buyers, _TD_QTR)
    return base - base.shift(_TD_QTR)


def _buy_cnt21_second_diff(buy: pd.Series) -> pd.Series:
    """2nd-derivative: second diff of 21-day buy count."""
    base = _rolling_sum(buy, _TD_MO)
    d1   = base - base.shift(_TD_MO)
    return d1 - d1.shift(_TD_MO)


def _cnt63_second_diff(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: second diff of 63-day total count."""
    base = _rolling_sum(_total(buy, sell), _TD_QTR)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _surge_ratio_diff63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of (21d-rate / 252d-rate) lagged 63 days."""
    t       = _total(buy, sell)
    r21     = _rolling_sum(t, _TD_MO) / _TD_MO
    r252    = _rolling_sum(t, _TD_YEAR) / _TD_YEAR
    ratio   = _safe_div(r21, r252)
    return ratio - ratio.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def itf_drv3_001_cnt21_diff21_diff21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (21d-count diff 21d) lagged another 21 days."""
    d2 = _cnt21_diff21(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_MO)


def itf_drv3_002_cnt63_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (63d-count diff 63d) lagged another 63 days."""
    d2 = _cnt63_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_003_buy_cnt63_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """3rd diff: change in (63d-buy-count diff 63d) lagged another 63 days."""
    d2 = _buy_cnt63_diff63(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_004_active_density_63d_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (63d active-density diff) lagged another 63 days."""
    d2 = _active_density_63_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_005_txn_accel_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (txn_accel_21v252 diff 63d) lagged another 63 days."""
    d2 = _txn_accel_21v252_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_006_buy_accel_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """3rd diff: change in (buy_accel_21v252 diff 63d) lagged another 63 days."""
    d2 = _buy_accel_21v252_diff63(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_007_buyers_63_diff63_diff63(insider_buyers: pd.Series) -> pd.Series:
    """3rd diff: change in (buyers_63 diff 63d) lagged another 63 days."""
    d2 = _buyers_63_diff63(insider_buyers)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_008_buy_cnt21_third_diff(insider_buy_count: pd.Series) -> pd.Series:
    """Third finite difference of 21-day buy count (jerk in buy momentum)."""
    d2 = _buy_cnt21_second_diff(insider_buy_count)
    return d2 - d2.shift(_TD_MO)


def itf_drv3_009_cnt63_third_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Third finite difference of 63-day total count (jerk in quarterly activity)."""
    d2 = _cnt63_second_diff(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_010_cnt21_diff21_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (21d-count diff 21d) over 252-day window."""
    d2 = _cnt21_diff21(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_011_cnt63_diff63_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (63d-count diff 63d) over 252-day window."""
    d2 = _cnt63_diff63(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_012_buy_cnt63_diff63_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of (63d-buy-count diff 63d) over 252-day window."""
    d2 = _buy_cnt63_diff63(insider_buy_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_013_txn_accel_diff63_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (txn_accel_21v252 diff 63d) over 252-day window."""
    d2 = _txn_accel_21v252_diff63(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_014_surge_ratio_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff of surge-ratio: change in (surge_ratio diff 63d) lagged another 63 days."""
    d2 = _surge_ratio_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_015_cnt21_diff21_ewm_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) of 2nd-derivative (cnt21_diff21) minus its 63-day EWM."""
    d2   = _cnt21_diff21(insider_buy_count, insider_sell_count)
    fast = _ewm_mean(d2, _TD_MO)
    slow = _ewm_mean(d2, _TD_QTR)
    return fast - slow


def itf_drv3_016_buyers_63_diff63_slope_252d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of (buyers_63 diff 63d) over 252-day window."""
    d2 = _buyers_63_diff63(insider_buyers)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_017_cnt21_diff21_pct_change_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of (cnt21_diff21) lagged 21 days."""
    d2    = _cnt21_diff21(insider_buy_count, insider_sell_count)
    prior = d2.shift(_TD_MO)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_018_cnt63_diff63_pct_change_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of (cnt63_diff63) lagged 63 days."""
    d2    = _cnt63_diff63(insider_buy_count, insider_sell_count)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_019_active_density_63d_diff63_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (active_density_63 diff 63d) over 252-day window."""
    d2 = _active_density_63_diff63(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_020_buy_accel_diff63_pct_change_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Pct change of (buy_accel_21v252 diff 63d) lagged 63 days."""
    d2    = _buy_accel_21v252_diff63(insider_buy_count)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_021_cnt21_third_diff_ewm(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) of third finite difference of 21-day total count."""
    total = _total(insider_buy_count, insider_sell_count)
    base  = _rolling_sum(total, _TD_MO)
    d1    = base - base.shift(_TD_MO)
    d2    = d1 - d1.shift(_TD_MO)
    d3    = d2 - d2.shift(_TD_MO)
    return _ewm_mean(d3, _TD_MO)


def itf_drv3_022_buy_cnt63_diff63_zscore_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of (63d-buy-count diff 63d) within a 252-day window."""
    d2 = _buy_cnt63_diff63(insider_buy_count)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def itf_drv3_023_txn_jerk_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Jerk in total transactions: 3rd-order finite diff at 21-day step.
    d3 = d2 - d2.shift(21), where d2 = d1 - d1.shift(21), d1 = cnt21 - cnt21.shift(21).
    """
    total = _total(insider_buy_count, insider_sell_count)
    base  = _rolling_sum(total, _TD_MO)
    d1    = base - base.shift(_TD_MO)
    d2    = d1 - d1.shift(_TD_MO)
    return d2 - d2.shift(_TD_MO)


def itf_drv3_024_surge_ratio_third_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Third diff of surge_ratio (21d/252d rate ratio), each diff lagged 63d."""
    t      = _total(insider_buy_count, insider_sell_count)
    r21    = _rolling_sum(t, _TD_MO) / _TD_MO
    r252   = _rolling_sum(t, _TD_YEAR) / _TD_YEAR
    ratio  = _safe_div(r21, r252)
    d1     = ratio - ratio.shift(_TD_QTR)
    d2     = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_025_composite_jerk(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Composite jerk score: third-order change in the activity-acceleration composite.
    Equally weights jerk in (txn_accel_21v252, buy_accel_21v252, active_density_diff).
    """
    total     = _total(insider_buy_count, insider_sell_count)
    rate_21   = _rolling_sum(total, _TD_MO) / _TD_MO
    rate_252  = _rolling_sum(total, _TD_YEAR) / _TD_YEAR
    accel_txn = rate_21 - rate_252

    brate_21  = _rolling_sum(insider_buyers, _TD_MO) / _TD_MO
    brate_252 = _rolling_sum(insider_buyers, _TD_YEAR) / _TD_YEAR
    accel_buy = brate_21 - brate_252

    any_txn   = (total > 0).astype(float)
    dens_21   = _rolling_mean(any_txn, _TD_MO)
    dens_252  = _rolling_mean(any_txn, _TD_YEAR)
    accel_den = dens_21 - dens_252

    def _jerk3(s: pd.Series, lag: int) -> pd.Series:
        d1 = s - s.shift(lag)
        d2 = d1 - d1.shift(lag)
        return d2 - d2.shift(lag)

    j1 = _jerk3(accel_txn, _TD_QTR)
    j2 = _jerk3(accel_buy, _TD_QTR)
    j3 = _jerk3(accel_den, _TD_QTR)
    return (j1 + j2 + j3) / 3.0


# ── 3rd-derivative helpers (additional 2nd-derivative concepts) ───────────────

def _sell_cnt63_diff63(sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day sell count lagged 63 days."""
    base = _rolling_sum(sell, _TD_QTR)
    return base - base.shift(_TD_QTR)


def _net_txn63_diff63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day net txns lagged 63 days."""
    base = _rolling_sum(buy - sell, _TD_QTR)
    return base - base.shift(_TD_QTR)


def _active_density_21_diff21(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 21-day active-day density lagged 21 days."""
    base = _rolling_mean(((buy + sell) > 0).astype(float), _TD_MO)
    return base - base.shift(_TD_MO)


def _active_density_21_diff63(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 21-day active-day density lagged 63 days."""
    base = _rolling_mean(((buy + sell) > 0).astype(float), _TD_MO)
    return base - base.shift(_TD_QTR)


def _buy_accel_21v63_diff63(buy: pd.Series) -> pd.Series:
    """2nd-derivative: diff of (buy_rate_21 - buy_rate_63) lagged 63 days."""
    r21  = _rolling_sum(buy, _TD_MO) / _TD_MO
    r63  = _rolling_sum(buy, _TD_QTR) / _TD_QTR
    base = r21 - r63
    return base - base.shift(_TD_QTR)


def _cnt5_diff5(buy: pd.Series, sell: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 5-day total count lagged 5 days."""
    base = _rolling_sum(buy + sell, _TD_WK)
    return base - base.shift(_TD_WK)


def _sellers_63_diff63(sellers: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 63-day seller sum lagged 63 days."""
    base = _rolling_sum(sellers, _TD_QTR)
    return base - base.shift(_TD_QTR)


def _officer_cnt252_diff252(officer_buy_count: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 252-day officer buy count lagged 252 days."""
    base = _rolling_sum(officer_buy_count, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def _director_cnt252_diff252(director_buy_count: pd.Series) -> pd.Series:
    """2nd-derivative: diff of 252-day director buy count lagged 252 days."""
    base = _rolling_sum(director_buy_count, _TD_YEAR)
    return base - base.shift(_TD_YEAR)


# ── 3rd-derivative feature functions 026-075 ──────────────────────────────────

# --- Group: 3rd diffs of new 2nd-derivative concepts (026-040) ---

def itf_drv3_026_sell_cnt63_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (63d-sell-count diff 63d) lagged another 63 days."""
    d2 = _sell_cnt63_diff63(insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_027_net_txn63_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (63d-net-txn diff 63d) lagged another 63 days."""
    d2 = _net_txn63_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_028_active_density_21_diff21_diff21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (21d-active-density diff 21d) lagged another 21 days."""
    d2 = _active_density_21_diff21(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_MO)


def itf_drv3_029_active_density_21_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (21d-active-density diff 63d) lagged another 63 days."""
    d2 = _active_density_21_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_030_buy_accel_21v63_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """3rd diff: change in (buy_accel_21v63 diff 63d) lagged another 63 days."""
    d2 = _buy_accel_21v63_diff63(insider_buy_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_031_cnt5_diff5_diff5(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """3rd diff: change in (5d-count diff 5d) lagged another 5 days."""
    d2 = _cnt5_diff5(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_WK)


def itf_drv3_032_sellers_63_diff63_diff63(insider_sellers: pd.Series) -> pd.Series:
    """3rd diff: change in (sellers_63 diff 63d) lagged another 63 days."""
    d2 = _sellers_63_diff63(insider_sellers)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_033_officer_cnt252_diff252_diff252(officer_buy_count: pd.Series) -> pd.Series:
    """3rd diff: change in (officer_cnt252 diff 252d) lagged another 252 days."""
    d2 = _officer_cnt252_diff252(officer_buy_count)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_034_director_cnt252_diff252_diff252(director_buy_count: pd.Series) -> pd.Series:
    """3rd diff: change in (director_cnt252 diff 252d) lagged another 252 days."""
    d2 = _director_cnt252_diff252(director_buy_count)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_035_buy_cnt63_diff63_pct_change_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Pct change of (63d-buy-count diff 63d) lagged 63 days."""
    d2    = _buy_cnt63_diff63(insider_buy_count)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs())


# --- Group: OLS slopes of 2nd-derivative concepts (036-048) ---

def itf_drv3_036_sell_cnt63_diff63_slope_252d(insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (63d-sell-count diff 63d) over 252-day window."""
    d2 = _sell_cnt63_diff63(insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_037_net_txn63_diff63_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (63d-net-txn diff 63d) over 252-day window."""
    d2 = _net_txn63_diff63(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_038_active_density_21_diff21_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (21d-active-density diff 21d) over 252-day window."""
    d2 = _active_density_21_diff21(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_039_buy_accel_21v63_diff63_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of (buy_accel_21v63 diff 63d) over 252-day window."""
    d2 = _buy_accel_21v63_diff63(insider_buy_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_040_sellers_63_diff63_slope_252d(insider_sellers: pd.Series) -> pd.Series:
    """OLS slope of (sellers_63 diff 63d) over 252-day window."""
    d2 = _sellers_63_diff63(insider_sellers)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_041_cnt5_diff5_slope_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (5d-count diff 5d) over 63-day window."""
    d2 = _cnt5_diff5(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_042_buy_cnt63_diff63_ewm_diff(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=63) of (63d-buy-count diff 63d)."""
    d2 = _buy_cnt63_diff63(insider_buy_count)
    return _ewm_mean(d2, _TD_MO) - _ewm_mean(d2, _TD_QTR)


def itf_drv3_043_cnt21_diff21_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of (21d-count diff 21d) within 252-day window."""
    d2 = _cnt21_diff21(insider_buy_count, insider_sell_count)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def itf_drv3_044_active_density_63_diff63_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of (63d-active-density diff 63d) within 252-day window."""
    d2 = _active_density_63_diff63(insider_buy_count, insider_sell_count)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def itf_drv3_045_txn_accel_diff63_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of (txn_accel_21v252 diff 63d) within 252-day window."""
    d2 = _txn_accel_21v252_diff63(insider_buy_count, insider_sell_count)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def itf_drv3_046_buyers_63_diff63_zscore_252d(insider_buyers: pd.Series) -> pd.Series:
    """Z-score of (buyers_63 diff 63d) within 252-day window."""
    d2 = _buyers_63_diff63(insider_buyers)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def itf_drv3_047_sell_cnt63_diff63_zscore_252d(insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of (63d-sell-count diff 63d) within 252-day window."""
    d2 = _sell_cnt63_diff63(insider_sell_count)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


def itf_drv3_048_net_txn63_diff63_zscore_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of (63d-net-txn diff 63d) within 252-day window."""
    d2 = _net_txn63_diff63(insider_buy_count, insider_sell_count)
    m  = _rolling_mean(d2, _TD_YEAR)
    sd = _rolling_std(d2, _TD_YEAR)
    return _safe_div(d2 - m, sd)


# --- Group: pct-change and EWM dynamics on 2nd-derivative signals (049-063) ---

def itf_drv3_049_sell_cnt63_diff63_pct_change_63d(insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of (63d-sell-count diff 63d) lagged 63 days."""
    d2    = _sell_cnt63_diff63(insider_sell_count)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_050_net_txn63_diff63_pct_change_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of (63d-net-txn diff 63d) lagged 63 days."""
    d2    = _net_txn63_diff63(insider_buy_count, insider_sell_count)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_051_active_density_21_diff21_pct_change_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Pct change of (21d-active-density diff 21d) lagged 21 days."""
    d2    = _active_density_21_diff21(insider_buy_count, insider_sell_count)
    prior = d2.shift(_TD_MO)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_052_sellers_63_diff63_pct_change_63d(insider_sellers: pd.Series) -> pd.Series:
    """Pct change of (sellers_63 diff 63d) lagged 63 days."""
    d2    = _sellers_63_diff63(insider_sellers)
    prior = d2.shift(_TD_QTR)
    return _safe_div(d2 - prior, prior.abs())


def itf_drv3_053_cnt21_diff21_ewm_diff_21d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of EWM(span=21) of (cnt21_diff21) lagged 21 days."""
    d2   = _cnt21_diff21(insider_buy_count, insider_sell_count)
    fast = _ewm_mean(d2, _TD_MO)
    return fast - fast.shift(_TD_MO)


def itf_drv3_054_cnt63_diff63_ewm_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of EWM(span=21) of (cnt63_diff63) lagged 63 days."""
    d2   = _cnt63_diff63(insider_buy_count, insider_sell_count)
    ema  = _ewm_mean(d2, _TD_MO)
    return ema - ema.shift(_TD_QTR)


def itf_drv3_055_buy_cnt63_diff63_ewm_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of EWM(span=21) of (63d-buy-count diff 63d) over 252-day window."""
    d2  = _buy_cnt63_diff63(insider_buy_count)
    ema = _ewm_mean(d2, _TD_MO)
    return ema.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_056_buyers_63_diff63_ewm_diff_63d(insider_buyers: pd.Series) -> pd.Series:
    """Diff of EWM(span=21) of (buyers_63 diff 63d) lagged 63 days."""
    d2  = _buyers_63_diff63(insider_buyers)
    ema = _ewm_mean(d2, _TD_MO)
    return ema - ema.shift(_TD_QTR)


def itf_drv3_057_txn_accel_diff63_ewm_diff_63d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of EWM(span=21) of (txn_accel_21v252 diff 63d) lagged 63 days."""
    d2  = _txn_accel_21v252_diff63(insider_buy_count, insider_sell_count)
    ema = _ewm_mean(d2, _TD_MO)
    return ema - ema.shift(_TD_QTR)


def itf_drv3_058_buy_accel_diff63_ewm_diff_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of EWM(span=21) of (buy_accel_21v252 diff 63d) lagged 63 days."""
    d2  = _buy_accel_21v252_diff63(insider_buy_count)
    ema = _ewm_mean(d2, _TD_MO)
    return ema - ema.shift(_TD_QTR)


# --- Group: composite / combined 3rd-order signals (059-075) ---

def itf_drv3_059_cnt63_third_diff_ewm(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) of third finite difference of 63-day total count."""
    base = _rolling_sum(insider_buy_count + insider_sell_count, _TD_QTR)
    d1   = base - base.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    d3   = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_MO)


def itf_drv3_060_sell_cnt63_third_diff(insider_sell_count: pd.Series) -> pd.Series:
    """Third finite difference of 63-day sell count, each diff lagged 63 days."""
    base = _rolling_sum(insider_sell_count, _TD_QTR)
    d1   = base - base.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_061_net_txn63_third_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Third finite difference of 63-day net-transaction count, each diff lagged 63 days."""
    base = _rolling_sum(insider_buy_count - insider_sell_count, _TD_QTR)
    d1   = base - base.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_062_buyers_63_third_diff(insider_buyers: pd.Series) -> pd.Series:
    """Third finite difference of 63-day buyer sum, each diff lagged 63 days."""
    base = _rolling_sum(insider_buyers, _TD_QTR)
    d1   = base - base.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_063_surge_ratio_diff63_slope_252d(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of (surge_ratio diff 63d) over 252-day window."""
    d2 = _surge_ratio_diff63(insider_buy_count, insider_sell_count)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_064_buy_cnt21_third_diff_ewm(insider_buy_count: pd.Series) -> pd.Series:
    """EWM(span=21) of third finite difference of 21-day buy count."""
    d2 = _buy_cnt21_second_diff(insider_buy_count)
    d3 = d2 - d2.shift(_TD_MO)
    return _ewm_mean(d3, _TD_MO)


def itf_drv3_065_active_density_63_diff63_ewm_diff(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=63) of (63d-active-density diff 63d)."""
    d2 = _active_density_63_diff63(insider_buy_count, insider_sell_count)
    return _ewm_mean(d2, _TD_MO) - _ewm_mean(d2, _TD_QTR)


def itf_drv3_066_buy_cnt63_second_diff_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of second diff of 63-day buy count over 252-day window."""
    cnt  = _rolling_sum(insider_buy_count, _TD_QTR)
    d1   = cnt - cnt.shift(_TD_QTR)
    d2   = d1 - d1.shift(_TD_QTR)
    return d2.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(_ols_slope, raw=True)


def itf_drv3_067_buyers_63_second_diff(insider_buyers: pd.Series) -> pd.Series:
    """Second finite difference of 63-day buyer sum, each diff lagged 63 days."""
    base = _rolling_sum(insider_buyers, _TD_QTR)
    d1   = base - base.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def itf_drv3_068_txn_accel_diff63_diff252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of (txn_accel_21v252 diff 63d) lagged 252 days (cross-lag jerk)."""
    d2 = _txn_accel_21v252_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_069_buy_accel_diff63_diff252(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of (buy_accel_21v252 diff 63d) lagged 252 days (YoY jerk)."""
    d2 = _buy_accel_21v252_diff63(insider_buy_count)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_070_cnt21_diff21_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of (cnt21_diff21) lagged 63 days (cross-lag: monthly jerk vs quarter)."""
    d2 = _cnt21_diff21(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_QTR)


def itf_drv3_071_sellers_63_diff63_ewm_diff(insider_sellers: pd.Series) -> pd.Series:
    """EWM(span=21) minus EWM(span=63) of (sellers_63 diff 63d)."""
    d2 = _sellers_63_diff63(insider_sellers)
    return _ewm_mean(d2, _TD_MO) - _ewm_mean(d2, _TD_QTR)


def itf_drv3_072_cnt63_diff63_diff252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Diff of (cnt63_diff63) lagged 252 days (YoY change in quarterly jerk)."""
    d2 = _cnt63_diff63(insider_buy_count, insider_sell_count)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_073_buy_cnt63_diff63_diff252(insider_buy_count: pd.Series) -> pd.Series:
    """Diff of (buy_cnt63_diff63) lagged 252 days."""
    d2 = _buy_cnt63_diff63(insider_buy_count)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_074_buyers_63_diff63_diff252(insider_buyers: pd.Series) -> pd.Series:
    """Diff of (buyers_63_diff63) lagged 252 days."""
    d2 = _buyers_63_diff63(insider_buyers)
    return d2 - d2.shift(_TD_YEAR)


def itf_drv3_075_composite_jerk_score_yoy(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Composite jerk score YoY: equally weighted sum of YoY diffs of three 2nd-derivative signals:
    (cnt63_diff63, buy_accel_21v252_diff63, buyers_63_diff63).
    Captures whether the jerk itself has accelerated over the past year.
    """
    d_cnt63  = _cnt63_diff63(insider_buy_count, insider_sell_count)
    d_accel  = _buy_accel_21v252_diff63(insider_buy_count)
    d_buyers = _buyers_63_diff63(insider_buyers)

    def _z(s: pd.Series) -> pd.Series:
        m  = _rolling_mean(s, _TD_YEAR)
        sd = _rolling_std(s, _TD_YEAR)
        return _safe_div(s - m, sd)

    yoy_cnt63  = _z(d_cnt63)  - _z(d_cnt63).shift(_TD_YEAR)
    yoy_accel  = _z(d_accel)  - _z(d_accel).shift(_TD_YEAR)
    yoy_buyers = _z(d_buyers) - _z(d_buyers).shift(_TD_YEAR)
    return (yoy_cnt63 + yoy_accel + yoy_buyers) / 3.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

INSIDER_TRANSACTION_FREQ_REGISTRY_3RD_DERIVATIVES = {
    "itf_drv3_001_cnt21_diff21_diff21":              {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_001_cnt21_diff21_diff21},
    "itf_drv3_002_cnt63_diff63_diff63":              {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_002_cnt63_diff63_diff63},
    "itf_drv3_003_buy_cnt63_diff63_diff63":          {"inputs": ["insider_buy_count"],                                         "func": itf_drv3_003_buy_cnt63_diff63_diff63},
    "itf_drv3_004_active_density_63d_diff63_diff63": {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_004_active_density_63d_diff63_diff63},
    "itf_drv3_005_txn_accel_diff63_diff63":          {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_005_txn_accel_diff63_diff63},
    "itf_drv3_006_buy_accel_diff63_diff63":          {"inputs": ["insider_buy_count"],                                         "func": itf_drv3_006_buy_accel_diff63_diff63},
    "itf_drv3_007_buyers_63_diff63_diff63":          {"inputs": ["insider_buyers"],                                            "func": itf_drv3_007_buyers_63_diff63_diff63},
    "itf_drv3_008_buy_cnt21_third_diff":             {"inputs": ["insider_buy_count"],                                         "func": itf_drv3_008_buy_cnt21_third_diff},
    "itf_drv3_009_cnt63_third_diff":                 {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_009_cnt63_third_diff},
    "itf_drv3_010_cnt21_diff21_slope_252d":          {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_010_cnt21_diff21_slope_252d},
    "itf_drv3_011_cnt63_diff63_slope_252d":          {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_011_cnt63_diff63_slope_252d},
    "itf_drv3_012_buy_cnt63_diff63_slope_252d":      {"inputs": ["insider_buy_count"],                                         "func": itf_drv3_012_buy_cnt63_diff63_slope_252d},
    "itf_drv3_013_txn_accel_diff63_slope_252d":      {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_013_txn_accel_diff63_slope_252d},
    "itf_drv3_014_surge_ratio_diff63_diff63":        {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_014_surge_ratio_diff63_diff63},
    "itf_drv3_015_cnt21_diff21_ewm_diff":            {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_015_cnt21_diff21_ewm_diff},
    "itf_drv3_016_buyers_63_diff63_slope_252d":      {"inputs": ["insider_buyers"],                                            "func": itf_drv3_016_buyers_63_diff63_slope_252d},
    "itf_drv3_017_cnt21_diff21_pct_change_21d":      {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_017_cnt21_diff21_pct_change_21d},
    "itf_drv3_018_cnt63_diff63_pct_change_63d":      {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_018_cnt63_diff63_pct_change_63d},
    "itf_drv3_019_active_density_63d_diff63_slope_252d": {"inputs": ["insider_buy_count", "insider_sell_count"],               "func": itf_drv3_019_active_density_63d_diff63_slope_252d},
    "itf_drv3_020_buy_accel_diff63_pct_change_63d":  {"inputs": ["insider_buy_count"],                                         "func": itf_drv3_020_buy_accel_diff63_pct_change_63d},
    "itf_drv3_021_cnt21_third_diff_ewm":             {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_021_cnt21_third_diff_ewm},
    "itf_drv3_022_buy_cnt63_diff63_zscore_252d":     {"inputs": ["insider_buy_count"],                                         "func": itf_drv3_022_buy_cnt63_diff63_zscore_252d},
    "itf_drv3_023_txn_jerk_21d":                     {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_023_txn_jerk_21d},
    "itf_drv3_024_surge_ratio_third_diff":           {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": itf_drv3_024_surge_ratio_third_diff},
    "itf_drv3_025_composite_jerk":                        {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"],  "func": itf_drv3_025_composite_jerk},
    "itf_drv3_026_sell_cnt63_diff63_diff63":              {"inputs": ["insider_sell_count"],                                          "func": itf_drv3_026_sell_cnt63_diff63_diff63},
    "itf_drv3_027_net_txn63_diff63_diff63":               {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_027_net_txn63_diff63_diff63},
    "itf_drv3_028_active_density_21_diff21_diff21":       {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_028_active_density_21_diff21_diff21},
    "itf_drv3_029_active_density_21_diff63_diff63":       {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_029_active_density_21_diff63_diff63},
    "itf_drv3_030_buy_accel_21v63_diff63_diff63":         {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_030_buy_accel_21v63_diff63_diff63},
    "itf_drv3_031_cnt5_diff5_diff5":                      {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_031_cnt5_diff5_diff5},
    "itf_drv3_032_sellers_63_diff63_diff63":              {"inputs": ["insider_sellers"],                                             "func": itf_drv3_032_sellers_63_diff63_diff63},
    "itf_drv3_033_officer_cnt252_diff252_diff252":        {"inputs": ["officer_buy_count"],                                           "func": itf_drv3_033_officer_cnt252_diff252_diff252},
    "itf_drv3_034_director_cnt252_diff252_diff252":       {"inputs": ["director_buy_count"],                                          "func": itf_drv3_034_director_cnt252_diff252_diff252},
    "itf_drv3_035_buy_cnt63_diff63_pct_change_63d":       {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_035_buy_cnt63_diff63_pct_change_63d},
    "itf_drv3_036_sell_cnt63_diff63_slope_252d":          {"inputs": ["insider_sell_count"],                                          "func": itf_drv3_036_sell_cnt63_diff63_slope_252d},
    "itf_drv3_037_net_txn63_diff63_slope_252d":           {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_037_net_txn63_diff63_slope_252d},
    "itf_drv3_038_active_density_21_diff21_slope_252d":   {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_038_active_density_21_diff21_slope_252d},
    "itf_drv3_039_buy_accel_21v63_diff63_slope_252d":     {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_039_buy_accel_21v63_diff63_slope_252d},
    "itf_drv3_040_sellers_63_diff63_slope_252d":          {"inputs": ["insider_sellers"],                                             "func": itf_drv3_040_sellers_63_diff63_slope_252d},
    "itf_drv3_041_cnt5_diff5_slope_63d":                  {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_041_cnt5_diff5_slope_63d},
    "itf_drv3_042_buy_cnt63_diff63_ewm_diff":             {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_042_buy_cnt63_diff63_ewm_diff},
    "itf_drv3_043_cnt21_diff21_zscore_252d":              {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_043_cnt21_diff21_zscore_252d},
    "itf_drv3_044_active_density_63_diff63_zscore_252d":  {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_044_active_density_63_diff63_zscore_252d},
    "itf_drv3_045_txn_accel_diff63_zscore_252d":          {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_045_txn_accel_diff63_zscore_252d},
    "itf_drv3_046_buyers_63_diff63_zscore_252d":          {"inputs": ["insider_buyers"],                                              "func": itf_drv3_046_buyers_63_diff63_zscore_252d},
    "itf_drv3_047_sell_cnt63_diff63_zscore_252d":         {"inputs": ["insider_sell_count"],                                          "func": itf_drv3_047_sell_cnt63_diff63_zscore_252d},
    "itf_drv3_048_net_txn63_diff63_zscore_252d":          {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_048_net_txn63_diff63_zscore_252d},
    "itf_drv3_049_sell_cnt63_diff63_pct_change_63d":      {"inputs": ["insider_sell_count"],                                          "func": itf_drv3_049_sell_cnt63_diff63_pct_change_63d},
    "itf_drv3_050_net_txn63_diff63_pct_change_63d":       {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_050_net_txn63_diff63_pct_change_63d},
    "itf_drv3_051_active_density_21_diff21_pct_change_21d":{"inputs": ["insider_buy_count", "insider_sell_count"],                    "func": itf_drv3_051_active_density_21_diff21_pct_change_21d},
    "itf_drv3_052_sellers_63_diff63_pct_change_63d":      {"inputs": ["insider_sellers"],                                             "func": itf_drv3_052_sellers_63_diff63_pct_change_63d},
    "itf_drv3_053_cnt21_diff21_ewm_diff_21d":             {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_053_cnt21_diff21_ewm_diff_21d},
    "itf_drv3_054_cnt63_diff63_ewm_diff_63d":             {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_054_cnt63_diff63_ewm_diff_63d},
    "itf_drv3_055_buy_cnt63_diff63_ewm_slope_252d":       {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_055_buy_cnt63_diff63_ewm_slope_252d},
    "itf_drv3_056_buyers_63_diff63_ewm_diff_63d":         {"inputs": ["insider_buyers"],                                              "func": itf_drv3_056_buyers_63_diff63_ewm_diff_63d},
    "itf_drv3_057_txn_accel_diff63_ewm_diff_63d":         {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_057_txn_accel_diff63_ewm_diff_63d},
    "itf_drv3_058_buy_accel_diff63_ewm_diff_63d":         {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_058_buy_accel_diff63_ewm_diff_63d},
    "itf_drv3_059_cnt63_third_diff_ewm":                  {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_059_cnt63_third_diff_ewm},
    "itf_drv3_060_sell_cnt63_third_diff":                 {"inputs": ["insider_sell_count"],                                          "func": itf_drv3_060_sell_cnt63_third_diff},
    "itf_drv3_061_net_txn63_third_diff":                  {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_061_net_txn63_third_diff},
    "itf_drv3_062_buyers_63_third_diff":                  {"inputs": ["insider_buyers"],                                              "func": itf_drv3_062_buyers_63_third_diff},
    "itf_drv3_063_surge_ratio_diff63_slope_252d":         {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_063_surge_ratio_diff63_slope_252d},
    "itf_drv3_064_buy_cnt21_third_diff_ewm":              {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_064_buy_cnt21_third_diff_ewm},
    "itf_drv3_065_active_density_63_diff63_ewm_diff":     {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_065_active_density_63_diff63_ewm_diff},
    "itf_drv3_066_buy_cnt63_second_diff_slope_252d":      {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_066_buy_cnt63_second_diff_slope_252d},
    "itf_drv3_067_buyers_63_second_diff":                 {"inputs": ["insider_buyers"],                                              "func": itf_drv3_067_buyers_63_second_diff},
    "itf_drv3_068_txn_accel_diff63_diff252":              {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_068_txn_accel_diff63_diff252},
    "itf_drv3_069_buy_accel_diff63_diff252":              {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_069_buy_accel_diff63_diff252},
    "itf_drv3_070_cnt21_diff21_diff63":                   {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_070_cnt21_diff21_diff63},
    "itf_drv3_071_sellers_63_diff63_ewm_diff":            {"inputs": ["insider_sellers"],                                             "func": itf_drv3_071_sellers_63_diff63_ewm_diff},
    "itf_drv3_072_cnt63_diff63_diff252":                  {"inputs": ["insider_buy_count", "insider_sell_count"],                     "func": itf_drv3_072_cnt63_diff63_diff252},
    "itf_drv3_073_buy_cnt63_diff63_diff252":              {"inputs": ["insider_buy_count"],                                           "func": itf_drv3_073_buy_cnt63_diff63_diff252},
    "itf_drv3_074_buyers_63_diff63_diff252":              {"inputs": ["insider_buyers"],                                              "func": itf_drv3_074_buyers_63_diff63_diff252},
    "itf_drv3_075_composite_jerk_score_yoy":              {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"],   "func": itf_drv3_075_composite_jerk_score_yoy},
}
