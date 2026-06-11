"""
94_holder_count_dynamics — Base Features 076-200
=================================================
Domain: CROSS-SECTIONAL peer-relative breadth of institutional holder base.
Continuation of features 001-075 — same domain, different angles.

CROSS-SECTIONAL PEER-MEDIAN INPUT CONTRACT
------------------------------------------
Every feature function receives:
  own_series   : daily pd.Series, forward-filled from quarterly SF3 13F data,
                 representing one metric for THIS ticker.
  peer_series  : daily pd.Series with the SAME DatetimeIndex, containing the
                 SECTOR/INDUSTRY PEER-MEDIAN of that same metric, computed
                 universe-wide by the pipeline for each calendar date.

The pipeline aligns both series to a common daily index before calling any
feature function.  _align_quarterly_to_daily is available for functions that
need quarterly grid subsampling.

Quarterly cadence on a trading-day axis:
  1 quarter  = 63 trading days  (_TD_QTR)
  1 year     = 252 trading days (_TD_YEAR)
  2 years    = 504 trading days (_TD_2Y)
  3 years    = 756 trading days (_TD_3Y)

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
    """Subsample series every _TD_QTR rows then forward-fill to daily index."""
    if series.empty:
        return series
    sampled = series.iloc[::_TD_QTR]
    return sampled.reindex(series.index, method="ffill")


def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    denom = b.replace(0, np.nan)
    return a / denom


def _safe_div_abs(a: pd.Series, b: pd.Series) -> pd.Series:
    denom = b.abs().replace(0, np.nan)
    return a / denom


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    return _safe_div(own, peer.replace(0, np.nan))


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.clip(lower=_EPS))


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
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
# Feature Functions 076 – 150
# ===========================================================================

# --- Additional ratio / gap flavors ----------------------------------------

def hcd_076_inst_holders_ratio_clipped(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio clipped to [0.05, 5] for outlier robustness."""
    return _rel_ratio(inst_holders, peer_median_inst_holders).clip(0.05, 5.0)


