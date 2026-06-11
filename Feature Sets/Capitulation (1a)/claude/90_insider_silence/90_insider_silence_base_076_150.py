"""
90_insider_silence — Base Features 076-150
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
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_TD_2Q    = 126
_TD_MO    = 21
_TD_WK    = 5
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
    (full history). Backward-only using ffill of last-seen index position.
    """
    nonzero = (s > 0).astype(int)
    idx     = pd.Series(np.where(nonzero.values, np.arange(len(s)), np.nan), index=s.index)
    last_pos = idx.ffill()
    row_num  = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    result   = row_num - last_pos
    result   = result.where(last_pos.notna(), row_num + 1)
    return result


def _current_zero_run_length(s: pd.Series) -> pd.Series:
    """
    Current consecutive zero-run length. Resets to 0 on any positive observation.
    An all-zero input returns [1,2,...,n].
    """
    is_zero = (s == 0).astype(int).values
    run     = np.zeros(len(s), dtype=float)
    for i in range(len(is_zero)):
        if i == 0:
            run[i] = float(is_zero[i])
        else:
            run[i] = (run[i - 1] + 1) * is_zero[i]
    return pd.Series(run, index=s.index)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Director / officer / CEO / CFO / 10%-holder specific silence ---

def isl_076_days_since_last_director_buy(director_buy_count: pd.Series) -> pd.Series:
    """Days since last director buy transaction."""
    return _days_since_last_nonzero(director_buy_count)


def isl_077_director_buy_zero_run_days(director_buy_count: pd.Series) -> pd.Series:
    """Current consecutive zero-run for director buys."""
    return _current_zero_run_length(director_buy_count)


