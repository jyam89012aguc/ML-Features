"""
62_margin_compression — Extended Features 001-075
Domain: gross / operating / EBITDA / net / pretax margin erosion —
        additional variants: new horizons, range positions, acceleration,
        recovery distance, percentile ranks, cost-ratio variants, composites
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
_TD_2Q   = 126
_TD_3Q   = 189
_TD_YEAR = 252   # 1 year
_TD_2Y   = 504
_TD_3Y   = 756
_TD_4Y   = 1008
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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _range_position(s: pd.Series, w: int) -> pd.Series:
    """Position of s within its trailing w-window range: 0=at low, 1=at high."""
    mn = _rolling_min(s, w)
    mx = _rolling_max(s, w)
    return _safe_div(s - mn, mx - mn)


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


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): Additional change horizons for core margins ---

def mgc_ext_001_gross_margin_2q_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-quarter (126-day) change in gross margin."""
    return _gross_margin(gp, revenue).diff(_TD_2Q)


def mgc_ext_002_gross_margin_3q_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-quarter (189-day) change in gross margin."""
    return _gross_margin(gp, revenue).diff(_TD_3Q)


def mgc_ext_003_gross_margin_3y_change(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year (756-day) change in gross margin."""
    return _gross_margin(gp, revenue).diff(_TD_3Y)


def mgc_ext_004_op_margin_2q_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-quarter change in operating margin."""
    return _op_margin(opinc, revenue).diff(_TD_2Q)


def mgc_ext_005_op_margin_3y_change(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year change in operating margin."""
    return _op_margin(opinc, revenue).diff(_TD_3Y)


def mgc_ext_006_ebitda_margin_2q_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-quarter change in EBITDA margin."""
    return _ebitda_margin(ebitda, revenue).diff(_TD_2Q)


def mgc_ext_007_ebitda_margin_3y_change(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """3-year change in EBITDA margin."""
    return _ebitda_margin(ebitda, revenue).diff(_TD_3Y)


def mgc_ext_008_net_margin_2q_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-quarter change in net margin."""
    return _net_margin(netinc, revenue).diff(_TD_2Q)


