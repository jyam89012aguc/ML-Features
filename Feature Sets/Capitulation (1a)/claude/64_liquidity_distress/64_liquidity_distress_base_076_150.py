"""
64_liquidity_distress — Base Features 076-150
Domain: short-term liquidity collapse — multi-period ratio trajectories, consecutive
        declining-liquidity quarters, speed of liquidity erosion, net-current-asset
        coverage depth, cash-adequacy vs obligations, trailing-window averages,
        receivables/inventory dynamics, and advanced cross-ratio interactions.
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


# ── Derived ratio builders ────────────────────────────────────────────────────

def _current_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return _safe_div(assetsc, liabilitiesc)


def _quick_ratio(assetsc: pd.Series, inventory: pd.Series,
                 liabilitiesc: pd.Series) -> pd.Series:
    return _safe_div(assetsc - inventory, liabilitiesc)


def _cash_ratio(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    return _safe_div(cashnequiv, liabilitiesc)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Multi-period ratio trajectories and trends ---

def lqd_076_current_ratio_3y_change(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in current ratio over 3 years (756-day lag)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - cr.shift(_TD_3Y)


def lqd_077_current_ratio_3y_pct_change(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """Percent change in current ratio over 3 years."""
    cr    = _current_ratio(assetsc, liabilitiesc)
    prior = cr.shift(_TD_3Y)
    return _safe_div_abs(cr - prior, prior)


def lqd_078_quick_ratio_2y_change(assetsc: pd.Series, inventory: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in quick ratio over 2 years (504-day lag)."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - qr.shift(_TD_2Y)


def lqd_079_cash_ratio_2y_change(cashnequiv: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Absolute change in cash ratio over 2 years (504-day lag)."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return cr - cr.shift(_TD_2Y)


def lqd_080_cashnequiv_yoy_change(cashnequiv: pd.Series) -> pd.Series:
    """Absolute YoY change in cash & equivalents."""
    return cashnequiv - cashnequiv.shift(_TD_YEAR)


def lqd_081_cashnequiv_2y_change(cashnequiv: pd.Series) -> pd.Series:
    """Absolute 2-year change in cash & equivalents."""
    return cashnequiv - cashnequiv.shift(_TD_2Y)


def lqd_082_assetsc_2y_change(assetsc: pd.Series) -> pd.Series:
    """Absolute 2-year change in current assets."""
    return assetsc - assetsc.shift(_TD_2Y)


def lqd_083_liabilitiesc_2y_change(liabilitiesc: pd.Series) -> pd.Series:
    """Absolute 2-year change in current liabilities."""
    return liabilitiesc - liabilitiesc.shift(_TD_2Y)


def lqd_084_current_ratio_4q_avg(assetsc: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Trailing 4-quarter (252-day) mean of current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_mean(cr, _TD_YEAR)


def lqd_085_current_ratio_8q_avg(assetsc: pd.Series,
                                  liabilitiesc: pd.Series) -> pd.Series:
    """Trailing 8-quarter (504-day) mean of current ratio."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_mean(cr, _TD_2Y)


