"""
94_holder_count_dynamics — Base Features 001-100
=================================================
Domain: CROSS-SECTIONAL peer-relative breadth of institutional holder base.
Measures how many institutions hold a ticker RELATIVE TO its sector/industry
peer median — ratios, gaps, z-scores, ranks, and QoQ/YoY dynamics thereof.

CROSS-SECTIONAL PEER-MEDIAN INPUT CONTRACT
------------------------------------------
Every feature function receives:
  own_series   : daily pd.Series, forward-filled from quarterly SF3 13F data,
                 representing one metric for THIS ticker.
  peer_series  : daily pd.Series with the SAME DatetimeIndex, containing the
                 SECTOR/INDUSTRY PEER-MEDIAN of that same metric, computed
                 universe-wide by the pipeline for each calendar date.

The pipeline is responsible for aligning both series to a common daily index
before calling any feature function.  Functions call _align_quarterly_to_daily
internally only when they need to down-sample to quarterly grid points before
computing rolling statistics.

Quarterly cadence on a trading-day axis:
  1 quarter  ≈ 63 trading days  (_TD_QTR)
  1 year     ≈ 252 trading days (_TD_YEAR)
  2 years    ≈ 504 trading days (_TD_2Y)
  3 years    ≈ 756 trading days (_TD_3Y)

All features are BACKWARD-LOOKING ONLY (no forward leakage).
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

def _align_quarterly_to_daily(series: pd.Series, window_td: int) -> pd.Series:
    """Return series resampled to approx-quarterly grid then reindexed to daily.

    Used when a rolling window should only count ~quarterly observations rather
    than all daily forward-fill copies.  Samples every _TD_QTR trading days
    (counting from the last available date backwards), then forward-fills back
    to the original daily index.
    """
    if series.empty:
        return series
    sampled = series.iloc[::_TD_QTR]
    return sampled.reindex(series.index, method="ffill")


def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / b with zero-denominator guard."""
    denom = b.replace(0, np.nan)
    return a / denom


