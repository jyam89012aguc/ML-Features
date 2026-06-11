"""
62_margin_compression — Base Features 076-150
Domain: gross / operating / EBITDA / net / pretax margin erosion (continued)
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
_TD_QTR  = 63
_TD_YEAR = 252
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


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (scalar helper, raw=False)."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 4):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        xv_m = x.mean()
        num = ((xi - xi_m) * (x - xv_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=False)


# ── Margin constructors ────────────────────────────────────────────────────────

def _gross_margin(gp, revenue):
    return _safe_div(gp, revenue)

def _op_margin(opinc, revenue):
    return _safe_div(opinc, revenue)

def _ebitda_margin(ebitda, revenue):
    return _safe_div(ebitda, revenue)

def _net_margin(netinc, revenue):
    return _safe_div(netinc, revenue)

def _pretax_margin(ebt, revenue):
    return _safe_div(ebt, revenue)

def _ebit_margin(ebit, revenue):
    return _safe_div(ebit, revenue)

def _cor_ratio(cor, revenue):
    return _safe_div(cor, revenue)

def _opex_ratio(opex, revenue):
    return _safe_div(opex, revenue)

def _sgna_ratio(sgna, revenue):
    return _safe_div(sgna, revenue)

def _rnd_ratio(rnd, revenue):
    return _safe_div(rnd, revenue)

def _depamor_ratio(depamor, revenue):
    return _safe_div(depamor, revenue)

def _sbcomp_ratio(sbcomp, revenue):
    return _safe_div(sbcomp, revenue)

def _intexp_ratio(intexp, revenue):
    return _safe_div(intexp, revenue)

def _taxexp_ratio(taxexp, revenue):
    return _safe_div(taxexp, revenue)


# ── Feature functions 076-150 ──────────────────────────────────────────────────

# --- Group H (076-085): Operating leverage / revenue-margin divergence ---

def mgc_076_op_leverage_signal(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Operating leverage distress: YoY revenue change minus YoY op-margin change.
    Negative when revenue rises but margins fall faster (negative operating leverage).
    """
    rev_chg = _safe_div(revenue.diff(_TD_YEAR), revenue.shift(_TD_YEAR).replace(0, np.nan))
    om_chg = (_op_margin(opinc, revenue)).diff(_TD_YEAR)
    return rev_chg - om_chg


