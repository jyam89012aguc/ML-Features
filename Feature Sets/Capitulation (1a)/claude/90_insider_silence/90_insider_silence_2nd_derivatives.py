"""
90_insider_silence — 2nd-Derivative Features 001-025
Domain: rate-of-change of base insider-silence features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records. Most days are ZERO (no transactions filed) — NOT
forward-filled. This file computes first differences, slopes, and pct-changes
of base silence concepts. Because the underlying series are event-driven and
sparse, 2nd-derivative series will themselves be sparse/stepwise on the daily
index — this is correct and expected.
All functions use .shift(positive), .rolling(), or .expanding() — never
.shift(negative) or forward-looking access.

Trading-day constants: 252/yr, 63/qtr, 21/mo, 5/wk.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_QTR   = 63
_TD_2Q    = 126
_TD_MO    = 21
_TD_WK    = 5
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero/NaN denominators become NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


# ── Base-concept inline helpers (self-contained, no cross-file imports) ───────

def _days_since_last_nonzero(s: pd.Series) -> pd.Series:
    nonzero  = (s > 0).astype(int)
    idx      = pd.Series(np.where(nonzero.values, np.arange(len(s)), np.nan), index=s.index)
    last_pos = idx.ffill()
    row_num  = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    result   = row_num - last_pos
    result   = result.where(last_pos.notna(), row_num + 1)
    return result


def _current_zero_run_length(s: pd.Series) -> pd.Series:
    is_zero = (s == 0).astype(int).values
    run     = np.zeros(len(s), dtype=float)
    for i in range(len(is_zero)):
        if i == 0:
            run[i] = float(is_zero[i])
        else:
            run[i] = (run[i - 1] + 1) * is_zero[i]
    return pd.Series(run, index=s.index)


def _buy_zero_frac_1qtr(s: pd.Series) -> pd.Series:
    return _rolling_mean((s == 0).astype(float), _TD_QTR)


def _buy_zero_frac_1yr(s: pd.Series) -> pd.Series:
    return _rolling_mean((s == 0).astype(float), _TD_YEAR)


def _buy_count_rolling_qtr(s: pd.Series) -> pd.Series:
    return _rolling_sum(s, _TD_QTR)


def _buy_count_rolling_yr(s: pd.Series) -> pd.Series:
    return _rolling_sum(s, _TD_YEAR)


# ── 2nd-Derivative Feature functions 001-025 ─────────────────────────────────

def isl_drv2_001_days_since_buy_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day first difference of 'days since last buy'. Positive = silence growing."""
    base = _days_since_last_nonzero(insider_buy_count)
    return base - base.shift(_TD_MO)


def isl_drv2_002_days_since_buy_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day first difference of 'days since last buy'."""
    base = _days_since_last_nonzero(insider_buy_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_003_buy_zero_run_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in current buy zero-run length."""
    base = _current_zero_run_length(insider_buy_count)
    return base - base.shift(_TD_MO)


