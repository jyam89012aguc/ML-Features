"""
72_solvency_scores — Extended Features 001-075
Domain: composite distress / solvency scores — additional variants: alternate
        coefficient weightings, new ratio combos, distress-depth and severity
        measures, zone-streak/time-since features, rolling stability and trend
        diagnostics of the distress scores not covered by the base files.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

These features are NET-NEW relative to base_001_075, base_076_150,
2nd_derivatives and 3rd_derivatives — they explore different angles
(severity depths, ratio z-scores, streaks, percentile ranks, composites)
rather than duplicating the assembled-score and component features.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  Functions look strictly backward using
.shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252   # 1 year in trading days
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_TD_QTR  = 63    # 1 quarter in trading days
_TD_2Q   = 126
_TD_3Q   = 189
_EPS     = 1e-9

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
    """Element-wise division; replaces zero denominators with NaN."""
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
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _streak_true(cond: pd.Series) -> pd.Series:
    """Consecutive-True streak length up to each row (backward-looking)."""
    arr = cond.astype(int).values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) * arr[i]
    if len(arr) > 0:
        out[0] = float(arr[0])
    return pd.Series(out, index=cond.index)


def _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities):
    """Altman Z'' (book-equity variant) assembled score."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return 6.56 * x1 + 3.26 * x2 + 6.72 * x3 + 1.05 * x4


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Distress-depth / severity below thresholds ---

