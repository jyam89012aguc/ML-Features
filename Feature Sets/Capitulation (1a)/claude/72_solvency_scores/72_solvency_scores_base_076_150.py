"""
72_solvency_scores — Base Features 076-150
Domain: composite distress / solvency scores (extended ratios, trends, custom indices)
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

NOTE — Altman Z'' (book-value variant)
---------------------------------------
All Altman-related features in this file use the Z'' double-prime variant
(book equity substituted for market equity).  See file 001-075 header for
the full substitution rationale and model coefficients.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  All feature functions in this file look strictly backward.
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
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
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
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


def _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities):
    """Internal: compute Altman Z'' from component Series."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue):
    """Internal: compute Piotroski F-score (0-9) from component Series."""
    f1 = (netinc > 0).astype(float)
    f2 = (ncfo > 0).astype(float)
    roa = _safe_div(netinc, assets)
    f3 = (roa > roa.shift(_TD_QTR)).astype(float)
    f4 = (_safe_div(ncfo, assets) > roa).astype(float)
    lev = _safe_div(debt, assets)
    f5 = (lev < lev.shift(_TD_QTR)).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    f6 = (cr > cr.shift(_TD_QTR)).astype(float)
    f7 = (shareswa <= shareswa.shift(_TD_QTR)).astype(float)
    gm = _safe_div(gp, revenue)
    f8 = (gm > gm.shift(_TD_QTR)).astype(float)
    at_ = _safe_div(revenue, assets)
    f9 = (at_ > at_.shift(_TD_QTR)).astype(float)
    return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Extended Altman Z'' dynamics and weighted components ---

