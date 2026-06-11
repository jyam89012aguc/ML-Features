"""
63_cash_burn — 2nd Derivatives (Features cbr_drv2_001-025)
Domain: rate of change of base cash-burn features — captures acceleration of burn
Asset class: US equities | Sharadar SF1 fundamentals (FUNDAMENTAL folder)
Each feature computes a .diff(n), slope, or pct-change of a base cash-burn concept.
All features are backward-looking only; no forward information.

Quarterly cadence on daily index:
  1 quarter = 63 trading days, 1 year = 252 td.
  Derivative features are sparse/stepwise because underlying data is quarterly.
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def cbr_drv2_001_fcf_qoq_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in QoQ-FCF-change (2nd difference): acceleration of FCF deterioration."""
    d1 = fcf.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv2_002_fcf_yoy_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in YoY FCF change (velocity of annual deterioration)."""
    d1 = fcf.diff(_TD_YEAR)
    return d1.diff(_TD_QTR)


def cbr_drv2_003_fcf_4q_sum_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in trailing 4q FCF sum (burn rate momentum)."""
    s4q = _rolling_sum(fcf, _TD_YEAR)
    return s4q.diff(_TD_QTR)


def cbr_drv2_004_fcf_4q_sum_diff_yoy(fcf: pd.Series) -> pd.Series:
    """YoY change in trailing 4q FCF sum (year-over-year burn rate shift)."""
    s4q = _rolling_sum(fcf, _TD_YEAR)
    return s4q.diff(_TD_YEAR)


def cbr_drv2_005_ncfo_4q_sum_diff_qoq(ncfo: pd.Series) -> pd.Series:
    """QoQ change in trailing 4q NCFO sum (operating burn momentum)."""
    s4q = _rolling_sum(ncfo, _TD_YEAR)
    return s4q.diff(_TD_QTR)


