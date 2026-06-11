"""valuation_extreme_snapshot base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of the 150 distinct hypotheses from __base__001_075.py. PIT-clean.
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
#                    FEATURES 076-150
# ============================================================

# -------- Block H continued: Composite z-scores (076-081) --------

def f15_vesp_076_composite_z_pe_evebitda_1260d(pe: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5y composite z of PE and EV/EBITDA — earnings-multiple consensus stretch."""
    return (_rolling_zscore(pe, 1260) + _rolling_zscore(evebitda, 1260)) / 2.0


def f15_vesp_077_composite_z_ps_evsales_504d(ps: pd.Series, evsales: pd.Series) -> pd.Series:
    """504d composite z of PS and EV/Sales — sales-multiple stretch."""
    return (_rolling_zscore(ps, 504) + _rolling_zscore(evsales, 504)) / 2.0


def f15_vesp_078_composite_z_pb_mcap_tangibles_1260d(pb: pd.Series, marketcap: pd.Series, tangibles: pd.Series) -> pd.Series:
    """5y composite z of PB and mcap/tangibles — book-multiple consensus stretch."""
    mt = _safe_div(marketcap, tangibles)
    return (_rolling_zscore(pb, 1260) + _rolling_zscore(mt, 1260)) / 2.0


def f15_vesp_079_max_z_across_multiples_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Max of 252d z-scores across multiples — worst-extreme detector."""
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS),
                    _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS)], axis=1)
    return df.max(axis=1)


def f15_vesp_080_min_z_across_multiples_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Min of 252d z-scores across multiples — divergence-anchor."""
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS),
                    _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS)], axis=1)
    return df.min(axis=1)


def f15_vesp_081_count_multiples_above_z2_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Count of multiples whose 252d z > 2 — multi-axis bubble detector."""
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS),
                    _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS)], axis=1)
    return (df > 2.0).sum(axis=1).astype(float)


# -------- Block I: Bubble heuristic flags (082-091) --------

def f15_vesp_082_mcap_gt_10x_revenue_flag(marketcap: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 when marketcap > 10x trailing revenue — sales-bubble flag."""
    flag = (marketcap > 10.0 * revenue).astype(float)
    return flag.where(~(marketcap.isna() | revenue.isna()), np.nan)


def f15_vesp_083_mcap_gt_5x_book_flag(marketcap: pd.Series, equity: pd.Series) -> pd.Series:
    """1 when marketcap > 5x book equity — book-bubble flag."""
    flag = (marketcap > 5.0 * equity).astype(float)
    return flag.where(~(marketcap.isna() | equity.isna()), np.nan)


def f15_vesp_084_evsales_gt_20_flag(evsales: pd.Series) -> pd.Series:
    """1 when EV/Sales > 20 — extreme sales-multiple bubble flag."""
    flag = (evsales > 20.0).astype(float)
    return flag.where(~evsales.isna(), np.nan)


def f15_vesp_085_evebitda_gt_50_flag(evebitda: pd.Series) -> pd.Series:
    """1 when EV/EBITDA > 50 — extreme earnings-multiple bubble flag."""
    flag = (evebitda > 50.0).astype(float)
    return flag.where(~evebitda.isna(), np.nan)


def f15_vesp_086_pe_gt_100_flag(pe: pd.Series) -> pd.Series:
    """1 when PE > 100 — bubble PE flag."""
    flag = (pe > 100.0).astype(float)
    return flag.where(~pe.isna(), np.nan)


def f15_vesp_087_ps_gt_15_flag(ps: pd.Series) -> pd.Series:
    """1 when PS > 15 — bubble PS flag."""
    flag = (ps > 15.0).astype(float)
    return flag.where(~ps.isna(), np.nan)


def f15_vesp_088_pb_gt_10_flag(pb: pd.Series) -> pd.Series:
    """1 when PB > 10 — bubble PB flag."""
    flag = (pb > 10.0).astype(float)
    return flag.where(~pb.isna(), np.nan)


