"""
64_liquidity_distress — Base Features 001-075
Domain: short-term liquidity collapse — current ratio, quick/acid ratio, cash ratio,
        defensive-interval measures, QoQ/YoY ratio declines, below-1.0 breaches,
        drawdown from trailing peak, speed of liquidity erosion, net-current-asset
        coverage, cash-vs-liabilities adequacy.
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


# ── Derived ratio builders (used across multiple features) ────────────────────

def _current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current assets / current liabilities."""
    return _safe_div(assetsc, liabilitiesc)


def _quick_ratio(assetsc: pd.Series, inventory: pd.Series,
                 liabilitiesc: pd.Series) -> pd.Series:
    """(Current assets - inventory) / current liabilities."""
    return _safe_div(assetsc - inventory, liabilitiesc)


def _cash_ratio(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash & equivalents / current liabilities."""
    return _safe_div(cashnequiv, liabilitiesc)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Level ratios — current, quick, cash ---

def lqd_001_current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio: current assets / current liabilities."""
    return _current_ratio(assetsc, liabilitiesc)


def lqd_002_quick_ratio(assetsc: pd.Series, inventory: pd.Series,
                        liabilitiesc: pd.Series) -> pd.Series:
    """Quick (acid-test) ratio: (current assets - inventory) / current liabilities."""
    return _quick_ratio(assetsc, inventory, liabilitiesc)


def lqd_003_cash_ratio(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash ratio: cash & equivalents / current liabilities."""
    return _cash_ratio(cashnequiv, liabilitiesc)


def lqd_004_receivables_ratio(receivables: pd.Series,
                               liabilitiesc: pd.Series) -> pd.Series:
    """Receivables / current liabilities — liquid near-cash coverage."""
    return _safe_div(receivables, liabilitiesc)


def lqd_005_investmentsc_ratio(investmentsc: pd.Series,
                                liabilitiesc: pd.Series) -> pd.Series:
    """Short-term investments / current liabilities."""
    return _safe_div(investmentsc, liabilitiesc)


def lqd_006_cash_plus_receivables_ratio(cashnequiv: pd.Series, receivables: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """(Cash + receivables) / current liabilities — narrow defensive coverage."""
    return _safe_div(cashnequiv + receivables, liabilitiesc)


def lqd_007_cash_plus_investmentsc_ratio(cashnequiv: pd.Series, investmentsc: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """(Cash + short-term investments) / current liabilities."""
    return _safe_div(cashnequiv + investmentsc, liabilitiesc)


def lqd_008_nca_coverage(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Net current assets (working capital) divided by current liabilities: (CA-CL)/CL."""
    return _safe_div(assetsc - liabilitiesc, liabilitiesc)


def lqd_009_inventory_to_current_assets(inventory: pd.Series,
                                          assetsc: pd.Series) -> pd.Series:
    """Inventory as fraction of current assets — illiquid component weight."""
    return _safe_div(inventory, assetsc)


def lqd_010_cash_to_current_assets(cashnequiv: pd.Series,
                                    assetsc: pd.Series) -> pd.Series:
    """Cash as fraction of current assets — most-liquid component share."""
    return _safe_div(cashnequiv, assetsc)


def lqd_011_receivables_to_current_assets(receivables: pd.Series,
                                           assetsc: pd.Series) -> pd.Series:
    """Receivables as fraction of current assets."""
    return _safe_div(receivables, assetsc)


def lqd_012_current_liab_to_total_liab(liabilitiesc: pd.Series,
                                        liabilities: pd.Series) -> pd.Series:
    """Current liabilities as fraction of total liabilities — short-term pressure."""
    return _safe_div(liabilitiesc, liabilities)


def lqd_013_current_liab_to_total_assets(liabilitiesc: pd.Series,
                                          assets: pd.Series) -> pd.Series:
    """Current liabilities divided by total assets."""
    return _safe_div(liabilitiesc, assets)


def lqd_014_cash_to_total_assets(cashnequiv: pd.Series,
                                  assets: pd.Series) -> pd.Series:
    """Cash & equivalents divided by total assets."""
    return _safe_div(cashnequiv, assets)


def lqd_015_working_capital_ratio(assetsc: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """Absolute working capital = assetsc - liabilitiesc (level, not ratio)."""
    return assetsc - liabilitiesc


# --- Group B (016-030): QoQ and YoY ratio changes ---

def lqd_016_current_ratio_qoq_change(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """QoQ absolute change in current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_QTR)


def lqd_017_current_ratio_yoy_change(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """YoY absolute change in current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_YEAR)


def lqd_018_quick_ratio_qoq_change(assetsc: pd.Series, inventory: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """QoQ absolute change in quick ratio."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - qr.shift(_TD_QTR)


def lqd_019_quick_ratio_yoy_change(assetsc: pd.Series, inventory: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """YoY absolute change in quick ratio."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - qr.shift(_TD_YEAR)


def lqd_020_cash_ratio_qoq_change(cashnequiv: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """QoQ absolute change in cash ratio."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - cr.shift(_TD_QTR)


def lqd_021_cash_ratio_yoy_change(cashnequiv: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """YoY absolute change in cash ratio."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - cr.shift(_TD_YEAR)


def lqd_022_current_ratio_qoq_pct(assetsc: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """QoQ percent change in current ratio."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    prior = cr.shift(_TD_QTR)
    return _safe_div_abs(cr - prior, prior)


def lqd_023_current_ratio_yoy_pct(assetsc: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """YoY percent change in current ratio."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    prior = cr.shift(_TD_YEAR)
    return _safe_div_abs(cr - prior, prior)


def lqd_024_quick_ratio_qoq_pct(assetsc: pd.Series, inventory: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """QoQ percent change in quick ratio."""
    qr    = _quick_ratio(assetsc, inventory, liabilitiesc)
    prior = qr.shift(_TD_QTR)
    return _safe_div_abs(qr - prior, prior)


def lqd_025_cash_ratio_qoq_pct(cashnequiv: pd.Series,
                                 liabilitiesc: pd.Series) -> pd.Series:
    """QoQ percent change in cash ratio."""
    cr    = _cash_ratio(cashnequiv, liabilitiesc)
    prior = cr.shift(_TD_QTR)
    return _safe_div_abs(cr - prior, prior)


def lqd_026_assetsc_qoq_pct(assetsc: pd.Series) -> pd.Series:
    """QoQ percent change in current assets."""
    prior = assetsc.shift(_TD_QTR)
    return _safe_div_abs(assetsc - prior, prior)


def lqd_027_liabilitiesc_qoq_pct(liabilitiesc: pd.Series) -> pd.Series:
    """QoQ percent change in current liabilities."""
    prior = liabilitiesc.shift(_TD_QTR)
    return _safe_div_abs(liabilitiesc - prior, prior)


def lqd_028_cashnequiv_qoq_pct(cashnequiv: pd.Series) -> pd.Series:
    """QoQ percent change in cash & equivalents."""
    prior = cashnequiv.shift(_TD_QTR)
    return _safe_div_abs(cashnequiv - prior, prior)


def lqd_029_assetsc_yoy_pct(assetsc: pd.Series) -> pd.Series:
    """YoY percent change in current assets."""
    prior = assetsc.shift(_TD_YEAR)
    return _safe_div_abs(assetsc - prior, prior)


def lqd_030_liabilitiesc_yoy_pct(liabilitiesc: pd.Series) -> pd.Series:
    """YoY percent change in current liabilities."""
    prior = liabilitiesc.shift(_TD_YEAR)
    return _safe_div_abs(liabilitiesc - prior, prior)


# --- Group C (031-045): Breach of 1.0 and distress threshold flags ---

def lqd_031_current_ratio_below_1(assetsc: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if current ratio < 1.0 (current liabilities exceed current assets)."""
    return (_current_ratio(assetsc, liabilitiesc) < 1.0).astype(float)


def lqd_032_quick_ratio_below_1(assetsc: pd.Series, inventory: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if quick ratio < 1.0."""
    return (_quick_ratio(assetsc, inventory, liabilitiesc) < 1.0).astype(float)


def lqd_033_cash_ratio_below_05(cashnequiv: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if cash ratio < 0.5."""
    return (_cash_ratio(cashnequiv, liabilitiesc) < 0.5).astype(float)


def lqd_034_cash_ratio_below_02(cashnequiv: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if cash ratio < 0.2 (severe cash shortage)."""
    return (_cash_ratio(cashnequiv, liabilitiesc) < 0.2).astype(float)


def lqd_035_current_ratio_below_075(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if current ratio < 0.75 (severe undercoverage)."""
    return (_current_ratio(assetsc, liabilitiesc) < 0.75).astype(float)


def lqd_036_working_capital_negative(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if working capital (assetsc - liabilitiesc) < 0."""
    return ((assetsc - liabilitiesc) < 0).astype(float)


def lqd_037_cashnequiv_below_debtc(cashnequiv: pd.Series,
                                    debtc: pd.Series) -> pd.Series:
    """Binary: 1 if cash < short-term debt (can't cover maturing debt with cash)."""
    return (cashnequiv < debtc).astype(float)


def lqd_038_below_1_quarters_1y(assetsc: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Count of rolling 252-day observations where current ratio < 1.0."""
    flag = (_current_ratio(assetsc, liabilitiesc) < 1.0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def lqd_039_below_1_quarters_2y(assetsc: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Count of rolling 504-day observations where current ratio < 1.0."""
    flag = (_current_ratio(assetsc, liabilitiesc) < 1.0).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def lqd_040_current_ratio_turned_below_1(assetsc: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """1 on the first day current ratio falls below 1.0 from above."""
    cr     = _current_ratio(assetsc, liabilitiesc)
    now    = (cr < 1.0).astype(float)
    before = (cr.shift(_TD_QTR) >= 1.0).astype(float)
    return now * before


def lqd_041_quick_ratio_turned_below_1(assetsc: pd.Series, inventory: pd.Series,
                                        liabilitiesc: pd.Series) -> pd.Series:
    """1 when quick ratio drops below 1.0 from >= 1.0 in prior quarter."""
    qr     = _quick_ratio(assetsc, inventory, liabilitiesc)
    now    = (qr < 1.0).astype(float)
    before = (qr.shift(_TD_QTR) >= 1.0).astype(float)
    return now * before


def lqd_042_liabilitiesc_exceeds_cashnequiv_mult(cashnequiv: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Ratio of current liabilities to cash (inverse cash ratio) — times covered."""
    return _safe_div(liabilitiesc, cashnequiv)


def lqd_043_debtc_to_cashnequiv(debtc: pd.Series,
                                  cashnequiv: pd.Series) -> pd.Series:
    """Short-term debt / cash — immediate debt burden relative to cash on hand."""
    return _safe_div(debtc, cashnequiv)


def lqd_044_payables_to_cashnequiv(payables: pd.Series,
                                    cashnequiv: pd.Series) -> pd.Series:
    """Accounts payable / cash — near-term payables relative to cash."""
    return _safe_div(payables, cashnequiv)


def lqd_045_both_ratios_below_1_flag(assetsc: pd.Series, inventory: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """1 when both current ratio AND quick ratio are below 1.0 simultaneously."""
    cr = _current_ratio(assetsc, liabilitiesc)
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return ((cr < 1.0) & (qr < 1.0)).astype(float)


# --- Group D (046-060): Drawdown from trailing peak ---

def lqd_046_current_ratio_drawdown_4q(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its 4-quarter (252-day) trailing peak."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - _rolling_max(cr, _TD_YEAR)


def lqd_047_current_ratio_drawdown_8q(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its 8-quarter (504-day) trailing peak."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - _rolling_max(cr, _TD_2Y)


def lqd_048_current_ratio_drawdown_12q(assetsc: pd.Series,
                                        liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its 12-quarter (756-day) trailing peak."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - _rolling_max(cr, _TD_3Y)


def lqd_049_current_ratio_pct_drawdown_4q(assetsc: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of current ratio from its 4-quarter peak."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = _rolling_max(cr, _TD_YEAR)
    return _safe_div_abs(cr - peak, peak)


def lqd_050_quick_ratio_drawdown_4q(assetsc: pd.Series, inventory: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio minus its 4-quarter trailing peak."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - _rolling_max(qr, _TD_YEAR)


def lqd_051_quick_ratio_pct_drawdown_4q(assetsc: pd.Series, inventory: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of quick ratio from its 4-quarter peak."""
    qr   = _quick_ratio(assetsc, inventory, liabilitiesc)
    peak = _rolling_max(qr, _TD_YEAR)
    return _safe_div_abs(qr - peak, peak)


def lqd_052_cash_ratio_drawdown_4q(cashnequiv: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Cash ratio minus its 4-quarter trailing peak."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - _rolling_max(cr, _TD_YEAR)


def lqd_053_cash_ratio_pct_drawdown_8q(cashnequiv: pd.Series,
                                        liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of cash ratio from its 8-quarter peak."""
    cr   = _cash_ratio(cashnequiv, liabilitiesc)
    peak = _rolling_max(cr, _TD_2Y)
    return _safe_div_abs(cr - peak, peak)


def lqd_054_cashnequiv_drawdown_from_4q_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash & equivalents level minus its 4-quarter rolling maximum."""
    return cashnequiv - _rolling_max(cashnequiv, _TD_YEAR)


def lqd_055_cashnequiv_pct_drawdown_from_4q_peak(cashnequiv: pd.Series) -> pd.Series:
    """Percent drawdown of cash & equivalents from its 4-quarter peak."""
    peak = _rolling_max(cashnequiv, _TD_YEAR)
    return _safe_div_abs(cashnequiv - peak, peak)


def lqd_056_current_ratio_drawdown_expanding_peak(assetsc: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its all-history expanding maximum."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = cr.expanding(min_periods=1).max()
    return cr - peak


def lqd_057_current_ratio_pct_drawdown_expanding(assetsc: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of current ratio from its all-history expanding peak."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    peak = cr.expanding(min_periods=1).max()
    return _safe_div_abs(cr - peak, peak)


def lqd_058_quick_ratio_drawdown_expanding(assetsc: pd.Series, inventory: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio minus its all-history expanding maximum."""
    qr   = _quick_ratio(assetsc, inventory, liabilitiesc)
    peak = qr.expanding(min_periods=1).max()
    return qr - peak


def lqd_059_assetsc_vs_4q_avg(assetsc: pd.Series) -> pd.Series:
    """Current assets minus trailing 4-quarter mean — level deviation."""
    return assetsc - _rolling_mean(assetsc, _TD_YEAR)


def lqd_060_liabilitiesc_vs_4q_avg(liabilitiesc: pd.Series) -> pd.Series:
    """Current liabilities minus trailing 4-quarter mean — liability growth signal."""
    return liabilitiesc - _rolling_mean(liabilitiesc, _TD_YEAR)


# --- Group E (061-075): Z-score, percentile rank, trailing range, composite ---

def lqd_061_current_ratio_zscore_4q(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current ratio within a trailing 4-quarter (252-day) window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _zscore_rolling(cr, _TD_YEAR)


def lqd_062_current_ratio_zscore_8q(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current ratio within a trailing 8-quarter (504-day) window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _zscore_rolling(cr, _TD_2Y)


def lqd_063_current_ratio_zscore_12q(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current ratio within a trailing 12-quarter (756-day) window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _zscore_rolling(cr, _TD_3Y)


def lqd_064_quick_ratio_zscore_4q(assetsc: pd.Series, inventory: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of quick ratio within a trailing 4-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _zscore_rolling(qr, _TD_YEAR)


def lqd_065_cash_ratio_zscore_4q(cashnequiv: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of cash ratio within a trailing 4-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _zscore_rolling(cr, _TD_YEAR)


def lqd_066_current_ratio_pct_rank_4q(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of current ratio within trailing 4-quarter window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_YEAR)


def lqd_067_current_ratio_pct_rank_8q(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of current ratio within trailing 8-quarter window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_2Y)


def lqd_068_current_ratio_expanding_pct_rank(assetsc: pd.Series,
                                              liabilitiesc: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr.expanding(min_periods=2).rank(pct=True)


def lqd_069_current_ratio_range_position_4q(assetsc: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """Position of current ratio within its 4-quarter [min, max] range: (cr-min)/(max-min)."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    lo  = _rolling_min(cr, _TD_YEAR)
    hi  = _rolling_max(cr, _TD_YEAR)
    return _safe_div(cr - lo, hi - lo)


def lqd_070_quick_ratio_pct_rank_4q(assetsc: pd.Series, inventory: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of quick ratio within trailing 4-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _rolling_rank_pct(qr, _TD_YEAR)


def lqd_071_current_ratio_ewm_deviation(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its EWM (span=252) — momentum deviation signal."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    ewm = _ewm_mean(cr, _TD_YEAR)
    return cr - ewm


def lqd_072_cash_ratio_pct_rank_4q(cashnequiv: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of cash ratio within trailing 4-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_YEAR)


def lqd_073_current_ratio_consecutive_decline_streak(assetsc: pd.Series,
                                                      liabilitiesc: pd.Series) -> pd.Series:
    """
    Current consecutive-decline streak in current ratio (in daily observations).
    Resets to 0 on any day when current ratio rises vs prior day.
    """
    cr     = _current_ratio(assetsc, liabilitiesc)
    down   = (cr < cr.shift(1)).astype(int)
    arr    = down.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=assetsc.index)


def lqd_074_liquidity_distress_composite_3ratio(assetsc: pd.Series, inventory: pd.Series,
                                                 cashnequiv: pd.Series,
                                                 liabilitiesc: pd.Series) -> pd.Series:
    """
    Composite liquidity-distress score: equally weighted z-score sum of
    current ratio, quick ratio, and cash ratio within a 4-quarter window.
    Lower (more negative) = more stressed.
    """
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    z_cr  = _zscore_rolling(cr,  _TD_YEAR)
    z_qr  = _zscore_rolling(qr,  _TD_YEAR)
    z_car = _zscore_rolling(car, _TD_YEAR)
    return (z_cr + z_qr + z_car) / 3.0


def lqd_075_current_ratio_2y_change(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in current ratio over 2 years (504-day lag)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_2Y)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

LIQUIDITY_DISTRESS_REGISTRY_001_075 = {
    "lqd_001_current_ratio":                         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_001_current_ratio},
    "lqd_002_quick_ratio":                           {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_002_quick_ratio},
    "lqd_003_cash_ratio":                            {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_003_cash_ratio},
    "lqd_004_receivables_ratio":                     {"inputs": ["receivables", "liabilitiesc"],                          "func": lqd_004_receivables_ratio},
    "lqd_005_investmentsc_ratio":                    {"inputs": ["investmentsc", "liabilitiesc"],                         "func": lqd_005_investmentsc_ratio},
    "lqd_006_cash_plus_receivables_ratio":           {"inputs": ["cashnequiv", "receivables", "liabilitiesc"],            "func": lqd_006_cash_plus_receivables_ratio},
    "lqd_007_cash_plus_investmentsc_ratio":          {"inputs": ["cashnequiv", "investmentsc", "liabilitiesc"],           "func": lqd_007_cash_plus_investmentsc_ratio},
    "lqd_008_nca_coverage":                          {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_008_nca_coverage},
    "lqd_009_inventory_to_current_assets":           {"inputs": ["inventory", "assetsc"],                                 "func": lqd_009_inventory_to_current_assets},
    "lqd_010_cash_to_current_assets":                {"inputs": ["cashnequiv", "assetsc"],                                "func": lqd_010_cash_to_current_assets},
    "lqd_011_receivables_to_current_assets":         {"inputs": ["receivables", "assetsc"],                               "func": lqd_011_receivables_to_current_assets},
    "lqd_012_current_liab_to_total_liab":            {"inputs": ["liabilitiesc", "liabilities"],                          "func": lqd_012_current_liab_to_total_liab},
    "lqd_013_current_liab_to_total_assets":          {"inputs": ["liabilitiesc", "assets"],                               "func": lqd_013_current_liab_to_total_assets},
    "lqd_014_cash_to_total_assets":                  {"inputs": ["cashnequiv", "assets"],                                 "func": lqd_014_cash_to_total_assets},
    "lqd_015_working_capital_ratio":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_015_working_capital_ratio},
    "lqd_016_current_ratio_qoq_change":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_016_current_ratio_qoq_change},
    "lqd_017_current_ratio_yoy_change":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_017_current_ratio_yoy_change},
    "lqd_018_quick_ratio_qoq_change":                {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_018_quick_ratio_qoq_change},
    "lqd_019_quick_ratio_yoy_change":                {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_019_quick_ratio_yoy_change},
    "lqd_020_cash_ratio_qoq_change":                 {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_020_cash_ratio_qoq_change},
    "lqd_021_cash_ratio_yoy_change":                 {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_021_cash_ratio_yoy_change},
    "lqd_022_current_ratio_qoq_pct":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_022_current_ratio_qoq_pct},
    "lqd_023_current_ratio_yoy_pct":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_023_current_ratio_yoy_pct},
    "lqd_024_quick_ratio_qoq_pct":                   {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_024_quick_ratio_qoq_pct},
    "lqd_025_cash_ratio_qoq_pct":                    {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_025_cash_ratio_qoq_pct},
    "lqd_026_assetsc_qoq_pct":                       {"inputs": ["assetsc"],                                              "func": lqd_026_assetsc_qoq_pct},
    "lqd_027_liabilitiesc_qoq_pct":                  {"inputs": ["liabilitiesc"],                                         "func": lqd_027_liabilitiesc_qoq_pct},
    "lqd_028_cashnequiv_qoq_pct":                    {"inputs": ["cashnequiv"],                                           "func": lqd_028_cashnequiv_qoq_pct},
    "lqd_029_assetsc_yoy_pct":                       {"inputs": ["assetsc"],                                              "func": lqd_029_assetsc_yoy_pct},
    "lqd_030_liabilitiesc_yoy_pct":                  {"inputs": ["liabilitiesc"],                                         "func": lqd_030_liabilitiesc_yoy_pct},
    "lqd_031_current_ratio_below_1":                 {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_031_current_ratio_below_1},
    "lqd_032_quick_ratio_below_1":                   {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_032_quick_ratio_below_1},
    "lqd_033_cash_ratio_below_05":                   {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_033_cash_ratio_below_05},
    "lqd_034_cash_ratio_below_02":                   {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_034_cash_ratio_below_02},
    "lqd_035_current_ratio_below_075":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_035_current_ratio_below_075},
    "lqd_036_working_capital_negative":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_036_working_capital_negative},
    "lqd_037_cashnequiv_below_debtc":                {"inputs": ["cashnequiv", "debtc"],                                  "func": lqd_037_cashnequiv_below_debtc},
    "lqd_038_below_1_quarters_1y":                   {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_038_below_1_quarters_1y},
    "lqd_039_below_1_quarters_2y":                   {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_039_below_1_quarters_2y},
    "lqd_040_current_ratio_turned_below_1":          {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_040_current_ratio_turned_below_1},
    "lqd_041_quick_ratio_turned_below_1":            {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_041_quick_ratio_turned_below_1},
    "lqd_042_liabilitiesc_exceeds_cashnequiv_mult":  {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_042_liabilitiesc_exceeds_cashnequiv_mult},
    "lqd_043_debtc_to_cashnequiv":                   {"inputs": ["debtc", "cashnequiv"],                                  "func": lqd_043_debtc_to_cashnequiv},
    "lqd_044_payables_to_cashnequiv":                {"inputs": ["payables", "cashnequiv"],                               "func": lqd_044_payables_to_cashnequiv},
    "lqd_045_both_ratios_below_1_flag":              {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_045_both_ratios_below_1_flag},
    "lqd_046_current_ratio_drawdown_4q":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_046_current_ratio_drawdown_4q},
    "lqd_047_current_ratio_drawdown_8q":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_047_current_ratio_drawdown_8q},
    "lqd_048_current_ratio_drawdown_12q":            {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_048_current_ratio_drawdown_12q},
    "lqd_049_current_ratio_pct_drawdown_4q":         {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_049_current_ratio_pct_drawdown_4q},
    "lqd_050_quick_ratio_drawdown_4q":               {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_050_quick_ratio_drawdown_4q},
    "lqd_051_quick_ratio_pct_drawdown_4q":           {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_051_quick_ratio_pct_drawdown_4q},
    "lqd_052_cash_ratio_drawdown_4q":                {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_052_cash_ratio_drawdown_4q},
    "lqd_053_cash_ratio_pct_drawdown_8q":            {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_053_cash_ratio_pct_drawdown_8q},
    "lqd_054_cashnequiv_drawdown_from_4q_peak":      {"inputs": ["cashnequiv"],                                           "func": lqd_054_cashnequiv_drawdown_from_4q_peak},
    "lqd_055_cashnequiv_pct_drawdown_from_4q_peak":  {"inputs": ["cashnequiv"],                                           "func": lqd_055_cashnequiv_pct_drawdown_from_4q_peak},
    "lqd_056_current_ratio_drawdown_expanding_peak": {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_056_current_ratio_drawdown_expanding_peak},
    "lqd_057_current_ratio_pct_drawdown_expanding":  {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_057_current_ratio_pct_drawdown_expanding},
    "lqd_058_quick_ratio_drawdown_expanding":        {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_058_quick_ratio_drawdown_expanding},
    "lqd_059_assetsc_vs_4q_avg":                     {"inputs": ["assetsc"],                                              "func": lqd_059_assetsc_vs_4q_avg},
    "lqd_060_liabilitiesc_vs_4q_avg":                {"inputs": ["liabilitiesc"],                                         "func": lqd_060_liabilitiesc_vs_4q_avg},
    "lqd_061_current_ratio_zscore_4q":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_061_current_ratio_zscore_4q},
    "lqd_062_current_ratio_zscore_8q":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_062_current_ratio_zscore_8q},
    "lqd_063_current_ratio_zscore_12q":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_063_current_ratio_zscore_12q},
    "lqd_064_quick_ratio_zscore_4q":                 {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_064_quick_ratio_zscore_4q},
    "lqd_065_cash_ratio_zscore_4q":                  {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_065_cash_ratio_zscore_4q},
    "lqd_066_current_ratio_pct_rank_4q":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_066_current_ratio_pct_rank_4q},
    "lqd_067_current_ratio_pct_rank_8q":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_067_current_ratio_pct_rank_8q},
    "lqd_068_current_ratio_expanding_pct_rank":      {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_068_current_ratio_expanding_pct_rank},
    "lqd_069_current_ratio_range_position_4q":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_069_current_ratio_range_position_4q},
    "lqd_070_quick_ratio_pct_rank_4q":               {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_070_quick_ratio_pct_rank_4q},
    "lqd_071_current_ratio_ewm_deviation":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_071_current_ratio_ewm_deviation},
    "lqd_072_cash_ratio_pct_rank_4q":                {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_072_cash_ratio_pct_rank_4q},
    "lqd_073_current_ratio_consecutive_decline_streak": {"inputs": ["assetsc", "liabilitiesc"],                           "func": lqd_073_current_ratio_consecutive_decline_streak},
    "lqd_074_liquidity_distress_composite_3ratio":   {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_074_liquidity_distress_composite_3ratio},
    "lqd_075_current_ratio_2y_change":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_075_current_ratio_2y_change},
}
