"""
67_working_capital_drain — Base Features 001-075
Domain: working-capital depletion trend, cash-conversion-cycle deterioration
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Working capital level, NWC, and QoQ/YoY changes ---

def wcd_001_wc_level(workingcapital: pd.Series) -> pd.Series:
    """Working capital level (Sharadar field, current assets minus current liabilities)."""
    return workingcapital.copy()


def wcd_002_nwc_level(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Net working capital: assetsc - liabilitiesc (cross-check / alternate construction)."""
    return assetsc - liabilitiesc


def wcd_003_wc_qoq_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital absolute QoQ change (63-day lag)."""
    return workingcapital - workingcapital.shift(_TD_QTR)


def wcd_004_wc_yoy_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital absolute YoY change (252-day lag)."""
    return workingcapital - workingcapital.shift(_TD_YEAR)


def wcd_005_wc_2y_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital absolute change over 2 years (504-day lag)."""
    return workingcapital - workingcapital.shift(_TD_2Y)


def wcd_006_wc_3y_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital absolute change over 3 years (756-day lag)."""
    return workingcapital - workingcapital.shift(_TD_3Y)


def wcd_007_wc_qoq_pct(workingcapital: pd.Series) -> pd.Series:
    """Working capital QoQ percent change; denominator is abs(prior)."""
    prior = workingcapital.shift(_TD_QTR)
    return _safe_div_abs(workingcapital - prior, prior)


def wcd_008_wc_yoy_pct(workingcapital: pd.Series) -> pd.Series:
    """Working capital YoY percent change; denominator is abs(prior)."""
    prior = workingcapital.shift(_TD_YEAR)
    return _safe_div_abs(workingcapital - prior, prior)


def wcd_009_wc_2y_pct(workingcapital: pd.Series) -> pd.Series:
    """Working capital 2-year percent change; denominator is abs(prior)."""
    prior = workingcapital.shift(_TD_2Y)
    return _safe_div_abs(workingcapital - prior, prior)


