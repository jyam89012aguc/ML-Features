"""
71_accruals_quality — Base Features 001-075
Domain: earnings-quality erosion via accruals — divergence between reported net
income and operating cash flow, Sloan accruals ratio, working-capital accruals,
cash-backed vs accrual-backed earnings, red-flag constellations.
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Total accruals level and Sloan accrual ratio ---

def acq_001_total_accruals(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Total accruals = net income minus operating cash flow (Sloan 1996)."""
    return netinc - ncfo


def acq_002_sloan_accruals_ratio(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Sloan accruals ratio = (netinc - ncfo) / avg total assets."""
    accruals = netinc - ncfo
    avg_assets = _rolling_mean(assets, _TD_2Q)
    return _safe_div(accruals, avg_assets)


def acq_003_total_accruals_scaled_assets(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Total accruals scaled by total assets (point-in-time, not averaged)."""
    return _safe_div(netinc - ncfo, assets)


def acq_004_accruals_qoq_change(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ change in total accruals (netinc - ncfo)."""
    acc = netinc - ncfo
    return acc - acc.shift(_TD_QTR)


def acq_005_accruals_yoy_change(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """YoY change in total accruals."""
    acc = netinc - ncfo
    return acc - acc.shift(_TD_YEAR)


def acq_006_accruals_ratio_pct_rank_3y(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 3-year (756-day) percentile rank of the Sloan accruals ratio (position in 3-year accrual history)."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_007_cfo_to_netinc_ratio_zscore_4q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Rolling 4-quarter z-score of the CFO/|netinc| cash backing ratio (low z-score = cash quality eroding)."""
    ratio = _safe_div_abs(ncfo, netinc)
    return _zscore_rolling(ratio, _TD_YEAR)


def acq_008_accruals_is_positive(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Binary: 1 when total accruals > 0 (netinc exceeds ncfo)."""
    return ((netinc - ncfo) > 0).astype(float)


def acq_009_accruals_positive_quarters_1y(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Count of quarters in last 252 days where accruals > 0."""
    flag = ((netinc - ncfo) > 0).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def acq_010_accruals_positive_quarters_2y(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Count of quarters in last 504 days where accruals > 0."""
    flag = ((netinc - ncfo) > 0).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def acq_011_accruals_4q_rolling_mean(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of total accruals."""
    acc = netinc - ncfo
    return _rolling_mean(acc, _TD_YEAR)


def acq_012_accruals_8q_rolling_mean(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Trailing 8-quarter mean of total accruals."""
    acc = netinc - ncfo
    return _rolling_mean(acc, _TD_2Y)


def acq_013_accruals_ratio_4q_rolling_mean(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of the Sloan accruals ratio."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_mean(ratio, _TD_YEAR)


def acq_014_accruals_ratio_zscore_4q(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of the Sloan accruals ratio within a trailing 4-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _zscore_rolling(ratio, _TD_YEAR)


def acq_015_accruals_ratio_zscore_8q(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of the Sloan accruals ratio within a trailing 8-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _zscore_rolling(ratio, _TD_2Y)


# --- Group B (016-030): Cash-flow vs net-income divergence ---

def acq_016_ncfo_minus_netinc(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Operating cash flow minus net income (positive = cash quality is good)."""
    return ncfo - netinc


def acq_017_cfo_to_netinc_ratio(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Operating cash flow divided by absolute net income (cash backing ratio)."""
    return _safe_div_abs(ncfo, netinc)


def acq_018_cfo_to_netinc_ratio_4q_avg(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of the CFO/netinc ratio."""
    ratio = _safe_div_abs(ncfo, netinc)
    return _rolling_mean(ratio, _TD_YEAR)


def acq_019_cfo_to_netinc_ratio_zscore_8q(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Rolling 8-quarter (2-year) z-score of the CFO/|netinc| cash backing ratio (2-year cash quality extremity)."""
    ratio = _safe_div_abs(ncfo, netinc)
    return _zscore_rolling(ratio, _TD_2Y)


def acq_020_cfo_to_netinc_ratio_vs_4q_mean(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """CFO/|netinc| ratio minus its 4-quarter rolling mean (deviation from recent cash quality baseline)."""
    ratio = _safe_div_abs(ncfo, netinc)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def acq_021_cfo_to_netinc_below_one(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Binary: 1 when CFO/|netinc| < 1 (earnings exceed operating cash flow)."""
    ratio = _safe_div_abs(ncfo, netinc)
    return (ratio < 1.0).astype(float)


def acq_022_netinc_pos_ncfo_neg_flag(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Red-flag binary: 1 when netinc > 0 AND ncfo < 0 simultaneously."""
    return ((netinc > 0) & (ncfo < 0)).astype(float)


def acq_023_netinc_pos_ncfo_neg_quarters_1y(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Count of red-flag quarters (netinc>0, ncfo<0) in trailing 252 days."""
    flag = ((netinc > 0) & (ncfo < 0)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def acq_024_netinc_pos_ncfo_neg_quarters_2y(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Count of red-flag quarters (netinc>0, ncfo<0) in trailing 504 days."""
    flag = ((netinc > 0) & (ncfo < 0)).astype(float)
    return _rolling_sum(flag, _TD_2Y)


def acq_025_ncfo_divergence_scaled_revenue(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """(netinc - ncfo) / |revenue| — accruals divergence scaled by revenue."""
    return _safe_div_abs(netinc - ncfo, revenue)


def acq_026_ncfo_divergence_4q_avg_scaled_revenue(netinc: pd.Series, ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """4-quarter rolling mean of (netinc-ncfo)/|revenue|."""
    ratio = _safe_div_abs(netinc - ncfo, revenue)
    return _rolling_mean(ratio, _TD_YEAR)


def acq_027_fcf_to_netinc_ratio(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Free cash flow divided by absolute net income."""
    return _safe_div_abs(fcf, netinc)


def acq_028_fcf_minus_netinc_gap(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """FCF minus net income — wide gap flags accrual inflation of earnings."""
    return fcf - netinc


def acq_029_fcf_minus_netinc_gap_scaled_assets(netinc: pd.Series, fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """(FCF - netinc) / total assets."""
    return _safe_div(fcf - netinc, assets)


def acq_030_fcf_minus_netinc_gap_qoq(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """QoQ change in the FCF-minus-netinc gap."""
    gap = fcf - netinc
    return gap - gap.shift(_TD_QTR)


# --- Group C (031-045): Working-capital accruals ---

def acq_031_wc_accruals(receivables: pd.Series, inventory: pd.Series, payables: pd.Series) -> pd.Series:
    """
    Working-capital accruals = change in (receivables + inventory - payables).
    QoQ first difference of working capital items.
    """
    wc = receivables + inventory - payables
    return wc - wc.shift(_TD_QTR)


def acq_032_wc_accruals_scaled_assets(receivables: pd.Series, inventory: pd.Series,
                                       payables: pd.Series, assets: pd.Series) -> pd.Series:
    """Working-capital accruals scaled by total assets."""
    wc = receivables + inventory - payables
    delta_wc = wc - wc.shift(_TD_QTR)
    return _safe_div(delta_wc, assets)


def acq_033_receivables_change_qoq(receivables: pd.Series) -> pd.Series:
    """QoQ change in accounts receivable (rising AR = accrual inflation risk)."""
    return receivables - receivables.shift(_TD_QTR)


def acq_034_receivables_change_scaled_revenue(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in receivables / |revenue| — receivables as fraction of sales."""
    delta = receivables - receivables.shift(_TD_QTR)
    return _safe_div_abs(delta, revenue)


def acq_035_inventory_change_qoq(inventory: pd.Series) -> pd.Series:
    """QoQ change in inventory (rising inventory = potential demand weakness)."""
    return inventory - inventory.shift(_TD_QTR)


def acq_036_inventory_change_scaled_revenue(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in inventory / |revenue|."""
    delta = inventory - inventory.shift(_TD_QTR)
    return _safe_div_abs(delta, revenue)


def acq_037_payables_change_qoq(payables: pd.Series) -> pd.Series:
    """QoQ change in accounts payable (falling payables = reduced credit from suppliers)."""
    return payables - payables.shift(_TD_QTR)


def acq_038_receivables_to_revenue_ratio(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Receivables / revenue — days-sales-outstanding proxy."""
    return _safe_div_abs(receivables, revenue)


def acq_039_receivables_to_revenue_qoq_change(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in receivables/revenue ratio."""
    ratio = _safe_div_abs(receivables, revenue)
    return ratio - ratio.shift(_TD_QTR)


def acq_040_inventory_to_revenue_ratio(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory / revenue — inventory days proxy."""
    return _safe_div_abs(inventory, revenue)


def acq_041_inventory_to_revenue_qoq_change(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in inventory/revenue ratio."""
    ratio = _safe_div_abs(inventory, revenue)
    return ratio - ratio.shift(_TD_QTR)


def acq_042_wc_accruals_4q_sum(receivables: pd.Series, inventory: pd.Series,
                                payables: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of working-capital accruals."""
    wc = receivables + inventory - payables
    delta_wc = wc - wc.shift(_TD_QTR)
    return _rolling_sum(delta_wc, _TD_YEAR)


def acq_043_wc_accruals_rising_flag(receivables: pd.Series, inventory: pd.Series,
                                     payables: pd.Series) -> pd.Series:
    """Binary: 1 when working-capital accruals are higher than prior quarter."""
    wc = receivables + inventory - payables
    delta_wc = wc - wc.shift(_TD_QTR)
    return (delta_wc > delta_wc.shift(_TD_QTR)).astype(float)


def acq_044_wc_accruals_zscore_4q(receivables: pd.Series, inventory: pd.Series,
                                    payables: pd.Series) -> pd.Series:
    """Z-score of working-capital accruals in trailing 4-quarter window."""
    wc = receivables + inventory - payables
    delta_wc = wc - wc.shift(_TD_QTR)
    return _zscore_rolling(delta_wc, _TD_YEAR)


def acq_045_net_wc_level(receivables: pd.Series, inventory: pd.Series,
                          payables: pd.Series) -> pd.Series:
    """Net working capital position: receivables + inventory - payables (level)."""
    return receivables + inventory - payables


# --- Group D (046-060): Depreciation-adjusted accruals and D&A effects ---

def acq_046_operating_accruals_depamor_adj(netinc: pd.Series, ncfo: pd.Series,
                                            depamor: pd.Series) -> pd.Series:
    """
    Depreciation-adjusted total accruals: (netinc - ncfo) - depamor.
    Separates non-cash D&A from accrual-driven divergence.
    """
    return (netinc - ncfo) - depamor


def acq_047_depamor_to_netinc_ratio(netinc: pd.Series, depamor: pd.Series) -> pd.Series:
    """D&A / |netinc| — captures how much of reported earnings is offset by D&A."""
    return _safe_div_abs(depamor, netinc)


def acq_048_depamor_to_assets_ratio(depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """D&A / total assets — asset-intensity of depreciation."""
    return _safe_div(depamor, assets)


def acq_049_depamor_to_revenue_ratio(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """D&A / revenue — depreciation as fraction of sales."""
    return _safe_div_abs(depamor, revenue)


def acq_050_ebitda_minus_ncfo(ncfo: pd.Series, depamor: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    EBITDA proxy minus operating cash flow: (netinc + depamor) - ncfo.
    Positive values indicate earnings boosted above cash generation even after D&A add-back.
    """
    ebitda_proxy = netinc + depamor
    return ebitda_proxy - ncfo


def acq_051_ebitda_to_ncfo_ratio(ncfo: pd.Series, depamor: pd.Series, netinc: pd.Series) -> pd.Series:
    """EBITDA proxy / |ncfo|; ratio > 1 means non-cash items inflate EBITDA above cash."""
    ebitda_proxy = netinc + depamor
    return _safe_div_abs(ebitda_proxy, ncfo)


def acq_052_depamor_change_qoq(depamor: pd.Series) -> pd.Series:
    """QoQ change in D&A; rising D&A can mask worsening asset quality."""
    return depamor - depamor.shift(_TD_QTR)


def acq_053_depamor_change_yoy(depamor: pd.Series) -> pd.Series:
    """YoY change in D&A."""
    return depamor - depamor.shift(_TD_YEAR)


def acq_054_accruals_ex_depamor_scaled_assets(netinc: pd.Series, ncfo: pd.Series,
                                               depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """(netinc - ncfo - depamor) / assets — non-D&A accruals scaled by assets."""
    return _safe_div((netinc - ncfo) - depamor, assets)


def acq_055_cash_earnings_fraction(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    Fraction of earnings backed by cash: ncfo / (ncfo + |accruals|).
    Approaches 1 when earnings are fully cash-backed; <0.5 is a red flag.
    """
    accruals = (netinc - ncfo).abs()
    return _safe_div(ncfo.clip(lower=0), ncfo.clip(lower=0) + accruals)


def acq_056_accruals_to_ebitda(netinc: pd.Series, ncfo: pd.Series,
                                depamor: pd.Series) -> pd.Series:
    """Total accruals / EBITDA proxy; measures accrual inflation relative to operating profit."""
    ebitda_proxy = netinc + depamor
    return _safe_div_abs(netinc - ncfo, ebitda_proxy)


def acq_057_ncfo_to_ebitda_ratio(ncfo: pd.Series, netinc: pd.Series,
                                  depamor: pd.Series) -> pd.Series:
    """ncfo / EBITDA proxy — cash conversion of EBITDA."""
    ebitda_proxy = netinc + depamor
    return _safe_div_abs(ncfo, ebitda_proxy)


def acq_058_depamor_4q_avg(depamor: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of D&A (smoothed depreciation run-rate)."""
    return _rolling_mean(depamor, _TD_YEAR)


def acq_059_depamor_vs_4q_avg(depamor: pd.Series) -> pd.Series:
    """D&A deviation from its own 4-quarter mean."""
    return depamor - _rolling_mean(depamor, _TD_YEAR)


def acq_060_accruals_4q_sum_scaled_assets(netinc: pd.Series, ncfo: pd.Series,
                                           assets: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of accruals / total assets (TTM Sloan ratio)."""
    acc = netinc - ncfo
    return _safe_div(_rolling_sum(acc, _TD_YEAR), assets)


# --- Group E (061-075): Composite, trend, rank, and reversal signals ---

def acq_061_accruals_ratio_4q_pct_rank(netinc: pd.Series, ncfo: pd.Series,
                                        assets: pd.Series) -> pd.Series:
    """Percentile rank of Sloan accruals ratio in trailing 4-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def acq_062_accruals_ratio_8q_pct_rank(netinc: pd.Series, ncfo: pd.Series,
                                        assets: pd.Series) -> pd.Series:
    """Percentile rank of Sloan accruals ratio in trailing 8-quarter window."""
    ratio = _safe_div(netinc - ncfo, assets)
    return _rolling_rank_pct(ratio, _TD_2Y)


def acq_063_accruals_ratio_expanding_pct_rank(netinc: pd.Series, ncfo: pd.Series,
                                               assets: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of Sloan accruals ratio."""
    ratio = _safe_div(netinc - ncfo, assets)
    return ratio.expanding(min_periods=2).rank(pct=True)


def acq_064_cfo_to_netinc_4q_pct_rank(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Percentile rank of CFO/netinc cash backing ratio in trailing 4-quarter window."""
    ratio = _safe_div_abs(ncfo, netinc)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def acq_065_wc_accruals_pct_rank_4q(receivables: pd.Series, inventory: pd.Series,
                                      payables: pd.Series) -> pd.Series:
    """Percentile rank of working-capital accruals in trailing 4-quarter window."""
    wc = receivables + inventory - payables
    delta_wc = wc - wc.shift(_TD_QTR)
    return _rolling_rank_pct(delta_wc, _TD_YEAR)


def acq_066_accruals_consecutive_rise_streak(netinc: pd.Series, ncfo: pd.Series,
                                              assets: pd.Series) -> pd.Series:
    """
    Current consecutive-quarter streak of rising Sloan accruals ratio.
    Resets to 0 when the ratio declines.
    """
    ratio = _safe_div(netinc - ncfo, assets)
    rising = (ratio > ratio.shift(_TD_QTR)).astype(int)
    arr = rising.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=netinc.index)


def acq_067_accruals_reversal_flag(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    1 when accruals were positive last quarter and are negative this quarter
    (potential accrual reversal — earnings reverting toward cash flow).
    """
    acc = netinc - ncfo
    curr_neg  = (acc < 0).astype(float)
    prior_pos = (acc.shift(_TD_QTR) > 0).astype(float)
    return curr_neg * prior_pos


def acq_068_accruals_reversal_magnitude(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Magnitude of accrual reversal: current accruals minus prior-quarter accruals (signed)."""
    acc = netinc - ncfo
    return acc - acc.shift(_TD_QTR)


def acq_069_accrual_quality_composite_4q(netinc: pd.Series, ncfo: pd.Series,
                                          assets: pd.Series,
                                          receivables: pd.Series,
                                          inventory: pd.Series,
                                          payables: pd.Series) -> pd.Series:
    """
    Composite accrual quality score: equally weighted average z-score of
    (1) Sloan accruals ratio and (2) WC accruals/assets; higher = worse quality.
    """
    sloan_ratio = _safe_div(netinc - ncfo, assets)
    wc = receivables + inventory - payables
    wc_acc = _safe_div(wc - wc.shift(_TD_QTR), assets)
    z1 = _zscore_rolling(sloan_ratio, _TD_YEAR)
    z2 = _zscore_rolling(wc_acc, _TD_YEAR)
    return (z1 + z2) / 2.0


def acq_070_cfo_deficit_fraction_1y(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Fraction of 1-year window where CFO < net income (accruals positive)."""
    flag = ((ncfo < netinc)).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def acq_071_cfo_deficit_fraction_3y(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Fraction of 3-year window where CFO < net income."""
    flag = (ncfo < netinc).astype(float)
    return _rolling_mean(flag, _TD_3Y)


def acq_072_accruals_ratio_expanding_zscore(netinc: pd.Series, ncfo: pd.Series,
                                             assets: pd.Series) -> pd.Series:
    """Expanding z-score of Sloan accruals ratio — how extreme vs full history."""
    ratio = _safe_div(netinc - ncfo, assets)
    m  = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - m, sd)


def acq_073_fcf_to_netinc_4q_avg(netinc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of FCF/|netinc| cash coverage ratio."""
    ratio = _safe_div_abs(fcf, netinc)
    return _rolling_mean(ratio, _TD_YEAR)


def acq_074_netinc_accrual_component_fraction(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """
    Accrual component as fraction of |netinc|: (netinc - ncfo) / |netinc|.
    Values >> 1 indicate earnings are almost entirely accrual-driven.
    """
    return _safe_div_abs(netinc - ncfo, netinc)


def acq_075_high_accrual_and_positive_netinc_flag(netinc: pd.Series, ncfo: pd.Series,
                                                    assets: pd.Series) -> pd.Series:
    """
    Composite red-flag: 1 when netinc > 0 AND Sloan accruals ratio > 0.05.
    Signals high-accrual earnings that may not be sustainable.
    """
    sloan = _safe_div(netinc - ncfo, assets)
    return ((netinc > 0) & (sloan > 0.05)).astype(float)


# ── Registry 001-075 ──────────────────────────────────────────────────────────

ACCRUALS_QUALITY_REGISTRY_001_075 = {
    "acq_001_total_accruals":                        {"inputs": ["netinc", "ncfo"],                                        "func": acq_001_total_accruals},
    "acq_002_sloan_accruals_ratio":                  {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_002_sloan_accruals_ratio},
    "acq_003_total_accruals_scaled_assets":          {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_003_total_accruals_scaled_assets},
    "acq_004_accruals_qoq_change":                   {"inputs": ["netinc", "ncfo"],                                        "func": acq_004_accruals_qoq_change},
    "acq_005_accruals_yoy_change":                   {"inputs": ["netinc", "ncfo"],                                        "func": acq_005_accruals_yoy_change},
    "acq_006_accruals_ratio_pct_rank_3y":            {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_006_accruals_ratio_pct_rank_3y},
    "acq_007_cfo_to_netinc_ratio_zscore_4q":        {"inputs": ["netinc", "ncfo"],                                        "func": acq_007_cfo_to_netinc_ratio_zscore_4q},
    "acq_008_accruals_is_positive":                  {"inputs": ["netinc", "ncfo"],                                        "func": acq_008_accruals_is_positive},
    "acq_009_accruals_positive_quarters_1y":         {"inputs": ["netinc", "ncfo"],                                        "func": acq_009_accruals_positive_quarters_1y},
    "acq_010_accruals_positive_quarters_2y":         {"inputs": ["netinc", "ncfo"],                                        "func": acq_010_accruals_positive_quarters_2y},
    "acq_011_accruals_4q_rolling_mean":              {"inputs": ["netinc", "ncfo"],                                        "func": acq_011_accruals_4q_rolling_mean},
    "acq_012_accruals_8q_rolling_mean":              {"inputs": ["netinc", "ncfo"],                                        "func": acq_012_accruals_8q_rolling_mean},
    "acq_013_accruals_ratio_4q_rolling_mean":        {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_013_accruals_ratio_4q_rolling_mean},
    "acq_014_accruals_ratio_zscore_4q":              {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_014_accruals_ratio_zscore_4q},
    "acq_015_accruals_ratio_zscore_8q":              {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_015_accruals_ratio_zscore_8q},
    "acq_016_ncfo_minus_netinc":                     {"inputs": ["netinc", "ncfo"],                                        "func": acq_016_ncfo_minus_netinc},
    "acq_017_cfo_to_netinc_ratio":                   {"inputs": ["netinc", "ncfo"],                                        "func": acq_017_cfo_to_netinc_ratio},
    "acq_018_cfo_to_netinc_ratio_4q_avg":            {"inputs": ["netinc", "ncfo"],                                        "func": acq_018_cfo_to_netinc_ratio_4q_avg},
    "acq_019_cfo_to_netinc_ratio_zscore_8q":         {"inputs": ["netinc", "ncfo"],                                        "func": acq_019_cfo_to_netinc_ratio_zscore_8q},
    "acq_020_cfo_to_netinc_ratio_vs_4q_mean":        {"inputs": ["netinc", "ncfo"],                                        "func": acq_020_cfo_to_netinc_ratio_vs_4q_mean},
    "acq_021_cfo_to_netinc_below_one":               {"inputs": ["netinc", "ncfo"],                                        "func": acq_021_cfo_to_netinc_below_one},
    "acq_022_netinc_pos_ncfo_neg_flag":              {"inputs": ["netinc", "ncfo"],                                        "func": acq_022_netinc_pos_ncfo_neg_flag},
    "acq_023_netinc_pos_ncfo_neg_quarters_1y":       {"inputs": ["netinc", "ncfo"],                                        "func": acq_023_netinc_pos_ncfo_neg_quarters_1y},
    "acq_024_netinc_pos_ncfo_neg_quarters_2y":       {"inputs": ["netinc", "ncfo"],                                        "func": acq_024_netinc_pos_ncfo_neg_quarters_2y},
    "acq_025_ncfo_divergence_scaled_revenue":        {"inputs": ["netinc", "ncfo", "revenue"],                             "func": acq_025_ncfo_divergence_scaled_revenue},
    "acq_026_ncfo_divergence_4q_avg_scaled_revenue": {"inputs": ["netinc", "ncfo", "revenue"],                             "func": acq_026_ncfo_divergence_4q_avg_scaled_revenue},
    "acq_027_fcf_to_netinc_ratio":                   {"inputs": ["netinc", "fcf"],                                         "func": acq_027_fcf_to_netinc_ratio},
    "acq_028_fcf_minus_netinc_gap":                  {"inputs": ["netinc", "fcf"],                                         "func": acq_028_fcf_minus_netinc_gap},
    "acq_029_fcf_minus_netinc_gap_scaled_assets":    {"inputs": ["netinc", "fcf", "assets"],                               "func": acq_029_fcf_minus_netinc_gap_scaled_assets},
    "acq_030_fcf_minus_netinc_gap_qoq":              {"inputs": ["netinc", "fcf"],                                         "func": acq_030_fcf_minus_netinc_gap_qoq},
    "acq_031_wc_accruals":                           {"inputs": ["receivables", "inventory", "payables"],                  "func": acq_031_wc_accruals},
    "acq_032_wc_accruals_scaled_assets":             {"inputs": ["receivables", "inventory", "payables", "assets"],        "func": acq_032_wc_accruals_scaled_assets},
    "acq_033_receivables_change_qoq":                {"inputs": ["receivables"],                                           "func": acq_033_receivables_change_qoq},
    "acq_034_receivables_change_scaled_revenue":     {"inputs": ["receivables", "revenue"],                                 "func": acq_034_receivables_change_scaled_revenue},
    "acq_035_inventory_change_qoq":                  {"inputs": ["inventory"],                                             "func": acq_035_inventory_change_qoq},
    "acq_036_inventory_change_scaled_revenue":       {"inputs": ["inventory", "revenue"],                                  "func": acq_036_inventory_change_scaled_revenue},
    "acq_037_payables_change_qoq":                   {"inputs": ["payables"],                                              "func": acq_037_payables_change_qoq},
    "acq_038_receivables_to_revenue_ratio":          {"inputs": ["receivables", "revenue"],                                 "func": acq_038_receivables_to_revenue_ratio},
    "acq_039_receivables_to_revenue_qoq_change":     {"inputs": ["receivables", "revenue"],                                 "func": acq_039_receivables_to_revenue_qoq_change},
    "acq_040_inventory_to_revenue_ratio":            {"inputs": ["inventory", "revenue"],                                  "func": acq_040_inventory_to_revenue_ratio},
    "acq_041_inventory_to_revenue_qoq_change":       {"inputs": ["inventory", "revenue"],                                  "func": acq_041_inventory_to_revenue_qoq_change},
    "acq_042_wc_accruals_4q_sum":                    {"inputs": ["receivables", "inventory", "payables"],                  "func": acq_042_wc_accruals_4q_sum},
    "acq_043_wc_accruals_rising_flag":               {"inputs": ["receivables", "inventory", "payables"],                  "func": acq_043_wc_accruals_rising_flag},
    "acq_044_wc_accruals_zscore_4q":                 {"inputs": ["receivables", "inventory", "payables"],                  "func": acq_044_wc_accruals_zscore_4q},
    "acq_045_net_wc_level":                          {"inputs": ["receivables", "inventory", "payables"],                  "func": acq_045_net_wc_level},
    "acq_046_operating_accruals_depamor_adj":        {"inputs": ["netinc", "ncfo", "depamor"],                             "func": acq_046_operating_accruals_depamor_adj},
    "acq_047_depamor_to_netinc_ratio":               {"inputs": ["netinc", "depamor"],                                     "func": acq_047_depamor_to_netinc_ratio},
    "acq_048_depamor_to_assets_ratio":               {"inputs": ["depamor", "assets"],                                     "func": acq_048_depamor_to_assets_ratio},
    "acq_049_depamor_to_revenue_ratio":              {"inputs": ["depamor", "revenue"],                                    "func": acq_049_depamor_to_revenue_ratio},
    "acq_050_ebitda_minus_ncfo":                     {"inputs": ["ncfo", "depamor", "netinc"],                             "func": acq_050_ebitda_minus_ncfo},
    "acq_051_ebitda_to_ncfo_ratio":                  {"inputs": ["ncfo", "depamor", "netinc"],                             "func": acq_051_ebitda_to_ncfo_ratio},
    "acq_052_depamor_change_qoq":                    {"inputs": ["depamor"],                                               "func": acq_052_depamor_change_qoq},
    "acq_053_depamor_change_yoy":                    {"inputs": ["depamor"],                                               "func": acq_053_depamor_change_yoy},
    "acq_054_accruals_ex_depamor_scaled_assets":     {"inputs": ["netinc", "ncfo", "depamor", "assets"],                   "func": acq_054_accruals_ex_depamor_scaled_assets},
    "acq_055_cash_earnings_fraction":                {"inputs": ["netinc", "ncfo"],                                        "func": acq_055_cash_earnings_fraction},
    "acq_056_accruals_to_ebitda":                    {"inputs": ["netinc", "ncfo", "depamor"],                             "func": acq_056_accruals_to_ebitda},
    "acq_057_ncfo_to_ebitda_ratio":                  {"inputs": ["ncfo", "netinc", "depamor"],                             "func": acq_057_ncfo_to_ebitda_ratio},
    "acq_058_depamor_4q_avg":                        {"inputs": ["depamor"],                                               "func": acq_058_depamor_4q_avg},
    "acq_059_depamor_vs_4q_avg":                     {"inputs": ["depamor"],                                               "func": acq_059_depamor_vs_4q_avg},
    "acq_060_accruals_4q_sum_scaled_assets":         {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_060_accruals_4q_sum_scaled_assets},
    "acq_061_accruals_ratio_4q_pct_rank":            {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_061_accruals_ratio_4q_pct_rank},
    "acq_062_accruals_ratio_8q_pct_rank":            {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_062_accruals_ratio_8q_pct_rank},
    "acq_063_accruals_ratio_expanding_pct_rank":     {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_063_accruals_ratio_expanding_pct_rank},
    "acq_064_cfo_to_netinc_4q_pct_rank":             {"inputs": ["netinc", "ncfo"],                                        "func": acq_064_cfo_to_netinc_4q_pct_rank},
    "acq_065_wc_accruals_pct_rank_4q":               {"inputs": ["receivables", "inventory", "payables"],                  "func": acq_065_wc_accruals_pct_rank_4q},
    "acq_066_accruals_consecutive_rise_streak":      {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_066_accruals_consecutive_rise_streak},
    "acq_067_accruals_reversal_flag":                {"inputs": ["netinc", "ncfo"],                                        "func": acq_067_accruals_reversal_flag},
    "acq_068_accruals_reversal_magnitude":           {"inputs": ["netinc", "ncfo"],                                        "func": acq_068_accruals_reversal_magnitude},
    "acq_069_accrual_quality_composite_4q":          {"inputs": ["netinc", "ncfo", "assets", "receivables", "inventory", "payables"], "func": acq_069_accrual_quality_composite_4q},
    "acq_070_cfo_deficit_fraction_1y":               {"inputs": ["netinc", "ncfo"],                                        "func": acq_070_cfo_deficit_fraction_1y},
    "acq_071_cfo_deficit_fraction_3y":               {"inputs": ["netinc", "ncfo"],                                        "func": acq_071_cfo_deficit_fraction_3y},
    "acq_072_accruals_ratio_expanding_zscore":       {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_072_accruals_ratio_expanding_zscore},
    "acq_073_fcf_to_netinc_4q_avg":                  {"inputs": ["netinc", "fcf"],                                         "func": acq_073_fcf_to_netinc_4q_avg},
    "acq_074_netinc_accrual_component_fraction":     {"inputs": ["netinc", "ncfo"],                                        "func": acq_074_netinc_accrual_component_fraction},
    "acq_075_high_accrual_and_positive_netinc_flag": {"inputs": ["netinc", "ncfo", "assets"],                              "func": acq_075_high_accrual_and_positive_netinc_flag},
}
