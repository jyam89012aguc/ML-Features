"""
90_insider_silence — 3rd-Derivative Features 001-025
Domain: rate-of-change of 2nd-derivative insider-silence features
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records. Most days are ZERO (no transactions filed) — NOT
forward-filled. This file computes second differences, slopes-of-slopes, and
pct-changes of 2nd-derivative silence concepts. Series will be very sparse on
the daily index because the underlying data is event-driven — this is correct
and expected.
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


# ── Base and 2nd-derivative concept helpers (self-contained) ──────────────────

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


def _buy_count_rolling_yr(s: pd.Series) -> pd.Series:
    return _rolling_sum(s, _TD_YEAR)


# 2nd-derivative inline helpers

def _drv2_days_since_buy_diff_21(s: pd.Series) -> pd.Series:
    base = _days_since_last_nonzero(s)
    return base - base.shift(_TD_MO)


def _drv2_days_since_buy_diff_63(s: pd.Series) -> pd.Series:
    base = _days_since_last_nonzero(s)
    return base - base.shift(_TD_QTR)


def _drv2_buy_zero_run_diff_21(s: pd.Series) -> pd.Series:
    base = _current_zero_run_length(s)
    return base - base.shift(_TD_MO)


def _drv2_buy_zero_run_diff_63(s: pd.Series) -> pd.Series:
    base = _current_zero_run_length(s)
    return base - base.shift(_TD_QTR)


def _drv2_buy_zero_frac_1qtr_diff_63(s: pd.Series) -> pd.Series:
    base = _buy_zero_frac_1qtr(s)
    return base - base.shift(_TD_QTR)


def _drv2_buy_zero_frac_1yr_diff_63(s: pd.Series) -> pd.Series:
    base = _buy_zero_frac_1yr(s)
    return base - base.shift(_TD_QTR)


def _drv2_buy_zero_frac_1yr_diff_252(s: pd.Series) -> pd.Series:
    base = _buy_zero_frac_1yr(s)
    return base - base.shift(_TD_YEAR)


def _drv2_buy_active_days_diff_63(s: pd.Series) -> pd.Series:
    base = _rolling_sum((s > 0).astype(float), _TD_YEAR)
    return base - base.shift(_TD_QTR)


# ── 3rd-Derivative Feature functions 001-025 ─────────────────────────────────

def isl_drv3_001_days_since_buy_diff_21_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of the 21-day change in days-since-last-buy (2nd difference)."""
    drv2 = _drv2_days_since_buy_diff_21(insider_buy_count)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_002_days_since_buy_diff_63_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of the 63-day change in days-since-last-buy."""
    drv2 = _drv2_days_since_buy_diff_63(insider_buy_count)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_003_buy_zero_run_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of the 21-day change in buy zero-run (2nd diff of run length)."""
    drv2 = _drv2_buy_zero_run_diff_21(insider_buy_count)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_004_buy_zero_run_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of the 63-day change in buy zero-run."""
    drv2 = _drv2_buy_zero_run_diff_63(insider_buy_count)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_005_buy_zero_frac_1qtr_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 63-day buy zero-frac): 2nd diff of frac."""
    drv2 = _drv2_buy_zero_frac_1qtr_diff_63(insider_buy_count)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_006_buy_zero_frac_1yr_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day buy zero-frac)."""
    drv2 = _drv2_buy_zero_frac_1yr_diff_63(insider_buy_count)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_007_buy_zero_frac_1yr_diff252_diff252(insider_buy_count: pd.Series) -> pd.Series:
    """252-day change of (252-day change in 252-day buy zero-frac): annual 2nd diff."""
    drv2 = _drv2_buy_zero_frac_1yr_diff_252(insider_buy_count)
    return drv2 - drv2.shift(_TD_YEAR)


def isl_drv3_008_buy_count_pct_change_slope(insider_buy_count: pd.Series) -> pd.Series:
    """
    21-day slope of (21-day pct-change of rolling 63-day buy count).
    Captures whether the rate-of-decline of buy activity is itself accelerating.
    """
    base  = _rolling_sum(insider_buy_count, _TD_QTR)
    prior = base.shift(_TD_MO)
    pct   = _safe_div(base - prior, prior.abs())
    x     = pd.Series(np.arange(len(pct), dtype=float), index=pct.index)
    x_bar = _rolling_mean(x, _TD_MO)
    y_bar = _rolling_mean(pct, _TD_MO)
    cov   = _rolling_mean((x - x_bar) * (pct - y_bar), _TD_MO)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    return _safe_div(cov, var_x)


def isl_drv3_009_sell_zero_frac_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 63-day sell zero-frac)."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_010_days_since_sell_diff21_diff21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in days-since-last-sell)."""
    base = _days_since_last_nonzero(insider_sell_count)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_011_any_txn_zero_frac_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in any-txn 63-day zero-frac)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base     = _rolling_mean((combined == 0).astype(float), _TD_QTR)
    drv2     = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_012_buy_withdrawal_score_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in buy withdrawal score)."""
    zero_frac = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    run_norm  = (_current_zero_run_length(insider_buy_count) / _TD_YEAR).clip(upper=1.0)
    score     = ((zero_frac + run_norm) / 2.0).clip(upper=1.0)
    drv2      = score - score.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_013_officer_buy_zero_frac_diff63_diff63(officer_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in officer-buy 252-day zero-frac)."""
    base = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_014_buyer_zero_frac_diff63_diff63(insider_buyers: pd.Series) -> pd.Series:
    """63-day change of (63-day change in buyer 63-day zero-frac)."""
    base = _rolling_mean((insider_buyers == 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_015_ceo_buy_zero_run_diff63_diff63(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day change of (63-day change in CEO buy zero-run)."""
    base = _current_zero_run_length(ceo_buy_value)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_016_silence_zscore_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in expanding buy silence z-score)."""
    run = _current_zero_run_length(insider_buy_count)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    z   = _safe_div(run - mu, sd)
    drv2 = z - z.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_017_buy_count_slope_diff_63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change in the 63-day OLS slope of rolling 252-day buy count."""
    y     = _buy_count_rolling_yr(insider_buy_count)
    x     = pd.Series(np.arange(len(y), dtype=float), index=y.index)
    x_bar = _rolling_mean(x, _TD_QTR)
    y_bar = _rolling_mean(y, _TD_QTR)
    cov   = _rolling_mean((x - x_bar) * (y - y_bar), _TD_QTR)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_QTR)
    slope = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_QTR)


def isl_drv3_018_tenpct_buy_frac_diff63_diff63(tenpct_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 10%-holder buy 252-day zero-frac)."""
    base = _rolling_mean((tenpct_buy_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_019_sell_zero_run_diff21_diff21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in sell zero-run)."""
    base = _current_zero_run_length(insider_sell_count)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_020_buy_active_days_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in rolling 252-day buy-active day count)."""
    drv2 = _drv2_buy_active_days_diff_63(insider_buy_count)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_021_grand_composite_diff63_diff63(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buyers: pd.Series,
    officer_buy_count: pd.Series
) -> pd.Series:
    """63-day change of (63-day change in grand silence composite)."""
    buy_zero   = (insider_buy_count  == 0).astype(float)
    txn_zero   = ((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float)
    buyer_zero = (insider_buyers     == 0).astype(float)
    offr_zero  = (officer_buy_count  == 0).astype(float)
    score = (_rolling_mean(buy_zero, _TD_YEAR) + _rolling_mean(txn_zero, _TD_YEAR) +
             _rolling_mean(buyer_zero, _TD_YEAR) + _rolling_mean(offr_zero, _TD_YEAR)) / 4.0
    drv2  = score - score.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_022_buy_gap_ratio_accel_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in buy zero-frac ratio 63d/252d)."""
    zero  = (insider_buy_count == 0).astype(float)
    ratio = _safe_div(_rolling_mean(zero, _TD_QTR), _rolling_mean(zero, _TD_YEAR))
    drv2  = ratio - ratio.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_023_silence_excess_months_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in silence-excess-months)."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0) / 21.0
    drv2     = excess - excess.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_024_quiet_score_slope_diff_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change in the 21-day OLS slope of quiet-period score."""
    combined  = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero      = (combined == 0).astype(float)
    frac_qtr  = _rolling_mean(zero, _TD_QTR)
    frac_yr   = _rolling_mean(zero, _TD_YEAR)
    score     = (frac_qtr + frac_yr) / 2.0
    x         = pd.Series(np.arange(len(score), dtype=float), index=score.index)
    x_bar     = _rolling_mean(x, _TD_MO)
    y_bar     = _rolling_mean(score, _TD_MO)
    cov       = _rolling_mean((x - x_bar) * (score - y_bar), _TD_MO)
    var_x     = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    slope     = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_QTR)


def isl_drv3_025_buy_count_pct_change_slope_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of 21-day slope of (21-day pct-change of 63-day buy count)."""
    base  = _rolling_sum(insider_buy_count, _TD_QTR)
    prior = base.shift(_TD_MO)
    pct   = _safe_div(base - prior, prior.abs())
    x     = pd.Series(np.arange(len(pct), dtype=float), index=pct.index)
    x_bar = _rolling_mean(x, _TD_MO)
    y_bar = _rolling_mean(pct, _TD_MO)
    cov   = _rolling_mean((x - x_bar) * (pct - y_bar), _TD_MO)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    slope = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_QTR)


# ── 3rd-Derivative Feature functions 026-075 ─────────────────────────────────

def isl_drv3_026_days_since_buy_diff5_diff5(insider_buy_count: pd.Series) -> pd.Series:
    """5-day change of (5-day change in days-since-last-buy)."""
    base = _days_since_last_nonzero(insider_buy_count)
    drv2 = base - base.shift(_TD_WK)
    return drv2 - drv2.shift(_TD_WK)


def isl_drv3_027_buy_zero_run_diff5_diff5(insider_buy_count: pd.Series) -> pd.Series:
    """5-day change of (5-day change in buy zero-run length)."""
    base = _current_zero_run_length(insider_buy_count)
    drv2 = base - base.shift(_TD_WK)
    return drv2 - drv2.shift(_TD_WK)


def isl_drv3_028_buy_zero_frac_1mo_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 21-day buy zero-frac): 2nd diff of monthly frac."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_MO)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_029_buy_zero_frac_1qtr_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 63-day buy zero-frac)."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_030_buy_zero_frac_2yr_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 504-day buy zero-frac)."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_2Y)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_031_sell_zero_run_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in sell zero-run)."""
    base = _current_zero_run_length(insider_sell_count)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_032_sell_zero_frac_1yr_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day sell zero-frac)."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_033_days_since_sell_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in days-since-last-sell)."""
    base = _days_since_last_nonzero(insider_sell_count)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_034_buyer_zero_frac_diff21_diff21(insider_buyers: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 63-day buyer zero-frac)."""
    base = _rolling_mean((insider_buyers == 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_035_buyer_zero_frac_1yr_diff63_diff63(insider_buyers: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day buyer zero-frac)."""
    base = _rolling_mean((insider_buyers == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_036_officer_buy_run_diff21_diff21(officer_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in officer buy zero-run)."""
    base = _current_zero_run_length(officer_buy_count)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_037_officer_buy_run_diff63_diff63(officer_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in officer buy zero-run)."""
    base = _current_zero_run_length(officer_buy_count)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_038_officer_buy_zero_frac_diff63_diff63(officer_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day officer buy zero-frac)."""
    base = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_039_ceo_buy_zero_frac_diff63_diff63(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day CEO buy zero-frac)."""
    base = _rolling_mean((ceo_buy_value == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_040_ceo_buy_run_diff21_diff21(ceo_buy_value: pd.Series) -> pd.Series:
    """21-day change of (21-day change in CEO buy zero-run)."""
    base = _current_zero_run_length(ceo_buy_value)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_041_tenpct_buy_run_diff21_diff21(tenpct_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 10%-holder buy zero-run)."""
    base = _current_zero_run_length(tenpct_buy_count)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_042_tenpct_buy_run_diff63_diff63(tenpct_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 10%-holder buy zero-run)."""
    base = _current_zero_run_length(tenpct_buy_count)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_043_any_txn_zero_frac_1yr_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day any-txn zero-frac)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _rolling_mean((combined == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_044_any_txn_zero_run_diff21_diff21(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in any-txn zero-run)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _current_zero_run_length(combined)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_045_any_txn_zero_run_diff63_diff63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in any-txn zero-run)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _current_zero_run_length(combined)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_046_buy_active_days_1qtr_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 63-day buy-active day count)."""
    base = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_047_sell_active_days_1yr_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day sell-active day count)."""
    base = _rolling_sum((insider_sell_count > 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_048_buy_count_sum_1mo_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 21-day buy count sum)."""
    base = _rolling_sum(insider_buy_count, _TD_MO)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_049_buy_count_1qtr_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 63-day buy count sum)."""
    base = _rolling_sum(insider_buy_count, _TD_QTR)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_050_buy_value_zero_frac_1yr_diff63_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day buy-value zero-frac)."""
    base = _rolling_mean((insider_buy_value == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_051_buy_silence_zscore_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in expanding buy silence z-score)."""
    run  = _current_zero_run_length(insider_buy_count)
    mu   = run.expanding(min_periods=2).mean()
    sd   = run.expanding(min_periods=2).std()
    z    = _safe_div(run - mu, sd)
    drv2 = z - z.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_052_silence_excess_months_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in silence-excess-months)."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0) / 21.0
    drv2     = excess - excess.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_053_buy_withdrawal_score_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in buy withdrawal score)."""
    zero_frac = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    run_norm  = (_current_zero_run_length(insider_buy_count) / _TD_YEAR).clip(upper=1.0)
    score     = ((zero_frac + run_norm) / 2.0).clip(upper=1.0)
    drv2      = score - score.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_054_quiet_score_slope_63_diff_63(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of the 63-day OLS slope of quiet-period score."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero     = (combined == 0).astype(float)
    score    = (_rolling_mean(zero, _TD_QTR) + _rolling_mean(zero, _TD_YEAR)) / 2.0
    x        = pd.Series(np.arange(len(score), dtype=float), index=score.index)
    x_bar    = _rolling_mean(x, _TD_QTR)
    y_bar    = _rolling_mean(score, _TD_QTR)
    cov      = _rolling_mean((x - x_bar) * (score - y_bar), _TD_QTR)
    var_x    = _rolling_mean((x - x_bar) ** 2, _TD_QTR)
    slope    = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_QTR)


def isl_drv3_055_buy_count_1yr_slope_21_diff_21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of 21-day OLS slope of rolling 252-day buy count."""
    y     = _buy_count_rolling_yr(insider_buy_count)
    x     = pd.Series(np.arange(len(y), dtype=float), index=y.index)
    x_bar = _rolling_mean(x, _TD_MO)
    y_bar = _rolling_mean(y, _TD_MO)
    cov   = _rolling_mean((x - x_bar) * (y - y_bar), _TD_MO)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    slope = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_MO)


def isl_drv3_056_buy_zero_frac_1yr_diff21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 252-day buy zero-frac)."""
    base = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_057_sell_count_sum_1qtr_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 63-day sell count sum)."""
    base = _rolling_sum(insider_sell_count, _TD_QTR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_058_sell_count_sum_1yr_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day sell count sum)."""
    base = _rolling_sum(insider_sell_count, _TD_YEAR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_059_buy_count_yr_pct_change_21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day pct-change of 252-day buy count)."""
    base  = _rolling_sum(insider_buy_count, _TD_YEAR)
    prior = base.shift(_TD_MO)
    pct   = _safe_div(base - prior, prior.abs())
    return pct - pct.shift(_TD_MO)


def isl_drv3_060_sell_count_yr_pct_change_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day pct-change of 252-day sell count)."""
    base  = _rolling_sum(insider_sell_count, _TD_YEAR)
    prior = base.shift(_TD_QTR)
    pct   = _safe_div(base - prior, prior.abs())
    return pct - pct.shift(_TD_QTR)


def isl_drv3_061_grand_silence_diff21_diff21(insider_buy_count: pd.Series, insider_sell_count: pd.Series, insider_buyers: pd.Series, officer_buy_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in grand silence composite)."""
    buy_zero   = (insider_buy_count == 0).astype(float)
    txn_zero   = ((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float)
    buyer_zero = (insider_buyers == 0).astype(float)
    offr_zero  = (officer_buy_count == 0).astype(float)
    score = (_rolling_mean(buy_zero, _TD_YEAR) + _rolling_mean(txn_zero, _TD_YEAR) +
             _rolling_mean(buyer_zero, _TD_YEAR) + _rolling_mean(offr_zero, _TD_YEAR)) / 4.0
    drv2  = score - score.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_062_buy_silence_rank_1yr_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 252-day buy zero-run percentile rank)."""
    run  = _current_zero_run_length(insider_buy_count)
    rank = run.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)
    drv2 = rank - rank.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_063_buy_zero_frac_1qtr_slope21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of the 21-day OLS slope of 63-day buy zero-frac."""
    y     = _rolling_mean((insider_buy_count == 0).astype(float), _TD_QTR)
    x     = pd.Series(np.arange(len(y), dtype=float), index=y.index)
    x_bar = _rolling_mean(x, _TD_MO)
    y_bar = _rolling_mean(y, _TD_MO)
    cov   = _rolling_mean((x - x_bar) * (y - y_bar), _TD_MO)
    var_x = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    slope = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_MO)


