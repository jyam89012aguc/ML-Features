"""
91_institutional_exit — 2nd-Derivative Features (iex_drv2_001 – iex_drv2_075)
==============================================================================
Domain: Rate-of-change of base institutional-exit features.

These functions compute the *rate-of-change* (QoQ diff via shift(63), OLS slope,
EWM deviation, or acceleration) of selected base feature series from the
91_institutional_exit domain.

NOTE ON SPARSITY: Because the underlying SF3 data is quarterly, both the base
feature series and these derivative series are stepwise/sparse on a daily index.
This is expected and correct — do not attempt to interpolate.

This file is SELF-CONTAINED: it re-implements the required base feature
computations inline as helper functions (prefixed _b_) and requires NO imports
from other feature files.

Quarterly → Daily Alignment Contract
--------------------------------------
All inputs are **daily-frequency** pandas Series, forward-filled from quarterly
Sharadar SF3 13F snapshots.

    1 quarter ≈ 63 trading days  (_TD_QTR)
    1 year    ≈ 252 trading days (_TD_YEAR)
    2 years   ≈ 504 trading days (_TD_2Y)
    3 years   ≈ 756 trading days (_TD_3Y)

Input fields:
    inst_holders        — count of institutional (13F) holders
    inst_shares         — aggregate shares held by all institutions
    inst_value          — aggregate USD market value held
    inst_pct            — institutional ownership fraction (0..1)
    new_positions       — count of holders initiating a position this quarter
    closed_positions    — count of holders fully exiting this quarter
    increased_positions — count of holders adding to a position this quarter
    decreased_positions — count of holders trimming a position this quarter
"""

import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_QTR  = 63
_TD_2Q   = 126
_EPS     = 1e-9

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _align_quarterly_to_daily(series: pd.Series) -> pd.Series:
    """Forward-fill a quarterly Series to a daily index."""
    return series.ffill()


def _safe_div(a, b):
    return a / (b + _EPS)


def _safe_div_abs(a, b):
    return a / (b.abs() + _EPS)


def _rolling_mean(s, w):
    return s.rolling(w, min_periods=1).mean()


def _rolling_std(s, w):
    return s.rolling(w, min_periods=2).std()


def _rolling_max(s, w):
    return s.rolling(w, min_periods=1).max()


def _rolling_min(s, w):
    return s.rolling(w, min_periods=1).min()


def _zscore_rolling(s, w):
    mu = _rolling_mean(s, w)
    sigma = _rolling_std(s, w)
    return _safe_div(s - mu, sigma)


def _ewm_mean(s, span):
    return s.ewm(span=span, adjust=False).mean()


