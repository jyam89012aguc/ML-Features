"""
63_cash_burn — Base Features 001-075
Domain: negative free cash flow, operating cash burn, cash runway depletion
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
_TD_YEAR = 252          # trading days per year
_TD_HALF = 126          # half-year
_TD_QTR  = 63           # one quarter
_TD_2YR  = 504
_TD_3YR  = 756
_TD_5YR  = 1260
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


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Raw FCF level and sign ---

def cbr_001_fcf_level(fcf: pd.Series) -> pd.Series:
    """Raw free cash flow level (forward-filled quarterly, on daily index)."""
    return fcf.copy()


def cbr_002_fcf_negative_flag(fcf: pd.Series) -> pd.Series:
    """1 if FCF is negative (burning cash), 0 otherwise."""
    return (fcf < 0).astype(float)


def cbr_003_fcf_4q_rolling_sum(fcf: pd.Series) -> pd.Series:
    """Trailing 4-quarter (1-year, 252 td) sum of FCF — annual burn total."""
    return _rolling_sum(fcf, _TD_YEAR)


def cbr_004_fcf_8q_rolling_sum(fcf: pd.Series) -> pd.Series:
    """Trailing 8-quarter (2-year, 504 td) sum of FCF."""
    return _rolling_sum(fcf, _TD_2YR)


def cbr_005_ncfo_level(ncfo: pd.Series) -> pd.Series:
    """Raw net cash from operations (quarterly, daily-aligned)."""
    return ncfo.copy()


def cbr_006_ncfo_negative_flag(ncfo: pd.Series) -> pd.Series:
    """1 if operating cash flow is negative."""
    return (ncfo < 0).astype(float)


def cbr_007_ncfo_4q_sum(ncfo: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of operating cash flow."""
    return _rolling_sum(ncfo, _TD_YEAR)


def cbr_008_capex_level(capex: pd.Series) -> pd.Series:
    """Raw capex level (typically negative in SF1; magnitude = investment)."""
    return capex.copy()


