"""valuation_extreme_snapshot base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 of the 150 distinct hypotheses on bubble-multiple snapshots for Nasdaq stocks
near multi-year peaks. Continued in __base__076_150.py.

Inputs: SF1 quarterly fundamentals (forward-filled to daily by the binder) plus
DAILY-cadence valuation series. PIT-clean: right-anchored rolling windows with
explicit min_periods, no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _winsorize(s, lower=0.01, upper=0.99):
    lo = s.quantile(lower)
    hi = s.quantile(upper)
    return s.clip(lower=lo, upper=hi)


# ============================================================
#                    FEATURES 001-075
# ============================================================

# -------- Block A: Level multiples (001-015) --------

def f15_vesp_001_pe_level_raw(pe: pd.Series) -> pd.Series:
    """Raw P/E ratio level — direct snapshot multiple."""
    return pe.astype(float)


def f15_vesp_002_log_pe_level(pe: pd.Series) -> pd.Series:
    """Log P/E to compress the long right tail at bubble peaks."""
    return _safe_log(pe)


def f15_vesp_003_ps_level_raw(ps: pd.Series) -> pd.Series:
    """Raw P/S ratio — sales-multiple snapshot."""
    return ps.astype(float)


def f15_vesp_004_log_ps_level(ps: pd.Series) -> pd.Series:
    """Log P/S — tail-compressed sales multiple."""
    return _safe_log(ps)


def f15_vesp_005_pb_level_raw(pb: pd.Series) -> pd.Series:
    """Raw P/B ratio — book-multiple snapshot."""
    return pb.astype(float)


def f15_vesp_006_log_pb_level(pb: pd.Series) -> pd.Series:
    """Log P/B — tail-compressed book multiple."""
    return _safe_log(pb)


def f15_vesp_007_evebitda_level(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA level — capital-structure-adjusted earnings multiple."""
    return evebitda.astype(float)


def f15_vesp_008_log_evebitda_level(evebitda: pd.Series) -> pd.Series:
    """Log EV/EBITDA — bubble-tail compression."""
    return _safe_log(evebitda)


def f15_vesp_009_evebit_level(evebit: pd.Series) -> pd.Series:
    """EV/EBIT level — operating-earnings multiple."""
    return evebit.astype(float)


def f15_vesp_010_evsales_level(evsales: pd.Series) -> pd.Series:
    """EV/Sales — capital-structure-adjusted sales multiple."""
    return evsales.astype(float)


def f15_vesp_011_ev_to_fcf(ev: pd.Series, fcf: pd.Series) -> pd.Series:
    """EV-to-trailing free-cash-flow — true cash multiple."""
    return _safe_div(ev, fcf)


def f15_vesp_012_ev_to_cfo(ev: pd.Series, ncfo: pd.Series) -> pd.Series:
    """EV-to-operating-cash-flow — pre-capex valuation."""
    return _safe_div(ev, ncfo)


def f15_vesp_013_mcap_to_tangibles(marketcap: pd.Series, tangibles: pd.Series) -> pd.Series:
    """Marketcap-to-tangible-book — premium over hard assets."""
    return _safe_div(marketcap, tangibles)


def f15_vesp_014_mcap_to_retearn(marketcap: pd.Series, retearn: pd.Series) -> pd.Series:
    """Marketcap-to-retained-earnings — premium over cumulative profits."""
    return _safe_div(marketcap, retearn)


def f15_vesp_015_fcfp_inverse(fcfp: pd.Series) -> pd.Series:
    """Inverse FCF yield = price-to-FCF multiple."""
    return _safe_div(1.0, fcfp)


# -------- Block B: Yield inversions (016-023) --------

def f15_vesp_016_earnings_yield(pe: pd.Series) -> pd.Series:
    """Earnings yield = 1/PE — inverted multiple for additive scales."""
    return _safe_div(1.0, pe)