def mgc_077_gross_margin_erosion_per_rev_growth(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    QoQ gross margin change divided by QoQ revenue pct change.
    Negative when revenue growing but gross margin shrinking (price/mix deterioration).
    """
    gm_chg = (_gross_margin(gp, revenue)).diff(_TD_QTR)
    rev_pct = _safe_div(revenue.diff(_TD_QTR), revenue.shift(_TD_QTR).replace(0, np.nan))
    return _safe_div(gm_chg, rev_pct.abs() + _EPS)


def mgc_078_op_margin_slope_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of operating margin over trailing 4 quarters (252 days)."""
    om = _op_margin(opinc, revenue)
    return _linslope(om, _TD_YEAR)


def mgc_079_gross_margin_slope_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of gross margin over trailing 4 quarters."""
    gm = _gross_margin(gp, revenue)
    return _linslope(gm, _TD_YEAR)


def mgc_080_net_margin_slope_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of net margin over trailing 4 quarters."""
    nm = _net_margin(netinc, revenue)
    return _linslope(nm, _TD_YEAR)


def mgc_081_ebitda_margin_slope_4q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of EBITDA margin over trailing 4 quarters."""
    em = _ebitda_margin(ebitda, revenue)
    return _linslope(em, _TD_YEAR)


def mgc_082_gross_margin_slope_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of gross margin over trailing 8 quarters (504 days)."""
    gm = _gross_margin(gp, revenue)
    return _linslope(gm, _TD_2Y)


def mgc_083_op_margin_slope_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of operating margin over trailing 8 quarters."""
    om = _op_margin(opinc, revenue)
    return _linslope(om, _TD_2Y)


def mgc_084_net_margin_slope_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of net margin over trailing 8 quarters."""
    nm = _net_margin(netinc, revenue)
    return _linslope(nm, _TD_2Y)


def mgc_085_margin_slope_composite(
    gp: pd.Series, opinc: pd.Series, netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    Average of gross / op / net margin 4Q OLS slopes (composite trend signal).
    All three negative = broad-based margin trend deterioration.
    """
    gm_s = _linslope(_gross_margin(gp, revenue), _TD_YEAR)
    om_s = _linslope(_op_margin(opinc, revenue), _TD_YEAR)
    nm_s = _linslope(_net_margin(netinc, revenue), _TD_YEAR)
    return (gm_s + om_s + nm_s) / 3.0


# --- Group I (086-095): Margin below trailing averages (below-average flags) ---

def mgc_086_gross_margin_below_4q_avg_flag(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if current gross margin is below its 4-quarter trailing average."""
    gm = _gross_margin(gp, revenue)
    return (gm < _rolling_mean(gm, _TD_YEAR)).astype(float)


def mgc_087_op_margin_below_4q_avg_flag(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if current operating margin is below its 4-quarter trailing average."""
    om = _op_margin(opinc, revenue)
    return (om < _rolling_mean(om, _TD_YEAR)).astype(float)


def mgc_088_net_margin_below_4q_avg_flag(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if current net margin is below its 4-quarter trailing average."""
    nm = _net_margin(netinc, revenue)
    return (nm < _rolling_mean(nm, _TD_YEAR)).astype(float)


def mgc_089_ebitda_margin_below_4q_avg_flag(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if current EBITDA margin is below its 4-quarter trailing average."""
    em = _ebitda_margin(ebitda, revenue)
    return (em < _rolling_mean(em, _TD_YEAR)).astype(float)


def mgc_090_gross_margin_below_8q_avg_flag(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if gross margin is below its 8-quarter trailing average."""
    gm = _gross_margin(gp, revenue)
    return (gm < _rolling_mean(gm, _TD_2Y)).astype(float)


def mgc_091_op_margin_below_8q_avg_flag(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if operating margin is below its 8-quarter trailing average."""
    om = _op_margin(opinc, revenue)
    return (om < _rolling_mean(om, _TD_2Y)).astype(float)


def mgc_092_multi_margin_below_avg_score(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    Count of margin lines (gross/op/ebitda/net) currently below their
    4-quarter trailing average. Range 0-4.
    """
    gm = _gross_margin(gp, revenue)
    om = _op_margin(opinc, revenue)
    em = _ebitda_margin(ebitda, revenue)
    nm = _net_margin(netinc, revenue)
    return (
        (gm < _rolling_mean(gm, _TD_YEAR)).astype(float) +
        (om < _rolling_mean(om, _TD_YEAR)).astype(float) +
        (em < _rolling_mean(em, _TD_YEAR)).astype(float) +
        (nm < _rolling_mean(nm, _TD_YEAR)).astype(float)
    )


def mgc_093_gross_margin_below_4q_range_midpoint(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if gross margin is in the bottom half of its 4-quarter range."""
    gm = _gross_margin(gp, revenue)
    mn = _rolling_min(gm, _TD_YEAR)
    mx = _rolling_max(gm, _TD_YEAR)
    mid = (mn + mx) / 2.0
    return (gm < mid).astype(float)


def mgc_094_op_margin_below_4q_range_midpoint(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if operating margin is in the bottom half of its 4-quarter range."""
    om = _op_margin(opinc, revenue)
    mn = _rolling_min(om, _TD_YEAR)
    mx = _rolling_max(om, _TD_YEAR)
    mid = (mn + mx) / 2.0
    return (om < mid).astype(float)


def mgc_095_net_margin_4q_pct_rank(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of current net margin within its 4-quarter trailing window."""
    nm = _net_margin(netinc, revenue)
    return nm.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


# --- Group J (096-105): EWM smoothed margins and divergence from smoothed ---

def mgc_096_gross_margin_ewm_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """EWM (span=252) of gross margin — smoothed trend."""
    gm = _gross_margin(gp, revenue)
    return _ewm_mean(gm, _TD_YEAR)


def mgc_097_gross_margin_vs_ewm_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus its EWM-4Q (below = compression relative to trend)."""
    gm = _gross_margin(gp, revenue)
    return gm - _ewm_mean(gm, _TD_YEAR)


def mgc_098_op_margin_ewm_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """EWM (span=252) of operating margin."""
    om = _op_margin(opinc, revenue)
    return _ewm_mean(om, _TD_YEAR)


def mgc_099_op_margin_vs_ewm_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus its EWM-4Q."""
    om = _op_margin(opinc, revenue)
    return om - _ewm_mean(om, _TD_YEAR)


def mgc_100_net_margin_vs_ewm_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin minus its EWM-4Q."""
    nm = _net_margin(netinc, revenue)
    return nm - _ewm_mean(nm, _TD_YEAR)


def mgc_101_ebitda_margin_vs_ewm_4q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin minus its EWM-4Q."""
    em = _ebitda_margin(ebitda, revenue)
    return em - _ewm_mean(em, _TD_YEAR)


def mgc_102_gross_margin_ewm_cross(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    EWM-fast (span=63) minus EWM-slow (span=252) of gross margin.
    Negative = short-term margin deteriorating faster than long-term trend.
    """
    gm = _gross_margin(gp, revenue)
    return _ewm_mean(gm, _TD_QTR) - _ewm_mean(gm, _TD_YEAR)


def mgc_103_op_margin_ewm_cross(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """EWM-fast minus EWM-slow of operating margin."""
    om = _op_margin(opinc, revenue)
    return _ewm_mean(om, _TD_QTR) - _ewm_mean(om, _TD_YEAR)


def mgc_104_net_margin_ewm_cross(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """EWM-fast minus EWM-slow of net margin."""
    nm = _net_margin(netinc, revenue)
    return _ewm_mean(nm, _TD_QTR) - _ewm_mean(nm, _TD_YEAR)


def mgc_105_ebitda_margin_ewm_cross(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EWM-fast minus EWM-slow of EBITDA margin."""
    em = _ebitda_margin(ebitda, revenue)
    return _ewm_mean(em, _TD_QTR) - _ewm_mean(em, _TD_YEAR)


# --- Group K (106-115): Gross-to-net margin funnel and spread signals ---

def mgc_106_gross_to_net_margin_ratio(gp: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Gross margin divided by net margin.
    Rising ratio = overhead/taxes/interest consuming more gross profit.
    """
    gm = _gross_margin(gp, revenue)
    nm = _net_margin(netinc, revenue)
    return _safe_div(gm, nm.abs() + _EPS)


def mgc_107_gross_to_ebitda_spread(gp: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus EBITDA margin (opex overhead excluding D&A)."""
    return _gross_margin(gp, revenue) - _ebitda_margin(ebitda, revenue)


def mgc_108_ebitda_to_ebit_spread(ebitda: pd.Series, ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin minus EBIT margin = D&A as fraction of revenue."""
    return _ebitda_margin(ebitda, revenue) - _ebit_margin(ebit, revenue)


def mgc_109_ebit_to_net_spread(ebit: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBIT margin minus net margin = interest + tax as fraction of revenue."""
    return _ebit_margin(ebit, revenue) - _net_margin(netinc, revenue)


def mgc_110_gross_net_spread_yoy_change(gp: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in (gross margin - net margin) spread."""
    spread = _gross_margin(gp, revenue) - _net_margin(netinc, revenue)
    return spread.diff(_TD_YEAR)


def mgc_111_gross_ebitda_spread_yoy_change(gp: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in (gross - EBITDA) margin spread."""
    spread = _gross_margin(gp, revenue) - _ebitda_margin(ebitda, revenue)
    return spread.diff(_TD_YEAR)


def mgc_112_op_net_margin_spread(opinc: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus net margin (below-the-line burden: interest + tax)."""
    return _op_margin(opinc, revenue) - _net_margin(netinc, revenue)


def mgc_113_op_net_spread_yoy_change(opinc: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in op-net margin spread."""
    spread = _op_margin(opinc, revenue) - _net_margin(netinc, revenue)
    return spread.diff(_TD_YEAR)


def mgc_114_cor_ratio_vs_4q_avg(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """COR ratio minus its trailing 4-quarter average (rising COR burden)."""
    cr = _cor_ratio(cor, revenue)
    return cr - _rolling_mean(cr, _TD_YEAR)


def mgc_115_sgna_ratio_vs_4q_avg(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """SG&A ratio minus its trailing 4-quarter average."""
    sr = _sgna_ratio(sgna, revenue)
    return sr - _rolling_mean(sr, _TD_YEAR)


# --- Group L (116-125): Percentile ranks and z-scores ---

def mgc_116_gross_margin_pct_rank_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of gross margin within its 8-quarter trailing window."""
    gm = _gross_margin(gp, revenue)
    return gm.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def mgc_117_op_margin_pct_rank_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of op margin within its 8-quarter trailing window."""
    om = _op_margin(opinc, revenue)
    return om.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def mgc_118_net_margin_pct_rank_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of net margin within its 8-quarter trailing window."""
    nm = _net_margin(netinc, revenue)
    return nm.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def mgc_119_ebitda_margin_pct_rank_8q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA margin within its 8-quarter trailing window."""
    em = _ebitda_margin(ebitda, revenue)
    return em.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).rank(pct=True)


def mgc_120_gross_margin_zscore_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of gross margin over trailing 8 quarters."""
    gm = _gross_margin(gp, revenue)
    return _zscore_rolling(gm, _TD_2Y)


def mgc_121_op_margin_zscore_12q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating margin over trailing 12 quarters (756 days)."""
    om = _op_margin(opinc, revenue)
    return _zscore_rolling(om, _TD_3Y)


def mgc_122_net_margin_zscore_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of net margin over trailing 8 quarters."""
    nm = _net_margin(netinc, revenue)
    return _zscore_rolling(nm, _TD_2Y)


def mgc_123_ebitda_margin_zscore_12q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of EBITDA margin over trailing 12 quarters."""
    em = _ebitda_margin(ebitda, revenue)
    return _zscore_rolling(em, _TD_3Y)


def mgc_124_cor_ratio_zscore_4q(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of COR ratio over trailing 4 quarters."""
    cr = _cor_ratio(cor, revenue)
    return _zscore_rolling(cr, _TD_YEAR)


def mgc_125_opex_ratio_zscore_4q(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of opex ratio over trailing 4 quarters."""
    ox = _opex_ratio(opex, revenue)
    return _zscore_rolling(ox, _TD_YEAR)


# --- Group M (126-135): 3-year and 5-year margin change ---

def mgc_126_gross_margin_3y_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year change in gross margin (756-day diff)."""
    gm = _gross_margin(gp, revenue)
    return gm.diff(_TD_3Y)


def mgc_127_op_margin_3y_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year change in operating margin."""
    om = _op_margin(opinc, revenue)
    return om.diff(_TD_3Y)


def mgc_128_net_margin_3y_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year change in net margin."""
    nm = _net_margin(netinc, revenue)
    return nm.diff(_TD_3Y)


def mgc_129_ebitda_margin_3y_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year change in EBITDA margin."""
    em = _ebitda_margin(ebitda, revenue)
    return em.diff(_TD_3Y)


def mgc_130_gross_margin_pct_rank_20q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of gross margin within its trailing 20-quarter (5-year, 1260-day) window.
    Low rank (near 0) signals gross margin at its worst level in 5 years."""
    gm = _gross_margin(gp, revenue)
    return gm.rolling(_TD_5Y, min_periods=max(2, _TD_5Y // 4)).rank(pct=True)


def mgc_131_op_margin_pct_rank_20q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of operating margin within its trailing 20-quarter (5-year, 1260-day) window.
    Low rank signals operating margin at its worst level in 5 years."""
    om = _op_margin(opinc, revenue)
    return om.rolling(_TD_5Y, min_periods=max(2, _TD_5Y // 4)).rank(pct=True)


def mgc_132_net_margin_dist_to_5y_low(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin distance above its trailing 5-year minimum (0 = at multi-year worst)."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_min(nm, _TD_5Y)


def mgc_133_gross_margin_vs_3y_avg(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus trailing 3-year (756-day) mean."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_mean(gm, _TD_3Y)


def mgc_134_op_margin_vs_3y_avg(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus trailing 3-year mean."""
    om = _op_margin(opinc, revenue)
    return om - _rolling_mean(om, _TD_3Y)


def mgc_135_net_margin_vs_3y_avg(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin minus trailing 3-year mean."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_mean(nm, _TD_3Y)


# --- Group N (136-145): Cross-margin compression divergence ---

def mgc_136_gross_minus_net_margin_qoq_change(
    gp: pd.Series, netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """QoQ change in (gross - net) spread: widening = overhead/taxes/interest growing."""
    spread = _gross_margin(gp, revenue) - _net_margin(netinc, revenue)
    return spread.diff(_TD_QTR)


def mgc_137_op_minus_net_margin_qoq_change(
    opinc: pd.Series, netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """QoQ change in (op - net) spread: widening = below-the-line costs growing."""
    spread = _op_margin(opinc, revenue) - _net_margin(netinc, revenue)
    return spread.diff(_TD_QTR)


def mgc_138_gross_margin_median_deviation_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus trailing 4-quarter median."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_median(gm, _TD_YEAR)


def mgc_139_op_margin_median_deviation_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus trailing 4-quarter median."""
    om = _op_margin(opinc, revenue)
    return om - _rolling_median(om, _TD_YEAR)


def mgc_140_net_margin_median_deviation_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin minus trailing 8-quarter median."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_median(nm, _TD_2Y)


def mgc_141_sgna_ratio_yoy_change(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in SG&A ratio (rising SG&A burden)."""
    sr = _sgna_ratio(sgna, revenue)
    return sr.diff(_TD_YEAR)


def mgc_142_rnd_ratio_qoq_change(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in R&D ratio."""
    rr = _rnd_ratio(rnd, revenue)
    return rr.diff(_TD_QTR)


def mgc_143_depamor_ratio_yoy_change(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in D&A ratio (non-cash margin drag increasing)."""
    dr = _depamor_ratio(depamor, revenue)
    return dr.diff(_TD_YEAR)


def mgc_144_sbcomp_ratio_yoy_change(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in SBC ratio (dilution cost rising)."""
    sb = _sbcomp_ratio(sbcomp, revenue)
    return sb.diff(_TD_YEAR)


def mgc_145_intexp_ratio_qoq_change(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in interest expense ratio."""
    ir = _intexp_ratio(intexp, revenue)
    return ir.diff(_TD_QTR)


# --- Group O (146-150): Composite multi-margin stress scores ---

def mgc_146_margin_compression_composite_4q(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    Equally weighted average of gross/op/ebitda/net margin 4Q z-scores.
    More negative = broader-based, deeper margin compression.
    """
    gm_z = _zscore_rolling(_gross_margin(gp, revenue), _TD_YEAR)
    om_z = _zscore_rolling(_op_margin(opinc, revenue), _TD_YEAR)
    em_z = _zscore_rolling(_ebitda_margin(ebitda, revenue), _TD_YEAR)
    nm_z = _zscore_rolling(_net_margin(netinc, revenue), _TD_YEAR)
    return (gm_z + om_z + em_z + nm_z) / 4.0


def mgc_147_cost_ratio_composite_vs_4q_avg(
    cor: pd.Series, opex: pd.Series, sgna: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    Average of (COR ratio - 4Q avg) + (opex ratio - 4Q avg) + (SG&A ratio - 4Q avg).
    Positive = broad cost-ratio deterioration above recent norms.
    """
    cr_dev = _cor_ratio(cor, revenue) - _rolling_mean(_cor_ratio(cor, revenue), _TD_YEAR)
    ox_dev = _opex_ratio(opex, revenue) - _rolling_mean(_opex_ratio(opex, revenue), _TD_YEAR)
    sr_dev = _sgna_ratio(sgna, revenue) - _rolling_mean(_sgna_ratio(sgna, revenue), _TD_YEAR)
    return (cr_dev + ox_dev + sr_dev) / 3.0


def mgc_148_net_margin_expanding_pct_rank(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of net margin within its full expanding history."""
    nm = _net_margin(netinc, revenue)
    return nm.expanding(min_periods=2).rank(pct=True)


def mgc_149_gross_margin_expanding_pct_rank(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of gross margin within its full expanding history."""
    gm = _gross_margin(gp, revenue)
    return gm.expanding(min_periods=2).rank(pct=True)


def mgc_150_all_margins_negative_flag(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    1 if ALL four margin lines (gross/op/ebitda/net) are simultaneously negative.
    Extreme distress flag: full P&L in loss.
    """
    gm = _gross_margin(gp, revenue)
    om = _op_margin(opinc, revenue)
    em = _ebitda_margin(ebitda, revenue)
    nm = _net_margin(netinc, revenue)
    return ((gm < 0) & (om < 0) & (em < 0) & (nm < 0)).astype(float)


# ── Registry ───────────────────────────────────────────────────────────────────

MARGIN_COMPRESSION_REGISTRY_076_150 = {
    "mgc_076_op_leverage_signal": {"inputs": ["opinc", "revenue"], "func": mgc_076_op_leverage_signal},
    "mgc_077_gross_margin_erosion_per_rev_growth": {"inputs": ["gp", "revenue"], "func": mgc_077_gross_margin_erosion_per_rev_growth},
    "mgc_078_op_margin_slope_4q": {"inputs": ["opinc", "revenue"], "func": mgc_078_op_margin_slope_4q},
    "mgc_079_gross_margin_slope_4q": {"inputs": ["gp", "revenue"], "func": mgc_079_gross_margin_slope_4q},
    "mgc_080_net_margin_slope_4q": {"inputs": ["netinc", "revenue"], "func": mgc_080_net_margin_slope_4q},
    "mgc_081_ebitda_margin_slope_4q": {"inputs": ["ebitda", "revenue"], "func": mgc_081_ebitda_margin_slope_4q},
    "mgc_082_gross_margin_slope_8q": {"inputs": ["gp", "revenue"], "func": mgc_082_gross_margin_slope_8q},
    "mgc_083_op_margin_slope_8q": {"inputs": ["opinc", "revenue"], "func": mgc_083_op_margin_slope_8q},
    "mgc_084_net_margin_slope_8q": {"inputs": ["netinc", "revenue"], "func": mgc_084_net_margin_slope_8q},
    "mgc_085_margin_slope_composite": {"inputs": ["gp", "opinc", "netinc", "revenue"], "func": mgc_085_margin_slope_composite},
    "mgc_086_gross_margin_below_4q_avg_flag": {"inputs": ["gp", "revenue"], "func": mgc_086_gross_margin_below_4q_avg_flag},
    "mgc_087_op_margin_below_4q_avg_flag": {"inputs": ["opinc", "revenue"], "func": mgc_087_op_margin_below_4q_avg_flag},
    "mgc_088_net_margin_below_4q_avg_flag": {"inputs": ["netinc", "revenue"], "func": mgc_088_net_margin_below_4q_avg_flag},
    "mgc_089_ebitda_margin_below_4q_avg_flag": {"inputs": ["ebitda", "revenue"], "func": mgc_089_ebitda_margin_below_4q_avg_flag},
    "mgc_090_gross_margin_below_8q_avg_flag": {"inputs": ["gp", "revenue"], "func": mgc_090_gross_margin_below_8q_avg_flag},
    "mgc_091_op_margin_below_8q_avg_flag": {"inputs": ["opinc", "revenue"], "func": mgc_091_op_margin_below_8q_avg_flag},
    "mgc_092_multi_margin_below_avg_score": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_092_multi_margin_below_avg_score},
    "mgc_093_gross_margin_below_4q_range_midpoint": {"inputs": ["gp", "revenue"], "func": mgc_093_gross_margin_below_4q_range_midpoint},
    "mgc_094_op_margin_below_4q_range_midpoint": {"inputs": ["opinc", "revenue"], "func": mgc_094_op_margin_below_4q_range_midpoint},
    "mgc_095_net_margin_4q_pct_rank": {"inputs": ["netinc", "revenue"], "func": mgc_095_net_margin_4q_pct_rank},
    "mgc_096_gross_margin_ewm_4q": {"inputs": ["gp", "revenue"], "func": mgc_096_gross_margin_ewm_4q},
    "mgc_097_gross_margin_vs_ewm_4q": {"inputs": ["gp", "revenue"], "func": mgc_097_gross_margin_vs_ewm_4q},
    "mgc_098_op_margin_ewm_4q": {"inputs": ["opinc", "revenue"], "func": mgc_098_op_margin_ewm_4q},
    "mgc_099_op_margin_vs_ewm_4q": {"inputs": ["opinc", "revenue"], "func": mgc_099_op_margin_vs_ewm_4q},
    "mgc_100_net_margin_vs_ewm_4q": {"inputs": ["netinc", "revenue"], "func": mgc_100_net_margin_vs_ewm_4q},
    "mgc_101_ebitda_margin_vs_ewm_4q": {"inputs": ["ebitda", "revenue"], "func": mgc_101_ebitda_margin_vs_ewm_4q},
    "mgc_102_gross_margin_ewm_cross": {"inputs": ["gp", "revenue"], "func": mgc_102_gross_margin_ewm_cross},
    "mgc_103_op_margin_ewm_cross": {"inputs": ["opinc", "revenue"], "func": mgc_103_op_margin_ewm_cross},
    "mgc_104_net_margin_ewm_cross": {"inputs": ["netinc", "revenue"], "func": mgc_104_net_margin_ewm_cross},
    "mgc_105_ebitda_margin_ewm_cross": {"inputs": ["ebitda", "revenue"], "func": mgc_105_ebitda_margin_ewm_cross},
    "mgc_106_gross_to_net_margin_ratio": {"inputs": ["gp", "netinc", "revenue"], "func": mgc_106_gross_to_net_margin_ratio},
    "mgc_107_gross_to_ebitda_spread": {"inputs": ["gp", "ebitda", "revenue"], "func": mgc_107_gross_to_ebitda_spread},
    "mgc_108_ebitda_to_ebit_spread": {"inputs": ["ebitda", "ebit", "revenue"], "func": mgc_108_ebitda_to_ebit_spread},
    "mgc_109_ebit_to_net_spread": {"inputs": ["ebit", "netinc", "revenue"], "func": mgc_109_ebit_to_net_spread},
    "mgc_110_gross_net_spread_yoy_change": {"inputs": ["gp", "netinc", "revenue"], "func": mgc_110_gross_net_spread_yoy_change},
    "mgc_111_gross_ebitda_spread_yoy_change": {"inputs": ["gp", "ebitda", "revenue"], "func": mgc_111_gross_ebitda_spread_yoy_change},
    "mgc_112_op_net_margin_spread": {"inputs": ["opinc", "netinc", "revenue"], "func": mgc_112_op_net_margin_spread},
    "mgc_113_op_net_spread_yoy_change": {"inputs": ["opinc", "netinc", "revenue"], "func": mgc_113_op_net_spread_yoy_change},
    "mgc_114_cor_ratio_vs_4q_avg": {"inputs": ["cor", "revenue"], "func": mgc_114_cor_ratio_vs_4q_avg},
    "mgc_115_sgna_ratio_vs_4q_avg": {"inputs": ["sgna", "revenue"], "func": mgc_115_sgna_ratio_vs_4q_avg},
    "mgc_116_gross_margin_pct_rank_8q": {"inputs": ["gp", "revenue"], "func": mgc_116_gross_margin_pct_rank_8q},
    "mgc_117_op_margin_pct_rank_8q": {"inputs": ["opinc", "revenue"], "func": mgc_117_op_margin_pct_rank_8q},
    "mgc_118_net_margin_pct_rank_8q": {"inputs": ["netinc", "revenue"], "func": mgc_118_net_margin_pct_rank_8q},
    "mgc_119_ebitda_margin_pct_rank_8q": {"inputs": ["ebitda", "revenue"], "func": mgc_119_ebitda_margin_pct_rank_8q},
    "mgc_120_gross_margin_zscore_8q": {"inputs": ["gp", "revenue"], "func": mgc_120_gross_margin_zscore_8q},
    "mgc_121_op_margin_zscore_12q": {"inputs": ["opinc", "revenue"], "func": mgc_121_op_margin_zscore_12q},
    "mgc_122_net_margin_zscore_8q": {"inputs": ["netinc", "revenue"], "func": mgc_122_net_margin_zscore_8q},
    "mgc_123_ebitda_margin_zscore_12q": {"inputs": ["ebitda", "revenue"], "func": mgc_123_ebitda_margin_zscore_12q},
    "mgc_124_cor_ratio_zscore_4q": {"inputs": ["cor", "revenue"], "func": mgc_124_cor_ratio_zscore_4q},
    "mgc_125_opex_ratio_zscore_4q": {"inputs": ["opex", "revenue"], "func": mgc_125_opex_ratio_zscore_4q},
    "mgc_126_gross_margin_3y_change": {"inputs": ["gp", "revenue"], "func": mgc_126_gross_margin_3y_change},
    "mgc_127_op_margin_3y_change": {"inputs": ["opinc", "revenue"], "func": mgc_127_op_margin_3y_change},
    "mgc_128_net_margin_3y_change": {"inputs": ["netinc", "revenue"], "func": mgc_128_net_margin_3y_change},
    "mgc_129_ebitda_margin_3y_change": {"inputs": ["ebitda", "revenue"], "func": mgc_129_ebitda_margin_3y_change},
    "mgc_130_gross_margin_pct_rank_20q": {"inputs": ["gp", "revenue"], "func": mgc_130_gross_margin_pct_rank_20q},
    "mgc_131_op_margin_pct_rank_20q": {"inputs": ["opinc", "revenue"], "func": mgc_131_op_margin_pct_rank_20q},
    "mgc_132_net_margin_dist_to_5y_low": {"inputs": ["netinc", "revenue"], "func": mgc_132_net_margin_dist_to_5y_low},
    "mgc_133_gross_margin_vs_3y_avg": {"inputs": ["gp", "revenue"], "func": mgc_133_gross_margin_vs_3y_avg},
    "mgc_134_op_margin_vs_3y_avg": {"inputs": ["opinc", "revenue"], "func": mgc_134_op_margin_vs_3y_avg},
    "mgc_135_net_margin_vs_3y_avg": {"inputs": ["netinc", "revenue"], "func": mgc_135_net_margin_vs_3y_avg},
    "mgc_136_gross_minus_net_margin_qoq_change": {"inputs": ["gp", "netinc", "revenue"], "func": mgc_136_gross_minus_net_margin_qoq_change},
    "mgc_137_op_minus_net_margin_qoq_change": {"inputs": ["opinc", "netinc", "revenue"], "func": mgc_137_op_minus_net_margin_qoq_change},
    "mgc_138_gross_margin_median_deviation_4q": {"inputs": ["gp", "revenue"], "func": mgc_138_gross_margin_median_deviation_4q},
    "mgc_139_op_margin_median_deviation_4q": {"inputs": ["opinc", "revenue"], "func": mgc_139_op_margin_median_deviation_4q},
    "mgc_140_net_margin_median_deviation_8q": {"inputs": ["netinc", "revenue"], "func": mgc_140_net_margin_median_deviation_8q},
    "mgc_141_sgna_ratio_yoy_change": {"inputs": ["sgna", "revenue"], "func": mgc_141_sgna_ratio_yoy_change},
    "mgc_142_rnd_ratio_qoq_change": {"inputs": ["rnd", "revenue"], "func": mgc_142_rnd_ratio_qoq_change},
    "mgc_143_depamor_ratio_yoy_change": {"inputs": ["depamor", "revenue"], "func": mgc_143_depamor_ratio_yoy_change},
    "mgc_144_sbcomp_ratio_yoy_change": {"inputs": ["sbcomp", "revenue"], "func": mgc_144_sbcomp_ratio_yoy_change},
    "mgc_145_intexp_ratio_qoq_change": {"inputs": ["intexp", "revenue"], "func": mgc_145_intexp_ratio_qoq_change},
    "mgc_146_margin_compression_composite_4q": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_146_margin_compression_composite_4q},
    "mgc_147_cost_ratio_composite_vs_4q_avg": {"inputs": ["cor", "opex", "sgna", "revenue"], "func": mgc_147_cost_ratio_composite_vs_4q_avg},
    "mgc_148_net_margin_expanding_pct_rank": {"inputs": ["netinc", "revenue"], "func": mgc_148_net_margin_expanding_pct_rank},
    "mgc_149_gross_margin_expanding_pct_rank": {"inputs": ["gp", "revenue"], "func": mgc_149_gross_margin_expanding_pct_rank},
    "mgc_150_all_margins_negative_flag": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_150_all_margins_negative_flag},
}
