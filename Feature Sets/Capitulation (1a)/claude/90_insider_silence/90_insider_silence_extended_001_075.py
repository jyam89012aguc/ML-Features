"""
90_insider_silence — Extended Features 001-075
Domain: absence / withdrawal of insider activity — additional silence variants:
        new lookback windows, intensified streak/gap metrics, breadth-of-silence
        ratios, decay-weighted scores, additional insider-role series, and
        cross-series silence composites NOT covered by the four base files.
Asset class: US equities | Sharadar SF2 insider transactions (daily-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

These features explore DIFFERENT angles than base_001_075 / base_076_150 /
2nd_derivatives / 3rd_derivatives: half-year & 3-year windows, weeks/quarters
unit variants, longest-run-fraction ratios, silence dispersion, EWM-decay
silence on additional role series (director/CEO/CFO/10pct), and breadth scores.

SF2 Daily-Aggregated Insider Series Contract
---------------------------------------------
Inputs are daily-frequency pandas Series aggregated from Sharadar SF2 insider
transaction records. Most days carry ZERO (no insider transaction filed) —
this zero-dominated structure IS the signal domain. Series are NOT
forward-filled; emptiness/gaps/withdrawal are the measured quantities.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252   # 1 year in trading days
_TD_2Y   = 504
_TD_3Y   = 756
_TD_QTR  = 63    # 1 quarter
_TD_2Q   = 126
_TD_MO   = 21    # 1 month
_TD_WK   = 5     # 1 week
_EPS     = 1e-9

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
    """Rows elapsed since the last strictly-positive observation (backward-only)."""
    nonzero = (s > 0).astype(int)
    idx = pd.Series(np.where(nonzero.values, np.arange(len(s)), np.nan), index=s.index)
    last_pos = idx.ffill()
    row_num = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    result = row_num - last_pos
    result = result.where(last_pos.notna(), row_num + 1)
    return result


def _current_zero_run_length(s: pd.Series) -> pd.Series:
    """Count of consecutive trailing zeros up to and including each row."""
    is_zero = (s == 0).astype(int).values
    run = np.zeros(len(s), dtype=float)
    for i in range(len(is_zero)):
        if i == 0:
            run[i] = float(is_zero[i])
        else:
            run[i] = (run[i - 1] + 1) * is_zero[i]
    return pd.Series(run, index=s.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional silence windows and unit variants ---

def isl_ext_001_buy_zero_frac_1wk(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 5 days with zero buy transactions."""
    return _rolling_mean((insider_buy_count == 0).astype(float), _TD_WK)


