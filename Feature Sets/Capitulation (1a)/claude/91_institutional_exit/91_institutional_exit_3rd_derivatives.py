"""
91_institutional_exit — 3rd-Derivative Features (iex_drv3_001 – iex_drv3_075)
==============================================================================
Domain: Rate-of-change of the 2nd-derivative institutional-exit features.

These functions compute the *rate-of-change* of the 2nd-derivative series
defined in 91_institutional_exit_2nd_derivatives.py, forming third-order
dynamics (jerk/snap of exit flows, drawdown acceleration-of-acceleration, etc.).

NOTE ON SPARSITY: Because the underlying SF3 data is quarterly, all three
levels of derivatives are stepwise/sparse on a daily index.  This is
expected and correct.

This file is SELF-CONTAINED: it re-implements all required base and
2nd-derivative computations as inline helpers (prefixed _b_ and _d2_
respectively) and requires NO imports from other feature files.

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
# Inline 2nd-derivative recompute helpers (_d2_ prefix)
# ---------------------------------------------------------------------------

def _d2_holder_qoq_diff_qoq_change(inst_holders):
    base = _b_holder_qoq_diff(inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_holder_qoq_pct_qoq_change(inst_holders):
    base = _b_holder_qoq_pct(inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_shares_qoq_pct_qoq_change(inst_shares):
    base = _b_shares_qoq_pct(inst_shares)
    return base - base.shift(_TD_QTR)


def _d2_inst_pct_qoq_diff_qoq_change(inst_pct):
    base = _b_inst_pct_qoq_diff(inst_pct)
    return base - base.shift(_TD_QTR)


def _d2_net_exits_qoq_change(closed_positions, decreased_positions, new_positions, increased_positions):
    base = _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def _d2_net_exits_ratio_qoq_change(closed_positions, decreased_positions, new_positions, increased_positions):
    base = _b_net_exits_ratio(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders):
    base = _b_exit_breadth(closed_positions, decreased_positions, inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_holder_drawdown_qoq_change(inst_holders):
    base = _b_holder_drawdown_from_peak(inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_inst_pct_drawdown_qoq_change(inst_pct):
    base = _b_inst_pct_drawdown_from_peak(inst_pct)
    return base - base.shift(_TD_QTR)


def _d2_shares_drawdown_qoq_change(inst_shares):
    base = _b_shares_drawdown_from_peak(inst_shares)
    return base - base.shift(_TD_QTR)


def _d2_holder_qoq_diff_ewm_deviation(inst_holders):
    base = _b_holder_qoq_diff(inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)


def _d2_net_exits_ewm_deviation(closed_positions, decreased_positions, new_positions, increased_positions):
    base = _b_net_exits(closed_positions, decreased_positions, new_positions, increased_positions)
    return base - _ewm_mean(base, _TD_YEAR)


def _d2_exit_breadth_ewm_deviation(closed_positions, decreased_positions, inst_holders):
    base = _b_exit_breadth(closed_positions, decreased_positions, inst_holders)
    return base - _ewm_mean(base, _TD_YEAR)

# ---------------------------------------------------------------------------
# 3rd-derivative feature functions
# ---------------------------------------------------------------------------

def iex_drv3_001_holder_qoq_diff_3rd_diff(inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of holder count (jerk of holder decay)."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_002_holder_qoq_pct_3rd_diff(inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of QoQ % holder change."""
    d2 = _d2_holder_qoq_pct_qoq_change(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_003_shares_qoq_pct_3rd_diff(inst_shares: pd.Series) -> pd.Series:
    """3rd QoQ difference of QoQ % shares change."""
    d2 = _d2_shares_qoq_pct_qoq_change(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_004_inst_pct_qoq_diff_3rd_diff(inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of QoQ ownership-fraction diff."""
    d2 = _d2_inst_pct_qoq_diff_qoq_change(inst_pct)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_005_net_exits_3rd_diff(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of net exits (snap of exit flow)."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_006_net_exits_ratio_3rd_diff(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of exit/entry ratio."""
    d2 = _d2_net_exits_ratio_qoq_change(closed_positions, decreased_positions,
                                         new_positions, increased_positions)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_007_exit_breadth_3rd_diff(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_008_holder_drawdown_3rd_diff(inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of holder-count drawdown from peak."""
    d2 = _d2_holder_drawdown_qoq_change(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_009_inst_pct_drawdown_3rd_diff(inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of ownership-fraction drawdown from peak."""
    d2 = _d2_inst_pct_drawdown_qoq_change(inst_pct)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_010_shares_drawdown_3rd_diff(inst_shares: pd.Series) -> pd.Series:
    """3rd QoQ difference of shares drawdown from peak."""
    d2 = _d2_shares_drawdown_qoq_change(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_011_holder_qoq_diff_d2_slope(inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative (acceleration) of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_012_shares_qoq_pct_d2_slope(inst_shares: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of QoQ % shares change."""
    d2 = _d2_shares_qoq_pct_qoq_change(inst_shares)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_013_net_exits_d2_slope(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_014_exit_breadth_d2_slope(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_015_holder_qoq_diff_d2_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_016_net_exits_d2_ewm_deviation(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              new_positions: pd.Series,
                                              increased_positions: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_017_holder_qoq_diff_d2_zscore(inst_holders: pd.Series) -> pd.Series:
    """4q z-score of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _zscore_rolling(d2, _TD_YEAR)


def iex_drv3_018_shares_qoq_pct_d2_zscore(inst_shares: pd.Series) -> pd.Series:
    """4q z-score of the 2nd-derivative of QoQ % shares change."""
    d2 = _d2_shares_qoq_pct_qoq_change(inst_shares)
    return _zscore_rolling(d2, _TD_YEAR)


def iex_drv3_019_net_exits_d2_zscore(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """4q z-score of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return _zscore_rolling(d2, _TD_YEAR)


def iex_drv3_020_exit_breadth_d2_zscore(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """4q z-score of the 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return _zscore_rolling(d2, _TD_YEAR)


def iex_drv3_021_holder_drawdown_d2_zscore(inst_holders: pd.Series) -> pd.Series:
    """4q z-score of the 2nd-derivative of holder-count drawdown."""
    d2 = _d2_holder_drawdown_qoq_change(inst_holders)
    return _zscore_rolling(d2, _TD_YEAR)


def iex_drv3_022_holder_d2_ewm_dev_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of holder QoQ diff (3rd-order via diff of d2 deviation)."""
    d2_dev = _d2_holder_qoq_diff_ewm_deviation(inst_holders)
    return d2_dev - d2_dev.shift(_TD_QTR)


def iex_drv3_023_net_exits_d2_ewm_dev_qoq_change(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    new_positions: pd.Series,
                                                    increased_positions: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of net exits (3rd-order via diff of d2 deviation)."""
    d2_dev = _d2_net_exits_ewm_deviation(closed_positions, decreased_positions,
                                          new_positions, increased_positions)
    return d2_dev - d2_dev.shift(_TD_QTR)


def iex_drv3_024_exit_breadth_d2_ewm_dev_qoq_change(closed_positions: pd.Series,
                                                       decreased_positions: pd.Series,
                                                       inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of exit breadth (3rd-order via diff of d2 deviation)."""
    d2_dev = _d2_exit_breadth_ewm_deviation(closed_positions, decreased_positions, inst_holders)
    return d2_dev - d2_dev.shift(_TD_QTR)


def iex_drv3_025_inst_pct_qoq_diff_d2_zscore(inst_pct: pd.Series) -> pd.Series:
    """4q z-score of the 2nd-derivative of QoQ ownership-fraction diff."""
    d2 = _d2_inst_pct_qoq_diff_qoq_change(inst_pct)
    return _zscore_rolling(d2, _TD_YEAR)


# ---------------------------------------------------------------------------
# Additional inline helpers for 3rd-derivative features 026–075
# ---------------------------------------------------------------------------

def _b_value_qoq_pct(inst_value):
    return _safe_div(inst_value - inst_value.shift(_TD_QTR),
                     inst_value.shift(_TD_QTR).abs())


def _b_exit_breadth_4q_slope(closed_positions, decreased_positions, inst_holders):
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _ols_slope(breadth, _TD_YEAR)


def _b_holder_4q_slope(inst_holders):
    return _ols_slope(inst_holders, _TD_YEAR)


def _b_shares_4q_slope(inst_shares):
    return _ols_slope(inst_shares, _TD_YEAR)


def _b_inst_pct_4q_slope(inst_pct):
    return _ols_slope(inst_pct, _TD_YEAR)


def _b_exit_fraction_of_total(closed_positions, decreased_positions,
                               new_positions, increased_positions):
    exits = closed_positions + decreased_positions
    total = exits + new_positions + increased_positions
    return _safe_div(exits, total)


def _b_net_exits_ratio_4q_mean(closed_positions, decreased_positions,
                                new_positions, increased_positions):
    ratio = _safe_div(closed_positions + decreased_positions,
                      new_positions + increased_positions)
    return ratio.rolling(_TD_YEAR, min_periods=1).mean()


def _b_shares_per_holder(inst_shares, inst_holders):
    return _safe_div(inst_shares, inst_holders)


def _b_value_per_holder(inst_value, inst_holders):
    return _safe_div(inst_value, inst_holders)


def _b_holder_yoy_pct(inst_holders):
    return _safe_div(inst_holders - inst_holders.shift(_TD_YEAR),
                     inst_holders.shift(_TD_YEAR).abs())


def _b_value_zscore_4q(inst_value):
    return _zscore_rolling(inst_value, _TD_YEAR)


def _d2_value_qoq_pct_qoq_change(inst_value):
    base = _b_value_qoq_pct(inst_value)
    return base - base.shift(_TD_QTR)


def _d2_holder_4q_slope_qoq_change(inst_holders):
    base = _b_holder_4q_slope(inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_shares_4q_slope_qoq_change(inst_shares):
    base = _b_shares_4q_slope(inst_shares)
    return base - base.shift(_TD_QTR)


def _d2_inst_pct_4q_slope_qoq_change(inst_pct):
    base = _b_inst_pct_4q_slope(inst_pct)
    return base - base.shift(_TD_QTR)


def _d2_exit_fraction_qoq_change(closed_positions, decreased_positions,
                                  new_positions, increased_positions):
    base = _b_exit_fraction_of_total(closed_positions, decreased_positions,
                                      new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def _d2_net_exits_ratio_4q_mean_qoq_change(closed_positions, decreased_positions,
                                             new_positions, increased_positions):
    base = _b_net_exits_ratio_4q_mean(closed_positions, decreased_positions,
                                       new_positions, increased_positions)
    return base - base.shift(_TD_QTR)


def _d2_shares_per_holder_qoq_change(inst_shares, inst_holders):
    base = _b_shares_per_holder(inst_shares, inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_value_per_holder_qoq_change(inst_value, inst_holders):
    base = _b_value_per_holder(inst_value, inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_holder_yoy_pct_qoq_change(inst_holders):
    base = _b_holder_yoy_pct(inst_holders)
    return base - base.shift(_TD_QTR)


def _d2_holder_qoq_diff_8q_slope(inst_holders):
    base = _b_holder_qoq_diff(inst_holders)
    return _ols_slope(base, _TD_2Y)


def _d2_shares_qoq_pct_8q_slope(inst_shares):
    base = _b_shares_qoq_pct(inst_shares)
    return _ols_slope(base, _TD_2Y)


def _d2_net_exits_8q_slope(closed_positions, decreased_positions,
                            new_positions, increased_positions):
    base = _b_net_exits(closed_positions, decreased_positions,
                         new_positions, increased_positions)
    return _ols_slope(base, _TD_2Y)


def _d2_holder_drawdown_qoq_change_slope(inst_holders):
    chg = _d2_holder_drawdown_qoq_change(inst_holders)
    return _ols_slope(chg, _TD_YEAR)


def _d2_value_zscore_4q_qoq_change(inst_value):
    base = _b_value_zscore_4q(inst_value)
    return base - base.shift(_TD_QTR)


# ---------------------------------------------------------------------------
# 3rd-derivative feature functions 026–075
# ---------------------------------------------------------------------------

def iex_drv3_026_value_qoq_pct_3rd_diff(inst_value: pd.Series) -> pd.Series:
    """3rd QoQ difference of QoQ % value change (jerk of value exit)."""
    d2 = _d2_value_qoq_pct_qoq_change(inst_value)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_027_holder_4q_slope_3rd_diff(inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of the 4q OLS slope of holder count."""
    d2 = _d2_holder_4q_slope_qoq_change(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_028_shares_4q_slope_3rd_diff(inst_shares: pd.Series) -> pd.Series:
    """3rd QoQ difference of the 4q OLS slope of aggregate shares."""
    d2 = _d2_shares_4q_slope_qoq_change(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_029_inst_pct_4q_slope_3rd_diff(inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of the 4q OLS slope of institutional ownership fraction."""
    d2 = _d2_inst_pct_4q_slope_qoq_change(inst_pct)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_030_exit_fraction_3rd_diff(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of exit fraction of total activity."""
    d2 = _d2_exit_fraction_qoq_change(closed_positions, decreased_positions,
                                       new_positions, increased_positions)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_031_net_exits_ratio_4q_mean_3rd_diff(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    new_positions: pd.Series,
                                                    increased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of the 4q rolling mean of the exit/entry ratio."""
    d2 = _d2_net_exits_ratio_4q_mean_qoq_change(closed_positions, decreased_positions,
                                                  new_positions, increased_positions)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_032_shares_per_holder_3rd_diff(inst_shares: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of average shares per holder."""
    d2 = _d2_shares_per_holder_qoq_change(inst_shares, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_033_value_per_holder_3rd_diff(inst_value: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of average USD value per holder."""
    d2 = _d2_value_per_holder_qoq_change(inst_value, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_034_holder_yoy_pct_3rd_diff(inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of year-over-year % holder change."""
    d2 = _d2_holder_yoy_pct_qoq_change(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_035_value_zscore_3rd_diff(inst_value: pd.Series) -> pd.Series:
    """3rd QoQ difference of 4q z-score of aggregate institutional value."""
    d2 = _d2_value_zscore_4q_qoq_change(inst_value)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_036_holder_qoq_diff_d2_8q_slope(inst_holders: pd.Series) -> pd.Series:
    """8q OLS slope of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _ols_slope(d2, _TD_2Y)


def iex_drv3_037_shares_qoq_pct_d2_8q_slope(inst_shares: pd.Series) -> pd.Series:
    """8q OLS slope of the 2nd-derivative of QoQ % shares change."""
    d2 = _d2_shares_qoq_pct_qoq_change(inst_shares)
    return _ols_slope(d2, _TD_2Y)


def iex_drv3_038_net_exits_d2_8q_slope(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series) -> pd.Series:
    """8q OLS slope of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return _ols_slope(d2, _TD_2Y)


def iex_drv3_039_exit_breadth_d2_8q_slope(closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            inst_holders: pd.Series) -> pd.Series:
    """8q OLS slope of the 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return _ols_slope(d2, _TD_2Y)


def iex_drv3_040_holder_4q_slope_d2_slope(inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the QoQ change in 4q holder slope (3rd-order via slope-of-slope-change)."""
    d2 = _d2_holder_4q_slope_qoq_change(inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_041_net_exits_d2_ewm_deviation_qoq_change(closed_positions: pd.Series,
                                                         decreased_positions: pd.Series,
                                                         new_positions: pd.Series,
                                                         increased_positions: pd.Series) -> pd.Series:
    """QoQ change in EWM deviation of 2nd-derivative net exits."""
    d2_dev = _d2_net_exits_ewm_deviation(closed_positions, decreased_positions,
                                          new_positions, increased_positions)
    return d2_dev - d2_dev.shift(_TD_QTR)


def iex_drv3_042_holder_qoq_diff_d2_ewm_dev_zscore(inst_holders: pd.Series) -> pd.Series:
    """4q z-score of EWM deviation of 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    dev = d2 - _ewm_mean(d2, _TD_YEAR)
    return _zscore_rolling(dev, _TD_YEAR)


def iex_drv3_043_net_exits_d2_zscore_ewm_deviation(closed_positions: pd.Series,
                                                     decreased_positions: pd.Series,
                                                     new_positions: pd.Series,
                                                     increased_positions: pd.Series) -> pd.Series:
    """EWM deviation of the 4q z-score of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    zs = _zscore_rolling(d2, _TD_YEAR)
    return zs - _ewm_mean(zs, _TD_YEAR)


def iex_drv3_044_exit_breadth_d2_ewm_dev_zscore(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series,
                                                   inst_holders: pd.Series) -> pd.Series:
    """4q z-score of EWM deviation of 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    dev = d2 - _ewm_mean(d2, _TD_YEAR)
    return _zscore_rolling(dev, _TD_YEAR)


def iex_drv3_045_holder_d2_zscore_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 4q z-score of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    zs = _zscore_rolling(d2, _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def iex_drv3_046_shares_d2_zscore_qoq_change(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the 4q z-score of the 2nd-derivative of QoQ % shares change."""
    d2 = _d2_shares_qoq_pct_qoq_change(inst_shares)
    zs = _zscore_rolling(d2, _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def iex_drv3_047_net_exits_d2_zscore_qoq_change(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series,
                                                   new_positions: pd.Series,
                                                   increased_positions: pd.Series) -> pd.Series:
    """QoQ change in the 4q z-score of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    zs = _zscore_rolling(d2, _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def iex_drv3_048_inst_pct_d2_zscore_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in the 4q z-score of the 2nd-derivative of QoQ ownership diff."""
    d2 = _d2_inst_pct_qoq_diff_qoq_change(inst_pct)
    zs = _zscore_rolling(d2, _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def iex_drv3_049_holder_drawdown_d2_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of holder drawdown from peak."""
    d2 = _d2_holder_drawdown_qoq_change(inst_holders)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_050_inst_pct_drawdown_d2_ewm_deviation(inst_pct: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of ownership-fraction drawdown."""
    d2 = _d2_inst_pct_drawdown_qoq_change(inst_pct)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_051_shares_drawdown_d2_ewm_deviation(inst_shares: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of shares drawdown."""
    d2 = _d2_shares_drawdown_qoq_change(inst_shares)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_052_holder_drawdown_d2_ewm_dev_qoq_change(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM deviation of 2nd-derivative of holder drawdown."""
    d2 = _d2_holder_drawdown_qoq_change(inst_holders)
    dev = d2 - _ewm_mean(d2, _TD_YEAR)
    return dev - dev.shift(_TD_QTR)


def iex_drv3_053_shares_drawdown_d2_ewm_dev_qoq_change(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in EWM deviation of 2nd-derivative of shares drawdown."""
    d2 = _d2_shares_drawdown_qoq_change(inst_shares)
    dev = d2 - _ewm_mean(d2, _TD_YEAR)
    return dev - dev.shift(_TD_QTR)


def iex_drv3_054_inst_pct_drawdown_d2_ewm_dev_qoq_change(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in EWM deviation of 2nd-derivative of ownership-fraction drawdown."""
    d2 = _d2_inst_pct_drawdown_qoq_change(inst_pct)
    dev = d2 - _ewm_mean(d2, _TD_YEAR)
    return dev - dev.shift(_TD_QTR)


def iex_drv3_055_holder_qoq_diff_d2_4q_mean(inst_holders: pd.Series) -> pd.Series:
    """4q rolling mean of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _rolling_mean(d2, _TD_YEAR)


def iex_drv3_056_net_exits_d2_4q_mean(closed_positions: pd.Series,
                                        decreased_positions: pd.Series,
                                        new_positions: pd.Series,
                                        increased_positions: pd.Series) -> pd.Series:
    """4q rolling mean of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return _rolling_mean(d2, _TD_YEAR)


def iex_drv3_057_exit_breadth_d2_4q_mean(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """4q rolling mean of the 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return _rolling_mean(d2, _TD_YEAR)


def iex_drv3_058_holder_qoq_diff_d2_8q_mean(inst_holders: pd.Series) -> pd.Series:
    """8q rolling mean of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _rolling_mean(d2, _TD_2Y)


def iex_drv3_059_net_exits_d2_8q_mean(closed_positions: pd.Series,
                                        decreased_positions: pd.Series,
                                        new_positions: pd.Series,
                                        increased_positions: pd.Series) -> pd.Series:
    """8q rolling mean of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return _rolling_mean(d2, _TD_2Y)


def iex_drv3_060_value_qoq_pct_d2_3rd_diff(inst_value: pd.Series) -> pd.Series:
    """3rd QoQ difference of the 2nd-derivative of QoQ % value change."""
    d2 = _d2_value_qoq_pct_qoq_change(inst_value)
    return d2 - d2.shift(_TD_QTR)


def iex_drv3_061_holder_4q_slope_d2_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of 4q holder slope."""
    d2 = _d2_holder_4q_slope_qoq_change(inst_holders)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_062_shares_4q_slope_d2_ewm_deviation(inst_shares: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of 4q shares slope."""
    d2 = _d2_shares_4q_slope_qoq_change(inst_shares)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_063_inst_pct_4q_slope_d2_ewm_deviation(inst_pct: pd.Series) -> pd.Series:
    """EWM deviation (span=4q) of the 2nd-derivative of 4q ownership-fraction slope."""
    d2 = _d2_inst_pct_4q_slope_qoq_change(inst_pct)
    return d2 - _ewm_mean(d2, _TD_YEAR)


def iex_drv3_064_exit_fraction_d2_slope(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of exit fraction of total activity."""
    d2 = _d2_exit_fraction_qoq_change(closed_positions, decreased_positions,
                                       new_positions, increased_positions)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_065_shares_per_holder_d2_slope(inst_shares: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of shares per holder."""
    d2 = _d2_shares_per_holder_qoq_change(inst_shares, inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_066_value_per_holder_d2_slope(inst_value: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of value per holder."""
    d2 = _d2_value_per_holder_qoq_change(inst_value, inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_067_holder_yoy_pct_d2_slope(inst_holders: pd.Series) -> pd.Series:
    """4q OLS slope of the 2nd-derivative of YoY % holder change."""
    d2 = _d2_holder_yoy_pct_qoq_change(inst_holders)
    return _ols_slope(d2, _TD_YEAR)


def iex_drv3_068_holder_qoq_diff_d2_zscore_8q(inst_holders: pd.Series) -> pd.Series:
    """8q z-score of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _zscore_rolling(d2, _TD_2Y)


def iex_drv3_069_net_exits_d2_zscore_8q(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """8q z-score of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return _zscore_rolling(d2, _TD_2Y)


def iex_drv3_070_exit_breadth_d2_zscore_8q(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """8q z-score of the 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return _zscore_rolling(d2, _TD_2Y)


def iex_drv3_071_holder_d2_ewm_ratio(inst_holders: pd.Series) -> pd.Series:
    """Ratio of 2nd-derivative of holder QoQ diff to its EWM (span=4q)."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return _safe_div(d2, _ewm_mean(d2.abs() + _EPS, _TD_YEAR))


def iex_drv3_072_net_exits_d2_4q_sum(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """4q rolling sum of the 2nd-derivative of net exits."""
    d2 = _d2_net_exits_qoq_change(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return d2.rolling(_TD_YEAR, min_periods=1).sum()


def iex_drv3_073_holder_qoq_diff_d2_4q_sum(inst_holders: pd.Series) -> pd.Series:
    """4q rolling sum of the 2nd-derivative of holder QoQ diff."""
    d2 = _d2_holder_qoq_diff_qoq_change(inst_holders)
    return d2.rolling(_TD_YEAR, min_periods=1).sum()


def iex_drv3_074_exit_breadth_d2_4q_sum(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """4q rolling sum of the 2nd-derivative of exit breadth."""
    d2 = _d2_exit_breadth_qoq_change(closed_positions, decreased_positions, inst_holders)
    return d2.rolling(_TD_YEAR, min_periods=1).sum()


def iex_drv3_075_inst_pct_qoq_diff_d2_8q_slope(inst_pct: pd.Series) -> pd.Series:
    """8q OLS slope of the 2nd-derivative of QoQ ownership-fraction diff."""
    d2 = _d2_inst_pct_qoq_diff_qoq_change(inst_pct)
    return _ols_slope(d2, _TD_2Y)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
INSTITUTIONAL_EXIT_REGISTRY_3RD_DERIVATIVES = {
    "iex_drv3_001_holder_qoq_diff_3rd_diff": {"inputs": ["inst_holders"], "func": iex_drv3_001_holder_qoq_diff_3rd_diff},
    "iex_drv3_002_holder_qoq_pct_3rd_diff": {"inputs": ["inst_holders"], "func": iex_drv3_002_holder_qoq_pct_3rd_diff},
    "iex_drv3_003_shares_qoq_pct_3rd_diff": {"inputs": ["inst_shares"], "func": iex_drv3_003_shares_qoq_pct_3rd_diff},
    "iex_drv3_004_inst_pct_qoq_diff_3rd_diff": {"inputs": ["inst_pct"], "func": iex_drv3_004_inst_pct_qoq_diff_3rd_diff},
    "iex_drv3_005_net_exits_3rd_diff": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_005_net_exits_3rd_diff},
    "iex_drv3_006_net_exits_ratio_3rd_diff": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_006_net_exits_ratio_3rd_diff},
    "iex_drv3_007_exit_breadth_3rd_diff": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_007_exit_breadth_3rd_diff},
    "iex_drv3_008_holder_drawdown_3rd_diff": {"inputs": ["inst_holders"], "func": iex_drv3_008_holder_drawdown_3rd_diff},
    "iex_drv3_009_inst_pct_drawdown_3rd_diff": {"inputs": ["inst_pct"], "func": iex_drv3_009_inst_pct_drawdown_3rd_diff},
    "iex_drv3_010_shares_drawdown_3rd_diff": {"inputs": ["inst_shares"], "func": iex_drv3_010_shares_drawdown_3rd_diff},
    "iex_drv3_011_holder_qoq_diff_d2_slope": {"inputs": ["inst_holders"], "func": iex_drv3_011_holder_qoq_diff_d2_slope},
    "iex_drv3_012_shares_qoq_pct_d2_slope": {"inputs": ["inst_shares"], "func": iex_drv3_012_shares_qoq_pct_d2_slope},
    "iex_drv3_013_net_exits_d2_slope": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_013_net_exits_d2_slope},
    "iex_drv3_014_exit_breadth_d2_slope": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_014_exit_breadth_d2_slope},
    "iex_drv3_015_holder_qoq_diff_d2_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv3_015_holder_qoq_diff_d2_ewm_deviation},
    "iex_drv3_016_net_exits_d2_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_016_net_exits_d2_ewm_deviation},
    "iex_drv3_017_holder_qoq_diff_d2_zscore": {"inputs": ["inst_holders"], "func": iex_drv3_017_holder_qoq_diff_d2_zscore},
    "iex_drv3_018_shares_qoq_pct_d2_zscore": {"inputs": ["inst_shares"], "func": iex_drv3_018_shares_qoq_pct_d2_zscore},
    "iex_drv3_019_net_exits_d2_zscore": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_019_net_exits_d2_zscore},
    "iex_drv3_020_exit_breadth_d2_zscore": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_020_exit_breadth_d2_zscore},
    "iex_drv3_021_holder_drawdown_d2_zscore": {"inputs": ["inst_holders"], "func": iex_drv3_021_holder_drawdown_d2_zscore},
    "iex_drv3_022_holder_d2_ewm_dev_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv3_022_holder_d2_ewm_dev_qoq_change},
    "iex_drv3_023_net_exits_d2_ewm_dev_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_023_net_exits_d2_ewm_dev_qoq_change},
    "iex_drv3_024_exit_breadth_d2_ewm_dev_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_024_exit_breadth_d2_ewm_dev_qoq_change},
    "iex_drv3_025_inst_pct_qoq_diff_d2_zscore": {"inputs": ["inst_pct"], "func": iex_drv3_025_inst_pct_qoq_diff_d2_zscore},
    "iex_drv3_026_value_qoq_pct_3rd_diff": {"inputs": ["inst_value"], "func": iex_drv3_026_value_qoq_pct_3rd_diff},
    "iex_drv3_027_holder_4q_slope_3rd_diff": {"inputs": ["inst_holders"], "func": iex_drv3_027_holder_4q_slope_3rd_diff},
    "iex_drv3_028_shares_4q_slope_3rd_diff": {"inputs": ["inst_shares"], "func": iex_drv3_028_shares_4q_slope_3rd_diff},
    "iex_drv3_029_inst_pct_4q_slope_3rd_diff": {"inputs": ["inst_pct"], "func": iex_drv3_029_inst_pct_4q_slope_3rd_diff},
    "iex_drv3_030_exit_fraction_3rd_diff": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_030_exit_fraction_3rd_diff},
    "iex_drv3_031_net_exits_ratio_4q_mean_3rd_diff": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_031_net_exits_ratio_4q_mean_3rd_diff},
    "iex_drv3_032_shares_per_holder_3rd_diff": {"inputs": ["inst_shares", "inst_holders"], "func": iex_drv3_032_shares_per_holder_3rd_diff},
    "iex_drv3_033_value_per_holder_3rd_diff": {"inputs": ["inst_value", "inst_holders"], "func": iex_drv3_033_value_per_holder_3rd_diff},
    "iex_drv3_034_holder_yoy_pct_3rd_diff": {"inputs": ["inst_holders"], "func": iex_drv3_034_holder_yoy_pct_3rd_diff},
    "iex_drv3_035_value_zscore_3rd_diff": {"inputs": ["inst_value"], "func": iex_drv3_035_value_zscore_3rd_diff},
    "iex_drv3_036_holder_qoq_diff_d2_8q_slope": {"inputs": ["inst_holders"], "func": iex_drv3_036_holder_qoq_diff_d2_8q_slope},
    "iex_drv3_037_shares_qoq_pct_d2_8q_slope": {"inputs": ["inst_shares"], "func": iex_drv3_037_shares_qoq_pct_d2_8q_slope},
    "iex_drv3_038_net_exits_d2_8q_slope": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_038_net_exits_d2_8q_slope},
    "iex_drv3_039_exit_breadth_d2_8q_slope": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_039_exit_breadth_d2_8q_slope},
    "iex_drv3_040_holder_4q_slope_d2_slope": {"inputs": ["inst_holders"], "func": iex_drv3_040_holder_4q_slope_d2_slope},
    "iex_drv3_041_net_exits_d2_ewm_deviation_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_041_net_exits_d2_ewm_deviation_qoq_change},
    "iex_drv3_042_holder_qoq_diff_d2_ewm_dev_zscore": {"inputs": ["inst_holders"], "func": iex_drv3_042_holder_qoq_diff_d2_ewm_dev_zscore},
    "iex_drv3_043_net_exits_d2_zscore_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_043_net_exits_d2_zscore_ewm_deviation},
    "iex_drv3_044_exit_breadth_d2_ewm_dev_zscore": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_044_exit_breadth_d2_ewm_dev_zscore},
    "iex_drv3_045_holder_d2_zscore_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv3_045_holder_d2_zscore_qoq_change},
    "iex_drv3_046_shares_d2_zscore_qoq_change": {"inputs": ["inst_shares"], "func": iex_drv3_046_shares_d2_zscore_qoq_change},
    "iex_drv3_047_net_exits_d2_zscore_qoq_change": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_047_net_exits_d2_zscore_qoq_change},
    "iex_drv3_048_inst_pct_d2_zscore_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv3_048_inst_pct_d2_zscore_qoq_change},
    "iex_drv3_049_holder_drawdown_d2_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv3_049_holder_drawdown_d2_ewm_deviation},
    "iex_drv3_050_inst_pct_drawdown_d2_ewm_deviation": {"inputs": ["inst_pct"], "func": iex_drv3_050_inst_pct_drawdown_d2_ewm_deviation},
    "iex_drv3_051_shares_drawdown_d2_ewm_deviation": {"inputs": ["inst_shares"], "func": iex_drv3_051_shares_drawdown_d2_ewm_deviation},
    "iex_drv3_052_holder_drawdown_d2_ewm_dev_qoq_change": {"inputs": ["inst_holders"], "func": iex_drv3_052_holder_drawdown_d2_ewm_dev_qoq_change},
    "iex_drv3_053_shares_drawdown_d2_ewm_dev_qoq_change": {"inputs": ["inst_shares"], "func": iex_drv3_053_shares_drawdown_d2_ewm_dev_qoq_change},
    "iex_drv3_054_inst_pct_drawdown_d2_ewm_dev_qoq_change": {"inputs": ["inst_pct"], "func": iex_drv3_054_inst_pct_drawdown_d2_ewm_dev_qoq_change},
    "iex_drv3_055_holder_qoq_diff_d2_4q_mean": {"inputs": ["inst_holders"], "func": iex_drv3_055_holder_qoq_diff_d2_4q_mean},
    "iex_drv3_056_net_exits_d2_4q_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_056_net_exits_d2_4q_mean},
    "iex_drv3_057_exit_breadth_d2_4q_mean": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_057_exit_breadth_d2_4q_mean},
    "iex_drv3_058_holder_qoq_diff_d2_8q_mean": {"inputs": ["inst_holders"], "func": iex_drv3_058_holder_qoq_diff_d2_8q_mean},
    "iex_drv3_059_net_exits_d2_8q_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_059_net_exits_d2_8q_mean},
    "iex_drv3_060_value_qoq_pct_d2_3rd_diff": {"inputs": ["inst_value"], "func": iex_drv3_060_value_qoq_pct_d2_3rd_diff},
    "iex_drv3_061_holder_4q_slope_d2_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_drv3_061_holder_4q_slope_d2_ewm_deviation},
    "iex_drv3_062_shares_4q_slope_d2_ewm_deviation": {"inputs": ["inst_shares"], "func": iex_drv3_062_shares_4q_slope_d2_ewm_deviation},
    "iex_drv3_063_inst_pct_4q_slope_d2_ewm_deviation": {"inputs": ["inst_pct"], "func": iex_drv3_063_inst_pct_4q_slope_d2_ewm_deviation},
    "iex_drv3_064_exit_fraction_d2_slope": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_064_exit_fraction_d2_slope},
    "iex_drv3_065_shares_per_holder_d2_slope": {"inputs": ["inst_shares", "inst_holders"], "func": iex_drv3_065_shares_per_holder_d2_slope},
    "iex_drv3_066_value_per_holder_d2_slope": {"inputs": ["inst_value", "inst_holders"], "func": iex_drv3_066_value_per_holder_d2_slope},
    "iex_drv3_067_holder_yoy_pct_d2_slope": {"inputs": ["inst_holders"], "func": iex_drv3_067_holder_yoy_pct_d2_slope},
    "iex_drv3_068_holder_qoq_diff_d2_zscore_8q": {"inputs": ["inst_holders"], "func": iex_drv3_068_holder_qoq_diff_d2_zscore_8q},
    "iex_drv3_069_net_exits_d2_zscore_8q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_069_net_exits_d2_zscore_8q},
    "iex_drv3_070_exit_breadth_d2_zscore_8q": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_070_exit_breadth_d2_zscore_8q},
    "iex_drv3_071_holder_d2_ewm_ratio": {"inputs": ["inst_holders"], "func": iex_drv3_071_holder_d2_ewm_ratio},
    "iex_drv3_072_net_exits_d2_4q_sum": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_drv3_072_net_exits_d2_4q_sum},
    "iex_drv3_073_holder_qoq_diff_d2_4q_sum": {"inputs": ["inst_holders"], "func": iex_drv3_073_holder_qoq_diff_d2_4q_sum},
    "iex_drv3_074_exit_breadth_d2_4q_sum": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_drv3_074_exit_breadth_d2_4q_sum},
    "iex_drv3_075_inst_pct_qoq_diff_d2_8q_slope": {"inputs": ["inst_pct"], "func": iex_drv3_075_inst_pct_qoq_diff_d2_8q_slope},
}
