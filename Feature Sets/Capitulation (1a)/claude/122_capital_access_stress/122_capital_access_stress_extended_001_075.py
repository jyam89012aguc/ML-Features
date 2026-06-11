"""
122_capital_access_stress — Extended Features 001-075
Domain: stress on the firm's access to external capital — deeper variants, multi-signal
        confluence, regime flags, long-horizon ratios, earnings-adjusted financing metrics,
        working-capital funded vs externally funded distinctions, invcap-based leverage.
Asset class: US equities | Sharadar SF1 fundamentals (FUNDAMENTAL folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly cadence on daily index:
  1 quarter = 63 trading days, 1 year = 252 td.
  QoQ change = .diff(63) or .shift(63); YoY = 252.
  Forward-filled quarterly data steps 4x/year — expected and correct.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2YR  = 504
_TD_3YR  = 756
_TD_5YR  = 1260
_EPS     = 1e-9

# ── Alignment helper ──────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


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


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=False)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Long-horizon financing and leverage ratios ---

def cas_ext_001_ncff_12q_sum(ncff: pd.Series) -> pd.Series:
    """Trailing 12-quarter (3-year, 756 td) sum of NCFF — long-horizon external capital need."""
    return _rolling_sum(ncff, _TD_3YR)


def cas_ext_002_ncfdebt_12q_sum(ncfdebt: pd.Series) -> pd.Series:
    """Trailing 12-quarter sum of net debt issuance."""
    return _rolling_sum(ncfdebt, _TD_3YR)


def cas_ext_003_ncfcommon_12q_sum(ncfcommon: pd.Series) -> pd.Series:
    """Trailing 12-quarter sum of ncfcommon (long-horizon equity capital raised)."""
    return _rolling_sum(ncfcommon, _TD_3YR)


def cas_ext_004_ncff_pct_rank_12q(ncff: pd.Series) -> pd.Series:
    """Percentile rank of NCFF within trailing 12-quarter (3-year) window."""
    return ncff.rolling(_TD_3YR, min_periods=max(2, _TD_3YR // 4)).rank(pct=True)


def cas_ext_005_ncfdebt_pct_rank_12q(ncfdebt: pd.Series) -> pd.Series:
    """Percentile rank of ncfdebt within trailing 12-quarter window."""
    return ncfdebt.rolling(_TD_3YR, min_periods=max(2, _TD_3YR // 4)).rank(pct=True)


def cas_ext_006_leverage_pct_rank_12q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Percentile rank of leverage (debt/equity) within trailing 12-quarter window."""
    lev = _safe_div(debt, equity.abs())
    return lev.rolling(_TD_3YR, min_periods=max(2, _TD_3YR // 4)).rank(pct=True)


def cas_ext_007_debt_to_invcap_ratio(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    """Debt / invested capital (invcap): leverage against the total capital deployed."""
    return _safe_div(debt, invcap.abs())


def cas_ext_008_ncff_to_invcap(ncff: pd.Series, invcap: pd.Series) -> pd.Series:
    """TTM NCFF / invested capital: external capital raised as fraction of invested base."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return _safe_div(ncff4q, invcap.abs())


def cas_ext_009_debt_to_ebitda_ratio(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Total debt / EBITDA: classic credit-stress leverage ratio (high = strained access)."""
    return _safe_div(debt, ebitda.abs())


def cas_ext_010_net_debt_to_ebitda(debt: pd.Series, cashnequiv: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Net debt / EBITDA: credit-adjusted leverage."""
    net_debt = debt - cashnequiv
    return _safe_div(net_debt, ebitda.abs())


def cas_ext_011_debt_to_ebit_ratio(debt: pd.Series, ebit: pd.Series) -> pd.Series:
    """Total debt / EBIT: leverage against operating income (excludes DA from coverage)."""
    return _safe_div(debt, ebit.abs())


def cas_ext_012_intexp_to_ebit_ratio(intexp: pd.Series, ebit: pd.Series) -> pd.Series:
    """Interest expense / EBIT: classic interest coverage from earnings (< 1 = coverage gap)."""
    return _safe_div(intexp.abs(), ebit.abs())


def cas_ext_013_ncff_zscore_12q(ncff: pd.Series) -> pd.Series:
    """Z-score of NCFF within trailing 12-quarter distribution."""
    return _zscore_rolling(ncff, _TD_3YR)


def cas_ext_014_ncfdebt_zscore_12q(ncfdebt: pd.Series) -> pd.Series:
    """Z-score of ncfdebt within trailing 12-quarter distribution."""
    return _zscore_rolling(ncfdebt, _TD_3YR)


def cas_ext_015_leverage_expanding_pct_rank(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of leverage (debt/equity) — at all-time high?"""
    lev = _safe_div(debt, equity.abs())
    return lev.expanding(min_periods=4).rank(pct=True)


# --- Group B (016-028): Earnings-adjusted financing measures ---

def cas_ext_016_ncff_to_netinc(ncff: pd.Series, netinc: pd.Series) -> pd.Series:
    """NCFF / |net income|: external capital raised per dollar of earnings (high = reliant)."""
    return _safe_div(ncff, netinc.abs())


def cas_ext_017_ncfdebt_to_netinc(ncfdebt: pd.Series, netinc: pd.Series) -> pd.Series:
    """ncfdebt / |net income|: debt capital raised relative to earnings."""
    return _safe_div(ncfdebt, netinc.abs())


def cas_ext_018_ncfcommon_to_netinc(ncfcommon: pd.Series, netinc: pd.Series) -> pd.Series:
    """ncfcommon / |net income|: equity capital raised relative to earnings."""
    return _safe_div(ncfcommon, netinc.abs())


def cas_ext_019_intexp_to_netinc(intexp: pd.Series, netinc: pd.Series) -> pd.Series:
    """Interest expense / |net income|: debt burden relative to after-tax earnings."""
    return _safe_div(intexp.abs(), netinc.abs())


def cas_ext_020_debt_to_netinc_ratio(debt: pd.Series, netinc: pd.Series) -> pd.Series:
    """Total debt / TTM net income: debt payback in earnings years."""
    netinc4q = _rolling_sum(netinc, _TD_YEAR)
    return _safe_div(debt, netinc4q.abs())


def cas_ext_021_ncff_to_eps(ncff: pd.Series, eps: pd.Series) -> pd.Series:
    """TTM NCFF / |EPS|: per-share external-capital intensity (high = heavy equity reliance)."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return _safe_div(ncff4q, eps.abs())


def cas_ext_022_debt_negative_netinc_flag(debt: pd.Series, netinc: pd.Series) -> pd.Series:
    """1 if debt > 0 and net income is negative (loss-making while leveraged — constrained access)."""
    return ((debt > 0) & (netinc < 0)).astype(float)


def cas_ext_023_ncff_positive_netinc_negative_flag(ncff: pd.Series, netinc: pd.Series) -> pd.Series:
    """1 if ncff > 0 and net income < 0 — raising external capital while losing money."""
    return ((ncff > 0) & (netinc < 0)).astype(float)


def cas_ext_024_ncfdebt_positive_netinc_negative_flag(ncfdebt: pd.Series, netinc: pd.Series) -> pd.Series:
    """1 if ncfdebt > 0 and net income < 0 — borrowing while losing money (severe distress)."""
    return ((ncfdebt > 0) & (netinc < 0)).astype(float)


def cas_ext_025_all_stress_flag(ncff: pd.Series, netinc: pd.Series,
                                  ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """1 if: ncff > 0 AND net income < 0 AND ncfo < 0 AND debt > 0 (maximum capital stress indicator)."""
    return ((ncff > 0) & (netinc < 0) & (ncfo < 0) & (debt > 0)).astype(float)


def cas_ext_026_ncff_to_ebitda(ncff: pd.Series, ebitda: pd.Series) -> pd.Series:
    """TTM NCFF / |EBITDA|: external capital raised relative to cash earnings proxy."""
    ncff4q   = _rolling_sum(ncff, _TD_YEAR)
    ebitda4q = _rolling_sum(ebitda, _TD_YEAR)
    return _safe_div(ncff4q, ebitda4q.abs())


def cas_ext_027_intexp_to_ebitda_ratio(intexp: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Interest expense / EBITDA (standard bond-covenant coverage proxy)."""
    intexp4q = _rolling_sum(intexp.abs(), _TD_YEAR)
    ebitda4q = _rolling_sum(ebitda, _TD_YEAR)
    return _safe_div(intexp4q, ebitda4q.abs())


def cas_ext_028_debt_to_ebitda_pct_rank_8q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Percentile rank of debt/EBITDA within 8-quarter window."""
    ratio = _safe_div(debt, ebitda.abs())
    return ratio.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


# --- Group C (029-040): Working capital and liquidity stress ---

def cas_ext_029_working_capital_level(workingcapital: pd.Series) -> pd.Series:
    """Working capital level — negative = short-term funding stress."""
    return workingcapital.copy()


def cas_ext_030_working_capital_negative_flag(workingcapital: pd.Series) -> pd.Series:
    """1 if working capital is negative (short-term liabilities exceed short-term assets)."""
    return (workingcapital < 0).astype(float)


def cas_ext_031_working_capital_qoq_change(workingcapital: pd.Series) -> pd.Series:
    """QoQ change in working capital — declining = liquidity deterioration."""
    return workingcapital.diff(_TD_QTR)


def cas_ext_032_working_capital_to_debt(workingcapital: pd.Series, debt: pd.Series) -> pd.Series:
    """Working capital / total debt: short-term liquidity buffer vs debt obligations."""
    return _safe_div(workingcapital, debt.abs())


def cas_ext_033_working_capital_to_revenue(workingcapital: pd.Series, revenue: pd.Series) -> pd.Series:
    """Working capital / revenue: liquidity relative to operational scale."""
    return _safe_div(workingcapital, revenue)


def cas_ext_034_liabilitiesc_to_assetsc(liabilitiesc: pd.Series, assetsc: pd.Series) -> pd.Series:
    """Current liabilities / current assets: liquidity ratio (inverse of current ratio; high = stress)."""
    return _safe_div(liabilitiesc, assetsc)


def cas_ext_035_liabilitiesc_to_cashnequiv(liabilitiesc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Current liabilities / cash: immediate cash coverage of current obligations."""
    return _safe_div(liabilitiesc, cashnequiv)


def cas_ext_036_debtc_to_liabilitiesc(debtc: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Current debt / current liabilities: financial vs operating near-term claims ratio."""
    return _safe_div(debtc, liabilitiesc)


def cas_ext_037_ncfi_positive_ncff_positive_flag(ncfi: pd.Series, ncff: pd.Series) -> pd.Series:
    """1 if both ncfi > 0 and ncff > 0 — asset sales AND external capital raised (capital trap)."""
    return ((ncfi > 0) & (ncff > 0)).astype(float)


def cas_ext_038_ncff_ncfi_ncfo_all_positive_flag(ncfo: pd.Series, ncfi: pd.Series,
                                                   ncff: pd.Series) -> pd.Series:
    """1 if all three cash flows positive: ops, investing, and financing all provide cash (unusual)."""
    return ((ncfo > 0) & (ncfi > 0) & (ncff > 0)).astype(float)


def cas_ext_039_cash_to_currentliab_ratio(cashnequiv: pd.Series, liabilitiesc: pd.Series) -> pd.Series:
    """Cash / current liabilities: quick-ratio proxy (low = near-term liquidity stress)."""
    return _safe_div(cashnequiv, liabilitiesc)


def cas_ext_040_debtc_plus_liabilitiesc_to_assets(debtc: pd.Series, liabilitiesc: pd.Series,
                                                    assets: pd.Series) -> pd.Series:
    """(Current debt + current liabilities) / total assets: total near-term claim intensity."""
    return _safe_div(debtc + liabilitiesc, assets)


# --- Group D (041-052): Capital structure and access-channel stress flags ---

def cas_ext_041_ncfcommon_positive_ncfdebt_positive_yoy_flag(ncfcommon: pd.Series,
                                                               ncfdebt: pd.Series) -> pd.Series:
    """1 if both ncfcommon and ncfdebt positive for TWO consecutive years (sustained dual-channel access)."""
    flag = ((ncfcommon > 0) & (ncfdebt > 0)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def cas_ext_042_ncff_above_2yr_mean_flag(ncff: pd.Series) -> pd.Series:
    """1 if ncff > 2-year rolling mean (above-average external financing — elevated reliance)."""
    m = _rolling_mean(ncff, _TD_2YR)
    return (ncff > m).astype(float)


def cas_ext_043_ncfdebt_above_2yr_mean_flag(ncfdebt: pd.Series) -> pd.Series:
    """1 if ncfdebt > 2-year rolling mean (above-average debt issuance)."""
    m = _rolling_mean(ncfdebt, _TD_2YR)
    return (ncfdebt > m).astype(float)


def cas_ext_044_debt_to_equity_above_2yr_mean_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if leverage > 2-year rolling mean leverage (above historically normal leverage)."""
    lev = _safe_div(debt, equity.abs())
    m   = _rolling_mean(lev, _TD_2YR)
    return (lev > m).astype(float)


def cas_ext_045_ncff_4q_sum_expanding_pct_rank(ncff: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of TTM NCFF (at all-time financing high?)."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return ncff4q.expanding(min_periods=4).rank(pct=True)


def cas_ext_046_ncfdebt_4q_sum_expanding_pct_rank(ncfdebt: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of TTM ncfdebt."""
    ncfdebt4q = _rolling_sum(ncfdebt, _TD_YEAR)
    return ncfdebt4q.expanding(min_periods=4).rank(pct=True)


def cas_ext_047_ncfcommon_4q_sum_expanding_pct_rank(ncfcommon: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of TTM ncfcommon."""
    ncfcommon4q = _rolling_sum(ncfcommon, _TD_YEAR)
    return ncfcommon4q.expanding(min_periods=4).rank(pct=True)


def cas_ext_048_debt_expanding_pct_rank(debt: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of total debt (at an all-time debt high?)."""
    return debt.expanding(min_periods=4).rank(pct=True)


def cas_ext_049_net_debt_expanding_pct_rank(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of net debt."""
    net_debt = debt - cashnequiv
    return net_debt.expanding(min_periods=4).rank(pct=True)


def cas_ext_050_leverage_drawdown_from_alltime_min(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Leverage (debt/equity) drawdown from its all-time expanding minimum (deterioration from best)."""
    lev = _safe_div(debt, equity.abs())
    mn  = lev.expanding(min_periods=4).min()
    return _safe_div(lev - mn, mn.abs())


def cas_ext_051_intexp_to_ncfo_above_1_flag(intexp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """1 if interest expense > |NCFO| (interest exceeds operating cash — severe financing stress)."""
    return (intexp.abs() > ncfo.abs()).astype(float)


def cas_ext_052_debtc_3yr_trend_slope(debtc: pd.Series) -> pd.Series:
    """OLS slope of current debt over trailing 3 years (756 td) — structural near-term debt trend."""
    return _linslope(debtc, _TD_3YR)


# --- Group E (053-063): EWM-smoothed and cross-signal combinations ---

def cas_ext_053_ncff_ewm_3q(ncff: pd.Series) -> pd.Series:
    """3-quarter EWM-smoothed NCFF (reduces stepwise quarterly noise)."""
    return _ewm_mean(ncff, _TD_QTR * 3)


def cas_ext_054_ncfdebt_ewm_3q(ncfdebt: pd.Series) -> pd.Series:
    """3-quarter EWM-smoothed ncfdebt."""
    return _ewm_mean(ncfdebt, _TD_QTR * 3)


def cas_ext_055_leverage_ewm_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """4-quarter EWM-smoothed leverage (debt/equity)."""
    lev = _safe_div(debt, equity.abs())
    return _ewm_mean(lev, _TD_YEAR)


def cas_ext_056_ncff_vs_ncfo_ratio_ewm_4q(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """4-quarter EWM-smoothed (NCFF/|NCFO|) ratio."""
    ratio = _safe_div(ncff, ncfo.abs())
    return _ewm_mean(ratio, _TD_YEAR)


def cas_ext_057_debt_to_ebitda_ewm_4q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """4-quarter EWM-smoothed debt/EBITDA ratio."""
    ratio = _safe_div(debt, ebitda.abs())
    return _ewm_mean(ratio, _TD_YEAR)


def cas_ext_058_intexp_ewm_4q(intexp: pd.Series) -> pd.Series:
    """4-quarter EWM-smoothed interest expense."""
    return _ewm_mean(intexp.abs(), _TD_YEAR)


def cas_ext_059_ncff_minus_capex(ncff: pd.Series, capex: pd.Series) -> pd.Series:
    """TTM NCFF - |capex|: external capital net of investment (surplus = excess external reliance)."""
    ncff4q  = _rolling_sum(ncff, _TD_YEAR)
    capex4q = _rolling_sum(capex.abs(), _TD_YEAR)
    return ncff4q - capex4q


def cas_ext_060_ncfdebt_plus_ncfcommon_vs_ncfo(ncfdebt: pd.Series, ncfcommon: pd.Series,
                                                  ncfo: pd.Series) -> pd.Series:
    """(TTM ncfdebt + ncfcommon) / |TTM NCFO|: combined external capital vs operational funding."""
    external = _rolling_sum(ncfdebt + ncfcommon, _TD_YEAR)
    ops      = _rolling_sum(ncfo, _TD_YEAR)
    return _safe_div(external, ops.abs())


def cas_ext_061_capital_access_worsening_flag(ncff: pd.Series, debt: pd.Series,
                                               equity: pd.Series) -> pd.Series:
    """1 if NCFF > 0 (external reliance) AND leverage is above its 4-quarter mean (rising leverage)."""
    lev  = _safe_div(debt, equity.abs())
    m4q  = _rolling_mean(lev, _TD_YEAR)
    return ((ncff > 0) & (lev > m4q)).astype(float)


def cas_ext_062_financing_distress_triple_flag(ncff: pd.Series, ncfo: pd.Series,
                                                ncfcommon: pd.Series) -> pd.Series:
    """1 if ncff > 0 AND ncfo < 0 AND ncfcommon > 0 (raising equity in a cash-burning firm)."""
    return ((ncff > 0) & (ncfo < 0) & (ncfcommon > 0)).astype(float)


def cas_ext_063_ncff_4q_sum_zscore_expanding(ncff: pd.Series) -> pd.Series:
    """Expanding all-history z-score of TTM NCFF."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    m      = ncff4q.expanding(min_periods=4).mean()
    s      = ncff4q.expanding(min_periods=4).std()
    return _safe_div(ncff4q - m, s)


# --- Group F (064-075): Prefdivis, retearn and equity-regeneration indicators ---

def cas_ext_064_retearn_level(retearn: pd.Series) -> pd.Series:
    """Retained earnings level — negative retained earnings = accumulated capital deficit."""
    return retearn.copy()


def cas_ext_065_retearn_negative_flag(retearn: pd.Series) -> pd.Series:
    """1 if retained earnings are negative (accumulated deficit — equity regeneration needed)."""
    return (retearn < 0).astype(float)


def cas_ext_066_retearn_qoq_change(retearn: pd.Series) -> pd.Series:
    """QoQ change in retained earnings (declining = ongoing capital erosion)."""
    return retearn.diff(_TD_QTR)


def cas_ext_067_retearn_drawdown_from_2yr_peak(retearn: pd.Series) -> pd.Series:
    """Retained earnings drawdown from 2-year peak."""
    peak = _rolling_max(retearn, _TD_2YR)
    return _safe_div(retearn - peak, peak.abs())


def cas_ext_068_retearn_to_equity_ratio(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Retained earnings / book equity: quality of equity (high = organic; low/negative = distressed)."""
    return _safe_div(retearn, equity.abs())


def cas_ext_069_ncfcommon_to_retearn(ncfcommon: pd.Series, retearn: pd.Series) -> pd.Series:
    """TTM ncfcommon / |retained earnings|: equity issuance relative to accumulated surplus/deficit."""
    ncfcommon4q = _rolling_sum(ncfcommon, _TD_YEAR)
    return _safe_div(ncfcommon4q, retearn.abs())


def cas_ext_070_prefdivis_to_dividends(prefdivis: pd.Series, dividends: pd.Series) -> pd.Series:
    """Preferred dividends / total dividends: preferred obligation share of total return (high = constrained)."""
    return _safe_div(prefdivis.abs(), dividends.clip(lower=_EPS))


def cas_ext_071_prefdivis_pct_rank_8q(prefdivis: pd.Series) -> pd.Series:
    """Percentile rank of preferred dividends in 8-quarter window."""
    return prefdivis.abs().rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_ext_072_ncff_negative_retearn_flag(ncff: pd.Series, retearn: pd.Series) -> pd.Series:
    """1 if ncff > 0 AND retained earnings negative (accessing markets to fund an accumulated deficit)."""
    return ((ncff > 0) & (retearn < 0)).astype(float)


def cas_ext_073_triple_constraint_flag(debt: pd.Series, equity: pd.Series,
                                        retearn: pd.Series, ncfo: pd.Series) -> pd.Series:
    """1 if: leverage > 2, retained earnings negative, AND NCFO < 0 (triple-stressed capital access)."""
    lev = _safe_div(debt, equity.abs()).fillna(0)
    return ((lev > 2.0) & (retearn < 0) & (ncfo < 0)).astype(float)


def cas_ext_074_capital_access_stress_score_extended(ncff: pd.Series, ncfdebt: pd.Series,
                                                      ncfcommon: pd.Series, debt: pd.Series,
                                                      equity: pd.Series, cashnequiv: pd.Series,
                                                      intexp: pd.Series, ncfo: pd.Series,
                                                      retearn: pd.Series) -> pd.Series:
    """Extended capital access stress score — 9-input composite.
    Incorporates NCFF reliance, leverage, interest coverage, net-debt rank, and retained-earnings signal.
    Higher = more severe external capital stress."""
    ncff_r  = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    lev     = _safe_div(debt, equity.abs()).fillna(0)
    lev_r   = lev.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    ncfo4q  = _rolling_sum(ncfo, _TD_YEAR)
    int4q   = _rolling_sum(intexp.abs(), _TD_YEAR)
    cov     = _safe_div(ncfo4q, int4q).fillna(1.0).clip(-5, 5)
    cov_n   = 1.0 - (cov + 5.0) / 10.0
    net_d   = debt - cashnequiv
    nd_r    = net_d.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    re_flag = (retearn < 0).astype(float)
    return (0.25 * ncff_r + 0.20 * lev_r + 0.20 * cov_n + 0.20 * nd_r + 0.15 * re_flag)


def cas_ext_075_financing_cycle_length(ncfdebt: pd.Series) -> pd.Series:
    """Estimated financing cycle — periods between consecutive positive ncfdebt quarters
    proxied as: 1 / (fraction of trailing 12q with ncfdebt > 0), clipped to 1-12 quarters."""
    pos_frac = _rolling_sum((ncfdebt > 0).astype(float), _TD_3YR) / 12.0
    cycle    = _safe_div(pd.Series(1.0, index=ncfdebt.index), pos_frac)
    return cycle.clip(lower=1.0, upper=12.0)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITAL_ACCESS_STRESS_EXTENDED_REGISTRY_001_075 = {
    "cas_ext_001_ncff_12q_sum":                          {"inputs": ["ncff"],                                                 "func": cas_ext_001_ncff_12q_sum},
    "cas_ext_002_ncfdebt_12q_sum":                       {"inputs": ["ncfdebt"],                                              "func": cas_ext_002_ncfdebt_12q_sum},
    "cas_ext_003_ncfcommon_12q_sum":                     {"inputs": ["ncfcommon"],                                            "func": cas_ext_003_ncfcommon_12q_sum},
    "cas_ext_004_ncff_pct_rank_12q":                     {"inputs": ["ncff"],                                                 "func": cas_ext_004_ncff_pct_rank_12q},
    "cas_ext_005_ncfdebt_pct_rank_12q":                  {"inputs": ["ncfdebt"],                                              "func": cas_ext_005_ncfdebt_pct_rank_12q},
    "cas_ext_006_leverage_pct_rank_12q":                 {"inputs": ["debt", "equity"],                                       "func": cas_ext_006_leverage_pct_rank_12q},
    "cas_ext_007_debt_to_invcap_ratio":                  {"inputs": ["debt", "invcap"],                                       "func": cas_ext_007_debt_to_invcap_ratio},
    "cas_ext_008_ncff_to_invcap":                        {"inputs": ["ncff", "invcap"],                                       "func": cas_ext_008_ncff_to_invcap},
    "cas_ext_009_debt_to_ebitda_ratio":                  {"inputs": ["debt", "ebitda"],                                       "func": cas_ext_009_debt_to_ebitda_ratio},
    "cas_ext_010_net_debt_to_ebitda":                    {"inputs": ["debt", "cashnequiv", "ebitda"],                         "func": cas_ext_010_net_debt_to_ebitda},
    "cas_ext_011_debt_to_ebit_ratio":                    {"inputs": ["debt", "ebit"],                                         "func": cas_ext_011_debt_to_ebit_ratio},
    "cas_ext_012_intexp_to_ebit_ratio":                  {"inputs": ["intexp", "ebit"],                                       "func": cas_ext_012_intexp_to_ebit_ratio},
    "cas_ext_013_ncff_zscore_12q":                       {"inputs": ["ncff"],                                                 "func": cas_ext_013_ncff_zscore_12q},
    "cas_ext_014_ncfdebt_zscore_12q":                    {"inputs": ["ncfdebt"],                                              "func": cas_ext_014_ncfdebt_zscore_12q},
    "cas_ext_015_leverage_expanding_pct_rank":           {"inputs": ["debt", "equity"],                                       "func": cas_ext_015_leverage_expanding_pct_rank},
    "cas_ext_016_ncff_to_netinc":                        {"inputs": ["ncff", "netinc"],                                       "func": cas_ext_016_ncff_to_netinc},
    "cas_ext_017_ncfdebt_to_netinc":                     {"inputs": ["ncfdebt", "netinc"],                                    "func": cas_ext_017_ncfdebt_to_netinc},
    "cas_ext_018_ncfcommon_to_netinc":                   {"inputs": ["ncfcommon", "netinc"],                                  "func": cas_ext_018_ncfcommon_to_netinc},
    "cas_ext_019_intexp_to_netinc":                      {"inputs": ["intexp", "netinc"],                                     "func": cas_ext_019_intexp_to_netinc},
    "cas_ext_020_debt_to_netinc_ratio":                  {"inputs": ["debt", "netinc"],                                       "func": cas_ext_020_debt_to_netinc_ratio},
    "cas_ext_021_ncff_to_eps":                           {"inputs": ["ncff", "eps"],                                          "func": cas_ext_021_ncff_to_eps},
    "cas_ext_022_debt_negative_netinc_flag":             {"inputs": ["debt", "netinc"],                                       "func": cas_ext_022_debt_negative_netinc_flag},
    "cas_ext_023_ncff_positive_netinc_negative_flag":    {"inputs": ["ncff", "netinc"],                                       "func": cas_ext_023_ncff_positive_netinc_negative_flag},
    "cas_ext_024_ncfdebt_positive_netinc_negative_flag": {"inputs": ["ncfdebt", "netinc"],                                    "func": cas_ext_024_ncfdebt_positive_netinc_negative_flag},
    "cas_ext_025_all_stress_flag":                       {"inputs": ["ncff", "netinc", "ncfo", "debt"],                       "func": cas_ext_025_all_stress_flag},
    "cas_ext_026_ncff_to_ebitda":                        {"inputs": ["ncff", "ebitda"],                                       "func": cas_ext_026_ncff_to_ebitda},
    "cas_ext_027_intexp_to_ebitda_ratio":                {"inputs": ["intexp", "ebitda"],                                     "func": cas_ext_027_intexp_to_ebitda_ratio},
    "cas_ext_028_debt_to_ebitda_pct_rank_8q":            {"inputs": ["debt", "ebitda"],                                       "func": cas_ext_028_debt_to_ebitda_pct_rank_8q},
    "cas_ext_029_working_capital_level":                 {"inputs": ["workingcapital"],                                       "func": cas_ext_029_working_capital_level},
    "cas_ext_030_working_capital_negative_flag":         {"inputs": ["workingcapital"],                                       "func": cas_ext_030_working_capital_negative_flag},
    "cas_ext_031_working_capital_qoq_change":            {"inputs": ["workingcapital"],                                       "func": cas_ext_031_working_capital_qoq_change},
    "cas_ext_032_working_capital_to_debt":               {"inputs": ["workingcapital", "debt"],                               "func": cas_ext_032_working_capital_to_debt},
    "cas_ext_033_working_capital_to_revenue":            {"inputs": ["workingcapital", "revenue"],                            "func": cas_ext_033_working_capital_to_revenue},
    "cas_ext_034_liabilitiesc_to_assetsc":               {"inputs": ["liabilitiesc", "assetsc"],                              "func": cas_ext_034_liabilitiesc_to_assetsc},
    "cas_ext_035_liabilitiesc_to_cashnequiv":            {"inputs": ["liabilitiesc", "cashnequiv"],                           "func": cas_ext_035_liabilitiesc_to_cashnequiv},
    "cas_ext_036_debtc_to_liabilitiesc":                 {"inputs": ["debtc", "liabilitiesc"],                                "func": cas_ext_036_debtc_to_liabilitiesc},
    "cas_ext_037_ncfi_positive_ncff_positive_flag":      {"inputs": ["ncfi", "ncff"],                                         "func": cas_ext_037_ncfi_positive_ncff_positive_flag},
    "cas_ext_038_ncff_ncfi_ncfo_all_positive_flag":      {"inputs": ["ncfo", "ncfi", "ncff"],                                  "func": cas_ext_038_ncff_ncfi_ncfo_all_positive_flag},
    "cas_ext_039_cash_to_currentliab_ratio":             {"inputs": ["cashnequiv", "liabilitiesc"],                           "func": cas_ext_039_cash_to_currentliab_ratio},
    "cas_ext_040_debtc_plus_liabilitiesc_to_assets":     {"inputs": ["debtc", "liabilitiesc", "assets"],                      "func": cas_ext_040_debtc_plus_liabilitiesc_to_assets},
    "cas_ext_041_ncfcommon_positive_ncfdebt_positive_yoy_flag": {"inputs": ["ncfcommon", "ncfdebt"],                          "func": cas_ext_041_ncfcommon_positive_ncfdebt_positive_yoy_flag},
    "cas_ext_042_ncff_above_2yr_mean_flag":              {"inputs": ["ncff"],                                                  "func": cas_ext_042_ncff_above_2yr_mean_flag},
    "cas_ext_043_ncfdebt_above_2yr_mean_flag":           {"inputs": ["ncfdebt"],                                              "func": cas_ext_043_ncfdebt_above_2yr_mean_flag},
    "cas_ext_044_debt_to_equity_above_2yr_mean_flag":    {"inputs": ["debt", "equity"],                                       "func": cas_ext_044_debt_to_equity_above_2yr_mean_flag},
    "cas_ext_045_ncff_4q_sum_expanding_pct_rank":        {"inputs": ["ncff"],                                                  "func": cas_ext_045_ncff_4q_sum_expanding_pct_rank},
    "cas_ext_046_ncfdebt_4q_sum_expanding_pct_rank":     {"inputs": ["ncfdebt"],                                              "func": cas_ext_046_ncfdebt_4q_sum_expanding_pct_rank},
    "cas_ext_047_ncfcommon_4q_sum_expanding_pct_rank":   {"inputs": ["ncfcommon"],                                            "func": cas_ext_047_ncfcommon_4q_sum_expanding_pct_rank},
    "cas_ext_048_debt_expanding_pct_rank":               {"inputs": ["debt"],                                                  "func": cas_ext_048_debt_expanding_pct_rank},
    "cas_ext_049_net_debt_expanding_pct_rank":           {"inputs": ["debt", "cashnequiv"],                                   "func": cas_ext_049_net_debt_expanding_pct_rank},
    "cas_ext_050_leverage_drawdown_from_alltime_min":    {"inputs": ["debt", "equity"],                                       "func": cas_ext_050_leverage_drawdown_from_alltime_min},
    "cas_ext_051_intexp_to_ncfo_above_1_flag":           {"inputs": ["intexp", "ncfo"],                                       "func": cas_ext_051_intexp_to_ncfo_above_1_flag},
    "cas_ext_052_debtc_3yr_trend_slope":                 {"inputs": ["debtc"],                                                "func": cas_ext_052_debtc_3yr_trend_slope},
    "cas_ext_053_ncff_ewm_3q":                           {"inputs": ["ncff"],                                                  "func": cas_ext_053_ncff_ewm_3q},
    "cas_ext_054_ncfdebt_ewm_3q":                        {"inputs": ["ncfdebt"],                                              "func": cas_ext_054_ncfdebt_ewm_3q},
    "cas_ext_055_leverage_ewm_4q":                       {"inputs": ["debt", "equity"],                                       "func": cas_ext_055_leverage_ewm_4q},
    "cas_ext_056_ncff_vs_ncfo_ratio_ewm_4q":             {"inputs": ["ncff", "ncfo"],                                         "func": cas_ext_056_ncff_vs_ncfo_ratio_ewm_4q},
    "cas_ext_057_debt_to_ebitda_ewm_4q":                 {"inputs": ["debt", "ebitda"],                                       "func": cas_ext_057_debt_to_ebitda_ewm_4q},
    "cas_ext_058_intexp_ewm_4q":                         {"inputs": ["intexp"],                                               "func": cas_ext_058_intexp_ewm_4q},
    "cas_ext_059_ncff_minus_capex":                      {"inputs": ["ncff", "capex"],                                        "func": cas_ext_059_ncff_minus_capex},
    "cas_ext_060_ncfdebt_plus_ncfcommon_vs_ncfo":        {"inputs": ["ncfdebt", "ncfcommon", "ncfo"],                         "func": cas_ext_060_ncfdebt_plus_ncfcommon_vs_ncfo},
    "cas_ext_061_capital_access_worsening_flag":         {"inputs": ["ncff", "debt", "equity"],                               "func": cas_ext_061_capital_access_worsening_flag},
    "cas_ext_062_financing_distress_triple_flag":        {"inputs": ["ncff", "ncfo", "ncfcommon"],                            "func": cas_ext_062_financing_distress_triple_flag},
    "cas_ext_063_ncff_4q_sum_zscore_expanding":          {"inputs": ["ncff"],                                                  "func": cas_ext_063_ncff_4q_sum_zscore_expanding},
    "cas_ext_064_retearn_level":                         {"inputs": ["retearn"],                                              "func": cas_ext_064_retearn_level},
    "cas_ext_065_retearn_negative_flag":                 {"inputs": ["retearn"],                                              "func": cas_ext_065_retearn_negative_flag},
    "cas_ext_066_retearn_qoq_change":                    {"inputs": ["retearn"],                                              "func": cas_ext_066_retearn_qoq_change},
    "cas_ext_067_retearn_drawdown_from_2yr_peak":        {"inputs": ["retearn"],                                              "func": cas_ext_067_retearn_drawdown_from_2yr_peak},
    "cas_ext_068_retearn_to_equity_ratio":               {"inputs": ["retearn", "equity"],                                    "func": cas_ext_068_retearn_to_equity_ratio},
    "cas_ext_069_ncfcommon_to_retearn":                  {"inputs": ["ncfcommon", "retearn"],                                 "func": cas_ext_069_ncfcommon_to_retearn},
    "cas_ext_070_prefdivis_to_dividends":                {"inputs": ["prefdivis", "dividends"],                               "func": cas_ext_070_prefdivis_to_dividends},
    "cas_ext_071_prefdivis_pct_rank_8q":                 {"inputs": ["prefdivis"],                                            "func": cas_ext_071_prefdivis_pct_rank_8q},
    "cas_ext_072_ncff_negative_retearn_flag":            {"inputs": ["ncff", "retearn"],                                      "func": cas_ext_072_ncff_negative_retearn_flag},
    "cas_ext_073_triple_constraint_flag":                {"inputs": ["debt", "equity", "retearn", "ncfo"],                    "func": cas_ext_073_triple_constraint_flag},
    "cas_ext_074_capital_access_stress_score_extended":  {"inputs": ["ncff", "ncfdebt", "ncfcommon", "debt", "equity", "cashnequiv", "intexp", "ncfo", "retearn"], "func": cas_ext_074_capital_access_stress_score_extended},
    "cas_ext_075_financing_cycle_length":                {"inputs": ["ncfdebt"],                                              "func": cas_ext_075_financing_cycle_length},
}