def isl_ext_002_buy_zero_frac_2mo(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 42 days with zero buy transactions."""
    return _rolling_mean((insider_buy_count == 0).astype(float), 2 * _TD_MO)


def isl_ext_003_buy_zero_frac_2q(insider_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 126 days with zero buy transactions."""
    return _rolling_mean((insider_buy_count == 0).astype(float), _TD_2Q)


def isl_ext_004_any_txn_zero_frac_3yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 756 days with no insider transaction of any kind."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return _rolling_mean((combined == 0).astype(float), _TD_3Y)


def isl_ext_005_sell_zero_frac_2yr(insider_sell_count: pd.Series) -> pd.Series:
    """Fraction of last 504 days with zero sell transactions."""
    return _rolling_mean((insider_sell_count == 0).astype(float), _TD_2Y)


def isl_ext_006_buyer_zero_frac_1yr(insider_buyers: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero distinct insider buyers."""
    return _rolling_mean((insider_buyers == 0).astype(float), _TD_YEAR)


def isl_ext_007_buy_silence_half_years(insider_buy_count: pd.Series) -> pd.Series:
    """Days since last buy expressed in half-years (divided by 126)."""
    return _days_since_last_nonzero(insider_buy_count) / 126.0


def isl_ext_008_buy_silence_years(insider_buy_count: pd.Series) -> pd.Series:
    """Days since last buy expressed in years (divided by 252)."""
    return _days_since_last_nonzero(insider_buy_count) / 252.0


def isl_ext_009_sell_silence_quarters(insider_sell_count: pd.Series) -> pd.Series:
    """Days since last sell expressed in quarters (divided by 63)."""
    return _days_since_last_nonzero(insider_sell_count) / 63.0


def isl_ext_010_buy_zero_run_years(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run expressed in years (divided by 252)."""
    return _current_zero_run_length(insider_buy_count) / 252.0


def isl_ext_011_any_txn_zero_run_weeks(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Current any-transaction zero-run expressed in weeks."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return _current_zero_run_length(combined) / 5.0


def isl_ext_012_buyer_silence_weeks(insider_buyers: pd.Series) -> pd.Series:
    """Days since last distinct buyer expressed in weeks."""
    return _days_since_last_nonzero(insider_buyers) / 5.0


# --- Group B (013-024): Intensified silence threshold flags ---

def isl_ext_013_buy_silence_gt_2mo_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if no buy for more than 42 trading days (2 months)."""
    return (_days_since_last_nonzero(insider_buy_count) > 2 * _TD_MO).astype(float)


def isl_ext_014_buy_silence_gt_2qtr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if no buy for more than 126 trading days (2 quarters)."""
    return (_days_since_last_nonzero(insider_buy_count) > _TD_2Q).astype(float)


def isl_ext_015_buy_silence_gt_2yr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if no buy for more than 504 trading days (2 years)."""
    return (_days_since_last_nonzero(insider_buy_count) > _TD_2Y).astype(float)


def isl_ext_016_buy_run_gt_2mo_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if current buy zero-run exceeds 42 days."""
    return (_current_zero_run_length(insider_buy_count) > 2 * _TD_MO).astype(float)


def isl_ext_017_buy_run_gt_2yr_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if current buy zero-run exceeds 504 days."""
    return (_current_zero_run_length(insider_buy_count) > _TD_2Y).astype(float)


def isl_ext_018_sell_run_gt_1qtr_flag(insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if current sell zero-run exceeds 63 days."""
    return (_current_zero_run_length(insider_sell_count) > _TD_QTR).astype(float)


def isl_ext_019_any_txn_run_gt_1yr_flag(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if any-transaction zero-run exceeds 252 days."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return (_current_zero_run_length(combined) > _TD_YEAR).astype(float)


def isl_ext_020_buyer_run_gt_1qtr_flag(insider_buyers: pd.Series) -> pd.Series:
    """Binary: 1 if no distinct buyer seen for more than 63 days."""
    return (_current_zero_run_length(insider_buyers) > _TD_QTR).astype(float)


def isl_ext_021_buy_value_run_gt_1yr_flag(insider_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if buy-value zero-run exceeds 252 days."""
    return (_current_zero_run_length(insider_buy_value) > _TD_YEAR).astype(float)


def isl_ext_022_officer_buy_run_gt_1qtr_flag(officer_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if officer buy zero-run exceeds 63 days."""
    return (_current_zero_run_length(officer_buy_count) > _TD_QTR).astype(float)


def isl_ext_023_buy_zero_frac_1yr_gt_90pct_flag(insider_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if more than 90% of last 252 days had zero buys."""
    return (_rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR) > 0.90).astype(float)


def isl_ext_024_no_activity_full_qtr_flag(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Binary: 1 if the last 63 days had zero transactions of any kind."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return (_rolling_sum((combined > 0).astype(float), _TD_QTR) == 0).astype(float)


# --- Group C (025-036): Director / CEO / CFO / 10pct role silence variants ---

def isl_ext_025_director_buy_silence_months(director_buy_count: pd.Series) -> pd.Series:
    """Days since last director buy, expressed in months."""
    return _days_since_last_nonzero(director_buy_count) / 21.0


def isl_ext_026_director_buy_zero_frac_1qtr(director_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 63 days with zero director buy activity."""
    return _rolling_mean((director_buy_count == 0).astype(float), _TD_QTR)


def isl_ext_027_director_buy_run_gt_1yr_flag(director_buy_count: pd.Series) -> pd.Series:
    """Binary: 1 if director buy zero-run exceeds 252 days."""
    return (_current_zero_run_length(director_buy_count) > _TD_YEAR).astype(float)


def isl_ext_028_ceo_buy_silence_quarters(ceo_buy_value: pd.Series) -> pd.Series:
    """Days since last CEO buy value, expressed in quarters."""
    return _days_since_last_nonzero(ceo_buy_value) / 63.0


def isl_ext_029_ceo_buy_zero_frac_2yr(ceo_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 504 days with zero CEO buy value."""
    return _rolling_mean((ceo_buy_value == 0).astype(float), _TD_2Y)


def isl_ext_030_cfo_buy_silence_quarters(cfo_buy_value: pd.Series) -> pd.Series:
    """Days since last CFO buy value, expressed in quarters."""
    return _days_since_last_nonzero(cfo_buy_value) / 63.0


def isl_ext_031_cfo_buy_zero_frac_2yr(cfo_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 504 days with zero CFO buy value."""
    return _rolling_mean((cfo_buy_value == 0).astype(float), _TD_2Y)


def isl_ext_032_tenpct_buy_silence_quarters(tenpct_buy_count: pd.Series) -> pd.Series:
    """Days since last 10%-holder buy, expressed in quarters."""
    return _days_since_last_nonzero(tenpct_buy_count) / 63.0


def isl_ext_033_tenpct_buy_zero_frac_2yr(tenpct_buy_count: pd.Series) -> pd.Series:
    """Fraction of last 504 days with zero 10%-holder buy transactions."""
    return _rolling_mean((tenpct_buy_count == 0).astype(float), _TD_2Y)


def isl_ext_034_ceo_cfo_combined_zero_frac_1yr(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Fraction of last 252 days with zero combined CEO+CFO buy value."""
    combined = ceo_buy_value + cfo_buy_value
    return _rolling_mean((combined == 0).astype(float), _TD_YEAR)


def isl_ext_035_director_vs_officer_silence_gap(director_buy_count: pd.Series, officer_buy_count: pd.Series) -> pd.Series:
    """Director buy silence days minus officer buy silence days."""
    return _days_since_last_nonzero(director_buy_count) - _days_since_last_nonzero(officer_buy_count)


def isl_ext_036_topbrass_silence_min(ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """Most recent top-brass buy: min of CEO and CFO buy-value silence days."""
    ceo = _days_since_last_nonzero(ceo_buy_value)
    cfo = _days_since_last_nonzero(cfo_buy_value)
    return pd.concat([ceo, cfo], axis=1).min(axis=1)


# --- Group D (037-048): Longest-run, run-fraction and dispersion metrics ---

def isl_ext_037_longest_buy_silence_3yr(insider_buy_count: pd.Series) -> pd.Series:
    """Longest buy zero-run observed in the trailing 756 days."""
    return _rolling_max(_current_zero_run_length(insider_buy_count), _TD_3Y)


def isl_ext_038_longest_any_txn_silence_2yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Longest any-transaction zero-run in the trailing 504 days."""
    combined = (insider_buy_count + insider_sell_count).clip(lower=0)
    return _rolling_max(_current_zero_run_length(combined), _TD_2Y)


def isl_ext_039_buy_run_pct_of_2yr_longest(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run as fraction of the longest run in trailing 504 days."""
    run = _current_zero_run_length(insider_buy_count)
    return _safe_div(run, _rolling_max(run, _TD_2Y))


def isl_ext_040_buy_run_minus_1yr_max(insider_buy_count: pd.Series) -> pd.Series:
    """Current buy zero-run minus the longest run seen in trailing 252 days."""
    run = _current_zero_run_length(insider_buy_count)
    return run - _rolling_max(run, _TD_YEAR)


def isl_ext_041_buy_silence_dispersion_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Rolling 252-day standard deviation of the buy zero-run length."""
    return _rolling_std(_current_zero_run_length(insider_buy_count), _TD_YEAR)


def isl_ext_042_buy_silence_cv_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Coefficient of variation of the buy zero-run over trailing 252 days."""
    run = _current_zero_run_length(insider_buy_count)
    return _safe_div(_rolling_std(run, _TD_YEAR), _rolling_mean(run, _TD_YEAR))


def isl_ext_043_days_since_buy_vs_1yr_median(insider_buy_count: pd.Series) -> pd.Series:
    """Days-since-last-buy minus its rolling 252-day median."""
    dsn = _days_since_last_nonzero(insider_buy_count)
    return dsn - _rolling_median(dsn, _TD_YEAR)


def isl_ext_044_buy_silence_range_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Range (max minus min) of the buy zero-run over trailing 252 days."""
    run = _current_zero_run_length(insider_buy_count)
    return _rolling_max(run, _TD_YEAR) - _rolling_min(run, _TD_YEAR)


def isl_ext_045_buy_run_zscore_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of current buy zero-run within trailing 252-day distribution."""
    run = _current_zero_run_length(insider_buy_count)
    return _safe_div(run - _rolling_mean(run, _TD_YEAR), _rolling_std(run, _TD_YEAR))


def isl_ext_046_buy_run_zscore_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of current buy zero-run within trailing 504-day distribution."""
    run = _current_zero_run_length(insider_buy_count)
    return _safe_div(run - _rolling_mean(run, _TD_2Y), _rolling_std(run, _TD_2Y))


def isl_ext_047_buy_run_pct_rank_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of current buy zero-run within trailing 504 days."""
    run = _current_zero_run_length(insider_buy_count)
    return run.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def isl_ext_048_days_since_buy_pct_rank_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Percentile rank of days-since-last-buy within trailing 504 days."""
    dsn = _days_since_last_nonzero(insider_buy_count)
    return dsn.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


# --- Group E (049-060): Activity-count collapse and breadth-of-silence ratios ---

def isl_ext_049_buy_active_days_1mo(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days in last 21 days with at least one insider buy."""
    return _rolling_sum((insider_buy_count > 0).astype(float), _TD_MO)


def isl_ext_050_buy_active_days_2yr(insider_buy_count: pd.Series) -> pd.Series:
    """Count of days in last 504 days with at least one insider buy."""
    return _rolling_sum((insider_buy_count > 0).astype(float), _TD_2Y)


def isl_ext_051_buy_active_days_drop_1qtr_vs_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Buy-active-day fraction over 63 days minus that over 252 days."""
    active = (insider_buy_count > 0).astype(float)
    return _rolling_mean(active, _TD_QTR) - _rolling_mean(active, _TD_YEAR)


def isl_ext_052_buy_count_collapse_ratio_1qtr_vs_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Annualized 63-day buy count divided by 252-day buy count."""
    recent = _rolling_sum(insider_buy_count, _TD_QTR) * 4.0
    hist = _rolling_sum(insider_buy_count, _TD_YEAR)
    return _safe_div(recent, hist)


def isl_ext_053_buyer_breadth_collapse_ratio(insider_buyers: pd.Series) -> pd.Series:
    """Annualized 63-day buyer sum divided by trailing 252-day buyer sum."""
    recent = _rolling_sum(insider_buyers, _TD_QTR) * 4.0
    hist = _rolling_sum(insider_buyers, _TD_YEAR)
    return _safe_div(recent, hist)


def isl_ext_054_buy_value_collapse_ratio(insider_buy_value: pd.Series) -> pd.Series:
    """Annualized 63-day buy value divided by trailing 252-day buy value."""
    recent = _rolling_sum(insider_buy_value, _TD_QTR) * 4.0
    hist = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(recent, hist)


def isl_ext_055_buy_to_total_activity_share_1yr(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Share of buy days among all active days over trailing 252 days."""
    buy_days = _rolling_sum((insider_buy_count > 0).astype(float), _TD_YEAR)
    any_days = _rolling_sum(((insider_buy_count + insider_sell_count).clip(lower=0) > 0).astype(float), _TD_YEAR)
    return _safe_div(buy_days, any_days)


def isl_ext_056_silence_ratio_buy_vs_any(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    """Buy zero-fraction over 252 days divided by any-txn zero-fraction over 252 days."""
    buy_zero = _rolling_mean((insider_buy_count == 0).astype(float), _TD_YEAR)
    any_zero = _rolling_mean(((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float), _TD_YEAR)
    return _safe_div(buy_zero, any_zero)


def isl_ext_057_buyer_silence_minus_buy_silence(insider_buyers: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Distinct-buyer silence days minus buy-transaction silence days."""
    return _days_since_last_nonzero(insider_buyers) - _days_since_last_nonzero(insider_buy_count)


def isl_ext_058_buy_value_silence_minus_buy_silence(insider_buy_value: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    """Buy-value silence days minus buy-count silence days (small-trade proxy)."""
    return _days_since_last_nonzero(insider_buy_value) - _days_since_last_nonzero(insider_buy_count)


def isl_ext_059_active_day_count_zscore_1yr(insider_buy_count: pd.Series) -> pd.Series:
    """Z-score of rolling 63-day buy-active-day count within 252-day window."""
    cnt = _rolling_sum((insider_buy_count > 0).astype(float), _TD_QTR)
    return _safe_div(cnt - _rolling_mean(cnt, _TD_YEAR), _rolling_std(cnt, _TD_YEAR))


def isl_ext_060_buyer_count_drop_1yr(insider_buyers: pd.Series) -> pd.Series:
    """Trailing 63-day mean distinct buyers minus trailing 252-day mean."""
    return _rolling_mean(insider_buyers, _TD_QTR) - _rolling_mean(insider_buyers, _TD_YEAR)


# --- Group F (061-075): Decay-weighted and composite silence signals ---

def isl_ext_061_buy_ewm_silence_span126(insider_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed buy silence indicator with span=126 (half-year decay)."""
    return _ewm_mean((insider_buy_count == 0).astype(float), span=_TD_2Q)


def isl_ext_062_buy_ewm_silence_span5(insider_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed buy silence indicator with span=5 (very fast decay)."""
    return _ewm_mean((insider_buy_count == 0).astype(float), span=_TD_WK)


def isl_ext_063_sell_ewm_silence_span21(insider_sell_count: pd.Series) -> pd.Series:
    """EWM-smoothed sell silence indicator with span=21."""
    return _ewm_mean((insider_sell_count == 0).astype(float), span=_TD_MO)


def isl_ext_064_director_ewm_silence_span63(director_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed director buy silence indicator with span=63."""
    return _ewm_mean((director_buy_count == 0).astype(float), span=_TD_QTR)


def isl_ext_065_ceo_ewm_silence_span63(ceo_buy_value: pd.Series) -> pd.Series:
    """EWM-smoothed CEO buy-value silence indicator with span=63."""
    return _ewm_mean((ceo_buy_value == 0).astype(float), span=_TD_QTR)


def isl_ext_066_tenpct_ewm_silence_span63(tenpct_buy_count: pd.Series) -> pd.Series:
    """EWM-smoothed 10%-holder buy silence indicator with span=63."""
    return _ewm_mean((tenpct_buy_count == 0).astype(float), span=_TD_QTR)


def isl_ext_067_buy_ewm_silence_span252_minus_span21(insider_buy_count: pd.Series) -> pd.Series:
    """Long minus short EWM buy silence: span=252 minus span=21 (silence-trend)."""
    zero = (insider_buy_count == 0).astype(float)
    return _ewm_mean(zero, span=_TD_YEAR) - _ewm_mean(zero, span=_TD_MO)


def isl_ext_068_days_since_buy_ewm_span126(insider_buy_count: pd.Series) -> pd.Series:
    """EWM mean of days-since-last-buy with span=126."""
    return _ewm_mean(_days_since_last_nonzero(insider_buy_count), span=_TD_2Q)


def isl_ext_069_buy_run_ewm_span126(insider_buy_count: pd.Series) -> pd.Series:
    """EWM mean of current buy zero-run with span=126."""
    return _ewm_mean(_current_zero_run_length(insider_buy_count), span=_TD_2Q)


def isl_ext_070_role_silence_breadth_count(officer_buy_count: pd.Series,
                                           director_buy_count: pd.Series,
                                           ceo_buy_value: pd.Series,
                                           cfo_buy_value: pd.Series) -> pd.Series:
    """Count of insider roles (officer/director/CEO/CFO) silent for more than 63 days."""
    flags = [
        (_current_zero_run_length(officer_buy_count) > _TD_QTR).astype(float),
        (_current_zero_run_length(director_buy_count) > _TD_QTR).astype(float),
        (_current_zero_run_length(ceo_buy_value) > _TD_QTR).astype(float),
        (_current_zero_run_length(cfo_buy_value) > _TD_QTR).astype(float),
    ]
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def isl_ext_071_all_roles_silent_1qtr_flag(officer_buy_count: pd.Series,
                                           director_buy_count: pd.Series,
                                           ceo_buy_value: pd.Series,
                                           cfo_buy_value: pd.Series) -> pd.Series:
    """Binary: 1 if officer, director, CEO and CFO buys are ALL silent over 63 days."""
    o = _current_zero_run_length(officer_buy_count) > _TD_QTR
    d = _current_zero_run_length(director_buy_count) > _TD_QTR
    c = _current_zero_run_length(ceo_buy_value) > _TD_QTR
    f = _current_zero_run_length(cfo_buy_value) > _TD_QTR
    return (o & d & c & f).astype(float)


def isl_ext_072_buy_silence_severity_score(insider_buy_count: pd.Series) -> pd.Series:
    """Severity score: average of run/504 (capped 1), 252-day zero-frac, 63-day zero-frac."""
    run_norm = (_current_zero_run_length(insider_buy_count) / _TD_2Y).clip(upper=1.0)
    zero = (insider_buy_count == 0).astype(float)
    return (run_norm + _rolling_mean(zero, _TD_YEAR) + _rolling_mean(zero, _TD_QTR)) / 3.0


def isl_ext_073_buyer_withdrawal_composite(insider_buyers: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    """Composite: average of 252-day buyer zero-frac and 252-day buy-value zero-frac."""
    buyer_zero = _rolling_mean((insider_buyers == 0).astype(float), _TD_YEAR)
    value_zero = _rolling_mean((insider_buy_value == 0).astype(float), _TD_YEAR)
    return (buyer_zero + value_zero) / 2.0


def isl_ext_074_silence_intensity_ewm_composite(insider_buy_count: pd.Series,
                                                insider_sell_count: pd.Series) -> pd.Series:
    """Composite of buy and any-txn EWM silence (span=126), averaged."""
    buy_z = _ewm_mean((insider_buy_count == 0).astype(float), span=_TD_2Q)
    any_z = _ewm_mean(((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float), span=_TD_2Q)
    return (buy_z + any_z) / 2.0


def isl_ext_075_deep_silence_composite(insider_buy_count: pd.Series,
                                       insider_sell_count: pd.Series,
                                       insider_buyers: pd.Series,
                                       officer_buy_count: pd.Series) -> pd.Series:
    """
    Deep silence composite combining four normalized signals (each 0-1):
      - buy zero-run / 504 (capped)
      - any-txn 252-day zero fraction
      - buyer 252-day zero fraction
      - officer buy zero-run / 504 (capped)
    Average of the four; higher = broader, deeper insider withdrawal.
    """
    buy_run = (_current_zero_run_length(insider_buy_count) / _TD_2Y).clip(upper=1.0)
    any_zero = _rolling_mean(((insider_buy_count + insider_sell_count).clip(lower=0) == 0).astype(float), _TD_YEAR)
    buyer_zero = _rolling_mean((insider_buyers == 0).astype(float), _TD_YEAR)
    off_run = (_current_zero_run_length(officer_buy_count) / _TD_2Y).clip(upper=1.0)
    return (buy_run + any_zero + buyer_zero + off_run) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────
INSIDER_SILENCE_EXTENDED_REGISTRY_001_075 = {
    "isl_ext_001_buy_zero_frac_1wk":               {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_001_buy_zero_frac_1wk},
    "isl_ext_002_buy_zero_frac_2mo":               {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_002_buy_zero_frac_2mo},
    "isl_ext_003_buy_zero_frac_2q":                {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_003_buy_zero_frac_2q},
    "isl_ext_004_any_txn_zero_frac_3yr":           {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_004_any_txn_zero_frac_3yr},
    "isl_ext_005_sell_zero_frac_2yr":              {"inputs": ["insider_sell_count"],                                                    "func": isl_ext_005_sell_zero_frac_2yr},
    "isl_ext_006_buyer_zero_frac_1yr":             {"inputs": ["insider_buyers"],                                                        "func": isl_ext_006_buyer_zero_frac_1yr},
    "isl_ext_007_buy_silence_half_years":          {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_007_buy_silence_half_years},
    "isl_ext_008_buy_silence_years":               {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_008_buy_silence_years},
    "isl_ext_009_sell_silence_quarters":           {"inputs": ["insider_sell_count"],                                                    "func": isl_ext_009_sell_silence_quarters},
    "isl_ext_010_buy_zero_run_years":              {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_010_buy_zero_run_years},
    "isl_ext_011_any_txn_zero_run_weeks":          {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_011_any_txn_zero_run_weeks},
    "isl_ext_012_buyer_silence_weeks":             {"inputs": ["insider_buyers"],                                                        "func": isl_ext_012_buyer_silence_weeks},
    "isl_ext_013_buy_silence_gt_2mo_flag":         {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_013_buy_silence_gt_2mo_flag},
    "isl_ext_014_buy_silence_gt_2qtr_flag":        {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_014_buy_silence_gt_2qtr_flag},
    "isl_ext_015_buy_silence_gt_2yr_flag":         {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_015_buy_silence_gt_2yr_flag},
    "isl_ext_016_buy_run_gt_2mo_flag":             {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_016_buy_run_gt_2mo_flag},
    "isl_ext_017_buy_run_gt_2yr_flag":             {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_017_buy_run_gt_2yr_flag},
    "isl_ext_018_sell_run_gt_1qtr_flag":           {"inputs": ["insider_sell_count"],                                                    "func": isl_ext_018_sell_run_gt_1qtr_flag},
    "isl_ext_019_any_txn_run_gt_1yr_flag":         {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_019_any_txn_run_gt_1yr_flag},
    "isl_ext_020_buyer_run_gt_1qtr_flag":          {"inputs": ["insider_buyers"],                                                        "func": isl_ext_020_buyer_run_gt_1qtr_flag},
    "isl_ext_021_buy_value_run_gt_1yr_flag":       {"inputs": ["insider_buy_value"],                                                     "func": isl_ext_021_buy_value_run_gt_1yr_flag},
    "isl_ext_022_officer_buy_run_gt_1qtr_flag":    {"inputs": ["officer_buy_count"],                                                     "func": isl_ext_022_officer_buy_run_gt_1qtr_flag},
    "isl_ext_023_buy_zero_frac_1yr_gt_90pct_flag": {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_023_buy_zero_frac_1yr_gt_90pct_flag},
    "isl_ext_024_no_activity_full_qtr_flag":       {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_024_no_activity_full_qtr_flag},
    "isl_ext_025_director_buy_silence_months":     {"inputs": ["director_buy_count"],                                                    "func": isl_ext_025_director_buy_silence_months},
    "isl_ext_026_director_buy_zero_frac_1qtr":     {"inputs": ["director_buy_count"],                                                    "func": isl_ext_026_director_buy_zero_frac_1qtr},
    "isl_ext_027_director_buy_run_gt_1yr_flag":    {"inputs": ["director_buy_count"],                                                    "func": isl_ext_027_director_buy_run_gt_1yr_flag},
    "isl_ext_028_ceo_buy_silence_quarters":        {"inputs": ["ceo_buy_value"],                                                         "func": isl_ext_028_ceo_buy_silence_quarters},
    "isl_ext_029_ceo_buy_zero_frac_2yr":           {"inputs": ["ceo_buy_value"],                                                         "func": isl_ext_029_ceo_buy_zero_frac_2yr},
    "isl_ext_030_cfo_buy_silence_quarters":        {"inputs": ["cfo_buy_value"],                                                         "func": isl_ext_030_cfo_buy_silence_quarters},
    "isl_ext_031_cfo_buy_zero_frac_2yr":           {"inputs": ["cfo_buy_value"],                                                         "func": isl_ext_031_cfo_buy_zero_frac_2yr},
    "isl_ext_032_tenpct_buy_silence_quarters":     {"inputs": ["tenpct_buy_count"],                                                      "func": isl_ext_032_tenpct_buy_silence_quarters},
    "isl_ext_033_tenpct_buy_zero_frac_2yr":        {"inputs": ["tenpct_buy_count"],                                                      "func": isl_ext_033_tenpct_buy_zero_frac_2yr},
    "isl_ext_034_ceo_cfo_combined_zero_frac_1yr":  {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                        "func": isl_ext_034_ceo_cfo_combined_zero_frac_1yr},
    "isl_ext_035_director_vs_officer_silence_gap": {"inputs": ["director_buy_count", "officer_buy_count"],                               "func": isl_ext_035_director_vs_officer_silence_gap},
    "isl_ext_036_topbrass_silence_min":            {"inputs": ["ceo_buy_value", "cfo_buy_value"],                                        "func": isl_ext_036_topbrass_silence_min},
    "isl_ext_037_longest_buy_silence_3yr":         {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_037_longest_buy_silence_3yr},
    "isl_ext_038_longest_any_txn_silence_2yr":     {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_038_longest_any_txn_silence_2yr},
    "isl_ext_039_buy_run_pct_of_2yr_longest":      {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_039_buy_run_pct_of_2yr_longest},
    "isl_ext_040_buy_run_minus_1yr_max":           {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_040_buy_run_minus_1yr_max},
    "isl_ext_041_buy_silence_dispersion_1yr":      {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_041_buy_silence_dispersion_1yr},
    "isl_ext_042_buy_silence_cv_1yr":              {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_042_buy_silence_cv_1yr},
    "isl_ext_043_days_since_buy_vs_1yr_median":    {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_043_days_since_buy_vs_1yr_median},
    "isl_ext_044_buy_silence_range_1yr":           {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_044_buy_silence_range_1yr},
    "isl_ext_045_buy_run_zscore_1yr":              {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_045_buy_run_zscore_1yr},
    "isl_ext_046_buy_run_zscore_2yr":              {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_046_buy_run_zscore_2yr},
    "isl_ext_047_buy_run_pct_rank_2yr":            {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_047_buy_run_pct_rank_2yr},
    "isl_ext_048_days_since_buy_pct_rank_2yr":     {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_048_days_since_buy_pct_rank_2yr},
    "isl_ext_049_buy_active_days_1mo":             {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_049_buy_active_days_1mo},
    "isl_ext_050_buy_active_days_2yr":             {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_050_buy_active_days_2yr},
    "isl_ext_051_buy_active_days_drop_1qtr_vs_1yr":{"inputs": ["insider_buy_count"],                                                     "func": isl_ext_051_buy_active_days_drop_1qtr_vs_1yr},
    "isl_ext_052_buy_count_collapse_ratio_1qtr_vs_1yr":{"inputs": ["insider_buy_count"],                                                 "func": isl_ext_052_buy_count_collapse_ratio_1qtr_vs_1yr},
    "isl_ext_053_buyer_breadth_collapse_ratio":    {"inputs": ["insider_buyers"],                                                        "func": isl_ext_053_buyer_breadth_collapse_ratio},
    "isl_ext_054_buy_value_collapse_ratio":        {"inputs": ["insider_buy_value"],                                                     "func": isl_ext_054_buy_value_collapse_ratio},
    "isl_ext_055_buy_to_total_activity_share_1yr": {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_055_buy_to_total_activity_share_1yr},
    "isl_ext_056_silence_ratio_buy_vs_any":        {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_056_silence_ratio_buy_vs_any},
    "isl_ext_057_buyer_silence_minus_buy_silence": {"inputs": ["insider_buyers", "insider_buy_count"],                                   "func": isl_ext_057_buyer_silence_minus_buy_silence},
    "isl_ext_058_buy_value_silence_minus_buy_silence":{"inputs": ["insider_buy_value", "insider_buy_count"],                             "func": isl_ext_058_buy_value_silence_minus_buy_silence},
    "isl_ext_059_active_day_count_zscore_1yr":     {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_059_active_day_count_zscore_1yr},
    "isl_ext_060_buyer_count_drop_1yr":            {"inputs": ["insider_buyers"],                                                        "func": isl_ext_060_buyer_count_drop_1yr},
    "isl_ext_061_buy_ewm_silence_span126":         {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_061_buy_ewm_silence_span126},
    "isl_ext_062_buy_ewm_silence_span5":           {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_062_buy_ewm_silence_span5},
    "isl_ext_063_sell_ewm_silence_span21":         {"inputs": ["insider_sell_count"],                                                    "func": isl_ext_063_sell_ewm_silence_span21},
    "isl_ext_064_director_ewm_silence_span63":     {"inputs": ["director_buy_count"],                                                    "func": isl_ext_064_director_ewm_silence_span63},
    "isl_ext_065_ceo_ewm_silence_span63":          {"inputs": ["ceo_buy_value"],                                                         "func": isl_ext_065_ceo_ewm_silence_span63},
    "isl_ext_066_tenpct_ewm_silence_span63":       {"inputs": ["tenpct_buy_count"],                                                      "func": isl_ext_066_tenpct_ewm_silence_span63},
    "isl_ext_067_buy_ewm_silence_span252_minus_span21":{"inputs": ["insider_buy_count"],                                                 "func": isl_ext_067_buy_ewm_silence_span252_minus_span21},
    "isl_ext_068_days_since_buy_ewm_span126":      {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_068_days_since_buy_ewm_span126},
    "isl_ext_069_buy_run_ewm_span126":             {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_069_buy_run_ewm_span126},
    "isl_ext_070_role_silence_breadth_count":      {"inputs": ["officer_buy_count", "director_buy_count", "ceo_buy_value", "cfo_buy_value"],"func": isl_ext_070_role_silence_breadth_count},
    "isl_ext_071_all_roles_silent_1qtr_flag":      {"inputs": ["officer_buy_count", "director_buy_count", "ceo_buy_value", "cfo_buy_value"],"func": isl_ext_071_all_roles_silent_1qtr_flag},
    "isl_ext_072_buy_silence_severity_score":      {"inputs": ["insider_buy_count"],                                                     "func": isl_ext_072_buy_silence_severity_score},
    "isl_ext_073_buyer_withdrawal_composite":      {"inputs": ["insider_buyers", "insider_buy_value"],                                   "func": isl_ext_073_buyer_withdrawal_composite},
    "isl_ext_074_silence_intensity_ewm_composite": {"inputs": ["insider_buy_count", "insider_sell_count"],                               "func": isl_ext_074_silence_intensity_ewm_composite},
    "isl_ext_075_deep_silence_composite":          {"inputs": ["insider_buy_count", "insider_sell_count", "insider_buyers", "officer_buy_count"],"func": isl_ext_075_deep_silence_composite},
}