def _ols_slope(s, w):
    """Rolling OLS slope over window w."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        t = np.arange(n, dtype=float)
        t_m = t - t.mean()
        x_m = x - x.mean()
        denom = (t_m ** 2).sum()
        if denom < _EPS:
            return np.nan
        return (t_m * x_m).sum() / denom
    return s.rolling(w, min_periods=2).apply(_slope, raw=True)

# ---------------------------------------------------------------------------
# Inline base-feature recompute helpers (_b_ prefix)
# ---------------------------------------------------------------------------

def _b_holder_qoq_diff(inst_holders):
    return inst_holders - inst_holders.shift(_TD_QTR)


def _b_holder_qoq_pct(inst_holders):
    return _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                     inst_holders.shift(_TD_QTR).abs())


def _b_shares_qoq_pct(inst_shares):
    return _safe_div(inst_shares - inst_shares.shift(_TD_QTR),
                     inst_shares.shift(_TD_QTR).abs())


def _b_inst_pct_qoq_diff(inst_pct):
    return inst_pct - inst_pct.shift(_TD_QTR)


def _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions):
    return (closed_positions + decreased_positions) - (new_positions + increased_positions)


def _b_net_exits_ratio(closed_positions, decreased_positions, new_positions, increased_positions):
    return _safe_div(closed_positions + decreased_positions,
                     new_positions + increased_positions)


def _b_exit_breadth(closed_positions, decreased_positions, inst_holders):
    return _safe_div(closed_positions + decreased_positions, inst_holders)


def _b_holder_drawdown_from_peak(inst_holders):
    peak = inst_holders.expanding(min_periods=1).max()
    return _safe_div(inst_holders - peak, peak.abs())


def _b_inst_pct_drawdown_from_peak(inst_pct):
    peak = inst_pct.expanding(min_periods=1).max()
    return _safe_div(inst_pct - peak, peak.abs())


def _b_shares_drawdown_from_peak(inst_shares):
    peak = inst_shares.expanding(min_periods=1).max()
    return _safe_div(inst_shares - peak, peak.abs())


def _b_holder_zscore_4q(inst_holders):
    return _zscore_rolling(inst_holders, _TD_YEAR)


def _b_inst_pct_zscore_4q(inst_pct):
    return _zscore_rolling(inst_pct, _TD_YEAR)


def _b_shares_zscore_4q(inst_shares):
    return _zscore_rolling(inst_shares, _TD_YEAR)

# ---------------------------------------------------------------------------
# 2nd-derivative feature functions
# ---------------------------------------------------------------------------

def iex_drv2_001_holder_qoq_diff_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the QoQ holder-count diff (velocity of the velocity)."""
    base = _b_holder_qoq_diff(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_002_holder_qoq_pct_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the QoQ % holder-count change."""
    base = _b_holder_qoq_pct(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_003_shares_qoq_pct_qoq_change(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the QoQ % aggregate-shares change."""
    base = _b_shares_qoq_pct(inst_shares)
    return base - base.shift(_TD_QTR)


def iex_drv2_004_inst_pct_qoq_diff_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in the QoQ ownership-fraction diff."""
    base = _b_inst_pct_qoq_diff(inst_pct)
    return base - base.shift(_TD_QTR)


def iex_drv2_005_net_exits_qoq_change(closed_positions: pd.Series,
                                        decreased_positions: pd.Series,
                                        new_positions: pd.Series,
                                        increased_positions: pd.Series) -> pd.Series:
    """QoQ change in net exits (acceleration of exit flow)."""
    base = _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_006_net_exits_ratio_qoq_change(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              new_positions: pd.Series,
                                              increased_positions: pd.Series) -> pd.Series:
    """QoQ change in the exit/entry ratio."""
    base = _b_net_exits_ratio(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_007_exit_breadth_qoq_change(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """QoQ change in exit breadth (fraction of holders reducing)."""
    base = _b_exit_breadth(closed_positions, decreased_positions, inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_008_holder_drawdown_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in holder-count drawdown from all-time peak."""
    base = _b_holder_drawdown_from_peak(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_009_inst_pct_drawdown_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in ownership-fraction drawdown from all-time peak."""
    base = _b_inst_pct_drawdown_from_peak(inst_pct)
    return base - base.shift(_TD_QTR)


def iex_drv2_010_shares_drawdown_qoq_change(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in aggregate-shares drawdown from all-time peak."""
    base = _b_shares_drawdown_from_peak(inst_shares)
    return base - base.shift(_TD_QTR)


def iex_drv2_011_holder_qoq_diff_4q_slope(inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the QoQ holder-count diff series."""
    base = _b_holder_qoq_diff(inst_holders)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_012_shares_qoq_pct_4q_slope(inst_shares: pd.Series) -> pd.Series:
    """4q OLS slope of the QoQ % shares-change series."""
    base = _b_shares_qoq_pct(inst_shares)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_013_inst_pct_qoq_diff_4q_slope(inst_pct: pd.Series) -> pd.Series:
    """4q OLS slope of the QoQ ownership-fraction diff series."""
    base = _b_inst_pct_qoq_diff(inst_pct)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_014_net_exits_4q_slope(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """4q OLS slope of the net-exits series (trend in exit momentum)."""
    base = _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_015_holder_zscore_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling z-score of holder count."""
    base = _b_holder_zscore_4q(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_016_inst_pct_zscore_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling z-score of ownership fraction."""
    base = _b_inst_pct_zscore_4q(inst_pct)
    return base - base.shift(_TD_QTR)


def iex_drv2_017_shares_zscore_qoq_change(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling z-score of aggregate shares."""
    base = _b_shares_zscore_4q(inst_shares)
    return base - base.shift(_TD_QTR)


def iex_drv2_018_holder_qoq_diff_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the QoQ holder-count diff."""
    base = _b_holder_qoq_diff(inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_019_shares_qoq_pct_ewm_deviation(inst_shares: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the QoQ % shares change."""
    base = _b_shares_qoq_pct(inst_shares)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_020_net_exits_ewm_deviation(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the net-exits series."""
    base = _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_021_exit_breadth_ewm_deviation(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of exit breadth."""
    base = _b_exit_breadth(closed_positions, decreased_positions, inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_022_holder_drawdown_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of holder-count drawdown from peak."""
    base = _b_holder_drawdown_from_peak(inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_023_holder_qoq_pct_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    """Z-score of the QoQ % holder change over a 4q window (2nd-order normalization)."""
    base = _b_holder_qoq_pct(inst_holders)
    return _zscore_rolling(base, _TD_YEAR)


def iex_drv2_024_net_exits_ratio_zscore_4q(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             new_positions: pd.Series,
                                             increased_positions: pd.Series) -> pd.Series:
    """Z-score of the exit/entry ratio over a 4q rolling window."""
    base = _b_net_exits_ratio(closed_positions, decreased_positions, new_positions, increased_positions)
    return _zscore_rolling(base, _TD_YEAR)


def iex_drv2_025_inst_pct_drawdown_ewm_deviation(inst_pct: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the ownership-fraction drawdown from peak."""
    base = _b_inst_pct_drawdown_from_peak(inst_pct)
    return base - _ewm_mean(base, _TD_YEAR)


# ---------------------------------------------------------------------------
# Additional inline base helpers for features 026–075
# ---------------------------------------------------------------------------

def _b_value_qoq_pct(inst_value):
    return _safe_div(inst_value - inst_value.shift(_TD_QTR),
                     inst_value.shift(_TD_QTR).abs())


def _b_exit_breadth_8q_mean(closed_positions, decreased_positions, inst_holders):
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _rolling_mean(breadth, _TD_2Y)


def _b_net_exits_4q_mean(closed_positions, decreased_positions, new_positions, increased_positions):
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_mean(net, _TD_YEAR)


def _b_shares_per_holder(inst_shares, inst_holders):
    return _safe_div(inst_shares, inst_holders)


def _b_value_per_holder(inst_value, inst_holders):
    return _safe_div(inst_value, inst_holders)


def _b_net_exits_ratio_4q_mean(closed_positions, decreased_positions, new_positions, increased_positions):
    ratio = _safe_div(closed_positions + decreased_positions,
                      new_positions + increased_positions)
    return _rolling_mean(ratio, _TD_YEAR)


def _b_holder_qoq_diff_normalized(inst_holders):
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    sigma = _rolling_std(diff, _TD_YEAR)
    return _safe_div(diff, sigma)


def _b_holder_yoy_pct(inst_holders):
    return _safe_div(inst_holders - inst_holders.shift(_TD_YEAR),
                     inst_holders.shift(_TD_YEAR).abs())


def _b_inst_pct_zscore_8q(inst_pct):
    return _zscore_rolling(inst_pct, _TD_2Y)


def _b_closed_qoq_pct(closed_positions):
    return _safe_div(closed_positions - closed_positions.shift(_TD_QTR),
                     closed_positions.shift(_TD_QTR).abs())


def _b_decreased_qoq_pct(decreased_positions):
    return _safe_div(decreased_positions - decreased_positions.shift(_TD_QTR),
                     decreased_positions.shift(_TD_QTR).abs())


def _b_exit_fraction_of_total(closed_positions, decreased_positions, new_positions, increased_positions):
    exits = closed_positions + decreased_positions
    total = exits + new_positions + increased_positions
    return _safe_div(exits, total)


def _b_holder_decay_ewm(inst_holders):
    pct = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                    inst_holders.shift(_TD_QTR).abs())
    return pct.ewm(span=_TD_2Q, adjust=False).mean()


def _b_value_zscore_4q(inst_value):
    return _zscore_rolling(inst_value, _TD_YEAR)


def _b_holder_4q_slope(inst_holders):
    return _ols_slope(inst_holders, _TD_YEAR)


def _b_shares_4q_slope(inst_shares):
    return _ols_slope(inst_shares, _TD_YEAR)


def _b_inst_pct_4q_slope(inst_pct):
    return _ols_slope(inst_pct, _TD_YEAR)


# ---------------------------------------------------------------------------
# 2nd-derivative feature functions 026–075
# ---------------------------------------------------------------------------

def iex_drv2_026_holder_qoq_diff_21d_change(inst_holders: pd.Series) -> pd.Series:
    """21-day change in QoQ holder-count diff (shorter-horizon velocity)."""
    base = _b_holder_qoq_diff(inst_holders)
    return base - base.shift(21)


def iex_drv2_027_shares_qoq_pct_21d_change(inst_shares: pd.Series) -> pd.Series:
    """21-day change in QoQ % shares change."""
    base = _b_shares_qoq_pct(inst_shares)
    return base - base.shift(21)


def iex_drv2_028_inst_pct_qoq_diff_21d_change(inst_pct: pd.Series) -> pd.Series:
    """21-day change in QoQ ownership-fraction diff."""
    base = _b_inst_pct_qoq_diff(inst_pct)
    return base - base.shift(21)


def iex_drv2_029_net_exits_21d_change(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """21-day change in net exits."""
    base = _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - base.shift(21)


def iex_drv2_030_value_qoq_pct_qoq_change(inst_value: pd.Series) -> pd.Series:
    """QoQ change in the QoQ % aggregate-value change."""
    base = _b_value_qoq_pct(inst_value)
    return base - base.shift(_TD_QTR)


def iex_drv2_031_value_qoq_pct_ewm_deviation(inst_value: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the QoQ % value change."""
    base = _b_value_qoq_pct(inst_value)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_032_value_qoq_pct_zscore_4q(inst_value: pd.Series) -> pd.Series:
    """Z-score of the QoQ % value change over 4-quarter window."""
    base = _b_value_qoq_pct(inst_value)
    return _zscore_rolling(base, _TD_YEAR)


def iex_drv2_033_value_zscore_4q_qoq_change(inst_value: pd.Series) -> pd.Series:
    """QoQ change in the 4q z-score of aggregate institutional value."""
    base = _b_value_zscore_4q(inst_value)
    return base - base.shift(_TD_QTR)


def iex_drv2_034_exit_breadth_8q_mean_qoq_change(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series,
                                                   inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 8q rolling mean of exit breadth."""
    base = _b_exit_breadth_8q_mean(closed_positions, decreased_positions, inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_035_net_exits_4q_mean_qoq_change(closed_positions: pd.Series,
                                                decreased_positions: pd.Series,
                                                new_positions: pd.Series,
                                                increased_positions: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling mean of net exits."""
    base = _b_net_exits_4q_mean(closed_positions, decreased_positions,
                                 new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_036_shares_per_holder_qoq_change(inst_shares: pd.Series,
                                                inst_holders: pd.Series) -> pd.Series:
    """QoQ change in average shares per holder."""
    base = _b_shares_per_holder(inst_shares, inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_037_shares_per_holder_ewm_deviation(inst_shares: pd.Series,
                                                   inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of shares per holder."""
    base = _b_shares_per_holder(inst_shares, inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_038_value_per_holder_qoq_change(inst_value: pd.Series,
                                               inst_holders: pd.Series) -> pd.Series:
    """QoQ change in average USD value per holder."""
    base = _b_value_per_holder(inst_value, inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_039_value_per_holder_ewm_deviation(inst_value: pd.Series,
                                                  inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of value per holder."""
    base = _b_value_per_holder(inst_value, inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_040_net_exits_ratio_4q_mean_qoq_change(closed_positions: pd.Series,
                                                      decreased_positions: pd.Series,
                                                      new_positions: pd.Series,
                                                      increased_positions: pd.Series) -> pd.Series:
    """QoQ change in the 4q rolling mean of the exit/entry ratio."""
    base = _b_net_exits_ratio_4q_mean(closed_positions, decreased_positions,
                                       new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_041_holder_qoq_diff_norm_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the normalized (signal-to-noise) QoQ holder diff."""
    base = _b_holder_qoq_diff_normalized(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_042_holder_yoy_pct_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the year-over-year % holder change."""
    base = _b_holder_yoy_pct(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_043_inst_pct_zscore_8q_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in the 8q z-score of institutional ownership fraction."""
    base = _b_inst_pct_zscore_8q(inst_pct)
    return base - base.shift(_TD_QTR)


def iex_drv2_044_closed_qoq_pct_qoq_change(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in the QoQ % change of fully-closed positions."""
    base = _b_closed_qoq_pct(closed_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_045_decreased_qoq_pct_qoq_change(decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in the QoQ % change of decreased positions."""
    base = _b_decreased_qoq_pct(decreased_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_046_exit_fraction_qoq_change(closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            new_positions: pd.Series,
                                            increased_positions: pd.Series) -> pd.Series:
    """QoQ change in exit fraction of total activity."""
    base = _b_exit_fraction_of_total(closed_positions, decreased_positions,
                                      new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def iex_drv2_047_exit_fraction_ewm_deviation(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               new_positions: pd.Series,
                                               increased_positions: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of exit fraction of total activity."""
    base = _b_exit_fraction_of_total(closed_positions, decreased_positions,
                                      new_positions, increased_positions)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_048_holder_decay_ewm_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the EWM-smoothed holder decay rate."""
    base = _b_holder_decay_ewm(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_049_holder_4q_slope_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 4q OLS slope of holder count."""
    base = _b_holder_4q_slope(inst_holders)
    return base - base.shift(_TD_QTR)


def iex_drv2_050_shares_4q_slope_qoq_change(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4q OLS slope of aggregate shares."""
    base = _b_shares_4q_slope(inst_shares)
    return base - base.shift(_TD_QTR)


def iex_drv2_051_inst_pct_4q_slope_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in the 4q OLS slope of institutional ownership fraction."""
    base = _b_inst_pct_4q_slope(inst_pct)
    return base - base.shift(_TD_QTR)


def iex_drv2_052_holder_qoq_diff_8q_slope(inst_holders: pd.Series) -> pd.Series:
    """8q OLS slope of the QoQ holder-count diff series."""
    base = _b_holder_qoq_diff(inst_holders)
    return _ols_slope(base, _TD_2Y)


def iex_drv2_053_shares_qoq_pct_8q_slope(inst_shares: pd.Series) -> pd.Series:
    """8q OLS slope of the QoQ % shares-change series."""
    base = _b_shares_qoq_pct(inst_shares)
    return _ols_slope(base, _TD_2Y)


def iex_drv2_054_inst_pct_qoq_diff_8q_slope(inst_pct: pd.Series) -> pd.Series:
    """8q OLS slope of the QoQ ownership-fraction diff series."""
    base = _b_inst_pct_qoq_diff(inst_pct)
    return _ols_slope(base, _TD_2Y)


def iex_drv2_055_net_exits_8q_slope(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     new_positions: pd.Series,
                                     increased_positions: pd.Series) -> pd.Series:
    """8q OLS slope of the net-exits series."""
    base = _b_net_exits(closed_positions, decreased_positions,
                         new_positions, increased_positions)
    return _ols_slope(base, _TD_2Y)


def iex_drv2_056_exit_breadth_4q_slope(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the exit-breadth series."""
    base = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_057_holder_qoq_pct_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the QoQ % holder change."""
    base = _b_holder_qoq_pct(inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_058_inst_pct_qoq_diff_ewm_deviation(inst_pct: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the QoQ ownership-fraction diff."""
    base = _b_inst_pct_qoq_diff(inst_pct)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_059_exit_breadth_qoq_change_zscore_4q(closed_positions: pd.Series,
                                                      decreased_positions: pd.Series,
                                                      inst_holders: pd.Series) -> pd.Series:
    """4q z-score of the QoQ change in exit breadth."""
    base = _safe_div(closed_positions + decreased_positions, inst_holders)
    chg = base - base.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def iex_drv2_060_net_exits_qoq_change_zscore_4q(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series,
                                                   new_positions: pd.Series,
                                                   increased_positions: pd.Series) -> pd.Series:
    """4q z-score of the QoQ change in net exits."""
    base = _b_net_exits(closed_positions, decreased_positions,
                         new_positions, increased_positions)
    chg = base - base.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def iex_drv2_061_holder_drawdown_4q_slope(inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the holder-count drawdown-from-peak series."""
    base = _b_holder_drawdown_from_peak(inst_holders)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_062_shares_drawdown_4q_slope(inst_shares: pd.Series) -> pd.Series:
    """4q OLS slope of the aggregate-shares drawdown-from-peak series."""
    base = _b_shares_drawdown_from_peak(inst_shares)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_063_inst_pct_drawdown_4q_slope(inst_pct: pd.Series) -> pd.Series:
    """4q OLS slope of the ownership-fraction drawdown-from-peak series."""
    base = _b_inst_pct_drawdown_from_peak(inst_pct)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_064_holder_zscore_4q_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 4q holder z-score."""
    base = _b_holder_zscore_4q(inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_065_shares_zscore_4q_ewm_deviation(inst_shares: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 4q shares z-score."""
    base = _b_shares_zscore_4q(inst_shares)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_066_inst_pct_zscore_4q_ewm_deviation(inst_pct: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 4q ownership-fraction z-score."""
    base = _b_inst_pct_zscore_4q(inst_pct)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_067_holder_qoq_diff_qoq_change_8q_mean(inst_holders: pd.Series) -> pd.Series:
    """8q rolling mean of the QoQ change in the QoQ holder-count diff."""
    acc = _b_holder_qoq_diff(inst_holders)
    chg = acc - acc.shift(_TD_QTR)
    return _rolling_mean(chg, _TD_2Y)


def iex_drv2_068_net_exits_qoq_change_8q_mean(closed_positions: pd.Series,
                                                decreased_positions: pd.Series,
                                                new_positions: pd.Series,
                                                increased_positions: pd.Series) -> pd.Series:
    """8q rolling mean of the QoQ change in net exits."""
    base = _b_net_exits(closed_positions, decreased_positions,
                         new_positions, increased_positions)
    chg = base - base.shift(_TD_QTR)
    return _rolling_mean(chg, _TD_2Y)


def iex_drv2_069_value_qoq_pct_4q_slope(inst_value: pd.Series) -> pd.Series:
    """4q OLS slope of the QoQ % aggregate-value change series."""
    base = _b_value_qoq_pct(inst_value)
    return _ols_slope(base, _TD_YEAR)


def iex_drv2_070_shares_per_holder_zscore_4q(inst_shares: pd.Series,
                                               inst_holders: pd.Series) -> pd.Series:
    """4q z-score of shares per institutional holder."""
    base = _b_shares_per_holder(inst_shares, inst_holders)
    return _zscore_rolling(base, _TD_YEAR)


def iex_drv2_071_value_per_holder_zscore_4q(inst_value: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """4q z-score of USD value per institutional holder."""
    base = _b_value_per_holder(inst_value, inst_holders)
    return _zscore_rolling(base, _TD_YEAR)


def iex_drv2_072_closed_qoq_pct_ewm_deviation(closed_positions: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of QoQ % change in fully-closed positions."""
    base = _b_closed_qoq_pct(closed_positions)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_073_decreased_qoq_pct_ewm_deviation(decreased_positions: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of QoQ % change in decreased positions."""
    base = _b_decreased_qoq_pct(decreased_positions)
    return base - _ewm_mean(base, _TD_YEAR)


def iex_drv2_074_exit_fraction_zscore_4q(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series) -> pd.Series:
    """4q z-score of exit fraction of total activity."""
    base = _b_exit_fraction_of_total(closed_positions, decreased_positions,
                                      new_positions, increased_positions)
    return _zscore_rolling(base, _TD_YEAR)


def iex_drv2_075_net_exits_ratio_ewm_deviation(closed_positions: pd.Series,
                                                 decreased_positions: pd.Series,
                                                 new_positions: pd.Series,
                                                 increased_positions: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the exit/entry ratio."""
    base = _b_net_exits_ratio(closed_positions, decreased_positions,
                               new_positions, increased_positions)
    return base - _ewm_mean(base, _TD_YEAR)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
INSTITUTIONAL_EXIT_REGISTRY_2ND_DERIVATIVES = {
    "iex_drv2_001_holder_qoq_diff_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_001_holder_qoq_diff_qoq_change},
    "iex_drv2_002_holder_qoq_pct_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_002_holder_qoq_pct_qoq_change},
    "iex_drv2_003_shares_qoq_pct_qoq_change": {"inputs": ["inst_shares"], "func": iex_drv2_003_shares_qoq_pct_qoq_change},
    "iex_drv2_004_inst_pct_qoq_diff_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv2_004_inst_pct_qoq_diff_qoq_change},
    "iex_drv2_005_net_exits_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_005_net_exits_qoq_change},
    "iex_drv2_006_net_exits_ratio_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_006_net_exits_ratio_qoq_change},
    "iex_drv2_007_exit_breadth_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv2_007_exit_breadth_qoq_change},
    "iex_drv2_008_holder_drawdown_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_008_holder_drawdown_qoq_change},
    "iex_drv2_009_inst_pct_drawdown_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv2_009_inst_pct_drawdown_qoq_change},
    "iex_drv2_010_shares_drawdown_qoq_change": {"inputs": ["inst_shares"], "func": iex_drv2_010_shares_drawdown_qoq_change},
    "iex_drv2_011_holder_qoq_diff_4q_slope": {"inputs": ["inst_holders"], "func": iex_drv2_011_holder_qoq_diff_4q_slope},
    "iex_drv2_012_shares_qoq_pct_4q_slope": {"inputs": ["inst_shares"], "func": iex_drv2_012_shares_qoq_pct_4q_slope},
    "iex_drv2_013_inst_pct_qoq_diff_4q_slope": {"inputs": ["inst_pct"], "func": iex_drv2_013_inst_pct_qoq_diff_4q_slope},
    "iex_drv2_014_net_exits_4q_slope": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_014_net_exits_4q_slope},
    "iex_drv2_015_holder_zscore_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_015_holder_zscore_qoq_change},
    "iex_drv2_016_inst_pct_zscore_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv2_016_inst_pct_zscore_qoq_change},
    "iex_drv2_017_shares_zscore_qoq_change": {"inputs": ["inst_shares"], "func": iex_drv2_017_shares_zscore_qoq_change},
    "iex_drv2_018_holder_qoq_diff_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv2_018_holder_qoq_diff_ewm_deviation},
    "iex_drv2_019_shares_qoq_pct_ewm_deviation": {"inputs": ["inst_shares"], "func": iex_drv2_019_shares_qoq_pct_ewm_deviation},
    "iex_drv2_020_net_exits_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_020_net_exits_ewm_deviation},
    "iex_drv2_021_exit_breadth_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv2_021_exit_breadth_ewm_deviation},
    "iex_drv2_022_holder_drawdown_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv2_022_holder_drawdown_ewm_deviation},
    "iex_drv2_023_holder_qoq_pct_zscore_4q": {"inputs": ["inst_holders"], "func": iex_drv2_023_holder_qoq_pct_zscore_4q},
    "iex_drv2_024_net_exits_ratio_zscore_4q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_024_net_exits_ratio_zscore_4q},
    "iex_drv2_025_inst_pct_drawdown_ewm_deviation": {"inputs": ["inst_pct"], "func": iex_drv2_025_inst_pct_drawdown_ewm_deviation},
    "iex_drv2_026_holder_qoq_diff_21d_change": {"inputs": ["inst_holders"], "func": iex_drv2_026_holder_qoq_diff_21d_change},
    "iex_drv2_027_shares_qoq_pct_21d_change": {"inputs": ["inst_shares"], "func": iex_drv2_027_shares_qoq_pct_21d_change},
    "iex_drv2_028_inst_pct_qoq_diff_21d_change": {"inputs": ["inst_pct"], "func": iex_drv2_028_inst_pct_qoq_diff_21d_change},
    "iex_drv2_029_net_exits_21d_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_029_net_exits_21d_change},
    "iex_drv2_030_value_qoq_pct_qoq_change": {"inputs": ["inst_value"], "func": iex_drv2_030_value_qoq_pct_qoq_change},
    "iex_drv2_031_value_qoq_pct_ewm_deviation": {"inputs": ["inst_value"], "func": iex_drv2_031_value_qoq_pct_ewm_deviation},
    "iex_drv2_032_value_qoq_pct_zscore_4q": {"inputs": ["inst_value"], "func": iex_drv2_032_value_qoq_pct_zscore_4q},
    "iex_drv2_033_value_zscore_4q_qoq_change": {"inputs": ["inst_value"], "func": iex_drv2_033_value_zscore_4q_qoq_change},
    "iex_drv2_034_exit_breadth_8q_mean_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv2_034_exit_breadth_8q_mean_qoq_change},
    "iex_drv2_035_net_exits_4q_mean_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_035_net_exits_4q_mean_qoq_change},
    "iex_drv2_036_shares_per_holder_qoq_change": {"inputs": ["inst_shares", "inst_holders"], "func": iex_drv2_036_shares_per_holder_qoq_change},
    "iex_drv2_037_shares_per_holder_ewm_deviation": {"inputs": ["inst_shares", "inst_holders"], "func": iex_drv2_037_shares_per_holder_ewm_deviation},
    "iex_drv2_038_value_per_holder_qoq_change": {"inputs": ["inst_value", "inst_holders"], "func": iex_drv2_038_value_per_holder_qoq_change},
    "iex_drv2_039_value_per_holder_ewm_deviation": {"inputs": ["inst_value", "inst_holders"], "func": iex_drv2_039_value_per_holder_ewm_deviation},
    "iex_drv2_040_net_exits_ratio_4q_mean_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_040_net_exits_ratio_4q_mean_qoq_change},
    "iex_drv2_041_holder_qoq_diff_norm_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_041_holder_qoq_diff_norm_qoq_change},
    "iex_drv2_042_holder_yoy_pct_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_042_holder_yoy_pct_qoq_change},
    "iex_drv2_043_inst_pct_zscore_8q_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv2_043_inst_pct_zscore_8q_qoq_change},
    "iex_drv2_044_closed_qoq_pct_qoq_change": {"inputs": ["closed_positions"], "func": iex_drv2_044_closed_qoq_pct_qoq_change},
    "iex_drv2_045_decreased_qoq_pct_qoq_change": {"inputs": ["decreased_positions"], "func": iex_drv2_045_decreased_qoq_pct_qoq_change},
    "iex_drv2_046_exit_fraction_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_046_exit_fraction_qoq_change},
    "iex_drv2_047_exit_fraction_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_047_exit_fraction_ewm_deviation},
    "iex_drv2_048_holder_decay_ewm_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_048_holder_decay_ewm_qoq_change},
    "iex_drv2_049_holder_4q_slope_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv2_049_holder_4q_slope_qoq_change},
    "iex_drv2_050_shares_4q_slope_qoq_change": {"inputs": ["inst_shares"], "func": iex_drv2_050_shares_4q_slope_qoq_change},
    "iex_drv2_051_inst_pct_4q_slope_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv2_051_inst_pct_4q_slope_qoq_change},
    "iex_drv2_052_holder_qoq_diff_8q_slope": {"inputs": ["inst_holders"], "func": iex_drv2_052_holder_qoq_diff_8q_slope},
    "iex_drv2_053_shares_qoq_pct_8q_slope": {"inputs": ["inst_shares"], "func": iex_drv2_053_shares_qoq_pct_8q_slope},
    "iex_drv2_054_inst_pct_qoq_diff_8q_slope": {"inputs": ["inst_pct"], "func": iex_drv2_054_inst_pct_qoq_diff_8q_slope},
    "iex_drv2_055_net_exits_8q_slope": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_055_net_exits_8q_slope},
    "iex_drv2_056_exit_breadth_4q_slope": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv2_056_exit_breadth_4q_slope},
    "iex_drv2_057_holder_qoq_pct_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv2_057_holder_qoq_pct_ewm_deviation},
    "iex_drv2_058_inst_pct_qoq_diff_ewm_deviation": {"inputs": ["inst_pct"], "func": iex_drv2_058_inst_pct_qoq_diff_ewm_deviation},
    "iex_drv2_059_exit_breadth_qoq_change_zscore_4q": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv2_059_exit_breadth_qoq_change_zscore_4q},
    "iex_drv2_060_net_exits_qoq_change_zscore_4q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_060_net_exits_qoq_change_zscore_4q},
    "iex_drv2_061_holder_drawdown_4q_slope": {"inputs": ["inst_holders"], "func": iex_drv2_061_holder_drawdown_4q_slope},
    "iex_drv2_062_shares_drawdown_4q_slope": {"inputs": ["inst_shares"], "func": iex_drv2_062_shares_drawdown_4q_slope},
    "iex_drv2_063_inst_pct_drawdown_4q_slope": {"inputs": ["inst_pct"], "func": iex_drv2_063_inst_pct_drawdown_4q_slope},
    "iex_drv2_064_holder_zscore_4q_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv2_064_holder_zscore_4q_ewm_deviation},
    "iex_drv2_065_shares_zscore_4q_ewm_deviation": {"inputs": ["inst_shares"], "func": iex_drv2_065_shares_zscore_4q_ewm_deviation},
    "iex_drv2_066_inst_pct_zscore_4q_ewm_deviation": {"inputs": ["inst_pct"], "func": iex_drv2_066_inst_pct_zscore_4q_ewm_deviation},
    "iex_drv2_067_holder_qoq_diff_qoq_change_8q_mean": {"inputs": ["inst_holders"], "func": iex_drv2_067_holder_qoq_diff_qoq_change_8q_mean},
    "iex_drv2_068_net_exits_qoq_change_8q_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_068_net_exits_qoq_change_8q_mean},
    "iex_drv2_069_value_qoq_pct_4q_slope": {"inputs": ["inst_value"], "func": iex_drv2_069_value_qoq_pct_4q_slope},
    "iex_drv2_070_shares_per_holder_zscore_4q": {"inputs": ["inst_shares", "inst_holders"], "func": iex_drv2_070_shares_per_holder_zscore_4q},
    "iex_drv2_071_value_per_holder_zscore_4q": {"inputs": ["inst_value", "inst_holders"], "func": iex_drv2_071_value_per_holder_zscore_4q},
    "iex_drv2_072_closed_qoq_pct_ewm_deviation": {"inputs": ["closed_positions"], "func": iex_drv2_072_closed_qoq_pct_ewm_deviation},
    "iex_drv2_073_decreased_qoq_pct_ewm_deviation": {"inputs": ["decreased_positions"], "func": iex_drv2_073_decreased_qoq_pct_ewm_deviation},
    "iex_drv2_074_exit_fraction_zscore_4q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_074_exit_fraction_zscore_4q},
    "iex_drv2_075_net_exits_ratio_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv2_075_net_exits_ratio_ewm_deviation},
}
