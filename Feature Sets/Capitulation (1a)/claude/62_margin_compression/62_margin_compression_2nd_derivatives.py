"""
62_margin_compression — 2nd Derivatives (Features drv2_001-025)
Domain: rate of change of base margin-compression features
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Each feature computes a .diff(n), slope, or pct-change of a base-feature concept.
All features are backward-looking only; no forward information.

All inputs are daily-frequency pandas Series, forward-filled from the most
recent quarterly Sharadar SF1 report known as of each date.
Functions look strictly backward. No future information is used.

Quarterly cadence on daily index:
  1 quarter = 63 trading days  (QoQ diff = .diff(63) / .shift(63))
  1 year    = 252 trading days (YoY diff = .diff(252) / .shift(252))
  2 years   = 504 | 3 years = 756 | 5 years = 1260
Note: on a forward-filled quarterly series, derivative steps are sparse
(change only ~4x/year) — this is expected and correct.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_QTR  = 63
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope (scalar helper, raw=False)."""
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

def _ebit_margin(ebit, revenue):
    return _safe_div(ebit, revenue)

def _cor_ratio(cor, revenue):
    return _safe_div(cor, revenue)

def _sgna_ratio(sgna, revenue):
    return _safe_div(sgna, revenue)

def _opex_ratio(opex, revenue):
    return _safe_div(opex, revenue)


# ── 2nd-Derivative Feature Functions ──────────────────────────────────────────