def isl_drv3_064_sell_zero_frac_1qtr_diff21_diff21(insider_sell_count: pd.Series) -> pd.Series:
    """21-day change of (21-day change in 63-day sell zero-frac)."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_MO)
    return drv2 - drv2.shift(_TD_MO)


def isl_drv3_065_buyer_collapse_ratio_diff63_diff63(insider_buyers: pd.Series) -> pd.Series:
    """63-day change of (63-day change in buyer collapse ratio)."""
    recent = _rolling_sum(insider_buyers, _TD_QTR) * 4.0
    hist   = _rolling_sum(insider_buyers, _TD_YEAR)
    ratio  = _safe_div(recent, hist)
    drv2   = ratio - ratio.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_066_sell_active_collapse_diff63_diff63(insider_sell_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in sell active days collapse ratio)."""
    recent = _rolling_sum((insider_sell_count > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_sell_count > 0).astype(float), _TD_YEAR)
    ratio  = _safe_div(recent, hist)
    drv2   = ratio - ratio.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_067_buy_value_zero_frac_1qtr_diff63_diff63(insider_buy_value: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 63-day buy-value zero-frac)."""
    base = _rolling_mean((insider_buy_value == 0).astype(float), _TD_QTR)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_068_buy_active_collapse_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in buy active days collapse ratio)."""
    recent = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_buy_count > 0).astype(float), _TD_YEAR)
    ratio  = _safe_div(recent, hist)
    drv2   = ratio - ratio.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_069_silence_excess_slope21_diff21(insider_buy_count: pd.Series) -> pd.Series:
    """21-day change of the 21-day OLS slope of silence-excess-months."""
    run      = _current_zero_run_length(insider_buy_count)
    hist_med = run.expanding(min_periods=2).median()
    excess   = (run - hist_med).clip(lower=0) / 21.0
    x        = pd.Series(np.arange(len(excess), dtype=float), index=excess.index)
    x_bar    = _rolling_mean(x, _TD_MO)
    y_bar    = _rolling_mean(excess, _TD_MO)
    cov      = _rolling_mean((x - x_bar) * (excess - y_bar), _TD_MO)
    var_x    = _rolling_mean((x - x_bar) ** 2, _TD_MO)
    slope    = _safe_div(cov, var_x)
    return slope - slope.shift(_TD_MO)