def isl_078_director_buy_zero_frac_1yr(director_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero director buy activity."""
    zero = (director_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_079_days_since_last_ceo_buy(ceo_buy_value: pd.Series) -> pd.Series:
    """Days since last day with positive CEO buy dollar value."""
    return _days_since_last_nonzero(ceo_buy_value)


def isl_080_ceo_buy_zero_run_days(ceo_buy_value: pd.Series) -> pd.Series:
    """Current consecutive zero-run for CEO buy activity (by value)."""
    return _current_zero_run_length(ceo_buy_value)


def isl_081_ceo_buy_zero_frac_1yr(ceo_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero CEO buy value."""
    zero = (ceo_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_082_days_since_last_cfo_buy(cfo_buy_value: pd.Series) -> pd.Series:
    """Days since last day with positive CFO buy dollar value."""
    return _days_since_last_nonzero(cfo_buy_value)


def isl_083_cfo_buy_zero_run_days(cfo_buy_value: pd.Series) -> pd.Series:
    """Current consecutive zero-run for CFO buy activity."""
    return _current_zero_run_length(cfo_buy_value)


def isl_084_cfo_buy_zero_frac_1yr(cfo_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero CFO buy value."""
    zero = (cfo_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_085_days_since_last_tenpct_buy(tenpct_buy_count: pd.Series) -> pd.Series:
    """Days since last 10%-holder buy transaction."""
    return _days_since_last_nonzero(tenpct_buy_count)


def isl_086_tenpct_buy_zero_run_days(tenpct_buy_count: pd.Series) -> pd.Series:
    """Current consecutive zero-run for 10%-holder buys."""
    return _current_zero_run_length(tenpct_buy_count)


def isl_087_tenpct_buy_zero_frac_1yr(tenpct_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero 10%-holder buy transactions."""
    zero = (tenpct_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_088_officer_vs_director_silence_gap(officer_buy_count: pd.Series, director_buy_count: pd.Series) -> pd.Series:
    """Officer buy silence days minus director buy silence days."""
    return _days_since_last_nonzero(officer_buy_count) - _days_since_last_nonzero(director_buy_count)


def isl_089_ceo_cfo_combined_zero_run(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Zero-run for combined CEO+CFO buy value. Both must be zero for the run to count."""
    combined = ceo_buy_value + cfo_buy_value
    return _current_zero_run_length(combined)


def isl_090_ceo_buy_silence_gt_1yr_flag(ceo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if no CEO buy value observed for more than 252 days."""
    return (_current_zero_run_length(ceo_buy_value) > _TD_YEAR).astype(float)


# --- Group G (091-105): Sell-side silence and asymmetric silence metrics ---

def isl_091_days_since_last_sell_value(insider_sell_value: pd.Series) -> pd.Series:
    """Days since last day with positive insider sell dollar value."""
    return _days_since_last_nonzero(insider_sell_value)


def isl_092_sell_value_zero_run_days(insider_sell_value: pd.Series) -> pd.Series:
    """Current consecutive zero-run for insider sell value."""
    return _current_zero_run_length(insider_sell_value)


def isl_093_sell_value_zero_frac_1qtr(insider_sell_value: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero insider sell dollar value."""
    zero = (insider_sell_value == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_094_seller_zero_frac_1yr(insider_sellers: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero distinct sellers."""
    zero = (insider_sellers == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_095_days_since_last_seller(insider_sellers: pd.Series) -> pd.Series:
    """Days since any distinct insider seller was seen."""
    return _days_since_last_nonzero(insider_sellers)


def isl_096_sell_silence_months(insider_sell_count: pd.Series) -> pd.Series:
    """Days since last insider sell, expressed in months."""
    return _safe_div(_days_since_last_nonzero(insider_sell_count),
                     pd.Series(21.0, index=insider_sell_count.index))


def isl_097_buy_silence_minus_sell_silence(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Buy silence days minus sell silence days. Positive = buys more silent."""
    return _days_since_last_nonzero(insider_buy_count) - _days_since_last_nonzero(insider_sell_count)


def isl_098_buy_run_minus_sell_run(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Current buy zero-run minus current sell zero-run."""
    return _current_zero_run_length(insider_buy_count) - _current_zero_run_length(insider_sell_count)


def isl_099_officer_sell_zero_frac_1yr(officer_sell_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero officer sell dollar value."""
    zero = (officer_sell_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_100_director_sell_zero_frac_1yr(director_sell_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero director sell dollar value."""
    zero = (director_sell_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_101_total_silence_both_sides_score(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Combined bilateral silence: average of buy zero-frac and sell zero-frac
    over 252 days. High = both sides gone quiet simultaneously.
    """
    buy_zero  = (insider_buy_count  == 0).astype(float)
    sell_zero = (insider_sell_count == 0).astype(float)
    return (_rolling_mean(buy_zero, _TD_YEAR) + _rolling_mean(sell_zero, _TD_YEAR)) / 2.0


def isl_102_sell_active_days_collapse(insider_sell_count: pd.Series) -> pd.Series:
    """
    Ratio of sell-active days in last 63 days vs last 252 days (annualized).
    <1 = recent sell silence relative to history.
    """
    recent = _rolling_sum((insider_sell_count > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_sell_count > 0).astype(float), _TD_YEAR)
    return _safe_div(recent, hist)


def isl_103_sell_silence_zscore(insider_sell_count: pd.Series) -> pd.Series:
    """Z-score of current sell zero-run relative to expanding history."""
    run = _current_zero_run_length(insider_sell_count)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    return _safe_div(run - mu, sd)


def isl_104_buy_sell_silence_product(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """
    Product of buy zero-frac (1yr) and sell zero-frac (1yr).
    High only when BOTH sides are simultaneously silent.
    """
    buy_zero  = (insider_buy_count  == 0).astype(float)
    sell_zero = (insider_sell_count == 0).astype(float)
    return _rolling_mean(buy_zero, _TD_YEAR) * _rolling_mean(sell_zero, _TD_YEAR)


def isl_105_tenpct_buy_silence_months(tenpct_buy_count: pd.Series) -> pd.Series:
    """Days since last 10%-holder buy, expressed in months."""
    return _safe_div(_days_since_last_nonzero(tenpct_buy_count),
                     pd.Series(21.0, index=tenpct_buy_count.index))


# --- Group H (106-120): Share-based silence and value-weighted gaps ---

def isl_106_days_since_last_buy_shares(insider_buy_shares: pd.Series) -> pd.Series:
    """Days since last day with positive insider buy share volume."""
    return _days_since_last_nonzero(insider_buy_shares)


def isl_107_buy_shares_zero_run_days(insider_buy_shares: pd.Series) -> pd.Series:
    """Current consecutive zero-run for insider buy share volume."""
    return _current_zero_run_length(insider_buy_shares)


def isl_108_buy_shares_zero_frac_1yr(insider_buy_shares: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero insider buy share volume."""
    zero = (insider_buy_shares == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_109_sell_shares_zero_frac_1yr(insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero insider sell share volume."""
    zero = (insider_sell_shares == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_110_days_since_last_sell_shares(insider_sell_shares: pd.Series) -> pd.Series:
    """Days since last day with positive insider sell share volume."""
    return _days_since_last_nonzero(insider_sell_shares)


def isl_111_buy_value_silence_months(insider_buy_value: pd.Series) -> pd.Series:
    """Days since last positive buy value, expressed in months."""
    return _safe_div(_days_since_last_nonzero(insider_buy_value),
                     pd.Series(21.0, index=insider_buy_value.index))


def isl_112_buy_value_zero_frac_1yr(insider_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero insider buy dollar value."""
    zero = (insider_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_113_sell_value_zero_frac_1yr(insider_sell_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero insider sell dollar value."""
    zero = (insider_sell_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_114_buy_value_active_days_1yr(insider_buy_value: pd.Series) -> pd.Series:
    """Count of days in last 252 days with positive insider buy value."""
    active = (insider_buy_value > 0).astype(float)
    return _rolling_sum(active, _TD_YEAR)


def isl_115_buy_value_active_days_collapse(insider_buy_value: pd.Series) -> pd.Series:
    """Ratio of buy-value active days last 63 days vs last 252 (annualized)."""
    recent = _rolling_sum((insider_buy_value > 0).astype(float), _TD_QTR) * 4.0
    hist   = _rolling_sum((insider_buy_value > 0).astype(float), _TD_YEAR)
    return _safe_div(recent, hist)


def isl_116_buy_shares_active_days_1yr(insider_buy_shares: pd.Series) -> pd.Series:
    """Count of days in last 252 days with positive insider buy share volume."""
    active = (insider_buy_shares > 0).astype(float)
    return _rolling_sum(active, _TD_YEAR)


def isl_117_tenpct_buy_zero_run_months(tenpct_buy_count: pd.Series) -> pd.Series:
    """Current 10%-holder buy zero-run expressed in months."""
    return _safe_div(_current_zero_run_length(tenpct_buy_count),
                     pd.Series(21.0, index=tenpct_buy_count.index))


def isl_118_tenpct_buy_value_silence(tenpct_buy_value: pd.Series) -> pd.Series:
    """Days since last positive 10%-holder buy value."""
    return _days_since_last_nonzero(tenpct_buy_value)


def isl_119_tenpct_buy_value_zero_frac_1yr(tenpct_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero 10%-holder buy value."""
    zero = (tenpct_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_YEAR)


def isl_120_buy_shares_silence_zscore(insider_buy_shares: pd.Series) -> pd.Series:
    """Z-score of current buy-shares zero-run vs expanding history."""
    run = _current_zero_run_length(insider_buy_shares)
    mu  = run.expanding(min_periods=2).mean()
    sd  = run.expanding(min_periods=2).std()
    return _safe_div(run - mu, sd)


# --- Group I (121-135): Multi-window gap analysis and silence duration ratios ---

def isl_121_buy_gap_ratio_1mo_vs_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """
    Ratio of buy zero-frac (last 21 days) to buy zero-frac (last 252 days).
    >1 = recent month more silent than annual average.
    """
    zero = (insider_buy_count == 0).astype(float)
    return _safe_div(_rolling_mean(zero, _TD_MO), _rolling_mean(zero, _TD_YEAR))


def isl_122_buy_gap_ratio_1qtr_vs_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of buy zero-frac (63 days) to buy zero-frac (252 days)."""
    zero = (insider_buy_count == 0).astype(float)
    return _safe_div(_rolling_mean(zero, _TD_QTR), _rolling_mean(zero, _TD_YEAR))


def isl_123_buy_gap_ratio_1qtr_vs_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Ratio of buy zero-frac (63 days) to buy zero-frac (504 days)."""
    zero = (insider_buy_count == 0).astype(float)
    return _safe_div(_rolling_mean(zero, _TD_QTR), _rolling_mean(zero, _TD_2Y))


def isl_124_any_txn_gap_ratio_1mo_vs_1yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Any-txn zero-frac (21 days) / zero-frac (252 days)."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    zero     = (combined == 0).astype(float)
    return _safe_div(_rolling_mean(zero, _TD_MO), _rolling_mean(zero, _TD_YEAR))


def isl_125_silence_acceleration_1mo_vs_3mo(insider_buy_count: pd.Series) -> pd.Series:
    """Buy zero-frac (21 days) minus buy zero-frac (63 days). Positive = deepening silence."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_MO) - _rolling_mean(zero, _TD_QTR)


def isl_126_silence_acceleration_1qtr_vs_4qtr(insider_buy_count: pd.Series) -> pd.Series:
    """Buy zero-frac (63 days) minus buy zero-frac (252 days). Positive = deepening."""
    zero = (insider_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR) - _rolling_mean(zero, _TD_YEAR)


def isl_127_buy_count_sum_1mo(insider_buy_count: pd.Series) -> pd.Series:
    """Total buy transaction count in last 21 days. Low values near zero = silence."""
    return _rolling_sum(insider_buy_count, _TD_MO)


def isl_128_buy_count_sum_1qtr(insider_buy_count: pd.Series) -> pd.Series:
    """Total buy transaction count in last 63 days."""
    return _rolling_sum(insider_buy_count, _TD_QTR)


def isl_129_buy_count_sum_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Total buy transaction count in last 252 days."""
    return _rolling_sum(insider_buy_count, _TD_YEAR)


def isl_130_buy_count_sum_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Total buy transaction count in last 504 days."""
    return _rolling_sum(insider_buy_count, _TD_2Y)


def isl_131_buy_count_1qtr_vs_prior_1qtr(insider_buy_count: pd.Series) -> pd.Series:
    """Buy count in last 63 days minus buy count in prior 63 days (shift 63)."""
    recent = _rolling_sum(insider_buy_count, _TD_QTR)
    prior  = _rolling_sum(insider_buy_count, _TD_QTR).shift(_TD_QTR)
    return recent - prior


def isl_132_buy_count_1yr_vs_prior_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Buy count in last 252 days minus buy count in prior 252 days."""
    recent = _rolling_sum(insider_buy_count, _TD_YEAR)
    prior  = _rolling_sum(insider_buy_count, _TD_YEAR).shift(_TD_YEAR)
    return recent - prior


def isl_133_sell_count_1qtr_vs_prior_1qtr(insider_sell_count: pd.Series) -> pd.Series:
    """Sell count in last 63 days minus sell count in prior 63 days."""
    recent = _rolling_sum(insider_sell_count, _TD_QTR)
    prior  = _rolling_sum(insider_sell_count, _TD_QTR).shift(_TD_QTR)
    return recent - prior


def isl_134_buy_count_1qtr_pct_change(insider_buy_count: pd.Series) -> pd.Series:
    """Percent change in rolling 63-day buy count vs 63 days ago."""
    recent = _rolling_sum(insider_buy_count, _TD_QTR)
    prior  = recent.shift(_TD_QTR)
    return _safe_div(recent - prior, prior.abs())


def isl_135_buy_count_expanding_pct_rank(insider_buy_count: pd.Series) -> pd.Series:
    """Expanding percentile rank of rolling 63-day buy count. Near 0 = historically silent."""
    rolling_cnt = _rolling_sum(insider_buy_count, _TD_QTR)
    return rolling_cnt.expanding(min_periods=2).rank(pct=True)


# --- Group J (136-150): Advanced composite silence and withdrawal patterns ---

def isl_136_insider_shares_held_change_1yr(insider_shares_held: pd.Series) -> pd.Series:
    """Change in aggregate insider shares held over 252 days. Declining = net selling/silence."""
    return insider_shares_held - insider_shares_held.shift(_TD_YEAR)


def isl_137_insider_shares_held_pct_change_1yr(insider_shares_held: pd.Series) -> pd.Series:
    """Percent change in insider shares held over 252 days."""
    prior = insider_shares_held.shift(_TD_YEAR)
    return _safe_div(insider_shares_held - prior, prior.abs())


def isl_138_insider_shares_held_drawdown(insider_shares_held: pd.Series) -> pd.Series:
    """Insider shares held minus 2-year expanding peak. Negative = net reduction."""
    peak = insider_shares_held.rolling(_TD_2Y, min_periods=max(1, _TD_2Y // 4)).max()
    return insider_shares_held - peak


def isl_139_no_buyer_no_seller_flag(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Binary: 1 on days with zero buyers AND zero sellers simultaneously."""
    return ((insider_buyers == 0) & (insider_sellers == 0)).astype(float)


def isl_140_no_buyer_no_seller_frac_1qtr(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero buyers AND zero sellers."""
    flag = ((insider_buyers == 0) & (insider_sellers == 0)).astype(float)
    return _rolling_mean(flag, _TD_QTR)


def isl_141_no_buyer_no_seller_frac_1yr(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero buyers AND zero sellers."""
    flag = ((insider_buyers == 0) & (insider_sellers == 0)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def isl_142_buyer_count_sum_1qtr(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct buyers seen in last 63 days."""
    return _rolling_sum(insider_buyers, _TD_QTR)


def isl_143_buyer_count_sum_1yr(insider_buyers: pd.Series) -> pd.Series:
    """Total distinct buyers seen in last 252 days."""
    return _rolling_sum(insider_buyers, _TD_YEAR)


def isl_144_buyer_collapse_ratio(insider_buyers: pd.Series) -> pd.Series:
    """Buyers in last 63 days annualized vs last 252 days. <1 = recent withdrawal."""
    recent = _rolling_sum(insider_buyers, _TD_QTR) * 4.0
    hist   = _rolling_sum(insider_buyers, _TD_YEAR)
    return _safe_div(recent, hist)


def isl_145_seller_collapse_ratio(insider_sellers: pd.Series) -> pd.Series:
    """Sellers in last 63 days annualized vs last 252 days. <1 = recent withdrawal."""
    recent = _rolling_sum(insider_sellers, _TD_QTR) * 4.0
    hist   = _rolling_sum(insider_sellers, _TD_YEAR)
    return _safe_div(recent, hist)


def isl_146_buy_value_1qtr_vs_hist_mean(insider_buy_value: pd.Series) -> pd.Series:
    """Rolling 63-day buy value sum minus rolling 252-day mean of such sums."""
    qtr_sum  = _rolling_sum(insider_buy_value, _TD_QTR)
    hist_avg = _rolling_mean(qtr_sum, _TD_YEAR)
    return qtr_sum - hist_avg


def isl_147_silent_quarters_last_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """
    Count of complete 63-day quarters (non-overlapping, using shifted sums)
    in the last 504 days with zero total buys. Uses 4 shifted 63-day windows.
    """
    q1 = (_rolling_sum(insider_buy_count, _TD_QTR) == 0).astype(float)
    q2 = (_rolling_sum(insider_buy_count, _TD_QTR).shift(_TD_QTR)  == 0).astype(float)
    q3 = (_rolling_sum(insider_buy_count, _TD_QTR).shift(_TD_2Q)   == 0).astype(float)
    q4 = (_rolling_sum(insider_buy_count, _TD_QTR).shift(_TD_QTR * 3) == 0).astype(float)
    return q1 + q2 + q3 + q4


def isl_148_silent_quarters_last_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Count of recent 63-day windows with zero buys: current + 1 prior quarter."""
    q1 = (_rolling_sum(insider_buy_count, _TD_QTR) == 0).astype(float)
    q2 = (_rolling_sum(insider_buy_count, _TD_QTR).shift(_TD_QTR) == 0).astype(float)
    return q1 + q2


def isl_149_officer_buy_count_1yr_sum(officer_buy_count: pd.Series) -> pd.Series:
    """Total officer buy transaction count in last 252 days."""
    return _rolling_sum(officer_buy_count, _TD_YEAR)


def isl_150_grand_silence_composite(
    insider_buy_count: pd.Series,
    insider_sell_count: pd.Series,
    insider_buyers: pd.Series,
    officer_buy_count: pd.Series
) -> pd.Series:
    """
    Grand silence composite (4 components averaged, each 0-1):
      1. buy zero-frac over 252 days
      2. any-txn zero-frac over 252 days
      3. buyer zero-frac over 252 days
      4. officer buy zero-frac over 252 days
    Higher = deeper multi-dimensional silence.
    """
    buy_zero    = (insider_buy_count  == 0).astype(float)
    txn_zero    = ((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float)
    buyer_zero  = (insider_buyers     == 0).astype(float)
    offr_zero   = (officer_buy_count  == 0).astype(float)
    c1 = _rolling_mean(buy_zero,   _TD_YEAR)
    c2 = _rolling_mean(txn_zero,   _TD_YEAR)
    c3 = _rolling_mean(buyer_zero, _TD_YEAR)
    c4 = _rolling_mean(offr_zero,  _TD_YEAR)
    return (c1 + c2 + c3 + c4) / 4.0


# ── Feature functions 176-200 ─────────────────────────────────────────────────

# --- Group K2 (176-188): Director/CFO/10%-holder extended silence metrics ---

def isl_176_director_buy_silence_months(director_buy_count: pd.Series) -> pd.Series:
    """Days since last director buy, expressed in months."""
    return _safe_div(_days_since_last_nonzero(director_buy_count),
                     pd.Series(21.0, index=director_buy_count.index))


def isl_177_director_buy_zero_frac_1qtr(director_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero director buy transactions."""
    zero = (director_buy_count == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_178_director_buy_zero_run_months(director_buy_count: pd.Series) -> pd.Series:
    """Current director buy zero-run expressed in months."""
    return _safe_div(_current_zero_run_length(director_buy_count),
                     pd.Series(21.0, index=director_buy_count.index))


def isl_179_director_buy_run_gt_1yr_flag(director_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if director buy zero-run exceeds 252 days."""
    return (_current_zero_run_length(director_buy_count) > _TD_YEAR).astype(float)


def isl_180_cfo_buy_zero_frac_1qtr(cfo_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero CFO buy value."""
    zero = (cfo_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_181_cfo_buy_silence_months(cfo_buy_value: pd.Series) -> pd.Series:
    """Days since last CFO buy value, expressed in months."""
    return _safe_div(_days_since_last_nonzero(cfo_buy_value),
                     pd.Series(21.0, index=cfo_buy_value.index))


def isl_182_cfo_buy_run_gt_1yr_flag(cfo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if CFO buy zero-run exceeds 252 days."""
    return (_current_zero_run_length(cfo_buy_value) > _TD_YEAR).astype(float)


def isl_183_tenpct_buy_run_gt_1yr_flag(tenpct_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if 10%-holder buy zero-run exceeds 252 days."""
    return (_current_zero_run_length(tenpct_buy_count) > _TD_YEAR).astype(float)


def isl_184_tenpct_buy_value_zero_frac_1qtr(tenpct_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero 10%-holder buy value."""
    zero = (tenpct_buy_value == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_185_tenpct_buy_value_run_months(tenpct_buy_value: pd.Series) -> pd.Series:
    """Current 10%-holder buy value zero-run expressed in months."""
    return _safe_div(_current_zero_run_length(tenpct_buy_value),
                     pd.Series(21.0, index=tenpct_buy_value.index))


def isl_186_officer_sell_zero_frac_1qtr(officer_sell_value: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero officer sell dollar value."""
    zero = (officer_sell_value == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_187_director_sell_zero_frac_1qtr(director_sell_value: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero director sell dollar value."""
    zero = (director_sell_value == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_188_ceo_cfo_silence_avg_months(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Average of CEO and CFO buy silence (days since last), in months."""
    ceo_m = _safe_div(_days_since_last_nonzero(ceo_buy_value),
                      pd.Series(21.0, index=ceo_buy_value.index))
    cfo_m = _safe_div(_days_since_last_nonzero(cfo_buy_value),
                      pd.Series(21.0, index=cfo_buy_value.index))
    return (ceo_m + cfo_m) / 2.0


# --- Group L2 (189-200): Shares held, share-based silence, and extended composites ---

def isl_189_insider_shares_held_change_1qtr(insider_shares_held: pd.Series) -> pd.Series:
    """Change in insider shares held over 63 days. Negative = recent reduction."""
    return insider_shares_held - insider_shares_held.shift(_TD_QTR)


def isl_190_insider_shares_held_zscore_1yr(insider_shares_held: pd.Series) -> pd.Series:
    """Z-score of insider shares held relative to rolling 252-day mean/std."""
    mu = _rolling_mean(insider_shares_held, _TD_YEAR)
    sd = _rolling_std(insider_shares_held, _TD_YEAR)
    return _safe_div(insider_shares_held - mu, sd)


def isl_191_buy_shares_zero_frac_1qtr(insider_buy_shares: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero insider buy share volume."""
    zero = (insider_buy_shares == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_192_sell_shares_zero_frac_1qtr(insider_sell_shares: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero insider sell share volume."""
    zero = (insider_sell_shares == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_193_buy_shares_zero_run_days(insider_buy_shares: pd.Series) -> pd.Series:
    """Current consecutive zero-run for insider buy share volume (days)."""
    return _current_zero_run_length(insider_buy_shares)


def isl_194_sell_shares_zero_run_days(insider_sell_shares: pd.Series) -> pd.Series:
    """Current consecutive zero-run for insider sell share volume (days)."""
    return _current_zero_run_length(insider_sell_shares)


def isl_195_buy_shares_run_gt_1qtr_flag(insider_buy_shares: pd.Series) -> pd.Series:
    """Binary: 1 if buy-share zero-run exceeds 63 days."""
    return (_current_zero_run_length(insider_buy_shares) > _TD_QTR).astype(float)


def isl_196_seller_zero_frac_1qtr(insider_sellers: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero distinct sellers."""
    zero = (insider_sellers == 0).astype(float)
    return _rolling_mean(zero, _TD_QTR)


def isl_197_seller_zero_run_days(insider_sellers: pd.Series) -> pd.Series:
    """Current consecutive zero-run for distinct seller count."""
    return _current_zero_run_length(insider_sellers)


def isl_198_buyer_seller_run_product(insider_buyers: pd.Series, insider_sellers: pd.Series) -> pd.Series:
    """Product of buyer zero-run and seller zero-run. High when BOTH sides in long silence."""
    buy_run  = _current_zero_run_length(insider_buyers)
    sell_run = _current_zero_run_length(insider_sellers)
    return buy_run * sell_run


def isl_199_executive_silence_composite(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series, officer_buy_count: pd.Series) -> pd.Series:
    """
    Executive silence composite: average of CEO, CFO, and officer buy zero-fracs
    over 252 days. Near 1 = all executive buy channels silent.
    """
    ceo_z  = _rolling_mean((ceo_buy_value   == 0).astype(float), _TD_YEAR)
    cfo_z  = _rolling_mean((cfo_buy_value   == 0).astype(float), _TD_YEAR)
    offr_z = _rolling_mean((officer_buy_count == 0).astype(float), _TD_YEAR)
    return (ceo_z + cfo_z + offr_z) / 3.0


def isl_200_shares_value_silence_composite(insider_buy_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_shares: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    """
    Shares-and-value silence composite: average of buy-shares, buy-value,
    sell-shares, and sell-value zero-fracs over 252 days.
    """
    c1 = _rolling_mean((insider_buy_shares  == 0).astype(float), _TD_YEAR)
    c2 = _rolling_mean((insider_buy_value   == 0).astype(float), _TD_YEAR)
    c3 = _rolling_mean((insider_sell_shares == 0).astype(float), _TD_YEAR)
    c4 = _rolling_mean((insider_sell_value  == 0).astype(float), _TD_YEAR)
    return (c1 + c2 + c3 + c4) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────
INSIDER_SILENCE_REGISTRY_076_150 = {
    "isl_076_days_since_last_director_buy":        {"inputs": ["director_buy_count"],                                              "func": isl_076_days_since_last_director_buy},
    "isl_077_director_buy_zero_run_days":           {"inputs": ["director_buy_count"],                                              "func": isl_077_director_buy_zero_run_days},
    "isl_078_director_buy_zero_frac_1yr":           {"inputs": ["director_buy_count"],                                              "func": isl_078_director_buy_zero_frac_1yr},
    "isl_079_days_since_last_ceo_buy":              {"inputs": ["ceo_buy_value"],                                                   "func": isl_079_days_since_last_ceo_buy},
    "isl_080_ceo_buy_zero_run_days":                {"inputs": ["ceo_buy_value"],                                                   "func": isl_080_ceo_buy_zero_run_days},
    "isl_081_ceo_buy_zero_frac_1yr":                {"inputs": ["ceo_buy_value"],                                                   "func": isl_081_ceo_buy_zero_frac_1yr},
    "isl_082_days_since_last_cfo_buy":              {"inputs": ["cfo_buy_value"],                                                   "func": isl_082_days_since_last_cfo_buy},
    "isl_083_cfo_buy_zero_run_days":                {"inputs": ["cfo_buy_value"],                                                   "func": isl_083_cfo_buy_zero_run_days},
    "isl_084_cfo_buy_zero_frac_1yr":                {"inputs": ["cfo_buy_value"],                                                   "func": isl_084_cfo_buy_zero_frac_1yr},
    "isl_085_days_since_last_tenpct_buy":           {"inputs": ["tenpct_buy_count"],                                                "func": isl_085_days_since_last_tenpct_buy},
    "isl_086_tenpct_buy_zero_run_days":             {"inputs": ["tenpct_buy_count"],                                                "func": isl_086_tenpct_buy_zero_run_days},
    "isl_087_tenpct_buy_zero_frac_1yr":             {"inputs": ["tenpct_buy_count"],                                                "func": isl_087_tenpct_buy_zero_frac_1yr},
    "isl_088_officer_vs_director_silence_gap":      {"inputs": ["officer_buy_count", "director_buy_count"],                        "func": isl_088_officer_vs_director_silence_gap},
    "isl_089_ceo_cfo_combined_zero_run":            {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                 "func": isl_089_ceo_cfo_combined_zero_run},
    "isl_090_ceo_buy_silence_gt_1yr_flag":          {"inputs": ["ceo_buy_value"],                                                   "func": isl_090_ceo_buy_silence_gt_1yr_flag},
    "isl_091_days_since_last_sell_value":           {"inputs": ["insider_sell_value"],                                              "func": isl_091_days_since_last_sell_value},
    "isl_092_sell_value_zero_run_days":             {"inputs": ["insider_sell_value"],                                              "func": isl_092_sell_value_zero_run_days},
    "isl_093_sell_value_zero_frac_1qtr":            {"inputs": ["insider_sell_value"],                                              "func": isl_093_sell_value_zero_frac_1qtr},
    "isl_094_seller_zero_frac_1yr":                 {"inputs": ["insider_sellers"],                                                 "func": isl_094_seller_zero_frac_1yr},
    "isl_095_days_since_last_seller":               {"inputs": ["insider_sellers"],                                                 "func": isl_095_days_since_last_seller},
    "isl_096_sell_silence_months":                  {"inputs": ["insider_sell_count"],                                              "func": isl_096_sell_silence_months},
    "isl_097_buy_silence_minus_sell_silence":       {"inputs": ["insider_buy_count", "insider_sell_count"],                        "func": isl_097_buy_silence_minus_sell_silence},
    "isl_098_buy_run_minus_sell_run":               {"inputs": ["insider_buy_count", "insider_sell_count"],                        "func": isl_098_buy_run_minus_sell_run},
    "isl_099_officer_sell_zero_frac_1yr":           {"inputs": ["officer_sell_value"],                                              "func": isl_099_officer_sell_zero_frac_1yr},
    "isl_100_director_sell_zero_frac_1yr":          {"inputs": ["director_sell_value"],                                             "func": isl_100_director_sell_zero_frac_1yr},
    "isl_101_total_silence_both_sides_score":       {"inputs": ["insider_buy_count", "insider_sell_count"],                        "func": isl_101_total_silence_both_sides_score},
    "isl_102_sell_active_days_collapse":            {"inputs": ["insider_sell_count"],                                              "func": isl_102_sell_active_days_collapse},
    "isl_103_sell_silence_zscore":                  {"inputs": ["insider_sell_count"],                                              "func": isl_103_sell_silence_zscore},
    "isl_104_buy_sell_silence_product":             {"inputs": ["insider_buy_count", "insider_sell_count"],                        "func": isl_104_buy_sell_silence_product},
    "isl_105_tenpct_buy_silence_months":            {"inputs": ["tenpct_buy_count"],                                                "func": isl_105_tenpct_buy_silence_months},
    "isl_106_days_since_last_buy_shares":           {"inputs": ["insider_buy_shares"],                                              "func": isl_106_days_since_last_buy_shares},
    "isl_107_buy_shares_zero_run_days":             {"inputs": ["insider_buy_shares"],                                              "func": isl_107_buy_shares_zero_run_days},
    "isl_108_buy_shares_zero_frac_1yr":             {"inputs": ["insider_buy_shares"],                                              "func": isl_108_buy_shares_zero_frac_1yr},
    "isl_109_sell_shares_zero_frac_1yr":            {"inputs": ["insider_sell_shares"],                                             "func": isl_109_sell_shares_zero_frac_1yr},
    "isl_110_days_since_last_sell_shares":          {"inputs": ["insider_sell_shares"],                                             "func": isl_110_days_since_last_sell_shares},
    "isl_111_buy_value_silence_months":             {"inputs": ["insider_buy_value"],                                               "func": isl_111_buy_value_silence_months},
    "isl_112_buy_value_zero_frac_1yr":              {"inputs": ["insider_buy_value"],                                               "func": isl_112_buy_value_zero_frac_1yr},
    "isl_113_sell_value_zero_frac_1yr":             {"inputs": ["insider_sell_value"],                                              "func": isl_113_sell_value_zero_frac_1yr},
    "isl_114_buy_value_active_days_1yr":            {"inputs": ["insider_buy_value"],                                               "func": isl_114_buy_value_active_days_1yr},
    "isl_115_buy_value_active_days_collapse":       {"inputs": ["insider_buy_value"],                                               "func": isl_115_buy_value_active_days_collapse},
    "isl_116_buy_shares_active_days_1yr":           {"inputs": ["insider_buy_shares"],                                              "func": isl_116_buy_shares_active_days_1yr},
    "isl_117_tenpct_buy_zero_run_months":           {"inputs": ["tenpct_buy_count"],                                                "func": isl_117_tenpct_buy_zero_run_months},
    "isl_118_tenpct_buy_value_silence":             {"inputs": ["tenpct_buy_value"],                                                "func": isl_118_tenpct_buy_value_silence},
    "isl_119_tenpct_buy_value_zero_frac_1yr":       {"inputs": ["tenpct_buy_value"],                                                "func": isl_119_tenpct_buy_value_zero_frac_1yr},
    "isl_120_buy_shares_silence_zscore":            {"inputs": ["insider_buy_shares"],                                              "func": isl_120_buy_shares_silence_zscore},
    "isl_121_buy_gap_ratio_1mo_vs_1yr":             {"inputs": ["insider_buy_count"],                                               "func": isl_121_buy_gap_ratio_1mo_vs_1yr},
    "isl_122_buy_gap_ratio_1qtr_vs_1yr":            {"inputs": ["insider_buy_count"],                                               "func": isl_122_buy_gap_ratio_1qtr_vs_1yr},
    "isl_123_buy_gap_ratio_1qtr_vs_2yr":            {"inputs": ["insider_buy_count"],                                               "func": isl_123_buy_gap_ratio_1qtr_vs_2yr},
    "isl_124_any_txn_gap_ratio_1mo_vs_1yr":         {"inputs": ["insider_buy_count", "insider_sell_count"],                        "func": isl_124_any_txn_gap_ratio_1mo_vs_1yr},
    "isl_125_silence_acceleration_1mo_vs_3mo":      {"inputs": ["insider_buy_count"],                                               "func": isl_125_silence_acceleration_1mo_vs_3mo},
    "isl_126_silence_acceleration_1qtr_vs_4qtr":    {"inputs": ["insider_buy_count"],                                               "func": isl_126_silence_acceleration_1qtr_vs_4qtr},
    "isl_127_buy_count_sum_1mo":                    {"inputs": ["insider_buy_count"],                                               "func": isl_127_buy_count_sum_1mo},
    "isl_128_buy_count_sum_1qtr":                   {"inputs": ["insider_buy_count"],                                               "func": isl_128_buy_count_sum_1qtr},
    "isl_129_buy_count_sum_1yr":                    {"inputs": ["insider_buy_count"],                                               "func": isl_129_buy_count_sum_1yr},
    "isl_130_buy_count_sum_2yr":                    {"inputs": ["insider_buy_count"],                                               "func": isl_130_buy_count_sum_2yr},
    "isl_131_buy_count_1qtr_vs_prior_1qtr":         {"inputs": ["insider_buy_count"],                                               "func": isl_131_buy_count_1qtr_vs_prior_1qtr},
    "isl_132_buy_count_1yr_vs_prior_1yr":           {"inputs": ["insider_buy_count"],                                               "func": isl_132_buy_count_1yr_vs_prior_1yr},
    "isl_133_sell_count_1qtr_vs_prior_1qtr":        {"inputs": ["insider_sell_count"],                                              "func": isl_133_sell_count_1qtr_vs_prior_1qtr},
    "isl_134_buy_count_1qtr_pct_change":            {"inputs": ["insider_buy_count"],                                               "func": isl_134_buy_count_1qtr_pct_change},
    "isl_135_buy_count_expanding_pct_rank":         {"inputs": ["insider_buy_count"],                                               "func": isl_135_buy_count_expanding_pct_rank},
    "isl_136_insider_shares_held_change_1yr":       {"inputs": ["insider_shares_held"],                                             "func": isl_136_insider_shares_held_change_1yr},
    "isl_137_insider_shares_held_pct_change_1yr":   {"inputs": ["insider_shares_held"],                                             "func": isl_137_insider_shares_held_pct_change_1yr},
    "isl_138_insider_shares_held_drawdown":         {"inputs": ["insider_shares_held"],                                             "func": isl_138_insider_shares_held_drawdown},
    "isl_139_no_buyer_no_seller_flag":              {"inputs": ["insider_buyers", "insider_sellers"],                               "func": isl_139_no_buyer_no_seller_flag},
    "isl_140_no_buyer_no_seller_frac_1qtr":         {"inputs": ["insider_buyers", "insider_sellers"],                               "func": isl_140_no_buyer_no_seller_frac_1qtr},
    "isl_141_no_buyer_no_seller_frac_1yr":          {"inputs": ["insider_buyers", "insider_sellers"],                               "func": isl_141_no_buyer_no_seller_frac_1yr},
    "isl_142_buyer_count_sum_1qtr":                 {"inputs": ["insider_buyers"],                                                  "func": isl_142_buyer_count_sum_1qtr},
    "isl_143_buyer_count_sum_1yr":                  {"inputs": ["insider_buyers"],                                                  "func": isl_143_buyer_count_sum_1yr},
    "isl_144_buyer_collapse_ratio":                 {"inputs": ["insider_buyers"],                                                  "func": isl_144_buyer_collapse_ratio},
    "isl_145_seller_collapse_ratio":                {"inputs": ["insider_sellers"],                                                  "func": isl_145_seller_collapse_ratio},
    "isl_146_buy_value_1qtr_vs_hist_mean":          {"inputs": ["insider_buy_value"],                                               "func": isl_146_buy_value_1qtr_vs_hist_mean},
    "isl_147_silent_quarters_last_2yr":             {"inputs": ["insider_buy_count"],                                               "func": isl_147_silent_quarters_last_2yr},
    "isl_148_silent_quarters_last_1yr":             {"inputs": ["insider_buy_count"],                                               "func": isl_148_silent_quarters_last_1yr},
    "isl_149_officer_buy_count_1yr_sum":            {"inputs": ["officer_buy_count"],                                               "func": isl_149_officer_buy_count_1yr_sum},
    "isl_150_grand_silence_composite":              {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "officer_buy_count"], "func": isl_150_grand_silence_composite},
    "isl_176_director_buy_silence_months":          {"inputs": ["director_buy_count"],                                                              "func": isl_176_director_buy_silence_months},
    "isl_177_director_buy_zero_frac_1qtr":          {"inputs": ["director_buy_count"],                                                              "func": isl_177_director_buy_zero_frac_1qtr},
    "isl_178_director_buy_zero_run_months":          {"inputs": ["director_buy_count"],                                                              "func": isl_178_director_buy_zero_run_months},
    "isl_179_director_buy_run_gt_1yr_flag":          {"inputs": ["director_buy_count"],                                                              "func": isl_179_director_buy_run_gt_1yr_flag},
    "isl_180_cfo_buy_zero_frac_1qtr":               {"inputs": ["cfo_buy_value"],                                                                   "func": isl_180_cfo_buy_zero_frac_1qtr},
    "isl_181_cfo_buy_silence_months":               {"inputs": ["cfo_buy_value"],                                                                   "func": isl_181_cfo_buy_silence_months},
    "isl_182_cfo_buy_run_gt_1yr_flag":              {"inputs": ["cfo_buy_value"],                                                                   "func": isl_182_cfo_buy_run_gt_1yr_flag},
    "isl_183_tenpct_buy_run_gt_1yr_flag":           {"inputs": ["tenpct_buy_count"],                                                                "func": isl_183_tenpct_buy_run_gt_1yr_flag},
    "isl_184_tenpct_buy_value_zero_frac_1qtr":      {"inputs": ["tenpct_buy_value"],                                                                "func": isl_184_tenpct_buy_value_zero_frac_1qtr},
    "isl_185_tenpct_buy_value_run_months":          {"inputs": ["tenpct_buy_value"],                                                                "func": isl_185_tenpct_buy_value_run_months},
    "isl_186_officer_sell_zero_frac_1qtr":          {"inputs": ["officer_sell_value"],                                                              "func": isl_186_officer_sell_zero_frac_1qtr},
    "isl_187_director_sell_zero_frac_1qtr":         {"inputs": ["director_sell_value"],                                                             "func": isl_187_director_sell_zero_frac_1qtr},
    "isl_188_ceo_cfo_silence_avg_months":           {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                                  "func": isl_188_ceo_cfo_silence_avg_months},
    "isl_189_insider_shares_held_change_1qtr":      {"inputs": ["insider_shares_held"],                                                             "func": isl_189_insider_shares_held_change_1qtr},
    "isl_190_insider_shares_held_zscore_1yr":       {"inputs": ["insider_shares_held"],                                                             "func": isl_190_insider_shares_held_zscore_1yr},
    "isl_191_buy_shares_zero_frac_1qtr":            {"inputs": ["insider_buy_shares"],                                                              "func": isl_191_buy_shares_zero_frac_1qtr},
    "isl_192_sell_shares_zero_frac_1qtr":           {"inputs": ["insider_sell_shares"],                                                             "func": isl_192_sell_shares_zero_frac_1qtr},
    "isl_193_buy_shares_zero_run_days":             {"inputs": ["insider_buy_shares"],                                                              "func": isl_193_buy_shares_zero_run_days},
    "isl_194_sell_shares_zero_run_days":            {"inputs": ["insider_sell_shares"],                                                             "func": isl_194_sell_shares_zero_run_days},
    "isl_195_buy_shares_run_gt_1qtr_flag":          {"inputs": ["insider_buy_shares"],                                                              "func": isl_195_buy_shares_run_gt_1qtr_flag},
    "isl_196_seller_zero_frac_1qtr":               {"inputs": ["insider_sellers"],                                                                  "func": isl_196_seller_zero_frac_1qtr},
    "isl_197_seller_zero_run_days":                {"inputs": ["insider_sellers"],                                                                  "func": isl_197_seller_zero_run_days},
    "isl_198_buyer_seller_run_product":            {"inputs": ["insider_buyers", "insider_sellers"],                                                "func": isl_198_buyer_seller_run_product},
    "isl_199_executive_silence_composite":         {"inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_count"],                             "func": isl_199_executive_silence_composite},
    "isl_200_shares_value_silence_composite":      {"inputs": ["insider_buy_shares", "insider_buy_value", "insider_sell_shares", "insider_sell_value"], "func": isl_200_shares_value_silence_composite},
}