def _safe_div_abs(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / |b| with zero-denominator guard."""
    denom = b.abs().replace(0, np.nan)
    return a / denom


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    """own / peer_median ratio (>1 means above peer)."""
    return _safe_div(own, peer.replace(0, np.nan))


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    """log(own / peer) — symmetric log-relative deviation."""
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.clip(lower=_EPS))


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
    """Absolute arithmetic gap: own - peer_median."""
    return own - peer


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    """Percentile rank of current value within rolling window [0,1]."""
    def _rank(x):
        if len(x) < 2:
            return np.nan
        return (x[:-1] < x[-1]).sum() / (len(x) - 1)
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_rank, raw=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - mu, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


# ===========================================================================
# Feature Functions 001 – 075
# ===========================================================================

# --- Ratio features (own / peer_median) ------------------------------------

def hcd_001_inst_holders_ratio_raw(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Raw ratio of ticker's institution-holder count to peer median."""
    return _rel_ratio(inst_holders, peer_median_inst_holders)


def hcd_002_inst_holders_log_rel(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Log-relative holder breadth vs peer: log(own/peer)."""
    return _log_rel(inst_holders, peer_median_inst_holders)


def hcd_003_inst_holders_gap(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """Arithmetic gap: ticker inst_holders minus peer median."""
    return _gap(inst_holders, peer_median_inst_holders)


def hcd_004_inst_holders_gap_pct(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Gap as percentage of peer median: (own-peer)/peer."""
    return _safe_div(_gap(inst_holders, peer_median_inst_holders),
                     peer_median_inst_holders.replace(0, np.nan))


def hcd_005_below_peer_flag(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """Binary 1 if ticker holder count is below peer median, else 0."""
    return (inst_holders < peer_median_inst_holders).astype(float)


def hcd_006_inst_pct_ratio(inst_pct: pd.Series,
                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """Ratio of ticker institutional-ownership pct to peer median."""
    return _rel_ratio(inst_pct, peer_median_inst_pct)


def hcd_007_inst_pct_log_rel(inst_pct: pd.Series,
                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """Log-relative institutional-ownership pct vs peer."""
    return _log_rel(inst_pct, peer_median_inst_pct)


def hcd_008_inst_pct_gap(inst_pct: pd.Series,
                          peer_median_inst_pct: pd.Series) -> pd.Series:
    """Arithmetic gap: ticker inst_pct minus peer median inst_pct."""
    return _gap(inst_pct, peer_median_inst_pct)


def hcd_009_inst_shares_ratio(inst_shares: pd.Series,
                               peer_median_inst_shares: pd.Series) -> pd.Series:
    """Ratio of ticker institutional shares held to peer median."""
    return _rel_ratio(inst_shares, peer_median_inst_shares)


def hcd_010_inst_shares_log_rel(inst_shares: pd.Series,
                                 peer_median_inst_shares: pd.Series) -> pd.Series:
    """Log-relative institutional shares held vs peer median."""
    return _log_rel(inst_shares, peer_median_inst_shares)


# --- Rolling mean of ratio / gap -------------------------------------------

def hcd_011_ratio_rolling_mean_1q(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-quarter rolling mean of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_mean(ratio, _TD_QTR)


def hcd_012_ratio_rolling_mean_2q(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter rolling mean of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_mean(ratio, _TD_2Q)


def hcd_013_ratio_rolling_mean_1y(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_mean(ratio, _TD_YEAR)


def hcd_014_ratio_rolling_mean_2y(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling mean of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_mean(ratio, _TD_2Y)


def hcd_015_gap_rolling_mean_1q(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-quarter rolling mean of holder-count gap (own-peer)."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return _rolling_mean(gap, _TD_QTR)


def hcd_016_gap_rolling_mean_1y(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of holder-count gap."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return _rolling_mean(gap, _TD_YEAR)


# --- Rolling z-scores of relative metrics ----------------------------------

def hcd_017_ratio_zscore_1y(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling z-score of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def hcd_018_ratio_zscore_2y(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling z-score of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(ratio, _TD_2Y)


def hcd_019_ratio_zscore_3y(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling z-score of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(ratio, _TD_3Y)


def hcd_020_log_rel_zscore_1y(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling z-score of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(lr, _TD_YEAR)


def hcd_021_log_rel_zscore_2y(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling z-score of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _zscore_rolling(lr, _TD_2Y)


def hcd_022_inst_pct_ratio_zscore_1y(inst_pct: pd.Series,
                                      peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling z-score of inst_pct ratio vs peer."""
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    return _zscore_rolling(ratio, _TD_YEAR)


def hcd_023_inst_pct_gap_zscore_1y(inst_pct: pd.Series,
                                    peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling z-score of inst_pct gap (own-peer)."""
    gap = _gap(inst_pct, peer_median_inst_pct)
    return _zscore_rolling(gap, _TD_YEAR)


# --- Rolling rank (percentile) features ------------------------------------

def hcd_024_ratio_rank_1y(inst_holders: pd.Series,
                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def hcd_025_ratio_rank_2y(inst_holders: pd.Series,
                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_rank_pct(ratio, _TD_2Y)


def hcd_026_ratio_rank_3y(inst_holders: pd.Series,
                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling percentile rank of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_rank_pct(ratio, _TD_3Y)


def hcd_027_log_rel_rank_1y(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _rolling_rank_pct(lr, _TD_YEAR)


def hcd_028_inst_pct_ratio_rank_1y(inst_pct: pd.Series,
                                    peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of inst_pct ratio vs peer."""
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    return _rolling_rank_pct(ratio, _TD_YEAR)


# --- QoQ change in relative metrics ----------------------------------------

def hcd_029_ratio_qoq_change(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change (diff over 63 td) in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - ratio.shift(_TD_QTR)


def hcd_030_ratio_qoq_pct_change(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ percentage change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    prev = ratio.shift(_TD_QTR)
    return _safe_div(ratio - prev, prev.abs().replace(0, np.nan))


def hcd_031_log_rel_qoq_change(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - lr.shift(_TD_QTR)


def hcd_032_gap_qoq_change(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in arithmetic holder-count gap (own-peer)."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return gap - gap.shift(_TD_QTR)


def hcd_033_inst_pct_ratio_qoq(inst_pct: pd.Series,
                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in inst_pct ratio vs peer median."""
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    return ratio - ratio.shift(_TD_QTR)


def hcd_034_inst_pct_gap_qoq(inst_pct: pd.Series,
                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in inst_pct gap (own-peer)."""
    gap = _gap(inst_pct, peer_median_inst_pct)
    return gap - gap.shift(_TD_QTR)


# --- YoY change in relative metrics ----------------------------------------

def hcd_035_ratio_yoy_change(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change (diff over 252 td) in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - ratio.shift(_TD_YEAR)


def hcd_036_ratio_yoy_pct_change(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY percentage change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    prev = ratio.shift(_TD_YEAR)
    return _safe_div(ratio - prev, prev.abs().replace(0, np.nan))


def hcd_037_log_rel_yoy_change(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - lr.shift(_TD_YEAR)


def hcd_038_gap_yoy_change(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in arithmetic holder-count gap."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return gap - gap.shift(_TD_YEAR)


def hcd_039_inst_pct_ratio_yoy(inst_pct: pd.Series,
                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """YoY change in inst_pct ratio vs peer median."""
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    return ratio - ratio.shift(_TD_YEAR)


def hcd_040_inst_pct_gap_yoy(inst_pct: pd.Series,
                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """YoY change in inst_pct gap (own-peer)."""
    gap = _gap(inst_pct, peer_median_inst_pct)
    return gap - gap.shift(_TD_YEAR)


# --- Rolling min / max of relative metrics ---------------------------------

def hcd_041_ratio_rolling_min_1y(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_min(ratio, _TD_YEAR)


def hcd_042_ratio_rolling_max_1y(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling maximum of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_max(ratio, _TD_YEAR)


def hcd_043_ratio_vs_rolling_min(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Current ratio minus its 1-year rolling min (distance above trough)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _rolling_min(ratio, _TD_YEAR)


def hcd_044_ratio_vs_rolling_max(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Current ratio minus its 1-year rolling max (drawdown from peak)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _rolling_max(ratio, _TD_YEAR)


def hcd_045_ratio_2y_min(inst_holders: pd.Series,
                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling minimum of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_min(ratio, _TD_2Y)


def hcd_046_ratio_drawdown_from_2y_max(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Ratio drawdown: current ratio / 2-year max ratio - 1."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mx = _rolling_max(ratio, _TD_2Y)
    return _safe_div(ratio, mx.replace(0, np.nan)) - 1.0


def hcd_047_gap_rolling_min_1y(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling minimum of holder-count gap (most negative)."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return _rolling_min(gap, _TD_YEAR)


def hcd_048_log_rel_rolling_min_2y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling minimum of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _rolling_min(lr, _TD_2Y)


# --- EWM (exponential) smoothing of relative metrics ----------------------

def hcd_049_ratio_ewm_1q(inst_holders: pd.Series,
                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=63 td) of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _ewm_mean(ratio, _TD_QTR)


def hcd_050_ratio_ewm_2q(inst_holders: pd.Series,
                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=126 td) of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _ewm_mean(ratio, _TD_2Q)


def hcd_051_ratio_ewm_1y(inst_holders: pd.Series,
                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=252 td) of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _ewm_mean(ratio, _TD_YEAR)


def hcd_052_log_rel_ewm_1q(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=63) of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _ewm_mean(lr, _TD_QTR)


def hcd_053_ratio_vs_ewm_deviation(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Current ratio minus its EWM(1q): deviation from short-term trend."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _ewm_mean(ratio, _TD_QTR)


def hcd_054_ratio_ewm_vs_long_ewm(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """Short EWM(1q) minus long EWM(1y) of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _ewm_mean(ratio, _TD_QTR) - _ewm_mean(ratio, _TD_YEAR)


# --- Consecutive below-peer streaks ----------------------------------------

def hcd_055_consec_qtrs_below_peer(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Consecutive trading days below peer median (cumulative streak)."""
    below = (inst_holders < peer_median_inst_holders).astype(int)
    streak = below * (below.groupby((below != below.shift()).cumsum()).cumcount() + 1)
    return streak.astype(float)


def hcd_056_below_peer_fraction_1y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 1 year where ticker was below peer median."""
    below = (inst_holders < peer_median_inst_holders).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def hcd_057_below_peer_fraction_2y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past 2 years where ticker was below peer median."""
    below = (inst_holders < peer_median_inst_holders).astype(float)
    return _rolling_mean(below, _TD_2Y)


def hcd_058_below_peer_fraction_qtr(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of days in past quarter where ticker was below peer median."""
    below = (inst_holders < peer_median_inst_holders).astype(float)
    return _rolling_mean(below, _TD_QTR)


# --- Rolling std / volatility of relative series --------------------------

def hcd_059_ratio_rolling_std_1y(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling std of holder-breadth ratio (relative breadth volatility)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_std(ratio, _TD_YEAR)


def hcd_060_log_rel_rolling_std_1y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling std of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _rolling_std(lr, _TD_YEAR)


def hcd_061_gap_rolling_std_1y(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling std of holder-count gap (own-peer)."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return _rolling_std(gap, _TD_YEAR)


# --- Expanding-window features (lifetime perspective) ----------------------

def hcd_062_ratio_expanding_mean(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding (lifetime) mean of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio.expanding(min_periods=1).mean()


def hcd_063_ratio_expanding_zscore(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding z-score of holder-breadth ratio (full history)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mu = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - mu, sd)


def hcd_064_ratio_expanding_rank(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding percentile rank of current holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    def _exp_rank(x):
        if len(x) < 2:
            return np.nan
        return (x[:-1] < x[-1]).sum() / (len(x) - 1)
    return ratio.expanding(min_periods=2).apply(_exp_rank, raw=True)


def hcd_065_log_rel_expanding_min(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding minimum of log-relative holder breadth (worst ever vs peer)."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr.expanding(min_periods=1).min()


# --- Multi-field composite relative features --------------------------------

def hcd_066_holders_and_pct_composite_ratio(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series,
                                             inst_pct: pd.Series,
                                             peer_median_inst_pct: pd.Series) -> pd.Series:
    """Geometric mean of holder-count ratio and inst_pct ratio vs peer."""
    r1 = _rel_ratio(inst_holders, peer_median_inst_holders).clip(lower=_EPS)
    r2 = _rel_ratio(inst_pct, peer_median_inst_pct).clip(lower=_EPS)
    return np.sqrt(r1 * r2)


def hcd_067_holders_pct_composite_log_rel(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series,
                                           inst_pct: pd.Series,
                                           peer_median_inst_pct: pd.Series) -> pd.Series:
    """Sum of log-rel for holders count and inst_pct — combined breadth signal."""
    return (_log_rel(inst_holders, peer_median_inst_holders) +
            _log_rel(inst_pct, peer_median_inst_pct))


def hcd_068_composite_ratio_zscore_1y(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series,
                                       inst_pct: pd.Series,
                                       peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year z-score of composite (holders + pct) log-rel signal."""
    composite = (_log_rel(inst_holders, peer_median_inst_holders) +
                 _log_rel(inst_pct, peer_median_inst_pct))
    return _zscore_rolling(composite, _TD_YEAR)


def hcd_069_shares_holders_ratio_composite(inst_shares: pd.Series,
                                            peer_median_inst_shares: pd.Series,
                                            inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """Difference between shares-ratio and holders-ratio vs peer (concentration signal)."""
    return (_rel_ratio(inst_shares, peer_median_inst_shares) -
            _rel_ratio(inst_holders, peer_median_inst_holders))


# --- Trend / slope features ------------------------------------------------

def hcd_070_ratio_slope_1y(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder-breadth ratio over trailing 1-year window."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    x = np.arange(_TD_YEAR, dtype=float)
    def _slope(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xm = np.arange(len(y), dtype=float)[mask]
        ym = y[mask]
        xm = xm - xm.mean()
        return np.dot(xm, ym) / (np.dot(xm, xm) + _EPS)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_slope, raw=True)


def hcd_071_ratio_slope_2y(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder-breadth ratio over trailing 2-year window."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    x = np.arange(_TD_2Y, dtype=float)
    def _slope(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xm = np.arange(len(y), dtype=float)[mask]
        ym = y[mask]
        xm = xm - xm.mean()
        return np.dot(xm, ym) / (np.dot(xm, xm) + _EPS)
    return ratio.rolling(_TD_2Y, min_periods=_TD_QTR).apply(_slope, raw=True)


def hcd_072_log_rel_slope_1y(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """OLS slope of log-relative holder breadth over 1-year window."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    x = np.arange(_TD_YEAR, dtype=float)
    def _slope(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xm = np.arange(len(y), dtype=float)[mask]
        ym = y[mask]
        xm = xm - xm.mean()
        return np.dot(xm, ym) / (np.dot(xm, xm) + _EPS)
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_slope, raw=True)


def hcd_073_gap_slope_1y(inst_holders: pd.Series,
                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder-count gap (own-peer) over 1-year window."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    x = np.arange(_TD_YEAR, dtype=float)
    def _slope(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xm = np.arange(len(y), dtype=float)[mask]
        ym = y[mask]
        xm = xm - xm.mean()
        return np.dot(xm, ym) / (np.dot(xm, xm) + _EPS)
    return gap.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_slope, raw=True)


def hcd_074_ratio_acceleration_1y(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in QoQ-change of holder-breadth ratio (acceleration)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    delta = ratio - ratio.shift(_TD_QTR)
    return delta - delta.shift(_TD_QTR)


def hcd_075_ratio_rolling_median_1y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling median of holder-breadth ratio (robust central tendency)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_median(ratio, _TD_YEAR)


# ===========================================================================
# Feature Functions 151 – 175
# ===========================================================================

# --- inst_shares cross-sectional features -----------------------------------

def hcd_151_inst_shares_zscore_1y(inst_shares: pd.Series,
                                   peer_median_inst_shares: pd.Series) -> pd.Series:
    """1-year rolling z-score of inst_shares ratio vs peer."""
    return _zscore_rolling(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_YEAR)


def hcd_152_inst_shares_zscore_2y(inst_shares: pd.Series,
                                   peer_median_inst_shares: pd.Series) -> pd.Series:
    """2-year rolling z-score of inst_shares ratio vs peer."""
    return _zscore_rolling(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_2Y)


def hcd_153_inst_shares_rank_1y(inst_shares: pd.Series,
                                 peer_median_inst_shares: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of inst_shares ratio vs peer."""
    return _rolling_rank_pct(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_YEAR)


def hcd_154_inst_shares_ratio_qoq(inst_shares: pd.Series,
                                   peer_median_inst_shares: pd.Series) -> pd.Series:
    """QoQ change in inst_shares ratio vs peer."""
    r = _rel_ratio(inst_shares, peer_median_inst_shares)
    return r - r.shift(_TD_QTR)


def hcd_155_inst_shares_ratio_yoy(inst_shares: pd.Series,
                                   peer_median_inst_shares: pd.Series) -> pd.Series:
    """YoY change in inst_shares ratio vs peer."""
    r = _rel_ratio(inst_shares, peer_median_inst_shares)
    return r - r.shift(_TD_YEAR)


def hcd_156_inst_shares_collapse_score(inst_shares: pd.Series,
                                        peer_median_inst_shares: pd.Series) -> pd.Series:
    """Collapse score for inst_shares: -log_rel clipped to [0, inf]."""
    return (-_log_rel(inst_shares, peer_median_inst_shares)).clip(lower=0.0)


def hcd_157_inst_shares_rolling_mean_1y(inst_shares: pd.Series,
                                         peer_median_inst_shares: pd.Series) -> pd.Series:
    """1-year rolling mean of inst_shares ratio vs peer."""
    return _rolling_mean(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_YEAR)


def hcd_158_inst_shares_drawdown_2y(inst_shares: pd.Series,
                                     peer_median_inst_shares: pd.Series) -> pd.Series:
    """Drawdown of inst_shares ratio from 2-year rolling max."""
    r = _rel_ratio(inst_shares, peer_median_inst_shares)
    mx = _rolling_max(r, _TD_2Y)
    return _safe_div(r, mx.replace(0, np.nan)) - 1.0


def hcd_159_inst_shares_position_in_range_1y(inst_shares: pd.Series,
                                              peer_median_inst_shares: pd.Series) -> pd.Series:
    """Position of inst_shares ratio within its 1-year range: (cur-min)/(max-min)."""
    r = _rel_ratio(inst_shares, peer_median_inst_shares)
    mn = _rolling_min(r, _TD_YEAR)
    mx = _rolling_max(r, _TD_YEAR)
    return _safe_div(r - mn, (mx - mn).replace(0, np.nan))


# --- new/closed position additional analytics --------------------------------

def hcd_160_new_pos_ratio_rolling_mean_2y(new_positions: pd.Series,
                                           peer_median_new_positions: pd.Series) -> pd.Series:
    """2-year rolling mean of new-positions ratio vs peer."""
    return _rolling_mean(_rel_ratio(new_positions, peer_median_new_positions), _TD_2Y)


def hcd_161_closed_pos_ratio_rolling_mean_2y(closed_positions: pd.Series,
                                              peer_median_closed_positions: pd.Series) -> pd.Series:
    """2-year rolling mean of closed-positions ratio vs peer."""
    return _rolling_mean(_rel_ratio(closed_positions, peer_median_closed_positions), _TD_2Y)


def hcd_162_new_pos_ratio_rank_1y(new_positions: pd.Series,
                                   peer_median_new_positions: pd.Series) -> pd.Series:
    """1-year percentile rank of new-positions ratio vs peer."""
    return _rolling_rank_pct(_rel_ratio(new_positions, peer_median_new_positions), _TD_YEAR)


def hcd_163_closed_pos_ratio_rank_1y(closed_positions: pd.Series,
                                      peer_median_closed_positions: pd.Series) -> pd.Series:
    """1-year percentile rank of closed-positions ratio vs peer."""
    return _rolling_rank_pct(_rel_ratio(closed_positions, peer_median_closed_positions), _TD_YEAR)


def hcd_164_net_flow_ratio_rolling_mean_1y(new_positions: pd.Series,
                                            peer_median_new_positions: pd.Series,
                                            closed_positions: pd.Series,
                                            peer_median_closed_positions: pd.Series) -> pd.Series:
    """1-year rolling mean of net relative flow (new_ratio - closed_ratio)."""
    flow = (_rel_ratio(new_positions, peer_median_new_positions) -
            _rel_ratio(closed_positions, peer_median_closed_positions))
    return _rolling_mean(flow, _TD_YEAR)


def hcd_165_net_flow_ratio_zscore_1y(new_positions: pd.Series,
                                      peer_median_new_positions: pd.Series,
                                      closed_positions: pd.Series,
                                      peer_median_closed_positions: pd.Series) -> pd.Series:
    """1-year rolling z-score of net relative flow (new_ratio - closed_ratio)."""
    flow = (_rel_ratio(new_positions, peer_median_new_positions) -
            _rel_ratio(closed_positions, peer_median_closed_positions))
    return _zscore_rolling(flow, _TD_YEAR)


# --- additional ratio/gap rolling statistics ---------------------------------

def hcd_166_ratio_rolling_std_2y(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling std of holder-breadth ratio."""
    return _rolling_std(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_167_gap_rolling_mean_2y(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling mean of holder-count gap (own-peer)."""
    return _rolling_mean(_gap(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_168_log_rel_rolling_mean_1q(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-quarter rolling mean of log-relative holder breadth."""
    return _rolling_mean(_log_rel(inst_holders, peer_median_inst_holders), _TD_QTR)


def hcd_169_log_rel_rolling_mean_2y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling mean of log-relative holder breadth."""
    return _rolling_mean(_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_170_inst_pct_ratio_rolling_mean_1q(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-quarter rolling mean of inst_pct ratio vs peer."""
    return _rolling_mean(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_QTR)


# --- EWM and cross-field features --------------------------------------------

def hcd_171_inst_pct_ratio_ewm_1q(inst_pct: pd.Series,
                                   peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM(1q) of inst_pct ratio vs peer."""
    return _ewm_mean(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_QTR)


def hcd_172_inst_pct_log_rel_ewm_1q(inst_pct: pd.Series,
                                     peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM(1q) of log-relative inst_pct vs peer."""
    return _ewm_mean(_log_rel(inst_pct, peer_median_inst_pct), _TD_QTR)


def hcd_173_composite_ratio_ewm_1q(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series,
                                    inst_pct: pd.Series,
                                    peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM(1q) of composite (holders + pct) log-rel signal."""
    composite = (_log_rel(inst_holders, peer_median_inst_holders) +
                 _log_rel(inst_pct, peer_median_inst_pct))
    return _ewm_mean(composite, _TD_QTR)


def hcd_174_shares_ratio_ewm_1q(inst_shares: pd.Series,
                                 peer_median_inst_shares: pd.Series) -> pd.Series:
    """EWM(1q) of inst_shares ratio vs peer."""
    return _ewm_mean(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_QTR)


def hcd_175_inst_pct_zscore_2y(inst_pct: pd.Series,
                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-year rolling z-score of inst_pct ratio vs peer."""
    return _zscore_rolling(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_2Y)


# ===========================================================================
# Registry
# ===========================================================================
HOLDER_COUNT_DYNAMICS_REGISTRY_001_075 = {
    "hcd_001_inst_holders_ratio_raw": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_001_inst_holders_ratio_raw,
    },
    "hcd_002_inst_holders_log_rel": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_002_inst_holders_log_rel,
    },
    "hcd_003_inst_holders_gap": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_003_inst_holders_gap,
    },
    "hcd_004_inst_holders_gap_pct": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_004_inst_holders_gap_pct,
    },
    "hcd_005_below_peer_flag": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_005_below_peer_flag,
    },
    "hcd_006_inst_pct_ratio": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_006_inst_pct_ratio,
    },
    "hcd_007_inst_pct_log_rel": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_007_inst_pct_log_rel,
    },
    "hcd_008_inst_pct_gap": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_008_inst_pct_gap,
    },
    "hcd_009_inst_shares_ratio": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_009_inst_shares_ratio,
    },
    "hcd_010_inst_shares_log_rel": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_010_inst_shares_log_rel,
    },
    "hcd_011_ratio_rolling_mean_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_011_ratio_rolling_mean_1q,
    },
    "hcd_012_ratio_rolling_mean_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_012_ratio_rolling_mean_2q,
    },
    "hcd_013_ratio_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_013_ratio_rolling_mean_1y,
    },
    "hcd_014_ratio_rolling_mean_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_014_ratio_rolling_mean_2y,
    },
    "hcd_015_gap_rolling_mean_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_015_gap_rolling_mean_1q,
    },
    "hcd_016_gap_rolling_mean_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_016_gap_rolling_mean_1y,
    },
    "hcd_017_ratio_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_017_ratio_zscore_1y,
    },
    "hcd_018_ratio_zscore_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_018_ratio_zscore_2y,
    },
    "hcd_019_ratio_zscore_3y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_019_ratio_zscore_3y,
    },
    "hcd_020_log_rel_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_020_log_rel_zscore_1y,
    },
    "hcd_021_log_rel_zscore_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_021_log_rel_zscore_2y,
    },
    "hcd_022_inst_pct_ratio_zscore_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_022_inst_pct_ratio_zscore_1y,
    },
    "hcd_023_inst_pct_gap_zscore_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_023_inst_pct_gap_zscore_1y,
    },
    "hcd_024_ratio_rank_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_024_ratio_rank_1y,
    },
    "hcd_025_ratio_rank_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_025_ratio_rank_2y,
    },
    "hcd_026_ratio_rank_3y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_026_ratio_rank_3y,
    },
    "hcd_027_log_rel_rank_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_027_log_rel_rank_1y,
    },
    "hcd_028_inst_pct_ratio_rank_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_028_inst_pct_ratio_rank_1y,
    },
    "hcd_029_ratio_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_029_ratio_qoq_change,
    },
    "hcd_030_ratio_qoq_pct_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_030_ratio_qoq_pct_change,
    },
    "hcd_031_log_rel_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_031_log_rel_qoq_change,
    },
    "hcd_032_gap_qoq_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_032_gap_qoq_change,
    },
    "hcd_033_inst_pct_ratio_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_033_inst_pct_ratio_qoq,
    },
    "hcd_034_inst_pct_gap_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_034_inst_pct_gap_qoq,
    },
    "hcd_035_ratio_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_035_ratio_yoy_change,
    },
    "hcd_036_ratio_yoy_pct_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_036_ratio_yoy_pct_change,
    },
    "hcd_037_log_rel_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_037_log_rel_yoy_change,
    },
    "hcd_038_gap_yoy_change": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_038_gap_yoy_change,
    },
    "hcd_039_inst_pct_ratio_yoy": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_039_inst_pct_ratio_yoy,
    },
    "hcd_040_inst_pct_gap_yoy": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_040_inst_pct_gap_yoy,
    },
    "hcd_041_ratio_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_041_ratio_rolling_min_1y,
    },
    "hcd_042_ratio_rolling_max_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_042_ratio_rolling_max_1y,
    },
    "hcd_043_ratio_vs_rolling_min": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_043_ratio_vs_rolling_min,
    },
    "hcd_044_ratio_vs_rolling_max": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_044_ratio_vs_rolling_max,
    },
    "hcd_045_ratio_2y_min": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_045_ratio_2y_min,
    },
    "hcd_046_ratio_drawdown_from_2y_max": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_046_ratio_drawdown_from_2y_max,
    },
    "hcd_047_gap_rolling_min_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_047_gap_rolling_min_1y,
    },
    "hcd_048_log_rel_rolling_min_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_048_log_rel_rolling_min_2y,
    },
    "hcd_049_ratio_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_049_ratio_ewm_1q,
    },
    "hcd_050_ratio_ewm_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_050_ratio_ewm_2q,
    },
    "hcd_051_ratio_ewm_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_051_ratio_ewm_1y,
    },
    "hcd_052_log_rel_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_052_log_rel_ewm_1q,
    },
    "hcd_053_ratio_vs_ewm_deviation": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_053_ratio_vs_ewm_deviation,
    },
    "hcd_054_ratio_ewm_vs_long_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_054_ratio_ewm_vs_long_ewm,
    },
    "hcd_055_consec_qtrs_below_peer": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_055_consec_qtrs_below_peer,
    },
    "hcd_056_below_peer_fraction_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_056_below_peer_fraction_1y,
    },
    "hcd_057_below_peer_fraction_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_057_below_peer_fraction_2y,
    },
    "hcd_058_below_peer_fraction_qtr": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_058_below_peer_fraction_qtr,
    },
    "hcd_059_ratio_rolling_std_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_059_ratio_rolling_std_1y,
    },
    "hcd_060_log_rel_rolling_std_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_060_log_rel_rolling_std_1y,
    },
    "hcd_061_gap_rolling_std_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_061_gap_rolling_std_1y,
    },
    "hcd_062_ratio_expanding_mean": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_062_ratio_expanding_mean,
    },
    "hcd_063_ratio_expanding_zscore": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_063_ratio_expanding_zscore,
    },
    "hcd_064_ratio_expanding_rank": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_064_ratio_expanding_rank,
    },
    "hcd_065_log_rel_expanding_min": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_065_log_rel_expanding_min,
    },
    "hcd_066_holders_and_pct_composite_ratio": {
        "inputs": ["inst_holders", "peer_median_inst_holders", "inst_pct", "peer_median_inst_pct"],
        "func": hcd_066_holders_and_pct_composite_ratio,
    },
    "hcd_067_holders_pct_composite_log_rel": {
        "inputs": ["inst_holders", "peer_median_inst_holders", "inst_pct", "peer_median_inst_pct"],
        "func": hcd_067_holders_pct_composite_log_rel,
    },
    "hcd_068_composite_ratio_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders", "inst_pct", "peer_median_inst_pct"],
        "func": hcd_068_composite_ratio_zscore_1y,
    },
    "hcd_069_shares_holders_ratio_composite": {
        "inputs": ["inst_shares", "peer_median_inst_shares", "inst_holders", "peer_median_inst_holders"],
        "func": hcd_069_shares_holders_ratio_composite,
    },
    "hcd_070_ratio_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_070_ratio_slope_1y,
    },
    "hcd_071_ratio_slope_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_071_ratio_slope_2y,
    },
    "hcd_072_log_rel_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_072_log_rel_slope_1y,
    },
    "hcd_073_gap_slope_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_073_gap_slope_1y,
    },
    "hcd_074_ratio_acceleration_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_074_ratio_acceleration_1y,
    },
    "hcd_075_ratio_rolling_median_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_075_ratio_rolling_median_1y,
    },
    "hcd_151_inst_shares_zscore_1y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_151_inst_shares_zscore_1y,
    },
    "hcd_152_inst_shares_zscore_2y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_152_inst_shares_zscore_2y,
    },
    "hcd_153_inst_shares_rank_1y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_153_inst_shares_rank_1y,
    },
    "hcd_154_inst_shares_ratio_qoq": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_154_inst_shares_ratio_qoq,
    },
    "hcd_155_inst_shares_ratio_yoy": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_155_inst_shares_ratio_yoy,
    },
    "hcd_156_inst_shares_collapse_score": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_156_inst_shares_collapse_score,
    },
    "hcd_157_inst_shares_rolling_mean_1y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_157_inst_shares_rolling_mean_1y,
    },
    "hcd_158_inst_shares_drawdown_2y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_158_inst_shares_drawdown_2y,
    },
    "hcd_159_inst_shares_position_in_range_1y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_159_inst_shares_position_in_range_1y,
    },
    "hcd_160_new_pos_ratio_rolling_mean_2y": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_160_new_pos_ratio_rolling_mean_2y,
    },
    "hcd_161_closed_pos_ratio_rolling_mean_2y": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_161_closed_pos_ratio_rolling_mean_2y,
    },
    "hcd_162_new_pos_ratio_rank_1y": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_162_new_pos_ratio_rank_1y,
    },
    "hcd_163_closed_pos_ratio_rank_1y": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_163_closed_pos_ratio_rank_1y,
    },
    "hcd_164_net_flow_ratio_rolling_mean_1y": {
        "inputs": ["new_positions", "peer_median_new_positions",
                   "closed_positions", "peer_median_closed_positions"],
        "func": hcd_164_net_flow_ratio_rolling_mean_1y,
    },
    "hcd_165_net_flow_ratio_zscore_1y": {
        "inputs": ["new_positions", "peer_median_new_positions",
                   "closed_positions", "peer_median_closed_positions"],
        "func": hcd_165_net_flow_ratio_zscore_1y,
    },
    "hcd_166_ratio_rolling_std_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_166_ratio_rolling_std_2y,
    },
    "hcd_167_gap_rolling_mean_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_167_gap_rolling_mean_2y,
    },
    "hcd_168_log_rel_rolling_mean_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_168_log_rel_rolling_mean_1q,
    },
    "hcd_169_log_rel_rolling_mean_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_169_log_rel_rolling_mean_2y,
    },
    "hcd_170_inst_pct_ratio_rolling_mean_1q": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_170_inst_pct_ratio_rolling_mean_1q,
    },
    "hcd_171_inst_pct_ratio_ewm_1q": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_171_inst_pct_ratio_ewm_1q,
    },
    "hcd_172_inst_pct_log_rel_ewm_1q": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_172_inst_pct_log_rel_ewm_1q,
    },
    "hcd_173_composite_ratio_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders",
                   "inst_pct", "peer_median_inst_pct"],
        "func": hcd_173_composite_ratio_ewm_1q,
    },
    "hcd_174_shares_ratio_ewm_1q": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_174_shares_ratio_ewm_1q,
    },
    "hcd_175_inst_pct_zscore_2y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_175_inst_pct_zscore_2y,
    },
}
