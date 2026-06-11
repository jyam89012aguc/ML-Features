"""
60_earnings_collapse — Base Features 001-075
Domain: net-income decline, loss onset, magnitude of earnings collapse
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
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): QoQ and YoY net-income change levels ---

def ecl_001_netinc_qoq_change(netinc: pd.Series) -> pd.Series:
    """Net income QoQ change (absolute, 63-day lag)."""
    return netinc - netinc.shift(_TD_QTR)


def ecl_002_netinc_yoy_change(netinc: pd.Series) -> pd.Series:
    """Net income YoY change (absolute, 252-day lag)."""
    return netinc - netinc.shift(_TD_YEAR)


def ecl_003_netinc_qoq_pct(netinc: pd.Series) -> pd.Series:
    """Net income QoQ percent change; denominator is abs(prior)."""
    prior = netinc.shift(_TD_QTR)
    return _safe_div_abs(netinc - prior, prior)


def ecl_004_netinc_yoy_pct(netinc: pd.Series) -> pd.Series:
    """Net income YoY percent change; denominator is abs(prior)."""
    prior = netinc.shift(_TD_YEAR)
    return _safe_div_abs(netinc - prior, prior)


def ecl_005_netinc_2y_change(netinc: pd.Series) -> pd.Series:
    """Net income change over 2 years (504-day lag)."""
    return netinc - netinc.shift(_TD_2Y)


def ecl_006_netinc_3y_change(netinc: pd.Series) -> pd.Series:
    """Net income change over 3 years (756-day lag)."""
    return netinc - netinc.shift(_TD_3Y)


def ecl_007_netinc_2y_pct(netinc: pd.Series) -> pd.Series:
    """Net income 2-year percent change; denominator is abs(prior)."""
    prior = netinc.shift(_TD_2Y)
    return _safe_div_abs(netinc - prior, prior)


def ecl_008_netinc_3y_pct(netinc: pd.Series) -> pd.Series:
    """Net income 3-year percent change; denominator is abs(prior)."""
    prior = netinc.shift(_TD_3Y)
    return _safe_div_abs(netinc - prior, prior)


def ecl_009_netinccmn_qoq_change(netinccmn: pd.Series) -> pd.Series:
    """Net income (common) QoQ absolute change."""
    return netinccmn - netinccmn.shift(_TD_QTR)


def ecl_010_netinccmn_yoy_change(netinccmn: pd.Series) -> pd.Series:
    """Net income (common) YoY absolute change."""
    return netinccmn - netinccmn.shift(_TD_YEAR)


def ecl_011_eps_qoq_change(eps: pd.Series) -> pd.Series:
    """Basic EPS QoQ absolute change."""
    return eps - eps.shift(_TD_QTR)


def ecl_012_eps_yoy_change(eps: pd.Series) -> pd.Series:
    """Basic EPS YoY absolute change."""
    return eps - eps.shift(_TD_YEAR)


def ecl_013_epsdil_qoq_change(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS QoQ absolute change."""
    return epsdil - epsdil.shift(_TD_QTR)


