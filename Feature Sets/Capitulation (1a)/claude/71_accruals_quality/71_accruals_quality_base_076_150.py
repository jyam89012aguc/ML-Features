"""
71_accruals_quality — Base Features 076-150
Domain: earnings-quality erosion via accruals — extended set covering
multi-year accrual trends, accrual vs cash earnings comparisons, balance-sheet
accrual measures, revenue-quality indicators, and advanced accrual ratios.
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
    All feature functions in this file receive Series already prepared this way;
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

# --- Group F (076-090): Multi-year accrual accumulation and trends ---

def acq_076_accruals_3y_cumsum(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Trailing 3-year (756-day) cumulative sum of total accruals."""
    acc = netinc - ncfo
    return _rolling_sum(acc, _TD_3Y)


def acq_077_accruals_3y_cumsum_scaled_assets(netinc: pd.Series, ncfo: pd.Series,
                                              assets: pd.Series) -> pd.Series:
    """Trailing 3-year cumulative accruals scaled by total assets."""
    acc = netinc - ncfo
    return _safe_div(_rolling_sum(acc, _TD_3Y), assets)


def acq_078_accruals_2y_change(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """2-year change in total accruals."""
    acc = netinc - ncfo
    return acc - acc.shift(_TD_2Y)


def acq_079_accruals_3y_change(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """3-year change in total accruals."""
    acc = netinc - ncfo
    return acc - acc.shift(_TD_3Y)


def acq_080_accruals_ratio_2y_change(netinc: pd.Series, ncfo: pd.Series,
                                      assets: pd.Series) -> pd.Series:
    """2-year change in the Sloan accruals ratio."""
    ratio = _safe_div(netinc - ncfo, assets)
    return ratio - ratio.shift(_TD_2Y)


def acq_081_accruals_ratio_3y_change(netinc: pd.Series, ncfo: pd.Series,
                                      assets: pd.Series) -> pd.Series:
    """3-year change in the Sloan accruals ratio."""
    ratio = _safe_div(netinc - ncfo, assets)
    return ratio - ratio.shift(_TD_3Y)


def acq_082_accruals_ratio_drawdown_from_4q_peak(netinc: pd.Series, ncfo: pd.Series,
                                                   assets: pd.Series) -> pd.Series:
    """Accruals ratio vs its 4-quarter peak (measures deterioration from worst accrual regime)."""
    ratio = _safe_div(netinc - ncfo, assets)
    peak = _rolling_max(ratio, _TD_YEAR)
    return ratio - peak


def acq_083_accruals_ratio_drawdown_from_3y_peak(netinc: pd.Series, ncfo: pd.Series,
                                                   assets: pd.Series) -> pd.Series:
    """Accruals ratio vs its 3-year rolling peak."""
    ratio = _safe_div(netinc - ncfo, assets)
    peak = _rolling_max(ratio, _TD_3Y)
    return ratio - peak


def acq_084_accruals_ratio_zscore_3y(netinc: pd.Series, ncfo: pd.Series,
                                      assets: pd.Series) -> pd.Series:
    """Rolling 3-year (756-day) z-score of the Sloan accruals ratio (extremity vs 3-year accrual history)."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _zscore_rolling(ratio, _TD_3Y)


def acq_085_cfo_cumulative_4q(ncfo: pd.Series) -> pd.Series:
    """Trailing 4-quarter cumulative operating cash flow."""
    return _rolling_sum(ncfo, _TD_YEAR)


def acq_086_cfo_cumulative_8q(ncfo: pd.Series) -> pd.Series:
    """Trailing 8-quarter cumulative operating cash flow."""
    return _rolling_sum(ncfo, _TD_2Y)


def acq_087_netinc_cumulative_4q(netinc: pd.Series) -> pd.Series:
    """Trailing 4-quarter cumulative net income (TTM proxy)."""
    return _rolling_sum(netinc, _TD_YEAR)


def acq_088_ttm_accruals_ratio(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """TTM-based accruals ratio: sum(netinc,4q) - sum(ncfo,4q) divided by assets."""
    ttm_ni  = _rolling_sum(netinc, _TD_YEAR)
    ttm_cfo = _rolling_sum(ncfo, _TD_YEAR)
    return _safe_div(ttm_ni - ttm_cfo, assets)


def acq_089_ttm_accruals_ratio_pct_rank_4q(netinc: pd.Series, ncfo: pd.Series,
                                            assets: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of the TTM-based accruals ratio (position within 1-year window)."""
    ttm_ni  = _rolling_sum(netinc, _TD_YEAR)
    ttm_cfo = _rolling_sum(ncfo, _TD_YEAR)
    ratio = _safe_div(ttm_ni - ttm_cfo, assets)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def acq_090_ttm_cfo_to_netinc_ratio(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """TTM operating cash flow / |TTM net income| — trailing cash quality."""
    ttm_ni  = _rolling_sum(netinc, _TD_YEAR)
    ttm_cfo = _rolling_sum(ncfo, _TD_YEAR)
    return _safe_div_abs(ttm_cfo, ttm_ni)


# --- Group G (091-105): Balance-sheet-based accrual measures ---

def acq_091_bs_accruals_change_in_assets(assets: pd.Series, cashnequiv: pd.Series,
                                          debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Balance-sheet total accruals (Richardson 2005):
    change in (assets - cash) - change in (debt + equity).
    Approximates total accruals using balance-sheet method.
    """
    net_oa  = (assets - cashnequiv) - (debt + equity)
    return net_oa - net_oa.shift(_TD_QTR)


def acq_092_noncash_working_capital_change(workingcapital: pd.Series,
                                            cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in non-cash working capital = change in (workingcapital - cashnequiv)."""
    noncash_wc = workingcapital - cashnequiv
    return noncash_wc - noncash_wc.shift(_TD_QTR)


def acq_093_noncash_wc_scaled_assets(workingcapital: pd.Series, cashnequiv: pd.Series,
                                      assets: pd.Series) -> pd.Series:
    """QoQ change in non-cash WC / assets."""
    noncash_wc = workingcapital - cashnequiv
    delta = noncash_wc - noncash_wc.shift(_TD_QTR)
    return _safe_div(delta, assets)


def acq_094_noncash_wc_level(workingcapital: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Level of non-cash working capital: workingcapital minus cashnequiv."""
    return workingcapital - cashnequiv


def acq_095_noncash_wc_to_revenue(workingcapital: pd.Series, cashnequiv: pd.Series,
                                   revenue: pd.Series) -> pd.Series:
    """Non-cash working capital / revenue — operating cycle intensity."""
    return _safe_div_abs(workingcapital - cashnequiv, revenue)


def acq_096_retearn_change_minus_netinc(retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    QoQ change in retained earnings minus net income.
    Residual reflects dividends and other equity adjustments not in netinc.
    """
    delta_re = retearn - retearn.shift(_TD_QTR)
    return delta_re - netinc


def acq_097_assets_growth_qoq(assets: pd.Series) -> pd.Series:
    """QoQ percent change in total assets (aggressive asset growth is an accrual red flag)."""
    prior = assets.shift(_TD_QTR)
    return _safe_div_abs(assets - prior, prior)


def acq_098_assets_growth_yoy(assets: pd.Series) -> pd.Series:
    """YoY percent change in total assets."""
    prior = assets.shift(_TD_YEAR)
    return _safe_div_abs(assets - prior, prior)


def acq_099_assetsc_change_qoq(assetsc: pd.Series) -> pd.Series:
    """QoQ change in current assets (proxy for WC accrual component)."""
    return assetsc - assetsc.shift(_TD_QTR)


def acq_100_liabilitiesc_change_qoq(liabilitiesc: pd.Series) -> pd.Series:
    """QoQ change in current liabilities."""
    return liabilitiesc - liabilitiesc.shift(_TD_QTR)


def acq_101_net_operating_assets(assets: pd.Series, cashnequiv: pd.Series,
                                  liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """
    Net operating assets = (assets - cashnequiv) - (liabilities - debt).
    Measures operating asset base funded by operating liabilities.
    """
    return (assets - cashnequiv) - (liabilities - debt)


def acq_102_noa_change_qoq(assets: pd.Series, cashnequiv: pd.Series,
                             liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in net operating assets."""
    noa = (assets - cashnequiv) - (liabilities - debt)
    return noa - noa.shift(_TD_QTR)


def acq_103_noa_scaled_assets(assets: pd.Series, cashnequiv: pd.Series,
                               liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """Net operating assets / total assets."""
    noa = (assets - cashnequiv) - (liabilities - debt)
    return _safe_div(noa, assets)


def acq_104_noa_change_scaled_assets(assets: pd.Series, cashnequiv: pd.Series,
                                      liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """QoQ change in NOA / total assets — accruals via balance sheet method."""
    noa = (assets - cashnequiv) - (liabilities - debt)
    delta_noa = noa - noa.shift(_TD_QTR)
    return _safe_div(delta_noa, assets)


def acq_105_payables_to_revenue_ratio(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Accounts payable / revenue — payables days proxy; declining = supplier stress."""
    return _safe_div_abs(payables, revenue)


# --- Group H (106-120): Revenue quality and accrual cross-signals ---

def acq_106_revenue_vs_receivables_growth(revenue: pd.Series,
                                           receivables: pd.Series) -> pd.Series:
    """
    QoQ revenue growth minus QoQ receivables growth.
    Negative divergence (AR growing faster than sales) is a quality red flag.
    """
    rev_growth = _safe_div_abs(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR))
    ar_growth  = _safe_div_abs(receivables - receivables.shift(_TD_QTR),
                                receivables.shift(_TD_QTR))
    return rev_growth - ar_growth


def acq_107_ar_days_qoq_change(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in accounts-receivable days (receivables / daily_revenue)."""
    ar_days = _safe_div_abs(receivables, revenue) * 91  # approx days in quarter
    return ar_days - ar_days.shift(_TD_QTR)


def acq_108_inventory_days_qoq_change(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in inventory days (inventory / daily_revenue)."""
    inv_days = _safe_div_abs(inventory, revenue) * 91
    return inv_days - inv_days.shift(_TD_QTR)


def acq_109_cash_conversion_cycle_level(receivables: pd.Series, inventory: pd.Series,
                                         payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Cash conversion cycle proxy = (AR days + Inventory days - AP days).
    Rising CCC implies worsening working-capital accruals.
    """
    ar_days  = _safe_div_abs(receivables, revenue) * 91
    inv_days = _safe_div_abs(inventory, revenue) * 91
    ap_days  = _safe_div_abs(payables, revenue) * 91
    return ar_days + inv_days - ap_days


def acq_110_ccc_pct_rank_4q(receivables: pd.Series, inventory: pd.Series,
                              payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of the cash conversion cycle (high rank = longest working-capital cycle)."""
    ar_days  = _safe_div_abs(receivables, revenue) * 91
    inv_days = _safe_div_abs(inventory, revenue) * 91
    ap_days  = _safe_div_abs(payables, revenue) * 91
    ccc = ar_days + inv_days - ap_days
    return _rolling_rank_pct(ccc, _TD_YEAR)


def acq_111_ccc_at_3y_high_flag(receivables: pd.Series, inventory: pd.Series,
                                  payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Binary: 1 if the cash conversion cycle equals or exceeds its rolling 3-year maximum (worst working-capital cycle in 3 years)."""
    ar_days  = _safe_div_abs(receivables, revenue) * 91
    inv_days = _safe_div_abs(inventory, revenue) * 91
    ap_days  = _safe_div_abs(payables, revenue) * 91
    ccc = ar_days + inv_days - ap_days
    return (ccc >= _rolling_max(ccc, _TD_3Y)).astype(float)


def acq_112_ccc_zscore_4q(receivables: pd.Series, inventory: pd.Series,
                           payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of the cash conversion cycle in trailing 4-quarter window."""
    ar_days  = _safe_div_abs(receivables, revenue) * 91
    inv_days = _safe_div_abs(inventory, revenue) * 91
    ap_days  = _safe_div_abs(payables, revenue) * 91
    ccc = ar_days + inv_days - ap_days
    return _zscore_rolling(ccc, _TD_YEAR)


def acq_113_revenue_qoq_pct(revenue: pd.Series) -> pd.Series:
    """Revenue QoQ percent change (revenue deceleration context for accruals)."""
    prior = revenue.shift(_TD_QTR)
    return _safe_div_abs(revenue - prior, prior)


def acq_114_revenue_vs_netinc_divergence(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    Revenue QoQ pct change minus netinc QoQ pct change.
    Positive = revenue growing but earnings collapsing; accrual inflation context.
    """
    rev_pct = _safe_div_abs(revenue - revenue.shift(_TD_QTR), revenue.shift(_TD_QTR))
    ni_pct  = _safe_div_abs(netinc - netinc.shift(_TD_QTR), netinc.shift(_TD_QTR))
    return rev_pct - ni_pct


def acq_115_netinc_margin_qoq_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in net income margin (netinc/revenue)."""
    margin = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return margin - margin.shift(_TD_QTR)


def acq_116_cfo_margin(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating cash flow margin: ncfo / revenue."""
    return _safe_div(ncfo, revenue.abs().replace(0, np.nan))


def acq_117_cfo_margin_minus_netinc_margin(netinc: pd.Series, ncfo: pd.Series,
                                            revenue: pd.Series) -> pd.Series:
    """CFO margin minus net income margin — positive = good cash quality."""
    rev_abs = revenue.abs().replace(0, np.nan)
    return _safe_div(ncfo, rev_abs) - _safe_div(netinc, rev_abs)


def acq_118_cfo_margin_zscore_4q(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 4-quarter z-score of CFO margin (ncfo/revenue); low z-score = margin at recent nadir."""
    margin = _safe_div(ncfo, revenue.abs().replace(0, np.nan))
    return _zscore_rolling(margin, _TD_YEAR)


def acq_119_cfo_margin_4q_avg(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of CFO margin."""
    margin = _safe_div(ncfo, revenue.abs().replace(0, np.nan))
    return _rolling_mean(margin, _TD_YEAR)


def acq_120_accruals_ratio_vs_industry_4q_self_zscore(netinc: pd.Series, ncfo: pd.Series,
                                                        assets: pd.Series) -> pd.Series:
    """
    Z-score of Sloan accruals ratio vs its own expanding history (self-benchmark).
    Indicates how extreme the current accrual regime is vs the company's own history.
    """
    ratio = _safe_div(netinc - ncfo, assets)
    m  = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - m, sd)


# --- Group I (121-135): Advanced accrual ratios and multi-input signals ---

def acq_121_net_income_quality_ratio(netinc: pd.Series, ncfo: pd.Series,
                                      fcf: pd.Series) -> pd.Series:
    """
    Earnings quality ratio: min(ncfo, fcf) / |netinc|.
    Uses the more conservative cash measure; < 1 indicates accrual inflation.
    """
    conservative_cash = pd.concat([ncfo, fcf], axis=1).min(axis=1)
    return _safe_div_abs(conservative_cash, netinc)


def acq_122_accruals_to_revenue_ratio(netinc: pd.Series, ncfo: pd.Series,
                                       revenue: pd.Series) -> pd.Series:
    """Total accruals (netinc - ncfo) / |revenue|."""
    return _safe_div_abs(netinc - ncfo, revenue)


def acq_123_accruals_to_revenue_4q_mean(netinc: pd.Series, ncfo: pd.Series,
                                         revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of accruals/revenue ratio."""
    ratio = _safe_div_abs(netinc - ncfo, revenue)
    return _rolling_mean(ratio, _TD_YEAR)


def acq_124_accruals_to_revenue_zscore_4q(netinc: pd.Series, ncfo: pd.Series,
                                           revenue: pd.Series) -> pd.Series:
    """Rolling 4-quarter z-score of the accruals/revenue ratio (high z-score = accrual-heavy earnings vs revenue)."""
    ratio = _safe_div_abs(netinc - ncfo, revenue)
    return _zscore_rolling(ratio, _TD_YEAR)


def acq_125_fcf_vs_cfo_divergence(ncfo: pd.Series, fcf: pd.Series) -> pd.Series:
    """ncfo - fcf = capex (approximately); rising capex vs FCF signals investment drag."""
    return ncfo - fcf


def acq_126_fcf_vs_cfo_scaled_assets(ncfo: pd.Series, fcf: pd.Series,
                                      assets: pd.Series) -> pd.Series:
    """(ncfo - fcf) / assets — capex intensity scaled by assets."""
    return _safe_div(ncfo - fcf, assets)


def acq_127_capex_to_depamor_ratio(fcf: pd.Series, ncfo: pd.Series,
                                    depamor: pd.Series) -> pd.Series:
    """
    Capex proxy (ncfo - fcf) / depamor — maintenance vs replacement capex indicator.
    > 1 means capex exceeds D&A; < 1 means under-investing.
    """
    capex_proxy = (ncfo - fcf).abs()
    return _safe_div(capex_proxy, depamor.abs().replace(0, np.nan))


def acq_128_operating_leverage_accruals(netinc: pd.Series, ncfo: pd.Series,
                                         revenue: pd.Series) -> pd.Series:
    """
    Accrual intensity relative to revenue scale.
    (netinc - ncfo) / revenue — signals earnings ahead of cash at any revenue level.
    """
    return _safe_div(netinc - ncfo, revenue.abs().replace(0, np.nan))


def acq_129_accruals_ewm_4q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """4-quarter EWM (span=252) of total accruals."""
    acc = netinc - ncfo
    return _ewm_mean(acc, _TD_YEAR)


def acq_130_accruals_vs_ewm_deviation(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Current accruals minus their 4-quarter EWM — deviation from accrual trend."""
    acc = netinc - ncfo
    return acc - _ewm_mean(acc, _TD_YEAR)


def acq_131_cfo_below_netinc_magnitude(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    How much ncfo falls short of netinc: max(netinc - ncfo, 0).
    Only counts the deficit; 0 when cash quality is adequate.
    """
    return (netinc - ncfo).clip(lower=0)


def acq_132_cfo_below_netinc_4q_sum(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of the CFO-below-netinc deficit."""
    deficit = (netinc - ncfo).clip(lower=0)
    return _rolling_sum(deficit, _TD_YEAR)


def acq_133_cfo_below_netinc_4q_sum_scaled_assets(netinc: pd.Series, ncfo: pd.Series,
                                                    assets: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of CFO deficit / assets."""
    deficit = (netinc - ncfo).clip(lower=0)
    return _safe_div(_rolling_sum(deficit, _TD_YEAR), assets)


def acq_134_accruals_ratio_high_flag(netinc: pd.Series, ncfo: pd.Series,
                                      assets: pd.Series) -> pd.Series:
    """Binary: 1 when Sloan accruals ratio > 0.10 (high-accrual threshold)."""
    ratio = _safe_div(netinc - ncfo, assets)
    return (ratio > 0.10).astype(float)


def acq_135_accruals_ratio_rising_and_high(netinc: pd.Series, ncfo: pd.Series,
                                            assets: pd.Series) -> pd.Series:
    """Binary: 1 when accruals ratio > 0.05 AND rising QoQ."""
    ratio = _safe_div(netinc - ncfo, assets)
    rising = (ratio > ratio.shift(_TD_QTR)).astype(float)
    high   = (ratio > 0.05).astype(float)
    return rising * high


# --- Group J (136-150): Accrual quality across multiple time horizons and aggregations ---

def acq_136_accruals_ratio_max_4q(netinc: pd.Series, ncfo: pd.Series,
                                   assets: pd.Series) -> pd.Series:
    """Maximum Sloan accruals ratio over trailing 4-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_max(ratio, _TD_YEAR)


def acq_137_accruals_ratio_max_8q(netinc: pd.Series, ncfo: pd.Series,
                                   assets: pd.Series) -> pd.Series:
    """Maximum Sloan accruals ratio over trailing 8-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_max(ratio, _TD_2Y)


def acq_138_accruals_ratio_min_4q(netinc: pd.Series, ncfo: pd.Series,
                                   assets: pd.Series) -> pd.Series:
    """Minimum Sloan accruals ratio over trailing 4-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_min(ratio, _TD_YEAR)


def acq_139_accruals_ratio_range_4q(netinc: pd.Series, ncfo: pd.Series,
                                     assets: pd.Series) -> pd.Series:
    """Range (max - min) of Sloan accruals ratio over 4-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_max(ratio, _TD_YEAR) - _rolling_min(ratio, _TD_YEAR)


def acq_140_accruals_volatility_4q(netinc: pd.Series, ncfo: pd.Series,
                                    assets: pd.Series) -> pd.Series:
    """Standard deviation of Sloan accruals ratio over trailing 4-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_std(ratio, _TD_YEAR)


def acq_141_accruals_volatility_8q(netinc: pd.Series, ncfo: pd.Series,
                                    assets: pd.Series) -> pd.Series:
    """Standard deviation of Sloan accruals ratio over trailing 8-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_std(ratio, _TD_2Y)


def acq_142_cfo_to_assets_ratio(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Operating cash flow / total assets — cash return on assets."""
    return _safe_div(ncfo, assets)


def acq_143_cfo_to_assets_qoq_change(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in CFO/assets."""
    ratio = _safe_div(ncfo, assets)
    return ratio - ratio.shift(_TD_QTR)


def acq_144_fcf_to_assets_ratio(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Free cash flow / total assets — FCF return on assets."""
    return _safe_div(fcf, assets)


def acq_145_fcf_to_assets_qoq_change(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ change in FCF/assets."""
    ratio = _safe_div(fcf, assets)
    return ratio - ratio.shift(_TD_QTR)


def acq_146_accruals_to_equity_ratio(netinc: pd.Series, ncfo: pd.Series,
                                      equity: pd.Series) -> pd.Series:
    """Total accruals / |equity| — accrual burden relative to shareholder equity."""
    return _safe_div_abs(netinc - ncfo, equity)


def acq_147_accruals_to_equity_qoq_change(netinc: pd.Series, ncfo: pd.Series,
                                           equity: pd.Series) -> pd.Series:
    """QoQ change in accruals/equity ratio."""
    ratio = _safe_div_abs(netinc - ncfo, equity)
    return ratio - ratio.shift(_TD_QTR)


def acq_148_ncfi_vs_depamor(ncfi: pd.Series, depamor: pd.Series) -> pd.Series:
    """
    Investing cash flow vs D&A: ncfi + depamor.
    Measures whether investment activity exceeds or lags asset consumption.
    """
    return ncfi + depamor


def acq_149_accruals_quality_composite_3signal(netinc: pd.Series, ncfo: pd.Series,
                                                assets: pd.Series,
                                                revenue: pd.Series,
                                                receivables: pd.Series) -> pd.Series:
    """
    3-signal composite accrual quality z-score:
    z(sloan_ratio) + z(accruals/revenue) + z(AR/revenue); higher = worse quality.
    """
    sloan  = _safe_div(netinc - ncfo, assets)
    acc_rev = _safe_div_abs(netinc - ncfo, revenue)
    ar_rev  = _safe_div_abs(receivables, revenue)
    z1 = _zscore_rolling(sloan, _TD_YEAR)
    z2 = _zscore_rolling(acc_rev, _TD_YEAR)
    z3 = _zscore_rolling(ar_rev, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


def acq_150_accruals_high_consecutive_quarters_3y(netinc: pd.Series, ncfo: pd.Series,
                                                    assets: pd.Series) -> pd.Series:
    """
    Count of quarters in trailing 3 years where Sloan accruals ratio > 0.05.
    Persistent high-accrual regimes are associated with future earnings reversals.
    """
    ratio = _safe_div(netinc - ncfo, assets)
    flag  = (ratio > 0.05).astype(float)
    return _rolling_sum(flag, _TD_3Y)


# ── Registry 076-150 ──────────────────────────────────────────────────────────

ACCRUALS_QUALITY_REGISTRY_076_150 = {
    "acq_076_accruals_3y_cumsum":                        {"inputs": ["netinc", "ncfo"],                                          "func": acq_076_accruals_3y_cumsum},
    "acq_077_accruals_3y_cumsum_scaled_assets":          {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_077_accruals_3y_cumsum_scaled_assets},
    "acq_078_accruals_2y_change":                        {"inputs": ["netinc", "ncfo"],                                          "func": acq_078_accruals_2y_change},
    "acq_079_accruals_3y_change":                        {"inputs": ["netinc", "ncfo"],                                          "func": acq_079_accruals_3y_change},
    "acq_080_accruals_ratio_2y_change":                  {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_080_accruals_ratio_2y_change},
    "acq_081_accruals_ratio_3y_change":                  {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_081_accruals_ratio_3y_change},
    "acq_082_accruals_ratio_drawdown_from_4q_peak":      {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_082_accruals_ratio_drawdown_from_4q_peak},
    "acq_083_accruals_ratio_drawdown_from_3y_peak":      {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_083_accruals_ratio_drawdown_from_3y_peak},
    "acq_084_accruals_ratio_zscore_3y":                  {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_084_accruals_ratio_zscore_3y},
    "acq_085_cfo_cumulative_4q":                         {"inputs": ["ncfo"],                                                    "func": acq_085_cfo_cumulative_4q},
    "acq_086_cfo_cumulative_8q":                         {"inputs": ["ncfo"],                                                    "func": acq_086_cfo_cumulative_8q},
    "acq_087_netinc_cumulative_4q":                      {"inputs": ["netinc"],                                                  "func": acq_087_netinc_cumulative_4q},
    "acq_088_ttm_accruals_ratio":                        {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_088_ttm_accruals_ratio},
    "acq_089_ttm_accruals_ratio_pct_rank_4q":            {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_089_ttm_accruals_ratio_pct_rank_4q},
    "acq_090_ttm_cfo_to_netinc_ratio":                   {"inputs": ["netinc", "ncfo"],                                          "func": acq_090_ttm_cfo_to_netinc_ratio},
    "acq_091_bs_accruals_change_in_assets":              {"inputs": ["assets", "cashnequiv", "debt", "equity"],                  "func": acq_091_bs_accruals_change_in_assets},
    "acq_092_noncash_working_capital_change":            {"inputs": ["workingcapital", "cashnequiv"],                            "func": acq_092_noncash_working_capital_change},
    "acq_093_noncash_wc_scaled_assets":                  {"inputs": ["workingcapital", "cashnequiv", "assets"],                  "func": acq_093_noncash_wc_scaled_assets},
    "acq_094_noncash_wc_level":                          {"inputs": ["workingcapital", "cashnequiv"],                            "func": acq_094_noncash_wc_level},
    "acq_095_noncash_wc_to_revenue":                     {"inputs": ["workingcapital", "cashnequiv", "revenue"],                 "func": acq_095_noncash_wc_to_revenue},
    "acq_096_retearn_change_minus_netinc":               {"inputs": ["retearn", "netinc"],                                       "func": acq_096_retearn_change_minus_netinc},
    "acq_097_assets_growth_qoq":                         {"inputs": ["assets"],                                                  "func": acq_097_assets_growth_qoq},
    "acq_098_assets_growth_yoy":                         {"inputs": ["assets"],                                                  "func": acq_098_assets_growth_yoy},
    "acq_099_assetsc_change_qoq":                        {"inputs": ["assetsc"],                                                 "func": acq_099_assetsc_change_qoq},
    "acq_100_liabilitiesc_change_qoq":                   {"inputs": ["liabilitiesc"],                                            "func": acq_100_liabilitiesc_change_qoq},
    "acq_101_net_operating_assets":                      {"inputs": ["assets", "cashnequiv", "liabilities", "debt"],             "func": acq_101_net_operating_assets},
    "acq_102_noa_change_qoq":                            {"inputs": ["assets", "cashnequiv", "liabilities", "debt"],             "func": acq_102_noa_change_qoq},
    "acq_103_noa_scaled_assets":                         {"inputs": ["assets", "cashnequiv", "liabilities", "debt"],             "func": acq_103_noa_scaled_assets},
    "acq_104_noa_change_scaled_assets":                  {"inputs": ["assets", "cashnequiv", "liabilities", "debt"],             "func": acq_104_noa_change_scaled_assets},
    "acq_105_payables_to_revenue_ratio":                 {"inputs": ["payables", "revenue"],                                     "func": acq_105_payables_to_revenue_ratio},
    "acq_106_revenue_vs_receivables_growth":             {"inputs": ["revenue", "receivables"],                                  "func": acq_106_revenue_vs_receivables_growth},
    "acq_107_ar_days_qoq_change":                        {"inputs": ["receivables", "revenue"],                                  "func": acq_107_ar_days_qoq_change},
    "acq_108_inventory_days_qoq_change":                 {"inputs": ["inventory", "revenue"],                                    "func": acq_108_inventory_days_qoq_change},
    "acq_109_cash_conversion_cycle_level":               {"inputs": ["receivables", "inventory", "payables", "revenue"],         "func": acq_109_cash_conversion_cycle_level},
    "acq_110_ccc_pct_rank_4q":                           {"inputs": ["receivables", "inventory", "payables", "revenue"],         "func": acq_110_ccc_pct_rank_4q},
    "acq_111_ccc_at_3y_high_flag":                       {"inputs": ["receivables", "inventory", "payables", "revenue"],         "func": acq_111_ccc_at_3y_high_flag},
    "acq_112_ccc_zscore_4q":                             {"inputs": ["receivables", "inventory", "payables", "revenue"],         "func": acq_112_ccc_zscore_4q},
    "acq_113_revenue_qoq_pct":                           {"inputs": ["revenue"],                                                  "func": acq_113_revenue_qoq_pct},
    "acq_114_revenue_vs_netinc_divergence":              {"inputs": ["revenue", "netinc"],                                        "func": acq_114_revenue_vs_netinc_divergence},
    "acq_115_netinc_margin_qoq_change":                  {"inputs": ["netinc", "revenue"],                                        "func": acq_115_netinc_margin_qoq_change},
    "acq_116_cfo_margin":                                {"inputs": ["ncfo", "revenue"],                                          "func": acq_116_cfo_margin},
    "acq_117_cfo_margin_minus_netinc_margin":            {"inputs": ["netinc", "ncfo", "revenue"],                                "func": acq_117_cfo_margin_minus_netinc_margin},
    "acq_118_cfo_margin_zscore_4q":                      {"inputs": ["ncfo", "revenue"],                                          "func": acq_118_cfo_margin_zscore_4q},
    "acq_119_cfo_margin_4q_avg":                         {"inputs": ["ncfo", "revenue"],                                          "func": acq_119_cfo_margin_4q_avg},
    "acq_120_accruals_ratio_vs_industry_4q_self_zscore": {"inputs": ["netinc", "ncfo", "assets"],                                "func": acq_120_accruals_ratio_vs_industry_4q_self_zscore},
    "acq_121_net_income_quality_ratio":                  {"inputs": ["netinc", "ncfo", "fcf"],                                    "func": acq_121_net_income_quality_ratio},
    "acq_122_accruals_to_revenue_ratio":                 {"inputs": ["netinc", "ncfo", "revenue"],                                "func": acq_122_accruals_to_revenue_ratio},
    "acq_123_accruals_to_revenue_4q_mean":               {"inputs": ["netinc", "ncfo", "revenue"],                                "func": acq_123_accruals_to_revenue_4q_mean},
    "acq_124_accruals_to_revenue_zscore_4q":             {"inputs": ["netinc", "ncfo", "revenue"],                                "func": acq_124_accruals_to_revenue_zscore_4q},
    "acq_125_fcf_vs_cfo_divergence":                     {"inputs": ["ncfo", "fcf"],                                              "func": acq_125_fcf_vs_cfo_divergence},
    "acq_126_fcf_vs_cfo_scaled_assets":                  {"inputs": ["ncfo", "fcf", "assets"],                                    "func": acq_126_fcf_vs_cfo_scaled_assets},
    "acq_127_capex_to_depamor_ratio":                    {"inputs": ["fcf", "ncfo", "depamor"],                                   "func": acq_127_capex_to_depamor_ratio},
    "acq_128_operating_leverage_accruals":               {"inputs": ["netinc", "ncfo", "revenue"],                                "func": acq_128_operating_leverage_accruals},
    "acq_129_accruals_ewm_4q":                           {"inputs": ["netinc", "ncfo"],                                           "func": acq_129_accruals_ewm_4q},
    "acq_130_accruals_vs_ewm_deviation":                 {"inputs": ["netinc", "ncfo"],                                           "func": acq_130_accruals_vs_ewm_deviation},
    "acq_131_cfo_below_netinc_magnitude":                {"inputs": ["netinc", "ncfo"],                                           "func": acq_131_cfo_below_netinc_magnitude},
    "acq_132_cfo_below_netinc_4q_sum":                   {"inputs": ["netinc", "ncfo"],                                           "func": acq_132_cfo_below_netinc_4q_sum},
    "acq_133_cfo_below_netinc_4q_sum_scaled_assets":     {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_133_cfo_below_netinc_4q_sum_scaled_assets},
    "acq_134_accruals_ratio_high_flag":                  {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_134_accruals_ratio_high_flag},
    "acq_135_accruals_ratio_rising_and_high":            {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_135_accruals_ratio_rising_and_high},
    "acq_136_accruals_ratio_max_4q":                     {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_136_accruals_ratio_max_4q},
    "acq_137_accruals_ratio_max_8q":                     {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_137_accruals_ratio_max_8q},
    "acq_138_accruals_ratio_min_4q":                     {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_138_accruals_ratio_min_4q},
    "acq_139_accruals_ratio_range_4q":                   {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_139_accruals_ratio_range_4q},
    "acq_140_accruals_volatility_4q":                    {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_140_accruals_volatility_4q},
    "acq_141_accruals_volatility_8q":                    {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_141_accruals_volatility_8q},
    "acq_142_cfo_to_assets_ratio":                       {"inputs": ["ncfo", "assets"],                                           "func": acq_142_cfo_to_assets_ratio},
    "acq_143_cfo_to_assets_qoq_change":                  {"inputs": ["ncfo", "assets"],                                           "func": acq_143_cfo_to_assets_qoq_change},
    "acq_144_fcf_to_assets_ratio":                       {"inputs": ["fcf", "assets"],                                            "func": acq_144_fcf_to_assets_ratio},
    "acq_145_fcf_to_assets_qoq_change":                  {"inputs": ["fcf", "assets"],                                            "func": acq_145_fcf_to_assets_qoq_change},
    "acq_146_accruals_to_equity_ratio":                  {"inputs": ["netinc", "ncfo", "equity"],                                 "func": acq_146_accruals_to_equity_ratio},
    "acq_147_accruals_to_equity_qoq_change":             {"inputs": ["netinc", "ncfo", "equity"],                                 "func": acq_147_accruals_to_equity_qoq_change},
    "acq_148_ncfi_vs_depamor":                           {"inputs": ["ncfi", "depamor"],                                          "func": acq_148_ncfi_vs_depamor},
    "acq_149_accruals_quality_composite_3signal":        {"inputs": ["netinc", "ncfo", "assets", "revenue", "receivables"],       "func": acq_149_accruals_quality_composite_3signal},
    "acq_150_accruals_high_consecutive_quarters_3y":     {"inputs": ["netinc", "ncfo", "assets"],                                 "func": acq_150_accruals_high_consecutive_quarters_3y},
}
