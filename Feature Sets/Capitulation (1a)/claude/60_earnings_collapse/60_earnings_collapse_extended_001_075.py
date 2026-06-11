"""
60_earnings_collapse — Extended Features 001-075
Domain: net-income decline, loss onset, magnitude of earnings collapse —
        additional variants: new horizons, range positions, acceleration,
        recovery-distance, TTM aggregates, dispersion, cross-line composites
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_4Y    = 1008
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_TD_3Q    = 189
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _range_position(s: pd.Series, w: int) -> pd.Series:
    """Position of s within its trailing w-window range: 0=at low, 1=at high."""
    mn = _rolling_min(s, w)
    mx = _rolling_max(s, w)
    return _safe_div(s - mn, mx - mn)


def _streak_negative(s: pd.Series) -> pd.Series:
    """Consecutive-day streak length where s < 0 (resets to 0 otherwise)."""
    neg = (s < 0).astype(int)
    arr = neg.values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1.0) * arr[i]
    return pd.Series(out, index=s.index)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Additional change horizons (half-year, 3Q, 4-year) ---

def ecl_ext_001_netinc_2q_change(netinc: pd.Series) -> pd.Series:
    """Net income change over 2 quarters (126-day lag)."""
    return netinc - netinc.shift(_TD_2Q)


def ecl_ext_002_netinc_3q_change(netinc: pd.Series) -> pd.Series:
    """Net income change over 3 quarters (189-day lag)."""
    return netinc - netinc.shift(_TD_3Q)


def ecl_ext_003_netinc_4y_change(netinc: pd.Series) -> pd.Series:
    """Net income change over 4 years (1008-day lag)."""
    return netinc - netinc.shift(_TD_4Y)


def ecl_ext_004_netinc_2q_pct(netinc: pd.Series) -> pd.Series:
    """Net income 2-quarter percent change; denominator abs(prior)."""
    prior = netinc.shift(_TD_2Q)
    return _safe_div_abs(netinc - prior, prior)


def ecl_ext_005_netinc_3q_pct(netinc: pd.Series) -> pd.Series:
    """Net income 3-quarter percent change; denominator abs(prior)."""
    prior = netinc.shift(_TD_3Q)
    return _safe_div_abs(netinc - prior, prior)


def ecl_ext_006_netinc_5y_pct(netinc: pd.Series) -> pd.Series:
    """Net income 5-year percent change; denominator abs(prior)."""
    prior = netinc.shift(_TD_5Y)
    return _safe_div_abs(netinc - prior, prior)


def ecl_ext_007_eps_2q_change(eps: pd.Series) -> pd.Series:
    """Basic EPS change over 2 quarters."""
    return eps - eps.shift(_TD_2Q)


def ecl_ext_008_eps_2y_change(eps: pd.Series) -> pd.Series:
    """Basic EPS change over 2 years."""
    return eps - eps.shift(_TD_2Y)


def ecl_ext_009_epsdil_2y_change(epsdil: pd.Series) -> pd.Series:
    """Diluted EPS change over 2 years."""
    return epsdil - epsdil.shift(_TD_2Y)


def ecl_ext_010_ebit_2y_change(ebit: pd.Series) -> pd.Series:
    """EBIT change over 2 years."""
    return ebit - ebit.shift(_TD_2Y)


def ecl_ext_011_ebitda_yoy_change(ebitda: pd.Series) -> pd.Series:
    """EBITDA YoY absolute change."""
    return ebitda - ebitda.shift(_TD_YEAR)


def ecl_ext_012_ebt_yoy_change(ebt: pd.Series) -> pd.Series:
    """EBT YoY absolute change."""
    return ebt - ebt.shift(_TD_YEAR)


# --- Group B (013-024): Range position within trailing earnings windows ---

def ecl_ext_013_netinc_range_pos_4q(netinc: pd.Series) -> pd.Series:
    """Net income position within trailing 4-quarter range (0=low, 1=high)."""
    return _range_position(netinc, _TD_YEAR)


def ecl_ext_014_netinc_range_pos_8q(netinc: pd.Series) -> pd.Series:
    """Net income position within trailing 8-quarter range."""
    return _range_position(netinc, _TD_2Y)


def ecl_ext_015_netinc_range_pos_12q(netinc: pd.Series) -> pd.Series:
    """Net income position within trailing 12-quarter range."""
    return _range_position(netinc, _TD_3Y)


def ecl_ext_016_netinc_range_pos_20q(netinc: pd.Series) -> pd.Series:
    """Net income position within trailing 20-quarter (5-year) range."""
    return _range_position(netinc, _TD_5Y)


def ecl_ext_017_eps_range_pos_4q(eps: pd.Series) -> pd.Series:
    """EPS position within trailing 4-quarter range."""
    return _range_position(eps, _TD_YEAR)


def ecl_ext_018_eps_range_pos_12q(eps: pd.Series) -> pd.Series:
    """EPS position within trailing 12-quarter range."""
    return _range_position(eps, _TD_3Y)


def ecl_ext_019_ebit_range_pos_8q(ebit: pd.Series) -> pd.Series:
    """EBIT position within trailing 8-quarter range."""
    return _range_position(ebit, _TD_2Y)


def ecl_ext_020_ebitda_range_pos_8q(ebitda: pd.Series) -> pd.Series:
    """EBITDA position within trailing 8-quarter range."""
    return _range_position(ebitda, _TD_2Y)


def ecl_ext_021_netinc_at_4q_low_flag(netinc: pd.Series) -> pd.Series:
    """Binary flag: net income at or below its trailing 4-quarter minimum."""
    return (netinc <= _rolling_min(netinc, _TD_YEAR)).astype(float)


def ecl_ext_022_netinc_at_12q_low_flag(netinc: pd.Series) -> pd.Series:
    """Binary flag: net income at or below its trailing 12-quarter minimum."""
    return (netinc <= _rolling_min(netinc, _TD_3Y)).astype(float)


def ecl_ext_023_netinc_at_alltime_low_flag(netinc: pd.Series) -> pd.Series:
    """Binary flag: net income at or below its all-history expanding minimum."""
    return (netinc <= netinc.expanding(min_periods=1).min()).astype(float)


def ecl_ext_024_eps_at_8q_low_flag(eps: pd.Series) -> pd.Series:
    """Binary flag: EPS at or below its trailing 8-quarter minimum."""
    return (eps <= _rolling_min(eps, _TD_2Y)).astype(float)


# --- Group C (025-036): Earnings acceleration (change of change) ---

def ecl_ext_025_netinc_qoq_accel(netinc: pd.Series) -> pd.Series:
    """Acceleration of net income: QoQ change minus prior-quarter QoQ change."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return qoq - qoq.shift(_TD_QTR)


