"""
94_holder_count_dynamics — 3rd-Derivative Features (hcd_drv3_001 … hcd_drv3_075)
==================================================================================
Domain: Rate-of-change of 2nd-derivative peer-relative holder-breadth metrics.

CROSS-SECTIONAL PEER-MEDIAN INPUT CONTRACT
------------------------------------------
Every feature function receives:
  own_series   : daily pd.Series, forward-filled from quarterly SF3 13F data.
  peer_series  : daily pd.Series, SAME DatetimeIndex, sector/industry peer-median
                 computed universe-wide by the pipeline for each calendar date.

NOTE ON SPARSITY: Underlying SF3 13F data is quarterly → base series are
step-wise on a daily axis.  First differences (2nd-derivative file) are
non-zero only at quarterly boundaries; second differences (this file) are
non-zero only at boundaries of the boundary transitions.  Rolling
means/EWMs smooth over sparsity as needed.

Quarterly cadence: 1 qtr = 63 td, 1 yr = 252 td, 2 yr = 504 td, 3 yr = 756 td.

NO cross-imports — all base and 2nd-derivative logic recomputed inline.
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
# Inline helpers
# ---------------------------------------------------------------------------

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, np.nan)


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    return _safe_div(own, peer.replace(0, np.nan))


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    return np.log(_rel_ratio(own, peer).clip(lower=_EPS))


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
    return own - peer


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - mu, sd)


def _slope(s: pd.Series, w: int) -> pd.Series:
    def _sl(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xm = np.arange(len(y), dtype=float)[mask]; ym = y[mask]
        xm = xm - xm.mean()
        return np.dot(xm, ym) / (np.dot(xm, xm) + _EPS)
    return s.rolling(w, min_periods=max(4, w // 4)).apply(_sl, raw=True)


# --- 2nd-derivative recompute helpers (inline, no import) ------------------

def _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders):
    """Recompute 2nd diff of ratio QoQ (same as drv2_001)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders):
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders):
    gap = _gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_ratio_slope_qoq(inst_holders, peer_median_inst_holders):
    slp = _slope(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


def _drv2_ratio_ewm1q_qoq(inst_holders, peer_median_inst_holders):
    ewm = _ewm_mean(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def _drv2_zscore_1y_qoq(inst_holders, peer_median_inst_holders):
    zs = _zscore_rolling(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders):
    score = (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)
    return score - score.shift(_TD_QTR)


def _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct):
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def _drv2_ratio_qoq_ewm(inst_holders, peer_median_inst_holders):
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_QTR)


