"""
83_insider_buy_cluster — Base Features 076-200
Domain: insider buy clustering — multiple distinct insiders buying within a trailing window
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction filings to one row per (ticker, date).  These are EVENT-DRIVEN
flow series: most days are ZERO (no insider transaction filed); positive values
appear only on filing days.  Do NOT forward-fill — a transaction count is a
flow, not a stock.  All features aggregate over trailing windows with rolling
sums/counts.  The sparsity (mostly-zero) is correct and expected.

Canonical SF2 field names used in this file (lowercase):
    insider_buy_count, insider_buyers, insider_buy_value,
    officer_buy_count, director_buy_count, tenpct_buy_count

Feature numbering: ibc_076 .. ibc_200
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WK   = 5
_TD_MO   = 21
_TD_QTR  = 63
_TD_2Q   = 126
_TD_YEAR = 252
_TD_2Y   = 504
_EPS     = 1e-9

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
    return _rolling_sum((s > 0).astype(float), w)


def _ols_slope(arr: np.ndarray) -> float:
    """OLS slope for a 1-D array; returns nan if degenerate."""
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

# --- Group F (076-090): EWM-based cluster signals and momentum ---

def ibc_076_ewm_buyers_span21(insider_buyers: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of daily distinct-buyer counts, span=21."""
    return _ewm_mean(insider_buyers, _TD_MO)


