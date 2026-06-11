"""
94_holder_count_dynamics — Extended Features 001-075
=====================================================
Domain: CROSS-SECTIONAL peer-relative breadth of institutional holder base —
        additional variants: new lookback windows, mixed-window z-scores,
        percentile/rank dynamics, streaks, EWM crossovers, drawdown of the
        peer-relative ratio, and composite peer-relative distress scores.
Asset class: US equities | Sharadar SF3 13F institutional ownership (quarterly,
        forward-filled to a daily index).
All features are backward-looking only; no forward information.

These extended features do NOT duplicate base_001_075, base_076_150,
2nd_derivatives or 3rd_derivatives — they explore different windows, thresholds,
smoothing and composite angles within the same peer-relative breadth domain.

CROSS-SECTIONAL PEER-MEDIAN INPUT CONTRACT
------------------------------------------
Every feature function receives an own-ticker daily Series PLUS a matching
`peer_median_<field>` daily Series:
  own_series          : daily pd.Series forward-filled from quarterly SF3 13F
                        data for THIS ticker (e.g. inst_holders).
  peer_median_<field> : daily pd.Series, SAME DatetimeIndex, holding the
                        sector/industry PEER-MEDIAN of that metric, computed
                        universe-wide by the pipeline for each calendar date.
The pipeline aligns both series to a common daily index before any feature
function is called. Functions never look forward.

Quarterly cadence on a trading-day axis:
  1 quarter  ~ 63 trading days  (_TD_QTR)
  1 year     ~ 252 trading days (_TD_YEAR)
  2 years    ~ 504 trading days (_TD_2Y)
  3 years    ~ 756 trading days (_TD_3Y)
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
_TD_3Q   = 189
_EPS     = 1e-9

# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------

def _align_quarterly_to_daily(series: pd.Series, window_td: int = _TD_QTR) -> pd.Series:
    """Resample a daily-ffilled series onto an approx-quarterly grid then ffill
    back to the daily index. Used when a rolling window should count quarterly
    observations rather than all daily forward-fill copies."""
    if series.empty:
        return series
    sampled = series.iloc[::window_td]
    return sampled.reindex(series.index, method="ffill")


def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    """Element-wise a / b with zero-denominator guard."""
    return a / b.replace(0, np.nan)


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    """own / peer_median ratio (>1 means above peer)."""
    return _safe_div(own, peer.replace(0, np.nan))


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    """log(own / peer) — symmetric log-relative deviation."""
    return np.log(_rel_ratio(own, peer).clip(lower=_EPS))


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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    grp = (~cond).cumsum()
    return c.groupby(grp).cumsum().astype(float)


# ===========================================================================
# Extended Features 001 - 075
# ===========================================================================

# --- Group A (001-010): Ratio rolling means / medians, new windows ---

def hcd_ext_001_ratio_rolling_mean_3q(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-quarter rolling mean of holder-breadth ratio."""
    return _rolling_mean(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Q)