def cbr_009_capex_4q_sum(capex: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of capex."""
    return _rolling_sum(capex, _TD_YEAR)


def cbr_010_ncf_level(ncf: pd.Series) -> pd.Series:
    """Net change in cash (ncf) — total cash flow net of all activities."""
    return ncf.copy()


def cbr_011_ncf_negative_flag(ncf: pd.Series) -> pd.Series:
    """1 if net cash flow is negative (cash balance declining)."""
    return (ncf < 0).astype(float)


def cbr_012_ncf_4q_sum(ncf: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of net cash change."""
    return _rolling_sum(ncf, _TD_YEAR)


# --- Group B (013-025): QoQ and YoY FCF changes ---

def cbr_013_fcf_qoq_change(fcf: pd.Series) -> pd.Series:
    """QoQ change in FCF (diff over 63 trading days = one quarter)."""
    return fcf.diff(_TD_QTR)


def cbr_014_fcf_yoy_change(fcf: pd.Series) -> pd.Series:
    """YoY change in FCF (diff over 252 trading days)."""
    return fcf.diff(_TD_YEAR)


def cbr_015_fcf_qoq_pct_change(fcf: pd.Series) -> pd.Series:
    """QoQ percent change in FCF."""
    return _safe_div(fcf.diff(_TD_QTR), fcf.shift(_TD_QTR).abs())


def cbr_016_fcf_yoy_pct_change(fcf: pd.Series) -> pd.Series:
    """YoY percent change in FCF."""
    return _safe_div(fcf.diff(_TD_YEAR), fcf.shift(_TD_YEAR).abs())


def cbr_017_ncfo_qoq_change(ncfo: pd.Series) -> pd.Series:
    """QoQ change in operating cash flow."""
    return ncfo.diff(_TD_QTR)


def cbr_018_ncfo_yoy_change(ncfo: pd.Series) -> pd.Series:
    """YoY change in operating cash flow."""
    return ncfo.diff(_TD_YEAR)


def cbr_019_ncfo_qoq_pct_change(ncfo: pd.Series) -> pd.Series:
    """QoQ percent change in operating cash flow."""
    return _safe_div(ncfo.diff(_TD_QTR), ncfo.shift(_TD_QTR).abs())


def cbr_020_ncfo_yoy_pct_change(ncfo: pd.Series) -> pd.Series:
    """YoY percent change in operating cash flow."""
    return _safe_div(ncfo.diff(_TD_YEAR), ncfo.shift(_TD_YEAR).abs())


def cbr_021_capex_qoq_change(capex: pd.Series) -> pd.Series:
    """QoQ change in capex (rising capex while burning cash intensifies burn)."""
    return capex.diff(_TD_QTR)


def cbr_022_capex_yoy_change(capex: pd.Series) -> pd.Series:
    """YoY change in capex."""
    return capex.diff(_TD_YEAR)


def cbr_023_cashnequiv_qoq_change(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in cash & equivalents balance."""
    return cashnequiv.diff(_TD_QTR)


def cbr_024_cashnequiv_yoy_change(cashnequiv: pd.Series) -> pd.Series:
    """YoY change in cash & equivalents balance."""
    return cashnequiv.diff(_TD_YEAR)


def cbr_025_cashnequiv_2yr_change(cashnequiv: pd.Series) -> pd.Series:
    """2-year change in cash balance (multi-year depletion signal)."""
    return cashnequiv.diff(_TD_2YR)


# --- Group C (026-036): Burn rate and runway estimation ---

def cbr_026_quarterly_burn_rate(fcf: pd.Series) -> pd.Series:
    """Quarterly burn rate: negative FCF magnitude per quarter.
    Positive = burning, negative = generating.  = -FCF when FCF < 0, else NaN."""
    burn = -fcf
    burn[fcf >= 0] = np.nan
    return burn


def cbr_027_annual_burn_rate(fcf: pd.Series) -> pd.Series:
    """Annual burn rate: trailing 4-quarter average burn (-FCF, cash-burn periods only).
    Periods with positive 4q sum are set to NaN (no burn)."""
    fcf4q = _rolling_sum(fcf, _TD_YEAR)
    burn = -fcf4q
    burn[fcf4q >= 0] = np.nan
    return burn


def cbr_028_cash_runway_quarters(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Estimated cash runway in quarters: cash / quarterly burn rate.
    Returns NaN when FCF >= 0 (not burning) — runway is undefined/infinite."""
    burn = -fcf
    runway = _safe_div(cashnequiv, burn)
    runway[fcf >= 0] = np.nan
    runway[runway < 0] = np.nan   # cash also negative => undefined
    return runway


def cbr_029_cash_runway_years(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Estimated cash runway in years (runway_quarters / 4)."""
    rq = cbr_028_cash_runway_quarters(cashnequiv, fcf)
    return rq / 4.0


def cbr_030_cash_runway_4q_avg_burn(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Runway using trailing 4-quarter average burn rate as denominator."""
    avg_burn = -_rolling_mean(fcf, _TD_YEAR)
    runway = _safe_div(cashnequiv, avg_burn)
    runway[avg_burn <= 0] = np.nan
    return runway


def cbr_031_cash_runway_ncfo_based(cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Runway using operating cash outflow as burn proxy."""
    burn = -ncfo
    runway = _safe_div(cashnequiv, burn)
    runway[ncfo >= 0] = np.nan
    runway[runway < 0] = np.nan
    return runway


def cbr_032_runway_declining_flag(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if estimated runway shortened QoQ (burn worsening or cash declining)."""
    rw = cbr_028_cash_runway_quarters(cashnequiv, fcf)
    return (rw.diff(_TD_QTR) < 0).astype(float)


def cbr_033_cash_to_annual_burn_ratio(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Cash balance divided by trailing annual burn (4q sum).
    Measures how many years of cash remain at current burn pace."""
    annual_burn = -_rolling_sum(fcf, _TD_YEAR)
    ratio = _safe_div(cashnequiv, annual_burn)
    ratio[annual_burn <= 0] = np.nan
    return ratio


def cbr_034_burn_acceleration(fcf: pd.Series) -> pd.Series:
    """QoQ change in quarterly burn rate (negative FCF worsening = positive accel)."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    return burn.diff(_TD_QTR)


def cbr_035_annual_burn_pct_rank_8q(fcf: pd.Series) -> pd.Series:
    """Percentile rank of trailing 4-quarter FCF sum (annual burn) within 8-quarter window.
    Low rank (near 0) signals the annual FCF total is at its worst level in 2 years."""
    burn4q = _rolling_sum(fcf, _TD_YEAR)
    return burn4q.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 2)).rank(pct=True)


def cbr_036_burn_rate_zscore_8q(fcf: pd.Series) -> pd.Series:
    """Z-score of quarterly FCF over trailing 8 quarters (504 td)."""
    return _zscore_rolling(fcf, _TD_2YR)


# --- Group D (037-048): FCF relative to revenue and operations ---

def cbr_037_fcf_to_revenue(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """FCF margin: FCF / revenue (negative = burning relative to revenue scale)."""
    return _safe_div(fcf, revenue)


def cbr_038_ncfo_to_revenue(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating cash flow margin: NCFO / revenue."""
    return _safe_div(ncfo, revenue)


def cbr_039_capex_to_revenue(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Capex intensity: |capex| / revenue."""
    return _safe_div(capex.abs(), revenue)


def cbr_040_fcf_margin_pct_rank_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of FCF margin (FCF/revenue) within trailing 8-quarter window.
    Low rank signals FCF margin is at its worst level in 2 years."""
    margin = _safe_div(fcf, revenue)
    return margin.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 2)).rank(pct=True)


def cbr_041_fcf_margin_zscore_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of FCF margin (FCF/revenue) within trailing 8-quarter (504-day) window.
    Negative z-score signals FCF margin is well below its 2-year distribution."""
    margin = _safe_div(fcf, revenue)
    return _zscore_rolling(margin, _TD_2YR)


def cbr_042_ncfo_minus_capex_spread(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """NCFO - |capex|: how much operating cash flow exceeds investment spending.
    Negative = operating cash insufficient to cover capex (pure burn signal)."""
    return ncfo - capex.abs()


def cbr_043_ncfo_capex_coverage_ratio(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """NCFO / |capex|: coverage of capex by operating cash. <1 = undercovered."""
    return _safe_div(ncfo, capex.abs())


def cbr_044_burn_relative_to_revenue_4q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 4q FCF sum / trailing 4q revenue sum (annual FCF margin)."""
    return _safe_div(_rolling_sum(fcf, _TD_YEAR), _rolling_sum(revenue, _TD_YEAR))


def cbr_045_fcf_margin_drawdown_from_4q_peak(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """FCF margin (FCF/revenue) drawdown from its trailing 4-quarter (252-day) peak.
    Measures how far current FCF margin has fallen from its recent best."""
    margin = _safe_div(fcf, revenue)
    peak = _rolling_max(margin, _TD_YEAR)
    return _safe_div(margin - peak, peak.abs())


def cbr_046_cash_to_revenue_ratio(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """Cash balance / quarterly revenue (months of revenue in cash)."""
    return _safe_div(cashnequiv, revenue)


def cbr_047_cash_to_revenue_yoy_change(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in cash-to-revenue ratio."""
    ratio = _safe_div(cashnequiv, revenue)
    return ratio.diff(_TD_YEAR)


def cbr_048_sbcomp_adjusted_fcf(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """FCF adjusted by stripping out SBC add-back: fcf - sbcomp.
    Stock-based comp inflates reported NCFO; this is a stricter burn measure."""
    return fcf - sbcomp.abs()


# --- Group E (049-060): Cash balance depletion and persistence ---

def cbr_049_cashnequiv_level(cashnequiv: pd.Series) -> pd.Series:
    """Raw cash & equivalents balance level."""
    return cashnequiv.copy()


def cbr_050_cashnequiv_drawdown_from_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash drawdown from trailing 4-quarter (252 td) peak cash balance."""
    peak = _rolling_max(cashnequiv, _TD_YEAR)
    return _safe_div(cashnequiv - peak, peak)


def cbr_051_cashnequiv_drawdown_from_2yr_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash drawdown from 2-year peak cash balance."""
    peak = _rolling_max(cashnequiv, _TD_2YR)
    return _safe_div(cashnequiv - peak, peak)


def cbr_052_cashnequiv_drawdown_from_alltime_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash drawdown from all-time (expanding) peak cash balance."""
    peak = cashnequiv.expanding(min_periods=1).max()
    return _safe_div(cashnequiv - peak, peak)


def cbr_053_consecutive_neg_fcf_quarters(fcf: pd.Series) -> pd.Series:
    """Estimated consecutive quarters of negative FCF (rolling 252-td window count)."""
    neg = (fcf < 0).astype(float)
    # count of negative-FCF days in trailing year / 63 gives rough quarters
    return _rolling_sum(neg, _TD_YEAR) / _TD_QTR


def cbr_054_consecutive_neg_ncfo_quarters(ncfo: pd.Series) -> pd.Series:
    """Estimated consecutive quarters of negative NCFO."""
    neg = (ncfo < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR) / _TD_QTR


def cbr_055_cash_depletion_rate_qoq(cashnequiv: pd.Series) -> pd.Series:
    """Quarterly cash depletion rate: -(QoQ change) / prior cash balance.
    Positive = depleting, negative = accumulating."""
    delta = cashnequiv.diff(_TD_QTR)
    return _safe_div(-delta, cashnequiv.shift(_TD_QTR).abs())


def cbr_056_cash_depletion_rate_yoy(cashnequiv: pd.Series) -> pd.Series:
    """Annual cash depletion rate: -(YoY change) / prior cash balance."""
    delta = cashnequiv.diff(_TD_YEAR)
    return _safe_div(-delta, cashnequiv.shift(_TD_YEAR).abs())


def cbr_057_cash_below_1yr_burn_flag(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if cash balance < 4 quarters of trailing burn (< 1 year runway)."""
    runway = cbr_033_cash_to_annual_burn_ratio(cashnequiv, fcf)
    return (runway < 1.0).astype(float)


def cbr_058_cash_below_2yr_burn_flag(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if cash balance < 2 years of trailing burn."""
    runway = cbr_033_cash_to_annual_burn_ratio(cashnequiv, fcf)
    return (runway < 2.0).astype(float)


def cbr_059_cash_depletion_rate_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of quarterly cash depletion rate within trailing 8-quarter window.
    Depletion rate = -(QoQ change in cash) / prior cash balance.
    High rank signals cash is being drawn down faster than almost any point in the prior 2 years."""
    depl = _safe_div(-cashnequiv.diff(_TD_QTR), cashnequiv.shift(_TD_QTR).abs())
    return depl.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 2)).rank(pct=True)


def cbr_060_cashnequiv_zscore_8q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash balance over trailing 8 quarters (504 td) — how low is cash."""
    return _zscore_rolling(cashnequiv, _TD_2YR)


# --- Group F (061-075): FCF drawdown, persistence intensity, composite signals ---

def cbr_061_fcf_drawdown_from_4q_peak(fcf: pd.Series) -> pd.Series:
    """FCF drawdown from trailing 4-quarter (252 td) peak FCF."""
    peak = _rolling_max(fcf, _TD_YEAR)
    return _safe_div(fcf - peak, peak.abs())


def cbr_062_fcf_drawdown_from_8q_peak(fcf: pd.Series) -> pd.Series:
    """FCF drawdown from trailing 8-quarter (504 td) peak FCF."""
    peak = _rolling_max(fcf, _TD_2YR)
    return _safe_div(fcf - peak, peak.abs())


def cbr_063_fcf_drawdown_from_alltime_peak(fcf: pd.Series) -> pd.Series:
    """FCF drawdown from all-time expanding peak FCF."""
    peak = fcf.expanding(min_periods=1).max()
    return _safe_div(fcf - peak, peak.abs())


def cbr_064_ncfo_drawdown_from_4q_peak(ncfo: pd.Series) -> pd.Series:
    """NCFO drawdown from trailing 4-quarter peak operating cash flow."""
    peak = _rolling_max(ncfo, _TD_YEAR)
    return _safe_div(ncfo - peak, peak.abs())


def cbr_065_fcf_pct_rank_8q(fcf: pd.Series) -> pd.Series:
    """Percentile rank of FCF within trailing 8-quarter (504 td) window."""
    return fcf.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)


def cbr_066_ncfo_pct_rank_8q(ncfo: pd.Series) -> pd.Series:
    """Percentile rank of NCFO within trailing 8-quarter window."""
    return ncfo.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)


def cbr_067_fcf_negative_fraction_4q(fcf: pd.Series) -> pd.Series:
    """Fraction of trailing 4-quarter window where FCF was negative."""
    neg = (fcf < 0).astype(float)
    return _rolling_mean(neg, _TD_YEAR)


def cbr_068_fcf_negative_fraction_8q(fcf: pd.Series) -> pd.Series:
    """Fraction of trailing 8-quarter window where FCF was negative."""
    neg = (fcf < 0).astype(float)
    return _rolling_mean(neg, _TD_2YR)


def cbr_069_ncfo_negative_fraction_4q(ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 4-quarter window where NCFO was negative."""
    neg = (ncfo < 0).astype(float)
    return _rolling_mean(neg, _TD_YEAR)


def cbr_070_fcf_mean_4q(fcf: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean FCF (smoothed burn level)."""
    return _rolling_mean(fcf, _TD_YEAR)


def cbr_071_fcf_std_4q(fcf: pd.Series) -> pd.Series:
    """Trailing 4-quarter std of FCF (burn rate volatility)."""
    return _rolling_std(fcf, _TD_YEAR)


def cbr_072_fcf_trend_slope_4q(fcf: pd.Series) -> pd.Series:
    """OLS slope of FCF over trailing 4 quarters (252 td) — trend direction."""
    return _linslope(fcf, _TD_YEAR)


def cbr_073_dual_burn_flag(fcf: pd.Series, ncfo: pd.Series) -> pd.Series:
    """1 if both FCF and NCFO are negative simultaneously (deep distress)."""
    return ((fcf < 0) & (ncfo < 0)).astype(float)


def cbr_074_triple_burn_flag(fcf: pd.Series, ncfo: pd.Series, ncf: pd.Series) -> pd.Series:
    """1 if FCF, NCFO, and NCF are all negative simultaneously."""
    return ((fcf < 0) & (ncfo < 0) & (ncf < 0)).astype(float)


def cbr_075_composite_burn_intensity(fcf: pd.Series, cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Composite burn intensity: weighted sum of normalized burn signals.
    50% FCF rank (inverted) + 30% NCFO rank (inverted) + 20% cash-drawdown severity."""
    fcf_rank  = 1.0 - fcf.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    ncfo_rank = 1.0 - ncfo.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    peak      = cashnequiv.expanding(min_periods=1).max()
    cash_dd   = _safe_div(peak - cashnequiv, peak.abs()).clip(lower=0)
    return 0.5 * fcf_rank + 0.3 * ncfo_rank + 0.2 * cash_dd


# ── Registry ──────────────────────────────────────────────────────────────────

CASH_BURN_REGISTRY_001_075 = {
    "cbr_001_fcf_level":                       {"inputs": ["fcf"],                    "func": cbr_001_fcf_level},
    "cbr_002_fcf_negative_flag":               {"inputs": ["fcf"],                    "func": cbr_002_fcf_negative_flag},
    "cbr_003_fcf_4q_rolling_sum":              {"inputs": ["fcf"],                    "func": cbr_003_fcf_4q_rolling_sum},
    "cbr_004_fcf_8q_rolling_sum":              {"inputs": ["fcf"],                    "func": cbr_004_fcf_8q_rolling_sum},
    "cbr_005_ncfo_level":                      {"inputs": ["ncfo"],                   "func": cbr_005_ncfo_level},
    "cbr_006_ncfo_negative_flag":              {"inputs": ["ncfo"],                   "func": cbr_006_ncfo_negative_flag},
    "cbr_007_ncfo_4q_sum":                     {"inputs": ["ncfo"],                   "func": cbr_007_ncfo_4q_sum},
    "cbr_008_capex_level":                     {"inputs": ["capex"],                  "func": cbr_008_capex_level},
    "cbr_009_capex_4q_sum":                    {"inputs": ["capex"],                  "func": cbr_009_capex_4q_sum},
    "cbr_010_ncf_level":                       {"inputs": ["ncf"],                    "func": cbr_010_ncf_level},
    "cbr_011_ncf_negative_flag":               {"inputs": ["ncf"],                    "func": cbr_011_ncf_negative_flag},
    "cbr_012_ncf_4q_sum":                      {"inputs": ["ncf"],                    "func": cbr_012_ncf_4q_sum},
    "cbr_013_fcf_qoq_change":                  {"inputs": ["fcf"],                    "func": cbr_013_fcf_qoq_change},
    "cbr_014_fcf_yoy_change":                  {"inputs": ["fcf"],                    "func": cbr_014_fcf_yoy_change},
    "cbr_015_fcf_qoq_pct_change":             {"inputs": ["fcf"],                    "func": cbr_015_fcf_qoq_pct_change},
    "cbr_016_fcf_yoy_pct_change":             {"inputs": ["fcf"],                    "func": cbr_016_fcf_yoy_pct_change},
    "cbr_017_ncfo_qoq_change":                 {"inputs": ["ncfo"],                   "func": cbr_017_ncfo_qoq_change},
    "cbr_018_ncfo_yoy_change":                 {"inputs": ["ncfo"],                   "func": cbr_018_ncfo_yoy_change},
    "cbr_019_ncfo_qoq_pct_change":            {"inputs": ["ncfo"],                   "func": cbr_019_ncfo_qoq_pct_change},
    "cbr_020_ncfo_yoy_pct_change":            {"inputs": ["ncfo"],                   "func": cbr_020_ncfo_yoy_pct_change},
    "cbr_021_capex_qoq_change":                {"inputs": ["capex"],                  "func": cbr_021_capex_qoq_change},
    "cbr_022_capex_yoy_change":                {"inputs": ["capex"],                  "func": cbr_022_capex_yoy_change},
    "cbr_023_cashnequiv_qoq_change":           {"inputs": ["cashnequiv"],             "func": cbr_023_cashnequiv_qoq_change},
    "cbr_024_cashnequiv_yoy_change":           {"inputs": ["cashnequiv"],             "func": cbr_024_cashnequiv_yoy_change},
    "cbr_025_cashnequiv_2yr_change":           {"inputs": ["cashnequiv"],             "func": cbr_025_cashnequiv_2yr_change},
    "cbr_026_quarterly_burn_rate":             {"inputs": ["fcf"],                    "func": cbr_026_quarterly_burn_rate},
    "cbr_027_annual_burn_rate":                {"inputs": ["fcf"],                    "func": cbr_027_annual_burn_rate},
    "cbr_028_cash_runway_quarters":            {"inputs": ["cashnequiv", "fcf"],      "func": cbr_028_cash_runway_quarters},
    "cbr_029_cash_runway_years":               {"inputs": ["cashnequiv", "fcf"],      "func": cbr_029_cash_runway_years},
    "cbr_030_cash_runway_4q_avg_burn":         {"inputs": ["cashnequiv", "fcf"],      "func": cbr_030_cash_runway_4q_avg_burn},
    "cbr_031_cash_runway_ncfo_based":          {"inputs": ["cashnequiv", "ncfo"],     "func": cbr_031_cash_runway_ncfo_based},
    "cbr_032_runway_declining_flag":           {"inputs": ["cashnequiv", "fcf"],      "func": cbr_032_runway_declining_flag},
    "cbr_033_cash_to_annual_burn_ratio":       {"inputs": ["cashnequiv", "fcf"],      "func": cbr_033_cash_to_annual_burn_ratio},
    "cbr_034_burn_acceleration":               {"inputs": ["fcf"],                    "func": cbr_034_burn_acceleration},
    "cbr_035_annual_burn_pct_rank_8q":         {"inputs": ["fcf"],                    "func": cbr_035_annual_burn_pct_rank_8q},
    "cbr_036_burn_rate_zscore_8q":             {"inputs": ["fcf"],                    "func": cbr_036_burn_rate_zscore_8q},
    "cbr_037_fcf_to_revenue":                  {"inputs": ["fcf", "revenue"],         "func": cbr_037_fcf_to_revenue},
    "cbr_038_ncfo_to_revenue":                 {"inputs": ["ncfo", "revenue"],        "func": cbr_038_ncfo_to_revenue},
    "cbr_039_capex_to_revenue":                {"inputs": ["capex", "revenue"],       "func": cbr_039_capex_to_revenue},
    "cbr_040_fcf_margin_pct_rank_8q":          {"inputs": ["fcf", "revenue"],         "func": cbr_040_fcf_margin_pct_rank_8q},
    "cbr_041_fcf_margin_zscore_8q":           {"inputs": ["fcf", "revenue"],         "func": cbr_041_fcf_margin_zscore_8q},
    "cbr_042_ncfo_minus_capex_spread":         {"inputs": ["ncfo", "capex"],          "func": cbr_042_ncfo_minus_capex_spread},
    "cbr_043_ncfo_capex_coverage_ratio":       {"inputs": ["ncfo", "capex"],          "func": cbr_043_ncfo_capex_coverage_ratio},
    "cbr_044_burn_relative_to_revenue_4q":     {"inputs": ["fcf", "revenue"],         "func": cbr_044_burn_relative_to_revenue_4q},
    "cbr_045_fcf_margin_drawdown_from_4q_peak": {"inputs": ["fcf", "revenue"],        "func": cbr_045_fcf_margin_drawdown_from_4q_peak},
    "cbr_046_cash_to_revenue_ratio":           {"inputs": ["cashnequiv", "revenue"],  "func": cbr_046_cash_to_revenue_ratio},
    "cbr_047_cash_to_revenue_yoy_change":      {"inputs": ["cashnequiv", "revenue"],  "func": cbr_047_cash_to_revenue_yoy_change},
    "cbr_048_sbcomp_adjusted_fcf":             {"inputs": ["fcf", "sbcomp"],          "func": cbr_048_sbcomp_adjusted_fcf},
    "cbr_049_cashnequiv_level":                {"inputs": ["cashnequiv"],             "func": cbr_049_cashnequiv_level},
    "cbr_050_cashnequiv_drawdown_from_peak":   {"inputs": ["cashnequiv"],             "func": cbr_050_cashnequiv_drawdown_from_peak},
    "cbr_051_cashnequiv_drawdown_from_2yr_peak": {"inputs": ["cashnequiv"],           "func": cbr_051_cashnequiv_drawdown_from_2yr_peak},
    "cbr_052_cashnequiv_drawdown_from_alltime_peak": {"inputs": ["cashnequiv"],       "func": cbr_052_cashnequiv_drawdown_from_alltime_peak},
    "cbr_053_consecutive_neg_fcf_quarters":    {"inputs": ["fcf"],                    "func": cbr_053_consecutive_neg_fcf_quarters},
    "cbr_054_consecutive_neg_ncfo_quarters":   {"inputs": ["ncfo"],                   "func": cbr_054_consecutive_neg_ncfo_quarters},
    "cbr_055_cash_depletion_rate_qoq":         {"inputs": ["cashnequiv"],             "func": cbr_055_cash_depletion_rate_qoq},
    "cbr_056_cash_depletion_rate_yoy":         {"inputs": ["cashnequiv"],             "func": cbr_056_cash_depletion_rate_yoy},
    "cbr_057_cash_below_1yr_burn_flag":        {"inputs": ["cashnequiv", "fcf"],      "func": cbr_057_cash_below_1yr_burn_flag},
    "cbr_058_cash_below_2yr_burn_flag":        {"inputs": ["cashnequiv", "fcf"],      "func": cbr_058_cash_below_2yr_burn_flag},
    "cbr_059_cash_depletion_rate_pct_rank_8q": {"inputs": ["cashnequiv"],             "func": cbr_059_cash_depletion_rate_pct_rank_8q},
    "cbr_060_cashnequiv_zscore_8q":            {"inputs": ["cashnequiv"],             "func": cbr_060_cashnequiv_zscore_8q},
    "cbr_061_fcf_drawdown_from_4q_peak":       {"inputs": ["fcf"],                    "func": cbr_061_fcf_drawdown_from_4q_peak},
    "cbr_062_fcf_drawdown_from_8q_peak":       {"inputs": ["fcf"],                    "func": cbr_062_fcf_drawdown_from_8q_peak},
    "cbr_063_fcf_drawdown_from_alltime_peak":  {"inputs": ["fcf"],                    "func": cbr_063_fcf_drawdown_from_alltime_peak},
    "cbr_064_ncfo_drawdown_from_4q_peak":      {"inputs": ["ncfo"],                   "func": cbr_064_ncfo_drawdown_from_4q_peak},
    "cbr_065_fcf_pct_rank_8q":                 {"inputs": ["fcf"],                    "func": cbr_065_fcf_pct_rank_8q},
    "cbr_066_ncfo_pct_rank_8q":                {"inputs": ["ncfo"],                   "func": cbr_066_ncfo_pct_rank_8q},
    "cbr_067_fcf_negative_fraction_4q":        {"inputs": ["fcf"],                    "func": cbr_067_fcf_negative_fraction_4q},
    "cbr_068_fcf_negative_fraction_8q":        {"inputs": ["fcf"],                    "func": cbr_068_fcf_negative_fraction_8q},
    "cbr_069_ncfo_negative_fraction_4q":       {"inputs": ["ncfo"],                   "func": cbr_069_ncfo_negative_fraction_4q},
    "cbr_070_fcf_mean_4q":                     {"inputs": ["fcf"],                    "func": cbr_070_fcf_mean_4q},
    "cbr_071_fcf_std_4q":                      {"inputs": ["fcf"],                    "func": cbr_071_fcf_std_4q},
    "cbr_072_fcf_trend_slope_4q":              {"inputs": ["fcf"],                    "func": cbr_072_fcf_trend_slope_4q},
    "cbr_073_dual_burn_flag":                  {"inputs": ["fcf", "ncfo"],            "func": cbr_073_dual_burn_flag},
    "cbr_074_triple_burn_flag":                {"inputs": ["fcf", "ncfo", "ncf"],     "func": cbr_074_triple_burn_flag},
    "cbr_075_composite_burn_intensity":        {"inputs": ["fcf", "cashnequiv", "ncfo"], "func": cbr_075_composite_burn_intensity},
}