def slv_076_altman_z_weighted_x2(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' weighted X2 contribution: 3.26 * (retearn/assets)."""
    return 3.26 * _safe_div(retearn, assets)


def slv_077_altman_z_weighted_x3(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' weighted X3 contribution: 6.72 * (ebit/assets)."""
    return 6.72 * _safe_div(ebit, assets)


def slv_078_altman_z_weighted_x4(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Altman Z'' weighted X4 contribution: 1.05 * (equity/liabilities)."""
    return 1.05 * _safe_div(equity, liabilities)


def slv_079_altman_z_2y_avg(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Trailing 2-year (504-day) rolling mean of Altman Z'' score."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_mean(z, _TD_2Y)


def slv_080_altman_z_2y_change(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """2-year change in Altman Z'' score (504-day diff)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z - z.shift(_TD_2Y)


def slv_081_altman_z_3y_change(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """3-year change in Altman Z'' score (756-day diff)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z - z.shift(_TD_3Y)


def slv_082_altman_z_pct_change_yoy(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """YoY percent change in Altman Z'' score."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    prior = z.shift(_TD_YEAR)
    return _safe_div_abs(z - prior, prior)


def slv_083_altman_z_min_1y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Trailing 1-year minimum of Altman Z'' (worst point in past year)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_min(z, _TD_YEAR)


def slv_084_altman_z_min_3y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Trailing 3-year minimum of Altman Z'' (worst point in past 3 years)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_min(z, _TD_3Y)


def slv_085_altman_z_pct_rank_4q(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Altman Z'' within trailing 4-quarter (252-day) window."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_rank_pct(z, _TD_YEAR)


def slv_086_altman_z_pct_rank_12q(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Altman Z'' within trailing 12-quarter (756-day) window."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_rank_pct(z, _TD_3Y)


def slv_087_altman_z_ewm_span1y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """EWM (span=252) of Altman Z'' — smooth trend signal."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _ewm_mean(z, _TD_YEAR)


def slv_088_altman_z_vs_ewm_deviation(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Altman Z'' minus its EWM (span=252): current deviation from smoothed trend."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z - _ewm_mean(z, _TD_YEAR)


def slv_089_altman_z_consecutive_decline_days(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Consecutive daily steps Altman Z'' has been declining (QoQ diff < 0). Resets at improvement."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    declining = (z < z.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(declining), dtype=float)
    arr = declining.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=z.index)


def slv_090_altman_z_below_distress_fraction_1y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Fraction of trailing 1-year window where Altman Z'' < 1.1 (distress zone)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    below = (z < 1.1).astype(float)
    return _rolling_mean(below, _TD_YEAR)


# --- Group G (091-105): Extended Piotroski dynamics ---

def slv_091_piotroski_fscore_drawdown_from_1y_peak(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Piotroski F-score drawdown from its trailing 1-year (252-day) peak."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    peak  = _rolling_max(score, _TD_YEAR)
    return score - peak


def slv_092_piotroski_fscore_drawdown_from_expanding_peak(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Piotroski F-score drawdown from all-history expanding peak."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    peak  = score.expanding(min_periods=1).max()
    return score - peak


def slv_093_piotroski_fscore_min_1y(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Trailing 1-year minimum Piotroski F-score."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    return _rolling_min(score, _TD_YEAR)


def slv_094_piotroski_fscore_ewm(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """EWM (span=252) of Piotroski F-score — smooth trend signal."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    return _ewm_mean(score, _TD_YEAR)


def slv_095_piotroski_fscore_zscore_4q(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Z-score of Piotroski F-score within trailing 4-quarter (252-day) window."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    return _zscore_rolling(score, _TD_YEAR)


def slv_096_piotroski_fscore_pct_rank_4q(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Percentile rank of Piotroski F-score within trailing 4-quarter window."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    return _rolling_rank_pct(score, _TD_YEAR)


def slv_097_piotroski_distress_fraction_2y(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Fraction of trailing 2-year window where Piotroski F-score <= 2."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    low = (score <= 2).astype(float)
    return _rolling_mean(low, _TD_2Y)


def slv_098_piotroski_fscore_distance_to_low_2y(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """
    Distance of current Piotroski F-score from its trailing 2-year (504-day) minimum.
    Zero means the score is at its 2-year low; higher values = further from the nadir.
    """
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    low_2y = _rolling_min(score, _TD_2Y)
    return score - low_2y


def slv_099_altman_z_distance_to_low_2y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """
    Distance of current Altman Z'' score from its trailing 2-year (504-day) minimum.
    Zero means the score is at its 2-year low; higher values = further from the nadir.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    low_2y = _rolling_min(z, _TD_2Y)
    return z - low_2y


def slv_100_zmijewski_score_yoy_change(
    netinc: pd.Series, assets: pd.Series, liabilities: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """YoY change in Zmijewski-style score (positive = deteriorating)."""
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    z = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    return z - z.shift(_TD_YEAR)


def slv_101_zmijewski_distress_flag(
    netinc: pd.Series, assets: pd.Series, liabilities: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """Binary: 1 if Zmijewski-style score > 0 (distress-leaning), else 0."""
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    z = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    return (z > 0).astype(float)


def slv_102_zmijewski_score_drawdown_from_peak(
    netinc: pd.Series, assets: pd.Series, liabilities: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """Zmijewski-style score vs its trailing 1-year minimum (best health = min for this score)."""
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    z = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    best = _rolling_min(z, _TD_YEAR)
    return z - best


def slv_103_springate_score_yoy_change(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series,
    ebt: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """YoY change in Springate-style score (decline = deteriorating)."""
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return s - s.shift(_TD_YEAR)


def slv_104_springate_score_drawdown_from_1y_peak(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series,
    ebt: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Springate-style score vs its trailing 1-year peak (drawdown)."""
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    peak = _rolling_max(s, _TD_YEAR)
    return s - peak


def slv_105_springate_score_zscore_4q(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series,
    ebt: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Z-score of Springate-style score within trailing 4-quarter window."""
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return _zscore_rolling(s, _TD_YEAR)


# --- Group H (106-120): Additional single-ratio distress signals ---

def slv_106_net_debt_to_assets(debt: pd.Series, cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Net debt (debt - cash) / assets: leverage net of cash holdings."""
    return _safe_div(debt - cashnequiv, assets)


def slv_107_net_debt_to_ebitda(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net debt / EBITDA: how many years of EBITDA to repay net debt."""
    return _safe_div(debt - cashnequiv, ebitda.abs().replace(0, np.nan))


def slv_108_fcf_to_debt_ratio(fcf: pd.Series, debt: pd.Series) -> pd.Series:
    """Free cash flow / total debt: FCF-based debt coverage."""
    return _safe_div(fcf, debt.abs().replace(0, np.nan))


def slv_109_fcf_negative_flag(fcf: pd.Series) -> pd.Series:
    """Binary: 1 if free cash flow < 0, else 0."""
    return (fcf < 0).astype(float)


def slv_110_ncfi_negative_flag(ncfi: pd.Series) -> pd.Series:
    """Binary: 1 if investing cash flow < 0 (net cash consumption), else 0."""
    return (ncfi < 0).astype(float)


def slv_111_ncff_negative_flag(ncff: pd.Series) -> pd.Series:
    """Binary: 1 if financing cash flow < 0 (net repayments/buybacks), else 0."""
    return (ncff < 0).astype(float)


def slv_112_ncf_negative_flag(ncf: pd.Series) -> pd.Series:
    """Binary: 1 if total net cash flow < 0, else 0."""
    return (ncf < 0).astype(float)


def slv_113_debt_to_invcap_ratio(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    """Debt / invested capital: proportion of invested capital financed by debt."""
    return _safe_div(debt, invcap.abs().replace(0, np.nan))


def slv_114_tangibles_to_liabilities(tangibles: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Tangible assets / total liabilities: tangible coverage of obligations."""
    return _safe_div(tangibles, liabilities)


def slv_115_intangibles_to_assets(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Intangibles / total assets: asset quality / goodwill concentration risk."""
    return _safe_div(intangibles, assets)


def slv_116_ppnenet_to_assets(ppnenet: pd.Series, assets: pd.Series) -> pd.Series:
    """Net PP&E / total assets: tangible fixed asset intensity."""
    return _safe_div(ppnenet, assets)


def slv_117_debtc_to_debt_ratio(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Current debt / total debt: short-term debt concentration (refinancing risk)."""
    return _safe_div(debtc, debt.abs().replace(0, np.nan))


def slv_118_ncfdebt_to_debt_ratio(ncfdebt: pd.Series, debt: pd.Series) -> pd.Series:
    """Net change in debt (ncfdebt) / total debt: pace of debt accumulation or paydown."""
    return _safe_div(ncfdebt, debt.abs().replace(0, np.nan))


def slv_119_capex_to_assets_ratio(capex: pd.Series, assets: pd.Series) -> pd.Series:
    """Capex / total assets: investment intensity relative to asset base."""
    return _safe_div(capex.abs(), assets)


def slv_120_sbcomp_to_assets_ratio(sbcomp: pd.Series, assets: pd.Series) -> pd.Series:
    """Stock-based compensation / assets: SBC dilution pressure relative to asset base."""
    return _safe_div(sbcomp.abs(), assets)


# --- Group I (121-135): Multi-score composite signals and divergence ---

def slv_121_altman_piotroski_combined_score(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """
    Combined normalized solvency score: z-score of Altman Z'' + z-score of
    Piotroski F-score (both on trailing 4Q), averaged. Higher = healthier.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    zz = _zscore_rolling(z, _TD_YEAR)
    zf = _zscore_rolling(f, _TD_YEAR)
    return (zz + zf) / 2.0


def slv_122_altman_piotroski_divergence(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """
    Divergence between normalized Altman Z'' and Piotroski F-score:
    z-score(Z'') minus z-score(F). Captures model disagreement.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    zz = _zscore_rolling(z, _TD_YEAR)
    zf = _zscore_rolling(f, _TD_YEAR)
    return zz - zf


def slv_123_three_score_average(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series, liabilitiesnc: pd.Series,
) -> pd.Series:
    """
    Average z-score across three models: Altman Z'', Piotroski F, and Springate.
    All normalized to 4Q z-score before averaging.
    """
    z_alt = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f_pio = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    ebt_proxy = ebit - _safe_div(debt * 0.05, assets) * assets
    c = _safe_div(ebt_proxy, liabilitiesc)
    d = _safe_div(revenue, assets)
    spr = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    zz1 = _zscore_rolling(z_alt, _TD_YEAR)
    zz2 = _zscore_rolling(f_pio, _TD_YEAR)
    zz3 = _zscore_rolling(spr, _TD_YEAR)
    return (zz1 + zz2 + zz3) / 3.0


def slv_124_distress_signal_breadth(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, liabilitiesc: pd.Series,
    ebt: pd.Series, revenue: pd.Series, debt: pd.Series,
    assetsc: pd.Series, shareswa: pd.Series, gp: pd.Series,
) -> pd.Series:
    """
    Count of distress signals active simultaneously (0-5):
    (1) Altman Z'' < 1.1, (2) Piotroski F <= 2, (3) negative equity,
    (4) current ratio < 1, (5) interest-coverage proxy ebit/assets < 0.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    s1 = (z < 1.1).astype(float)
    s2 = (f <= 2).astype(float)
    s3 = (equity < 0).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    s4 = (cr < 1.0).astype(float)
    roa_ratio = _safe_div(ebit, assets)
    s5 = (roa_ratio < 0).astype(float)
    return s1 + s2 + s3 + s4 + s5


def slv_125_roa_trailing_4q_avg(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Trailing 4-quarter (252-day) average ROA (netinc/assets)."""
    return _rolling_mean(_safe_div(netinc, assets), _TD_YEAR)


def slv_126_roa_zscore_4q(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of ROA (netinc/assets) within trailing 4-quarter window."""
    return _zscore_rolling(_safe_div(netinc, assets), _TD_YEAR)


def slv_127_leverage_zscore_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of total leverage (liabilities/assets) within trailing 4Q window."""
    return _zscore_rolling(_safe_div(liabilities, assets), _TD_YEAR)


def slv_128_current_ratio_zscore_4q(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current ratio within trailing 4Q window."""
    return _zscore_rolling(_safe_div(assetsc, liabilitiesc), _TD_YEAR)


def slv_129_interest_coverage_zscore_4q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of interest coverage ratio within trailing 4Q window."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return _zscore_rolling(cov, _TD_YEAR)


def slv_130_debt_to_equity_zscore_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of debt/equity within trailing 4Q window."""
    return _zscore_rolling(_safe_div(debt, equity), _TD_YEAR)


def slv_131_composite_leverage_distress_index(
    debt: pd.Series, assets: pd.Series, equity: pd.Series, ebit: pd.Series,
    intexp: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """
    Custom leverage distress index: equally weighted sum of three z-scored
    leverage indicators (debt/assets, debt/equity, liabilities/assets).
    Higher = more leveraged / distressed.
    """
    r1 = _safe_div(debt, assets)
    r2 = _safe_div(debt, equity)
    r3 = _safe_div(liabilities, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


def slv_132_composite_liquidity_health_index(
    assetsc: pd.Series, liabilitiesc: pd.Series,
    ncfo: pd.Series, assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """
    Custom liquidity health index: equally weighted sum of three z-scored
    liquidity ratios (current ratio, cash/liabilities, ncfo/assets).
    Higher = more liquid / healthier.
    """
    r1 = _safe_div(assetsc, liabilitiesc)
    r2 = _safe_div(cashnequiv, liabilities)
    r3 = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


def slv_133_composite_profitability_index(
    netinc: pd.Series, assets: pd.Series, ebit: pd.Series,
    gp: pd.Series, revenue: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """
    Custom profitability composite: z-score avg of ROA, EBIT/assets,
    gross margin, and CFO/assets. Higher = more profitable.
    """
    r1 = _safe_div(netinc, assets)
    r2 = _safe_div(ebit, assets)
    r3 = _safe_div(gp, revenue)
    r4 = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    z4 = _zscore_rolling(r4, _TD_YEAR)
    return (z1 + z2 + z3 + z4) / 4.0


def slv_134_solvency_momentum_score(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """
    Solvency momentum: QoQ change in Altman Z'' z-score + QoQ change in
    Piotroski F z-score, averaged. Positive = improving solvency trend.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    zz = _zscore_rolling(z, _TD_YEAR)
    zf = _zscore_rolling(f, _TD_YEAR)
    d_zz = zz - zz.shift(_TD_QTR)
    d_zf = zf - zf.shift(_TD_QTR)
    return (d_zz + d_zf) / 2.0


def slv_135_triple_distress_flag(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, liabilitiesc: pd.Series,
    ebt: pd.Series, revenue: pd.Series, debt: pd.Series,
    assetsc: pd.Series, shareswa: pd.Series, gp: pd.Series,
) -> pd.Series:
    """
    Binary: 1 if all three models flag distress simultaneously:
    Altman Z'' < 1.1, Piotroski F <= 2, AND Springate < 0.862.
    Maximum consensus distress signal.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    spr = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return ((z < 1.1) & (f <= 2) & (spr < 0.862)).astype(float)


# --- Group J (136-150): Long-horizon / persistence distress signals ---

def slv_136_altman_z_below_distress_fraction_3y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Fraction of trailing 3-year window where Altman Z'' < 1.1 (distress zone)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    below = (z < 1.1).astype(float)
    return _rolling_mean(below, _TD_3Y)


def slv_137_piotroski_distress_fraction_3y(
    netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Fraction of trailing 3-year window where Piotroski F-score <= 2."""
    score = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    low = (score <= 2).astype(float)
    return _rolling_mean(low, _TD_3Y)


def slv_138_negative_equity_fraction_3y(equity: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where equity was negative."""
    neg = (equity < 0).astype(float)
    return _rolling_mean(neg, _TD_3Y)


def slv_139_negative_ncfo_fraction_3y(ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where operating cash flow was negative."""
    neg = (ncfo < 0).astype(float)
    return _rolling_mean(neg, _TD_3Y)


def slv_140_current_ratio_below1_fraction_3y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where current ratio was below 1.0."""
    cr = _safe_div(assetsc, liabilitiesc)
    below = (cr < 1.0).astype(float)
    return _rolling_mean(below, _TD_3Y)


def slv_141_roa_negative_fraction_3y(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Fraction of trailing 3-year window where ROA (netinc/assets) was negative."""
    roa = _safe_div(netinc, assets)
    neg = (roa < 0).astype(float)
    return _rolling_mean(neg, _TD_3Y)


def slv_142_altman_z_expanding_min(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """All-history expanding minimum of Altman Z'' score."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z.expanding(min_periods=1).min()


def slv_143_altman_z_vs_expanding_min(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Altman Z'' vs its all-history expanding minimum (proximity to record low)."""
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z - z.expanding(min_periods=1).min()


def slv_144_composite_distress_index_3y_avg(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """Trailing 3-year rolling mean of the custom composite distress index."""
    r1 = _safe_div(workingcapital, assets)
    r2 = _safe_div(retearn, assets)
    r3 = _safe_div(ebit, assets)
    r4 = _safe_div(equity, liabilities)
    r5 = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    z4 = _zscore_rolling(r4, _TD_YEAR)
    z5 = _zscore_rolling(r5, _TD_YEAR)
    composite = (z1 + z2 + z3 + z4 + z5) / 5.0
    return _rolling_mean(composite, _TD_3Y)


def slv_145_composite_distress_qoq_change(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """QoQ change in the custom composite distress index."""
    r1 = _safe_div(workingcapital, assets)
    r2 = _safe_div(retearn, assets)
    r3 = _safe_div(ebit, assets)
    r4 = _safe_div(equity, liabilities)
    r5 = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    z4 = _zscore_rolling(r4, _TD_YEAR)
    z5 = _zscore_rolling(r5, _TD_YEAR)
    composite = (z1 + z2 + z3 + z4 + z5) / 5.0
    return composite - composite.shift(_TD_QTR)


def slv_146_composite_distress_drawdown_expanding_peak(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """Custom composite distress index vs its all-history expanding peak."""
    r1 = _safe_div(workingcapital, assets)
    r2 = _safe_div(retearn, assets)
    r3 = _safe_div(ebit, assets)
    r4 = _safe_div(equity, liabilities)
    r5 = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(r1, _TD_YEAR)
    z2 = _zscore_rolling(r2, _TD_YEAR)
    z3 = _zscore_rolling(r3, _TD_YEAR)
    z4 = _zscore_rolling(r4, _TD_YEAR)
    z5 = _zscore_rolling(r5, _TD_YEAR)
    composite = (z1 + z2 + z3 + z4 + z5) / 5.0
    peak = composite.expanding(min_periods=1).max()
    return composite - peak


def slv_147_solvency_stress_intensity(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, liabilitiesc: pd.Series,
    ebt: pd.Series, revenue: pd.Series, debt: pd.Series,
    assetsc: pd.Series, shareswa: pd.Series, gp: pd.Series,
) -> pd.Series:
    """
    Solvency stress intensity: sum of all individual distress flags:
    negative equity, negative ROA, current ratio < 1, Altman distress,
    Springate distress, Zmijewski distress, Piotroski low, negative NCFo.
    Range 0-8; higher = more concurrent stress signals.
    """
    s1 = (equity < 0).astype(float)
    roa = _safe_div(netinc, assets)
    s2 = (roa < 0).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    s3 = (cr < 1.0).astype(float)
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    s4 = (z < 1.1).astype(float)
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    spr = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    s5 = (spr < 0.862).astype(float)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    zmi = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    s6 = (zmi > 0).astype(float)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    s7 = (f <= 2).astype(float)
    s8 = (ncfo < 0).astype(float)
    return s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8


def slv_148_solvency_stress_intensity_trailing_1y_avg(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, liabilitiesc: pd.Series,
    ebt: pd.Series, revenue: pd.Series, debt: pd.Series,
    assetsc: pd.Series, shareswa: pd.Series, gp: pd.Series,
) -> pd.Series:
    """Trailing 1-year rolling mean of the solvency stress intensity score."""
    s1 = (equity < 0).astype(float)
    roa = _safe_div(netinc, assets)
    s2 = (roa < 0).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    s3 = (cr < 1.0).astype(float)
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    s4 = (z < 1.1).astype(float)
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    spr = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    s5 = (spr < 0.862).astype(float)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    zmi = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    s6 = (zmi > 0).astype(float)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    s7 = (f <= 2).astype(float)
    s8 = (ncfo < 0).astype(float)
    intensity = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
    return _rolling_mean(intensity, _TD_YEAR)


def slv_149_solvency_recovery_flag(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """
    Binary: 1 if Altman Z'' improved from distress (was < 1.1 one quarter ago,
    now >= 1.1) OR Piotroski improved from distress (was <= 2, now > 2).
    Early recovery signal.
    """
    z = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    alt_recovery = ((z.shift(_TD_QTR) < 1.1) & (z >= 1.1)).astype(float)
    pio_recovery = ((f.shift(_TD_QTR) <= 2) & (f > 2)).astype(float)
    return ((alt_recovery + pio_recovery) > 0).astype(float)


def slv_150_solvency_grand_composite(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series, debt: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series, shareswa: pd.Series,
    gp: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """
    Grand solvency composite: z-score average of five normalized signals:
    Altman Z'' (4Q z-score), Piotroski F (4Q z-score), ROA (4Q z-score),
    current ratio (4Q z-score), NCFo/assets (4Q z-score).
    Higher = stronger solvency position. The definitive single-number summary.
    """
    z_alt = _altman_z_pp(workingcapital, assets, retearn, ebit, equity, liabilities)
    f_pio = _piotroski_score(netinc, ncfo, assets, debt, assetsc, liabilitiesc, shareswa, gp, revenue)
    roa   = _safe_div(netinc, assets)
    cr    = _safe_div(assetsc, liabilitiesc)
    cfo_r = _safe_div(ncfo, assets)
    z1 = _zscore_rolling(z_alt, _TD_YEAR)
    z2 = _zscore_rolling(f_pio, _TD_YEAR)
    z3 = _zscore_rolling(roa, _TD_YEAR)
    z4 = _zscore_rolling(cr, _TD_YEAR)
    z5 = _zscore_rolling(cfo_r, _TD_YEAR)
    return (z1 + z2 + z3 + z4 + z5) / 5.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

SOLVENCY_SCORES_REGISTRY_076_150 = {
    "slv_076_altman_z_weighted_x2":                        {"inputs": ["retearn", "assets"],                                                                                                                "func": slv_076_altman_z_weighted_x2},
    "slv_077_altman_z_weighted_x3":                        {"inputs": ["ebit", "assets"],                                                                                                                  "func": slv_077_altman_z_weighted_x3},
    "slv_078_altman_z_weighted_x4":                        {"inputs": ["equity", "liabilities"],                                                                                                           "func": slv_078_altman_z_weighted_x4},
    "slv_079_altman_z_2y_avg":                             {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_079_altman_z_2y_avg},
    "slv_080_altman_z_2y_change":                          {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_080_altman_z_2y_change},
    "slv_081_altman_z_3y_change":                          {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_081_altman_z_3y_change},
    "slv_082_altman_z_pct_change_yoy":                     {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_082_altman_z_pct_change_yoy},
    "slv_083_altman_z_min_1y":                             {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_083_altman_z_min_1y},
    "slv_084_altman_z_min_3y":                             {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_084_altman_z_min_3y},
    "slv_085_altman_z_pct_rank_4q":                        {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_085_altman_z_pct_rank_4q},
    "slv_086_altman_z_pct_rank_12q":                       {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_086_altman_z_pct_rank_12q},
    "slv_087_altman_z_ewm_span1y":                         {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_087_altman_z_ewm_span1y},
    "slv_088_altman_z_vs_ewm_deviation":                   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_088_altman_z_vs_ewm_deviation},
    "slv_089_altman_z_consecutive_decline_days":           {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_089_altman_z_consecutive_decline_days},
    "slv_090_altman_z_below_distress_fraction_1y":         {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_090_altman_z_below_distress_fraction_1y},
    "slv_091_piotroski_fscore_drawdown_from_1y_peak":      {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_091_piotroski_fscore_drawdown_from_1y_peak},
    "slv_092_piotroski_fscore_drawdown_from_expanding_peak": {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                    "func": slv_092_piotroski_fscore_drawdown_from_expanding_peak},
    "slv_093_piotroski_fscore_min_1y":                     {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_093_piotroski_fscore_min_1y},
    "slv_094_piotroski_fscore_ewm":                        {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_094_piotroski_fscore_ewm},
    "slv_095_piotroski_fscore_zscore_4q":                  {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_095_piotroski_fscore_zscore_4q},
    "slv_096_piotroski_fscore_pct_rank_4q":                {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_096_piotroski_fscore_pct_rank_4q},
    "slv_097_piotroski_distress_fraction_2y":              {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_097_piotroski_distress_fraction_2y},
    "slv_098_piotroski_fscore_distance_to_low_2y":         {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_098_piotroski_fscore_distance_to_low_2y},
    "slv_099_altman_z_distance_to_low_2y":                 {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_099_altman_z_distance_to_low_2y},
    "slv_100_zmijewski_score_yoy_change":                  {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                                      "func": slv_100_zmijewski_score_yoy_change},
    "slv_101_zmijewski_distress_flag":                     {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                                      "func": slv_101_zmijewski_distress_flag},
    "slv_102_zmijewski_score_drawdown_from_peak":          {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                                      "func": slv_102_zmijewski_score_drawdown_from_peak},
    "slv_103_springate_score_yoy_change":                  {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                              "func": slv_103_springate_score_yoy_change},
    "slv_104_springate_score_drawdown_from_1y_peak":       {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                              "func": slv_104_springate_score_drawdown_from_1y_peak},
    "slv_105_springate_score_zscore_4q":                   {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                              "func": slv_105_springate_score_zscore_4q},
    "slv_106_net_debt_to_assets":                          {"inputs": ["debt", "cashnequiv", "assets"],                                                                                                    "func": slv_106_net_debt_to_assets},
    "slv_107_net_debt_to_ebitda":                          {"inputs": ["debt", "cashnequiv", "ebitda"],                                                                                                    "func": slv_107_net_debt_to_ebitda},
    "slv_108_fcf_to_debt_ratio":                           {"inputs": ["fcf", "debt"],                                                                                                                     "func": slv_108_fcf_to_debt_ratio},
    "slv_109_fcf_negative_flag":                           {"inputs": ["fcf"],                                                                                                                             "func": slv_109_fcf_negative_flag},
    "slv_110_ncfi_negative_flag":                          {"inputs": ["ncfi"],                                                                                                                            "func": slv_110_ncfi_negative_flag},
    "slv_111_ncff_negative_flag":                          {"inputs": ["ncff"],                                                                                                                            "func": slv_111_ncff_negative_flag},
    "slv_112_ncf_negative_flag":                           {"inputs": ["ncf"],                                                                                                                             "func": slv_112_ncf_negative_flag},
    "slv_113_debt_to_invcap_ratio":                        {"inputs": ["debt", "invcap"],                                                                                                                  "func": slv_113_debt_to_invcap_ratio},
    "slv_114_tangibles_to_liabilities":                    {"inputs": ["tangibles", "liabilities"],                                                                                                        "func": slv_114_tangibles_to_liabilities},
    "slv_115_intangibles_to_assets":                       {"inputs": ["intangibles", "assets"],                                                                                                           "func": slv_115_intangibles_to_assets},
    "slv_116_ppnenet_to_assets":                           {"inputs": ["ppnenet", "assets"],                                                                                                               "func": slv_116_ppnenet_to_assets},
    "slv_117_debtc_to_debt_ratio":                         {"inputs": ["debtc", "debt"],                                                                                                                   "func": slv_117_debtc_to_debt_ratio},
    "slv_118_ncfdebt_to_debt_ratio":                       {"inputs": ["ncfdebt", "debt"],                                                                                                                 "func": slv_118_ncfdebt_to_debt_ratio},
    "slv_119_capex_to_assets_ratio":                       {"inputs": ["capex", "assets"],                                                                                                                 "func": slv_119_capex_to_assets_ratio},
    "slv_120_sbcomp_to_assets_ratio":                      {"inputs": ["sbcomp", "assets"],                                                                                                                "func": slv_120_sbcomp_to_assets_ratio},
    "slv_121_altman_piotroski_combined_score":             {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"], "func": slv_121_altman_piotroski_combined_score},
    "slv_122_altman_piotroski_divergence":                 {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"], "func": slv_122_altman_piotroski_divergence},
    "slv_123_three_score_average":                         {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue", "liabilitiesnc"], "func": slv_123_three_score_average},
    "slv_124_distress_signal_breadth":                     {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue", "debt", "assetsc", "shareswa", "gp"], "func": slv_124_distress_signal_breadth},
    "slv_125_roa_trailing_4q_avg":                         {"inputs": ["netinc", "assets"],                                                                                                                "func": slv_125_roa_trailing_4q_avg},
    "slv_126_roa_zscore_4q":                               {"inputs": ["netinc", "assets"],                                                                                                                "func": slv_126_roa_zscore_4q},
    "slv_127_leverage_zscore_4q":                          {"inputs": ["liabilities", "assets"],                                                                                                           "func": slv_127_leverage_zscore_4q},
    "slv_128_current_ratio_zscore_4q":                     {"inputs": ["assetsc", "liabilitiesc"],                                                                                                         "func": slv_128_current_ratio_zscore_4q},
    "slv_129_interest_coverage_zscore_4q":                 {"inputs": ["ebit", "intexp"],                                                                                                                  "func": slv_129_interest_coverage_zscore_4q},
    "slv_130_debt_to_equity_zscore_4q":                    {"inputs": ["debt", "equity"],                                                                                                                  "func": slv_130_debt_to_equity_zscore_4q},
    "slv_131_composite_leverage_distress_index":           {"inputs": ["debt", "assets", "equity", "ebit", "intexp", "liabilities"],                                                                       "func": slv_131_composite_leverage_distress_index},
    "slv_132_composite_liquidity_health_index":            {"inputs": ["assetsc", "liabilitiesc", "ncfo", "assets", "cashnequiv", "liabilities"],                                                          "func": slv_132_composite_liquidity_health_index},
    "slv_133_composite_profitability_index":               {"inputs": ["netinc", "assets", "ebit", "gp", "revenue", "ncfo"],                                                                               "func": slv_133_composite_profitability_index},
    "slv_134_solvency_momentum_score":                     {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"], "func": slv_134_solvency_momentum_score},
    "slv_135_triple_distress_flag":                        {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue", "debt", "assetsc", "shareswa", "gp"], "func": slv_135_triple_distress_flag},
    "slv_136_altman_z_below_distress_fraction_3y":         {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_136_altman_z_below_distress_fraction_3y},
    "slv_137_piotroski_distress_fraction_3y":              {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                                        "func": slv_137_piotroski_distress_fraction_3y},
    "slv_138_negative_equity_fraction_3y":                 {"inputs": ["equity"],                                                                                                                          "func": slv_138_negative_equity_fraction_3y},
    "slv_139_negative_ncfo_fraction_3y":                   {"inputs": ["ncfo"],                                                                                                                            "func": slv_139_negative_ncfo_fraction_3y},
    "slv_140_current_ratio_below1_fraction_3y":            {"inputs": ["assetsc", "liabilitiesc"],                                                                                                         "func": slv_140_current_ratio_below1_fraction_3y},
    "slv_141_roa_negative_fraction_3y":                    {"inputs": ["netinc", "assets"],                                                                                                                "func": slv_141_roa_negative_fraction_3y},
    "slv_142_altman_z_expanding_min":                      {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_142_altman_z_expanding_min},
    "slv_143_altman_z_vs_expanding_min":                   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                            "func": slv_143_altman_z_vs_expanding_min},
    "slv_144_composite_distress_index_3y_avg":             {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                                          "func": slv_144_composite_distress_index_3y_avg},
    "slv_145_composite_distress_qoq_change":               {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                                          "func": slv_145_composite_distress_qoq_change},
    "slv_146_composite_distress_drawdown_expanding_peak":  {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                                          "func": slv_146_composite_distress_drawdown_expanding_peak},
    "slv_147_solvency_stress_intensity":                   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue", "debt", "assetsc", "shareswa", "gp"], "func": slv_147_solvency_stress_intensity},
    "slv_148_solvency_stress_intensity_trailing_1y_avg":   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue", "debt", "assetsc", "shareswa", "gp"], "func": slv_148_solvency_stress_intensity_trailing_1y_avg},
    "slv_149_solvency_recovery_flag":                      {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],        "func": slv_149_solvency_recovery_flag},
    "slv_150_solvency_grand_composite":                    {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],        "func": slv_150_solvency_grand_composite},
}
