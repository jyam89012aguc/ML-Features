"""
94_holder_count_dynamics — 2nd-Derivative Features (hcd_drv2_001 … hcd_drv2_075)
==================================================================================
Domain: Rate-of-change of base peer-relative holder-breadth metrics.

CROSS-SECTIONAL PEER-MEDIAN INPUT CONTRACT
------------------------------------------
Every feature function receives:
  own_series   : daily pd.Series, forward-filled from quarterly SF3 13F data.
  peer_series  : daily pd.Series, SAME DatetimeIndex, sector/industry peer-median
                 of the same metric, computed universe-wide by the pipeline.

NOTE ON SPARSITY: Because underlying SF3 13F data is quarterly, all relative
series (ratios, gaps, log-relatives) are step-wise on a daily axis — values
change only once per quarter.  Derivative (diff) series will therefore be
SPARSE: non-zero only at quarterly step boundaries, zero elsewhere.  This is
expected and correct.  Rolling means / EWMs smooth over the sparsity.

Quarterly cadence: 1 qtr = 63 td, 1 yr = 252 td, 2 yr = 504 td, 3 yr = 756 td.

NO cross-imports from base files — all base-feature logic is recomputed inline
via self-contained helpers defined in this file.
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
# Inline helpers (self-contained, no cross-imports)
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
    """OLS slope of s over rolling window w."""
    def _sl(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xm = np.arange(len(y), dtype=float)[mask]; ym = y[mask]
        xm = xm - xm.mean()
        return np.dot(xm, ym) / (np.dot(xm, xm) + _EPS)
    return s.rolling(w, min_periods=max(4, w // 4)).apply(_sl, raw=True)


# --- Base series recompute helpers -----------------------------------------

def _base_ratio(inst_holders, peer_median_inst_holders):
    return _rel_ratio(inst_holders, peer_median_inst_holders)


def _base_log_rel(inst_holders, peer_median_inst_holders):
    return _log_rel(inst_holders, peer_median_inst_holders)


def _base_gap(inst_holders, peer_median_inst_holders):
    return _gap(inst_holders, peer_median_inst_holders)


def _base_inst_pct_ratio(inst_pct, peer_median_inst_pct):
    return _rel_ratio(inst_pct, peer_median_inst_pct)


def _base_inst_pct_gap(inst_pct, peer_median_inst_pct):
    return _gap(inst_pct, peer_median_inst_pct)


def _base_collapse_score(inst_holders, peer_median_inst_holders):
    return (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)


# ===========================================================================
# 2nd-Derivative Feature Functions
# ===========================================================================

def hcd_drv2_001_ratio_qoq_diff_of_qoq(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of holder-breadth ratio (2nd diff)."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def hcd_drv2_002_ratio_yoy_diff_of_yoy(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in the YoY-change of holder-breadth ratio (2nd diff)."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def hcd_drv2_003_log_rel_qoq_diff_of_qoq(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ 2nd difference of log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def hcd_drv2_004_gap_qoq_diff_of_qoq(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ 2nd difference of holder-count gap (own-peer)."""
    gap = _base_gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def hcd_drv2_005_inst_pct_ratio_qoq_diff2(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ 2nd difference of inst_pct ratio vs peer."""
    ratio = _base_inst_pct_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def hcd_drv2_006_ratio_slope_qoq_change(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 1-year OLS slope of holder-breadth ratio."""
    slp = _slope(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


def hcd_drv2_007_ratio_slope_yoy_change(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in the 1-year OLS slope of holder-breadth ratio."""
    slp = _slope(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return slp - slp.shift(_TD_YEAR)


def hcd_drv2_008_log_rel_slope_qoq_change(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year OLS slope of log-relative holder breadth."""
    slp = _slope(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


def hcd_drv2_009_ratio_ewm1q_qoq_change(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of holder-breadth ratio."""
    ewm = _ewm_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv2_010_ratio_ewm1y_qoq_change(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1y) of holder-breadth ratio."""
    ewm = _ewm_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv2_011_ratio_ewm1q_yoy_change(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in EWM(1q) of holder-breadth ratio."""
    ewm = _ewm_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_YEAR)


def hcd_drv2_012_zscore_1y_qoq_change(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year rolling z-score of holder-breadth ratio."""
    zs = _zscore_rolling(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def hcd_drv2_013_zscore_2y_qoq_change(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 2-year rolling z-score of holder-breadth ratio."""
    zs = _zscore_rolling(_base_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)
    return zs - zs.shift(_TD_QTR)


def hcd_drv2_014_log_rel_zscore_1y_qoq_change(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year z-score of log-relative holder breadth."""
    zs = _zscore_rolling(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def hcd_drv2_015_collapse_score_qoq_change(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in relative-breadth collapse score (-log_rel clipped)."""
    score = _base_collapse_score(inst_holders, peer_median_inst_holders)
    return score - score.shift(_TD_QTR)


def hcd_drv2_016_collapse_score_yoy_change(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in relative-breadth collapse score."""
    score = _base_collapse_score(inst_holders, peer_median_inst_holders)
    return score - score.shift(_TD_YEAR)


def hcd_drv2_017_collapse_score_ewm_qoq(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of collapse score."""
    ewm = _ewm_mean(_base_collapse_score(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv2_018_inst_pct_gap_qoq_diff2(inst_pct: pd.Series,
                                          peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ 2nd difference of inst_pct gap (own-peer)."""
    gap = _base_inst_pct_gap(inst_pct, peer_median_inst_pct)
    d1 = gap - gap.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def hcd_drv2_019_ratio_qoq_rolling_mean_1y(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of the QoQ-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_YEAR)


def hcd_drv2_020_ratio_qoq_ewm(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of QoQ-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_QTR)


def hcd_drv2_021_log_rel_qoq_ewm(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of QoQ-change in log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_QTR)


def hcd_drv2_022_ratio_qoq_zscore_1y(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of the QoQ-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _zscore_rolling(d1, _TD_YEAR)


def hcd_drv2_023_gap_slope_qoq_change(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year OLS slope of holder-count gap."""
    slp = _slope(_base_gap(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


def hcd_drv2_024_ratio_rolling_mean_1y_qoq_change(inst_holders: pd.Series,
                                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year rolling mean of holder-breadth ratio."""
    rm = _rolling_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return rm - rm.shift(_TD_QTR)


def hcd_drv2_025_inst_pct_ratio_slope_qoq(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in 1-year OLS slope of inst_pct ratio vs peer."""
    slp = _slope(_base_inst_pct_ratio(inst_pct, peer_median_inst_pct), _TD_YEAR)
    return slp - slp.shift(_TD_QTR)


# ===========================================================================
# 2nd-Derivative Feature Functions 026 – 075
# ===========================================================================

# --- Additional QoQ 2nd differences -----------------------------------------

def hcd_drv2_026_ratio_2q_diff_of_qoq(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Half-year (2Q) change in the QoQ-change of holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_2Q)


def hcd_drv2_027_log_rel_yoy_diff_of_yoy(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY 2nd difference of log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def hcd_drv2_028_gap_yoy_diff_of_yoy(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY 2nd difference of holder-count gap."""
    gap = _base_gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def hcd_drv2_029_inst_pct_gap_yoy_diff2(inst_pct: pd.Series,
                                          peer_median_inst_pct: pd.Series) -> pd.Series:
    """YoY 2nd difference of inst_pct gap vs peer."""
    gap = _base_inst_pct_gap(inst_pct, peer_median_inst_pct)
    d1 = gap - gap.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


def hcd_drv2_030_inst_pct_ratio_yoy_diff2(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """YoY 2nd difference of inst_pct ratio vs peer."""
    ratio = _base_inst_pct_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_YEAR)
    return d1 - d1.shift(_TD_YEAR)


# --- Smoothed 1st-derivative (QoQ diff) with various windows ---------------

def hcd_drv2_031_ratio_qoq_rolling_mean_2y(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling mean of the QoQ-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_2Y)


def hcd_drv2_032_log_rel_qoq_rolling_mean_1y(inst_holders: pd.Series,
                                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of QoQ-change in log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_YEAR)


def hcd_drv2_033_gap_qoq_rolling_mean_1y(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of QoQ-change in holder-count gap."""
    gap = _base_gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_YEAR)


def hcd_drv2_034_inst_pct_ratio_qoq_rolling_mean_1y(inst_pct: pd.Series,
                                                       peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling mean of QoQ-change in inst_pct ratio vs peer."""
    ratio = _base_inst_pct_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_YEAR)


def hcd_drv2_035_collapse_score_qoq_rolling_mean_1y(inst_holders: pd.Series,
                                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of QoQ-change in collapse score."""
    score = _base_collapse_score(inst_holders, peer_median_inst_holders)
    d1 = score - score.shift(_TD_QTR)
    return _rolling_mean(d1, _TD_YEAR)


# --- EWM of 1st-derivative with longer spans --------------------------------

def hcd_drv2_036_ratio_qoq_ewm_2q(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(2q) of QoQ-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_2Q)


def hcd_drv2_037_log_rel_qoq_ewm_2q(inst_holders: pd.Series,
                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(2q) of QoQ-change in log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_2Q)


def hcd_drv2_038_gap_qoq_ewm_1q(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of QoQ-change in holder-count gap."""
    gap = _base_gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_QTR)


def hcd_drv2_039_inst_pct_ratio_qoq_ewm_1q(inst_pct: pd.Series,
                                             peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM(1q) of QoQ-change in inst_pct ratio vs peer."""
    ratio = _base_inst_pct_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_QTR)


def hcd_drv2_040_collapse_score_qoq_ewm_2q(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(2q) of QoQ-change in collapse score."""
    score = _base_collapse_score(inst_holders, peer_median_inst_holders)
    d1 = score - score.shift(_TD_QTR)
    return _ewm_mean(d1, _TD_2Q)


# --- z-score of 1st-derivative series ---------------------------------------

def hcd_drv2_041_log_rel_qoq_zscore_1y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of QoQ-change in log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return _zscore_rolling(d1, _TD_YEAR)


def hcd_drv2_042_gap_qoq_zscore_1y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of QoQ-change in holder-count gap."""
    gap = _base_gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_QTR)
    return _zscore_rolling(d1, _TD_YEAR)


def hcd_drv2_043_inst_pct_ratio_qoq_zscore_1y(inst_pct: pd.Series,
                                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year z-score of QoQ-change in inst_pct ratio vs peer."""
    ratio = _base_inst_pct_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _zscore_rolling(d1, _TD_YEAR)


def hcd_drv2_044_collapse_score_qoq_zscore_1y(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of QoQ-change in collapse score."""
    score = _base_collapse_score(inst_holders, peer_median_inst_holders)
    d1 = score - score.shift(_TD_QTR)
    return _zscore_rolling(d1, _TD_YEAR)


def hcd_drv2_045_ratio_yoy_change_zscore_1y(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of YoY-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_YEAR)
    return _zscore_rolling(d1, _TD_YEAR)


# --- slope-of-derivative features -------------------------------------------

def hcd_drv2_046_ratio_qoq_slope_1y(inst_holders: pd.Series,
                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of QoQ-change series of holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _slope(d1, _TD_YEAR)


def hcd_drv2_047_log_rel_qoq_slope_1y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year OLS slope of QoQ-change series of log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    return _slope(d1, _TD_YEAR)


def hcd_drv2_048_gap_slope_2y(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year OLS slope of holder-count gap."""
    return _slope(_base_gap(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_drv2_049_log_rel_slope_2y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year OLS slope of log-relative holder breadth."""
    return _slope(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_drv2_050_ratio_slope_2y_qoq_change(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 2-year OLS slope of holder-breadth ratio."""
    slp = _slope(_base_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)
    return slp - slp.shift(_TD_QTR)


# --- EWM changes over YoY window --------------------------------------------

def hcd_drv2_051_ratio_ewm1q_yoy_diff(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in EWM(1q) of holder-breadth ratio (long-horizon momentum of trend)."""
    ewm = _ewm_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_YEAR)


def hcd_drv2_052_ratio_ewm2q_qoq_change(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(2q) of holder-breadth ratio."""
    ewm = _ewm_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_2Q)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv2_053_log_rel_ewm1q_qoq_change(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of log-relative holder breadth."""
    ewm = _ewm_mean(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv2_054_inst_pct_ratio_ewm1q_qoq(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in EWM(1q) of inst_pct ratio vs peer."""
    ewm = _ewm_mean(_base_inst_pct_ratio(inst_pct, peer_median_inst_pct), _TD_QTR)
    return ewm - ewm.shift(_TD_QTR)


def hcd_drv2_055_collapse_score_ewm1q_yoy(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in EWM(1q) of collapse score."""
    ewm = _ewm_mean(_base_collapse_score(inst_holders, peer_median_inst_holders), _TD_QTR)
    return ewm - ewm.shift(_TD_YEAR)


# --- rolling mean changes (QoQ and YoY) ------------------------------------

def hcd_drv2_056_ratio_rolling_mean_2y_qoq_change(inst_holders: pd.Series,
                                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 2-year rolling mean of holder-breadth ratio."""
    rm = _rolling_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)
    return rm - rm.shift(_TD_QTR)


def hcd_drv2_057_log_rel_rolling_mean_1y_qoq_change(inst_holders: pd.Series,
                                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year rolling mean of log-relative holder breadth."""
    rm = _rolling_mean(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return rm - rm.shift(_TD_QTR)


def hcd_drv2_058_gap_rolling_mean_1y_qoq_change(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 1-year rolling mean of holder-count gap."""
    rm = _rolling_mean(_base_gap(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return rm - rm.shift(_TD_QTR)


def hcd_drv2_059_inst_pct_ratio_rolling_mean_1y_qoq(inst_pct: pd.Series,
                                                      peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in 1-year rolling mean of inst_pct ratio vs peer."""
    rm = _rolling_mean(_base_inst_pct_ratio(inst_pct, peer_median_inst_pct), _TD_YEAR)
    return rm - rm.shift(_TD_QTR)


def hcd_drv2_060_ratio_rolling_mean_1y_yoy_change(inst_holders: pd.Series,
                                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in 1-year rolling mean of holder-breadth ratio."""
    rm = _rolling_mean(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return rm - rm.shift(_TD_YEAR)


# --- zscore-level dynamics (QoQ of z-scores) --------------------------------

def hcd_drv2_061_zscore_3y_qoq_change(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 3-year rolling z-score of holder-breadth ratio."""
    zs = _zscore_rolling(_base_ratio(inst_holders, peer_median_inst_holders), _TD_3Y)
    return zs - zs.shift(_TD_QTR)


def hcd_drv2_062_log_rel_zscore_2y_qoq_change(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in 2-year z-score of log-relative holder breadth."""
    zs = _zscore_rolling(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)
    return zs - zs.shift(_TD_QTR)


def hcd_drv2_063_inst_pct_ratio_zscore_1y_qoq(inst_pct: pd.Series,
                                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in 1-year z-score of inst_pct ratio vs peer."""
    zs = _zscore_rolling(_base_inst_pct_ratio(inst_pct, peer_median_inst_pct), _TD_YEAR)
    return zs - zs.shift(_TD_QTR)


def hcd_drv2_064_zscore_1y_yoy_change(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in 1-year rolling z-score of holder-breadth ratio."""
    zs = _zscore_rolling(_base_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return zs - zs.shift(_TD_YEAR)


def hcd_drv2_065_log_rel_zscore_1y_yoy_change(inst_holders: pd.Series,
                                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in 1-year z-score of log-relative holder breadth."""
    zs = _zscore_rolling(_base_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return zs - zs.shift(_TD_YEAR)


# --- absolute and signed velocity features ----------------------------------

def hcd_drv2_066_ratio_qoq_abs_ewm_1q(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of |QoQ-change in holder-breadth ratio| (magnitude of change)."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = (ratio - ratio.shift(_TD_QTR)).abs()
    return _ewm_mean(d1, _TD_QTR)


def hcd_drv2_067_log_rel_qoq_abs_rolling_mean_1y(inst_holders: pd.Series,
                                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of |QoQ-change in log-relative holder breadth|."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = (lr - lr.shift(_TD_QTR)).abs()
    return _rolling_mean(d1, _TD_YEAR)


def hcd_drv2_068_ratio_qoq_sign(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Sign of QoQ-change in holder-breadth ratio (+1 improving, -1 deteriorating)."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return np.sign(d1)


def hcd_drv2_069_ratio_qoq_positive_fraction_1y(inst_holders: pd.Series,
                                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 1 year where QoQ-change in ratio was positive."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    return _rolling_mean((d1 > 0).astype(float), _TD_YEAR)


def hcd_drv2_070_collapse_score_qoq_positive_fraction_1y(inst_holders: pd.Series,
                                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days where QoQ-change in collapse score was positive (worsening)."""
    score = _base_collapse_score(inst_holders, peer_median_inst_holders)
    d1 = score - score.shift(_TD_QTR)
    return _rolling_mean((d1 > 0).astype(float), _TD_YEAR)


# --- 2nd-diff absolute/min/max features ------------------------------------

def hcd_drv2_071_ratio_qoq_diff2_abs_rolling_mean_1y(inst_holders: pd.Series,
                                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of |2nd QoQ diff of holder-breadth ratio|."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_QTR)
    d2 = (d1 - d1.shift(_TD_QTR)).abs()
    return _rolling_mean(d2, _TD_YEAR)


def hcd_drv2_072_log_rel_qoq_diff2_rolling_mean_1y(inst_holders: pd.Series,
                                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of 2nd QoQ diff of log-relative holder breadth."""
    lr = _base_log_rel(inst_holders, peer_median_inst_holders)
    d1 = lr - lr.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _rolling_mean(d2, _TD_YEAR)


def hcd_drv2_073_gap_qoq_diff2_rolling_mean_1y(inst_holders: pd.Series,
                                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of 2nd QoQ diff of holder-count gap."""
    gap = _base_gap(inst_holders, peer_median_inst_holders)
    d1 = gap - gap.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _rolling_mean(d2, _TD_YEAR)


def hcd_drv2_074_inst_pct_ratio_qoq_diff2_ewm_1q(inst_pct: pd.Series,
                                                    peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM(1q) of 2nd QoQ diff of inst_pct ratio vs peer."""
    ratio = _base_inst_pct_ratio(inst_pct, peer_median_inst_pct)
    d1 = ratio - ratio.shift(_TD_QTR)
    d2 = d1 - d1.shift(_TD_QTR)
    return _ewm_mean(d2, _TD_QTR)


def hcd_drv2_075_ratio_yoy_change_ewm_1q(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of YoY-change in holder-breadth ratio."""
    ratio = _base_ratio(inst_holders, peer_median_inst_holders)
    d1 = ratio - ratio.shift(_TD_YEAR)
    return _ewm_mean(d1, _TD_QTR)


# ===========================================================================
# Registry
# ===========================================================================
HOLDER_COUNT_DYNAMICS_REGISTRY_2ND_DERIVATIVES = {
    "hcd_drv2_001_ratio_qoq_diff_of_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_001_ratio_qoq_diff_of_qoq,
    },
    "hcd_drv2_002_ratio_yoy_diff_of_yoy": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_002_ratio_yoy_diff_of_yoy,
    },
    "hcd_drv2_003_log_rel_qoq_diff_of_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_003_log_rel_qoq_diff_of_qoq,
    },
    "hcd_drv2_004_gap_qoq_diff_of_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_004_gap_qoq_diff_of_qoq,
    },
    "hcd_drv2_005_inst_pct_ratio_qoq_diff2": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_005_inst_pct_ratio_qoq_diff2,
    },
    "hcd_drv2_006_ratio_slope_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_006_ratio_slope_qoq_change,
    },
    "hcd_drv2_007_ratio_slope_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_007_ratio_slope_yoy_change,
    },
    "hcd_drv2_008_log_rel_slope_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_008_log_rel_slope_qoq_change,
    },
    "hcd_drv2_009_ratio_ewm1q_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_009_ratio_ewm1q_qoq_change,
    },
    "hcd_drv2_010_ratio_ewm1y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_010_ratio_ewm1y_qoq_change,
    },
    "hcd_drv2_011_ratio_ewm1q_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_011_ratio_ewm1q_yoy_change,
    },
    "hcd_drv2_012_zscore_1y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_012_zscore_1y_qoq_change,
    },
    "hcd_drv2_013_zscore_2y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_013_zscore_2y_qoq_change,
    },
    "hcd_drv2_014_log_rel_zscore_1y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_014_log_rel_zscore_1y_qoq_change,
    },
    "hcd_drv2_015_collapse_score_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_015_collapse_score_qoq_change,
    },
    "hcd_drv2_016_collapse_score_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_016_collapse_score_yoy_change,
    },
    "hcd_drv2_017_collapse_score_ewm_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_017_collapse_score_ewm_qoq,
    },
    "hcd_drv2_018_inst_pct_gap_qoq_diff2": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_018_inst_pct_gap_qoq_diff2,
    },
    "hcd_drv2_019_ratio_qoq_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_019_ratio_qoq_rolling_mean_1y,
    },
    "hcd_drv2_020_ratio_qoq_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_020_ratio_qoq_ewm,
    },
    "hcd_drv2_021_log_rel_qoq_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_021_log_rel_qoq_ewm,
    },
    "hcd_drv2_022_ratio_qoq_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_022_ratio_qoq_zscore_1y,
    },
    "hcd_drv2_023_gap_slope_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_023_gap_slope_qoq_change,
    },
    "hcd_drv2_024_ratio_rolling_mean_1y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_024_ratio_rolling_mean_1y_qoq_change,
    },
    "hcd_drv2_025_inst_pct_ratio_slope_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_025_inst_pct_ratio_slope_qoq,
    },
    "hcd_drv2_026_ratio_2q_diff_of_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_026_ratio_2q_diff_of_qoq,
    },
    "hcd_drv2_027_log_rel_yoy_diff_of_yoy": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_027_log_rel_yoy_diff_of_yoy,
    },
    "hcd_drv2_028_gap_yoy_diff_of_yoy": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_028_gap_yoy_diff_of_yoy,
    },
    "hcd_drv2_029_inst_pct_gap_yoy_diff2": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_029_inst_pct_gap_yoy_diff2,
    },
    "hcd_drv2_030_inst_pct_ratio_yoy_diff2": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_030_inst_pct_ratio_yoy_diff2,
    },
    "hcd_drv2_031_ratio_qoq_rolling_mean_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_031_ratio_qoq_rolling_mean_2y,
    },
    "hcd_drv2_032_log_rel_qoq_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_032_log_rel_qoq_rolling_mean_1y,
    },
    "hcd_drv2_033_gap_qoq_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_033_gap_qoq_rolling_mean_1y,
    },
    "hcd_drv2_034_inst_pct_ratio_qoq_rolling_mean_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_034_inst_pct_ratio_qoq_rolling_mean_1y,
    },
    "hcd_drv2_035_collapse_score_qoq_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_035_collapse_score_qoq_rolling_mean_1y,
    },
    "hcd_drv2_036_ratio_qoq_ewm_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_036_ratio_qoq_ewm_2q,
    },
    "hcd_drv2_037_log_rel_qoq_ewm_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_037_log_rel_qoq_ewm_2q,
    },
    "hcd_drv2_038_gap_qoq_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_038_gap_qoq_ewm_1q,
    },
    "hcd_drv2_039_inst_pct_ratio_qoq_ewm_1q": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_039_inst_pct_ratio_qoq_ewm_1q,
    },
    "hcd_drv2_040_collapse_score_qoq_ewm_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_040_collapse_score_qoq_ewm_2q,
    },
    "hcd_drv2_041_log_rel_qoq_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_041_log_rel_qoq_zscore_1y,
    },
    "hcd_drv2_042_gap_qoq_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_042_gap_qoq_zscore_1y,
    },
    "hcd_drv2_043_inst_pct_ratio_qoq_zscore_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_043_inst_pct_ratio_qoq_zscore_1y,
    },
    "hcd_drv2_044_collapse_score_qoq_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_044_collapse_score_qoq_zscore_1y,
    },
    "hcd_drv2_045_ratio_yoy_change_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_045_ratio_yoy_change_zscore_1y,
    },
    "hcd_drv2_046_ratio_qoq_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_046_ratio_qoq_slope_1y,
    },
    "hcd_drv2_047_log_rel_qoq_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_047_log_rel_qoq_slope_1y,
    },
    "hcd_drv2_048_gap_slope_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_048_gap_slope_2y,
    },
    "hcd_drv2_049_log_rel_slope_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_049_log_rel_slope_2y,
    },
    "hcd_drv2_050_ratio_slope_2y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_050_ratio_slope_2y_qoq_change,
    },
    "hcd_drv2_051_ratio_ewm1q_yoy_diff": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_051_ratio_ewm1q_yoy_diff,
    },
    "hcd_drv2_052_ratio_ewm2q_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_052_ratio_ewm2q_qoq_change,
    },
    "hcd_drv2_053_log_rel_ewm1q_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_053_log_rel_ewm1q_qoq_change,
    },
    "hcd_drv2_054_inst_pct_ratio_ewm1q_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_054_inst_pct_ratio_ewm1q_qoq,
    },
    "hcd_drv2_055_collapse_score_ewm1q_yoy": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_055_collapse_score_ewm1q_yoy,
    },
    "hcd_drv2_056_ratio_rolling_mean_2y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_056_ratio_rolling_mean_2y_qoq_change,
    },
    "hcd_drv2_057_log_rel_rolling_mean_1y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_057_log_rel_rolling_mean_1y_qoq_change,
    },
    "hcd_drv2_058_gap_rolling_mean_1y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_058_gap_rolling_mean_1y_qoq_change,
    },
    "hcd_drv2_059_inst_pct_ratio_rolling_mean_1y_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_059_inst_pct_ratio_rolling_mean_1y_qoq,
    },
    "hcd_drv2_060_ratio_rolling_mean_1y_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_060_ratio_rolling_mean_1y_yoy_change,
    },
    "hcd_drv2_061_zscore_3y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_061_zscore_3y_qoq_change,
    },
    "hcd_drv2_062_log_rel_zscore_2y_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_062_log_rel_zscore_2y_qoq_change,
    },
    "hcd_drv2_063_inst_pct_ratio_zscore_1y_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_063_inst_pct_ratio_zscore_1y_qoq,
    },
    "hcd_drv2_064_zscore_1y_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_064_zscore_1y_yoy_change,
    },
    "hcd_drv2_065_log_rel_zscore_1y_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_065_log_rel_zscore_1y_yoy_change,
    },
    "hcd_drv2_066_ratio_qoq_abs_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_066_ratio_qoq_abs_ewm_1q,
    },
    "hcd_drv2_067_log_rel_qoq_abs_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_067_log_rel_qoq_abs_rolling_mean_1y,
    },
    "hcd_drv2_068_ratio_qoq_sign": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_068_ratio_qoq_sign,
    },
    "hcd_drv2_069_ratio_qoq_positive_fraction_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_069_ratio_qoq_positive_fraction_1y,
    },
    "hcd_drv2_070_collapse_score_qoq_positive_fraction_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_070_collapse_score_qoq_positive_fraction_1y,
    },
    "hcd_drv2_071_ratio_qoq_diff2_abs_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_071_ratio_qoq_diff2_abs_rolling_mean_1y,
    },
    "hcd_drv2_072_log_rel_qoq_diff2_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_072_log_rel_qoq_diff2_rolling_mean_1y,
    },
    "hcd_drv2_073_gap_qoq_diff2_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_073_gap_qoq_diff2_rolling_mean_1y,
    },
    "hcd_drv2_074_inst_pct_ratio_qoq_diff2_ewm_1q": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_drv2_074_inst_pct_ratio_qoq_diff2_ewm_1q,
    },
    "hcd_drv2_075_ratio_yoy_change_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_drv2_075_ratio_yoy_change_ewm_1q,
    },
}
