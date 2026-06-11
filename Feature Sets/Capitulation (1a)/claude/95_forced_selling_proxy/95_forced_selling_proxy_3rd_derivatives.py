"""
95_forced_selling_proxy — 3rd-Derivative Features (drv3_001 to drv3_075)
=========================================================================
Domain: Rate-of-change of the 2nd-derivative features — the third-order
dynamics of forced institutional liquidation.

These features detect the INFLECTION POINTS in the fire-sale acceleration:
is the acceleration of forced selling itself speeding up or reversing?

Quarterly -> Daily Alignment Contract
--------------------------------------
All input Series are daily-indexed pandas Series forward-filled from quarterly
SF3/13F data.  Derived Series are stepwise/sparse — expected and correct.

The computation pattern:
  base_series   = <inline recompute of base feature>
  drv2_series   = base_series - base_series.shift(63)          # 2nd deriv
  drv3_series   = drv2_series - drv2_series.shift(63)          # 3rd deriv

This file is SELF-CONTAINED — no cross-imports from other files.

Cadence: 1 qtr = 63 td, 1 yr = 252 td, 2 yr = 504 td, 3 yr = 756 td.
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
# Utility helpers (self-contained)
# ---------------------------------------------------------------------------

def _align_quarterly_to_daily(s: pd.Series) -> pd.Series:
    """Return s unchanged — caller is responsible for forward-filling."""
    return s


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / (den.replace(0, np.nan) + _EPS)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu = _rolling_mean(s, w)
    sigma = _rolling_std(s, w)
    return (s - mu) / (sigma + _EPS)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, adjust=False).mean()


# ---------------------------------------------------------------------------
# Base and 2nd-derivative inline recompute helpers (no cross-imports)
# ---------------------------------------------------------------------------

def _base_closed_breadth(closed_positions: pd.Series,
                          inst_holders: pd.Series) -> pd.Series:
    return _safe_div(closed_positions, inst_holders)


def _drv2_closed_breadth(closed_positions: pd.Series,
                          inst_holders: pd.Series) -> pd.Series:
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_combined_selling_breadth(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    return _safe_div(closed_positions + decreased_positions, inst_holders)


def _drv2_combined_selling_breadth(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_closed_zscore_4q(closed_positions: pd.Series) -> pd.Series:
    return _zscore_rolling(closed_positions, _TD_YEAR)


def _drv2_closed_zscore_4q(closed_positions: pd.Series) -> pd.Series:
    b = _base_closed_zscore_4q(closed_positions)
    return b - b.shift(_TD_QTR)


def _base_combined_selling_zscore_4q(closed_positions: pd.Series,
                                      decreased_positions: pd.Series) -> pd.Series:
    return _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR)


def _drv2_combined_selling_zscore_4q(closed_positions: pd.Series,
                                      decreased_positions: pd.Series) -> pd.Series:
    b = _base_combined_selling_zscore_4q(closed_positions, decreased_positions)
    return b - b.shift(_TD_QTR)


def _base_inst_shares_pct_qoq(inst_shares: pd.Series) -> pd.Series:
    prev = inst_shares.shift(_TD_QTR)
    return _safe_div(inst_shares - prev, prev)


def _drv2_inst_shares_pct_qoq(inst_shares: pd.Series) -> pd.Series:
    b = _base_inst_shares_pct_qoq(inst_shares)
    return b - b.shift(_TD_QTR)


def _base_avg_position_pct_qoq(avg_position: pd.Series) -> pd.Series:
    prev = avg_position.shift(_TD_QTR)
    return _safe_div(avg_position - prev, prev)


def _drv2_avg_position_pct_qoq(avg_position: pd.Series) -> pd.Series:
    b = _base_avg_position_pct_qoq(avg_position)
    return b - b.shift(_TD_QTR)


def _base_holders_pct_qoq(inst_holders: pd.Series) -> pd.Series:
    prev = inst_holders.shift(_TD_QTR)
    return _safe_div(inst_holders - prev, prev)


def _drv2_holders_pct_qoq(inst_holders: pd.Series) -> pd.Series:
    b = _base_holders_pct_qoq(inst_holders)
    return b - b.shift(_TD_QTR)


def _base_sell_buy_imbalance(closed_positions: pd.Series,
                              decreased_positions: pd.Series,
                              new_positions: pd.Series,
                              increased_positions: pd.Series) -> pd.Series:
    return _safe_div(closed_positions + decreased_positions,
                     new_positions + increased_positions + _EPS)


def _drv2_sell_buy_imbalance(closed_positions: pd.Series,
                              decreased_positions: pd.Series,
                              new_positions: pd.Series,
                              increased_positions: pd.Series) -> pd.Series:
    b = _base_sell_buy_imbalance(closed_positions, decreased_positions,
                                  new_positions, increased_positions)
    return b - b.shift(_TD_QTR)


def _base_avg_position_zscore_4q(avg_position: pd.Series) -> pd.Series:
    return _zscore_rolling(avg_position, _TD_YEAR)


def _drv2_avg_position_zscore_4q(avg_position: pd.Series) -> pd.Series:
    b = _base_avg_position_zscore_4q(avg_position)
    return b - b.shift(_TD_QTR)


def _base_holders_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_holders, _TD_YEAR)


def _drv2_holders_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    b = _base_holders_zscore_4q(inst_holders)
    return b - b.shift(_TD_QTR)


def _base_inst_shares_zscore_4q(inst_shares: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_shares, _TD_YEAR)


def _drv2_inst_shares_zscore_4q(inst_shares: pd.Series) -> pd.Series:
    b = _base_inst_shares_zscore_4q(inst_shares)
    return b - b.shift(_TD_QTR)


def _base_selling_breadth_zscore_4q(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def _drv2_selling_breadth_zscore_4q(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    b = _base_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_net_selling_flow(closed_positions: pd.Series,
                            decreased_positions: pd.Series,
                            new_positions: pd.Series,
                            increased_positions: pd.Series,
                            inst_holders: pd.Series) -> pd.Series:
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _safe_div(net, inst_holders)


def _drv2_net_selling_flow(closed_positions: pd.Series,
                            decreased_positions: pd.Series,
                            new_positions: pd.Series,
                            increased_positions: pd.Series,
                            inst_holders: pd.Series) -> pd.Series:
    b = _base_net_selling_flow(closed_positions, decreased_positions,
                                new_positions, increased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_firesale_composite(closed_positions: pd.Series,
                               decreased_positions: pd.Series,
                               inst_holders: pd.Series,
                               inst_shares: pd.Series,
                               avg_position: pd.Series) -> pd.Series:
    z1 = _zscore_rolling(closed_positions, _TD_YEAR)
    z2 = _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR)
    z3 = _zscore_rolling(inst_shares, _TD_YEAR)
    z4 = _zscore_rolling(avg_position, _TD_YEAR)
    return z1 + z2 + z3.clip(upper=0) + z4.clip(upper=0)


def _drv2_firesale_composite(closed_positions: pd.Series,
                               decreased_positions: pd.Series,
                               inst_holders: pd.Series,
                               inst_shares: pd.Series,
                               avg_position: pd.Series) -> pd.Series:
    b = _base_firesale_composite(closed_positions, decreased_positions,
                                  inst_holders, inst_shares, avg_position)
    return b - b.shift(_TD_QTR)


def _base_inst_shares_drawdown_4q(inst_shares: pd.Series) -> pd.Series:
    pk = _rolling_max(inst_shares, _TD_YEAR)
    return _safe_div(inst_shares - pk, pk)


def _drv2_inst_shares_drawdown_4q(inst_shares: pd.Series) -> pd.Series:
    b = _base_inst_shares_drawdown_4q(inst_shares)
    return b - b.shift(_TD_QTR)


def _base_holders_drawdown_4q(inst_holders: pd.Series) -> pd.Series:
    pk = _rolling_max(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders - pk, pk)


def _drv2_holders_drawdown_4q(inst_holders: pd.Series) -> pd.Series:
    b = _base_holders_drawdown_4q(inst_holders)
    return b - b.shift(_TD_QTR)


def _base_closed_ewm_spike(closed_positions: pd.Series) -> pd.Series:
    return _safe_div(closed_positions, _ewm_mean(closed_positions, _TD_YEAR))


def _drv2_closed_ewm_spike(closed_positions: pd.Series) -> pd.Series:
    b = _base_closed_ewm_spike(closed_positions)
    return b - b.shift(_TD_QTR)


def _base_inst_pct_qoq_drop(inst_pct: pd.Series) -> pd.Series:
    return inst_pct - inst_pct.shift(_TD_QTR)


def _drv2_inst_pct_qoq_drop(inst_pct: pd.Series) -> pd.Series:
    b = _base_inst_pct_qoq_drop(inst_pct)
    return b - b.shift(_TD_QTR)


def _base_closed_vs_4q_max(closed_positions: pd.Series) -> pd.Series:
    return _safe_div(closed_positions, _rolling_max(closed_positions, _TD_YEAR))


def _drv2_closed_vs_4q_max(closed_positions: pd.Series) -> pd.Series:
    b = _base_closed_vs_4q_max(closed_positions)
    return b - b.shift(_TD_QTR)


def _base_closed_breadth_ewm_deviation(closed_positions: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - _ewm_mean(b, _TD_QTR)


def _drv2_closed_breadth_ewm_deviation(closed_positions: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    b = _base_closed_breadth_ewm_deviation(closed_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_selling_breadth_ewm_accel(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    return b - _ewm_mean(b, _TD_QTR)


def _drv2_selling_breadth_ewm_accel(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    b = _base_selling_breadth_ewm_accel(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


# ===========================================================================
# 3rd-Derivative Feature Functions
# ===========================================================================

def fsp_drv3_001_closed_breadth_3rd_deriv(closed_positions: pd.Series,
                                            inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of closed/inst_holders breadth — inflection in exit acceleration."""
    d2 = _drv2_closed_breadth(closed_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_002_combined_selling_breadth_3rd_deriv(closed_positions: pd.Series,
                                                      decreased_positions: pd.Series,
                                                      inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of combined-selling breadth — inflection in breadth acceleration."""
    d2 = _drv2_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_003_closed_zscore_3rd_deriv(closed_positions: pd.Series) -> pd.Series:
    """3rd derivative of closed-positions 4Q z-score — jerk in z-score trajectory."""
    d2 = _drv2_closed_zscore_4q(closed_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_004_combined_selling_zscore_3rd_deriv(closed_positions: pd.Series,
                                                     decreased_positions: pd.Series) -> pd.Series:
    """3rd derivative of (closed+decreased) z-score."""
    d2 = _drv2_combined_selling_zscore_4q(closed_positions, decreased_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_005_inst_shares_pct_drop_3rd_deriv(inst_shares: pd.Series) -> pd.Series:
    """3rd derivative of QoQ inst_shares pct drop — jerk in share exodus rate."""
    d2 = _drv2_inst_shares_pct_qoq(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_006_avg_position_pct_collapse_3rd_deriv(avg_position: pd.Series) -> pd.Series:
    """3rd derivative of QoQ avg_position pct collapse — jerk in position shrinkage."""
    d2 = _drv2_avg_position_pct_qoq(avg_position)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_007_holders_pct_drop_3rd_deriv(inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of QoQ holder pct drop — jerk in holder departure rate."""
    d2 = _drv2_holders_pct_qoq(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_008_sell_buy_imbalance_3rd_deriv(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               new_positions: pd.Series,
                                               increased_positions: pd.Series) -> pd.Series:
    """3rd derivative of sell/buy imbalance ratio — jerk in flow imbalance."""
    d2 = _drv2_sell_buy_imbalance(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_009_avg_position_zscore_3rd_deriv(avg_position: pd.Series) -> pd.Series:
    """3rd derivative of avg_position 4Q z-score."""
    d2 = _drv2_avg_position_zscore_4q(avg_position)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_010_holders_zscore_3rd_deriv(inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of holder count 4Q z-score."""
    d2 = _drv2_holders_zscore_4q(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_011_inst_shares_zscore_3rd_deriv(inst_shares: pd.Series) -> pd.Series:
    """3rd derivative of inst_shares 4Q z-score."""
    d2 = _drv2_inst_shares_zscore_4q(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_012_selling_breadth_zscore_3rd_deriv(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of selling-breadth 4Q z-score."""
    d2 = _drv2_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_013_net_selling_flow_3rd_deriv(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             new_positions: pd.Series,
                                             increased_positions: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of normalized net selling flow."""
    d2 = _drv2_net_selling_flow(closed_positions, decreased_positions,
                                 new_positions, increased_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_014_firesale_composite_3rd_deriv(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               inst_holders: pd.Series,
                                               inst_shares: pd.Series,
                                               avg_position: pd.Series) -> pd.Series:
    """3rd derivative of the fire-sale composite score."""
    d2 = _drv2_firesale_composite(closed_positions, decreased_positions,
                                   inst_holders, inst_shares, avg_position)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_015_inst_shares_drawdown_3rd_deriv(inst_shares: pd.Series) -> pd.Series:
    """3rd derivative of inst_shares drawdown from 4Q peak."""
    d2 = _drv2_inst_shares_drawdown_4q(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_016_holders_drawdown_3rd_deriv(inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of holder-count drawdown from 4Q peak."""
    d2 = _drv2_holders_drawdown_4q(inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_017_closed_ewm_spike_3rd_deriv(closed_positions: pd.Series) -> pd.Series:
    """3rd derivative of closed-positions EWM spike ratio."""
    d2 = _drv2_closed_ewm_spike(closed_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_018_inst_pct_drop_3rd_deriv(inst_pct: pd.Series) -> pd.Series:
    """3rd derivative of QoQ inst_pct drop."""
    d2 = _drv2_inst_pct_qoq_drop(inst_pct)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_019_closed_vs_4q_max_3rd_deriv(closed_positions: pd.Series) -> pd.Series:
    """3rd derivative of closed/4Q-max spike ratio."""
    d2 = _drv2_closed_vs_4q_max(closed_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_020_closed_breadth_ewm_dev_3rd_deriv(closed_positions: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of closed-breadth EWM deviation."""
    d2 = _drv2_closed_breadth_ewm_deviation(closed_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_021_selling_breadth_ewm_accel_3rd_deriv(closed_positions: pd.Series,
                                                       decreased_positions: pd.Series,
                                                       inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of selling-breadth EWM acceleration."""
    d2 = _drv2_selling_breadth_ewm_accel(closed_positions, decreased_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_022_closed_breadth_zscore_3rd_deriv_ewm(closed_positions: pd.Series,
                                                       inst_holders: pd.Series) -> pd.Series:
    """EWM(span=63) of 3rd-derivative of closed-breadth — smoothed jerk signal."""
    d2 = _drv2_closed_breadth(closed_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_023_combined_selling_zscore_3rd_deriv_ewm(closed_positions: pd.Series,
                                                         decreased_positions: pd.Series) -> pd.Series:
    """EWM(span=63) of 3rd-derivative of combined-selling z-score — smoothed jerk."""
    d2 = _drv2_combined_selling_zscore_4q(closed_positions, decreased_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_024_inst_shares_3rd_deriv_zscore_2y(inst_shares: pd.Series) -> pd.Series:
    """Z-score of the 3rd derivative of inst_shares zscore over 2Y window."""
    d2 = _drv2_inst_shares_zscore_4q(inst_shares)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_025_selling_breadth_3rd_deriv_zscore_2y(closed_positions: pd.Series,
                                                       decreased_positions: pd.Series,
                                                       inst_holders: pd.Series) -> pd.Series:
    """Z-score of 3rd derivative of selling-breadth over 2Y window."""
    d2 = _drv2_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


# ===========================================================================
# Additional inline helpers for 3rd-derivative features 026-075
# ===========================================================================

def _base_inst_value_pct_qoq(inst_value: pd.Series) -> pd.Series:
    prev = inst_value.shift(_TD_QTR)
    return _safe_div(inst_value - prev, prev)


def _drv2_inst_value_pct_qoq(inst_value: pd.Series) -> pd.Series:
    b = _base_inst_value_pct_qoq(inst_value)
    return b - b.shift(_TD_QTR)


def _base_closed_median_spike_2q(closed_positions: pd.Series) -> pd.Series:
    med = _rolling_median(closed_positions, _TD_2Q)
    return _safe_div(closed_positions, med)


def _drv2_closed_median_spike_2q(closed_positions: pd.Series) -> pd.Series:
    b = _base_closed_median_spike_2q(closed_positions)
    return b - b.shift(_TD_QTR)


def _base_inst_pct_zscore_4q(inst_pct: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_pct, _TD_YEAR)


def _drv2_inst_pct_zscore_4q(inst_pct: pd.Series) -> pd.Series:
    b = _base_inst_pct_zscore_4q(inst_pct)
    return b - b.shift(_TD_QTR)


def _base_closed_breadth_zscore_4q(closed_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    ratio = _safe_div(closed_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def _drv2_closed_breadth_zscore_4q(closed_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    b = _base_closed_breadth_zscore_4q(closed_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_inst_value_zscore_4q(inst_value: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_value, _TD_YEAR)


def _drv2_inst_value_zscore_4q(inst_value: pd.Series) -> pd.Series:
    b = _base_inst_value_zscore_4q(inst_value)
    return b - b.shift(_TD_QTR)


def _base_decreased_pos_zscore_4q(decreased_positions: pd.Series) -> pd.Series:
    return _zscore_rolling(decreased_positions, _TD_YEAR)


def _drv2_decreased_pos_zscore_4q(decreased_positions: pd.Series) -> pd.Series:
    b = _base_decreased_pos_zscore_4q(decreased_positions)
    return b - b.shift(_TD_QTR)


def _base_selling_surplus(closed_positions: pd.Series,
                           decreased_positions: pd.Series,
                           new_positions: pd.Series,
                           increased_positions: pd.Series) -> pd.Series:
    return ((closed_positions + decreased_positions) -
            (new_positions + increased_positions)).clip(lower=0)


def _drv2_selling_surplus(closed_positions: pd.Series,
                           decreased_positions: pd.Series,
                           new_positions: pd.Series,
                           increased_positions: pd.Series) -> pd.Series:
    b = _base_selling_surplus(closed_positions, decreased_positions,
                               new_positions, increased_positions)
    return b - b.shift(_TD_QTR)


def _base_holder_turnover(closed_positions: pd.Series,
                           new_positions: pd.Series,
                           inst_holders: pd.Series) -> pd.Series:
    return _safe_div(closed_positions + new_positions, inst_holders)


def _drv2_holder_turnover(closed_positions: pd.Series,
                           new_positions: pd.Series,
                           inst_holders: pd.Series) -> pd.Series:
    b = _base_holder_turnover(closed_positions, new_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_combined_selling_ewm_spike(closed_positions: pd.Series,
                                      decreased_positions: pd.Series) -> pd.Series:
    s = closed_positions + decreased_positions
    return _safe_div(s, _ewm_mean(s, _TD_YEAR))


def _drv2_combined_selling_ewm_spike(closed_positions: pd.Series,
                                      decreased_positions: pd.Series) -> pd.Series:
    b = _base_combined_selling_ewm_spike(closed_positions, decreased_positions)
    return b - b.shift(_TD_QTR)


def _base_inst_shares_per_holder(inst_shares: pd.Series,
                                  inst_holders: pd.Series) -> pd.Series:
    return _safe_div(inst_shares, inst_holders)


def _drv2_inst_shares_per_holder(inst_shares: pd.Series,
                                  inst_holders: pd.Series) -> pd.Series:
    b = _base_inst_shares_per_holder(inst_shares, inst_holders)
    return b - b.shift(_TD_QTR)


def _base_avg_position_cliff_drop_2q(avg_position: pd.Series) -> pd.Series:
    mx = _rolling_max(avg_position, _TD_2Q)
    return _safe_div(avg_position - mx, mx)


def _drv2_avg_position_cliff_drop_2q(avg_position: pd.Series) -> pd.Series:
    b = _base_avg_position_cliff_drop_2q(avg_position)
    return b - b.shift(_TD_QTR)


def _base_inst_shares_cliff_drop_2q(inst_shares: pd.Series) -> pd.Series:
    mx = _rolling_max(inst_shares, _TD_2Q)
    return _safe_div(inst_shares - mx, mx)


def _drv2_inst_shares_cliff_drop_2q_helper(inst_shares: pd.Series) -> pd.Series:
    b = _base_inst_shares_cliff_drop_2q(inst_shares)
    return b - b.shift(_TD_QTR)


def _base_net_selling_flow(closed_positions: pd.Series,
                            decreased_positions: pd.Series,
                            new_positions: pd.Series,
                            increased_positions: pd.Series,
                            inst_holders: pd.Series) -> pd.Series:
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _safe_div(net, inst_holders)


def _drv2_net_selling_flow_h(closed_positions: pd.Series,
                               decreased_positions: pd.Series,
                               new_positions: pd.Series,
                               increased_positions: pd.Series,
                               inst_holders: pd.Series) -> pd.Series:
    b = _base_net_selling_flow(closed_positions, decreased_positions,
                                new_positions, increased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


# ===========================================================================
# 3rd-Derivative Feature Functions 026 – 075
# ===========================================================================

def fsp_drv3_026_inst_value_pct_drop_3rd_deriv(inst_value: pd.Series) -> pd.Series:
    """3rd derivative of QoQ inst_value pct drop — jerk in value erosion rate."""
    d2 = _drv2_inst_value_pct_qoq(inst_value)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_027_closed_median_spike_3rd_deriv(closed_positions: pd.Series) -> pd.Series:
    """3rd derivative of closed/2Q-median spike ratio."""
    d2 = _drv2_closed_median_spike_2q(closed_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_028_inst_pct_zscore_3rd_deriv(inst_pct: pd.Series) -> pd.Series:
    """3rd derivative of inst_pct 4Q z-score — jerk in ownership z-score trajectory."""
    d2 = _drv2_inst_pct_zscore_4q(inst_pct)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_029_closed_breadth_zscore_3rd_deriv(closed_positions: pd.Series,
                                                   inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of closed-breadth 4Q z-score."""
    d2 = _drv2_closed_breadth_zscore_4q(closed_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_030_inst_value_zscore_3rd_deriv(inst_value: pd.Series) -> pd.Series:
    """3rd derivative of inst_value 4Q z-score."""
    d2 = _drv2_inst_value_zscore_4q(inst_value)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_031_decreased_pos_zscore_3rd_deriv(decreased_positions: pd.Series) -> pd.Series:
    """3rd derivative of decreased-positions 4Q z-score."""
    d2 = _drv2_decreased_pos_zscore_4q(decreased_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_032_selling_surplus_3rd_deriv(closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            new_positions: pd.Series,
                                            increased_positions: pd.Series) -> pd.Series:
    """3rd derivative of selling surplus — jerk in excess sell pressure."""
    d2 = _drv2_selling_surplus(closed_positions, decreased_positions,
                                new_positions, increased_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_033_holder_turnover_3rd_deriv(closed_positions: pd.Series,
                                            new_positions: pd.Series,
                                            inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of holder turnover rate."""
    d2 = _drv2_holder_turnover(closed_positions, new_positions, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_034_combined_selling_ewm_spike_3rd_deriv(closed_positions: pd.Series,
                                                        decreased_positions: pd.Series) -> pd.Series:
    """3rd derivative of combined-selling EWM spike ratio."""
    d2 = _drv2_combined_selling_ewm_spike(closed_positions, decreased_positions)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_035_inst_shares_per_holder_3rd_deriv(inst_shares: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of inst_shares/inst_holders."""
    d2 = _drv2_inst_shares_per_holder(inst_shares, inst_holders)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_036_avg_position_cliff_3rd_deriv(avg_position: pd.Series) -> pd.Series:
    """3rd derivative of avg_position 2Q cliff-drop ratio."""
    d2 = _drv2_avg_position_cliff_drop_2q(avg_position)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_037_inst_shares_cliff_3rd_deriv(inst_shares: pd.Series) -> pd.Series:
    """3rd derivative of inst_shares 2Q cliff-drop ratio."""
    d2 = _drv2_inst_shares_cliff_drop_2q_helper(inst_shares)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_038_closed_breadth_3rd_deriv_ewm63(closed_positions: pd.Series,
                                                  inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of closed-breadth ratio — smoothed jerk."""
    d2 = _drv2_closed_breadth(closed_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_039_selling_breadth_3rd_deriv_ewm63(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series,
                                                   inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of combined-selling breadth."""
    d2 = _drv2_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_040_inst_pct_3rd_deriv_zscore_2y(inst_pct: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of inst_pct 4Q z-score."""
    d2 = _drv2_inst_pct_zscore_4q(inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_041_inst_value_3rd_deriv_zscore_2y(inst_value: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of inst_value 4Q z-score."""
    d2 = _drv2_inst_value_zscore_4q(inst_value)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_042_closed_breadth_zscore_3rd_deriv_zscore(closed_positions: pd.Series,
                                                          inst_holders: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of closed-breadth 4Q z-score."""
    d2 = _drv2_closed_breadth_zscore_4q(closed_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_043_holder_turnover_3rd_deriv_ewm(closed_positions: pd.Series,
                                                 new_positions: pd.Series,
                                                 inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of holder turnover rate."""
    d2 = _drv2_holder_turnover(closed_positions, new_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_044_decreased_pos_3rd_deriv_ewm(decreased_positions: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of decreased-positions 4Q z-score."""
    d2 = _drv2_decreased_pos_zscore_4q(decreased_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_045_selling_surplus_3rd_deriv_zscore(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    new_positions: pd.Series,
                                                    increased_positions: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of selling surplus."""
    d2 = _drv2_selling_surplus(closed_positions, decreased_positions,
                                new_positions, increased_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_046_inst_shares_per_holder_3rd_deriv_ewm(inst_shares: pd.Series,
                                                        inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of inst_shares/inst_holders."""
    d2 = _drv2_inst_shares_per_holder(inst_shares, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_047_net_selling_flow_3rd_deriv_2q_chg(closed_positions: pd.Series,
                                                     decreased_positions: pd.Series,
                                                     new_positions: pd.Series,
                                                     increased_positions: pd.Series,
                                                     inst_holders: pd.Series) -> pd.Series:
    """3rd derivative of net selling flow using 2Q shift instead of 1Q."""
    b = _base_net_selling_flow(closed_positions, decreased_positions,
                                new_positions, increased_positions, inst_holders)
    d2 = b - b.shift(_TD_2Q)
    return d2 - d2.shift(_TD_QTR)


def fsp_drv3_048_firesale_composite_3rd_deriv_zscore(closed_positions: pd.Series,
                                                       decreased_positions: pd.Series,
                                                       inst_holders: pd.Series,
                                                       inst_shares: pd.Series,
                                                       avg_position: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of fire-sale composite."""
    d2 = _drv2_firesale_composite(closed_positions, decreased_positions,
                                   inst_holders, inst_shares, avg_position)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_049_avg_position_zscore_3rd_deriv_ewm(avg_position: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of avg_position 4Q z-score."""
    d2 = _drv2_avg_position_zscore_4q(avg_position)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_050_holders_zscore_3rd_deriv_ewm(inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of holders 4Q z-score."""
    d2 = _drv2_holders_zscore_4q(inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_051_inst_shares_zscore_3rd_deriv_ewm(inst_shares: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of inst_shares 4Q z-score."""
    d2 = _drv2_inst_shares_zscore_4q(inst_shares)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_052_sell_buy_imbalance_3rd_deriv_zscore(closed_positions: pd.Series,
                                                       decreased_positions: pd.Series,
                                                       new_positions: pd.Series,
                                                       increased_positions: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of sell/buy imbalance."""
    d2 = _drv2_sell_buy_imbalance(closed_positions, decreased_positions,
                                   new_positions, increased_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_053_closed_zscore_3rd_deriv_zscore_2y(closed_positions: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of closed-positions 4Q z-score."""
    d2 = _drv2_closed_zscore_4q(closed_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_054_holders_drawdown_3rd_deriv_zscore(inst_holders: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of holder-count 4Q-peak drawdown."""
    d2 = _drv2_holders_drawdown_4q(inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_055_inst_shares_drawdown_3rd_deriv_zscore(inst_shares: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of inst_shares 4Q-peak drawdown."""
    d2 = _drv2_inst_shares_drawdown_4q(inst_shares)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_056_combined_selling_breadth_3rd_ewm(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """EWM(21d) of 3rd derivative of combined-selling breadth."""
    d2 = _drv2_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, 21)


def fsp_drv3_057_inst_pct_drop_3rd_deriv_ewm21(inst_pct: pd.Series) -> pd.Series:
    """EWM(21d) of 3rd derivative of QoQ inst_pct drop."""
    d2 = _drv2_inst_pct_qoq_drop(inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, 21)


def fsp_drv3_058_closed_vs_4q_max_3rd_deriv_ewm(closed_positions: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of closed/4Q-max spike ratio."""
    d2 = _drv2_closed_vs_4q_max(closed_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_059_net_flow_3rd_deriv_ewm(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) of 3rd derivative of normalized net selling flow."""
    d2 = _drv2_net_selling_flow(closed_positions, decreased_positions,
                                 new_positions, increased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def fsp_drv3_060_selling_breadth_zscore_3rd_deriv_ewm(closed_positions: pd.Series,
                                                        decreased_positions: pd.Series,
                                                        inst_holders: pd.Series) -> pd.Series:
    """EWM(21d) of 3rd derivative of selling-breadth 4Q z-score."""
    d2 = _drv2_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, 21)


def fsp_drv3_061_avg_position_pct_3rd_deriv_zscore(avg_position: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of avg_position QoQ pct collapse."""
    d2 = _drv2_avg_position_pct_qoq(avg_position)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_062_holders_pct_3rd_deriv_zscore(inst_holders: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of holder QoQ pct drop."""
    d2 = _drv2_holders_pct_qoq(inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_063_inst_shares_pct_3rd_deriv_zscore(inst_shares: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of inst_shares QoQ pct drop."""
    d2 = _drv2_inst_shares_pct_qoq(inst_shares)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_064_closed_ewm_spike_3rd_deriv_zscore(closed_positions: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of closed-positions EWM spike ratio."""
    d2 = _drv2_closed_ewm_spike(closed_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_065_selling_surplus_3rd_deriv_ewm21(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series,
                                                   new_positions: pd.Series,
                                                   increased_positions: pd.Series) -> pd.Series:
    """EWM(21d) of 3rd derivative of selling surplus."""
    d2 = _drv2_selling_surplus(closed_positions, decreased_positions,
                                new_positions, increased_positions)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, 21)


def fsp_drv3_066_firesale_composite_3rd_ewm21(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               inst_holders: pd.Series,
                                               inst_shares: pd.Series,
                                               avg_position: pd.Series) -> pd.Series:
    """EWM(21d) of 3rd derivative of fire-sale composite score."""
    d2 = _drv2_firesale_composite(closed_positions, decreased_positions,
                                   inst_holders, inst_shares, avg_position)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, 21)


def fsp_drv3_067_closed_breadth_3rd_deriv_abs(closed_positions: pd.Series,
                                               inst_holders: pd.Series) -> pd.Series:
    """Absolute value of 3rd derivative of closed-breadth — magnitude of jerk."""
    d2 = _drv2_closed_breadth(closed_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.abs()


def fsp_drv3_068_selling_breadth_3rd_deriv_abs(closed_positions: pd.Series,
                                                decreased_positions: pd.Series,
                                                inst_holders: pd.Series) -> pd.Series:
    """Absolute value of 3rd derivative of combined-selling breadth."""
    d2 = _drv2_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.abs()


def fsp_drv3_069_inst_pct_3rd_deriv_abs(inst_pct: pd.Series) -> pd.Series:
    """Absolute value of 3rd derivative of inst_pct QoQ drop — magnitude of ownership jerk."""
    d2 = _drv2_inst_pct_qoq_drop(inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.abs()


def fsp_drv3_070_inst_shares_3rd_deriv_abs(inst_shares: pd.Series) -> pd.Series:
    """Absolute value of 3rd derivative of inst_shares 4Q z-score."""
    d2 = _drv2_inst_shares_zscore_4q(inst_shares)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.abs()


def fsp_drv3_071_closed_breadth_3rd_deriv_sign(closed_positions: pd.Series,
                                                inst_holders: pd.Series) -> pd.Series:
    """Sign of 3rd derivative of closed-breadth — direction of inflection (+1/0/-1)."""
    d2 = _drv2_closed_breadth(closed_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return np.sign(d3)


def fsp_drv3_072_selling_breadth_zscore_3rd_deriv_2y_ewm(closed_positions: pd.Series,
                                                           decreased_positions: pd.Series,
                                                           inst_holders: pd.Series) -> pd.Series:
    """EWM(21d) of z-score over 2Y of 3rd derivative of selling-breadth z-score."""
    d2 = _drv2_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(_zscore_rolling(d3, _TD_2Y), 21)


def fsp_drv3_073_multi_dim_3rd_deriv_composite(closed_positions: pd.Series,
                                                 decreased_positions: pd.Series,
                                                 inst_holders: pd.Series,
                                                 inst_shares: pd.Series,
                                                 avg_position: pd.Series) -> pd.Series:
    """Sum of abs 3rd derivatives across 4 dimensions — composite jerk magnitude."""
    def _d3(b): return (b - b.shift(_TD_QTR)) - (b - b.shift(_TD_QTR)).shift(_TD_QTR)
    d3_cb  = _d3(_drv2_closed_breadth(closed_positions, inst_holders)).abs()
    d3_sel = _d3(_drv2_combined_selling_breadth(closed_positions, decreased_positions,
                                                 inst_holders)).abs()
    d3_sh  = _d3(_drv2_inst_shares_zscore_4q(inst_shares)).abs()
    d3_pos = _d3(_drv2_avg_position_zscore_4q(avg_position)).abs()
    return d3_cb + d3_sel + d3_sh + d3_pos


def fsp_drv3_074_avg_position_3rd_deriv_zscore_2y(avg_position: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of avg_position 4Q z-score."""
    d2 = _drv2_avg_position_zscore_4q(avg_position)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def fsp_drv3_075_holders_3rd_deriv_zscore_2y(inst_holders: pd.Series) -> pd.Series:
    """Z-score over 2Y of 3rd derivative of holders 4Q z-score."""
    d2 = _drv2_holders_zscore_4q(inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


# ===========================================================================
# Registry
# ===========================================================================

FORCED_SELLING_PROXY_REGISTRY_3RD_DERIVATIVES = {
    "fsp_drv3_001_closed_breadth_3rd_deriv":               {"inputs": ["closed_positions", "inst_holders"],                                                                "func": fsp_drv3_001_closed_breadth_3rd_deriv},
    "fsp_drv3_002_combined_selling_breadth_3rd_deriv":     {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv3_002_combined_selling_breadth_3rd_deriv},
    "fsp_drv3_003_closed_zscore_3rd_deriv":                {"inputs": ["closed_positions"],                                                                                "func": fsp_drv3_003_closed_zscore_3rd_deriv},
    "fsp_drv3_004_combined_selling_zscore_3rd_deriv":      {"inputs": ["closed_positions", "decreased_positions"],                                                         "func": fsp_drv3_004_combined_selling_zscore_3rd_deriv},
    "fsp_drv3_005_inst_shares_pct_drop_3rd_deriv":         {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv3_005_inst_shares_pct_drop_3rd_deriv},
    "fsp_drv3_006_avg_position_pct_collapse_3rd_deriv":    {"inputs": ["avg_position"],                                                                                    "func": fsp_drv3_006_avg_position_pct_collapse_3rd_deriv},
    "fsp_drv3_007_holders_pct_drop_3rd_deriv":             {"inputs": ["inst_holders"],                                                                                    "func": fsp_drv3_007_holders_pct_drop_3rd_deriv},
    "fsp_drv3_008_sell_buy_imbalance_3rd_deriv":           {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                  "func": fsp_drv3_008_sell_buy_imbalance_3rd_deriv},
    "fsp_drv3_009_avg_position_zscore_3rd_deriv":          {"inputs": ["avg_position"],                                                                                    "func": fsp_drv3_009_avg_position_zscore_3rd_deriv},
    "fsp_drv3_010_holders_zscore_3rd_deriv":               {"inputs": ["inst_holders"],                                                                                    "func": fsp_drv3_010_holders_zscore_3rd_deriv},
    "fsp_drv3_011_inst_shares_zscore_3rd_deriv":           {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv3_011_inst_shares_zscore_3rd_deriv},
    "fsp_drv3_012_selling_breadth_zscore_3rd_deriv":       {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv3_012_selling_breadth_zscore_3rd_deriv},
    "fsp_drv3_013_net_selling_flow_3rd_deriv":             {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],  "func": fsp_drv3_013_net_selling_flow_3rd_deriv},
    "fsp_drv3_014_firesale_composite_3rd_deriv":           {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],          "func": fsp_drv3_014_firesale_composite_3rd_deriv},
    "fsp_drv3_015_inst_shares_drawdown_3rd_deriv":         {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv3_015_inst_shares_drawdown_3rd_deriv},
    "fsp_drv3_016_holders_drawdown_3rd_deriv":             {"inputs": ["inst_holders"],                                                                                    "func": fsp_drv3_016_holders_drawdown_3rd_deriv},
    "fsp_drv3_017_closed_ewm_spike_3rd_deriv":             {"inputs": ["closed_positions"],                                                                                "func": fsp_drv3_017_closed_ewm_spike_3rd_deriv},
    "fsp_drv3_018_inst_pct_drop_3rd_deriv":                {"inputs": ["inst_pct"],                                                                                        "func": fsp_drv3_018_inst_pct_drop_3rd_deriv},
    "fsp_drv3_019_closed_vs_4q_max_3rd_deriv":             {"inputs": ["closed_positions"],                                                                                "func": fsp_drv3_019_closed_vs_4q_max_3rd_deriv},
    "fsp_drv3_020_closed_breadth_ewm_dev_3rd_deriv":       {"inputs": ["closed_positions", "inst_holders"],                                                                "func": fsp_drv3_020_closed_breadth_ewm_dev_3rd_deriv},
    "fsp_drv3_021_selling_breadth_ewm_accel_3rd_deriv":    {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv3_021_selling_breadth_ewm_accel_3rd_deriv},
    "fsp_drv3_022_closed_breadth_zscore_3rd_deriv_ewm":    {"inputs": ["closed_positions", "inst_holders"],                                                                "func": fsp_drv3_022_closed_breadth_zscore_3rd_deriv_ewm},
    "fsp_drv3_023_combined_selling_zscore_3rd_deriv_ewm":  {"inputs": ["closed_positions", "decreased_positions"],                                                         "func": fsp_drv3_023_combined_selling_zscore_3rd_deriv_ewm},
    "fsp_drv3_024_inst_shares_3rd_deriv_zscore_2y":        {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv3_024_inst_shares_3rd_deriv_zscore_2y},
    "fsp_drv3_025_selling_breadth_3rd_deriv_zscore_2y":    {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv3_025_selling_breadth_3rd_deriv_zscore_2y},
    "fsp_drv3_026_inst_value_pct_drop_3rd_deriv":          {"inputs": ["inst_value"],                                                                                     "func": fsp_drv3_026_inst_value_pct_drop_3rd_deriv},
    "fsp_drv3_027_closed_median_spike_3rd_deriv":          {"inputs": ["closed_positions"],                                                                               "func": fsp_drv3_027_closed_median_spike_3rd_deriv},
    "fsp_drv3_028_inst_pct_zscore_3rd_deriv":              {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv3_028_inst_pct_zscore_3rd_deriv},
    "fsp_drv3_029_closed_breadth_zscore_3rd_deriv":        {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv3_029_closed_breadth_zscore_3rd_deriv},
    "fsp_drv3_030_inst_value_zscore_3rd_deriv":            {"inputs": ["inst_value"],                                                                                     "func": fsp_drv3_030_inst_value_zscore_3rd_deriv},
    "fsp_drv3_031_decreased_pos_zscore_3rd_deriv":         {"inputs": ["decreased_positions"],                                                                            "func": fsp_drv3_031_decreased_pos_zscore_3rd_deriv},
    "fsp_drv3_032_selling_surplus_3rd_deriv":              {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv3_032_selling_surplus_3rd_deriv},
    "fsp_drv3_033_holder_turnover_3rd_deriv":              {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                              "func": fsp_drv3_033_holder_turnover_3rd_deriv},
    "fsp_drv3_034_combined_selling_ewm_spike_3rd_deriv":   {"inputs": ["closed_positions", "decreased_positions"],                                                        "func": fsp_drv3_034_combined_selling_ewm_spike_3rd_deriv},
    "fsp_drv3_035_inst_shares_per_holder_3rd_deriv":       {"inputs": ["inst_shares", "inst_holders"],                                                                    "func": fsp_drv3_035_inst_shares_per_holder_3rd_deriv},
    "fsp_drv3_036_avg_position_cliff_3rd_deriv":           {"inputs": ["avg_position"],                                                                                   "func": fsp_drv3_036_avg_position_cliff_3rd_deriv},
    "fsp_drv3_037_inst_shares_cliff_3rd_deriv":            {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv3_037_inst_shares_cliff_3rd_deriv},
    "fsp_drv3_038_closed_breadth_3rd_deriv_ewm63":         {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv3_038_closed_breadth_3rd_deriv_ewm63},
    "fsp_drv3_039_selling_breadth_3rd_deriv_ewm63":        {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv3_039_selling_breadth_3rd_deriv_ewm63},
    "fsp_drv3_040_inst_pct_3rd_deriv_zscore_2y":           {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv3_040_inst_pct_3rd_deriv_zscore_2y},
    "fsp_drv3_041_inst_value_3rd_deriv_zscore_2y":         {"inputs": ["inst_value"],                                                                                     "func": fsp_drv3_041_inst_value_3rd_deriv_zscore_2y},
    "fsp_drv3_042_closed_breadth_zscore_3rd_deriv_zscore": {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv3_042_closed_breadth_zscore_3rd_deriv_zscore},
    "fsp_drv3_043_holder_turnover_3rd_deriv_ewm":          {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                              "func": fsp_drv3_043_holder_turnover_3rd_deriv_ewm},
    "fsp_drv3_044_decreased_pos_3rd_deriv_ewm":            {"inputs": ["decreased_positions"],                                                                            "func": fsp_drv3_044_decreased_pos_3rd_deriv_ewm},
    "fsp_drv3_045_selling_surplus_3rd_deriv_zscore":       {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv3_045_selling_surplus_3rd_deriv_zscore},
    "fsp_drv3_046_inst_shares_per_holder_3rd_deriv_ewm":   {"inputs": ["inst_shares", "inst_holders"],                                                                    "func": fsp_drv3_046_inst_shares_per_holder_3rd_deriv_ewm},
    "fsp_drv3_047_net_selling_flow_3rd_deriv_2q_chg":      {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],"func": fsp_drv3_047_net_selling_flow_3rd_deriv_2q_chg},
    "fsp_drv3_048_firesale_composite_3rd_deriv_zscore":    {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],         "func": fsp_drv3_048_firesale_composite_3rd_deriv_zscore},
    "fsp_drv3_049_avg_position_zscore_3rd_deriv_ewm":      {"inputs": ["avg_position"],                                                                                   "func": fsp_drv3_049_avg_position_zscore_3rd_deriv_ewm},
    "fsp_drv3_050_holders_zscore_3rd_deriv_ewm":           {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv3_050_holders_zscore_3rd_deriv_ewm},
    "fsp_drv3_051_inst_shares_zscore_3rd_deriv_ewm":       {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv3_051_inst_shares_zscore_3rd_deriv_ewm},
    "fsp_drv3_052_sell_buy_imbalance_3rd_deriv_zscore":    {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv3_052_sell_buy_imbalance_3rd_deriv_zscore},
    "fsp_drv3_053_closed_zscore_3rd_deriv_zscore_2y":      {"inputs": ["closed_positions"],                                                                               "func": fsp_drv3_053_closed_zscore_3rd_deriv_zscore_2y},
    "fsp_drv3_054_holders_drawdown_3rd_deriv_zscore":      {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv3_054_holders_drawdown_3rd_deriv_zscore},
    "fsp_drv3_055_inst_shares_drawdown_3rd_deriv_zscore":  {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv3_055_inst_shares_drawdown_3rd_deriv_zscore},
    "fsp_drv3_056_combined_selling_breadth_3rd_ewm":       {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv3_056_combined_selling_breadth_3rd_ewm},
    "fsp_drv3_057_inst_pct_drop_3rd_deriv_ewm21":          {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv3_057_inst_pct_drop_3rd_deriv_ewm21},
    "fsp_drv3_058_closed_vs_4q_max_3rd_deriv_ewm":         {"inputs": ["closed_positions"],                                                                               "func": fsp_drv3_058_closed_vs_4q_max_3rd_deriv_ewm},
    "fsp_drv3_059_net_flow_3rd_deriv_ewm":                 {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],"func": fsp_drv3_059_net_flow_3rd_deriv_ewm},
    "fsp_drv3_060_selling_breadth_zscore_3rd_deriv_ewm":   {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv3_060_selling_breadth_zscore_3rd_deriv_ewm},
    "fsp_drv3_061_avg_position_pct_3rd_deriv_zscore":      {"inputs": ["avg_position"],                                                                                   "func": fsp_drv3_061_avg_position_pct_3rd_deriv_zscore},
    "fsp_drv3_062_holders_pct_3rd_deriv_zscore":           {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv3_062_holders_pct_3rd_deriv_zscore},
    "fsp_drv3_063_inst_shares_pct_3rd_deriv_zscore":       {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv3_063_inst_shares_pct_3rd_deriv_zscore},
    "fsp_drv3_064_closed_ewm_spike_3rd_deriv_zscore":      {"inputs": ["closed_positions"],                                                                               "func": fsp_drv3_064_closed_ewm_spike_3rd_deriv_zscore},
    "fsp_drv3_065_selling_surplus_3rd_deriv_ewm21":        {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv3_065_selling_surplus_3rd_deriv_ewm21},
    "fsp_drv3_066_firesale_composite_3rd_ewm21":           {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],         "func": fsp_drv3_066_firesale_composite_3rd_ewm21},
    "fsp_drv3_067_closed_breadth_3rd_deriv_abs":           {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv3_067_closed_breadth_3rd_deriv_abs},
    "fsp_drv3_068_selling_breadth_3rd_deriv_abs":          {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv3_068_selling_breadth_3rd_deriv_abs},
    "fsp_drv3_069_inst_pct_3rd_deriv_abs":                 {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv3_069_inst_pct_3rd_deriv_abs},
    "fsp_drv3_070_inst_shares_3rd_deriv_abs":              {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv3_070_inst_shares_3rd_deriv_abs},
    "fsp_drv3_071_closed_breadth_3rd_deriv_sign":          {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv3_071_closed_breadth_3rd_deriv_sign},
    "fsp_drv3_072_selling_breadth_zscore_3rd_deriv_2y_ewm":{"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv3_072_selling_breadth_zscore_3rd_deriv_2y_ewm},
    "fsp_drv3_073_multi_dim_3rd_deriv_composite":          {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],         "func": fsp_drv3_073_multi_dim_3rd_deriv_composite},
    "fsp_drv3_074_avg_position_3rd_deriv_zscore_2y":       {"inputs": ["avg_position"],                                                                                   "func": fsp_drv3_074_avg_position_3rd_deriv_zscore_2y},
    "fsp_drv3_075_holders_3rd_deriv_zscore_2y":            {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv3_075_holders_3rd_deriv_zscore_2y},
}