def hcd_ext_002_ratio_rolling_mean_3y(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling mean of holder-breadth ratio."""
    return _rolling_mean(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Y)


def hcd_ext_003_ratio_rolling_median_2y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling median of holder-breadth ratio (robust central tendency)."""
    return _rolling_median(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_004_log_rel_rolling_mean_2y(inst_holders: pd.Series,
                                         peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling mean of log-relative holder breadth."""
    return _rolling_mean(_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_005_gap_rolling_mean_2q(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter rolling mean of holder-count gap (own-peer)."""
    return _rolling_mean(_gap(inst_holders, peer_median_inst_holders), _TD_2Q)


def hcd_ext_006_gap_rolling_median_1y(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling median of holder-count gap."""
    return _rolling_median(_gap(inst_holders, peer_median_inst_holders), _TD_YEAR)


def hcd_ext_007_inst_pct_ratio_rolling_mean_1y(inst_pct: pd.Series,
                                                peer_median_inst_pct: pd.Series) -> pd.Series:
    """1-year rolling mean of inst_pct ratio vs peer."""
    return _rolling_mean(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_YEAR)


def hcd_ext_008_inst_shares_ratio_rolling_mean_1y(inst_shares: pd.Series,
                                                   peer_median_inst_shares: pd.Series) -> pd.Series:
    """1-year rolling mean of inst_shares ratio vs peer."""
    return _rolling_mean(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_YEAR)


def hcd_ext_009_ratio_minus_rolling_mean_1y(inst_holders: pd.Series,
                                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio minus its 1-yr rolling mean (deviation from trend)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _rolling_mean(ratio, _TD_YEAR)


def hcd_ext_010_log_rel_minus_rolling_median_2y(inst_holders: pd.Series,
                                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """Log-relative breadth minus its 2-yr rolling median."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - _rolling_median(lr, _TD_2Y)


# --- Group B (011-020): Mixed-window z-scores of relative metrics ---

def hcd_ext_011_ratio_zscore_2q(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter rolling z-score of holder-breadth ratio."""
    return _zscore_rolling(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Q)


def hcd_ext_012_ratio_zscore_3q(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-quarter rolling z-score of holder-breadth ratio."""
    return _zscore_rolling(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Q)


def hcd_ext_013_log_rel_zscore_3y(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling z-score of log-relative holder breadth."""
    return _zscore_rolling(_log_rel(inst_holders, peer_median_inst_holders), _TD_3Y)


def hcd_ext_014_gap_zscore_1y(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling z-score of holder-count gap (own-peer)."""
    return _zscore_rolling(_gap(inst_holders, peer_median_inst_holders), _TD_YEAR)


def hcd_ext_015_gap_zscore_2y(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling z-score of holder-count gap."""
    return _zscore_rolling(_gap(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_016_inst_pct_ratio_zscore_2y(inst_pct: pd.Series,
                                          peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-year rolling z-score of inst_pct ratio vs peer."""
    return _zscore_rolling(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_2Y)


def hcd_ext_017_inst_shares_ratio_zscore_1y(inst_shares: pd.Series,
                                             peer_median_inst_shares: pd.Series) -> pd.Series:
    """1-year rolling z-score of inst_shares ratio vs peer."""
    return _zscore_rolling(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_YEAR)


def hcd_ext_018_inst_shares_ratio_zscore_2y(inst_shares: pd.Series,
                                             peer_median_inst_shares: pd.Series) -> pd.Series:
    """2-year rolling z-score of inst_shares ratio vs peer."""
    return _zscore_rolling(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_2Y)


def hcd_ext_019_ratio_expanding_zscore_neg_clip(inst_holders: pd.Series,
                                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding z-score of holder-breadth ratio clipped to negative side (distress only)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mu = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - mu, sd).clip(upper=0)


def hcd_ext_020_log_rel_expanding_zscore(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """Expanding all-history z-score of log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    mu = lr.expanding(min_periods=2).mean()
    sd = lr.expanding(min_periods=2).std()
    return _safe_div(lr - mu, sd)


# --- Group C (021-030): Percentile-rank dynamics of relative metrics ---

def hcd_ext_021_ratio_rank_2q(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter rolling percentile rank of holder-breadth ratio."""
    return _rolling_rank_pct(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Q)


def hcd_ext_022_ratio_rank_3q(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-quarter rolling percentile rank of holder-breadth ratio."""
    return _rolling_rank_pct(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Q)


def hcd_ext_023_log_rel_rank_2y(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of log-relative holder breadth."""
    return _rolling_rank_pct(_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_024_log_rel_rank_3y(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling percentile rank of log-relative holder breadth."""
    return _rolling_rank_pct(_log_rel(inst_holders, peer_median_inst_holders), _TD_3Y)


def hcd_ext_025_gap_rank_1y(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of holder-count gap (own-peer)."""
    return _rolling_rank_pct(_gap(inst_holders, peer_median_inst_holders), _TD_YEAR)


def hcd_ext_026_gap_rank_2y(inst_holders: pd.Series,
                             peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of holder-count gap."""
    return _rolling_rank_pct(_gap(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_027_inst_pct_ratio_rank_2y(inst_pct: pd.Series,
                                        peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-year rolling percentile rank of inst_pct ratio vs peer."""
    return _rolling_rank_pct(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_2Y)


def hcd_ext_028_inst_shares_ratio_rank_1y(inst_shares: pd.Series,
                                           peer_median_inst_shares: pd.Series) -> pd.Series:
    """1-year rolling percentile rank of inst_shares ratio vs peer."""
    return _rolling_rank_pct(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_YEAR)


def hcd_ext_029_ratio_rank_qoq_change(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """QoQ change in the 1-yr rolling percentile rank of holder-breadth ratio."""
    rank = _rolling_rank_pct(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_YEAR)
    return rank - rank.shift(_TD_QTR)


def hcd_ext_030_ratio_expanding_rank_inverse(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """1 minus expanding percentile rank of holder-breadth ratio (1 = worst ever vs peer)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    def _exp_rank(x):
        if len(x) < 2:
            return np.nan
        return (x[:-1] < x[-1]).sum() / (len(x) - 1)
    return 1.0 - ratio.expanding(min_periods=2).apply(_exp_rank, raw=True)


# --- Group D (031-040): QoQ / multi-quarter change dynamics ---

def hcd_ext_031_ratio_2q_change(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - ratio.shift(_TD_2Q)


def hcd_ext_032_ratio_3q_change(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-quarter change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - ratio.shift(_TD_3Q)


def hcd_ext_033_log_rel_2q_change(inst_holders: pd.Series,
                                   peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter change in log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - lr.shift(_TD_2Q)


def hcd_ext_034_gap_2q_change(inst_holders: pd.Series,
                               peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-quarter change in holder-count gap (own-peer)."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return gap - gap.shift(_TD_2Q)


def hcd_ext_035_ratio_2y_change(inst_holders: pd.Series,
                                 peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - ratio.shift(_TD_2Y)


def hcd_ext_036_ratio_2y_pct_change(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year percentage change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    prev = ratio.shift(_TD_2Y)
    return _safe_div(ratio - prev, prev.abs().replace(0, np.nan))


def hcd_ext_037_inst_pct_ratio_2q_change(inst_pct: pd.Series,
                                          peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-quarter change in inst_pct ratio vs peer."""
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    return ratio - ratio.shift(_TD_2Q)


def hcd_ext_038_inst_shares_ratio_qoq_change(inst_shares: pd.Series,
                                              peer_median_inst_shares: pd.Series) -> pd.Series:
    """QoQ change in inst_shares ratio vs peer."""
    ratio = _rel_ratio(inst_shares, peer_median_inst_shares)
    return ratio - ratio.shift(_TD_QTR)


def hcd_ext_039_ratio_qoq_change_zscore_2y(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year z-score of QoQ change in holder-breadth ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    chg = ratio - ratio.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_2Y)


def hcd_ext_040_log_rel_yoy_pct_change(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """YoY percentage change in log-relative holder breadth."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    prev = lr.shift(_TD_YEAR)
    return _safe_div(lr - prev, prev.abs().replace(0, np.nan))


# --- Group E (041-050): Below-peer streaks and persistence flags ---

def hcd_ext_041_consec_qtrs_above_peer(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Consecutive days holder count has been above the peer median."""
    return _consec_streak(inst_holders > peer_median_inst_holders)


def hcd_ext_042_consec_qtrs_inst_pct_below_peer(inst_pct: pd.Series,
                                                 peer_median_inst_pct: pd.Series) -> pd.Series:
    """Consecutive days inst_pct has been below the peer median."""
    return _consec_streak(inst_pct < peer_median_inst_pct)


def hcd_ext_043_consec_qtrs_shares_below_peer(inst_shares: pd.Series,
                                               peer_median_inst_shares: pd.Series) -> pd.Series:
    """Consecutive days inst_shares has been below the peer median."""
    return _consec_streak(inst_shares < peer_median_inst_shares)


def hcd_ext_044_max_below_peer_streak_2y(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """Longest below-peer-median streak within trailing 2 years."""
    streak = _consec_streak(inst_holders < peer_median_inst_holders)
    return _rolling_max(streak, _TD_2Y)


def hcd_ext_045_below_peer_fraction_3y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of trailing 3 years that holder count was below peer median."""
    below = (inst_holders < peer_median_inst_holders).astype(float)
    return _rolling_mean(below, _TD_3Y)


def hcd_ext_046_below_peer_fraction_2q(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """Fraction of trailing 2 quarters that holder count was below peer median."""
    below = (inst_holders < peer_median_inst_holders).astype(float)
    return _rolling_mean(below, _TD_2Q)


def hcd_ext_047_inst_pct_below_peer_fraction_1y(inst_pct: pd.Series,
                                                 peer_median_inst_pct: pd.Series) -> pd.Series:
    """Fraction of trailing year that inst_pct was below peer median."""
    below = (inst_pct < peer_median_inst_pct).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def hcd_ext_048_below_peer_days_count_1y(inst_holders: pd.Series,
                                          peer_median_inst_holders: pd.Series) -> pd.Series:
    """Count of trailing-year days where holder count was below peer median."""
    below = (inst_holders < peer_median_inst_holders).astype(float)
    return _rolling_sum(below, _TD_YEAR)


def hcd_ext_049_far_below_peer_flag(inst_holders: pd.Series,
                                     peer_median_inst_holders: pd.Series) -> pd.Series:
    """1 if holder count is below 50% of the peer median (deep breadth deficit)."""
    return (_rel_ratio(inst_holders, peer_median_inst_holders) < 0.5).astype(float)


def hcd_ext_050_consec_days_ratio_falling(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """Consecutive days the holder-breadth ratio fell below its QoQ-prior value."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _consec_streak(ratio < ratio.shift(_TD_QTR))


# --- Group F (051-060): EWM smoothing and crossovers of relative metrics ---

def hcd_ext_051_ratio_ewm_3q(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=3 quarters) of holder-breadth ratio."""
    return _ewm_mean(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Q)


def hcd_ext_052_ratio_ewm_2y(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=2 years) of holder-breadth ratio."""
    return _ewm_mean(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_053_log_rel_ewm_1y(inst_holders: pd.Series,
                                peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=1 year) of log-relative holder breadth."""
    return _ewm_mean(_log_rel(inst_holders, peer_median_inst_holders), _TD_YEAR)


def hcd_ext_054_gap_ewm_1q(inst_holders: pd.Series,
                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """EWM (span=1 quarter) of holder-count gap (own-peer)."""
    return _ewm_mean(_gap(inst_holders, peer_median_inst_holders), _TD_QTR)


def hcd_ext_055_ratio_ewm_2q_minus_2y(inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio EWM(2q) minus EWM(2y) — medium-vs-long crossover."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _ewm_mean(ratio, _TD_2Q) - _ewm_mean(ratio, _TD_2Y)


def hcd_ext_056_log_rel_ewm_short_minus_long(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """Log-relative breadth EWM(1q) minus EWM(1y) — momentum crossover."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return _ewm_mean(lr, _TD_QTR) - _ewm_mean(lr, _TD_YEAR)


def hcd_ext_057_ratio_vs_ewm_2y_deviation(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio minus its EWM(2y) — deviation from long-term trend."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return ratio - _ewm_mean(ratio, _TD_2Y)


def hcd_ext_058_inst_pct_ratio_ewm_1q(inst_pct: pd.Series,
                                       peer_median_inst_pct: pd.Series) -> pd.Series:
    """EWM (span=1 quarter) of inst_pct ratio vs peer."""
    return _ewm_mean(_rel_ratio(inst_pct, peer_median_inst_pct), _TD_QTR)


def hcd_ext_059_inst_shares_ratio_ewm_1q(inst_shares: pd.Series,
                                          peer_median_inst_shares: pd.Series) -> pd.Series:
    """EWM (span=1 quarter) of inst_shares ratio vs peer."""
    return _ewm_mean(_rel_ratio(inst_shares, peer_median_inst_shares), _TD_QTR)


def hcd_ext_060_gap_ewm_vs_long_deviation(inst_holders: pd.Series,
                                           peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-count gap EWM(1q) minus EWM(1y) — gap momentum crossover."""
    gap = _gap(inst_holders, peer_median_inst_holders)
    return _ewm_mean(gap, _TD_QTR) - _ewm_mean(gap, _TD_YEAR)


# --- Group G (061-068): Ratio drawdown / trough proximity ---

def hcd_ext_061_ratio_drawdown_from_1y_max(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio drawdown: ratio / 1-yr max ratio - 1."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _safe_div(ratio, _rolling_max(ratio, _TD_YEAR).replace(0, np.nan)) - 1.0


def hcd_ext_062_ratio_drawdown_from_3y_max(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio drawdown vs 3-yr max ratio."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _safe_div(ratio, _rolling_max(ratio, _TD_3Y).replace(0, np.nan)) - 1.0


def hcd_ext_063_ratio_above_2y_min(inst_holders: pd.Series,
                                    peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio / its 2-yr rolling min minus 1 — rebound off trough."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _safe_div(ratio, _rolling_min(ratio, _TD_2Y).replace(0, np.nan)) - 1.0


def hcd_ext_064_ratio_3y_min(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling minimum of holder-breadth ratio (worst-ever-window vs peer)."""
    return _rolling_min(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Y)


def hcd_ext_065_ratio_3y_max(inst_holders: pd.Series,
                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """3-year rolling maximum of holder-breadth ratio."""
    return _rolling_max(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_3Y)


def hcd_ext_066_log_rel_drawdown_from_2y_max(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series) -> pd.Series:
    """Log-relative breadth minus its 2-yr rolling max (gap below relative peak)."""
    lr = _log_rel(inst_holders, peer_median_inst_holders)
    return lr - _rolling_max(lr, _TD_2Y)


def hcd_ext_067_inst_pct_ratio_drawdown_2y(inst_pct: pd.Series,
                                            peer_median_inst_pct: pd.Series) -> pd.Series:
    """Inst_pct ratio drawdown vs 2-yr max ratio."""
    ratio = _rel_ratio(inst_pct, peer_median_inst_pct)
    return _safe_div(ratio, _rolling_max(ratio, _TD_2Y).replace(0, np.nan)) - 1.0


def hcd_ext_068_ratio_position_in_3y_range(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """Holder-breadth ratio position within its 3-yr min-max range [0,1]."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    mn = _rolling_min(ratio, _TD_3Y)
    mx = _rolling_max(ratio, _TD_3Y)
    return _safe_div(ratio - mn, (mx - mn).replace(0, np.nan))


# --- Group H (069-075): Volatility, dispersion and composite peer-relative scores ---

def hcd_ext_069_ratio_rolling_std_2y(inst_holders: pd.Series,
                                      peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling std of holder-breadth ratio (relative breadth volatility)."""
    return _rolling_std(_rel_ratio(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_070_log_rel_rolling_std_2y(inst_holders: pd.Series,
                                        peer_median_inst_holders: pd.Series) -> pd.Series:
    """2-year rolling std of log-relative holder breadth."""
    return _rolling_std(_log_rel(inst_holders, peer_median_inst_holders), _TD_2Y)


def hcd_ext_071_ratio_coef_of_variation_1y(inst_holders: pd.Series,
                                            peer_median_inst_holders: pd.Series) -> pd.Series:
    """1-year coefficient of variation of holder-breadth ratio (std / mean)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    return _safe_div(_rolling_std(ratio, _TD_YEAR), _rolling_mean(ratio, _TD_YEAR))


def hcd_ext_072_shares_per_holder_rel(inst_shares: pd.Series, peer_median_inst_shares: pd.Series,
                                       inst_holders: pd.Series,
                                       peer_median_inst_holders: pd.Series) -> pd.Series:
    """Shares-ratio / holders-ratio vs peer — relative position-size concentration."""
    return _safe_div(_rel_ratio(inst_shares, peer_median_inst_shares),
                     _rel_ratio(inst_holders, peer_median_inst_holders))


def hcd_ext_073_composite_peer_deficit_score(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series,
                                              inst_pct: pd.Series,
                                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """Composite breadth deficit: sum of (1 - holders ratio) and (1 - inst_pct ratio),
    positive when both metrics sit below peer median. Higher = deeper relative deficit."""
    r1 = _rel_ratio(inst_holders, peer_median_inst_holders)
    r2 = _rel_ratio(inst_pct, peer_median_inst_pct)
    return (1.0 - r1).clip(lower=0) + (1.0 - r2).clip(lower=0)


def hcd_ext_074_composite_relative_zscore_2y(inst_holders: pd.Series,
                                              peer_median_inst_holders: pd.Series,
                                              inst_pct: pd.Series,
                                              peer_median_inst_pct: pd.Series) -> pd.Series:
    """2-year z-score of the combined (holders + inst_pct) log-relative breadth signal."""
    composite = (_log_rel(inst_holders, peer_median_inst_holders) +
                 _log_rel(inst_pct, peer_median_inst_pct))
    return _zscore_rolling(composite, _TD_2Y)


def hcd_ext_075_capitulation_breadth_composite(inst_holders: pd.Series,
                                               peer_median_inst_holders: pd.Series,
                                               inst_pct: pd.Series,
                                               peer_median_inst_pct: pd.Series) -> pd.Series:
    """Capitulation breadth composite: 1-yr percentile rank inversion of holder-breadth
    ratio plus below-peer-fraction of inst_pct over 1yr. Higher = more peer-relative
    breadth distress (holder base thin AND ownership below peers)."""
    ratio = _rel_ratio(inst_holders, peer_median_inst_holders)
    rank_inv = 1.0 - _rolling_rank_pct(ratio, _TD_YEAR).fillna(0.5)
    pct_below = _rolling_mean((inst_pct < peer_median_inst_pct).astype(float), _TD_YEAR)
    return rank_inv + pct_below


# ===========================================================================
# Registry
# ===========================================================================
HOLDER_COUNT_DYNAMICS_EXTENDED_REGISTRY_001_075 = {
    "hcd_ext_001_ratio_rolling_mean_3q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_001_ratio_rolling_mean_3q},
    "hcd_ext_002_ratio_rolling_mean_3y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_002_ratio_rolling_mean_3y},
    "hcd_ext_003_ratio_rolling_median_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_003_ratio_rolling_median_2y},
    "hcd_ext_004_log_rel_rolling_mean_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_004_log_rel_rolling_mean_2y},
    "hcd_ext_005_gap_rolling_mean_2q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_005_gap_rolling_mean_2q},
    "hcd_ext_006_gap_rolling_median_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_006_gap_rolling_median_1y},
    "hcd_ext_007_inst_pct_ratio_rolling_mean_1y": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_007_inst_pct_ratio_rolling_mean_1y},
    "hcd_ext_008_inst_shares_ratio_rolling_mean_1y": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_008_inst_shares_ratio_rolling_mean_1y},
    "hcd_ext_009_ratio_minus_rolling_mean_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_009_ratio_minus_rolling_mean_1y},
    "hcd_ext_010_log_rel_minus_rolling_median_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_010_log_rel_minus_rolling_median_2y},
    "hcd_ext_011_ratio_zscore_2q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_011_ratio_zscore_2q},
    "hcd_ext_012_ratio_zscore_3q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_012_ratio_zscore_3q},
    "hcd_ext_013_log_rel_zscore_3y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_013_log_rel_zscore_3y},
    "hcd_ext_014_gap_zscore_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_014_gap_zscore_1y},
    "hcd_ext_015_gap_zscore_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_015_gap_zscore_2y},
    "hcd_ext_016_inst_pct_ratio_zscore_2y": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_016_inst_pct_ratio_zscore_2y},
    "hcd_ext_017_inst_shares_ratio_zscore_1y": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_017_inst_shares_ratio_zscore_1y},
    "hcd_ext_018_inst_shares_ratio_zscore_2y": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_018_inst_shares_ratio_zscore_2y},
    "hcd_ext_019_ratio_expanding_zscore_neg_clip": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_019_ratio_expanding_zscore_neg_clip},
    "hcd_ext_020_log_rel_expanding_zscore": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_020_log_rel_expanding_zscore},
    "hcd_ext_021_ratio_rank_2q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_021_ratio_rank_2q},
    "hcd_ext_022_ratio_rank_3q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_022_ratio_rank_3q},
    "hcd_ext_023_log_rel_rank_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_023_log_rel_rank_2y},
    "hcd_ext_024_log_rel_rank_3y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_024_log_rel_rank_3y},
    "hcd_ext_025_gap_rank_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_025_gap_rank_1y},
    "hcd_ext_026_gap_rank_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_026_gap_rank_2y},
    "hcd_ext_027_inst_pct_ratio_rank_2y": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_027_inst_pct_ratio_rank_2y},
    "hcd_ext_028_inst_shares_ratio_rank_1y": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_028_inst_shares_ratio_rank_1y},
    "hcd_ext_029_ratio_rank_qoq_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_029_ratio_rank_qoq_change},
    "hcd_ext_030_ratio_expanding_rank_inverse": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_030_ratio_expanding_rank_inverse},
    "hcd_ext_031_ratio_2q_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_031_ratio_2q_change},
    "hcd_ext_032_ratio_3q_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_032_ratio_3q_change},
    "hcd_ext_033_log_rel_2q_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_033_log_rel_2q_change},
    "hcd_ext_034_gap_2q_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_034_gap_2q_change},
    "hcd_ext_035_ratio_2y_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_035_ratio_2y_change},
    "hcd_ext_036_ratio_2y_pct_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_036_ratio_2y_pct_change},
    "hcd_ext_037_inst_pct_ratio_2q_change": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_037_inst_pct_ratio_2q_change},
    "hcd_ext_038_inst_shares_ratio_qoq_change": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_038_inst_shares_ratio_qoq_change},
    "hcd_ext_039_ratio_qoq_change_zscore_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_039_ratio_qoq_change_zscore_2y},
    "hcd_ext_040_log_rel_yoy_pct_change": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_040_log_rel_yoy_pct_change},
    "hcd_ext_041_consec_qtrs_above_peer": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_041_consec_qtrs_above_peer},
    "hcd_ext_042_consec_qtrs_inst_pct_below_peer": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_042_consec_qtrs_inst_pct_below_peer},
    "hcd_ext_043_consec_qtrs_shares_below_peer": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_043_consec_qtrs_shares_below_peer},
    "hcd_ext_044_max_below_peer_streak_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_044_max_below_peer_streak_2y},
    "hcd_ext_045_below_peer_fraction_3y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_045_below_peer_fraction_3y},
    "hcd_ext_046_below_peer_fraction_2q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_046_below_peer_fraction_2q},
    "hcd_ext_047_inst_pct_below_peer_fraction_1y": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_047_inst_pct_below_peer_fraction_1y},
    "hcd_ext_048_below_peer_days_count_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_048_below_peer_days_count_1y},
    "hcd_ext_049_far_below_peer_flag": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_049_far_below_peer_flag},
    "hcd_ext_050_consec_days_ratio_falling": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_050_consec_days_ratio_falling},
    "hcd_ext_051_ratio_ewm_3q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_051_ratio_ewm_3q},
    "hcd_ext_052_ratio_ewm_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_052_ratio_ewm_2y},
    "hcd_ext_053_log_rel_ewm_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_053_log_rel_ewm_1y},
    "hcd_ext_054_gap_ewm_1q": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_054_gap_ewm_1q},
    "hcd_ext_055_ratio_ewm_2q_minus_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_055_ratio_ewm_2q_minus_2y},
    "hcd_ext_056_log_rel_ewm_short_minus_long": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_056_log_rel_ewm_short_minus_long},
    "hcd_ext_057_ratio_vs_ewm_2y_deviation": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_057_ratio_vs_ewm_2y_deviation},
    "hcd_ext_058_inst_pct_ratio_ewm_1q": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_058_inst_pct_ratio_ewm_1q},
    "hcd_ext_059_inst_shares_ratio_ewm_1q": {"inputs": ["inst_shares", "peer_median_inst_shares"], "func": hcd_ext_059_inst_shares_ratio_ewm_1q},
    "hcd_ext_060_gap_ewm_vs_long_deviation": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_060_gap_ewm_vs_long_deviation},
    "hcd_ext_061_ratio_drawdown_from_1y_max": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_061_ratio_drawdown_from_1y_max},
    "hcd_ext_062_ratio_drawdown_from_3y_max": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_062_ratio_drawdown_from_3y_max},
    "hcd_ext_063_ratio_above_2y_min": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_063_ratio_above_2y_min},
    "hcd_ext_064_ratio_3y_min": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_064_ratio_3y_min},
    "hcd_ext_065_ratio_3y_max": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_065_ratio_3y_max},
    "hcd_ext_066_log_rel_drawdown_from_2y_max": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_066_log_rel_drawdown_from_2y_max},
    "hcd_ext_067_inst_pct_ratio_drawdown_2y": {"inputs": ["inst_pct", "peer_median_inst_pct"], "func": hcd_ext_067_inst_pct_ratio_drawdown_2y},
    "hcd_ext_068_ratio_position_in_3y_range": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_068_ratio_position_in_3y_range},
    "hcd_ext_069_ratio_rolling_std_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_069_ratio_rolling_std_2y},
    "hcd_ext_070_log_rel_rolling_std_2y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_070_log_rel_rolling_std_2y},
    "hcd_ext_071_ratio_coef_of_variation_1y": {"inputs": ["inst_holders", "peer_median_inst_holders"], "func": hcd_ext_071_ratio_coef_of_variation_1y},
    "hcd_ext_072_shares_per_holder_rel": {"inputs": ["inst_shares", "peer_median_inst_shares", "inst_holders", "peer_median_inst_holders"], "func": hcd_ext_072_shares_per_holder_rel},
    "hcd_ext_073_composite_peer_deficit_score": {"inputs": ["inst_holders", "peer_median_inst_holders", "inst_pct", "peer_median_inst_pct"], "func": hcd_ext_073_composite_peer_deficit_score},
    "hcd_ext_074_composite_relative_zscore_2y": {"inputs": ["inst_holders", "peer_median_inst_holders", "inst_pct", "peer_median_inst_pct"], "func": hcd_ext_074_composite_relative_zscore_2y},
    "hcd_ext_075_capitulation_breadth_composite": {"inputs": ["inst_holders", "peer_median_inst_holders", "inst_pct", "peer_median_inst_pct"], "func": hcd_ext_075_capitulation_breadth_composite},
}
