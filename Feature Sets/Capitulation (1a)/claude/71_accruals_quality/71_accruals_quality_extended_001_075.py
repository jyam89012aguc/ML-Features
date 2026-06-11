"""
71_accruals_quality — Extended Features 001-075
Domain: accruals quality — deeper variants, EWM smoothing, z-scores,
        percentile ranks, acceleration, cross-ratio composites, streak counters,
        multi-window flags, and skewness of accrual distribution.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_TD_QTR  = 63
_TD_2Q   = 126
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
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


def _consec_true(cond: pd.Series) -> pd.Series:
    c = cond.astype(int)
    grp = (~cond).cumsum()
    return c.groupby(grp).cumsum().astype(float)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    def _skew(x):
        v = x[~np.isnan(x)]
        if len(v) < 3:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd < _EPS:
            return np.nan
        return float(((v - m) ** 3).mean() / sd ** 3)
    return s.rolling(w, min_periods=max(3, w // 4)).apply(_skew, raw=True)


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    def _kurt(x):
        v = x[~np.isnan(x)]
        if len(v) < 4:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd < _EPS:
            return np.nan
        return float(((v - m) ** 4).mean() / sd ** 4) - 3.0
    return s.rolling(w, min_periods=max(4, w // 4)).apply(_kurt, raw=True)


# ── Extended Feature functions 001-075 ────────────────────────────────────────

# --- Group A (001-012): Balance-sheet accrual (BS accrual) deeper variants ---

def acq_ext_001_bs_accrual_3y_zscore(assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of balance-sheet accrual ratio (extreme = manipulated earnings)."""
    accrual = (assets - cashnequiv) - (liabilities - debt)
    avg_assets = _rolling_mean(assets, _TD_QTR)
    ratio = _safe_div(accrual, avg_assets)
    return _zscore_rolling(ratio, _TD_3Y)


