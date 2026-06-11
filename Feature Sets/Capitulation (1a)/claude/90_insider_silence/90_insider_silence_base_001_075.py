"""
90_insider_silence — Base Features 001-075
Domain: absence / withdrawal of insider activity (the dog that didn't bark)
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records. Each row represents one calendar/trading date. Most days
carry ZERO (no insider transaction filed on that date) — this zero-dominated
structure IS the signal domain of this folder. Series are NOT forward-filled.
Feature functions measure EMPTINESS, GAPS, and WITHDRAWAL — the inverse of
activity. Raw transaction frequency lives in folder 88; this folder is
specifically the SILENCE/ABSENCE domain.

Canonical field names (lowercase):
    insider_buy_count, insider_sell_count, insider_buy_shares, insider_sell_shares,
    insider_buy_value, insider_sell_value, insider_buyers, insider_sellers,
    officer_buy_count, officer_buy_value, officer_sell_value,
    director_buy_count, director_buy_value, director_sell_value,
    ceo_buy_value, cfo_buy_value, tenpct_buy_count, tenpct_buy_value,
    insider_shares_held

Primary fields for silence: insider_buy_count, insider_sell_count,
    insider_buyers, insider_sellers, insider_buy_value, officer_buy_count

Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
All functions use .shift(positive), .rolling(), or .expanding() — never
.shift(negative) or forward-looking access.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63    # 1 quarter
_TD_2Q    = 126
_TD_MO    = 21    # 1 month
_TD_WK    = 5     # 1 week
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero/NaN denominators become NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _days_since_last_nonzero(s: pd.Series) -> pd.Series:
    """
    For each position i, returns the number of rows since the last row where
    s > 0 (strictly positive). If no prior nonzero exists, returns i+1
    (full history). Uses a backward-only cummax trick — no loops.
    Result is always >= 0; equals len(s) at most on an all-zero series.
    """
    nonzero = (s > 0).astype(int)
    # Position index of each nonzero event; NaN elsewhere
    idx = pd.Series(np.where(nonzero.values, np.arange(len(s)), np.nan), index=s.index)
    # Forward-fill to carry last nonzero position forward
    last_pos = idx.ffill()
    row_num   = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    result    = row_num - last_pos
    # Where last_pos is still NaN (never saw nonzero yet), use row_num+1
    result    = result.where(last_pos.notna(), row_num + 1)
    return result


def _current_zero_run_length(s: pd.Series) -> pd.Series:
    """
    Current consecutive zero-run length: count of consecutive trailing zeros up
    to and including each row. Resets to 0 on any positive (nonzero) observation.
    An all-zero input returns [1,2,3,...,n].
    """
    is_zero = (s == 0).astype(int).values
    run     = np.zeros(len(s), dtype=float)
    for i in range(len(is_zero)):
        if i == 0:
            run[i] = float(is_zero[i])
        else:
            run[i] = (run[i - 1] + 1) * is_zero[i]
    return pd.Series(run, index=s.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Days since last transaction ---

def isl_001_days_since_last_buy(insider_buy_count: pd.Series) -> pd.Series:
    """Days since last insider buy transaction (any count > 0)."""
    return _days_since_last_nonzero(insider_buy_count)


def isl_002_days_since_last_sell(insider_sell_count: pd.Series) -> pd.Series:
    """Days since last insider sell transaction."""
    return _days_since_last_nonzero(insider_sell_count)


def isl_003_days_since_last_any_transaction(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Days since last insider transaction of any kind (buy or sell)."""
    any_txn = (insider_buy_count + insider_sell_count).clip(lower=0)
    return _days_since_last_nonzero(any_txn)


def isl_004_days_since_last_buyer_seen(insider_buyers: pd.Series) -> pd.Series:
    """Days since any individual insider buyer appeared."""
    return _days_since_last_nonzero(insider_buyers)


def isl_005_days_since_last_seller_seen(insider_sellers: pd.Series) -> pd.Series:
    """Days since any individual insider seller appeared."""
    return _days_since_last_nonzero(insider_sellers)


def isl_006_days_since_last_buy_value(insider_buy_value: pd.Series) -> pd.Series:
    """Days since last day with positive insider buy dollar value."""
    return _days_since_last_nonzero(insider_buy_value)


def isl_007_days_since_last_officer_buy(officer_buy_count: pd.Series) -> pd.Series:
    """Days since last officer buy transaction."""
    return _days_since_last_nonzero(officer_buy_count)


def isl_008_buy_silence_weeks(insider_buy_count: pd.Series) -> pd.Series:
    """Days since last buy, expressed in weeks (divided by 5)."""
    return _safe_div(_days_since_last_nonzero(insider_buy_count),
                     pd.Series(5.0, index=insider_buy_count.index))


def isl_009_buy_silence_months(insider_buy_count: pd.Series) -> pd.Series:
    """Days since last buy, expressed in months (divided by 21)."""
    return _safe_div(_days_since_last_nonzero(insider_buy_count),
                     pd.Series(21.0, index=insider_buy_count.index))


def isl_010_buy_silence_quarters(insider_buy_count: pd.Series) -> pd.Series:
    """Days since last buy, expressed in quarters (divided by 63)."""
    return _safe_div(_days_since_last_nonzero(insider_buy_count),
                     pd.Series(63.0, index=insider_buy_count.index))


