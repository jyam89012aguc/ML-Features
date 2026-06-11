"""
72_solvency_scores — Base Features 001-075
Domain: composite distress / solvency scores (Altman Z'', Piotroski F, components)
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

NOTE — Altman Z'' (book-value variant)
---------------------------------------
The classic Altman Z-score uses MARKET value of equity in ratio X4
(market equity / total liabilities).  Because market price data is not
available in this SF1-only pipeline, this file implements the Altman Z''
(double-prime) model which substitutes BOOK VALUE of equity for market value.
The Z'' model was developed by Altman for private and non-publicly-traded firms
and uses the same five ratios with re-estimated coefficients:
  Z'' = 6.56*X1 + 3.26*X2 + 6.72*X3 + 1.05*X4
  X1 = workingcapital / assets
  X2 = retearn / assets
  X3 = ebit / assets
  X4 = equity (book) / liabilities
This substitution is fully documented here; all downstream uses of slv_*_altman_*
features reflect the Z'' book-value model, NOT the original Z-score.

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

# --- Group A (001-010): Altman Z'' components (book-equity variant) ---

def slv_001_altman_x1_wc_to_assets(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' component X1: workingcapital / assets (liquidity ratio)."""
    return _safe_div(workingcapital, assets)


def slv_002_altman_x2_retearn_to_assets(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' component X2: retained earnings / assets (cumulative profitability)."""
    return _safe_div(retearn, assets)


def slv_003_altman_x3_ebit_to_assets(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' component X3: ebit / assets (operating return on assets)."""
    return _safe_div(ebit, assets)


def slv_004_altman_x4_equity_to_liabilities(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Altman Z'' component X4: book equity / total liabilities (book leverage buffer)."""
    return _safe_div(equity, liabilities)


def slv_005_altman_x5_revenue_to_assets(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' component X5: revenue / assets (asset turnover efficiency)."""
    return _safe_div(revenue, assets)


def slv_006_altman_z_double_prime(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """
    Assembled Altman Z'' score (book-equity variant).
    Z'' = 6.56*X1 + 3.26*X2 + 6.72*X3 + 1.05*X4
    Zones: Z'' > 2.6 = safe, 1.1-2.6 = grey, < 1.1 = distress.
    Note: X5 (revenue/assets) is excluded from Z'' per Altman (1993) revision;
    included as a separate feature (slv_005).
    """
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


def slv_007_altman_z_safe_zone_flag(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Binary: 1 if Z'' >= 2.6 (safe zone), else 0."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return (z >= 2.6).astype(float)


def slv_008_altman_z_distress_zone_flag(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Binary: 1 if Z'' < 1.1 (distress zone), else 0."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return (z < 1.1).astype(float)


def slv_009_altman_z_grey_zone_flag(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Binary: 1 if Z'' between 1.1 and 2.6 (grey zone), else 0."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return ((z >= 1.1) & (z < 2.6)).astype(float)


def slv_010_altman_z_weighted_x1(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Altman Z'' weighted X1 contribution: 6.56 * (workingcapital/assets)."""
    return 6.56 * _safe_div(workingcapital, assets)


# --- Group B (011-025): Piotroski F-score signals ---

def slv_011_piotroski_f1_positive_netinc(netinc: pd.Series) -> pd.Series:
    """Piotroski signal F1: 1 if net income > 0, else 0."""
    return (netinc > 0).astype(float)


def slv_012_piotroski_f2_positive_ncfo(ncfo: pd.Series) -> pd.Series:
    """Piotroski signal F2: 1 if operating cash flow > 0, else 0."""
    return (ncfo > 0).astype(float)


def slv_013_piotroski_f3_rising_roa(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Piotroski signal F3: 1 if ROA (netinc/assets) improved QoQ, else 0."""
    roa = _safe_div(netinc, assets)
    return (roa > roa.shift(_TD_QTR)).astype(float)


def slv_014_piotroski_f4_accrual_quality(ncfo: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Piotroski signal F4: 1 if ncfo/assets > netinc/assets (cash earnings beat accrual)."""
    cfo_ratio = _safe_div(ncfo, assets)
    ni_ratio  = _safe_div(netinc, assets)
    return (cfo_ratio > ni_ratio).astype(float)


def slv_015_piotroski_f5_falling_leverage(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Piotroski signal F5: 1 if debt/assets ratio fell QoQ (leverage declining), else 0."""
    lev = _safe_div(debt, assets)
    return (lev < lev.shift(_TD_QTR)).astype(float)


def slv_016_piotroski_f6_rising_current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Piotroski signal F6: 1 if current ratio (assetsc/liabilitiesc) rose QoQ, else 0."""
    cr = _safe_div(assetsc, liabilitiesc)
    return (cr > cr.shift(_TD_QTR)).astype(float)


def slv_017_piotroski_f7_no_dilution(shareswa: pd.Series) -> pd.Series:
    """Piotroski signal F7: 1 if shares outstanding did NOT increase QoQ (no dilution)."""
    return (shareswa <= shareswa.shift(_TD_QTR)).astype(float)


def slv_018_piotroski_f8_rising_gross_margin(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Piotroski signal F8: 1 if gross margin (gp/revenue) improved QoQ, else 0."""
    gm = _safe_div(gp, revenue)
    return (gm > gm.shift(_TD_QTR)).astype(float)


def slv_019_piotroski_f9_rising_asset_turnover(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Piotroski signal F9: 1 if asset turnover (revenue/assets) improved QoQ, else 0."""
    at_ = _safe_div(revenue, assets)
    return (at_ > at_.shift(_TD_QTR)).astype(float)


def slv_020_piotroski_fscore(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Assembled Piotroski F-score (0-9): sum of all 9 binary signals.
    Higher score = stronger financial position; score <= 2 often signals distress.
    """
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


def slv_021_piotroski_distress_flag(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if Piotroski F-score <= 2 (high distress), else 0."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    return (score <= 2).astype(float)


def slv_022_piotroski_strong_flag(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if Piotroski F-score >= 8 (strong), else 0."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    return (score >= 8).astype(float)


def slv_023_piotroski_profitability_subscore(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Piotroski profitability sub-score: F1+F2+F3+F4 (0-4 signals)."""
    f1 = (netinc > 0).astype(float)
    f2 = (ncfo > 0).astype(float)
    roa = _safe_div(netinc, assets)
    f3 = (roa > roa.shift(_TD_QTR)).astype(float)
    f4 = (_safe_div(ncfo, assets) > roa).astype(float)
    return f1 + f2 + f3 + f4


def slv_024_piotroski_leverage_subscore(
    debt: pd.Series,
    assets: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
) -> pd.Series:
    """Piotroski leverage/liquidity sub-score: F5+F6+F7 (0-3 signals)."""
    lev = _safe_div(debt, assets)
    f5 = (lev < lev.shift(_TD_QTR)).astype(float)
    cr = _safe_div(assetsc, liabilitiesc)
    f6 = (cr > cr.shift(_TD_QTR)).astype(float)
    f7 = (shareswa <= shareswa.shift(_TD_QTR)).astype(float)
    return f5 + f6 + f7


def slv_025_piotroski_efficiency_subscore(gp: pd.Series, revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Piotroski efficiency sub-score: F8+F9 (0-2 signals)."""
    gm = _safe_div(gp, revenue)
    f8 = (gm > gm.shift(_TD_QTR)).astype(float)
    at_ = _safe_div(revenue, assets)
    f9 = (at_ > at_.shift(_TD_QTR)).astype(float)
    return f8 + f9


# --- Group C (026-040): Zmijewski-style, Springate-style, Ohlson-style components ---

def slv_026_zmijewski_roa(netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski-style component: ROA = netinc / assets."""
    return _safe_div(netinc, assets)


def slv_027_zmijewski_leverage(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Zmijewski-style component: leverage = liabilities / assets."""
    return _safe_div(liabilities, assets)


def slv_028_zmijewski_liquidity(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Zmijewski-style component: liquidity = assetsc / liabilitiesc (current ratio)."""
    return _safe_div(assetsc, liabilitiesc)


def slv_029_zmijewski_score(netinc: pd.Series, assets: pd.Series, liabilities: pd.Series, assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """
    Zmijewski-style distress score (logit approximation):
    -4.3 - 4.5*(netinc/assets) + 5.7*(liabilities/assets) - 0.004*(assetsc/liabilitiesc).
    Higher = more distress. Not a probability — use for ordinal ranking.
    """
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    return -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq


def slv_030_springate_working_capital_ratio(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate-style component A: workingcapital / assets."""
    return _safe_div(workingcapital, assets)


def slv_031_springate_ebit_ratio(ebit: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate-style component B: ebit / assets."""
    return _safe_div(ebit, assets)


def slv_032_springate_ebt_ratio(ebt: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Springate-style component C: ebt / current liabilities."""
    return _safe_div(ebt, liabilitiesc)


def slv_033_springate_revenue_ratio(revenue: pd.Series, assets: pd.Series) -> pd.Series:
    """Springate-style component D: revenue / assets (asset turnover)."""
    return _safe_div(revenue, assets)


def slv_034_springate_score(
    workingcapital: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    ebt: pd.Series,
    liabilitiesc: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Springate-style distress score:
    S = 1.03*A + 3.07*B + 0.66*C + 0.4*D
    A=wc/assets, B=ebit/assets, C=ebt/currentliab, D=revenue/assets.
    S < 0.862 historically indicates distress; higher = healthier.
    """
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    return 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d


def slv_035_springate_distress_flag(
    workingcapital: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    ebt: pd.Series,
    liabilitiesc: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Binary: 1 if Springate-style score < 0.862 (distress threshold), else 0."""
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return (s < 0.862).astype(float)


def slv_036_ohlson_size_component(assets: pd.Series) -> pd.Series:
    """Ohlson O-score component: log(total assets) — size proxy."""
    return np.log(assets.abs().replace(0, np.nan))


def slv_037_ohlson_leverage_component(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson O-score component: total liabilities / total assets."""
    return _safe_div(liabilities, assets)


def slv_038_ohlson_working_capital_component(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Ohlson O-score component: workingcapital / total assets."""
    return _safe_div(workingcapital, assets)


def slv_039_ohlson_current_ratio_component(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Ohlson O-score component: current liabilities / current assets (inverted current ratio)."""
    return _safe_div(liabilitiesc, assetsc)


def slv_040_ohlson_netinc_negative_flag(netinc: pd.Series) -> pd.Series:
    """Ohlson O-score binary: 1 if net income < 0 for two consecutive periods."""
    neg = (netinc < 0).astype(float)
    return (neg * neg.shift(_TD_QTR)).fillna(0.0)


# --- Group D (041-055): Custom distress indices ---

def slv_041_debt_to_equity_ratio(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Debt-to-equity ratio: debt / equity (leverage indicator)."""
    return _safe_div(debt, equity)


def slv_042_debt_to_ebitda_ratio(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Debt / EBITDA: how many years of EBITDA to repay total debt."""
    return _safe_div(debt, ebitda.abs().replace(0, np.nan))


def slv_043_interest_coverage_ratio(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Interest coverage ratio: ebit / interest expense. < 1.5 signals stress."""
    return _safe_div(ebit, intexp.abs().replace(0, np.nan))


def slv_044_interest_coverage_below_1(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Binary: 1 if interest coverage (ebit/intexp) < 1.0 (cannot cover interest), else 0."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return (cov < 1.0).astype(float)


def slv_045_cash_to_liabilities_ratio(cashnequiv: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Cash / total liabilities: immediate liquidity coverage of all obligations."""
    return _safe_div(cashnequiv, liabilities)


def slv_046_ncfo_to_debt_ratio(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """Operating cash flow / total debt: cash flow-based debt coverage."""
    return _safe_div(ncfo, debt.abs().replace(0, np.nan))


def slv_047_equity_to_assets_ratio(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Equity / assets: capital adequacy / solvency cushion ratio."""
    return _safe_div(equity, assets)


def slv_048_negative_equity_flag(equity: pd.Series) -> pd.Series:
    """Binary: 1 if book equity is negative (technical insolvency), else 0."""
    return (equity < 0).astype(float)


def slv_049_ncfo_negative_flag(ncfo: pd.Series) -> pd.Series:
    """Binary: 1 if operating cash flow is negative, else 0."""
    return (ncfo < 0).astype(float)


def slv_050_liabilities_to_assets_ratio(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Total liabilities / total assets: overall leverage ratio."""
    return _safe_div(liabilities, assets)


def slv_051_current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio: assetsc / liabilitiesc. < 1.0 = current insolvency risk."""
    return _safe_div(assetsc, liabilitiesc)


def slv_052_current_ratio_below_1_flag(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if current ratio < 1.0, else 0."""
    cr = _safe_div(assetsc, liabilitiesc)
    return (cr < 1.0).astype(float)


def slv_053_quick_ratio_proxy(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio proxy: (assetsc - inventory) / liabilitiesc."""
    return _safe_div(assetsc - inventory, liabilitiesc)


def slv_054_debt_coverage_ratio(ncfo: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Operating cash flow / current liabilities: short-term debt coverage from cash."""
    return _safe_div(ncfo, liabilitiesc.abs().replace(0, np.nan))


def slv_055_retained_earnings_negative_flag(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retained earnings < 0 (accumulated losses exceed paid-in capital)."""
    return (retearn < 0).astype(float)


# --- Group E (056-075): Composite distress indices, zone flags, trends ---

def slv_056_composite_distress_index(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """
    Custom composite distress index: equally weighted Z-score average of
    five normalized ratios (wc/assets, retearn/assets, ebit/assets,
    equity/liabilities, ncfo/assets).  Higher = healthier.
    """
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
    return (z1 + z2 + z3 + z4 + z5) / 5.0


def slv_057_altman_z_qoq_change(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """QoQ change in the Altman Z'' score (63-day diff)."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return z - z.shift(_TD_QTR)


def slv_058_altman_z_yoy_change(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """YoY change in the Altman Z'' score (252-day diff)."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return z - z.shift(_TD_YEAR)


def slv_059_altman_z_drawdown_from_1y_peak(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Altman Z'' score drawdown from its trailing 1-year peak."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    peak = _rolling_max(z, _TD_YEAR)
    return z - peak


def slv_060_altman_z_drawdown_from_expanding_peak(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Altman Z'' score drawdown from its all-history expanding peak."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    peak = z.expanding(min_periods=1).max()
    return z - peak


def slv_061_piotroski_fscore_qoq_change(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """QoQ change in Piotroski F-score (63-day diff)."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    return score - score.shift(_TD_QTR)


def slv_062_piotroski_fscore_yoy_change(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """YoY change in Piotroski F-score (252-day diff)."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    return score - score.shift(_TD_YEAR)


def slv_063_consecutive_altman_distress_quarters(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """
    Consecutive quarters (daily steps) the Altman Z'' score has remained below
    1.1 (distress zone). Resets to 0 on any day Z'' >= 1.1.
    """
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    in_distress = (z < 1.1).astype(int)
    streak = np.zeros(len(in_distress), dtype=float)
    arr = in_distress.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=z.index)


def slv_064_consecutive_piotroski_low_quarters(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Consecutive daily steps Piotroski F-score <= 2 (distress zone). Resets at > 2."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    low = (score <= 2).astype(int)
    streak = np.zeros(len(low), dtype=float)
    arr = low.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=score.index)


def slv_065_zmijewski_score_qoq_change(
    netinc: pd.Series,
    assets: pd.Series,
    liabilities: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
) -> pd.Series:
    """QoQ change in Zmijewski-style score (higher change = worsening)."""
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(assetsc, liabilitiesc)
    z = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    return z - z.shift(_TD_QTR)


def slv_066_springate_score_qoq_change(
    workingcapital: pd.Series,
    assets: pd.Series,
    ebit: pd.Series,
    ebt: pd.Series,
    liabilitiesc: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """QoQ change in Springate-style score."""
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    s = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    return s - s.shift(_TD_QTR)


def slv_067_multi_score_distress_count(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    liabilitiesc: pd.Series,
    ebt: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Count of how many composite models flag distress simultaneously (0-3):
    Altman Z'' < 1.1, Springate < 0.862, Zmijewski > 0 (positive = distress-leaning).
    """
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z_alt = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    alt_flag = (z_alt < 1.1).astype(float)

    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    spr = 1.03 * a + 3.07 * b + 0.66 * c + 0.4 * d
    spr_flag = (spr < 0.862).astype(float)

    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    liq = _safe_div(workingcapital, assets)
    zmi = -4.3 - 4.5 * roa + 5.7 * lev - 0.004 * liq
    zmi_flag = (zmi > 0).astype(float)

    return alt_flag + spr_flag + zmi_flag


def slv_068_altman_z_3y_avg(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Trailing 3-year (756-day) rolling mean of Altman Z'' score."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return _rolling_mean(z, _TD_3Y)


def slv_069_altman_z_vs_3y_avg(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Current Altman Z'' minus its trailing 3-year mean (deviation from trend)."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return z - _rolling_mean(z, _TD_3Y)


def slv_070_piotroski_fscore_3y_avg(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Trailing 3-year rolling mean of Piotroski F-score."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    return _rolling_mean(score, _TD_3Y)


def slv_071_altman_z_expanding_pct_rank(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Expanding percentile rank of Altman Z'' (all-history rank; 0=worst)."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return z.expanding(min_periods=2).rank(pct=True)


def slv_072_altman_z_zscore_4q(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
) -> pd.Series:
    """Z-score of Altman Z'' within a trailing 4-quarter (252-day) window."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    return _zscore_rolling(z, _TD_YEAR)


def slv_073_piotroski_fscore_expanding_pct_rank(
    netinc: pd.Series,
    ncfo: pd.Series,
    assets: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """Expanding percentile rank of Piotroski F-score (all-history rank)."""
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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    return score.expanding(min_periods=2).rank(pct=True)


def slv_074_dual_distress_flag(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
    debt: pd.Series,
    assetsc: pd.Series,
    liabilitiesc: pd.Series,
    shareswa: pd.Series,
    gp: pd.Series,
    revenue: pd.Series,
) -> pd.Series:
    """
    Binary: 1 if BOTH Altman Z'' < 1.1 AND Piotroski F-score <= 2 simultaneously.
    Strongest dual-model distress signal.
    """
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    z = 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4
    alt_flag = z < 1.1

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
    score = f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9
    pio_flag = score <= 2

    return (alt_flag & pio_flag).astype(float)


def slv_075_solvency_composite_ewm(
    workingcapital: pd.Series,
    assets: pd.Series,
    retearn: pd.Series,
    ebit: pd.Series,
    equity: pd.Series,
    liabilities: pd.Series,
    netinc: pd.Series,
    ncfo: pd.Series,
) -> pd.Series:
    """
    EWM-smoothed solvency composite: span=252 exponential weighted mean of the
    custom composite distress index (slv_056 logic). Provides a smoother trend.
    """
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
    return _ewm_mean(composite, _TD_YEAR)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

SOLVENCY_SCORES_REGISTRY_001_075 = {
    "slv_001_altman_x1_wc_to_assets":           {"inputs": ["workingcapital", "assets"],                                                                                              "func": slv_001_altman_x1_wc_to_assets},
    "slv_002_altman_x2_retearn_to_assets":       {"inputs": ["retearn", "assets"],                                                                                                    "func": slv_002_altman_x2_retearn_to_assets},
    "slv_003_altman_x3_ebit_to_assets":          {"inputs": ["ebit", "assets"],                                                                                                       "func": slv_003_altman_x3_ebit_to_assets},
    "slv_004_altman_x4_equity_to_liabilities":   {"inputs": ["equity", "liabilities"],                                                                                               "func": slv_004_altman_x4_equity_to_liabilities},
    "slv_005_altman_x5_revenue_to_assets":       {"inputs": ["revenue", "assets"],                                                                                                    "func": slv_005_altman_x5_revenue_to_assets},
    "slv_006_altman_z_double_prime":             {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                 "func": slv_006_altman_z_double_prime},
    "slv_007_altman_z_safe_zone_flag":           {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                 "func": slv_007_altman_z_safe_zone_flag},
    "slv_008_altman_z_distress_zone_flag":       {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                 "func": slv_008_altman_z_distress_zone_flag},
    "slv_009_altman_z_grey_zone_flag":           {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                 "func": slv_009_altman_z_grey_zone_flag},
    "slv_010_altman_z_weighted_x1":             {"inputs": ["workingcapital", "assets"],                                                                                              "func": slv_010_altman_z_weighted_x1},
    "slv_011_piotroski_f1_positive_netinc":      {"inputs": ["netinc"],                                                                                                               "func": slv_011_piotroski_f1_positive_netinc},
    "slv_012_piotroski_f2_positive_ncfo":        {"inputs": ["ncfo"],                                                                                                                 "func": slv_012_piotroski_f2_positive_ncfo},
    "slv_013_piotroski_f3_rising_roa":           {"inputs": ["netinc", "assets"],                                                                                                     "func": slv_013_piotroski_f3_rising_roa},
    "slv_014_piotroski_f4_accrual_quality":      {"inputs": ["ncfo", "netinc", "assets"],                                                                                             "func": slv_014_piotroski_f4_accrual_quality},
    "slv_015_piotroski_f5_falling_leverage":     {"inputs": ["debt", "assets"],                                                                                                       "func": slv_015_piotroski_f5_falling_leverage},
    "slv_016_piotroski_f6_rising_current_ratio": {"inputs": ["assetsc", "liabilitiesc"],                                                                                              "func": slv_016_piotroski_f6_rising_current_ratio},
    "slv_017_piotroski_f7_no_dilution":          {"inputs": ["shareswa"],                                                                                                             "func": slv_017_piotroski_f7_no_dilution},
    "slv_018_piotroski_f8_rising_gross_margin":  {"inputs": ["gp", "revenue"],                                                                                                        "func": slv_018_piotroski_f8_rising_gross_margin},
    "slv_019_piotroski_f9_rising_asset_turnover":{"inputs": ["revenue", "assets"],                                                                                                    "func": slv_019_piotroski_f9_rising_asset_turnover},
    "slv_020_piotroski_fscore":                  {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                             "func": slv_020_piotroski_fscore},
    "slv_021_piotroski_distress_flag":           {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                             "func": slv_021_piotroski_distress_flag},
    "slv_022_piotroski_strong_flag":             {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                             "func": slv_022_piotroski_strong_flag},
    "slv_023_piotroski_profitability_subscore":  {"inputs": ["netinc", "ncfo", "assets"],                                                                                             "func": slv_023_piotroski_profitability_subscore},
    "slv_024_piotroski_leverage_subscore":       {"inputs": ["debt", "assets", "assetsc", "liabilitiesc", "shareswa"],                                                                "func": slv_024_piotroski_leverage_subscore},
    "slv_025_piotroski_efficiency_subscore":     {"inputs": ["gp", "revenue", "assets"],                                                                                              "func": slv_025_piotroski_efficiency_subscore},
    "slv_026_zmijewski_roa":                     {"inputs": ["netinc", "assets"],                                                                                                     "func": slv_026_zmijewski_roa},
    "slv_027_zmijewski_leverage":                {"inputs": ["liabilities", "assets"],                                                                                                "func": slv_027_zmijewski_leverage},
    "slv_028_zmijewski_liquidity":               {"inputs": ["assetsc", "liabilitiesc"],                                                                                              "func": slv_028_zmijewski_liquidity},
    "slv_029_zmijewski_score":                   {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                           "func": slv_029_zmijewski_score},
    "slv_030_springate_working_capital_ratio":   {"inputs": ["workingcapital", "assets"],                                                                                             "func": slv_030_springate_working_capital_ratio},
    "slv_031_springate_ebit_ratio":              {"inputs": ["ebit", "assets"],                                                                                                       "func": slv_031_springate_ebit_ratio},
    "slv_032_springate_ebt_ratio":               {"inputs": ["ebt", "liabilitiesc"],                                                                                                  "func": slv_032_springate_ebt_ratio},
    "slv_033_springate_revenue_ratio":           {"inputs": ["revenue", "assets"],                                                                                                    "func": slv_033_springate_revenue_ratio},
    "slv_034_springate_score":                   {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                   "func": slv_034_springate_score},
    "slv_035_springate_distress_flag":           {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                   "func": slv_035_springate_distress_flag},
    "slv_036_ohlson_size_component":             {"inputs": ["assets"],                                                                                                               "func": slv_036_ohlson_size_component},
    "slv_037_ohlson_leverage_component":         {"inputs": ["liabilities", "assets"],                                                                                                "func": slv_037_ohlson_leverage_component},
    "slv_038_ohlson_working_capital_component":  {"inputs": ["workingcapital", "assets"],                                                                                             "func": slv_038_ohlson_working_capital_component},
    "slv_039_ohlson_current_ratio_component":    {"inputs": ["assetsc", "liabilitiesc"],                                                                                              "func": slv_039_ohlson_current_ratio_component},
    "slv_040_ohlson_netinc_negative_flag":       {"inputs": ["netinc"],                                                                                                               "func": slv_040_ohlson_netinc_negative_flag},
    "slv_041_debt_to_equity_ratio":              {"inputs": ["debt", "equity"],                                                                                                       "func": slv_041_debt_to_equity_ratio},
    "slv_042_debt_to_ebitda_ratio":              {"inputs": ["debt", "ebitda"],                                                                                                       "func": slv_042_debt_to_ebitda_ratio},
    "slv_043_interest_coverage_ratio":           {"inputs": ["ebit", "intexp"],                                                                                                       "func": slv_043_interest_coverage_ratio},
    "slv_044_interest_coverage_below_1":         {"inputs": ["ebit", "intexp"],                                                                                                       "func": slv_044_interest_coverage_below_1},
    "slv_045_cash_to_liabilities_ratio":         {"inputs": ["cashnequiv", "liabilities"],                                                                                            "func": slv_045_cash_to_liabilities_ratio},
    "slv_046_ncfo_to_debt_ratio":                {"inputs": ["ncfo", "debt"],                                                                                                         "func": slv_046_ncfo_to_debt_ratio},
    "slv_047_equity_to_assets_ratio":            {"inputs": ["equity", "assets"],                                                                                                     "func": slv_047_equity_to_assets_ratio},
    "slv_048_negative_equity_flag":              {"inputs": ["equity"],                                                                                                               "func": slv_048_negative_equity_flag},
    "slv_049_ncfo_negative_flag":                {"inputs": ["ncfo"],                                                                                                                 "func": slv_049_ncfo_negative_flag},
    "slv_050_liabilities_to_assets_ratio":       {"inputs": ["liabilities", "assets"],                                                                                                "func": slv_050_liabilities_to_assets_ratio},
    "slv_051_current_ratio":                     {"inputs": ["assetsc", "liabilitiesc"],                                                                                              "func": slv_051_current_ratio},
    "slv_052_current_ratio_below_1_flag":        {"inputs": ["assetsc", "liabilitiesc"],                                                                                              "func": slv_052_current_ratio_below_1_flag},
    "slv_053_quick_ratio_proxy":                 {"inputs": ["assetsc", "inventory", "liabilitiesc"],                                                                                 "func": slv_053_quick_ratio_proxy},
    "slv_054_debt_coverage_ratio":               {"inputs": ["ncfo", "liabilitiesc"],                                                                                                 "func": slv_054_debt_coverage_ratio},
    "slv_055_retained_earnings_negative_flag":   {"inputs": ["retearn"],                                                                                                              "func": slv_055_retained_earnings_negative_flag},
    "slv_056_composite_distress_index":          {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                               "func": slv_056_composite_distress_index},
    "slv_057_altman_z_qoq_change":              {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                  "func": slv_057_altman_z_qoq_change},
    "slv_058_altman_z_yoy_change":              {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                  "func": slv_058_altman_z_yoy_change},
    "slv_059_altman_z_drawdown_from_1y_peak":   {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                  "func": slv_059_altman_z_drawdown_from_1y_peak},
    "slv_060_altman_z_drawdown_from_expanding_peak": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                            "func": slv_060_altman_z_drawdown_from_expanding_peak},
    "slv_061_piotroski_fscore_qoq_change":       {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                             "func": slv_061_piotroski_fscore_qoq_change},
    "slv_062_piotroski_fscore_yoy_change":       {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                             "func": slv_062_piotroski_fscore_yoy_change},
    "slv_063_consecutive_altman_distress_quarters": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                             "func": slv_063_consecutive_altman_distress_quarters},
    "slv_064_consecutive_piotroski_low_quarters": {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                           "func": slv_064_consecutive_piotroski_low_quarters},
    "slv_065_zmijewski_score_qoq_change":        {"inputs": ["netinc", "assets", "liabilities", "assetsc", "liabilitiesc"],                                                           "func": slv_065_zmijewski_score_qoq_change},
    "slv_066_springate_score_qoq_change":        {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"],                                                   "func": slv_066_springate_score_qoq_change},
    "slv_067_multi_score_distress_count":        {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "liabilitiesc", "ebt", "revenue"], "func": slv_067_multi_score_distress_count},
    "slv_068_altman_z_3y_avg":                  {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                  "func": slv_068_altman_z_3y_avg},
    "slv_069_altman_z_vs_3y_avg":               {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                  "func": slv_069_altman_z_vs_3y_avg},
    "slv_070_piotroski_fscore_3y_avg":           {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                             "func": slv_070_piotroski_fscore_3y_avg},
    "slv_071_altman_z_expanding_pct_rank":       {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                 "func": slv_071_altman_z_expanding_pct_rank},
    "slv_072_altman_z_zscore_4q":               {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"],                                                  "func": slv_072_altman_z_zscore_4q},
    "slv_073_piotroski_fscore_expanding_pct_rank": {"inputs": ["netinc", "ncfo", "assets", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"],                          "func": slv_073_piotroski_fscore_expanding_pct_rank},
    "slv_074_dual_distress_flag":                {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo", "debt", "assetsc", "liabilitiesc", "shareswa", "gp", "revenue"], "func": slv_074_dual_distress_flag},
    "slv_075_solvency_composite_ewm":            {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"],                               "func": slv_075_solvency_composite_ewm},
}