def ibc_077_ewm_buyers_span63(insider_buyers: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of daily distinct-buyer counts, span=63."""
    return _ewm_mean(insider_buyers, _TD_QTR)


def ibc_078_ewm_buy_count_span21(insider_buy_count: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of daily buy-transaction counts, span=21."""
    return _ewm_mean(insider_buy_count, _TD_MO)


def ibc_079_ewm_buy_count_span63(insider_buy_count: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of daily buy-transaction counts, span=63."""
    return _ewm_mean(insider_buy_count, _TD_QTR)


def ibc_080_buyers_vs_ewm_deviation_21(insider_buyers: pd.Series) -> pd.Series:
    """63-day buyer sum minus its own EWM (span=63); captures acceleration above trend."""
    b63 = _rolling_sum(insider_buyers, _TD_QTR)
    return b63 - _ewm_mean(b63, _TD_QTR)


def ibc_081_buyers_vs_ewm_deviation_63(insider_buyers: pd.Series) -> pd.Series:
    """252-day buyer sum minus its own EWM (span=252)."""
    b252 = _rolling_sum(insider_buyers, _TD_YEAR)
    return b252 - _ewm_mean(b252, _TD_YEAR)


def ibc_082_buy_count_ewm_cross_21_63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM span=21 minus EWM span=63 for buy-transaction counts (fast-minus-slow)."""
    return _ewm_mean(insider_buy_count, _TD_MO) - _ewm_mean(insider_buy_count, _TD_QTR)


def ibc_083_buyers_ewm_cross_21_63(insider_buyers: pd.Series) -> pd.Series:
    """EWM span=21 minus EWM span=63 for distinct-buyer counts."""
    return _ewm_mean(insider_buyers, _TD_MO) - _ewm_mean(insider_buyers, _TD_QTR)


def ibc_084_officer_ewm_span21(officer_buy_count: pd.Series) -> pd.Series:
    """EWM (span=21) of daily officer buy-transaction counts."""
    return _ewm_mean(officer_buy_count, _TD_MO)


def ibc_085_director_ewm_span21(director_buy_count: pd.Series) -> pd.Series:
    """EWM (span=21) of daily director buy-transaction counts."""
    return _ewm_mean(director_buy_count, _TD_MO)


def ibc_086_tenpct_ewm_span63(tenpct_buy_count: pd.Series) -> pd.Series:
    """EWM (span=63) of daily 10%-holder buy-transaction counts."""
    return _ewm_mean(tenpct_buy_count, _TD_QTR)


def ibc_087_buyers_expanding_max(insider_buyers: pd.Series) -> pd.Series:
    """Expanding historical maximum of daily distinct-buyer count."""
    return insider_buyers.expanding(min_periods=1).max()


def ibc_088_buyers_pct_of_expanding_max(insider_buyers: pd.Series) -> pd.Series:
    """Daily distinct-buyer count as fraction of its expanding all-time max."""
    exp_max = insider_buyers.expanding(min_periods=1).max().replace(0, np.nan)
    return insider_buyers / exp_max


def ibc_089_buy_count_expanding_sum(insider_buy_count: pd.Series) -> pd.Series:
    """Expanding cumulative sum of all insider buy transactions."""
    return insider_buy_count.expanding(min_periods=1).sum()


def ibc_090_buyers_rolling_ols_slope_63d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of distinct-buyer daily series over trailing 63-day window."""
    return insider_buyers.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


# --- Group G (091-105): Multi-window comparison and acceleration ---

def ibc_091_buyers_rolling_ols_slope_252d(insider_buyers: pd.Series) -> pd.Series:
    """OLS slope of distinct-buyer daily series over trailing 252-day window."""
    return insider_buyers.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_092_buy_count_slope_63d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of buy-transaction daily series over trailing 63-day window."""
    return insider_buy_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_093_buy_count_slope_252d(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of buy-transaction daily series over trailing 252-day window."""
    return insider_buy_count.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True)


def ibc_094_officer_slope_63d(officer_buy_count: pd.Series) -> pd.Series:
    """OLS slope of officer buy daily series over trailing 63-day window."""
    return officer_buy_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_095_director_slope_63d(director_buy_count: pd.Series) -> pd.Series:
    """OLS slope of director buy daily series over trailing 63-day window."""
    return director_buy_count.rolling(_TD_QTR, min_periods=max(2, _TD_QTR // 4)).apply(
        _ols_slope, raw=True)


def ibc_096_buyer_count_21d_vs_prior_21d(insider_buyers: pd.Series) -> pd.Series:
    """Change in 21-day buyer count vs the prior 21-day period (21-day lag)."""
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    return b21 - b21.shift(_TD_MO)


def ibc_097_buyer_count_63d_vs_prior_63d(insider_buyers: pd.Series) -> pd.Series:
    """Change in 63-day buyer count vs the prior 63-day period."""
    b63 = _rolling_sum(insider_buyers, _TD_QTR)
    return b63 - b63.shift(_TD_QTR)


def ibc_098_buy_count_21d_vs_prior_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Change in 21-day buy-transaction count vs the prior 21-day period."""
    b21 = _rolling_sum(insider_buy_count, _TD_MO)
    return b21 - b21.shift(_TD_MO)


def ibc_099_buy_count_63d_vs_prior_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Change in 63-day buy-transaction count vs the prior 63-day period."""
    b63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return b63 - b63.shift(_TD_QTR)


def ibc_100_buyer_count_21d_pct_chg(insider_buyers: pd.Series) -> pd.Series:
    """Percent change in 21-day buyer count vs the prior 21-day period."""
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    prior = b21.shift(_TD_MO).replace(0, np.nan)
    return (b21 - prior) / prior


def ibc_101_buyer_count_63d_pct_chg(insider_buyers: pd.Series) -> pd.Series:
    """Percent change in 63-day buyer count vs the prior 63-day period."""
    b63 = _rolling_sum(insider_buyers, _TD_QTR)
    prior = b63.shift(_TD_QTR).replace(0, np.nan)
    return (b63 - prior) / prior


def ibc_102_buy_count_252d_vs_prior_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Change in annual buy-transaction count vs the prior annual period."""
    b252 = _rolling_sum(insider_buy_count, _TD_YEAR)
    return b252 - b252.shift(_TD_YEAR)


def ibc_103_active_days_21d_vs_prior_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Change in number of active buy days (21d) vs prior 21-day period."""
    a21 = _active_days(insider_buy_count, _TD_MO)
    return a21 - a21.shift(_TD_MO)


def ibc_104_active_days_63d_vs_prior_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Change in number of active buy days (63d) vs prior 63-day period."""
    a63 = _active_days(insider_buy_count, _TD_QTR)
    return a63 - a63.shift(_TD_QTR)


def ibc_105_multi_buyer_days_21d_vs_prior(insider_buyers: pd.Series) -> pd.Series:
    """Change in multi-buyer days (>=2 buyers, 21d) vs prior 21-day period."""
    mb = _rolling_sum((insider_buyers >= 2).astype(float), _TD_MO)
    return mb - mb.shift(_TD_MO)


# --- Group H (106-120): Cluster concentration and Herfindahl-style scores ---

def ibc_106_buyer_concentration_21d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """
    Buyer concentration over 21 days: distinct buyers / total transactions.
    Low ratio = many transactions from few buyers; high = spread across many.
    """
    txns = _rolling_sum(insider_buy_count, _TD_MO).replace(0, np.nan)
    buyers = _rolling_sum(insider_buyers, _TD_MO)
    return buyers / txns


def ibc_107_buyer_concentration_63d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Buyer concentration over 63 days: distinct buyers / total transactions."""
    txns = _rolling_sum(insider_buy_count, _TD_QTR).replace(0, np.nan)
    buyers = _rolling_sum(insider_buyers, _TD_QTR)
    return buyers / txns


def ibc_108_officer_share_of_active_days_63d(officer_buy_count: pd.Series,
                                               insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of active buy days in 63d window that had at least one officer buy."""
    active_total   = _active_days(insider_buy_count, _TD_QTR).replace(0, np.nan)
    active_officer = _active_days(officer_buy_count, _TD_QTR)
    return active_officer / active_total


def ibc_109_director_share_of_active_days_63d(director_buy_count: pd.Series,
                                                insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of active buy days in 63d window that had at least one director buy."""
    active_total    = _active_days(insider_buy_count, _TD_QTR).replace(0, np.nan)
    active_director = _active_days(director_buy_count, _TD_QTR)
    return active_director / active_total


def ibc_110_cluster_span_ratio_21_to_252(insider_buyers: pd.Series) -> pd.Series:
    """
    Ratio of 21-day active-buyer days to 252-day active-buyer days;
    high value = recent buyers clustered more tightly relative to year.
    """
    a21  = _active_days(insider_buyers, _TD_MO)
    a252 = _active_days(insider_buyers, _TD_YEAR).replace(0, np.nan)
    return a21 / a252


def ibc_111_cluster_span_ratio_63_to_252(insider_buyers: pd.Series) -> pd.Series:
    """Ratio of 63-day active-buyer days to 252-day active-buyer days."""
    a63  = _active_days(insider_buyers, _TD_QTR)
    a252 = _active_days(insider_buyers, _TD_YEAR).replace(0, np.nan)
    return a63 / a252


def ibc_112_max_buyers_21d_vs_median_252d(insider_buyers: pd.Series) -> pd.Series:
    """Max daily buyers in 21d window minus median daily buyers in 252d window."""
    max21  = _rolling_max(insider_buyers, _TD_MO)
    med252 = _rolling_median(insider_buyers, _TD_YEAR)
    return max21 - med252


def ibc_113_max_buyers_63d_vs_median_252d(insider_buyers: pd.Series) -> pd.Series:
    """Max daily buyers in 63d window minus median daily buyers in 252d window."""
    max63  = _rolling_max(insider_buyers, _TD_QTR)
    med252 = _rolling_median(insider_buyers, _TD_YEAR)
    return max63 - med252


def ibc_114_buyer_std_63d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of daily distinct-buyer counts."""
    return _rolling_std(insider_buyers, _TD_QTR)


def ibc_115_buyer_std_252d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 252-day standard deviation of daily distinct-buyer counts."""
    return _rolling_std(insider_buyers, _TD_YEAR)


def ibc_116_buy_count_std_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 63-day standard deviation of daily buy-transaction counts."""
    return _rolling_std(insider_buy_count, _TD_QTR)


def ibc_117_buy_count_cv_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of buy-transaction counts over 63 days."""
    m = _rolling_mean(insider_buy_count, _TD_QTR).replace(0, np.nan)
    s = _rolling_std(insider_buy_count, _TD_QTR)
    return s / m


def ibc_118_officers_plus_tenpct_63d(officer_buy_count: pd.Series, tenpct_buy_count: pd.Series) -> pd.Series:
    """Combined officer + 10%-holder buy count over trailing 63 days."""
    return _rolling_sum(officer_buy_count, _TD_QTR) + _rolling_sum(tenpct_buy_count, _TD_QTR)


def ibc_119_directors_plus_tenpct_63d(director_buy_count: pd.Series, tenpct_buy_count: pd.Series) -> pd.Series:
    """Combined director + 10%-holder buy count over trailing 63 days."""
    return _rolling_sum(director_buy_count, _TD_QTR) + _rolling_sum(tenpct_buy_count, _TD_QTR)


def ibc_120_all_roles_combined_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                    tenpct_buy_count: pd.Series) -> pd.Series:
    """Combined officer + director + 10%-holder buy count over trailing 63 days."""
    return (_rolling_sum(officer_buy_count, _TD_QTR)
            + _rolling_sum(director_buy_count, _TD_QTR)
            + _rolling_sum(tenpct_buy_count, _TD_QTR))


# --- Group I (121-135): Longest cluster window and streak statistics ---

def ibc_121_longest_consecutive_buy_days_21d(insider_buy_count: pd.Series) -> pd.Series:
    """
    Longest run of consecutive days with at least one buy, within trailing 21-day window.
    Uses a scalar-returning apply.
    """
    active = (insider_buy_count > 0).astype(int)

    def _longest_run(arr):
        best = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return active.rolling(_TD_MO, min_periods=1).apply(_longest_run, raw=True)


def ibc_122_longest_consecutive_buy_days_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Longest run of consecutive buy days within trailing 63-day window."""
    active = (insider_buy_count > 0).astype(int)

    def _longest_run(arr):
        best = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return active.rolling(_TD_QTR, min_periods=1).apply(_longest_run, raw=True)


def ibc_123_longest_consecutive_buy_days_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Longest run of consecutive buy days within trailing 252-day window."""
    active = (insider_buy_count > 0).astype(int)

    def _longest_run(arr):
        best = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)

    return active.rolling(_TD_YEAR, min_periods=1).apply(_longest_run, raw=True)


def ibc_124_buy_gap_avg_21d(insider_buy_count: pd.Series) -> pd.Series:
    """
    Average gap (in trading days) between consecutive buy events within trailing 21-day window.
    = (window_size - 1) / (active_days - 1) when active_days >= 2; else NaN.
    """
    active = _active_days(insider_buy_count, _TD_MO)
    denom = (active - 1).replace(0, np.nan)
    return pd.Series(_TD_MO - 1, index=insider_buy_count.index, dtype=float) / denom


def ibc_125_buy_gap_avg_63d(insider_buy_count: pd.Series) -> pd.Series:
    """Average gap between buy events within trailing 63-day window."""
    active = _active_days(insider_buy_count, _TD_QTR)
    denom = (active - 1).replace(0, np.nan)
    return pd.Series(_TD_QTR - 1, index=insider_buy_count.index, dtype=float) / denom


def ibc_126_buy_gap_avg_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Average gap between buy events within trailing 252-day window."""
    active = _active_days(insider_buy_count, _TD_YEAR)
    denom = (active - 1).replace(0, np.nan)
    return pd.Series(_TD_YEAR - 1, index=insider_buy_count.index, dtype=float) / denom


def ibc_127_buy_recency_weight_63d(insider_buy_count: pd.Series) -> pd.Series:
    """
    Recency-weighted buy count over 63 days: linearly weights recent days more.
    Weight for day i (0=oldest, 62=today) = (i+1); sum of weights = 63*64/2 = 2016.
    """
    weights = np.arange(1, _TD_QTR + 1, dtype=float)

    def _wsum(arr):
        w = weights[-len(arr):]
        return float(np.dot(arr, w))

    return insider_buy_count.rolling(_TD_QTR, min_periods=1).apply(_wsum, raw=True)


def ibc_128_buyer_recency_weight_63d(insider_buyers: pd.Series) -> pd.Series:
    """Recency-weighted distinct-buyer count over 63 days (linear weights, recent=high)."""
    weights = np.arange(1, _TD_QTR + 1, dtype=float)

    def _wsum(arr):
        w = weights[-len(arr):]
        return float(np.dot(arr, w))

    return insider_buyers.rolling(_TD_QTR, min_periods=1).apply(_wsum, raw=True)


def ibc_129_buy_recency_weight_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Recency-weighted buy count over 252 days (linear weights)."""
    weights = np.arange(1, _TD_YEAR + 1, dtype=float)

    def _wsum(arr):
        w = weights[-len(arr):]
        return float(np.dot(arr, w))

    return insider_buy_count.rolling(_TD_YEAR, min_periods=1).apply(_wsum, raw=True)


def ibc_130_officer_recency_weight_63d(officer_buy_count: pd.Series) -> pd.Series:
    """Recency-weighted officer buy count over 63 days."""
    weights = np.arange(1, _TD_QTR + 1, dtype=float)

    def _wsum(arr):
        w = weights[-len(arr):]
        return float(np.dot(arr, w))

    return officer_buy_count.rolling(_TD_QTR, min_periods=1).apply(_wsum, raw=True)


def ibc_131_director_recency_weight_63d(director_buy_count: pd.Series) -> pd.Series:
    """Recency-weighted director buy count over 63 days."""
    weights = np.arange(1, _TD_QTR + 1, dtype=float)

    def _wsum(arr):
        w = weights[-len(arr):]
        return float(np.dot(arr, w))

    return director_buy_count.rolling(_TD_QTR, min_periods=1).apply(_wsum, raw=True)


def ibc_132_buy_count_21d_rank_in_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of 21-day buy count within a trailing 252-day window."""
    b21 = _rolling_sum(insider_buy_count, _TD_MO)
    return _rolling_rank_pct(b21, _TD_YEAR)


def ibc_133_buyers_21d_rank_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 21-day distinct-buyer count within a trailing 252-day window."""
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    return _rolling_rank_pct(b21, _TD_YEAR)


def ibc_134_buyers_63d_rank_in_504d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 63-day distinct-buyer count within a trailing 504-day window."""
    b63 = _rolling_sum(insider_buyers, _TD_QTR)
    return _rolling_rank_pct(b63, _TD_2Y)


def ibc_135_buy_count_63d_rank_in_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of 63-day buy-transaction count within a trailing 504-day window."""
    b63 = _rolling_sum(insider_buy_count, _TD_QTR)
    return _rolling_rank_pct(b63, _TD_2Y)


# --- Group J (136-150): Composite, cross-role, and burst-detection features ---

def ibc_136_role_diversity_score_63d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                      tenpct_buy_count: pd.Series) -> pd.Series:
    """
    Count of distinct role-types that bought in trailing 63 days (0-3 scale).
    +1 for officers, +1 for directors, +1 for 10%-holders.
    """
    o = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_QTR) > 0).astype(float)
    return o + d + t


def ibc_137_role_diversity_score_21d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                      tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of distinct role-types that bought in trailing 21 days."""
    o = (_rolling_sum(officer_buy_count, _TD_MO) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_MO) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_MO) > 0).astype(float)
    return o + d + t


def ibc_138_burst_flag_21d_vs_252d_mean(insider_buy_count: pd.Series) -> pd.Series:
    """
    Binary flag: 1 when 21-day buy count exceeds 2x the trailing 252-day mean of
    21-day buy counts (buy-burst detection).
    """
    b21   = _rolling_sum(insider_buy_count, _TD_MO)
    avg   = _rolling_mean(b21, _TD_YEAR)
    return (b21 > 2.0 * avg).astype(float)


def ibc_139_burst_flag_63d_vs_252d_mean(insider_buy_count: pd.Series) -> pd.Series:
    """Binary flag: 1 when 63-day buy count exceeds 2x the 252-day mean of 63d counts."""
    b63 = _rolling_sum(insider_buy_count, _TD_QTR)
    avg = _rolling_mean(b63, _TD_YEAR)
    return (b63 > 2.0 * avg).astype(float)


def ibc_140_buyer_burst_flag_21d(insider_buyers: pd.Series) -> pd.Series:
    """
    Binary flag: 1 when 21-day distinct-buyer sum exceeds 2x its 252-day mean.
    """
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    avg = _rolling_mean(b21, _TD_YEAR)
    return (b21 > 2.0 * avg).astype(float)


def ibc_141_buyer_burst_flag_63d(insider_buyers: pd.Series) -> pd.Series:
    """Binary flag: 1 when 63-day distinct-buyer sum exceeds 2x its 252-day mean."""
    b63 = _rolling_sum(insider_buyers, _TD_QTR)
    avg = _rolling_mean(b63, _TD_YEAR)
    return (b63 > 2.0 * avg).astype(float)


def ibc_142_cluster_quality_score_63d(insider_buyers: pd.Series, insider_buy_count: pd.Series,
                                       officer_buy_count: pd.Series) -> pd.Series:
    """
    Cluster quality score (63d): sum of normalized sub-scores.
    Sub-scores: distinct buyers (vs 252d mean), active days (vs 252d mean), officer active.
    Each sub-score clipped to [0, 2].
    """
    b63   = _rolling_sum(insider_buyers, _TD_QTR)
    avg_b = _rolling_mean(b63, _TD_YEAR).replace(0, np.nan)
    s1    = (b63 / avg_b).clip(0, 2)

    a63   = _active_days(insider_buy_count, _TD_QTR)
    avg_a = _rolling_mean(a63, _TD_YEAR).replace(0, np.nan)
    s2    = (a63 / avg_a).clip(0, 2)

    s3 = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    return s1 + s2 + s3


def ibc_143_buy_event_regularity_63d(insider_buy_count: pd.Series) -> pd.Series:
    """
    Regularity of buy events in 63-day window:
    = active_days / (longest_gap_proxy + 1).
    Longest gap proxy = (63 - 1) / max(1, active_days - 1).
    High when events are spread evenly across the window.
    """
    active = _active_days(insider_buy_count, _TD_QTR)
    gap    = _safe_div(pd.Series(_TD_QTR - 1, index=insider_buy_count.index, dtype=float),
                       (active - 1).clip(lower=1))
    return _safe_div(active, gap + 1)


def ibc_144_officer_dir_combined_21d_burst(officer_buy_count: pd.Series,
                                            director_buy_count: pd.Series) -> pd.Series:
    """
    Binary: 1 when combined officer+director 21-day count exceeds 2x its 252-day mean.
    """
    combined = _rolling_sum(officer_buy_count, _TD_MO) + _rolling_sum(director_buy_count, _TD_MO)
    avg = _rolling_mean(combined, _TD_YEAR)
    return (combined > 2.0 * avg).astype(float)


def ibc_145_cluster_present_and_accelerating(insider_buyers: pd.Series) -> pd.Series:
    """
    1 when: (a) 21-day buyer count >= 2, AND (b) 21-day count > prior 21-day count.
    Captures a cluster that is growing.
    """
    b21   = _rolling_sum(insider_buyers, _TD_MO)
    has_cluster  = (b21 >= 2).astype(float)
    is_accel     = (b21 > b21.shift(_TD_MO)).astype(float)
    return has_cluster * is_accel


def ibc_146_tenpct_active_flag_21d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if any 10%-holder bought within trailing 21 days."""
    return (_rolling_sum(tenpct_buy_count, _TD_MO) > 0).astype(float)


def ibc_147_tenpct_active_flag_63d(tenpct_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if any 10%-holder bought within trailing 63 days."""
    return (_rolling_sum(tenpct_buy_count, _TD_QTR) > 0).astype(float)


def ibc_148_cumulative_cluster_weeks_1y(insider_buy_count: pd.Series) -> pd.Series:
    """Count of 5-day windows (out of 252 trailing days) that had at least one buy."""
    weekly = _rolling_sum(insider_buy_count, _TD_WK)
    had_buy_week = (weekly > 0).astype(float)
    return _rolling_sum(had_buy_week, _TD_YEAR)


def ibc_149_buyer_cluster_zscore_composite(insider_buyers: pd.Series,
                                            insider_buy_count: pd.Series) -> pd.Series:
    """
    Composite z-score: average of z-scores of the 21-day and 63-day buyer counts,
    computed against their own 252-day rolling distributions.
    """
    z21 = _zscore_rolling(_rolling_sum(insider_buyers, _TD_MO), _TD_YEAR)
    z63 = _zscore_rolling(_rolling_sum(insider_buyers, _TD_QTR), _TD_YEAR)
    zc  = _zscore_rolling(_rolling_sum(insider_buy_count, _TD_MO), _TD_YEAR)
    return (z21 + z63 + zc) / 3.0


def ibc_150_cluster_signal_strength_63d(insider_buyers: pd.Series, insider_buy_count: pd.Series,
                                         officer_buy_count: pd.Series,
                                         director_buy_count: pd.Series) -> pd.Series:
    """
    Overall cluster signal strength over 63 days (additive score 0-6):
    +1 buyers>=1, +1 buyers>=2, +1 buyers>=3,
    +1 officer active, +1 director active, +1 active days>=5.
    """
    b63  = _rolling_sum(insider_buyers, _TD_QTR)
    a63  = _active_days(insider_buy_count, _TD_QTR)
    s1   = (b63 >= 1).astype(float)
    s2   = (b63 >= 2).astype(float)
    s3   = (b63 >= 3).astype(float)
    s4   = (_rolling_sum(officer_buy_count, _TD_QTR) > 0).astype(float)
    s5   = (_rolling_sum(director_buy_count, _TD_QTR) > 0).astype(float)
    s6   = (a63 >= 5).astype(float)
    return s1 + s2 + s3 + s4 + s5 + s6


# --- Group K (176-200): Extended EWMs, new windows, concentration, composite ---

def ibc_176_ewm_buyers_span126(insider_buyers: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of daily distinct-buyer counts, span=126."""
    return _ewm_mean(insider_buyers, _TD_2Q)


def ibc_177_ewm_buy_count_span126(insider_buy_count: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of daily buy-transaction counts, span=126."""
    return _ewm_mean(insider_buy_count, _TD_2Q)


def ibc_178_ewm_officer_span63(officer_buy_count: pd.Series) -> pd.Series:
    """EWM (span=63) of daily officer buy-transaction counts."""
    return _ewm_mean(officer_buy_count, _TD_QTR)


def ibc_179_ewm_director_span63(director_buy_count: pd.Series) -> pd.Series:
    """EWM (span=63) of daily director buy-transaction counts."""
    return _ewm_mean(director_buy_count, _TD_QTR)


def ibc_180_ewm_tenpct_span21(tenpct_buy_count: pd.Series) -> pd.Series:
    """EWM (span=21) of daily 10%-holder buy-transaction counts."""
    return _ewm_mean(tenpct_buy_count, _TD_MO)


def ibc_181_buyers_ewm_cross_63_252(insider_buyers: pd.Series) -> pd.Series:
    """EWM span=63 minus EWM span=252 for distinct-buyer counts (medium-minus-slow)."""
    return _ewm_mean(insider_buyers, _TD_QTR) - _ewm_mean(insider_buyers, _TD_YEAR)


def ibc_182_buy_count_ewm_cross_63_252(insider_buy_count: pd.Series) -> pd.Series:
    """EWM span=63 minus EWM span=252 for buy-transaction counts."""
    return _ewm_mean(insider_buy_count, _TD_QTR) - _ewm_mean(insider_buy_count, _TD_YEAR)


def ibc_183_officer_slope_21d(officer_buy_count: pd.Series) -> pd.Series:
    """OLS slope of officer buy daily series over trailing 21-day window."""
    return officer_buy_count.rolling(_TD_MO, min_periods=max(2, _TD_MO // 4)).apply(
        _ols_slope, raw=True)


def ibc_184_director_slope_21d(director_buy_count: pd.Series) -> pd.Series:
    """OLS slope of director buy daily series over trailing 21-day window."""
    return director_buy_count.rolling(_TD_MO, min_periods=max(2, _TD_MO // 4)).apply(
        _ols_slope, raw=True)


def ibc_185_buyer_count_126d_vs_prior_126d(insider_buyers: pd.Series) -> pd.Series:
    """Change in 126-day buyer count vs the prior 126-day period."""
    b126 = _rolling_sum(insider_buyers, _TD_2Q)
    return b126 - b126.shift(_TD_2Q)


def ibc_186_buy_count_126d_vs_prior_126d(insider_buy_count: pd.Series) -> pd.Series:
    """Change in 126-day buy-transaction count vs the prior 126-day period."""
    b126 = _rolling_sum(insider_buy_count, _TD_2Q)
    return b126 - b126.shift(_TD_2Q)


def ibc_187_buyer_count_252d_pct_chg(insider_buyers: pd.Series) -> pd.Series:
    """Percent change in 252-day buyer count vs the prior 252-day period."""
    b252 = _rolling_sum(insider_buyers, _TD_YEAR)
    prior = b252.shift(_TD_YEAR).replace(0, np.nan)
    return (b252 - prior) / prior


def ibc_188_buyer_concentration_126d(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Buyer concentration over 126 days: distinct buyers / total transactions."""
    txns = _rolling_sum(insider_buy_count, _TD_2Q).replace(0, np.nan)
    return _rolling_sum(insider_buyers, _TD_2Q) / txns


def ibc_189_officer_share_of_active_days_21d(officer_buy_count: pd.Series,
                                              insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of active buy days in 21d window that had at least one officer buy."""
    active_total   = _active_days(insider_buy_count, _TD_MO).replace(0, np.nan)
    active_officer = _active_days(officer_buy_count, _TD_MO)
    return active_officer / active_total


def ibc_190_tenpct_share_of_active_days_63d(tenpct_buy_count: pd.Series,
                                             insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of active buy days in 63d window that had at least one 10%-holder buy."""
    active_total  = _active_days(insider_buy_count, _TD_QTR).replace(0, np.nan)
    active_tenpct = _active_days(tenpct_buy_count, _TD_QTR)
    return active_tenpct / active_total


def ibc_191_buyer_std_21d(insider_buyers: pd.Series) -> pd.Series:
    """Rolling 21-day standard deviation of daily distinct-buyer counts."""
    return _rolling_std(insider_buyers, _TD_MO)


def ibc_192_buy_count_cv_21d(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of buy-transaction counts over 21 days."""
    m = _rolling_mean(insider_buy_count, _TD_MO).replace(0, np.nan)
    s = _rolling_std(insider_buy_count, _TD_MO)
    return s / m


def ibc_193_buy_count_cv_252d(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation (std/mean) of buy-transaction counts over 252 days."""
    m = _rolling_mean(insider_buy_count, _TD_YEAR).replace(0, np.nan)
    s = _rolling_std(insider_buy_count, _TD_YEAR)
    return s / m


def ibc_194_buy_count_21d_rank_in_504d(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of 21-day buy count within a trailing 504-day window."""
    b21 = _rolling_sum(insider_buy_count, _TD_MO)
    return _rolling_rank_pct(b21, _TD_2Y)


def ibc_195_buyers_63d_rank_in_252d(insider_buyers: pd.Series) -> pd.Series:
    """Percentile rank of 63-day distinct-buyer count within a trailing 252-day window."""
    b63 = _rolling_sum(insider_buyers, _TD_QTR)
    return _rolling_rank_pct(b63, _TD_YEAR)


def ibc_196_burst_flag_21d_vs_252d_mean_3x(insider_buy_count: pd.Series) -> pd.Series:
    """Binary flag: 1 when 21-day buy count exceeds 3x the trailing 252-day mean (extreme burst)."""
    b21 = _rolling_sum(insider_buy_count, _TD_MO)
    avg = _rolling_mean(b21, _TD_YEAR)
    return (b21 > 3.0 * avg).astype(float)


def ibc_197_role_diversity_score_126d(officer_buy_count: pd.Series, director_buy_count: pd.Series,
                                       tenpct_buy_count: pd.Series) -> pd.Series:
    """Count of distinct role-types that bought in trailing 126 days (0-3 scale)."""
    o = (_rolling_sum(officer_buy_count, _TD_2Q) > 0).astype(float)
    d = (_rolling_sum(director_buy_count, _TD_2Q) > 0).astype(float)
    t = (_rolling_sum(tenpct_buy_count, _TD_2Q) > 0).astype(float)
    return o + d + t


def ibc_198_cluster_quality_score_21d(insider_buyers: pd.Series, insider_buy_count: pd.Series,
                                       officer_buy_count: pd.Series) -> pd.Series:
    """Cluster quality score (21d): normalized buyer ratio + normalized active-days + officer flag, each clipped [0,2]."""
    b21   = _rolling_sum(insider_buyers, _TD_MO)
    avg_b = _rolling_mean(b21, _TD_YEAR).replace(0, np.nan)
    s1    = (b21 / avg_b).clip(0, 2)
    a21   = _active_days(insider_buy_count, _TD_MO)
    avg_a = _rolling_mean(a21, _TD_YEAR).replace(0, np.nan)
    s2    = (a21 / avg_a).clip(0, 2)
    s3    = (_rolling_sum(officer_buy_count, _TD_MO) > 0).astype(float)
    return s1 + s2 + s3


def ibc_199_cumulative_cluster_weeks_2y(insider_buy_count: pd.Series) -> pd.Series:
    """Count of 5-day windows (out of 504 trailing days) that had at least one buy."""
    weekly      = _rolling_sum(insider_buy_count, _TD_WK)
    had_buy_wk  = (weekly > 0).astype(float)
    return _rolling_sum(had_buy_wk, _TD_2Y)


def ibc_200_cluster_signal_strength_21d(insider_buyers: pd.Series, insider_buy_count: pd.Series,
                                         officer_buy_count: pd.Series,
                                         director_buy_count: pd.Series) -> pd.Series:
    """Overall cluster signal strength over 21 days (additive score 0-6):
    +1 buyers>=1, +1 buyers>=2, +1 buyers>=3,
    +1 officer active, +1 director active, +1 active days>=3."""
    b21 = _rolling_sum(insider_buyers, _TD_MO)
    a21 = _active_days(insider_buy_count, _TD_MO)
    s1  = (b21 >= 1).astype(float)
    s2  = (b21 >= 2).astype(float)
    s3  = (b21 >= 3).astype(float)
    s4  = (_rolling_sum(officer_buy_count, _TD_MO) > 0).astype(float)
    s5  = (_rolling_sum(director_buy_count, _TD_MO) > 0).astype(float)
    s6  = (a21 >= 3).astype(float)
    return s1 + s2 + s3 + s4 + s5 + s6


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INSIDER_BUY_CLUSTER_REGISTRY_076_150 = {
    "ibc_076_ewm_buyers_span21":                    {"inputs": ["insider_buyers"],                                                    "func": ibc_076_ewm_buyers_span21},
    "ibc_077_ewm_buyers_span63":                    {"inputs": ["insider_buyers"],                                                    "func": ibc_077_ewm_buyers_span63},
    "ibc_078_ewm_buy_count_span21":                 {"inputs": ["insider_buy_count"],                                                 "func": ibc_078_ewm_buy_count_span21},
    "ibc_079_ewm_buy_count_span63":                 {"inputs": ["insider_buy_count"],                                                 "func": ibc_079_ewm_buy_count_span63},
    "ibc_080_buyers_vs_ewm_deviation_21":           {"inputs": ["insider_buyers"],                                                    "func": ibc_080_buyers_vs_ewm_deviation_21},
    "ibc_081_buyers_vs_ewm_deviation_63":           {"inputs": ["insider_buyers"],                                                    "func": ibc_081_buyers_vs_ewm_deviation_63},
    "ibc_082_buy_count_ewm_cross_21_63":            {"inputs": ["insider_buy_count"],                                                 "func": ibc_082_buy_count_ewm_cross_21_63},
    "ibc_083_buyers_ewm_cross_21_63":               {"inputs": ["insider_buyers"],                                                    "func": ibc_083_buyers_ewm_cross_21_63},
    "ibc_084_officer_ewm_span21":                   {"inputs": ["officer_buy_count"],                                                 "func": ibc_084_officer_ewm_span21},
    "ibc_085_director_ewm_span21":                  {"inputs": ["director_buy_count"],                                                "func": ibc_085_director_ewm_span21},
    "ibc_086_tenpct_ewm_span63":                    {"inputs": ["tenpct_buy_count"],                                                  "func": ibc_086_tenpct_ewm_span63},
    "ibc_087_buyers_expanding_max":                 {"inputs": ["insider_buyers"],                                                    "func": ibc_087_buyers_expanding_max},
    "ibc_088_buyers_pct_of_expanding_max":          {"inputs": ["insider_buyers"],                                                    "func": ibc_088_buyers_pct_of_expanding_max},
    "ibc_089_buy_count_expanding_sum":              {"inputs": ["insider_buy_count"],                                                 "func": ibc_089_buy_count_expanding_sum},
    "ibc_090_buyers_rolling_ols_slope_63d":         {"inputs": ["insider_buyers"],                                                    "func": ibc_090_buyers_rolling_ols_slope_63d},
    "ibc_091_buyers_rolling_ols_slope_252d":        {"inputs": ["insider_buyers"],                                                    "func": ibc_091_buyers_rolling_ols_slope_252d},
    "ibc_092_buy_count_slope_63d":                  {"inputs": ["insider_buy_count"],                                                 "func": ibc_092_buy_count_slope_63d},
    "ibc_093_buy_count_slope_252d":                 {"inputs": ["insider_buy_count"],                                                 "func": ibc_093_buy_count_slope_252d},
    "ibc_094_officer_slope_63d":                    {"inputs": ["officer_buy_count"],                                                 "func": ibc_094_officer_slope_63d},
    "ibc_095_director_slope_63d":                   {"inputs": ["director_buy_count"],                                                "func": ibc_095_director_slope_63d},
    "ibc_096_buyer_count_21d_vs_prior_21d":         {"inputs": ["insider_buyers"],                                                    "func": ibc_096_buyer_count_21d_vs_prior_21d},
    "ibc_097_buyer_count_63d_vs_prior_63d":         {"inputs": ["insider_buyers"],                                                    "func": ibc_097_buyer_count_63d_vs_prior_63d},
    "ibc_098_buy_count_21d_vs_prior_21d":           {"inputs": ["insider_buy_count"],                                                 "func": ibc_098_buy_count_21d_vs_prior_21d},
    "ibc_099_buy_count_63d_vs_prior_63d":           {"inputs": ["insider_buy_count"],                                                 "func": ibc_099_buy_count_63d_vs_prior_63d},
    "ibc_100_buyer_count_21d_pct_chg":              {"inputs": ["insider_buyers"],                                                    "func": ibc_100_buyer_count_21d_pct_chg},
    "ibc_101_buyer_count_63d_pct_chg":              {"inputs": ["insider_buyers"],                                                    "func": ibc_101_buyer_count_63d_pct_chg},
    "ibc_102_buy_count_252d_vs_prior_252d":         {"inputs": ["insider_buy_count"],                                                 "func": ibc_102_buy_count_252d_vs_prior_252d},
    "ibc_103_active_days_21d_vs_prior_21d":         {"inputs": ["insider_buy_count"],                                                 "func": ibc_103_active_days_21d_vs_prior_21d},
    "ibc_104_active_days_63d_vs_prior_63d":         {"inputs": ["insider_buy_count"],                                                 "func": ibc_104_active_days_63d_vs_prior_63d},
    "ibc_105_multi_buyer_days_21d_vs_prior":        {"inputs": ["insider_buyers"],                                                    "func": ibc_105_multi_buyer_days_21d_vs_prior},
    "ibc_106_buyer_concentration_21d":              {"inputs": ["insider_buyers", "insider_buy_count"],                               "func": ibc_106_buyer_concentration_21d},
    "ibc_107_buyer_concentration_63d":              {"inputs": ["insider_buyers", "insider_buy_count"],                               "func": ibc_107_buyer_concentration_63d},
    "ibc_108_officer_share_of_active_days_63d":     {"inputs": ["officer_buy_count", "insider_buy_count"],                           "func": ibc_108_officer_share_of_active_days_63d},
    "ibc_109_director_share_of_active_days_63d":    {"inputs": ["director_buy_count", "insider_buy_count"],                          "func": ibc_109_director_share_of_active_days_63d},
    "ibc_110_cluster_span_ratio_21_to_252":         {"inputs": ["insider_buyers"],                                                    "func": ibc_110_cluster_span_ratio_21_to_252},
    "ibc_111_cluster_span_ratio_63_to_252":         {"inputs": ["insider_buyers"],                                                    "func": ibc_111_cluster_span_ratio_63_to_252},
    "ibc_112_max_buyers_21d_vs_median_252d":        {"inputs": ["insider_buyers"],                                                    "func": ibc_112_max_buyers_21d_vs_median_252d},
    "ibc_113_max_buyers_63d_vs_median_252d":        {"inputs": ["insider_buyers"],                                                    "func": ibc_113_max_buyers_63d_vs_median_252d},
    "ibc_114_buyer_std_63d":                        {"inputs": ["insider_buyers"],                                                    "func": ibc_114_buyer_std_63d},
    "ibc_115_buyer_std_252d":                       {"inputs": ["insider_buyers"],                                                    "func": ibc_115_buyer_std_252d},
    "ibc_116_buy_count_std_63d":                    {"inputs": ["insider_buy_count"],                                                 "func": ibc_116_buy_count_std_63d},
    "ibc_117_buy_count_cv_63d":                     {"inputs": ["insider_buy_count"],                                                 "func": ibc_117_buy_count_cv_63d},
    "ibc_118_officers_plus_tenpct_63d":             {"inputs": ["officer_buy_count", "tenpct_buy_count"],                             "func": ibc_118_officers_plus_tenpct_63d},
    "ibc_119_directors_plus_tenpct_63d":            {"inputs": ["director_buy_count", "tenpct_buy_count"],                            "func": ibc_119_directors_plus_tenpct_63d},
    "ibc_120_all_roles_combined_63d":               {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],       "func": ibc_120_all_roles_combined_63d},
    "ibc_121_longest_consecutive_buy_days_21d":     {"inputs": ["insider_buy_count"],                                                 "func": ibc_121_longest_consecutive_buy_days_21d},
    "ibc_122_longest_consecutive_buy_days_63d":     {"inputs": ["insider_buy_count"],                                                 "func": ibc_122_longest_consecutive_buy_days_63d},
    "ibc_123_longest_consecutive_buy_days_252d":    {"inputs": ["insider_buy_count"],                                                 "func": ibc_123_longest_consecutive_buy_days_252d},
    "ibc_124_buy_gap_avg_21d":                      {"inputs": ["insider_buy_count"],                                                 "func": ibc_124_buy_gap_avg_21d},
    "ibc_125_buy_gap_avg_63d":                      {"inputs": ["insider_buy_count"],                                                 "func": ibc_125_buy_gap_avg_63d},
    "ibc_126_buy_gap_avg_252d":                     {"inputs": ["insider_buy_count"],                                                 "func": ibc_126_buy_gap_avg_252d},
    "ibc_127_buy_recency_weight_63d":               {"inputs": ["insider_buy_count"],                                                 "func": ibc_127_buy_recency_weight_63d},
    "ibc_128_buyer_recency_weight_63d":             {"inputs": ["insider_buyers"],                                                    "func": ibc_128_buyer_recency_weight_63d},
    "ibc_129_buy_recency_weight_252d":              {"inputs": ["insider_buy_count"],                                                 "func": ibc_129_buy_recency_weight_252d},
    "ibc_130_officer_recency_weight_63d":           {"inputs": ["officer_buy_count"],                                                 "func": ibc_130_officer_recency_weight_63d},
    "ibc_131_director_recency_weight_63d":          {"inputs": ["director_buy_count"],                                                "func": ibc_131_director_recency_weight_63d},
    "ibc_132_buy_count_21d_rank_in_252d":           {"inputs": ["insider_buy_count"],                                                 "func": ibc_132_buy_count_21d_rank_in_252d},
    "ibc_133_buyers_21d_rank_in_252d":              {"inputs": ["insider_buyers"],                                                    "func": ibc_133_buyers_21d_rank_in_252d},
    "ibc_134_buyers_63d_rank_in_504d":              {"inputs": ["insider_buyers"],                                                    "func": ibc_134_buyers_63d_rank_in_504d},
    "ibc_135_buy_count_63d_rank_in_504d":           {"inputs": ["insider_buy_count"],                                                 "func": ibc_135_buy_count_63d_rank_in_504d},
    "ibc_136_role_diversity_score_63d":             {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],       "func": ibc_136_role_diversity_score_63d},
    "ibc_137_role_diversity_score_21d":             {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],       "func": ibc_137_role_diversity_score_21d},
    "ibc_138_burst_flag_21d_vs_252d_mean":          {"inputs": ["insider_buy_count"],                                                 "func": ibc_138_burst_flag_21d_vs_252d_mean},
    "ibc_139_burst_flag_63d_vs_252d_mean":          {"inputs": ["insider_buy_count"],                                                 "func": ibc_139_burst_flag_63d_vs_252d_mean},
    "ibc_140_buyer_burst_flag_21d":                 {"inputs": ["insider_buyers"],                                                    "func": ibc_140_buyer_burst_flag_21d},
    "ibc_141_buyer_burst_flag_63d":                 {"inputs": ["insider_buyers"],                                                    "func": ibc_141_buyer_burst_flag_63d},
    "ibc_142_cluster_quality_score_63d":            {"inputs": ["insider_buyers", "insider_buy_count", "officer_buy_count"],          "func": ibc_142_cluster_quality_score_63d},
    "ibc_143_buy_event_regularity_63d":             {"inputs": ["insider_buy_count"],                                                 "func": ibc_143_buy_event_regularity_63d},
    "ibc_144_officer_dir_combined_21d_burst":       {"inputs": ["officer_buy_count", "director_buy_count"],                           "func": ibc_144_officer_dir_combined_21d_burst},
    "ibc_145_cluster_present_and_accelerating":     {"inputs": ["insider_buyers"],                                                    "func": ibc_145_cluster_present_and_accelerating},
    "ibc_146_tenpct_active_flag_21d":               {"inputs": ["tenpct_buy_count"],                                                  "func": ibc_146_tenpct_active_flag_21d},
    "ibc_147_tenpct_active_flag_63d":               {"inputs": ["tenpct_buy_count"],                                                  "func": ibc_147_tenpct_active_flag_63d},
    "ibc_148_cumulative_cluster_weeks_1y":          {"inputs": ["insider_buy_count"],                                                 "func": ibc_148_cumulative_cluster_weeks_1y},
    "ibc_149_buyer_cluster_zscore_composite":       {"inputs": ["insider_buyers", "insider_buy_count"],                               "func": ibc_149_buyer_cluster_zscore_composite},
    "ibc_150_cluster_signal_strength_63d":          {"inputs": ["insider_buyers", "insider_buy_count", "officer_buy_count", "director_buy_count"], "func": ibc_150_cluster_signal_strength_63d},
    # --- New features 176-200 ---
    "ibc_176_ewm_buyers_span126":                   {"inputs": ["insider_buyers"],                                                    "func": ibc_176_ewm_buyers_span126},
    "ibc_177_ewm_buy_count_span126":                {"inputs": ["insider_buy_count"],                                                 "func": ibc_177_ewm_buy_count_span126},
    "ibc_178_ewm_officer_span63":                   {"inputs": ["officer_buy_count"],                                                 "func": ibc_178_ewm_officer_span63},
    "ibc_179_ewm_director_span63":                  {"inputs": ["director_buy_count"],                                                "func": ibc_179_ewm_director_span63},
    "ibc_180_ewm_tenpct_span21":                    {"inputs": ["tenpct_buy_count"],                                                  "func": ibc_180_ewm_tenpct_span21},
    "ibc_181_buyers_ewm_cross_63_252":              {"inputs": ["insider_buyers"],                                                    "func": ibc_181_buyers_ewm_cross_63_252},
    "ibc_182_buy_count_ewm_cross_63_252":           {"inputs": ["insider_buy_count"],                                                 "func": ibc_182_buy_count_ewm_cross_63_252},
    "ibc_183_officer_slope_21d":                    {"inputs": ["officer_buy_count"],                                                 "func": ibc_183_officer_slope_21d},
    "ibc_184_director_slope_21d":                   {"inputs": ["director_buy_count"],                                                "func": ibc_184_director_slope_21d},
    "ibc_185_buyer_count_126d_vs_prior_126d":       {"inputs": ["insider_buyers"],                                                    "func": ibc_185_buyer_count_126d_vs_prior_126d},
    "ibc_186_buy_count_126d_vs_prior_126d":         {"inputs": ["insider_buy_count"],                                                 "func": ibc_186_buy_count_126d_vs_prior_126d},
    "ibc_187_buyer_count_252d_pct_chg":             {"inputs": ["insider_buyers"],                                                    "func": ibc_187_buyer_count_252d_pct_chg},
    "ibc_188_buyer_concentration_126d":             {"inputs": ["insider_buyers", "insider_buy_count"],                               "func": ibc_188_buyer_concentration_126d},
    "ibc_189_officer_share_of_active_days_21d":     {"inputs": ["officer_buy_count", "insider_buy_count"],                           "func": ibc_189_officer_share_of_active_days_21d},
    "ibc_190_tenpct_share_of_active_days_63d":      {"inputs": ["tenpct_buy_count", "insider_buy_count"],                            "func": ibc_190_tenpct_share_of_active_days_63d},
    "ibc_191_buyer_std_21d":                        {"inputs": ["insider_buyers"],                                                    "func": ibc_191_buyer_std_21d},
    "ibc_192_buy_count_cv_21d":                     {"inputs": ["insider_buy_count"],                                                 "func": ibc_192_buy_count_cv_21d},
    "ibc_193_buy_count_cv_252d":                    {"inputs": ["insider_buy_count"],                                                 "func": ibc_193_buy_count_cv_252d},
    "ibc_194_buy_count_21d_rank_in_504d":           {"inputs": ["insider_buy_count"],                                                 "func": ibc_194_buy_count_21d_rank_in_504d},
    "ibc_195_buyers_63d_rank_in_252d":              {"inputs": ["insider_buyers"],                                                    "func": ibc_195_buyers_63d_rank_in_252d},
    "ibc_196_burst_flag_21d_vs_252d_mean_3x":       {"inputs": ["insider_buy_count"],                                                 "func": ibc_196_burst_flag_21d_vs_252d_mean_3x},
    "ibc_197_role_diversity_score_126d":            {"inputs": ["officer_buy_count", "director_buy_count", "tenpct_buy_count"],       "func": ibc_197_role_diversity_score_126d},
    "ibc_198_cluster_quality_score_21d":            {"inputs": ["insider_buyers", "insider_buy_count", "officer_buy_count"],          "func": ibc_198_cluster_quality_score_21d},
    "ibc_199_cumulative_cluster_weeks_2y":          {"inputs": ["insider_buy_count"],                                                 "func": ibc_199_cumulative_cluster_weeks_2y},
    "ibc_200_cluster_signal_strength_21d":          {"inputs": ["insider_buyers", "insider_buy_count", "officer_buy_count", "director_buy_count"], "func": ibc_200_cluster_signal_strength_21d},
}
