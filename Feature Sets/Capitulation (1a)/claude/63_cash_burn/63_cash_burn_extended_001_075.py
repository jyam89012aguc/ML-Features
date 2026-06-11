"""
63_cash_burn — Extended Features 001-075
Domain: negative free cash flow, operating cash burn, cash runway depletion —
        deeper variants, additional windows, smoothings, z-scores, percentile
        ranks, streaks, composites, and cross-signal combinations.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract: inputs are already daily-frequency
Series forward-filled from the most recent quarterly SF1 report. Functions
look strictly backward using .shift(positive), .rolling(), or .expanding().
1 quarter = 63 trading days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2YR  = 504
_TD_3YR  = 756
_TD_5YR  = 1260
_EPS     = 1e-9

# ── Alignment helper (pipeline already does this; provided for completeness) ───

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    return q_series.reindex(daily_index).ffill()

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope; NaN-safe."""
    def _slope(x):
        valid = x[~np.isnan(x)]
        n = len(valid)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean(); x_m = valid.mean()
        num = ((xi - xi_m) * (valid - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-010): FCF 3yr and 5yr windows, new burn metrics ---

def cbr_ext_001_fcf_12q_rolling_sum(fcf: pd.Series) -> pd.Series:
    """Trailing 12-quarter (3-year, 756 td) sum of FCF — multi-year burn total."""
    return _rolling_sum(fcf, _TD_3YR)


def cbr_ext_002_fcf_20q_rolling_sum(fcf: pd.Series) -> pd.Series:
    """Trailing 20-quarter (5-year, 1260 td) sum of FCF — long-run burn total."""
    return _rolling_sum(fcf, _TD_5YR)


def cbr_ext_003_fcf_min_4q(fcf: pd.Series) -> pd.Series:
    """Worst (minimum) quarterly FCF in trailing 4 quarters (252 days)."""
    return _rolling_min(fcf, _TD_YEAR)


def cbr_ext_004_fcf_min_8q(fcf: pd.Series) -> pd.Series:
    """Worst quarterly FCF in trailing 8 quarters (504 days)."""
    return _rolling_min(fcf, _TD_2YR)


def cbr_ext_005_fcf_min_12q(fcf: pd.Series) -> pd.Series:
    """Worst quarterly FCF in trailing 12 quarters (756 days)."""
    return _rolling_min(fcf, _TD_3YR)


def cbr_ext_006_fcf_expanding_min(fcf: pd.Series) -> pd.Series:
    """All-history expanding minimum FCF (worst-ever quarterly FCF)."""
    return fcf.expanding(min_periods=1).min()


def cbr_ext_007_fcf_pct_rank_4q(fcf: pd.Series) -> pd.Series:
    """Percentile rank of FCF in trailing 4-quarter (252-day) window."""
    return _rolling_rank_pct(fcf, _TD_YEAR)


def cbr_ext_008_fcf_pct_rank_12q(fcf: pd.Series) -> pd.Series:
    """Percentile rank of FCF in trailing 12-quarter (756-day) window."""
    return _rolling_rank_pct(fcf, _TD_3YR)


def cbr_ext_009_fcf_expanding_pct_rank(fcf: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of FCF (how extreme vs full history)."""
    return fcf.expanding(min_periods=2).rank(pct=True)


def cbr_ext_010_fcf_zscore_4q(fcf: pd.Series) -> pd.Series:
    """Z-score of FCF within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(fcf, _TD_YEAR)


# --- Group B (011-020): FCF trend, momentum, acceleration variants ---

def cbr_ext_011_fcf_zscore_12q(fcf: pd.Series) -> pd.Series:
    """Z-score of FCF within trailing 12-quarter (756-day) window."""
    return _zscore_rolling(fcf, _TD_3YR)


def cbr_ext_012_fcf_expanding_zscore(fcf: pd.Series) -> pd.Series:
    """All-history expanding z-score of FCF."""
    m  = fcf.expanding(min_periods=2).mean()
    sd = fcf.expanding(min_periods=2).std()
    return _safe_div(fcf - m, sd)


def cbr_ext_013_fcf_trend_slope_8q(fcf: pd.Series) -> pd.Series:
    """OLS slope of FCF over trailing 8 quarters (504 td) — medium-term trend."""
    return _linslope(fcf, _TD_2YR)


def cbr_ext_014_fcf_trend_slope_12q(fcf: pd.Series) -> pd.Series:
    """OLS slope of FCF over trailing 12 quarters (756 td) — long-term trend."""
    return _linslope(fcf, _TD_3YR)


def cbr_ext_015_fcf_ewm_deviation_4q(fcf: pd.Series) -> pd.Series:
    """FCF minus its 4-quarter EWM (span=252) — momentum deviation."""
    ewm = _ewm_mean(fcf, _TD_YEAR)
    return fcf - ewm


def cbr_ext_016_fcf_ewm_deviation_8q(fcf: pd.Series) -> pd.Series:
    """FCF minus its 8-quarter EWM (span=504) — slower-momentum deviation."""
    ewm = _ewm_mean(fcf, _TD_2YR)
    return fcf - ewm


def cbr_ext_017_fcf_median_4q(fcf: pd.Series) -> pd.Series:
    """Trailing 4-quarter median FCF (robust central tendency of burn level)."""
    return _rolling_median(fcf, _TD_YEAR)


def cbr_ext_018_fcf_range_4q(fcf: pd.Series) -> pd.Series:
    """4-quarter FCF range: max - min (volatility of burn rate over 1 year)."""
    return _rolling_max(fcf, _TD_YEAR) - _rolling_min(fcf, _TD_YEAR)


def cbr_ext_019_fcf_range_position_4q(fcf: pd.Series) -> pd.Series:
    """FCF position within 4-quarter [min, max] range: (fcf-min)/(max-min)."""
    lo = _rolling_min(fcf, _TD_YEAR)
    hi = _rolling_max(fcf, _TD_YEAR)
    return _safe_div(fcf - lo, hi - lo)


def cbr_ext_020_fcf_qoq_acceleration(fcf: pd.Series) -> pd.Series:
    """QoQ change in the QoQ change of FCF (second difference = acceleration)."""
    d1 = fcf.diff(_TD_QTR)
    return d1.diff(_TD_QTR)


# --- Group C (021-030): NCFO extended variants ---

def cbr_ext_021_ncfo_min_4q(ncfo: pd.Series) -> pd.Series:
    """Worst (minimum) NCFO in trailing 4 quarters (252 days)."""
    return _rolling_min(ncfo, _TD_YEAR)


def cbr_ext_022_ncfo_min_8q(ncfo: pd.Series) -> pd.Series:
    """Worst NCFO in trailing 8 quarters."""
    return _rolling_min(ncfo, _TD_2YR)


def cbr_ext_023_ncfo_zscore_4q(ncfo: pd.Series) -> pd.Series:
    """Z-score of NCFO within trailing 4-quarter window."""
    return _zscore_rolling(ncfo, _TD_YEAR)


def cbr_ext_024_ncfo_zscore_8q(ncfo: pd.Series) -> pd.Series:
    """Z-score of NCFO within trailing 8-quarter window."""
    return _zscore_rolling(ncfo, _TD_2YR)


def cbr_ext_025_ncfo_pct_rank_4q(ncfo: pd.Series) -> pd.Series:
    """Percentile rank of NCFO within trailing 4-quarter window."""
    return _rolling_rank_pct(ncfo, _TD_YEAR)


def cbr_ext_026_ncfo_pct_rank_8q(ncfo: pd.Series) -> pd.Series:
    """Percentile rank of NCFO within trailing 8-quarter window."""
    return _rolling_rank_pct(ncfo, _TD_2YR)


def cbr_ext_027_ncfo_expanding_pct_rank(ncfo: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of NCFO."""
    return ncfo.expanding(min_periods=2).rank(pct=True)


def cbr_ext_028_ncfo_trend_slope_4q(ncfo: pd.Series) -> pd.Series:
    """OLS slope of NCFO over trailing 4 quarters."""
    return _linslope(ncfo, _TD_YEAR)


def cbr_ext_029_ncfo_negative_fraction_8q(ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 8-quarter window where NCFO was negative."""
    neg = (ncfo < 0).astype(float)
    return _rolling_mean(neg, _TD_2YR)


def cbr_ext_030_ncfo_drawdown_from_8q_peak(ncfo: pd.Series) -> pd.Series:
    """NCFO drawdown from trailing 8-quarter peak operating cash flow."""
    peak = _rolling_max(ncfo, _TD_2YR)
    return _safe_div(ncfo - peak, peak.abs())


# --- Group D (031-040): Cash balance extended measures ---

def cbr_ext_031_cashnequiv_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 4-quarter (252-day) window."""
    return _zscore_rolling(cashnequiv, _TD_YEAR)


def cbr_ext_032_cashnequiv_zscore_12q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash & equivalents within trailing 12-quarter window."""
    return _zscore_rolling(cashnequiv, _TD_3YR)


def cbr_ext_033_cashnequiv_pct_rank_4q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash balance within trailing 4-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_YEAR)


def cbr_ext_034_cashnequiv_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash balance within trailing 8-quarter window."""
    return _rolling_rank_pct(cashnequiv, _TD_2YR)


def cbr_ext_035_cashnequiv_expanding_pct_rank(cashnequiv: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of cash balance."""
    return cashnequiv.expanding(min_periods=2).rank(pct=True)


def cbr_ext_036_cashnequiv_drawdown_from_3yr_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash drawdown from 3-year (756 td) rolling peak."""
    peak = _rolling_max(cashnequiv, _TD_3YR)
    return _safe_div(cashnequiv - peak, peak)


def cbr_ext_037_cashnequiv_drawdown_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Pct-rank of cash-to-2yr-peak ratio within trailing 8-quarter window."""
    peak = _rolling_max(cashnequiv, _TD_2YR)
    dd   = _safe_div(cashnequiv - peak, peak.abs())
    return _rolling_rank_pct(dd, _TD_2YR)


def cbr_ext_038_cashnequiv_trend_slope_4q(cashnequiv: pd.Series) -> pd.Series:
    """OLS slope of cash balance over trailing 4 quarters (trend direction)."""
    return _linslope(cashnequiv, _TD_YEAR)


def cbr_ext_039_cashnequiv_trend_slope_8q(cashnequiv: pd.Series) -> pd.Series:
    """OLS slope of cash balance over trailing 8 quarters."""
    return _linslope(cashnequiv, _TD_2YR)


def cbr_ext_040_cashnequiv_3yr_change(cashnequiv: pd.Series) -> pd.Series:
    """3-year change in cash & equivalents balance (long-term depletion signal)."""
    return cashnequiv.diff(_TD_3YR)


# --- Group E (041-050): Relative metrics and ratios ---

def cbr_ext_041_fcf_to_revenue_zscore_4q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of FCF margin (FCF/revenue) within trailing 4-quarter window."""
    margin = _safe_div(fcf, revenue)
    return _zscore_rolling(margin, _TD_YEAR)


def cbr_ext_042_fcf_to_revenue_pct_rank_4q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of FCF margin within trailing 4-quarter window."""
    margin = _safe_div(fcf, revenue)
    return _rolling_rank_pct(margin, _TD_YEAR)


def cbr_ext_043_ncfo_to_revenue_zscore_4q(ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating cash flow margin (NCFO/revenue) within 4-quarter window."""
    margin = _safe_div(ncfo, revenue)
    return _zscore_rolling(margin, _TD_YEAR)


def cbr_ext_044_fcf_to_revenue_trend_slope_4q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of FCF margin over trailing 4 quarters."""
    margin = _safe_div(fcf, revenue)
    return _linslope(margin, _TD_YEAR)


def cbr_ext_045_capex_to_revenue_zscore_4q(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of capex intensity (|capex|/revenue) within 4-quarter window."""
    ratio = _safe_div(capex.abs(), revenue)
    return _zscore_rolling(ratio, _TD_YEAR)


def cbr_ext_046_fcf_to_revenue_4q_avg(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter average FCF margin (smoothed FCF/revenue)."""
    return _rolling_mean(_safe_div(fcf, revenue), _TD_YEAR)


def cbr_ext_047_ncfo_minus_capex_spread_zscore_4q(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """Z-score of NCFO minus |capex| spread within trailing 4-quarter window."""
    spread = ncfo - capex.abs()
    return _zscore_rolling(spread, _TD_YEAR)


def cbr_ext_048_ncfo_capex_coverage_pct_rank_4q(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """Pct rank of NCFO/|capex| coverage ratio within 4-quarter window."""
    ratio = _safe_div(ncfo, capex.abs())
    return _rolling_rank_pct(ratio, _TD_YEAR)


def cbr_ext_049_ncfo_capex_coverage_zscore_8q(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """Z-score of NCFO/|capex| coverage within 8-quarter window."""
    ratio = _safe_div(ncfo, capex.abs())
    return _zscore_rolling(ratio, _TD_2YR)


def cbr_ext_050_sbcomp_to_revenue(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """SBC as fraction of revenue — dilutive burn severity normalized by scale."""
    return _safe_div(sbcomp.abs(), revenue.abs())


# --- Group F (051-060): Streak, regime, and persistence signals ---

def cbr_ext_051_fcf_negative_streak_days(fcf: pd.Series) -> pd.Series:
    """Consecutive daily observations where FCF has been negative (streak length)."""
    neg = (fcf < 0).astype(int)
    arr = neg.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=fcf.index)


def cbr_ext_052_ncfo_negative_streak_days(ncfo: pd.Series) -> pd.Series:
    """Consecutive daily observations where NCFO has been negative."""
    neg = (ncfo < 0).astype(int)
    arr = neg.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=ncfo.index)


def cbr_ext_053_fcf_declining_streak_days(fcf: pd.Series) -> pd.Series:
    """Consecutive days FCF has been below its prior-quarter level (declining trend)."""
    declining = (fcf < fcf.shift(_TD_QTR)).astype(int)
    arr = declining.values
    streak = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=fcf.index)


def cbr_ext_054_fcf_negative_fraction_12q(fcf: pd.Series) -> pd.Series:
    """Fraction of trailing 12-quarter (3-year) window where FCF was negative."""
    neg = (fcf < 0).astype(float)
    return _rolling_mean(neg, _TD_3YR)


def cbr_ext_055_dual_burn_fraction_4q(fcf: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 4-quarter window where both FCF and NCFO were negative."""
    dual = ((fcf < 0) & (ncfo < 0)).astype(float)
    return _rolling_mean(dual, _TD_YEAR)


def cbr_ext_056_dual_burn_fraction_8q(fcf: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Fraction of trailing 8-quarter window where both FCF and NCFO were negative."""
    dual = ((fcf < 0) & (ncfo < 0)).astype(float)
    return _rolling_mean(dual, _TD_2YR)


def cbr_ext_057_cash_depletion_acceleration(cashnequiv: pd.Series) -> pd.Series:
    """QoQ change in the quarterly cash depletion rate (second derivative of cash)."""
    depl = _safe_div(-cashnequiv.diff(_TD_QTR), cashnequiv.shift(_TD_QTR).abs())
    return depl.diff(_TD_QTR)


def cbr_ext_058_cash_depletion_rate_zscore_4q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of quarterly cash depletion rate within trailing 4-quarter window."""
    depl = _safe_div(-cashnequiv.diff(_TD_QTR), cashnequiv.shift(_TD_QTR).abs())
    return _zscore_rolling(depl, _TD_YEAR)


def cbr_ext_059_cash_depletion_rate_3yr_change(cashnequiv: pd.Series) -> pd.Series:
    """3-year change in quarterly cash depletion rate."""
    depl = _safe_div(-cashnequiv.diff(_TD_QTR), cashnequiv.shift(_TD_QTR).abs())
    return depl - depl.shift(_TD_3YR)


def cbr_ext_060_cash_below_halfyr_burn_flag(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if cash balance < 2 quarters of trailing burn (< 6-month runway)."""
    annual_burn = -_rolling_sum(fcf, _TD_YEAR)
    halfyr_burn = annual_burn / 2.0
    ratio = _safe_div(cashnequiv, halfyr_burn.where(halfyr_burn > 0, np.nan))
    return (ratio < 1.0).astype(float)


# --- Group G (061-070): Revenue-normalized and scaled burn metrics ---

def cbr_ext_061_fcf_4q_sum_zscore_8q(fcf: pd.Series) -> pd.Series:
    """Z-score of trailing 4Q FCF sum within a trailing 8-quarter (504-day) window."""
    fcf4q = _rolling_sum(fcf, _TD_YEAR)
    return _zscore_rolling(fcf4q, _TD_2YR)


def cbr_ext_062_fcf_4q_sum_pct_rank_8q(fcf: pd.Series) -> pd.Series:
    """Pct rank of trailing 4Q FCF sum within a trailing 8-quarter window."""
    fcf4q = _rolling_sum(fcf, _TD_YEAR)
    return _rolling_rank_pct(fcf4q, _TD_2YR)


def cbr_ext_063_ncfo_4q_sum_zscore_8q(ncfo: pd.Series) -> pd.Series:
    """Z-score of trailing 4Q NCFO sum within an 8-quarter window."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    return _zscore_rolling(ncfo4q, _TD_2YR)


def cbr_ext_064_fcf_to_revenue_expanding_rank(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of FCF margin (FCF/revenue)."""
    margin = _safe_div(fcf, revenue)
    return margin.expanding(min_periods=2).rank(pct=True)


def cbr_ext_065_cash_to_revenue_zscore_4q(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of cash-to-revenue ratio within trailing 4-quarter window."""
    ratio = _safe_div(cashnequiv, revenue.abs())
    return _zscore_rolling(ratio, _TD_YEAR)


def cbr_ext_066_cash_to_revenue_pct_rank_8q(cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pct rank of cash-to-revenue ratio within 8-quarter window."""
    ratio = _safe_div(cashnequiv, revenue.abs())
    return _rolling_rank_pct(ratio, _TD_2YR)


def cbr_ext_067_sbcomp_adjusted_fcf_zscore_4q(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """Z-score of SBC-adjusted FCF (fcf - sbcomp) within 4-quarter window."""
    adj = fcf - sbcomp.abs()
    return _zscore_rolling(adj, _TD_YEAR)


def cbr_ext_068_sbcomp_adjusted_fcf_pct_rank_8q(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """Pct rank of SBC-adjusted FCF within 8-quarter window."""
    adj = fcf - sbcomp.abs()
    return _rolling_rank_pct(adj, _TD_2YR)


def cbr_ext_069_sbcomp_adjusted_fcf_negative_flag(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """1 if SBC-adjusted FCF (fcf - sbcomp) is negative."""
    adj = fcf - sbcomp.abs()
    return (adj < 0).astype(float)


def cbr_ext_070_sbcomp_adj_fcf_negative_fraction_4q(fcf: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """Fraction of trailing 4-quarter window where SBC-adjusted FCF was negative."""
    adj = (fcf - sbcomp.abs() < 0).astype(float)
    return _rolling_mean(adj, _TD_YEAR)


# --- Group H (071-075): Composite and multi-signal distress scores ---

def cbr_ext_071_burn_severity_composite_3q(fcf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Composite: (1 - FCF pct-rank in 4Q) * 0.6 + (1 - cash pct-rank in 4Q) * 0.4.
    Higher = more severe burn / cash distress within recent 4-quarter context.
    """
    fcf_rank  = _rolling_rank_pct(fcf, _TD_YEAR)
    cash_rank = _rolling_rank_pct(cashnequiv, _TD_YEAR)
    return 0.6 * (1.0 - fcf_rank) + 0.4 * (1.0 - cash_rank)


def cbr_ext_072_burn_composite_zscore_avg(fcf: pd.Series, ncfo: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """
    Equally weighted composite z-score: (z_fcf + z_ncfo + z_cash) / 3,
    all within 4-quarter windows. Negative = coordinated burn/cash distress.
    """
    z_fcf  = _zscore_rolling(fcf, _TD_YEAR)
    z_ncfo = _zscore_rolling(ncfo, _TD_YEAR)
    z_cash = _zscore_rolling(cashnequiv, _TD_YEAR)
    return (z_fcf + z_ncfo + z_cash) / 3.0


def cbr_ext_073_runway_pct_rank_4q(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Pct rank of cash runway (cash / quarterly burn) within 4-quarter window.
    Low rank = runway near its shortest level in recent history."""
    burn   = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway = runway.where(runway >= 0, np.nan)
    return _rolling_rank_pct(runway, _TD_YEAR)


def cbr_ext_074_fcf_margin_12q_trend_slope(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """OLS slope of FCF margin (fcf/revenue) over trailing 12 quarters (756 td)."""
    margin = _safe_div(fcf, revenue)
    return _linslope(margin, _TD_3YR)


def cbr_ext_075_triple_burn_composite(fcf: pd.Series, ncfo: pd.Series, ncf: pd.Series,
                                       cashnequiv: pd.Series) -> pd.Series:
    """
    Composite distress score combining: triple-burn flag (FCF+NCFO+NCF all neg),
    8-quarter FCF rank (inverted), and cash-depletion severity.
    = triple_flag * 0.3 + (1 - fcf_rank_8q) * 0.5 + (1 - cash_rank_8q) * 0.2.
    Higher = deeper simultaneous cash-flow and balance-sheet distress.
    """
    triple   = ((fcf < 0) & (ncfo < 0) & (ncf < 0)).astype(float)
    fcf_rank = _rolling_rank_pct(fcf, _TD_2YR)
    csh_rank = _rolling_rank_pct(cashnequiv, _TD_2YR)
    return 0.3 * triple + 0.5 * (1.0 - fcf_rank) + 0.2 * (1.0 - csh_rank)


# ── Registry ───────────────────────────────────────────────────────────────────

CASH_BURN_EXTENDED_REGISTRY_001_075 = {
    "cbr_ext_001_fcf_12q_rolling_sum":              {"inputs": ["fcf"],                        "func": cbr_ext_001_fcf_12q_rolling_sum},
    "cbr_ext_002_fcf_20q_rolling_sum":              {"inputs": ["fcf"],                        "func": cbr_ext_002_fcf_20q_rolling_sum},
    "cbr_ext_003_fcf_min_4q":                       {"inputs": ["fcf"],                        "func": cbr_ext_003_fcf_min_4q},
    "cbr_ext_004_fcf_min_8q":                       {"inputs": ["fcf"],                        "func": cbr_ext_004_fcf_min_8q},
    "cbr_ext_005_fcf_min_12q":                      {"inputs": ["fcf"],                        "func": cbr_ext_005_fcf_min_12q},
    "cbr_ext_006_fcf_expanding_min":                {"inputs": ["fcf"],                        "func": cbr_ext_006_fcf_expanding_min},
    "cbr_ext_007_fcf_pct_rank_4q":                  {"inputs": ["fcf"],                        "func": cbr_ext_007_fcf_pct_rank_4q},
    "cbr_ext_008_fcf_pct_rank_12q":                 {"inputs": ["fcf"],                        "func": cbr_ext_008_fcf_pct_rank_12q},
    "cbr_ext_009_fcf_expanding_pct_rank":           {"inputs": ["fcf"],                        "func": cbr_ext_009_fcf_expanding_pct_rank},
    "cbr_ext_010_fcf_zscore_4q":                    {"inputs": ["fcf"],                        "func": cbr_ext_010_fcf_zscore_4q},
    "cbr_ext_011_fcf_zscore_12q":                   {"inputs": ["fcf"],                        "func": cbr_ext_011_fcf_zscore_12q},
    "cbr_ext_012_fcf_expanding_zscore":             {"inputs": ["fcf"],                        "func": cbr_ext_012_fcf_expanding_zscore},
    "cbr_ext_013_fcf_trend_slope_8q":               {"inputs": ["fcf"],                        "func": cbr_ext_013_fcf_trend_slope_8q},
    "cbr_ext_014_fcf_trend_slope_12q":              {"inputs": ["fcf"],                        "func": cbr_ext_014_fcf_trend_slope_12q},
    "cbr_ext_015_fcf_ewm_deviation_4q":             {"inputs": ["fcf"],                        "func": cbr_ext_015_fcf_ewm_deviation_4q},
    "cbr_ext_016_fcf_ewm_deviation_8q":             {"inputs": ["fcf"],                        "func": cbr_ext_016_fcf_ewm_deviation_8q},
    "cbr_ext_017_fcf_median_4q":                    {"inputs": ["fcf"],                        "func": cbr_ext_017_fcf_median_4q},
    "cbr_ext_018_fcf_range_4q":                     {"inputs": ["fcf"],                        "func": cbr_ext_018_fcf_range_4q},
    "cbr_ext_019_fcf_range_position_4q":            {"inputs": ["fcf"],                        "func": cbr_ext_019_fcf_range_position_4q},
    "cbr_ext_020_fcf_qoq_acceleration":             {"inputs": ["fcf"],                        "func": cbr_ext_020_fcf_qoq_acceleration},
    "cbr_ext_021_ncfo_min_4q":                      {"inputs": ["ncfo"],                       "func": cbr_ext_021_ncfo_min_4q},
    "cbr_ext_022_ncfo_min_8q":                      {"inputs": ["ncfo"],                       "func": cbr_ext_022_ncfo_min_8q},
    "cbr_ext_023_ncfo_zscore_4q":                   {"inputs": ["ncfo"],                       "func": cbr_ext_023_ncfo_zscore_4q},
    "cbr_ext_024_ncfo_zscore_8q":                   {"inputs": ["ncfo"],                       "func": cbr_ext_024_ncfo_zscore_8q},
    "cbr_ext_025_ncfo_pct_rank_4q":                 {"inputs": ["ncfo"],                       "func": cbr_ext_025_ncfo_pct_rank_4q},
    "cbr_ext_026_ncfo_pct_rank_8q":                 {"inputs": ["ncfo"],                       "func": cbr_ext_026_ncfo_pct_rank_8q},
    "cbr_ext_027_ncfo_expanding_pct_rank":          {"inputs": ["ncfo"],                       "func": cbr_ext_027_ncfo_expanding_pct_rank},
    "cbr_ext_028_ncfo_trend_slope_4q":              {"inputs": ["ncfo"],                       "func": cbr_ext_028_ncfo_trend_slope_4q},
    "cbr_ext_029_ncfo_negative_fraction_8q":        {"inputs": ["ncfo"],                       "func": cbr_ext_029_ncfo_negative_fraction_8q},
    "cbr_ext_030_ncfo_drawdown_from_8q_peak":       {"inputs": ["ncfo"],                       "func": cbr_ext_030_ncfo_drawdown_from_8q_peak},
    "cbr_ext_031_cashnequiv_zscore_4q":             {"inputs": ["cashnequiv"],                 "func": cbr_ext_031_cashnequiv_zscore_4q},
    "cbr_ext_032_cashnequiv_zscore_12q":            {"inputs": ["cashnequiv"],                 "func": cbr_ext_032_cashnequiv_zscore_12q},
    "cbr_ext_033_cashnequiv_pct_rank_4q":           {"inputs": ["cashnequiv"],                 "func": cbr_ext_033_cashnequiv_pct_rank_4q},
    "cbr_ext_034_cashnequiv_pct_rank_8q":           {"inputs": ["cashnequiv"],                 "func": cbr_ext_034_cashnequiv_pct_rank_8q},
    "cbr_ext_035_cashnequiv_expanding_pct_rank":    {"inputs": ["cashnequiv"],                 "func": cbr_ext_035_cashnequiv_expanding_pct_rank},
    "cbr_ext_036_cashnequiv_drawdown_from_3yr_peak":{"inputs": ["cashnequiv"],                 "func": cbr_ext_036_cashnequiv_drawdown_from_3yr_peak},
    "cbr_ext_037_cashnequiv_drawdown_pct_rank_8q":  {"inputs": ["cashnequiv"],                 "func": cbr_ext_037_cashnequiv_drawdown_pct_rank_8q},
    "cbr_ext_038_cashnequiv_trend_slope_4q":        {"inputs": ["cashnequiv"],                 "func": cbr_ext_038_cashnequiv_trend_slope_4q},
    "cbr_ext_039_cashnequiv_trend_slope_8q":        {"inputs": ["cashnequiv"],                 "func": cbr_ext_039_cashnequiv_trend_slope_8q},
    "cbr_ext_040_cashnequiv_3yr_change":            {"inputs": ["cashnequiv"],                 "func": cbr_ext_040_cashnequiv_3yr_change},
    "cbr_ext_041_fcf_to_revenue_zscore_4q":         {"inputs": ["fcf", "revenue"],             "func": cbr_ext_041_fcf_to_revenue_zscore_4q},
    "cbr_ext_042_fcf_to_revenue_pct_rank_4q":       {"inputs": ["fcf", "revenue"],             "func": cbr_ext_042_fcf_to_revenue_pct_rank_4q},
    "cbr_ext_043_ncfo_to_revenue_zscore_4q":        {"inputs": ["ncfo", "revenue"],            "func": cbr_ext_043_ncfo_to_revenue_zscore_4q},
    "cbr_ext_044_fcf_to_revenue_trend_slope_4q":    {"inputs": ["fcf", "revenue"],             "func": cbr_ext_044_fcf_to_revenue_trend_slope_4q},
    "cbr_ext_045_capex_to_revenue_zscore_4q":       {"inputs": ["capex", "revenue"],           "func": cbr_ext_045_capex_to_revenue_zscore_4q},
    "cbr_ext_046_fcf_to_revenue_4q_avg":            {"inputs": ["fcf", "revenue"],             "func": cbr_ext_046_fcf_to_revenue_4q_avg},
    "cbr_ext_047_ncfo_minus_capex_spread_zscore_4q":{"inputs": ["ncfo", "capex"],              "func": cbr_ext_047_ncfo_minus_capex_spread_zscore_4q},
    "cbr_ext_048_ncfo_capex_coverage_pct_rank_4q":  {"inputs": ["ncfo", "capex"],              "func": cbr_ext_048_ncfo_capex_coverage_pct_rank_4q},
    "cbr_ext_049_ncfo_capex_coverage_zscore_8q":    {"inputs": ["ncfo", "capex"],              "func": cbr_ext_049_ncfo_capex_coverage_zscore_8q},
    "cbr_ext_050_sbcomp_to_revenue":                {"inputs": ["sbcomp", "revenue"],          "func": cbr_ext_050_sbcomp_to_revenue},
    "cbr_ext_051_fcf_negative_streak_days":         {"inputs": ["fcf"],                        "func": cbr_ext_051_fcf_negative_streak_days},
    "cbr_ext_052_ncfo_negative_streak_days":        {"inputs": ["ncfo"],                       "func": cbr_ext_052_ncfo_negative_streak_days},
    "cbr_ext_053_fcf_declining_streak_days":        {"inputs": ["fcf"],                        "func": cbr_ext_053_fcf_declining_streak_days},
    "cbr_ext_054_fcf_negative_fraction_12q":        {"inputs": ["fcf"],                        "func": cbr_ext_054_fcf_negative_fraction_12q},
    "cbr_ext_055_dual_burn_fraction_4q":            {"inputs": ["fcf", "ncfo"],                "func": cbr_ext_055_dual_burn_fraction_4q},
    "cbr_ext_056_dual_burn_fraction_8q":            {"inputs": ["fcf", "ncfo"],                "func": cbr_ext_056_dual_burn_fraction_8q},
    "cbr_ext_057_cash_depletion_acceleration":      {"inputs": ["cashnequiv"],                 "func": cbr_ext_057_cash_depletion_acceleration},
    "cbr_ext_058_cash_depletion_rate_zscore_4q":    {"inputs": ["cashnequiv"],                 "func": cbr_ext_058_cash_depletion_rate_zscore_4q},
    "cbr_ext_059_cash_depletion_rate_3yr_change":   {"inputs": ["cashnequiv"],                 "func": cbr_ext_059_cash_depletion_rate_3yr_change},
    "cbr_ext_060_cash_below_halfyr_burn_flag":       {"inputs": ["cashnequiv", "fcf"],          "func": cbr_ext_060_cash_below_halfyr_burn_flag},
    "cbr_ext_061_fcf_4q_sum_zscore_8q":             {"inputs": ["fcf"],                        "func": cbr_ext_061_fcf_4q_sum_zscore_8q},
    "cbr_ext_062_fcf_4q_sum_pct_rank_8q":           {"inputs": ["fcf"],                        "func": cbr_ext_062_fcf_4q_sum_pct_rank_8q},
    "cbr_ext_063_ncfo_4q_sum_zscore_8q":            {"inputs": ["ncfo"],                       "func": cbr_ext_063_ncfo_4q_sum_zscore_8q},
    "cbr_ext_064_fcf_to_revenue_expanding_rank":    {"inputs": ["fcf", "revenue"],             "func": cbr_ext_064_fcf_to_revenue_expanding_rank},
    "cbr_ext_065_cash_to_revenue_zscore_4q":        {"inputs": ["cashnequiv", "revenue"],      "func": cbr_ext_065_cash_to_revenue_zscore_4q},
    "cbr_ext_066_cash_to_revenue_pct_rank_8q":      {"inputs": ["cashnequiv", "revenue"],      "func": cbr_ext_066_cash_to_revenue_pct_rank_8q},
    "cbr_ext_067_sbcomp_adjusted_fcf_zscore_4q":    {"inputs": ["fcf", "sbcomp"],              "func": cbr_ext_067_sbcomp_adjusted_fcf_zscore_4q},
    "cbr_ext_068_sbcomp_adjusted_fcf_pct_rank_8q":  {"inputs": ["fcf", "sbcomp"],              "func": cbr_ext_068_sbcomp_adjusted_fcf_pct_rank_8q},
    "cbr_ext_069_sbcomp_adjusted_fcf_negative_flag":{"inputs": ["fcf", "sbcomp"],              "func": cbr_ext_069_sbcomp_adjusted_fcf_negative_flag},
    "cbr_ext_070_sbcomp_adj_fcf_negative_frac_4q":  {"inputs": ["fcf", "sbcomp"],              "func": cbr_ext_070_sbcomp_adj_fcf_negative_fraction_4q},
    "cbr_ext_071_burn_severity_composite_3q":       {"inputs": ["fcf", "cashnequiv"],          "func": cbr_ext_071_burn_severity_composite_3q},
    "cbr_ext_072_burn_composite_zscore_avg":        {"inputs": ["fcf", "ncfo", "cashnequiv"],  "func": cbr_ext_072_burn_composite_zscore_avg},
    "cbr_ext_073_runway_pct_rank_4q":               {"inputs": ["cashnequiv", "fcf"],          "func": cbr_ext_073_runway_pct_rank_4q},
    "cbr_ext_074_fcf_margin_12q_trend_slope":       {"inputs": ["fcf", "revenue"],             "func": cbr_ext_074_fcf_margin_12q_trend_slope},
    "cbr_ext_075_triple_burn_composite":            {"inputs": ["fcf", "ncfo", "ncf", "cashnequiv"], "func": cbr_ext_075_triple_burn_composite},
}
