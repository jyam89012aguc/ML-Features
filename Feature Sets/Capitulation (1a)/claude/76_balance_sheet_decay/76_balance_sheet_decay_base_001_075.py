"""
76_balance_sheet_decay — Base Features 001-100
Domain: holistic multi-quarter balance-sheet deterioration
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
    this helper is for documentation and optional manual use.
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

# --- Group A (001-015): Total assets and equity absolute change / pct change ---

def bsd_001_assets_qoq_change(assets: pd.Series) -> pd.Series:
    """Total assets QoQ absolute change (63-day lag)."""
    return assets - assets.shift(_TD_QTR)


def bsd_002_assets_yoy_change(assets: pd.Series) -> pd.Series:
    """Total assets YoY absolute change (252-day lag)."""
    return assets - assets.shift(_TD_YEAR)


def bsd_003_assets_yoy_pct(assets: pd.Series) -> pd.Series:
    """Total assets YoY percent change; denominator is abs(prior)."""
    prior = assets.shift(_TD_YEAR)
    return _safe_div_abs(assets - prior, prior)


def bsd_004_assets_2y_pct(assets: pd.Series) -> pd.Series:
    """Total assets 2-year percent change."""
    prior = assets.shift(_TD_2Y)
    return _safe_div_abs(assets - prior, prior)


def bsd_005_equity_qoq_change(equity: pd.Series) -> pd.Series:
    """Total equity QoQ absolute change."""
    return equity - equity.shift(_TD_QTR)


def bsd_006_equity_yoy_change(equity: pd.Series) -> pd.Series:
    """Total equity YoY absolute change."""
    return equity - equity.shift(_TD_YEAR)


def bsd_007_equity_yoy_pct(equity: pd.Series) -> pd.Series:
    """Total equity YoY percent change; denominator is abs(prior)."""
    prior = equity.shift(_TD_YEAR)
    return _safe_div_abs(equity - prior, prior)


def bsd_008_equity_2y_pct(equity: pd.Series) -> pd.Series:
    """Total equity 2-year percent change."""
    prior = equity.shift(_TD_2Y)
    return _safe_div_abs(equity - prior, prior)


def bsd_009_equity_3y_pct(equity: pd.Series) -> pd.Series:
    """Total equity 3-year percent change."""
    prior = equity.shift(_TD_3Y)
    return _safe_div_abs(equity - prior, prior)


def bsd_010_retearn_yoy_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings YoY absolute change."""
    return retearn - retearn.shift(_TD_YEAR)


def bsd_011_retearn_2y_pct(retearn: pd.Series) -> pd.Series:
    """Retained earnings 2-year percent change."""
    prior = retearn.shift(_TD_2Y)
    return _safe_div_abs(retearn - prior, prior)


def bsd_012_invcap_yoy_change(invcap: pd.Series) -> pd.Series:
    """Invested capital YoY absolute change."""
    return invcap - invcap.shift(_TD_YEAR)


def bsd_013_invcap_yoy_pct(invcap: pd.Series) -> pd.Series:
    """Invested capital YoY percent change."""
    prior = invcap.shift(_TD_YEAR)
    return _safe_div_abs(invcap - prior, prior)


def bsd_014_cashnequiv_yoy_change(cashnequiv: pd.Series) -> pd.Series:
    """Cash and equivalents YoY absolute change."""
    return cashnequiv - cashnequiv.shift(_TD_YEAR)


def bsd_015_cashnequiv_yoy_pct(cashnequiv: pd.Series) -> pd.Series:
    """Cash and equivalents YoY percent change."""
    prior = cashnequiv.shift(_TD_YEAR)
    return _safe_div_abs(cashnequiv - prior, prior)


# --- Group B (016-030): Liabilities and debt growth ---

def bsd_016_liabilities_qoq_change(liabilities: pd.Series) -> pd.Series:
    """Total liabilities QoQ absolute change."""
    return liabilities - liabilities.shift(_TD_QTR)


def bsd_017_liabilities_yoy_change(liabilities: pd.Series) -> pd.Series:
    """Total liabilities YoY absolute change."""
    return liabilities - liabilities.shift(_TD_YEAR)


def bsd_018_liabilities_yoy_pct(liabilities: pd.Series) -> pd.Series:
    """Total liabilities YoY percent change."""
    prior = liabilities.shift(_TD_YEAR)
    return _safe_div_abs(liabilities - prior, prior)


def bsd_019_debt_yoy_change(debt: pd.Series) -> pd.Series:
    """Total debt YoY absolute change."""
    return debt - debt.shift(_TD_YEAR)


def bsd_020_debt_yoy_pct(debt: pd.Series) -> pd.Series:
    """Total debt YoY percent change."""
    prior = debt.shift(_TD_YEAR)
    return _safe_div_abs(debt - prior, prior)


def bsd_021_debt_2y_pct(debt: pd.Series) -> pd.Series:
    """Total debt 2-year percent change."""
    prior = debt.shift(_TD_2Y)
    return _safe_div_abs(debt - prior, prior)


