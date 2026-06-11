"""
63_cash_burn — 3rd Derivatives (Features cbr_drv3_001-025)
Domain: rate of change of 2nd-derivative cash-burn features — convexity of burn
Asset class: US equities | Sharadar SF1 fundamentals (FUNDAMENTAL folder)
Each feature computes .diff(n), slope, or pct-change of a 2nd-derivative concept.
All features are backward-looking only; no forward information.

Quarterly cadence on daily index:
  1 quarter = 63 trading days, 1 year = 252 td.
  3rd-derivative features are highly sparse on a daily index — expected and correct.
  They capture whether the rate-of-change of the burn rate is itself changing.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2YR  = 504
_TD_3YR  = 756
_EPS     = 1e-9

# ── Alignment helper ──────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: All inputs to feature functions in this file are daily-frequency
    Series, forward-filled from the most recent quarterly Sharadar SF1 report
    known as of each date.  Functions look strictly backward.

    This helper re-aligns a quarterly Series onto a daily trading-day index
    using forward-fill, replicating what the pipeline already does upstream.
    It is provided for completeness; feature functions receive already-aligned
    daily Series and do NOT need to call this internally.
    """
    return q_series.reindex(daily_index).ffill()


# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


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
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def cbr_drv3_001_fcf_3rd_diff_qoq(fcf: pd.Series) -> pd.Series:
    """3rd-order QoQ difference of FCF: d/dt of burn acceleration.
    Non-zero = the rate of burn change is itself changing (convexity)."""
    d1 = fcf.diff(_TD_QTR)
    d2 = d1.diff(_TD_QTR)
    return d2.diff(_TD_QTR)


def cbr_drv3_002_fcf_4q_sum_3rd_diff(fcf: pd.Series) -> pd.Series:
    """3rd-order QoQ difference of trailing 4q FCF sum."""
    s4q = _rolling_sum(fcf, _TD_YEAR)
    d1  = s4q.diff(_TD_QTR)
    d2  = d1.diff(_TD_QTR)
    return d2.diff(_TD_QTR)


def cbr_drv3_003_ncfo_4q_sum_3rd_diff(ncfo: pd.Series) -> pd.Series:
    """3rd-order QoQ difference of trailing 4q NCFO sum."""
    s4q = _rolling_sum(ncfo, _TD_YEAR)
    d1  = s4q.diff(_TD_QTR)
    d2  = d1.diff(_TD_QTR)
    return d2.diff(_TD_QTR)


def cbr_drv3_004_cashnequiv_3rd_diff_qoq(cashnequiv: pd.Series) -> pd.Series:
    """3rd-order QoQ difference of cash balance (cash depletion convexity)."""
    d1 = cashnequiv.diff(_TD_QTR)
    d2 = d1.diff(_TD_QTR)
    return d2.diff(_TD_QTR)


