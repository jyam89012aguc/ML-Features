"""
93_institutional_bottom_fish | SF3 Institutional Ownership — 3rd-Derivative Features (001-075)

DOMAIN
------
Rate-of-change of the 2nd-derivative accumulation signals — i.e. the jerk /
acceleration of the acceleration.  These features capture whether the
bottom-fishing momentum is itself speeding up or reversing.

NOTE ON SPARSITY
----------------
Third derivatives of quarterly-updated step-functions are extremely sparse on
a daily index: most observations will be zero or NaN between quarterly updates.
This is expected and correct — the signal fires only when quarterly data
transitions.  Downstream models should treat these as sparse categorical
impulses rather than continuous series.

QUARTERLY → DAILY ALIGNMENT CONTRACT
-------------------------------------
All ownership fields are forward-filled quarterly snapshots. `close` is a
genuine daily series.  No cross-file imports; all base and 2nd-derivative
signals are recomputed inline.

Trading-day conventions
------------------------
1 quarter  = 63  trading days  (_TD_QTR)
2 quarters = 126 trading days  (_TD_2Q)
1 year     = 252 trading days  (_TD_YEAR)
2 years    = 504 trading days  (_TD_2Y)
3 years    = 756 trading days  (_TD_3Y)
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
# Utility helpers (self-contained, no cross-file imports)
# ---------------------------------------------------------------------------

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / (den.replace(0, np.nan) + _EPS * (den == 0).astype(float))


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=2).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu = _rolling_mean(s, w)
    sd = _rolling_std(s, w).replace(0, np.nan)
    return (s - mu) / (sd + _EPS)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=1).mean()


def _proximity_to_trailing_low(close: pd.Series, window: int) -> pd.Series:
    trail_low = _rolling_min(close, window)
    return _safe_div(close - trail_low, trail_low)


def _drawdown_from_trailing_high(close: pd.Series, window: int) -> pd.Series:
    trail_high = _rolling_max(close, window)
    return _safe_div(trail_high - close, trail_high)


# ---------------------------------------------------------------------------
# Inline base-signal recompute helpers
# ---------------------------------------------------------------------------

def _base_gross_additions(new_positions: pd.Series,
                           increased_positions: pd.Series) -> pd.Series:
    return new_positions.fillna(0) + increased_positions.fillna(0)


def _base_net_additions(new_positions: pd.Series,
                        increased_positions: pd.Series,
                        closed_positions: pd.Series,
                        decreased_positions: pd.Series) -> pd.Series:
    return (new_positions.fillna(0) + increased_positions.fillna(0)
            - closed_positions.fillna(0) - decreased_positions.fillna(0))


def _base_add_to_exit_ratio(new_positions: pd.Series,
                             increased_positions: pd.Series,
                             closed_positions: pd.Series,
                             decreased_positions: pd.Series) -> pd.Series:
    adds = new_positions.fillna(0) + increased_positions.fillna(0)
    exits = closed_positions.fillna(0) + decreased_positions.fillna(0)
    return _safe_div(adds, exits + _EPS)


def _base_buyer_breadth(new_positions: pd.Series,
                         increased_positions: pd.Series,
                         inst_holders: pd.Series) -> pd.Series:
    gross = _base_gross_additions(new_positions, increased_positions)
    return _safe_div(gross, inst_holders.ffill().replace(0, np.nan))


# ---------------------------------------------------------------------------
# Inline 2nd-derivative recompute helpers
# ---------------------------------------------------------------------------

def _drv2_gross_add_qoq_roc(new_positions: pd.Series,
                              increased_positions: pd.Series) -> pd.Series:
    """2nd derivative: QoQ diff of (QoQ diff of gross additions)."""
    gross = _base_gross_additions(new_positions, increased_positions)
    return gross.diff(_TD_QTR).diff(_TD_QTR)


def _drv2_net_add_qoq_roc(new_positions: pd.Series,
                            increased_positions: pd.Series,
                            closed_positions: pd.Series,
                            decreased_positions: pd.Series) -> pd.Series:
    net = _base_net_additions(new_positions, increased_positions,
                              closed_positions, decreased_positions)
    return net.diff(_TD_QTR).diff(_TD_QTR)


def _drv2_new_pos_qoq_roc(new_positions: pd.Series) -> pd.Series:
    return new_positions.fillna(0).diff(_TD_QTR).diff(_TD_QTR)


def _drv2_increased_pos_qoq_roc(increased_positions: pd.Series) -> pd.Series:
    return increased_positions.fillna(0).diff(_TD_QTR).diff(_TD_QTR)


def _drv2_inst_shares_qoq_roc(inst_shares: pd.Series) -> pd.Series:
    return inst_shares.ffill().diff(_TD_QTR).diff(_TD_QTR)


def _drv2_inst_value_qoq_roc(inst_value: pd.Series) -> pd.Series:
    return inst_value.ffill().diff(_TD_QTR).diff(_TD_QTR)


def _drv2_inst_pct_qoq_roc(inst_pct: pd.Series) -> pd.Series:
    return inst_pct.ffill().diff(_TD_QTR).diff(_TD_QTR)


def _drv2_gross_add_ewm_dev(new_positions: pd.Series,
                              increased_positions: pd.Series) -> pd.Series:
    gross = _base_gross_additions(new_positions, increased_positions)
    return gross - _ewm_mean(gross, _TD_2Q)


def _drv2_add_exit_ratio_roc(new_positions: pd.Series,
                               increased_positions: pd.Series,
                               closed_positions: pd.Series,
                               decreased_positions: pd.Series) -> pd.Series:
    ratio = _base_add_to_exit_ratio(new_positions, increased_positions,
                                    closed_positions, decreased_positions)
    return ratio.diff(_TD_QTR).diff(_TD_QTR)


def _drv2_buyer_breadth_roc(new_positions: pd.Series,
                              increased_positions: pd.Series,
                              inst_holders: pd.Series) -> pd.Series:
    breadth = _base_buyer_breadth(new_positions, increased_positions, inst_holders)
    return breadth.diff(_TD_QTR).diff(_TD_QTR)


# ===========================================================================
# 3rd-Derivative Features: rate-of-change of the 2nd-derivative signals
# Convention: take QoQ diff of each 2nd-derivative, or slope/EWM of it.
# ===========================================================================

def ibf_drv3_001_gross_add_3rd_diff(new_positions: pd.Series,
                                     increased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of gross additions (jerk of accumulation count)."""
    d2 = _drv2_gross_add_qoq_roc(new_positions, increased_positions)
    return d2.diff(_TD_QTR)