def wcd_010_nwc_qoq_change(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """NWC (assetsc - liabilitiesc) QoQ absolute change."""
    nwc = assetsc - liabilitiesc
    return nwc - nwc.shift(_TD_QTR)


def wcd_011_nwc_yoy_change(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """NWC YoY absolute change."""
    nwc = assetsc - liabilitiesc
    return nwc - nwc.shift(_TD_YEAR)


def wcd_012_wc_is_negative(workingcapital: pd.Series) -> pd.Series:
    """Binary flag: 1 if working capital < 0 (negative WC = current insolvency risk)."""
    return (workingcapital < 0).astype(float)


def wcd_013_nwc_is_negative(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Binary flag: 1 if assetsc < liabilitiesc."""
    return (assetsc < liabilitiesc).astype(float)


def wcd_014_wc_turned_negative_flag(workingcapital: pd.Series) -> pd.Series:
    """1 when WC flips from non-negative (prior quarter) to negative (current)."""
    curr_neg  = (workingcapital < 0).astype(float)
    prior_pos = (workingcapital.shift(_TD_QTR) >= 0).astype(float)
    return curr_neg * prior_pos


def wcd_015_wc_consecutive_decline_streak(workingcapital: pd.Series) -> pd.Series:
    """
    Current consecutive-decline streak length (days) in working capital.
    Resets to 0 whenever WC is >= prior observation.
    """
    dec = (workingcapital < workingcapital.shift(1)).astype(int)
    streak = np.zeros(len(dec), dtype=float)
    arr = dec.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=workingcapital.index)


# --- Group B (016-025): WC as fraction of revenue and of assets ---

def wcd_016_wc_to_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """Working capital divided by revenue — WC adequacy relative to scale."""
    return _safe_div(workingcapital, revenue.abs().replace(0, np.nan))


def wcd_017_wc_to_assets(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Working capital divided by total assets — WC as fraction of asset base."""
    return _safe_div(workingcapital, assets.abs().replace(0, np.nan))


def wcd_018_wc_to_assetsc(workingcapital: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Working capital divided by current assets — coverage of current book value."""
    return _safe_div(workingcapital, assetsc.abs().replace(0, np.nan))


def wcd_019_nwc_to_revenue(assetsc: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series) -> pd.Series:
    """NWC divided by revenue."""
    nwc = assetsc - liabilitiesc
    return _safe_div(nwc, revenue.abs().replace(0, np.nan))


def wcd_020_wc_to_revenue_yoy_change(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in working-capital-to-revenue ratio."""
    ratio = _safe_div(workingcapital, revenue.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_021_wc_to_assets_yoy_change(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in working-capital-to-assets ratio."""
    ratio = _safe_div(workingcapital, assets.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_022_wc_to_revenue_qoq_change(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in working-capital-to-revenue ratio."""
    ratio = _safe_div(workingcapital, revenue.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_QTR)


def wcd_023_assetsc_to_liabilitiesc_ratio(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio: assetsc / liabilitiesc (trend context for WC drain direction)."""
    return _safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan))


def wcd_024_assetsc_to_liabilitiesc_yoy_change(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """YoY change in current ratio (deterioration trend)."""
    ratio = _safe_div(assetsc, liabilitiesc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_025_wc_to_liabilitiesc(workingcapital: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Working capital divided by current liabilities — net buffer per unit of near-term obligation."""
    return _safe_div(workingcapital, liabilitiesc.abs().replace(0, np.nan))


# --- Group C (026-040): Cash-conversion-cycle components (DSO, DIO, DPO, CCC) ---

def wcd_026_dso_days(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Days Sales Outstanding: receivables / (revenue / 91.25).
    Approximates days of revenue tied up in receivables. Rising DSO signals collection risk.
    Uses 91.25 days/quarter; SF1 fields are quarterly snap-shots.
    """
    daily_rev = revenue / 91.25
    return _safe_div(receivables, daily_rev.abs().replace(0, np.nan))


def wcd_027_dio_days(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """
    Days Inventory Outstanding: inventory / (cor / 91.25).
    Rising DIO signals inventory build-up (demand weakness or over-ordering).
    """
    daily_cor = cor / 91.25
    return _safe_div(inventory, daily_cor.abs().replace(0, np.nan))


def wcd_028_dpo_days(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """
    Days Payable Outstanding: payables / (cor / 91.25).
    Rising DPO signals payables stretching (cash preservation at expense of suppliers).
    """
    daily_cor = cor / 91.25
    return _safe_div(payables, daily_cor.abs().replace(0, np.nan))


def wcd_029_ccc_days(receivables: pd.Series, inventory: pd.Series,
                     payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """
    Cash Conversion Cycle: DSO + DIO - DPO.
    Rising CCC indicates working capital is being absorbed by operations.
    """
    daily_rev = revenue / 91.25
    daily_cor = cor / 91.25
    dso = _safe_div(receivables, daily_rev.abs().replace(0, np.nan))
    dio = _safe_div(inventory, daily_cor.abs().replace(0, np.nan))
    dpo = _safe_div(payables, daily_cor.abs().replace(0, np.nan))
    return dso + dio - dpo


def wcd_030_dso_qoq_change(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in DSO (receivables build-up rate)."""
    dso = _safe_div(receivables, (revenue / 91.25).abs().replace(0, np.nan))
    return dso - dso.shift(_TD_QTR)


def wcd_031_dso_yoy_change(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in DSO."""
    dso = _safe_div(receivables, (revenue / 91.25).abs().replace(0, np.nan))
    return dso - dso.shift(_TD_YEAR)


def wcd_032_dio_qoq_change(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ change in DIO (inventory build-up rate)."""
    dio = _safe_div(inventory, (cor / 91.25).abs().replace(0, np.nan))
    return dio - dio.shift(_TD_QTR)


def wcd_033_dio_yoy_change(inventory: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in DIO."""
    dio = _safe_div(inventory, (cor / 91.25).abs().replace(0, np.nan))
    return dio - dio.shift(_TD_YEAR)


def wcd_034_dpo_qoq_change(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ change in DPO (payables stretching rate)."""
    dpo = _safe_div(payables, (cor / 91.25).abs().replace(0, np.nan))
    return dpo - dpo.shift(_TD_QTR)


def wcd_035_dpo_yoy_change(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in DPO."""
    dpo = _safe_div(payables, (cor / 91.25).abs().replace(0, np.nan))
    return dpo - dpo.shift(_TD_YEAR)


def wcd_036_ccc_qoq_change(receivables: pd.Series, inventory: pd.Series,
                            payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """QoQ change in CCC — captures acceleration of WC drain via operations."""
    dr = (revenue / 91.25).abs().replace(0, np.nan)
    dc = (cor / 91.25).abs().replace(0, np.nan)
    ccc = _safe_div(receivables, dr) + _safe_div(inventory, dc) - _safe_div(payables, dc)
    return ccc - ccc.shift(_TD_QTR)


def wcd_037_ccc_yoy_change(receivables: pd.Series, inventory: pd.Series,
                            payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """YoY change in CCC."""
    dr = (revenue / 91.25).abs().replace(0, np.nan)
    dc = (cor / 91.25).abs().replace(0, np.nan)
    ccc = _safe_div(receivables, dr) + _safe_div(inventory, dc) - _safe_div(payables, dc)
    return ccc - ccc.shift(_TD_YEAR)


def wcd_038_dso_zscore_4q(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of DSO within trailing 4-quarter (252-day) window."""
    dso = _safe_div(receivables, (revenue / 91.25).abs().replace(0, np.nan))
    return _zscore_rolling(dso, _TD_YEAR)


def wcd_039_ccc_zscore_4q(receivables: pd.Series, inventory: pd.Series,
                           payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """Z-score of CCC within trailing 4-quarter window."""
    dr = (revenue / 91.25).abs().replace(0, np.nan)
    dc = (cor / 91.25).abs().replace(0, np.nan)
    ccc = _safe_div(receivables, dr) + _safe_div(inventory, dc) - _safe_div(payables, dc)
    return _zscore_rolling(ccc, _TD_YEAR)


def wcd_040_ccc_drawdown_from_4q_trough(receivables: pd.Series, inventory: pd.Series,
                                         payables: pd.Series, revenue: pd.Series, cor: pd.Series) -> pd.Series:
    """
    CCC minus its rolling 4-quarter minimum (trough).
    Rising value = CCC worsening vs recent best level.
    """
    dr = (revenue / 91.25).abs().replace(0, np.nan)
    dc = (cor / 91.25).abs().replace(0, np.nan)
    ccc = _safe_div(receivables, dr) + _safe_div(inventory, dc) - _safe_div(payables, dc)
    trough = _rolling_min(ccc, _TD_YEAR)
    return ccc - trough


# --- Group D (041-055): Receivables and inventory build-up vs WC ---

def wcd_041_receivables_qoq_change(receivables: pd.Series) -> pd.Series:
    """Receivables absolute QoQ change (build-up signal)."""
    return receivables - receivables.shift(_TD_QTR)


def wcd_042_inventory_qoq_change(inventory: pd.Series) -> pd.Series:
    """Inventory absolute QoQ change (excess inventory build signal)."""
    return inventory - inventory.shift(_TD_QTR)


def wcd_043_receivables_to_revenue(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Receivables as a fraction of revenue — rising ratio signals collection deterioration."""
    return _safe_div(receivables, revenue.abs().replace(0, np.nan))


def wcd_044_inventory_to_revenue(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Inventory as a fraction of revenue — rising ratio signals demand softness."""
    return _safe_div(inventory, revenue.abs().replace(0, np.nan))


def wcd_045_payables_to_cor(payables: pd.Series, cor: pd.Series) -> pd.Series:
    """Payables as a fraction of COGS — rising signals supplier stress / stretched terms."""
    return _safe_div(payables, cor.abs().replace(0, np.nan))


def wcd_046_receivables_yoy_pct(receivables: pd.Series) -> pd.Series:
    """Receivables YoY percent change; denominator is abs(prior)."""
    prior = receivables.shift(_TD_YEAR)
    return _safe_div_abs(receivables - prior, prior)


def wcd_047_inventory_yoy_pct(inventory: pd.Series) -> pd.Series:
    """Inventory YoY percent change; denominator is abs(prior)."""
    prior = inventory.shift(_TD_YEAR)
    return _safe_div_abs(inventory - prior, prior)


def wcd_048_receivables_minus_wc_change(receivables: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """
    QoQ change in receivables minus QoQ change in WC.
    Positive = receivables growing faster than overall WC (crowding out cash).
    """
    dr = receivables - receivables.shift(_TD_QTR)
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return dr - dw


def wcd_049_inventory_minus_wc_change(inventory: pd.Series, workingcapital: pd.Series) -> pd.Series:
    """
    QoQ change in inventory minus QoQ change in WC.
    Positive = inventory growing faster than overall WC.
    """
    di = inventory - inventory.shift(_TD_QTR)
    dw = workingcapital - workingcapital.shift(_TD_QTR)
    return di - dw


def wcd_050_receivables_to_assetsc(receivables: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Receivables as fraction of current assets — composition shift signal."""
    return _safe_div(receivables, assetsc.abs().replace(0, np.nan))


def wcd_051_inventory_to_assetsc(inventory: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Inventory as fraction of current assets."""
    return _safe_div(inventory, assetsc.abs().replace(0, np.nan))


def wcd_052_cash_to_assetsc(cashnequiv: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Cash fraction of current assets — declining cash share within current assets."""
    return _safe_div(cashnequiv, assetsc.abs().replace(0, np.nan))


def wcd_053_cash_to_assetsc_yoy_change(cashnequiv: pd.Series, assetsc: pd.Series) -> pd.Series:
    """YoY change in cash's share of current assets."""
    ratio = _safe_div(cashnequiv, assetsc.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_054_receivables_to_revenue_yoy_change(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in receivables-to-revenue ratio."""
    ratio = _safe_div(receivables, revenue.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


def wcd_055_inventory_to_revenue_yoy_change(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in inventory-to-revenue ratio."""
    ratio = _safe_div(inventory, revenue.abs().replace(0, np.nan))
    return ratio - ratio.shift(_TD_YEAR)


# --- Group E (056-065): WC drawdown from trailing peak ---

def wcd_056_wc_drawdown_from_4q_peak(workingcapital: pd.Series) -> pd.Series:
    """Working capital vs its rolling 4-quarter peak (level drawdown)."""
    peak = _rolling_max(workingcapital, _TD_YEAR)
    return workingcapital - peak


def wcd_057_wc_drawdown_from_8q_peak(workingcapital: pd.Series) -> pd.Series:
    """Working capital vs its rolling 8-quarter peak."""
    peak = _rolling_max(workingcapital, _TD_2Y)
    return workingcapital - peak


def wcd_058_wc_drawdown_from_12q_peak(workingcapital: pd.Series) -> pd.Series:
    """Working capital vs its rolling 12-quarter (3-year) peak."""
    peak = _rolling_max(workingcapital, _TD_3Y)
    return workingcapital - peak


def wcd_059_wc_pct_drawdown_from_4q_peak(workingcapital: pd.Series) -> pd.Series:
    """Percent drawdown of WC from its 4-quarter peak."""
    peak = _rolling_max(workingcapital, _TD_YEAR)
    return _safe_div_abs(workingcapital - peak, peak)


def wcd_060_wc_pct_drawdown_from_8q_peak(workingcapital: pd.Series) -> pd.Series:
    """Percent drawdown of WC from its 8-quarter peak."""
    peak = _rolling_max(workingcapital, _TD_2Y)
    return _safe_div_abs(workingcapital - peak, peak)


def wcd_061_wc_drawdown_from_expanding_peak(workingcapital: pd.Series) -> pd.Series:
    """WC vs its all-history expanding maximum."""
    peak = workingcapital.expanding(min_periods=1).max()
    return workingcapital - peak


def wcd_062_wc_pct_drawdown_from_expanding_peak(workingcapital: pd.Series) -> pd.Series:
    """Percent drawdown of WC from its all-history expanding peak."""
    peak = workingcapital.expanding(min_periods=1).max()
    return _safe_div_abs(workingcapital - peak, peak)


def wcd_063_wc_min_4q(workingcapital: pd.Series) -> pd.Series:
    """Worst (minimum) working capital in trailing 4 quarters (252 days)."""
    return _rolling_min(workingcapital, _TD_YEAR)


def wcd_064_wc_min_8q(workingcapital: pd.Series) -> pd.Series:
    """Worst working capital in trailing 8 quarters."""
    return _rolling_min(workingcapital, _TD_2Y)


def wcd_065_wc_min_12q(workingcapital: pd.Series) -> pd.Series:
    """Worst working capital in trailing 12 quarters."""
    return _rolling_min(workingcapital, _TD_3Y)


# --- Group F (066-075): Z-scores, percentile ranks, and composite severity ---

def wcd_066_wc_zscore_4q(workingcapital: pd.Series) -> pd.Series:
    """Z-score of working capital within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(workingcapital, _TD_YEAR)


def wcd_067_wc_zscore_8q(workingcapital: pd.Series) -> pd.Series:
    """Z-score of working capital within trailing 8-quarter window."""
    return _zscore_rolling(workingcapital, _TD_2Y)


def wcd_068_wc_zscore_12q(workingcapital: pd.Series) -> pd.Series:
    """Z-score of working capital within trailing 12-quarter window."""
    return _zscore_rolling(workingcapital, _TD_3Y)


def wcd_069_wc_expanding_zscore(workingcapital: pd.Series) -> pd.Series:
    """Expanding z-score of working capital (how extreme vs entire history)."""
    m  = workingcapital.expanding(min_periods=2).mean()
    sd = workingcapital.expanding(min_periods=2).std()
    return _safe_div(workingcapital - m, sd)


def wcd_070_wc_pct_rank_4q(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of working capital within trailing 4-quarter window."""
    return _rolling_rank_pct(workingcapital, _TD_YEAR)


def wcd_071_wc_pct_rank_8q(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of working capital within trailing 8-quarter window."""
    return _rolling_rank_pct(workingcapital, _TD_2Y)


def wcd_072_wc_ewm_deviation(workingcapital: pd.Series) -> pd.Series:
    """Working capital minus its 4-quarter EWM (span=252); captures momentum shift."""
    ewm = _ewm_mean(workingcapital, _TD_YEAR)
    return workingcapital - ewm


def wcd_073_wc_negative_quarters_1y(workingcapital: pd.Series) -> pd.Series:
    """Count of daily observations with negative WC in trailing 252 days."""
    neg = (workingcapital < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def wcd_074_wc_negative_quarters_3y(workingcapital: pd.Series) -> pd.Series:
    """Count of daily observations with negative WC in trailing 756 days."""
    neg = (workingcapital < 0).astype(float)
    return _rolling_sum(neg, _TD_3Y)


def wcd_075_wc_drain_composite(workingcapital: pd.Series, receivables: pd.Series,
                                inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Composite WC-drain severity: equally weighted mean of three z-scores in
    4-quarter window — WC level, receivables-to-revenue, inventory-to-revenue.
    Lower = more distressed (WC low, receivables/inventory ratios high).
    """
    z_wc  = _zscore_rolling(workingcapital, _TD_YEAR)
    rec_rev = _safe_div(receivables, revenue.abs().replace(0, np.nan))
    inv_rev = _safe_div(inventory, revenue.abs().replace(0, np.nan))
    z_rec = _zscore_rolling(rec_rev, _TD_YEAR)
    z_inv = _zscore_rolling(inv_rev, _TD_YEAR)
    return (z_wc - z_rec - z_inv) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

WORKING_CAPITAL_DRAIN_REGISTRY_001_075 = {
    "wcd_001_wc_level":                          {"inputs": ["workingcapital"],                                               "func": wcd_001_wc_level},
    "wcd_002_nwc_level":                         {"inputs": ["assetsc", "liabilitiesc"],                                      "func": wcd_002_nwc_level},
    "wcd_003_wc_qoq_change":                     {"inputs": ["workingcapital"],                                               "func": wcd_003_wc_qoq_change},
    "wcd_004_wc_yoy_change":                     {"inputs": ["workingcapital"],                                               "func": wcd_004_wc_yoy_change},
    "wcd_005_wc_2y_change":                      {"inputs": ["workingcapital"],                                               "func": wcd_005_wc_2y_change},
    "wcd_006_wc_3y_change":                      {"inputs": ["workingcapital"],                                               "func": wcd_006_wc_3y_change},
    "wcd_007_wc_qoq_pct":                        {"inputs": ["workingcapital"],                                               "func": wcd_007_wc_qoq_pct},
    "wcd_008_wc_yoy_pct":                        {"inputs": ["workingcapital"],                                               "func": wcd_008_wc_yoy_pct},
    "wcd_009_wc_2y_pct":                         {"inputs": ["workingcapital"],                                               "func": wcd_009_wc_2y_pct},
    "wcd_010_nwc_qoq_change":                    {"inputs": ["assetsc", "liabilitiesc"],                                      "func": wcd_010_nwc_qoq_change},
    "wcd_011_nwc_yoy_change":                    {"inputs": ["assetsc", "liabilitiesc"],                                      "func": wcd_011_nwc_yoy_change},
    "wcd_012_wc_is_negative":                    {"inputs": ["workingcapital"],                                               "func": wcd_012_wc_is_negative},
    "wcd_013_nwc_is_negative":                   {"inputs": ["assetsc", "liabilitiesc"],                                      "func": wcd_013_nwc_is_negative},
    "wcd_014_wc_turned_negative_flag":           {"inputs": ["workingcapital"],                                               "func": wcd_014_wc_turned_negative_flag},
    "wcd_015_wc_consecutive_decline_streak":     {"inputs": ["workingcapital"],                                               "func": wcd_015_wc_consecutive_decline_streak},
    "wcd_016_wc_to_revenue":                     {"inputs": ["workingcapital", "revenue"],                                    "func": wcd_016_wc_to_revenue},
    "wcd_017_wc_to_assets":                      {"inputs": ["workingcapital", "assets"],                                     "func": wcd_017_wc_to_assets},
    "wcd_018_wc_to_assetsc":                     {"inputs": ["workingcapital", "assetsc"],                                    "func": wcd_018_wc_to_assetsc},
    "wcd_019_nwc_to_revenue":                    {"inputs": ["assetsc", "liabilitiesc", "revenue"],                           "func": wcd_019_nwc_to_revenue},
    "wcd_020_wc_to_revenue_yoy_change":          {"inputs": ["workingcapital", "revenue"],                                    "func": wcd_020_wc_to_revenue_yoy_change},
    "wcd_021_wc_to_assets_yoy_change":           {"inputs": ["workingcapital", "assets"],                                     "func": wcd_021_wc_to_assets_yoy_change},
    "wcd_022_wc_to_revenue_qoq_change":          {"inputs": ["workingcapital", "revenue"],                                    "func": wcd_022_wc_to_revenue_qoq_change},
    "wcd_023_assetsc_to_liabilitiesc_ratio":     {"inputs": ["assetsc", "liabilitiesc"],                                      "func": wcd_023_assetsc_to_liabilitiesc_ratio},
    "wcd_024_assetsc_to_liabilitiesc_yoy_change": {"inputs": ["assetsc", "liabilitiesc"],                                     "func": wcd_024_assetsc_to_liabilitiesc_yoy_change},
    "wcd_025_wc_to_liabilitiesc":               {"inputs": ["workingcapital", "liabilitiesc"],                               "func": wcd_025_wc_to_liabilitiesc},
    "wcd_026_dso_days":                          {"inputs": ["receivables", "revenue"],                                       "func": wcd_026_dso_days},
    "wcd_027_dio_days":                          {"inputs": ["inventory", "cor"],                                             "func": wcd_027_dio_days},
    "wcd_028_dpo_days":                          {"inputs": ["payables", "cor"],                                              "func": wcd_028_dpo_days},
    "wcd_029_ccc_days":                          {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],       "func": wcd_029_ccc_days},
    "wcd_030_dso_qoq_change":                    {"inputs": ["receivables", "revenue"],                                       "func": wcd_030_dso_qoq_change},
    "wcd_031_dso_yoy_change":                    {"inputs": ["receivables", "revenue"],                                       "func": wcd_031_dso_yoy_change},
    "wcd_032_dio_qoq_change":                    {"inputs": ["inventory", "cor"],                                             "func": wcd_032_dio_qoq_change},
    "wcd_033_dio_yoy_change":                    {"inputs": ["inventory", "cor"],                                             "func": wcd_033_dio_yoy_change},
    "wcd_034_dpo_qoq_change":                    {"inputs": ["payables", "cor"],                                              "func": wcd_034_dpo_qoq_change},
    "wcd_035_dpo_yoy_change":                    {"inputs": ["payables", "cor"],                                              "func": wcd_035_dpo_yoy_change},
    "wcd_036_ccc_qoq_change":                    {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],       "func": wcd_036_ccc_qoq_change},
    "wcd_037_ccc_yoy_change":                    {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],       "func": wcd_037_ccc_yoy_change},
    "wcd_038_dso_zscore_4q":                     {"inputs": ["receivables", "revenue"],                                       "func": wcd_038_dso_zscore_4q},
    "wcd_039_ccc_zscore_4q":                     {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],       "func": wcd_039_ccc_zscore_4q},
    "wcd_040_ccc_drawdown_from_4q_trough":       {"inputs": ["receivables", "inventory", "payables", "revenue", "cor"],       "func": wcd_040_ccc_drawdown_from_4q_trough},
    "wcd_041_receivables_qoq_change":            {"inputs": ["receivables"],                                                  "func": wcd_041_receivables_qoq_change},
    "wcd_042_inventory_qoq_change":              {"inputs": ["inventory"],                                                    "func": wcd_042_inventory_qoq_change},
    "wcd_043_receivables_to_revenue":            {"inputs": ["receivables", "revenue"],                                       "func": wcd_043_receivables_to_revenue},
    "wcd_044_inventory_to_revenue":              {"inputs": ["inventory", "revenue"],                                         "func": wcd_044_inventory_to_revenue},
    "wcd_045_payables_to_cor":                   {"inputs": ["payables", "cor"],                                              "func": wcd_045_payables_to_cor},
    "wcd_046_receivables_yoy_pct":               {"inputs": ["receivables"],                                                  "func": wcd_046_receivables_yoy_pct},
    "wcd_047_inventory_yoy_pct":                 {"inputs": ["inventory"],                                                    "func": wcd_047_inventory_yoy_pct},
    "wcd_048_receivables_minus_wc_change":       {"inputs": ["receivables", "workingcapital"],                                "func": wcd_048_receivables_minus_wc_change},
    "wcd_049_inventory_minus_wc_change":         {"inputs": ["inventory", "workingcapital"],                                  "func": wcd_049_inventory_minus_wc_change},
    "wcd_050_receivables_to_assetsc":            {"inputs": ["receivables", "assetsc"],                                       "func": wcd_050_receivables_to_assetsc},
    "wcd_051_inventory_to_assetsc":              {"inputs": ["inventory", "assetsc"],                                         "func": wcd_051_inventory_to_assetsc},
    "wcd_052_cash_to_assetsc":                   {"inputs": ["cashnequiv", "assetsc"],                                        "func": wcd_052_cash_to_assetsc},
    "wcd_053_cash_to_assetsc_yoy_change":        {"inputs": ["cashnequiv", "assetsc"],                                        "func": wcd_053_cash_to_assetsc_yoy_change},
    "wcd_054_receivables_to_revenue_yoy_change": {"inputs": ["receivables", "revenue"],                                       "func": wcd_054_receivables_to_revenue_yoy_change},
    "wcd_055_inventory_to_revenue_yoy_change":   {"inputs": ["inventory", "revenue"],                                         "func": wcd_055_inventory_to_revenue_yoy_change},
    "wcd_056_wc_drawdown_from_4q_peak":          {"inputs": ["workingcapital"],                                               "func": wcd_056_wc_drawdown_from_4q_peak},
    "wcd_057_wc_drawdown_from_8q_peak":          {"inputs": ["workingcapital"],                                               "func": wcd_057_wc_drawdown_from_8q_peak},
    "wcd_058_wc_drawdown_from_12q_peak":         {"inputs": ["workingcapital"],                                               "func": wcd_058_wc_drawdown_from_12q_peak},
    "wcd_059_wc_pct_drawdown_from_4q_peak":      {"inputs": ["workingcapital"],                                               "func": wcd_059_wc_pct_drawdown_from_4q_peak},
    "wcd_060_wc_pct_drawdown_from_8q_peak":      {"inputs": ["workingcapital"],                                               "func": wcd_060_wc_pct_drawdown_from_8q_peak},
    "wcd_061_wc_drawdown_from_expanding_peak":   {"inputs": ["workingcapital"],                                               "func": wcd_061_wc_drawdown_from_expanding_peak},
    "wcd_062_wc_pct_drawdown_from_expanding_peak": {"inputs": ["workingcapital"],                                             "func": wcd_062_wc_pct_drawdown_from_expanding_peak},
    "wcd_063_wc_min_4q":                         {"inputs": ["workingcapital"],                                               "func": wcd_063_wc_min_4q},
    "wcd_064_wc_min_8q":                         {"inputs": ["workingcapital"],                                               "func": wcd_064_wc_min_8q},
    "wcd_065_wc_min_12q":                        {"inputs": ["workingcapital"],                                               "func": wcd_065_wc_min_12q},
    "wcd_066_wc_zscore_4q":                      {"inputs": ["workingcapital"],                                               "func": wcd_066_wc_zscore_4q},
    "wcd_067_wc_zscore_8q":                      {"inputs": ["workingcapital"],                                               "func": wcd_067_wc_zscore_8q},
    "wcd_068_wc_zscore_12q":                     {"inputs": ["workingcapital"],                                               "func": wcd_068_wc_zscore_12q},
    "wcd_069_wc_expanding_zscore":               {"inputs": ["workingcapital"],                                               "func": wcd_069_wc_expanding_zscore},
    "wcd_070_wc_pct_rank_4q":                    {"inputs": ["workingcapital"],                                               "func": wcd_070_wc_pct_rank_4q},
    "wcd_071_wc_pct_rank_8q":                    {"inputs": ["workingcapital"],                                               "func": wcd_071_wc_pct_rank_8q},
    "wcd_072_wc_ewm_deviation":                  {"inputs": ["workingcapital"],                                               "func": wcd_072_wc_ewm_deviation},
    "wcd_073_wc_negative_quarters_1y":           {"inputs": ["workingcapital"],                                               "func": wcd_073_wc_negative_quarters_1y},
    "wcd_074_wc_negative_quarters_3y":           {"inputs": ["workingcapital"],                                               "func": wcd_074_wc_negative_quarters_3y},
    "wcd_075_wc_drain_composite":                {"inputs": ["workingcapital", "receivables", "inventory", "revenue"],        "func": wcd_075_wc_drain_composite},
}
