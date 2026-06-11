"""
65_leverage_stress — Base Features 001-075
Domain: debt/equity and debt/assets escalation, capital-structure stress
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
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """
    Element-wise division; replaces zero denominator with NaN.
    Negative denominators (e.g. negative equity) are preserved as-is —
    they carry economic meaning (technical insolvency) and must not be masked.
    Only exact-zero denominators are replaced with NaN to avoid inf.
    """
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of denominator; avoids sign confusion in pct features."""
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

# --- Group A (001-015): Core leverage ratios ---

def lvs_001_debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Debt / equity. Negative equity is preserved (technical insolvency signal)."""
    return _safe_div(debt, equity)


def lvs_002_debt_to_assets(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Total debt / total assets."""
    return _safe_div(debt, assets)


def lvs_003_liabilities_to_assets(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Total liabilities / total assets."""
    return _safe_div(liabilities, assets)


def lvs_004_net_debt(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt = debt - cash & equivalents."""
    return debt - cashnequiv


def lvs_005_net_debt_to_equity(debt: pd.Series, cashnequiv: pd.Series, equity: pd.Series) -> pd.Series:
    """Net debt / equity. Negative equity is preserved."""
    net_debt = debt - cashnequiv
    return _safe_div(net_debt, equity)


def lvs_006_net_debt_to_assets(debt: pd.Series, cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Net debt / assets."""
    net_debt = debt - cashnequiv
    return _safe_div(net_debt, assets)


def lvs_007_debt_to_ebitda(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Total debt / EBITDA. Classic leverage coverage ratio."""
    return _safe_div(debt, ebitda)


def lvs_008_net_debt_to_ebitda(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net debt / EBITDA."""
    net_debt = debt - cashnequiv
    return _safe_div(net_debt, ebitda)


def lvs_009_financial_leverage_multiplier(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Financial leverage = assets / equity (equity multiplier)."""
    return _safe_div(assets, equity)


def lvs_010_short_term_debt_mix(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Short-term debt / total debt (ST debt concentration)."""
    return _safe_div(debtc, debt)


def lvs_011_long_term_debt_mix(debtnc: pd.Series, debt: pd.Series) -> pd.Series:
    """Long-term debt / total debt."""
    return _safe_div(debtnc, debt)


def lvs_012_liabilities_to_equity(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Liabilities / equity. Negative equity preserved."""
    return _safe_div(liabilities, equity)


def lvs_013_noncurrent_liab_to_assets(liabilitiesnc: pd.Series, assets: pd.Series) -> pd.Series:
    """Non-current liabilities / total assets."""
    return _safe_div(liabilitiesnc, assets)


def lvs_014_current_liab_to_assets(liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current liabilities / total assets."""
    return _safe_div(liabilitiesc, assets)


def lvs_015_net_debt_to_liabilities(debt: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net debt / total liabilities."""
    net_debt = debt - cashnequiv
    return _safe_div(net_debt, liabilities)


# --- Group B (016-030): QoQ escalation of leverage ratios ---

def lvs_016_debt_to_equity_qoq_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ absolute change in D/E ratio."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(_TD_QTR)


def lvs_017_debt_to_assets_qoq_change(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ absolute change in D/A ratio."""
    ratio = _safe_div(debt, assets)
    return ratio - ratio.shift(_TD_QTR)


def lvs_018_liabilities_to_assets_qoq_change(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ absolute change in L/A ratio."""
    ratio = _safe_div(liabilities, assets)
    return ratio - ratio.shift(_TD_QTR)


def lvs_019_net_debt_to_ebitda_qoq_change(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """QoQ change in net-debt/EBITDA."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return ratio - ratio.shift(_TD_QTR)


def lvs_020_financial_leverage_qoq_change(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in financial leverage multiplier."""
    ratio = _safe_div(assets, equity)
    return ratio - ratio.shift(_TD_QTR)


def lvs_021_short_term_debt_mix_qoq_change(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in short-term debt fraction."""
    ratio = _safe_div(debtc, debt)
    return ratio - ratio.shift(_TD_QTR)


def lvs_022_debt_to_equity_yoy_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY absolute change in D/E ratio."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(_TD_YEAR)


def lvs_023_debt_to_assets_yoy_change(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY absolute change in D/A ratio."""
    ratio = _safe_div(debt, assets)
    return ratio - ratio.shift(_TD_YEAR)


def lvs_024_net_debt_to_equity_yoy_change(debt: pd.Series, cashnequiv: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in net-D/E ratio."""
    ratio = _safe_div(debt - cashnequiv, equity)
    return ratio - ratio.shift(_TD_YEAR)


def lvs_025_debt_to_ebitda_yoy_change(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """YoY change in D/EBITDA."""
    ratio = _safe_div(debt, ebitda)
    return ratio - ratio.shift(_TD_YEAR)


def lvs_026_liabilities_to_equity_yoy_change(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in liabilities/equity."""
    ratio = _safe_div(liabilities, equity)
    return ratio - ratio.shift(_TD_YEAR)


def lvs_027_net_debt_qoq_change(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in net debt level."""
    net_debt = debt - cashnequiv
    return net_debt - net_debt.shift(_TD_QTR)


def lvs_028_net_debt_yoy_change(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in net debt level."""
    net_debt = debt - cashnequiv
    return net_debt - net_debt.shift(_TD_YEAR)


def lvs_029_debt_qoq_pct_change(debt: pd.Series) -> pd.Series:
    """QoQ percent change in total debt."""
    prior = debt.shift(_TD_QTR)
    return _safe_div_abs(debt - prior, prior)


def lvs_030_debt_yoy_pct_change(debt: pd.Series) -> pd.Series:
    """YoY percent change in total debt."""
    prior = debt.shift(_TD_YEAR)
    return _safe_div_abs(debt - prior, prior)


# --- Group C (031-045): Leverage above trailing range / drawup from minimum ---

def lvs_031_debt_to_equity_above_4q_max(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its trailing 4-quarter maximum (drawup from range top)."""
    ratio = _safe_div(debt, equity)
    return ratio - _rolling_max(ratio, _TD_YEAR)


def lvs_032_debt_to_equity_above_8q_max(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its trailing 8-quarter maximum."""
    ratio = _safe_div(debt, equity)
    return ratio - _rolling_max(ratio, _TD_2Y)


def lvs_033_debt_to_assets_above_4q_max(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """D/A ratio minus its trailing 4-quarter maximum."""
    ratio = _safe_div(debt, assets)
    return ratio - _rolling_max(ratio, _TD_YEAR)


def lvs_034_net_debt_to_ebitda_above_4q_max(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net-D/EBITDA minus its trailing 4-quarter maximum."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return ratio - _rolling_max(ratio, _TD_YEAR)


def lvs_035_leverage_drawup_from_4q_min(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its trailing 4-quarter minimum (leverage drawup)."""
    ratio = _safe_div(debt, equity)
    return ratio - _rolling_min(ratio, _TD_YEAR)


def lvs_036_leverage_drawup_from_8q_min(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its trailing 8-quarter minimum."""
    ratio = _safe_div(debt, equity)
    return ratio - _rolling_min(ratio, _TD_2Y)


def lvs_037_leverage_drawup_from_12q_min(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its trailing 12-quarter minimum."""
    ratio = _safe_div(debt, equity)
    return ratio - _rolling_min(ratio, _TD_3Y)


def lvs_038_debt_to_assets_above_8q_avg(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """D/A ratio minus its trailing 8-quarter mean."""
    ratio = _safe_div(debt, assets)
    return ratio - _rolling_mean(ratio, _TD_2Y)


def lvs_039_net_debt_drawup_from_4q_min(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt minus its trailing 4-quarter minimum."""
    nd = debt - cashnequiv
    return nd - _rolling_min(nd, _TD_YEAR)


def lvs_040_net_debt_drawup_from_12q_min(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt minus its trailing 12-quarter minimum."""
    nd = debt - cashnequiv
    return nd - _rolling_min(nd, _TD_3Y)


def lvs_041_leverage_rank_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Percentile rank of D/E ratio within trailing 4-quarter window."""
    ratio = _safe_div(debt, equity)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def lvs_042_leverage_rank_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Percentile rank of D/E ratio within trailing 8-quarter window."""
    ratio = _safe_div(debt, equity)
    return _rolling_rank_pct(ratio, _TD_2Y)


def lvs_043_debt_to_assets_rank_4q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of D/A ratio within trailing 4-quarter window."""
    ratio = _safe_div(debt, assets)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def lvs_044_net_debt_to_ebitda_rank_4q(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Percentile rank of net-D/EBITDA in trailing 4-quarter window."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def lvs_045_leverage_expanding_pct_rank(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Expanding percentile rank of D/E ratio vs all-history."""
    ratio = _safe_div(debt, equity)
    return ratio.expanding(min_periods=2).rank(pct=True)


# --- Group D (046-060): Consecutive rising quarters and binary stress flags ---

def lvs_046_consecutive_rising_leverage_qtrs(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Current streak of consecutive quarters where D/E ratio has risen.
    Resets to 0 when D/E falls or stays flat.
    """
    ratio = _safe_div(debt, equity)
    rose  = (ratio > ratio.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(rose), dtype=float)
    arr = rose.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=debt.index)


def lvs_047_consecutive_rising_debt_qtrs(debt: pd.Series) -> pd.Series:
    """Consecutive quarters where total debt level has risen."""
    rose   = (debt > debt.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(rose), dtype=float)
    arr = rose.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=debt.index)


def lvs_048_rising_debt_falling_equity_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 when debt rose QoQ AND equity shrank QoQ simultaneously."""
    debt_up   = (debt   > debt.shift(_TD_QTR)).astype(float)
    equity_dn = (equity < equity.shift(_TD_QTR)).astype(float)
    return debt_up * equity_dn


def lvs_049_negative_equity_flag(equity: pd.Series) -> pd.Series:
    """Binary: 1 if equity < 0 (technical insolvency)."""
    return (equity < 0).astype(float)


def lvs_050_negative_equity_quarters_1y(equity: pd.Series) -> pd.Series:
    """Count of daily observations with negative equity in trailing 252 days."""
    return _rolling_sum((equity < 0).astype(float), _TD_YEAR)


def lvs_051_negative_equity_quarters_2y(equity: pd.Series) -> pd.Series:
    """Count of daily observations with negative equity in trailing 504 days."""
    return _rolling_sum((equity < 0).astype(float), _TD_2Y)


def lvs_052_equity_turned_negative_flag(equity: pd.Series) -> pd.Series:
    """1 when equity crosses from non-negative to negative vs prior quarter."""
    curr_neg  = (equity < 0).astype(float)
    prior_pos = (equity.shift(_TD_QTR) >= 0).astype(float)
    return curr_neg * prior_pos


def lvs_053_leverage_above_2x_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Binary: 1 if D/E > 2.0."""
    return (_safe_div(debt, equity) > 2.0).astype(float)


def lvs_054_leverage_above_4x_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Binary: 1 if D/E > 4.0."""
    return (_safe_div(debt, equity) > 4.0).astype(float)


def lvs_055_net_debt_positive_flag(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Binary: 1 if net debt > 0 (debt exceeds cash)."""
    return ((debt - cashnequiv) > 0).astype(float)


def lvs_056_debt_to_assets_above_50pct_flag(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 if D/A > 0.5."""
    return (_safe_div(debt, assets) > 0.5).astype(float)


def lvs_057_debt_to_assets_above_75pct_flag(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 if D/A > 0.75."""
    return (_safe_div(debt, assets) > 0.75).astype(float)


def lvs_058_liabilities_to_assets_above_90pct_flag(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 if L/A > 0.9 (near-insolvent balance sheet)."""
    return (_safe_div(liabilities, assets) > 0.9).astype(float)


def lvs_059_rising_leverage_fraction_1y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where D/E was rising (vs 63-day lag)."""
    ratio = _safe_div(debt, equity)
    rose  = (ratio > ratio.shift(_TD_QTR)).astype(float)
    return _rolling_mean(rose, _TD_YEAR)


def lvs_060_rising_leverage_fraction_3y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Fraction of trailing 756 days where D/E was rising."""
    ratio = _safe_div(debt, equity)
    rose  = (ratio > ratio.shift(_TD_QTR)).astype(float)
    return _rolling_mean(rose, _TD_3Y)


# --- Group E (061-075): Z-scores, multi-year change, and composite stress ---

def lvs_061_debt_to_equity_zscore_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of D/E ratio within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(_safe_div(debt, equity), _TD_YEAR)


def lvs_062_debt_to_equity_zscore_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of D/E ratio within trailing 8-quarter window."""
    return _zscore_rolling(_safe_div(debt, equity), _TD_2Y)


def lvs_063_debt_to_assets_zscore_4q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of D/A ratio within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(debt, assets), _TD_YEAR)


def lvs_064_net_debt_to_ebitda_zscore_4q(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of net-D/EBITDA within trailing 4-quarter window."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return _zscore_rolling(ratio, _TD_YEAR)


def lvs_065_financial_leverage_zscore_4q(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of financial leverage multiplier within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(assets, equity), _TD_YEAR)


def lvs_066_debt_to_equity_2y_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio change over 2 years (504-day lag)."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(_TD_2Y)


def lvs_067_debt_to_equity_3y_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio change over 3 years (756-day lag)."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(_TD_3Y)


def lvs_068_net_debt_2y_pct_change(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt 2-year percent change."""
    nd    = debt - cashnequiv
    prior = nd.shift(_TD_2Y)
    return _safe_div_abs(nd - prior, prior)


def lvs_069_net_debt_3y_pct_change(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt 3-year percent change."""
    nd    = debt - cashnequiv
    prior = nd.shift(_TD_3Y)
    return _safe_div_abs(nd - prior, prior)


def lvs_070_debt_growth_while_equity_shrinks_3y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Compound stress: 1 if total debt has grown over 3y AND equity has shrunk over 3y.
    """
    debt_grew   = (debt   > debt.shift(_TD_3Y)).astype(float)
    equity_fell = (equity < equity.shift(_TD_3Y)).astype(float)
    return debt_grew * equity_fell


def lvs_071_leverage_ewm_deviation(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its 4-quarter EWM (span=252); captures momentum shift."""
    ratio = _safe_div(debt, equity)
    ewm   = _ewm_mean(ratio, _TD_YEAR)
    return ratio - ewm


def lvs_072_debt_to_assets_ewm_deviation(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """D/A ratio minus its 4-quarter EWM."""
    ratio = _safe_div(debt, assets)
    ewm   = _ewm_mean(ratio, _TD_YEAR)
    return ratio - ewm


def lvs_073_leverage_range_position_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Position of D/E ratio within its trailing 8-quarter [min, max] range:
    (ratio - min) / (max - min).  1.0 = at 8-quarter high (maximum stress).
    """
    ratio = _safe_div(debt, equity)
    lo = _rolling_min(ratio, _TD_2Y)
    hi = _rolling_max(ratio, _TD_2Y)
    return _safe_div(ratio - lo, hi - lo)


def lvs_074_net_debt_to_ebitda_pct_rank_8q(debt: pd.Series, cashnequiv: pd.Series,
                                            ebitda: pd.Series) -> pd.Series:
    """
    Percentile rank of net-debt/EBITDA within the trailing 8-quarter (504-day) window.
    High rank = leverage coverage near its worst level over 2 years.
    """
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return _rolling_rank_pct(ratio, _TD_2Y)


def lvs_075_leverage_stress_composite(debt: pd.Series, equity: pd.Series, assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """
    Composite leverage-stress score: equally weighted average of z-scores of
    D/E, D/A, and D/EBITDA within a trailing 4-quarter window.
    """
    z_de = _zscore_rolling(_safe_div(debt, equity),  _TD_YEAR)
    z_da = _zscore_rolling(_safe_div(debt, assets),  _TD_YEAR)
    z_deb= _zscore_rolling(_safe_div(debt, ebitda),  _TD_YEAR)
    return (z_de + z_da + z_deb) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

LEVERAGE_STRESS_REGISTRY_001_075 = {
    "lvs_001_debt_to_equity":                        {"inputs": ["debt", "equity"],                              "func": lvs_001_debt_to_equity},
    "lvs_002_debt_to_assets":                        {"inputs": ["debt", "assets"],                              "func": lvs_002_debt_to_assets},
    "lvs_003_liabilities_to_assets":                 {"inputs": ["liabilities", "assets"],                      "func": lvs_003_liabilities_to_assets},
    "lvs_004_net_debt":                              {"inputs": ["debt", "cashnequiv"],                         "func": lvs_004_net_debt},
    "lvs_005_net_debt_to_equity":                    {"inputs": ["debt", "cashnequiv", "equity"],               "func": lvs_005_net_debt_to_equity},
    "lvs_006_net_debt_to_assets":                    {"inputs": ["debt", "cashnequiv", "assets"],               "func": lvs_006_net_debt_to_assets},
    "lvs_007_debt_to_ebitda":                        {"inputs": ["debt", "ebitda"],                             "func": lvs_007_debt_to_ebitda},
    "lvs_008_net_debt_to_ebitda":                    {"inputs": ["debt", "cashnequiv", "ebitda"],               "func": lvs_008_net_debt_to_ebitda},
    "lvs_009_financial_leverage_multiplier":         {"inputs": ["assets", "equity"],                           "func": lvs_009_financial_leverage_multiplier},
    "lvs_010_short_term_debt_mix":                   {"inputs": ["debtc", "debt"],                              "func": lvs_010_short_term_debt_mix},
    "lvs_011_long_term_debt_mix":                    {"inputs": ["debtnc", "debt"],                             "func": lvs_011_long_term_debt_mix},
    "lvs_012_liabilities_to_equity":                 {"inputs": ["liabilities", "equity"],                      "func": lvs_012_liabilities_to_equity},
    "lvs_013_noncurrent_liab_to_assets":             {"inputs": ["liabilitiesnc", "assets"],                    "func": lvs_013_noncurrent_liab_to_assets},
    "lvs_014_current_liab_to_assets":                {"inputs": ["liabilitiesc", "assets"],                     "func": lvs_014_current_liab_to_assets},
    "lvs_015_net_debt_to_liabilities":               {"inputs": ["debt", "cashnequiv", "liabilities"],          "func": lvs_015_net_debt_to_liabilities},
    "lvs_016_debt_to_equity_qoq_change":             {"inputs": ["debt", "equity"],                              "func": lvs_016_debt_to_equity_qoq_change},
    "lvs_017_debt_to_assets_qoq_change":             {"inputs": ["debt", "assets"],                              "func": lvs_017_debt_to_assets_qoq_change},
    "lvs_018_liabilities_to_assets_qoq_change":      {"inputs": ["liabilities", "assets"],                      "func": lvs_018_liabilities_to_assets_qoq_change},
    "lvs_019_net_debt_to_ebitda_qoq_change":         {"inputs": ["debt", "cashnequiv", "ebitda"],               "func": lvs_019_net_debt_to_ebitda_qoq_change},
    "lvs_020_financial_leverage_qoq_change":         {"inputs": ["assets", "equity"],                           "func": lvs_020_financial_leverage_qoq_change},
    "lvs_021_short_term_debt_mix_qoq_change":        {"inputs": ["debtc", "debt"],                              "func": lvs_021_short_term_debt_mix_qoq_change},
    "lvs_022_debt_to_equity_yoy_change":             {"inputs": ["debt", "equity"],                              "func": lvs_022_debt_to_equity_yoy_change},
    "lvs_023_debt_to_assets_yoy_change":             {"inputs": ["debt", "assets"],                              "func": lvs_023_debt_to_assets_yoy_change},
    "lvs_024_net_debt_to_equity_yoy_change":         {"inputs": ["debt", "cashnequiv", "equity"],               "func": lvs_024_net_debt_to_equity_yoy_change},
    "lvs_025_debt_to_ebitda_yoy_change":             {"inputs": ["debt", "ebitda"],                             "func": lvs_025_debt_to_ebitda_yoy_change},
    "lvs_026_liabilities_to_equity_yoy_change":      {"inputs": ["liabilities", "equity"],                      "func": lvs_026_liabilities_to_equity_yoy_change},
    "lvs_027_net_debt_qoq_change":                   {"inputs": ["debt", "cashnequiv"],                         "func": lvs_027_net_debt_qoq_change},
    "lvs_028_net_debt_yoy_change":                   {"inputs": ["debt", "cashnequiv"],                         "func": lvs_028_net_debt_yoy_change},
    "lvs_029_debt_qoq_pct_change":                   {"inputs": ["debt"],                                       "func": lvs_029_debt_qoq_pct_change},
    "lvs_030_debt_yoy_pct_change":                   {"inputs": ["debt"],                                       "func": lvs_030_debt_yoy_pct_change},
    "lvs_031_debt_to_equity_above_4q_max":           {"inputs": ["debt", "equity"],                              "func": lvs_031_debt_to_equity_above_4q_max},
    "lvs_032_debt_to_equity_above_8q_max":           {"inputs": ["debt", "equity"],                              "func": lvs_032_debt_to_equity_above_8q_max},
    "lvs_033_debt_to_assets_above_4q_max":           {"inputs": ["debt", "assets"],                              "func": lvs_033_debt_to_assets_above_4q_max},
    "lvs_034_net_debt_to_ebitda_above_4q_max":       {"inputs": ["debt", "cashnequiv", "ebitda"],               "func": lvs_034_net_debt_to_ebitda_above_4q_max},
    "lvs_035_leverage_drawup_from_4q_min":           {"inputs": ["debt", "equity"],                              "func": lvs_035_leverage_drawup_from_4q_min},
    "lvs_036_leverage_drawup_from_8q_min":           {"inputs": ["debt", "equity"],                              "func": lvs_036_leverage_drawup_from_8q_min},
    "lvs_037_leverage_drawup_from_12q_min":          {"inputs": ["debt", "equity"],                              "func": lvs_037_leverage_drawup_from_12q_min},
    "lvs_038_debt_to_assets_above_8q_avg":           {"inputs": ["debt", "assets"],                              "func": lvs_038_debt_to_assets_above_8q_avg},
    "lvs_039_net_debt_drawup_from_4q_min":           {"inputs": ["debt", "cashnequiv"],                         "func": lvs_039_net_debt_drawup_from_4q_min},
    "lvs_040_net_debt_drawup_from_12q_min":          {"inputs": ["debt", "cashnequiv"],                         "func": lvs_040_net_debt_drawup_from_12q_min},
    "lvs_041_leverage_rank_4q":                      {"inputs": ["debt", "equity"],                              "func": lvs_041_leverage_rank_4q},
    "lvs_042_leverage_rank_8q":                      {"inputs": ["debt", "equity"],                              "func": lvs_042_leverage_rank_8q},
    "lvs_043_debt_to_assets_rank_4q":                {"inputs": ["debt", "assets"],                              "func": lvs_043_debt_to_assets_rank_4q},
    "lvs_044_net_debt_to_ebitda_rank_4q":            {"inputs": ["debt", "cashnequiv", "ebitda"],               "func": lvs_044_net_debt_to_ebitda_rank_4q},
    "lvs_045_leverage_expanding_pct_rank":           {"inputs": ["debt", "equity"],                              "func": lvs_045_leverage_expanding_pct_rank},
    "lvs_046_consecutive_rising_leverage_qtrs":      {"inputs": ["debt", "equity"],                              "func": lvs_046_consecutive_rising_leverage_qtrs},
    "lvs_047_consecutive_rising_debt_qtrs":          {"inputs": ["debt"],                                       "func": lvs_047_consecutive_rising_debt_qtrs},
    "lvs_048_rising_debt_falling_equity_flag":       {"inputs": ["debt", "equity"],                              "func": lvs_048_rising_debt_falling_equity_flag},
    "lvs_049_negative_equity_flag":                  {"inputs": ["equity"],                                     "func": lvs_049_negative_equity_flag},
    "lvs_050_negative_equity_quarters_1y":           {"inputs": ["equity"],                                     "func": lvs_050_negative_equity_quarters_1y},
    "lvs_051_negative_equity_quarters_2y":           {"inputs": ["equity"],                                     "func": lvs_051_negative_equity_quarters_2y},
    "lvs_052_equity_turned_negative_flag":           {"inputs": ["equity"],                                     "func": lvs_052_equity_turned_negative_flag},
    "lvs_053_leverage_above_2x_flag":                {"inputs": ["debt", "equity"],                              "func": lvs_053_leverage_above_2x_flag},
    "lvs_054_leverage_above_4x_flag":                {"inputs": ["debt", "equity"],                              "func": lvs_054_leverage_above_4x_flag},
    "lvs_055_net_debt_positive_flag":                {"inputs": ["debt", "cashnequiv"],                         "func": lvs_055_net_debt_positive_flag},
    "lvs_056_debt_to_assets_above_50pct_flag":       {"inputs": ["debt", "assets"],                              "func": lvs_056_debt_to_assets_above_50pct_flag},
    "lvs_057_debt_to_assets_above_75pct_flag":       {"inputs": ["debt", "assets"],                              "func": lvs_057_debt_to_assets_above_75pct_flag},
    "lvs_058_liabilities_to_assets_above_90pct_flag":{"inputs": ["liabilities", "assets"],                      "func": lvs_058_liabilities_to_assets_above_90pct_flag},
    "lvs_059_rising_leverage_fraction_1y":           {"inputs": ["debt", "equity"],                              "func": lvs_059_rising_leverage_fraction_1y},
    "lvs_060_rising_leverage_fraction_3y":           {"inputs": ["debt", "equity"],                              "func": lvs_060_rising_leverage_fraction_3y},
    "lvs_061_debt_to_equity_zscore_4q":              {"inputs": ["debt", "equity"],                              "func": lvs_061_debt_to_equity_zscore_4q},
    "lvs_062_debt_to_equity_zscore_8q":              {"inputs": ["debt", "equity"],                              "func": lvs_062_debt_to_equity_zscore_8q},
    "lvs_063_debt_to_assets_zscore_4q":              {"inputs": ["debt", "assets"],                              "func": lvs_063_debt_to_assets_zscore_4q},
    "lvs_064_net_debt_to_ebitda_zscore_4q":          {"inputs": ["debt", "cashnequiv", "ebitda"],               "func": lvs_064_net_debt_to_ebitda_zscore_4q},
    "lvs_065_financial_leverage_zscore_4q":          {"inputs": ["assets", "equity"],                           "func": lvs_065_financial_leverage_zscore_4q},
    "lvs_066_debt_to_equity_2y_change":              {"inputs": ["debt", "equity"],                              "func": lvs_066_debt_to_equity_2y_change},
    "lvs_067_debt_to_equity_3y_change":              {"inputs": ["debt", "equity"],                              "func": lvs_067_debt_to_equity_3y_change},
    "lvs_068_net_debt_2y_pct_change":                {"inputs": ["debt", "cashnequiv"],                         "func": lvs_068_net_debt_2y_pct_change},
    "lvs_069_net_debt_3y_pct_change":                {"inputs": ["debt", "cashnequiv"],                         "func": lvs_069_net_debt_3y_pct_change},
    "lvs_070_debt_growth_while_equity_shrinks_3y":   {"inputs": ["debt", "equity"],                              "func": lvs_070_debt_growth_while_equity_shrinks_3y},
    "lvs_071_leverage_ewm_deviation":                {"inputs": ["debt", "equity"],                              "func": lvs_071_leverage_ewm_deviation},
    "lvs_072_debt_to_assets_ewm_deviation":          {"inputs": ["debt", "assets"],                              "func": lvs_072_debt_to_assets_ewm_deviation},
    "lvs_073_leverage_range_position_8q":            {"inputs": ["debt", "equity"],                              "func": lvs_073_leverage_range_position_8q},
    "lvs_074_net_debt_to_ebitda_pct_rank_8q":        {"inputs": ["debt", "cashnequiv", "ebitda"],               "func": lvs_074_net_debt_to_ebitda_pct_rank_8q},
    "lvs_075_leverage_stress_composite":             {"inputs": ["debt", "equity", "assets", "ebitda"],         "func": lvs_075_leverage_stress_composite},
}
