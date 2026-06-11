"""
76_balance_sheet_decay — Extended Features 001-075
Domain: holistic multi-quarter balance-sheet deterioration — additional cross-line
        ratios, new lookback windows, decay streaks, EWM-deviation and rank variants
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

These are EXTENDED features in the balance-sheet-decay domain: net-new variants
that do NOT duplicate base_001_075, base_076_150, 2nd_derivatives or
3rd_derivatives.  They explore new windows (1Q/3Q/3Y/5Y), additional cross-line
ratios (cash/debt, retained-earnings/equity, debt/assets growth spreads),
EWM-deviation smoothing, percentile-rank distress, decay-streak persistence and
multi-line composite decay scores at new horizons.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series,
forward-filled from the most recent quarterly Sharadar SF1 report known as of
each date.  A forward-filled quarterly series steps at most 4 times per year;
flat stretches between report dates are correct and expected.  Functions look
strictly backward using .shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days, 1 year = 252.
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
_TD_3Q   = 189
_EPS     = 1e-9

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
    """Element-wise division; replaces zero denominator with NaN."""
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _yoy_pct(s: pd.Series) -> pd.Series:
    """YoY percent change with abs-denominator guard."""
    prior = s.shift(_TD_YEAR)
    return _safe_div_abs(s - prior, prior)


def _consec_streak(cond: pd.Series, index: pd.Index) -> pd.Series:
    """Consecutive-row streak of True values (backward-looking)."""
    arr = cond.astype(int).values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): New-window single-line changes (3Q, 3Y, 5Y) ---

def bsd_ext_001_assets_3q_change(assets: pd.Series) -> pd.Series:
    """Total assets 3-quarter absolute change (189-day lag)."""
    return assets - assets.shift(_TD_3Q)


def bsd_ext_002_assets_3y_pct(assets: pd.Series) -> pd.Series:
    """Total assets 3-year percent change."""
    prior = assets.shift(_TD_3Y)
    return _safe_div_abs(assets - prior, prior)


def bsd_ext_003_assets_5y_pct(assets: pd.Series) -> pd.Series:
    """Total assets 5-year percent change."""
    prior = assets.shift(_TD_5Y)
    return _safe_div_abs(assets - prior, prior)


def bsd_ext_004_equity_3q_change(equity: pd.Series) -> pd.Series:
    """Total equity 3-quarter absolute change."""
    return equity - equity.shift(_TD_3Q)


def bsd_ext_005_equity_5y_pct(equity: pd.Series) -> pd.Series:
    """Total equity 5-year percent change."""
    prior = equity.shift(_TD_5Y)
    return _safe_div_abs(equity - prior, prior)


def bsd_ext_006_retearn_3q_change(retearn: pd.Series) -> pd.Series:
    """Retained earnings 3-quarter absolute change."""
    return retearn - retearn.shift(_TD_3Q)


def bsd_ext_007_retearn_3y_pct(retearn: pd.Series) -> pd.Series:
    """Retained earnings 3-year percent change."""
    prior = retearn.shift(_TD_3Y)
    return _safe_div_abs(retearn - prior, prior)


def bsd_ext_008_debt_3q_change(debt: pd.Series) -> pd.Series:
    """Total debt 3-quarter absolute change."""
    return debt - debt.shift(_TD_3Q)


def bsd_ext_009_debt_3y_pct(debt: pd.Series) -> pd.Series:
    """Total debt 3-year percent change."""
    prior = debt.shift(_TD_3Y)
    return _safe_div_abs(debt - prior, prior)


def bsd_ext_010_liabilities_3q_change(liabilities: pd.Series) -> pd.Series:
    """Total liabilities 3-quarter absolute change."""
    return liabilities - liabilities.shift(_TD_3Q)


def bsd_ext_011_cashnequiv_3q_change(cashnequiv: pd.Series) -> pd.Series:
    """Cash and equivalents 3-quarter absolute change."""
    return cashnequiv - cashnequiv.shift(_TD_3Q)


def bsd_ext_012_workingcapital_qoq_change(workingcapital: pd.Series) -> pd.Series:
    """Working capital QoQ absolute change (63-day lag)."""
    return workingcapital - workingcapital.shift(_TD_QTR)


# --- Group B (013-024): Additional cross-line ratios ---

def bsd_ext_013_cash_to_debt_ratio(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """Cash and equivalents divided by total debt — debt-coverage liquidity ratio."""
    return _safe_div(cashnequiv, debt)


def bsd_ext_014_cash_to_assets_ratio(cashnequiv: pd.Series, assets: pd.Series) -> pd.Series:
    """Cash and equivalents divided by total assets — cash buffer ratio."""
    return _safe_div(cashnequiv, assets)


def bsd_ext_015_retearn_to_equity_ratio(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Retained earnings divided by equity — accumulated-profit share of book."""
    return _safe_div(retearn, equity.abs().replace(0, np.nan))