def bsd_022_liabilities_to_assets_ratio(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Liabilities divided by total assets — financial leverage ratio."""
    return _safe_div(liabilities, assets)


def bsd_023_liabilities_to_equity_ratio(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Liabilities divided by equity (D/E style ratio)."""
    return _safe_div(liabilities, equity.abs().replace(0, np.nan))


def bsd_024_debt_to_equity_ratio(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Total debt divided by equity."""
    return _safe_div(debt, equity.abs().replace(0, np.nan))


def bsd_025_debt_to_assets_ratio(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Total debt divided by total assets."""
    return _safe_div(debt, assets)


def bsd_026_liabilities_growth_minus_assets_growth(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY pct growth of liabilities minus YoY pct growth of assets — leverage spread."""
    liab_pct  = _safe_div_abs(liabilities - liabilities.shift(_TD_YEAR), liabilities.shift(_TD_YEAR))
    asset_pct = _safe_div_abs(assets - assets.shift(_TD_YEAR), assets.shift(_TD_YEAR))
    return liab_pct - asset_pct


def bsd_027_debt_growth_minus_equity_growth(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY pct growth of debt minus YoY pct growth of equity."""
    debt_pct  = _safe_div_abs(debt - debt.shift(_TD_YEAR), debt.shift(_TD_YEAR))
    eq_pct    = _safe_div_abs(equity - equity.shift(_TD_YEAR), equity.shift(_TD_YEAR).abs().replace(0, np.nan))
    return debt_pct - eq_pct


def bsd_028_liabilitiesc_yoy_pct(liabilitiesc: pd.Series) -> pd.Series:
    """Current liabilities YoY percent change."""
    prior = liabilitiesc.shift(_TD_YEAR)
    return _safe_div_abs(liabilitiesc - prior, prior)


def bsd_029_liabilitiesnc_yoy_pct(liabilitiesnc: pd.Series) -> pd.Series:
    """Non-current liabilities YoY percent change."""
    prior = liabilitiesnc.shift(_TD_YEAR)
    return _safe_div_abs(liabilitiesnc - prior, prior)


def bsd_030_debtnc_yoy_pct(debtnc: pd.Series) -> pd.Series:
    """Non-current (long-term) debt YoY percent change."""
    prior = debtnc.shift(_TD_YEAR)
    return _safe_div_abs(debtnc - prior, prior)


# --- Group C (031-045): Net asset value and working capital erosion ---

def bsd_031_nav_level(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset value = assets - liabilities."""
    return assets - liabilities


def bsd_032_nav_yoy_change(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """YoY change in net asset value (assets - liabilities)."""
    nav = assets - liabilities
    return nav - nav.shift(_TD_YEAR)


def bsd_033_nav_yoy_pct(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """YoY percent change in net asset value."""
    nav   = assets - liabilities
    prior = nav.shift(_TD_YEAR)
    return _safe_div_abs(nav - prior, prior)


def bsd_034_nav_2y_pct(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """2-year percent change in net asset value."""
    nav   = assets - liabilities
    prior = nav.shift(_TD_2Y)
    return _safe_div_abs(nav - prior, prior)


def bsd_035_nav_drawdown_from_4q_peak(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset value vs its 4-quarter rolling peak."""
    nav  = assets - liabilities
    peak = _rolling_max(nav, _TD_YEAR)
    return nav - peak


def bsd_036_nav_drawdown_from_expanding_peak(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset value vs its all-history expanding maximum."""
    nav  = assets - liabilities
    peak = nav.expanding(min_periods=1).max()
    return nav - peak


def bsd_037_workingcapital_yoy_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital YoY absolute change."""
    return workingcapital - workingcapital.shift(_TD_YEAR)


def bsd_038_workingcapital_yoy_pct(workingcapital: pd.Series) -> pd.Series:
    """Working capital YoY percent change."""
    prior = workingcapital.shift(_TD_YEAR)
    return _safe_div_abs(workingcapital - prior, prior)


def bsd_039_workingcapital_drawdown_from_4q_peak(workingcapital: pd.Series) -> pd.Series:
    """Working capital vs its 4-quarter rolling peak."""
    peak = _rolling_max(workingcapital, _TD_YEAR)
    return workingcapital - peak


def bsd_040_workingcapital_is_negative(workingcapital: pd.Series) -> pd.Series:
    """Binary: 1 if working capital < 0."""
    return (workingcapital < 0).astype(float)


def bsd_041_retearn_is_negative(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retained earnings < 0 (accumulated deficit)."""
    return (retearn < 0).astype(float)


def bsd_042_equity_is_negative(equity: pd.Series) -> pd.Series:
    """Binary: 1 if total equity < 0 (balance-sheet insolvency)."""
    return (equity < 0).astype(float)


def bsd_043_retearn_drawdown_from_expanding_peak(retearn: pd.Series) -> pd.Series:
    """Retained earnings vs its all-history expanding maximum."""
    peak = retearn.expanding(min_periods=1).max()
    return retearn - peak


def bsd_044_retearn_drawdown_from_4q_peak(retearn: pd.Series) -> pd.Series:
    """Retained earnings vs its 4-quarter rolling peak."""
    peak = _rolling_max(retearn, _TD_YEAR)
    return retearn - peak


def bsd_045_cashnequiv_drawdown_from_expanding_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash vs its all-history expanding maximum (cash burn proxy)."""
    peak = cashnequiv.expanding(min_periods=1).max()
    return cashnequiv - peak


# --- Group D (046-060): Composite balance-sheet health index ---

def bsd_046_bs_health_index_4q(assets: pd.Series, liabilities: pd.Series,
                                equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Composite balance-sheet health index (4-quarter z-score average).
    Equally weighted sum of z-scores of: assets, (neg)liabilities, equity, cashnequiv.
    Negative = deteriorating.
    """
    z_assets = _zscore_rolling(assets, _TD_YEAR)
    z_liab   = _zscore_rolling(-liabilities, _TD_YEAR)
    z_eq     = _zscore_rolling(equity, _TD_YEAR)
    z_cash   = _zscore_rolling(cashnequiv, _TD_YEAR)
    return (z_assets + z_liab + z_eq + z_cash) / 4.0


def bsd_047_bs_health_index_8q(assets: pd.Series, liabilities: pd.Series,
                                equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Composite balance-sheet health index over 8-quarter window."""
    z_assets = _zscore_rolling(assets, _TD_2Y)
    z_liab   = _zscore_rolling(-liabilities, _TD_2Y)
    z_eq     = _zscore_rolling(equity, _TD_2Y)
    z_cash   = _zscore_rolling(cashnequiv, _TD_2Y)
    return (z_assets + z_liab + z_eq + z_cash) / 4.0


def bsd_048_bs_health_index_12q(assets: pd.Series, liabilities: pd.Series,
                                 equity: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Composite balance-sheet health index over 12-quarter window."""
    z_assets = _zscore_rolling(assets, _TD_3Y)
    z_liab   = _zscore_rolling(-liabilities, _TD_3Y)
    z_eq     = _zscore_rolling(equity, _TD_3Y)
    z_wc     = _zscore_rolling(workingcapital, _TD_3Y)
    return (z_assets + z_liab + z_eq + z_wc) / 4.0


def bsd_049_bs_health_expanded_6line(assets: pd.Series, liabilities: pd.Series,
                                      equity: pd.Series, cashnequiv: pd.Series,
                                      retearn: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Composite balance-sheet health: average z-score of 6 key balance-sheet lines (4Q)."""
    z_assets = _zscore_rolling(assets, _TD_YEAR)
    z_liab   = _zscore_rolling(-liabilities, _TD_YEAR)
    z_eq     = _zscore_rolling(equity, _TD_YEAR)
    z_cash   = _zscore_rolling(cashnequiv, _TD_YEAR)
    z_re     = _zscore_rolling(retearn, _TD_YEAR)
    z_wc     = _zscore_rolling(workingcapital, _TD_YEAR)
    return (z_assets + z_liab + z_eq + z_cash + z_re + z_wc) / 6.0


def bsd_050_bs_health_4q_qoq_slope(assets: pd.Series, liabilities: pd.Series,
                                    equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the 4-quarter composite health index (slope of health)."""
    idx = bsd_046_bs_health_index_4q(assets, liabilities, equity, cashnequiv)
    return idx - idx.shift(_TD_QTR)


def bsd_051_bs_health_4q_yoy_slope(assets: pd.Series, liabilities: pd.Series,
                                    equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY change in the 4-quarter composite health index."""
    idx = bsd_046_bs_health_index_4q(assets, liabilities, equity, cashnequiv)
    return idx - idx.shift(_TD_YEAR)


def bsd_052_bs_deterioration_count_4lines(assets: pd.Series, liabilities: pd.Series,
                                           equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Breadth: count of balance-sheet lines worsening QoQ.
    assets down + liabilities up + equity down + cashnequiv down.
    Range 0-4.
    """
    d_assets = (assets < assets.shift(_TD_QTR)).astype(float)
    d_liab   = (liabilities > liabilities.shift(_TD_QTR)).astype(float)
    d_eq     = (equity < equity.shift(_TD_QTR)).astype(float)
    d_cash   = (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float)
    return d_assets + d_liab + d_eq + d_cash


def bsd_053_bs_deterioration_count_8lines(assets: pd.Series, liabilities: pd.Series,
                                           equity: pd.Series, cashnequiv: pd.Series,
                                           retearn: pd.Series, workingcapital: pd.Series,
                                           invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Breadth: count of 8 balance-sheet lines worsening QoQ.
    Range 0-8.
    """
    d_assets = (assets < assets.shift(_TD_QTR)).astype(float)
    d_liab   = (liabilities > liabilities.shift(_TD_QTR)).astype(float)
    d_eq     = (equity < equity.shift(_TD_QTR)).astype(float)
    d_cash   = (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float)
    d_re     = (retearn < retearn.shift(_TD_QTR)).astype(float)
    d_wc     = (workingcapital < workingcapital.shift(_TD_QTR)).astype(float)
    d_ic     = (invcap < invcap.shift(_TD_QTR)).astype(float)
    d_debt   = (debt > debt.shift(_TD_QTR)).astype(float)
    return d_assets + d_liab + d_eq + d_cash + d_re + d_wc + d_ic + d_debt


def bsd_054_bs_deterioration_fraction_8lines(assets: pd.Series, liabilities: pd.Series,
                                              equity: pd.Series, cashnequiv: pd.Series,
                                              retearn: pd.Series, workingcapital: pd.Series,
                                              invcap: pd.Series, debt: pd.Series) -> pd.Series:
    """Fraction of 8 balance-sheet lines worsening QoQ (range 0-1)."""
    count = bsd_053_bs_deterioration_count_8lines(
        assets, liabilities, equity, cashnequiv, retearn, workingcapital, invcap, debt)
    return count / 8.0


def bsd_055_bs_deterioration_streak_4lines(assets: pd.Series, liabilities: pd.Series,
                                            equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Consecutive quarters with majority (>=3/4) of 4 key lines worsening.
    Resets to 0 when fewer than 3 lines are worsening.
    """
    count = bsd_052_bs_deterioration_count_4lines(assets, liabilities, equity, cashnequiv)
    majority = (count >= 3).astype(int)
    arr    = majority.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=assets.index)


# --- Group E (056-075): Persistence, rolling deterioration, and drawdown composites ---

def bsd_056_equity_declining_quarters_4q(equity: pd.Series) -> pd.Series:
    """Count of quarters with equity declining QoQ in the past 4 quarters (252 days)."""
    declining = (equity < equity.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_YEAR)


def bsd_057_equity_declining_quarters_8q(equity: pd.Series) -> pd.Series:
    """Count of quarters with equity declining QoQ in the past 8 quarters (504 days)."""
    declining = (equity < equity.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_2Y)


def bsd_058_retearn_declining_quarters_4q(retearn: pd.Series) -> pd.Series:
    """Count of quarters with retained earnings declining QoQ in the past 4 quarters."""
    declining = (retearn < retearn.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_YEAR)


def bsd_059_cashnequiv_declining_quarters_4q(cashnequiv: pd.Series) -> pd.Series:
    """Count of quarters with cash declining QoQ in the past 4 quarters."""
    declining = (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_YEAR)


def bsd_060_assets_declining_quarters_4q(assets: pd.Series) -> pd.Series:
    """Count of quarters with total assets declining QoQ in the past 4 quarters."""
    declining = (assets < assets.shift(_TD_QTR)).astype(float)
    return _rolling_sum(declining, _TD_YEAR)


def bsd_061_equity_drawdown_from_4q_peak(equity: pd.Series) -> pd.Series:
    """Equity vs its 4-quarter rolling peak (level drawdown)."""
    peak = _rolling_max(equity, _TD_YEAR)
    return equity - peak


def bsd_062_equity_drawdown_from_8q_peak(equity: pd.Series) -> pd.Series:
    """Equity vs its 8-quarter rolling peak."""
    peak = _rolling_max(equity, _TD_2Y)
    return equity - peak


def bsd_063_equity_pct_drawdown_from_8q_peak(equity: pd.Series) -> pd.Series:
    """Equity percent drawdown from 8-quarter peak."""
    peak = _rolling_max(equity, _TD_2Y)
    return _safe_div_abs(equity - peak, peak)


def bsd_064_equity_drawdown_from_expanding_peak(equity: pd.Series) -> pd.Series:
    """Equity vs its all-history expanding maximum."""
    peak = equity.expanding(min_periods=1).max()
    return equity - peak


def bsd_065_assets_drawdown_from_expanding_peak(assets: pd.Series) -> pd.Series:
    """Total assets vs its all-history expanding maximum."""
    peak = assets.expanding(min_periods=1).max()
    return assets - peak


def bsd_066_invcap_drawdown_from_4q_peak(invcap: pd.Series) -> pd.Series:
    """Invested capital vs its 4-quarter rolling peak."""
    peak = _rolling_max(invcap, _TD_YEAR)
    return invcap - peak


def bsd_067_invcap_drawdown_from_expanding_peak(invcap: pd.Series) -> pd.Series:
    """Invested capital vs its all-history expanding maximum."""
    peak = invcap.expanding(min_periods=1).max()
    return invcap - peak


def bsd_068_bs_composite_drawdown_4lines_4q(assets: pd.Series, liabilities: pd.Series,
                                             equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Composite percent-drawdown score across 4 key BS lines vs their 4Q peaks.
    Uses signed fractional drawdown averaged across lines.
    """
    dd_a  = _safe_div_abs(assets - _rolling_max(assets, _TD_YEAR), _rolling_max(assets, _TD_YEAR))
    dd_e  = _safe_div_abs(equity - _rolling_max(equity, _TD_YEAR), _rolling_max(equity, _TD_YEAR))
    dd_c  = _safe_div_abs(cashnequiv - _rolling_max(cashnequiv, _TD_YEAR), _rolling_max(cashnequiv, _TD_YEAR))
    dd_li = _safe_div_abs(liabilities - _rolling_min(liabilities, _TD_YEAR), _rolling_min(liabilities, _TD_YEAR))
    return (dd_a + dd_e + dd_c - dd_li) / 4.0


def bsd_069_equity_zscore_4q(equity: pd.Series) -> pd.Series:
    """Z-score of equity within a trailing 4-quarter window."""
    return _zscore_rolling(equity, _TD_YEAR)


def bsd_070_equity_zscore_8q(equity: pd.Series) -> pd.Series:
    """Z-score of equity within a trailing 8-quarter window."""
    return _zscore_rolling(equity, _TD_2Y)


def bsd_071_retearn_zscore_4q(retearn: pd.Series) -> pd.Series:
    """Z-score of retained earnings within a trailing 4-quarter window."""
    return _zscore_rolling(retearn, _TD_YEAR)


def bsd_072_cashnequiv_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash and equivalents within a trailing 4-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_YEAR)


def bsd_073_assets_zscore_4q(assets: pd.Series) -> pd.Series:
    """Z-score of total assets within a trailing 4-quarter window."""
    return _zscore_rolling(assets, _TD_YEAR)


def bsd_074_liabilities_zscore_8q(liabilities: pd.Series) -> pd.Series:
    """Z-score of total liabilities within a trailing 8-quarter window."""
    return _zscore_rolling(liabilities, _TD_2Y)


def bsd_075_bs_decay_composite_6line_8q(assets: pd.Series, liabilities: pd.Series,
                                         equity: pd.Series, cashnequiv: pd.Series,
                                         retearn: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """
    Composite balance-sheet decay score over 8-quarter window.
    Equally weighted average of 6 z-scores; negative = deteriorating balance sheet.
    """
    z_a  = _zscore_rolling(assets, _TD_2Y)
    z_l  = _zscore_rolling(-liabilities, _TD_2Y)
    z_e  = _zscore_rolling(equity, _TD_2Y)
    z_c  = _zscore_rolling(cashnequiv, _TD_2Y)
    z_r  = _zscore_rolling(retearn, _TD_2Y)
    z_w  = _zscore_rolling(workingcapital, _TD_2Y)
    return (z_a + z_l + z_e + z_c + z_r + z_w) / 6.0


# --- Group K (151-175): Extended single-line transforms, cross-line ratios, new windows ---

def bsd_151_equity_qoq_pct(equity: pd.Series) -> pd.Series:
    """Total equity QoQ percent change; denominator is abs(prior)."""
    prior = equity.shift(_TD_QTR)
    return _safe_div_abs(equity - prior, prior)


def bsd_152_assets_qoq_pct(assets: pd.Series) -> pd.Series:
    """Total assets QoQ percent change."""
    prior = assets.shift(_TD_QTR)
    return _safe_div_abs(assets - prior, prior)


def bsd_153_debt_qoq_change(debt: pd.Series) -> pd.Series:
    """Total debt QoQ absolute change."""
    return debt - debt.shift(_TD_QTR)


def bsd_154_liabilities_2y_pct(liabilities: pd.Series) -> pd.Series:
    """Total liabilities 2-year percent change."""
    prior = liabilities.shift(_TD_2Y)
    return _safe_div_abs(liabilities - prior, prior)


def bsd_155_retearn_qoq_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings QoQ absolute change."""
    return retearn - retearn.shift(_TD_QTR)


def bsd_156_invcap_2y_pct(invcap: pd.Series) -> pd.Series:
    """Invested capital 2-year percent change."""
    prior = invcap.shift(_TD_2Y)
    return _safe_div_abs(invcap - prior, prior)


def bsd_157_cashnequiv_2y_pct(cashnequiv: pd.Series) -> pd.Series:
    """Cash and equivalents 2-year percent change."""
    prior = cashnequiv.shift(_TD_2Y)
    return _safe_div_abs(cashnequiv - prior, prior)


def bsd_158_nav_3y_pct(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset value 3-year percent change."""
    nav   = assets - liabilities
    prior = nav.shift(_TD_3Y)
    return _safe_div_abs(nav - prior, prior)


def bsd_159_debt_to_invcap_ratio(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    """Total debt divided by invested capital — leverage vs invested base."""
    return _safe_div(debt, invcap.abs().replace(0, np.nan))


def bsd_160_cashnequiv_to_liabilities_ratio(cashnequiv: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Cash and equivalents divided by total liabilities — liquidity coverage ratio."""
    return _safe_div(cashnequiv, liabilities.abs().replace(0, np.nan))


def bsd_161_equity_zscore_12q(equity: pd.Series) -> pd.Series:
    """Z-score of total equity within a trailing 12-quarter (3-year) window."""
    return _zscore_rolling(equity, _TD_3Y)


def bsd_162_retearn_zscore_8q(retearn: pd.Series) -> pd.Series:
    """Z-score of retained earnings within a trailing 8-quarter window."""
    return _zscore_rolling(retearn, _TD_2Y)


def bsd_163_cashnequiv_zscore_8q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash and equivalents within a trailing 8-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_2Y)


def bsd_164_assets_zscore_8q(assets: pd.Series) -> pd.Series:
    """Z-score of total assets within a trailing 8-quarter window."""
    return _zscore_rolling(assets, _TD_2Y)


def bsd_165_liabilities_zscore_4q(liabilities: pd.Series) -> pd.Series:
    """Z-score of total liabilities within a trailing 4-quarter window."""
    return _zscore_rolling(liabilities, _TD_YEAR)


def bsd_166_workingcapital_zscore_4q(workingcapital: pd.Series) -> pd.Series:
    """Z-score of working capital within a trailing 4-quarter window."""
    return _zscore_rolling(workingcapital, _TD_YEAR)


def bsd_167_nav_zscore_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Z-score of net asset value within a trailing 4-quarter window."""
    nav = assets - liabilities
    return _zscore_rolling(nav, _TD_YEAR)


def bsd_168_equity_pct_rank_4q(equity: pd.Series) -> pd.Series:
    """Percentile rank of equity in a trailing 4-quarter window."""
    return _rolling_rank_pct(equity, _TD_YEAR)


def bsd_169_cashnequiv_pct_rank_4q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash and equivalents in a trailing 4-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_YEAR)


def bsd_170_debt_pct_rank_8q(debt: pd.Series) -> pd.Series:
    """Percentile rank of total debt in a trailing 8-quarter window."""
    return _rolling_rank_pct(debt, _TD_2Y)


def bsd_171_retearn_drawdown_from_8q_peak(retearn: pd.Series) -> pd.Series:
    """Retained earnings vs its 8-quarter rolling peak."""
    peak = _rolling_max(retearn, _TD_2Y)
    return retearn - peak


def bsd_172_workingcapital_drawdown_from_8q_peak(workingcapital: pd.Series) -> pd.Series:
    """Working capital vs its 8-quarter rolling peak."""
    peak = _rolling_max(workingcapital, _TD_2Y)
    return workingcapital - peak


def bsd_173_invcap_pct_drawdown_from_4q_peak(invcap: pd.Series) -> pd.Series:
    """Invested capital percent drawdown from 4-quarter peak."""
    peak = _rolling_max(invcap, _TD_YEAR)
    return _safe_div_abs(invcap - peak, peak)


def bsd_174_bs_deterioration_count_yoy_4lines(assets: pd.Series, liabilities: pd.Series,
                                               equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Breadth: count of 4 balance-sheet lines worsening on a YoY basis.
    assets down + liabilities up + equity down + cashnequiv down. Range 0-4.
    """
    d_assets = (assets < assets.shift(_TD_YEAR)).astype(float)
    d_liab   = (liabilities > liabilities.shift(_TD_YEAR)).astype(float)
    d_eq     = (equity < equity.shift(_TD_YEAR)).astype(float)
    d_cash   = (cashnequiv < cashnequiv.shift(_TD_YEAR)).astype(float)
    return d_assets + d_liab + d_eq + d_cash


def bsd_175_bs_health_index_3y_vs_1y(assets: pd.Series, liabilities: pd.Series,
                                      equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    3-year composite BS health minus 1-year composite BS health.
    Positive = recent 1Y health is better than the 3Y baseline (recovery signal).
    Negative = recent deterioration worse than 3Y average (deepening distress).
    """
    idx_1y = (
        _zscore_rolling(assets, _TD_YEAR) +
        _zscore_rolling(-liabilities, _TD_YEAR) +
        _zscore_rolling(equity, _TD_YEAR) +
        _zscore_rolling(cashnequiv, _TD_YEAR)
    ) / 4.0
    idx_3y = (
        _zscore_rolling(assets, _TD_3Y) +
        _zscore_rolling(-liabilities, _TD_3Y) +
        _zscore_rolling(equity, _TD_3Y) +
        _zscore_rolling(cashnequiv, _TD_3Y)
    ) / 4.0
    return idx_1y - idx_3y


# ── Registry 001-075 ──────────────────────────────────────────────────────────

BALANCE_SHEET_DECAY_REGISTRY_001_075 = {
    "bsd_001_assets_qoq_change":                      {"inputs": ["assets"],                                                                     "func": bsd_001_assets_qoq_change},
    "bsd_002_assets_yoy_change":                      {"inputs": ["assets"],                                                                     "func": bsd_002_assets_yoy_change},
    "bsd_003_assets_yoy_pct":                         {"inputs": ["assets"],                                                                     "func": bsd_003_assets_yoy_pct},
    "bsd_004_assets_2y_pct":                          {"inputs": ["assets"],                                                                     "func": bsd_004_assets_2y_pct},
    "bsd_005_equity_qoq_change":                      {"inputs": ["equity"],                                                                     "func": bsd_005_equity_qoq_change},
    "bsd_006_equity_yoy_change":                      {"inputs": ["equity"],                                                                     "func": bsd_006_equity_yoy_change},
    "bsd_007_equity_yoy_pct":                         {"inputs": ["equity"],                                                                     "func": bsd_007_equity_yoy_pct},
    "bsd_008_equity_2y_pct":                          {"inputs": ["equity"],                                                                     "func": bsd_008_equity_2y_pct},
    "bsd_009_equity_3y_pct":                          {"inputs": ["equity"],                                                                     "func": bsd_009_equity_3y_pct},
    "bsd_010_retearn_yoy_change":                     {"inputs": ["retearn"],                                                                    "func": bsd_010_retearn_yoy_change},
    "bsd_011_retearn_2y_pct":                         {"inputs": ["retearn"],                                                                    "func": bsd_011_retearn_2y_pct},
    "bsd_012_invcap_yoy_change":                      {"inputs": ["invcap"],                                                                     "func": bsd_012_invcap_yoy_change},
    "bsd_013_invcap_yoy_pct":                         {"inputs": ["invcap"],                                                                     "func": bsd_013_invcap_yoy_pct},
    "bsd_014_cashnequiv_yoy_change":                  {"inputs": ["cashnequiv"],                                                                 "func": bsd_014_cashnequiv_yoy_change},
    "bsd_015_cashnequiv_yoy_pct":                     {"inputs": ["cashnequiv"],                                                                 "func": bsd_015_cashnequiv_yoy_pct},
    "bsd_016_liabilities_qoq_change":                 {"inputs": ["liabilities"],                                                                "func": bsd_016_liabilities_qoq_change},
    "bsd_017_liabilities_yoy_change":                 {"inputs": ["liabilities"],                                                                "func": bsd_017_liabilities_yoy_change},
    "bsd_018_liabilities_yoy_pct":                    {"inputs": ["liabilities"],                                                                "func": bsd_018_liabilities_yoy_pct},
    "bsd_019_debt_yoy_change":                        {"inputs": ["debt"],                                                                       "func": bsd_019_debt_yoy_change},
    "bsd_020_debt_yoy_pct":                           {"inputs": ["debt"],                                                                       "func": bsd_020_debt_yoy_pct},
    "bsd_021_debt_2y_pct":                            {"inputs": ["debt"],                                                                       "func": bsd_021_debt_2y_pct},
    "bsd_022_liabilities_to_assets_ratio":            {"inputs": ["liabilities", "assets"],                                                      "func": bsd_022_liabilities_to_assets_ratio},
    "bsd_023_liabilities_to_equity_ratio":            {"inputs": ["liabilities", "equity"],                                                      "func": bsd_023_liabilities_to_equity_ratio},
    "bsd_024_debt_to_equity_ratio":                   {"inputs": ["debt", "equity"],                                                             "func": bsd_024_debt_to_equity_ratio},
    "bsd_025_debt_to_assets_ratio":                   {"inputs": ["debt", "assets"],                                                             "func": bsd_025_debt_to_assets_ratio},
    "bsd_026_liabilities_growth_minus_assets_growth": {"inputs": ["liabilities", "assets"],                                                      "func": bsd_026_liabilities_growth_minus_assets_growth},
    "bsd_027_debt_growth_minus_equity_growth":        {"inputs": ["debt", "equity"],                                                             "func": bsd_027_debt_growth_minus_equity_growth},
    "bsd_028_liabilitiesc_yoy_pct":                   {"inputs": ["liabilitiesc"],                                                               "func": bsd_028_liabilitiesc_yoy_pct},
    "bsd_029_liabilitiesnc_yoy_pct":                  {"inputs": ["liabilitiesnc"],                                                              "func": bsd_029_liabilitiesnc_yoy_pct},
    "bsd_030_debtnc_yoy_pct":                         {"inputs": ["debtnc"],                                                                     "func": bsd_030_debtnc_yoy_pct},
    "bsd_031_nav_level":                              {"inputs": ["assets", "liabilities"],                                                      "func": bsd_031_nav_level},
    "bsd_032_nav_yoy_change":                         {"inputs": ["assets", "liabilities"],                                                      "func": bsd_032_nav_yoy_change},
    "bsd_033_nav_yoy_pct":                            {"inputs": ["assets", "liabilities"],                                                      "func": bsd_033_nav_yoy_pct},
    "bsd_034_nav_2y_pct":                             {"inputs": ["assets", "liabilities"],                                                      "func": bsd_034_nav_2y_pct},
    "bsd_035_nav_drawdown_from_4q_peak":              {"inputs": ["assets", "liabilities"],                                                      "func": bsd_035_nav_drawdown_from_4q_peak},
    "bsd_036_nav_drawdown_from_expanding_peak":       {"inputs": ["assets", "liabilities"],                                                      "func": bsd_036_nav_drawdown_from_expanding_peak},
    "bsd_037_workingcapital_yoy_change":              {"inputs": ["workingcapital"],                                                             "func": bsd_037_workingcapital_yoy_change},
    "bsd_038_workingcapital_yoy_pct":                 {"inputs": ["workingcapital"],                                                             "func": bsd_038_workingcapital_yoy_pct},
    "bsd_039_workingcapital_drawdown_from_4q_peak":   {"inputs": ["workingcapital"],                                                             "func": bsd_039_workingcapital_drawdown_from_4q_peak},
    "bsd_040_workingcapital_is_negative":             {"inputs": ["workingcapital"],                                                             "func": bsd_040_workingcapital_is_negative},
    "bsd_041_retearn_is_negative":                    {"inputs": ["retearn"],                                                                    "func": bsd_041_retearn_is_negative},
    "bsd_042_equity_is_negative":                     {"inputs": ["equity"],                                                                     "func": bsd_042_equity_is_negative},
    "bsd_043_retearn_drawdown_from_expanding_peak":   {"inputs": ["retearn"],                                                                    "func": bsd_043_retearn_drawdown_from_expanding_peak},
    "bsd_044_retearn_drawdown_from_4q_peak":          {"inputs": ["retearn"],                                                                    "func": bsd_044_retearn_drawdown_from_4q_peak},
    "bsd_045_cashnequiv_drawdown_from_expanding_peak":{"inputs": ["cashnequiv"],                                                                 "func": bsd_045_cashnequiv_drawdown_from_expanding_peak},
    "bsd_046_bs_health_index_4q":                     {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_046_bs_health_index_4q},
    "bsd_047_bs_health_index_8q":                     {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_047_bs_health_index_8q},
    "bsd_048_bs_health_index_12q":                    {"inputs": ["assets", "liabilities", "equity", "workingcapital"],                         "func": bsd_048_bs_health_index_12q},
    "bsd_049_bs_health_expanded_6line":               {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital"],"func": bsd_049_bs_health_expanded_6line},
    "bsd_050_bs_health_4q_qoq_slope":                 {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_050_bs_health_4q_qoq_slope},
    "bsd_051_bs_health_4q_yoy_slope":                 {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_051_bs_health_4q_yoy_slope},
    "bsd_052_bs_deterioration_count_4lines":          {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_052_bs_deterioration_count_4lines},
    "bsd_053_bs_deterioration_count_8lines":          {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"], "func": bsd_053_bs_deterioration_count_8lines},
    "bsd_054_bs_deterioration_fraction_8lines":       {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital", "invcap", "debt"], "func": bsd_054_bs_deterioration_fraction_8lines},
    "bsd_055_bs_deterioration_streak_4lines":         {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_055_bs_deterioration_streak_4lines},
    "bsd_056_equity_declining_quarters_4q":           {"inputs": ["equity"],                                                                     "func": bsd_056_equity_declining_quarters_4q},
    "bsd_057_equity_declining_quarters_8q":           {"inputs": ["equity"],                                                                     "func": bsd_057_equity_declining_quarters_8q},
    "bsd_058_retearn_declining_quarters_4q":          {"inputs": ["retearn"],                                                                    "func": bsd_058_retearn_declining_quarters_4q},
    "bsd_059_cashnequiv_declining_quarters_4q":       {"inputs": ["cashnequiv"],                                                                 "func": bsd_059_cashnequiv_declining_quarters_4q},
    "bsd_060_assets_declining_quarters_4q":           {"inputs": ["assets"],                                                                     "func": bsd_060_assets_declining_quarters_4q},
    "bsd_061_equity_drawdown_from_4q_peak":           {"inputs": ["equity"],                                                                     "func": bsd_061_equity_drawdown_from_4q_peak},
    "bsd_062_equity_drawdown_from_8q_peak":           {"inputs": ["equity"],                                                                     "func": bsd_062_equity_drawdown_from_8q_peak},
    "bsd_063_equity_pct_drawdown_from_8q_peak":       {"inputs": ["equity"],                                                                     "func": bsd_063_equity_pct_drawdown_from_8q_peak},
    "bsd_064_equity_drawdown_from_expanding_peak":    {"inputs": ["equity"],                                                                     "func": bsd_064_equity_drawdown_from_expanding_peak},
    "bsd_065_assets_drawdown_from_expanding_peak":    {"inputs": ["assets"],                                                                     "func": bsd_065_assets_drawdown_from_expanding_peak},
    "bsd_066_invcap_drawdown_from_4q_peak":           {"inputs": ["invcap"],                                                                     "func": bsd_066_invcap_drawdown_from_4q_peak},
    "bsd_067_invcap_drawdown_from_expanding_peak":    {"inputs": ["invcap"],                                                                     "func": bsd_067_invcap_drawdown_from_expanding_peak},
    "bsd_068_bs_composite_drawdown_4lines_4q":        {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_068_bs_composite_drawdown_4lines_4q},
    "bsd_069_equity_zscore_4q":                       {"inputs": ["equity"],                                                                     "func": bsd_069_equity_zscore_4q},
    "bsd_070_equity_zscore_8q":                       {"inputs": ["equity"],                                                                     "func": bsd_070_equity_zscore_8q},
    "bsd_071_retearn_zscore_4q":                      {"inputs": ["retearn"],                                                                    "func": bsd_071_retearn_zscore_4q},
    "bsd_072_cashnequiv_zscore_4q":                   {"inputs": ["cashnequiv"],                                                                 "func": bsd_072_cashnequiv_zscore_4q},
    "bsd_073_assets_zscore_4q":                       {"inputs": ["assets"],                                                                     "func": bsd_073_assets_zscore_4q},
    "bsd_074_liabilities_zscore_8q":                  {"inputs": ["liabilities"],                                                                "func": bsd_074_liabilities_zscore_8q},
    "bsd_075_bs_decay_composite_6line_8q":            {"inputs": ["assets", "liabilities", "equity", "cashnequiv", "retearn", "workingcapital"],"func": bsd_075_bs_decay_composite_6line_8q},
    "bsd_151_equity_qoq_pct":                         {"inputs": ["equity"],                                                                     "func": bsd_151_equity_qoq_pct},
    "bsd_152_assets_qoq_pct":                         {"inputs": ["assets"],                                                                     "func": bsd_152_assets_qoq_pct},
    "bsd_153_debt_qoq_change":                        {"inputs": ["debt"],                                                                       "func": bsd_153_debt_qoq_change},
    "bsd_154_liabilities_2y_pct":                     {"inputs": ["liabilities"],                                                                "func": bsd_154_liabilities_2y_pct},
    "bsd_155_retearn_qoq_change":                     {"inputs": ["retearn"],                                                                    "func": bsd_155_retearn_qoq_change},
    "bsd_156_invcap_2y_pct":                          {"inputs": ["invcap"],                                                                     "func": bsd_156_invcap_2y_pct},
    "bsd_157_cashnequiv_2y_pct":                      {"inputs": ["cashnequiv"],                                                                 "func": bsd_157_cashnequiv_2y_pct},
    "bsd_158_nav_3y_pct":                             {"inputs": ["assets", "liabilities"],                                                      "func": bsd_158_nav_3y_pct},
    "bsd_159_debt_to_invcap_ratio":                   {"inputs": ["debt", "invcap"],                                                             "func": bsd_159_debt_to_invcap_ratio},
    "bsd_160_cashnequiv_to_liabilities_ratio":        {"inputs": ["cashnequiv", "liabilities"],                                                  "func": bsd_160_cashnequiv_to_liabilities_ratio},
    "bsd_161_equity_zscore_12q":                      {"inputs": ["equity"],                                                                     "func": bsd_161_equity_zscore_12q},
    "bsd_162_retearn_zscore_8q":                      {"inputs": ["retearn"],                                                                    "func": bsd_162_retearn_zscore_8q},
    "bsd_163_cashnequiv_zscore_8q":                   {"inputs": ["cashnequiv"],                                                                 "func": bsd_163_cashnequiv_zscore_8q},
    "bsd_164_assets_zscore_8q":                       {"inputs": ["assets"],                                                                     "func": bsd_164_assets_zscore_8q},
    "bsd_165_liabilities_zscore_4q":                  {"inputs": ["liabilities"],                                                                "func": bsd_165_liabilities_zscore_4q},
    "bsd_166_workingcapital_zscore_4q":               {"inputs": ["workingcapital"],                                                             "func": bsd_166_workingcapital_zscore_4q},
    "bsd_167_nav_zscore_4q":                          {"inputs": ["assets", "liabilities"],                                                      "func": bsd_167_nav_zscore_4q},
    "bsd_168_equity_pct_rank_4q":                     {"inputs": ["equity"],                                                                     "func": bsd_168_equity_pct_rank_4q},
    "bsd_169_cashnequiv_pct_rank_4q":                 {"inputs": ["cashnequiv"],                                                                 "func": bsd_169_cashnequiv_pct_rank_4q},
    "bsd_170_debt_pct_rank_8q":                       {"inputs": ["debt"],                                                                       "func": bsd_170_debt_pct_rank_8q},
    "bsd_171_retearn_drawdown_from_8q_peak":          {"inputs": ["retearn"],                                                                    "func": bsd_171_retearn_drawdown_from_8q_peak},
    "bsd_172_workingcapital_drawdown_from_8q_peak":   {"inputs": ["workingcapital"],                                                             "func": bsd_172_workingcapital_drawdown_from_8q_peak},
    "bsd_173_invcap_pct_drawdown_from_4q_peak":       {"inputs": ["invcap"],                                                                     "func": bsd_173_invcap_pct_drawdown_from_4q_peak},
    "bsd_174_bs_deterioration_count_yoy_4lines":      {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_174_bs_deterioration_count_yoy_4lines},
    "bsd_175_bs_health_index_3y_vs_1y":               {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],                             "func": bsd_175_bs_health_index_3y_vs_1y},
}