def mgc_ext_009_net_margin_2y_change(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in net margin."""
    return _net_margin(netinc, revenue).diff(_TD_2Y)


def mgc_ext_010_pretax_margin_2y_change(ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in pretax margin."""
    return _pretax_margin(ebt, revenue).diff(_TD_2Y)


def mgc_ext_011_ebit_margin_2q_change(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-quarter change in EBIT margin."""
    return _ebit_margin(ebit, revenue).diff(_TD_2Q)


def mgc_ext_012_ebit_margin_2y_change(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in EBIT margin."""
    return _ebit_margin(ebit, revenue).diff(_TD_2Y)


# --- Group B (013-024): Margin range position and new-low flags ---

def mgc_ext_013_gross_margin_range_pos_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin position within its trailing 4-quarter range (0=low, 1=high)."""
    return _range_position(_gross_margin(gp, revenue), _TD_YEAR)


def mgc_ext_014_gross_margin_range_pos_12q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin position within its trailing 12-quarter range."""
    return _range_position(_gross_margin(gp, revenue), _TD_3Y)


def mgc_ext_015_op_margin_range_pos_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin position within its trailing 8-quarter range."""
    return _range_position(_op_margin(opinc, revenue), _TD_2Y)


def mgc_ext_016_op_margin_range_pos_12q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin position within its trailing 12-quarter range."""
    return _range_position(_op_margin(opinc, revenue), _TD_3Y)


def mgc_ext_017_ebitda_margin_range_pos_8q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin position within its trailing 8-quarter range."""
    return _range_position(_ebitda_margin(ebitda, revenue), _TD_2Y)


def mgc_ext_018_net_margin_range_pos_12q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin position within its trailing 12-quarter range."""
    return _range_position(_net_margin(netinc, revenue), _TD_3Y)


def mgc_ext_019_gross_margin_at_4q_low_flag(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: gross margin at or below its trailing 4-quarter minimum."""
    gm = _gross_margin(gp, revenue)
    return (gm <= _rolling_min(gm, _TD_YEAR)).astype(float)


def mgc_ext_020_op_margin_at_8q_low_flag(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: operating margin at or below its trailing 8-quarter minimum."""
    om = _op_margin(opinc, revenue)
    return (om <= _rolling_min(om, _TD_2Y)).astype(float)


def mgc_ext_021_net_margin_at_12q_low_flag(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: net margin at or below its trailing 12-quarter minimum."""
    nm = _net_margin(netinc, revenue)
    return (nm <= _rolling_min(nm, _TD_3Y)).astype(float)


def mgc_ext_022_gross_margin_at_ath_low_flag(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: gross margin at or below its all-history expanding minimum."""
    gm = _gross_margin(gp, revenue)
    return (gm <= gm.expanding(min_periods=1).min()).astype(float)


def mgc_ext_023_op_margin_below_8q_avg_flag(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: operating margin strictly below its trailing 8-quarter average."""
    om = _op_margin(opinc, revenue)
    return (om < _rolling_mean(om, _TD_2Y)).astype(float)


def mgc_ext_024_ebitda_margin_at_8q_low_flag(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: EBITDA margin at or below its trailing 8-quarter minimum."""
    em = _ebitda_margin(ebitda, revenue)
    return (em <= _rolling_min(em, _TD_2Y)).astype(float)


# --- Group C (025-036): Margin acceleration (change of change) ---

def mgc_ext_025_gross_margin_qoq_accel(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Acceleration of gross margin: QoQ change minus prior-quarter QoQ change."""
    d = _gross_margin(gp, revenue).diff(_TD_QTR)
    return d - d.shift(_TD_QTR)


def mgc_ext_026_op_margin_qoq_accel(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Acceleration of operating margin QoQ change."""
    d = _op_margin(opinc, revenue).diff(_TD_QTR)
    return d - d.shift(_TD_QTR)


def mgc_ext_027_net_margin_qoq_accel(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Acceleration of net margin QoQ change."""
    d = _net_margin(netinc, revenue).diff(_TD_QTR)
    return d - d.shift(_TD_QTR)


def mgc_ext_028_ebitda_margin_qoq_accel(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Acceleration of EBITDA margin QoQ change."""
    d = _ebitda_margin(ebitda, revenue).diff(_TD_QTR)
    return d - d.shift(_TD_QTR)


def mgc_ext_029_gross_margin_yoy_accel(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Acceleration of gross margin: YoY change minus prior-year YoY change."""
    d = _gross_margin(gp, revenue).diff(_TD_YEAR)
    return d - d.shift(_TD_YEAR)


def mgc_ext_030_op_margin_decline_worsening_flag(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Flag: operating margin declining QoQ and decline deeper than prior quarter."""
    d = _op_margin(opinc, revenue).diff(_TD_QTR)
    return ((d < 0) & (d < d.shift(_TD_QTR))).astype(float)


def mgc_ext_031_gross_margin_chg_slope_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of QoQ gross margin change (smoothed compression rate)."""
    return _rolling_mean(_gross_margin(gp, revenue).diff(_TD_QTR), _TD_YEAR)


def mgc_ext_032_op_margin_chg_slope_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 8-quarter mean of QoQ operating margin change."""
    return _rolling_mean(_op_margin(opinc, revenue).diff(_TD_QTR), _TD_2Y)


def mgc_ext_033_net_margin_chg_slope_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of QoQ net margin change."""
    return _rolling_mean(_net_margin(netinc, revenue).diff(_TD_QTR), _TD_YEAR)


def mgc_ext_034_gross_margin_second_diff(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second difference of gross margin at quarterly cadence (curvature)."""
    d = _gross_margin(gp, revenue).diff(_TD_QTR)
    return d.diff(_TD_QTR)


def mgc_ext_035_op_margin_worst_qoq_drop_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Worst (most negative) single QoQ operating margin change over trailing 8 quarters."""
    return _rolling_min(_op_margin(opinc, revenue).diff(_TD_QTR), _TD_2Y)


def mgc_ext_036_net_margin_worst_qoq_drop_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Worst (most negative) single QoQ net margin change over trailing 8 quarters."""
    return _rolling_min(_net_margin(netinc, revenue).diff(_TD_QTR), _TD_2Y)


# --- Group D (037-048): Recovery distance and peak-drawdown variants ---

def mgc_ext_037_gross_margin_recovery_from_4q_low(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin minus its trailing 4-quarter minimum (rebound off trough)."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_min(gm, _TD_YEAR)


def mgc_ext_038_op_margin_recovery_from_8q_low(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus its trailing 8-quarter minimum."""
    om = _op_margin(opinc, revenue)
    return om - _rolling_min(om, _TD_2Y)


def mgc_ext_039_net_margin_recovery_from_12q_low(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin minus its trailing 12-quarter minimum."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_min(nm, _TD_3Y)


def mgc_ext_040_gross_margin_dd_from_2q_peak(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin drawdown from its trailing 2-quarter (126-day) peak."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_max(gm, _TD_2Q)


def mgc_ext_041_gross_margin_dd_from_12q_peak(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Gross margin drawdown from its trailing 12-quarter peak."""
    gm = _gross_margin(gp, revenue)
    return gm - _rolling_max(gm, _TD_3Y)


def mgc_ext_042_op_margin_dd_from_12q_peak(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin drawdown from its trailing 12-quarter peak."""
    om = _op_margin(opinc, revenue)
    return om - _rolling_max(om, _TD_3Y)


def mgc_ext_043_ebitda_margin_dd_from_12q_peak(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin drawdown from its trailing 12-quarter peak."""
    em = _ebitda_margin(ebitda, revenue)
    return em - _rolling_max(em, _TD_3Y)


def mgc_ext_044_net_margin_dd_from_12q_peak(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin drawdown from its trailing 12-quarter peak."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_max(nm, _TD_3Y)


def mgc_ext_045_ebit_margin_dd_from_8q_peak(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBIT margin drawdown from its trailing 8-quarter peak."""
    em = _ebit_margin(ebit, revenue)
    return em - _rolling_max(em, _TD_2Y)


def mgc_ext_046_pretax_margin_dd_from_8q_peak(ebt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Pretax margin drawdown from its trailing 8-quarter peak."""
    pm = _pretax_margin(ebt, revenue)
    return pm - _rolling_max(pm, _TD_2Y)


def mgc_ext_047_op_margin_dd_intensity_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current 8q operating-margin drawdown as fraction of worst 8q drawdown over 5y."""
    om = _op_margin(opinc, revenue)
    dd = om - _rolling_max(om, _TD_2Y)
    return _safe_div(dd, _rolling_min(dd, _TD_5Y).abs())


def mgc_ext_048_gross_margin_time_below_peak_frac_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Fraction of trailing 8 quarters gross margin spent below its 8q peak."""
    gm = _gross_margin(gp, revenue)
    flag = (gm < _rolling_max(gm, _TD_2Y)).astype(float)
    return _rolling_mean(flag, _TD_2Y)


# --- Group E (049-060): Percentile rank, z-score, EWM deviation variants ---

def mgc_ext_049_gross_margin_zscore_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of gross margin over the trailing 8-quarter window."""
    return _zscore_rolling(_gross_margin(gp, revenue), _TD_2Y)


def mgc_ext_050_gross_margin_zscore_12q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of gross margin over the trailing 12-quarter window."""
    return _zscore_rolling(_gross_margin(gp, revenue), _TD_3Y)


def mgc_ext_051_op_margin_zscore_12q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating margin over the trailing 12-quarter window."""
    return _zscore_rolling(_op_margin(opinc, revenue), _TD_3Y)


def mgc_ext_052_net_margin_zscore_12q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of net margin over the trailing 12-quarter window."""
    return _zscore_rolling(_net_margin(netinc, revenue), _TD_3Y)


def mgc_ext_053_gross_margin_pct_rank_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of gross margin within trailing 4-quarter window."""
    return _rolling_rank_pct(_gross_margin(gp, revenue), _TD_YEAR)


def mgc_ext_054_gross_margin_pct_rank_12q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of gross margin within trailing 12-quarter window."""
    return _rolling_rank_pct(_gross_margin(gp, revenue), _TD_3Y)


def mgc_ext_055_op_margin_pct_rank_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of operating margin within trailing 8-quarter window."""
    return _rolling_rank_pct(_op_margin(opinc, revenue), _TD_2Y)


def mgc_ext_056_net_margin_pct_rank_12q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of net margin within trailing 12-quarter window."""
    return _rolling_rank_pct(_net_margin(netinc, revenue), _TD_3Y)


def mgc_ext_057_ebitda_margin_pct_rank_8q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Percentile rank of EBITDA margin within trailing 8-quarter window."""
    return _rolling_rank_pct(_ebitda_margin(ebitda, revenue), _TD_2Y)


def mgc_ext_058_gross_margin_expanding_zscore(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Expanding all-history z-score of gross margin."""
    gm = _gross_margin(gp, revenue)
    m = gm.expanding(min_periods=2).mean()
    sd = gm.expanding(min_periods=2).std()
    return _safe_div(gm - m, sd)


def mgc_ext_059_op_margin_vs_ewm_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus its trailing 8-quarter exponentially-weighted mean."""
    om = _op_margin(opinc, revenue)
    return om - _ewm_mean(om, _TD_2Y)


def mgc_ext_060_net_margin_vs_8q_median(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Net margin minus its trailing 8-quarter median."""
    nm = _net_margin(netinc, revenue)
    return nm - _rolling_median(nm, _TD_2Y)


# --- Group F (061-068): Cost-ratio rises and dispersion ---

def mgc_ext_061_cor_ratio_2y_change(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in cost-of-revenue ratio (rising = sustained gross compression)."""
    return _safe_div(cor, revenue).diff(_TD_2Y)


def mgc_ext_062_cor_ratio_zscore_8q(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of cost-of-revenue ratio over the trailing 8-quarter window."""
    return _zscore_rolling(_safe_div(cor, revenue), _TD_2Y)


def mgc_ext_063_opex_ratio_2y_change(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in operating-expense ratio."""
    return _safe_div(opex, revenue).diff(_TD_2Y)


def mgc_ext_064_opex_ratio_zscore_8q(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of operating-expense ratio over the trailing 8-quarter window."""
    return _zscore_rolling(_safe_div(opex, revenue), _TD_2Y)


def mgc_ext_065_sgna_ratio_yoy_change(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in SG&A-to-revenue ratio (rising = overhead margin drag)."""
    return _safe_div(sgna, revenue).diff(_TD_YEAR)


def mgc_ext_066_rnd_ratio_qoq_change(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in R&D-to-revenue ratio."""
    return _safe_div(rnd, revenue).diff(_TD_QTR)


def mgc_ext_067_intexp_ratio_2y_change(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """2-year change in interest-expense-to-revenue ratio (financing burden trend)."""
    return _safe_div(intexp, revenue).diff(_TD_2Y)


def mgc_ext_068_depamor_ratio_yoy_change(depamor: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY change in depreciation-and-amortization-to-revenue ratio."""
    return _safe_div(depamor, revenue).diff(_TD_YEAR)


# --- Group G (069-075): Cross-margin streaks, spreads, and composites ---

def mgc_ext_069_gross_margin_below_zero_count_3y(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count of days in the trailing 3 years with negative gross margin."""
    gm = _gross_margin(gp, revenue)
    return _rolling_sum((gm < 0).astype(float), _TD_3Y)


def mgc_ext_070_op_margin_negative_fraction_3y(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Fraction of the trailing 3-year window with negative operating margin."""
    om = _op_margin(opinc, revenue)
    return _rolling_mean((om < 0).astype(float), _TD_3Y)


def mgc_ext_071_op_to_net_margin_spread(opinc: pd.Series, netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Operating margin minus net margin (below-the-line drag: interest, tax, items)."""
    return _op_margin(opinc, revenue) - _net_margin(netinc, revenue)


def mgc_ext_072_ebitda_to_op_margin_spread(ebitda: pd.Series, opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """EBITDA margin minus operating margin (the D&A add-back component)."""
    return _ebitda_margin(ebitda, revenue) - _op_margin(opinc, revenue)


def mgc_ext_073_multi_margin_at_low_score(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """Count of margin lines (gross/op/ebitda/net) at their trailing 8-quarter low — range 0-4."""
    def _atlow(m):
        return (m <= _rolling_min(m, _TD_2Y)).astype(float)
    return (_atlow(_gross_margin(gp, revenue)) + _atlow(_op_margin(opinc, revenue))
            + _atlow(_ebitda_margin(ebitda, revenue)) + _atlow(_net_margin(netinc, revenue)))


def mgc_ext_074_multi_margin_yoy_decline_score(
    gp: pd.Series, opinc: pd.Series, ebitda: pd.Series,
    netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """Count of margin lines (gross/op/ebitda/net) with negative YoY change — range 0-4."""
    g = (_gross_margin(gp, revenue).diff(_TD_YEAR) < 0).astype(float)
    o = (_op_margin(opinc, revenue).diff(_TD_YEAR) < 0).astype(float)
    e = (_ebitda_margin(ebitda, revenue).diff(_TD_YEAR) < 0).astype(float)
    n = (_net_margin(netinc, revenue).diff(_TD_YEAR) < 0).astype(float)
    return g + o + e + n


def mgc_ext_075_margin_compression_severity_composite(
    gp: pd.Series, opinc: pd.Series, netinc: pd.Series, revenue: pd.Series
) -> pd.Series:
    """Composite compression severity: gross-margin depth-from-12q-peak, inverse 12q
    pct-rank of operating margin, and abs 12q z-score of net margin. Higher = worse."""
    gm = _gross_margin(gp, revenue)
    depth = (_rolling_max(gm, _TD_3Y) - gm).clip(lower=0.0, upper=1.0)
    rank = _rolling_rank_pct(_op_margin(opinc, revenue), _TD_3Y).fillna(0.5)
    z = _zscore_rolling(_net_margin(netinc, revenue), _TD_3Y).abs().clip(upper=3.0) / 3.0
    return depth + (1.0 - rank) + z


# ── Registry ───────────────────────────────────────────────────────────────────

MARGIN_COMPRESSION_EXTENDED_REGISTRY_001_075 = {
    "mgc_ext_001_gross_margin_2q_change": {"inputs": ["gp", "revenue"], "func": mgc_ext_001_gross_margin_2q_change},
    "mgc_ext_002_gross_margin_3q_change": {"inputs": ["gp", "revenue"], "func": mgc_ext_002_gross_margin_3q_change},
    "mgc_ext_003_gross_margin_3y_change": {"inputs": ["gp", "revenue"], "func": mgc_ext_003_gross_margin_3y_change},
    "mgc_ext_004_op_margin_2q_change": {"inputs": ["opinc", "revenue"], "func": mgc_ext_004_op_margin_2q_change},
    "mgc_ext_005_op_margin_3y_change": {"inputs": ["opinc", "revenue"], "func": mgc_ext_005_op_margin_3y_change},
    "mgc_ext_006_ebitda_margin_2q_change": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_006_ebitda_margin_2q_change},
    "mgc_ext_007_ebitda_margin_3y_change": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_007_ebitda_margin_3y_change},
    "mgc_ext_008_net_margin_2q_change": {"inputs": ["netinc", "revenue"], "func": mgc_ext_008_net_margin_2q_change},
    "mgc_ext_009_net_margin_2y_change": {"inputs": ["netinc", "revenue"], "func": mgc_ext_009_net_margin_2y_change},
    "mgc_ext_010_pretax_margin_2y_change": {"inputs": ["ebt", "revenue"], "func": mgc_ext_010_pretax_margin_2y_change},
    "mgc_ext_011_ebit_margin_2q_change": {"inputs": ["ebit", "revenue"], "func": mgc_ext_011_ebit_margin_2q_change},
    "mgc_ext_012_ebit_margin_2y_change": {"inputs": ["ebit", "revenue"], "func": mgc_ext_012_ebit_margin_2y_change},
    "mgc_ext_013_gross_margin_range_pos_4q": {"inputs": ["gp", "revenue"], "func": mgc_ext_013_gross_margin_range_pos_4q},
    "mgc_ext_014_gross_margin_range_pos_12q": {"inputs": ["gp", "revenue"], "func": mgc_ext_014_gross_margin_range_pos_12q},
    "mgc_ext_015_op_margin_range_pos_8q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_015_op_margin_range_pos_8q},
    "mgc_ext_016_op_margin_range_pos_12q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_016_op_margin_range_pos_12q},
    "mgc_ext_017_ebitda_margin_range_pos_8q": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_017_ebitda_margin_range_pos_8q},
    "mgc_ext_018_net_margin_range_pos_12q": {"inputs": ["netinc", "revenue"], "func": mgc_ext_018_net_margin_range_pos_12q},
    "mgc_ext_019_gross_margin_at_4q_low_flag": {"inputs": ["gp", "revenue"], "func": mgc_ext_019_gross_margin_at_4q_low_flag},
    "mgc_ext_020_op_margin_at_8q_low_flag": {"inputs": ["opinc", "revenue"], "func": mgc_ext_020_op_margin_at_8q_low_flag},
    "mgc_ext_021_net_margin_at_12q_low_flag": {"inputs": ["netinc", "revenue"], "func": mgc_ext_021_net_margin_at_12q_low_flag},
    "mgc_ext_022_gross_margin_at_ath_low_flag": {"inputs": ["gp", "revenue"], "func": mgc_ext_022_gross_margin_at_ath_low_flag},
    "mgc_ext_023_op_margin_below_8q_avg_flag": {"inputs": ["opinc", "revenue"], "func": mgc_ext_023_op_margin_below_8q_avg_flag},
    "mgc_ext_024_ebitda_margin_at_8q_low_flag": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_024_ebitda_margin_at_8q_low_flag},
    "mgc_ext_025_gross_margin_qoq_accel": {"inputs": ["gp", "revenue"], "func": mgc_ext_025_gross_margin_qoq_accel},
    "mgc_ext_026_op_margin_qoq_accel": {"inputs": ["opinc", "revenue"], "func": mgc_ext_026_op_margin_qoq_accel},
    "mgc_ext_027_net_margin_qoq_accel": {"inputs": ["netinc", "revenue"], "func": mgc_ext_027_net_margin_qoq_accel},
    "mgc_ext_028_ebitda_margin_qoq_accel": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_028_ebitda_margin_qoq_accel},
    "mgc_ext_029_gross_margin_yoy_accel": {"inputs": ["gp", "revenue"], "func": mgc_ext_029_gross_margin_yoy_accel},
    "mgc_ext_030_op_margin_decline_worsening_flag": {"inputs": ["opinc", "revenue"], "func": mgc_ext_030_op_margin_decline_worsening_flag},
    "mgc_ext_031_gross_margin_chg_slope_4q": {"inputs": ["gp", "revenue"], "func": mgc_ext_031_gross_margin_chg_slope_4q},
    "mgc_ext_032_op_margin_chg_slope_8q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_032_op_margin_chg_slope_8q},
    "mgc_ext_033_net_margin_chg_slope_4q": {"inputs": ["netinc", "revenue"], "func": mgc_ext_033_net_margin_chg_slope_4q},
    "mgc_ext_034_gross_margin_second_diff": {"inputs": ["gp", "revenue"], "func": mgc_ext_034_gross_margin_second_diff},
    "mgc_ext_035_op_margin_worst_qoq_drop_8q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_035_op_margin_worst_qoq_drop_8q},
    "mgc_ext_036_net_margin_worst_qoq_drop_8q": {"inputs": ["netinc", "revenue"], "func": mgc_ext_036_net_margin_worst_qoq_drop_8q},
    "mgc_ext_037_gross_margin_recovery_from_4q_low": {"inputs": ["gp", "revenue"], "func": mgc_ext_037_gross_margin_recovery_from_4q_low},
    "mgc_ext_038_op_margin_recovery_from_8q_low": {"inputs": ["opinc", "revenue"], "func": mgc_ext_038_op_margin_recovery_from_8q_low},
    "mgc_ext_039_net_margin_recovery_from_12q_low": {"inputs": ["netinc", "revenue"], "func": mgc_ext_039_net_margin_recovery_from_12q_low},
    "mgc_ext_040_gross_margin_dd_from_2q_peak": {"inputs": ["gp", "revenue"], "func": mgc_ext_040_gross_margin_dd_from_2q_peak},
    "mgc_ext_041_gross_margin_dd_from_12q_peak": {"inputs": ["gp", "revenue"], "func": mgc_ext_041_gross_margin_dd_from_12q_peak},
    "mgc_ext_042_op_margin_dd_from_12q_peak": {"inputs": ["opinc", "revenue"], "func": mgc_ext_042_op_margin_dd_from_12q_peak},
    "mgc_ext_043_ebitda_margin_dd_from_12q_peak": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_043_ebitda_margin_dd_from_12q_peak},
    "mgc_ext_044_net_margin_dd_from_12q_peak": {"inputs": ["netinc", "revenue"], "func": mgc_ext_044_net_margin_dd_from_12q_peak},
    "mgc_ext_045_ebit_margin_dd_from_8q_peak": {"inputs": ["ebit", "revenue"], "func": mgc_ext_045_ebit_margin_dd_from_8q_peak},
    "mgc_ext_046_pretax_margin_dd_from_8q_peak": {"inputs": ["ebt", "revenue"], "func": mgc_ext_046_pretax_margin_dd_from_8q_peak},
    "mgc_ext_047_op_margin_dd_intensity_8q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_047_op_margin_dd_intensity_8q},
    "mgc_ext_048_gross_margin_time_below_peak_frac_8q": {"inputs": ["gp", "revenue"], "func": mgc_ext_048_gross_margin_time_below_peak_frac_8q},
    "mgc_ext_049_gross_margin_zscore_8q": {"inputs": ["gp", "revenue"], "func": mgc_ext_049_gross_margin_zscore_8q},
    "mgc_ext_050_gross_margin_zscore_12q": {"inputs": ["gp", "revenue"], "func": mgc_ext_050_gross_margin_zscore_12q},
    "mgc_ext_051_op_margin_zscore_12q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_051_op_margin_zscore_12q},
    "mgc_ext_052_net_margin_zscore_12q": {"inputs": ["netinc", "revenue"], "func": mgc_ext_052_net_margin_zscore_12q},
    "mgc_ext_053_gross_margin_pct_rank_4q": {"inputs": ["gp", "revenue"], "func": mgc_ext_053_gross_margin_pct_rank_4q},
    "mgc_ext_054_gross_margin_pct_rank_12q": {"inputs": ["gp", "revenue"], "func": mgc_ext_054_gross_margin_pct_rank_12q},
    "mgc_ext_055_op_margin_pct_rank_8q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_055_op_margin_pct_rank_8q},
    "mgc_ext_056_net_margin_pct_rank_12q": {"inputs": ["netinc", "revenue"], "func": mgc_ext_056_net_margin_pct_rank_12q},
    "mgc_ext_057_ebitda_margin_pct_rank_8q": {"inputs": ["ebitda", "revenue"], "func": mgc_ext_057_ebitda_margin_pct_rank_8q},
    "mgc_ext_058_gross_margin_expanding_zscore": {"inputs": ["gp", "revenue"], "func": mgc_ext_058_gross_margin_expanding_zscore},
    "mgc_ext_059_op_margin_vs_ewm_8q": {"inputs": ["opinc", "revenue"], "func": mgc_ext_059_op_margin_vs_ewm_8q},
    "mgc_ext_060_net_margin_vs_8q_median": {"inputs": ["netinc", "revenue"], "func": mgc_ext_060_net_margin_vs_8q_median},
    "mgc_ext_061_cor_ratio_2y_change": {"inputs": ["cor", "revenue"], "func": mgc_ext_061_cor_ratio_2y_change},
    "mgc_ext_062_cor_ratio_zscore_8q": {"inputs": ["cor", "revenue"], "func": mgc_ext_062_cor_ratio_zscore_8q},
    "mgc_ext_063_opex_ratio_2y_change": {"inputs": ["opex", "revenue"], "func": mgc_ext_063_opex_ratio_2y_change},
    "mgc_ext_064_opex_ratio_zscore_8q": {"inputs": ["opex", "revenue"], "func": mgc_ext_064_opex_ratio_zscore_8q},
    "mgc_ext_065_sgna_ratio_yoy_change": {"inputs": ["sgna", "revenue"], "func": mgc_ext_065_sgna_ratio_yoy_change},
    "mgc_ext_066_rnd_ratio_qoq_change": {"inputs": ["rnd", "revenue"], "func": mgc_ext_066_rnd_ratio_qoq_change},
    "mgc_ext_067_intexp_ratio_2y_change": {"inputs": ["intexp", "revenue"], "func": mgc_ext_067_intexp_ratio_2y_change},
    "mgc_ext_068_depamor_ratio_yoy_change": {"inputs": ["depamor", "revenue"], "func": mgc_ext_068_depamor_ratio_yoy_change},
    "mgc_ext_069_gross_margin_below_zero_count_3y": {"inputs": ["gp", "revenue"], "func": mgc_ext_069_gross_margin_below_zero_count_3y},
    "mgc_ext_070_op_margin_negative_fraction_3y": {"inputs": ["opinc", "revenue"], "func": mgc_ext_070_op_margin_negative_fraction_3y},
    "mgc_ext_071_op_to_net_margin_spread": {"inputs": ["opinc", "netinc", "revenue"], "func": mgc_ext_071_op_to_net_margin_spread},
    "mgc_ext_072_ebitda_to_op_margin_spread": {"inputs": ["ebitda", "opinc", "revenue"], "func": mgc_ext_072_ebitda_to_op_margin_spread},
    "mgc_ext_073_multi_margin_at_low_score": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_ext_073_multi_margin_at_low_score},
    "mgc_ext_074_multi_margin_yoy_decline_score": {"inputs": ["gp", "opinc", "ebitda", "netinc", "revenue"], "func": mgc_ext_074_multi_margin_yoy_decline_score},
    "mgc_ext_075_margin_compression_severity_composite": {"inputs": ["gp", "opinc", "netinc", "revenue"], "func": mgc_ext_075_margin_compression_severity_composite},
}
