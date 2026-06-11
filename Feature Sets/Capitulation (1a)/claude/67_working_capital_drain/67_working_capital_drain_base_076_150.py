"""
67_working_capital_drain — Base Features 076-150
Domain: working-capital depletion trend, payables stretching, depletion speed
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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Payables stretching and supplier stress ---

def wcd_076_payables_qoq_change(payables: pd.Series) -> pd.Series:
    """Payables absolute QoQ change (rising = stretching supplier terms)."""
    return payables - payables.shift(_TD_QTR)


def wcd_077_payables_yoy_change(payables: pd.Series) -> pd.Series:
    """Payables absolute YoY change."""
    return payables - payables.shift(_TD_YEAR)


def wcd_078_payables_yoy_pct(payables: pd.Series) -> pd.Series:
    """Payables YoY percent change; denominator is abs(prior)."""
    prior = payables.shift(_TD_YEAR)
    return _safe_div_abs(payables - prior, prior)


def wcd_079_payables_to_liabilitiesc(payables: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Payables as fraction of total current liabilities — payables concentration."""
    return _safe_div(payables, liabilitiesc.abs().replace(0, np.nan))


def wcd_080_payables_to_revenue(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Payables as fraction of revenue — payables days proxy at revenue scale."""
    return _safe_div(payables, revenue.abs().replace(0, np.nan))


def wcd_081_payables_to_revenue_yoy_change(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in payables-to-revenue ratio (deteriorating = stretching more aggressively)."""
    ratio = _safe_div(payables, revenue.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_082_payables_to_cor_yoy_change(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in payables-to-COGS ratio."""
    ratio = _safe_div(payables, cor.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_083_payables_zscore_4q(payables: pd.Series) -> pd.Series:
    """Z-score of payables within trailing 4-quarter window."""
    return _zscore_rolling(payables, _TD_YEAR)


def wcd_084_payables_drawdown_from_expanding_trough(payables: pd.Series) -> pd.Series:
    """
    Payables vs expanding all-history minimum.
    Positive value = payables are elevated above their historical floor.
    """
    trough = payables.expanding(min_periods=1).min()
    return payables - trough


def wcd_085_liabilitiesc_qoq_change(liabilitiesc: pd.Series) -> pd.Series:
    """Current liabilities QoQ absolute change."""
    return liabilitiesc - liabilitiesc.shift(_TD_QTR)


def wcd_086_liabilitiesc_yoy_change(liabilitiesc: pd.Series) -> pd.Series:
    """Current liabilities YoY absolute change."""
    return liabilitiesc - liabilitiesc.shift(_TD_YEAR)


def wcd_087_liabilitiesc_to_assets(liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current liabilities as fraction of total assets (short-term leverage pressure)."""
    return _safe_div(liabilitiesc, assets.abs().replace(0, np.nan))


def wcd_088_liabilitiesc_to_assets_yoy_change(liabilitiesc: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in current-liabilities-to-assets ratio."""
    ratio = _safe_div(liabilitiesc, assets.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_089_debtc_to_liabilitiesc(debtc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Short-term debt as fraction of current liabilities — debt maturity pressure."""
    return _safe_div(debtc, liabilitiesc.abs().replace(0, np.nan))


def wcd_090_debtc_to_wc(debtc: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Short-term debt divided by working capital; NaN when WC=0."""
    return _safe_div(debtc, workingcapital.replace(0, np.nan))


# --- Group H (091-105): Cash position decline and depletion speed ---

def wcd_091_cash_qoq_change(cashnequiv: pd.Series) -> pd.Series:
    """Cash & equivalents QoQ absolute change (negative = cash burn)."""
    return cashnequiv - cashnequiv.shift(_TD_QTR)


def wcd_092_cash_yoy_change(cashnequiv: pd.Series) -> pd.Series:
    """Cash & equivalents YoY absolute change."""
    return cashnequiv - cashnequiv.shift(_TD_YEAR)


def wcd_093_cash_yoy_pct(cashnequiv: pd.Series) -> pd.Series:
    """Cash YoY percent change; denominator is abs(prior)."""
    prior = cashnequiv.shift(_TD_YEAR)
    return _safe_div_abs(cashnequiv - prior, prior)


def wcd_094_cash_to_liabilitiesc(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash coverage of current liabilities (cash-only quick proxy)."""
    return _safe_div(cashnequiv, liabilitiesc.abs().replace(0, np.nan))


def wcd_095_cash_to_liabilitiesc_yoy_change(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in cash-to-current-liabilities ratio."""
    ratio = _safe_div(cashnequiv, liabilitiesc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_096_cash_drawdown_from_4q_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash vs its 4-quarter rolling peak (cash depletion from recent high)."""
    peak = _rolling_max(cashnequiv, _TD_YEAR)
    return cashnequiv - peak


def wcd_097_cash_pct_drawdown_from_4q_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash percent drawdown from 4-quarter peak."""
    peak = _rolling_max(cashnequiv, _TD_YEAR)
    return _safe_div_abs(cashnequiv - peak, peak)


def wcd_098_cash_drawdown_from_expanding_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash vs all-history expanding peak (total cash depletion from best level)."""
    peak = cashnequiv.expanding(min_periods=1).max()
    return cashnequiv - peak


def wcd_099_cash_pct_drawdown_from_expanding_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash percent drawdown from all-history expanding peak."""
    peak = cashnequiv.expanding(min_periods=1).max()
    return _safe_div_abs(cashnequiv - peak, peak)


def wcd_100_cash_depletion_rate_4q(cashnequiv: pd.Series) -> pd.Series:
    """
    Average quarterly cash burn rate over trailing 4 quarters:
    (cash[t] - cash[t-252]) / 4  — annualized quarterly rate.
    """
    return (cashnequiv - cashnequiv.shift(_TD_YEAR)) / 4.0


def wcd_101_cash_depletion_rate_8q(cashnequiv: pd.Series) -> pd.Series:
    """Average quarterly cash burn rate over trailing 8 quarters."""
    return (cashnequiv - cashnequiv.shift(_TD_2Y)) / 8.0


def wcd_102_cash_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 4-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_YEAR)


def wcd_103_cash_pct_rank_4q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash within trailing 4-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_YEAR)


def wcd_104_cash_to_wc(cashnequiv: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Cash as fraction of working capital; NaN when WC=0."""
    return _safe_div(cashnequiv, workingcapital.replace(0, np.nan))


def wcd_105_cash_to_revenue(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """Cash as fraction of revenue — cash buffer at operating scale."""
    return _safe_div(cashnequiv, revenue.abs().replace(0, np.nan))


# --- Group I (106-120): WC vs avg, rolling variance, and depletion speed ---

def wcd_106_wc_vs_4q_avg(workingcapital: pd.Series) -> pd.Series:
    """Working capital minus trailing 4-quarter mean (level vs recent average)."""
    avg = _rolling_mean(workingcapital, _TD_YEAR)
    return workingcapital - avg


def wcd_107_wc_vs_8q_avg(workingcapital: pd.Series) -> pd.Series:
    """Working capital minus trailing 8-quarter mean."""
    avg = _rolling_mean(workingcapital, _TD_2Y)
    return workingcapital - avg


def wcd_108_wc_pct_vs_4q_avg(workingcapital: pd.Series) -> pd.Series:
    """Working capital percent deviation from trailing 4-quarter mean."""
    avg = _rolling_mean(workingcapital, _TD_YEAR)
    return _safe_div_abs(workingcapital - avg, avg)


def wcd_109_wc_pct_vs_8q_avg(workingcapital: pd.Series) -> pd.Series:
    """Working capital percent deviation from trailing 8-quarter mean."""
    avg = _rolling_mean(workingcapital, _TD_2Y)
    return _safe_div_abs(workingcapital - avg, avg)


def wcd_110_wc_rolling_std_4q(workingcapital: pd.Series) -> pd.Series:
    """Rolling 4-quarter standard deviation of WC (volatility of WC position)."""
    return _rolling_std(workingcapital, _TD_YEAR)


def wcd_111_wc_rolling_std_8q(workingcapital: pd.Series) -> pd.Series:
    """Rolling 8-quarter standard deviation of WC."""
    return _rolling_std(workingcapital, _TD_2Y)


def wcd_112_wc_decline_speed_4q(workingcapital: pd.Series) -> pd.Series:
    """
    WC decline speed: total WC decline over 4 quarters divided by 4.
    Equivalent to average quarterly WC change — negative = draining.
    """
    return (workingcapital - workingcapital.shift(_TD_YEAR)) / 4.0


def wcd_113_wc_decline_speed_8q(workingcapital: pd.Series) -> pd.Series:
    """Average quarterly WC change over trailing 8 quarters."""
    return (workingcapital - workingcapital.shift(_TD_2Y)) / 8.0


def wcd_114_wc_decline_speed_12q(workingcapital: pd.Series) -> pd.Series:
    """Average quarterly WC change over trailing 12 quarters."""
    return (workingcapital - workingcapital.shift(_TD_3Y)) / 12.0


def wcd_115_wc_range_position_8q(workingcapital: pd.Series) -> pd.Series:
    """
    Position of working capital within its trailing 8-quarter [min, max] range:
    (wc - min) / (max - min).  0.0 = at 8-quarter low (maximum depletion stress).
    """
    lo = _rolling_min(workingcapital, _TD_2Y)
    hi = _rolling_max(workingcapital, _TD_2Y)
    return _safe_div(workingcapital - lo, hi - lo)


def wcd_116_wc_decline_fraction_4q(workingcapital: pd.Series) -> pd.Series:
    """Fraction of days in trailing 4 quarters where WC was below its 4-quarter mean."""
    avg = _rolling_mean(workingcapital, _TD_YEAR)
    below = (workingcapital < avg).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def wcd_117_wc_below_zero_fraction_8q(workingcapital: pd.Series) -> pd.Series:
    """Fraction of trailing 8-quarter window where WC was negative."""
    neg = (workingcapital < 0).astype(float)
    return _rolling_mean(neg, _TD_2Y)


def wcd_118_wc_ewm_vs_level(workingcapital: pd.Series) -> pd.Series:
    """WC minus its 8-quarter EWM (span=504); captures sudden WC deterioration."""
    ewm = _ewm_mean(workingcapital, _TD_2Y)
    return workingcapital - ewm


def wcd_119_wc_median_deviation_4q(workingcapital: pd.Series) -> pd.Series:
    """Working capital minus trailing 4-quarter rolling median."""
    med = _rolling_median(workingcapital, _TD_YEAR)
    return workingcapital - med


def wcd_120_wc_pct_rank_12q(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of WC within trailing 12-quarter (756-day) window."""
    return _rolling_rank_pct(workingcapital, _TD_3Y)


# --- Group J (121-135): Cross-balance-sheet WC deterioration signals ---

def wcd_121_assetsc_qoq_change(assetsc: pd.Series) -> pd.Series:
    """Current assets QoQ absolute change (declining current assets signal)."""
    return assetsc - assetsc.shift(_TD_QTR)


def wcd_122_assetsc_yoy_change(assetsc: pd.Series) -> pd.Series:
    """Current assets YoY absolute change."""
    return assetsc - assetsc.shift(_TD_YEAR)


def wcd_123_assetsc_to_assets(assetsc: pd.Series, assets: pd.Series) -> pd.Series:
    """Current assets as fraction of total assets (liquidity composition)."""
    return _safe_div(assetsc, assets.abs().replace(0, np.nan))


def wcd_124_assetsc_to_assets_yoy_change(assetsc: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in current-assets-to-total-assets ratio."""
    ratio = _safe_div(assetsc, assets.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_125_liabilitiesc_growth_vs_assetsc_growth(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """
    YoY growth in current liabilities minus YoY growth in current assets.
    Positive = liabilities growing faster than assets (WC squeeze signal).
    """
    da = assetsc - assetsc.shift(_TD_YEAR)
    dl = liabilitiesc - liabilitiesc.shift(_TD_YEAR)
    return dl - da


def wcd_126_wc_as_days_of_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """Working capital expressed in days of revenue (WC / daily revenue)."""
    daily_rev = revenue / 91.25
    return _safe_div(workingcapital, daily_rev.abs().replace(0, np.nan))


def wcd_127_wc_as_days_of_revenue_yoy_change(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in WC-days-of-revenue."""
    daily_rev = revenue / 91.25
    wc_days = _safe_div(workingcapital, daily_rev.abs().replace(0, np.nan))
    return wc_days - wc_days.shift(_TD_YEAR)


def wcd_128_noncash_wc(assetsc: pd.Series, cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Non-cash working capital: (assetsc - cashnequiv) - liabilitiesc."""
    return (assetsc - cashnequiv) - liabilitiesc


def wcd_129_noncash_wc_qoq_change(assetsc: pd.Series, cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in non-cash working capital."""
    nwc = (assetsc - cashnequiv) - liabilitiesc
    return nwc - nwc.shift(_TD_QTR)


def wcd_130_noncash_wc_yoy_change(assetsc: pd.Series, cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in non-cash working capital."""
    nwc = (assetsc - cashnequiv) - liabilitiesc
    return nwc - nwc.shift(_TD_YEAR)


def wcd_131_receivables_plus_inventory_to_wc(receivables: pd.Series, inventory: pd.Series,
                                               workingcapital: pd.Series) -> pd.Series:
    """
    (receivables + inventory) as fraction of WC.
    Rising value = WC increasingly tied up in hard-to-liquidate items.
    """
    return _safe_div(receivables + inventory, workingcapital.replace(0, np.nan))


def wcd_132_receivables_plus_inventory_to_assetsc(receivables: pd.Series, inventory: pd.Series,
                                                    assetsc: pd.Series) -> pd.Series:
    """(Receivables + inventory) as fraction of current assets."""
    return _safe_div(receivables + inventory, assetsc.abs().replace(0, np.nan))


def wcd_133_wc_to_debtc(workingcapital: pd.Series, debtc: pd.Series) -> pd.Series:
    """Working capital divided by short-term debt (coverage of immediate debt maturities)."""
    return _safe_div(workingcapital, debtc.abs().replace(0, np.nan))


def wcd_134_wc_minus_debtc(workingcapital: pd.Series, debtc: pd.Series) -> pd.Series:
    """Working capital minus short-term debt (residual liquidity after near-term obligations)."""
    return workingcapital - debtc


def wcd_135_wc_minus_debtc_yoy_change(workingcapital: pd.Series, debtc: pd.Series) -> pd.Series:
    """YoY change in (WC - short-term debt)."""
    residual = workingcapital - debtc
    return residual - residual.shift(_TD_YEAR)


# --- Group K (136-150): Operating cash flow and WC interaction ---

def wcd_136_ncfo_to_wc(ncfo: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """Operating cash flow divided by WC — how much FCF the WC base generates."""
    return _safe_div(ncfo, workingcapital.replace(0, np.nan))


def wcd_137_ncfo_minus_wc_change(ncfo: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """
    Operating cash flow minus QoQ WC change.
    Captures whether OCF is offset by WC build (cash trapped in operations).
    """
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return ncfo - dw


def wcd_138_ncfo_qoq_change(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow QoQ absolute change."""
    return ncfo - ncfo.shift(_TD_QTR)


def wcd_139_ncfo_yoy_change(ncfo: pd.Series) -> pd.Series:
    """Operating cash flow YoY absolute change."""
    return ncfo - ncfo.shift(_TD_YEAR)


def wcd_140_ncfo_to_liabilitiesc(ncfo: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Operating cash flow divided by current liabilities (cash coverage of ST obligations)."""
    return _safe_div(ncfo, liabilitiesc.abs().replace(0, np.nan))


def wcd_141_ncfo_is_negative(ncfo: pd.Series) -> pd.Series:
    """Binary: 1 if operating cash flow < 0."""
    return (ncfo < 0).astype(float)


def wcd_142_ncfo_negative_fraction_4q(ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day window where operating cash flow was negative."""
    neg = (ncfo < 0).astype(float)
    return _rolling_mean(neg, _TD_YEAR)


def wcd_143_wc_change_to_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ WC change divided by revenue (WC drain intensity relative to scale)."""
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _safe_div(dw, revenue.abs().replace(0, np.nan))


def wcd_144_wc_change_to_assets(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ WC change divided by total assets (WC drain as fraction of asset base)."""
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _safe_div(dw, assets.abs().replace(0, np.nan))


def wcd_145_wc_drain_4q_cumulative(workingcapital: pd.Series) -> pd.Series:
    """
    Cumulative WC change over trailing 4 quarters:
    rolling sum of QoQ WC changes, window=252.
    Persistent negative = chronic drain.
    """
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _rolling_sum(dw, _TD_YEAR)


def wcd_146_wc_drain_8q_cumulative(workingcapital: pd.Series) -> pd.Series:
    """Cumulative WC change over trailing 8 quarters."""
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return _rolling_sum(dw, _TD_2Y)


def wcd_147_wc_consecutive_qoq_decline_count(workingcapital: pd.Series) -> pd.Series:
    """
    Count of consecutive quarters (by 63-day steps) with QoQ WC decline.
    Resets when WC improves.
    """
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    dec = (dw < 0).astype(int)
    streak = np.zeros(len(dec), dtype=float)
    arr = dec.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=workingcapital.index)


def wcd_148_wc_drain_vs_cash_drain(workingcapital: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    YoY WC change minus YoY cash change.
    Negative = WC is draining faster than cash (non-cash WC deterioration).
    """
    dw = workingcapital - workingcapital.shift(_TD_YEAR)
    dc = cashnequiv - cashnequiv.shift(_TD_YEAR)
    return dw - dc


def wcd_149_wc_to_ncfo(workingcapital: pd.Series, ncfo: pd.Series) -> pd.Series:
    """WC level divided by operating cash flow (how many quarters of OCF the WC covers)."""
    return _safe_div(workingcapital, ncfo.replace(0, np.nan))


def wcd_150_wc_drain_severity_composite(workingcapital: pd.Series, cashnequiv: pd.Series,
                                          receivables: pd.Series, payables: pd.Series,
                                          revenue: pd.Series) -> pd.Series:
    """
    Composite WC-drain severity (features 076-150 perspective):
    Equally weighted mean of: WC z-score(4q), cash-to-liabilities z-score(4q),
    receivables-to-revenue z-score(4q), payables z-score(4q).
    Lower = more distressed WC position.
    """
    z_wc  = _zscore_rolling(workingcapital, _TD_YEAR)
    cash_cov = _safe_div(cashnequiv, revenue.abs().replace(0, np.nan))
    z_cc  = _zscore_rolling(cash_cov, _TD_YEAR)
    rec_rev = _safe_div(receivables, revenue.abs().replace(0, np.nan))
    z_rec = _zscore_rolling(rec_rev, _TD_YEAR)
    z_pay = _zscore_rolling(payables, _TD_YEAR)
    return (z_wc + z_cc - z_rec - z_pay) / 4.0


# ── Registry 076-150 ──────────────────────────────────────────────────────────

WORKING_CAPITAL_DRAIN_REGISTRY_076_150 = {
    "wcd_076_payables_qoq_change":                      {"inputs": ["payables"],                                                            "func": wcd_076_payables_qoq_change},
    "wcd_077_payables_yoy_change":                      {"inputs": ["payables"],                                                            "func": wcd_077_payables_yoy_change},
    "wcd_078_payables_yoy_pct":                         {"inputs": ["payables"],                                                            "func": wcd_078_payables_yoy_pct},
    "wcd_079_payables_to_liabilitiesc":                 {"inputs": ["payables", "liabilitiesc"],                                            "func": wcd_079_payables_to_liabilitiesc},
    "wcd_080_payables_to_revenue":                      {"inputs": ["payables", "revenue"],                                                 "func": wcd_080_payables_to_revenue},
    "wcd_081_payables_to_revenue_yoy_change":           {"inputs": ["payables", "revenue"],                                                 "func": wcd_081_payables_to_revenue_yoy_change},
    "wcd_082_payables_to_cor_yoy_change":               {"inputs": ["payables", "cor"],                                                     "func": wcd_082_payables_to_cor_yoy_change},
    "wcd_083_payables_zscore_4q":                       {"inputs": ["payables"],                                                            "func": wcd_083_payables_zscore_4q},
    "wcd_084_payables_drawdown_from_expanding_trough":  {"inputs": ["payables"],                                                            "func": wcd_084_payables_drawdown_from_expanding_trough},
    "wcd_085_liabilitiesc_qoq_change":                  {"inputs": ["liabilitiesc"],                                                        "func": wcd_085_liabilitiesc_qoq_change},
    "wcd_086_liabilitiesc_yoy_change":                  {"inputs": ["liabilitiesc"],                                                        "func": wcd_086_liabilitiesc_yoy_change},
    "wcd_087_liabilitiesc_to_assets":                   {"inputs": ["liabilitiesc", "assets"],                                              "func": wcd_087_liabilitiesc_to_assets},
    "wcd_088_liabilitiesc_to_assets_yoy_change":        {"inputs": ["liabilitiesc", "assets"],                                              "func": wcd_088_liabilitiesc_to_assets_yoy_change},
    "wcd_089_debtc_to_liabilitiesc":                    {"inputs": ["debtc", "liabilitiesc"],                                               "func": wcd_089_debtc_to_liabilitiesc},
    "wcd_090_debtc_to_wc":                              {"inputs": ["debtc", "workingcapital"],                                             "func": wcd_090_debtc_to_wc},
    "wcd_091_cash_qoq_change":                          {"inputs": ["cashnequiv"],                                                          "func": wcd_091_cash_qoq_change},
    "wcd_092_cash_yoy_change":                          {"inputs": ["cashnequiv"],                                                          "func": wcd_092_cash_yoy_change},
    "wcd_093_cash_yoy_pct":                             {"inputs": ["cashnequiv"],                                                          "func": wcd_093_cash_yoy_pct},
    "wcd_094_cash_to_liabilitiesc":                     {"inputs": ["cashnequiv", "liabilitiesc"],                                          "func": wcd_094_cash_to_liabilitiesc},
    "wcd_095_cash_to_liabilitiesc_yoy_change":          {"inputs": ["cashnequiv", "liabilitiesc"],                                          "func": wcd_095_cash_to_liabilitiesc_yoy_change},
    "wcd_096_cash_drawdown_from_4q_peak":               {"inputs": ["cashnequiv"],                                                          "func": wcd_096_cash_drawdown_from_4q_peak},
    "wcd_097_cash_pct_drawdown_from_4q_peak":           {"inputs": ["cashnequiv"],                                                          "func": wcd_097_cash_pct_drawdown_from_4q_peak},
    "wcd_098_cash_drawdown_from_expanding_peak":        {"inputs": ["cashnequiv"],                                                          "func": wcd_098_cash_drawdown_from_expanding_peak},
    "wcd_099_cash_pct_drawdown_from_expanding_peak":    {"inputs": ["cashnequiv"],                                                          "func": wcd_099_cash_pct_drawdown_from_expanding_peak},
    "wcd_100_cash_depletion_rate_4q":                   {"inputs": ["cashnequiv"],                                                          "func": wcd_100_cash_depletion_rate_4q},
    "wcd_101_cash_depletion_rate_8q":                   {"inputs": ["cashnequiv"],                                                          "func": wcd_101_cash_depletion_rate_8q},
    "wcd_102_cash_zscore_4q":                           {"inputs": ["cashnequiv"],                                                          "func": wcd_102_cash_zscore_4q},
    "wcd_103_cash_pct_rank_4q":                         {"inputs": ["cashnequiv"],                                                          "func": wcd_103_cash_pct_rank_4q},
    "wcd_104_cash_to_wc":                               {"inputs": ["cashnequiv", "workingcapital"],                                        "func": wcd_104_cash_to_wc},
    "wcd_105_cash_to_revenue":                          {"inputs": ["cashnequiv", "revenue"],                                               "func": wcd_105_cash_to_revenue},
    "wcd_106_wc_vs_4q_avg":                             {"inputs": ["workingcapital"],                                                      "func": wcd_106_wc_vs_4q_avg},
    "wcd_107_wc_vs_8q_avg":                             {"inputs": ["workingcapital"],                                                      "func": wcd_107_wc_vs_8q_avg},
    "wcd_108_wc_pct_vs_4q_avg":                         {"inputs": ["workingcapital"],                                                      "func": wcd_108_wc_pct_vs_4q_avg},
    "wcd_109_wc_pct_vs_8q_avg":                         {"inputs": ["workingcapital"],                                                      "func": wcd_109_wc_pct_vs_8q_avg},
    "wcd_110_wc_rolling_std_4q":                        {"inputs": ["workingcapital"],                                                      "func": wcd_110_wc_rolling_std_4q},
    "wcd_111_wc_rolling_std_8q":                        {"inputs": ["workingcapital"],                                                      "func": wcd_111_wc_rolling_std_8q},
    "wcd_112_wc_decline_speed_4q":                      {"inputs": ["workingcapital"],                                                      "func": wcd_112_wc_decline_speed_4q},
    "wcd_113_wc_decline_speed_8q":                      {"inputs": ["workingcapital"],                                                      "func": wcd_113_wc_decline_speed_8q},
    "wcd_114_wc_decline_speed_12q":                     {"inputs": ["workingcapital"],                                                      "func": wcd_114_wc_decline_speed_12q},
    "wcd_115_wc_range_position_8q":                     {"inputs": ["workingcapital"],                                                      "func": wcd_115_wc_range_position_8q},
    "wcd_116_wc_decline_fraction_4q":                   {"inputs": ["workingcapital"],                                                      "func": wcd_116_wc_decline_fraction_4q},
    "wcd_117_wc_below_zero_fraction_8q":                {"inputs": ["workingcapital"],                                                      "func": wcd_117_wc_below_zero_fraction_8q},
    "wcd_118_wc_ewm_vs_level":                          {"inputs": ["workingcapital"],                                                      "func": wcd_118_wc_ewm_vs_level},
    "wcd_119_wc_median_deviation_4q":                   {"inputs": ["workingcapital"],                                                      "func": wcd_119_wc_median_deviation_4q},
    "wcd_120_wc_pct_rank_12q":                          {"inputs": ["workingcapital"],                                                      "func": wcd_120_wc_pct_rank_12q},
    "wcd_121_assetsc_qoq_change":                       {"inputs": ["assetsc"],                                                             "func": wcd_121_assetsc_qoq_change},
    "wcd_122_assetsc_yoy_change":                       {"inputs": ["assetsc"],                                                             "func": wcd_122_assetsc_yoy_change},
    "wcd_123_assetsc_to_assets":                        {"inputs": ["assetsc", "assets"],                                                   "func": wcd_123_assetsc_to_assets},
    "wcd_124_assetsc_to_assets_yoy_change":             {"inputs": ["assetsc", "assets"],                                                   "func": wcd_124_assetsc_to_assets_yoy_change},
    "wcd_125_liabilitiesc_growth_vs_assetsc_growth":    {"inputs": ["assetsc", "liabilitiesc"],                                             "func": wcd_125_liabilitiesc_growth_vs_assetsc_growth},
    "wcd_126_wc_as_days_of_revenue":                    {"inputs": ["workingcapital", "revenue"],                                           "func": wcd_126_wc_as_days_of_revenue},
    "wcd_127_wc_as_days_of_revenue_yoy_change":         {"inputs": ["workingcapital", "revenue"],                                           "func": wcd_127_wc_as_days_of_revenue_yoy_change},
    "wcd_128_noncash_wc":                               {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                               "func": wcd_128_noncash_wc},
    "wcd_129_noncash_wc_qoq_change":                    {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                               "func": wcd_129_noncash_wc_qoq_change},
    "wcd_130_noncash_wc_yoy_change":                    {"inputs": ["assetsc", "cashnequiv", "liabilitiesc"],                               "func": wcd_130_noncash_wc_yoy_change},
    "wcd_131_receivables_plus_inventory_to_wc":         {"inputs": ["receivables", "inventory", "workingcapital"],                          "func": wcd_131_receivables_plus_inventory_to_wc},
    "wcd_132_receivables_plus_inventory_to_assetsc":    {"inputs": ["receivables", "inventory", "assetsc"],                                 "func": wcd_132_receivables_plus_inventory_to_assetsc},
    "wcd_133_wc_to_debtc":                              {"inputs": ["workingcapital", "debtc"],                                             "func": wcd_133_wc_to_debtc},
    "wcd_134_wc_minus_debtc":                           {"inputs": ["workingcapital", "debtc"],                                             "func": wcd_134_wc_minus_debtc},
    "wcd_135_wc_minus_debtc_yoy_change":                {"inputs": ["workingcapital", "debtc"],                                             "func": wcd_135_wc_minus_debtc_yoy_change},
    "wcd_136_ncfo_to_wc":                               {"inputs": ["ncfo", "workingcapital"],                                              "func": wcd_136_ncfo_to_wc},
    "wcd_137_ncfo_minus_wc_change":                     {"inputs": ["ncfo", "workingcapital"],                                              "func": wcd_137_ncfo_minus_wc_change},
    "wcd_138_ncfo_qoq_change":                          {"inputs": ["ncfo"],                                                                "func": wcd_138_ncfo_qoq_change},
    "wcd_139_ncfo_yoy_change":                          {"inputs": ["ncfo"],                                                                "func": wcd_139_ncfo_yoy_change},
    "wcd_140_ncfo_to_liabilitiesc":                     {"inputs": ["ncfo", "liabilitiesc"],                                                "func": wcd_140_ncfo_to_liabilitiesc},
    "wcd_141_ncfo_is_negative":                         {"inputs": ["ncfo"],                                                                "func": wcd_141_ncfo_is_negative},
    "wcd_142_ncfo_negative_fraction_4q":                {"inputs": ["ncfo"],                                                                "func": wcd_142_ncfo_negative_fraction_4q},
    "wcd_143_wc_change_to_revenue":                     {"inputs": ["workingcapital", "revenue"],                                           "func": wcd_143_wc_change_to_revenue},
    "wcd_144_wc_change_to_assets":                      {"inputs": ["workingcapital", "assets"],                                            "func": wcd_144_wc_change_to_assets},
    "wcd_145_wc_drain_4q_cumulative":                   {"inputs": ["workingcapital"],                                                      "func": wcd_145_wc_drain_4q_cumulative},
    "wcd_146_wc_drain_8q_cumulative":                   {"inputs": ["workingcapital"],                                                      "func": wcd_146_wc_drain_8q_cumulative},
    "wcd_147_wc_consecutive_qoq_decline_count":         {"inputs": ["workingcapital"],                                                      "func": wcd_147_wc_consecutive_qoq_decline_count},
    "wcd_148_wc_drain_vs_cash_drain":                   {"inputs": ["workingcapital", "cashnequiv"],                                        "func": wcd_148_wc_drain_vs_cash_drain},
    "wcd_149_wc_to_ncfo":                               {"inputs": ["workingcapital", "ncfo"],                                              "func": wcd_149_wc_to_ncfo},
    "wcd_150_wc_drain_severity_composite":              {"inputs": ["workingcapital", "cashnequiv", "receivables", "payables", "revenue"],  "func": wcd_150_wc_drain_severity_composite},
}