def mgc_drv2_001_gross_margin_qoq_velocity(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day first diff of the QoQ gross margin change — acceleration of gross
    margin compression. Negative = compression is speeding up.
    """
    gm = _gross_margin(gp, revenue)
    qoq = gm.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_002_op_margin_qoq_velocity(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day first diff of the QoQ operating margin change (acceleration)."""
    om = _op_margin(opinc, revenue)
    qoq = om.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_003_net_margin_qoq_velocity(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day first diff of the QoQ net margin change (acceleration)."""
    nm = _net_margin(netinc, revenue)
    qoq = nm.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_004_ebitda_margin_qoq_velocity(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day first diff of the QoQ EBITDA margin change (acceleration)."""
    em = _ebitda_margin(ebitda, revenue)
    qoq = em.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_005_gross_margin_yoy_velocity(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """252-day first diff of the YoY gross margin change (annual pace acceleration)."""
    gm = _gross_margin(gp, revenue)
    yoy = gm.diff(_TD_YEAR)
    return yoy.diff(_TD_YEAR)


def mgc_drv2_006_op_margin_yoy_velocity(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """252-day first diff of the YoY op margin change."""
    om = _op_margin(opinc, revenue)
    yoy = om.diff(_TD_YEAR)
    return yoy.diff(_TD_YEAR)


def mgc_drv2_007_gross_margin_slope_4q_diff(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of the 4Q OLS slope of gross margin — acceleration of the trend.
    Increasingly negative = structural deterioration accelerating.
    """
    gm = _gross_margin(gp, revenue)
    slope = _linslope(gm, _TD_YEAR)
    return slope.diff(_TD_QTR)


def mgc_drv2_008_op_margin_slope_4q_diff(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 4Q OLS slope of op margin."""
    om = _op_margin(opinc, revenue)
    slope = _linslope(om, _TD_YEAR)
    return slope.diff(_TD_QTR)


def mgc_drv2_009_net_margin_slope_4q_diff(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 4Q OLS slope of net margin."""
    nm = _net_margin(netinc, revenue)
    slope = _linslope(nm, _TD_YEAR)
    return slope.diff(_TD_QTR)


def mgc_drv2_010_cor_ratio_qoq_velocity(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day first diff of QoQ COR ratio change — acceleration of cost-ratio
    deterioration (mirror of gross margin acceleration).
    """
    cr = _cor_ratio(cor, revenue)
    qoq = cr.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_011_gross_margin_vs_4q_avg_diff(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of (gross margin - 4Q avg) deviation — velocity of divergence
    from the rolling mean.
    """
    gm = _gross_margin(gp, revenue)
    dev = gm - _rolling_mean(gm, _TD_YEAR)
    return dev.diff(_TD_QTR)


def mgc_drv2_012_op_margin_vs_4q_avg_diff(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of (op margin - 4Q avg) deviation."""
    om = _op_margin(opinc, revenue)
    dev = om - _rolling_mean(om, _TD_YEAR)
    return dev.diff(_TD_QTR)


def mgc_drv2_013_gross_margin_dd_velocity(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of gross margin drawdown from 4Q peak — acceleration of the
    gap widening below prior peak.
    """
    gm = _gross_margin(gp, revenue)
    pk = _rolling_max(gm, _TD_YEAR)
    dd = gm - pk
    return dd.diff(_TD_QTR)


def mgc_drv2_014_op_margin_dd_velocity(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of op margin drawdown from 8Q peak."""
    om = _op_margin(opinc, revenue)
    pk = _rolling_max(om, _TD_2Y)
    dd = om - pk
    return dd.diff(_TD_QTR)


def mgc_drv2_015_net_margin_dd_velocity(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of net margin drawdown from 8Q peak."""
    nm = _net_margin(netinc, revenue)
    pk = _rolling_max(nm, _TD_2Y)
    dd = nm - pk
    return dd.diff(_TD_QTR)


def mgc_drv2_016_ebitda_margin_dd_velocity(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of EBITDA margin drawdown from 8Q peak."""
    em = _ebitda_margin(ebitda, revenue)
    pk = _rolling_max(em, _TD_2Y)
    dd = em - pk
    return dd.diff(_TD_QTR)


def mgc_drv2_017_gross_margin_ewm_cross_diff(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of (EWM-fast minus EWM-slow) of gross margin.
    Accelerating negative = short-term deterioration increasing relative to trend.
    """
    gm = _gross_margin(gp, revenue)
    cross = _ewm_mean(gm, _TD_QTR) - _ewm_mean(gm, _TD_YEAR)
    return cross.diff(_TD_QTR)


def mgc_drv2_018_op_margin_ewm_cross_diff(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of EWM-fast minus EWM-slow of op margin."""
    om = _op_margin(opinc, revenue)
    cross = _ewm_mean(om, _TD_QTR) - _ewm_mean(om, _TD_YEAR)
    return cross.diff(_TD_QTR)


def mgc_drv2_019_multi_contraction_score_diff(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    63-day diff of multi-margin contraction score (count of lines contracting QoQ).
    Rising = broader deterioration spreading to more margin lines.
    """
    gm_c = ((_gross_margin(gp, revenue)).diff(_TD_QTR) < 0).astype(float)
    om_c = ((_op_margin(opinc, revenue)).diff(_TD_QTR) < 0).astype(float)
    em_c = ((_ebitda_margin(ebitda, revenue)).diff(_TD_QTR) < 0).astype(float)
    nm_c = ((_net_margin(netinc, revenue)).diff(_TD_QTR) < 0).astype(float)
    score = gm_c + om_c + em_c + nm_c
    return score.diff(_TD_QTR)


def mgc_drv2_020_gross_margin_zscore_diff(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of rolling 4Q z-score of gross margin.
    Accelerating negative = statistical distress deepening.
    """
    gm = _gross_margin(gp, revenue)
    m = _rolling_mean(gm, _TD_YEAR)
    sd = _rolling_std(gm, _TD_YEAR)
    z = _safe_div(gm - m, sd)
    return z.diff(_TD_QTR)


def mgc_drv2_021_op_margin_zscore_diff(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of rolling 4Q z-score of operating margin."""
    om = _op_margin(opinc, revenue)
    m = _rolling_mean(om, _TD_YEAR)
    sd = _rolling_std(om, _TD_YEAR)
    z = _safe_div(om - m, sd)
    return z.diff(_TD_QTR)


def mgc_drv2_022_sgna_ratio_qoq_velocity(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of QoQ SG&A ratio change — acceleration of SG&A burden."""
    sr = _sgna_ratio(sgna, revenue)
    qoq = sr.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_023_gross_op_spread_qoq_velocity(
    gp: pd.Series, opinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    63-day diff of QoQ (gross - op) margin spread change.
    Accelerating positive = overhead eroding gross profit increasingly faster.
    """
    spread = _gross_margin(gp, revenue) - _op_margin(opinc, revenue)
    qoq = spread.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def mgc_drv2_024_net_margin_slope_8q_diff(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 8Q OLS slope of net margin (acceleration of long-trend)."""
    nm = _net_margin(netinc, revenue)
    slope = _linslope(nm, _TD_2Y)
    return slope.diff(_TD_QTR)


def mgc_drv2_025_ebit_margin_yoy_velocity(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """252-day diff of the YoY EBIT margin change (annual pace of EBIT erosion)."""
    em = _ebit_margin(ebit, revenue)
    yoy = em.diff(_TD_YEAR)
    return yoy.diff(_TD_YEAR)


# ── Registry ───────────────────────────────────────────────────────────────────

MARGIN_COMPRESSION_REGISTRY_2ND_DERIVATIVES = {
    "mgc_drv2_001_gross_margin_qoq_velocity": {"inputs": ["gp", "revenue"], "func": mgc_drv2_001_gross_margin_qoq_velocity},
    "mgc_drv2_002_op_margin_qoq_velocity": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_002_op_margin_qoq_velocity},
    "mgc_drv2_003_net_margin_qoq_velocity": {"inputs": ["netinc", "revenue"], "func": mgc_drv2_003_net_margin_qoq_velocity},
    "mgc_drv2_004_ebitda_margin_qoq_velocity": {"inputs": ["ebitda", "revenue"], "func": mgc_drv2_004_ebitda_margin_qoq_velocity},
    "mgc_drv2_005_gross_margin_yoy_velocity": {"inputs": ["gp", "revenue"], "func": mgc_drv2_005_gross_margin_yoy_velocity},
    "mgc_drv2_006_op_margin_yoy_velocity": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_006_op_margin_yoy_velocity},
    "mgc_drv2_007_gross_margin_slope_4q_diff": {"inputs": ["gp", "revenue"], "func": mgc_drv2_007_gross_margin_slope_4q_diff},
    "mgc_drv2_008_op_margin_slope_4q_diff": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_008_op_margin_slope_4q_diff},
    "mgc_drv2_009_net_margin_slope_4q_diff": {"inputs": ["netinc", "revenue"], "func": mgc_drv2_009_net_margin_slope_4q_diff},
    "mgc_drv2_010_cor_ratio_qoq_velocity": {"inputs": ["cor", "revenue"], "func": mgc_drv2_010_cor_ratio_qoq_velocity},
    "mgc_drv2_011_gross_margin_vs_4q_avg_diff": {"inputs": ["gp", "revenue"], "func": mgc_drv2_011_gross_margin_vs_4q_avg_diff},
    "mgc_drv2_012_op_margin_vs_4q_avg_diff": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_012_op_margin_vs_4q_avg_diff},
    "mgc_drv2_013_gross_margin_dd_velocity": {"inputs": ["gp", "revenue"], "func": mgc_drv2_013_gross_margin_dd_velocity},
    "mgc_drv2_014_op_margin_dd_velocity": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_014_op_margin_dd_velocity},
    "mgc_drv2_015_net_margin_dd_velocity": {"inputs": ["netinc", "revenue"], "func": mgc_drv2_015_net_margin_dd_velocity},
    "mgc_drv2_016_ebitda_margin_dd_velocity": {"inputs": ["ebitda", "revenue"], "func": mgc_drv2_016_ebitda_margin_dd_velocity},
    "mgc_drv2_017_gross_margin_ewm_cross_diff": {"inputs": ["gp", "revenue"], "func": mgc_drv2_017_gross_margin_ewm_cross_diff},
    "mgc_drv2_018_op_margin_ewm_cross_diff": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_018_op_margin_ewm_cross_diff},
    "mgc_drv2_019_multi_contraction_score_diff": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_drv2_019_multi_contraction_score_diff},
    "mgc_drv2_020_gross_margin_zscore_diff": {"inputs": ["gp", "revenue"], "func": mgc_drv2_020_gross_margin_zscore_diff},
    "mgc_drv2_021_op_margin_zscore_diff": {"inputs": ["opinc", "revenue"], "func": mgc_drv2_021_op_margin_zscore_diff},
    "mgc_drv2_022_sgna_ratio_qoq_velocity": {"inputs": ["sgna", "revenue"], "func": mgc_drv2_022_sgna_ratio_qoq_velocity},
    "mgc_drv2_023_gross_op_spread_qoq_velocity": {"inputs": ["gp", "opinc", "revenue"], "func": mgc_drv2_023_gross_op_spread_qoq_velocity},
    "mgc_drv2_024_net_margin_slope_8q_diff": {"inputs": ["netinc", "revenue"], "func": mgc_drv2_024_net_margin_slope_8q_diff},
    "mgc_drv2_025_ebit_margin_yoy_velocity": {"inputs": ["ebit", "revenue"], "func": mgc_drv2_025_ebit_margin_yoy_velocity},
}