def isl_drv2_004_buy_zero_run_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in current buy zero-run length."""
    base = _current_zero_run_length(insider_buy_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_005_buy_zero_frac_1qtr_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in rolling 63-day buy zero-fraction."""
    base = _buy_zero_frac_1qtr(insider_buy_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_006_buy_zero_frac_1yr_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in rolling 252-day buy zero-fraction."""
    base = _buy_zero_frac_1yr(insider_buy_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_007_buy_zero_frac_1yr_diff_252(insider_buy_count: pd.Series) -> pd.Series:
    """252-day change in rolling 252-day buy zero-fraction (YoY acceleration)."""
    base = _buy_zero_frac_1yr(insider_buy_count)
    return base - base.shift(_TD_YEAR)


def isl_drv2_008_buy_count_qtr_pct_change_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day pct-change of rolling 63-day buy count. Negative = collapsing activity."""
    base = _buy_count_rolling_qtr(insider_buy_count)
    prior = base.shift(_TD_MO)
    return _safe_div(base - prior, prior.abs())


def isl_drv2_009_buy_count_yr_pct_change_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day pct-change of rolling 252-day buy count."""
    base  = _buy_count_rolling_yr(insider_buy_count)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs())


def isl_drv2_010_sell_zero_frac_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in rolling 63-day sell zero-fraction."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_QTR)


def isl_drv2_011_days_since_sell_diff_21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day change in days-since-last-sell."""
    base = _days_since_last_nonzero(insider_sell_count)
    return base - base.shift(_TD_MO)


def isl_drv2_012_any_txn_zero_frac_1qtr_diff_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in any-transaction 63-day zero-fraction."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _rolling_mean((combined == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_QTR)


def isl_drv2_013_quiet_score_slope_21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Linear slope (OLS) of quiet-period score over the last 21 days."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero     = (combined == 0).astype(float)
    frac_qtr = _rolling_mean(zero, _TD_QTR)
    frac_yr  = _rolling_mean(zero, _TD_YEAR)
    score    = (frac_qtr + frac_yr) / 2.0
    x        = pd.Series(np.arange(len(score), dtype=float), index=score.index)
    x_roll   = _rolling_mean(x, _TD_MO)
    y_roll   = _rolling_mean(score, _TD_MO)
    cov      = _rolling_mean((x - x_roll) * (score - y_roll), _TD_MO)
    var_x    = _rolling_mean((x - x_roll) ** 2, _TD_MO)
    return _safe_div(cov, var_x)


def isl_drv2_014_buy_withdrawal_score_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in buy withdrawal score."""
    zero_frac = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    run_norm  = (_current_zero_run_length(insider_buy_count) / _TD_YEAR).clip(upper=1.0)
    score     = ((zero_frac + run_norm) / 2.0).clip(upper=1.0)
    return score - score.shift(_TD_QTR)


def isl_drv2_015_officer_buy_zero_frac_diff_63(officer_buy_count: pd.Series) -> pd.Series:
    """63-day change in officer-buy 252-day zero-fraction."""
    base = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_016_buyer_zero_frac_diff_63(insider_buyers: pd.Series) -> pd.Series:
    """63-day change in buyers zero-fraction (63-day window)."""
    base = _rolling_mean((insider_buyers == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_QTR)


def isl_drv2_017_ceo_buy_zero_run_diff_63(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day change in CEO buy zero-run."""
    base = _current_zero_run_length(ceo_buy_value)
    return base - base.shift(_TD_QTR)


def isl_drv2_018_silence_excess_months_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in silence-excess-months feature."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0) / 21.0
    return excess - excess.shift(_TD_MO)


def isl_drv2_019_buy_silence_zscore_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in expanding-zscore of buy zero-run."""
    run = _current_zero_run_length(insider_buy_count)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    z   = _safe_div(run - mu, sd)
    return z - z.shift(_TD_MO)


def isl_drv2_020_buy_count_1yr_rolling_slope(insider_buy_count: pd.Series) -> pd.Series:
    """
    Slope of rolling 252-day buy count over the last 63 days (OLS regression
    of the rolling-sum series on time). Negative = count trend falling.
    """
    y     = _buy_count_rolling_yr(insider_buy_count)
    x     = pd.Series(np.arange(len(y), dtype=float), index=y.index)
    x_bar = _rolling_mean(x, _TD_QTR)
    y_bar = _rolling_mean(y, _TD_QTR)
    cov   = _rolling_mean((x - x_bar) * (y - y_bar), _TD_QTR)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_QTR)
    return _safe_div(cov, var_x)


def isl_drv2_021_tenpct_buy_zero_frac_diff_63(tenpct_buy_count: pd.Series) -> pd.Series:
    """63-day change in 10%-holder buy 252-day zero-fraction."""
    base = _rolling_mean((tenpct_buy_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_022_sell_zero_run_diff_21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day change in sell zero-run length."""
    base = _current_zero_run_length(insider_sell_count)
    return base - base.shift(_TD_MO)


def isl_drv2_023_buy_active_days_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in rolling 252-day count of buy-active days."""
    base = _rolling_sum((insider_buy_count > 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_024_grand_silence_composite_diff_63(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buyers: pd.Series,
    officer_buy_count: pd.Series
) -> pd.Series:
    """63-day change in the grand silence composite score."""
    buy_zero   = (insider_buy_count  == 0).astype(float)
    txn_zero   = ((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float)
    buyer_zero = (insider_buyers    == 0).astype(float)
    offr_zero  = (officer_buy_count == 0).astype(float)
    score = (_rolling_mean(buy_zero, _TD_YEAR) + _rolling_mean(txn_zero, _TD_YEAR) +
             _rolling_mean(buyer_zero, _TD_YEAR) + _rolling_mean(offr_zero, _TD_YEAR)) / 4.0
    return score - score.shift(_TD_QTR)


def isl_drv2_025_buy_gap_ratio_acceleration(insider_buy_count: pd.Series) -> pd.Series:
    """
    63-day change in (buy zero-frac 63-day / buy zero-frac 252-day) ratio.
    Rising positive = short-term silence accelerating vs long-term baseline.
    """
    zero     = (insider_buy_count == 0).astype(float)
    ratio    = _safe_div(_rolling_mean(zero, _TD_QTR), _rolling_mean(zero, _TD_YEAR))
    return ratio - ratio.shift(_TD_QTR)


# ── 2nd-Derivative Feature functions 026-075 ──────────────────────────────────

def isl_drv2_026_days_since_buy_diff_5(insider_buy_count: pd.Series) -> pd.Series:
    """5-day first difference of days-since-last-buy. Captures week-on-week silence shift."""
    base = _days_since_last_nonzero(insider_buy_count)
    return base - base.shift(_TD_WK)


def isl_drv2_027_buy_zero_run_diff_5(insider_buy_count: pd.Series) -> pd.Series:
    """5-day change in current buy zero-run length."""
    base = _current_zero_run_length(insider_buy_count)
    return base - base.shift(_TD_WK)


def isl_drv2_028_buy_zero_frac_1mo_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in 21-day rolling buy zero-fraction."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_MO)
    return base - base.shift(_TD_MO)


def isl_drv2_029_buy_zero_frac_1qtr_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in rolling 63-day buy zero-fraction."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_MO)


def isl_drv2_030_buy_zero_frac_2yr_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in 504-day rolling buy zero-fraction."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_2Y)
    return base - base.shift(_TD_QTR)


def isl_drv2_031_sell_zero_run_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in current sell zero-run length."""
    base = _current_zero_run_length(insider_sell_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_032_sell_zero_frac_1yr_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in 252-day rolling sell zero-fraction."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_033_days_since_sell_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day first difference of days-since-last-sell."""
    base = _days_since_last_nonzero(insider_sell_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_034_buyer_zero_frac_diff_21(insider_buyers: pd.Series) -> pd.Series:
    """21-day change in 63-day buyer zero-fraction."""
    base = _rolling_mean((insider_buyers == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_MO)


def isl_drv2_035_buyer_zero_frac_1yr_diff_63(insider_buyers: pd.Series) -> pd.Series:
    """63-day change in 252-day buyer zero-fraction."""
    base = _rolling_mean((insider_buyers == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_036_officer_buy_zero_frac_diff_21(officer_buy_count: pd.Series) -> pd.Series:
    """21-day change in 252-day officer buy zero-fraction."""
    base = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_MO)


def isl_drv2_037_officer_buy_run_diff_21(officer_buy_count: pd.Series) -> pd.Series:
    """21-day change in officer buy zero-run length."""
    base = _current_zero_run_length(officer_buy_count)
    return base - base.shift(_TD_MO)


def isl_drv2_038_officer_buy_run_diff_63(officer_buy_count: pd.Series) -> pd.Series:
    """63-day change in officer buy zero-run length."""
    base = _current_zero_run_length(officer_buy_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_039_ceo_buy_zero_frac_1yr_diff_63(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day change in 252-day CEO buy zero-fraction."""
    base = _rolling_mean((ceo_buy_value == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_040_ceo_buy_run_diff_21(ceo_buy_value: pd.Series) -> pd.Series:
    """21-day change in CEO buy zero-run length."""
    base = _current_zero_run_length(ceo_buy_value)
    return base - base.shift(_TD_MO)


def isl_drv2_041_tenpct_buy_run_diff_21(tenpct_buy_count: pd.Series) -> pd.Series:
    """21-day change in 10%-holder buy zero-run length."""
    base = _current_zero_run_length(tenpct_buy_count)
    return base - base.shift(_TD_MO)


def isl_drv2_042_tenpct_buy_run_diff_63(tenpct_buy_count: pd.Series) -> pd.Series:
    """63-day change in 10%-holder buy zero-run length."""
    base = _current_zero_run_length(tenpct_buy_count)
    return base - base.shift(_TD_QTR)


def isl_drv2_043_any_txn_zero_frac_1yr_diff_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in 252-day any-transaction zero-fraction."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _rolling_mean((combined == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_044_any_txn_zero_run_diff_21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day change in any-transaction zero-run length."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _current_zero_run_length(combined)
    return base - base.shift(_TD_MO)


def isl_drv2_045_any_txn_zero_run_diff_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in any-transaction zero-run length."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _current_zero_run_length(combined)
    return base - base.shift(_TD_QTR)


def isl_drv2_046_buy_active_days_1qtr_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in rolling 63-day count of buy-active days."""
    base = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_QTR)


def isl_drv2_047_sell_active_days_1yr_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in rolling 252-day count of sell-active days."""
    base = _rolling_sum((insider_sell_count > 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_048_buy_count_sum_1mo_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in rolling 21-day buy count sum."""
    base = _rolling_sum(insider_buy_count, _TD_MO)
    return base - base.shift(_TD_MO)


def isl_drv2_049_buy_count_sum_1qtr_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in rolling 63-day buy count sum."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    return base - base.shift(_TD_MO)


def isl_drv2_050_buy_value_zero_frac_1yr_diff_63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day change in 252-day buy-value zero-fraction."""
    base = _rolling_mean((insider_buy_value == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_051_buy_silence_zscore_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in expanding buy silence z-score."""
    run = _current_zero_run_length(insider_buy_count)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    z   = _safe_div(run - mu, sd)
    return z - z.shift(_TD_QTR)


def isl_drv2_052_silence_excess_months_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in silence-excess-months feature."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0) / 21.0
    return excess - excess.shift(_TD_QTR)


def isl_drv2_053_buy_withdrawal_score_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in buy withdrawal score."""
    zero_frac = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    run_norm  = (_current_zero_run_length(insider_buy_count) / _TD_YEAR).clip(upper=1.0)
    score     = ((zero_frac + run_norm) / 2.0).clip(upper=1.0)
    return score - score.shift(_TD_MO)


def isl_drv2_054_quiet_score_slope_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """OLS slope of quiet-period score over the last 63 days."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero     = (combined == 0).astype(float)
    score    = (_rolling_mean(zero, _TD_QTR) + _rolling_mean(zero, _TD_YEAR)) / 2.0
    x        = pd.Series(np.arange(len(score), dtype=float), index=score.index)
    x_bar    = _rolling_mean(x, _TD_QTR)
    y_bar    = _rolling_mean(score, _TD_QTR)
    cov      = _rolling_mean((x - x_bar) * (score - y_bar), _TD_QTR)
    var_x    = _rolling_mean((x - x_bar) ** 2, _TD_QTR)
    return _safe_div(cov, var_x)


def isl_drv2_055_buy_count_1yr_slope_21(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of rolling 252-day buy count over 21 days."""
    y     = _rolling_sum(insider_buy_count, _TD_YEAR)
    x     = pd.Series(np.arange(len(y), dtype=float), index=y.index)
    x_bar = _rolling_mean(x, _TD_MO)
    y_bar = _rolling_mean(y, _TD_MO)
    cov   = _rolling_mean((x - x_bar) * (y - y_bar), _TD_MO)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    return _safe_div(cov, var_x)


def isl_drv2_056_buy_zero_frac_1yr_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change in 252-day rolling buy zero-fraction (short-term acceleration)."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_MO)


def isl_drv2_057_sell_count_sum_1qtr_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in rolling 63-day sell count sum."""
    base = _rolling_sum(insider_sell_count, _TD_QTR)
    return base - base.shift(_TD_QTR)


def isl_drv2_058_sell_count_sum_1yr_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in rolling 252-day sell count sum."""
    base = _rolling_sum(insider_sell_count, _TD_YEAR)
    return base - base.shift(_TD_QTR)


def isl_drv2_059_buy_count_yr_pct_change_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day pct-change of rolling 252-day buy count."""
    base  = _rolling_sum(insider_buy_count, _TD_YEAR)
    prior = base.shift(_TD_MO)
    return _safe_div(base - prior, prior.abs())


def isl_drv2_060_sell_count_yr_pct_change_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day pct-change of rolling 252-day sell count."""
    base  = _rolling_sum(insider_sell_count, _TD_YEAR)
    prior = base.shift(_TD_QTR)
    return _safe_div(base - prior, prior.abs())


def isl_drv2_061_grand_silence_diff_21(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series, officer_buy_count: pd.Series) -> pd.Series:
    """21-day change in the grand silence composite score."""
    buy_zero   = (insider_buy_count == 0).astype(float)
    txn_zero   = ((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float)
    buyer_zero = (insider_buyers == 0).astype(float)
    offr_zero  = (officer_buy_count == 0).astype(float)
    score = (_rolling_mean(buy_zero, _TD_YEAR) + _rolling_mean(txn_zero, _TD_YEAR) +
             _rolling_mean(buyer_zero, _TD_YEAR) + _rolling_mean(offr_zero, _TD_YEAR)) / 4.0
    return score - score.shift(_TD_MO)


def isl_drv2_062_buy_silence_rank_1yr_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in the 252-day percentile rank of buy zero-run."""
    run  = _current_zero_run_length(insider_buy_count)
    rank = run.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)
    return rank - rank.shift(_TD_QTR)


def isl_drv2_063_buy_zero_frac_1qtr_slope_21(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of 63-day buy zero-frac over last 21 days."""
    y     = _rolling_mean((insider_buy_count == 0).astype(float), _TD_QTR)
    x     = pd.Series(np.arange(len(y), dtype=float), index=y.index)
    x_bar = _rolling_mean(x, _TD_MO)
    y_bar = _rolling_mean(y, _TD_MO)
    cov   = _rolling_mean((x - x_bar) * (y - y_bar), _TD_MO)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    return _safe_div(cov, var_x)


def isl_drv2_064_sell_zero_frac_1qtr_diff_21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day change in rolling 63-day sell zero-fraction."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_MO)


def isl_drv2_065_buyer_collapse_ratio_diff_63(insider_buyers: pd.Series) -> pd.Series:
    """63-day change in buyer collapse ratio (63d annualized / 252d)."""
    recent = _rolling_sum(insider_buyers, _TD_QTR) * 4.0
    hist   = _rolling_sum(insider_buyers, _TD_YEAR)
    ratio  = _safe_div(recent, hist)
    return ratio - ratio.shift(_TD_QTR)


def isl_drv2_066_sell_active_days_collapse_diff_63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in sell-active-days collapse ratio."""
    recent = _rolling_sum((insider_sell_count > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_sell_count > 0).astype(float), _TD_YEAR)
    ratio  = _safe_div(recent, hist)
    return ratio - ratio.shift(_TD_QTR)


def isl_drv2_067_buy_value_zero_frac_1qtr_diff_63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day change in 63-day buy-value zero-fraction."""
    base = _rolling_mean((insider_buy_value == 0).astype(float), _TD_QTR)
    return base - base.shift(_TD_QTR)


def isl_drv2_068_buy_active_collapse_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in buy active days collapse ratio (63d ann / 252d)."""
    recent = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_buy_count > 0).astype(float), _TD_YEAR)
    ratio  = _safe_div(recent, hist)
    return ratio - ratio.shift(_TD_QTR)


def isl_drv2_069_silence_excess_months_slope_21(insider_buy_count: pd.Series) -> pd.Series:
    """OLS slope of silence-excess-months over last 21 days."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0) / 21.0
    x        = pd.Series(np.arange(len(excess), dtype=float), index=excess.index)
    x_bar    = _rolling_mean(x, _TD_MO)
    y_bar    = _rolling_mean(excess, _TD_MO)
    cov      = _rolling_mean((x - x_bar) * (excess - y_bar), _TD_MO)
    var_x    = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    return _safe_div(cov, var_x)


def isl_drv2_070_ceo_buy_zero_frac_diff_21(ceo_buy_value: pd.Series) -> pd.Series:
    """21-day change in 252-day CEO buy zero-fraction."""
    base = _rolling_mean((ceo_buy_value == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_MO)


def isl_drv2_071_buy_count_2yr_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in rolling 504-day buy count sum."""
    base = _rolling_sum(insider_buy_count, _TD_2Y)
    return base - base.shift(_TD_QTR)


def isl_drv2_072_any_txn_zero_frac_1yr_diff_252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """252-day change in 252-day any-transaction zero-fraction (YoY silence shift)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _rolling_mean((combined == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def isl_drv2_073_buy_silence_pct_rank_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in expanding percentile rank of buy zero-run."""
    run  = _current_zero_run_length(insider_buy_count)
    rank = run.expanding(min_periods=2).rank(pct=True)
    return rank - rank.shift(_TD_QTR)


def isl_drv2_074_sell_zero_frac_1yr_diff_252(insider_sell_count: pd.Series) -> pd.Series:
    """252-day change in 252-day sell zero-fraction (YoY sell silence trend)."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_YEAR)


def isl_drv2_075_officer_buy_zero_frac_diff_252(officer_buy_count: pd.Series) -> pd.Series:
    """252-day change in 252-day officer buy zero-fraction (YoY officer silence)."""
    base = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────
INSIDER_SILENCE_REGISTRY_2ND_DERIVATIVES = {
    "isl_drv2_001_days_since_buy_diff_21":           {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_001_days_since_buy_diff_21},
    "isl_drv2_002_days_since_buy_diff_63":           {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_002_days_since_buy_diff_63},
    "isl_drv2_003_buy_zero_run_diff_21":             {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_003_buy_zero_run_diff_21},
    "isl_drv2_004_buy_zero_run_diff_63":             {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_004_buy_zero_run_diff_63},
    "isl_drv2_005_buy_zero_frac_1qtr_diff_63":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_005_buy_zero_frac_1qtr_diff_63},
    "isl_drv2_006_buy_zero_frac_1yr_diff_63":        {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_006_buy_zero_frac_1yr_diff_63},
    "isl_drv2_007_buy_zero_frac_1yr_diff_252":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_007_buy_zero_frac_1yr_diff_252},
    "isl_drv2_008_buy_count_qtr_pct_change_21":      {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_008_buy_count_qtr_pct_change_21},
    "isl_drv2_009_buy_count_yr_pct_change_63":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_009_buy_count_yr_pct_change_63},
    "isl_drv2_010_sell_zero_frac_diff_63":           {"inputs": ["insider_sell_count"],                                                            "func": isl_drv2_010_sell_zero_frac_diff_63},
    "isl_drv2_011_days_since_sell_diff_21":          {"inputs": ["insider_sell_count"],                                                            "func": isl_drv2_011_days_since_sell_diff_21},
    "isl_drv2_012_any_txn_zero_frac_1qtr_diff_63":  {"inputs": ["insider_buy_count", "insider_sell_count"],                                       "func": isl_drv2_012_any_txn_zero_frac_1qtr_diff_63},
    "isl_drv2_013_quiet_score_slope_21":             {"inputs": ["insider_buy_count", "insider_sell_count"],                                       "func": isl_drv2_013_quiet_score_slope_21},
    "isl_drv2_014_buy_withdrawal_score_diff_63":     {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_014_buy_withdrawal_score_diff_63},
    "isl_drv2_015_officer_buy_zero_frac_diff_63":    {"inputs": ["officer_buy_count"],                                                             "func": isl_drv2_015_officer_buy_zero_frac_diff_63},
    "isl_drv2_016_buyer_zero_frac_diff_63":          {"inputs": ["insider_buyers"],                                                                "func": isl_drv2_016_buyer_zero_frac_diff_63},
    "isl_drv2_017_ceo_buy_zero_run_diff_63":         {"inputs": ["ceo_buy_value"],                                                                 "func": isl_drv2_017_ceo_buy_zero_run_diff_63},
    "isl_drv2_018_silence_excess_months_diff_21":    {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_018_silence_excess_months_diff_21},
    "isl_drv2_019_buy_silence_zscore_diff_21":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_019_buy_silence_zscore_diff_21},
    "isl_drv2_020_buy_count_1yr_rolling_slope":      {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_020_buy_count_1yr_rolling_slope},
    "isl_drv2_021_tenpct_buy_zero_frac_diff_63":     {"inputs": ["tenpct_buy_count"],                                                              "func": isl_drv2_021_tenpct_buy_zero_frac_diff_63},
    "isl_drv2_022_sell_zero_run_diff_21":            {"inputs": ["insider_sell_count"],                                                            "func": isl_drv2_022_sell_zero_run_diff_21},
    "isl_drv2_023_buy_active_days_diff_63":          {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_023_buy_active_days_diff_63},
    "isl_drv2_024_grand_silence_composite_diff_63":  {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "officer_buy_count"], "func": isl_drv2_024_grand_silence_composite_diff_63},
    "isl_drv2_025_buy_gap_ratio_acceleration":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_025_buy_gap_ratio_acceleration},
    "isl_drv2_026_days_since_buy_diff_5":            {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_026_days_since_buy_diff_5},
    "isl_drv2_027_buy_zero_run_diff_5":              {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_027_buy_zero_run_diff_5},
    "isl_drv2_028_buy_zero_frac_1mo_diff_21":        {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_028_buy_zero_frac_1mo_diff_21},
    "isl_drv2_029_buy_zero_frac_1qtr_diff_21":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_029_buy_zero_frac_1qtr_diff_21},
    "isl_drv2_030_buy_zero_frac_2yr_diff_63":        {"inputs": ["insider_buy_count"],                                                             "func": isl_drv2_030_buy_zero_frac_2yr_diff_63},
    "isl_drv2_031_sell_zero_run_diff_63":            {"inputs": ["insider_sell_count"],                                                            "func": isl_drv2_031_sell_zero_run_diff_63},
    "isl_drv2_032_sell_zero_frac_1yr_diff_63":       {"inputs": ["insider_sell_count"],                                                            "func": isl_drv2_032_sell_zero_frac_1yr_diff_63},
    "isl_drv2_033_days_since_sell_diff_63":          {"inputs": ["insider_sell_count"],                                                            "func": isl_drv2_033_days_since_sell_diff_63},
    "isl_drv2_034_buyer_zero_frac_diff_21":          {"inputs": ["insider_buyers"],                                                                "func": isl_drv2_034_buyer_zero_frac_diff_21},
    "isl_drv2_035_buyer_zero_frac_1yr_diff_63":      {"inputs": ["insider_buyers"],                                                                "func": isl_drv2_035_buyer_zero_frac_1yr_diff_63},
    "isl_drv2_036_officer_buy_zero_frac_diff_21":    {"inputs": ["officer_buy_count"],                                                            "func": isl_drv2_036_officer_buy_zero_frac_diff_21},
    "isl_drv2_037_officer_buy_run_diff_21":          {"inputs": ["officer_buy_count"],                                                            "func": isl_drv2_037_officer_buy_run_diff_21},
    "isl_drv2_038_officer_buy_run_diff_63":          {"inputs": ["officer_buy_count"],                                                            "func": isl_drv2_038_officer_buy_run_diff_63},
    "isl_drv2_039_ceo_buy_zero_frac_1yr_diff_63":    {"inputs": ["ceo_buy_value"],                                                                "func": isl_drv2_039_ceo_buy_zero_frac_1yr_diff_63},
    "isl_drv2_040_ceo_buy_run_diff_21":              {"inputs": ["ceo_buy_value"],                                                                "func": isl_drv2_040_ceo_buy_run_diff_21},
    "isl_drv2_041_tenpct_buy_run_diff_21":           {"inputs": ["tenpct_buy_count"],                                                             "func": isl_drv2_041_tenpct_buy_run_diff_21},
    "isl_drv2_042_tenpct_buy_run_diff_63":           {"inputs": ["tenpct_buy_count"],                                                             "func": isl_drv2_042_tenpct_buy_run_diff_63},
    "isl_drv2_043_any_txn_zero_frac_1yr_diff_63":    {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv2_043_any_txn_zero_frac_1yr_diff_63},
    "isl_drv2_044_any_txn_zero_run_diff_21":         {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv2_044_any_txn_zero_run_diff_21},
    "isl_drv2_045_any_txn_zero_run_diff_63":         {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv2_045_any_txn_zero_run_diff_63},
    "isl_drv2_046_buy_active_days_1qtr_diff_63":     {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_046_buy_active_days_1qtr_diff_63},
    "isl_drv2_047_sell_active_days_1yr_diff_63":     {"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_047_sell_active_days_1yr_diff_63},
    "isl_drv2_048_buy_count_sum_1mo_diff_21":        {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_048_buy_count_sum_1mo_diff_21},
    "isl_drv2_049_buy_count_sum_1qtr_diff_21":       {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_049_buy_count_sum_1qtr_diff_21},
    "isl_drv2_050_buy_value_zero_frac_1yr_diff_63":  {"inputs": ["insider_buy_value"],                                                            "func": isl_drv2_050_buy_value_zero_frac_1yr_diff_63},
    "isl_drv2_051_buy_silence_zscore_diff_63":       {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_051_buy_silence_zscore_diff_63},
    "isl_drv2_052_silence_excess_months_diff_63":    {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_052_silence_excess_months_diff_63},
    "isl_drv2_053_buy_withdrawal_score_diff_21":     {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_053_buy_withdrawal_score_diff_21},
    "isl_drv2_054_quiet_score_slope_63":             {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv2_054_quiet_score_slope_63},
    "isl_drv2_055_buy_count_1yr_slope_21":           {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_055_buy_count_1yr_slope_21},
    "isl_drv2_056_buy_zero_frac_1yr_diff_21":        {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_056_buy_zero_frac_1yr_diff_21},
    "isl_drv2_057_sell_count_sum_1qtr_diff_63":      {"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_057_sell_count_sum_1qtr_diff_63},
    "isl_drv2_058_sell_count_sum_1yr_diff_63":       {"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_058_sell_count_sum_1yr_diff_63},
    "isl_drv2_059_buy_count_yr_pct_change_21":       {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_059_buy_count_yr_pct_change_21},
    "isl_drv2_060_sell_count_yr_pct_change_63":      {"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_060_sell_count_yr_pct_change_63},
    "isl_drv2_061_grand_silence_diff_21":            {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "officer_buy_count"], "func": isl_drv2_061_grand_silence_diff_21},
    "isl_drv2_062_buy_silence_rank_1yr_diff_63":     {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_062_buy_silence_rank_1yr_diff_63},
    "isl_drv2_063_buy_zero_frac_1qtr_slope_21":      {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_063_buy_zero_frac_1qtr_slope_21},
    "isl_drv2_064_sell_zero_frac_1qtr_diff_21":      {"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_064_sell_zero_frac_1qtr_diff_21},
    "isl_drv2_065_buyer_collapse_ratio_diff_63":     {"inputs": ["insider_buyers"],                                                               "func": isl_drv2_065_buyer_collapse_ratio_diff_63},
    "isl_drv2_066_sell_active_days_collapse_diff_63":{"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_066_sell_active_days_collapse_diff_63},
    "isl_drv2_067_buy_value_zero_frac_1qtr_diff_63": {"inputs": ["insider_buy_value"],                                                            "func": isl_drv2_067_buy_value_zero_frac_1qtr_diff_63},
    "isl_drv2_068_buy_active_collapse_diff_63":      {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_068_buy_active_collapse_diff_63},
    "isl_drv2_069_silence_excess_months_slope_21":   {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_069_silence_excess_months_slope_21},
    "isl_drv2_070_ceo_buy_zero_frac_diff_21":        {"inputs": ["ceo_buy_value"],                                                                "func": isl_drv2_070_ceo_buy_zero_frac_diff_21},
    "isl_drv2_071_buy_count_2yr_diff_63":            {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_071_buy_count_2yr_diff_63},
    "isl_drv2_072_any_txn_zero_frac_1yr_diff_252":   {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv2_072_any_txn_zero_frac_1yr_diff_252},
    "isl_drv2_073_buy_silence_pct_rank_diff_63":     {"inputs": ["insider_buy_count"],                                                            "func": isl_drv2_073_buy_silence_pct_rank_diff_63},
    "isl_drv2_074_sell_zero_frac_1yr_diff_252":      {"inputs": ["insider_sell_count"],                                                           "func": isl_drv2_074_sell_zero_frac_1yr_diff_252},
    "isl_drv2_075_officer_buy_zero_frac_diff_252":   {"inputs": ["officer_buy_count"],                                                            "func": isl_drv2_075_officer_buy_zero_frac_diff_252},
}