def lqd_086_quick_ratio_4q_avg(assetsc: pd.Series, inventory: pd.Series,
                                 liabilitiesc: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of quick ratio."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _rolling_mean(qr, _TD_YEAR)


def lqd_087_cash_ratio_4q_avg(cashnequiv: pd.Series,
                                liabilitiesc: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of cash ratio."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_mean(cr, _TD_YEAR)


def lqd_088_current_ratio_vs_4q_avg(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its trailing 4-quarter mean."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - _rolling_mean(cr, _TD_YEAR)


def lqd_089_current_ratio_vs_8q_avg(assetsc: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its trailing 8-quarter mean."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - _rolling_mean(cr, _TD_2Y)


def lqd_090_quick_ratio_vs_4q_avg(assetsc: pd.Series, inventory: pd.Series,
                                   liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio minus its trailing 4-quarter mean."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - _rolling_mean(qr, _TD_YEAR)


# --- Group G (091-105): Consecutive decline and erosion speed ---

def lqd_091_current_ratio_declining_qtrs_1y(assetsc: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """Count of 252-day window observations where current ratio declined QoQ."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    down = (cr < cr.shift(_TD_QTR)).astype(float)
    return _rolling_sum(down, _TD_YEAR)


def lqd_092_current_ratio_declining_qtrs_2y(assetsc: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """Count of 504-day window observations where current ratio declined QoQ."""
    cr   = _current_ratio(assetsc, liabilitiesc)
    down = (cr < cr.shift(_TD_QTR)).astype(float)
    return _rolling_sum(down, _TD_2Y)


def lqd_093_quick_ratio_declining_qtrs_1y(assetsc: pd.Series, inventory: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """Count of 252-day observations where quick ratio declined QoQ."""
    qr   = _quick_ratio(assetsc, inventory, liabilitiesc)
    down = (qr < qr.shift(_TD_QTR)).astype(float)
    return _rolling_sum(down, _TD_YEAR)


def lqd_094_cash_declining_qtrs_1y(cashnequiv: pd.Series) -> pd.Series:
    """Count of 252-day observations where cash & equivalents declined QoQ."""
    down = (cashnequiv < cashnequiv.shift(_TD_QTR)).astype(float)
    return _rolling_sum(down, _TD_YEAR)


def lqd_095_current_ratio_speed_of_erosion_1q(assetsc: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """Speed of current ratio erosion: QoQ change clipped to <= 0 (negative only)."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    chg = cr - cr.shift(_TD_QTR)
    return chg.clip(upper=0)


def lqd_096_current_ratio_speed_of_erosion_yoy(assetsc: pd.Series,
                                                liabilitiesc: pd.Series) -> pd.Series:
    """YoY current ratio decline clipped to <= 0."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    chg = cr - cr.shift(_TD_YEAR)
    return chg.clip(upper=0)


def lqd_097_cashnequiv_burn_rate_qoq(cashnequiv: pd.Series) -> pd.Series:
    """QoQ decline in cash (negative = cash burn): cash - prior-quarter cash, <= 0."""
    chg = cashnequiv - cashnequiv.shift(_TD_QTR)
    return chg.clip(upper=0)


def lqd_098_cashnequiv_burn_rate_yoy(cashnequiv: pd.Series) -> pd.Series:
    """YoY decline in cash clipped to <= 0."""
    chg = cashnequiv - cashnequiv.shift(_TD_YEAR)
    return chg.clip(upper=0)


def lqd_099_liabilitiesc_growth_qoq(liabilitiesc: pd.Series) -> pd.Series:
    """QoQ growth in current liabilities clipped to >= 0 (increase only)."""
    chg = liabilitiesc - liabilitiesc.shift(_TD_QTR)
    return chg.clip(lower=0)


def lqd_100_liabilitiesc_growth_yoy(liabilitiesc: pd.Series) -> pd.Series:
    """YoY growth in current liabilities clipped to >= 0."""
    chg = liabilitiesc - liabilitiesc.shift(_TD_YEAR)
    return chg.clip(lower=0)


def lqd_101_current_ratio_distance_to_1(assetsc: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """
    Distance of current ratio to the 1.0 distress threshold: (assetsc/liabilitiesc) - 1.0.
    Negative = current assets already below current liabilities (distress zone).
    """
    cr = _current_ratio(assetsc, liabilitiesc)
    return cr - 1.0


def lqd_102_quick_ratio_distance_to_1(assetsc: pd.Series, inventory: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """
    Distance of quick ratio to the 1.0 distress threshold: ((assetsc-inventory)/liabilitiesc) - 1.0.
    Negative = quick assets cannot cover current liabilities.
    """
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return qr - 1.0


def lqd_103_cash_ratio_pct_rank_12q(cashnequiv: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """
    Percentile rank of cash ratio within the trailing 12-quarter (756-day) window.
    Low rank = cash ratio is near its worst level over 3 years.
    """
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_3Y)


def lqd_104_current_ratio_worst_4q(assetsc: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Worst (minimum) current ratio over trailing 4 quarters (252 days)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_min(cr, _TD_YEAR)


def lqd_105_current_ratio_worst_8q(assetsc: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Worst (minimum) current ratio over trailing 8 quarters (504 days)."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_min(cr, _TD_2Y)


# --- Group H (106-120): Net-current-asset and cash-adequacy measures ---

def lqd_106_net_current_assets_4q_avg(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of net current assets (working capital)."""
    nca = assetsc - liabilitiesc
    return _rolling_mean(nca, _TD_YEAR)


def lqd_107_net_current_assets_drawdown_from_peak(assetsc: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """Net current assets minus their 4-quarter rolling maximum."""
    nca  = assetsc - liabilitiesc
    peak = _rolling_max(nca, _TD_YEAR)
    return nca - peak


def lqd_108_net_current_assets_pct_drawdown(assetsc: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """Percent drawdown of net current assets from 4-quarter peak."""
    nca  = assetsc - liabilitiesc
    peak = _rolling_max(nca, _TD_YEAR)
    return _safe_div_abs(nca - peak, peak)


def lqd_109_cashnequiv_to_liabilitiesc_shortfall(cashnequiv: pd.Series,
                                                  liabilitiesc: pd.Series) -> pd.Series:
    """Cash shortfall: cashnequiv - liabilitiesc (negative = unable to cover with cash)."""
    return cashnequiv - liabilitiesc


def lqd_110_cashnequiv_covers_debtc_fraction(cashnequiv: pd.Series,
                                              debtc: pd.Series) -> pd.Series:
    """Fraction of short-term debt covered by cash (cashnequiv / debtc)."""
    return _safe_div(cashnequiv, debtc)


def lqd_111_liquid_assets_to_liabilitiesc(cashnequiv: pd.Series, receivables: pd.Series,
                                           investmentsc: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """(Cash + receivables + short-term investments) / current liabilities."""
    liquid = cashnequiv + receivables + investmentsc
    return _safe_div(liquid, liabilitiesc)


def lqd_112_cashnequiv_rolling_min_4q(cashnequiv: pd.Series) -> pd.Series:
    """Rolling 4-quarter minimum of cash & equivalents — floor of liquidity."""
    return _rolling_min(cashnequiv, _TD_YEAR)


def lqd_113_cashnequiv_rolling_min_8q(cashnequiv: pd.Series) -> pd.Series:
    """Rolling 8-quarter minimum of cash & equivalents."""
    return _rolling_min(cashnequiv, _TD_2Y)


def lqd_114_cashnequiv_vs_4q_avg(cashnequiv: pd.Series) -> pd.Series:
    """Cash vs its trailing 4-quarter mean — level deviation."""
    return cashnequiv - _rolling_mean(cashnequiv, _TD_YEAR)


def lqd_115_cashnequiv_pct_vs_4q_avg(cashnequiv: pd.Series) -> pd.Series:
    """Cash percent deviation from its trailing 4-quarter mean."""
    avg = _rolling_mean(cashnequiv, _TD_YEAR)
    return _safe_div_abs(cashnequiv - avg, avg)


def lqd_116_receivables_qoq_change(receivables: pd.Series) -> pd.Series:
    """QoQ absolute change in receivables."""
    return receivables - receivables.shift(_TD_QTR)


def lqd_117_receivables_yoy_change(receivables: pd.Series) -> pd.Series:
    """YoY absolute change in receivables."""
    return receivables - receivables.shift(_TD_YEAR)


def lqd_118_inventory_qoq_change(inventory: pd.Series) -> pd.Series:
    """QoQ absolute change in inventory."""
    return inventory - inventory.shift(_TD_QTR)


def lqd_119_inventory_yoy_change(inventory: pd.Series) -> pd.Series:
    """YoY absolute change in inventory."""
    return inventory - inventory.shift(_TD_YEAR)


def lqd_120_payables_qoq_change(payables: pd.Series) -> pd.Series:
    """QoQ absolute change in accounts payable."""
    return payables - payables.shift(_TD_QTR)


# --- Group I (121-135): Receivables and inventory liquidity dynamics ---

def lqd_121_receivables_to_liabilitiesc_ratio(receivables: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """Receivables / current liabilities over time."""
    return _safe_div(receivables, liabilitiesc)


def lqd_122_receivables_plus_cash_vs_liabilitiesc(receivables: pd.Series,
                                                   cashnequiv: pd.Series,
                                                   liabilitiesc: pd.Series) -> pd.Series:
    """(Receivables + cash) as a fraction of current liabilities."""
    return _safe_div(receivables + cashnequiv, liabilitiesc)


def lqd_123_inventory_growth_vs_assetsc_growth(inventory: pd.Series,
                                                assetsc: pd.Series) -> pd.Series:
    """
    Inventory QoQ growth rate minus current assets QoQ growth rate.
    Positive = inventory growing faster than current assets (illiquid buildup).
    """
    inv_g = _safe_div_abs(inventory - inventory.shift(_TD_QTR), inventory.shift(_TD_QTR))
    ca_g  = _safe_div_abs(assetsc - assetsc.shift(_TD_QTR), assetsc.shift(_TD_QTR))
    return inv_g - ca_g


def lqd_124_receivables_growth_vs_assetsc_growth(receivables: pd.Series,
                                                  assetsc: pd.Series) -> pd.Series:
    """
    Receivables QoQ growth minus current assets QoQ growth.
    Positive = receivables inflating faster (quality concern).
    """
    rec_g = _safe_div_abs(receivables - receivables.shift(_TD_QTR), receivables.shift(_TD_QTR))
    ca_g  = _safe_div_abs(assetsc - assetsc.shift(_TD_QTR), assetsc.shift(_TD_QTR))
    return rec_g - ca_g


def lqd_125_non_cash_current_assets_ratio(assetsc: pd.Series, cashnequiv: pd.Series,
                                           liabilitiesc: pd.Series) -> pd.Series:
    """(Current assets - cash) / current liabilities — non-cash liquidity coverage."""
    return _safe_div(assetsc - cashnequiv, liabilitiesc)


def lqd_126_inventory_coverage_of_liabilitiesc(inventory: pd.Series,
                                                liabilitiesc: pd.Series) -> pd.Series:
    """Inventory / current liabilities — illiquid asset coverage fraction."""
    return _safe_div(inventory, liabilitiesc)


def lqd_127_payables_to_liabilitiesc(payables: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """Accounts payable as fraction of current liabilities."""
    return _safe_div(payables, liabilitiesc)


def lqd_128_payables_to_receivables(payables: pd.Series,
                                     receivables: pd.Series) -> pd.Series:
    """Payables / receivables — indicates payment stress when > 1."""
    return _safe_div(payables, receivables)


def lqd_129_deferred_rev_to_liabilitiesc(deferredrev: pd.Series,
                                          liabilitiesc: pd.Series) -> pd.Series:
    """Deferred revenue / current liabilities — obligation weight."""
    return _safe_div(deferredrev, liabilitiesc)


def lqd_130_current_liab_qoq_vs_assetsc_qoq(liabilitiesc: pd.Series,
                                              assetsc: pd.Series) -> pd.Series:
    """
    QoQ pct change of current liabilities minus QoQ pct change of current assets.
    Positive = liabilities growing faster than assets (deteriorating coverage).
    """
    cl_g = _safe_div_abs(liabilitiesc - liabilitiesc.shift(_TD_QTR),
                         liabilitiesc.shift(_TD_QTR))
    ca_g = _safe_div_abs(assetsc - assetsc.shift(_TD_QTR), assetsc.shift(_TD_QTR))
    return cl_g - ca_g


def lqd_131_cashnequiv_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(cashnequiv, _TD_YEAR)


def lqd_132_cashnequiv_zscore_8q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 8-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_2Y)


def lqd_133_assetsc_zscore_4q(assetsc: pd.Series) -> pd.Series:
    """Z-score of current assets within trailing 4-quarter window."""
    return _zscore_rolling(assetsc, _TD_YEAR)


def lqd_134_liabilitiesc_zscore_4q(liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of current liabilities within trailing 4-quarter window."""
    return _zscore_rolling(liabilitiesc, _TD_YEAR)


def lqd_135_working_capital_zscore_4q(assetsc: pd.Series,
                                       liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of working capital (assetsc - liabilitiesc) within 4-quarter window."""
    wc = assetsc - liabilitiesc
    return _zscore_rolling(wc, _TD_YEAR)


# --- Group J (136-150): Advanced cross-ratio interactions and composite ---

def lqd_136_cr_minus_qr_gap(assetsc: pd.Series, inventory: pd.Series,
                              liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus quick ratio = inventory component of liquidity gap."""
    cr = _current_ratio(assetsc, liabilitiesc)
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return cr - qr


def lqd_137_qr_minus_cash_ratio_gap(assetsc: pd.Series, inventory: pd.Series,
                                     cashnequiv: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Quick ratio minus cash ratio = receivables/investments component gap."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    ca = _cash_ratio(cashnequiv, liabilitiesc)
    return qr - ca


def lqd_138_cr_minus_qr_gap_qoq_change(assetsc: pd.Series, inventory: pd.Series,
                                         liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in the (current ratio - quick ratio) gap — inventory illiquidity drift."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    gap = cr - qr
    return gap - gap.shift(_TD_QTR)


def lqd_139_current_ratio_pct_rank_12q(assetsc: pd.Series,
                                        liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of current ratio within trailing 12-quarter (756-day) window."""
    cr = _current_ratio(assetsc, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_3Y)


def lqd_140_quick_ratio_pct_rank_8q(assetsc: pd.Series, inventory: pd.Series,
                                     liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of quick ratio within trailing 8-quarter window."""
    qr = _quick_ratio(assetsc, inventory, liabilitiesc)
    return _rolling_rank_pct(qr, _TD_2Y)


def lqd_141_cash_ratio_pct_rank_8q(cashnequiv: pd.Series,
                                    liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of cash ratio within trailing 8-quarter window."""
    cr = _cash_ratio(cashnequiv, liabilitiesc)
    return _rolling_rank_pct(cr, _TD_2Y)


def lqd_142_current_ratio_median_deviation_4q(assetsc: pd.Series,
                                               liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio minus its trailing 4-quarter median."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    med = _rolling_median(cr, _TD_YEAR)
    return cr - med


def lqd_143_cash_ratio_median_deviation_4q(cashnequiv: pd.Series,
                                            liabilitiesc: pd.Series) -> pd.Series:
    """Cash ratio minus its trailing 4-quarter median."""
    cr  = _cash_ratio(cashnequiv, liabilitiesc)
    med = _rolling_median(cr, _TD_YEAR)
    return cr - med


def lqd_144_cashnequiv_pct_rank_4q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash & equivalents within trailing 4-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_YEAR)


def lqd_145_liabilitiesc_pct_rank_4q(liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of current liabilities within trailing 4-quarter window
    (high rank = stress; liabilities near multi-quarter high)."""
    return _rolling_rank_pct(liabilitiesc, _TD_YEAR)


def lqd_146_current_ratio_range_position_8q(assetsc: pd.Series,
                                             liabilitiesc: pd.Series) -> pd.Series:
    """Position of current ratio within its 8-quarter [min, max] range."""
    cr = _current_ratio(assetsc, liabilitiesc)
    lo = _rolling_min(cr, _TD_2Y)
    hi = _rolling_max(cr, _TD_2Y)
    return _safe_div(cr - lo, hi - lo)


def lqd_147_liabilitiesc_growth_outpacing_assetsc_flag(assetsc: pd.Series,
                                                        liabilitiesc: pd.Series) -> pd.Series:
    """Binary: 1 if current liabilities grew YoY AND current assets shrank YoY."""
    cl_grew   = (liabilitiesc > liabilitiesc.shift(_TD_YEAR)).astype(float)
    ca_shrunk = (assetsc < assetsc.shift(_TD_YEAR)).astype(float)
    return cl_grew * ca_shrunk


def lqd_148_triple_stress_flag(assetsc: pd.Series, inventory: pd.Series,
                                cashnequiv: pd.Series,
                                liabilitiesc: pd.Series) -> pd.Series:
    """1 when current ratio < 1.0, quick ratio < 1.0, AND cash ratio < 0.2."""
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    return ((cr < 1.0) & (qr < 1.0) & (car < 0.2)).astype(float)


def lqd_149_current_ratio_ewm_zscore(assetsc: pd.Series,
                                      liabilitiesc: pd.Series) -> pd.Series:
    """
    EWM-based z-score of current ratio: (cr - ewm_mean) / rolling_std,
    using span=252 EWM mean and 252-day rolling std.
    """
    cr  = _current_ratio(assetsc, liabilitiesc)
    mu  = _ewm_mean(cr, _TD_YEAR)
    sd  = _rolling_std(cr, _TD_YEAR)
    return _safe_div(cr - mu, sd)


def lqd_150_liquidity_distress_composite_4signal(assetsc: pd.Series,
                                                  inventory: pd.Series,
                                                  cashnequiv: pd.Series,
                                                  liabilitiesc: pd.Series) -> pd.Series:
    """
    Composite liquidity distress: equally weighted z-scores of current ratio,
    quick ratio, cash ratio, and net current assets within 4-quarter window.
    Lower = more distressed.
    """
    cr  = _current_ratio(assetsc, liabilitiesc)
    qr  = _quick_ratio(assetsc, inventory, liabilitiesc)
    car = _cash_ratio(cashnequiv, liabilitiesc)
    nca = assetsc - liabilitiesc
    z1 = _zscore_rolling(cr,  _TD_YEAR)
    z2 = _zscore_rolling(qr,  _TD_YEAR)
    z3 = _zscore_rolling(car, _TD_YEAR)
    z4 = _zscore_rolling(nca, _TD_YEAR)
    return (z1 + z2 + z3 + z4) / 4.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

LIQUIDITY_DISTRESS_REGISTRY_076_150 = {
    "lqd_076_current_ratio_3y_change":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_076_current_ratio_3y_change},
    "lqd_077_current_ratio_3y_pct_change":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_077_current_ratio_3y_pct_change},
    "lqd_078_quick_ratio_2y_change":                 {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_078_quick_ratio_2y_change},
    "lqd_079_cash_ratio_2y_change":                  {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_079_cash_ratio_2y_change},
    "lqd_080_cashnequiv_yoy_change":                 {"inputs": ["cashnequiv"],                                           "func": lqd_080_cashnequiv_yoy_change},
    "lqd_081_cashnequiv_2y_change":                  {"inputs": ["cashnequiv"],                                           "func": lqd_081_cashnequiv_2y_change},
    "lqd_082_assetsc_2y_change":                     {"inputs": ["assetsc"],                                              "func": lqd_082_assetsc_2y_change},
    "lqd_083_liabilitiesc_2y_change":                {"inputs": ["liabilitiesc"],                                         "func": lqd_083_liabilitiesc_2y_change},
    "lqd_084_current_ratio_4q_avg":                  {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_084_current_ratio_4q_avg},
    "lqd_085_current_ratio_8q_avg":                  {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_085_current_ratio_8q_avg},
    "lqd_086_quick_ratio_4q_avg":                    {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_086_quick_ratio_4q_avg},
    "lqd_087_cash_ratio_4q_avg":                     {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_087_cash_ratio_4q_avg},
    "lqd_088_current_ratio_vs_4q_avg":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_088_current_ratio_vs_4q_avg},
    "lqd_089_current_ratio_vs_8q_avg":               {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_089_current_ratio_vs_8q_avg},
    "lqd_090_quick_ratio_vs_4q_avg":                 {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_090_quick_ratio_vs_4q_avg},
    "lqd_091_current_ratio_declining_qtrs_1y":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_091_current_ratio_declining_qtrs_1y},
    "lqd_092_current_ratio_declining_qtrs_2y":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_092_current_ratio_declining_qtrs_2y},
    "lqd_093_quick_ratio_declining_qtrs_1y":         {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_093_quick_ratio_declining_qtrs_1y},
    "lqd_094_cash_declining_qtrs_1y":                {"inputs": ["cashnequiv"],                                           "func": lqd_094_cash_declining_qtrs_1y},
    "lqd_095_current_ratio_speed_of_erosion_1q":     {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_095_current_ratio_speed_of_erosion_1q},
    "lqd_096_current_ratio_speed_of_erosion_yoy":    {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_096_current_ratio_speed_of_erosion_yoy},
    "lqd_097_cashnequiv_burn_rate_qoq":              {"inputs": ["cashnequiv"],                                           "func": lqd_097_cashnequiv_burn_rate_qoq},
    "lqd_098_cashnequiv_burn_rate_yoy":              {"inputs": ["cashnequiv"],                                           "func": lqd_098_cashnequiv_burn_rate_yoy},
    "lqd_099_liabilitiesc_growth_qoq":               {"inputs": ["liabilitiesc"],                                         "func": lqd_099_liabilitiesc_growth_qoq},
    "lqd_100_liabilitiesc_growth_yoy":               {"inputs": ["liabilitiesc"],                                         "func": lqd_100_liabilitiesc_growth_yoy},
    "lqd_101_current_ratio_distance_to_1":           {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_101_current_ratio_distance_to_1},
    "lqd_102_quick_ratio_distance_to_1":             {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_102_quick_ratio_distance_to_1},
    "lqd_103_cash_ratio_pct_rank_12q":               {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_103_cash_ratio_pct_rank_12q},
    "lqd_104_current_ratio_worst_4q":                {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_104_current_ratio_worst_4q},
    "lqd_105_current_ratio_worst_8q":                {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_105_current_ratio_worst_8q},
    "lqd_106_net_current_assets_4q_avg":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_106_net_current_assets_4q_avg},
    "lqd_107_net_current_assets_drawdown_from_peak": {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_107_net_current_assets_drawdown_from_peak},
    "lqd_108_net_current_assets_pct_drawdown":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_108_net_current_assets_pct_drawdown},
    "lqd_109_cashnequiv_to_liabilitiesc_shortfall":  {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_109_cashnequiv_to_liabilitiesc_shortfall},
    "lqd_110_cashnequiv_covers_debtc_fraction":      {"inputs": ["cashnequiv", "debtc"],                                  "func": lqd_110_cashnequiv_covers_debtc_fraction},
    "lqd_111_liquid_assets_to_liabilitiesc":         {"inputs": ["cashnequiv", "receivables", "investmentsc", "liabilitiesc"], "func": lqd_111_liquid_assets_to_liabilitiesc},
    "lqd_112_cashnequiv_rolling_min_4q":             {"inputs": ["cashnequiv"],                                           "func": lqd_112_cashnequiv_rolling_min_4q},
    "lqd_113_cashnequiv_rolling_min_8q":             {"inputs": ["cashnequiv"],                                           "func": lqd_113_cashnequiv_rolling_min_8q},
    "lqd_114_cashnequiv_vs_4q_avg":                  {"inputs": ["cashnequiv"],                                           "func": lqd_114_cashnequiv_vs_4q_avg},
    "lqd_115_cashnequiv_pct_vs_4q_avg":              {"inputs": ["cashnequiv"],                                           "func": lqd_115_cashnequiv_pct_vs_4q_avg},
    "lqd_116_receivables_qoq_change":                {"inputs": ["receivables"],                                          "func": lqd_116_receivables_qoq_change},
    "lqd_117_receivables_yoy_change":                {"inputs": ["receivables"],                                          "func": lqd_117_receivables_yoy_change},
    "lqd_118_inventory_qoq_change":                  {"inputs": ["inventory"],                                            "func": lqd_118_inventory_qoq_change},
    "lqd_119_inventory_yoy_change":                  {"inputs": ["inventory"],                                            "func": lqd_119_inventory_yoy_change},
    "lqd_120_payables_qoq_change":                   {"inputs": ["payables"],                                             "func": lqd_120_payables_qoq_change},
    "lqd_121_receivables_to_liabilitiesc_ratio":     {"inputs": ["receivables", "liabilitiesc"],                          "func": lqd_121_receivables_to_liabilitiesc_ratio},
    "lqd_122_receivables_plus_cash_vs_liabilitiesc": {"inputs": ["receivables", "cashnequiv", "liabilitiesc"],            "func": lqd_122_receivables_plus_cash_vs_liabilitiesc},
    "lqd_123_inventory_growth_vs_assetsc_growth":    {"inputs": ["inventory", "assetsc"],                                 "func": lqd_123_inventory_growth_vs_assetsc_growth},
    "lqd_124_receivables_growth_vs_assetsc_growth":  {"inputs": ["receivables", "assetsc"],                               "func": lqd_124_receivables_growth_vs_assetsc_growth},
    "lqd_125_non_cash_current_assets_ratio":         {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                "func": lqd_125_non_cash_current_assets_ratio},
    "lqd_126_inventory_coverage_of_liabilitiesc":    {"inputs": ["inventory", "liabilitiesc"],                            "func": lqd_126_inventory_coverage_of_liabilitiesc},
    "lqd_127_payables_to_liabilitiesc":              {"inputs": ["payables", "liabilitiesc"],                             "func": lqd_127_payables_to_liabilitiesc},
    "lqd_128_payables_to_receivables":               {"inputs": ["payables", "receivables"],                              "func": lqd_128_payables_to_receivables},
    "lqd_129_deferred_rev_to_liabilitiesc":          {"inputs": ["deferredrev", "liabilitiesc"],                          "func": lqd_129_deferred_rev_to_liabilitiesc},
    "lqd_130_current_liab_qoq_vs_assetsc_qoq":       {"inputs": ["liabilitiesc", "assetsc"],                              "func": lqd_130_current_liab_qoq_vs_assetsc_qoq},
    "lqd_131_cashnequiv_zscore_4q":                  {"inputs": ["cashnequiv"],                                           "func": lqd_131_cashnequiv_zscore_4q},
    "lqd_132_cashnequiv_zscore_8q":                  {"inputs": ["cashnequiv"],                                           "func": lqd_132_cashnequiv_zscore_8q},
    "lqd_133_assetsc_zscore_4q":                     {"inputs": ["assetsc"],                                              "func": lqd_133_assetsc_zscore_4q},
    "lqd_134_liabilitiesc_zscore_4q":                {"inputs": ["liabilitiesc"],                                         "func": lqd_134_liabilitiesc_zscore_4q},
    "lqd_135_working_capital_zscore_4q":             {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_135_working_capital_zscore_4q},
    "lqd_136_cr_minus_qr_gap":                       {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_136_cr_minus_qr_gap},
    "lqd_137_qr_minus_cash_ratio_gap":               {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_137_qr_minus_cash_ratio_gap},
    "lqd_138_cr_minus_qr_gap_qoq_change":            {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_138_cr_minus_qr_gap_qoq_change},
    "lqd_139_current_ratio_pct_rank_12q":            {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_139_current_ratio_pct_rank_12q},
    "lqd_140_quick_ratio_pct_rank_8q":               {"inputs": ["assetsc", "inventory", "liabilitiesc"],                 "func": lqd_140_quick_ratio_pct_rank_8q},
    "lqd_141_cash_ratio_pct_rank_8q":                {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_141_cash_ratio_pct_rank_8q},
    "lqd_142_current_ratio_median_deviation_4q":     {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_142_current_ratio_median_deviation_4q},
    "lqd_143_cash_ratio_median_deviation_4q":        {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": lqd_143_cash_ratio_median_deviation_4q},
    "lqd_144_cashnequiv_pct_rank_4q":                {"inputs": ["cashnequiv"],                                           "func": lqd_144_cashnequiv_pct_rank_4q},
    "lqd_145_liabilitiesc_pct_rank_4q":              {"inputs": ["liabilitiesc"],                                         "func": lqd_145_liabilitiesc_pct_rank_4q},
    "lqd_146_current_ratio_range_position_8q":       {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_146_current_ratio_range_position_8q},
    "lqd_147_liabilitiesc_growth_outpacing_assetsc_flag": {"inputs": ["assetsc", "liabilitiesc"],                         "func": lqd_147_liabilitiesc_growth_outpacing_assetsc_flag},
    "lqd_148_triple_stress_flag":                    {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_148_triple_stress_flag},
    "lqd_149_current_ratio_ewm_zscore":              {"inputs": ["assetsc", "liabilitiesc"],                              "func": lqd_149_current_ratio_ewm_zscore},
    "lqd_150_liquidity_distress_composite_4signal":  {"inputs": ["assetsc", "inventory", "cashnequiv", "liabilitiesc"],   "func": lqd_150_liquidity_distress_composite_4signal},
}