def f15_vesp_017_fcf_yield_level(fcfp: pd.Series) -> pd.Series:
    """FCF yield level — cash-flow-based return-on-price."""
    return fcfp.astype(float)


def f15_vesp_018_cfo_yield(ncfo: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Operating cash flow yield = ncfo / marketcap."""
    return _safe_div(ncfo, marketcap)


def f15_vesp_019_sales_yield(revenue: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Sales yield = revenue / marketcap — inverted P/S."""
    return _safe_div(revenue, marketcap)


def f15_vesp_020_ebitda_yield(ebitda: pd.Series, ev: pd.Series) -> pd.Series:
    """EBITDA yield on EV = ebitda / ev — inverted EV/EBITDA."""
    return _safe_div(ebitda, ev)


def f15_vesp_021_ebit_yield(ebit: pd.Series, ev: pd.Series) -> pd.Series:
    """EBIT yield on EV = ebit / ev — pre-tax operating return on EV."""
    return _safe_div(ebit, ev)


def f15_vesp_022_book_yield(equity: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Book yield = equity / marketcap — inverted P/B."""
    return _safe_div(equity, marketcap)


def f15_vesp_023_dividend_yield_level(divyield: pd.Series) -> pd.Series:
    """Dividend yield level — bubble names typically zero, mature reflexive opposite."""
    return divyield.astype(float)


# -------- Block C: PEG-style growth-adjusted multiples (024-033) --------

def f15_vesp_024_pe_to_revenue_growth(pe: pd.Series, revenue: pd.Series) -> pd.Series:
    """PE divided by YoY revenue growth — PE-PEG bubble measure."""
    rev_growth = revenue.pct_change(YDAYS)
    return _safe_div(pe, rev_growth)


def f15_vesp_025_ps_to_revenue_growth(ps: pd.Series, revenue: pd.Series) -> pd.Series:
    """PS / YoY revenue growth — sales-PEG."""
    rev_growth = revenue.pct_change(YDAYS)
    return _safe_div(ps, rev_growth)


def f15_vesp_026_evebitda_to_ebitda_growth(evebitda: pd.Series, ebitda: pd.Series) -> pd.Series:
    """EV/EBITDA divided by YoY EBITDA growth — EBITDA-PEG."""
    eg = ebitda.pct_change(YDAYS)
    return _safe_div(evebitda, eg)


def f15_vesp_027_evsales_to_revenue_growth(evsales: pd.Series, revenue: pd.Series) -> pd.Series:
    """EV/Sales divided by sales growth — capital-adjusted sales-PEG."""
    rev_growth = revenue.pct_change(YDAYS)
    return _safe_div(evsales, rev_growth)


def f15_vesp_028_pe_to_earnings_growth(pe: pd.Series, netinc: pd.Series) -> pd.Series:
    """Classic PEG = PE / YoY earnings growth."""
    ng = netinc.pct_change(YDAYS)
    return _safe_div(pe, ng)


def f15_vesp_029_pb_to_equity_growth(pb: pd.Series, equity: pd.Series) -> pd.Series:
    """PB normalized by book growth — bubble book multiple per book-growth point."""
    eg = equity.pct_change(YDAYS)
    return _safe_div(pb, eg)


def f15_vesp_030_ps_to_revenue_growth_63d(ps: pd.Series, revenue: pd.Series) -> pd.Series:
    """Short-horizon sales-PEG (63d revenue trend) — fast-decel detector."""
    rev_growth = revenue.pct_change(QDAYS)
    return _safe_div(ps, rev_growth)


def f15_vesp_031_pe_to_eps_growth(pe: pd.Series, eps: pd.Series) -> pd.Series:
    """PE / YoY EPS growth — per-share PEG."""
    eg = eps.pct_change(YDAYS)
    return _safe_div(pe, eg)


def f15_vesp_032_evebit_to_ebit_growth(evebit: pd.Series, ebit: pd.Series) -> pd.Series:
    """EV/EBIT divided by EBIT growth — operating-PEG."""
    g = ebit.pct_change(YDAYS)
    return _safe_div(evebit, g)


def f15_vesp_033_ev_to_fcf_growth(ev: pd.Series, fcf: pd.Series) -> pd.Series:
    """EV / FCF-growth — cash-PEG, sensitive to growth collapse at peak."""
    g = fcf.pct_change(YDAYS)
    fg_eff = ev / fcf.replace(0, np.nan)
    return _safe_div(fg_eff, g)


# -------- Block D: Multiple z-scores vs trailing history (034-045) --------

def f15_vesp_034_pe_zscore_252d(pe: pd.Series) -> pd.Series:
    """PE z-score vs trailing 252d — 1y stretch hypothesis."""
    return _rolling_zscore(pe, YDAYS)


def f15_vesp_035_pe_zscore_504d(pe: pd.Series) -> pd.Series:
    """PE z-score vs trailing 504d — 2y regime stretch hypothesis."""
    return _rolling_zscore(pe, 504)


def f15_vesp_036_pe_zscore_1260d(pe: pd.Series) -> pd.Series:
    """PE z-score vs trailing 5y — secular bubble overshoot hypothesis."""
    return _rolling_zscore(pe, 1260)


def f15_vesp_037_ps_zscore_252d(ps: pd.Series) -> pd.Series:
    """PS z-score vs trailing 252d — annual sales-multiple stretch."""
    return _rolling_zscore(ps, YDAYS)


def f15_vesp_038_ps_zscore_504d(ps: pd.Series) -> pd.Series:
    """PS z-score vs trailing 504d — biennial regime stretch."""
    return _rolling_zscore(ps, 504)


def f15_vesp_039_ps_zscore_1260d(ps: pd.Series) -> pd.Series:
    """PS z-score vs trailing 5y — secular sales-multiple overshoot."""
    return _rolling_zscore(ps, 1260)


def f15_vesp_040_evebitda_zscore_252d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA z vs 1y — annual EBITDA-multiple stretch."""
    return _rolling_zscore(evebitda, YDAYS)


def f15_vesp_041_evebitda_zscore_504d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA z vs 2y — biennial regime stretch."""
    return _rolling_zscore(evebitda, 504)


def f15_vesp_042_evebitda_zscore_1260d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA z vs 5y — secular overshoot."""
    return _rolling_zscore(evebitda, 1260)


def f15_vesp_043_pb_zscore_252d(pb: pd.Series) -> pd.Series:
    """PB z vs 1y — annual book-multiple stretch."""
    return _rolling_zscore(pb, YDAYS)


def f15_vesp_044_pb_zscore_1260d(pb: pd.Series) -> pd.Series:
    """PB z vs 5y — secular book-multiple overshoot."""
    return _rolling_zscore(pb, 1260)


def f15_vesp_045_evsales_zscore_504d(evsales: pd.Series) -> pd.Series:
    """EV/Sales z vs 2y — capital-adjusted sales stretch."""
    return _rolling_zscore(evsales, 504)


# -------- Block E: Distance-to-history (046-055) --------

def f15_vesp_046_pe_over_252d_mean(pe: pd.Series) -> pd.Series:
    """PE divided by trailing 252d mean PE — ratio-to-history."""
    m = pe.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(pe, m)


def f15_vesp_047_pe_over_252d_median(pe: pd.Series) -> pd.Series:
    """PE divided by trailing 252d median PE — outlier-resistant ratio."""
    m = pe.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(pe, m)


def f15_vesp_048_pe_over_1260d_max(pe: pd.Series) -> pd.Series:
    """PE divided by trailing 5y max PE — fraction of prior secular peak."""
    m = pe.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(pe, m)


def f15_vesp_049_pe_over_252d_p90(pe: pd.Series) -> pd.Series:
    """PE relative to trailing 252d 90th percentile."""
    q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.90)
    return _safe_div(pe, q)


def f15_vesp_050_ps_over_252d_mean(ps: pd.Series) -> pd.Series:
    """PS divided by trailing 252d mean PS."""
    m = ps.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(ps, m)


def f15_vesp_051_ps_over_1260d_max(ps: pd.Series) -> pd.Series:
    """PS divided by trailing 5y max PS."""
    m = ps.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(ps, m)


def f15_vesp_052_evebitda_over_504d_mean(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA divided by trailing 504d mean — biennial baseline ratio."""
    m = evebitda.rolling(504, min_periods=YDAYS).mean()
    return _safe_div(evebitda, m)


def f15_vesp_053_evebitda_over_1260d_p90(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA divided by trailing 5y 90th percentile."""
    q = evebitda.rolling(1260, min_periods=YDAYS).quantile(0.90)
    return _safe_div(evebitda, q)


def f15_vesp_054_pb_over_1260d_median(pb: pd.Series) -> pd.Series:
    """PB divided by trailing 5y median PB."""
    m = pb.rolling(1260, min_periods=YDAYS).median()
    return _safe_div(pb, m)


def f15_vesp_055_evsales_over_1260d_max(evsales: pd.Series) -> pd.Series:
    """EV/Sales divided by trailing 5y max — share of historic stretch."""
    m = evsales.rolling(1260, min_periods=YDAYS).max()
    return _safe_div(evsales, m)


# -------- Block F: EV-to-invested-capital variants (056-063) --------

def f15_vesp_056_ev_to_invested_capital(ev: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """EV / (equity + debt) — premium over invested capital."""
    ic = equity.fillna(0) + debt.fillna(0)
    return _safe_div(ev, ic)


def f15_vesp_057_ev_to_equity_plus_debtnc(ev: pd.Series, equity: pd.Series, debtnc: pd.Series) -> pd.Series:
    """EV / (equity + long-term debt) — long-tenor capital multiple."""
    ic = equity.fillna(0) + debtnc.fillna(0)
    return _safe_div(ev, ic)


def f15_vesp_058_ev_to_tangible_ic(ev: pd.Series, tangibles: pd.Series, debt: pd.Series) -> pd.Series:
    """EV / (tangible book + debt) — hard-asset invested-capital multiple."""
    ic = tangibles.fillna(0) + debt.fillna(0)
    return _safe_div(ev, ic)


def f15_vesp_059_ev_to_assets(ev: pd.Series, assets: pd.Series) -> pd.Series:
    """EV / total assets — asset-based capital multiple."""
    return _safe_div(ev, assets)


def f15_vesp_060_ev_to_equity_only(ev: pd.Series, equity: pd.Series) -> pd.Series:
    """EV / equity — leverage-aware book multiple."""
    return _safe_div(ev, equity)


def f15_vesp_061_ev_to_tangibles_only(ev: pd.Series, tangibles: pd.Series) -> pd.Series:
    """EV / tangible book — premium over hard assets ex-goodwill."""
    return _safe_div(ev, tangibles)


def f15_vesp_062_ev_minus_cash_to_ic(ev: pd.Series, cashneq: pd.Series, equity: pd.Series, debt: pd.Series) -> pd.Series:
    """(EV - cash) / (equity + debt) — net-of-cash IC multiple."""
    ic = equity.fillna(0) + debt.fillna(0)
    return _safe_div(ev - cashneq.fillna(0), ic)


def f15_vesp_063_ev_to_equity_plus_debtc(ev: pd.Series, equity: pd.Series, debtc: pd.Series) -> pd.Series:
    """EV / (equity + short-term debt) — short-tenor capital multiple."""
    ic = equity.fillna(0) + debtc.fillna(0)
    return _safe_div(ev, ic)


# -------- Block G: Negative-fundamental flags (064-071) --------

def f15_vesp_064_loss_making_bubble_flag(pe: pd.Series, netinc: pd.Series) -> pd.Series:
    """1 when netinc < 0 yet PE field is positive (broken multiple) — loss-making bubble."""
    flag = ((netinc < 0) & (pe > 0)).astype(float)
    return flag.where(~(pe.isna() | netinc.isna()), np.nan)


def f15_vesp_065_negative_fcf_high_evsales_flag(fcf: pd.Series, evsales: pd.Series) -> pd.Series:
    """1 when fcf < 0 and EV/Sales > 5 — cash-burning bubble flag."""
    flag = ((fcf < 0) & (evsales > 5)).astype(float)
    return flag.where(~(fcf.isna() | evsales.isna()), np.nan)


def f15_vesp_066_negative_ebitda_high_mcap_flag(ebitda: pd.Series, marketcap: pd.Series) -> pd.Series:
    """1 when ebitda < 0 yet marketcap > 500M — pre-profit hype flag."""
    flag = ((ebitda < 0) & (marketcap > 5e8)).astype(float)
    return flag.where(~(ebitda.isna() | marketcap.isna()), np.nan)


def f15_vesp_067_negative_retearn_with_premium_flag(retearn: pd.Series, marketcap: pd.Series, equity: pd.Series) -> pd.Series:
    """1 when cumulative retained earnings < 0 and price-to-book > 3."""
    pb_eff = _safe_div(marketcap, equity)
    flag = ((retearn < 0) & (pb_eff > 3)).astype(float)
    return flag.where(~(retearn.isna() | pb_eff.isna()), np.nan)


def f15_vesp_068_negative_netinc_persistent_count_4q(netinc: pd.Series) -> pd.Series:
    """Fraction of last 252 days with negative trailing netinc — persistence of unprofitability."""
    return (netinc < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_069_negative_fcf_persistent_count_4q(fcf: pd.Series) -> pd.Series:
    """Fraction of last 252 days with negative trailing FCF — persistent cash-burn flag."""
    return (fcf < 0).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_070_intangible_dominance_flag(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """1 when intangibles / assets > 0.5 — goodwill-heavy book vulnerable to writedown."""
    share = _safe_div(intangibles, assets)
    flag = (share > 0.5).astype(float)
    return flag.where(~share.isna(), np.nan)


def f15_vesp_071_debt_exceeds_equity_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 when total debt > book equity — over-leveraged valuation snapshot."""
    flag = (debt > equity).astype(float)
    return flag.where(~(debt.isna() | equity.isna()), np.nan)


# -------- Block H (first 4): Composite z-scores (072-075) --------

def f15_vesp_072_composite_z_pe_ps_pb_evebitda_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Average of 252d z-scores of PE, PS, PB, EV/EBITDA — composite stretch."""
    z = (_rolling_zscore(pe, YDAYS) + _rolling_zscore(ps, YDAYS) +
         _rolling_zscore(pb, YDAYS) + _rolling_zscore(evebitda, YDAYS)) / 4.0
    return z


def f15_vesp_073_composite_z_pe_ps_pb_evebitda_1260d(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5y composite z of PE/PS/PB/EV-EBITDA — secular stretch composite."""
    z = (_rolling_zscore(pe, 1260) + _rolling_zscore(ps, 1260) +
         _rolling_zscore(pb, 1260) + _rolling_zscore(evebitda, 1260)) / 4.0
    return z


def f15_vesp_074_composite_z_ev_multiples_504d(evebitda: pd.Series, evebit: pd.Series, evsales: pd.Series) -> pd.Series:
    """504d composite z of EV/EBITDA, EV/EBIT, EV/Sales — EV-side composite."""
    z = (_rolling_zscore(evebitda, 504) + _rolling_zscore(evebit, 504) +
         _rolling_zscore(evsales, 504)) / 3.0
    return z


def f15_vesp_075_composite_z_equity_multiples_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series) -> pd.Series:
    """252d composite z of equity multiples PE/PS/PB."""
    z = (_rolling_zscore(pe, YDAYS) + _rolling_zscore(ps, YDAYS) + _rolling_zscore(pb, YDAYS)) / 3.0
    return z


# ============================================================
#                        REGISTRY
# ============================================================

VALUATION_EXTREME_SNAPSHOT_BASE_REGISTRY_001_075 = {
    "f15_vesp_001_pe_level_raw": {"inputs": ["pe"], "func": f15_vesp_001_pe_level_raw},
    "f15_vesp_002_log_pe_level": {"inputs": ["pe"], "func": f15_vesp_002_log_pe_level},
    "f15_vesp_003_ps_level_raw": {"inputs": ["ps"], "func": f15_vesp_003_ps_level_raw},
    "f15_vesp_004_log_ps_level": {"inputs": ["ps"], "func": f15_vesp_004_log_ps_level},
    "f15_vesp_005_pb_level_raw": {"inputs": ["pb"], "func": f15_vesp_005_pb_level_raw},
    "f15_vesp_006_log_pb_level": {"inputs": ["pb"], "func": f15_vesp_006_log_pb_level},
    "f15_vesp_007_evebitda_level": {"inputs": ["evebitda"], "func": f15_vesp_007_evebitda_level},
    "f15_vesp_008_log_evebitda_level": {"inputs": ["evebitda"], "func": f15_vesp_008_log_evebitda_level},
    "f15_vesp_009_evebit_level": {"inputs": ["evebit"], "func": f15_vesp_009_evebit_level},
    "f15_vesp_010_evsales_level": {"inputs": ["evsales"], "func": f15_vesp_010_evsales_level},
    "f15_vesp_011_ev_to_fcf": {"inputs": ["ev", "fcf"], "func": f15_vesp_011_ev_to_fcf},
    "f15_vesp_012_ev_to_cfo": {"inputs": ["ev", "ncfo"], "func": f15_vesp_012_ev_to_cfo},
    "f15_vesp_013_mcap_to_tangibles": {"inputs": ["marketcap", "tangibles"], "func": f15_vesp_013_mcap_to_tangibles},
    "f15_vesp_014_mcap_to_retearn": {"inputs": ["marketcap", "retearn"], "func": f15_vesp_014_mcap_to_retearn},
    "f15_vesp_015_fcfp_inverse": {"inputs": ["fcfp"], "func": f15_vesp_015_fcfp_inverse},
    "f15_vesp_016_earnings_yield": {"inputs": ["pe"], "func": f15_vesp_016_earnings_yield},
    "f15_vesp_017_fcf_yield_level": {"inputs": ["fcfp"], "func": f15_vesp_017_fcf_yield_level},
    "f15_vesp_018_cfo_yield": {"inputs": ["ncfo", "marketcap"], "func": f15_vesp_018_cfo_yield},
    "f15_vesp_019_sales_yield": {"inputs": ["revenue", "marketcap"], "func": f15_vesp_019_sales_yield},
    "f15_vesp_020_ebitda_yield": {"inputs": ["ebitda", "ev"], "func": f15_vesp_020_ebitda_yield},
    "f15_vesp_021_ebit_yield": {"inputs": ["ebit", "ev"], "func": f15_vesp_021_ebit_yield},
    "f15_vesp_022_book_yield": {"inputs": ["equity", "marketcap"], "func": f15_vesp_022_book_yield},
    "f15_vesp_023_dividend_yield_level": {"inputs": ["divyield"], "func": f15_vesp_023_dividend_yield_level},
    "f15_vesp_024_pe_to_revenue_growth": {"inputs": ["pe", "revenue"], "func": f15_vesp_024_pe_to_revenue_growth},
    "f15_vesp_025_ps_to_revenue_growth": {"inputs": ["ps", "revenue"], "func": f15_vesp_025_ps_to_revenue_growth},
    "f15_vesp_026_evebitda_to_ebitda_growth": {"inputs": ["evebitda", "ebitda"], "func": f15_vesp_026_evebitda_to_ebitda_growth},
    "f15_vesp_027_evsales_to_revenue_growth": {"inputs": ["evsales", "revenue"], "func": f15_vesp_027_evsales_to_revenue_growth},
    "f15_vesp_028_pe_to_earnings_growth": {"inputs": ["pe", "netinc"], "func": f15_vesp_028_pe_to_earnings_growth},
    "f15_vesp_029_pb_to_equity_growth": {"inputs": ["pb", "equity"], "func": f15_vesp_029_pb_to_equity_growth},
    "f15_vesp_030_ps_to_revenue_growth_63d": {"inputs": ["ps", "revenue"], "func": f15_vesp_030_ps_to_revenue_growth_63d},
    "f15_vesp_031_pe_to_eps_growth": {"inputs": ["pe", "eps"], "func": f15_vesp_031_pe_to_eps_growth},
    "f15_vesp_032_evebit_to_ebit_growth": {"inputs": ["evebit", "ebit"], "func": f15_vesp_032_evebit_to_ebit_growth},
    "f15_vesp_033_ev_to_fcf_growth": {"inputs": ["ev", "fcf"], "func": f15_vesp_033_ev_to_fcf_growth},
    "f15_vesp_034_pe_zscore_252d": {"inputs": ["pe"], "func": f15_vesp_034_pe_zscore_252d},
    "f15_vesp_035_pe_zscore_504d": {"inputs": ["pe"], "func": f15_vesp_035_pe_zscore_504d},
    "f15_vesp_036_pe_zscore_1260d": {"inputs": ["pe"], "func": f15_vesp_036_pe_zscore_1260d},
    "f15_vesp_037_ps_zscore_252d": {"inputs": ["ps"], "func": f15_vesp_037_ps_zscore_252d},
    "f15_vesp_038_ps_zscore_504d": {"inputs": ["ps"], "func": f15_vesp_038_ps_zscore_504d},
    "f15_vesp_039_ps_zscore_1260d": {"inputs": ["ps"], "func": f15_vesp_039_ps_zscore_1260d},
    "f15_vesp_040_evebitda_zscore_252d": {"inputs": ["evebitda"], "func": f15_vesp_040_evebitda_zscore_252d},
    "f15_vesp_041_evebitda_zscore_504d": {"inputs": ["evebitda"], "func": f15_vesp_041_evebitda_zscore_504d},
    "f15_vesp_042_evebitda_zscore_1260d": {"inputs": ["evebitda"], "func": f15_vesp_042_evebitda_zscore_1260d},
    "f15_vesp_043_pb_zscore_252d": {"inputs": ["pb"], "func": f15_vesp_043_pb_zscore_252d},
    "f15_vesp_044_pb_zscore_1260d": {"inputs": ["pb"], "func": f15_vesp_044_pb_zscore_1260d},
    "f15_vesp_045_evsales_zscore_504d": {"inputs": ["evsales"], "func": f15_vesp_045_evsales_zscore_504d},
    "f15_vesp_046_pe_over_252d_mean": {"inputs": ["pe"], "func": f15_vesp_046_pe_over_252d_mean},
    "f15_vesp_047_pe_over_252d_median": {"inputs": ["pe"], "func": f15_vesp_047_pe_over_252d_median},
    "f15_vesp_048_pe_over_1260d_max": {"inputs": ["pe"], "func": f15_vesp_048_pe_over_1260d_max},
    "f15_vesp_049_pe_over_252d_p90": {"inputs": ["pe"], "func": f15_vesp_049_pe_over_252d_p90},
    "f15_vesp_050_ps_over_252d_mean": {"inputs": ["ps"], "func": f15_vesp_050_ps_over_252d_mean},
    "f15_vesp_051_ps_over_1260d_max": {"inputs": ["ps"], "func": f15_vesp_051_ps_over_1260d_max},
    "f15_vesp_052_evebitda_over_504d_mean": {"inputs": ["evebitda"], "func": f15_vesp_052_evebitda_over_504d_mean},
    "f15_vesp_053_evebitda_over_1260d_p90": {"inputs": ["evebitda"], "func": f15_vesp_053_evebitda_over_1260d_p90},
    "f15_vesp_054_pb_over_1260d_median": {"inputs": ["pb"], "func": f15_vesp_054_pb_over_1260d_median},
    "f15_vesp_055_evsales_over_1260d_max": {"inputs": ["evsales"], "func": f15_vesp_055_evsales_over_1260d_max},
    "f15_vesp_056_ev_to_invested_capital": {"inputs": ["ev", "equity", "debt"], "func": f15_vesp_056_ev_to_invested_capital},
    "f15_vesp_057_ev_to_equity_plus_debtnc": {"inputs": ["ev", "equity", "debtnc"], "func": f15_vesp_057_ev_to_equity_plus_debtnc},
    "f15_vesp_058_ev_to_tangible_ic": {"inputs": ["ev", "tangibles", "debt"], "func": f15_vesp_058_ev_to_tangible_ic},
    "f15_vesp_059_ev_to_assets": {"inputs": ["ev", "assets"], "func": f15_vesp_059_ev_to_assets},
    "f15_vesp_060_ev_to_equity_only": {"inputs": ["ev", "equity"], "func": f15_vesp_060_ev_to_equity_only},
    "f15_vesp_061_ev_to_tangibles_only": {"inputs": ["ev", "tangibles"], "func": f15_vesp_061_ev_to_tangibles_only},
    "f15_vesp_062_ev_minus_cash_to_ic": {"inputs": ["ev", "cashneq", "equity", "debt"], "func": f15_vesp_062_ev_minus_cash_to_ic},
    "f15_vesp_063_ev_to_equity_plus_debtc": {"inputs": ["ev", "equity", "debtc"], "func": f15_vesp_063_ev_to_equity_plus_debtc},
    "f15_vesp_064_loss_making_bubble_flag": {"inputs": ["pe", "netinc"], "func": f15_vesp_064_loss_making_bubble_flag},
    "f15_vesp_065_negative_fcf_high_evsales_flag": {"inputs": ["fcf", "evsales"], "func": f15_vesp_065_negative_fcf_high_evsales_flag},
    "f15_vesp_066_negative_ebitda_high_mcap_flag": {"inputs": ["ebitda", "marketcap"], "func": f15_vesp_066_negative_ebitda_high_mcap_flag},
    "f15_vesp_067_negative_retearn_with_premium_flag": {"inputs": ["retearn", "marketcap", "equity"], "func": f15_vesp_067_negative_retearn_with_premium_flag},
    "f15_vesp_068_negative_netinc_persistent_count_4q": {"inputs": ["netinc"], "func": f15_vesp_068_negative_netinc_persistent_count_4q},
    "f15_vesp_069_negative_fcf_persistent_count_4q": {"inputs": ["fcf"], "func": f15_vesp_069_negative_fcf_persistent_count_4q},
    "f15_vesp_070_intangible_dominance_flag": {"inputs": ["intangibles", "assets"], "func": f15_vesp_070_intangible_dominance_flag},
    "f15_vesp_071_debt_exceeds_equity_flag": {"inputs": ["debt", "equity"], "func": f15_vesp_071_debt_exceeds_equity_flag},
    "f15_vesp_072_composite_z_pe_ps_pb_evebitda_252d": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_072_composite_z_pe_ps_pb_evebitda_252d},
    "f15_vesp_073_composite_z_pe_ps_pb_evebitda_1260d": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_073_composite_z_pe_ps_pb_evebitda_1260d},
    "f15_vesp_074_composite_z_ev_multiples_504d": {"inputs": ["evebitda", "evebit", "evsales"], "func": f15_vesp_074_composite_z_ev_multiples_504d},
    "f15_vesp_075_composite_z_equity_multiples_252d": {"inputs": ["pe", "ps", "pb"], "func": f15_vesp_075_composite_z_equity_multiples_252d},
}
