"""
62_margin_compression — Base Features 001-075
Domain: gross / operating / EBITDA / net / pretax margin erosion
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Target context: capitulation — absolute multi-year low / maximum distress

All inputs are daily-frequency pandas Series, forward-filled from the most
recent quarterly Sharadar SF1 report known as of each date.
Functions look strictly backward. No future information is used.

Quarterly cadence on daily index:
  1 quarter = 63 trading days  (QoQ diff = .diff(63) / .shift(63))
  1 year    = 252 trading days (YoY diff = .diff(252) / .shift(252))
  2 years   = 504 | 3 years = 756 | 5 years = 1260
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_QTR  = 63    # 1 quarter in trading days
_TD_YEAR = 252   # 1 year
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_EPS     = 1e-9

# ── Alignment helper ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Re-index a quarterly SF1 series onto a daily trading-day index and
    forward-fill. Contract: all inputs to feature functions in this file are
    already daily-frequency Series that have been forward-filled from the most
    recent quarterly report. This helper is provided for pipeline use; feature
    functions receive pre-aligned Series and do not call it themselves.
    """
    return q_series.reindex(daily_index).ffill()

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; zero denominator → NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Margin constructors ────────────────────────────────────────────────────────

def _gross_margin(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(gp, revenue)

def _op_margin(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opinc, revenue)

def _ebitda_margin(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ebitda, revenue)

def _net_margin(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(netinc, revenue)

def _pretax_margin(ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ebt, revenue)

def _ebit_margin(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(ebit, revenue)

def _cor_ratio(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(cor, revenue)

def _opex_ratio(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opex, revenue)

def _sgna_ratio(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(sgna, revenue)

def _rnd_ratio(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(rnd, revenue)

def _depamor_ratio(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(depamor, revenue)

def _sbcomp_ratio(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(sbcomp, revenue)

def _intexp_ratio(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(intexp, revenue)

def _taxexp_ratio(taxexp: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(taxexp, revenue)


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-010): Gross margin level and QoQ / YoY change ---

def mgc_001_gross_margin_level(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current gross margin (gp / revenue)."""
    return _gross_margin(gp, revenue)


def mgc_002_gross_margin_qoq_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in gross margin (63-day diff on daily-fwd-filled series)."""
    gm = _gross_margin(gp, revenue)
    return gm.diff(_TD_QTR)


def mgc_003_gross_margin_yoy_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in gross margin (252-day diff)."""
    gm = _gross_margin(gp, revenue)
    return gm.diff(_TD_YEAR)


def mgc_004_gross_margin_2y_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in gross margin (504-day diff)."""
    gm = _gross_margin(gp, revenue)
    return gm.diff(_TD_2Y)


def mgc_005_gross_margin_vs_4q_avg(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus its trailing 4-quarter (252-day) rolling mean."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_mean(gm, _TD_YEAR)


def mgc_006_gross_margin_vs_8q_avg(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus its trailing 8-quarter (504-day) rolling mean."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_mean(gm, _TD_2Y)


def mgc_007_gross_margin_vs_peak_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin vs its trailing 4-quarter peak (drawdown from local peak)."""
    gm = _gross_margin(gp, revenue)
    pk = _rolling_max(gm, _TD_YEAR)
    return gm - pk


def mgc_008_gross_margin_vs_peak_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin vs its trailing 8-quarter peak (drawdown from longer peak)."""
    gm = _gross_margin(gp, revenue)
    pk = _rolling_max(gm, _TD_2Y)
    return gm - pk


def mgc_009_gross_margin_vs_peak_ath(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin vs expanding (all-time) peak — maximum drawdown from best-ever GM."""
    gm = _gross_margin(gp, revenue)
    pk = gm.expanding(min_periods=1).max()
    return gm - pk


def mgc_010_gross_margin_below_4q_min(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus trailing 4-quarter minimum (0 when at new low, positive otherwise)."""
    gm = _gross_margin(gp, revenue)
    mn = _rolling_min(gm, _TD_YEAR)
    return gm - mn


# --- Group B (011-020): Operating margin level and changes ---

def mgc_011_op_margin_level(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current operating margin (opinc / revenue)."""
    return _op_margin(opinc, revenue)


def mgc_012_op_margin_qoq_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in operating margin."""
    om = _op_margin(opinc, revenue)
    return om.diff(_TD_QTR)


def mgc_013_op_margin_yoy_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in operating margin."""
    om = _op_margin(opinc, revenue)
    return om.diff(_TD_YEAR)


def mgc_014_op_margin_2y_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in operating margin."""
    om = _op_margin(opinc, revenue)
    return om.diff(_TD_2Y)


def mgc_015_op_margin_vs_4q_avg(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus trailing 4-quarter mean."""
    om = _op_margin(opinc, revenue)
    return om - _rolling_mean(om, _TD_YEAR)


def mgc_016_op_margin_vs_peak_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin vs trailing 4-quarter peak."""
    om = _op_margin(opinc, revenue)
    pk = _rolling_max(om, _TD_YEAR)
    return om - pk


def mgc_017_op_margin_vs_peak_ath(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin vs all-time peak (maximum operating margin compression)."""
    om = _op_margin(opinc, revenue)
    pk = om.expanding(min_periods=1).max()
    return om - pk


def mgc_018_op_margin_negative_flag(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if operating margin is negative, 0 otherwise."""
    om = _op_margin(opinc, revenue)
    return (om < 0).astype(float)


def mgc_019_op_margin_zscore_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating margin over trailing 4 quarters (252 days)."""
    om = _op_margin(opinc, revenue)
    return _zscore_rolling(om, _TD_YEAR)


def mgc_020_op_margin_zscore_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating margin over trailing 8 quarters (504 days)."""
    om = _op_margin(opinc, revenue)
    return _zscore_rolling(om, _TD_2Y)


# --- Group C (021-030): EBITDA margin level and changes ---

def mgc_021_ebitda_margin_level(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current EBITDA margin (ebitda / revenue)."""
    return _ebitda_margin(ebitda, revenue)


def mgc_022_ebitda_margin_qoq_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in EBITDA margin."""
    em = _ebitda_margin(ebitda, revenue)
    return em.diff(_TD_QTR)


def mgc_023_ebitda_margin_yoy_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in EBITDA margin."""
    em = _ebitda_margin(ebitda, revenue)
    return em.diff(_TD_YEAR)


def mgc_024_ebitda_margin_vs_4q_avg(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin minus trailing 4-quarter mean."""
    em = _ebitda_margin(ebitda, revenue)
    return em - _rolling_mean(em, _TD_YEAR)


def mgc_025_ebitda_margin_vs_peak_4q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin vs trailing 4-quarter peak."""
    em = _ebitda_margin(ebitda, revenue)
    pk = _rolling_max(em, _TD_YEAR)
    return em - pk


def mgc_026_ebitda_margin_vs_peak_ath(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin vs all-time expanding peak."""
    em = _ebitda_margin(ebitda, revenue)
    pk = em.expanding(min_periods=1).max()
    return em - pk


def mgc_027_ebitda_margin_zscore_4q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of EBITDA margin over trailing 4 quarters."""
    em = _ebitda_margin(ebitda, revenue)
    return _zscore_rolling(em, _TD_YEAR)


def mgc_028_ebitda_margin_negative_flag(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if EBITDA margin is negative (EBITDA loss), 0 otherwise."""
    em = _ebitda_margin(ebitda, revenue)
    return (em < 0).astype(float)


def mgc_029_ebitda_margin_2y_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in EBITDA margin."""
    em = _ebitda_margin(ebitda, revenue)
    return em.diff(_TD_2Y)


def mgc_030_ebitda_margin_vs_8q_avg(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin minus trailing 8-quarter mean."""
    em = _ebitda_margin(ebitda, revenue)
    return em - _rolling_mean(em, _TD_2Y)


# --- Group D (031-040): Net and pretax margin ---

def mgc_031_net_margin_level(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current net margin (netinc / revenue)."""
    return _net_margin(netinc, revenue)


def mgc_032_net_margin_qoq_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in net margin."""
    nm = _net_margin(netinc, revenue)
    return nm.diff(_TD_QTR)


def mgc_033_net_margin_yoy_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in net margin."""
    nm = _net_margin(netinc, revenue)
    return nm.diff(_TD_YEAR)


def mgc_034_net_margin_vs_4q_avg(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin minus trailing 4-quarter mean."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_mean(nm, _TD_YEAR)


def mgc_035_net_margin_vs_peak_ath(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin vs all-time expanding peak."""
    nm = _net_margin(netinc, revenue)
    pk = nm.expanding(min_periods=1).max()
    return nm - pk


def mgc_036_net_margin_negative_flag(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if net margin is negative, 0 otherwise."""
    nm = _net_margin(netinc, revenue)
    return (nm < 0).astype(float)


def mgc_037_net_margin_zscore_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of net margin over trailing 4 quarters."""
    nm = _net_margin(netinc, revenue)
    return _zscore_rolling(nm, _TD_YEAR)


def mgc_038_pretax_margin_level(ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current pretax margin (ebt / revenue)."""
    return _pretax_margin(ebt, revenue)


def mgc_039_pretax_margin_qoq_change(ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in pretax margin."""
    pm = _pretax_margin(ebt, revenue)
    return pm.diff(_TD_QTR)


def mgc_040_pretax_margin_yoy_change(ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in pretax margin."""
    pm = _pretax_margin(ebt, revenue)
    return pm.diff(_TD_YEAR)


# --- Group E (041-050): Cost-ratio deterioration (mirror of margin compression) ---

def mgc_041_cor_ratio_level(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Cost of revenue as fraction of revenue (high = low gross margin)."""
    return _cor_ratio(cor, revenue)


def mgc_042_cor_ratio_qoq_change(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ rise in COR ratio (rising = gross margin compression)."""
    cr = _cor_ratio(cor, revenue)
    return cr.diff(_TD_QTR)


def mgc_043_cor_ratio_yoy_change(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY rise in COR ratio."""
    cr = _cor_ratio(cor, revenue)
    return cr.diff(_TD_YEAR)


def mgc_044_opex_ratio_level(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating expenses as fraction of revenue."""
    return _opex_ratio(opex, revenue)


def mgc_045_opex_ratio_qoq_change(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ rise in opex ratio."""
    ox = _opex_ratio(opex, revenue)
    return ox.diff(_TD_QTR)


def mgc_046_opex_ratio_yoy_change(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY rise in opex ratio."""
    ox = _opex_ratio(opex, revenue)
    return ox.diff(_TD_YEAR)


def mgc_047_sgna_ratio_level(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """SG&A as fraction of revenue."""
    return _sgna_ratio(sgna, revenue)


def mgc_048_sgna_ratio_qoq_change(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ rise in SG&A ratio."""
    sr = _sgna_ratio(sgna, revenue)
    return sr.diff(_TD_QTR)


def mgc_049_rnd_ratio_level(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """R&D as fraction of revenue."""
    return _rnd_ratio(rnd, revenue)


def mgc_050_rnd_ratio_yoy_change(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY rise in R&D ratio."""
    rr = _rnd_ratio(rnd, revenue)
    return rr.diff(_TD_YEAR)


# --- Group F (051-060): Consecutive contraction counts and streaks ---

def mgc_051_gross_margin_consec_qoq_contraction(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Count of consecutive quarters (each 63-day step) with QoQ gross margin decline.
    Resets to 0 on any improvement.
    """
    gm = _gross_margin(gp, revenue)
    delta = gm.diff(_TD_QTR)
    contracting = (delta < 0).astype(float)

    def _streak(x):
        count = 0.0
        for v in x:
            if v == 1.0:
                count += 1.0
            else:
                count = 0.0
        return count

    return contracting.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def mgc_052_op_margin_consec_qoq_contraction(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count of consecutive quarters with QoQ operating margin decline."""
    om = _op_margin(opinc, revenue)
    delta = om.diff(_TD_QTR)
    contracting = (delta < 0).astype(float)

    def _streak(x):
        count = 0.0
        for v in x:
            if v == 1.0:
                count += 1.0
            else:
                count = 0.0
        return count

    return contracting.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def mgc_053_net_margin_consec_qoq_contraction(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count of consecutive quarters with QoQ net margin decline."""
    nm = _net_margin(netinc, revenue)
    delta = nm.diff(_TD_QTR)
    contracting = (delta < 0).astype(float)

    def _streak(x):
        count = 0.0
        for v in x:
            if v == 1.0:
                count += 1.0
            else:
                count = 0.0
        return count

    return contracting.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def mgc_054_ebitda_margin_consec_qoq_contraction(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count of consecutive quarters with QoQ EBITDA margin decline."""
    em = _ebitda_margin(ebitda, revenue)
    delta = em.diff(_TD_QTR)
    contracting = (delta < 0).astype(float)

    def _streak(x):
        count = 0.0
        for v in x:
            if v == 1.0:
                count += 1.0
            else:
                count = 0.0
        return count

    return contracting.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def mgc_055_gross_margin_qoq_contraction_fraction_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Fraction of last 4 quarters where gross margin contracted QoQ."""
    gm = _gross_margin(gp, revenue)
    contracting = (gm.diff(_TD_QTR) < 0).astype(float)
    return _rolling_mean(contracting, _TD_YEAR)


def mgc_056_op_margin_qoq_contraction_fraction_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Fraction of last 4 quarters where operating margin contracted QoQ."""
    om = _op_margin(opinc, revenue)
    contracting = (om.diff(_TD_QTR) < 0).astype(float)
    return _rolling_mean(contracting, _TD_YEAR)


def mgc_057_net_margin_qoq_contraction_fraction_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Fraction of last 8 quarters where net margin contracted QoQ."""
    nm = _net_margin(netinc, revenue)
    contracting = (nm.diff(_TD_QTR) < 0).astype(float)
    return _rolling_mean(contracting, _TD_2Y)


def mgc_058_multi_margin_contraction_score(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    Number of margin lines (gross/op/ebitda/net) contracting QoQ simultaneously.
    Range 0-4; 4 = all four margin lines declining together.
    """
    gm_c = ((_gross_margin(gp, revenue)).diff(_TD_QTR) < 0).astype(float)
    om_c = ((_op_margin(opinc, revenue)).diff(_TD_QTR) < 0).astype(float)
    em_c = ((_ebitda_margin(ebitda, revenue)).diff(_TD_QTR) < 0).astype(float)
    nm_c = ((_net_margin(netinc, revenue)).diff(_TD_QTR) < 0).astype(float)
    return gm_c + om_c + em_c + nm_c


def mgc_059_any_margin_negative_count(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    Number of margin lines (gross/op/ebitda/net) currently negative.
    Range 0-4; 4 = all negative simultaneously.
    """
    gm_n = (_gross_margin(gp, revenue) < 0).astype(float)
    om_n = (_op_margin(opinc, revenue) < 0).astype(float)
    em_n = (_ebitda_margin(ebitda, revenue) < 0).astype(float)
    nm_n = (_net_margin(netinc, revenue) < 0).astype(float)
    return gm_n + om_n + em_n + nm_n


def mgc_060_gross_to_op_margin_spread(gp: pd.Series, opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Gross margin minus operating margin (the opex burden above COR).
    Widening spread signals rising SG&A / R&D overhead eating into gross profit.
    """
    return _gross_margin(gp, revenue) - _op_margin(opinc, revenue)


# --- Group G (061-075): Peak drawdown depth, range position, leverage metrics ---

def mgc_061_gross_margin_dd_from_4q_peak(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin depth below its 4-quarter peak (absolute gap, always <=0)."""
    gm = _gross_margin(gp, revenue)
    pk = _rolling_max(gm, _TD_YEAR)
    return gm - pk


def mgc_062_op_margin_dd_from_8q_peak(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin depth below its 8-quarter peak."""
    om = _op_margin(opinc, revenue)
    pk = _rolling_max(om, _TD_2Y)
    return om - pk


def mgc_063_net_margin_dd_from_8q_peak(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin depth below its 8-quarter peak."""
    nm = _net_margin(netinc, revenue)
    pk = _rolling_max(nm, _TD_2Y)
    return nm - pk


def mgc_064_ebitda_margin_dd_from_8q_peak(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin depth below its 8-quarter peak."""
    em = _ebitda_margin(ebitda, revenue)
    pk = _rolling_max(em, _TD_2Y)
    return em - pk


def mgc_065_gross_margin_range_position_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin position in its 4-quarter range: 0 = at 4q low, 1 = at 4q high."""
    gm = _gross_margin(gp, revenue)
    mn = _rolling_min(gm, _TD_YEAR)
    mx = _rolling_max(gm, _TD_YEAR)
    return _safe_div(gm - mn, mx - mn)


def mgc_066_op_margin_range_position_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin position in its 4-quarter range."""
    om = _op_margin(opinc, revenue)
    mn = _rolling_min(om, _TD_YEAR)
    mx = _rolling_max(om, _TD_YEAR)
    return _safe_div(om - mn, mx - mn)


def mgc_067_net_margin_range_position_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin position in its 8-quarter range."""
    nm = _net_margin(netinc, revenue)
    mn = _rolling_min(nm, _TD_2Y)
    mx = _rolling_max(nm, _TD_2Y)
    return _safe_div(nm - mn, mx - mn)


def mgc_068_gross_op_margin_compression_ratio(gp: pd.Series, opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Ratio of QoQ gross margin change to QoQ operating margin change.
    Values < 1 indicate opex growing faster than gross profit (double compression).
    """
    gm_chg = (_gross_margin(gp, revenue)).diff(_TD_QTR)
    om_chg = (_op_margin(opinc, revenue)).diff(_TD_QTR)
    return _safe_div(gm_chg, om_chg.abs() + _EPS)


def mgc_069_ebit_margin_level(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBIT margin (ebit / revenue); distinct from EBITDA (excludes D&A add-back)."""
    return _ebit_margin(ebit, revenue)


def mgc_070_ebit_margin_yoy_change(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in EBIT margin."""
    em = _ebit_margin(ebit, revenue)
    return em.diff(_TD_YEAR)


def mgc_071_intexp_ratio_level(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Interest expense as fraction of revenue (financing burden on margins)."""
    return _intexp_ratio(intexp, revenue)


def mgc_072_intexp_ratio_yoy_change(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in interest expense ratio (rising = increasing margin drag)."""
    ir = _intexp_ratio(intexp, revenue)
    return ir.diff(_TD_YEAR)


def mgc_073_taxexp_ratio_level(taxexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Tax expense as fraction of revenue."""
    return _taxexp_ratio(taxexp, revenue)


def mgc_074_depamor_ratio_level(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Depreciation & amortization as fraction of revenue (non-cash margin drag)."""
    return _depamor_ratio(depamor, revenue)


def mgc_075_sbcomp_ratio_level(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Stock-based compensation as fraction of revenue (dilutive margin drag)."""
    return _sbcomp_ratio(sbcomp, revenue)


# ── Registry ───────────────────────────────────────────────────────────────────

MARGIN_COMPRESSION_REGISTRY_001_075 = {
    "mgc_001_gross_margin_level": {"inputs": ["gp", "revenue"], "func": mgc_001_gross_margin_level},
    "mgc_002_gross_margin_qoq_change": {"inputs": ["gp", "revenue"], "func": mgc_002_gross_margin_qoq_change},
    "mgc_003_gross_margin_yoy_change": {"inputs": ["gp", "revenue"], "func": mgc_003_gross_margin_yoy_change},
    "mgc_004_gross_margin_2y_change": {"inputs": ["gp", "revenue"], "func": mgc_004_gross_margin_2y_change},
    "mgc_005_gross_margin_vs_4q_avg": {"inputs": ["gp", "revenue"], "func": mgc_005_gross_margin_vs_4q_avg},
    "mgc_006_gross_margin_vs_8q_avg": {"inputs": ["gp", "revenue"], "func": mgc_006_gross_margin_vs_8q_avg},
    "mgc_007_gross_margin_vs_peak_4q": {"inputs": ["gp", "revenue"], "func": mgc_007_gross_margin_vs_peak_4q},
    "mgc_008_gross_margin_vs_peak_8q": {"inputs": ["gp", "revenue"], "func": mgc_008_gross_margin_vs_peak_8q},
    "mgc_009_gross_margin_vs_peak_ath": {"inputs": ["gp", "revenue"], "func": mgc_009_gross_margin_vs_peak_ath},
    "mgc_010_gross_margin_below_4q_min": {"inputs": ["gp", "revenue"], "func": mgc_010_gross_margin_below_4q_min},
    "mgc_011_op_margin_level": {"inputs": ["opinc", "revenue"], "func": mgc_011_op_margin_level},
    "mgc_012_op_margin_qoq_change": {"inputs": ["opinc", "revenue"], "func": mgc_012_op_margin_qoq_change},
    "mgc_013_op_margin_yoy_change": {"inputs": ["opinc", "revenue"], "func": mgc_013_op_margin_yoy_change},
    "mgc_014_op_margin_2y_change": {"inputs": ["opinc", "revenue"], "func": mgc_014_op_margin_2y_change},
    "mgc_015_op_margin_vs_4q_avg": {"inputs": ["opinc", "revenue"], "func": mgc_015_op_margin_vs_4q_avg},
    "mgc_016_op_margin_vs_peak_4q": {"inputs": ["opinc", "revenue"], "func": mgc_016_op_margin_vs_peak_4q},
    "mgc_017_op_margin_vs_peak_ath": {"inputs": ["opinc", "revenue"], "func": mgc_017_op_margin_vs_peak_ath},
    "mgc_018_op_margin_negative_flag": {"inputs": ["opinc", "revenue"], "func": mgc_018_op_margin_negative_flag},
    "mgc_019_op_margin_zscore_4q": {"inputs": ["opinc", "revenue"], "func": mgc_019_op_margin_zscore_4q},
    "mgc_020_op_margin_zscore_8q": {"inputs": ["opinc", "revenue"], "func": mgc_020_op_margin_zscore_8q},
    "mgc_021_ebitda_margin_level": {"inputs": ["ebitda", "revenue"], "func": mgc_021_ebitda_margin_level},
    "mgc_022_ebitda_margin_qoq_change": {"inputs": ["ebitda", "revenue"], "func": mgc_022_ebitda_margin_qoq_change},
    "mgc_023_ebitda_margin_yoy_change": {"inputs": ["ebitda", "revenue"], "func": mgc_023_ebitda_margin_yoy_change},
    "mgc_024_ebitda_margin_vs_4q_avg": {"inputs": ["ebitda", "revenue"], "func": mgc_024_ebitda_margin_vs_4q_avg},
    "mgc_025_ebitda_margin_vs_peak_4q": {"inputs": ["ebitda", "revenue"], "func": mgc_025_ebitda_margin_vs_peak_4q},
    "mgc_026_ebitda_margin_vs_peak_ath": {"inputs": ["ebitda", "revenue"], "func": mgc_026_ebitda_margin_vs_peak_ath},
    "mgc_027_ebitda_margin_zscore_4q": {"inputs": ["ebitda", "revenue"], "func": mgc_027_ebitda_margin_zscore_4q},
    "mgc_028_ebitda_margin_negative_flag": {"inputs": ["ebitda", "revenue"], "func": mgc_028_ebitda_margin_negative_flag},
    "mgc_029_ebitda_margin_2y_change": {"inputs": ["ebitda", "revenue"], "func": mgc_029_ebitda_margin_2y_change},
    "mgc_030_ebitda_margin_vs_8q_avg": {"inputs": ["ebitda", "revenue"], "func": mgc_030_ebitda_margin_vs_8q_avg},
    "mgc_031_net_margin_level": {"inputs": ["netinc", "revenue"], "func": mgc_031_net_margin_level},
    "mgc_032_net_margin_qoq_change": {"inputs": ["netinc", "revenue"], "func": mgc_032_net_margin_qoq_change},
    "mgc_033_net_margin_yoy_change": {"inputs": ["netinc", "revenue"], "func": mgc_033_net_margin_yoy_change},
    "mgc_034_net_margin_vs_4q_avg": {"inputs": ["netinc", "revenue"], "func": mgc_034_net_margin_vs_4q_avg},
    "mgc_035_net_margin_vs_peak_ath": {"inputs": ["netinc", "revenue"], "func": mgc_035_net_margin_vs_peak_ath},
    "mgc_036_net_margin_negative_flag": {"inputs": ["netinc", "revenue"], "func": mgc_036_net_margin_negative_flag},
    "mgc_037_net_margin_zscore_4q": {"inputs": ["netinc", "revenue"], "func": mgc_037_net_margin_zscore_4q},
    "mgc_038_pretax_margin_level": {"inputs": ["ebt", "revenue"], "func": mgc_038_pretax_margin_level},
    "mgc_039_pretax_margin_qoq_change": {"inputs": ["ebt", "revenue"], "func": mgc_039_pretax_margin_qoq_change},
    "mgc_040_pretax_margin_yoy_change": {"inputs": ["ebt", "revenue"], "func": mgc_040_pretax_margin_yoy_change},
    "mgc_041_cor_ratio_level": {"inputs": ["cor", "revenue"], "func": mgc_041_cor_ratio_level},
    "mgc_042_cor_ratio_qoq_change": {"inputs": ["cor", "revenue"], "func": mgc_042_cor_ratio_qoq_change},
    "mgc_043_cor_ratio_yoy_change": {"inputs": ["cor", "revenue"], "func": mgc_043_cor_ratio_yoy_change},
    "mgc_044_opex_ratio_level": {"inputs": ["opex", "revenue"], "func": mgc_044_opex_ratio_level},
    "mgc_045_opex_ratio_qoq_change": {"inputs": ["opex", "revenue"], "func": mgc_045_opex_ratio_qoq_change},
    "mgc_046_opex_ratio_yoy_change": {"inputs": ["opex", "revenue"], "func": mgc_046_opex_ratio_yoy_change},
    "mgc_047_sgna_ratio_level": {"inputs": ["sgna", "revenue"], "func": mgc_047_sgna_ratio_level},
    "mgc_048_sgna_ratio_qoq_change": {"inputs": ["sgna", "revenue"], "func": mgc_048_sgna_ratio_qoq_change},
    "mgc_049_rnd_ratio_level": {"inputs": ["rnd", "revenue"], "func": mgc_049_rnd_ratio_level},
    "mgc_050_rnd_ratio_yoy_change": {"inputs": ["rnd", "revenue"], "func": mgc_050_rnd_ratio_yoy_change},
    "mgc_051_gross_margin_consec_qoq_contraction": {"inputs": ["gp", "revenue"], "func": mgc_051_gross_margin_consec_qoq_contraction},
    "mgc_052_op_margin_consec_qoq_contraction": {"inputs": ["opinc", "revenue"], "func": mgc_052_op_margin_consec_qoq_contraction},
    "mgc_053_net_margin_consec_qoq_contraction": {"inputs": ["netinc", "revenue"], "func": mgc_053_net_margin_consec_qoq_contraction},
    "mgc_054_ebitda_margin_consec_qoq_contraction": {"inputs": ["ebitda", "revenue"], "func": mgc_054_ebitda_margin_consec_qoq_contraction},
    "mgc_055_gross_margin_qoq_contraction_fraction_4q": {"inputs": ["gp", "revenue"], "func": mgc_055_gross_margin_qoq_contraction_fraction_4q},
    "mgc_056_op_margin_qoq_contraction_fraction_4q": {"inputs": ["opinc", "revenue"], "func": mgc_056_op_margin_qoq_contraction_fraction_4q},
    "mgc_057_net_margin_qoq_contraction_fraction_8q": {"inputs": ["netinc", "revenue"], "func": mgc_057_net_margin_qoq_contraction_fraction_8q},
    "mgc_058_multi_margin_contraction_score": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_058_multi_margin_contraction_score},
    "mgc_059_any_margin_negative_count": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_059_any_margin_negative_count},
    "mgc_060_gross_to_op_margin_spread": {"inputs": ["gp", "opinc", "revenue"], "func": mgc_060_gross_to_op_margin_spread},
    "mgc_061_gross_margin_dd_from_4q_peak": {"inputs": ["gp", "revenue"], "func": mgc_061_gross_margin_dd_from_4q_peak},
    "mgc_062_op_margin_dd_from_8q_peak": {"inputs": ["opinc", "revenue"], "func": mgc_062_op_margin_dd_from_8q_peak},
    "mgc_063_net_margin_dd_from_8q_peak": {"inputs": ["netinc", "revenue"], "func": mgc_063_net_margin_dd_from_8q_peak},
    "mgc_064_ebitda_margin_dd_from_8q_peak": {"inputs": ["ebitda", "revenue"], "func": mgc_064_ebitda_margin_dd_from_8q_peak},
    "mgc_065_gross_margin_range_position_4q": {"inputs": ["gp", "revenue"], "func": mgc_065_gross_margin_range_position_4q},
    "mgc_066_op_margin_range_position_4q": {"inputs": ["opinc", "revenue"], "func": mgc_066_op_margin_range_position_4q},
    "mgc_067_net_margin_range_position_8q": {"inputs": ["netinc", "revenue"], "func": mgc_067_net_margin_range_position_8q},
    "mgc_068_gross_op_margin_compression_ratio": {"inputs": ["gp", "opinc", "revenue"], "func": mgc_068_gross_op_margin_compression_ratio},
    "mgc_069_ebit_margin_level": {"inputs": ["ebit", "revenue"], "func": mgc_069_ebit_margin_level},
    "mgc_070_ebit_margin_yoy_change": {"inputs": ["ebit", "revenue"], "func": mgc_070_ebit_margin_yoy_change},
    "mgc_071_intexp_ratio_level": {"inputs": ["intexp", "revenue"], "func": mgc_071_intexp_ratio_level},
    "mgc_072_intexp_ratio_yoy_change": {"inputs": ["intexp", "revenue"], "func": mgc_072_intexp_ratio_yoy_change},
    "mgc_073_taxexp_ratio_level": {"inputs": ["taxexp", "revenue"], "func": mgc_073_taxexp_ratio_level},
    "mgc_074_depamor_ratio_level": {"inputs": ["depamor", "revenue"], "func": mgc_074_depamor_ratio_level},
    "mgc_075_sbcomp_ratio_level": {"inputs": ["sbcomp", "revenue"], "func": mgc_075_sbcomp_ratio_level},
}