def cbr_drv2_006_cashnequiv_qoq_change_diff_qoq(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in QoQ cash balance change (cash burn acceleration)."""
    d1 = cashnequiv.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


def cbr_drv2_007_cash_depletion_rate_diff_qoq(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in quarterly cash depletion rate (speed of depletion accelerating)."""
    depl = _safe_div(-cashnequiv.diff(_TD_QTR), cashnequiv.shift(_TD_QTR).abs())
    return depl.diff(_TD_QTR)


def cbr_drv2_008_fcf_to_revenue_margin_diff_qoq(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in FCF margin (rate of FCF-margin deterioration)."""
    margin = _safe_div(fcf, revenue)
    return margin.diff(_TD_QTR)


def cbr_drv2_009_fcf_to_revenue_margin_diff_yoy(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in FCF margin (annual FCF-margin deterioration)."""
    margin = _safe_div(fcf, revenue)
    return margin.diff(_TD_YEAR)


def cbr_drv2_010_runway_qoq_diff(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """QoQ change in estimated runway (quarters): runway shrinking faster = negative."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway[runway < 0] = np.nan
    return runway.diff(_TD_QTR)


def cbr_drv2_011_runway_yoy_diff(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """YoY change in estimated runway (annual deterioration in cash cushion)."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway[runway < 0] = np.nan
    return runway.diff(_TD_YEAR)


def cbr_drv2_012_burn_acceleration_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in burn acceleration (third-order signal of burn escalation)."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    accel = burn.diff(_TD_QTR)
    return accel.diff(_TD_QTR)


def cbr_drv2_013_fcf_drawdown_from_4q_peak_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in FCF drawdown from 4q peak (deepening of FCF trough)."""
    peak = _rolling_max(fcf, _TD_YEAR)
    dd   = _safe_div(fcf - peak, peak.abs())
    return dd.diff(_TD_QTR)


def cbr_drv2_014_ncfo_to_capex_ratio_diff_qoq(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """QoQ change in NCFO/|capex| coverage ratio (worsening coverage rate)."""
    ratio = _safe_div(ncfo, capex.abs())
    return ratio.diff(_TD_QTR)


def cbr_drv2_015_fcf_trend_slope_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in 4q OLS slope of FCF (slope becoming more negative = accelerating)."""
    slope = _linslope(fcf, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cbr_drv2_016_fcf_zscore_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in 4q z-score of FCF (getting more statistically extreme)."""
    z = _zscore_rolling(fcf, _TD_YEAR)
    return z.diff(_TD_QTR)


def cbr_drv2_017_fcf_neg_fraction_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in 4q negative-FCF fraction (persistence increasing)."""
    neg_frac = _rolling_mean((fcf < 0).astype(float), _TD_YEAR)
    return neg_frac.diff(_TD_QTR)


def cbr_drv2_018_ncfo_4q_slope_diff_qoq(ncfo: pd.Series) -> pd.Series:
    """QoQ change in 4q OLS slope of NCFO."""
    slope = _linslope(ncfo, _TD_YEAR)
    return slope.diff(_TD_QTR)


def cbr_drv2_019_cashnequiv_zscore_diff_qoq(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in 8q z-score of cash balance (cash position getting more extreme)."""
    z = _zscore_rolling(cashnequiv, _TD_2YR)
    return z.diff(_TD_QTR)


def cbr_drv2_020_burn_regime_score_diff_qoq(fcf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in composite burn regime score (worsening distress regime)."""
    fcf_rank  = 1.0 - fcf.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    cash_rank = 1.0 - cashnequiv.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    score     = fcf_rank * cash_rank
    return score.diff(_TD_QTR)


def cbr_drv2_021_fcf_ewm_trend_diff_qoq(fcf: pd.Series) -> pd.Series:
    """QoQ change in FCF EWM trend (fast minus slow EWM becoming more negative)."""
    fast  = _ewm_mean(fcf, _TD_QTR)
    slow  = _ewm_mean(fcf, _TD_YEAR)
    trend = fast - slow
    return trend.diff(_TD_QTR)


def cbr_drv2_022_cash_runway_yrs_slope_4q(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """OLS slope of cash runway (years) over 4q window (trend in runway availability)."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    runway_q = _safe_div(cashnequiv, burn)
    runway_q[runway_q < 0] = np.nan
    runway_y = runway_q / 4.0
    return _linslope(runway_y, _TD_YEAR)


def cbr_drv2_023_cash_to_revenue_ratio_diff_qoq(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in cash-to-revenue ratio (cash position relative to revenue scale)."""
    ratio = _safe_div(cashnequiv, revenue)
    return ratio.diff(_TD_QTR)


def cbr_drv2_024_ncfo_margin_slope_4q(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of NCFO margin over 4 quarters (trending toward cash drain)."""
    margin = _safe_div(ncfo, revenue)
    return _linslope(margin, _TD_YEAR)


def cbr_drv2_025_composite_burn_diff_qoq(fcf: pd.Series, cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """QoQ change in composite burn intensity (50% FCF rank + 30% NCFO rank + 20% cash DD).
    Positive = composite distress worsening this quarter."""
    fcf_rank  = 1.0 - fcf.rolling(_TD_2YR,  min_periods=_TD_QTR).rank(pct=True)
    ncfo_rank = 1.0 - ncfo.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    peak      = cashnequiv.expanding(min_periods=1).max()
    cash_dd   = _safe_div(peak - cashnequiv, peak.abs()).clip(lower=0)
    composite = 0.5 * fcf_rank + 0.3 * ncfo_rank + 0.2 * cash_dd
    return composite.diff(_TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

CASH_BURN_REGISTRY_2ND_DERIVATIVES = {
    "cbr_drv2_001_fcf_qoq_diff_qoq":               {"inputs": ["fcf"],                     "func": cbr_drv2_001_fcf_qoq_diff_qoq},
    "cbr_drv2_002_fcf_yoy_diff_qoq":               {"inputs": ["fcf"],                     "func": cbr_drv2_002_fcf_yoy_diff_qoq},
    "cbr_drv2_003_fcf_4q_sum_diff_qoq":            {"inputs": ["fcf"],                     "func": cbr_drv2_003_fcf_4q_sum_diff_qoq},
    "cbr_drv2_004_fcf_4q_sum_diff_yoy":            {"inputs": ["fcf"],                     "func": cbr_drv2_004_fcf_4q_sum_diff_yoy},
    "cbr_drv2_005_ncfo_4q_sum_diff_qoq":           {"inputs": ["ncfo"],                    "func": cbr_drv2_005_ncfo_4q_sum_diff_qoq},
    "cbr_drv2_006_cashnequiv_qoq_change_diff_qoq": {"inputs": ["cashnequiv"],              "func": cbr_drv2_006_cashnequiv_qoq_change_diff_qoq},
    "cbr_drv2_007_cash_depletion_rate_diff_qoq":   {"inputs": ["cashnequiv"],              "func": cbr_drv2_007_cash_depletion_rate_diff_qoq},
    "cbr_drv2_008_fcf_to_revenue_margin_diff_qoq": {"inputs": ["fcf", "revenue"],          "func": cbr_drv2_008_fcf_to_revenue_margin_diff_qoq},
    "cbr_drv2_009_fcf_to_revenue_margin_diff_yoy": {"inputs": ["fcf", "revenue"],          "func": cbr_drv2_009_fcf_to_revenue_margin_diff_yoy},
    "cbr_drv2_010_runway_qoq_diff":                {"inputs": ["cashnequiv", "fcf"],       "func": cbr_drv2_010_runway_qoq_diff},
    "cbr_drv2_011_runway_yoy_diff":                {"inputs": ["cashnequiv", "fcf"],       "func": cbr_drv2_011_runway_yoy_diff},
    "cbr_drv2_012_burn_acceleration_diff_qoq":     {"inputs": ["fcf"],                     "func": cbr_drv2_012_burn_acceleration_diff_qoq},
    "cbr_drv2_013_fcf_drawdown_peak_diff_qoq":     {"inputs": ["fcf"],                     "func": cbr_drv2_013_fcf_drawdown_from_4q_peak_diff_qoq},
    "cbr_drv2_014_ncfo_to_capex_ratio_diff_qoq":   {"inputs": ["ncfo", "capex"],           "func": cbr_drv2_014_ncfo_to_capex_ratio_diff_qoq},
    "cbr_drv2_015_fcf_trend_slope_diff_qoq":       {"inputs": ["fcf"],                     "func": cbr_drv2_015_fcf_trend_slope_diff_qoq},
    "cbr_drv2_016_fcf_zscore_diff_qoq":            {"inputs": ["fcf"],                     "func": cbr_drv2_016_fcf_zscore_diff_qoq},
    "cbr_drv2_017_fcf_neg_fraction_diff_qoq":      {"inputs": ["fcf"],                     "func": cbr_drv2_017_fcf_neg_fraction_diff_qoq},
    "cbr_drv2_018_ncfo_4q_slope_diff_qoq":         {"inputs": ["ncfo"],                    "func": cbr_drv2_018_ncfo_4q_slope_diff_qoq},
    "cbr_drv2_019_cashnequiv_zscore_diff_qoq":     {"inputs": ["cashnequiv"],              "func": cbr_drv2_019_cashnequiv_zscore_diff_qoq},
    "cbr_drv2_020_burn_regime_score_diff_qoq":     {"inputs": ["fcf", "cashnequiv"],       "func": cbr_drv2_020_burn_regime_score_diff_qoq},
    "cbr_drv2_021_fcf_ewm_trend_diff_qoq":         {"inputs": ["fcf"],                     "func": cbr_drv2_021_fcf_ewm_trend_diff_qoq},
    "cbr_drv2_022_cash_runway_yrs_slope_4q":       {"inputs": ["cashnequiv", "fcf"],       "func": cbr_drv2_022_cash_runway_yrs_slope_4q},
    "cbr_drv2_023_cash_to_revenue_ratio_diff_qoq": {"inputs": ["cashnequiv", "revenue"],   "func": cbr_drv2_023_cash_to_revenue_ratio_diff_qoq},
    "cbr_drv2_024_ncfo_margin_slope_4q":           {"inputs": ["ncfo", "revenue"],         "func": cbr_drv2_024_ncfo_margin_slope_4q},
    "cbr_drv2_025_composite_burn_diff_qoq":        {"inputs": ["fcf", "cashnequiv", "ncfo"], "func": cbr_drv2_025_composite_burn_diff_qoq},
}