def ecl_ext_026_netinc_yoy_accel(netinc: pd.Series) -> pd.Series:
    """Acceleration of net income: YoY change minus prior-year YoY change."""
    yoy = netinc - netinc.shift(_TD_YEAR)
    return yoy - yoy.shift(_TD_YEAR)


def ecl_ext_027_eps_qoq_accel(eps: pd.Series) -> pd.Series:
    """Acceleration of EPS: QoQ change minus prior-quarter QoQ change."""
    qoq = eps - eps.shift(_TD_QTR)
    return qoq - qoq.shift(_TD_QTR)


def ecl_ext_028_ebit_yoy_accel(ebit: pd.Series) -> pd.Series:
    """Acceleration of EBIT: YoY change minus prior-year YoY change."""
    yoy = ebit - ebit.shift(_TD_YEAR)
    return yoy - yoy.shift(_TD_YEAR)


def ecl_ext_029_netinc_qoq_pct_accel(netinc: pd.Series) -> pd.Series:
    """Acceleration of net income QoQ percent growth rate."""
    g = _safe_div_abs(netinc - netinc.shift(_TD_QTR), netinc.shift(_TD_QTR))
    return g - g.shift(_TD_QTR)


def ecl_ext_030_netinc_decline_worsening_flag(netinc: pd.Series) -> pd.Series:
    """Flag: net income declining QoQ and the decline larger than prior quarter."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return ((qoq < 0) & (qoq < qoq.shift(_TD_QTR))).astype(float)


def ecl_ext_031_netinc_growth_slope_4q(netinc: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of QoQ net income change (smoothed growth slope)."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return _rolling_mean(qoq, _TD_YEAR)


def ecl_ext_032_netinc_growth_slope_8q(netinc: pd.Series) -> pd.Series:
    """Trailing 8-quarter mean of QoQ net income change."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return _rolling_mean(qoq, _TD_2Y)