def isl_drv3_070_ceo_buy_run_diff63_diff63(ceo_buy_value: pd.Series) -> pd.Series:
    """63-day change of (63-day change in CEO buy zero-run)."""
    base = _current_zero_run_length(ceo_buy_value)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_071_buy_count_2yr_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in 504-day buy count sum)."""
    base = _rolling_sum(insider_buy_count, _TD_2Y)
    drv2 = base - base.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_072_any_txn_zero_frac_1yr_diff252_diff252(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """252-day change of (252-day change in 252-day any-txn zero-frac)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    base = _rolling_mean((combined == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_YEAR)
    return drv2 - drv2.shift(_TD_YEAR)


def isl_drv3_073_buy_silence_pct_rank_diff63_diff63(insider_buy_count: pd.Series) -> pd.Series:
    """63-day change of (63-day change in expanding percentile rank of buy zero-run)."""
    run  = _current_zero_run_length(insider_buy_count)
    rank = run.expanding(min_periods=2).rank(pct=True)
    drv2 = rank - rank.shift(_TD_QTR)
    return drv2 - drv2.shift(_TD_QTR)


def isl_drv3_074_sell_zero_frac_1yr_diff252_diff252(insider_sell_count: pd.Series) -> pd.Series:
    """252-day change of (252-day change in 252-day sell zero-frac)."""
    base = _rolling_mean((insider_sell_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_YEAR)
    return drv2 - drv2.shift(_TD_YEAR)


def isl_drv3_075_officer_buy_zero_frac_diff252_diff252(officer_buy_count: pd.Series) -> pd.Series:
    """252-day change of (252-day change in 252-day officer buy zero-frac)."""
    base = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    drv2 = base - base.shift(_TD_YEAR)
    return drv2 - drv2.shift(_TD_YEAR)


# ── Registry ──────────────────────────────────────────────────────────────────
INSIDER_SILENCE_REGISTRY_3RD_DERIVATIVES = {
    "isl_drv3_001_days_since_buy_diff_21_diff_21":      {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_001_days_since_buy_diff_21_diff_21},
    "isl_drv3_002_days_since_buy_diff_63_diff_63":      {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_002_days_since_buy_diff_63_diff_63},
    "isl_drv3_003_buy_zero_run_diff21_diff21":          {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_003_buy_zero_run_diff21_diff21},
    "isl_drv3_004_buy_zero_run_diff63_diff63":          {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_004_buy_zero_run_diff63_diff63},
    "isl_drv3_005_buy_zero_frac_1qtr_diff63_diff63":   {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_005_buy_zero_frac_1qtr_diff63_diff63},
    "isl_drv3_006_buy_zero_frac_1yr_diff63_diff63":    {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_006_buy_zero_frac_1yr_diff63_diff63},
    "isl_drv3_007_buy_zero_frac_1yr_diff252_diff252":  {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_007_buy_zero_frac_1yr_diff252_diff252},
    "isl_drv3_008_buy_count_pct_change_slope":         {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_008_buy_count_pct_change_slope},
    "isl_drv3_009_sell_zero_frac_diff63_diff63":       {"inputs": ["insider_sell_count"],                                                            "func": isl_drv3_009_sell_zero_frac_diff63_diff63},
    "isl_drv3_010_days_since_sell_diff21_diff21":      {"inputs": ["insider_sell_count"],                                                            "func": isl_drv3_010_days_since_sell_diff21_diff21},
    "isl_drv3_011_any_txn_zero_frac_diff63_diff63":   {"inputs": ["insider_buy_count", "insider_sell_count"],                                       "func": isl_drv3_011_any_txn_zero_frac_diff63_diff63},
    "isl_drv3_012_buy_withdrawal_score_diff63_diff63": {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_012_buy_withdrawal_score_diff63_diff63},
    "isl_drv3_013_officer_buy_zero_frac_diff63_diff63":{"inputs": ["officer_buy_count"],                                                             "func": isl_drv3_013_officer_buy_zero_frac_diff63_diff63},
    "isl_drv3_014_buyer_zero_frac_diff63_diff63":      {"inputs": ["insider_buyers"],                                                                "func": isl_drv3_014_buyer_zero_frac_diff63_diff63},
    "isl_drv3_015_ceo_buy_zero_run_diff63_diff63":     {"inputs": ["ceo_buy_value"],                                                                 "func": isl_drv3_015_ceo_buy_zero_run_diff63_diff63},
    "isl_drv3_016_silence_zscore_diff21_diff21":       {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_016_silence_zscore_diff21_diff21},
    "isl_drv3_017_buy_count_slope_diff_63":            {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_017_buy_count_slope_diff_63},
    "isl_drv3_018_tenpct_buy_frac_diff63_diff63":      {"inputs": ["tenpct_buy_count"],                                                              "func": isl_drv3_018_tenpct_buy_frac_diff63_diff63},
    "isl_drv3_019_sell_zero_run_diff21_diff21":        {"inputs": ["insider_sell_count"],                                                            "func": isl_drv3_019_sell_zero_run_diff21_diff21},
    "isl_drv3_020_buy_active_days_diff63_diff63":      {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_020_buy_active_days_diff63_diff63},
    "isl_drv3_021_grand_composite_diff63_diff63":      {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "officer_buy_count"], "func": isl_drv3_021_grand_composite_diff63_diff63},
    "isl_drv3_022_buy_gap_ratio_accel_diff63":         {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_022_buy_gap_ratio_accel_diff63},
    "isl_drv3_023_silence_excess_months_diff21_diff21":{"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_023_silence_excess_months_diff21_diff21},
    "isl_drv3_024_quiet_score_slope_diff_63":          {"inputs": ["insider_buy_count", "insider_sell_count"],                                       "func": isl_drv3_024_quiet_score_slope_diff_63},
    "isl_drv3_025_buy_count_pct_change_slope_diff63":  {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_025_buy_count_pct_change_slope_diff63},
    "isl_drv3_026_days_since_buy_diff5_diff5":          {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_026_days_since_buy_diff5_diff5},
    "isl_drv3_027_buy_zero_run_diff5_diff5":            {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_027_buy_zero_run_diff5_diff5},
    "isl_drv3_028_buy_zero_frac_1mo_diff21_diff21":     {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_028_buy_zero_frac_1mo_diff21_diff21},
    "isl_drv3_029_buy_zero_frac_1qtr_diff21_diff21":    {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_029_buy_zero_frac_1qtr_diff21_diff21},
    "isl_drv3_030_buy_zero_frac_2yr_diff63_diff63":     {"inputs": ["insider_buy_count"],                                                             "func": isl_drv3_030_buy_zero_frac_2yr_diff63_diff63},
    "isl_drv3_031_sell_zero_run_diff63_diff63":         {"inputs": ["insider_sell_count"],                                                            "func": isl_drv3_031_sell_zero_run_diff63_diff63},
    "isl_drv3_032_sell_zero_frac_1yr_diff63_diff63":    {"inputs": ["insider_sell_count"],                                                            "func": isl_drv3_032_sell_zero_frac_1yr_diff63_diff63},
    "isl_drv3_033_days_since_sell_diff63_diff63":       {"inputs": ["insider_sell_count"],                                                            "func": isl_drv3_033_days_since_sell_diff63_diff63},
    "isl_drv3_034_buyer_zero_frac_diff21_diff21":       {"inputs": ["insider_buyers"],                                                                "func": isl_drv3_034_buyer_zero_frac_diff21_diff21},
    "isl_drv3_035_buyer_zero_frac_1yr_diff63_diff63":   {"inputs": ["insider_buyers"],                                                                "func": isl_drv3_035_buyer_zero_frac_1yr_diff63_diff63},
    "isl_drv3_036_officer_buy_run_diff21_diff21":       {"inputs": ["officer_buy_count"],                                                            "func": isl_drv3_036_officer_buy_run_diff21_diff21},
    "isl_drv3_037_officer_buy_run_diff63_diff63":       {"inputs": ["officer_buy_count"],                                                            "func": isl_drv3_037_officer_buy_run_diff63_diff63},
    "isl_drv3_038_officer_buy_zero_frac_diff63_diff63": {"inputs": ["officer_buy_count"],                                                            "func": isl_drv3_038_officer_buy_zero_frac_diff63_diff63},
    "isl_drv3_039_ceo_buy_zero_frac_diff63_diff63":     {"inputs": ["ceo_buy_value"],                                                                "func": isl_drv3_039_ceo_buy_zero_frac_diff63_diff63},
    "isl_drv3_040_ceo_buy_run_diff21_diff21":           {"inputs": ["ceo_buy_value"],                                                                "func": isl_drv3_040_ceo_buy_run_diff21_diff21},
    "isl_drv3_041_tenpct_buy_run_diff21_diff21":        {"inputs": ["tenpct_buy_count"],                                                             "func": isl_drv3_041_tenpct_buy_run_diff21_diff21},
    "isl_drv3_042_tenpct_buy_run_diff63_diff63":        {"inputs": ["tenpct_buy_count"],                                                             "func": isl_drv3_042_tenpct_buy_run_diff63_diff63},
    "isl_drv3_043_any_txn_zero_frac_1yr_diff63_diff63": {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv3_043_any_txn_zero_frac_1yr_diff63_diff63},
    "isl_drv3_044_any_txn_zero_run_diff21_diff21":      {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv3_044_any_txn_zero_run_diff21_diff21},
    "isl_drv3_045_any_txn_zero_run_diff63_diff63":      {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv3_045_any_txn_zero_run_diff63_diff63},
    "isl_drv3_046_buy_active_days_1qtr_diff63_diff63":  {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_046_buy_active_days_1qtr_diff63_diff63},
    "isl_drv3_047_sell_active_days_1yr_diff63_diff63":  {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_047_sell_active_days_1yr_diff63_diff63},
    "isl_drv3_048_buy_count_sum_1mo_diff21_diff21":     {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_048_buy_count_sum_1mo_diff21_diff21},
    "isl_drv3_049_buy_count_1qtr_diff21_diff21":        {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_049_buy_count_1qtr_diff21_diff21},
    "isl_drv3_050_buy_value_zero_frac_1yr_diff63_diff63":{"inputs": ["insider_buy_value"],                                                           "func": isl_drv3_050_buy_value_zero_frac_1yr_diff63_diff63},
    "isl_drv3_051_buy_silence_zscore_diff63_diff63":    {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_051_buy_silence_zscore_diff63_diff63},
    "isl_drv3_052_silence_excess_months_diff63_diff63": {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_052_silence_excess_months_diff63_diff63},
    "isl_drv3_053_buy_withdrawal_score_diff21_diff21":  {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_053_buy_withdrawal_score_diff21_diff21},
    "isl_drv3_054_quiet_score_slope_63_diff_63":        {"inputs": ["insider_buy_count", "insider_sell_count"],                                      "func": isl_drv3_054_quiet_score_slope_63_diff_63},
    "isl_drv3_055_buy_count_1yr_slope_21_diff_21":      {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_055_buy_count_1yr_slope_21_diff_21},
    "isl_drv3_056_buy_zero_frac_1yr_diff21_diff21":     {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_056_buy_zero_frac_1yr_diff21_diff21},
    "isl_drv3_057_sell_count_sum_1qtr_diff63_diff63":   {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_057_sell_count_sum_1qtr_diff63_diff63},
    "isl_drv3_058_sell_count_sum_1yr_diff63_diff63":    {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_058_sell_count_sum_1yr_diff63_diff63},
    "isl_drv3_059_buy_count_yr_pct_change_21_diff21":   {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_059_buy_count_yr_pct_change_21_diff21},
    "isl_drv3_060_sell_count_yr_pct_change_diff63":     {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_060_sell_count_yr_pct_change_diff63},
    "isl_drv3_061_grand_silence_diff21_diff21":         {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "officer_buy_count"], "func": isl_drv3_061_grand_silence_diff21_diff21},
    "isl_drv3_062_buy_silence_rank_1yr_diff63_diff63":  {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_062_buy_silence_rank_1yr_diff63_diff63},
    "isl_drv3_063_buy_zero_frac_1qtr_slope21_diff21":   {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_063_buy_zero_frac_1qtr_slope21_diff21},
    "isl_drv3_064_sell_zero_frac_1qtr_diff21_diff21":   {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_064_sell_zero_frac_1qtr_diff21_diff21},
    "isl_drv3_065_buyer_collapse_ratio_diff63_diff63":  {"inputs": ["insider_buyers"],                                                               "func": isl_drv3_065_buyer_collapse_ratio_diff63_diff63},
    "isl_drv3_066_sell_active_collapse_diff63_diff63":  {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_066_sell_active_collapse_diff63_diff63},
    "isl_drv3_067_buy_value_zero_frac_1qtr_diff63_diff63":{"inputs": ["insider_buy_value"],                                                          "func": isl_drv3_067_buy_value_zero_frac_1qtr_diff63_diff63},
    "isl_drv3_068_buy_active_collapse_diff63_diff63":   {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_068_buy_active_collapse_diff63_diff63},
    "isl_drv3_069_silence_excess_slope21_diff21":       {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_069_silence_excess_slope21_diff21},
    "isl_drv3_070_ceo_buy_run_diff63_diff63":           {"inputs": ["ceo_buy_value"],                                                                "func": isl_drv3_070_ceo_buy_run_diff63_diff63},
    "isl_drv3_071_buy_count_2yr_diff63_diff63":         {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_071_buy_count_2yr_diff63_diff63},
    "isl_drv3_072_any_txn_zero_frac_1yr_diff252_diff252":{"inputs": ["insider_buy_count", "insider_sell_count"],                                     "func": isl_drv3_072_any_txn_zero_frac_1yr_diff252_diff252},
    "isl_drv3_073_buy_silence_pct_rank_diff63_diff63":  {"inputs": ["insider_buy_count"],                                                            "func": isl_drv3_073_buy_silence_pct_rank_diff63_diff63},
    "isl_drv3_074_sell_zero_frac_1yr_diff252_diff252":  {"inputs": ["insider_sell_count"],                                                           "func": isl_drv3_074_sell_zero_frac_1yr_diff252_diff252},
    "isl_drv3_075_officer_buy_zero_frac_diff252_diff252":{"inputs": ["officer_buy_count"],                                                           "func": isl_drv3_075_officer_buy_zero_frac_diff252_diff252},
}