def ecl_014_epsdil_yoy_change(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS YoY absolute change."""
    return epsdil - epsdil.shift(_TD_YEAR)


def ecl_015_ebit_yoy_change(ebit: pd.Series) -> pd.Series:
    """EBIT YoY absolute change."""
    return ebit - ebit.shift(_TD_YEAR)


# --- Group B (016-030): Loss onset and negative-income indicators ---

def ecl_016_netinc_is_negative(netinc: pd.Series) -> pd.Series:
    """Binary: 1 if net income < 0, else 0."""
    return (netinc < 0).astype(float)


def ecl_017_eps_is_negative(eps: pd.Series) -> pd.Series:
    """Binary: 1 if EPS < 0, else 0."""
    return (eps < 0).astype(float)


def ecl_018_ebit_is_negative(ebit: pd.Series) -> pd.Series:
    """Binary: 1 if EBIT < 0, else 0."""
    return (ebit < 0).astype(float)


def ecl_019_ebt_is_negative(ebt: pd.Series) -> pd.Series:
    """Binary: 1 if EBT < 0, else 0."""
    return (ebt < 0).astype(float)


def ecl_020_netinc_loss_quarters_1y(netinc: pd.Series) -> pd.Series:
    """Count of quarters (steps) with netinc < 0 in the last 252 trading days."""
    loss = (netinc < 0).astype(float)
    return _rolling_sum(loss, _TD_YEAR)


def ecl_021_netinc_loss_quarters_2y(netinc: pd.Series) -> pd.Series:
    """Count of loss quarters in the last 504 trading days."""
    loss = (netinc < 0).astype(float)
    return _rolling_sum(loss, _TD_2Y)


def ecl_022_netinc_loss_quarters_3y(netinc: pd.Series) -> pd.Series:
    """Count of loss quarters in the last 756 trading days."""
    loss = (netinc < 0).astype(float)
    return _rolling_sum(loss, _TD_3Y)


def ecl_023_netinc_consecutive_loss_streak(netinc: pd.Series) -> pd.Series:
    """
    Current consecutive-loss streak length (in daily observations).
    Resets to 0 on any non-negative netinc observation.
    """
    loss = (netinc < 0).astype(int)
    streak = np.zeros(len(loss), dtype=float)
    arr = loss.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=netinc.index)


def ecl_024_turned_negative_flag(netinc: pd.Series) -> pd.Series:
    """1 on the first day net income flips from non-negative (prior) to negative (current)."""
    curr_neg  = (netinc < 0).astype(float)
    prior_pos = (netinc.shift(_TD_QTR) >= 0).astype(float)
    return (curr_neg * prior_pos)


def ecl_025_turned_positive_flag(netinc: pd.Series) -> pd.Series:
    """1 when net income flips from negative (prior quarter) to non-negative (current)."""
    curr_pos  = (netinc >= 0).astype(float)
    prior_neg = (netinc.shift(_TD_QTR) < 0).astype(float)
    return (curr_pos * prior_neg)


def ecl_026_eps_turned_negative_flag(eps: pd.Series) -> pd.Series:
    """1 when EPS turns negative relative to prior quarter."""
    curr_neg  = (eps < 0).astype(float)
    prior_pos = (eps.shift(_TD_QTR) >= 0).astype(float)
    return curr_neg * prior_pos


def ecl_027_ebit_turned_negative_flag(ebit: pd.Series) -> pd.Series:
    """1 when EBIT turns negative relative to prior quarter."""
    curr_neg  = (ebit < 0).astype(float)
    prior_pos = (ebit.shift(_TD_QTR) >= 0).astype(float)
    return curr_neg * prior_pos


def ecl_028_all_three_negative_flag(netinc: pd.Series, ebit: pd.Series, ebt: pd.Series) -> pd.Series:
    """1 when netinc, ebit, AND ebt are all simultaneously negative."""
    return ((netinc < 0) & (ebit < 0) & (ebt < 0)).astype(float)


def ecl_029_netinc_worst_loss_1y(netinc: pd.Series) -> pd.Series:
    """Worst (most negative) net income value in trailing 252 days."""
    return _rolling_min(netinc, _TD_YEAR)


def ecl_030_netinc_worst_loss_3y(netinc: pd.Series) -> pd.Series:
    """Worst (most negative) net income value in trailing 756 days."""
    return _rolling_min(netinc, _TD_3Y)


# --- Group C (031-045): Magnitude of earnings decline vs trailing average ---

def ecl_031_netinc_vs_4q_avg(netinc: pd.Series) -> pd.Series:
    """Net income minus trailing 4-quarter (252-day) mean — level deviation."""
    avg = _rolling_mean(netinc, _TD_YEAR)
    return netinc - avg


def ecl_032_netinc_vs_8q_avg(netinc: pd.Series) -> pd.Series:
    """Net income minus trailing 8-quarter (504-day) mean."""
    avg = _rolling_mean(netinc, _TD_2Y)
    return netinc - avg


def ecl_033_netinc_pct_vs_4q_avg(netinc: pd.Series) -> pd.Series:
    """Net income percent deviation from trailing 4-quarter mean."""
    avg = _rolling_mean(netinc, _TD_YEAR)
    return _safe_div_abs(netinc - avg, avg)


def ecl_034_netinc_pct_vs_8q_avg(netinc: pd.Series) -> pd.Series:
    """Net income percent deviation from trailing 8-quarter mean."""
    avg = _rolling_mean(netinc, _TD_2Y)
    return _safe_div_abs(netinc - avg, avg)


def ecl_035_eps_vs_4q_avg(eps: pd.Series) -> pd.Series:
    """EPS minus trailing 4-quarter mean."""
    return eps - _rolling_mean(eps, _TD_YEAR)


def ecl_036_eps_pct_vs_4q_avg(eps: pd.Series) -> pd.Series:
    """EPS percent deviation from trailing 4-quarter mean."""
    avg = _rolling_mean(eps, _TD_YEAR)
    return _safe_div_abs(eps - avg, avg)


def ecl_037_netinc_drawdown_from_4q_peak(netinc: pd.Series) -> pd.Series:
    """Net income vs its 4-quarter (252-day) rolling peak (peak-to-trough decline)."""
    peak = _rolling_max(netinc, _TD_YEAR)
    return netinc - peak


def ecl_038_netinc_drawdown_from_8q_peak(netinc: pd.Series) -> pd.Series:
    """Net income vs its 8-quarter (504-day) rolling peak."""
    peak = _rolling_max(netinc, _TD_2Y)
    return netinc - peak


def ecl_039_netinc_drawdown_from_12q_peak(netinc: pd.Series) -> pd.Series:
    """Net income vs its 12-quarter (756-day) rolling peak."""
    peak = _rolling_max(netinc, _TD_3Y)
    return netinc - peak


def ecl_040_netinc_pct_drawdown_from_4q_peak(netinc: pd.Series) -> pd.Series:
    """Net income percent drawdown from 4-quarter peak (sign-preserving)."""
    peak = _rolling_max(netinc, _TD_YEAR)
    return _safe_div_abs(netinc - peak, peak)


def ecl_041_netinc_pct_drawdown_from_8q_peak(netinc: pd.Series) -> pd.Series:
    """Net income percent drawdown from 8-quarter peak."""
    peak = _rolling_max(netinc, _TD_2Y)
    return _safe_div_abs(netinc - peak, peak)


def ecl_042_netinc_drawdown_from_expanding_peak(netinc: pd.Series) -> pd.Series:
    """Net income vs its all-history expanding maximum."""
    peak = netinc.expanding(min_periods=1).max()
    return netinc - peak


def ecl_043_netinc_pct_drawdown_from_expanding_peak(netinc: pd.Series) -> pd.Series:
    """Net income percent drawdown from all-history expanding peak."""
    peak = netinc.expanding(min_periods=1).max()
    return _safe_div_abs(netinc - peak, peak)


def ecl_044_ebit_drawdown_from_4q_peak(ebit: pd.Series) -> pd.Series:
    """EBIT level drawdown from its 4-quarter rolling peak."""
    peak = _rolling_max(ebit, _TD_YEAR)
    return ebit - peak


def ecl_045_ebitda_drawdown_from_4q_peak(ebitda: pd.Series) -> pd.Series:
    """EBITDA level drawdown from its 4-quarter rolling peak."""
    peak = _rolling_max(ebitda, _TD_YEAR)
    return ebitda - peak


# --- Group D (046-060): Loss as fraction of revenue / earnings base ---

def ecl_046_loss_to_revenue_ratio(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net income (can be loss) divided by revenue — net margin signal."""
    return _safe_div(netinc, revenue.abs().replace(0, np.nan))


def ecl_047_loss_depth_vs_revenue_1y(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean net income divided by trailing 4-quarter mean revenue."""
    avg_ni  = _rolling_mean(netinc, _TD_YEAR)
    avg_rev = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div(avg_ni, avg_rev.abs().replace(0, np.nan))


def ecl_048_loss_to_ebitda_ratio(netinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net income divided by abs(EBITDA) — net income quality vs cash earnings."""
    return _safe_div(netinc, ebitda.abs().replace(0, np.nan))


def ecl_049_netinc_to_opinc_ratio(netinc: pd.Series, opinc: pd.Series) -> pd.Series:
    """Net income divided by abs(operating income)."""
    return _safe_div(netinc, opinc.abs().replace(0, np.nan))


def ecl_050_eps_to_4q_peak_eps_ratio(eps: pd.Series) -> pd.Series:
    """Current EPS divided by trailing 4-quarter peak EPS."""
    peak = _rolling_max(eps, _TD_YEAR)
    return _safe_div(eps, peak.replace(0, np.nan))


def ecl_051_worst_loss_to_revenue_1y(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Worst (min) net income in 1 year divided by mean revenue in 1 year."""
    worst   = _rolling_min(netinc, _TD_YEAR)
    avg_rev = _rolling_mean(revenue, _TD_YEAR)
    return _safe_div(worst, avg_rev.abs().replace(0, np.nan))


def ecl_052_netinc_loss_fraction_3y(netinc: pd.Series) -> pd.Series:
    """Fraction of 3-year (756-day) window where net income was negative."""
    loss = (netinc < 0).astype(float)
    return _rolling_mean(loss, _TD_3Y)


def ecl_053_eps_loss_fraction_3y(eps: pd.Series) -> pd.Series:
    """Fraction of 3-year window where EPS was negative."""
    loss = (eps < 0).astype(float)
    return _rolling_mean(loss, _TD_3Y)


def ecl_054_netinc_severity_ratio_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ percent change in net income clipped to [-10, 0] to measure loss acceleration."""
    chg = _safe_div_abs(netinc - netinc.shift(_TD_QTR), netinc.shift(_TD_QTR))
    return chg.clip(upper=0)


def ecl_055_netinc_severity_ratio_yoy(netinc: pd.Series) -> pd.Series:
    """YoY percent change in net income clipped to [-10, 0]."""
    chg = _safe_div_abs(netinc - netinc.shift(_TD_YEAR), netinc.shift(_TD_YEAR))
    return chg.clip(upper=0)


def ecl_056_gp_minus_netinc_gap(gp: pd.Series, netinc: pd.Series) -> pd.Series:
    """Gross profit minus net income — captures below-the-line cost drag."""
    return gp - netinc


def ecl_057_opinc_minus_netinc_gap(opinc: pd.Series, netinc: pd.Series) -> pd.Series:
    """Operating income minus net income — below-operating-line drag."""
    return opinc - netinc


def ecl_058_ebt_minus_netinc_gap(ebt: pd.Series, netinc: pd.Series) -> pd.Series:
    """EBT minus net income — tax and extraordinary drag."""
    return ebt - netinc


def ecl_059_netinc_cumulative_4q_sum(netinc: pd.Series) -> pd.Series:
    """Rolling sum of net income over last 252 days (trailing-twelve-month proxy)."""
    return _rolling_sum(netinc, _TD_YEAR)


def ecl_060_netinc_cumulative_8q_sum(netinc: pd.Series) -> pd.Series:
    """Rolling sum of net income over last 504 days (TTM 2-year total)."""
    return _rolling_sum(netinc, _TD_2Y)


# --- Group E (061-075): Z-score, percentile rank, and composite severity ---

def ecl_061_netinc_zscore_4q(netinc: pd.Series) -> pd.Series:
    """Z-score of net income within a trailing 4-quarter (252-day) window."""
    return _zscore_rolling(netinc, _TD_YEAR)


def ecl_062_netinc_zscore_8q(netinc: pd.Series) -> pd.Series:
    """Z-score of net income within a trailing 8-quarter (504-day) window."""
    return _zscore_rolling(netinc, _TD_2Y)


def ecl_063_netinc_zscore_12q(netinc: pd.Series) -> pd.Series:
    """Z-score of net income within a trailing 12-quarter (756-day) window."""
    return _zscore_rolling(netinc, _TD_3Y)


def ecl_064_netinc_expanding_zscore(netinc: pd.Series) -> pd.Series:
    """Expanding z-score of net income (how extreme vs entire history)."""
    m  = netinc.expanding(min_periods=2).mean()
    sd = netinc.expanding(min_periods=2).std()
    return _safe_div(netinc - m, sd)


def ecl_065_eps_zscore_4q(eps: pd.Series) -> pd.Series:
    """Z-score of EPS within a trailing 4-quarter window."""
    return _zscore_rolling(eps, _TD_YEAR)


def ecl_066_eps_zscore_8q(eps: pd.Series) -> pd.Series:
    """Z-score of EPS within a trailing 8-quarter window."""
    return _zscore_rolling(eps, _TD_2Y)


def ecl_067_netinc_pct_rank_4q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income within a trailing 4-quarter (252-day) window."""
    return _rolling_rank_pct(netinc, _TD_YEAR)


def ecl_068_netinc_pct_rank_8q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income within a trailing 8-quarter (504-day) window."""
    return _rolling_rank_pct(netinc, _TD_2Y)


def ecl_069_netinc_pct_rank_12q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income within a trailing 12-quarter (756-day) window."""
    return _rolling_rank_pct(netinc, _TD_3Y)


def ecl_070_netinc_expanding_pct_rank(netinc: pd.Series) -> pd.Series:
    """Expanding percentile rank of net income (all-history rank)."""
    return netinc.expanding(min_periods=2).rank(pct=True)


def ecl_071_eps_pct_rank_4q(eps: pd.Series) -> pd.Series:
    """Percentile rank of EPS within a trailing 4-quarter window."""
    return _rolling_rank_pct(eps, _TD_YEAR)


def ecl_072_ebit_zscore_4q(ebit: pd.Series) -> pd.Series:
    """Z-score of EBIT within a trailing 4-quarter window."""
    return _zscore_rolling(ebit, _TD_YEAR)


def ecl_073_netinc_ewm_deviation(netinc: pd.Series) -> pd.Series:
    """Net income minus its 4-quarter EWM (span=252); captures momentum shift."""
    ewm = _ewm_mean(netinc, _TD_YEAR)
    return netinc - ewm


def ecl_074_netinc_ttm_pct_of_5y_peak_ttm(netinc: pd.Series) -> pd.Series:
    """TTM net income (4Q rolling sum) divided by its 5-year expanding maximum TTM.
    Ratio <= 1 always; deep collapse toward 0 signals severe earnings erosion."""
    ttm  = _rolling_sum(netinc, _TD_YEAR)
    peak = ttm.rolling(_TD_5Y, min_periods=max(1, _TD_YEAR)).max()
    return _safe_div(ttm, peak.replace(0, np.nan))


def ecl_075_earnings_collapse_composite(netinc: pd.Series, eps: pd.Series, ebit: pd.Series) -> pd.Series:
    """
    Composite earnings-collapse severity score:
    equally weighted sum of three z-scores (netinc, eps, ebit) in 4-quarter window.
    """
    z_ni   = _zscore_rolling(netinc, _TD_YEAR)
    z_eps  = _zscore_rolling(eps,    _TD_YEAR)
    z_ebit = _zscore_rolling(ebit,   _TD_YEAR)
    return (z_ni + z_eps + z_ebit) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

EARNINGS_COLLAPSE_REGISTRY_001_075 = {
    "ecl_001_netinc_qoq_change":                   {"inputs": ["netinc"],                        "func": ecl_001_netinc_qoq_change},
    "ecl_002_netinc_yoy_change":                   {"inputs": ["netinc"],                        "func": ecl_002_netinc_yoy_change},
    "ecl_003_netinc_qoq_pct":                      {"inputs": ["netinc"],                        "func": ecl_003_netinc_qoq_pct},
    "ecl_004_netinc_yoy_pct":                      {"inputs": ["netinc"],                        "func": ecl_004_netinc_yoy_pct},
    "ecl_005_netinc_2y_change":                    {"inputs": ["netinc"],                        "func": ecl_005_netinc_2y_change},
    "ecl_006_netinc_3y_change":                    {"inputs": ["netinc"],                        "func": ecl_006_netinc_3y_change},
    "ecl_007_netinc_2y_pct":                       {"inputs": ["netinc"],                        "func": ecl_007_netinc_2y_pct},
    "ecl_008_netinc_3y_pct":                       {"inputs": ["netinc"],                        "func": ecl_008_netinc_3y_pct},
    "ecl_009_netinccmn_qoq_change":                {"inputs": ["netinccmn"],                     "func": ecl_009_netinccmn_qoq_change},
    "ecl_010_netinccmn_yoy_change":                {"inputs": ["netinccmn"],                     "func": ecl_010_netinccmn_yoy_change},
    "ecl_011_eps_qoq_change":                      {"inputs": ["eps"],                           "func": ecl_011_eps_qoq_change},
    "ecl_012_eps_yoy_change":                      {"inputs": ["eps"],                           "func": ecl_012_eps_yoy_change},
    "ecl_013_epsdil_qoq_change":                   {"inputs": ["epsdil"],                        "func": ecl_013_epsdil_qoq_change},
    "ecl_014_epsdil_yoy_change":                   {"inputs": ["epsdil"],                        "func": ecl_014_epsdil_yoy_change},
    "ecl_015_ebit_yoy_change":                     {"inputs": ["ebit"],                          "func": ecl_015_ebit_yoy_change},
    "ecl_016_netinc_is_negative":                  {"inputs": ["netinc"],                        "func": ecl_016_netinc_is_negative},
    "ecl_017_eps_is_negative":                     {"inputs": ["eps"],                           "func": ecl_017_eps_is_negative},
    "ecl_018_ebit_is_negative":                    {"inputs": ["ebit"],                          "func": ecl_018_ebit_is_negative},
    "ecl_019_ebt_is_negative":                     {"inputs": ["ebt"],                           "func": ecl_019_ebt_is_negative},
    "ecl_020_netinc_loss_quarters_1y":             {"inputs": ["netinc"],                        "func": ecl_020_netinc_loss_quarters_1y},
    "ecl_021_netinc_loss_quarters_2y":             {"inputs": ["netinc"],                        "func": ecl_021_netinc_loss_quarters_2y},
    "ecl_022_netinc_loss_quarters_3y":             {"inputs": ["netinc"],                        "func": ecl_022_netinc_loss_quarters_3y},
    "ecl_023_netinc_consecutive_loss_streak":      {"inputs": ["netinc"],                        "func": ecl_023_netinc_consecutive_loss_streak},
    "ecl_024_turned_negative_flag":                {"inputs": ["netinc"],                        "func": ecl_024_turned_negative_flag},
    "ecl_025_turned_positive_flag":                {"inputs": ["netinc"],                        "func": ecl_025_turned_positive_flag},
    "ecl_026_eps_turned_negative_flag":            {"inputs": ["eps"],                           "func": ecl_026_eps_turned_negative_flag},
    "ecl_027_ebit_turned_negative_flag":           {"inputs": ["ebit"],                          "func": ecl_027_ebit_turned_negative_flag},
    "ecl_028_all_three_negative_flag":             {"inputs": ["netinc", "ebit", "ebt"],         "func": ecl_028_all_three_negative_flag},
    "ecl_029_netinc_worst_loss_1y":                {"inputs": ["netinc"],                        "func": ecl_029_netinc_worst_loss_1y},
    "ecl_030_netinc_worst_loss_3y":                {"inputs": ["netinc"],                        "func": ecl_030_netinc_worst_loss_3y},
    "ecl_031_netinc_vs_4q_avg":                    {"inputs": ["netinc"],                        "func": ecl_031_netinc_vs_4q_avg},
    "ecl_032_netinc_vs_8q_avg":                    {"inputs": ["netinc"],                        "func": ecl_032_netinc_vs_8q_avg},
    "ecl_033_netinc_pct_vs_4q_avg":               {"inputs": ["netinc"],                        "func": ecl_033_netinc_pct_vs_4q_avg},
    "ecl_034_netinc_pct_vs_8q_avg":               {"inputs": ["netinc"],                        "func": ecl_034_netinc_pct_vs_8q_avg},
    "ecl_035_eps_vs_4q_avg":                       {"inputs": ["eps"],                           "func": ecl_035_eps_vs_4q_avg},
    "ecl_036_eps_pct_vs_4q_avg":                   {"inputs": ["eps"],                           "func": ecl_036_eps_pct_vs_4q_avg},
    "ecl_037_netinc_drawdown_from_4q_peak":        {"inputs": ["netinc"],                        "func": ecl_037_netinc_drawdown_from_4q_peak},
    "ecl_038_netinc_drawdown_from_8q_peak":        {"inputs": ["netinc"],                        "func": ecl_038_netinc_drawdown_from_8q_peak},
    "ecl_039_netinc_drawdown_from_12q_peak":       {"inputs": ["netinc"],                        "func": ecl_039_netinc_drawdown_from_12q_peak},
    "ecl_040_netinc_pct_drawdown_from_4q_peak":    {"inputs": ["netinc"],                        "func": ecl_040_netinc_pct_drawdown_from_4q_peak},
    "ecl_041_netinc_pct_drawdown_from_8q_peak":    {"inputs": ["netinc"],                        "func": ecl_041_netinc_pct_drawdown_from_8q_peak},
    "ecl_042_netinc_drawdown_from_expanding_peak": {"inputs": ["netinc"],                        "func": ecl_042_netinc_drawdown_from_expanding_peak},
    "ecl_043_netinc_pct_drawdown_from_expanding_peak": {"inputs": ["netinc"],                   "func": ecl_043_netinc_pct_drawdown_from_expanding_peak},
    "ecl_044_ebit_drawdown_from_4q_peak":          {"inputs": ["ebit"],                          "func": ecl_044_ebit_drawdown_from_4q_peak},
    "ecl_045_ebitda_drawdown_from_4q_peak":        {"inputs": ["ebitda"],                        "func": ecl_045_ebitda_drawdown_from_4q_peak},
    "ecl_046_loss_to_revenue_ratio":               {"inputs": ["netinc", "revenue"],             "func": ecl_046_loss_to_revenue_ratio},
    "ecl_047_loss_depth_vs_revenue_1y":            {"inputs": ["netinc", "revenue"],             "func": ecl_047_loss_depth_vs_revenue_1y},
    "ecl_048_loss_to_ebitda_ratio":                {"inputs": ["netinc", "ebitda"],              "func": ecl_048_loss_to_ebitda_ratio},
    "ecl_049_netinc_to_opinc_ratio":               {"inputs": ["netinc", "opinc"],               "func": ecl_049_netinc_to_opinc_ratio},
    "ecl_050_eps_to_4q_peak_eps_ratio":            {"inputs": ["eps"],                           "func": ecl_050_eps_to_4q_peak_eps_ratio},
    "ecl_051_worst_loss_to_revenue_1y":            {"inputs": ["netinc", "revenue"],             "func": ecl_051_worst_loss_to_revenue_1y},
    "ecl_052_netinc_loss_fraction_3y":             {"inputs": ["netinc"],                        "func": ecl_052_netinc_loss_fraction_3y},
    "ecl_053_eps_loss_fraction_3y":                {"inputs": ["eps"],                           "func": ecl_053_eps_loss_fraction_3y},
    "ecl_054_netinc_severity_ratio_qoq":           {"inputs": ["netinc"],                        "func": ecl_054_netinc_severity_ratio_qoq},
    "ecl_055_netinc_severity_ratio_yoy":           {"inputs": ["netinc"],                        "func": ecl_055_netinc_severity_ratio_yoy},
    "ecl_056_gp_minus_netinc_gap":                 {"inputs": ["gp", "netinc"],                  "func": ecl_056_gp_minus_netinc_gap},
    "ecl_057_opinc_minus_netinc_gap":              {"inputs": ["opinc", "netinc"],               "func": ecl_057_opinc_minus_netinc_gap},
    "ecl_058_ebt_minus_netinc_gap":                {"inputs": ["ebt", "netinc"],                 "func": ecl_058_ebt_minus_netinc_gap},
    "ecl_059_netinc_cumulative_4q_sum":            {"inputs": ["netinc"],                        "func": ecl_059_netinc_cumulative_4q_sum},
    "ecl_060_netinc_cumulative_8q_sum":            {"inputs": ["netinc"],                        "func": ecl_060_netinc_cumulative_8q_sum},
    "ecl_061_netinc_zscore_4q":                    {"inputs": ["netinc"],                        "func": ecl_061_netinc_zscore_4q},
    "ecl_062_netinc_zscore_8q":                    {"inputs": ["netinc"],                        "func": ecl_062_netinc_zscore_8q},
    "ecl_063_netinc_zscore_12q":                   {"inputs": ["netinc"],                        "func": ecl_063_netinc_zscore_12q},
    "ecl_064_netinc_expanding_zscore":             {"inputs": ["netinc"],                        "func": ecl_064_netinc_expanding_zscore},
    "ecl_065_eps_zscore_4q":                       {"inputs": ["eps"],                           "func": ecl_065_eps_zscore_4q},
    "ecl_066_eps_zscore_8q":                       {"inputs": ["eps"],                           "func": ecl_066_eps_zscore_8q},
    "ecl_067_netinc_pct_rank_4q":                  {"inputs": ["netinc"],                        "func": ecl_067_netinc_pct_rank_4q},
    "ecl_068_netinc_pct_rank_8q":                  {"inputs": ["netinc"],                        "func": ecl_068_netinc_pct_rank_8q},
    "ecl_069_netinc_pct_rank_12q":                 {"inputs": ["netinc"],                        "func": ecl_069_netinc_pct_rank_12q},
    "ecl_070_netinc_expanding_pct_rank":           {"inputs": ["netinc"],                        "func": ecl_070_netinc_expanding_pct_rank},
    "ecl_071_eps_pct_rank_4q":                     {"inputs": ["eps"],                           "func": ecl_071_eps_pct_rank_4q},
    "ecl_072_ebit_zscore_4q":                      {"inputs": ["ebit"],                          "func": ecl_072_ebit_zscore_4q},
    "ecl_073_netinc_ewm_deviation":                {"inputs": ["netinc"],                        "func": ecl_073_netinc_ewm_deviation},
    "ecl_074_netinc_ttm_pct_of_5y_peak_ttm":       {"inputs": ["netinc"],                        "func": ecl_074_netinc_ttm_pct_of_5y_peak_ttm},
    "ecl_075_earnings_collapse_composite":         {"inputs": ["netinc", "eps", "ebit"],         "func": ecl_075_earnings_collapse_composite},
}