def hcd_077_inst_holders_gap_abs(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Absolute value of holder-count gap |own - peer|."""
    return _gap(inst_holders, peer_median_inst_holders).abs()


def hcd_078_inst_pct_gap_pct_of_peer(inst_pct: pd.Series,
                                      peer_median_inst_pct: pd.Series) -> pd.Series:
    """inst_pct gap as fraction of peer median pct."""
    return _safe_div(_gap(inst_pct, peer_median_inst_pct),
                     peer_median_inst_pct.replace(0, np.nan))


def hcd_079_inst_shares_gap(inst_shares: pd.Series,
                             peer_median_inst_shares: pd.Series) -> pd.Series:
    """Arithmetic gap of inst_shares vs peer median."""
    return _gap(inst_shares, peer_median_inst_shares)


def hcd_080_inst_shares_gap_pct(inst_shares: pd.Series,
                                 peer_median_inst_shares: pd.Series) -> pd.Series:
    """inst_shares gap as fraction of peer median inst_shares."""
    return _safe_div(_gap(inst_shares, peer_median_inst_shares),
                     peer_median_inst_shares.replace(0, np.nan))


# --- New/closed positions relative to peer ---------------------------------

def hcd_081_new_pos_ratio(new_positions: pd.Series,
                           peer_median_new_positions: pd.Series) -> pd.Series:
    """Ratio of ticker new positions to peer median new positions."""
    return _rel_ratio(new_positions, peer_median_new_positions)


def hcd_082_closed_pos_ratio(closed_positions: pd.Series,
                              peer_median_closed_positions: pd.Series) -> pd.Series:
    """Ratio of ticker closed positions to peer median closed positions."""
    return _rel_ratio(closed_positions, peer_median_closed_positions)


def hcd_083_net_flow_ratio(new_positions: pd.Series,
                            peer_median_new_positions: pd.Series,
                            closed_positions: pd.Series,
                            peer_median_closed_positions: pd.Series) -> pd.Series:
    """Net relative flow: new_pos_ratio - closed_pos_ratio vs peer."""
    return (_rel_ratio(new_positions, peer_median_new_positions) -
            _rel_ratio(closed_positions, peer_median_closed_positions))


def hcd_084_net_flow_gap(new_positions: pd.Series,
                          peer_median_new_positions: pd.Series,
                          closed_positions: pd.Series,
                          peer_median_closed_positions: pd.Series) -> pd.Series:
    """Net flow gap: (new-peer_new) - (closed-peer_closed)."""
    return (_gap(new_positions, peer_median_new_positions) -
            _gap(closed_positions, peer_median_closed_positions))


def hcd_085_closed_pos_log_rel(closed_positions: pd.Series,
                                peer_median_closed_positions: pd.Series) -> pd.Series:
    """Log-relative closed positions vs peer median."""
    return _log_rel(closed_positions, peer_median_closed_positions)


def hcd_086_new_pos_log_rel(new_positions: pd.Series,
                             peer_median_new_positions: pd.Series) -> pd.Series:
    """Log-relative new positions vs peer median."""
    return _log_rel(new_positions, peer_median_new_positions)


# --- Rolling QoQ dynamics of new/closed relative metrics ------------------

def hcd_087_new_pos_ratio_qoq(new_positions: pd.Series,
                               peer_median_new_positions: pd.Series) -> pd.Series:
    """QoQ change in new-positions ratio vs peer."""
    r = _rel_ratio(new_positions, peer_median_new_positions)
    return r - r.shift(_TD_QTR)


def hcd_088_closed_pos_ratio_qoq(closed_positions: pd.Series,
                                   peer_median_closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed-positions ratio vs peer."""
    r = _rel_ratio(closed_positions, peer_median_closed_positions)
    return r - r.shift(_TD_QTR)


def hcd_089_net_flow_ratio_qoq(new_positions: pd.Series,
                                 peer_median_new_positions: pd.Series,
                                 closed_positions: pd.Series,
                                 peer_median_closed_positions: pd.Series) -> pd.Series:
    """QoQ change in net relative flow (new_ratio - closed_ratio)."""
    flow = (_rel_ratio(new_positions, peer_median_new_positions) -
            _rel_ratio(closed_positions, peer_median_closed_positions))
    return flow - flow.shift(_TD_QTR)


def hcd_090_new_pos_ratio_rolling_mean_1y(new_positions: pd.Series,
                                           peer_median_new_positions: pd.Series) -> pd.Series:
    """1-year rolling mean of new-positions ratio vs peer."""
    r = _rel_ratio(new_positions, peer_median_new_positions)
    return _rolling_mean(r, _TD_YEAR)


def hcd_091_closed_pos_ratio_rolling_mean_1y(closed_positions: pd.Series,
                                              peer_median_closed_positions: pd.Series) -> pd.Series:
    """1-year rolling mean of closed-positions ratio vs peer."""
    r = _rel_ratio(closed_positions, peer_median_closed_positions)
    return _rolling_mean(r, _TD_YEAR)


def hcd_092_closed_pos_ratio_zscore_1y(closed_positions: pd.Series,
                                        peer_median_closed_positions: pd.Series) -> pd.Series:
    """1-year rolling z-score of closed-positions ratio vs peer."""
    r = _rel_ratio(closed_positions, peer_median_closed_positions)
    return _zscore_rolling(r, _TD_YEAR)


def hcd_093_new_pos_ratio_zscore_1y(new_positions: pd.Series,
                                     peer_median_new_positions: pd.Series) -> pd.Series:
    """1-year rolling z-score of new-positions ratio vs peer."""
    r = _rel_ratio(new_positions, peer_median_new_positions)
    return _zscore_rolling(r, _TD_YEAR)


# --- Ratio drawdown and recovery features ----------------------------------

def hcd_094_ratio_drawdown_from_1y_max(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Drawdown of holder-breadth ratio from 1-year rolling max."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mx = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(ratio, mx.replace(0, np.nan)) - 1.0


def hcd_095_ratio_recovery_from_1y_min(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Recovery of holder-breadth ratio from 1-year rolling min."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mn = _rolling_min(ratio, _TD_YEAR)
    return ratio - mn


def hcd_096_ratio_range_1y(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling range (max-min) of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_max(ratio, _TD_YEAR) - _rolling_min(ratio, _TD_YEAR)


def hcd_097_ratio_position_in_range_1y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Position of current ratio within 1-year range: (cur-min)/(max-min)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mn = _rolling_min(ratio, _TD_YEAR)
    mx = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(ratio - mn, (mx - mn).replace(0, np.nan))


def hcd_098_ratio_position_in_range_2y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Position of current ratio within 2-year range."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mn = _rolling_min(ratio, _TD_2Y)
    mx = _rolling_max(ratio, _TD_2Y)
    return _safe_div(ratio - mn, (mx - mn).replace(0, np.nan))


def hcd_099_ratio_position_in_range_3y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Position of current ratio within 3-year range."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mn = _rolling_min(ratio, _TD_3Y)
    mx = _rolling_max(ratio, _TD_3Y)
    return _safe_div(ratio - mn, (mx - mn).replace(0, np.nan))


# --- Cross-field relative breadth scores -----------------------------------

def hcd_100_holders_vs_shares_gap_ratio(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series,
                                         inst_shares: pd.Series,
                                         peer_median_inst_shares: pd.Series) -> pd.Series:
    """Log-rel holders minus log-rel shares: breadth vs depth divergence."""
    return (_log_rel(inst_holders, peer_median_inst_holders) -
            _log_rel(inst_shares, peer_median_inst_shares))


def hcd_101_inst_pct_below_peer_flag(inst_pct: pd.Series,
                                      peer_median_inst_pct: pd.Series) -> pd.Series:
    """Binary 1 if ticker inst_pct is below peer median, else 0."""
    return (inst_pct < peer_median_inst_pct).astype(float)


def hcd_102_inst_pct_below_peer_fraction_1y(inst_pct: pd.Series,
                                             peer_median_inst_pct: pd.Series) -> pd.Series:
    """Fraction of days in past year where ticker inst_pct < peer median."""
    below = (inst_pct < peer_median_inst_pct).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def hcd_103_both_below_peer_flag(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series,
                                  inst_pct: pd.Series,
                                  peer_median_inst_pct: pd.Series) -> pd.Series:
    """1 if both inst_holders AND inst_pct are below their peer medians."""
    h_below = (inst_holders < peer_median_inst_holders).astype(float)
    p_below = (inst_pct < peer_median_inst_pct).astype(float)
    return (h_below * p_below)


def hcd_104_both_below_peer_fraction_1y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series,
                                         inst_pct: pd.Series,
                                         peer_median_inst_pct: pd.Series) -> pd.Series:
    """Fraction of days in past year where both holders and pct below peer."""
    both = ((inst_holders < peer_median_inst_holders) &
            (inst_pct < peer_median_inst_pct)).astype(float)
    return _rolling_mean(both, _TD_YEAR)


# --- Peer-gap normalized by rolling std ------------------------------------

def hcd_105_ratio_normalized_by_std_1y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio divided by its 1-year rolling std."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    sd = _rolling_std(ratio, _TD_YEAR)
    return _safe_div(ratio, sd)


def hcd_106_gap_normalized_by_peer_1y(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """Gap (own-peer) normalized by 1-year rolling std of peer median."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    peer_sd = _rolling_std(peer_median_inst_holders, _TD_YEAR)
    return _safe_div(gap, peer_sd)


def hcd_107_inst_pct_gap_normalized_1y(inst_pct: pd.Series,
                                        peer_median_inst_pct: pd.Series) -> pd.Series:
    """inst_pct gap normalized by 1-year rolling std of peer median pct."""
    gap = _gap(inst_pct, peer_median_inst_pct)
    peer_sd = _rolling_std(peer_median_inst_pct, _TD_YEAR)
    return _safe_div(gap, peer_sd)


# --- Quartile-relative flags -----------------------------------------------

def hcd_108_ratio_below_0p5(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """Flag: ratio < 0.5 (ticker has <50% of peer-median holder breadth)."""
    return (_rel_ratio(inst_holders, peer_median_inst_holders) < 0.5).astype(float)


def hcd_109_ratio_below_0p75(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """Flag: ratio < 0.75 (ticker has <75% of peer-median holder breadth)."""
    return (_rel_ratio(inst_holders, peer_median_inst_holders) < 0.75).astype(float)


def hcd_110_ratio_above_1p5(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """Flag: ratio > 1.5 (ticker has >150% of peer-median holder breadth)."""
    return (_rel_ratio(inst_holders, peer_median_inst_holders) > 1.5).astype(float)


def hcd_111_ratio_below_0p5_fraction_1y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of past 1 year where ratio < 0.5."""
    flag = (_rel_ratio(inst_holders, peer_median_inst_holders) < 0.5).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


def hcd_112_ratio_below_0p75_fraction_1y(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of past 1 year where ratio < 0.75."""
    flag = (_rel_ratio(inst_holders, peer_median_inst_holders) < 0.75).astype(float)
    return _rolling_mean(flag, _TD_YEAR)


# --- Velocity and momentum of relative series ------------------------------

def hcd_113_ratio_momentum_1q(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-quarter momentum of holder-breadth ratio (ratio / ratio[63d ago] - 1)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    prev = ratio.shift(_TD_QTR)
    return _safe_div(ratio - prev, prev.abs().replace(0, np.nan))


def hcd_114_ratio_momentum_2q(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter momentum of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    prev = ratio.shift(_TD_2Q)
    return _safe_div(ratio - prev, prev.abs().replace(0, np.nan))


def hcd_115_ratio_momentum_1y(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year momentum of holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    prev = ratio.shift(_TD_YEAR)
    return _safe_div(ratio - prev, prev.abs().replace(0, np.nan))


def hcd_116_log_rel_momentum_1q(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-quarter change in log-relative holder breadth (log-momentum)."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - lr.shift(_TD_QTR)


def hcd_117_log_rel_momentum_2q(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter change in log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - lr.shift(_TD_2Q)


def hcd_118_log_rel_momentum_1y(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year change in log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - lr.shift(_TD_YEAR)


# --- Ratio trend strength (R-squared proxy) --------------------------------

def hcd_119_ratio_trend_strength_1y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """Correlation of ratio with time index over trailing 1 year (trend signal)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    t = pd.Series(np.arange(len(ratio)), index=ratio.index, dtype=float)
    def _corr(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xv = np.arange(len(y), dtype=float)[mask]
        yv = y[mask]
        if xv.std() < _EPS or yv.std() < _EPS:
            return np.nan
        return np.corrcoef(xv, yv)[0, 1]
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(_corr, raw=True)


def hcd_120_ratio_trend_strength_2y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """Correlation of ratio with time index over trailing 2 years."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    def _corr(y):
        mask = ~np.isnan(y)
        if mask.sum() < 4:
            return np.nan
        xv = np.arange(len(y), dtype=float)[mask]
        yv = y[mask]
        if xv.std() < _EPS or yv.std() < _EPS:
            return np.nan
        return np.corrcoef(xv, yv)[0, 1]
    return ratio.rolling(_TD_2Y, min_periods=_TD_QTR).apply(_corr, raw=True)


# --- Peer-median own-vs-peer rolling correlation --------------------------

def hcd_121_holders_vs_peer_corr_1y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling Pearson correlation between own and peer holder counts."""
    def _corr(w_own, w_peer):
        mask = ~(np.isnan(w_own) | np.isnan(w_peer))
        if mask.sum() < 4:
            return np.nan
        xv, yv = w_own[mask], w_peer[mask]
        if xv.std() < _EPS or yv.std() < _EPS:
            return np.nan
        return np.corrcoef(xv, yv)[0, 1]
    combined = pd.concat([inst_holders, peer_median_inst_holders], axis=1)
    combined.columns = ["own", "peer"]
    return combined.rolling(_TD_YEAR, min_periods=_TD_QTR).apply(
        lambda x: x[0], raw=True  # placeholder; done with corr below
    )["own"] * 0 + combined["own"].rolling(_TD_YEAR).corr(combined["peer"])


def hcd_122_holders_vs_peer_corr_2y(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling Pearson correlation between own and peer holder counts."""
    return inst_holders.rolling(_TD_2Y, min_periods=_TD_QTR).corr(peer_median_inst_holders)


# --- EWM relative features with various spans ------------------------------

def hcd_123_ratio_ewm_span10(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM span=10 td of holder-breadth ratio (very short trend)."""
    return _ewm_mean(_rel_ratio(inst_holders, peer_median_inst_holders), 10)


def hcd_124_ratio_ewm_span21(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM span=21 td of holder-breadth ratio (~1 month)."""
    return _ewm_mean(_rel_ratio(inst_holders, peer_median_inst_holders), 21)


def hcd_125_ratio_ewm_deviation_2q(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Ratio deviation from EWM(2q): distance from medium-term trend."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _ewm_mean(ratio, _TD_2Q)


def hcd_126_ratio_ewm_deviation_1y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Ratio deviation from EWM(1y): distance from long-term trend."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _ewm_mean(ratio, _TD_YEAR)


def hcd_127_log_rel_ewm_2q(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(2q) of log-relative holder breadth."""
    return _ewm_mean(_log_rel(inst_holders, peer_median_inst_holders), _TD_2Q)


def hcd_128_log_rel_ewm_1y(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1y) of log-relative holder breadth."""
    return _ewm_mean(_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)


# --- Normalized breadth collapse indicators --------------------------------

def hcd_129_ratio_collapse_score(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Collapse score: -log_rel clipped to [0, inf] — larger = more collapsed vs peer."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return (-lr).clip(lower=0.0)


def hcd_130_ratio_collapse_score_ewm(inst_holders: pd.Series,
                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM(1q) of collapse score (smooth capitulation breadth signal)."""
    score = (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)
    return _ewm_mean(score, _TD_QTR)


def hcd_131_ratio_collapse_score_1y_max(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling max of collapse score (peak relative breadth collapse)."""
    score = (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)
    return _rolling_max(score, _TD_YEAR)


def hcd_132_ratio_collapse_score_zscore_1y(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year z-score of collapse score."""
    score = (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)
    return _zscore_rolling(score, _TD_YEAR)


# --- Peer-median divergence features --------------------------------------

def hcd_133_peer_holder_trend_qoq(peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in peer median holder count itself (peer trend context)."""
    return peer_median_inst_holders - peer_median_inst_holders.shift(_TD_QTR)


def hcd_134_own_vs_peer_trend_divergence_qoq(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in own holders minus QoQ change in peer median holders."""
    own_chg = inst_holders - inst_holders.shift(_TD_QTR)
    peer_chg = peer_median_inst_holders - peer_median_inst_holders.shift(_TD_QTR)
    return own_chg - peer_chg


def hcd_135_own_vs_peer_trend_divergence_yoy(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY change in own holders minus YoY change in peer median holders."""
    own_chg = inst_holders - inst_holders.shift(_TD_YEAR)
    peer_chg = peer_median_inst_holders - peer_median_inst_holders.shift(_TD_YEAR)
    return own_chg - peer_chg


def hcd_136_peer_holder_yoy_growth(peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY growth of peer median holder count (sector-wide breadth trend)."""
    prev = peer_median_inst_holders.shift(_TD_YEAR)
    return _safe_div(peer_median_inst_holders - prev, prev.abs().replace(0, np.nan))


def hcd_137_own_growth_vs_peer_growth(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """Own YoY growth minus peer YoY growth (relative growth rate)."""
    own_g = _safe_div(inst_holders - inst_holders.shift(_TD_YEAR),
                      inst_holders.shift(_TD_YEAR).abs().replace(0, np.nan))
    peer_g = _safe_div(peer_median_inst_holders - peer_median_inst_holders.shift(_TD_YEAR),
                       peer_median_inst_holders.shift(_TD_YEAR).abs().replace(0, np.nan))
    return own_g - peer_g


# --- Ratio regime features (sustained below/above peer) -------------------

def hcd_138_ratio_below_1_consec(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Consecutive trading days where holder-breadth ratio < 1.0."""
    below = (_rel_ratio(inst_holders, peer_median_inst_holders) < 1.0).astype(int)
    streak = below * (below.groupby((below != below.shift()).cumsum()).cumcount() + 1)
    return streak.astype(float)


def hcd_139_ratio_below_075_consec(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Consecutive trading days where holder-breadth ratio < 0.75."""
    below = (_rel_ratio(inst_holders, peer_median_inst_holders) < 0.75).astype(int)
    streak = below * (below.groupby((below != below.shift()).cumsum()).cumcount() + 1)
    return streak.astype(float)


def hcd_140_ratio_above_1_consec(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """Consecutive trading days where holder-breadth ratio > 1.0."""
    above = (_rel_ratio(inst_holders, peer_median_inst_holders) > 1.0).astype(int)
    streak = above * (above.groupby((above != above.shift()).cumsum()).cumcount() + 1)
    return streak.astype(float)


# --- Cross-peer metrics on inst_pct ----------------------------------------

def hcd_141_inst_pct_ratio_rolling_mean_2y(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-year rolling mean of inst_pct ratio vs peer."""
    return _rolling_mean(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_2Y)


def hcd_142_inst_pct_ratio_rolling_min_1y(inst_pct: pd.Series,
                                           peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling minimum of inst_pct ratio vs peer."""
    return _rolling_min(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_YEAR)


def hcd_143_inst_pct_ratio_rank_2y(inst_pct: pd.Series,
                                    peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of inst_pct ratio vs peer."""
    return _rolling_rank_pct(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_2Y)


def hcd_144_inst_pct_ratio_collapse_score(inst_pct: pd.Series,
                                           peer_median_inst_pct: pd.Series) -> pd.Series:
    """Inst_pct collapse score vs peer: -log_rel clipped to [0, inf]."""
    return (-_log_rel(inst_pct, peer_median_inst_pct)).clip(lower=0.0)


def hcd_145_inst_pct_gap_rolling_min_1y(inst_pct: pd.Series,
                                         peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling minimum of inst_pct gap (own-peer)."""
    return _rolling_min(_gap(inst_pct, peer_median_inst_pct), _TD_YEAR)


# --- Combined multi-metric collapse score ----------------------------------

def hcd_146_triple_collapse_score(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series,
                                   inst_pct: pd.Series,
                                   peer_median_inst_pct: pd.Series,
                                   inst_shares: pd.Series,
                                   peer_median_inst_shares: pd.Series) -> pd.Series:
    """Sum of collapse scores for holders, pct, and shares — all vs peer."""
    s1 = (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)
    s2 = (-_log_rel(inst_pct, peer_median_inst_pct)).clip(lower=0.0)
    s3 = (-_log_rel(inst_shares, peer_median_inst_shares)).clip(lower=0.0)
    return s1 + s2 + s3


def hcd_147_triple_collapse_score_ewm_1q(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series,
                                          inst_pct: pd.Series,
                                          peer_median_inst_pct: pd.Series,
                                          inst_shares: pd.Series,
                                          peer_median_inst_shares: pd.Series) -> pd.Series:
    """EWM(1q) of triple collapse score."""
    s1 = (-_log_rel(inst_holders, peer_median_inst_holders)).clip(lower=0.0)
    s2 = (-_log_rel(inst_pct, peer_median_inst_pct)).clip(lower=0.0)
    s3 = (-_log_rel(inst_shares, peer_median_inst_shares)).clip(lower=0.0)
    return _ewm_mean(s1 + s2 + s3, _TD_QTR)


# --- Ratio mean-reversion signals -----------------------------------------

def hcd_148_ratio_mean_reversion_gap_1y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """Current ratio minus 1-year rolling mean (mean-reversion gap)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def hcd_149_ratio_mean_reversion_gap_2y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """Current ratio minus 2-year rolling mean."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _rolling_mean(ratio, _TD_2Y)


def hcd_150_log_rel_mean_reversion_gap_1y(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """Log-relative holder breadth minus its 1-year rolling mean."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - _rolling_mean(lr, _TD_YEAR)


# ===========================================================================
# Feature Functions 176 – 200
# ===========================================================================

# --- mean-reversion and regime features on additional fields -----------------

def hcd_176_inst_pct_ratio_mean_reversion_1y(inst_pct: pd.Series,
                                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """inst_pct ratio minus its 1-year rolling mean (mean-reversion gap)."""
    r = _rel_ratio(inst_pct, peer_median_inst_pct)
    return r - _rolling_mean(r, _TD_YEAR)


def hcd_177_inst_pct_ratio_mean_reversion_2y(inst_pct: pd.Series,
                                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """inst_pct ratio minus its 2-year rolling mean."""
    r = _rel_ratio(inst_pct, peer_median_inst_pct)
    return r - _rolling_mean(r, _TD_2Y)


def hcd_178_inst_pct_gap_mean_reversion_1y(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """inst_pct gap (own-peer) minus its 1-year rolling mean."""
    g = _gap(inst_pct, peer_median_inst_pct)
    return g - _rolling_mean(g, _TD_YEAR)


def hcd_179_inst_shares_mean_reversion_1y(inst_shares: pd.Series,
                                           peer_median_inst_shares: pd.Series) -> pd.Series:
    """inst_shares ratio minus its 1-year rolling mean."""
    r = _rel_ratio(inst_shares, peer_median_inst_shares)
    return r - _rolling_mean(r, _TD_YEAR)


def hcd_180_inst_shares_log_rel_ewm_1q(inst_shares: pd.Series,
                                        peer_median_inst_shares: pd.Series) -> pd.Series:
    """EWM(1q) of log-relative inst_shares vs peer."""
    return _ewm_mean(_log_rel(inst_shares, peer_median_inst_shares), _TD_QTR)


# --- peer-median level analytics (sector context) ---------------------------

def hcd_181_peer_inst_pct_qoq_change(peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in peer median inst_pct (sector ownership trend)."""
    return peer_median_inst_pct - peer_median_inst_pct.shift(_TD_QTR)


def hcd_182_peer_inst_pct_yoy_change(peer_median_inst_pct: pd.Series) -> pd.Series:
    """YoY change in peer median inst_pct (sector-wide ownership trend)."""
    return peer_median_inst_pct - peer_median_inst_pct.shift(_TD_YEAR)


def hcd_183_own_inst_pct_vs_peer_trend_qoq(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """QoQ change in own inst_pct minus QoQ change in peer median inst_pct."""
    own_chg = inst_pct - inst_pct.shift(_TD_QTR)
    peer_chg = peer_median_inst_pct - peer_median_inst_pct.shift(_TD_QTR)
    return own_chg - peer_chg


def hcd_184_own_inst_pct_vs_peer_trend_yoy(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """YoY change in own inst_pct minus YoY change in peer median inst_pct."""
    own_chg = inst_pct - inst_pct.shift(_TD_YEAR)
    peer_chg = peer_median_inst_pct - peer_median_inst_pct.shift(_TD_YEAR)
    return own_chg - peer_chg


def hcd_185_peer_inst_shares_qoq_change(peer_median_inst_shares: pd.Series) -> pd.Series:
    """QoQ change in peer median inst_shares (sector buying/selling context)."""
    return peer_median_inst_shares - peer_median_inst_shares.shift(_TD_QTR)


# --- ratio rolling max / range analytics ------------------------------------

def hcd_186_ratio_rolling_max_2y(inst_holders: pd.Series,
                                  peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling maximum of holder-breadth ratio."""
    return _rolling_max(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_187_ratio_range_2y(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling range (max-min) of holder-breadth ratio."""
    r = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _rolling_max(r, _TD_2Y) - _rolling_min(r, _TD_2Y)


def hcd_188_log_rel_rolling_max_1y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling maximum of log-relative holder breadth."""
    return _rolling_max(_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)


def hcd_189_log_rel_rolling_std_2y(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling std of log-relative holder breadth."""
    return _rolling_std(_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_190_gap_rolling_max_1y(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling maximum of holder-count gap (own-peer)."""
    return _rolling_max(_gap(inst_holders, peer_median_inst_holders), _TD_YEAR)


# --- expanding-window analytics on additional series -----------------------

def hcd_191_inst_pct_ratio_expanding_zscore(inst_pct: pd.Series,
                                             peer_median_inst_pct: pd.Series) -> pd.Series:
    """Expanding z-score of inst_pct ratio vs peer (lifetime perspective)."""
    r = _rel_ratio(inst_pct, peer_median_inst_pct)
    mu = r.expanding(min_periods=2).mean()
    sd = r.expanding(min_periods=2).std()
    return _safe_div(r - mu, sd)


def hcd_192_inst_shares_ratio_expanding_mean(inst_shares: pd.Series,
                                              peer_median_inst_shares: pd.Series) -> pd.Series:
    """Expanding mean of inst_shares ratio vs peer."""
    return _rel_ratio(inst_shares, peer_median_inst_shares).expanding(min_periods=1).mean()


def hcd_193_ratio_expanding_min(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding minimum of holder-breadth ratio (all-time floor vs peer)."""
    return _rel_ratio(inst_holders, peer_median_inst_holders).expanding(min_periods=1).min()


def hcd_194_log_rel_expanding_zscore(inst_holders: pd.Series,
                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding z-score of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    mu = lr.expanding(min_periods=2).mean()
    sd = lr.expanding(min_periods=2).std()
    return _safe_div(lr - mu, sd)


# --- below-peer fraction / streak on additional fields ----------------------

def hcd_195_inst_pct_consec_below_peer(inst_pct: pd.Series,
                                        peer_median_inst_pct: pd.Series) -> pd.Series:
    """Consecutive trading days where inst_pct < peer median."""
    below = (inst_pct < peer_median_inst_pct).astype(int)
    streak = below * (below.groupby((below != below.shift()).cumsum()).cumcount() + 1)
    return streak.astype(float)


def hcd_196_inst_pct_below_peer_fraction_2y(inst_pct: pd.Series,
                                             peer_median_inst_pct: pd.Series) -> pd.Series:
    """Fraction of days in past 2 years where inst_pct < peer median."""
    return _rolling_mean((inst_pct < peer_median_inst_pct).astype(float), _TD_2Y)


def hcd_197_inst_shares_below_peer_flag(inst_shares: pd.Series,
                                         peer_median_inst_shares: pd.Series) -> pd.Series:
    """Binary 1 if ticker inst_shares < peer median inst_shares, else 0."""
    return (inst_shares < peer_median_inst_shares).astype(float)


def hcd_198_inst_shares_below_peer_fraction_1y(inst_shares: pd.Series,
                                                peer_median_inst_shares: pd.Series) -> pd.Series:
    """Fraction of past 1 year where inst_shares < peer median."""
    return _rolling_mean((inst_shares < peer_median_inst_shares).astype(float), _TD_YEAR)


def hcd_199_new_pos_ratio_yoy(new_positions: pd.Series,
                               peer_median_new_positions: pd.Series) -> pd.Series:
    """YoY change in new-positions ratio vs peer."""
    r = _rel_ratio(new_positions, peer_median_new_positions)
    return r - r.shift(_TD_YEAR)


def hcd_200_closed_pos_ratio_yoy(closed_positions: pd.Series,
                                  peer_median_closed_positions: pd.Series) -> pd.Series:
    """YoY change in closed-positions ratio vs peer."""
    r = _rel_ratio(closed_positions, peer_median_closed_positions)
    return r - r.shift(_TD_YEAR)


# ===========================================================================
# Registry
# ===========================================================================
HOLDER_COUNT_DYNAMICS_REGISTRY_076_150 = {
    "hcd_076_inst_holders_ratio_clipped": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_076_inst_holders_ratio_clipped,
    },
    "hcd_077_inst_holders_gap_abs": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_077_inst_holders_gap_abs,
    },
    "hcd_078_inst_pct_gap_pct_of_peer": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_078_inst_pct_gap_pct_of_peer,
    },
    "hcd_079_inst_shares_gap": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_079_inst_shares_gap,
    },
    "hcd_080_inst_shares_gap_pct": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_080_inst_shares_gap_pct,
    },
    "hcd_081_new_pos_ratio": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_081_new_pos_ratio,
    },
    "hcd_082_closed_pos_ratio": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_082_closed_pos_ratio,
    },
    "hcd_083_net_flow_ratio": {
        "inputs": ["new_positions", "peer_median_new_positions",
                   "closed_positions", "peer_median_closed_positions"],
        "func": hcd_083_net_flow_ratio,
    },
    "hcd_084_net_flow_gap": {
        "inputs": ["new_positions", "peer_median_new_positions",
                   "closed_positions", "peer_median_closed_positions"],
        "func": hcd_084_net_flow_gap,
    },
    "hcd_085_closed_pos_log_rel": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_085_closed_pos_log_rel,
    },
    "hcd_086_new_pos_log_rel": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_086_new_pos_log_rel,
    },
    "hcd_087_new_pos_ratio_qoq": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_087_new_pos_ratio_qoq,
    },
    "hcd_088_closed_pos_ratio_qoq": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_088_closed_pos_ratio_qoq,
    },
    "hcd_089_net_flow_ratio_qoq": {
        "inputs": ["new_positions", "peer_median_new_positions",
                   "closed_positions", "peer_median_closed_positions"],
        "func": hcd_089_net_flow_ratio_qoq,
    },
    "hcd_090_new_pos_ratio_rolling_mean_1y": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_090_new_pos_ratio_rolling_mean_1y,
    },
    "hcd_091_closed_pos_ratio_rolling_mean_1y": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_091_closed_pos_ratio_rolling_mean_1y,
    },
    "hcd_092_closed_pos_ratio_zscore_1y": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_092_closed_pos_ratio_zscore_1y,
    },
    "hcd_093_new_pos_ratio_zscore_1y": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_093_new_pos_ratio_zscore_1y,
    },
    "hcd_094_ratio_drawdown_from_1y_max": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_094_ratio_drawdown_from_1y_max,
    },
    "hcd_095_ratio_recovery_from_1y_min": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_095_ratio_recovery_from_1y_min,
    },
    "hcd_096_ratio_range_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_096_ratio_range_1y,
    },
    "hcd_097_ratio_position_in_range_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_097_ratio_position_in_range_1y,
    },
    "hcd_098_ratio_position_in_range_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_098_ratio_position_in_range_2y,
    },
    "hcd_099_ratio_position_in_range_3y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_099_ratio_position_in_range_3y,
    },
    "hcd_100_holders_vs_shares_gap_ratio": {
        "inputs": ["inst_holders", "peer_median_inst_holders",
                   "inst_shares", "peer_median_inst_shares"],
        "func": hcd_100_holders_vs_shares_gap_ratio,
    },
    "hcd_101_inst_pct_below_peer_flag": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_101_inst_pct_below_peer_flag,
    },
    "hcd_102_inst_pct_below_peer_fraction_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_102_inst_pct_below_peer_fraction_1y,
    },
    "hcd_103_both_below_peer_flag": {
        "inputs": ["inst_holders", "peer_median_inst_holders",
                   "inst_pct", "peer_median_inst_pct"],
        "func": hcd_103_both_below_peer_flag,
    },
    "hcd_104_both_below_peer_fraction_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders",
                   "inst_pct", "peer_median_inst_pct"],
        "func": hcd_104_both_below_peer_fraction_1y,
    },
    "hcd_105_ratio_normalized_by_std_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_105_ratio_normalized_by_std_1y,
    },
    "hcd_106_gap_normalized_by_peer_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_106_gap_normalized_by_peer_1y,
    },
    "hcd_107_inst_pct_gap_normalized_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_107_inst_pct_gap_normalized_1y,
    },
    "hcd_108_ratio_below_0p5": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_108_ratio_below_0p5,
    },
    "hcd_109_ratio_below_0p75": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_109_ratio_below_0p75,
    },
    "hcd_110_ratio_above_1p5": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_110_ratio_above_1p5,
    },
    "hcd_111_ratio_below_0p5_fraction_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_111_ratio_below_0p5_fraction_1y,
    },
    "hcd_112_ratio_below_0p75_fraction_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_112_ratio_below_0p75_fraction_1y,
    },
    "hcd_113_ratio_momentum_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_113_ratio_momentum_1q,
    },
    "hcd_114_ratio_momentum_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_114_ratio_momentum_2q,
    },
    "hcd_115_ratio_momentum_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_115_ratio_momentum_1y,
    },
    "hcd_116_log_rel_momentum_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_116_log_rel_momentum_1q,
    },
    "hcd_117_log_rel_momentum_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_117_log_rel_momentum_2q,
    },
    "hcd_118_log_rel_momentum_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_118_log_rel_momentum_1y,
    },
    "hcd_119_ratio_trend_strength_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_119_ratio_trend_strength_1y,
    },
    "hcd_120_ratio_trend_strength_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_120_ratio_trend_strength_2y,
    },
    "hcd_121_holders_vs_peer_corr_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_121_holders_vs_peer_corr_1y,
    },
    "hcd_122_holders_vs_peer_corr_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_122_holders_vs_peer_corr_2y,
    },
    "hcd_123_ratio_ewm_span10": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_123_ratio_ewm_span10,
    },
    "hcd_124_ratio_ewm_span21": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_124_ratio_ewm_span21,
    },
    "hcd_125_ratio_ewm_deviation_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_125_ratio_ewm_deviation_2q,
    },
    "hcd_126_ratio_ewm_deviation_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_126_ratio_ewm_deviation_1y,
    },
    "hcd_127_log_rel_ewm_2q": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_127_log_rel_ewm_2q,
    },
    "hcd_128_log_rel_ewm_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_128_log_rel_ewm_1y,
    },
    "hcd_129_ratio_collapse_score": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_129_ratio_collapse_score,
    },
    "hcd_130_ratio_collapse_score_ewm": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_130_ratio_collapse_score_ewm,
    },
    "hcd_131_ratio_collapse_score_1y_max": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_131_ratio_collapse_score_1y_max,
    },
    "hcd_132_ratio_collapse_score_zscore_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_132_ratio_collapse_score_zscore_1y,
    },
    "hcd_133_peer_holder_trend_qoq": {
        "inputs": ["peer_median_inst_holders"],
        "func": hcd_133_peer_holder_trend_qoq,
    },
    "hcd_134_own_vs_peer_trend_divergence_qoq": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_134_own_vs_peer_trend_divergence_qoq,
    },
    "hcd_135_own_vs_peer_trend_divergence_yoy": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_135_own_vs_peer_trend_divergence_yoy,
    },
    "hcd_136_peer_holder_yoy_growth": {
        "inputs": ["peer_median_inst_holders"],
        "func": hcd_136_peer_holder_yoy_growth,
    },
    "hcd_137_own_growth_vs_peer_growth": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_137_own_growth_vs_peer_growth,
    },
    "hcd_138_ratio_below_1_consec": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_138_ratio_below_1_consec,
    },
    "hcd_139_ratio_below_075_consec": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_139_ratio_below_075_consec,
    },
    "hcd_140_ratio_above_1_consec": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_140_ratio_above_1_consec,
    },
    "hcd_141_inst_pct_ratio_rolling_mean_2y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_141_inst_pct_ratio_rolling_mean_2y,
    },
    "hcd_142_inst_pct_ratio_rolling_min_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_142_inst_pct_ratio_rolling_min_1y,
    },
    "hcd_143_inst_pct_ratio_rank_2y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_143_inst_pct_ratio_rank_2y,
    },
    "hcd_144_inst_pct_ratio_collapse_score": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_144_inst_pct_ratio_collapse_score,
    },
    "hcd_145_inst_pct_gap_rolling_min_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_145_inst_pct_gap_rolling_min_1y,
    },
    "hcd_146_triple_collapse_score": {
        "inputs": ["inst_holders", "peer_median_inst_holders",
                   "inst_pct", "peer_median_inst_pct",
                   "inst_shares", "peer_median_inst_shares"],
        "func": hcd_146_triple_collapse_score,
    },
    "hcd_147_triple_collapse_score_ewm_1q": {
        "inputs": ["inst_holders", "peer_median_inst_holders",
                   "inst_pct", "peer_median_inst_pct",
                   "inst_shares", "peer_median_inst_shares"],
        "func": hcd_147_triple_collapse_score_ewm_1q,
    },
    "hcd_148_ratio_mean_reversion_gap_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_148_ratio_mean_reversion_gap_1y,
    },
    "hcd_149_ratio_mean_reversion_gap_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_149_ratio_mean_reversion_gap_2y,
    },
    "hcd_150_log_rel_mean_reversion_gap_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_150_log_rel_mean_reversion_gap_1y,
    },
    "hcd_176_inst_pct_ratio_mean_reversion_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_176_inst_pct_ratio_mean_reversion_1y,
    },
    "hcd_177_inst_pct_ratio_mean_reversion_2y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_177_inst_pct_ratio_mean_reversion_2y,
    },
    "hcd_178_inst_pct_gap_mean_reversion_1y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_178_inst_pct_gap_mean_reversion_1y,
    },
    "hcd_179_inst_shares_mean_reversion_1y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_179_inst_shares_mean_reversion_1y,
    },
    "hcd_180_inst_shares_log_rel_ewm_1q": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_180_inst_shares_log_rel_ewm_1q,
    },
    "hcd_181_peer_inst_pct_qoq_change": {
        "inputs": ["peer_median_inst_pct"],
        "func": hcd_181_peer_inst_pct_qoq_change,
    },
    "hcd_182_peer_inst_pct_yoy_change": {
        "inputs": ["peer_median_inst_pct"],
        "func": hcd_182_peer_inst_pct_yoy_change,
    },
    "hcd_183_own_inst_pct_vs_peer_trend_qoq": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_183_own_inst_pct_vs_peer_trend_qoq,
    },
    "hcd_184_own_inst_pct_vs_peer_trend_yoy": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_184_own_inst_pct_vs_peer_trend_yoy,
    },
    "hcd_185_peer_inst_shares_qoq_change": {
        "inputs": ["peer_median_inst_shares"],
        "func": hcd_185_peer_inst_shares_qoq_change,
    },
    "hcd_186_ratio_rolling_max_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_186_ratio_rolling_max_2y,
    },
    "hcd_187_ratio_range_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_187_ratio_range_2y,
    },
    "hcd_188_log_rel_rolling_max_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_188_log_rel_rolling_max_1y,
    },
    "hcd_189_log_rel_rolling_std_2y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_189_log_rel_rolling_std_2y,
    },
    "hcd_190_gap_rolling_max_1y": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_190_gap_rolling_max_1y,
    },
    "hcd_191_inst_pct_ratio_expanding_zscore": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_191_inst_pct_ratio_expanding_zscore,
    },
    "hcd_192_inst_shares_ratio_expanding_mean": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_192_inst_shares_ratio_expanding_mean,
    },
    "hcd_193_ratio_expanding_min": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_193_ratio_expanding_min,
    },
    "hcd_194_log_rel_expanding_zscore": {
        "inputs": ["inst_holders", "peer_median_inst_holders"],
        "func": hcd_194_log_rel_expanding_zscore,
    },
    "hcd_195_inst_pct_consec_below_peer": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_195_inst_pct_consec_below_peer,
    },
    "hcd_196_inst_pct_below_peer_fraction_2y": {
        "inputs": ["inst_pct", "peer_median_inst_pct"],
        "func": hcd_196_inst_pct_below_peer_fraction_2y,
    },
    "hcd_197_inst_shares_below_peer_flag": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_197_inst_shares_below_peer_flag,
    },
    "hcd_198_inst_shares_below_peer_fraction_1y": {
        "inputs": ["inst_shares", "peer_median_inst_shares"],
        "func": hcd_198_inst_shares_below_peer_fraction_1y,
    },
    "hcd_199_new_pos_ratio_yoy": {
        "inputs": ["new_positions", "peer_median_new_positions"],
        "func": hcd_199_new_pos_ratio_yoy,
    },
    "hcd_200_closed_pos_ratio_yoy": {
        "inputs": ["closed_positions", "peer_median_closed_positions"],
        "func": hcd_200_closed_pos_ratio_yoy,
    },
}