def slv_ext_001_altman_z_depth_below_1p1(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Depth of Altman Z'' below the 1.1 distress threshold (0 when above)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return (1.1 - z).clip(lower=0.0)


def slv_ext_002_altman_z_depth_below_0(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Depth of Altman Z'' below zero (severe-distress magnitude)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return (0.0 - z).clip(lower=0.0)


def slv_ext_003_altman_z_distance_to_safe(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Distance of Altman Z'' below the 2.6 safe-zone boundary (0 when in safe zone)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return (2.6 - z).clip(lower=0.0)


def slv_ext_004_altman_z_severe_distress_flag(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Binary flag: Altman Z'' below 0 (severe distress, well past 1.1 threshold)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return (z < 0.0).astype(float)


def slv_ext_005_leverage_excess_over_1(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Excess of liabilities/assets above 1.0 (insolvency-depth magnitude)."""
    return (_safe_div(liabilities, assets) - 1.0).clip(lower=0.0)


def slv_ext_006_current_ratio_shortfall_below_1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Shortfall of current ratio below 1.0 (short-term liquidity gap depth)."""
    return (1.0 - _safe_div(assetsc, liabilitiesc)).clip(lower=0.0)


def slv_ext_007_interest_coverage_shortfall(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Shortfall of interest coverage below 1.0 (depth of inability to cover interest)."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return (1.0 - cov).clip(lower=0.0)


def slv_ext_008_equity_to_assets_shortfall_below_0p2(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Shortfall of equity/assets below the 0.2 capital-cushion floor."""
    return (0.2 - _safe_div(equity, assets)).clip(lower=0.0)


def slv_ext_009_negative_equity_depth(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Magnitude of negative book equity scaled by assets (insolvency depth)."""
    return _safe_div_abs((-equity).clip(lower=0.0), assets)


def slv_ext_010_debt_to_ebitda_excess_over_4(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Excess of debt/EBITDA above the 4x high-leverage threshold."""
    de = _safe_div(debt, ebitda.abs().replace(0, np.nan))
    return (de - 4.0).clip(lower=0.0)


def slv_ext_011_cash_coverage_shortfall_below_0p1(cashnequiv: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Shortfall of cash/liabilities below the 0.1 minimum-liquidity floor."""
    return (0.1 - _safe_div(cashnequiv, liabilities)).clip(lower=0.0)


def slv_ext_012_altman_z_distress_severity_norm(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Normalized distress severity: depth of Z'' below 1.1 divided by 1.1."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return (1.1 - z).clip(lower=0.0) / 1.1


# --- Group B (013-024): Alternate-weighting and alternate-ratio distress scores ---

def slv_ext_013_altman_z_original_coeffs(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Altman Z' (1983 private-firm) coefficients with book equity: 0.717,0.847,3.107,0.420,0.998."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return 0.717 * x1 + 0.847 * x2 + 3.107 * x3 + 0.420 * x4


def slv_ext_014_altman_z_equal_weight(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Equal-weighted distress score: simple sum of the four Altman Z'' ratios."""
    x1 = _safe_div(workingcapital, assets)
    x2 = _safe_div(retearn, assets)
    x3 = _safe_div(ebit, assets)
    x4 = _safe_div(equity, liabilities)
    return x1 + x2 + x3 + x4


def slv_ext_015_profitability_weighted_score(
    retearn: pd.Series, assets: pd.Series, ebit: pd.Series, netinc: pd.Series,
) -> pd.Series:
    """Profitability-weighted distress score: 3*ebit/assets + 2*retearn/assets + netinc/assets."""
    return (3.0 * _safe_div(ebit, assets)
            + 2.0 * _safe_div(retearn, assets)
            + _safe_div(netinc, assets))


def slv_ext_016_liquidity_weighted_score(
    workingcapital: pd.Series, assets: pd.Series, assetsc: pd.Series,
    liabilitiesc: pd.Series, cashnequiv: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Liquidity-weighted distress score: wc/assets + current ratio + cash/liabilities."""
    return (_safe_div(workingcapital, assets)
            + _safe_div(assetsc, liabilitiesc)
            + _safe_div(cashnequiv, liabilities))


def slv_ext_017_cashflow_solvency_score(
    ncfo: pd.Series, debt: pd.Series, liabilitiesc: pd.Series, assets: pd.Series,
) -> pd.Series:
    """Cash-flow solvency score: ncfo/debt + ncfo/currentliab + ncfo/assets."""
    return (_safe_div(ncfo, debt.abs().replace(0, np.nan))
            + _safe_div(ncfo, liabilitiesc.abs().replace(0, np.nan))
            + _safe_div(ncfo, assets))


def slv_ext_018_zmijewski_no_liquidity(netinc: pd.Series, assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Zmijewski-style score dropping the liquidity term: -4.3 - 4.5*ROA + 5.7*leverage."""
    roa = _safe_div(netinc, assets)
    lev = _safe_div(liabilities, assets)
    return -4.3 - 4.5 * roa + 5.7 * lev


def slv_ext_019_springate_revenue_heavy(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series,
    ebt: pd.Series, liabilitiesc: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Revenue-emphasised Springate variant: 1.03*A + 3.07*B + 0.66*C + 1.0*D."""
    a = _safe_div(workingcapital, assets)
    b = _safe_div(ebit, assets)
    c = _safe_div(ebt, liabilitiesc)
    d = _safe_div(revenue, assets)
    return 1.03 * a + 3.07 * b + 0.66 * c + 1.0 * d


def slv_ext_020_contingent_claims_proxy(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Distance-to-default proxy: log(equity/liabilities) — solvency cushion in log space."""
    ratio = _safe_div(equity, liabilities)
    return np.log(ratio.where(ratio > 0, np.nan))


def slv_ext_021_ohlson_style_score(
    assets: pd.Series, liabilities: pd.Series, workingcapital: pd.Series,
    netinc: pd.Series, liabilitiesc: pd.Series, assetsc: pd.Series,
) -> pd.Series:
    """Ohlson-style O-score approximation using available SF1 fields."""
    size = np.log(assets.abs().replace(0, np.nan))
    tlta = _safe_div(liabilities, assets)
    wcta = _safe_div(workingcapital, assets)
    clca = _safe_div(liabilitiesc, assetsc)
    ni_ta = _safe_div(netinc, assets)
    return -1.32 - 0.407 * size + 6.03 * tlta - 1.43 * wcta + 0.0757 * clca - 2.37 * ni_ta


def slv_ext_022_grover_style_score(
    workingcapital: pd.Series, assets: pd.Series, ebit: pd.Series, netinc: pd.Series,
) -> pd.Series:
    """Grover-style distress score: 1.650*X1 + 3.404*X3 + 0.016*ROA + 0.057."""
    x1 = _safe_div(workingcapital, assets)
    x3 = _safe_div(ebit, assets)
    roa = _safe_div(netinc, assets)
    return 1.650 * x1 + 3.404 * x3 + 0.016 * roa + 0.057


def slv_ext_023_fulmer_style_partial(
    retearn: pd.Series, assets: pd.Series, ebit: pd.Series,
    equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Fulmer-style partial H-factor: retearn/assets + ebit/equity + equity/liabilities."""
    return (_safe_div(retearn, assets)
            + _safe_div_abs(ebit, equity)
            + _safe_div(equity, liabilities))


def slv_ext_024_taffler_style_score(
    ebt: pd.Series, liabilitiesc: pd.Series, assetsc: pd.Series,
    liabilities: pd.Series, assets: pd.Series,
) -> pd.Series:
    """Taffler-style UK distress score: 3.20 + 12.18*ebt/cl + 2.50*ca/tl - 10.68*cl/ta."""
    pbt_cl = _safe_div(ebt, liabilitiesc)
    ca_tl = _safe_div(assetsc, liabilities)
    cl_ta = _safe_div(liabilitiesc, assets)
    return 3.20 + 12.18 * pbt_cl + 2.50 * ca_tl - 10.68 * cl_ta


# --- Group C (025-036): New solvency ratios not in base files ---

def slv_ext_025_long_term_debt_to_equity(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Total debt / book equity (leverage ratio); uses debt as LT-debt proxy."""
    return _safe_div_abs(debt, equity)


def slv_ext_026_long_term_debt_to_assets(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Total debt / total assets (capital structure ratio)."""
    return _safe_div(debt, assets)


def slv_ext_027_short_term_debt_share(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Current debt as a share of total debt (refinancing-pressure ratio)."""
    return _safe_div(debtc, debt)


def slv_ext_028_net_debt_to_assets(debt: pd.Series, cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Net debt (debt minus cash) / total assets."""
    return _safe_div(debt - cashnequiv, assets)


def slv_ext_029_net_debt_to_ebitda(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net debt / EBITDA — leverage net of cash holdings."""
    return _safe_div(debt - cashnequiv, ebitda.abs().replace(0, np.nan))


def slv_ext_030_equity_multiplier(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Equity multiplier: assets / equity (financial leverage factor)."""
    return _safe_div_abs(assets, equity)


def slv_ext_031_cash_to_current_liabilities(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash ratio: cash & equivalents / current liabilities (strictest liquidity test)."""
    return _safe_div(cashnequiv, liabilitiesc)


def slv_ext_032_working_capital_to_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """Working capital / revenue — liquidity buffer relative to operating scale."""
    return _safe_div(workingcapital, revenue)


def slv_ext_033_retearn_to_equity(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Retained earnings / book equity — share of equity from accumulated profit."""
    return _safe_div_abs(retearn, equity)


def slv_ext_034_ebitda_to_interest(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """EBITDA / interest expense — cash-based interest coverage ratio."""
    return _safe_div(ebitda, intexp.abs().replace(0, np.nan))


def slv_ext_035_debt_service_coverage(ncfo: pd.Series, intexp: pd.Series, debtc: pd.Series) -> pd.Series:
    """Debt-service coverage proxy: ncfo / (interest + current debt)."""
    service = intexp.abs() + debtc.abs()
    return _safe_div(ncfo, service.replace(0, np.nan))


def slv_ext_036_defensive_interval_proxy(assetsc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Defensive-interval proxy: current assets relative to quarterly revenue (burn cover)."""
    return _safe_div(assetsc, revenue)


# --- Group D (037-048): Distress-zone streaks and time-since features ---

def slv_ext_037_consec_days_negative_equity(equity: pd.Series) -> pd.Series:
    """Consecutive daily steps book equity has been negative."""
    return _streak_true(equity < 0.0)


def slv_ext_038_consec_days_current_ratio_below_1(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Consecutive daily steps current ratio has been below 1.0."""
    return _streak_true(_safe_div(assetsc, liabilitiesc) < 1.0)


def slv_ext_039_consec_days_negative_netinc(netinc: pd.Series) -> pd.Series:
    """Consecutive daily steps net income has been negative."""
    return _streak_true(netinc < 0.0)


def slv_ext_040_consec_days_negative_ncfo(ncfo: pd.Series) -> pd.Series:
    """Consecutive daily steps operating cash flow has been negative."""
    return _streak_true(ncfo < 0.0)


def slv_ext_041_consec_days_altman_severe(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Consecutive daily steps Altman Z'' has been below 0 (severe distress)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _streak_true(z < 0.0)


def slv_ext_042_consec_days_interest_uncovered(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Consecutive daily steps interest coverage (ebit/intexp) has been below 1.0."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return _streak_true(cov < 1.0)


def slv_ext_043_time_since_altman_safe(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Days elapsed since Altman Z'' was last at/above the 2.6 safe-zone boundary."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    safe = (z >= 2.6).astype(float)
    idx = pd.Series(np.arange(len(z), dtype=float), index=z.index)
    last = idx.where(safe == 1.0).ffill().fillna(0.0)
    return (idx - last).where(~z.isna(), np.nan)


def slv_ext_044_time_since_positive_equity(equity: pd.Series) -> pd.Series:
    """Days elapsed since book equity was last positive."""
    pos = (equity > 0.0).astype(float)
    idx = pd.Series(np.arange(len(equity), dtype=float), index=equity.index)
    last = idx.where(pos == 1.0).ffill().fillna(0.0)
    return (idx - last).where(~equity.isna(), np.nan)


def slv_ext_045_distress_quarter_count_3y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Count of days in trailing 3 years with Altman Z'' in the distress zone (< 1.1)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_sum((z < 1.1).astype(float), _TD_3Y)


def slv_ext_046_negative_netinc_quarter_count_3y(netinc: pd.Series) -> pd.Series:
    """Count of days in trailing 3 years with negative net income."""
    return _rolling_sum((netinc < 0.0).astype(float), _TD_3Y)


def slv_ext_047_current_ratio_below_1_count_2y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Count of days in trailing 2 years with current ratio below 1.0."""
    return _rolling_sum((_safe_div(assetsc, liabilitiesc) < 1.0).astype(float), _TD_2Y)


def slv_ext_048_altman_below_safe_fraction_2y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Fraction of trailing 2 years Altman Z'' spent below the 2.6 safe boundary."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_mean((z < 2.6).astype(float), _TD_2Y)


# --- Group E (049-060): Rolling z-score / percentile-rank of solvency ratios ---

def slv_ext_049_leverage_zscore_2y(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of liabilities/assets within a trailing 2-year window."""
    return _zscore_rolling(_safe_div(liabilities, assets), _TD_2Y)


def slv_ext_050_current_ratio_zscore_2y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Z-score of the current ratio within a trailing 2-year window."""
    return _zscore_rolling(_safe_div(assetsc, liabilitiesc), _TD_2Y)


def slv_ext_051_interest_coverage_zscore_2y(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of interest coverage within a trailing 2-year window."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return _zscore_rolling(cov, _TD_2Y)


def slv_ext_052_equity_to_assets_zscore_3y(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of equity/assets within a trailing 3-year window."""
    return _zscore_rolling(_safe_div(equity, assets), _TD_3Y)


def slv_ext_053_debt_to_ebitda_zscore_2y(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of debt/EBITDA within a trailing 2-year window."""
    de = _safe_div(debt, ebitda.abs().replace(0, np.nan))
    return _zscore_rolling(de, _TD_2Y)


def slv_ext_054_leverage_pct_rank_3y(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of liabilities/assets within a trailing 3-year window."""
    return _rolling_rank_pct(_safe_div(liabilities, assets), _TD_3Y)


def slv_ext_055_current_ratio_pct_rank_3y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Percentile rank of the current ratio within a trailing 3-year window."""
    return _rolling_rank_pct(_safe_div(assetsc, liabilitiesc), _TD_3Y)


def slv_ext_056_altman_z_pct_rank_3y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Percentile rank of Altman Z'' within a trailing 3-year window."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_rank_pct(z, _TD_3Y)


def slv_ext_057_altman_z_zscore_3y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Z-score of Altman Z'' within a trailing 3-year window."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _zscore_rolling(z, _TD_3Y)


def slv_ext_058_interest_coverage_pct_rank_2y(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Percentile rank of interest coverage within a trailing 2-year window."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return _rolling_rank_pct(cov, _TD_2Y)


def slv_ext_059_cash_to_liabilities_pct_rank_3y(cashnequiv: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Percentile rank of cash/liabilities within a trailing 3-year window."""
    return _rolling_rank_pct(_safe_div(cashnequiv, liabilities), _TD_3Y)


def slv_ext_060_altman_z_expanding_zscore(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Expanding all-history z-score of Altman Z''."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    m = z.expanding(min_periods=2).mean()
    s = z.expanding(min_periods=2).std()
    return _safe_div(z - m, s)


# --- Group F (061-068): Distress-score drawdown and trend diagnostics ---

def slv_ext_061_altman_z_drawdown_2y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Altman Z'' drawdown from its trailing 2-year peak."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z - _rolling_max(z, _TD_2Y)


def slv_ext_062_altman_z_drawdown_pct_2y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Altman Z'' drawdown from 2-year peak as a fraction of that peak."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    peak = _rolling_max(z, _TD_2Y)
    return _safe_div_abs(z - peak, peak)


def slv_ext_063_current_ratio_drawdown_2y(assetsc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current ratio drawdown from its trailing 2-year peak."""
    cr = _safe_div(assetsc, liabilitiesc)
    return cr - _rolling_max(cr, _TD_2Y)


def slv_ext_064_equity_to_assets_drawdown_3y(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Equity/assets drawdown from its trailing 3-year peak."""
    ea = _safe_div(equity, assets)
    return ea - _rolling_max(ea, _TD_3Y)


def slv_ext_065_altman_z_2y_change(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Two-year (504-day) change in the Altman Z'' score."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return z - z.shift(_TD_2Y)


def slv_ext_066_leverage_yoy_change(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY (252-day) change in liabilities/assets leverage ratio."""
    lev = _safe_div(liabilities, assets)
    return lev - lev.shift(_TD_YEAR)


def slv_ext_067_interest_coverage_yoy_change(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """YoY (252-day) change in interest coverage."""
    cov = _safe_div(ebit, intexp.abs().replace(0, np.nan))
    return cov - cov.shift(_TD_YEAR)


def slv_ext_068_altman_z_rolling_std_2y(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Rolling 2-year std of the Altman Z'' score (distress-score instability)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    return _rolling_std(z, _TD_2Y)


# --- Group G (069-075): Multi-model confluence and capitulation composites ---

def slv_ext_069_low_liquidity_low_profit_flag(
    assetsc: pd.Series, liabilitiesc: pd.Series, netinc: pd.Series,
) -> pd.Series:
    """Binary flag: current ratio below 1.0 AND net income negative (twin distress)."""
    cr_low = (_safe_div(assetsc, liabilitiesc) < 1.0)
    ni_neg = (netinc < 0.0)
    return (cr_low & ni_neg).astype(float)


def slv_ext_070_high_leverage_negative_cf_flag(
    liabilities: pd.Series, assets: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """Binary flag: leverage above 0.8 AND operating cash flow negative."""
    lev_high = (_safe_div(liabilities, assets) > 0.8)
    cf_neg = (ncfo < 0.0)
    return (lev_high & cf_neg).astype(float)


def slv_ext_071_triple_distress_count(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """Count (0-3) of distress conditions: Z'' < 1.1, negative netinc, current ratio < 1."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    f1 = (z < 1.1).astype(float)
    f2 = (netinc < 0.0).astype(float)
    f3 = (_safe_div(assetsc, liabilitiesc) < 1.0).astype(float)
    return f1 + f2 + f3


def slv_ext_072_solvency_health_zscore_index(
    equity: pd.Series, assets: pd.Series, assetsc: pd.Series,
    liabilitiesc: pd.Series, ebit: pd.Series, intexp: pd.Series,
    ncfo: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Composite solvency-health index: mean 2-year z-score of four solvency ratios."""
    z1 = _zscore_rolling(_safe_div(equity, assets), _TD_2Y)
    z2 = _zscore_rolling(_safe_div(assetsc, liabilitiesc), _TD_2Y)
    z3 = _zscore_rolling(_safe_div(ebit, intexp.abs().replace(0, np.nan)), _TD_2Y)
    z4 = _zscore_rolling(_safe_div(ncfo, liabilities), _TD_2Y)
    return (z1 + z2 + z3 + z4) / 4.0


def slv_ext_073_distress_severity_composite(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    assetsc: pd.Series, liabilitiesc: pd.Series,
) -> pd.Series:
    """Capitulation severity composite: Z'' distress depth + current-ratio + leverage shortfalls."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    z_depth = (1.1 - z).clip(lower=0.0) / 1.1
    cr_gap = (1.0 - _safe_div(assetsc, liabilitiesc)).clip(lower=0.0)
    lev_excess = (_safe_div(liabilities, assets) - 1.0).clip(lower=0.0)
    return z_depth + cr_gap + lev_excess


def slv_ext_074_solvency_deterioration_flag(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
) -> pd.Series:
    """Binary flag: Altman Z'' below its 2-year mean AND falling YoY (deterioration regime)."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    below_avg = (z < _rolling_mean(z, _TD_2Y))
    falling = (z < z.shift(_TD_YEAR))
    return (below_avg & falling).astype(float)


def slv_ext_075_capitulation_solvency_score(
    workingcapital: pd.Series, assets: pd.Series, retearn: pd.Series,
    ebit: pd.Series, equity: pd.Series, liabilities: pd.Series,
    netinc: pd.Series, ncfo: pd.Series,
) -> pd.Series:
    """Capitulation solvency score: normalized Z'' distress depth + inverse 3y pct-rank
    + negative-equity flag + negative-cashflow flag. Higher = more extreme distress."""
    z = _altman_z(workingcapital, assets, retearn, ebit, equity, liabilities)
    depth = (1.1 - z).clip(lower=0.0) / 1.1
    rank = _rolling_rank_pct(z, _TD_3Y)
    neg_eq = (equity < 0.0).astype(float)
    neg_cf = (ncfo < 0.0).astype(float)
    return depth + (1.0 - rank.fillna(0.5)) + 0.5 * neg_eq + 0.5 * neg_cf


# ── Registry 001-075 ──────────────────────────────────────────────────────────

SOLVENCY_SCORES_EXTENDED_REGISTRY_001_075 = {
    "slv_ext_001_altman_z_depth_below_1p1": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_001_altman_z_depth_below_1p1},
    "slv_ext_002_altman_z_depth_below_0": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_002_altman_z_depth_below_0},
    "slv_ext_003_altman_z_distance_to_safe": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_003_altman_z_distance_to_safe},
    "slv_ext_004_altman_z_severe_distress_flag": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_004_altman_z_severe_distress_flag},
    "slv_ext_005_leverage_excess_over_1": {"inputs": ["liabilities", "assets"], "func": slv_ext_005_leverage_excess_over_1},
    "slv_ext_006_current_ratio_shortfall_below_1": {"inputs": ["assetsc", "liabilitiesc"], "func": slv_ext_006_current_ratio_shortfall_below_1},
    "slv_ext_007_interest_coverage_shortfall": {"inputs": ["ebit", "intexp"], "func": slv_ext_007_interest_coverage_shortfall},
    "slv_ext_008_equity_to_assets_shortfall_below_0p2": {"inputs": ["equity", "assets"], "func": slv_ext_008_equity_to_assets_shortfall_below_0p2},
    "slv_ext_009_negative_equity_depth": {"inputs": ["equity", "assets"], "func": slv_ext_009_negative_equity_depth},
    "slv_ext_010_debt_to_ebitda_excess_over_4": {"inputs": ["debt", "ebitda"], "func": slv_ext_010_debt_to_ebitda_excess_over_4},
    "slv_ext_011_cash_coverage_shortfall_below_0p1": {"inputs": ["cashnequiv", "liabilities"], "func": slv_ext_011_cash_coverage_shortfall_below_0p1},
    "slv_ext_012_altman_z_distress_severity_norm": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_012_altman_z_distress_severity_norm},
    "slv_ext_013_altman_z_original_coeffs": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_013_altman_z_original_coeffs},
    "slv_ext_014_altman_z_equal_weight": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_014_altman_z_equal_weight},
    "slv_ext_015_profitability_weighted_score": {"inputs": ["retearn", "assets", "ebit", "netinc"], "func": slv_ext_015_profitability_weighted_score},
    "slv_ext_016_liquidity_weighted_score": {"inputs": ["workingcapital", "assets", "assetsc", "liabilitiesc", "cashnequiv", "liabilities"], "func": slv_ext_016_liquidity_weighted_score},
    "slv_ext_017_cashflow_solvency_score": {"inputs": ["ncfo", "debt", "liabilitiesc", "assets"], "func": slv_ext_017_cashflow_solvency_score},
    "slv_ext_018_zmijewski_no_liquidity": {"inputs": ["netinc", "assets", "liabilities"], "func": slv_ext_018_zmijewski_no_liquidity},
    "slv_ext_019_springate_revenue_heavy": {"inputs": ["workingcapital", "assets", "ebit", "ebt", "liabilitiesc", "revenue"], "func": slv_ext_019_springate_revenue_heavy},
    "slv_ext_020_contingent_claims_proxy": {"inputs": ["equity", "liabilities"], "func": slv_ext_020_contingent_claims_proxy},
    "slv_ext_021_ohlson_style_score": {"inputs": ["assets", "liabilities", "workingcapital", "netinc", "liabilitiesc", "assetsc"], "func": slv_ext_021_ohlson_style_score},
    "slv_ext_022_grover_style_score": {"inputs": ["workingcapital", "assets", "ebit", "netinc"], "func": slv_ext_022_grover_style_score},
    "slv_ext_023_fulmer_style_partial": {"inputs": ["retearn", "assets", "ebit", "equity", "liabilities"], "func": slv_ext_023_fulmer_style_partial},
    "slv_ext_024_taffler_style_score": {"inputs": ["ebt", "liabilitiesc", "assetsc", "liabilities", "assets"], "func": slv_ext_024_taffler_style_score},
    "slv_ext_025_long_term_debt_to_equity": {"inputs": ["debt", "equity"], "func": slv_ext_025_long_term_debt_to_equity},
    "slv_ext_026_long_term_debt_to_assets": {"inputs": ["debt", "assets"], "func": slv_ext_026_long_term_debt_to_assets},
    "slv_ext_027_short_term_debt_share": {"inputs": ["debtc", "debt"], "func": slv_ext_027_short_term_debt_share},
    "slv_ext_028_net_debt_to_assets": {"inputs": ["debt", "cashnequiv", "assets"], "func": slv_ext_028_net_debt_to_assets},
    "slv_ext_029_net_debt_to_ebitda": {"inputs": ["debt", "cashnequiv", "ebitda"], "func": slv_ext_029_net_debt_to_ebitda},
    "slv_ext_030_equity_multiplier": {"inputs": ["assets", "equity"], "func": slv_ext_030_equity_multiplier},
    "slv_ext_031_cash_to_current_liabilities": {"inputs": ["cashnequiv", "liabilitiesc"], "func": slv_ext_031_cash_to_current_liabilities},
    "slv_ext_032_working_capital_to_revenue": {"inputs": ["workingcapital", "revenue"], "func": slv_ext_032_working_capital_to_revenue},
    "slv_ext_033_retearn_to_equity": {"inputs": ["retearn", "equity"], "func": slv_ext_033_retearn_to_equity},
    "slv_ext_034_ebitda_to_interest": {"inputs": ["ebitda", "intexp"], "func": slv_ext_034_ebitda_to_interest},
    "slv_ext_035_debt_service_coverage": {"inputs": ["ncfo", "intexp", "debtc"], "func": slv_ext_035_debt_service_coverage},
    "slv_ext_036_defensive_interval_proxy": {"inputs": ["assetsc", "revenue"], "func": slv_ext_036_defensive_interval_proxy},
    "slv_ext_037_consec_days_negative_equity": {"inputs": ["equity"], "func": slv_ext_037_consec_days_negative_equity},
    "slv_ext_038_consec_days_current_ratio_below_1": {"inputs": ["assetsc", "liabilitiesc"], "func": slv_ext_038_consec_days_current_ratio_below_1},
    "slv_ext_039_consec_days_negative_netinc": {"inputs": ["netinc"], "func": slv_ext_039_consec_days_negative_netinc},
    "slv_ext_040_consec_days_negative_ncfo": {"inputs": ["ncfo"], "func": slv_ext_040_consec_days_negative_ncfo},
    "slv_ext_041_consec_days_altman_severe": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_041_consec_days_altman_severe},
    "slv_ext_042_consec_days_interest_uncovered": {"inputs": ["ebit", "intexp"], "func": slv_ext_042_consec_days_interest_uncovered},
    "slv_ext_043_time_since_altman_safe": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_043_time_since_altman_safe},
    "slv_ext_044_time_since_positive_equity": {"inputs": ["equity"], "func": slv_ext_044_time_since_positive_equity},
    "slv_ext_045_distress_quarter_count_3y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_045_distress_quarter_count_3y},
    "slv_ext_046_negative_netinc_quarter_count_3y": {"inputs": ["netinc"], "func": slv_ext_046_negative_netinc_quarter_count_3y},
    "slv_ext_047_current_ratio_below_1_count_2y": {"inputs": ["assetsc", "liabilitiesc"], "func": slv_ext_047_current_ratio_below_1_count_2y},
    "slv_ext_048_altman_below_safe_fraction_2y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_048_altman_below_safe_fraction_2y},
    "slv_ext_049_leverage_zscore_2y": {"inputs": ["liabilities", "assets"], "func": slv_ext_049_leverage_zscore_2y},
    "slv_ext_050_current_ratio_zscore_2y": {"inputs": ["assetsc", "liabilitiesc"], "func": slv_ext_050_current_ratio_zscore_2y},
    "slv_ext_051_interest_coverage_zscore_2y": {"inputs": ["ebit", "intexp"], "func": slv_ext_051_interest_coverage_zscore_2y},
    "slv_ext_052_equity_to_assets_zscore_3y": {"inputs": ["equity", "assets"], "func": slv_ext_052_equity_to_assets_zscore_3y},
    "slv_ext_053_debt_to_ebitda_zscore_2y": {"inputs": ["debt", "ebitda"], "func": slv_ext_053_debt_to_ebitda_zscore_2y},
    "slv_ext_054_leverage_pct_rank_3y": {"inputs": ["liabilities", "assets"], "func": slv_ext_054_leverage_pct_rank_3y},
    "slv_ext_055_current_ratio_pct_rank_3y": {"inputs": ["assetsc", "liabilitiesc"], "func": slv_ext_055_current_ratio_pct_rank_3y},
    "slv_ext_056_altman_z_pct_rank_3y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_056_altman_z_pct_rank_3y},
    "slv_ext_057_altman_z_zscore_3y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_057_altman_z_zscore_3y},
    "slv_ext_058_interest_coverage_pct_rank_2y": {"inputs": ["ebit", "intexp"], "func": slv_ext_058_interest_coverage_pct_rank_2y},
    "slv_ext_059_cash_to_liabilities_pct_rank_3y": {"inputs": ["cashnequiv", "liabilities"], "func": slv_ext_059_cash_to_liabilities_pct_rank_3y},
    "slv_ext_060_altman_z_expanding_zscore": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_060_altman_z_expanding_zscore},
    "slv_ext_061_altman_z_drawdown_2y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_061_altman_z_drawdown_2y},
    "slv_ext_062_altman_z_drawdown_pct_2y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_062_altman_z_drawdown_pct_2y},
    "slv_ext_063_current_ratio_drawdown_2y": {"inputs": ["assetsc", "liabilitiesc"], "func": slv_ext_063_current_ratio_drawdown_2y},
    "slv_ext_064_equity_to_assets_drawdown_3y": {"inputs": ["equity", "assets"], "func": slv_ext_064_equity_to_assets_drawdown_3y},
    "slv_ext_065_altman_z_2y_change": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_065_altman_z_2y_change},
    "slv_ext_066_leverage_yoy_change": {"inputs": ["liabilities", "assets"], "func": slv_ext_066_leverage_yoy_change},
    "slv_ext_067_interest_coverage_yoy_change": {"inputs": ["ebit", "intexp"], "func": slv_ext_067_interest_coverage_yoy_change},
    "slv_ext_068_altman_z_rolling_std_2y": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_068_altman_z_rolling_std_2y},
    "slv_ext_069_low_liquidity_low_profit_flag": {"inputs": ["assetsc", "liabilitiesc", "netinc"], "func": slv_ext_069_low_liquidity_low_profit_flag},
    "slv_ext_070_high_leverage_negative_cf_flag": {"inputs": ["liabilities", "assets", "ncfo"], "func": slv_ext_070_high_leverage_negative_cf_flag},
    "slv_ext_071_triple_distress_count": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "assetsc", "liabilitiesc"], "func": slv_ext_071_triple_distress_count},
    "slv_ext_072_solvency_health_zscore_index": {"inputs": ["equity", "assets", "assetsc", "liabilitiesc", "ebit", "intexp", "ncfo", "liabilities"], "func": slv_ext_072_solvency_health_zscore_index},
    "slv_ext_073_distress_severity_composite": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "assetsc", "liabilitiesc"], "func": slv_ext_073_distress_severity_composite},
    "slv_ext_074_solvency_deterioration_flag": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities"], "func": slv_ext_074_solvency_deterioration_flag},
    "slv_ext_075_capitulation_solvency_score": {"inputs": ["workingcapital", "assets", "retearn", "ebit", "equity", "liabilities", "netinc", "ncfo"], "func": slv_ext_075_capitulation_solvency_score},
}
