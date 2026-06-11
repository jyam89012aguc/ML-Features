"""
62_margin_compression — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative margin-compression features
Asset class: US equities | Sharadar SF1 fundamentals ONLY (no price/volume)
Each feature takes a 2nd-derivative concept and applies another .diff(n)/slope.
All features are backward-looking only; no forward information.

All inputs are daily-frequency pandas Series, forward-filled from the most
recent quarterly Sharadar SF1 report known as of each date.
Functions look strictly backward. No future information is used.

Quarterly cadence on daily index:
  1 quarter = 63 trading days  (QoQ diff = .diff(63) / .shift(63))
  1 year    = 252 trading days (YoY diff = .diff(252) / .shift(252))
  2 years   = 504 | 3 years = 756
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


# ── 3rd-Derivative Feature Functions ──────────────────────────────────────────

def mgc_drv3_001_gross_margin_qoq_jerk(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    Third derivative: 63-day diff of the 2nd-derivative gross margin QoQ velocity.
    Captures jerk — is the compression acceleration itself changing direction?
    """
    gm = _gross_margin(gp, revenue)
    qoq = gm.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_002_op_margin_qoq_jerk(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of QoQ op margin change (jerk of compression)."""
    om = _op_margin(opinc, revenue)
    qoq = om.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_003_net_margin_qoq_jerk(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of QoQ net margin change."""
    nm = _net_margin(netinc, revenue)
    qoq = nm.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_004_ebitda_margin_qoq_jerk(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of QoQ EBITDA margin change."""
    em = _ebitda_margin(ebitda, revenue)
    qoq = em.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_005_gross_margin_slope_4q_2nd_diff(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of (63-day diff of 4Q slope of gross margin).
    Third derivative via double-differencing the slope series.
    """
    gm = _gross_margin(gp, revenue)
    slope = _linslope(gm, _TD_YEAR)
    return slope.diff(_TD_QTR).diff(_TD_QTR)


def mgc_drv3_006_op_margin_slope_4q_2nd_diff(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day double-diff of 4Q slope of op margin."""
    om = _op_margin(opinc, revenue)
    slope = _linslope(om, _TD_YEAR)
    return slope.diff(_TD_QTR).diff(_TD_QTR)


def mgc_drv3_007_net_margin_slope_4q_2nd_diff(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day double-diff of 4Q slope of net margin."""
    nm = _net_margin(netinc, revenue)
    slope = _linslope(nm, _TD_YEAR)
    return slope.diff(_TD_QTR).diff(_TD_QTR)


def mgc_drv3_008_gross_margin_yoy_jerk(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """252-day diff of the 2nd-derivative gross margin YoY velocity."""
    gm = _gross_margin(gp, revenue)
    yoy = gm.diff(_TD_YEAR)
    vel = yoy.diff(_TD_YEAR)
    return vel.diff(_TD_YEAR)


def mgc_drv3_009_op_margin_yoy_jerk(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """252-day diff of the 2nd-derivative op margin YoY velocity."""
    om = _op_margin(opinc, revenue)
    yoy = om.diff(_TD_YEAR)
    vel = yoy.diff(_TD_YEAR)
    return vel.diff(_TD_YEAR)


def mgc_drv3_010_cor_ratio_qoq_jerk(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of QoQ COR ratio change (jerk of cost acceleration)."""
    cr = _cor_ratio(cor, revenue)
    qoq = cr.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_011_gross_margin_dd_jerk(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of the 2nd-derivative gross margin peak-drawdown velocity.
    Measures whether the drawdown gap is accelerating, decelerating, or reversing.
    """
    gm = _gross_margin(gp, revenue)
    pk = _rolling_max(gm, _TD_YEAR)
    dd = gm - pk
    vel = dd.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_012_op_margin_dd_jerk(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative op margin peak-drawdown velocity."""
    om = _op_margin(opinc, revenue)
    pk = _rolling_max(om, _TD_2Y)
    dd = om - pk
    vel = dd.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_013_net_margin_dd_jerk(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative net margin peak-drawdown velocity."""
    nm = _net_margin(netinc, revenue)
    pk = _rolling_max(nm, _TD_2Y)
    dd = nm - pk
    vel = dd.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_014_ebitda_margin_dd_jerk(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative EBITDA margin peak-drawdown velocity."""
    em = _ebitda_margin(ebitda, revenue)
    pk = _rolling_max(em, _TD_2Y)
    dd = em - pk
    vel = dd.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_015_gross_margin_ewm_cross_jerk(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """
    63-day diff of the 2nd-derivative EWM-cross velocity for gross margin.
    Captures whether the short/long EWM divergence is itself accelerating.
    """
    gm = _gross_margin(gp, revenue)
    cross = _ewm_mean(gm, _TD_QTR) - _ewm_mean(gm, _TD_YEAR)
    vel = cross.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_016_op_margin_ewm_cross_jerk(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative EWM-cross velocity for op margin."""
    om = _op_margin(opinc, revenue)
    cross = _ewm_mean(om, _TD_QTR) - _ewm_mean(om, _TD_YEAR)
    vel = cross.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_017_gross_margin_vs_4q_avg_jerk(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative (gross margin - 4Q avg) deviation velocity."""
    gm = _gross_margin(gp, revenue)
    dev = gm - _rolling_mean(gm, _TD_YEAR)
    vel = dev.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_018_op_margin_vs_4q_avg_jerk(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative (op margin - 4Q avg) deviation velocity."""
    om = _op_margin(opinc, revenue)
    dev = om - _rolling_mean(om, _TD_YEAR)
    vel = dev.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_019_gross_margin_zscore_jerk(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative gross margin 4Q z-score velocity."""
    gm = _gross_margin(gp, revenue)
    m = _rolling_mean(gm, _TD_YEAR)
    sd = _rolling_std(gm, _TD_YEAR)
    z = _safe_div(gm - m, sd)
    vel = z.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_020_op_margin_zscore_jerk(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative op margin 4Q z-score velocity."""
    om = _op_margin(opinc, revenue)
    m = _rolling_mean(om, _TD_YEAR)
    sd = _rolling_std(om, _TD_YEAR)
    z = _safe_div(om - m, sd)
    vel = z.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_021_sgna_ratio_qoq_jerk(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """Third derivative of QoQ SG&A ratio change."""
    sr = _sgna_ratio(sgna, revenue)
    qoq = sr.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_022_gross_op_spread_jerk(
    gp: pd.Series, opinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """Third derivative of (gross - op) margin spread QoQ change."""
    spread = _gross_margin(gp, revenue) - _op_margin(opinc, revenue)
    qoq = spread.diff(_TD_QTR)
    vel = qoq.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_023_net_margin_slope_8q_jerk(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """63-day diff of 2nd-derivative 8Q net margin slope velocity."""
    nm = _net_margin(netinc, revenue)
    slope = _linslope(nm, _TD_2Y)
    vel = slope.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


def mgc_drv3_024_ebit_margin_yoy_jerk(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """252-day diff of the 2nd-derivative EBIT margin YoY velocity."""
    em = _ebit_margin(ebit, revenue)
    yoy = em.diff(_TD_YEAR)
    vel = yoy.diff(_TD_YEAR)
    return vel.diff(_TD_YEAR)


def mgc_drv3_025_multi_contraction_score_jerk(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """
    63-day diff of 2nd-derivative multi-margin contraction score velocity.
    Captures whether the rate of broadening across margin lines is itself changing.
    """
    gm_c = ((_gross_margin(gp, revenue)).diff(_TD_QTR) < 0).astype(float)
    om_c = ((_op_margin(opinc, revenue)).diff(_TD_QTR) < 0).astype(float)
    em_c = ((_ebitda_margin(ebitda, revenue)).diff(_TD_QTR) < 0).astype(float)
    nm_c = ((_net_margin(netinc, revenue)).diff(_TD_QTR) < 0).astype(float)
    score = gm_c + om_c + em_c + nm_c
    vel = score.diff(_TD_QTR)
    return vel.diff(_TD_QTR)


# ── Registry ───────────────────────────────────────────────────────────────────

MARGIN_COMPRESSION_REGISTRY_3RD_DERIVATIVES = {
    "mgc_drv3_001_gross_margin_qoq_jerk": {"inputs": ["gp", "revenue"], "func": mgc_drv3_001_gross_margin_qoq_jerk},
    "mgc_drv3_002_op_margin_qoq_jerk": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_002_op_margin_qoq_jerk},
    "mgc_drv3_003_net_margin_qoq_jerk": {"inputs": ["netinc", "revenue"], "func": mgc_drv3_003_net_margin_qoq_jerk},
    "mgc_drv3_004_ebitda_margin_qoq_jerk": {"inputs": ["ebitda", "revenue"], "func": mgc_drv3_004_ebitda_margin_qoq_jerk},
    "mgc_drv3_005_gross_margin_slope_4q_2nd_diff": {"inputs": ["gp", "revenue"], "func": mgc_drv3_005_gross_margin_slope_4q_2nd_diff},
    "mgc_drv3_006_op_margin_slope_4q_2nd_diff": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_006_op_margin_slope_4q_2nd_diff},
    "mgc_drv3_007_net_margin_slope_4q_2nd_diff": {"inputs": ["netinc", "revenue"], "func": mgc_drv3_007_net_margin_slope_4q_2nd_diff},
    "mgc_drv3_008_gross_margin_yoy_jerk": {"inputs": ["gp", "revenue"], "func": mgc_drv3_008_gross_margin_yoy_jerk},
    "mgc_drv3_009_op_margin_yoy_jerk": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_009_op_margin_yoy_jerk},
    "mgc_drv3_010_cor_ratio_qoq_jerk": {"inputs": ["cor", "revenue"], "func": mgc_drv3_010_cor_ratio_qoq_jerk},
    "mgc_drv3_011_gross_margin_dd_jerk": {"inputs": ["gp", "revenue"], "func": mgc_drv3_011_gross_margin_dd_jerk},
    "mgc_drv3_012_op_margin_dd_jerk": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_012_op_margin_dd_jerk},
    "mgc_drv3_013_net_margin_dd_jerk": {"inputs": ["netinc", "revenue"], "func": mgc_drv3_013_net_margin_dd_jerk},
    "mgc_drv3_014_ebitda_margin_dd_jerk": {"inputs": ["ebitda", "revenue"], "func": mgc_drv3_014_ebitda_margin_dd_jerk},
    "mgc_drv3_015_gross_margin_ewm_cross_jerk": {"inputs": ["gp", "revenue"], "func": mgc_drv3_015_gross_margin_ewm_cross_jerk},
    "mgc_drv3_016_op_margin_ewm_cross_jerk": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_016_op_margin_ewm_cross_jerk},
    "mgc_drv3_017_gross_margin_vs_4q_avg_jerk": {"inputs": ["gp", "revenue"], "func": mgc_drv3_017_gross_margin_vs_4q_avg_jerk},
    "mgc_drv3_018_op_margin_vs_4q_avg_jerk": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_018_op_margin_vs_4q_avg_jerk},
    "mgc_drv3_019_gross_margin_zscore_jerk": {"inputs": ["gp", "revenue"], "func": mgc_drv3_019_gross_margin_zscore_jerk},
    "mgc_drv3_020_op_margin_zscore_jerk": {"inputs": ["opinc", "revenue"], "func": mgc_drv3_020_op_margin_zscore_jerk},
    "mgc_drv3_021_sgna_ratio_qoq_jerk": {"inputs": ["sgna", "revenue"], "func": mgc_drv3_021_sgna_ratio_qoq_jerk},
    "mgc_drv3_022_gross_op_spread_jerk": {"inputs": ["gp", "opinc", "revenue"], "func": mgc_drv3_022_gross_op_spread_jerk},
    "mgc_drv3_023_net_margin_slope_8q_jerk": {"inputs": ["netinc", "revenue"], "func": mgc_drv3_023_net_margin_slope_8q_jerk},
    "mgc_drv3_024_ebit_margin_yoy_jerk": {"inputs": ["ebit", "revenue"], "func": mgc_drv3_024_ebit_margin_yoy_jerk},
    "mgc_drv3_025_multi_contraction_score_jerk": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_drv3_025_multi_contraction_score_jerk},
}