def ecl_ext_033_eps_growth_slope_4q(eps: pd.Series) -> pd.Series:
    """Trailing 4-quarter mean of QoQ EPS change."""
    qoq = eps - eps.shift(_TD_QTR)
    return _rolling_mean(qoq, _TD_YEAR)


def ecl_ext_034_netinc_second_diff(netinc: pd.Series) -> pd.Series:
    """Second difference of net income at quarterly cadence (curvature)."""
    d1 = netinc - netinc.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def ecl_ext_035_netinc_qoq_chg_minus_yoy_chg(netinc: pd.Series) -> pd.Series:
    """QoQ net income change minus YoY net income change (short vs long divergence)."""
    qoq = netinc - netinc.shift(_TD_QTR)
    yoy = netinc - netinc.shift(_TD_YEAR)
    return qoq - yoy


def ecl_ext_036_netinc_worst_qoq_drop_8q(netinc: pd.Series) -> pd.Series:
    """Worst (most negative) single QoQ net income change in trailing 8 quarters."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return _rolling_min(qoq, _TD_2Y)


# --- Group D (037-048): Recovery distance and depth-from-peak variants ---

def ecl_ext_037_netinc_recovery_from_4q_low(netinc: pd.Series) -> pd.Series:
    """Net income minus its trailing 4-quarter minimum (rebound off the trough)."""
    return netinc - _rolling_min(netinc, _TD_YEAR)


def ecl_ext_038_netinc_recovery_from_12q_low(netinc: pd.Series) -> pd.Series:
    """Net income minus its trailing 12-quarter minimum."""
    return netinc - _rolling_min(netinc, _TD_3Y)


def ecl_ext_039_netinc_pct_recovery_from_4q_low(netinc: pd.Series) -> pd.Series:
    """Net income rebound off 4-quarter trough as fraction of abs(trough)."""
    mn = _rolling_min(netinc, _TD_YEAR)
    return _safe_div_abs(netinc - mn, mn)


def ecl_ext_040_eps_recovery_from_8q_low(eps: pd.Series) -> pd.Series:
    """EPS minus its trailing 8-quarter minimum."""
    return eps - _rolling_min(eps, _TD_2Y)


def ecl_ext_041_netinc_dd_from_2q_peak(netinc: pd.Series) -> pd.Series:
    """Net income drawdown from trailing 2-quarter (126-day) peak."""
    return netinc - _rolling_max(netinc, _TD_2Q)


def ecl_ext_042_netinc_dd_from_20q_peak(netinc: pd.Series) -> pd.Series:
    """Net income drawdown from trailing 20-quarter (5-year) peak."""
    return netinc - _rolling_max(netinc, _TD_5Y)


def ecl_ext_043_netinc_pct_dd_from_12q_peak(netinc: pd.Series) -> pd.Series:
    """Net income percent drawdown from 12-quarter peak."""
    peak = _rolling_max(netinc, _TD_3Y)
    return _safe_div_abs(netinc - peak, peak)


def ecl_ext_044_eps_dd_from_8q_peak(eps: pd.Series) -> pd.Series:
    """EPS drawdown from trailing 8-quarter peak."""
    return eps - _rolling_max(eps, _TD_2Y)


def ecl_ext_045_eps_pct_dd_from_expanding_peak(eps: pd.Series) -> pd.Series:
    """EPS percent drawdown from all-history expanding peak."""
    peak = eps.expanding(min_periods=1).max()
    return _safe_div_abs(eps - peak, peak)


def ecl_ext_046_ebit_dd_from_8q_peak(ebit: pd.Series) -> pd.Series:
    """EBIT drawdown from trailing 8-quarter peak."""
    return ebit - _rolling_max(ebit, _TD_2Y)


def ecl_ext_047_ebitda_dd_from_8q_peak(ebitda: pd.Series) -> pd.Series:
    """EBITDA drawdown from trailing 8-quarter peak."""
    return ebitda - _rolling_max(ebitda, _TD_2Y)


def ecl_ext_048_netinc_dd_intensity_8q(netinc: pd.Series) -> pd.Series:
    """Current 8q net income drawdown as fraction of worst 8q drawdown over 5y."""
    dd  = _safe_div_abs(netinc - _rolling_max(netinc, _TD_2Y), _rolling_max(netinc, _TD_2Y))
    wdd = _rolling_min(dd, _TD_5Y)
    return _safe_div(dd, wdd.abs())


# --- Group E (049-060): TTM aggregates, sums, and ratios ---

def ecl_ext_049_netinc_ttm_qoq_change(netinc: pd.Series) -> pd.Series:
    """QoQ change in trailing-twelve-month net income (4Q rolling sum)."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return ttm - ttm.shift(_TD_QTR)


