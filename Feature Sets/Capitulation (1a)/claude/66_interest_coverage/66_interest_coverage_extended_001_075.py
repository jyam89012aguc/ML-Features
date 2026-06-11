"""
66_interest_coverage — Extended Features 001-075
Domain: interest-coverage / debt-servicing deterioration — additional variants:
        net-debt coverage, cash-vs-interest buffers, longer windows, slopes,
        range positions, accel signals, multi-metric confluences, severity ranks
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    flag = cond.fillna(False).astype(int)
    arr = flag.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=cond.index)


def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over a trailing window of width w."""
    def _slope(arr):
        n = len(arr)
        if n < 2:
            return np.nan
        x  = np.arange(n, dtype=float)
        xm = x.mean()
        ym = np.nanmean(arr)
        denom = ((x - xm) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((x - xm) * (arr - ym)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=True)


def _range_position(s: pd.Series, w: int) -> pd.Series:
    """Position of s within trailing [min,max] range; 0=window low."""
    lo = _rolling_min(s, w)
    hi = _rolling_max(s, w)
    return _safe_div(s - lo, hi - lo)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): EBIT coverage — additional windows and angles ---

def icv_ext_001_ebit_coverage_3y_avg(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 12-quarter (756-day) mean EBIT coverage ratio."""
    return _rolling_mean(_safe_div(ebit, intexp), _TD_3Y)


def icv_ext_002_ebit_coverage_5y_avg(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 20-quarter (1260-day) mean EBIT coverage ratio."""
    return _rolling_mean(_safe_div(ebit, intexp), _TD_5Y)


def icv_ext_003_ebit_coverage_drawdown_12q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBIT coverage drawdown from its 12-quarter rolling peak."""
    cov = _safe_div(ebit, intexp)
    return cov - _rolling_max(cov, _TD_3Y)


def icv_ext_004_ebit_coverage_range_position_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Position of EBIT coverage within its trailing 8-quarter [min,max] range."""
    return _range_position(_safe_div(ebit, intexp), _TD_2Y)


def icv_ext_005_ebit_coverage_range_position_12q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Position of EBIT coverage within its trailing 12-quarter [min,max] range."""
    return _range_position(_safe_div(ebit, intexp), _TD_3Y)


def icv_ext_006_ebit_coverage_5y_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """5-year change in EBIT coverage ratio (1260-day lag)."""
    cov = _safe_div(ebit, intexp)
    return cov - cov.shift(_TD_5Y)


def icv_ext_007_ebit_coverage_below_3_flag(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBIT coverage < 3.0 (sub-investment-grade buffer)."""
    return (_safe_div(ebit, intexp) < 3.0).astype(float)


def icv_ext_008_ebit_coverage_below_half_flag(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBIT coverage < 0.5 (deep distress — EBIT covers <half of interest)."""
    return (_safe_div(ebit, intexp) < 0.5).astype(float)


def icv_ext_009_ebit_coverage_2q_slope(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """OLS slope of EBIT coverage over trailing 2-quarter (126-day) window."""
    return _rolling_slope(_safe_div(ebit, intexp), _TD_2Q)


def icv_ext_010_ebit_coverage_8q_slope(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """OLS slope of EBIT coverage over trailing 8-quarter (504-day) window."""
    return _rolling_slope(_safe_div(ebit, intexp), _TD_2Y)


def icv_ext_011_ebit_coverage_below_1_streak(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of EBIT coverage below 1.0."""
    return _consec_streak(_safe_div(ebit, intexp) < 1.0)


def icv_ext_012_ebit_coverage_below_2_streak(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of EBIT coverage below 2.0."""
    return _consec_streak(_safe_div(ebit, intexp) < 2.0)


# --- Group B (013-024): EBITDA coverage — additional variants ---

def icv_ext_013_ebitda_coverage_3y_avg(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 12-quarter mean EBITDA coverage ratio."""
    return _rolling_mean(_safe_div(ebitda, intexp), _TD_3Y)


def icv_ext_014_ebitda_coverage_drawdown_12q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage drawdown from its 12-quarter rolling peak."""
    cov = _safe_div(ebitda, intexp)
    return cov - _rolling_max(cov, _TD_3Y)


def icv_ext_015_ebitda_coverage_range_position_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Position of EBITDA coverage within trailing 8-quarter [min,max] range."""
    return _range_position(_safe_div(ebitda, intexp), _TD_2Y)


def icv_ext_016_ebitda_coverage_3y_change(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """3-year change in EBITDA coverage ratio."""
    cov = _safe_div(ebitda, intexp)
    return cov - cov.shift(_TD_3Y)


def icv_ext_017_ebitda_coverage_below_3_flag(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBITDA coverage < 3.0."""
    return (_safe_div(ebitda, intexp) < 3.0).astype(float)


def icv_ext_018_ebitda_coverage_below_zero_flag(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if EBITDA coverage < 0 (negative EBITDA)."""
    return (_safe_div(ebitda, intexp) < 0.0).astype(float)


def icv_ext_019_ebitda_coverage_below_1_streak(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of EBITDA coverage below 1.0."""
    return _consec_streak(_safe_div(ebitda, intexp) < 1.0)


def icv_ext_020_ebitda_coverage_below_2_count_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of days in trailing 8 quarters with EBITDA coverage < 2.0."""
    flag = (_safe_div(ebitda, intexp) < 2.0).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def icv_ext_021_ebitda_coverage_8q_slope(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """OLS slope of EBITDA coverage over trailing 8-quarter window."""
    return _rolling_slope(_safe_div(ebitda, intexp), _TD_2Y)


def icv_ext_022_ebitda_coverage_ewm_dev_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA coverage minus its 8-quarter EWM (span=504)."""
    cov = _safe_div(ebitda, intexp)
    return cov - _ewm_mean(cov, _TD_2Y)


def icv_ext_023_ebitda_coverage_qoq_decel(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Acceleration: QoQ change in EBITDA coverage minus the prior-quarter QoQ change."""
    cov = _safe_div(ebitda, intexp)
    dq = cov - cov.shift(_TD_QTR)
    return dq - dq.shift(_TD_QTR)


def icv_ext_024_ebitda_coverage_expanding_pct_rank(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of EBITDA coverage."""
    cov = _safe_div(ebitda, intexp)
    return cov.expanding(min_periods=2).rank(pct=True)


# --- Group C (025-036): Net-debt coverage and cash buffers ---

def icv_ext_025_netdebt_to_ebitda(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net debt (debt - cash) divided by EBITDA — leverage burden vs earnings power."""
    netdebt = debt - cashnequiv
    return _safe_div(netdebt, ebitda.abs().replace(0, np.nan))


def icv_ext_026_netdebt_to_ebitda_yoy_change(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """YoY change in net-debt-to-EBITDA leverage ratio."""
    ratio = _safe_div(debt - cashnequiv, ebitda.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def icv_ext_027_netdebt_to_ebitda_zscore_4q(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of net-debt-to-EBITDA within trailing 4-quarter window."""
    ratio = _safe_div(debt - cashnequiv, ebitda.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_YEAR)


def icv_ext_028_debt_to_ebitda(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Gross debt divided by EBITDA (leverage multiple)."""
    return _safe_div(debt, ebitda.abs().replace(0, np.nan))


def icv_ext_029_debt_to_ebitda_above_6_flag(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Binary: 1 if gross debt-to-EBITDA exceeds 6.0 (highly levered)."""
    return (_safe_div(debt, ebitda.abs().replace(0, np.nan)) > 6.0).astype(float)


def icv_ext_030_cash_to_intexp(cashnequiv: pd.Series, intexp: pd.Series) -> pd.Series:
    """Cash & equivalents divided by interest expense (years of interest cash buffers)."""
    return _safe_div(cashnequiv, intexp)


def icv_ext_031_cash_to_intexp_below_1_flag(cashnequiv: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if cash covers less than one period of interest expense."""
    return (_safe_div(cashnequiv, intexp) < 1.0).astype(float)


def icv_ext_032_cash_to_intexp_yoy_change(cashnequiv: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in cash-to-interest-expense buffer ratio."""
    ratio = _safe_div(cashnequiv, intexp)
    return ratio - ratio.shift(_TD_YEAR)


def icv_ext_033_ebitda_plus_cash_coverage(ebitda: pd.Series, cashnequiv: pd.Series, intexp: pd.Series) -> pd.Series:
    """(EBITDA + cash) divided by interest expense — earnings-plus-liquidity coverage."""
    return _safe_div(ebitda + cashnequiv, intexp)


def icv_ext_034_netdebt_coverage_gap(ebitda: pd.Series, debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """EBITDA minus net debt — absolute earnings surplus over net leverage."""
    return ebitda - (debt - cashnequiv)


def icv_ext_035_debt_to_ebitda_drawup_4q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Debt-to-EBITDA minus its 4-quarter rolling minimum (leverage rise from trough)."""
    ratio = _safe_div(debt, ebitda.abs().replace(0, np.nan))
    return ratio - _rolling_min(ratio, _TD_YEAR)


def icv_ext_036_netdebt_to_ebitda_pct_rank_8q(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Percentile rank of net-debt-to-EBITDA within trailing 8-quarter window."""
    ratio = _safe_div(debt - cashnequiv, ebitda.abs().replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_2Y)


# --- Group D (037-048): NCFO / opinc coverage — additional variants ---

def icv_ext_037_ncfo_coverage_3y_avg(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Trailing 12-quarter mean ncfo coverage ratio."""
    return _rolling_mean(_safe_div(ncfo, intexp), _TD_3Y)


def icv_ext_038_ncfo_coverage_drawdown_12q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """ncfo coverage drawdown from its 12-quarter rolling peak."""
    cov = _safe_div(ncfo, intexp)
    return cov - _rolling_max(cov, _TD_3Y)


def icv_ext_039_ncfo_coverage_range_position_8q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Position of ncfo coverage within trailing 8-quarter [min,max] range."""
    return _range_position(_safe_div(ncfo, intexp), _TD_2Y)


def icv_ext_040_ncfo_coverage_below_2_flag(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if ncfo coverage < 2.0 (thin cash-flow buffer)."""
    return (_safe_div(ncfo, intexp) < 2.0).astype(float)


def icv_ext_041_ncfo_coverage_below_2_streak(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of ncfo coverage below 2.0."""
    return _consec_streak(_safe_div(ncfo, intexp) < 2.0)


def icv_ext_042_ncfo_coverage_8q_slope(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """OLS slope of ncfo coverage over trailing 8-quarter window."""
    return _rolling_slope(_safe_div(ncfo, intexp), _TD_2Y)


def icv_ext_043_ncfo_coverage_zscore_8q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of ncfo coverage within trailing 8-quarter window."""
    return _zscore_rolling(_safe_div(ncfo, intexp), _TD_2Y)


def icv_ext_044_ncfo_coverage_ewm_dev(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """ncfo coverage minus its 4-quarter EWM (span=252)."""
    cov = _safe_div(ncfo, intexp)
    return cov - _ewm_mean(cov, _TD_YEAR)


def icv_ext_045_opinc_coverage_3y_change(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """3-year change in operating-income coverage ratio."""
    cov = _safe_div(opinc, intexp)
    return cov - cov.shift(_TD_3Y)


def icv_ext_046_opinc_coverage_below_2_flag(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if opinc coverage < 2.0."""
    return (_safe_div(opinc, intexp) < 2.0).astype(float)


def icv_ext_047_opinc_coverage_below_1_streak(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of opinc coverage below 1.0."""
    return _consec_streak(_safe_div(opinc, intexp) < 1.0)


def icv_ext_048_opinc_coverage_range_position_8q(opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Position of opinc coverage within trailing 8-quarter [min,max] range."""
    return _range_position(_safe_div(opinc, intexp), _TD_2Y)


# --- Group E (049-058): Interest-expense burden — additional angles ---

def icv_ext_049_intexp_3y_change(intexp: pd.Series) -> pd.Series:
    """3-year absolute change in interest expense."""
    return intexp - intexp.shift(_TD_3Y)


def icv_ext_050_intexp_drawup_from_4q_min(intexp: pd.Series) -> pd.Series:
    """Interest expense minus its trailing 4-quarter rolling minimum."""
    return intexp - _rolling_min(intexp, _TD_YEAR)


def icv_ext_051_intexp_range_position_8q(intexp: pd.Series) -> pd.Series:
    """Position of interest expense within trailing 8-quarter [min,max] range."""
    return _range_position(intexp, _TD_2Y)


def icv_ext_052_intexp_zscore_8q(intexp: pd.Series) -> pd.Series:
    """Z-score of interest expense within trailing 8-quarter window."""
    return _zscore_rolling(intexp, _TD_2Y)


def icv_ext_053_intexp_pct_rank_8q(intexp: pd.Series) -> pd.Series:
    """Percentile rank of interest expense within trailing 8-quarter window."""
    return _rolling_rank_pct(intexp, _TD_2Y)


def icv_ext_054_intexp_rising_streak(intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of interest expense rising QoQ."""
    return _consec_streak(intexp > intexp.shift(_TD_QTR))


def icv_ext_055_intexp_8q_slope(intexp: pd.Series) -> pd.Series:
    """OLS slope of interest expense over trailing 8-quarter window."""
    return _rolling_slope(intexp, _TD_2Y)


def icv_ext_056_intexp_as_pct_assets(intexp: pd.Series, assets: pd.Series) -> pd.Series:
    """Interest expense as a fraction of total assets — interest drag on the asset base."""
    return _safe_div(intexp, assets.abs().replace(0, np.nan))


def icv_ext_057_intexp_as_pct_ebit_above_1_flag(intexp: pd.Series, ebit: pd.Series) -> pd.Series:
    """Binary: 1 if interest expense exceeds EBIT (intexp/|ebit| > 1)."""
    return (_safe_div(intexp, ebit.abs().replace(0, np.nan)) > 1.0).astype(float)


def icv_ext_058_effective_rate_drawup_from_4q_min(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Effective interest rate minus its trailing 4-quarter rolling minimum."""
    rate = _safe_div(intexp, debt.abs().replace(0, np.nan))
    return rate - _rolling_min(rate, _TD_YEAR)


# --- Group F (059-068): TTM coverage and longer-horizon ranks ---

def icv_ext_059_ebit_ttm_coverage_zscore_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of TTM EBIT coverage within trailing 8-quarter window."""
    cov = _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return _zscore_rolling(cov, _TD_2Y)


def icv_ext_060_ebitda_ttm_coverage_pct_rank_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of TTM EBITDA coverage within trailing 8-quarter window."""
    cov = _safe_div(_rolling_sum(ebitda, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return _rolling_rank_pct(cov, _TD_2Y)


def icv_ext_061_ncfo_ttm_coverage_below_1_flag(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if TTM ncfo coverage < 1.0."""
    cov = _safe_div(_rolling_sum(ncfo, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return (cov < 1.0).astype(float)


def icv_ext_062_ebit_ttm_coverage_yoy_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY change in TTM EBIT coverage ratio."""
    cov = _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return cov - cov.shift(_TD_YEAR)


def icv_ext_063_ebit_ttm_coverage_drawdown_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """TTM EBIT coverage drawdown from its 8-quarter rolling peak."""
    cov = _safe_div(_rolling_sum(ebit, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return cov - _rolling_max(cov, _TD_2Y)


def icv_ext_064_ebit_coverage_pct_rank_5y(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of EBIT coverage within trailing 20-quarter (1260-day) window."""
    return _rolling_rank_pct(_safe_div(ebit, intexp), _TD_5Y)


def icv_ext_065_ebitda_coverage_zscore_5y(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of EBITDA coverage within trailing 20-quarter (1260-day) window."""
    return _zscore_rolling(_safe_div(ebitda, intexp), _TD_5Y)


def icv_ext_066_ebit_coverage_expanding_max_drawdown(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percent drawdown of EBIT coverage from its all-history expanding peak."""
    cov = _safe_div(ebit, intexp)
    peak = cov.expanding(min_periods=1).max()
    return _safe_div_abs(cov - peak, peak)


def icv_ext_067_ncfo_coverage_pct_rank_12q(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of ncfo coverage within trailing 12-quarter window."""
    return _rolling_rank_pct(_safe_div(ncfo, intexp), _TD_3Y)


def icv_ext_068_ebitda_ttm_coverage_below_2_streak(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive-day streak of TTM EBITDA coverage below 2.0."""
    cov = _safe_div(_rolling_sum(ebitda, _TD_YEAR), _rolling_sum(intexp, _TD_YEAR))
    return _consec_streak(cov < 2.0)


# --- Group G (069-075): Multi-metric confluence and severity composites ---

def icv_ext_069_all_three_below_1_flag(ebit: pd.Series, ebitda: pd.Series,
                                       ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 when EBIT, EBITDA, AND ncfo coverages are ALL simultaneously < 1.0."""
    c_e = _safe_div(ebit, intexp)
    c_d = _safe_div(ebitda, intexp)
    c_n = _safe_div(ncfo, intexp)
    return ((c_e < 1.0) & (c_d < 1.0) & (c_n < 1.0)).astype(float)


def icv_ext_070_coverage_below_1_count(ebit: pd.Series, ebitda: pd.Series,
                                       ncfo: pd.Series, opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of coverage metrics (EBIT, EBITDA, ncfo, opinc) simultaneously below 1.0."""
    flags = [
        (_safe_div(ebit, intexp) < 1.0).astype(float),
        (_safe_div(ebitda, intexp) < 1.0).astype(float),
        (_safe_div(ncfo, intexp) < 1.0).astype(float),
        (_safe_div(opinc, intexp) < 1.0).astype(float),
    ]
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def icv_ext_071_coverage_below_2_count(ebit: pd.Series, ebitda: pd.Series,
                                       ncfo: pd.Series, opinc: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of coverage metrics (EBIT, EBITDA, ncfo, opinc) simultaneously below 2.0."""
    flags = [
        (_safe_div(ebit, intexp) < 2.0).astype(float),
        (_safe_div(ebitda, intexp) < 2.0).astype(float),
        (_safe_div(ncfo, intexp) < 2.0).astype(float),
        (_safe_div(opinc, intexp) < 2.0).astype(float),
    ]
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def icv_ext_072_coverage_zscore_min_4q(ebit: pd.Series, ebitda: pd.Series,
                                       ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Minimum (worst) of the 4-quarter z-scores of EBIT, EBITDA and ncfo coverage."""
    z_e = _zscore_rolling(_safe_div(ebit, intexp), _TD_YEAR)
    z_d = _zscore_rolling(_safe_div(ebitda, intexp), _TD_YEAR)
    z_n = _zscore_rolling(_safe_div(ncfo, intexp), _TD_YEAR)
    return pd.concat([z_e, z_d, z_n], axis=1).min(axis=1)


def icv_ext_073_coverage_composite_12q(ebit: pd.Series, ebitda: pd.Series,
                                       ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Composite coverage severity: equally weighted 12-quarter z-scores of EBIT,
    EBITDA and ncfo coverage ratios. Lower = more distressed."""
    z_e = _zscore_rolling(_safe_div(ebit, intexp), _TD_3Y)
    z_d = _zscore_rolling(_safe_div(ebitda, intexp), _TD_3Y)
    z_n = _zscore_rolling(_safe_div(ncfo, intexp), _TD_3Y)
    return (z_e + z_d + z_n) / 3.0


def icv_ext_074_coverage_deterioration_composite_qoq(ebit: pd.Series, ebitda: pd.Series,
                                                     ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """Composite QoQ deterioration: equally weighted mean of QoQ changes in
    EBIT, EBITDA and ncfo coverage ratios. More negative = broader deterioration."""
    c_e = _safe_div(ebit, intexp)
    c_d = _safe_div(ebitda, intexp)
    c_n = _safe_div(ncfo, intexp)
    d_e = c_e - c_e.shift(_TD_QTR)
    d_d = c_d - c_d.shift(_TD_QTR)
    d_n = c_n - c_n.shift(_TD_QTR)
    return (d_e + d_d + d_n) / 3.0


def icv_ext_075_distress_severity_composite(ebit: pd.Series, ebitda: pd.Series, ncfo: pd.Series,
                                            intexp: pd.Series, debt: pd.Series,
                                            cashnequiv: pd.Series) -> pd.Series:
    """Capitulation distress composite: averages normalized signals — EBIT-coverage
    distance below 1, fraction of coverage metrics under 1, net-debt-to-EBITDA
    rank, and inverse cash-to-interest buffer. Higher = more extreme distress."""
    cov_e = _safe_div(ebit, intexp)
    depth = (1.0 - cov_e).clip(lower=0.0).clip(upper=5.0) / 5.0
    flags = ((cov_e < 1.0).astype(float)
             + (_safe_div(ebitda, intexp) < 1.0).astype(float)
             + (_safe_div(ncfo, intexp) < 1.0).astype(float)) / 3.0
    nd_ratio = _safe_div(debt - cashnequiv, ebitda.abs().replace(0, np.nan))
    nd_rank = _rolling_rank_pct(nd_ratio, _TD_2Y).fillna(0.5)
    cash_buf = _safe_div(cashnequiv, intexp)
    cash_pen = (1.0 - cash_buf.clip(lower=0.0, upper=1.0))
    return (depth + flags + nd_rank + cash_pen) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

INTEREST_COVERAGE_EXTENDED_REGISTRY_001_075 = {
    "icv_ext_001_ebit_coverage_3y_avg":              {"inputs": ["ebit", "intexp"],                                "func": icv_ext_001_ebit_coverage_3y_avg},
    "icv_ext_002_ebit_coverage_5y_avg":              {"inputs": ["ebit", "intexp"],                                "func": icv_ext_002_ebit_coverage_5y_avg},
    "icv_ext_003_ebit_coverage_drawdown_12q":        {"inputs": ["ebit", "intexp"],                                "func": icv_ext_003_ebit_coverage_drawdown_12q},
    "icv_ext_004_ebit_coverage_range_position_8q":   {"inputs": ["ebit", "intexp"],                                "func": icv_ext_004_ebit_coverage_range_position_8q},
    "icv_ext_005_ebit_coverage_range_position_12q":  {"inputs": ["ebit", "intexp"],                                "func": icv_ext_005_ebit_coverage_range_position_12q},
    "icv_ext_006_ebit_coverage_5y_change":           {"inputs": ["ebit", "intexp"],                                "func": icv_ext_006_ebit_coverage_5y_change},
    "icv_ext_007_ebit_coverage_below_3_flag":        {"inputs": ["ebit", "intexp"],                                "func": icv_ext_007_ebit_coverage_below_3_flag},
    "icv_ext_008_ebit_coverage_below_half_flag":     {"inputs": ["ebit", "intexp"],                                "func": icv_ext_008_ebit_coverage_below_half_flag},
    "icv_ext_009_ebit_coverage_2q_slope":            {"inputs": ["ebit", "intexp"],                                "func": icv_ext_009_ebit_coverage_2q_slope},
    "icv_ext_010_ebit_coverage_8q_slope":            {"inputs": ["ebit", "intexp"],                                "func": icv_ext_010_ebit_coverage_8q_slope},
    "icv_ext_011_ebit_coverage_below_1_streak":      {"inputs": ["ebit", "intexp"],                                "func": icv_ext_011_ebit_coverage_below_1_streak},
    "icv_ext_012_ebit_coverage_below_2_streak":      {"inputs": ["ebit", "intexp"],                                "func": icv_ext_012_ebit_coverage_below_2_streak},
    "icv_ext_013_ebitda_coverage_3y_avg":            {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_013_ebitda_coverage_3y_avg},
    "icv_ext_014_ebitda_coverage_drawdown_12q":      {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_014_ebitda_coverage_drawdown_12q},
    "icv_ext_015_ebitda_coverage_range_position_8q": {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_015_ebitda_coverage_range_position_8q},
    "icv_ext_016_ebitda_coverage_3y_change":         {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_016_ebitda_coverage_3y_change},
    "icv_ext_017_ebitda_coverage_below_3_flag":      {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_017_ebitda_coverage_below_3_flag},
    "icv_ext_018_ebitda_coverage_below_zero_flag":   {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_018_ebitda_coverage_below_zero_flag},
    "icv_ext_019_ebitda_coverage_below_1_streak":    {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_019_ebitda_coverage_below_1_streak},
    "icv_ext_020_ebitda_coverage_below_2_count_8q":  {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_020_ebitda_coverage_below_2_count_8q},
    "icv_ext_021_ebitda_coverage_8q_slope":          {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_021_ebitda_coverage_8q_slope},
    "icv_ext_022_ebitda_coverage_ewm_dev_8q":        {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_022_ebitda_coverage_ewm_dev_8q},
    "icv_ext_023_ebitda_coverage_qoq_decel":         {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_023_ebitda_coverage_qoq_decel},
    "icv_ext_024_ebitda_coverage_expanding_pct_rank": {"inputs": ["ebitda", "intexp"],                             "func": icv_ext_024_ebitda_coverage_expanding_pct_rank},
    "icv_ext_025_netdebt_to_ebitda":                 {"inputs": ["debt", "cashnequiv", "ebitda"],                  "func": icv_ext_025_netdebt_to_ebitda},
    "icv_ext_026_netdebt_to_ebitda_yoy_change":      {"inputs": ["debt", "cashnequiv", "ebitda"],                  "func": icv_ext_026_netdebt_to_ebitda_yoy_change},
    "icv_ext_027_netdebt_to_ebitda_zscore_4q":       {"inputs": ["debt", "cashnequiv", "ebitda"],                  "func": icv_ext_027_netdebt_to_ebitda_zscore_4q},
    "icv_ext_028_debt_to_ebitda":                    {"inputs": ["debt", "ebitda"],                                "func": icv_ext_028_debt_to_ebitda},
    "icv_ext_029_debt_to_ebitda_above_6_flag":       {"inputs": ["debt", "ebitda"],                                "func": icv_ext_029_debt_to_ebitda_above_6_flag},
    "icv_ext_030_cash_to_intexp":                    {"inputs": ["cashnequiv", "intexp"],                          "func": icv_ext_030_cash_to_intexp},
    "icv_ext_031_cash_to_intexp_below_1_flag":       {"inputs": ["cashnequiv", "intexp"],                          "func": icv_ext_031_cash_to_intexp_below_1_flag},
    "icv_ext_032_cash_to_intexp_yoy_change":         {"inputs": ["cashnequiv", "intexp"],                          "func": icv_ext_032_cash_to_intexp_yoy_change},
    "icv_ext_033_ebitda_plus_cash_coverage":         {"inputs": ["ebitda", "cashnequiv", "intexp"],                "func": icv_ext_033_ebitda_plus_cash_coverage},
    "icv_ext_034_netdebt_coverage_gap":              {"inputs": ["ebitda", "debt", "cashnequiv"],                  "func": icv_ext_034_netdebt_coverage_gap},
    "icv_ext_035_debt_to_ebitda_drawup_4q":          {"inputs": ["debt", "ebitda"],                                "func": icv_ext_035_debt_to_ebitda_drawup_4q},
    "icv_ext_036_netdebt_to_ebitda_pct_rank_8q":     {"inputs": ["debt", "cashnequiv", "ebitda"],                  "func": icv_ext_036_netdebt_to_ebitda_pct_rank_8q},
    "icv_ext_037_ncfo_coverage_3y_avg":              {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_037_ncfo_coverage_3y_avg},
    "icv_ext_038_ncfo_coverage_drawdown_12q":        {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_038_ncfo_coverage_drawdown_12q},
    "icv_ext_039_ncfo_coverage_range_position_8q":   {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_039_ncfo_coverage_range_position_8q},
    "icv_ext_040_ncfo_coverage_below_2_flag":        {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_040_ncfo_coverage_below_2_flag},
    "icv_ext_041_ncfo_coverage_below_2_streak":      {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_041_ncfo_coverage_below_2_streak},
    "icv_ext_042_ncfo_coverage_8q_slope":            {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_042_ncfo_coverage_8q_slope},
    "icv_ext_043_ncfo_coverage_zscore_8q":           {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_043_ncfo_coverage_zscore_8q},
    "icv_ext_044_ncfo_coverage_ewm_dev":             {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_044_ncfo_coverage_ewm_dev},
    "icv_ext_045_opinc_coverage_3y_change":          {"inputs": ["opinc", "intexp"],                               "func": icv_ext_045_opinc_coverage_3y_change},
    "icv_ext_046_opinc_coverage_below_2_flag":       {"inputs": ["opinc", "intexp"],                               "func": icv_ext_046_opinc_coverage_below_2_flag},
    "icv_ext_047_opinc_coverage_below_1_streak":     {"inputs": ["opinc", "intexp"],                               "func": icv_ext_047_opinc_coverage_below_1_streak},
    "icv_ext_048_opinc_coverage_range_position_8q":  {"inputs": ["opinc", "intexp"],                               "func": icv_ext_048_opinc_coverage_range_position_8q},
    "icv_ext_049_intexp_3y_change":                  {"inputs": ["intexp"],                                        "func": icv_ext_049_intexp_3y_change},
    "icv_ext_050_intexp_drawup_from_4q_min":         {"inputs": ["intexp"],                                        "func": icv_ext_050_intexp_drawup_from_4q_min},
    "icv_ext_051_intexp_range_position_8q":          {"inputs": ["intexp"],                                        "func": icv_ext_051_intexp_range_position_8q},
    "icv_ext_052_intexp_zscore_8q":                  {"inputs": ["intexp"],                                        "func": icv_ext_052_intexp_zscore_8q},
    "icv_ext_053_intexp_pct_rank_8q":                {"inputs": ["intexp"],                                        "func": icv_ext_053_intexp_pct_rank_8q},
    "icv_ext_054_intexp_rising_streak":              {"inputs": ["intexp"],                                        "func": icv_ext_054_intexp_rising_streak},
    "icv_ext_055_intexp_8q_slope":                   {"inputs": ["intexp"],                                        "func": icv_ext_055_intexp_8q_slope},
    "icv_ext_056_intexp_as_pct_assets":              {"inputs": ["intexp", "assets"],                              "func": icv_ext_056_intexp_as_pct_assets},
    "icv_ext_057_intexp_as_pct_ebit_above_1_flag":   {"inputs": ["intexp", "ebit"],                                "func": icv_ext_057_intexp_as_pct_ebit_above_1_flag},
    "icv_ext_058_effective_rate_drawup_from_4q_min": {"inputs": ["intexp", "debt"],                                "func": icv_ext_058_effective_rate_drawup_from_4q_min},
    "icv_ext_059_ebit_ttm_coverage_zscore_8q":       {"inputs": ["ebit", "intexp"],                                "func": icv_ext_059_ebit_ttm_coverage_zscore_8q},
    "icv_ext_060_ebitda_ttm_coverage_pct_rank_8q":   {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_060_ebitda_ttm_coverage_pct_rank_8q},
    "icv_ext_061_ncfo_ttm_coverage_below_1_flag":    {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_061_ncfo_ttm_coverage_below_1_flag},
    "icv_ext_062_ebit_ttm_coverage_yoy_change":      {"inputs": ["ebit", "intexp"],                                "func": icv_ext_062_ebit_ttm_coverage_yoy_change},
    "icv_ext_063_ebit_ttm_coverage_drawdown_8q":     {"inputs": ["ebit", "intexp"],                                "func": icv_ext_063_ebit_ttm_coverage_drawdown_8q},
    "icv_ext_064_ebit_coverage_pct_rank_5y":         {"inputs": ["ebit", "intexp"],                                "func": icv_ext_064_ebit_coverage_pct_rank_5y},
    "icv_ext_065_ebitda_coverage_zscore_5y":         {"inputs": ["ebitda", "intexp"],                              "func": icv_ext_065_ebitda_coverage_zscore_5y},
    "icv_ext_066_ebit_coverage_expanding_max_drawdown": {"inputs": ["ebit", "intexp"],                             "func": icv_ext_066_ebit_coverage_expanding_max_drawdown},
    "icv_ext_067_ncfo_coverage_pct_rank_12q":        {"inputs": ["ncfo", "intexp"],                                "func": icv_ext_067_ncfo_coverage_pct_rank_12q},
    "icv_ext_068_ebitda_ttm_coverage_below_2_streak": {"inputs": ["ebitda", "intexp"],                             "func": icv_ext_068_ebitda_ttm_coverage_below_2_streak},
    "icv_ext_069_all_three_below_1_flag":            {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],              "func": icv_ext_069_all_three_below_1_flag},
    "icv_ext_070_coverage_below_1_count":            {"inputs": ["ebit", "ebitda", "ncfo", "opinc", "intexp"],     "func": icv_ext_070_coverage_below_1_count},
    "icv_ext_071_coverage_below_2_count":            {"inputs": ["ebit", "ebitda", "ncfo", "opinc", "intexp"],     "func": icv_ext_071_coverage_below_2_count},
    "icv_ext_072_coverage_zscore_min_4q":            {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],              "func": icv_ext_072_coverage_zscore_min_4q},
    "icv_ext_073_coverage_composite_12q":            {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],              "func": icv_ext_073_coverage_composite_12q},
    "icv_ext_074_coverage_deterioration_composite_qoq": {"inputs": ["ebit", "ebitda", "ncfo", "intexp"],           "func": icv_ext_074_coverage_deterioration_composite_qoq},
    "icv_ext_075_distress_severity_composite":       {"inputs": ["ebit", "ebitda", "ncfo", "intexp", "debt", "cashnequiv"], "func": icv_ext_075_distress_severity_composite},
}