def bsd_ext_016_retearn_to_assets_ratio(retearn: pd.Series, assets: pd.Series) -> pd.Series:
    """Retained earnings divided by total assets — Altman-style retained-earnings ratio."""
    return _safe_div(retearn, assets)


def bsd_ext_017_workingcapital_to_assets_ratio(workingcapital: pd.Series, assets: pd.Series) -> pd.Series:
    """Working capital divided by total assets — Altman-style liquidity ratio."""
    return _safe_div(workingcapital, assets)


def bsd_ext_018_equity_to_assets_ratio(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Total equity divided by total assets — equity ratio (inverse leverage)."""
    return _safe_div(equity, assets)


def bsd_ext_019_debtnc_to_debt_ratio(debtnc: pd.Series, debt: pd.Series) -> pd.Series:
    """Non-current debt divided by total debt — long-term debt mix."""
    return _safe_div(debtnc, debt)


def bsd_ext_020_liabilitiesc_to_liabilities_ratio(liabilitiesc: pd.Series,
                                                   liabilities: pd.Series) -> pd.Series:
    """Current liabilities divided by total liabilities — near-term obligation mix."""
    return _safe_div(liabilitiesc, liabilities)


def bsd_ext_021_invcap_to_assets_ratio(invcap: pd.Series, assets: pd.Series) -> pd.Series:
    """Invested capital divided by total assets — capital intensity of the base."""
    return _safe_div(invcap, assets)


def bsd_ext_022_nav_to_assets_ratio(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset value divided by total assets (equivalent to equity ratio proxy)."""
    nav = assets - liabilities
    return _safe_div(nav, assets)


def bsd_ext_023_debt_to_nav_ratio(debt: pd.Series, assets: pd.Series,
                                   liabilities: pd.Series) -> pd.Series:
    """Total debt divided by net asset value — leverage vs net worth."""
    nav = assets - liabilities
    return _safe_div(debt, nav.abs().replace(0, np.nan))


def bsd_ext_024_cashnequiv_to_workingcapital_ratio(cashnequiv: pd.Series,
                                                    workingcapital: pd.Series) -> pd.Series:
    """Cash divided by working capital — cash share of net current position."""
    return _safe_div(cashnequiv, workingcapital.abs().replace(0, np.nan))


# --- Group C (025-036): Cross-line growth spreads ---

def bsd_ext_025_debt_growth_minus_assets_growth(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY pct growth of debt minus YoY pct growth of assets — leverage build."""
    return _yoy_pct(debt) - _yoy_pct(assets)


def bsd_ext_026_liabilities_growth_minus_equity_growth(liabilities: pd.Series,
                                                        equity: pd.Series) -> pd.Series:
    """YoY pct growth of liabilities minus YoY pct growth of equity."""
    return _yoy_pct(liabilities) - _yoy_pct(equity)


def bsd_ext_027_debt_growth_minus_cash_growth(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY pct growth of debt minus YoY pct growth of cash — net liquidity erosion."""
    return _yoy_pct(debt) - _yoy_pct(cashnequiv)


def bsd_ext_028_assets_growth_minus_equity_growth(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY pct growth of assets minus YoY pct growth of equity — leverage inflation."""
    return _yoy_pct(assets) - _yoy_pct(equity)


def bsd_ext_029_liabilities_growth_minus_retearn_growth(liabilities: pd.Series,
                                                         retearn: pd.Series) -> pd.Series:
    """YoY pct growth of liabilities minus YoY pct growth of retained earnings."""
    return _yoy_pct(liabilities) - _yoy_pct(retearn)


def bsd_ext_030_debtnc_growth_minus_equity_growth(debtnc: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY pct growth of long-term debt minus YoY pct growth of equity."""
    return _yoy_pct(debtnc) - _yoy_pct(equity)


def bsd_ext_031_liabilitiesc_growth_minus_cash_growth(liabilitiesc: pd.Series,
                                                       cashnequiv: pd.Series) -> pd.Series:
    """YoY pct growth of current liabilities minus YoY pct growth of cash."""
    return _yoy_pct(liabilitiesc) - _yoy_pct(cashnequiv)


def bsd_ext_032_debt_growth_minus_invcap_growth(debt: pd.Series, invcap: pd.Series) -> pd.Series:
    """YoY pct growth of debt minus YoY pct growth of invested capital."""
    return _yoy_pct(debt) - _yoy_pct(invcap)


def bsd_ext_033_qoq_debt_growth_minus_equity_growth(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ pct growth of debt minus QoQ pct growth of equity (short-horizon spread)."""
    d = _safe_div_abs(debt - debt.shift(_TD_QTR), debt.shift(_TD_QTR))
    e = _safe_div_abs(equity - equity.shift(_TD_QTR), equity.shift(_TD_QTR))
    return d - e


def bsd_ext_034_assets_growth_minus_cash_growth(assets: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """YoY pct growth of assets minus YoY pct growth of cash."""
    return _yoy_pct(assets) - _yoy_pct(cashnequiv)


def bsd_ext_035_leverage_ratio_yoy_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in the debt-to-equity ratio (leverage drift over one year)."""
    de = _safe_div(debt, equity.abs().replace(0, np.nan))
    return de - de.shift(_TD_YEAR)


def bsd_ext_036_liab_to_assets_yoy_change(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """YoY change in the liabilities-to-assets ratio (financial-leverage drift)."""
    la = _safe_div(liabilities, assets)
    return la - la.shift(_TD_YEAR)


# --- Group D (037-048): EWM-deviation and rolling-mean-gap variants ---

def bsd_ext_037_equity_ewm_deviation_4q(equity: pd.Series) -> pd.Series:
    """Equity minus its 4Q-span EWM — current level vs smoothed trend."""
    return equity - _ewm_mean(equity, _TD_YEAR)


def bsd_ext_038_assets_ewm_deviation_4q(assets: pd.Series) -> pd.Series:
    """Total assets minus its 4Q-span EWM."""
    return assets - _ewm_mean(assets, _TD_YEAR)


def bsd_ext_039_cashnequiv_ewm_deviation_4q(cashnequiv: pd.Series) -> pd.Series:
    """Cash and equivalents minus its 4Q-span EWM (cash-burn smoothing gap)."""
    return cashnequiv - _ewm_mean(cashnequiv, _TD_YEAR)


def bsd_ext_040_retearn_ewm_deviation_8q(retearn: pd.Series) -> pd.Series:
    """Retained earnings minus its 8Q-span EWM."""
    return retearn - _ewm_mean(retearn, _TD_2Y)


def bsd_ext_041_debt_ewm_deviation_4q(debt: pd.Series) -> pd.Series:
    """Total debt minus its 4Q-span EWM (debt build vs smoothed level)."""
    return debt - _ewm_mean(debt, _TD_YEAR)


def bsd_ext_042_equity_minus_rolling_mean_8q(equity: pd.Series) -> pd.Series:
    """Equity minus its trailing 8Q rolling mean."""
    return equity - _rolling_mean(equity, _TD_2Y)


def bsd_ext_043_workingcapital_ewm_deviation_4q(workingcapital: pd.Series) -> pd.Series:
    """Working capital minus its 4Q-span EWM."""
    return workingcapital - _ewm_mean(workingcapital, _TD_YEAR)


def bsd_ext_044_liabilities_ewm_deviation_4q(liabilities: pd.Series) -> pd.Series:
    """Total liabilities minus its 4Q-span EWM."""
    return liabilities - _ewm_mean(liabilities, _TD_YEAR)


def bsd_ext_045_nav_ewm_deviation_4q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Net asset value minus its 4Q-span EWM."""
    nav = assets - liabilities
    return nav - _ewm_mean(nav, _TD_YEAR)


def bsd_ext_046_equity_norm_ewm_deviation_4q(equity: pd.Series) -> pd.Series:
    """Equity EWM-deviation normalized by abs(EWM) — relative deviation."""
    ewm = _ewm_mean(equity, _TD_YEAR)
    return _safe_div_abs(equity - ewm, ewm)


def bsd_ext_047_cashnequiv_norm_ewm_deviation_4q(cashnequiv: pd.Series) -> pd.Series:
    """Cash EWM-deviation normalized by abs(EWM) — relative cash deviation."""
    ewm = _ewm_mean(cashnequiv, _TD_YEAR)
    return _safe_div_abs(cashnequiv - ewm, ewm)


def bsd_ext_048_debt_norm_ewm_deviation_4q(debt: pd.Series) -> pd.Series:
    """Debt EWM-deviation normalized by abs(EWM) — relative debt deviation."""
    ewm = _ewm_mean(debt, _TD_YEAR)
    return _safe_div_abs(debt - ewm, ewm)


# --- Group E (049-060): Percentile-rank distress and range positions ---

def bsd_ext_049_equity_pct_rank_8q(equity: pd.Series) -> pd.Series:
    """Percentile rank of equity within trailing 8Q window (low = near worst)."""
    return _rolling_rank_pct(equity, _TD_2Y)


def bsd_ext_050_equity_pct_rank_12q(equity: pd.Series) -> pd.Series:
    """Percentile rank of equity within trailing 12Q window."""
    return _rolling_rank_pct(equity, _TD_3Y)


def bsd_ext_051_retearn_pct_rank_8q(retearn: pd.Series) -> pd.Series:
    """Percentile rank of retained earnings within trailing 8Q window."""
    return _rolling_rank_pct(retearn, _TD_2Y)


def bsd_ext_052_cashnequiv_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash and equivalents within trailing 8Q window."""
    return _rolling_rank_pct(cashnequiv, _TD_2Y)


def bsd_ext_053_assets_pct_rank_8q(assets: pd.Series) -> pd.Series:
    """Percentile rank of total assets within trailing 8Q window."""
    return _rolling_rank_pct(assets, _TD_2Y)


def bsd_ext_054_workingcapital_pct_rank_8q(workingcapital: pd.Series) -> pd.Series:
    """Percentile rank of working capital within trailing 8Q window."""
    return _rolling_rank_pct(workingcapital, _TD_2Y)


def bsd_ext_055_nav_pct_rank_8q(assets: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Percentile rank of net asset value within trailing 8Q window."""
    nav = assets - liabilities
    return _rolling_rank_pct(nav, _TD_2Y)


def bsd_ext_056_equity_range_position_8q(equity: pd.Series) -> pd.Series:
    """Equity position within its 8Q min-max range (0 = at the low, 1 = at the high)."""
    hi = _rolling_max(equity, _TD_2Y)
    lo = _rolling_min(equity, _TD_2Y)
    return _safe_div(equity - lo, hi - lo)


def bsd_ext_057_retearn_range_position_8q(retearn: pd.Series) -> pd.Series:
    """Retained earnings position within its 8Q min-max range."""
    hi = _rolling_max(retearn, _TD_2Y)
    lo = _rolling_min(retearn, _TD_2Y)
    return _safe_div(retearn - lo, hi - lo)


def bsd_ext_058_cashnequiv_range_position_4q(cashnequiv: pd.Series) -> pd.Series:
    """Cash and equivalents position within its 4Q min-max range."""
    hi = _rolling_max(cashnequiv, _TD_YEAR)
    lo = _rolling_min(cashnequiv, _TD_YEAR)
    return _safe_div(cashnequiv - lo, hi - lo)


def bsd_ext_059_debt_pct_rank_12q(debt: pd.Series) -> pd.Series:
    """Percentile rank of total debt within trailing 12Q window (high = max leverage)."""
    return _rolling_rank_pct(debt, _TD_3Y)


def bsd_ext_060_liabilities_pct_rank_12q(liabilities: pd.Series) -> pd.Series:
    """Percentile rank of total liabilities within trailing 12Q window."""
    return _rolling_rank_pct(liabilities, _TD_3Y)


# --- Group F (061-068): Decay-streak persistence and at-low flags ---

def bsd_ext_061_equity_decline_streak(equity: pd.Series) -> pd.Series:
    """Consecutive quarters of QoQ equity decline (daily-row streak)."""
    return _consec_streak(equity < equity.shift(_TD_QTR), equity.index)


def bsd_ext_062_retearn_decline_streak(retearn: pd.Series) -> pd.Series:
    """Consecutive quarters of QoQ retained-earnings decline (daily-row streak)."""
    return _consec_streak(retearn < retearn.shift(_TD_QTR), retearn.index)


def bsd_ext_063_cashnequiv_decline_streak(cashnequiv: pd.Series) -> pd.Series:
    """Consecutive quarters of QoQ cash decline (cash-burn streak)."""
    return _consec_streak(cashnequiv < cashnequiv.shift(_TD_QTR), cashnequiv.index)


def bsd_ext_064_debt_increase_streak(debt: pd.Series) -> pd.Series:
    """Consecutive quarters of QoQ debt increase (leverage-build streak)."""
    return _consec_streak(debt > debt.shift(_TD_QTR), debt.index)


def bsd_ext_065_equity_at_8q_low_flag(equity: pd.Series) -> pd.Series:
    """1 if equity is at or below its trailing 8Q rolling minimum."""
    lo = _rolling_min(equity, _TD_2Y)
    return (equity <= lo + _EPS).astype(float)


def bsd_ext_066_cashnequiv_at_8q_low_flag(cashnequiv: pd.Series) -> pd.Series:
    """1 if cash and equivalents is at or below its trailing 8Q rolling minimum."""
    lo = _rolling_min(cashnequiv, _TD_2Y)
    return (cashnequiv <= lo + _EPS).astype(float)


def bsd_ext_067_retearn_at_expanding_low_flag(retearn: pd.Series) -> pd.Series:
    """1 if retained earnings is at its all-history expanding minimum."""
    lo = retearn.expanding(min_periods=1).min()
    return (retearn <= lo + _EPS).astype(float)


def bsd_ext_068_debt_at_8q_high_flag(debt: pd.Series) -> pd.Series:
    """1 if total debt is at or above its trailing 8Q rolling maximum (peak leverage)."""
    hi = _rolling_max(debt, _TD_2Y)
    return (debt >= hi - _EPS).astype(float)


# --- Group G (069-075): Multi-line composite decay scores at new horizons ---

def bsd_ext_069_bs_decay_composite_4line_12q(assets: pd.Series, liabilities: pd.Series,
                                              equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Composite balance-sheet decay z-score (4 lines, 12Q window); negative = decay."""
    z_a = _zscore_rolling(assets, _TD_3Y)
    z_l = _zscore_rolling(-liabilities, _TD_3Y)
    z_e = _zscore_rolling(equity, _TD_3Y)
    z_c = _zscore_rolling(cashnequiv, _TD_3Y)
    return (z_a + z_l + z_e + z_c) / 4.0


def bsd_ext_070_bs_decay_composite_5line_8q(assets: pd.Series, equity: pd.Series,
                                             cashnequiv: pd.Series, retearn: pd.Series,
                                             debt: pd.Series) -> pd.Series:
    """Composite decay z-score over 8Q for assets, equity, cash, retained earnings, (neg)debt."""
    z_a = _zscore_rolling(assets, _TD_2Y)
    z_e = _zscore_rolling(equity, _TD_2Y)
    z_c = _zscore_rolling(cashnequiv, _TD_2Y)
    z_r = _zscore_rolling(retearn, _TD_2Y)
    z_d = _zscore_rolling(-debt, _TD_2Y)
    return (z_a + z_e + z_c + z_r + z_d) / 5.0


def bsd_ext_071_decline_breadth_yoy_6lines(assets: pd.Series, equity: pd.Series,
                                            cashnequiv: pd.Series, retearn: pd.Series,
                                            workingcapital: pd.Series, invcap: pd.Series) -> pd.Series:
    """Count of 6 balance-sheet lines lower YoY (assets, equity, cash, RE, WC, invcap; 0-6)."""
    flags = [
        (assets < assets.shift(_TD_YEAR)).astype(float),
        (equity < equity.shift(_TD_YEAR)).astype(float),
        (cashnequiv < cashnequiv.shift(_TD_YEAR)).astype(float),
        (retearn < retearn.shift(_TD_YEAR)).astype(float),
        (workingcapital < workingcapital.shift(_TD_YEAR)).astype(float),
        (invcap < invcap.shift(_TD_YEAR)).astype(float),
    ]
    return sum(flags)


def bsd_ext_072_leverage_distress_count(liabilities: pd.Series, assets: pd.Series,
                                         debt: pd.Series, equity: pd.Series) -> pd.Series:
    """
    Count of leverage-distress conditions met (0-4): liabilities/assets > 0.8,
    debt/equity > 2, equity < 0, debt rose YoY.
    """
    c1 = (_safe_div(liabilities, assets) > 0.8).astype(float)
    c2 = (_safe_div(debt, equity.abs().replace(0, np.nan)) > 2.0).astype(float)
    c3 = (equity < 0).astype(float)
    c4 = (debt > debt.shift(_TD_YEAR)).astype(float)
    return c1 + c2 + c3 + c4


def bsd_ext_073_bs_decay_index_qoq_slope_8q(assets: pd.Series, liabilities: pd.Series,
                                             equity: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the 8Q composite 4-line decay z-score (slope of decay)."""
    idx = bsd_ext_069_bs_decay_composite_4line_12q(assets, liabilities, equity, cashnequiv)
    return idx - idx.shift(_TD_QTR)


def bsd_ext_074_cash_runway_decay_score(cashnequiv: pd.Series, debt: pd.Series,
                                         equity: pd.Series) -> pd.Series:
    """
    Cash-runway decay score: average z-score (8Q) of cash/debt coverage and equity,
    minus debt z-score. Lower = thinner runway / deeper distress.
    """
    cov = _safe_div(cashnequiv, debt)
    z_cov = _zscore_rolling(cov, _TD_2Y)
    z_eq  = _zscore_rolling(equity, _TD_2Y)
    z_debt = _zscore_rolling(debt, _TD_2Y)
    return (z_cov + z_eq - z_debt) / 3.0


def bsd_ext_075_solvency_drawdown_composite(assets: pd.Series, liabilities: pd.Series,
                                             equity: pd.Series, retearn: pd.Series) -> pd.Series:
    """
    Composite solvency drawdown: average signed fractional drawdown from 8Q peaks
    of equity, net asset value and retained earnings. More negative = deeper erosion.
    """
    nav = assets - liabilities
    dd_e  = _safe_div_abs(equity - _rolling_max(equity, _TD_2Y), _rolling_max(equity, _TD_2Y))
    dd_n  = _safe_div_abs(nav - _rolling_max(nav, _TD_2Y), _rolling_max(nav, _TD_2Y))
    dd_r  = _safe_div_abs(retearn - _rolling_max(retearn, _TD_2Y), _rolling_max(retearn, _TD_2Y))
    return (dd_e + dd_n + dd_r) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

BALANCE_SHEET_DECAY_EXTENDED_REGISTRY_001_075 = {
    "bsd_ext_001_assets_3q_change":                  {"inputs": ["assets"],                                          "func": bsd_ext_001_assets_3q_change},
    "bsd_ext_002_assets_3y_pct":                     {"inputs": ["assets"],                                          "func": bsd_ext_002_assets_3y_pct},
    "bsd_ext_003_assets_5y_pct":                     {"inputs": ["assets"],                                          "func": bsd_ext_003_assets_5y_pct},
    "bsd_ext_004_equity_3q_change":                  {"inputs": ["equity"],                                          "func": bsd_ext_004_equity_3q_change},
    "bsd_ext_005_equity_5y_pct":                     {"inputs": ["equity"],                                          "func": bsd_ext_005_equity_5y_pct},
    "bsd_ext_006_retearn_3q_change":                 {"inputs": ["retearn"],                                         "func": bsd_ext_006_retearn_3q_change},
    "bsd_ext_007_retearn_3y_pct":                    {"inputs": ["retearn"],                                         "func": bsd_ext_007_retearn_3y_pct},
    "bsd_ext_008_debt_3q_change":                    {"inputs": ["debt"],                                            "func": bsd_ext_008_debt_3q_change},
    "bsd_ext_009_debt_3y_pct":                       {"inputs": ["debt"],                                            "func": bsd_ext_009_debt_3y_pct},
    "bsd_ext_010_liabilities_3q_change":             {"inputs": ["liabilities"],                                     "func": bsd_ext_010_liabilities_3q_change},
    "bsd_ext_011_cashnequiv_3q_change":              {"inputs": ["cashnequiv"],                                      "func": bsd_ext_011_cashnequiv_3q_change},
    "bsd_ext_012_workingcapital_qoq_change":         {"inputs": ["workingcapital"],                                  "func": bsd_ext_012_workingcapital_qoq_change},
    "bsd_ext_013_cash_to_debt_ratio":                {"inputs": ["cashnequiv", "debt"],                              "func": bsd_ext_013_cash_to_debt_ratio},
    "bsd_ext_014_cash_to_assets_ratio":              {"inputs": ["cashnequiv", "assets"],                            "func": bsd_ext_014_cash_to_assets_ratio},
    "bsd_ext_015_retearn_to_equity_ratio":           {"inputs": ["retearn", "equity"],                               "func": bsd_ext_015_retearn_to_equity_ratio},
    "bsd_ext_016_retearn_to_assets_ratio":           {"inputs": ["retearn", "assets"],                               "func": bsd_ext_016_retearn_to_assets_ratio},
    "bsd_ext_017_workingcapital_to_assets_ratio":    {"inputs": ["workingcapital", "assets"],                        "func": bsd_ext_017_workingcapital_to_assets_ratio},
    "bsd_ext_018_equity_to_assets_ratio":            {"inputs": ["equity", "assets"],                                "func": bsd_ext_018_equity_to_assets_ratio},
    "bsd_ext_019_debtnc_to_debt_ratio":              {"inputs": ["debtnc", "debt"],                                  "func": bsd_ext_019_debtnc_to_debt_ratio},
    "bsd_ext_020_liabilitiesc_to_liabilities_ratio": {"inputs": ["liabilitiesc", "liabilities"],                     "func": bsd_ext_020_liabilitiesc_to_liabilities_ratio},
    "bsd_ext_021_invcap_to_assets_ratio":            {"inputs": ["invcap", "assets"],                                "func": bsd_ext_021_invcap_to_assets_ratio},
    "bsd_ext_022_nav_to_assets_ratio":               {"inputs": ["assets", "liabilities"],                           "func": bsd_ext_022_nav_to_assets_ratio},
    "bsd_ext_023_debt_to_nav_ratio":                 {"inputs": ["debt", "assets", "liabilities"],                   "func": bsd_ext_023_debt_to_nav_ratio},
    "bsd_ext_024_cashnequiv_to_workingcapital_ratio":{"inputs": ["cashnequiv", "workingcapital"],                    "func": bsd_ext_024_cashnequiv_to_workingcapital_ratio},
    "bsd_ext_025_debt_growth_minus_assets_growth":   {"inputs": ["debt", "assets"],                                  "func": bsd_ext_025_debt_growth_minus_assets_growth},
    "bsd_ext_026_liabilities_growth_minus_equity_growth": {"inputs": ["liabilities", "equity"],                      "func": bsd_ext_026_liabilities_growth_minus_equity_growth},
    "bsd_ext_027_debt_growth_minus_cash_growth":     {"inputs": ["debt", "cashnequiv"],                              "func": bsd_ext_027_debt_growth_minus_cash_growth},
    "bsd_ext_028_assets_growth_minus_equity_growth": {"inputs": ["assets", "equity"],                                "func": bsd_ext_028_assets_growth_minus_equity_growth},
    "bsd_ext_029_liabilities_growth_minus_retearn_growth": {"inputs": ["liabilities", "retearn"],                    "func": bsd_ext_029_liabilities_growth_minus_retearn_growth},
    "bsd_ext_030_debtnc_growth_minus_equity_growth": {"inputs": ["debtnc", "equity"],                                "func": bsd_ext_030_debtnc_growth_minus_equity_growth},
    "bsd_ext_031_liabilitiesc_growth_minus_cash_growth": {"inputs": ["liabilitiesc", "cashnequiv"],                  "func": bsd_ext_031_liabilitiesc_growth_minus_cash_growth},
    "bsd_ext_032_debt_growth_minus_invcap_growth":   {"inputs": ["debt", "invcap"],                                  "func": bsd_ext_032_debt_growth_minus_invcap_growth},
    "bsd_ext_033_qoq_debt_growth_minus_equity_growth": {"inputs": ["debt", "equity"],                                "func": bsd_ext_033_qoq_debt_growth_minus_equity_growth},
    "bsd_ext_034_assets_growth_minus_cash_growth":   {"inputs": ["assets", "cashnequiv"],                            "func": bsd_ext_034_assets_growth_minus_cash_growth},
    "bsd_ext_035_leverage_ratio_yoy_change":         {"inputs": ["debt", "equity"],                                  "func": bsd_ext_035_leverage_ratio_yoy_change},
    "bsd_ext_036_liab_to_assets_yoy_change":         {"inputs": ["liabilities", "assets"],                           "func": bsd_ext_036_liab_to_assets_yoy_change},
    "bsd_ext_037_equity_ewm_deviation_4q":           {"inputs": ["equity"],                                          "func": bsd_ext_037_equity_ewm_deviation_4q},
    "bsd_ext_038_assets_ewm_deviation_4q":           {"inputs": ["assets"],                                          "func": bsd_ext_038_assets_ewm_deviation_4q},
    "bsd_ext_039_cashnequiv_ewm_deviation_4q":       {"inputs": ["cashnequiv"],                                      "func": bsd_ext_039_cashnequiv_ewm_deviation_4q},
    "bsd_ext_040_retearn_ewm_deviation_8q":          {"inputs": ["retearn"],                                         "func": bsd_ext_040_retearn_ewm_deviation_8q},
    "bsd_ext_041_debt_ewm_deviation_4q":             {"inputs": ["debt"],                                            "func": bsd_ext_041_debt_ewm_deviation_4q},
    "bsd_ext_042_equity_minus_rolling_mean_8q":      {"inputs": ["equity"],                                          "func": bsd_ext_042_equity_minus_rolling_mean_8q},
    "bsd_ext_043_workingcapital_ewm_deviation_4q":   {"inputs": ["workingcapital"],                                  "func": bsd_ext_043_workingcapital_ewm_deviation_4q},
    "bsd_ext_044_liabilities_ewm_deviation_4q":      {"inputs": ["liabilities"],                                     "func": bsd_ext_044_liabilities_ewm_deviation_4q},
    "bsd_ext_045_nav_ewm_deviation_4q":              {"inputs": ["assets", "liabilities"],                           "func": bsd_ext_045_nav_ewm_deviation_4q},
    "bsd_ext_046_equity_norm_ewm_deviation_4q":      {"inputs": ["equity"],                                          "func": bsd_ext_046_equity_norm_ewm_deviation_4q},
    "bsd_ext_047_cashnequiv_norm_ewm_deviation_4q":  {"inputs": ["cashnequiv"],                                      "func": bsd_ext_047_cashnequiv_norm_ewm_deviation_4q},
    "bsd_ext_048_debt_norm_ewm_deviation_4q":        {"inputs": ["debt"],                                            "func": bsd_ext_048_debt_norm_ewm_deviation_4q},
    "bsd_ext_049_equity_pct_rank_8q":                {"inputs": ["equity"],                                          "func": bsd_ext_049_equity_pct_rank_8q},
    "bsd_ext_050_equity_pct_rank_12q":               {"inputs": ["equity"],                                          "func": bsd_ext_050_equity_pct_rank_12q},
    "bsd_ext_051_retearn_pct_rank_8q":               {"inputs": ["retearn"],                                         "func": bsd_ext_051_retearn_pct_rank_8q},
    "bsd_ext_052_cashnequiv_pct_rank_8q":            {"inputs": ["cashnequiv"],                                      "func": bsd_ext_052_cashnequiv_pct_rank_8q},
    "bsd_ext_053_assets_pct_rank_8q":                {"inputs": ["assets"],                                          "func": bsd_ext_053_assets_pct_rank_8q},
    "bsd_ext_054_workingcapital_pct_rank_8q":        {"inputs": ["workingcapital"],                                  "func": bsd_ext_054_workingcapital_pct_rank_8q},
    "bsd_ext_055_nav_pct_rank_8q":                   {"inputs": ["assets", "liabilities"],                           "func": bsd_ext_055_nav_pct_rank_8q},
    "bsd_ext_056_equity_range_position_8q":          {"inputs": ["equity"],                                          "func": bsd_ext_056_equity_range_position_8q},
    "bsd_ext_057_retearn_range_position_8q":         {"inputs": ["retearn"],                                         "func": bsd_ext_057_retearn_range_position_8q},
    "bsd_ext_058_cashnequiv_range_position_4q":      {"inputs": ["cashnequiv"],                                      "func": bsd_ext_058_cashnequiv_range_position_4q},
    "bsd_ext_059_debt_pct_rank_12q":                 {"inputs": ["debt"],                                            "func": bsd_ext_059_debt_pct_rank_12q},
    "bsd_ext_060_liabilities_pct_rank_12q":          {"inputs": ["liabilities"],                                     "func": bsd_ext_060_liabilities_pct_rank_12q},
    "bsd_ext_061_equity_decline_streak":             {"inputs": ["equity"],                                          "func": bsd_ext_061_equity_decline_streak},
    "bsd_ext_062_retearn_decline_streak":            {"inputs": ["retearn"],                                         "func": bsd_ext_062_retearn_decline_streak},
    "bsd_ext_063_cashnequiv_decline_streak":         {"inputs": ["cashnequiv"],                                      "func": bsd_ext_063_cashnequiv_decline_streak},
    "bsd_ext_064_debt_increase_streak":              {"inputs": ["debt"],                                            "func": bsd_ext_064_debt_increase_streak},
    "bsd_ext_065_equity_at_8q_low_flag":             {"inputs": ["equity"],                                          "func": bsd_ext_065_equity_at_8q_low_flag},
    "bsd_ext_066_cashnequiv_at_8q_low_flag":         {"inputs": ["cashnequiv"],                                      "func": bsd_ext_066_cashnequiv_at_8q_low_flag},
    "bsd_ext_067_retearn_at_expanding_low_flag":     {"inputs": ["retearn"],                                         "func": bsd_ext_067_retearn_at_expanding_low_flag},
    "bsd_ext_068_debt_at_8q_high_flag":              {"inputs": ["debt"],                                            "func": bsd_ext_068_debt_at_8q_high_flag},
    "bsd_ext_069_bs_decay_composite_4line_12q":      {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],   "func": bsd_ext_069_bs_decay_composite_4line_12q},
    "bsd_ext_070_bs_decay_composite_5line_8q":       {"inputs": ["assets", "equity", "cashnequiv", "retearn", "debt"], "func": bsd_ext_070_bs_decay_composite_5line_8q},
    "bsd_ext_071_decline_breadth_yoy_6lines":        {"inputs": ["assets", "equity", "cashnequiv", "retearn", "workingcapital", "invcap"], "func": bsd_ext_071_decline_breadth_yoy_6lines},
    "bsd_ext_072_leverage_distress_count":           {"inputs": ["liabilities", "assets", "debt", "equity"],         "func": bsd_ext_072_leverage_distress_count},
    "bsd_ext_073_bs_decay_index_qoq_slope_8q":       {"inputs": ["assets", "liabilities", "equity", "cashnequiv"],   "func": bsd_ext_073_bs_decay_index_qoq_slope_8q},
    "bsd_ext_074_cash_runway_decay_score":           {"inputs": ["cashnequiv", "debt", "equity"],                    "func": bsd_ext_074_cash_runway_decay_score},
    "bsd_ext_075_solvency_drawdown_composite":       {"inputs": ["assets", "liabilities", "equity", "retearn"],      "func": bsd_ext_075_solvency_drawdown_composite},
}