def f15_vesp_089_mcap_gt_20x_fcf_flag(marketcap: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 when marketcap > 20x positive trailing FCF — extreme FCF multiple."""
    flag = ((fcf > 0) & (marketcap > 20.0 * fcf)).astype(float)
    return flag.where(~(marketcap.isna() | fcf.isna()), np.nan)


def f15_vesp_090_evebit_gt_40_flag(evebit: pd.Series) -> pd.Series:
    """1 when EV/EBIT > 40 — bubble EBIT multiple flag."""
    flag = (evebit > 40.0).astype(float)
    return flag.where(~evebit.isna(), np.nan)


def f15_vesp_091_bubble_count_total(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series, evsales: pd.Series) -> pd.Series:
    """Number of bubble thresholds breached across PE/PS/PB/EV-EBITDA/EV-Sales."""
    c = ((pe > 100.0).astype(float) + (ps > 15.0).astype(float) +
         (pb > 10.0).astype(float) + (evebitda > 50.0).astype(float) +
         (evsales > 20.0).astype(float))
    return c


# -------- Block J: Per-share growth-vs-price divergence (092-099) --------

def f15_vesp_092_bvps_growth_minus_price_growth_252d(equity: pd.Series, shareswa: pd.Series, marketcap: pd.Series) -> pd.Series:
    """YoY growth(bvps) - YoY growth(price-implied = mcap/shares) — book-vs-price divergence."""
    bvps = _safe_div(equity, shareswa)
    pps = _safe_div(marketcap, shareswa)
    return bvps.pct_change(YDAYS) - pps.pct_change(YDAYS)


def f15_vesp_093_eps_yield(eps: pd.Series, marketcap: pd.Series, shareswa: pd.Series) -> pd.Series:
    """EPS / price-per-share — per-share earnings yield."""
    pps = _safe_div(marketcap, shareswa)
    return _safe_div(eps, pps)


def f15_vesp_094_eps_growth_minus_price_growth_252d(eps: pd.Series, marketcap: pd.Series, shareswa: pd.Series) -> pd.Series:
    """YoY EPS growth minus YoY price-per-share growth — earnings-vs-price divergence."""
    pps = _safe_div(marketcap, shareswa)
    return eps.pct_change(YDAYS) - pps.pct_change(YDAYS)


def f15_vesp_095_bvps_minus_eps_growth_252d(equity: pd.Series, shareswa: pd.Series, eps: pd.Series) -> pd.Series:
    """YoY bvps growth minus YoY EPS growth — book-vs-earnings growth gap."""
    bvps = _safe_div(equity, shareswa)
    return bvps.pct_change(YDAYS) - eps.pct_change(YDAYS)


def f15_vesp_096_eps_to_epsdil_gap(eps: pd.Series, epsdil: pd.Series) -> pd.Series:
    """eps - epsdil — dilution drag on per-share earnings."""
    return eps - epsdil


def f15_vesp_097_pps_growth_252d(marketcap: pd.Series, shareswa: pd.Series) -> pd.Series:
    """YoY growth in implied price per share = marketcap / shareswa."""
    pps = _safe_div(marketcap, shareswa)
    return pps.pct_change(YDAYS)


def f15_vesp_098_bvps_level(equity: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Book value per share level."""
    return _safe_div(equity, shareswa)


def f15_vesp_099_eps_yield_dilution_adjusted(epsdil: pd.Series, marketcap: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Diluted EPS / diluted price-per-share — dilution-aware earnings yield."""
    pps_d = _safe_div(marketcap, shareswadil)
    return _safe_div(epsdil, pps_d)


# -------- Block K: Marketcap-to-balance-sheet ratios (100-109) --------

def f15_vesp_100_mcap_to_cashneq(marketcap: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Marketcap divided by cash-and-equivalents — premium over cash hoard."""
    return _safe_div(marketcap, cashneq)


def f15_vesp_101_mcap_to_assets(marketcap: pd.Series, assets: pd.Series) -> pd.Series:
    """Marketcap divided by total assets — premium per asset dollar."""
    return _safe_div(marketcap, assets)


def f15_vesp_102_mcap_to_equity(marketcap: pd.Series, equity: pd.Series) -> pd.Series:
    """Marketcap divided by equity — alternative PB definition."""
    return _safe_div(marketcap, equity)


def f15_vesp_103_mcap_to_tangible_book(marketcap: pd.Series, tangibles: pd.Series) -> pd.Series:
    """Marketcap divided by tangible book — premium over hard book."""
    return _safe_div(marketcap, tangibles)


def f15_vesp_104_mcap_minus_cash_to_equity(marketcap: pd.Series, cashneq: pd.Series, equity: pd.Series) -> pd.Series:
    """(Marketcap - cash) / equity — net-of-cash equity multiple."""
    return _safe_div(marketcap - cashneq.fillna(0), equity)


def f15_vesp_105_mcap_to_debt(marketcap: pd.Series, debt: pd.Series) -> pd.Series:
    """Marketcap divided by total debt — equity cushion vs leverage."""
    return _safe_div(marketcap, debt)


def f15_vesp_106_mcap_to_retained_earnings(marketcap: pd.Series, retearn: pd.Series) -> pd.Series:
    """Marketcap divided by retained earnings — premium over lifetime profits."""
    return _safe_div(marketcap, retearn)


def f15_vesp_107_mcap_to_capex(marketcap: pd.Series, capex: pd.Series) -> pd.Series:
    """Marketcap divided by absolute trailing capex — capacity-relative valuation."""
    return _safe_div(marketcap, capex.abs())


def f15_vesp_108_mcap_to_sbcomp(marketcap: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """Marketcap divided by stock-based-comp — comp-funded valuation premium."""
    return _safe_div(marketcap, sbcomp)


def f15_vesp_109_mcap_to_gp(marketcap: pd.Series, gp: pd.Series) -> pd.Series:
    """Marketcap divided by gross profit — quality-adjusted earnings multiple."""
    return _safe_div(marketcap, gp)


# -------- Block L: Dilution-adjusted multiples (110-115) --------

def f15_vesp_110_dilution_adjusted_pe(pe: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """PE scaled by (shareswadil / shareswa) — fully-diluted PE."""
    factor = _safe_div(shareswadil, shareswa)
    return pe * factor


def f15_vesp_111_dilution_adjusted_ps(ps: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """PS scaled by diluted share factor."""
    factor = _safe_div(shareswadil, shareswa)
    return ps * factor


def f15_vesp_112_dilution_adjusted_pb(pb: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """PB scaled by diluted share factor."""
    factor = _safe_div(shareswadil, shareswa)
    return pb * factor


def f15_vesp_113_dilution_adjusted_evsales(evsales: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """EV/Sales scaled by diluted share factor."""
    factor = _safe_div(shareswadil, shareswa)
    return evsales * factor


def f15_vesp_114_dilution_factor_level(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Raw dilution factor = shareswadil / shareswa — overhang severity."""
    return _safe_div(shareswadil, shareswa)


def f15_vesp_115_dilution_overhang_minus_one(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """(shareswadil / shareswa) - 1 — fraction overhang in pure terms."""
    return _safe_div(shareswadil, shareswa) - 1.0


# -------- Block M: Stretched-multiple persistence (116-123) --------

def f15_vesp_116_pe_frac_above_p80_252d(pe: pd.Series) -> pd.Series:
    """Fraction of last 252 days with PE above its own 252d 80th percentile — persistent stretch."""
    q = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    return (pe > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_117_ps_frac_above_p80_252d(ps: pd.Series) -> pd.Series:
    """Fraction of last 252d with PS above own 252d p80 — persistent PS stretch."""
    q = ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    return (ps > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_118_pb_frac_above_p80_252d(pb: pd.Series) -> pd.Series:
    """Fraction of last 252d with PB above own 252d p80."""
    q = pb.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    return (pb > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_119_evebitda_frac_above_p80_252d(evebitda: pd.Series) -> pd.Series:
    """Fraction of last 252d with EV/EBITDA above own 252d p80."""
    q = evebitda.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    return (evebitda > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_120_pe_frac_above_p80_1260d(pe: pd.Series) -> pd.Series:
    """Fraction of last 252d with PE above 5y p80 — secular persistent stretch."""
    q = pe.rolling(1260, min_periods=YDAYS).quantile(0.80)
    return (pe > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_121_ps_frac_above_p80_1260d(ps: pd.Series) -> pd.Series:
    """Fraction of last 252d with PS above 5y p80."""
    q = ps.rolling(1260, min_periods=YDAYS).quantile(0.80)
    return (ps > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_122_evsales_frac_above_p80_1260d(evsales: pd.Series) -> pd.Series:
    """Fraction of last 252d with EV/Sales above 5y p80."""
    q = evsales.rolling(1260, min_periods=YDAYS).quantile(0.80)
    return (evsales > q).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()


def f15_vesp_123_composite_persistence_above_p80(pe: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Avg fraction-above-p80(252d) across PE / PS / EV-EBITDA — composite stretch persistence."""
    qe = pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    qs = ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    qb = evebitda.rolling(YDAYS, min_periods=QDAYS).quantile(0.80)
    return ((pe > qe).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() +
            (ps > qs).astype(float).rolling(YDAYS, min_periods=QDAYS).mean() +
            (evebitda > qb).astype(float).rolling(YDAYS, min_periods=QDAYS).mean()) / 3.0


# -------- Block N: Multiple-to-fundamental divergence (124-131) --------

def f15_vesp_124_pe_change_minus_earnings_change_252d(pe: pd.Series, netinc: pd.Series) -> pd.Series:
    """YoY change in PE minus YoY change in netinc — multiple expansion despite flat earnings."""
    return pe.pct_change(YDAYS) - netinc.pct_change(YDAYS)


def f15_vesp_125_ps_change_minus_revenue_change_252d(ps: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in PS minus YoY change in revenue — sales-multiple inflation without growth."""
    return ps.pct_change(YDAYS) - revenue.pct_change(YDAYS)


def f15_vesp_126_evebitda_change_minus_ebitda_change_252d(evebitda: pd.Series, ebitda: pd.Series) -> pd.Series:
    """YoY change in EV/EBITDA minus YoY change in EBITDA — multiple re-rate vs fundamentals."""
    return evebitda.pct_change(YDAYS) - ebitda.pct_change(YDAYS)


def f15_vesp_127_pb_change_minus_equity_change_252d(pb: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in PB minus YoY change in equity — book-multiple stretch."""
    return pb.pct_change(YDAYS) - equity.pct_change(YDAYS)


def f15_vesp_128_evsales_change_minus_revenue_change_252d(evsales: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in EV/Sales minus YoY change in revenue."""
    return evsales.pct_change(YDAYS) - revenue.pct_change(YDAYS)


def f15_vesp_129_mcap_change_minus_book_change_252d(marketcap: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY mcap change minus YoY equity change — premium-creation divergence."""
    return marketcap.pct_change(YDAYS) - equity.pct_change(YDAYS)


def f15_vesp_130_mcap_change_minus_fcf_change_252d(marketcap: pd.Series, fcf: pd.Series) -> pd.Series:
    """YoY mcap change minus YoY FCF change — price vs free-cash-flow divergence."""
    return marketcap.pct_change(YDAYS) - fcf.pct_change(YDAYS)


def f15_vesp_131_mcap_change_minus_revenue_change_504d(marketcap: pd.Series, revenue: pd.Series) -> pd.Series:
    """504d mcap change minus 504d revenue change — biennial price-vs-sales divergence."""
    return marketcap.pct_change(504) - revenue.pct_change(504)


# -------- Block O: Valuation-to-growth-quality (132-137) --------

def f15_vesp_132_ps_over_gm_times_rev_growth(ps: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """PS divided by (gross_margin * revenue growth) — quality-adjusted sales multiple."""
    gm = _safe_div(gp, revenue)
    rg = revenue.pct_change(YDAYS)
    return _safe_div(ps, gm * rg)


def f15_vesp_133_evsales_over_gm_times_rev_growth(evsales: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """EV/Sales over (gross_margin * revenue growth) — capital-adjusted quality-PEG."""
    gm = _safe_div(gp, revenue)
    rg = revenue.pct_change(YDAYS)
    return _safe_div(evsales, gm * rg)


def f15_vesp_134_pe_over_eps_growth_times_roa(pe: pd.Series, eps: pd.Series, netinc: pd.Series, assets: pd.Series) -> pd.Series:
    """PE divided by (EPS growth * ROA) — quality-PEG using asset returns."""
    eg = eps.pct_change(YDAYS)
    roa = _safe_div(netinc, assets)
    return _safe_div(pe, eg * roa)


def f15_vesp_135_evebitda_over_ebitda_margin(evebitda: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EV/EBITDA divided by EBITDA margin — paying-up for margin."""
    margin = _safe_div(ebitda, revenue)
    return _safe_div(evebitda, margin)


def f15_vesp_136_pb_over_roe(pb: pd.Series, netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """PB divided by ROE — premium per unit of book return."""
    roe = _safe_div(netinc, equity)
    return _safe_div(pb, roe)


def f15_vesp_137_ps_over_ebitda_margin(ps: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """PS divided by EBITDA margin — paying-up for margin (equity version)."""
    margin = _safe_div(ebitda, revenue)
    return _safe_div(ps, margin)


# -------- Block P: Distance to historical percentile 50/90/99 (138-145) --------

def f15_vesp_138_pe_distance_to_p50_252d(pe: pd.Series) -> pd.Series:
    """PE minus its trailing 252d median — additive distance to historical centre."""
    return pe - pe.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)


def f15_vesp_139_pe_distance_to_p90_1260d(pe: pd.Series) -> pd.Series:
    """PE minus trailing 5y 90th percentile — distance to upper tail."""
    return pe - pe.rolling(1260, min_periods=YDAYS).quantile(0.90)


def f15_vesp_140_pe_distance_to_p99_1260d(pe: pd.Series) -> pd.Series:
    """PE minus trailing 5y 99th percentile — distance to extreme tail."""
    return pe - pe.rolling(1260, min_periods=YDAYS).quantile(0.99)


def f15_vesp_141_ps_distance_to_p50_252d(ps: pd.Series) -> pd.Series:
    """PS minus trailing 252d median PS."""
    return ps - ps.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)


def f15_vesp_142_ps_distance_to_p90_1260d(ps: pd.Series) -> pd.Series:
    """PS minus trailing 5y 90th percentile PS."""
    return ps - ps.rolling(1260, min_periods=YDAYS).quantile(0.90)


def f15_vesp_143_evebitda_distance_to_p90_1260d(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA minus trailing 5y 90th percentile."""
    return evebitda - evebitda.rolling(1260, min_periods=YDAYS).quantile(0.90)


def f15_vesp_144_pb_distance_to_p90_1260d(pb: pd.Series) -> pd.Series:
    """PB minus trailing 5y 90th percentile PB."""
    return pb - pb.rolling(1260, min_periods=YDAYS).quantile(0.90)


def f15_vesp_145_evsales_distance_to_p99_1260d(evsales: pd.Series) -> pd.Series:
    """EV/Sales minus trailing 5y 99th percentile."""
    return evsales - evsales.rolling(1260, min_periods=YDAYS).quantile(0.99)


# -------- Block Q: Closing intensity / interaction extras (146-150) --------

def f15_vesp_146_ev_to_revenue_plus_ebitda(ev: pd.Series, revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    """EV / (revenue + ebitda) — blended-numerator capital multiple."""
    return _safe_div(ev, revenue.fillna(0) + ebitda.fillna(0))


def f15_vesp_147_log_mcap_to_cash_minus_debt(marketcap: pd.Series, cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """log(marketcap / (cash - debt)) — premium per net-cash dollar (NaN when net cash <= 0)."""
    net_cash = cashneq.fillna(0) - debt.fillna(0)
    return _safe_log(_safe_div(marketcap, net_cash))


def f15_vesp_148_extreme_breadth_252d(pe: pd.Series, ps: pd.Series, pb: pd.Series, evebitda: pd.Series, evsales: pd.Series) -> pd.Series:
    """Mean of (1 if z > 1 else 0) across 5 multiples on 252d — breadth of multi-axis stretch."""
    df = pd.concat([_rolling_zscore(pe, YDAYS), _rolling_zscore(ps, YDAYS),
                    _rolling_zscore(pb, YDAYS), _rolling_zscore(evebitda, YDAYS),
                    _rolling_zscore(evsales, YDAYS)], axis=1)
    return (df > 1.0).astype(float).mean(axis=1)


def f15_vesp_149_valuation_to_quality_index(ps: pd.Series, pb: pd.Series, netinc: pd.Series, equity: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """(PS + PB) / (ROE + EBITDA-margin) — multi-axis valuation-over-quality."""
    roe = _safe_div(netinc, equity)
    margin = _safe_div(ebitda, revenue)
    return _safe_div(ps.fillna(0) + pb.fillna(0), roe.fillna(0) + margin.fillna(0))


def f15_vesp_150_log_extreme_intensity(pe: pd.Series, ps: pd.Series, evsales: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Sum of logs of four core multiples — additive bubble intensity."""
    return _safe_log(pe) + _safe_log(ps) + _safe_log(evsales) + _safe_log(evebitda)


# ============================================================
#                        REGISTRY
# ============================================================

VALUATION_EXTREME_SNAPSHOT_BASE_REGISTRY_076_150 = {
    "f15_vesp_076_composite_z_pe_evebitda_1260d": {"inputs": ["pe", "evebitda"], "func": f15_vesp_076_composite_z_pe_evebitda_1260d},
    "f15_vesp_077_composite_z_ps_evsales_504d": {"inputs": ["ps", "evsales"], "func": f15_vesp_077_composite_z_ps_evsales_504d},
    "f15_vesp_078_composite_z_pb_mcap_tangibles_1260d": {"inputs": ["pb", "marketcap", "tangibles"], "func": f15_vesp_078_composite_z_pb_mcap_tangibles_1260d},
    "f15_vesp_079_max_z_across_multiples_252d": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_079_max_z_across_multiples_252d},
    "f15_vesp_080_min_z_across_multiples_252d": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_080_min_z_across_multiples_252d},
    "f15_vesp_081_count_multiples_above_z2_252d": {"inputs": ["pe", "ps", "pb", "evebitda"], "func": f15_vesp_081_count_multiples_above_z2_252d},
    "f15_vesp_082_mcap_gt_10x_revenue_flag": {"inputs": ["marketcap", "revenue"], "func": f15_vesp_082_mcap_gt_10x_revenue_flag},
    "f15_vesp_083_mcap_gt_5x_book_flag": {"inputs": ["marketcap", "equity"], "func": f15_vesp_083_mcap_gt_5x_book_flag},
    "f15_vesp_084_evsales_gt_20_flag": {"inputs": ["evsales"], "func": f15_vesp_084_evsales_gt_20_flag},
    "f15_vesp_085_evebitda_gt_50_flag": {"inputs": ["evebitda"], "func": f15_vesp_085_evebitda_gt_50_flag},
    "f15_vesp_086_pe_gt_100_flag": {"inputs": ["pe"], "func": f15_vesp_086_pe_gt_100_flag},
    "f15_vesp_087_ps_gt_15_flag": {"inputs": ["ps"], "func": f15_vesp_087_ps_gt_15_flag},
    "f15_vesp_088_pb_gt_10_flag": {"inputs": ["pb"], "func": f15_vesp_088_pb_gt_10_flag},
    "f15_vesp_089_mcap_gt_20x_fcf_flag": {"inputs": ["marketcap", "fcf"], "func": f15_vesp_089_mcap_gt_20x_fcf_flag},
    "f15_vesp_090_evebit_gt_40_flag": {"inputs": ["evebit"], "func": f15_vesp_090_evebit_gt_40_flag},
    "f15_vesp_091_bubble_count_total": {"inputs": ["pe", "ps", "pb", "evebitda", "evsales"], "func": f15_vesp_091_bubble_count_total},
    "f15_vesp_092_bvps_growth_minus_price_growth_252d": {"inputs": ["equity", "shareswa", "marketcap"], "func": f15_vesp_092_bvps_growth_minus_price_growth_252d},
    "f15_vesp_093_eps_yield": {"inputs": ["eps", "marketcap", "shareswa"], "func": f15_vesp_093_eps_yield},
    "f15_vesp_094_eps_growth_minus_price_growth_252d": {"inputs": ["eps", "marketcap", "shareswa"], "func": f15_vesp_094_eps_growth_minus_price_growth_252d},
    "f15_vesp_095_bvps_minus_eps_growth_252d": {"inputs": ["equity", "shareswa", "eps"], "func": f15_vesp_095_bvps_minus_eps_growth_252d},
    "f15_vesp_096_eps_to_epsdil_gap": {"inputs": ["eps", "epsdil"], "func": f15_vesp_096_eps_to_epsdil_gap},
    "f15_vesp_097_pps_growth_252d": {"inputs": ["marketcap", "shareswa"], "func": f15_vesp_097_pps_growth_252d},
    "f15_vesp_098_bvps_level": {"inputs": ["equity", "shareswa"], "func": f15_vesp_098_bvps_level},
    "f15_vesp_099_eps_yield_dilution_adjusted": {"inputs": ["epsdil", "marketcap", "shareswadil"], "func": f15_vesp_099_eps_yield_dilution_adjusted},
    "f15_vesp_100_mcap_to_cashneq": {"inputs": ["marketcap", "cashneq"], "func": f15_vesp_100_mcap_to_cashneq},
    "f15_vesp_101_mcap_to_assets": {"inputs": ["marketcap", "assets"], "func": f15_vesp_101_mcap_to_assets},
    "f15_vesp_102_mcap_to_equity": {"inputs": ["marketcap", "equity"], "func": f15_vesp_102_mcap_to_equity},
    "f15_vesp_103_mcap_to_tangible_book": {"inputs": ["marketcap", "tangibles"], "func": f15_vesp_103_mcap_to_tangible_book},
    "f15_vesp_104_mcap_minus_cash_to_equity": {"inputs": ["marketcap", "cashneq", "equity"], "func": f15_vesp_104_mcap_minus_cash_to_equity},
    "f15_vesp_105_mcap_to_debt": {"inputs": ["marketcap", "debt"], "func": f15_vesp_105_mcap_to_debt},
    "f15_vesp_106_mcap_to_retained_earnings": {"inputs": ["marketcap", "retearn"], "func": f15_vesp_106_mcap_to_retained_earnings},
    "f15_vesp_107_mcap_to_capex": {"inputs": ["marketcap", "capex"], "func": f15_vesp_107_mcap_to_capex},
    "f15_vesp_108_mcap_to_sbcomp": {"inputs": ["marketcap", "sbcomp"], "func": f15_vesp_108_mcap_to_sbcomp},
    "f15_vesp_109_mcap_to_gp": {"inputs": ["marketcap", "gp"], "func": f15_vesp_109_mcap_to_gp},
    "f15_vesp_110_dilution_adjusted_pe": {"inputs": ["pe", "shareswadil", "shareswa"], "func": f15_vesp_110_dilution_adjusted_pe},
    "f15_vesp_111_dilution_adjusted_ps": {"inputs": ["ps", "shareswadil", "shareswa"], "func": f15_vesp_111_dilution_adjusted_ps},
    "f15_vesp_112_dilution_adjusted_pb": {"inputs": ["pb", "shareswadil", "shareswa"], "func": f15_vesp_112_dilution_adjusted_pb},
    "f15_vesp_113_dilution_adjusted_evsales": {"inputs": ["evsales", "shareswadil", "shareswa"], "func": f15_vesp_113_dilution_adjusted_evsales},
    "f15_vesp_114_dilution_factor_level": {"inputs": ["shareswadil", "shareswa"], "func": f15_vesp_114_dilution_factor_level},
    "f15_vesp_115_dilution_overhang_minus_one": {"inputs": ["shareswadil", "shareswa"], "func": f15_vesp_115_dilution_overhang_minus_one},
    "f15_vesp_116_pe_frac_above_p80_252d": {"inputs": ["pe"], "func": f15_vesp_116_pe_frac_above_p80_252d},
    "f15_vesp_117_ps_frac_above_p80_252d": {"inputs": ["ps"], "func": f15_vesp_117_ps_frac_above_p80_252d},
    "f15_vesp_118_pb_frac_above_p80_252d": {"inputs": ["pb"], "func": f15_vesp_118_pb_frac_above_p80_252d},
    "f15_vesp_119_evebitda_frac_above_p80_252d": {"inputs": ["evebitda"], "func": f15_vesp_119_evebitda_frac_above_p80_252d},
    "f15_vesp_120_pe_frac_above_p80_1260d": {"inputs": ["pe"], "func": f15_vesp_120_pe_frac_above_p80_1260d},
    "f15_vesp_121_ps_frac_above_p80_1260d": {"inputs": ["ps"], "func": f15_vesp_121_ps_frac_above_p80_1260d},
    "f15_vesp_122_evsales_frac_above_p80_1260d": {"inputs": ["evsales"], "func": f15_vesp_122_evsales_frac_above_p80_1260d},
    "f15_vesp_123_composite_persistence_above_p80": {"inputs": ["pe", "ps", "evebitda"], "func": f15_vesp_123_composite_persistence_above_p80},
    "f15_vesp_124_pe_change_minus_earnings_change_252d": {"inputs": ["pe", "netinc"], "func": f15_vesp_124_pe_change_minus_earnings_change_252d},
    "f15_vesp_125_ps_change_minus_revenue_change_252d": {"inputs": ["ps", "revenue"], "func": f15_vesp_125_ps_change_minus_revenue_change_252d},
    "f15_vesp_126_evebitda_change_minus_ebitda_change_252d": {"inputs": ["evebitda", "ebitda"], "func": f15_vesp_126_evebitda_change_minus_ebitda_change_252d},
    "f15_vesp_127_pb_change_minus_equity_change_252d": {"inputs": ["pb", "equity"], "func": f15_vesp_127_pb_change_minus_equity_change_252d},
    "f15_vesp_128_evsales_change_minus_revenue_change_252d": {"inputs": ["evsales", "revenue"], "func": f15_vesp_128_evsales_change_minus_revenue_change_252d},
    "f15_vesp_129_mcap_change_minus_book_change_252d": {"inputs": ["marketcap", "equity"], "func": f15_vesp_129_mcap_change_minus_book_change_252d},
    "f15_vesp_130_mcap_change_minus_fcf_change_252d": {"inputs": ["marketcap", "fcf"], "func": f15_vesp_130_mcap_change_minus_fcf_change_252d},
    "f15_vesp_131_mcap_change_minus_revenue_change_504d": {"inputs": ["marketcap", "revenue"], "func": f15_vesp_131_mcap_change_minus_revenue_change_504d},
    "f15_vesp_132_ps_over_gm_times_rev_growth": {"inputs": ["ps", "gp", "revenue"], "func": f15_vesp_132_ps_over_gm_times_rev_growth},
    "f15_vesp_133_evsales_over_gm_times_rev_growth": {"inputs": ["evsales", "gp", "revenue"], "func": f15_vesp_133_evsales_over_gm_times_rev_growth},
    "f15_vesp_134_pe_over_eps_growth_times_roa": {"inputs": ["pe", "eps", "netinc", "assets"], "func": f15_vesp_134_pe_over_eps_growth_times_roa},
    "f15_vesp_135_evebitda_over_ebitda_margin": {"inputs": ["evebitda", "ebitda", "revenue"], "func": f15_vesp_135_evebitda_over_ebitda_margin},
    "f15_vesp_136_pb_over_roe": {"inputs": ["pb", "netinc", "equity"], "func": f15_vesp_136_pb_over_roe},
    "f15_vesp_137_ps_over_ebitda_margin": {"inputs": ["ps", "ebitda", "revenue"], "func": f15_vesp_137_ps_over_ebitda_margin},
    "f15_vesp_138_pe_distance_to_p50_252d": {"inputs": ["pe"], "func": f15_vesp_138_pe_distance_to_p50_252d},
    "f15_vesp_139_pe_distance_to_p90_1260d": {"inputs": ["pe"], "func": f15_vesp_139_pe_distance_to_p90_1260d},
    "f15_vesp_140_pe_distance_to_p99_1260d": {"inputs": ["pe"], "func": f15_vesp_140_pe_distance_to_p99_1260d},
    "f15_vesp_141_ps_distance_to_p50_252d": {"inputs": ["ps"], "func": f15_vesp_141_ps_distance_to_p50_252d},
    "f15_vesp_142_ps_distance_to_p90_1260d": {"inputs": ["ps"], "func": f15_vesp_142_ps_distance_to_p90_1260d},
    "f15_vesp_143_evebitda_distance_to_p90_1260d": {"inputs": ["evebitda"], "func": f15_vesp_143_evebitda_distance_to_p90_1260d},
    "f15_vesp_144_pb_distance_to_p90_1260d": {"inputs": ["pb"], "func": f15_vesp_144_pb_distance_to_p90_1260d},
    "f15_vesp_145_evsales_distance_to_p99_1260d": {"inputs": ["evsales"], "func": f15_vesp_145_evsales_distance_to_p99_1260d},
    "f15_vesp_146_ev_to_revenue_plus_ebitda": {"inputs": ["ev", "revenue", "ebitda"], "func": f15_vesp_146_ev_to_revenue_plus_ebitda},
    "f15_vesp_147_log_mcap_to_cash_minus_debt": {"inputs": ["marketcap", "cashneq", "debt"], "func": f15_vesp_147_log_mcap_to_cash_minus_debt},
    "f15_vesp_148_extreme_breadth_252d": {"inputs": ["pe", "ps", "pb", "evebitda", "evsales"], "func": f15_vesp_148_extreme_breadth_252d},
    "f15_vesp_149_valuation_to_quality_index": {"inputs": ["ps", "pb", "netinc", "equity", "ebitda", "revenue"], "func": f15_vesp_149_valuation_to_quality_index},
    "f15_vesp_150_log_extreme_intensity": {"inputs": ["pe", "ps", "evsales", "evebitda"], "func": f15_vesp_150_log_extreme_intensity},
}
