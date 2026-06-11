"""
73_earnings_volatility — Base Features 001-075
Domain: instability / variance of the earnings series (rolling std, CV, swing
        magnitude, sign-change frequency, downside deviation, range, margin
        dispersion, volatility-of-volatility, residual variance around trend)
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
days, 1 year = 252 trading days.  All feature functions in this file look
strictly backward.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252   # 1 year in trading days
_TD_2Y    = 504
_TD_3Y    = 756
_TD_5Y    = 1260
_TD_QTR   = 63    # 1 quarter in trading days
_TD_2Q    = 126
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(2, span // 4)).std()


def _qoq_diff(s: pd.Series) -> pd.Series:
    """Quarter-over-quarter absolute change on the daily-forward-filled series."""
    return s - s.shift(_TD_QTR)


def _yoy_diff(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_YEAR)


def _cv(s: pd.Series, w: int) -> pd.Series:
    """Coefficient of variation = std / |mean| within a rolling window."""
    return _safe_div_abs(_rolling_std(s, w), _rolling_mean(s, w))


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Rolling std / variance of net income ---

def evl_001_netinc_std_4q(netinc: pd.Series) -> pd.Series:
    """Rolling std of net income over trailing 4 quarters (252 days)."""
    return _rolling_std(netinc, _TD_YEAR)


def evl_002_netinc_std_8q(netinc: pd.Series) -> pd.Series:
    """Rolling std of net income over trailing 8 quarters (504 days)."""
    return _rolling_std(netinc, _TD_2Y)


def evl_003_netinc_std_12q(netinc: pd.Series) -> pd.Series:
    """Rolling std of net income over trailing 12 quarters (756 days)."""
    return _rolling_std(netinc, _TD_3Y)


def evl_004_netinc_std_20q(netinc: pd.Series) -> pd.Series:
    """Rolling std of net income over trailing 20 quarters (1260 days)."""
    return _rolling_std(netinc, _TD_5Y)


def evl_005_netinc_variance_4q(netinc: pd.Series) -> pd.Series:
    """Rolling variance of net income over trailing 4 quarters."""
    return netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).var()


def evl_006_netinc_variance_8q(netinc: pd.Series) -> pd.Series:
    """Rolling variance of net income over trailing 8 quarters."""
    return netinc.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).var()


def evl_007_netinc_cv_4q(netinc: pd.Series) -> pd.Series:
    """Coefficient of variation (std / |mean|) of net income over 4 quarters."""
    return _cv(netinc, _TD_YEAR)


def evl_008_netinc_cv_8q(netinc: pd.Series) -> pd.Series:
    """Coefficient of variation of net income over 8 quarters."""
    return _cv(netinc, _TD_2Y)


def evl_009_netinc_cv_12q(netinc: pd.Series) -> pd.Series:
    """Coefficient of variation of net income over 12 quarters."""
    return _cv(netinc, _TD_3Y)


def evl_010_netinc_cv_20q(netinc: pd.Series) -> pd.Series:
    """Coefficient of variation of net income over 20 quarters."""
    return _cv(netinc, _TD_5Y)


def evl_011_netinccmn_std_4q(netinccmn: pd.Series) -> pd.Series:
    """Rolling std of net income (common) over 4 quarters."""
    return _rolling_std(netinccmn, _TD_YEAR)


def evl_012_netinccmn_std_8q(netinccmn: pd.Series) -> pd.Series:
    """Rolling std of net income (common) over 8 quarters."""
    return _rolling_std(netinccmn, _TD_2Y)


def evl_013_netinccmn_cv_4q(netinccmn: pd.Series) -> pd.Series:
    """Coefficient of variation of net income (common) over 4 quarters."""
    return _cv(netinccmn, _TD_YEAR)


def evl_014_netinc_ewm_std_4q(netinc: pd.Series) -> pd.Series:
    """Exponentially weighted std of net income (span=252 days)."""
    return _ewm_std(netinc, _TD_YEAR)


def evl_015_netinc_ewm_std_8q(netinc: pd.Series) -> pd.Series:
    """Exponentially weighted std of net income (span=504 days)."""
    return _ewm_std(netinc, _TD_2Y)


# --- Group B (016-030): Rolling std / CV of EPS, EBIT, EBITDA, OPINC ---

def evl_016_eps_std_4q(eps: pd.Series) -> pd.Series:
    """Rolling std of EPS over 4 quarters (252 days)."""
    return _rolling_std(eps, _TD_YEAR)


def evl_017_eps_std_8q(eps: pd.Series) -> pd.Series:
    """Rolling std of EPS over 8 quarters (504 days)."""
    return _rolling_std(eps, _TD_2Y)


def evl_018_eps_cv_4q(eps: pd.Series) -> pd.Series:
    """Coefficient of variation of EPS over 4 quarters."""
    return _cv(eps, _TD_YEAR)


def evl_019_eps_cv_8q(eps: pd.Series) -> pd.Series:
    """Coefficient of variation of EPS over 8 quarters."""
    return _cv(eps, _TD_2Y)


def evl_020_epsdil_std_4q(epsdil: pd.Series) -> pd.Series:
    """Rolling std of diluted EPS over 4 quarters."""
    return _rolling_std(epsdil, _TD_YEAR)


def evl_021_epsdil_cv_4q(epsdil: pd.Series) -> pd.Series:
    """Coefficient of variation of diluted EPS over 4 quarters."""
    return _cv(epsdil, _TD_YEAR)


def evl_022_ebit_std_4q(ebit: pd.Series) -> pd.Series:
    """Rolling std of EBIT over 4 quarters."""
    return _rolling_std(ebit, _TD_YEAR)


def evl_023_ebit_std_8q(ebit: pd.Series) -> pd.Series:
    """Rolling std of EBIT over 8 quarters."""
    return _rolling_std(ebit, _TD_2Y)


def evl_024_ebit_cv_4q(ebit: pd.Series) -> pd.Series:
    """Coefficient of variation of EBIT over 4 quarters."""
    return _cv(ebit, _TD_YEAR)


def evl_025_ebitda_std_4q(ebitda: pd.Series) -> pd.Series:
    """Rolling std of EBITDA over 4 quarters."""
    return _rolling_std(ebitda, _TD_YEAR)


def evl_026_ebitda_std_8q(ebitda: pd.Series) -> pd.Series:
    """Rolling std of EBITDA over 8 quarters."""
    return _rolling_std(ebitda, _TD_2Y)


def evl_027_ebitda_cv_4q(ebitda: pd.Series) -> pd.Series:
    """Coefficient of variation of EBITDA over 4 quarters."""
    return _cv(ebitda, _TD_YEAR)


def evl_028_opinc_std_4q(opinc: pd.Series) -> pd.Series:
    """Rolling std of operating income over 4 quarters."""
    return _rolling_std(opinc, _TD_YEAR)


def evl_029_opinc_cv_4q(opinc: pd.Series) -> pd.Series:
    """Coefficient of variation of operating income over 4 quarters."""
    return _cv(opinc, _TD_YEAR)


def evl_030_gp_std_4q(gp: pd.Series) -> pd.Series:
    """Rolling std of gross profit over 4 quarters."""
    return _rolling_std(gp, _TD_YEAR)


# --- Group C (031-045): QoQ swing magnitude and earnings range ---

def evl_031_netinc_qoq_swing_abs_4q(netinc: pd.Series) -> pd.Series:
    """Mean absolute QoQ swing of net income over trailing 4 quarters."""
    swings = _qoq_diff(netinc).abs()
    return _rolling_mean(swings, _TD_YEAR)


def evl_032_netinc_qoq_swing_abs_8q(netinc: pd.Series) -> pd.Series:
    """Mean absolute QoQ swing of net income over trailing 8 quarters."""
    swings = _qoq_diff(netinc).abs()
    return _rolling_mean(swings, _TD_2Y)


def evl_033_netinc_qoq_swing_max_4q(netinc: pd.Series) -> pd.Series:
    """Maximum absolute QoQ swing of net income over trailing 4 quarters."""
    swings = _qoq_diff(netinc).abs()
    return _rolling_max(swings, _TD_YEAR)


def evl_034_netinc_qoq_swing_max_8q(netinc: pd.Series) -> pd.Series:
    """Maximum absolute QoQ swing of net income over trailing 8 quarters."""
    swings = _qoq_diff(netinc).abs()
    return _rolling_max(swings, _TD_2Y)


def evl_035_eps_qoq_swing_abs_4q(eps: pd.Series) -> pd.Series:
    """Mean absolute QoQ swing of EPS over trailing 4 quarters."""
    swings = _qoq_diff(eps).abs()
    return _rolling_mean(swings, _TD_YEAR)


def evl_036_eps_qoq_swing_max_4q(eps: pd.Series) -> pd.Series:
    """Maximum absolute QoQ swing of EPS over trailing 4 quarters."""
    swings = _qoq_diff(eps).abs()
    return _rolling_max(swings, _TD_YEAR)


def evl_037_netinc_range_4q(netinc: pd.Series) -> pd.Series:
    """Earnings range (max - min) of net income over trailing 4 quarters."""
    return _rolling_max(netinc, _TD_YEAR) - _rolling_min(netinc, _TD_YEAR)


def evl_038_netinc_range_8q(netinc: pd.Series) -> pd.Series:
    """Earnings range of net income over trailing 8 quarters."""
    return _rolling_max(netinc, _TD_2Y) - _rolling_min(netinc, _TD_2Y)


def evl_039_netinc_range_12q(netinc: pd.Series) -> pd.Series:
    """Earnings range of net income over trailing 12 quarters."""
    return _rolling_max(netinc, _TD_3Y) - _rolling_min(netinc, _TD_3Y)


def evl_040_eps_range_4q(eps: pd.Series) -> pd.Series:
    """EPS range (max - min) over trailing 4 quarters."""
    return _rolling_max(eps, _TD_YEAR) - _rolling_min(eps, _TD_YEAR)


def evl_041_ebit_range_4q(ebit: pd.Series) -> pd.Series:
    """EBIT range over trailing 4 quarters."""
    return _rolling_max(ebit, _TD_YEAR) - _rolling_min(ebit, _TD_YEAR)


def evl_042_netinc_range_to_mean_4q(netinc: pd.Series) -> pd.Series:
    """Net income range divided by |mean| over 4 quarters — normalized volatility proxy."""
    rng = _rolling_max(netinc, _TD_YEAR) - _rolling_min(netinc, _TD_YEAR)
    return _safe_div_abs(rng, _rolling_mean(netinc, _TD_YEAR))


def evl_043_netinc_iqr_4q(netinc: pd.Series) -> pd.Series:
    """
    Inter-quartile range of net income over 4 quarters (Q75 - Q25).
    Robust dispersion measure less sensitive to outliers.
    """
    q75 = netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.75)
    q25 = netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.25)
    return q75 - q25


def evl_044_netinc_iqr_8q(netinc: pd.Series) -> pd.Series:
    """IQR of net income over 8 quarters."""
    q75 = netinc.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).quantile(0.75)
    q25 = netinc.rolling(_TD_2Y, min_periods=max(2, _TD_2Y // 4)).quantile(0.25)
    return q75 - q25


def evl_045_ebitda_range_8q(ebitda: pd.Series) -> pd.Series:
    """EBITDA range over trailing 8 quarters."""
    return _rolling_max(ebitda, _TD_2Y) - _rolling_min(ebitda, _TD_2Y)


# --- Group D (046-060): Sign-change frequency (profit/loss flip-flopping) ---

def evl_046_netinc_sign_changes_4q(netinc: pd.Series) -> pd.Series:
    """
    Count of profit/loss sign changes in trailing 4 quarters.
    A sign change occurs when sgn(netinc) != sgn(netinc.shift(63)).
    """
    sign = np.sign(netinc)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_YEAR)


def evl_047_netinc_sign_changes_8q(netinc: pd.Series) -> pd.Series:
    """Count of profit/loss sign changes in trailing 8 quarters."""
    sign = np.sign(netinc)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_2Y)


def evl_048_netinc_sign_changes_12q(netinc: pd.Series) -> pd.Series:
    """Count of profit/loss sign changes in trailing 12 quarters."""
    sign = np.sign(netinc)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_3Y)


def evl_049_eps_sign_changes_4q(eps: pd.Series) -> pd.Series:
    """Count of EPS sign changes (positive <-> negative) in trailing 4 quarters."""
    sign = np.sign(eps)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_YEAR)


def evl_050_eps_sign_changes_8q(eps: pd.Series) -> pd.Series:
    """Count of EPS sign changes in trailing 8 quarters."""
    sign = np.sign(eps)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_2Y)


def evl_051_ebit_sign_changes_4q(ebit: pd.Series) -> pd.Series:
    """Count of EBIT sign changes in trailing 4 quarters."""
    sign = np.sign(ebit)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_YEAR)


def evl_052_netinc_sign_change_rate_4q(netinc: pd.Series) -> pd.Series:
    """Fraction of QoQ steps in trailing 4q that involved a sign change."""
    sign = np.sign(netinc)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_mean(changed, _TD_YEAR)


def evl_053_netinc_sign_change_rate_8q(netinc: pd.Series) -> pd.Series:
    """Fraction of QoQ steps in trailing 8q that involved a sign change."""
    sign = np.sign(netinc)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_mean(changed, _TD_2Y)


def evl_054_ncfo_sign_changes_4q(ncfo: pd.Series) -> pd.Series:
    """Count of operating cash-flow sign changes in trailing 4 quarters."""
    sign = np.sign(ncfo)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_YEAR)


def evl_055_opinc_sign_changes_4q(opinc: pd.Series) -> pd.Series:
    """Count of operating income sign changes in trailing 4 quarters."""
    sign = np.sign(opinc)
    changed = (sign != sign.shift(_TD_QTR)).astype(float)
    return _rolling_sum(changed, _TD_YEAR)


# --- Group E (056-065): Downside / semi-deviation of earnings ---

def evl_056_netinc_downside_dev_4q(netinc: pd.Series) -> pd.Series:
    """
    Semi-deviation of net income below zero (downside-only volatility), 4-quarter window.
    sqrt( mean( min(netinc, 0)^2 ) ) within rolling window.
    """
    below = netinc.clip(upper=0)
    sq = below ** 2
    return _rolling_mean(sq, _TD_YEAR).apply(np.sqrt)


def evl_057_netinc_downside_dev_8q(netinc: pd.Series) -> pd.Series:
    """Semi-deviation of net income below zero, 8-quarter window."""
    below = netinc.clip(upper=0)
    sq = below ** 2
    return _rolling_mean(sq, _TD_2Y).apply(np.sqrt)


def evl_058_eps_downside_dev_4q(eps: pd.Series) -> pd.Series:
    """Semi-deviation of EPS below zero, 4-quarter window."""
    below = eps.clip(upper=0)
    sq = below ** 2
    return _rolling_mean(sq, _TD_YEAR).apply(np.sqrt)


def evl_059_ebit_downside_dev_4q(ebit: pd.Series) -> pd.Series:
    """Semi-deviation of EBIT below zero, 4-quarter window."""
    below = ebit.clip(upper=0)
    sq = below ** 2
    return _rolling_mean(sq, _TD_YEAR).apply(np.sqrt)


def evl_060_netinc_downside_dev_below_mean_4q(netinc: pd.Series) -> pd.Series:
    """
    Semi-deviation of net income below its rolling 4q mean (downside vs trend).
    sqrt( mean( min(netinc - mean, 0)^2 ) ).
    """
    mu = _rolling_mean(netinc, _TD_YEAR)
    dev = (netinc - mu).clip(upper=0)
    return _rolling_mean(dev ** 2, _TD_YEAR).apply(np.sqrt)


def evl_061_ncfo_downside_dev_4q(ncfo: pd.Series) -> pd.Series:
    """Semi-deviation of operating cash flow below zero, 4-quarter window."""
    below = ncfo.clip(upper=0)
    sq = below ** 2
    return _rolling_mean(sq, _TD_YEAR).apply(np.sqrt)


def evl_062_netinc_qoq_swing_std_4q(netinc: pd.Series) -> pd.Series:
    """Std of the QoQ swing series of net income over trailing 4 quarters."""
    swings = _qoq_diff(netinc)
    return _rolling_std(swings, _TD_YEAR)


def evl_063_eps_qoq_swing_std_4q(eps: pd.Series) -> pd.Series:
    """Std of the QoQ swing series of EPS over trailing 4 quarters."""
    swings = _qoq_diff(eps)
    return _rolling_std(swings, _TD_YEAR)


def evl_064_ncfo_std_4q(ncfo: pd.Series) -> pd.Series:
    """Rolling std of operating cash flow over 4 quarters."""
    return _rolling_std(ncfo, _TD_YEAR)


def evl_065_ncfo_cv_4q(ncfo: pd.Series) -> pd.Series:
    """Coefficient of variation of operating cash flow over 4 quarters."""
    return _cv(ncfo, _TD_YEAR)


# --- Group F (066-075): Revenue, gross-profit, and FCF volatility ---

def evl_066_revenue_std_4q(revenue: pd.Series) -> pd.Series:
    """Rolling std of revenue over 4 quarters."""
    return _rolling_std(revenue, _TD_YEAR)


def evl_067_revenue_std_8q(revenue: pd.Series) -> pd.Series:
    """Rolling std of revenue over 8 quarters."""
    return _rolling_std(revenue, _TD_2Y)


def evl_068_revenue_cv_4q(revenue: pd.Series) -> pd.Series:
    """Coefficient of variation of revenue over 4 quarters."""
    return _cv(revenue, _TD_YEAR)


def evl_069_gp_std_8q(gp: pd.Series) -> pd.Series:
    """Rolling std of gross profit over 8 quarters."""
    return _rolling_std(gp, _TD_2Y)


def evl_070_gp_cv_4q(gp: pd.Series) -> pd.Series:
    """Coefficient of variation of gross profit over 4 quarters."""
    return _cv(gp, _TD_YEAR)


def evl_071_fcf_std_4q(fcf: pd.Series) -> pd.Series:
    """Rolling std of free cash flow over 4 quarters."""
    return _rolling_std(fcf, _TD_YEAR)


def evl_072_fcf_cv_4q(fcf: pd.Series) -> pd.Series:
    """Coefficient of variation of free cash flow over 4 quarters."""
    return _cv(fcf, _TD_YEAR)


def evl_073_fcf_downside_dev_4q(fcf: pd.Series) -> pd.Series:
    """Semi-deviation of free cash flow below zero, 4-quarter window."""
    below = fcf.clip(upper=0)
    sq = below ** 2
    return _rolling_mean(sq, _TD_YEAR).apply(np.sqrt)


def evl_074_netinc_std_expanding(netinc: pd.Series) -> pd.Series:
    """Expanding (all-history) std of net income — long-run baseline volatility."""
    return netinc.expanding(min_periods=2).std()


def evl_075_earnings_volatility_composite_4q(
    netinc: pd.Series,
    eps: pd.Series,
    ebit: pd.Series,
) -> pd.Series:
    """
    Composite earnings-volatility score: equally weighted average of the
    4-quarter CVs of netinc, eps, and ebit (all absolute values of CV).
    """
    cv_ni   = _cv(netinc, _TD_YEAR).abs()
    cv_eps  = _cv(eps,    _TD_YEAR).abs()
    cv_ebit = _cv(ebit,   _TD_YEAR).abs()
    return (cv_ni + cv_eps + cv_ebit) / 3.0


# ── Registry 001-075 ──────────────────────────────────────────────────────────

EARNINGS_VOLATILITY_REGISTRY_001_075 = {
    "evl_001_netinc_std_4q":                      {"inputs": ["netinc"],                    "func": evl_001_netinc_std_4q},
    "evl_002_netinc_std_8q":                      {"inputs": ["netinc"],                    "func": evl_002_netinc_std_8q},
    "evl_003_netinc_std_12q":                     {"inputs": ["netinc"],                    "func": evl_003_netinc_std_12q},
    "evl_004_netinc_std_20q":                     {"inputs": ["netinc"],                    "func": evl_004_netinc_std_20q},
    "evl_005_netinc_variance_4q":                 {"inputs": ["netinc"],                    "func": evl_005_netinc_variance_4q},
    "evl_006_netinc_variance_8q":                 {"inputs": ["netinc"],                    "func": evl_006_netinc_variance_8q},
    "evl_007_netinc_cv_4q":                       {"inputs": ["netinc"],                    "func": evl_007_netinc_cv_4q},
    "evl_008_netinc_cv_8q":                       {"inputs": ["netinc"],                    "func": evl_008_netinc_cv_8q},
    "evl_009_netinc_cv_12q":                      {"inputs": ["netinc"],                    "func": evl_009_netinc_cv_12q},
    "evl_010_netinc_cv_20q":                      {"inputs": ["netinc"],                    "func": evl_010_netinc_cv_20q},
    "evl_011_netinccmn_std_4q":                   {"inputs": ["netinccmn"],                 "func": evl_011_netinccmn_std_4q},
    "evl_012_netinccmn_std_8q":                   {"inputs": ["netinccmn"],                 "func": evl_012_netinccmn_std_8q},
    "evl_013_netinccmn_cv_4q":                    {"inputs": ["netinccmn"],                 "func": evl_013_netinccmn_cv_4q},
    "evl_014_netinc_ewm_std_4q":                  {"inputs": ["netinc"],                    "func": evl_014_netinc_ewm_std_4q},
    "evl_015_netinc_ewm_std_8q":                  {"inputs": ["netinc"],                    "func": evl_015_netinc_ewm_std_8q},
    "evl_016_eps_std_4q":                         {"inputs": ["eps"],                       "func": evl_016_eps_std_4q},
    "evl_017_eps_std_8q":                         {"inputs": ["eps"],                       "func": evl_017_eps_std_8q},
    "evl_018_eps_cv_4q":                          {"inputs": ["eps"],                       "func": evl_018_eps_cv_4q},
    "evl_019_eps_cv_8q":                          {"inputs": ["eps"],                       "func": evl_019_eps_cv_8q},
    "evl_020_epsdil_std_4q":                      {"inputs": ["epsdil"],                    "func": evl_020_epsdil_std_4q},
    "evl_021_epsdil_cv_4q":                       {"inputs": ["epsdil"],                    "func": evl_021_epsdil_cv_4q},
    "evl_022_ebit_std_4q":                        {"inputs": ["ebit"],                      "func": evl_022_ebit_std_4q},
    "evl_023_ebit_std_8q":                        {"inputs": ["ebit"],                      "func": evl_023_ebit_std_8q},
    "evl_024_ebit_cv_4q":                         {"inputs": ["ebit"],                      "func": evl_024_ebit_cv_4q},
    "evl_025_ebitda_std_4q":                      {"inputs": ["ebitda"],                    "func": evl_025_ebitda_std_4q},
    "evl_026_ebitda_std_8q":                      {"inputs": ["ebitda"],                    "func": evl_026_ebitda_std_8q},
    "evl_027_ebitda_cv_4q":                       {"inputs": ["ebitda"],                    "func": evl_027_ebitda_cv_4q},
    "evl_028_opinc_std_4q":                       {"inputs": ["opinc"],                     "func": evl_028_opinc_std_4q},
    "evl_029_opinc_cv_4q":                        {"inputs": ["opinc"],                     "func": evl_029_opinc_cv_4q},
    "evl_030_gp_std_4q":                          {"inputs": ["gp"],                        "func": evl_030_gp_std_4q},
    "evl_031_netinc_qoq_swing_abs_4q":            {"inputs": ["netinc"],                    "func": evl_031_netinc_qoq_swing_abs_4q},
    "evl_032_netinc_qoq_swing_abs_8q":            {"inputs": ["netinc"],                    "func": evl_032_netinc_qoq_swing_abs_8q},
    "evl_033_netinc_qoq_swing_max_4q":            {"inputs": ["netinc"],                    "func": evl_033_netinc_qoq_swing_max_4q},
    "evl_034_netinc_qoq_swing_max_8q":            {"inputs": ["netinc"],                    "func": evl_034_netinc_qoq_swing_max_8q},
    "evl_035_eps_qoq_swing_abs_4q":               {"inputs": ["eps"],                       "func": evl_035_eps_qoq_swing_abs_4q},
    "evl_036_eps_qoq_swing_max_4q":               {"inputs": ["eps"],                       "func": evl_036_eps_qoq_swing_max_4q},
    "evl_037_netinc_range_4q":                    {"inputs": ["netinc"],                    "func": evl_037_netinc_range_4q},
    "evl_038_netinc_range_8q":                    {"inputs": ["netinc"],                    "func": evl_038_netinc_range_8q},
    "evl_039_netinc_range_12q":                   {"inputs": ["netinc"],                    "func": evl_039_netinc_range_12q},
    "evl_040_eps_range_4q":                       {"inputs": ["eps"],                       "func": evl_040_eps_range_4q},
    "evl_041_ebit_range_4q":                      {"inputs": ["ebit"],                      "func": evl_041_ebit_range_4q},
    "evl_042_netinc_range_to_mean_4q":            {"inputs": ["netinc"],                    "func": evl_042_netinc_range_to_mean_4q},
    "evl_043_netinc_iqr_4q":                      {"inputs": ["netinc"],                    "func": evl_043_netinc_iqr_4q},
    "evl_044_netinc_iqr_8q":                      {"inputs": ["netinc"],                    "func": evl_044_netinc_iqr_8q},
    "evl_045_ebitda_range_8q":                    {"inputs": ["ebitda"],                    "func": evl_045_ebitda_range_8q},
    "evl_046_netinc_sign_changes_4q":             {"inputs": ["netinc"],                    "func": evl_046_netinc_sign_changes_4q},
    "evl_047_netinc_sign_changes_8q":             {"inputs": ["netinc"],                    "func": evl_047_netinc_sign_changes_8q},
    "evl_048_netinc_sign_changes_12q":            {"inputs": ["netinc"],                    "func": evl_048_netinc_sign_changes_12q},
    "evl_049_eps_sign_changes_4q":                {"inputs": ["eps"],                       "func": evl_049_eps_sign_changes_4q},
    "evl_050_eps_sign_changes_8q":                {"inputs": ["eps"],                       "func": evl_050_eps_sign_changes_8q},
    "evl_051_ebit_sign_changes_4q":               {"inputs": ["ebit"],                      "func": evl_051_ebit_sign_changes_4q},
    "evl_052_netinc_sign_change_rate_4q":         {"inputs": ["netinc"],                    "func": evl_052_netinc_sign_change_rate_4q},
    "evl_053_netinc_sign_change_rate_8q":         {"inputs": ["netinc"],                    "func": evl_053_netinc_sign_change_rate_8q},
    "evl_054_ncfo_sign_changes_4q":               {"inputs": ["ncfo"],                      "func": evl_054_ncfo_sign_changes_4q},
    "evl_055_opinc_sign_changes_4q":              {"inputs": ["opinc"],                     "func": evl_055_opinc_sign_changes_4q},
    "evl_056_netinc_downside_dev_4q":             {"inputs": ["netinc"],                    "func": evl_056_netinc_downside_dev_4q},
    "evl_057_netinc_downside_dev_8q":             {"inputs": ["netinc"],                    "func": evl_057_netinc_downside_dev_8q},
    "evl_058_eps_downside_dev_4q":                {"inputs": ["eps"],                       "func": evl_058_eps_downside_dev_4q},
    "evl_059_ebit_downside_dev_4q":               {"inputs": ["ebit"],                      "func": evl_059_ebit_downside_dev_4q},
    "evl_060_netinc_downside_dev_below_mean_4q":  {"inputs": ["netinc"],                    "func": evl_060_netinc_downside_dev_below_mean_4q},
    "evl_061_ncfo_downside_dev_4q":               {"inputs": ["ncfo"],                      "func": evl_061_ncfo_downside_dev_4q},
    "evl_062_netinc_qoq_swing_std_4q":            {"inputs": ["netinc"],                    "func": evl_062_netinc_qoq_swing_std_4q},
    "evl_063_eps_qoq_swing_std_4q":               {"inputs": ["eps"],                       "func": evl_063_eps_qoq_swing_std_4q},
    "evl_064_ncfo_std_4q":                        {"inputs": ["ncfo"],                      "func": evl_064_ncfo_std_4q},
    "evl_065_ncfo_cv_4q":                         {"inputs": ["ncfo"],                      "func": evl_065_ncfo_cv_4q},
    "evl_066_revenue_std_4q":                     {"inputs": ["revenue"],                   "func": evl_066_revenue_std_4q},
    "evl_067_revenue_std_8q":                     {"inputs": ["revenue"],                   "func": evl_067_revenue_std_8q},
    "evl_068_revenue_cv_4q":                      {"inputs": ["revenue"],                   "func": evl_068_revenue_cv_4q},
    "evl_069_gp_std_8q":                          {"inputs": ["gp"],                        "func": evl_069_gp_std_8q},
    "evl_070_gp_cv_4q":                           {"inputs": ["gp"],                        "func": evl_070_gp_cv_4q},
    "evl_071_fcf_std_4q":                         {"inputs": ["fcf"],                       "func": evl_071_fcf_std_4q},
    "evl_072_fcf_cv_4q":                          {"inputs": ["fcf"],                       "func": evl_072_fcf_cv_4q},
    "evl_073_fcf_downside_dev_4q":                {"inputs": ["fcf"],                       "func": evl_073_fcf_downside_dev_4q},
    "evl_074_netinc_std_expanding":               {"inputs": ["netinc"],                    "func": evl_074_netinc_std_expanding},
    "evl_075_earnings_volatility_composite_4q":   {"inputs": ["netinc", "eps", "ebit"],     "func": evl_075_earnings_volatility_composite_4q},
}