def ibf_drv3_002_net_add_3rd_diff(new_positions: pd.Series,
                                    increased_positions: pd.Series,
                                    closed_positions: pd.Series,
                                    decreased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of net additions."""
    d2 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions)
    return d2.diff(_TD_QTR)


def ibf_drv3_003_new_pos_3rd_diff(new_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of new_positions."""
    d2 = _drv2_new_pos_qoq_roc(new_positions)
    return d2.diff(_TD_QTR)


def ibf_drv3_004_increased_pos_3rd_diff(increased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of increased_positions."""
    d2 = _drv2_increased_pos_qoq_roc(increased_positions)
    return d2.diff(_TD_QTR)


def ibf_drv3_005_inst_shares_3rd_diff(inst_shares: pd.Series) -> pd.Series:
    """3rd QoQ difference of institutional shares."""
    d2 = _drv2_inst_shares_qoq_roc(inst_shares)
    return d2.diff(_TD_QTR)


def ibf_drv3_006_inst_value_3rd_diff(inst_value: pd.Series) -> pd.Series:
    """3rd QoQ difference of institutional value."""
    d2 = _drv2_inst_value_qoq_roc(inst_value)
    return d2.diff(_TD_QTR)


def ibf_drv3_007_inst_pct_3rd_diff(inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of institutional ownership percentage."""
    d2 = _drv2_inst_pct_qoq_roc(inst_pct)
    return d2.diff(_TD_QTR)


def ibf_drv3_008_add_exit_ratio_3rd_diff(new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          closed_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """3rd QoQ difference of add-to-exit ratio."""
    d2 = _drv2_add_exit_ratio_roc(new_positions, increased_positions,
                                   closed_positions, decreased_positions)
    return d2.diff(_TD_QTR)


def ibf_drv3_009_buyer_breadth_3rd_diff(new_positions: pd.Series,
                                         increased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of buyer breadth."""
    d2 = _drv2_buyer_breadth_roc(new_positions, increased_positions, inst_holders)
    return d2.diff(_TD_QTR)


def ibf_drv3_010_gross_add_accel_ewm_dev(new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """EWM deviation of the 2nd-derivative gross-add series (surprise vs trend)."""
    d2 = _drv2_gross_add_qoq_roc(new_positions, increased_positions)
    return d2 - _ewm_mean(d2, _TD_2Q)


def ibf_drv3_011_net_add_accel_ewm_dev(new_positions: pd.Series,
                                        increased_positions: pd.Series,
                                        closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """EWM deviation of the 2nd-derivative net-add series."""
    d2 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions)
    return d2 - _ewm_mean(d2, _TD_2Q)


def ibf_drv3_012_inst_shares_accel_ewm_dev(inst_shares: pd.Series) -> pd.Series:
    """EWM deviation of 2nd-derivative institutional shares."""
    d2 = _drv2_inst_shares_qoq_roc(inst_shares)
    return d2 - _ewm_mean(d2, _TD_2Q)


def ibf_drv3_013_inst_value_accel_ewm_dev(inst_value: pd.Series) -> pd.Series:
    """EWM deviation of 2nd-derivative institutional value."""
    d2 = _drv2_inst_value_qoq_roc(inst_value)
    return d2 - _ewm_mean(d2, _TD_2Q)


def ibf_drv3_014_inst_pct_accel_ewm_dev(inst_pct: pd.Series) -> pd.Series:
    """EWM deviation of 2nd-derivative ownership pct."""
    d2 = _drv2_inst_pct_qoq_roc(inst_pct)
    return d2 - _ewm_mean(d2, _TD_2Q)


def ibf_drv3_015_gross_add_ewm_dev_slope(new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """Rolling 1-year OLS slope of the 2nd-derivative EWM-deviation signal."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean()
        ym = x.mean()
        denom = ((xi - xm) ** 2).sum()
        return 0.0 if denom < _EPS else float(((xi - xm) * (x - ym)).sum() / denom)
    d2_dev = _drv2_gross_add_ewm_dev(new_positions, increased_positions)
    return d2_dev.rolling(_TD_YEAR, min_periods=2).apply(_slope, raw=True)


def ibf_drv3_016_new_pos_accel_zscore(new_positions: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of the 3rd-diff new_positions."""
    d3 = _drv2_new_pos_qoq_roc(new_positions).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def ibf_drv3_017_gross_add_jerk_at_low(new_positions: pd.Series,
                                        increased_positions: pd.Series,
                                        close: pd.Series) -> pd.Series:
    """3rd-diff gross additions * 1-yr drawdown depth."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_YEAR)
    return d3 * dd


def ibf_drv3_018_net_add_jerk_at_low(new_positions: pd.Series,
                                      increased_positions: pd.Series,
                                      closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      close: pd.Series) -> pd.Series:
    """3rd-diff net additions * 1-yr drawdown depth."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_YEAR)
    return d3 * dd


def ibf_drv3_019_inst_shares_jerk_at_low(inst_shares: pd.Series,
                                          close: pd.Series) -> pd.Series:
    """3rd-diff institutional shares * 2-yr drawdown depth."""
    d3 = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


def ibf_drv3_020_inst_value_jerk_at_low(inst_value: pd.Series,
                                         close: pd.Series) -> pd.Series:
    """3rd-diff institutional value * 2-yr drawdown depth."""
    d3 = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


def ibf_drv3_021_add_ratio_3rd_diff_zscore(new_positions: pd.Series,
                                             increased_positions: pd.Series,
                                             closed_positions: pd.Series,
                                             decreased_positions: pd.Series) -> pd.Series:
    """2-year z-score of the 3rd-diff add-to-exit ratio."""
    d3 = _drv2_add_exit_ratio_roc(new_positions, increased_positions,
                                   closed_positions, decreased_positions).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def ibf_drv3_022_buyer_breadth_jerk_zscore(new_positions: pd.Series,
                                             increased_positions: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """2-year z-score of the 3rd-diff buyer-breadth series."""
    d3 = _drv2_buyer_breadth_roc(new_positions, increased_positions,
                                  inst_holders).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def ibf_drv3_023_gross_add_accel_rolling_mean(new_positions: pd.Series,
                                               increased_positions: pd.Series) -> pd.Series:
    """4-quarter rolling mean of the 2nd-derivative gross-add series."""
    d2 = _drv2_gross_add_qoq_roc(new_positions, increased_positions)
    return _rolling_mean(d2, _TD_YEAR)


def ibf_drv3_024_inst_pct_jerk_at_3y_low(inst_pct: pd.Series,
                                           close: pd.Series) -> pd.Series:
    """3rd-diff ownership pct * 3-yr drawdown depth."""
    d3 = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_3Y)
    return d3 * dd


def ibf_drv3_025_composite_jerk_at_3y_low(new_positions: pd.Series,
                                            increased_positions: pd.Series,
                                            closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            inst_shares: pd.Series,
                                            inst_value: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """Composite 3rd-diff signal: sum of z-scores of gross-add jerk, net-add jerk,
    shares jerk, value jerk, all scaled by 3-yr drawdown depth."""
    d3_gross = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    d3_net = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                    closed_positions, decreased_positions).diff(_TD_QTR)
    d3_shares = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    d3_value = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    z = (_zscore_rolling(d3_gross, _TD_2Y)
         + _zscore_rolling(d3_net, _TD_2Y)
         + _zscore_rolling(d3_shares, _TD_2Y)
         + _zscore_rolling(d3_value, _TD_2Y))
    dd = _drawdown_from_trailing_high(close, _TD_3Y)
    return z * dd


# ===========================================================================
# 3rd-Derivative Features 026 – 075  (NEW)
# ===========================================================================

# --- Additional 2nd-derivative helper functions (inline) -------------------

def _drv2_inst_holders_qoq_roc(inst_holders: pd.Series) -> pd.Series:
    return inst_holders.ffill().diff(_TD_QTR).diff(_TD_QTR)


def _drv2_inst_pct_qoq_roc2(inst_pct: pd.Series) -> pd.Series:
    return inst_pct.ffill().diff(_TD_QTR).diff(_TD_QTR)


def _drv2_gross_add_ewm_dev(new_positions: pd.Series,
                              increased_positions: pd.Series) -> pd.Series:
    gross = _base_gross_additions(new_positions, increased_positions)
    return gross - _ewm_mean(gross, _TD_2Q)


def _drv2_net_add_ewm_dev(new_positions: pd.Series,
                            increased_positions: pd.Series,
                            closed_positions: pd.Series,
                            decreased_positions: pd.Series) -> pd.Series:
    net = _base_net_additions(new_positions, increased_positions,
                              closed_positions, decreased_positions)
    return net - _ewm_mean(net, _TD_2Q)


def _drv2_inst_shares_ewm_dev(inst_shares: pd.Series) -> pd.Series:
    s = inst_shares.ffill().fillna(0)
    return s - _ewm_mean(s, _TD_QTR)


def _drv2_inst_value_ewm_dev(inst_value: pd.Series) -> pd.Series:
    v = inst_value.ffill().fillna(0)
    return v - _ewm_mean(v, _TD_QTR)


def _drv2_inst_pct_ewm_dev(inst_pct: pd.Series) -> pd.Series:
    p = inst_pct.ffill().fillna(0)
    return p - _ewm_mean(p, _TD_2Q)


def _drv2_buyer_breadth_ewm_dev(new_positions: pd.Series,
                                  increased_positions: pd.Series,
                                  inst_holders: pd.Series) -> pd.Series:
    breadth = _base_buyer_breadth(new_positions, increased_positions, inst_holders)
    return breadth - _ewm_mean(breadth, _TD_2Q)


def _drv2_add_ratio_ewm_dev(new_positions: pd.Series,
                              increased_positions: pd.Series,
                              closed_positions: pd.Series,
                              decreased_positions: pd.Series) -> pd.Series:
    ratio = _base_add_to_exit_ratio(new_positions, increased_positions,
                                    closed_positions, decreased_positions)
    return ratio.diff(_TD_QTR) - _ewm_mean(ratio.diff(_TD_QTR), _TD_2Q)


# --- 3rd differences of additional signals ----------------------------------

def ibf_drv3_026_inst_holders_3rd_diff(inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of institutional holder count."""
    d2 = _drv2_inst_holders_qoq_roc(inst_holders)
    return d2.diff(_TD_QTR)


def ibf_drv3_027_inst_pct_3rd_diff_alt(inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of institutional ownership pct (via alt helper)."""
    d2 = _drv2_inst_pct_qoq_roc2(inst_pct)
    return d2.diff(_TD_QTR)


def ibf_drv3_028_gross_add_ewm_dev_roc(new_positions: pd.Series,
                                         increased_positions: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of gross additions (derivative of surprise)."""
    d2_dev = _drv2_gross_add_ewm_dev(new_positions, increased_positions)
    return d2_dev.diff(_TD_QTR)


def ibf_drv3_029_net_add_ewm_dev_roc(new_positions: pd.Series,
                                       increased_positions: pd.Series,
                                       closed_positions: pd.Series,
                                       decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of net additions."""
    d2_dev = _drv2_net_add_ewm_dev(new_positions, increased_positions,
                                    closed_positions, decreased_positions)
    return d2_dev.diff(_TD_QTR)


def ibf_drv3_030_inst_shares_ewm_dev_roc(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of institutional shares."""
    d2_dev = _drv2_inst_shares_ewm_dev(inst_shares)
    return d2_dev.diff(_TD_QTR)


def ibf_drv3_031_inst_value_ewm_dev_roc(inst_value: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of institutional value."""
    d2_dev = _drv2_inst_value_ewm_dev(inst_value)
    return d2_dev.diff(_TD_QTR)


def ibf_drv3_032_inst_pct_ewm_dev_roc(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of ownership pct."""
    d2_dev = _drv2_inst_pct_ewm_dev(inst_pct)
    return d2_dev.diff(_TD_QTR)


def ibf_drv3_033_buyer_breadth_ewm_dev_roc(new_positions: pd.Series,
                                             increased_positions: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of buyer breadth."""
    d2_dev = _drv2_buyer_breadth_ewm_dev(new_positions, increased_positions, inst_holders)
    return d2_dev.diff(_TD_QTR)


def ibf_drv3_034_add_ratio_ewm_dev_roc(new_positions: pd.Series,
                                         increased_positions: pd.Series,
                                         closed_positions: pd.Series,
                                         decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in the EWM-deviation of the add-to-exit ratio velocity."""
    d2_dev = _drv2_add_ratio_ewm_dev(new_positions, increased_positions,
                                      closed_positions, decreased_positions)
    return d2_dev.diff(_TD_QTR)


# --- Z-score of 3rd-difference signals -------------------------------------

def ibf_drv3_035_gross_add_jerk_zscore_2y(new_positions: pd.Series,
                                            increased_positions: pd.Series) -> pd.Series:
    """2-year z-score of the 3rd QoQ diff of gross additions."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def ibf_drv3_036_net_add_jerk_zscore_2y(new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          closed_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """2-year z-score of the 3rd QoQ diff of net additions."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def ibf_drv3_037_inst_holders_jerk_zscore_2y(inst_holders: pd.Series) -> pd.Series:
    """2-year z-score of the 3rd QoQ diff of holder count."""
    d3 = _drv2_inst_holders_qoq_roc(inst_holders).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def ibf_drv3_038_inst_pct_jerk_zscore_2y(inst_pct: pd.Series) -> pd.Series:
    """2-year z-score of the 3rd QoQ diff of ownership pct."""
    d3 = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


# --- EWM deviation of 3rd-difference signals --------------------------------

def ibf_drv3_039_gross_add_jerk_ewm_dev(new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """3rd-diff gross additions minus its EWM(2Q)."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return d3 - _ewm_mean(d3, _TD_2Q)


def ibf_drv3_040_net_add_jerk_ewm_dev(new_positions: pd.Series,
                                        increased_positions: pd.Series,
                                        closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """3rd-diff net additions minus its EWM(2Q)."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    return d3 - _ewm_mean(d3, _TD_2Q)


def ibf_drv3_041_inst_shares_jerk_ewm_dev(inst_shares: pd.Series) -> pd.Series:
    """3rd-diff institutional shares minus its EWM(2Q)."""
    d3 = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    return d3 - _ewm_mean(d3, _TD_2Q)


def ibf_drv3_042_inst_value_jerk_ewm_dev(inst_value: pd.Series) -> pd.Series:
    """3rd-diff institutional value minus its EWM(2Q)."""
    d3 = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    return d3 - _ewm_mean(d3, _TD_2Q)


def ibf_drv3_043_inst_pct_jerk_ewm_dev(inst_pct: pd.Series) -> pd.Series:
    """3rd-diff ownership pct minus its EWM(2Q)."""
    d3 = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    return d3 - _ewm_mean(d3, _TD_2Q)


# --- Rolling mean of 3rd-difference signals ---------------------------------

def ibf_drv3_044_gross_add_jerk_mean_2q(new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """2-quarter rolling mean of 3rd-diff gross additions."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return _rolling_mean(d3, _TD_2Q)


def ibf_drv3_045_net_add_jerk_mean_2q(new_positions: pd.Series,
                                        increased_positions: pd.Series,
                                        closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """2-quarter rolling mean of 3rd-diff net additions."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    return _rolling_mean(d3, _TD_2Q)


def ibf_drv3_046_inst_shares_jerk_mean_4q(inst_shares: pd.Series) -> pd.Series:
    """4-quarter rolling mean of 3rd-diff institutional shares."""
    d3 = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


def ibf_drv3_047_inst_value_jerk_mean_4q(inst_value: pd.Series) -> pd.Series:
    """4-quarter rolling mean of 3rd-diff institutional value."""
    d3 = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


def ibf_drv3_048_inst_pct_jerk_mean_4q(inst_pct: pd.Series) -> pd.Series:
    """4-quarter rolling mean of 3rd-diff ownership pct."""
    d3 = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


# --- Drawdown-conditioned 3rd-diff signals ----------------------------------

def ibf_drv3_049_gross_add_jerk_at_2y_low(new_positions: pd.Series,
                                            increased_positions: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """3rd-diff gross additions * 2-yr drawdown depth."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


def ibf_drv3_050_net_add_jerk_at_2y_low(new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          close: pd.Series) -> pd.Series:
    """3rd-diff net additions * 2-yr drawdown depth."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


def ibf_drv3_051_inst_holders_jerk_at_1y_low(inst_holders: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """3rd-diff holder count * 1-yr drawdown depth."""
    d3 = _drv2_inst_holders_qoq_roc(inst_holders).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_YEAR)
    return d3 * dd


def ibf_drv3_052_inst_pct_jerk_at_2y_low(inst_pct: pd.Series,
                                           close: pd.Series) -> pd.Series:
    """3rd-diff ownership pct * 2-yr drawdown depth."""
    d3 = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


def ibf_drv3_053_buyer_breadth_jerk_at_2y_low(new_positions: pd.Series,
                                                increased_positions: pd.Series,
                                                inst_holders: pd.Series,
                                                close: pd.Series) -> pd.Series:
    """3rd-diff buyer breadth * 2-yr drawdown depth."""
    d3 = _drv2_buyer_breadth_roc(new_positions, increased_positions, inst_holders).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


def ibf_drv3_054_add_ratio_jerk_at_2y_low(new_positions: pd.Series,
                                            increased_positions: pd.Series,
                                            closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            close: pd.Series) -> pd.Series:
    """3rd-diff add-to-exit ratio * 2-yr drawdown depth."""
    d3 = _drv2_add_exit_ratio_roc(new_positions, increased_positions,
                                   closed_positions, decreased_positions).diff(_TD_QTR)
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return d3 * dd


# --- OLS slope of 3rd-difference signals (4th order, trend of jerk) --------

def ibf_drv3_055_gross_add_jerk_slope_1y(new_positions: pd.Series,
                                           increased_positions: pd.Series) -> pd.Series:
    """Rolling 1-year OLS slope of 3rd-diff gross additions."""
    def _slope(x):
        n = len(x)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float); xm = xi.mean(); ym = x.mean()
        denom = ((xi - xm) ** 2).sum()
        return 0.0 if denom < _EPS else float(((xi - xm) * (x - ym)).sum() / denom)
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=2).apply(_slope, raw=True)


def ibf_drv3_056_inst_shares_jerk_slope_2y(inst_shares: pd.Series) -> pd.Series:
    """Rolling 2-year OLS slope of 3rd-diff institutional shares."""
    def _slope(x):
        n = len(x)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float); xm = xi.mean(); ym = x.mean()
        denom = ((xi - xm) ** 2).sum()
        return 0.0 if denom < _EPS else float(((xi - xm) * (x - ym)).sum() / denom)
    d3 = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    return d3.rolling(_TD_2Y, min_periods=2).apply(_slope, raw=True)


def ibf_drv3_057_inst_value_jerk_slope_2y(inst_value: pd.Series) -> pd.Series:
    """Rolling 2-year OLS slope of 3rd-diff institutional value."""
    def _slope(x):
        n = len(x)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float); xm = xi.mean(); ym = x.mean()
        denom = ((xi - xm) ** 2).sum()
        return 0.0 if denom < _EPS else float(((xi - xm) * (x - ym)).sum() / denom)
    d3 = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    return d3.rolling(_TD_2Y, min_periods=2).apply(_slope, raw=True)


# --- Composite 3rd-derivative signals ---------------------------------------

def ibf_drv3_058_shares_and_value_jerk_composite(inst_shares: pd.Series,
                                                   inst_value: pd.Series) -> pd.Series:
    """Sum of 2-yr z-scores of 3rd-diff shares and 3rd-diff value."""
    d3_s = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    d3_v = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    return _zscore_rolling(d3_s, _TD_2Y) + _zscore_rolling(d3_v, _TD_2Y)


def ibf_drv3_059_gross_and_net_jerk_composite(new_positions: pd.Series,
                                               increased_positions: pd.Series,
                                               closed_positions: pd.Series,
                                               decreased_positions: pd.Series) -> pd.Series:
    """Sum of 2-yr z-scores of 3rd-diff gross-add and 3rd-diff net-add."""
    d3_g = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    d3_n = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                   closed_positions, decreased_positions).diff(_TD_QTR)
    return _zscore_rolling(d3_g, _TD_2Y) + _zscore_rolling(d3_n, _TD_2Y)


def ibf_drv3_060_five_signal_jerk_composite(new_positions: pd.Series,
                                              increased_positions: pd.Series,
                                              closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              inst_shares: pd.Series,
                                              inst_value: pd.Series,
                                              inst_pct: pd.Series) -> pd.Series:
    """Sum of 2-yr z-scores of 3rd-diffs: gross, net, shares, value, pct."""
    d3_g = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    d3_n = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                   closed_positions, decreased_positions).diff(_TD_QTR)
    d3_s = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    d3_v = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    d3_p = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    return (_zscore_rolling(d3_g, _TD_2Y) + _zscore_rolling(d3_n, _TD_2Y)
            + _zscore_rolling(d3_s, _TD_2Y) + _zscore_rolling(d3_v, _TD_2Y)
            + _zscore_rolling(d3_p, _TD_2Y))


def ibf_drv3_061_five_signal_jerk_at_1y_low(new_positions: pd.Series,
                                              increased_positions: pd.Series,
                                              closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              inst_shares: pd.Series,
                                              inst_value: pd.Series,
                                              inst_pct: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """Five-signal jerk composite * 1-yr drawdown depth."""
    combo = ibf_drv3_060_five_signal_jerk_composite(
        new_positions, increased_positions, closed_positions, decreased_positions,
        inst_shares, inst_value, inst_pct
    )
    dd = _drawdown_from_trailing_high(close, _TD_YEAR)
    return combo * dd


def ibf_drv3_062_seven_signal_jerk_at_3y_low(new_positions: pd.Series,
                                               increased_positions: pd.Series,
                                               closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               inst_holders: pd.Series,
                                               inst_shares: pd.Series,
                                               inst_value: pd.Series,
                                               inst_pct: pd.Series,
                                               close: pd.Series) -> pd.Series:
    """Seven-signal jerk composite (adds holders + buyer_breadth) * 3-yr drawdown."""
    d3_g = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    d3_n = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                   closed_positions, decreased_positions).diff(_TD_QTR)
    d3_h = _drv2_inst_holders_qoq_roc(inst_holders).diff(_TD_QTR)
    d3_s = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    d3_v = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    d3_p = _drv2_inst_pct_qoq_roc(inst_pct).diff(_TD_QTR)
    d3_bb = _drv2_buyer_breadth_roc(new_positions, increased_positions, inst_holders).diff(_TD_QTR)
    z = (_zscore_rolling(d3_g, _TD_2Y) + _zscore_rolling(d3_n, _TD_2Y)
         + _zscore_rolling(d3_h, _TD_2Y) + _zscore_rolling(d3_s, _TD_2Y)
         + _zscore_rolling(d3_v, _TD_2Y) + _zscore_rolling(d3_p, _TD_2Y)
         + _zscore_rolling(d3_bb, _TD_2Y))
    dd = _drawdown_from_trailing_high(close, _TD_3Y)
    return z * dd


# --- Positive-only jerk flags -----------------------------------------------

def ibf_drv3_063_gross_add_jerk_positive_flag(new_positions: pd.Series,
                                               increased_positions: pd.Series) -> pd.Series:
    """1 if 3rd-diff gross additions > 0 (jerk is positive), else 0."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return (d3 > 0).astype(float)


def ibf_drv3_064_net_add_jerk_positive_flag(new_positions: pd.Series,
                                             increased_positions: pd.Series,
                                             closed_positions: pd.Series,
                                             decreased_positions: pd.Series) -> pd.Series:
    """1 if 3rd-diff net additions > 0, else 0."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    return (d3 > 0).astype(float)


def ibf_drv3_065_shares_jerk_positive_flag(inst_shares: pd.Series) -> pd.Series:
    """1 if 3rd-diff institutional shares > 0, else 0."""
    d3 = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    return (d3 > 0).astype(float)


def ibf_drv3_066_value_jerk_positive_flag(inst_value: pd.Series) -> pd.Series:
    """1 if 3rd-diff institutional value > 0, else 0."""
    d3 = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    return (d3 > 0).astype(float)


def ibf_drv3_067_joint_jerk_positive_flag(new_positions: pd.Series,
                                            increased_positions: pd.Series,
                                            inst_shares: pd.Series,
                                            inst_value: pd.Series) -> pd.Series:
    """1 if gross-add, shares, and value jerks are all positive simultaneously."""
    d3_g = (_drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR) > 0).astype(float)
    d3_s = (_drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR) > 0).astype(float)
    d3_v = (_drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR) > 0).astype(float)
    return d3_g * d3_s * d3_v


# --- Rolling count of positive jerk days ------------------------------------

def ibf_drv3_068_gross_add_jerk_positive_count_4q(new_positions: pd.Series,
                                                    increased_positions: pd.Series) -> pd.Series:
    """Count of days in 4-quarter window where gross-add jerk > 0."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return _rolling_sum((d3 > 0).astype(float), _TD_YEAR)


def ibf_drv3_069_inst_shares_jerk_positive_count_4q(inst_shares: pd.Series) -> pd.Series:
    """Count of days in 4-quarter window where shares jerk > 0."""
    d3 = _drv2_inst_shares_qoq_roc(inst_shares).diff(_TD_QTR)
    return _rolling_sum((d3 > 0).astype(float), _TD_YEAR)


# --- Jerk std (volatility of jerk) ------------------------------------------

def ibf_drv3_070_gross_add_jerk_std_2y(new_positions: pd.Series,
                                         increased_positions: pd.Series) -> pd.Series:
    """Rolling 2-year std of 3rd-diff gross additions."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return d3.rolling(_TD_2Y, min_periods=2).std()


def ibf_drv3_071_inst_value_jerk_std_2y(inst_value: pd.Series) -> pd.Series:
    """Rolling 2-year std of 3rd-diff institutional value."""
    d3 = _drv2_inst_value_qoq_roc(inst_value).diff(_TD_QTR)
    return d3.rolling(_TD_2Y, min_periods=2).std()


# --- Accel-of-accel EWM ratio -----------------------------------------------

def ibf_drv3_072_gross_add_jerk_ewm_ratio(new_positions: pd.Series,
                                            increased_positions: pd.Series) -> pd.Series:
    """EWM(1Q) of jerk / EWM(2Q) of jerk — short vs medium momentum of jerk."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return _safe_div(_ewm_mean(d3, _TD_QTR), _ewm_mean(d3, _TD_2Q) + _EPS)


def ibf_drv3_073_net_add_jerk_ewm_ratio(new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          closed_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """EWM(1Q)/EWM(2Q) ratio of net-add jerk."""
    d3 = _drv2_net_add_qoq_roc(new_positions, increased_positions,
                                closed_positions, decreased_positions).diff(_TD_QTR)
    return _safe_div(_ewm_mean(d3, _TD_QTR), _ewm_mean(d3, _TD_2Q) + _EPS)


# --- 4th-order difference (jerk-of-jerk) ------------------------------------

def ibf_drv3_074_gross_add_4th_diff(new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """4th QoQ difference of gross additions (snap — derivative of jerk)."""
    d3 = _drv2_gross_add_qoq_roc(new_positions, increased_positions).diff(_TD_QTR)
    return d3.diff(_TD_QTR)


def ibf_drv3_075_five_signal_jerk_at_2y_low(new_positions: pd.Series,
                                              increased_positions: pd.Series,
                                              closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              inst_shares: pd.Series,
                                              inst_value: pd.Series,
                                              inst_pct: pd.Series,
                                              close: pd.Series) -> pd.Series:
    """Five-signal jerk composite * 2-yr drawdown depth."""
    combo = ibf_drv3_060_five_signal_jerk_composite(
        new_positions, increased_positions, closed_positions, decreased_positions,
        inst_shares, inst_value, inst_pct
    )
    dd = _drawdown_from_trailing_high(close, _TD_2Y)
    return combo * dd


# ===========================================================================
# Registry
# ===========================================================================
INSTITUTIONAL_BOTTOM_FISH_REGISTRY_3RD_DERIVATIVES = {
    "ibf_drv3_001_gross_add_3rd_diff": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_001_gross_add_3rd_diff},
    "ibf_drv3_002_net_add_3rd_diff": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_002_net_add_3rd_diff},
    "ibf_drv3_003_new_pos_3rd_diff": {"inputs": ["new_positions"], "func": ibf_drv3_003_new_pos_3rd_diff},
    "ibf_drv3_004_increased_pos_3rd_diff": {"inputs": ["increased_positions"], "func": ibf_drv3_004_increased_pos_3rd_diff},
    "ibf_drv3_005_inst_shares_3rd_diff": {"inputs": ["inst_shares"], "func": ibf_drv3_005_inst_shares_3rd_diff},
    "ibf_drv3_006_inst_value_3rd_diff": {"inputs": ["inst_value"], "func": ibf_drv3_006_inst_value_3rd_diff},
    "ibf_drv3_007_inst_pct_3rd_diff": {"inputs": ["inst_pct"], "func": ibf_drv3_007_inst_pct_3rd_diff},
    "ibf_drv3_008_add_exit_ratio_3rd_diff": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_008_add_exit_ratio_3rd_diff},
    "ibf_drv3_009_buyer_breadth_3rd_diff": {"inputs": ["new_positions", "increased_positions", "inst_holders"], "func": ibf_drv3_009_buyer_breadth_3rd_diff},
    "ibf_drv3_010_gross_add_accel_ewm_dev": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_010_gross_add_accel_ewm_dev},
    "ibf_drv3_011_net_add_accel_ewm_dev": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_011_net_add_accel_ewm_dev},
    "ibf_drv3_012_inst_shares_accel_ewm_dev": {"inputs": ["inst_shares"], "func": ibf_drv3_012_inst_shares_accel_ewm_dev},
    "ibf_drv3_013_inst_value_accel_ewm_dev": {"inputs": ["inst_value"], "func": ibf_drv3_013_inst_value_accel_ewm_dev},
    "ibf_drv3_014_inst_pct_accel_ewm_dev": {"inputs": ["inst_pct"], "func": ibf_drv3_014_inst_pct_accel_ewm_dev},
    "ibf_drv3_015_gross_add_ewm_dev_slope": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_015_gross_add_ewm_dev_slope},
    "ibf_drv3_016_new_pos_accel_zscore": {"inputs": ["new_positions"], "func": ibf_drv3_016_new_pos_accel_zscore},
    "ibf_drv3_017_gross_add_jerk_at_low": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_drv3_017_gross_add_jerk_at_low},
    "ibf_drv3_018_net_add_jerk_at_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "close"], "func": ibf_drv3_018_net_add_jerk_at_low},
    "ibf_drv3_019_inst_shares_jerk_at_low": {"inputs": ["inst_shares", "close"], "func": ibf_drv3_019_inst_shares_jerk_at_low},
    "ibf_drv3_020_inst_value_jerk_at_low": {"inputs": ["inst_value", "close"], "func": ibf_drv3_020_inst_value_jerk_at_low},
    "ibf_drv3_021_add_ratio_3rd_diff_zscore": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_021_add_ratio_3rd_diff_zscore},
    "ibf_drv3_022_buyer_breadth_jerk_zscore": {"inputs": ["new_positions", "increased_positions", "inst_holders"], "func": ibf_drv3_022_buyer_breadth_jerk_zscore},
    "ibf_drv3_023_gross_add_accel_rolling_mean": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_023_gross_add_accel_rolling_mean},
    "ibf_drv3_024_inst_pct_jerk_at_3y_low": {"inputs": ["inst_pct", "close"], "func": ibf_drv3_024_inst_pct_jerk_at_3y_low},
    "ibf_drv3_025_composite_jerk_at_3y_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_shares", "inst_value", "close"], "func": ibf_drv3_025_composite_jerk_at_3y_low},
    "ibf_drv3_026_inst_holders_3rd_diff": {"inputs": ["inst_holders"], "func": ibf_drv3_026_inst_holders_3rd_diff},
    "ibf_drv3_027_inst_pct_3rd_diff_alt": {"inputs": ["inst_pct"], "func": ibf_drv3_027_inst_pct_3rd_diff_alt},
    "ibf_drv3_028_gross_add_ewm_dev_roc": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_028_gross_add_ewm_dev_roc},
    "ibf_drv3_029_net_add_ewm_dev_roc": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_029_net_add_ewm_dev_roc},
    "ibf_drv3_030_inst_shares_ewm_dev_roc": {"inputs": ["inst_shares"], "func": ibf_drv3_030_inst_shares_ewm_dev_roc},
    "ibf_drv3_031_inst_value_ewm_dev_roc": {"inputs": ["inst_value"], "func": ibf_drv3_031_inst_value_ewm_dev_roc},
    "ibf_drv3_032_inst_pct_ewm_dev_roc": {"inputs": ["inst_pct"], "func": ibf_drv3_032_inst_pct_ewm_dev_roc},
    "ibf_drv3_033_buyer_breadth_ewm_dev_roc": {"inputs": ["new_positions", "increased_positions", "inst_holders"], "func": ibf_drv3_033_buyer_breadth_ewm_dev_roc},
    "ibf_drv3_034_add_ratio_ewm_dev_roc": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_034_add_ratio_ewm_dev_roc},
    "ibf_drv3_035_gross_add_jerk_zscore_2y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_035_gross_add_jerk_zscore_2y},
    "ibf_drv3_036_net_add_jerk_zscore_2y": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_036_net_add_jerk_zscore_2y},
    "ibf_drv3_037_inst_holders_jerk_zscore_2y": {"inputs": ["inst_holders"], "func": ibf_drv3_037_inst_holders_jerk_zscore_2y},
    "ibf_drv3_038_inst_pct_jerk_zscore_2y": {"inputs": ["inst_pct"], "func": ibf_drv3_038_inst_pct_jerk_zscore_2y},
    "ibf_drv3_039_gross_add_jerk_ewm_dev": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_039_gross_add_jerk_ewm_dev},
    "ibf_drv3_040_net_add_jerk_ewm_dev": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_040_net_add_jerk_ewm_dev},
    "ibf_drv3_041_inst_shares_jerk_ewm_dev": {"inputs": ["inst_shares"], "func": ibf_drv3_041_inst_shares_jerk_ewm_dev},
    "ibf_drv3_042_inst_value_jerk_ewm_dev": {"inputs": ["inst_value"], "func": ibf_drv3_042_inst_value_jerk_ewm_dev},
    "ibf_drv3_043_inst_pct_jerk_ewm_dev": {"inputs": ["inst_pct"], "func": ibf_drv3_043_inst_pct_jerk_ewm_dev},
    "ibf_drv3_044_gross_add_jerk_mean_2q": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_044_gross_add_jerk_mean_2q},
    "ibf_drv3_045_net_add_jerk_mean_2q": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_045_net_add_jerk_mean_2q},
    "ibf_drv3_046_inst_shares_jerk_mean_4q": {"inputs": ["inst_shares"], "func": ibf_drv3_046_inst_shares_jerk_mean_4q},
    "ibf_drv3_047_inst_value_jerk_mean_4q": {"inputs": ["inst_value"], "func": ibf_drv3_047_inst_value_jerk_mean_4q},
    "ibf_drv3_048_inst_pct_jerk_mean_4q": {"inputs": ["inst_pct"], "func": ibf_drv3_048_inst_pct_jerk_mean_4q},
    "ibf_drv3_049_gross_add_jerk_at_2y_low": {"inputs": ["new_positions", "increased_positions", "close"], "func": ibf_drv3_049_gross_add_jerk_at_2y_low},
    "ibf_drv3_050_net_add_jerk_at_2y_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "close"], "func": ibf_drv3_050_net_add_jerk_at_2y_low},
    "ibf_drv3_051_inst_holders_jerk_at_1y_low": {"inputs": ["inst_holders", "close"], "func": ibf_drv3_051_inst_holders_jerk_at_1y_low},
    "ibf_drv3_052_inst_pct_jerk_at_2y_low": {"inputs": ["inst_pct", "close"], "func": ibf_drv3_052_inst_pct_jerk_at_2y_low},
    "ibf_drv3_053_buyer_breadth_jerk_at_2y_low": {"inputs": ["new_positions", "increased_positions", "inst_holders", "close"], "func": ibf_drv3_053_buyer_breadth_jerk_at_2y_low},
    "ibf_drv3_054_add_ratio_jerk_at_2y_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "close"], "func": ibf_drv3_054_add_ratio_jerk_at_2y_low},
    "ibf_drv3_055_gross_add_jerk_slope_1y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_055_gross_add_jerk_slope_1y},
    "ibf_drv3_056_inst_shares_jerk_slope_2y": {"inputs": ["inst_shares"], "func": ibf_drv3_056_inst_shares_jerk_slope_2y},
    "ibf_drv3_057_inst_value_jerk_slope_2y": {"inputs": ["inst_value"], "func": ibf_drv3_057_inst_value_jerk_slope_2y},
    "ibf_drv3_058_shares_and_value_jerk_composite": {"inputs": ["inst_shares", "inst_value"], "func": ibf_drv3_058_shares_and_value_jerk_composite},
    "ibf_drv3_059_gross_and_net_jerk_composite": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_059_gross_and_net_jerk_composite},
    "ibf_drv3_060_five_signal_jerk_composite": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_shares", "inst_value", "inst_pct"], "func": ibf_drv3_060_five_signal_jerk_composite},
    "ibf_drv3_061_five_signal_jerk_at_1y_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_shares", "inst_value", "inst_pct", "close"], "func": ibf_drv3_061_five_signal_jerk_at_1y_low},
    "ibf_drv3_062_seven_signal_jerk_at_3y_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_holders", "inst_shares", "inst_value", "inst_pct", "close"], "func": ibf_drv3_062_seven_signal_jerk_at_3y_low},
    "ibf_drv3_063_gross_add_jerk_positive_flag": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_063_gross_add_jerk_positive_flag},
    "ibf_drv3_064_net_add_jerk_positive_flag": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_064_net_add_jerk_positive_flag},
    "ibf_drv3_065_shares_jerk_positive_flag": {"inputs": ["inst_shares"], "func": ibf_drv3_065_shares_jerk_positive_flag},
    "ibf_drv3_066_value_jerk_positive_flag": {"inputs": ["inst_value"], "func": ibf_drv3_066_value_jerk_positive_flag},
    "ibf_drv3_067_joint_jerk_positive_flag": {"inputs": ["new_positions", "increased_positions", "inst_shares", "inst_value"], "func": ibf_drv3_067_joint_jerk_positive_flag},
    "ibf_drv3_068_gross_add_jerk_positive_count_4q": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_068_gross_add_jerk_positive_count_4q},
    "ibf_drv3_069_inst_shares_jerk_positive_count_4q": {"inputs": ["inst_shares"], "func": ibf_drv3_069_inst_shares_jerk_positive_count_4q},
    "ibf_drv3_070_gross_add_jerk_std_2y": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_070_gross_add_jerk_std_2y},
    "ibf_drv3_071_inst_value_jerk_std_2y": {"inputs": ["inst_value"], "func": ibf_drv3_071_inst_value_jerk_std_2y},
    "ibf_drv3_072_gross_add_jerk_ewm_ratio": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_072_gross_add_jerk_ewm_ratio},
    "ibf_drv3_073_net_add_jerk_ewm_ratio": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions"], "func": ibf_drv3_073_net_add_jerk_ewm_ratio},
    "ibf_drv3_074_gross_add_4th_diff": {"inputs": ["new_positions", "increased_positions"], "func": ibf_drv3_074_gross_add_4th_diff},
    "ibf_drv3_075_five_signal_jerk_at_2y_low": {"inputs": ["new_positions", "increased_positions", "closed_positions", "decreased_positions", "inst_shares", "inst_value", "inst_pct", "close"], "func": ibf_drv3_075_five_signal_jerk_at_2y_low},
}
