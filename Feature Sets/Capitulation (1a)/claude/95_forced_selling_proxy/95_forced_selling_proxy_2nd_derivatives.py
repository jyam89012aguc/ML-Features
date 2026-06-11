"""
95_forced_selling_proxy — 2nd-Derivative Features (drv2_001 to drv2_075)
=========================================================================
Domain: Rate-of-change of the forced-selling base features.

These derivatives characterize how QUICKLY the forced-liquidation signals are
accelerating or decelerating — the second-order dynamics of the fire-sale.

Quarterly -> Daily Alignment Contract
--------------------------------------
All input Series are daily-indexed pandas Series forward-filled from quarterly
SF3/13F data.  Because underlying data updates ~once per 63 trading days,
derived Series are stepwise/sparse on a daily index — this is expected.

The derivative computation pattern:
  base_series = <inline recompute of base feature>
  deriv = base_series - base_series.shift(63)   # QoQ first difference

This file is SELF-CONTAINED — no cross-imports from base files.

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
# Base-feature recompute helpers (inline, no cross-imports)
# ---------------------------------------------------------------------------

def _base_closed_breadth(closed_positions: pd.Series,
                          inst_holders: pd.Series) -> pd.Series:
    return _safe_div(closed_positions, inst_holders)


def _base_combined_selling_breadth(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    return _safe_div(closed_positions + decreased_positions, inst_holders)


def _base_closed_zscore_4q(closed_positions: pd.Series) -> pd.Series:
    return _zscore_rolling(closed_positions, _TD_YEAR)


def _base_combined_selling_zscore_4q(closed_positions: pd.Series,
                                      decreased_positions: pd.Series) -> pd.Series:
    return _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR)


def _base_inst_shares_pct_drop_qoq(inst_shares: pd.Series) -> pd.Series:
    prev = inst_shares.shift(_TD_QTR)
    return _safe_div(inst_shares - prev, prev)


def _base_avg_position_pct_collapse_qoq(avg_position: pd.Series) -> pd.Series:
    prev = avg_position.shift(_TD_QTR)
    return _safe_div(avg_position - prev, prev)


def _base_holders_pct_drop_qoq(inst_holders: pd.Series) -> pd.Series:
    prev = inst_holders.shift(_TD_QTR)
    return _safe_div(inst_holders - prev, prev)


def _base_sell_buy_imbalance(closed_positions: pd.Series,
                              decreased_positions: pd.Series,
                              new_positions: pd.Series,
                              increased_positions: pd.Series) -> pd.Series:
    return _safe_div(closed_positions + decreased_positions,
                     new_positions + increased_positions + _EPS)


def _base_avg_position_zscore_4q(avg_position: pd.Series) -> pd.Series:
    return _zscore_rolling(avg_position, _TD_YEAR)


def _base_inst_pct_qoq_drop(inst_pct: pd.Series) -> pd.Series:
    return inst_pct - inst_pct.shift(_TD_QTR)


def _base_closed_vs_4q_max_ratio(closed_positions: pd.Series) -> pd.Series:
    return _safe_div(closed_positions, _rolling_max(closed_positions, _TD_YEAR))


def _base_holders_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_holders, _TD_YEAR)


def _base_inst_shares_zscore_4q(inst_shares: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_shares, _TD_YEAR)


def _base_selling_breadth_zscore_4q(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def _base_net_selling_flow(closed_positions: pd.Series,
                            decreased_positions: pd.Series,
                            new_positions: pd.Series,
                            increased_positions: pd.Series,
                            inst_holders: pd.Series) -> pd.Series:
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _safe_div(net, inst_holders)


def _base_liquidation_synchrony(closed_positions: pd.Series,
                                  inst_holders: pd.Series,
                                  avg_position: pd.Series) -> pd.Series:
    breadth = _safe_div(closed_positions, inst_holders)
    z_pos = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    return breadth * z_pos


def _base_closed_ewm_spike(closed_positions: pd.Series) -> pd.Series:
    return _safe_div(closed_positions, _ewm_mean(closed_positions, _TD_YEAR))


def _base_avg_position_cliff_drop_2q(avg_position: pd.Series) -> pd.Series:
    mx = _rolling_max(avg_position, _TD_2Q)
    return _safe_div(avg_position - mx, mx)


def _base_inst_shares_cliff_drop_2q(inst_shares: pd.Series) -> pd.Series:
    mx = _rolling_max(inst_shares, _TD_2Q)
    return _safe_div(inst_shares - mx, mx)


def _base_closed_pos_median_spike_4q(closed_positions: pd.Series) -> pd.Series:
    med = _rolling_median(closed_positions, _TD_YEAR)
    return _safe_div(closed_positions, med)


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


def _base_inst_shares_drawdown_4q(inst_shares: pd.Series) -> pd.Series:
    pk = _rolling_max(inst_shares, _TD_YEAR)
    return _safe_div(inst_shares - pk, pk)


def _base_holders_drawdown_4q(inst_holders: pd.Series) -> pd.Series:
    pk = _rolling_max(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders - pk, pk)


# ===========================================================================
# 2nd-Derivative Feature Functions
# ===========================================================================

def fsp_drv2_001_closed_breadth_qoq_chg(closed_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """QoQ change in closed/inst_holders breadth ratio."""
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_002_combined_selling_breadth_qoq_chg(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """QoQ change in (closed+decreased)/inst_holders breadth ratio."""
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_003_closed_zscore_4q_qoq_chg(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed-positions 4Q z-score — is the spike accelerating?"""
    b = _base_closed_zscore_4q(closed_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_004_combined_selling_zscore_qoq_chg(closed_positions: pd.Series,
                                                   decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in (closed+decreased) 4Q z-score."""
    b = _base_combined_selling_zscore_4q(closed_positions, decreased_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_005_inst_shares_pct_drop_qoq_chg(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in QoQ-pct-drop of inst_shares — second derivative of share exodus."""
    b = _base_inst_shares_pct_drop_qoq(inst_shares)
    return b - b.shift(_TD_QTR)


def fsp_drv2_006_avg_position_pct_collapse_qoq_chg(avg_position: pd.Series) -> pd.Series:
    """QoQ change in QoQ-pct-collapse of avg_position — acceleration of shrinkage."""
    b = _base_avg_position_pct_collapse_qoq(avg_position)
    return b - b.shift(_TD_QTR)


def fsp_drv2_007_holders_pct_drop_qoq_chg(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in QoQ-pct-drop of holder count."""
    b = _base_holders_pct_drop_qoq(inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_008_sell_buy_imbalance_qoq_chg(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              new_positions: pd.Series,
                                              increased_positions: pd.Series) -> pd.Series:
    """QoQ change in sell/buy imbalance ratio — is the imbalance worsening?"""
    b = _base_sell_buy_imbalance(closed_positions, decreased_positions,
                                  new_positions, increased_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_009_avg_position_zscore_qoq_chg(avg_position: pd.Series) -> pd.Series:
    """QoQ change in avg_position 4Q z-score."""
    b = _base_avg_position_zscore_4q(avg_position)
    return b - b.shift(_TD_QTR)


def fsp_drv2_010_inst_pct_drop_qoq_chg(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in QoQ ownership-pct drop — second derivative of ownership loss."""
    b = _base_inst_pct_qoq_drop(inst_pct)
    return b - b.shift(_TD_QTR)


def fsp_drv2_011_closed_vs_4q_max_qoq_chg(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed/4Q-max spike ratio."""
    b = _base_closed_vs_4q_max_ratio(closed_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_012_holders_zscore_qoq_chg(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in holder count 4Q z-score."""
    b = _base_holders_zscore_4q(inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_013_inst_shares_zscore_qoq_chg(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in inst_shares 4Q z-score."""
    b = _base_inst_shares_zscore_4q(inst_shares)
    return b - b.shift(_TD_QTR)


def fsp_drv2_014_selling_breadth_zscore_qoq_chg(closed_positions: pd.Series,
                                                  decreased_positions: pd.Series,
                                                  inst_holders: pd.Series) -> pd.Series:
    """QoQ change in selling-breadth 4Q z-score."""
    b = _base_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_015_net_selling_flow_qoq_chg(closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            new_positions: pd.Series,
                                            increased_positions: pd.Series,
                                            inst_holders: pd.Series) -> pd.Series:
    """QoQ change in normalized net selling flow."""
    b = _base_net_selling_flow(closed_positions, decreased_positions,
                                new_positions, increased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_016_liquidation_synchrony_qoq_chg(closed_positions: pd.Series,
                                                 inst_holders: pd.Series,
                                                 avg_position: pd.Series) -> pd.Series:
    """QoQ change in liquidation synchrony score."""
    b = _base_liquidation_synchrony(closed_positions, inst_holders, avg_position)
    return b - b.shift(_TD_QTR)


def fsp_drv2_017_closed_ewm_spike_qoq_chg(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed-positions EWM spike ratio."""
    b = _base_closed_ewm_spike(closed_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_018_avg_position_cliff_drop_qoq_chg(avg_position: pd.Series) -> pd.Series:
    """QoQ change in avg_position 2Q cliff-drop ratio."""
    b = _base_avg_position_cliff_drop_2q(avg_position)
    return b - b.shift(_TD_QTR)


def fsp_drv2_019_inst_shares_cliff_drop_qoq_chg(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in inst_shares 2Q cliff-drop ratio."""
    b = _base_inst_shares_cliff_drop_2q(inst_shares)
    return b - b.shift(_TD_QTR)


def fsp_drv2_020_closed_median_spike_qoq_chg(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed/4Q-median spike ratio."""
    b = _base_closed_pos_median_spike_4q(closed_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_021_firesale_composite_qoq_chg(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              inst_holders: pd.Series,
                                              inst_shares: pd.Series,
                                              avg_position: pd.Series) -> pd.Series:
    """QoQ change in the fire-sale composite score."""
    b = _base_firesale_composite(closed_positions, decreased_positions,
                                  inst_holders, inst_shares, avg_position)
    return b - b.shift(_TD_QTR)


def fsp_drv2_022_inst_shares_drawdown_qoq_chg(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in inst_shares drawdown from 4Q peak — worsening drawdown speed."""
    b = _base_inst_shares_drawdown_4q(inst_shares)
    return b - b.shift(_TD_QTR)


def fsp_drv2_023_holders_drawdown_qoq_chg(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in holder-count drawdown from 4Q peak."""
    b = _base_holders_drawdown_4q(inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_024_closed_breadth_ewm_slope(closed_positions: pd.Series,
                                            inst_holders: pd.Series) -> pd.Series:
    """EWM(span=63) slope of the closed/holders breadth ratio — smoothed 1st derivative."""
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_025_selling_breadth_ewm_acceleration(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """EWM deviation of selling breadth from its own EWM — acceleration above trend."""
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    ewm_b = _ewm_mean(b, _TD_QTR)
    return b - ewm_b


# ===========================================================================
# 2nd-Derivative Feature Functions 026 – 075
# ===========================================================================

# --- additional base helpers for new features ---

def _base_inst_value_pct_drop_qoq(inst_value: pd.Series) -> pd.Series:
    prev = inst_value.shift(_TD_QTR)
    return _safe_div(inst_value - prev, prev)


def _base_closed_median_spike_2q(closed_positions: pd.Series) -> pd.Series:
    med = _rolling_median(closed_positions, _TD_2Q)
    return _safe_div(closed_positions, med)


def _base_inst_pct_zscore_4q(inst_pct: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_pct, _TD_YEAR)


def _base_closed_breadth_zscore_4q(closed_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    ratio = _safe_div(closed_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def _base_inst_value_zscore_4q(inst_value: pd.Series) -> pd.Series:
    return _zscore_rolling(inst_value, _TD_YEAR)


def _base_decreased_pos_zscore_4q(decreased_positions: pd.Series) -> pd.Series:
    return _zscore_rolling(decreased_positions, _TD_YEAR)


def _base_selling_surplus(closed_positions: pd.Series,
                           decreased_positions: pd.Series,
                           new_positions: pd.Series,
                           increased_positions: pd.Series) -> pd.Series:
    return ((closed_positions + decreased_positions) -
            (new_positions + increased_positions)).clip(lower=0)


def _base_holder_turnover(closed_positions: pd.Series,
                           new_positions: pd.Series,
                           inst_holders: pd.Series) -> pd.Series:
    return _safe_div(closed_positions + new_positions, inst_holders)


def _base_combined_selling_ewm_spike(closed_positions: pd.Series,
                                      decreased_positions: pd.Series) -> pd.Series:
    s = closed_positions + decreased_positions
    return _safe_div(s, _ewm_mean(s, _TD_YEAR))


def _base_inst_shares_per_holder(inst_shares: pd.Series,
                                  inst_holders: pd.Series) -> pd.Series:
    return _safe_div(inst_shares, inst_holders)


def _base_liquidation_synchrony(closed_positions: pd.Series,
                                  inst_holders: pd.Series,
                                  avg_position: pd.Series) -> pd.Series:
    breadth = _safe_div(closed_positions, inst_holders)
    z_pos = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    return breadth * z_pos


def _base_net_selling_flow_zscore_4q(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    net = _safe_div((closed_positions + decreased_positions) -
                    (new_positions + increased_positions), inst_holders)
    return _zscore_rolling(net, _TD_YEAR)


def fsp_drv2_026_inst_value_pct_drop_qoq_chg(inst_value: pd.Series) -> pd.Series:
    """QoQ change in QoQ-pct-drop of inst_value — acceleration of value erosion."""
    b = _base_inst_value_pct_drop_qoq(inst_value)
    return b - b.shift(_TD_QTR)


def fsp_drv2_027_closed_pos_median_spike_2q_chg(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed/2Q-median spike ratio."""
    b = _base_closed_median_spike_2q(closed_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_028_inst_pct_qoq_drop_21d_slope(inst_pct: pd.Series) -> pd.Series:
    """EWM(21d) slope of QoQ inst_pct drop — smoothed acceleration of ownership loss."""
    b = _base_inst_pct_qoq_drop(inst_pct)
    return b - _ewm_mean(b, 21)


def fsp_drv2_029_closed_breadth_21d_slope(closed_positions: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """EWM(21d) deviation of closed-breadth — very short-term acceleration."""
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - _ewm_mean(b, 21)


def fsp_drv2_030_combined_selling_breadth_21d_slope(closed_positions: pd.Series,
                                                      decreased_positions: pd.Series,
                                                      inst_holders: pd.Series) -> pd.Series:
    """EWM(21d) deviation of combined-selling breadth."""
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    return b - _ewm_mean(b, 21)


def fsp_drv2_031_inst_shares_zscore_2q_chg(inst_shares: pd.Series) -> pd.Series:
    """2Q change in inst_shares 4Q z-score — half-year shift in z-score level."""
    b = _base_inst_shares_zscore_4q(inst_shares)
    return b - b.shift(_TD_2Q)


def fsp_drv2_032_avg_position_zscore_2q_chg(avg_position: pd.Series) -> pd.Series:
    """2Q change in avg_position 4Q z-score."""
    b = _base_avg_position_zscore_4q(avg_position)
    return b - b.shift(_TD_2Q)


def fsp_drv2_033_holders_zscore_2q_chg(inst_holders: pd.Series) -> pd.Series:
    """2Q change in holders 4Q z-score."""
    b = _base_holders_zscore_4q(inst_holders)
    return b - b.shift(_TD_2Q)


def fsp_drv2_034_sell_buy_imbalance_2q_chg(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             new_positions: pd.Series,
                                             increased_positions: pd.Series) -> pd.Series:
    """2Q change in sell/buy imbalance ratio."""
    b = _base_sell_buy_imbalance(closed_positions, decreased_positions,
                                  new_positions, increased_positions)
    return b - b.shift(_TD_2Q)


def fsp_drv2_035_closed_zscore_2q_chg(closed_positions: pd.Series) -> pd.Series:
    """2Q change in closed-positions 4Q z-score."""
    b = _base_closed_zscore_4q(closed_positions)
    return b - b.shift(_TD_2Q)


def fsp_drv2_036_net_selling_flow_2q_chg(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """2Q change in normalized net selling flow."""
    b = _base_net_selling_flow(closed_positions, decreased_positions,
                                new_positions, increased_positions, inst_holders)
    return b - b.shift(_TD_2Q)


def fsp_drv2_037_inst_shares_drawdown_2q_chg(inst_shares: pd.Series) -> pd.Series:
    """2Q change in inst_shares 4Q-peak drawdown."""
    b = _base_inst_shares_drawdown_4q(inst_shares)
    return b - b.shift(_TD_2Q)


def fsp_drv2_038_holders_drawdown_2q_chg(inst_holders: pd.Series) -> pd.Series:
    """2Q change in holder-count 4Q-peak drawdown."""
    b = _base_holders_drawdown_4q(inst_holders)
    return b - b.shift(_TD_2Q)


def fsp_drv2_039_firesale_composite_2q_chg(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             inst_holders: pd.Series,
                                             inst_shares: pd.Series,
                                             avg_position: pd.Series) -> pd.Series:
    """2Q change in fire-sale composite score."""
    b = _base_firesale_composite(closed_positions, decreased_positions,
                                  inst_holders, inst_shares, avg_position)
    return b - b.shift(_TD_2Q)


def fsp_drv2_040_closed_breadth_zscore_qoq_chg(closed_positions: pd.Series,
                                                 inst_holders: pd.Series) -> pd.Series:
    """QoQ change in closed-breadth 4Q z-score."""
    b = _base_closed_breadth_zscore_4q(closed_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_041_inst_pct_zscore_qoq_chg(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in inst_pct 4Q z-score."""
    b = _base_inst_pct_zscore_4q(inst_pct)
    return b - b.shift(_TD_QTR)


def fsp_drv2_042_inst_value_zscore_qoq_chg(inst_value: pd.Series) -> pd.Series:
    """QoQ change in inst_value 4Q z-score."""
    b = _base_inst_value_zscore_4q(inst_value)
    return b - b.shift(_TD_QTR)


def fsp_drv2_043_decreased_pos_zscore_qoq_chg(decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in decreased-positions 4Q z-score."""
    b = _base_decreased_pos_zscore_4q(decreased_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_044_selling_surplus_qoq_chg(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series) -> pd.Series:
    """QoQ change in selling surplus (clipped at 0)."""
    b = _base_selling_surplus(closed_positions, decreased_positions,
                               new_positions, increased_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_045_holder_turnover_qoq_chg(closed_positions: pd.Series,
                                           new_positions: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """QoQ change in holder turnover rate."""
    b = _base_holder_turnover(closed_positions, new_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_046_closed_ewm_spike_2q_chg(closed_positions: pd.Series) -> pd.Series:
    """2Q change in closed-positions EWM spike ratio."""
    b = _base_closed_ewm_spike(closed_positions)
    return b - b.shift(_TD_2Q)


def fsp_drv2_047_combined_selling_ewm_spike_qoq_chg(closed_positions: pd.Series,
                                                      decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in combined-selling EWM spike ratio."""
    b = _base_combined_selling_ewm_spike(closed_positions, decreased_positions)
    return b - b.shift(_TD_QTR)


def fsp_drv2_048_inst_shares_per_holder_qoq_chg(inst_shares: pd.Series,
                                                  inst_holders: pd.Series) -> pd.Series:
    """QoQ change in inst_shares/inst_holders — position-size rate of change."""
    b = _base_inst_shares_per_holder(inst_shares, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_049_selling_breadth_zscore_2q_chg(closed_positions: pd.Series,
                                                 decreased_positions: pd.Series,
                                                 inst_holders: pd.Series) -> pd.Series:
    """2Q change in selling-breadth 4Q z-score."""
    b = _base_selling_breadth_zscore_4q(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(_TD_2Q)


def fsp_drv2_050_liquidation_synchrony_2q_chg(closed_positions: pd.Series,
                                               inst_holders: pd.Series,
                                               avg_position: pd.Series) -> pd.Series:
    """2Q change in liquidation synchrony score."""
    b = _base_liquidation_synchrony(closed_positions, inst_holders, avg_position)
    return b - b.shift(_TD_2Q)


def fsp_drv2_051_closed_breadth_ewm_slope_5d(closed_positions: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """EWM(5d) deviation of closed-breadth — intra-week acceleration signal."""
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - _ewm_mean(b, 5)


def fsp_drv2_052_inst_shares_pct_drop_ewm_slope(inst_shares: pd.Series) -> pd.Series:
    """EWM(63d) deviation of inst_shares QoQ pct drop — smoothed exodus acceleration."""
    b = _base_inst_shares_pct_drop_qoq(inst_shares)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_053_avg_position_pct_drop_ewm_slope(avg_position: pd.Series) -> pd.Series:
    """EWM(63d) deviation of avg_position QoQ pct collapse."""
    b = _base_avg_position_pct_collapse_qoq(avg_position)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_054_holders_pct_drop_ewm_slope(inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) deviation of holder QoQ pct drop."""
    b = _base_holders_pct_drop_qoq(inst_holders)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_055_closed_pos_zscore_qoq_zscore_4q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of the QoQ change in closed-positions 4Q z-score over 4Q window."""
    b = _base_closed_zscore_4q(closed_positions)
    chg = b - b.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def fsp_drv2_056_sell_buy_imbalance_ewm_slope(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               new_positions: pd.Series,
                                               increased_positions: pd.Series) -> pd.Series:
    """EWM(63d) deviation of sell/buy imbalance ratio."""
    b = _base_sell_buy_imbalance(closed_positions, decreased_positions,
                                  new_positions, increased_positions)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_057_inst_pct_qoq_ewm_slope(inst_pct: pd.Series) -> pd.Series:
    """EWM(63d) deviation of QoQ inst_pct drop — smoothed ownership loss acceleration."""
    b = _base_inst_pct_qoq_drop(inst_pct)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_058_firesale_composite_ewm_slope(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               inst_holders: pd.Series,
                                               inst_shares: pd.Series,
                                               avg_position: pd.Series) -> pd.Series:
    """EWM(63d) deviation of firesale composite score."""
    b = _base_firesale_composite(closed_positions, decreased_positions,
                                  inst_holders, inst_shares, avg_position)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_059_net_flow_zscore_qoq_chg(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """QoQ change in net selling flow 4Q z-score."""
    b = _base_net_selling_flow_zscore_4q(closed_positions, decreased_positions,
                                          new_positions, increased_positions, inst_holders)
    return b - b.shift(_TD_QTR)


def fsp_drv2_060_closed_pos_above_2std_run(closed_positions: pd.Series) -> pd.Series:
    """Trailing-4Q sum of binary (closed > mean+2std) — count of extreme quarters."""
    mu = _rolling_mean(closed_positions, _TD_YEAR)
    std = _rolling_std(closed_positions, _TD_YEAR)
    flag = (closed_positions > mu + 2 * std).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def fsp_drv2_061_inst_shares_drawdown_ewm_slope(inst_shares: pd.Series) -> pd.Series:
    """EWM(63d) deviation of inst_shares 4Q-peak drawdown."""
    b = _base_inst_shares_drawdown_4q(inst_shares)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_062_holders_drawdown_ewm_slope(inst_holders: pd.Series) -> pd.Series:
    """EWM(63d) deviation of holder-count 4Q-peak drawdown."""
    b = _base_holders_drawdown_4q(inst_holders)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_063_selling_breadth_3q_chg(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """3Q change in combined selling breadth ratio."""
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    return b - b.shift(3 * _TD_QTR)


def fsp_drv2_064_closed_zscore_3q_chg(closed_positions: pd.Series) -> pd.Series:
    """3Q change in closed-positions 4Q z-score."""
    b = _base_closed_zscore_4q(closed_positions)
    return b - b.shift(3 * _TD_QTR)


def fsp_drv2_065_avg_position_cliff_drop_ewm_slope(avg_position: pd.Series) -> pd.Series:
    """EWM(63d) deviation of avg_position 2Q cliff-drop ratio."""
    b = _base_avg_position_cliff_drop_2q(avg_position)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_066_holders_pct_drop_zscore_qoq_chg(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in QoQ-pct-drop 4Q z-score of inst_holders."""
    pct_chg = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                        inst_holders.shift(_TD_QTR))
    b = _zscore_rolling(pct_chg, _TD_YEAR)
    return b - b.shift(_TD_QTR)


def fsp_drv2_067_inst_value_per_holder_qoq_chg(inst_value: pd.Series,
                                                 inst_holders: pd.Series) -> pd.Series:
    """QoQ change in value-per-holder — acceleration of per-institution value loss."""
    val_per = _safe_div(inst_value, inst_holders)
    b = _safe_div(val_per - val_per.shift(_TD_QTR), val_per.shift(_TD_QTR))
    return b - b.shift(_TD_QTR)


def fsp_drv2_068_closed_breadth_3q_chg(closed_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """3Q change in closed/inst_holders breadth ratio."""
    b = _base_closed_breadth(closed_positions, inst_holders)
    return b - b.shift(3 * _TD_QTR)


def fsp_drv2_069_sell_surplus_qoq_zscore(closed_positions: pd.Series,
                                           decreased_positions: pd.Series,
                                           new_positions: pd.Series,
                                           increased_positions: pd.Series) -> pd.Series:
    """Z-score of QoQ change in selling surplus over 4Q window."""
    b = _base_selling_surplus(closed_positions, decreased_positions,
                               new_positions, increased_positions)
    chg = b - b.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def fsp_drv2_070_inst_shares_cliff_ewm_slope(inst_shares: pd.Series) -> pd.Series:
    """EWM(63d) deviation of inst_shares 2Q cliff-drop ratio."""
    b = _base_inst_shares_cliff_drop_2q(inst_shares)
    return b - _ewm_mean(b, _TD_QTR)


def fsp_drv2_071_closed_pos_qoq_chg_ewm21(closed_positions: pd.Series) -> pd.Series:
    """EWM(21d) of QoQ change in closed positions — smoothed exit acceleration."""
    chg = closed_positions - closed_positions.shift(_TD_QTR)
    return _ewm_mean(chg, 21)


def fsp_drv2_072_combined_selling_qoq_chg_ewm21(closed_positions: pd.Series,
                                                  decreased_positions: pd.Series) -> pd.Series:
    """EWM(21d) of QoQ change in (closed+decreased) — smoothed combined selling acceleration."""
    s = closed_positions + decreased_positions
    chg = s - s.shift(_TD_QTR)
    return _ewm_mean(chg, 21)


def fsp_drv2_073_holder_qoq_chg_ewm21(inst_holders: pd.Series) -> pd.Series:
    """EWM(21d) of QoQ change in holder count — smoothed departure acceleration."""
    chg = inst_holders - inst_holders.shift(_TD_QTR)
    return _ewm_mean(chg, 21)


def fsp_drv2_074_selling_breadth_qoq_chg_zscore_2y(closed_positions: pd.Series,
                                                     decreased_positions: pd.Series,
                                                     inst_holders: pd.Series) -> pd.Series:
    """Z-score of QoQ change in selling breadth ratio over 2Y window."""
    b = _base_combined_selling_breadth(closed_positions, decreased_positions, inst_holders)
    chg = b - b.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_2Y)


def fsp_drv2_075_closed_breadth_qoq_chg_zscore_2y(closed_positions: pd.Series,
                                                    inst_holders: pd.Series) -> pd.Series:
    """Z-score of QoQ change in closed/holders breadth ratio over 2Y window."""
    b = _base_closed_breadth(closed_positions, inst_holders)
    chg = b - b.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_2Y)


# ===========================================================================
# Registry
# ===========================================================================

FORCED_SELLING_PROXY_REGISTRY_2ND_DERIVATIVES = {
    "fsp_drv2_001_closed_breadth_qoq_chg":             {"inputs": ["closed_positions", "inst_holders"],                                                                "func": fsp_drv2_001_closed_breadth_qoq_chg},
    "fsp_drv2_002_combined_selling_breadth_qoq_chg":   {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv2_002_combined_selling_breadth_qoq_chg},
    "fsp_drv2_003_closed_zscore_4q_qoq_chg":           {"inputs": ["closed_positions"],                                                                                "func": fsp_drv2_003_closed_zscore_4q_qoq_chg},
    "fsp_drv2_004_combined_selling_zscore_qoq_chg":    {"inputs": ["closed_positions", "decreased_positions"],                                                         "func": fsp_drv2_004_combined_selling_zscore_qoq_chg},
    "fsp_drv2_005_inst_shares_pct_drop_qoq_chg":       {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv2_005_inst_shares_pct_drop_qoq_chg},
    "fsp_drv2_006_avg_position_pct_collapse_qoq_chg":  {"inputs": ["avg_position"],                                                                                    "func": fsp_drv2_006_avg_position_pct_collapse_qoq_chg},
    "fsp_drv2_007_holders_pct_drop_qoq_chg":           {"inputs": ["inst_holders"],                                                                                    "func": fsp_drv2_007_holders_pct_drop_qoq_chg},
    "fsp_drv2_008_sell_buy_imbalance_qoq_chg":         {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                  "func": fsp_drv2_008_sell_buy_imbalance_qoq_chg},
    "fsp_drv2_009_avg_position_zscore_qoq_chg":        {"inputs": ["avg_position"],                                                                                    "func": fsp_drv2_009_avg_position_zscore_qoq_chg},
    "fsp_drv2_010_inst_pct_drop_qoq_chg":              {"inputs": ["inst_pct"],                                                                                        "func": fsp_drv2_010_inst_pct_drop_qoq_chg},
    "fsp_drv2_011_closed_vs_4q_max_qoq_chg":           {"inputs": ["closed_positions"],                                                                                "func": fsp_drv2_011_closed_vs_4q_max_qoq_chg},
    "fsp_drv2_012_holders_zscore_qoq_chg":             {"inputs": ["inst_holders"],                                                                                    "func": fsp_drv2_012_holders_zscore_qoq_chg},
    "fsp_drv2_013_inst_shares_zscore_qoq_chg":         {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv2_013_inst_shares_zscore_qoq_chg},
    "fsp_drv2_014_selling_breadth_zscore_qoq_chg":     {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv2_014_selling_breadth_zscore_qoq_chg},
    "fsp_drv2_015_net_selling_flow_qoq_chg":           {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],  "func": fsp_drv2_015_net_selling_flow_qoq_chg},
    "fsp_drv2_016_liquidation_synchrony_qoq_chg":      {"inputs": ["closed_positions", "inst_holders", "avg_position"],                                                "func": fsp_drv2_016_liquidation_synchrony_qoq_chg},
    "fsp_drv2_017_closed_ewm_spike_qoq_chg":           {"inputs": ["closed_positions"],                                                                                "func": fsp_drv2_017_closed_ewm_spike_qoq_chg},
    "fsp_drv2_018_avg_position_cliff_drop_qoq_chg":    {"inputs": ["avg_position"],                                                                                    "func": fsp_drv2_018_avg_position_cliff_drop_qoq_chg},
    "fsp_drv2_019_inst_shares_cliff_drop_qoq_chg":     {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv2_019_inst_shares_cliff_drop_qoq_chg},
    "fsp_drv2_020_closed_median_spike_qoq_chg":        {"inputs": ["closed_positions"],                                                                                "func": fsp_drv2_020_closed_median_spike_qoq_chg},
    "fsp_drv2_021_firesale_composite_qoq_chg":         {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],          "func": fsp_drv2_021_firesale_composite_qoq_chg},
    "fsp_drv2_022_inst_shares_drawdown_qoq_chg":       {"inputs": ["inst_shares"],                                                                                     "func": fsp_drv2_022_inst_shares_drawdown_qoq_chg},
    "fsp_drv2_023_holders_drawdown_qoq_chg":           {"inputs": ["inst_holders"],                                                                                    "func": fsp_drv2_023_holders_drawdown_qoq_chg},
    "fsp_drv2_024_closed_breadth_ewm_slope":           {"inputs": ["closed_positions", "inst_holders"],                                                                "func": fsp_drv2_024_closed_breadth_ewm_slope},
    "fsp_drv2_025_selling_breadth_ewm_acceleration":   {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                         "func": fsp_drv2_025_selling_breadth_ewm_acceleration},
    "fsp_drv2_026_inst_value_pct_drop_qoq_chg":        {"inputs": ["inst_value"],                                                                                     "func": fsp_drv2_026_inst_value_pct_drop_qoq_chg},
    "fsp_drv2_027_closed_pos_median_spike_2q_chg":     {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_027_closed_pos_median_spike_2q_chg},
    "fsp_drv2_028_inst_pct_qoq_drop_21d_slope":        {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv2_028_inst_pct_qoq_drop_21d_slope},
    "fsp_drv2_029_closed_breadth_21d_slope":           {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv2_029_closed_breadth_21d_slope},
    "fsp_drv2_030_combined_selling_breadth_21d_slope": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv2_030_combined_selling_breadth_21d_slope},
    "fsp_drv2_031_inst_shares_zscore_2q_chg":          {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv2_031_inst_shares_zscore_2q_chg},
    "fsp_drv2_032_avg_position_zscore_2q_chg":         {"inputs": ["avg_position"],                                                                                   "func": fsp_drv2_032_avg_position_zscore_2q_chg},
    "fsp_drv2_033_holders_zscore_2q_chg":              {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv2_033_holders_zscore_2q_chg},
    "fsp_drv2_034_sell_buy_imbalance_2q_chg":          {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv2_034_sell_buy_imbalance_2q_chg},
    "fsp_drv2_035_closed_zscore_2q_chg":               {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_035_closed_zscore_2q_chg},
    "fsp_drv2_036_net_selling_flow_2q_chg":            {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],"func": fsp_drv2_036_net_selling_flow_2q_chg},
    "fsp_drv2_037_inst_shares_drawdown_2q_chg":        {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv2_037_inst_shares_drawdown_2q_chg},
    "fsp_drv2_038_holders_drawdown_2q_chg":            {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv2_038_holders_drawdown_2q_chg},
    "fsp_drv2_039_firesale_composite_2q_chg":          {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],         "func": fsp_drv2_039_firesale_composite_2q_chg},
    "fsp_drv2_040_closed_breadth_zscore_qoq_chg":      {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv2_040_closed_breadth_zscore_qoq_chg},
    "fsp_drv2_041_inst_pct_zscore_qoq_chg":            {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv2_041_inst_pct_zscore_qoq_chg},
    "fsp_drv2_042_inst_value_zscore_qoq_chg":          {"inputs": ["inst_value"],                                                                                     "func": fsp_drv2_042_inst_value_zscore_qoq_chg},
    "fsp_drv2_043_decreased_pos_zscore_qoq_chg":       {"inputs": ["decreased_positions"],                                                                            "func": fsp_drv2_043_decreased_pos_zscore_qoq_chg},
    "fsp_drv2_044_selling_surplus_qoq_chg":            {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv2_044_selling_surplus_qoq_chg},
    "fsp_drv2_045_holder_turnover_qoq_chg":            {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                              "func": fsp_drv2_045_holder_turnover_qoq_chg},
    "fsp_drv2_046_closed_ewm_spike_2q_chg":            {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_046_closed_ewm_spike_2q_chg},
    "fsp_drv2_047_combined_selling_ewm_spike_qoq_chg": {"inputs": ["closed_positions", "decreased_positions"],                                                        "func": fsp_drv2_047_combined_selling_ewm_spike_qoq_chg},
    "fsp_drv2_048_inst_shares_per_holder_qoq_chg":     {"inputs": ["inst_shares", "inst_holders"],                                                                    "func": fsp_drv2_048_inst_shares_per_holder_qoq_chg},
    "fsp_drv2_049_selling_breadth_zscore_2q_chg":      {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv2_049_selling_breadth_zscore_2q_chg},
    "fsp_drv2_050_liquidation_synchrony_2q_chg":       {"inputs": ["closed_positions", "inst_holders", "avg_position"],                                               "func": fsp_drv2_050_liquidation_synchrony_2q_chg},
    "fsp_drv2_051_closed_breadth_ewm_slope_5d":        {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv2_051_closed_breadth_ewm_slope_5d},
    "fsp_drv2_052_inst_shares_pct_drop_ewm_slope":     {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv2_052_inst_shares_pct_drop_ewm_slope},
    "fsp_drv2_053_avg_position_pct_drop_ewm_slope":    {"inputs": ["avg_position"],                                                                                   "func": fsp_drv2_053_avg_position_pct_drop_ewm_slope},
    "fsp_drv2_054_holders_pct_drop_ewm_slope":         {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv2_054_holders_pct_drop_ewm_slope},
    "fsp_drv2_055_closed_pos_zscore_qoq_zscore_4q":    {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_055_closed_pos_zscore_qoq_zscore_4q},
    "fsp_drv2_056_sell_buy_imbalance_ewm_slope":       {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv2_056_sell_buy_imbalance_ewm_slope},
    "fsp_drv2_057_inst_pct_qoq_ewm_slope":             {"inputs": ["inst_pct"],                                                                                       "func": fsp_drv2_057_inst_pct_qoq_ewm_slope},
    "fsp_drv2_058_firesale_composite_ewm_slope":       {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],         "func": fsp_drv2_058_firesale_composite_ewm_slope},
    "fsp_drv2_059_net_flow_zscore_qoq_chg":            {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],"func": fsp_drv2_059_net_flow_zscore_qoq_chg},
    "fsp_drv2_060_closed_pos_above_2std_run":          {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_060_closed_pos_above_2std_run},
    "fsp_drv2_061_inst_shares_drawdown_ewm_slope":     {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv2_061_inst_shares_drawdown_ewm_slope},
    "fsp_drv2_062_holders_drawdown_ewm_slope":         {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv2_062_holders_drawdown_ewm_slope},
    "fsp_drv2_063_selling_breadth_3q_chg":             {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv2_063_selling_breadth_3q_chg},
    "fsp_drv2_064_closed_zscore_3q_chg":               {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_064_closed_zscore_3q_chg},
    "fsp_drv2_065_avg_position_cliff_drop_ewm_slope":  {"inputs": ["avg_position"],                                                                                   "func": fsp_drv2_065_avg_position_cliff_drop_ewm_slope},
    "fsp_drv2_066_holders_pct_drop_zscore_qoq_chg":   {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv2_066_holders_pct_drop_zscore_qoq_chg},
    "fsp_drv2_067_inst_value_per_holder_qoq_chg":      {"inputs": ["inst_value", "inst_holders"],                                                                     "func": fsp_drv2_067_inst_value_per_holder_qoq_chg},
    "fsp_drv2_068_closed_breadth_3q_chg":              {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv2_068_closed_breadth_3q_chg},
    "fsp_drv2_069_sell_surplus_qoq_zscore":            {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                "func": fsp_drv2_069_sell_surplus_qoq_zscore},
    "fsp_drv2_070_inst_shares_cliff_ewm_slope":        {"inputs": ["inst_shares"],                                                                                    "func": fsp_drv2_070_inst_shares_cliff_ewm_slope},
    "fsp_drv2_071_closed_pos_qoq_chg_ewm21":           {"inputs": ["closed_positions"],                                                                               "func": fsp_drv2_071_closed_pos_qoq_chg_ewm21},
    "fsp_drv2_072_combined_selling_qoq_chg_ewm21":     {"inputs": ["closed_positions", "decreased_positions"],                                                        "func": fsp_drv2_072_combined_selling_qoq_chg_ewm21},
    "fsp_drv2_073_holder_qoq_chg_ewm21":               {"inputs": ["inst_holders"],                                                                                   "func": fsp_drv2_073_holder_qoq_chg_ewm21},
    "fsp_drv2_074_selling_breadth_qoq_chg_zscore_2y":  {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                        "func": fsp_drv2_074_selling_breadth_qoq_chg_zscore_2y},
    "fsp_drv2_075_closed_breadth_qoq_chg_zscore_2y":   {"inputs": ["closed_positions", "inst_holders"],                                                               "func": fsp_drv2_075_closed_breadth_qoq_chg_zscore_2y},
}