def ecl_ext_050_netinc_ttm_yoy_change(netinc: pd.Series) -> pd.Series:
    """YoY change in trailing-twelve-month net income."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return ttm - ttm.shift(_TD_YEAR)


def ecl_ext_051_netinc_ttm_yoy_pct(netinc: pd.Series) -> pd.Series:
    """YoY percent change in TTM net income; denominator abs(prior TTM)."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return _safe_div_abs(ttm - ttm.shift(_TD_YEAR), ttm.shift(_TD_YEAR))


def ecl_ext_052_netinc_ttm_negative_flag(netinc: pd.Series) -> pd.Series:
    """Binary flag: trailing-twelve-month net income is negative (annual loss)."""
    return (_rolling_sum(netinc, _TD_YEAR) < 0).astype(float)


def ecl_ext_053_netinc_ttm_dd_from_peak(netinc: pd.Series) -> pd.Series:
    """TTM net income drawdown from its trailing 5-year peak."""
    ttm = _rolling_sum(netinc, _TD_YEAR)
    return ttm - ttm.rolling(_TD_5Y, min_periods=_TD_YEAR).max()


def ecl_ext_054_eps_ttm_sum(eps: pd.Series) -> pd.Series:
    """Trailing-twelve-month sum of EPS (annualized earnings power proxy)."""
    return _rolling_sum(eps, _TD_YEAR)


def ecl_ext_055_eps_ttm_yoy_change(eps: pd.Series) -> pd.Series:
    """YoY change in trailing-twelve-month EPS."""
    ttm = _rolling_sum(eps, _TD_YEAR)
    return ttm - ttm.shift(_TD_YEAR)


def ecl_ext_056_ebit_ttm_sum(ebit: pd.Series) -> pd.Series:
    """Trailing-twelve-month sum of EBIT."""
    return _rolling_sum(ebit, _TD_YEAR)


def ecl_ext_057_netinc_cumulative_3y_sum(netinc: pd.Series) -> pd.Series:
    """Rolling sum of net income over the last 756 days (3-year cumulative)."""
    return _rolling_sum(netinc, _TD_3Y)


def ecl_ext_058_netinc_3y_to_4q_avg_ratio(netinc: pd.Series) -> pd.Series:
    """Trailing 3-year mean net income divided by trailing 4-quarter mean."""
    return _safe_div_abs(_rolling_mean(netinc, _TD_3Y), _rolling_mean(netinc, _TD_YEAR))