def isl_011_any_txn_silence_months(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Days since last any transaction, in months."""
    any_txn = (insider_buy_count + insider_sell_count).clip(lower=0)
    return _safe_div(_days_since_last_nonzero(any_txn),
                     pd.Series(21.0, index=insider_buy_count.index))


def isl_012_officer_buy_silence_months(officer_buy_count: pd.Series) -> pd.Series:
    """Days since last officer buy, expressed in months."""
    return _safe_div(_days_since_last_nonzero(officer_buy_count),
                     pd.Series(21.0, index=officer_buy_count.index))


def isl_013_buy_silence_gt_1mo_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if no buy for more than 21 trading days."""
    return (_days_since_last_nonzero(insider_buy_count) > _TD_MO).astype(float)


def isl_014_buy_silence_gt_1qtr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if no buy for more than 63 trading days (1 quarter)."""
    return (_days_since_last_nonzero(insider_buy_count) > _TD_QTR).astype(float)


def isl_015_buy_silence_gt_1yr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if no buy for more than 252 trading days (1 year)."""
    return (_days_since_last_nonzero(insider_buy_count) > _TD_YEAR).astype(float)


# --- Group B (016-030): Current zero-run length ---

def isl_016_buy_zero_run_days(insider_buy_count: pd.Series) -> pd.Series:
    """Current consecutive zero-run length for insider buys."""
    return _current_zero_run_length(insider_buy_count)


def isl_017_sell_zero_run_days(insider_sell_count: pd.Series) -> pd.Series:
    """Current consecutive zero-run length for insider sells."""
    return _current_zero_run_length(insider_sell_count)


def isl_018_any_txn_zero_run_days(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Current consecutive zero-run for any insider transaction."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return _current_zero_run_length(combined)


def isl_019_buyer_zero_run_days(insider_buyers: pd.Series) -> pd.Series:
    """Consecutive days with zero distinct insider buyers."""
    return _current_zero_run_length(insider_buyers)


def isl_020_officer_buy_zero_run_days(officer_buy_count: pd.Series) -> pd.Series:
    """Consecutive days with zero officer buy transactions."""
    return _current_zero_run_length(officer_buy_count)


def isl_021_buy_zero_run_weeks(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run expressed in weeks."""
    return _safe_div(_current_zero_run_length(insider_buy_count),
                     pd.Series(5.0, index=insider_buy_count.index))


def isl_022_buy_zero_run_months(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run expressed in months."""
    return _safe_div(_current_zero_run_length(insider_buy_count),
                     pd.Series(21.0, index=insider_buy_count.index))


def isl_023_buy_zero_run_quarters(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run expressed in quarters."""
    return _safe_div(_current_zero_run_length(insider_buy_count),
                     pd.Series(63.0, index=insider_buy_count.index))


def isl_024_buy_value_zero_run_days(insider_buy_value: pd.Series) -> pd.Series:
    """Consecutive days with zero insider buy dollar value."""
    return _current_zero_run_length(insider_buy_value)


def isl_025_sell_zero_run_months(insider_sell_count: pd.Series) -> pd.Series:
    """Current sell zero-run expressed in months."""
    return _safe_div(_current_zero_run_length(insider_sell_count),
                     pd.Series(21.0, index=insider_sell_count.index))


def isl_026_buy_run_gt_1qtr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if current buy zero-run exceeds 63 days."""
    return (_current_zero_run_length(insider_buy_count) > _TD_QTR).astype(float)


def isl_027_buy_run_gt_1yr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if current buy zero-run exceeds 252 days."""
    return (_current_zero_run_length(insider_buy_count) > _TD_YEAR).astype(float)


def isl_028_any_txn_run_gt_1qtr_flag(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if any-transaction zero-run exceeds 63 days."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return (_current_zero_run_length(combined) > _TD_QTR).astype(float)


def isl_029_buyer_run_gt_2mo_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary: 1 if no buyer seen for more than 42 trading days (2 months)."""
    return (_current_zero_run_length(insider_buyers) > 42).astype(float)


def isl_030_officer_buy_run_gt_1yr_flag(officer_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if officer buy zero-run exceeds 1 year."""
    return (_current_zero_run_length(officer_buy_count) > _TD_YEAR).astype(float)


# --- Group C (031-045): Fraction of window with zero activity ---

def isl_031_buy_zero_frac_1mo(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 21 days with zero buy transactions."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_MO)


def isl_032_buy_zero_frac_1qtr(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero buy transactions."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_033_buy_zero_frac_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero buy transactions."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_034_sell_zero_frac_1qtr(insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero sell transactions."""
    zero = (insider_sell_count == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_035_any_txn_zero_frac_1mo(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 21 days with no insider transaction of any kind."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero = (combined == 0).astype(float)
    return _rolling_mean(zero, _TD_MO)


def isl_036_any_txn_zero_frac_1qtr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 63 days with no insider transaction."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero = (combined == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_037_any_txn_zero_frac_1yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with no insider transaction."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero = (combined == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_038_buyer_zero_frac_1qtr(insider_buyers: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero distinct buyers."""
    zero = (insider_buyers == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_039_officer_buy_zero_frac_1yr(officer_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero officer buy activity."""
    zero = (officer_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_040_buy_value_zero_frac_1qtr(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero insider buy dollar value."""
    zero = (insider_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_041_buy_zero_frac_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 504 days with zero buy transactions."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_2Y)


def isl_042_sell_zero_frac_1yr(insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero sell transactions."""
    zero = (insider_sell_count == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_043_buy_zero_frac_expanding(insider_buy_count: pd.Series) -> pd.Series:
    """Expanding-window fraction of all historical days with zero buys."""
    zero = (insider_buy_count == 0).astype(float)
    return zero.expanding(min_periods=1).mean()


def isl_044_sell_zero_frac_expanding(insider_sell_count: pd.Series) -> pd.Series:
    """Expanding-window fraction of all days with zero sells."""
    zero = (insider_sell_count == 0).astype(float)
    return zero.expanding(min_periods=1).mean()


def isl_045_buy_nonzero_frac_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days that had at least one buy (complement of silence)."""
    active = (insider_buy_count > 0).astype(float)
    return _rolling_mean(active, _TD_YEAR)


# --- Group D (046-060): Silence relative to ticker's own historical baseline ---

def isl_046_buy_silence_vs_hist_median(insider_buy_count: pd.Series) -> pd.Series:
    """
    Current buy zero-run minus the expanding median of all prior zero-run lengths.
    Positive = current silence exceeds the ticker's typical gap.
    """
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    return run - hist_med


def isl_047_buy_silence_vs_hist_mean(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run minus expanding mean of all prior gaps."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_avg = run.expanding(min_periods=2).mean()
    return run - hist_avg


def isl_048_buy_silence_pct_above_hist_median(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run as a fraction of historical median gap."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    return _safe_div(run, hist_med)


def isl_049_buy_silence_zscore_expanding(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of current buy zero-run relative to expanding mean/std."""
    run = _current_zero_run_length(insider_buy_count)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    return _safe_div(run - mu, sd)


def isl_050_longest_buy_silence_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Longest buy zero-run observed in the trailing 252 days."""
    run = _current_zero_run_length(insider_buy_count)
    return _rolling_max(run, _TD_YEAR)


def isl_051_longest_buy_silence_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Longest buy zero-run observed in the trailing 504 days."""
    run = _current_zero_run_length(insider_buy_count)
    return _rolling_max(run, _TD_2Y)


def isl_052_longest_buy_silence_expanding(insider_buy_count: pd.Series) -> pd.Series:
    """Longest buy zero-run ever observed (expanding max)."""
    run = _current_zero_run_length(insider_buy_count)
    return run.expanding(min_periods=1).max()


def isl_053_current_run_pct_of_longest(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run as fraction of the longest ever seen."""
    run     = _current_zero_run_length(insider_buy_count)
    longest = run.expanding(min_periods=1).max()
    return _safe_div(run, longest)


def isl_054_any_txn_silence_vs_hist_mean(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Any-transaction zero-run minus expanding historical mean."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    run      = _current_zero_run_length(combined)
    hist_avg = run.expanding(min_periods=2).mean()
    return run - hist_avg


def isl_055_buy_silence_rank_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of current buy zero-run within trailing 252-day distribution."""
    run = _current_zero_run_length(insider_buy_count)
    return run.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_056_any_txn_silence_rank_1yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of any-txn zero-run within trailing 252-day distribution."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    run      = _current_zero_run_length(combined)
    return run.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_057_buy_freq_drop_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """
    Drop in buy frequency: trailing 63-day mean minus trailing 252-day mean.
    Negative = recent silence relative to longer baseline.
    """
    recent = _rolling_mean(insider_buy_count, _TD_QTR)
    hist   = _rolling_mean(insider_buy_count, _TD_YEAR)
    return recent - hist


def isl_058_buy_freq_drop_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Trailing 63-day buy mean minus trailing 504-day mean."""
    recent = _rolling_mean(insider_buy_count, _TD_QTR)
    hist   = _rolling_mean(insider_buy_count, _TD_2Y)
    return recent - hist


def isl_059_sell_freq_drop_1yr(insider_sell_count: pd.Series) -> pd.Series:
    """Trailing 63-day sell mean minus trailing 252-day mean."""
    recent = _rolling_mean(insider_sell_count, _TD_QTR)
    hist   = _rolling_mean(insider_sell_count, _TD_YEAR)
    return recent - hist


def isl_060_buy_value_freq_drop_1yr(insider_buy_value: pd.Series) -> pd.Series:
    """Trailing 63-day buy-value mean minus trailing 252-day mean."""
    recent = _rolling_mean(insider_buy_value, _TD_QTR)
    hist   = _rolling_mean(insider_buy_value, _TD_YEAR)
    return recent - hist


# --- Group E (061-075): Withdrawal and quiet-period composite signals ---

def isl_061_quiet_period_score(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Composite quiet-period score: fraction of last 63 days with zero any-transaction
    plus fraction of last 252 days with zero any-transaction, averaged.
    Ranges 0-1; higher = deeper silence.
    """
    combined  = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero      = (combined == 0).astype(float)
    frac_qtr  = _rolling_mean(zero, _TD_QTR)
    frac_yr   = _rolling_mean(zero, _TD_YEAR)
    return (frac_qtr + frac_yr) / 2.0


def isl_062_buy_withdrawal_score(insider_buy_count: pd.Series) -> pd.Series:
    """
    Buy withdrawal score: fraction of last 252 days with zero buys, weighted by
    how long the current zero-run is (run / 252). Clipped to [0, 1].
    """
    zero_frac = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    run_norm  = (_current_zero_run_length(insider_buy_count) / _TD_YEAR).clip(upper=1.0)
    return ((zero_frac + run_norm) / 2.0).clip(upper=1.0)


def isl_063_no_buy_despite_depth_flag(insider_buy_count: pd.Series) -> pd.Series:
    """
    Proxy for 'no buys despite deep decline': 1 if buy zero-run exceeds 126 days.
    This captures extended silence when opportunistic buying would be expected.
    """
    return (_current_zero_run_length(insider_buy_count) > _TD_2Q).astype(float)


def isl_064_buy_to_sell_silence_ratio(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Ratio of buy-silence days to sell-silence days. >1 means buys are more silent
    than sells — a bearish divergence from a silence perspective.
    """
    buy_silence  = _days_since_last_nonzero(insider_buy_count)
    sell_silence = _days_since_last_nonzero(insider_sell_count)
    return _safe_div(buy_silence, sell_silence)


def isl_065_officer_buy_vs_buy_silence_gap(officer_buy_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Officer buy silence minus general insider buy silence (days)."""
    return _days_since_last_nonzero(officer_buy_count) - _days_since_last_nonzero(insider_buy_count)


def isl_066_buyer_count_1yr_sum(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct insider buyers seen in trailing 252 days (raw activity level)."""
    return _rolling_sum(insider_buyers, _TD_YEAR)


def isl_067_buy_active_days_1qtr(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days in last 63 days with at least one insider buy."""
    active = (insider_buy_count > 0).astype(float)
    return _rolling_sum(active, _TD_QTR)


def isl_068_buy_active_days_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days in last 252 days with at least one insider buy."""
    active = (insider_buy_count > 0).astype(float)
    return _rolling_sum(active, _TD_YEAR)


def isl_069_sell_active_days_1yr(insider_sell_count: pd.Series) -> pd.Series:
    """Count of days in last 252 days with at least one insider sell."""
    active = (insider_sell_count > 0).astype(float)
    return _rolling_sum(active, _TD_YEAR)


def isl_070_buy_active_days_collapse_ratio(insider_buy_count: pd.Series) -> pd.Series:
    """
    Ratio of buy-active days in last 63 days vs last 252 days (annualized).
    <1 = recent silence relative to longer history.
    """
    recent = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_buy_count > 0).astype(float), _TD_YEAR)
    return _safe_div(recent, hist)


def isl_071_silence_excess_months(insider_buy_count: pd.Series) -> pd.Series:
    """
    Excess silence in months: max(0, current_zero_run - expanding_median_gap) / 21.
    Measures how many months the current silence exceeds the typical gap.
    """
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0)
    return excess / 21.0


def isl_072_withdrawal_flag_both_sides(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    1 if both buy zero-run > 63 days AND sell zero-run > 63 days simultaneously.
    Total insider withdrawal from both buying and selling.
    """
    buy_silent  = (_current_zero_run_length(insider_buy_count)  > _TD_QTR).astype(float)
    sell_silent = (_current_zero_run_length(insider_sell_count) > _TD_QTR).astype(float)
    return (buy_silent * sell_silent)


def isl_073_buy_ewm_silence_score(insider_buy_count: pd.Series) -> pd.Series:
    """
    EWM-smoothed buy silence: EWM mean of (buy == 0) indicator with span=63.
    High value = sustained recent silence on a smoothed basis.
    """
    zero = (insider_buy_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR)


def isl_074_any_txn_ewm_silence_score(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed any-transaction silence with span=63."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero     = (combined == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR)


def isl_075_total_silence_composite(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """
    Composite silence score combining:
      - buy zero-run / 252 (capped at 1)
      - any-txn zero fraction over 252 days
      - buyer zero fraction over 252 days
    Average of the three; ranges 0-1.
    """
    run_score   = (_current_zero_run_length(insider_buy_count) / _TD_YEAR).clip(upper=1.0)
    txn_zero    = ((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float)
    frac_txn    = _rolling_mean(txn_zero, _TD_YEAR)
    buyer_zero  = (insider_buyers == 0).astype(float)
    frac_buyer  = _rolling_mean(buyer_zero, _TD_YEAR)
    return (run_score + frac_txn + frac_buyer) / 3.0


# ── Feature functions 151-175 ─────────────────────────────────────────────────

# --- Group K (151-163): EWM silence scores with varied spans ---

def isl_151_buy_ewm_silence_score_span21(insider_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed buy silence indicator with span=21 (short-term)."""
    zero = (insider_buy_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_MO)


def isl_152_buy_ewm_silence_score_span252(insider_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed buy silence indicator with span=252 (long-term)."""
    zero = (insider_buy_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_YEAR)


def isl_153_sell_ewm_silence_score_span63(insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed sell silence indicator with span=63."""
    zero = (insider_sell_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR)


def isl_154_any_txn_ewm_silence_score_span21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed any-transaction silence with span=21."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero = (combined == 0).astype(float)
    return _ewm_mean(zero, span=_TD_MO)


def isl_155_officer_buy_ewm_silence_span63(officer_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed officer buy silence with span=63."""
    zero = (officer_buy_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR)


def isl_156_buyer_ewm_silence_span63(insider_buyers: pd.Series) -> pd.Series:
    """EWM-smoothed buyer (distinct) zero indicator with span=63."""
    zero = (insider_buyers == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR)


def isl_157_buy_value_ewm_silence_span63(insider_buy_value: pd.Series) -> pd.Series:
    """EWM-smoothed buy-value silence indicator with span=63."""
    zero = (insider_buy_value == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR)


def isl_158_buy_ewm_vs_rolling_silence_diff(insider_buy_count: pd.Series) -> pd.Series:
    """EWM silence (span=63) minus rolling 63-day zero-frac. Divergence signal."""
    zero = (insider_buy_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_QTR) - _rolling_mean(zero, _TD_QTR)


def isl_159_buy_zero_run_ewm_span21(insider_buy_count: pd.Series) -> pd.Series:
    """EWM mean of current buy zero-run with span=21 (smoothed run length)."""
    run = _current_zero_run_length(insider_buy_count)
    return _ewm_mean(run, span=_TD_MO)


def isl_160_buy_zero_run_ewm_span63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM mean of current buy zero-run with span=63."""
    run = _current_zero_run_length(insider_buy_count)
    return _ewm_mean(run, span=_TD_QTR)


def isl_161_days_since_buy_ewm_span21(insider_buy_count: pd.Series) -> pd.Series:
    """EWM mean of days-since-last-buy with span=21 (smoothed silence days)."""
    dsn = _days_since_last_nonzero(insider_buy_count)
    return _ewm_mean(dsn, span=_TD_MO)


def isl_162_days_since_buy_ewm_span63(insider_buy_count: pd.Series) -> pd.Series:
    """EWM mean of days-since-last-buy with span=63."""
    dsn = _days_since_last_nonzero(insider_buy_count)
    return _ewm_mean(dsn, span=_TD_QTR)


def isl_163_ewm_composite_silence_score(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series) -> pd.Series:
    """Composite EWM silence: average of buy, any-txn, and buyer EWM silence (span=63)."""
    buy_z   = _ewm_mean((insider_buy_count == 0).astype(float), span=_TD_QTR)
    txn_z   = _ewm_mean(((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float), span=_TD_QTR)
    buyer_z = _ewm_mean((insider_buyers == 0).astype(float), span=_TD_QTR)
    return (buy_z + txn_z + buyer_z) / 3.0


# --- Group L (164-175): Rolling percentile ranks and median-based normalizations ---

def isl_164_buy_zero_run_rank_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of current buy zero-run within trailing 504-day distribution."""
    run = _current_zero_run_length(insider_buy_count)
    return run.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def isl_165_days_since_buy_rank_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of days-since-last-buy within trailing 252-day distribution."""
    dsn = _days_since_last_nonzero(insider_buy_count)
    return dsn.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_166_days_since_sell_rank_1yr(insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of days-since-last-sell within trailing 252-day distribution."""
    dsn = _days_since_last_nonzero(insider_sell_count)
    return dsn.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_167_any_txn_zero_frac_rank_1yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of any-txn 63-day zero-frac within trailing 252-day distribution."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    frac = _rolling_mean((combined == 0).astype(float), _TD_QTR)
    return frac.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_168_buy_zero_frac_1mo_rank_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of 21-day buy zero-frac within 252-day window."""
    frac = _rolling_mean((insider_buy_count == 0).astype(float), _TD_MO)
    return frac.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_169_buy_silence_vs_2yr_median(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run minus rolling 504-day median of that run."""
    run = _current_zero_run_length(insider_buy_count)
    return run - _rolling_median(run, _TD_2Y)


def isl_170_buy_silence_ratio_vs_2yr_median(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run divided by rolling 504-day median (ratio form)."""
    run = _current_zero_run_length(insider_buy_count)
    return _safe_div(run, _rolling_median(run, _TD_2Y))


def isl_171_buy_count_1qtr_rank_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of rolling 63-day buy count within trailing 504-day distribution."""
    cnt = _rolling_sum(insider_buy_count, _TD_QTR)
    return cnt.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def isl_172_buy_value_run_vs_hist_zscore(insider_buy_value: pd.Series) -> pd.Series:
    """Z-score of current buy-value zero-run relative to expanding mean/std."""
    run = _current_zero_run_length(insider_buy_value)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    return _safe_div(run - mu, sd)


def isl_173_sell_zero_run_rank_1yr(insider_sell_count: pd.Series) -> pd.Series:
    """Percentile rank of current sell zero-run within trailing 252-day distribution."""
    run = _current_zero_run_length(insider_sell_count)
    return run.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_174_officer_buy_run_rank_1yr(officer_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of officer buy zero-run within trailing 252-day distribution."""
    run = _current_zero_run_length(officer_buy_count)
    return run.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def isl_175_buy_zero_frac_3yr(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 756 days with zero buy transactions (3-year window)."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_3Y)


# ── Registry ──────────────────────────────────────────────────────────────────
INSIDER_SILENCE_REGISTRY_001_075 = {
    "isl_001_days_since_last_buy":              {"inputs": ["insider_buy_count"],                                         "func": isl_001_days_since_last_buy},
    "isl_002_days_since_last_sell":             {"inputs": ["insider_sell_count"],                                        "func": isl_002_days_since_last_sell},
    "isl_003_days_since_last_any_transaction":  {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_003_days_since_last_any_transaction},
    "isl_004_days_since_last_buyer_seen":       {"inputs": ["insider_buyers"],                                            "func": isl_004_days_since_last_buyer_seen},
    "isl_005_days_since_last_seller_seen":      {"inputs": ["insider_sellers"],                                           "func": isl_005_days_since_last_seller_seen},
    "isl_006_days_since_last_buy_value":        {"inputs": ["insider_buy_value"],                                         "func": isl_006_days_since_last_buy_value},
    "isl_007_days_since_last_officer_buy":      {"inputs": ["officer_buy_count"],                                         "func": isl_007_days_since_last_officer_buy},
    "isl_008_buy_silence_weeks":                {"inputs": ["insider_buy_count"],                                         "func": isl_008_buy_silence_weeks},
    "isl_009_buy_silence_months":               {"inputs": ["insider_buy_count"],                                         "func": isl_009_buy_silence_months},
    "isl_010_buy_silence_quarters":             {"inputs": ["insider_buy_count"],                                         "func": isl_010_buy_silence_quarters},
    "isl_011_any_txn_silence_months":           {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_011_any_txn_silence_months},
    "isl_012_officer_buy_silence_months":       {"inputs": ["officer_buy_count"],                                         "func": isl_012_officer_buy_silence_months},
    "isl_013_buy_silence_gt_1mo_flag":          {"inputs": ["insider_buy_count"],                                         "func": isl_013_buy_silence_gt_1mo_flag},
    "isl_014_buy_silence_gt_1qtr_flag":         {"inputs": ["insider_buy_count"],                                         "func": isl_014_buy_silence_gt_1qtr_flag},
    "isl_015_buy_silence_gt_1yr_flag":          {"inputs": ["insider_buy_count"],                                         "func": isl_015_buy_silence_gt_1yr_flag},
    "isl_016_buy_zero_run_days":                {"inputs": ["insider_buy_count"],                                         "func": isl_016_buy_zero_run_days},
    "isl_017_sell_zero_run_days":               {"inputs": ["insider_sell_count"],                                        "func": isl_017_sell_zero_run_days},
    "isl_018_any_txn_zero_run_days":            {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_018_any_txn_zero_run_days},
    "isl_019_buyer_zero_run_days":              {"inputs": ["insider_buyers"],                                            "func": isl_019_buyer_zero_run_days},
    "isl_020_officer_buy_zero_run_days":        {"inputs": ["officer_buy_count"],                                         "func": isl_020_officer_buy_zero_run_days},
    "isl_021_buy_zero_run_weeks":               {"inputs": ["insider_buy_count"],                                         "func": isl_021_buy_zero_run_weeks},
    "isl_022_buy_zero_run_months":              {"inputs": ["insider_buy_count"],                                         "func": isl_022_buy_zero_run_months},
    "isl_023_buy_zero_run_quarters":            {"inputs": ["insider_buy_count"],                                         "func": isl_023_buy_zero_run_quarters},
    "isl_024_buy_value_zero_run_days":          {"inputs": ["insider_buy_value"],                                         "func": isl_024_buy_value_zero_run_days},
    "isl_025_sell_zero_run_months":             {"inputs": ["insider_sell_count"],                                        "func": isl_025_sell_zero_run_months},
    "isl_026_buy_run_gt_1qtr_flag":             {"inputs": ["insider_buy_count"],                                         "func": isl_026_buy_run_gt_1qtr_flag},
    "isl_027_buy_run_gt_1yr_flag":              {"inputs": ["insider_buy_count"],                                         "func": isl_027_buy_run_gt_1yr_flag},
    "isl_028_any_txn_run_gt_1qtr_flag":         {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_028_any_txn_run_gt_1qtr_flag},
    "isl_029_buyer_run_gt_2mo_flag":            {"inputs": ["insider_buyers"],                                            "func": isl_029_buyer_run_gt_2mo_flag},
    "isl_030_officer_buy_run_gt_1yr_flag":      {"inputs": ["officer_buy_count"],                                         "func": isl_030_officer_buy_run_gt_1yr_flag},
    "isl_031_buy_zero_frac_1mo":                {"inputs": ["insider_buy_count"],                                         "func": isl_031_buy_zero_frac_1mo},
    "isl_032_buy_zero_frac_1qtr":               {"inputs": ["insider_buy_count"],                                         "func": isl_032_buy_zero_frac_1qtr},
    "isl_033_buy_zero_frac_1yr":                {"inputs": ["insider_buy_count"],                                         "func": isl_033_buy_zero_frac_1yr},
    "isl_034_sell_zero_frac_1qtr":              {"inputs": ["insider_sell_count"],                                        "func": isl_034_sell_zero_frac_1qtr},
    "isl_035_any_txn_zero_frac_1mo":            {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_035_any_txn_zero_frac_1mo},
    "isl_036_any_txn_zero_frac_1qtr":           {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_036_any_txn_zero_frac_1qtr},
    "isl_037_any_txn_zero_frac_1yr":            {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_037_any_txn_zero_frac_1yr},
    "isl_038_buyer_zero_frac_1qtr":             {"inputs": ["insider_buyers"],                                            "func": isl_038_buyer_zero_frac_1qtr},
    "isl_039_officer_buy_zero_frac_1yr":        {"inputs": ["officer_buy_count"],                                         "func": isl_039_officer_buy_zero_frac_1yr},
    "isl_040_buy_value_zero_frac_1qtr":         {"inputs": ["insider_buy_value"],                                         "func": isl_040_buy_value_zero_frac_1qtr},
    "isl_041_buy_zero_frac_2yr":                {"inputs": ["insider_buy_count"],                                         "func": isl_041_buy_zero_frac_2yr},
    "isl_042_sell_zero_frac_1yr":               {"inputs": ["insider_sell_count"],                                        "func": isl_042_sell_zero_frac_1yr},
    "isl_043_buy_zero_frac_expanding":          {"inputs": ["insider_buy_count"],                                         "func": isl_043_buy_zero_frac_expanding},
    "isl_044_sell_zero_frac_expanding":         {"inputs": ["insider_sell_count"],                                        "func": isl_044_sell_zero_frac_expanding},
    "isl_045_buy_nonzero_frac_1yr":             {"inputs": ["insider_buy_count"],                                         "func": isl_045_buy_nonzero_frac_1yr},
    "isl_046_buy_silence_vs_hist_median":       {"inputs": ["insider_buy_count"],                                         "func": isl_046_buy_silence_vs_hist_median},
    "isl_047_buy_silence_vs_hist_mean":         {"inputs": ["insider_buy_count"],                                         "func": isl_047_buy_silence_vs_hist_mean},
    "isl_048_buy_silence_pct_above_hist_median":{"inputs": ["insider_buy_count"],                                         "func": isl_048_buy_silence_pct_above_hist_median},
    "isl_049_buy_silence_zscore_expanding":     {"inputs": ["insider_buy_count"],                                         "func": isl_049_buy_silence_zscore_expanding},
    "isl_050_longest_buy_silence_1yr":          {"inputs": ["insider_buy_count"],                                         "func": isl_050_longest_buy_silence_1yr},
    "isl_051_longest_buy_silence_2yr":          {"inputs": ["insider_buy_count"],                                         "func": isl_051_longest_buy_silence_2yr},
    "isl_052_longest_buy_silence_expanding":    {"inputs": ["insider_buy_count"],                                         "func": isl_052_longest_buy_silence_expanding},
    "isl_053_current_run_pct_of_longest":       {"inputs": ["insider_buy_count"],                                         "func": isl_053_current_run_pct_of_longest},
    "isl_054_any_txn_silence_vs_hist_mean":     {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_054_any_txn_silence_vs_hist_mean},
    "isl_055_buy_silence_rank_1yr":             {"inputs": ["insider_buy_count"],                                         "func": isl_055_buy_silence_rank_1yr},
    "isl_056_any_txn_silence_rank_1yr":         {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_056_any_txn_silence_rank_1yr},
    "isl_057_buy_freq_drop_1yr":                {"inputs": ["insider_buy_count"],                                         "func": isl_057_buy_freq_drop_1yr},
    "isl_058_buy_freq_drop_2yr":                {"inputs": ["insider_buy_count"],                                         "func": isl_058_buy_freq_drop_2yr},
    "isl_059_sell_freq_drop_1yr":               {"inputs": ["insider_sell_count"],                                        "func": isl_059_sell_freq_drop_1yr},
    "isl_060_buy_value_freq_drop_1yr":          {"inputs": ["insider_buy_value"],                                         "func": isl_060_buy_value_freq_drop_1yr},
    "isl_061_quiet_period_score":               {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_061_quiet_period_score},
    "isl_062_buy_withdrawal_score":             {"inputs": ["insider_buy_count"],                                         "func": isl_062_buy_withdrawal_score},
    "isl_063_no_buy_despite_depth_flag":        {"inputs": ["insider_buy_count"],                                         "func": isl_063_no_buy_despite_depth_flag},
    "isl_064_buy_to_sell_silence_ratio":        {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_064_buy_to_sell_silence_ratio},
    "isl_065_officer_buy_vs_buy_silence_gap":   {"inputs": ["officer_buy_count", "insider_buy_count"],                   "func": isl_065_officer_buy_vs_buy_silence_gap},
    "isl_066_buyer_count_1yr_sum":              {"inputs": ["insider_buyers"],                                            "func": isl_066_buyer_count_1yr_sum},
    "isl_067_buy_active_days_1qtr":             {"inputs": ["insider_buy_count"],                                         "func": isl_067_buy_active_days_1qtr},
    "isl_068_buy_active_days_1yr":              {"inputs": ["insider_buy_count"],                                         "func": isl_068_buy_active_days_1yr},
    "isl_069_sell_active_days_1yr":             {"inputs": ["insider_sell_count"],                                        "func": isl_069_sell_active_days_1yr},
    "isl_070_buy_active_days_collapse_ratio":   {"inputs": ["insider_buy_count"],                                         "func": isl_070_buy_active_days_collapse_ratio},
    "isl_071_silence_excess_months":            {"inputs": ["insider_buy_count"],                                         "func": isl_071_silence_excess_months},
    "isl_072_withdrawal_flag_both_sides":       {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_072_withdrawal_flag_both_sides},
    "isl_073_buy_ewm_silence_score":            {"inputs": ["insider_buy_count"],                                         "func": isl_073_buy_ewm_silence_score},
    "isl_074_any_txn_ewm_silence_score":        {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_074_any_txn_ewm_silence_score},
    "isl_075_total_silence_composite":          {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"], "func": isl_075_total_silence_composite},
    "isl_151_buy_ewm_silence_score_span21":     {"inputs": ["insider_buy_count"],                                         "func": isl_151_buy_ewm_silence_score_span21},
    "isl_152_buy_ewm_silence_score_span252":    {"inputs": ["insider_buy_count"],                                         "func": isl_152_buy_ewm_silence_score_span252},
    "isl_153_sell_ewm_silence_score_span63":    {"inputs": ["insider_sell_count"],                                        "func": isl_153_sell_ewm_silence_score_span63},
    "isl_154_any_txn_ewm_silence_score_span21": {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_154_any_txn_ewm_silence_score_span21},
    "isl_155_officer_buy_ewm_silence_span63":   {"inputs": ["officer_buy_count"],                                         "func": isl_155_officer_buy_ewm_silence_span63},
    "isl_156_buyer_ewm_silence_span63":         {"inputs": ["insider_buyers"],                                            "func": isl_156_buyer_ewm_silence_span63},
    "isl_157_buy_value_ewm_silence_span63":     {"inputs": ["insider_buy_value"],                                         "func": isl_157_buy_value_ewm_silence_span63},
    "isl_158_buy_ewm_vs_rolling_silence_diff":  {"inputs": ["insider_buy_count"],                                         "func": isl_158_buy_ewm_vs_rolling_silence_diff},
    "isl_159_buy_zero_run_ewm_span21":          {"inputs": ["insider_buy_count"],                                         "func": isl_159_buy_zero_run_ewm_span21},
    "isl_160_buy_zero_run_ewm_span63":          {"inputs": ["insider_buy_count"],                                         "func": isl_160_buy_zero_run_ewm_span63},
    "isl_161_days_since_buy_ewm_span21":        {"inputs": ["insider_buy_count"],                                         "func": isl_161_days_since_buy_ewm_span21},
    "isl_162_days_since_buy_ewm_span63":        {"inputs": ["insider_buy_count"],                                         "func": isl_162_days_since_buy_ewm_span63},
    "isl_163_ewm_composite_silence_score":      {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers"], "func": isl_163_ewm_composite_silence_score},
    "isl_164_buy_zero_run_rank_2yr":            {"inputs": ["insider_buy_count"],                                         "func": isl_164_buy_zero_run_rank_2yr},
    "isl_165_days_since_buy_rank_1yr":          {"inputs": ["insider_buy_count"],                                         "func": isl_165_days_since_buy_rank_1yr},
    "isl_166_days_since_sell_rank_1yr":         {"inputs": ["insider_sell_count"],                                        "func": isl_166_days_since_sell_rank_1yr},
    "isl_167_any_txn_zero_frac_rank_1yr":       {"inputs": ["insider_buy_count", "insider_sell_count"],                   "func": isl_167_any_txn_zero_frac_rank_1yr},
    "isl_168_buy_zero_frac_1mo_rank_1yr":       {"inputs": ["insider_buy_count"],                                         "func": isl_168_buy_zero_frac_1mo_rank_1yr},
    "isl_169_buy_silence_vs_2yr_median":        {"inputs": ["insider_buy_count"],                                         "func": isl_169_buy_silence_vs_2yr_median},
    "isl_170_buy_silence_ratio_vs_2yr_median":  {"inputs": ["insider_buy_count"],                                         "func": isl_170_buy_silence_ratio_vs_2yr_median},
    "isl_171_buy_count_1qtr_rank_2yr":          {"inputs": ["insider_buy_count"],                                         "func": isl_171_buy_count_1qtr_rank_2yr},
    "isl_172_buy_value_run_vs_hist_zscore":     {"inputs": ["insider_buy_value"],                                         "func": isl_172_buy_value_run_vs_hist_zscore},
    "isl_173_sell_zero_run_rank_1yr":           {"inputs": ["insider_sell_count"],                                        "func": isl_173_sell_zero_run_rank_1yr},
    "isl_174_officer_buy_run_rank_1yr":         {"inputs": ["officer_buy_count"],                                         "func": isl_174_officer_buy_run_rank_1yr},
    "isl_175_buy_zero_frac_3yr":                {"inputs": ["insider_buy_count"],                                         "func": isl_175_buy_zero_frac_3yr},
}