def _drv2_ratio_rolling_mean_1y_qoq(inst_holders, peer_median_inst_holders):
    rm = _rolling_mean(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return rm - rm.shift(_TD_QTR)


# ===========================================================================
# 3rd-Derivative Feature Functions
# ===========================================================================

def hcd_drv3_001_ratio_qoq_diff3(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of holder-breadth ratio (diff of 2nd diff)."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_002_log_rel_qoq_diff3(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_003_gap_qoq_diff3(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """3rd QoQ difference of holder-count gap (own-peer)."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_004_ratio_slope_qoq_diff2(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 1-year ratio slope (3rd deriv)."""
    d2 = _drv2_ratio_slope_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_005_ratio_ewm_qoq_diff2(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of EWM(1q) ratio."""
    d2 = _drv2_ratio_ewm1q_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_006_zscore_qoq_diff2(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change in 1-year z-score of ratio."""
    d2 = _drv2_zscore_1y_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_007_collapse_score_qoq_diff2(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change in collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_008_inst_pct_ratio_qoq_diff3(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of inst_pct ratio vs peer."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_009_ratio_qoq_diff2_ewm(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ difference of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _ewm_mean(d2, _TD_QTR)


def hcd_drv3_010_log_rel_qoq_diff2_ewm(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ difference of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _ewm_mean(d2, _TD_QTR)


def hcd_drv3_011_ratio_qoq_diff2_rolling_mean_1y(inst_holders: pd.Series,
                                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of 2nd QoQ difference of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _rolling_mean(d2, _TD_YEAR)


def hcd_drv3_012_ratio_qoq_diff2_zscore_1y(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 2nd QoQ difference of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(d2, _TD_YEAR)


def hcd_drv3_013_collapse_score_qoq_diff2_ewm(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ diff of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_014_ratio_slope_qoq_diff2_ewm(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ diff of 1-year ratio slope."""
    d2 = _drv2_ratio_slope_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_015_ratio_qoq_ewm_diff2(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change of EWM(1q) ratio QoQ (3rd layer)."""
    d2 = _drv2_ratio_ewm1q_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_016_ratio_qoq_diff2_slope_1y(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of 2nd QoQ difference series of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _slope(d2, _TD_YEAR)


def hcd_drv3_017_log_rel_qoq_diff2_slope_1y(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of 2nd QoQ difference of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _slope(d2, _TD_YEAR)


def hcd_drv3_018_gap_qoq_diff2_ewm(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ diff of holder-count gap."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _ewm_mean(d2, _TD_QTR)


def hcd_drv3_019_zscore_qoq_diff2_ewm(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ diff of 1-year z-score of ratio."""
    d2 = _drv2_zscore_1y_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_020_ratio_rolling_mean_qoq_diff2(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ diff of the QoQ-change in 1-year rolling mean of ratio."""
    d2 = _drv2_ratio_rolling_mean_1y_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_021_ratio_qoq_diff2_abs_ewm(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of |2nd QoQ diff of ratio| (absolute acceleration magnitude)."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _ewm_mean(d2.abs(), _TD_QTR)


def hcd_drv3_022_collapse_score_qoq_diff2_zscore(inst_holders: pd.Series,
                                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 2nd QoQ diff of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_YEAR)


def hcd_drv3_023_log_rel_qoq_diff2_zscore(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 2nd QoQ diff of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(d2, _TD_YEAR)


def hcd_drv3_024_ratio_qoq_diff2_rolling_min_1y(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of 2nd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    return d2.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).min()


def hcd_drv3_025_inst_pct_ratio_qoq_diff3_ewm(inst_pct: pd.Series,
                                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM(1q) of 3rd QoQ diff of inst_pct ratio vs peer."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


# ===========================================================================
# Additional inline helpers for 3rd-derivative features 026-075
# ===========================================================================

def _drv2_log_rel_qoq_ewm(inst_holders, peer_median_inst_holders):
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_QTR)


def _drv2_ratio_qoq_rolling_mean_1y(inst_holders, peer_median_inst_holders):
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_YEAR)


def _drv2_inst_pct_ratio_slope_qoq(inst_pct, peer_median_inst_pct):
    slp = _slope(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


def _drv2_log_rel_slope_qoq(inst_holders, peer_median_inst_holders):
    slp = _slope(_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


def _drv2_ratio_yoy_diff2(inst_holders, peer_median_inst_holders):
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def _drv2_inst_pct_gap_qoq_diff2(inst_pct, peer_median_inst_pct):
    gap = _gap(inst_pct, peer_median_inst_pct)
    d1 = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


# ===========================================================================
# 3rd-Derivative Feature Functions 026 – 075
# ===========================================================================

# --- 3rd QoQ diff on additional base series ---------------------------------

def hcd_drv3_026_log_rel_yoy_diff3(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """3rd YoY difference of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_YEAR)
    d2 = d1 - d1.shift(_TD_YEAR)
    return d2 - d2.shift(_TD_YEAR)


def hcd_drv3_027_ratio_yoy_diff3(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """3rd YoY difference of holder-breadth ratio."""
    d2 = _drv2_ratio_yoy_diff2(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_YEAR)


def hcd_drv3_028_inst_pct_ratio_qoq_diff3(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of inst_pct ratio vs peer (distinct from drv3_008 which uses ewm)."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_029_inst_pct_gap_qoq_diff3(inst_pct: pd.Series,
                                          peer_median_inst_pct: pd.Series) -> pd.Series:
    """3rd QoQ difference of inst_pct gap vs peer."""
    d2 = _drv2_inst_pct_gap_qoq_diff2(inst_pct, peer_median_inst_pct)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_030_log_rel_slope_qoq_diff2(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 1-year log-rel slope (3rd deriv)."""
    d2 = _drv2_log_rel_slope_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


# --- EWM of 3rd-diff variants -----------------------------------------------

def hcd_drv3_031_ratio_qoq_diff3_ewm_2q(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(2q) of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_2Q)


def hcd_drv3_032_log_rel_qoq_diff3_ewm_1q(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 3rd QoQ diff of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_033_gap_qoq_diff3_ewm_1q(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of 3rd QoQ diff of holder-count gap."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_034_inst_pct_ratio_qoq_diff3_rolling_mean_1y(inst_pct: pd.Series,
                                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling mean of 3rd QoQ diff of inst_pct ratio vs peer."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


def hcd_drv3_035_collapse_score_qoq_diff3_rolling_mean_1y(inst_holders: pd.Series,
                                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of 3rd QoQ diff of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


# --- z-score of 3rd-diff series --------------------------------------------

def hcd_drv3_036_ratio_qoq_diff3_zscore_1y(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_YEAR)


def hcd_drv3_037_log_rel_qoq_diff3_zscore_1y(inst_holders: pd.Series,
                                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 3rd QoQ diff of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_YEAR)


def hcd_drv3_038_gap_qoq_diff3_zscore_1y(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 3rd QoQ diff of holder-count gap."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_YEAR)


def hcd_drv3_039_collapse_score_qoq_diff3_zscore_1y(inst_holders: pd.Series,
                                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of 3rd QoQ diff of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_YEAR)


def hcd_drv3_040_inst_pct_ratio_qoq_diff3_zscore_1y(inst_pct: pd.Series,
                                                      peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year z-score of 3rd QoQ diff of inst_pct ratio vs peer."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_YEAR)


# --- QoQ change of smoothed 2nd-derivative (slope / ewm of d2) -------------

def hcd_drv3_041_ratio_qoq_diff2_ewm_qoq(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of 2nd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    ewm = _ewm_mean(d2, _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv3_042_log_rel_qoq_diff2_ewm_qoq(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of 2nd QoQ diff of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    ewm = _ewm_mean(d2, _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv3_043_gap_qoq_diff2_ewm_qoq(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of 2nd QoQ diff of holder-count gap."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    ewm = _ewm_mean(d2, _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv3_044_ratio_qoq_diff2_rolling_mean_1y_qoq(inst_holders: pd.Series,
                                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year rolling mean of 2nd QoQ diff of ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    rm = _rolling_mean(d2, _TD_YEAR)
    return rm - rm.shift(_TD_QTR)


def hcd_drv3_045_ratio_slope_1y_qoq_diff2_rolling_mean(inst_holders: pd.Series,
                                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of 2nd QoQ diff of 1-year ratio slope."""
    d2 = _drv2_ratio_slope_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


# --- slope of 3rd-diff series -----------------------------------------------

def hcd_drv3_046_ratio_qoq_diff3_slope_1y(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of 3rd QoQ diff series of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _slope(d3, _TD_YEAR)


def hcd_drv3_047_log_rel_qoq_diff3_slope_1y(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of 3rd QoQ diff series of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _slope(d3, _TD_YEAR)


def hcd_drv3_048_collapse_score_qoq_diff3_slope_1y(inst_holders: pd.Series,
                                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of 3rd QoQ diff series of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _slope(d3, _TD_YEAR)


def hcd_drv3_049_inst_pct_ratio_qoq_diff3_slope_1y(inst_pct: pd.Series,
                                                     peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year OLS slope of 3rd QoQ diff series of inst_pct ratio vs peer."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _slope(d3, _TD_YEAR)


def hcd_drv3_050_ratio_slope_qoq_diff2_slope_1y(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of 2nd QoQ diff of 1-year ratio slope."""
    d2 = _drv2_ratio_slope_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _slope(d3, _TD_YEAR)


# --- QoQ change of 2nd-deriv EWM-variants (3rd layer) ----------------------

def hcd_drv3_051_ratio_qoq_ewm_qoq_diff2(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change of EWM(2q) ratio QoQ."""
    d2 = _drv2_ratio_ewm1q_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_2Q)


def hcd_drv3_052_log_rel_ewm_qoq_diff2(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change of EWM(1q) of log-relative QoQ."""
    d2 = _drv2_log_rel_qoq_ewm(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_053_ratio_qoq_rolling_mean_1y_qoq_diff2(inst_holders: pd.Series,
                                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change of 1y rolling mean of ratio QoQ."""
    d2 = _drv2_ratio_qoq_rolling_mean_1y(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_054_inst_pct_ratio_slope_qoq_diff2(inst_pct: pd.Series,
                                                  peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change of 1-year inst_pct ratio slope."""
    d2 = _drv2_inst_pct_ratio_slope_qoq(inst_pct, peer_median_inst_pct)
    return d2 - d2.shift(_TD_QTR)


def hcd_drv3_055_log_rel_slope_qoq_diff2(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change of the QoQ-change of 1-year log-rel slope."""
    d2 = _drv2_log_rel_slope_qoq(inst_holders, peer_median_inst_holders)
    return d2 - d2.shift(_TD_QTR)


# --- absolute value features on 3rd diff ------------------------------------

def hcd_drv3_056_ratio_qoq_diff3_abs_ewm_1q(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of |3rd QoQ diff of ratio| (convexity magnitude)."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = (d2 - d2.shift(_TD_QTR)).abs()
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_057_log_rel_qoq_diff3_abs_rolling_mean_1y(inst_holders: pd.Series,
                                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of |3rd QoQ diff of log-relative holder breadth|."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = (d2 - d2.shift(_TD_QTR)).abs()
    return _rolling_mean(d3, _TD_YEAR)


def hcd_drv3_058_collapse_score_qoq_diff3_abs_ewm_1q(inst_holders: pd.Series,
                                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of |3rd QoQ diff of collapse score|."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = (d2 - d2.shift(_TD_QTR)).abs()
    return _ewm_mean(d3, _TD_QTR)


def hcd_drv3_059_gap_qoq_diff3_abs_rolling_mean_1y(inst_holders: pd.Series,
                                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of |3rd QoQ diff of holder-count gap|."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = (d2 - d2.shift(_TD_QTR)).abs()
    return _rolling_mean(d3, _TD_YEAR)


def hcd_drv3_060_ratio_qoq_diff3_sign(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """Sign of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return np.sign(d3)


# --- rolling min / max of 3rd diff ------------------------------------------

def hcd_drv3_061_ratio_qoq_diff3_rolling_min_1y(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).min()


def hcd_drv3_062_ratio_qoq_diff3_rolling_max_1y(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling maximum of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).max()


def hcd_drv3_063_log_rel_qoq_diff3_rolling_min_1y(inst_holders: pd.Series,
                                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of 3rd QoQ diff of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).min()


def hcd_drv3_064_collapse_score_qoq_diff2_rolling_min_1y(inst_holders: pd.Series,
                                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of 2nd QoQ diff of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).min()


def hcd_drv3_065_gap_qoq_diff3_rolling_min_1y(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of 3rd QoQ diff of holder-count gap."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return d3.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).min()


# --- positive-fraction of 3rd diff ------------------------------------------

def hcd_drv3_066_ratio_qoq_diff3_positive_frac_1y(inst_holders: pd.Series,
                                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 1y where 3rd QoQ diff of ratio was positive."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean((d3 > 0).astype(float), _TD_YEAR)


def hcd_drv3_067_log_rel_qoq_diff3_positive_frac_1y(inst_holders: pd.Series,
                                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 1y where 3rd QoQ diff of log-rel was positive."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean((d3 > 0).astype(float), _TD_YEAR)


def hcd_drv3_068_collapse_qoq_diff3_positive_frac_1y(inst_holders: pd.Series,
                                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 1y where 3rd QoQ diff of collapse score was positive."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean((d3 > 0).astype(float), _TD_YEAR)


def hcd_drv3_069_inst_pct_ratio_qoq_diff3_positive_frac_1y(inst_pct: pd.Series,
                                                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """Fraction of days in past 1y where 3rd QoQ diff of inst_pct ratio was positive."""
    d2 = _drv2_inst_pct_ratio_qoq_diff2(inst_pct, peer_median_inst_pct)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean((d3 > 0).astype(float), _TD_YEAR)


def hcd_drv3_070_gap_qoq_diff3_positive_frac_1y(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 1y where 3rd QoQ diff of holder-count gap was positive."""
    d2 = _drv2_gap_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean((d3 > 0).astype(float), _TD_YEAR)


# --- composite/mixed 3rd-deriv signals --------------------------------------

def hcd_drv3_071_ratio_and_log_rel_diff3_sum(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """Sum of 3rd QoQ diffs of ratio and log-relative (composite 3rd-deriv)."""
    d2r = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d2l = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3r = d2r - d2r.shift(_TD_QTR)
    d3l = d2l - d2l.shift(_TD_QTR)
    return d3r + d3l


def hcd_drv3_072_ratio_qoq_diff3_zscore_2y(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year z-score of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def hcd_drv3_073_log_rel_qoq_diff3_zscore_2y(inst_holders: pd.Series,
                                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year z-score of 3rd QoQ diff of log-relative holder breadth."""
    d2 = _drv2_log_rel_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(d3, _TD_2Y)


def hcd_drv3_074_ratio_qoq_diff3_ewm_1q_zscore_1y(inst_holders: pd.Series,
                                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of EWM(1q) of 3rd QoQ diff of holder-breadth ratio."""
    d2 = _drv2_ratio_qoq_diff2(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _zscore_rolling(_ewm_mean(d3, _TD_QTR), _TD_YEAR)


def hcd_drv3_075_collapse_score_qoq_diff2_rolling_mean_1y(inst_holders: pd.Series,
                                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of 2nd QoQ diff of collapse score."""
    d2 = _drv2_collapse_score_qoq(inst_holders, peer_median_inst_holders)
    d3 = d2 - d2.shift(_TD_QTR)
    return _rolling_mean(d3, _TD_YEAR)


# ===========================================================================
# Registry
# ===========================================================================
HOLDER_COUNT_DYNAMICS_REGISTRY_3RD_DERIVATIVES = {
    "hcd_drv3_001_ratio_qoq_diff3": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_001_ratio_qoq_diff3,
    },
    "hcd_drv3_002_log_rel_qoq_diff3": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_002_log_rel_qoq_diff3,
    },
    "hcd_drv3_003_gap_qoq_diff3": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_003_gap_qoq_diff3,
    },
    "hcd_drv3_004_ratio_slope_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_004_ratio_slope_qoq_diff2,
    },
    "hcd_drv3_005_ratio_ewm_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_005_ratio_ewm_qoq_diff2,
    },
    "hcd_drv3_006_zscore_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_006_zscore_qoq_diff2,
    },
    "hcd_drv3_007_collapse_score_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_007_collapse_score_qoq_diff2,
    },
    "hcd_drv3_008_inst_pct_ratio_qoq_diff3": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_008_inst_pct_ratio_qoq_diff3,
    },
    "hcd_drv3_009_ratio_qoq_diff2_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_009_ratio_qoq_diff2_ewm,
    },
    "hcd_drv3_010_log_rel_qoq_diff2_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_010_log_rel_qoq_diff2_ewm,
    },
    "hcd_drv3_011_ratio_qoq_diff2_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_011_ratio_qoq_diff2_rolling_mean_1y,
    },
    "hcd_drv3_012_ratio_qoq_diff2_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_012_ratio_qoq_diff2_zscore_1y,
    },
    "hcd_drv3_013_collapse_score_qoq_diff2_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_013_collapse_score_qoq_diff2_ewm,
    },
    "hcd_drv3_014_ratio_slope_qoq_diff2_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_014_ratio_slope_qoq_diff2_ewm,
    },
    "hcd_drv3_015_ratio_qoq_ewm_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_015_ratio_qoq_ewm_diff2,
    },
    "hcd_drv3_016_ratio_qoq_diff2_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_016_ratio_qoq_diff2_slope_1y,
    },
    "hcd_drv3_017_log_rel_qoq_diff2_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_017_log_rel_qoq_diff2_slope_1y,
    },
    "hcd_drv3_018_gap_qoq_diff2_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_018_gap_qoq_diff2_ewm,
    },
    "hcd_drv3_019_zscore_qoq_diff2_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_019_zscore_qoq_diff2_ewm,
    },
    "hcd_drv3_020_ratio_rolling_mean_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_020_ratio_rolling_mean_qoq_diff2,
    },
    "hcd_drv3_021_ratio_qoq_diff2_abs_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_021_ratio_qoq_diff2_abs_ewm,
    },
    "hcd_drv3_022_collapse_score_qoq_diff2_zscore": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_022_collapse_score_qoq_diff2_zscore,
    },
    "hcd_drv3_023_log_rel_qoq_diff2_zscore": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_023_log_rel_qoq_diff2_zscore,
    },
    "hcd_drv3_024_ratio_qoq_diff2_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_024_ratio_qoq_diff2_rolling_min_1y,
    },
    "hcd_drv3_025_inst_pct_ratio_qoq_diff3_ewm": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_025_inst_pct_ratio_qoq_diff3_ewm,
    },
    "hcd_drv3_026_log_rel_yoy_diff3": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_026_log_rel_yoy_diff3,
    },
    "hcd_drv3_027_ratio_yoy_diff3": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_027_ratio_yoy_diff3,
    },
    "hcd_drv3_028_inst_pct_ratio_qoq_diff3": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_028_inst_pct_ratio_qoq_diff3,
    },
    "hcd_drv3_029_inst_pct_gap_qoq_diff3": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_029_inst_pct_gap_qoq_diff3,
    },
    "hcd_drv3_030_log_rel_slope_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_030_log_rel_slope_qoq_diff2,
    },
    "hcd_drv3_031_ratio_qoq_diff3_ewm_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_031_ratio_qoq_diff3_ewm_2q,
    },
    "hcd_drv3_032_log_rel_qoq_diff3_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_032_log_rel_qoq_diff3_ewm_1q,
    },
    "hcd_drv3_033_gap_qoq_diff3_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_033_gap_qoq_diff3_ewm_1q,
    },
    "hcd_drv3_034_inst_pct_ratio_qoq_diff3_rolling_mean_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_034_inst_pct_ratio_qoq_diff3_rolling_mean_1y,
    },
    "hcd_drv3_035_collapse_score_qoq_diff3_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_035_collapse_score_qoq_diff3_rolling_mean_1y,
    },
    "hcd_drv3_036_ratio_qoq_diff3_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_036_ratio_qoq_diff3_zscore_1y,
    },
    "hcd_drv3_037_log_rel_qoq_diff3_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_037_log_rel_qoq_diff3_zscore_1y,
    },
    "hcd_drv3_038_gap_qoq_diff3_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_038_gap_qoq_diff3_zscore_1y,
    },
    "hcd_drv3_039_collapse_score_qoq_diff3_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_039_collapse_score_qoq_diff3_zscore_1y,
    },
    "hcd_drv3_040_inst_pct_ratio_qoq_diff3_zscore_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_040_inst_pct_ratio_qoq_diff3_zscore_1y,
    },
    "hcd_drv3_041_ratio_qoq_diff2_ewm_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_041_ratio_qoq_diff2_ewm_qoq,
    },
    "hcd_drv3_042_log_rel_qoq_diff2_ewm_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_042_log_rel_qoq_diff2_ewm_qoq,
    },
    "hcd_drv3_043_gap_qoq_diff2_ewm_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_043_gap_qoq_diff2_ewm_qoq,
    },
    "hcd_drv3_044_ratio_qoq_diff2_rolling_mean_1y_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_044_ratio_qoq_diff2_rolling_mean_1y_qoq,
    },
    "hcd_drv3_045_ratio_slope_1y_qoq_diff2_rolling_mean": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_045_ratio_slope_1y_qoq_diff2_rolling_mean,
    },
    "hcd_drv3_046_ratio_qoq_diff3_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_046_ratio_qoq_diff3_slope_1y,
    },
    "hcd_drv3_047_log_rel_qoq_diff3_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_047_log_rel_qoq_diff3_slope_1y,
    },
    "hcd_drv3_048_collapse_score_qoq_diff3_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_048_collapse_score_qoq_diff3_slope_1y,
    },
    "hcd_drv3_049_inst_pct_ratio_qoq_diff3_slope_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_049_inst_pct_ratio_qoq_diff3_slope_1y,
    },
    "hcd_drv3_050_ratio_slope_qoq_diff2_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_050_ratio_slope_qoq_diff2_slope_1y,
    },
    "hcd_drv3_051_ratio_qoq_ewm_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_051_ratio_qoq_ewm_qoq_diff2,
    },
    "hcd_drv3_052_log_rel_ewm_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_052_log_rel_ewm_qoq_diff2,
    },
    "hcd_drv3_053_ratio_qoq_rolling_mean_1y_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_053_ratio_qoq_rolling_mean_1y_qoq_diff2,
    },
    "hcd_drv3_054_inst_pct_ratio_slope_qoq_diff2": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_054_inst_pct_ratio_slope_qoq_diff2,
    },
    "hcd_drv3_055_log_rel_slope_qoq_diff2": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_055_log_rel_slope_qoq_diff2,
    },
    "hcd_drv3_056_ratio_qoq_diff3_abs_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_056_ratio_qoq_diff3_abs_ewm_1q,
    },
    "hcd_drv3_057_log_rel_qoq_diff3_abs_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_057_log_rel_qoq_diff3_abs_rolling_mean_1y,
    },
    "hcd_drv3_058_collapse_score_qoq_diff3_abs_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_058_collapse_score_qoq_diff3_abs_ewm_1q,
    },
    "hcd_drv3_059_gap_qoq_diff3_abs_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_059_gap_qoq_diff3_abs_rolling_mean_1y,
    },
    "hcd_drv3_060_ratio_qoq_diff3_sign": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_060_ratio_qoq_diff3_sign,
    },
    "hcd_drv3_061_ratio_qoq_diff3_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_061_ratio_qoq_diff3_rolling_min_1y,
    },
    "hcd_drv3_062_ratio_qoq_diff3_rolling_max_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_062_ratio_qoq_diff3_rolling_max_1y,
    },
    "hcd_drv3_063_log_rel_qoq_diff3_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_063_log_rel_qoq_diff3_rolling_min_1y,
    },
    "hcd_drv3_064_collapse_score_qoq_diff2_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_064_collapse_score_qoq_diff2_rolling_min_1y,
    },
    "hcd_drv3_065_gap_qoq_diff3_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_065_gap_qoq_diff3_rolling_min_1y,
    },
    "hcd_drv3_066_ratio_qoq_diff3_positive_frac_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_066_ratio_qoq_diff3_positive_frac_1y,
    },
    "hcd_drv3_067_log_rel_qoq_diff3_positive_frac_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_067_log_rel_qoq_diff3_positive_frac_1y,
    },
    "hcd_drv3_068_collapse_qoq_diff3_positive_frac_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_068_collapse_qoq_diff3_positive_frac_1y,
    },
    "hcd_drv3_069_inst_pct_ratio_qoq_diff3_positive_frac_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv3_069_inst_pct_ratio_qoq_diff3_positive_frac_1y,
    },
    "hcd_drv3_070_gap_qoq_diff3_positive_frac_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_070_gap_qoq_diff3_positive_frac_1y,
    },
    "hcd_drv3_071_ratio_and_log_rel_diff3_sum": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_071_ratio_and_log_rel_diff3_sum,
    },
    "hcd_drv3_072_ratio_qoq_diff3_zscore_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_072_ratio_qoq_diff3_zscore_2y,
    },
    "hcd_drv3_073_log_rel_qoq_diff3_zscore_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_073_log_rel_qoq_diff3_zscore_2y,
    },
    "hcd_drv3_074_ratio_qoq_diff3_ewm_1q_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_074_ratio_qoq_diff3_ewm_1q_zscore_1y,
    },
    "hcd_drv3_075_collapse_score_qoq_diff2_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv3_075_collapse_score_qoq_diff2_rolling_mean_1y,
    },
}