def ecl_ext_059_netinc_to_ebitda_ttm_ratio(netinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    """TTM net income divided by abs(TTM EBITDA) — net earnings quality."""
    return _safe_div_abs(_rolling_sum(netinc, _TD_YEAR), _rolling_sum(ebitda, _TD_YEAR))


def ecl_ext_060_eps_to_ebit_ratio(eps: pd.Series, ebit: pd.Series) -> pd.Series:
    """EPS divided by abs(EBIT) — per-share earnings vs operating profit base."""
    return _safe_div_abs(eps, ebit)


# --- Group F (061-068): Dispersion, volatility, and stability of earnings ---

def ecl_ext_061_netinc_rolling_std_4q(netinc: pd.Series) -> pd.Series:
    """Rolling standard deviation of net income over trailing 4 quarters."""
    return _rolling_std(netinc, _TD_YEAR)


def ecl_ext_062_netinc_rolling_std_8q(netinc: pd.Series) -> pd.Series:
    """Rolling standard deviation of net income over trailing 8 quarters."""
    return _rolling_std(netinc, _TD_2Y)


def ecl_ext_063_netinc_coef_variation_8q(netinc: pd.Series) -> pd.Series:
    """Coefficient of variation of net income over trailing 8 quarters."""
    return _safe_div_abs(_rolling_std(netinc, _TD_2Y), _rolling_mean(netinc, _TD_2Y))


def ecl_ext_064_eps_rolling_std_8q(eps: pd.Series) -> pd.Series:
    """Rolling standard deviation of EPS over trailing 8 quarters."""
    return _rolling_std(eps, _TD_2Y)


def ecl_ext_065_netinc_qoq_chg_std_8q(netinc: pd.Series) -> pd.Series:
    """Rolling std of QoQ net income change over trailing 8 quarters (volatility of swings)."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return _rolling_std(qoq, _TD_2Y)


def ecl_ext_066_netinc_drop_vs_volatility(netinc: pd.Series) -> pd.Series:
    """Current QoQ net income drop normalized by trailing 8q std of QoQ changes."""
    qoq = netinc - netinc.shift(_TD_QTR)
    return _safe_div(qoq, _rolling_std(qoq, _TD_2Y))


def ecl_ext_067_netinc_below_median_flag_8q(netinc: pd.Series) -> pd.Series:
    """Binary flag: net income strictly below its trailing 8-quarter median."""
    return (netinc < _rolling_median(netinc, _TD_2Y)).astype(float)


def ecl_ext_068_netinc_vs_8q_median_pct(netinc: pd.Series) -> pd.Series:
    """Net income percent deviation from trailing 8-quarter median."""
    med = _rolling_median(netinc, _TD_2Y)
    return _safe_div_abs(netinc - med, med)


# --- Group G (069-075): Loss-intensity composites and cross-line scores ---

def ecl_ext_069_eps_loss_quarters_2y(eps: pd.Series) -> pd.Series:
    """Count of negative-EPS quarters in the trailing 504 days."""
    return _rolling_sum((eps < 0).astype(float), _TD_2Y)


def ecl_ext_070_ebit_loss_fraction_3y(ebit: pd.Series) -> pd.Series:
    """Fraction of the trailing 3-year window with negative EBIT."""
    return _rolling_mean((ebit < 0).astype(float), _TD_3Y)


def ecl_ext_071_eps_consecutive_loss_streak(eps: pd.Series) -> pd.Series:
    """Current consecutive-loss streak length in daily observations for EPS."""
    return _streak_negative(eps)


def ecl_ext_072_netinc_zscore_20q(netinc: pd.Series) -> pd.Series:
    """Z-score of net income within a trailing 20-quarter (5-year) window."""
    return _zscore_rolling(netinc, _TD_5Y)


def ecl_ext_073_netinc_pct_rank_20q(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income within a trailing 20-quarter (5-year) window."""
    return _rolling_rank_pct(netinc, _TD_5Y)


def ecl_ext_074_cross_line_negative_score(
    netinc: pd.Series, eps: pd.Series, ebit: pd.Series, ebitda: pd.Series, ebt: pd.Series
) -> pd.Series:
    """Count of earnings lines (netinc/eps/ebit/ebitda/ebt) currently negative — range 0-5."""
    return ((netinc < 0).astype(float) + (eps < 0).astype(float)
            + (ebit < 0).astype(float) + (ebitda < 0).astype(float)
            + (ebt < 0).astype(float))


def ecl_ext_075_earnings_collapse_severity_composite(
    netinc: pd.Series, eps: pd.Series, ebitda: pd.Series
) -> pd.Series:
    """Composite severity: net income depth-from-12q-peak (%), inverse 12q pct-rank,
    and abs 12q z-score (clipped). Higher = more extreme earnings collapse."""
    peak = _rolling_max(netinc, _TD_3Y)
    depth = _safe_div_abs(peak - netinc, peak).clip(lower=0.0, upper=2.0) / 2.0
    rank = _rolling_rank_pct(netinc, _TD_3Y).fillna(0.5)
    z = _zscore_rolling(eps, _TD_3Y).abs().clip(upper=3.0) / 3.0
    em = _zscore_rolling(ebitda, _TD_3Y).abs().clip(upper=3.0) / 3.0
    return depth + (1.0 - rank) + z + em


# ── Registry 001-075 ──────────────────────────────────────────────────────────

EARNINGS_COLLAPSE_EXTENDED_REGISTRY_001_075 = {
    "ecl_ext_001_netinc_2q_change": {"inputs": ["netinc"], "func": ecl_ext_001_netinc_2q_change},
    "ecl_ext_002_netinc_3q_change": {"inputs": ["netinc"], "func": ecl_ext_002_netinc_3q_change},
    "ecl_ext_003_netinc_4y_change": {"inputs": ["netinc"], "func": ecl_ext_003_netinc_4y_change},
    "ecl_ext_004_netinc_2q_pct": {"inputs": ["netinc"], "func": ecl_ext_004_netinc_2q_pct},
    "ecl_ext_005_netinc_3q_pct": {"inputs": ["netinc"], "func": ecl_ext_005_netinc_3q_pct},
    "ecl_ext_006_netinc_5y_pct": {"inputs": ["netinc"], "func": ecl_ext_006_netinc_5y_pct},
    "ecl_ext_007_eps_2q_change": {"inputs": ["eps"], "func": ecl_ext_007_eps_2q_change},
    "ecl_ext_008_eps_2y_change": {"inputs": ["eps"], "func": ecl_ext_008_eps_2y_change},
    "ecl_ext_009_epsdil_2y_change": {"inputs": ["epsdil"], "func": ecl_ext_009_epsdil_2y_change},
    "ecl_ext_010_ebit_2y_change": {"inputs": ["ebit"], "func": ecl_ext_010_ebit_2y_change},
    "ecl_ext_011_ebitda_yoy_change": {"inputs": ["ebitda"], "func": ecl_ext_011_ebitda_yoy_change},
    "ecl_ext_012_ebt_yoy_change": {"inputs": ["ebt"], "func": ecl_ext_012_ebt_yoy_change},
    "ecl_ext_013_netinc_range_pos_4q": {"inputs": ["netinc"], "func": ecl_ext_013_netinc_range_pos_4q},
    "ecl_ext_014_netinc_range_pos_8q": {"inputs": ["netinc"], "func": ecl_ext_014_netinc_range_pos_8q},
    "ecl_ext_015_netinc_range_pos_12q": {"inputs": ["netinc"], "func": ecl_ext_015_netinc_range_pos_12q},
    "ecl_ext_016_netinc_range_pos_20q": {"inputs": ["netinc"], "func": ecl_ext_016_netinc_range_pos_20q},
    "ecl_ext_017_eps_range_pos_4q": {"inputs": ["eps"], "func": ecl_ext_017_eps_range_pos_4q},
    "ecl_ext_018_eps_range_pos_12q": {"inputs": ["eps"], "func": ecl_ext_018_eps_range_pos_12q},
    "ecl_ext_019_ebit_range_pos_8q": {"inputs": ["ebit"], "func": ecl_ext_019_ebit_range_pos_8q},
    "ecl_ext_020_ebitda_range_pos_8q": {"inputs": ["ebitda"], "func": ecl_ext_020_ebitda_range_pos_8q},
    "ecl_ext_021_netinc_at_4q_low_flag": {"inputs": ["netinc"], "func": ecl_ext_021_netinc_at_4q_low_flag},
    "ecl_ext_022_netinc_at_12q_low_flag": {"inputs": ["netinc"], "func": ecl_ext_022_netinc_at_12q_low_flag},
    "ecl_ext_023_netinc_at_alltime_low_flag": {"inputs": ["netinc"], "func": ecl_ext_023_netinc_at_alltime_low_flag},
    "ecl_ext_024_eps_at_8q_low_flag": {"inputs": ["eps"], "func": ecl_ext_024_eps_at_8q_low_flag},
    "ecl_ext_025_netinc_qoq_accel": {"inputs": ["netinc"], "func": ecl_ext_025_netinc_qoq_accel},
    "ecl_ext_026_netinc_yoy_accel": {"inputs": ["netinc"], "func": ecl_ext_026_netinc_yoy_accel},
    "ecl_ext_027_eps_qoq_accel": {"inputs": ["eps"], "func": ecl_ext_027_eps_qoq_accel},
    "ecl_ext_028_ebit_yoy_accel": {"inputs": ["ebit"], "func": ecl_ext_028_ebit_yoy_accel},
    "ecl_ext_029_netinc_qoq_pct_accel": {"inputs": ["netinc"], "func": ecl_ext_029_netinc_qoq_pct_accel},
    "ecl_ext_030_netinc_decline_worsening_flag": {"inputs": ["netinc"], "func": ecl_ext_030_netinc_decline_worsening_flag},
    "ecl_ext_031_netinc_growth_slope_4q": {"inputs": ["netinc"], "func": ecl_ext_031_netinc_growth_slope_4q},
    "ecl_ext_032_netinc_growth_slope_8q": {"inputs": ["netinc"], "func": ecl_ext_032_netinc_growth_slope_8q},
    "ecl_ext_033_eps_growth_slope_4q": {"inputs": ["eps"], "func": ecl_ext_033_eps_growth_slope_4q},
    "ecl_ext_034_netinc_second_diff": {"inputs": ["netinc"], "func": ecl_ext_034_netinc_second_diff},
    "ecl_ext_035_netinc_qoq_chg_minus_yoy_chg": {"inputs": ["netinc"], "func": ecl_ext_035_netinc_qoq_chg_minus_yoy_chg},
    "ecl_ext_036_netinc_worst_qoq_drop_8q": {"inputs": ["netinc"], "func": ecl_ext_036_netinc_worst_qoq_drop_8q},
    "ecl_ext_037_netinc_recovery_from_4q_low": {"inputs": ["netinc"], "func": ecl_ext_037_netinc_recovery_from_4q_low},
    "ecl_ext_038_netinc_recovery_from_12q_low": {"inputs": ["netinc"], "func": ecl_ext_038_netinc_recovery_from_12q_low},
    "ecl_ext_039_netinc_pct_recovery_from_4q_low": {"inputs": ["netinc"], "func": ecl_ext_039_netinc_pct_recovery_from_4q_low},
    "ecl_ext_040_eps_recovery_from_8q_low": {"inputs": ["eps"], "func": ecl_ext_040_eps_recovery_from_8q_low},
    "ecl_ext_041_netinc_dd_from_2q_peak": {"inputs": ["netinc"], "func": ecl_ext_041_netinc_dd_from_2q_peak},
    "ecl_ext_042_netinc_dd_from_20q_peak": {"inputs": ["netinc"], "func": ecl_ext_042_netinc_dd_from_20q_peak},
    "ecl_ext_043_netinc_pct_dd_from_12q_peak": {"inputs": ["netinc"], "func": ecl_ext_043_netinc_pct_dd_from_12q_peak},
    "ecl_ext_044_eps_dd_from_8q_peak": {"inputs": ["eps"], "func": ecl_ext_044_eps_dd_from_8q_peak},
    "ecl_ext_045_eps_pct_dd_from_expanding_peak": {"inputs": ["eps"], "func": ecl_ext_045_eps_pct_dd_from_expanding_peak},
    "ecl_ext_046_ebit_dd_from_8q_peak": {"inputs": ["ebit"], "func": ecl_ext_046_ebit_dd_from_8q_peak},
    "ecl_ext_047_ebitda_dd_from_8q_peak": {"inputs": ["ebitda"], "func": ecl_ext_047_ebitda_dd_from_8q_peak},
    "ecl_ext_048_netinc_dd_intensity_8q": {"inputs": ["netinc"], "func": ecl_ext_048_netinc_dd_intensity_8q},
    "ecl_ext_049_netinc_ttm_qoq_change": {"inputs": ["netinc"], "func": ecl_ext_049_netinc_ttm_qoq_change},
    "ecl_ext_050_netinc_ttm_yoy_change": {"inputs": ["netinc"], "func": ecl_ext_050_netinc_ttm_yoy_change},
    "ecl_ext_051_netinc_ttm_yoy_pct": {"inputs": ["netinc"], "func": ecl_ext_051_netinc_ttm_yoy_pct},
    "ecl_ext_052_netinc_ttm_negative_flag": {"inputs": ["netinc"], "func": ecl_ext_052_netinc_ttm_negative_flag},
    "ecl_ext_053_netinc_ttm_dd_from_peak": {"inputs": ["netinc"], "func": ecl_ext_053_netinc_ttm_dd_from_peak},
    "ecl_ext_054_eps_ttm_sum": {"inputs": ["eps"], "func": ecl_ext_054_eps_ttm_sum},
    "ecl_ext_055_eps_ttm_yoy_change": {"inputs": ["eps"], "func": ecl_ext_055_eps_ttm_yoy_change},
    "ecl_ext_056_ebit_ttm_sum": {"inputs": ["ebit"], "func": ecl_ext_056_ebit_ttm_sum},
    "ecl_ext_057_netinc_cumulative_3y_sum": {"inputs": ["netinc"], "func": ecl_ext_057_netinc_cumulative_3y_sum},
    "ecl_ext_058_netinc_3y_to_4q_avg_ratio": {"inputs": ["netinc"], "func": ecl_ext_058_netinc_3y_to_4q_avg_ratio},
    "ecl_ext_059_netinc_to_ebitda_ttm_ratio": {"inputs": ["netinc", "ebitda"], "func": ecl_ext_059_netinc_to_ebitda_ttm_ratio},
    "ecl_ext_060_eps_to_ebit_ratio": {"inputs": ["eps", "ebit"], "func": ecl_ext_060_eps_to_ebit_ratio},
    "ecl_ext_061_netinc_rolling_std_4q": {"inputs": ["netinc"], "func": ecl_ext_061_netinc_rolling_std_4q},
    "ecl_ext_062_netinc_rolling_std_8q": {"inputs": ["netinc"], "func": ecl_ext_062_netinc_rolling_std_8q},
    "ecl_ext_063_netinc_coef_variation_8q": {"inputs": ["netinc"], "func": ecl_ext_063_netinc_coef_variation_8q},
    "ecl_ext_064_eps_rolling_std_8q": {"inputs": ["eps"], "func": ecl_ext_064_eps_rolling_std_8q},
    "ecl_ext_065_netinc_qoq_chg_std_8q": {"inputs": ["netinc"], "func": ecl_ext_065_netinc_qoq_chg_std_8q},
    "ecl_ext_066_netinc_drop_vs_volatility": {"inputs": ["netinc"], "func": ecl_ext_066_netinc_drop_vs_volatility},
    "ecl_ext_067_netinc_below_median_flag_8q": {"inputs": ["netinc"], "func": ecl_ext_067_netinc_below_median_flag_8q},
    "ecl_ext_068_netinc_vs_8q_median_pct": {"inputs": ["netinc"], "func": ecl_ext_068_netinc_vs_8q_median_pct},
    "ecl_ext_069_eps_loss_quarters_2y": {"inputs": ["eps"], "func": ecl_ext_069_eps_loss_quarters_2y},
    "ecl_ext_070_ebit_loss_fraction_3y": {"inputs": ["ebit"], "func": ecl_ext_070_ebit_loss_fraction_3y},
    "ecl_ext_071_eps_consecutive_loss_streak": {"inputs": ["eps"], "func": ecl_ext_071_eps_consecutive_loss_streak},
    "ecl_ext_072_netinc_zscore_20q": {"inputs": ["netinc"], "func": ecl_ext_072_netinc_zscore_20q},
    "ecl_ext_073_netinc_pct_rank_20q": {"inputs": ["netinc"], "func": ecl_ext_073_netinc_pct_rank_20q},
    "ecl_ext_074_cross_line_negative_score": {"inputs": ["netinc", "eps", "ebit", "ebitda", "ebt"], "func": ecl_ext_074_cross_line_negative_score},
    "ecl_ext_075_earnings_collapse_severity_composite": {"inputs": ["netinc", "eps", "ebitda"], "func": ecl_ext_075_earnings_collapse_severity_composite},
}