def acq_ext_002_bs_accrual_pct_rank_3y(assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of balance-sheet accrual ratio."""
    accrual = (assets - cashnequiv) - (liabilities - debt)
    avg_assets = _rolling_mean(assets, _TD_QTR)
    ratio = _safe_div(accrual, avg_assets)
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_003_bs_accrual_ewm_slope(assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of BS accrual ratio — smoothed deterioration trend."""
    accrual = (assets - cashnequiv) - (liabilities - debt)
    avg_assets = _rolling_mean(assets, _TD_QTR)
    ratio = _safe_div(accrual, avg_assets)
    e = _ewm_mean(ratio, 63)
    return e - e.shift(_TD_QTR)


def acq_ext_004_bs_accrual_skew_3y(assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of BS accrual ratio."""
    accrual = (assets - cashnequiv) - (liabilities - debt)
    avg_assets = _rolling_mean(assets, _TD_QTR)
    ratio = _safe_div(accrual, avg_assets)
    return _rolling_skew(ratio, _TD_3Y)


def acq_ext_005_bs_accrual_high_flag_3y(assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """Binary: 1 if BS accrual ratio equals 3-year rolling maximum (worst-ever accrual quality)."""
    accrual = (assets - cashnequiv) - (liabilities - debt)
    avg_assets = _rolling_mean(assets, _TD_QTR)
    ratio = _safe_div(accrual, avg_assets)
    return (ratio >= _rolling_max(ratio, _TD_3Y)).astype(float)


def acq_ext_006_bs_accrual_above_threshold_streak(assets: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series, debt: pd.Series) -> pd.Series:
    """Consecutive days BS accrual ratio > 0.05 (sustained high-accrual streak)."""
    accrual = (assets - cashnequiv) - (liabilities - debt)
    avg_assets = _rolling_mean(assets, _TD_QTR)
    ratio = _safe_div(accrual, avg_assets)
    return _consec_true(ratio > 0.05)


def acq_ext_007_net_accrual_3y_sum(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """3-year rolling sum of (net income - operating cash flow) — cumulative cash-flow accrual."""
    return _rolling_sum(netinc - ncfo, _TD_3Y)


def acq_ext_008_net_accrual_5y_sum(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """5-year rolling sum of (net income - operating cash flow)."""
    return _rolling_sum(netinc - ncfo, _TD_5Y)


def acq_ext_009_cf_accrual_pct_rank_3y(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of CF-based accrual ratio (netinc - ncfo)/assets."""
    ratio = _safe_div(netinc - ncfo, assets.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_010_cf_accrual_ewm_slope(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of CF accrual ratio."""
    ratio = _safe_div(netinc - ncfo, assets.replace(0, np.nan))
    e = _ewm_mean(ratio, 63)
    return e - e.shift(_TD_QTR)


def acq_ext_011_cf_accrual_zscore_2y(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of CF accrual ratio."""
    ratio = _safe_div(netinc - ncfo, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_012_cf_accrual_skew_3y(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of CF accrual ratio."""
    ratio = _safe_div(netinc - ncfo, assets.replace(0, np.nan))
    return _rolling_skew(ratio, _TD_3Y)


# --- Group B (013-024): Receivables and revenue accrual variants ---

def acq_ext_013_receivables_to_revenue_zscore_2y(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of receivables-to-revenue ratio (high = aggressive revenue recognition)."""
    ratio = _safe_div(receivables, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_014_receivables_to_revenue_pct_rank_3y(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of receivables-to-revenue ratio."""
    ratio = _safe_div(receivables, revenue.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_015_receivables_yoy_pct(receivables: pd.Series) -> pd.Series:
    """Receivables YoY percent change (outpacing revenue growth = quality concern)."""
    prior = receivables.shift(_TD_YEAR)
    return _safe_div(receivables - prior, prior.replace(0, np.nan))


def acq_ext_016_receivables_growth_vs_revenue_growth(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY receivables growth minus YoY revenue growth (positive = receivables outpacing sales)."""
    rec_g = _safe_div(receivables - receivables.shift(_TD_YEAR), receivables.shift(_TD_YEAR).replace(0, np.nan))
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).replace(0, np.nan))
    return rec_g - rev_g


def acq_ext_017_receivables_to_revenue_ewm_slope(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of receivables-to-revenue ratio."""
    ratio = _safe_div(receivables, revenue.replace(0, np.nan))
    e = _ewm_mean(ratio, 63)
    return e - e.shift(_TD_QTR)


def acq_ext_018_receivables_to_assets_zscore_2y(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of receivables-to-assets ratio."""
    ratio = _safe_div(receivables, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_019_receivables_to_assets_pct_rank_3y(receivables: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of receivables-to-assets ratio."""
    ratio = _safe_div(receivables, assets.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_020_receivables_days_zscore_2y(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of days-sales-outstanding (receivables / daily_revenue)."""
    dso = _safe_div(receivables * 252, revenue.replace(0, np.nan))
    return _zscore_rolling(dso, _TD_2Y)


def acq_ext_021_ncfo_to_revenue_zscore_2y(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of operating cash flow-to-revenue ratio."""
    ratio = _safe_div(ncfo, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_022_ncfo_to_revenue_pct_rank_3y(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of operating cash flow-to-revenue ratio."""
    ratio = _safe_div(ncfo, revenue.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_023_ncfo_to_netinc_zscore_2y(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of operating cash flow divided by net income."""
    ratio = _safe_div(ncfo, netinc.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_024_ncfo_to_netinc_pct_rank_3y(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of ncfo / net income (low = weak cash conversion)."""
    ratio = _safe_div(ncfo, netinc.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


# --- Group C (025-036): Inventory and payables accrual variants ---

def acq_ext_025_inventory_to_revenue_zscore_2y(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of inventory-to-revenue ratio (high = overproduction/demand miss)."""
    ratio = _safe_div(inventory, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_026_inventory_to_revenue_pct_rank_3y(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of inventory-to-revenue ratio."""
    ratio = _safe_div(inventory, revenue.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_027_inventory_yoy_pct(inventory: pd.Series) -> pd.Series:
    """Inventory YoY percent change."""
    prior = inventory.shift(_TD_YEAR)
    return _safe_div(inventory - prior, prior.replace(0, np.nan))


def acq_ext_028_inventory_growth_vs_revenue_growth(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY inventory growth minus YoY revenue growth (positive = inventory bloat)."""
    inv_g = _safe_div(inventory - inventory.shift(_TD_YEAR), inventory.shift(_TD_YEAR).replace(0, np.nan))
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).replace(0, np.nan))
    return inv_g - rev_g


def acq_ext_029_payables_to_revenue_zscore_2y(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of payables-to-revenue ratio."""
    ratio = _safe_div(payables, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_030_payables_to_assets_zscore_2y(payables: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of payables-to-assets ratio."""
    ratio = _safe_div(payables, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_031_payables_days_zscore_2y(payables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of days-payable-outstanding (payables / daily revenue)."""
    dpo = _safe_div(payables * 252, revenue.replace(0, np.nan))
    return _zscore_rolling(dpo, _TD_2Y)


def acq_ext_032_working_capital_to_revenue_zscore_2y(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of working capital-to-revenue ratio."""
    ratio = _safe_div(workingcapital, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_033_working_capital_to_assets_zscore_2y(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of working capital-to-assets ratio."""
    ratio = _safe_div(workingcapital, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_034_working_capital_pct_rank_3y(workingcapital: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of working capital (low = liquidity stress)."""
    return _rolling_rank_pct(workingcapital, _TD_3Y)


def acq_ext_035_working_capital_ewm_slope(workingcapital: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) working capital — smoothed liquidity trend."""
    e = _ewm_mean(workingcapital, 63)
    return e - e.shift(_TD_QTR)


def acq_ext_036_working_capital_negative_streak(workingcapital: pd.Series) -> pd.Series:
    """Consecutive days working capital is negative."""
    return _consec_true(workingcapital < 0)


# --- Group D (037-048): Depamor and FCF accrual variants ---

def acq_ext_037_depamor_to_assets_zscore_2y(depamor: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of depreciation & amortization to assets ratio."""
    ratio = _safe_div(depamor, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_038_depamor_to_revenue_zscore_2y(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of D&A to revenue ratio."""
    ratio = _safe_div(depamor, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_039_depamor_to_revenue_pct_rank_3y(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of D&A to revenue ratio."""
    ratio = _safe_div(depamor, revenue.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_040_fcf_to_netinc_zscore_2y(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of FCF-to-net-income ratio (low = weak earnings quality)."""
    ratio = _safe_div(fcf, netinc.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_041_fcf_to_netinc_pct_rank_3y(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of FCF-to-net-income ratio."""
    ratio = _safe_div(fcf, netinc.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_042_fcf_to_revenue_zscore_2y(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of FCF-to-revenue ratio."""
    ratio = _safe_div(fcf, revenue.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_043_fcf_to_assets_zscore_2y(fcf: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of FCF-to-assets ratio."""
    ratio = _safe_div(fcf, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_044_fcf_negative_streak(fcf: pd.Series) -> pd.Series:
    """Consecutive days FCF is negative (cash burn streak)."""
    return _consec_true(fcf < 0)


def acq_ext_045_fcf_pct_rank_3y(fcf: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of FCF."""
    return _rolling_rank_pct(fcf, _TD_3Y)


def acq_ext_046_ncfo_negative_streak(ncfo: pd.Series) -> pd.Series:
    """Consecutive days operating cash flow is negative."""
    return _consec_true(ncfo < 0)


def acq_ext_047_ncfi_to_assets_zscore_2y(ncfi: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of investing cash flow to assets ratio."""
    ratio = _safe_div(ncfi, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_048_ncfo_minus_capex_to_revenue(ncfo: pd.Series, ncfi: pd.Series, revenue: pd.Series) -> pd.Series:
    """(ncfo - abs(ncfi)) / revenue — simplified FCF margin proxy using ncfi as capex proxy."""
    return _safe_div(ncfo + ncfi, revenue.replace(0, np.nan))


# --- Group E (049-060): Current-ratio and liquidity ratio variants ---

def acq_ext_049_current_ratio_zscore_2y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of current ratio (low z-score = acute liquidity stress)."""
    ratio = _safe_div(assetsc, liabilitiesc.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_050_current_ratio_pct_rank_3y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of current ratio."""
    ratio = _safe_div(assetsc, liabilitiesc.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_051_current_ratio_ewm_slope(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of current ratio."""
    ratio = _safe_div(assetsc, liabilitiesc.replace(0, np.nan))
    e = _ewm_mean(ratio, 63)
    return e - e.shift(_TD_QTR)


def acq_ext_052_quick_ratio_zscore_2y(assetsc: pd.Series, inventory: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of quick ratio ((current assets - inventory) / current liabilities)."""
    ratio = _safe_div(assetsc - inventory, liabilitiesc.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_053_cash_ratio_zscore_2y(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of cash ratio (cash / current liabilities)."""
    ratio = _safe_div(cashnequiv, liabilitiesc.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_054_cash_ratio_pct_rank_3y(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of cash ratio."""
    ratio = _safe_div(cashnequiv, liabilitiesc.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_055_cash_to_assets_zscore_2y(cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of cash-to-assets ratio."""
    ratio = _safe_div(cashnequiv, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_056_cash_burn_rate_3y(cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Runway: cash divided by abs(average quarterly operating burn) — months of cash."""
    avg_burn = _rolling_mean(ncfo.clip(upper=0).abs(), _TD_3Y)
    return _safe_div(cashnequiv, avg_burn.replace(0, np.nan))


def acq_ext_057_retearn_to_equity_zscore_2y(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of retained-earnings-to-equity ratio."""
    ratio = _safe_div(retearn, equity.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_058_liabilities_to_assetsc_zscore_2y(liabilitiesc: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of current liabilities-to-current assets ratio."""
    ratio = _safe_div(liabilitiesc, assetsc.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_059_debt_to_equity_zscore_2y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of total debt-to-equity ratio."""
    ratio = _safe_div(debt, equity.abs().replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_060_ncfo_ewm_slope_63(ncfo: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of operating cash flow — smoothed cash-flow trend."""
    e = _ewm_mean(ncfo, 63)
    return e - e.shift(_TD_QTR)


# --- Group F (061-075): Composite accrual quality scores ---

def acq_ext_061_composite_accrual_score(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Composite accrual quality score: average of 3 z-scores (2-year):
    CF accrual ratio, receivables-to-revenue, ncfo-to-revenue.
    High = poor accrual quality.
    """
    z1 = _zscore_rolling(_safe_div(netinc - ncfo, assets.replace(0, np.nan)), _TD_2Y)
    z2 = _zscore_rolling(_safe_div(receivables, revenue.replace(0, np.nan)), _TD_2Y)
    z3 = _zscore_rolling(_safe_div(ncfo, revenue.replace(0, np.nan)), _TD_2Y)
    return (z1 + z2 - z3) / 3.0


def acq_ext_062_accrual_quality_rank_3y(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of CF accrual ratio (high = worst accrual quality)."""
    ratio = _safe_div(netinc - ncfo, assets.replace(0, np.nan))
    return _rolling_rank_pct(ratio, _TD_3Y)


def acq_ext_063_ncfo_to_assets_zscore_2y(ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of operating cash flow-to-assets ratio."""
    ratio = _safe_div(ncfo, assets.replace(0, np.nan))
    return _zscore_rolling(ratio, _TD_2Y)


def acq_ext_064_ncfo_skew_3y(ncfo: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of operating cash flow."""
    return _rolling_skew(ncfo, _TD_3Y)


def acq_ext_065_fcf_skew_3y(fcf: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of free cash flow."""
    return _rolling_skew(fcf, _TD_3Y)


def acq_ext_066_netinc_skew_3y(netinc: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of net income."""
    return _rolling_skew(netinc, _TD_3Y)


def acq_ext_067_receivables_skew_3y(receivables: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of receivables."""
    return _rolling_skew(receivables, _TD_3Y)


def acq_ext_068_working_capital_skew_3y(workingcapital: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of working capital."""
    return _rolling_skew(workingcapital, _TD_3Y)


def acq_ext_069_accrual_reversal_flag(netinc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Binary: 1 when net income > ncfo this quarter but was < ncfo last quarter (accrual reversal)."""
    curr_pos = (netinc > ncfo).astype(float)
    prev_neg = (netinc.shift(_TD_QTR) <= ncfo.shift(_TD_QTR)).astype(float)
    return curr_pos * prev_neg


def acq_ext_070_ncfo_to_netinc_below_one_streak(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """Consecutive days ncfo < netinc (cash earnings below reported earnings — accrual buildup)."""
    return _consec_true(ncfo < netinc)


def acq_ext_071_receivables_to_revenue_high_streak(receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """Consecutive days receivables-to-revenue above its 1-year rolling median."""
    ratio = _safe_div(receivables, revenue.replace(0, np.nan))
    med = _rolling_median(ratio, _TD_YEAR)
    return _consec_true(ratio > med)


def acq_ext_072_inventory_to_revenue_high_streak(inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """Consecutive days inventory-to-revenue above its 1-year rolling median."""
    ratio = _safe_div(inventory, revenue.replace(0, np.nan))
    med = _rolling_median(ratio, _TD_YEAR)
    return _consec_true(ratio > med)


def acq_ext_073_fcf_to_netinc_below_one_streak(fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    """Consecutive days FCF < net income (accrual persists, not converting to cash)."""
    return _consec_true(fcf < netinc)


def acq_ext_074_accrual_composite_pct_rank_5y(netinc: pd.Series, ncfo: pd.Series, assets: pd.Series, receivables: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    5-year percentile rank of composite accrual z-score (061):
    CF accrual ratio z-score + receivables-to-revenue z-score - ncfo-to-revenue z-score.
    """
    z1 = _zscore_rolling(_safe_div(netinc - ncfo, assets.replace(0, np.nan)), _TD_2Y)
    z2 = _zscore_rolling(_safe_div(receivables, revenue.replace(0, np.nan)), _TD_2Y)
    z3 = _zscore_rolling(_safe_div(ncfo, revenue.replace(0, np.nan)), _TD_2Y)
    composite = (z1 + z2 - z3) / 3.0
    return _rolling_rank_pct(composite, _TD_5Y)


def acq_ext_075_ncfo_3y_sum_to_netinc_3y_sum(ncfo: pd.Series, netinc: pd.Series) -> pd.Series:
    """3-year cumulative ncfo divided by 3-year cumulative net income — long-run cash quality."""
    ncfo_sum = _rolling_sum(ncfo, _TD_3Y)
    netinc_sum = _rolling_sum(netinc, _TD_3Y)
    return _safe_div(ncfo_sum, netinc_sum.replace(0, np.nan))


# ── Registry ──────────────────────────────────────────────────────────────────

ACCRUALS_QUALITY_EXTENDED_REGISTRY_001_075 = {
    "acq_ext_001_bs_accrual_3y_zscore": {
        "inputs": ["assets", "cashnequiv", "liabilities", "debt"],
        "func": acq_ext_001_bs_accrual_3y_zscore,
    },
    "acq_ext_002_bs_accrual_pct_rank_3y": {
        "inputs": ["assets", "cashnequiv", "liabilities", "debt"],
        "func": acq_ext_002_bs_accrual_pct_rank_3y,
    },
    "acq_ext_003_bs_accrual_ewm_slope": {
        "inputs": ["assets", "cashnequiv", "liabilities", "debt"],
        "func": acq_ext_003_bs_accrual_ewm_slope,
    },
    "acq_ext_004_bs_accrual_skew_3y": {
        "inputs": ["assets", "cashnequiv", "liabilities", "debt"],
        "func": acq_ext_004_bs_accrual_skew_3y,
    },
    "acq_ext_005_bs_accrual_high_flag_3y": {
        "inputs": ["assets", "cashnequiv", "liabilities", "debt"],
        "func": acq_ext_005_bs_accrual_high_flag_3y,
    },
    "acq_ext_006_bs_accrual_above_threshold_streak": {
        "inputs": ["assets", "cashnequiv", "liabilities", "debt"],
        "func": acq_ext_006_bs_accrual_above_threshold_streak,
    },
    "acq_ext_007_net_accrual_3y_sum": {
        "inputs": ["netinc", "ncfo"],
        "func": acq_ext_007_net_accrual_3y_sum,
    },
    "acq_ext_008_net_accrual_5y_sum": {
        "inputs": ["netinc", "ncfo"],
        "func": acq_ext_008_net_accrual_5y_sum,
    },
    "acq_ext_009_cf_accrual_pct_rank_3y": {
        "inputs": ["netinc", "ncfo", "assets"],
        "func": acq_ext_009_cf_accrual_pct_rank_3y,
    },
    "acq_ext_010_cf_accrual_ewm_slope": {
        "inputs": ["netinc", "ncfo", "assets"],
        "func": acq_ext_010_cf_accrual_ewm_slope,
    },
    "acq_ext_011_cf_accrual_zscore_2y": {
        "inputs": ["netinc", "ncfo", "assets"],
        "func": acq_ext_011_cf_accrual_zscore_2y,
    },
    "acq_ext_012_cf_accrual_skew_3y": {
        "inputs": ["netinc", "ncfo", "assets"],
        "func": acq_ext_012_cf_accrual_skew_3y,
    },
    "acq_ext_013_receivables_to_revenue_zscore_2y": {
        "inputs": ["receivables", "revenue"],
        "func": acq_ext_013_receivables_to_revenue_zscore_2y,
    },
    "acq_ext_014_receivables_to_revenue_pct_rank_3y": {
        "inputs": ["receivables", "revenue"],
        "func": acq_ext_014_receivables_to_revenue_pct_rank_3y,
    },
    "acq_ext_015_receivables_yoy_pct": {
        "inputs": ["receivables"],
        "func": acq_ext_015_receivables_yoy_pct,
    },
    "acq_ext_016_receivables_growth_vs_revenue_growth": {
        "inputs": ["receivables", "revenue"],
        "func": acq_ext_016_receivables_growth_vs_revenue_growth,
    },
    "acq_ext_017_receivables_to_revenue_ewm_slope": {
        "inputs": ["receivables", "revenue"],
        "func": acq_ext_017_receivables_to_revenue_ewm_slope,
    },
    "acq_ext_018_receivables_to_assets_zscore_2y": {
        "inputs": ["receivables", "assets"],
        "func": acq_ext_018_receivables_to_assets_zscore_2y,
    },
    "acq_ext_019_receivables_to_assets_pct_rank_3y": {
        "inputs": ["receivables", "assets"],
        "func": acq_ext_019_receivables_to_assets_pct_rank_3y,
    },
    "acq_ext_020_receivables_days_zscore_2y": {
        "inputs": ["receivables", "revenue"],
        "func": acq_ext_020_receivables_days_zscore_2y,
    },
    "acq_ext_021_ncfo_to_revenue_zscore_2y": {
        "inputs": ["ncfo", "revenue"],
        "func": acq_ext_021_ncfo_to_revenue_zscore_2y,
    },
    "acq_ext_022_ncfo_to_revenue_pct_rank_3y": {
        "inputs": ["ncfo", "revenue"],
        "func": acq_ext_022_ncfo_to_revenue_pct_rank_3y,
    },
    "acq_ext_023_ncfo_to_netinc_zscore_2y": {
        "inputs": ["ncfo", "netinc"],
        "func": acq_ext_023_ncfo_to_netinc_zscore_2y,
    },
    "acq_ext_024_ncfo_to_netinc_pct_rank_3y": {
        "inputs": ["ncfo", "netinc"],
        "func": acq_ext_024_ncfo_to_netinc_pct_rank_3y,
    },
    "acq_ext_025_inventory_to_revenue_zscore_2y": {
        "inputs": ["inventory", "revenue"],
        "func": acq_ext_025_inventory_to_revenue_zscore_2y,
    },
    "acq_ext_026_inventory_to_revenue_pct_rank_3y": {
        "inputs": ["inventory", "revenue"],
        "func": acq_ext_026_inventory_to_revenue_pct_rank_3y,
    },
    "acq_ext_027_inventory_yoy_pct": {
        "inputs": ["inventory"],
        "func": acq_ext_027_inventory_yoy_pct,
    },
    "acq_ext_028_inventory_growth_vs_revenue_growth": {
        "inputs": ["inventory", "revenue"],
        "func": acq_ext_028_inventory_growth_vs_revenue_growth,
    },
    "acq_ext_029_payables_to_revenue_zscore_2y": {
        "inputs": ["payables", "revenue"],
        "func": acq_ext_029_payables_to_revenue_zscore_2y,
    },
    "acq_ext_030_payables_to_assets_zscore_2y": {
        "inputs": ["payables", "assets"],
        "func": acq_ext_030_payables_to_assets_zscore_2y,
    },
    "acq_ext_031_payables_days_zscore_2y": {
        "inputs": ["payables", "revenue"],
        "func": acq_ext_031_payables_days_zscore_2y,
    },
    "acq_ext_032_working_capital_to_revenue_zscore_2y": {
        "inputs": ["workingcapital", "revenue"],
        "func": acq_ext_032_working_capital_to_revenue_zscore_2y,
    },
    "acq_ext_033_working_capital_to_assets_zscore_2y": {
        "inputs": ["workingcapital", "assets"],
        "func": acq_ext_033_working_capital_to_assets_zscore_2y,
    },
    "acq_ext_034_working_capital_pct_rank_3y": {
        "inputs": ["workingcapital"],
        "func": acq_ext_034_working_capital_pct_rank_3y,
    },
    "acq_ext_035_working_capital_ewm_slope": {
        "inputs": ["workingcapital"],
        "func": acq_ext_035_working_capital_ewm_slope,
    },
    "acq_ext_036_working_capital_negative_streak": {
        "inputs": ["workingcapital"],
        "func": acq_ext_036_working_capital_negative_streak,
    },
    "acq_ext_037_depamor_to_assets_zscore_2y": {
        "inputs": ["depamor", "assets"],
        "func": acq_ext_037_depamor_to_assets_zscore_2y,
    },
    "acq_ext_038_depamor_to_revenue_zscore_2y": {
        "inputs": ["depamor", "revenue"],
        "func": acq_ext_038_depamor_to_revenue_zscore_2y,
    },
    "acq_ext_039_depamor_to_revenue_pct_rank_3y": {
        "inputs": ["depamor", "revenue"],
        "func": acq_ext_039_depamor_to_revenue_pct_rank_3y,
    },
    "acq_ext_040_fcf_to_netinc_zscore_2y": {
        "inputs": ["fcf", "netinc"],
        "func": acq_ext_040_fcf_to_netinc_zscore_2y,
    },
    "acq_ext_041_fcf_to_netinc_pct_rank_3y": {
        "inputs": ["fcf", "netinc"],
        "func": acq_ext_041_fcf_to_netinc_pct_rank_3y,
    },
    "acq_ext_042_fcf_to_revenue_zscore_2y": {
        "inputs": ["fcf", "revenue"],
        "func": acq_ext_042_fcf_to_revenue_zscore_2y,
    },
    "acq_ext_043_fcf_to_assets_zscore_2y": {
        "inputs": ["fcf", "assets"],
        "func": acq_ext_043_fcf_to_assets_zscore_2y,
    },
    "acq_ext_044_fcf_negative_streak": {
        "inputs": ["fcf"],
        "func": acq_ext_044_fcf_negative_streak,
    },
    "acq_ext_045_fcf_pct_rank_3y": {
        "inputs": ["fcf"],
        "func": acq_ext_045_fcf_pct_rank_3y,
    },
    "acq_ext_046_ncfo_negative_streak": {
        "inputs": ["ncfo"],
        "func": acq_ext_046_ncfo_negative_streak,
    },
    "acq_ext_047_ncfi_to_assets_zscore_2y": {
        "inputs": ["ncfi", "assets"],
        "func": acq_ext_047_ncfi_to_assets_zscore_2y,
    },
    "acq_ext_048_ncfo_minus_capex_to_revenue": {
        "inputs": ["ncfo", "ncfi", "revenue"],
        "func": acq_ext_048_ncfo_minus_capex_to_revenue,
    },
    "acq_ext_049_current_ratio_zscore_2y": {
        "inputs": ["assetsc", "liabilitiesc"],
        "func": acq_ext_049_current_ratio_zscore_2y,
    },
    "acq_ext_050_current_ratio_pct_rank_3y": {
        "inputs": ["assetsc", "liabilitiesc"],
        "func": acq_ext_050_current_ratio_pct_rank_3y,
    },
    "acq_ext_051_current_ratio_ewm_slope": {
        "inputs": ["assetsc", "liabilitiesc"],
        "func": acq_ext_051_current_ratio_ewm_slope,
    },
    "acq_ext_052_quick_ratio_zscore_2y": {
        "inputs": ["assetsc", "inventory", "liabilitiesc"],
        "func": acq_ext_052_quick_ratio_zscore_2y,
    },
    "acq_ext_053_cash_ratio_zscore_2y": {
        "inputs": ["cashnequiv", "liabilitiesc"],
        "func": acq_ext_053_cash_ratio_zscore_2y,
    },
    "acq_ext_054_cash_ratio_pct_rank_3y": {
        "inputs": ["cashnequiv", "liabilitiesc"],
        "func": acq_ext_054_cash_ratio_pct_rank_3y,
    },
    "acq_ext_055_cash_to_assets_zscore_2y": {
        "inputs": ["cashnequiv", "assets"],
        "func": acq_ext_055_cash_to_assets_zscore_2y,
    },
    "acq_ext_056_cash_burn_rate_3y": {
        "inputs": ["cashnequiv", "ncfo"],
        "func": acq_ext_056_cash_burn_rate_3y,
    },
    "acq_ext_057_retearn_to_equity_zscore_2y": {
        "inputs": ["retearn", "equity"],
        "func": acq_ext_057_retearn_to_equity_zscore_2y,
    },
    "acq_ext_058_liabilities_to_assetsc_zscore_2y": {
        "inputs": ["liabilitiesc", "assetsc"],
        "func": acq_ext_058_liabilities_to_assetsc_zscore_2y,
    },
    "acq_ext_059_debt_to_equity_zscore_2y": {
        "inputs": ["debt", "equity"],
        "func": acq_ext_059_debt_to_equity_zscore_2y,
    },
    "acq_ext_060_ncfo_ewm_slope_63": {
        "inputs": ["ncfo"],
        "func": acq_ext_060_ncfo_ewm_slope_63,
    },
    "acq_ext_061_composite_accrual_score": {
        "inputs": ["netinc", "ncfo", "assets", "receivables", "revenue"],
        "func": acq_ext_061_composite_accrual_score,
    },
    "acq_ext_062_accrual_quality_rank_3y": {
        "inputs": ["netinc", "ncfo", "assets"],
        "func": acq_ext_062_accrual_quality_rank_3y,
    },
    "acq_ext_063_ncfo_to_assets_zscore_2y": {
        "inputs": ["ncfo", "assets"],
        "func": acq_ext_063_ncfo_to_assets_zscore_2y,
    },
    "acq_ext_064_ncfo_skew_3y": {
        "inputs": ["ncfo"],
        "func": acq_ext_064_ncfo_skew_3y,
    },
    "acq_ext_065_fcf_skew_3y": {
        "inputs": ["fcf"],
        "func": acq_ext_065_fcf_skew_3y,
    },
    "acq_ext_066_netinc_skew_3y": {
        "inputs": ["netinc"],
        "func": acq_ext_066_netinc_skew_3y,
    },
    "acq_ext_067_receivables_skew_3y": {
        "inputs": ["receivables"],
        "func": acq_ext_067_receivables_skew_3y,
    },
    "acq_ext_068_working_capital_skew_3y": {
        "inputs": ["workingcapital"],
        "func": acq_ext_068_working_capital_skew_3y,
    },
    "acq_ext_069_accrual_reversal_flag": {
        "inputs": ["netinc", "ncfo"],
        "func": acq_ext_069_accrual_reversal_flag,
    },
    "acq_ext_070_ncfo_to_netinc_below_one_streak": {
        "inputs": ["ncfo", "netinc"],
        "func": acq_ext_070_ncfo_to_netinc_below_one_streak,
    },
    "acq_ext_071_receivables_to_revenue_high_streak": {
        "inputs": ["receivables", "revenue"],
        "func": acq_ext_071_receivables_to_revenue_high_streak,
    },
    "acq_ext_072_inventory_to_revenue_high_streak": {
        "inputs": ["inventory", "revenue"],
        "func": acq_ext_072_inventory_to_revenue_high_streak,
    },
    "acq_ext_073_fcf_to_netinc_below_one_streak": {
        "inputs": ["fcf", "netinc"],
        "func": acq_ext_073_fcf_to_netinc_below_one_streak,
    },
    "acq_ext_074_accrual_composite_pct_rank_5y": {
        "inputs": ["netinc", "ncfo", "assets", "receivables", "revenue"],
        "func": acq_ext_074_accrual_composite_pct_rank_5y,
    },
    "acq_ext_075_ncfo_3y_sum_to_netinc_3y_sum": {
        "inputs": ["ncfo", "netinc"],
        "func": acq_ext_075_ncfo_3y_sum_to_netinc_3y_sum,
    },
}