def cbr_drv3_005_fcf_margin_3rd_diff(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """3rd-order QoQ difference of FCF margin (margin deterioration convexity)."""
    margin = _safe_div(fcf, revenue)
    d1     = margin.diff(_TD_QTR)
    d2     = d1.diff(_TD_QTR)
    return d2.diff(_TD_QTR)


def cbr_drv3_006_runway_3rd_diff(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """3rd-order QoQ difference of estimated runway quarters (runway crisis convexity)."""
    burn   = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway[runway < 0] = np.nan
    d1     = runway.diff(_TD_QTR)
    d2     = d1.diff(_TD_QTR)
    return d2.diff(_TD_QTR)


def cbr_drv3_007_fcf_yoy_change_diff_yoy(fcf: pd.Series) -> pd.Series:
    """YoY change in YoY FCF change (year-over-year convexity of deterioration)."""
    d1 = fcf.diff(_TD_YEAR)
    return d1.diff(_TD_YEAR)


def cbr_drv3_008_burn_accel_diff_yoy(fcf: pd.Series) -> pd.Series:
    """YoY change in burn acceleration (QoQ burn change): annual view of convexity."""
    burn  = (-fcf).where(fcf < 0, other=np.nan)
    accel = burn.diff(_TD_QTR)
    return accel.diff(_TD_YEAR)


def cbr_drv3_009_fcf_slope_diff_yoy(fcf: pd.Series) -> pd.Series:
    """YoY change in 4q OLS slope of FCF (is the trend slope changing shape)."""
    slope = _linslope(fcf, _TD_YEAR)
    return slope.diff(_TD_YEAR)


def cbr_drv3_010_cashnequiv_slope_diff_qoq(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in 4q OLS slope of cash balance (slope of cash trend accelerating)."""
    slope = _linslope(cashnequiv, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cbr_drv3_011_ncfo_slope_diff_qoq(ncfo: pd.Series) -> pd.Series:
    """QoQ change in 4q OLS slope of NCFO (operating cash trend accelerating down)."""
    slope = _linslope(ncfo, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cbr_drv3_012_fcf_zscore_2nd_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of FCF z-score (z-score velocity accelerating)."""
    z  = _zscore_rolling(fcf, _TD_YEAR)
    d1 = z.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_013_ncfo_margin_2nd_diff(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in QoQ NCFO margin change (margin deterioration convexity)."""
    margin = _safe_div(ncfo, revenue)
    d1     = margin.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_014_cashnequiv_depl_rate_2nd_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of cash depletion rate (depletion acceleration rate)."""
    depl = _safe_div(-cashnequiv.diff(_TD_QTR), cashnequiv.shift(_TD_QTR).abs())
    d1   = depl.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_015_ncfo_to_capex_2nd_diff(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of NCFO/capex coverage (coverage deterioration convexity)."""
    ratio = _safe_div(ncfo, capex.abs())
    d1    = ratio.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_016_burn_regime_score_2nd_diff(fcf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of burn regime score (distress regime convexity)."""
    fcf_rank  = 1.0 - fcf.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    cash_rank = 1.0 - cashnequiv.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    score     = fcf_rank * cash_rank
    d1        = score.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_017_fcf_ewm_trend_2nd_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of FCF EWM trend (momentum signal convexity)."""
    fast  = _ewm_mean(fcf, _TD_QTR)
    slow  = _ewm_mean(fcf, _TD_YEAR)
    trend = fast - slow
    d1    = trend.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_018_runway_slope_diff_qoq(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """QoQ change in OLS slope of runway (is the runway-trend slope itself bending)."""
    burn   = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway[runway < 0] = np.nan
    slope  = _linslope(runway, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cbr_drv3_019_cash_to_revenue_2nd_diff(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of cash-to-revenue ratio (liquidity cushion convexity)."""
    ratio = _safe_div(cashnequiv, revenue)
    d1    = ratio.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_020_fcf_neg_fraction_2nd_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of 4q negative-FCF fraction (persistence convexity)."""
    neg_frac = _rolling_mean((fcf < 0).astype(float), _TD_YEAR)
    d1       = neg_frac.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_021_fcf_drawdown_2nd_diff(fcf: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of FCF drawdown from 4q peak (trough-deepening convexity)."""
    peak = _rolling_max(fcf, _TD_YEAR)
    dd   = _safe_div(fcf - peak, peak.abs())
    d1   = dd.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_022_cashnequiv_zscore_2nd_diff(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of 8q cash z-score (cash distress convexity)."""
    z  = _zscore_rolling(cashnequiv, _TD_2YR)
    d1 = z.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_023_composite_burn_2nd_diff(fcf: pd.Series, cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of composite burn intensity (distress severity convexity)."""
    fcf_rank  = 1.0 - fcf.rolling(_TD_2YR,  min_periods=_TD_QTR).rank(pct=True)
    ncfo_rank = 1.0 - ncfo.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    peak      = cashnequiv.expanding(min_periods=1).max()
    cash_dd   = _safe_div(peak - cashnequiv, peak.abs()).clip(lower=0)
    composite = 0.5 * fcf_rank + 0.3 * ncfo_rank + 0.2 * cash_dd
    d1        = composite.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv3_024_fcf_4q_sum_yoy_2nd_diff(fcf: pd.Series) -> pd.Series:
    """YoY change in YoY-change of 4q FCF sum (annual burn-level convexity)."""
    s4q = _rolling_sum(fcf, _TD_YEAR)
    d1  = s4q.diff(_TD_YEAR)
    return d1.diff(_TD_YEAR)


def cbr_drv3_025_ncfo_margin_slope_diff_qoq(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in 4q OLS slope of NCFO margin (slope of margin trend accelerating)."""
    margin = _safe_div(ncfo, revenue)
    slope  = _linslope(margin, _TD_YEAR)
    return slope.diff(_TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

CASH_BURN_REGISTRY_3RD_DERIVATIVES = {
    "cbr_drv3_001_fcf_3rd_diff_qoq":             {"inputs": ["fcf"],                        "func": cbr_drv3_001_fcf_3rd_diff_qoq},
    "cbr_drv3_002_fcf_4q_sum_3rd_diff":          {"inputs": ["fcf"],                        "func": cbr_drv3_002_fcf_4q_sum_3rd_diff},
    "cbr_drv3_003_ncfo_4q_sum_3rd_diff":         {"inputs": ["ncfo"],                       "func": cbr_drv3_003_ncfo_4q_sum_3rd_diff},
    "cbr_drv3_004_cashnequiv_3rd_diff_qoq":      {"inputs": ["cashnequiv"],                 "func": cbr_drv3_004_cashnequiv_3rd_diff_qoq},
    "cbr_drv3_005_fcf_margin_3rd_diff":          {"inputs": ["fcf", "revenue"],             "func": cbr_drv3_005_fcf_margin_3rd_diff},
    "cbr_drv3_006_runway_3rd_diff":              {"inputs": ["cashnequiv", "fcf"],          "func": cbr_drv3_006_runway_3rd_diff},
    "cbr_drv3_007_fcf_yoy_change_diff_yoy":      {"inputs": ["fcf"],                        "func": cbr_drv3_007_fcf_yoy_change_diff_yoy},
    "cbr_drv3_008_burn_accel_diff_yoy":          {"inputs": ["fcf"],                        "func": cbr_drv3_008_burn_accel_diff_yoy},
    "cbr_drv3_009_fcf_slope_diff_yoy":           {"inputs": ["fcf"],                        "func": cbr_drv3_009_fcf_slope_diff_yoy},
    "cbr_drv3_010_cashnequiv_slope_diff_qoq":    {"inputs": ["cashnequiv"],                 "func": cbr_drv3_010_cashnequiv_slope_diff_qoq},
    "cbr_drv3_011_ncfo_slope_diff_qoq":          {"inputs": ["ncfo"],                       "func": cbr_drv3_011_ncfo_slope_diff_qoq},
    "cbr_drv3_012_fcf_zscore_2nd_diff":          {"inputs": ["fcf"],                        "func": cbr_drv3_012_fcf_zscore_2nd_diff},
    "cbr_drv3_013_ncfo_margin_2nd_diff":         {"inputs": ["ncfo", "revenue"],            "func": cbr_drv3_013_ncfo_margin_2nd_diff},
    "cbr_drv3_014_cashnequiv_depl_rate_2nd_diff": {"inputs": ["cashnequiv"],               "func": cbr_drv3_014_cashnequiv_depl_rate_2nd_diff},
    "cbr_drv3_015_ncfo_to_capex_2nd_diff":       {"inputs": ["ncfo", "capex"],             "func": cbr_drv3_015_ncfo_to_capex_2nd_diff},
    "cbr_drv3_016_burn_regime_score_2nd_diff":   {"inputs": ["fcf", "cashnequiv"],         "func": cbr_drv3_016_burn_regime_score_2nd_diff},
    "cbr_drv3_017_fcf_ewm_trend_2nd_diff":       {"inputs": ["fcf"],                        "func": cbr_drv3_017_fcf_ewm_trend_2nd_diff},
    "cbr_drv3_018_runway_slope_diff_qoq":        {"inputs": ["cashnequiv", "fcf"],          "func": cbr_drv3_018_runway_slope_diff_qoq},
    "cbr_drv3_019_cash_to_revenue_2nd_diff":     {"inputs": ["cashnequiv", "revenue"],      "func": cbr_drv3_019_cash_to_revenue_2nd_diff},
    "cbr_drv3_020_fcf_neg_fraction_2nd_diff":    {"inputs": ["fcf"],                        "func": cbr_drv3_020_fcf_neg_fraction_2nd_diff},
    "cbr_drv3_021_fcf_drawdown_2nd_diff":        {"inputs": ["fcf"],                        "func": cbr_drv3_021_fcf_drawdown_2nd_diff},
    "cbr_drv3_022_cashnequiv_zscore_2nd_diff":   {"inputs": ["cashnequiv"],                 "func": cbr_drv3_022_cashnequiv_zscore_2nd_diff},
    "cbr_drv3_023_composite_burn_2nd_diff":      {"inputs": ["fcf", "cashnequiv", "ncfo"],  "func": cbr_drv3_023_composite_burn_2nd_diff},
    "cbr_drv3_024_fcf_4q_sum_yoy_2nd_diff":      {"inputs": ["fcf"],                        "func": cbr_drv3_024_fcf_4q_sum_yoy_2nd_diff},
    "cbr_drv3_025_ncfo_margin_slope_diff_qoq":   {"inputs": ["ncfo", "revenue"],            "func": cbr_drv3_025_ncfo_margin_slope_diff_qoq},
}
