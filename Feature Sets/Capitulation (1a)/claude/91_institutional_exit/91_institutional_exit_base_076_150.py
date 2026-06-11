"""
91_institutional_exit — Base Features 076–200
==============================================
Domain: QoQ DECLINE in the institutional holder base — institutions LEAVING.
Captures falling count of 13F holders, falling aggregate shares/value held,
net exits (closed+decreased exceeding new+increased), acceleration of the
exodus, and depth/duration of the ownership bleed.

NOT in scope: accumulation/new-position features (folder 93),
concentration/HHI features (folder 92), abrupt fire-sale/forced-liquidation
breadth features (folder 95).

Quarterly → Daily Alignment Contract
--------------------------------------
All inputs are **daily-frequency** pandas Series that have been forward-filled
from quarterly Sharadar SF3 13F snapshots.  Because the underlying data updates
only once per quarter (~63 trading days), computed series will be
stepwise/sparse on a daily index — this is expected and correct.

Cadence constants:
    1 quarter ≈ 63 trading days  (_TD_QTR)
    1 year    ≈ 252 trading days (_TD_YEAR)
    2 years   ≈ 504 trading days (_TD_2Y)
    3 years   ≈ 756 trading days (_TD_3Y)

Input fields (all daily-frequency pandas Series, ff-filled from SF3):
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
    """
    Forward-fill a quarterly Series to a daily index.
    If the input is already daily (len > 300 per year), returns as-is.
    Otherwise reindexes to daily and forward-fills.
    """
    return series.ffill()


def _safe_div(a, b):
    """Element-wise a / (b + EPS), preserving Series index."""
    return a / (b + _EPS)


def _safe_div_abs(a, b):
    """Element-wise a / (|b| + EPS)."""
    return a / (b.abs() + _EPS)


def _rolling_mean(s, w):
    return s.rolling(w, min_periods=1).mean()


def _rolling_std(s, w):
    return s.rolling(w, min_periods=2).std()


def _rolling_sum(s, w):
    return s.rolling(w, min_periods=1).sum()


def _rolling_min(s, w):
    return s.rolling(w, min_periods=1).min()


def _rolling_max(s, w):
    return s.rolling(w, min_periods=1).max()


def _rolling_median(s, w):
    return s.rolling(w, min_periods=1).median()


def _rolling_rank_pct(s, w):
    """Percentile rank of current value within rolling window [0, 1]."""
    return s.rolling(w, min_periods=2).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def _zscore_rolling(s, w):
    mu = _rolling_mean(s, w)
    sigma = _rolling_std(s, w)
    return _safe_div(s - mu, sigma)


def _ewm_mean(s, span):
    return s.ewm(span=span, adjust=False).mean()

# ---------------------------------------------------------------------------
# Feature functions 076–150
# ---------------------------------------------------------------------------

def iex_076_holder_count_3q_diff(inst_holders: pd.Series) -> pd.Series:
    """Change in holder count over 3 quarters."""
    return inst_holders - inst_holders.shift(3 * _TD_QTR)


def iex_077_holder_count_6q_diff(inst_holders: pd.Series) -> pd.Series:
    """Change in holder count over 6 quarters."""
    return inst_holders - inst_holders.shift(6 * _TD_QTR)


def iex_078_holder_count_rolling_std_4q(inst_holders: pd.Series) -> pd.Series:
    """Rolling 4q standard deviation of holder count (volatility of exit rate)."""
    return _rolling_std(inst_holders, _TD_YEAR)


def iex_079_holder_count_rolling_std_8q(inst_holders: pd.Series) -> pd.Series:
    """Rolling 8q standard deviation of holder count."""
    return _rolling_std(inst_holders, _TD_2Y)


def iex_080_inst_shares_rolling_std_4q(inst_shares: pd.Series) -> pd.Series:
    """Rolling 4q standard deviation of aggregate shares held."""
    return _rolling_std(inst_shares, _TD_YEAR)


def iex_081_inst_value_rolling_std_4q(inst_value: pd.Series) -> pd.Series:
    """Rolling 4q standard deviation of aggregate institutional value."""
    return _rolling_std(inst_value, _TD_YEAR)


def iex_082_closed_positions_zscore_4q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions count over 4-quarter rolling window."""
    return _zscore_rolling(closed_positions, _TD_YEAR)


def iex_083_closed_positions_ewm_deviation(closed_positions: pd.Series) -> pd.Series:
    """Deviation of closed positions from EWM (span=4q)."""
    return closed_positions - _ewm_mean(closed_positions, _TD_YEAR)


def iex_084_decreased_positions_zscore_4q(decreased_positions: pd.Series) -> pd.Series:
    """Z-score of decreased positions count over 4-quarter rolling window."""
    return _zscore_rolling(decreased_positions, _TD_YEAR)


def iex_085_decreased_positions_ewm_deviation(decreased_positions: pd.Series) -> pd.Series:
    """Deviation of decreased positions from EWM (span=4q)."""
    return decreased_positions - _ewm_mean(decreased_positions, _TD_YEAR)


def iex_086_exit_vs_entry_spread(closed_positions: pd.Series,
                                   decreased_positions: pd.Series,
                                   new_positions: pd.Series,
                                   increased_positions: pd.Series) -> pd.Series:
    """
    Spread = (closed+decreased) - (new+increased) normalized by total activity.
    Positive = exits dominating.
    """
    exits = closed_positions + decreased_positions
    entries = new_positions + increased_positions
    total = exits + entries
    return _safe_div(exits - entries, total)


def iex_087_exit_vs_entry_spread_4q_mean(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """4q rolling mean of exit vs entry spread."""
    exits = closed_positions + decreased_positions
    entries = new_positions + increased_positions
    total = exits + entries
    spread = _safe_div(exits - entries, total)
    return _rolling_mean(spread, _TD_YEAR)


def iex_088_exit_vs_entry_spread_zscore(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series) -> pd.Series:
    """Z-score of the exit-vs-entry spread over 4-quarter window."""
    exits = closed_positions + decreased_positions
    entries = new_positions + increased_positions
    total = exits + entries
    spread = _safe_div(exits - entries, total)
    return _zscore_rolling(spread, _TD_YEAR)


def iex_089_holder_count_2q_vs_4q_slope_ratio(inst_holders: pd.Series) -> pd.Series:
    """
    Ratio of 2-quarter slope to 4-quarter slope of holder count.
    Above 1 means recent exit pace exceeds the longer-term trend.
    """
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

    s2 = inst_holders.rolling(_TD_2Q, min_periods=2).apply(_slope, raw=True)
    s4 = inst_holders.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)
    return _safe_div_abs(s2, s4)


def iex_090_holder_count_6q_slope(inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder count over rolling 6-quarter window."""
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
    return inst_holders.rolling(6 * _TD_QTR, min_periods=4).apply(_slope, raw=True)


def iex_091_inst_value_4q_slope(inst_value: pd.Series) -> pd.Series:
    """OLS slope of aggregate institutional value over 4-quarter window."""
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
    return inst_value.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def iex_092_shares_per_holder_qoq_diff(inst_shares: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """QoQ change in average shares per institutional holder."""
    sph = _safe_div(inst_shares, inst_holders)
    return sph - sph.shift(_TD_QTR)


def iex_093_shares_per_holder_yoy_pct(inst_shares: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """YoY % change in average shares per institutional holder."""
    sph = _safe_div(inst_shares, inst_holders)
    return _safe_div(sph - sph.shift(_TD_YEAR), sph.shift(_TD_YEAR).abs())


def iex_094_shares_per_holder_zscore_4q(inst_shares: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """Z-score of shares per holder over 4-quarter rolling window."""
    sph = _safe_div(inst_shares, inst_holders)
    return _zscore_rolling(sph, _TD_YEAR)


def iex_095_value_per_holder_qoq_diff(inst_value: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """QoQ change in average USD value per institutional holder."""
    vph = _safe_div(inst_value, inst_holders)
    return vph - vph.shift(_TD_QTR)


def iex_096_value_per_holder_yoy_pct(inst_value: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """YoY % change in average USD value per institutional holder."""
    vph = _safe_div(inst_value, inst_holders)
    return _safe_div(vph - vph.shift(_TD_YEAR), vph.shift(_TD_YEAR).abs())


def iex_097_value_per_holder_zscore_4q(inst_value: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """Z-score of value per holder over 4-quarter rolling window."""
    vph = _safe_div(inst_value, inst_holders)
    return _zscore_rolling(vph, _TD_YEAR)


def iex_098_holder_count_pct_from_3y_max(inst_holders: pd.Series) -> pd.Series:
    """Holder count drawdown from rolling 3-year maximum."""
    mx = _rolling_max(inst_holders, _TD_3Y)
    return _safe_div(inst_holders - mx, mx.abs())


def iex_099_inst_shares_pct_from_3y_max(inst_shares: pd.Series) -> pd.Series:
    """Aggregate shares drawdown from rolling 3-year maximum."""
    mx = _rolling_max(inst_shares, _TD_3Y)
    return _safe_div(inst_shares - mx, mx.abs())


def iex_100_inst_pct_pct_from_3y_max(inst_pct: pd.Series) -> pd.Series:
    """Institutional ownership fraction drawdown from rolling 3-year maximum."""
    mx = _rolling_max(inst_pct, _TD_3Y)
    return _safe_div(inst_pct - mx, mx.abs())


def iex_101_net_exits_4q_rolling_sum(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """Rolling 4-quarter sum of net exits (cumulative exit pressure)."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_sum(net, _TD_YEAR)


def iex_102_net_exits_4q_rolling_mean(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """Rolling 4-quarter mean of net exits."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_mean(net, _TD_YEAR)


def iex_103_net_exits_zscore_4q(closed_positions: pd.Series,
                                  decreased_positions: pd.Series,
                                  new_positions: pd.Series,
                                  increased_positions: pd.Series) -> pd.Series:
    """Z-score of net exits over 4-quarter rolling window."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _zscore_rolling(net, _TD_YEAR)


def iex_104_net_exits_zscore_8q(closed_positions: pd.Series,
                                  decreased_positions: pd.Series,
                                  new_positions: pd.Series,
                                  increased_positions: pd.Series) -> pd.Series:
    """Z-score of net exits over 8-quarter rolling window."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _zscore_rolling(net, _TD_2Y)


def iex_105_holder_count_vs_expanding_mean(inst_holders: pd.Series) -> pd.Series:
    """Ratio of holder count to its expanding historical mean."""
    return _safe_div(inst_holders, inst_holders.expanding(min_periods=1).mean())


def iex_106_inst_shares_vs_expanding_mean(inst_shares: pd.Series) -> pd.Series:
    """Ratio of aggregate shares to expanding historical mean."""
    return _safe_div(inst_shares, inst_shares.expanding(min_periods=1).mean())


def iex_107_inst_pct_vs_expanding_mean(inst_pct: pd.Series) -> pd.Series:
    """Ratio of institutional ownership fraction to expanding historical mean."""
    return _safe_div(inst_pct, inst_pct.expanding(min_periods=1).mean())


def iex_108_holder_count_ewm_span8q_deviation(inst_holders: pd.Series) -> pd.Series:
    """Deviation of holder count from EWM (span=8q)."""
    return inst_holders - _ewm_mean(inst_holders, _TD_2Y)


def iex_109_inst_shares_ewm_span8q_deviation(inst_shares: pd.Series) -> pd.Series:
    """Deviation of aggregate shares from EWM (span=8q)."""
    return inst_shares - _ewm_mean(inst_shares, _TD_2Y)


def iex_110_inst_pct_ewm_span8q_deviation(inst_pct: pd.Series) -> pd.Series:
    """Deviation of institutional ownership fraction from EWM (span=8q)."""
    return inst_pct - _ewm_mean(inst_pct, _TD_2Y)


def iex_111_closed_positions_pct_rank_4q(closed_positions: pd.Series) -> pd.Series:
    """Rolling 4q percentile rank of closed-position count."""
    return _rolling_rank_pct(closed_positions, _TD_YEAR)


def iex_112_decreased_positions_pct_rank_4q(decreased_positions: pd.Series) -> pd.Series:
    """Rolling 4q percentile rank of decreased-position count."""
    return _rolling_rank_pct(decreased_positions, _TD_YEAR)


def iex_113_net_exits_pct_rank_4q(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    new_positions: pd.Series,
                                    increased_positions: pd.Series) -> pd.Series:
    """Rolling 4q percentile rank of net exits."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_rank_pct(net, _TD_YEAR)


def iex_114_net_exits_pct_rank_8q(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    new_positions: pd.Series,
                                    increased_positions: pd.Series) -> pd.Series:
    """Rolling 8q percentile rank of net exits."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_rank_pct(net, _TD_2Y)


def iex_115_holder_count_vs_12q_ago(inst_holders: pd.Series) -> pd.Series:
    """Holder count vs 12-quarter (3-year) ago level."""
    return inst_holders - inst_holders.shift(12 * _TD_QTR)


def iex_116_inst_shares_vs_12q_ago(inst_shares: pd.Series) -> pd.Series:
    """Aggregate shares vs 12-quarter ago level."""
    return inst_shares - inst_shares.shift(12 * _TD_QTR)


def iex_117_inst_pct_vs_12q_ago(inst_pct: pd.Series) -> pd.Series:
    """Institutional ownership fraction vs 12-quarter ago level."""
    return inst_pct - inst_pct.shift(12 * _TD_QTR)


def iex_118_exit_breadth_expanding_pct_rank(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """Expanding percentile rank of exit breadth."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return breadth.expanding(min_periods=2).rank(pct=True)


def iex_119_holder_count_pct_chg_rolling_mean_4q(inst_holders: pd.Series) -> pd.Series:
    """4-quarter rolling mean of QoQ % change in holder count."""
    pct_chg = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                        inst_holders.shift(_TD_QTR).abs())
    return _rolling_mean(pct_chg, _TD_YEAR)


def iex_120_inst_shares_pct_chg_rolling_mean_4q(inst_shares: pd.Series) -> pd.Series:
    """4-quarter rolling mean of QoQ % change in aggregate shares."""
    pct_chg = _safe_div(inst_shares - inst_shares.shift(_TD_QTR),
                        inst_shares.shift(_TD_QTR).abs())
    return _rolling_mean(pct_chg, _TD_YEAR)


def iex_121_inst_pct_pct_chg_rolling_mean_4q(inst_pct: pd.Series) -> pd.Series:
    """4-quarter rolling mean of QoQ diff in institutional ownership fraction."""
    diff = inst_pct - inst_pct.shift(_TD_QTR)
    return _rolling_mean(diff, _TD_YEAR)


def iex_122_holder_count_qoq_below_zero_freq(inst_holders: pd.Series) -> pd.Series:
    """Fraction of rolling 4-quarter windows with negative QoQ holder change."""
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    below = (diff < 0).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def iex_123_inst_shares_qoq_below_zero_freq(inst_shares: pd.Series) -> pd.Series:
    """Fraction of rolling 4-quarter windows with negative QoQ shares change."""
    diff = inst_shares - inst_shares.shift(_TD_QTR)
    below = (diff < 0).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def iex_124_inst_pct_qoq_below_zero_freq(inst_pct: pd.Series) -> pd.Series:
    """Fraction of rolling 4-quarter windows with negative QoQ ownership-fraction change."""
    diff = inst_pct - inst_pct.shift(_TD_QTR)
    below = (diff < 0).astype(float)
    return _rolling_mean(below, _TD_YEAR)


def iex_125_holder_count_qoq_below_zero_freq_8q(inst_holders: pd.Series) -> pd.Series:
    """Fraction of rolling 8-quarter windows with negative QoQ holder change."""
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    below = (diff < 0).astype(float)
    return _rolling_mean(below, _TD_2Y)


def iex_126_net_exits_4q_sum_vs_8q_sum_ratio(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               new_positions: pd.Series,
                                               increased_positions: pd.Series) -> pd.Series:
    """Ratio of 4q-cumulative net exits to 8q-cumulative net exits (acceleration proxy)."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    s4 = _rolling_sum(net, _TD_YEAR)
    s8 = _rolling_sum(net, _TD_2Y)
    return _safe_div(s4, s8.abs())


def iex_127_holder_count_min_4q_vs_current(inst_holders: pd.Series) -> pd.Series:
    """Distance of current holder count from its 4q rolling min (0 = at trough)."""
    mn = _rolling_min(inst_holders, _TD_YEAR)
    return inst_holders - mn


def iex_128_holder_count_pct_above_4q_min(inst_holders: pd.Series) -> pd.Series:
    """Percent above 4q rolling minimum of holder count."""
    mn = _rolling_min(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders - mn, mn.abs())


def iex_129_inst_shares_min_8q_vs_current(inst_shares: pd.Series) -> pd.Series:
    """Distance of aggregate shares from their 8q rolling minimum."""
    mn = _rolling_min(inst_shares, _TD_2Y)
    return inst_shares - mn


def iex_130_inst_pct_min_8q_vs_current(inst_pct: pd.Series) -> pd.Series:
    """Distance of institutional ownership fraction from its 8q rolling minimum."""
    mn = _rolling_min(inst_pct, _TD_2Y)
    return inst_pct - mn


def iex_131_value_per_share_qoq_diff(inst_value: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in implied price per share from institutional perspective."""
    vps = _safe_div(inst_value, inst_shares)
    return vps - vps.shift(_TD_QTR)


def iex_132_holder_decay_rate_ewm(inst_holders: pd.Series) -> pd.Series:
    """EWM-smoothed QoQ % change in holder count (span=2q)."""
    pct = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                    inst_holders.shift(_TD_QTR).abs())
    return _ewm_mean(pct, _TD_2Q)


def iex_133_shares_decay_rate_ewm(inst_shares: pd.Series) -> pd.Series:
    """EWM-smoothed QoQ % change in aggregate shares (span=2q)."""
    pct = _safe_div(inst_shares - inst_shares.shift(_TD_QTR),
                    inst_shares.shift(_TD_QTR).abs())
    return _ewm_mean(pct, _TD_2Q)


def iex_134_inst_pct_decay_rate_ewm(inst_pct: pd.Series) -> pd.Series:
    """EWM-smoothed QoQ diff in institutional ownership fraction (span=2q)."""
    diff = inst_pct - inst_pct.shift(_TD_QTR)
    return _ewm_mean(diff, _TD_2Q)


def iex_135_holder_count_cross_below_8q_mean(inst_holders: pd.Series) -> pd.Series:
    """
    Binary: 1 on the day holder count crosses below its 8-quarter rolling mean.
    Detects the moment of crossing, not sustained below.
    """
    mean8q = _rolling_mean(inst_holders, _TD_2Y)
    below_now = inst_holders < mean8q
    below_prev = inst_holders.shift(1) >= mean8q.shift(1)
    return (below_now & below_prev).astype(float)


def iex_136_inst_pct_cross_below_8q_mean(inst_pct: pd.Series) -> pd.Series:
    """
    Binary: 1 on the day institutional ownership fraction crosses below its 8q mean.
    """
    mean8q = _rolling_mean(inst_pct, _TD_2Y)
    below_now = inst_pct < mean8q
    below_prev = inst_pct.shift(1) >= mean8q.shift(1)
    return (below_now & below_prev).astype(float)


def iex_137_closed_increased_ratio(closed_positions: pd.Series,
                                    increased_positions: pd.Series) -> pd.Series:
    """Ratio of closed to increased positions (high = more fully-exiting vs adding)."""
    return _safe_div(closed_positions, increased_positions)


def iex_138_decreased_new_ratio(decreased_positions: pd.Series,
                                  new_positions: pd.Series) -> pd.Series:
    """Ratio of decreased to new positions (high = trimmers exceeding initiators)."""
    return _safe_div(decreased_positions, new_positions)


def iex_139_net_exit_fraction_of_holders(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """Net exits as fraction of total holder base."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _safe_div(net, inst_holders)


def iex_140_holder_count_12q_slope(inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder count over rolling 12-quarter (3-year) window."""
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
    return inst_holders.rolling(_TD_3Y, min_periods=4).apply(_slope, raw=True)


def iex_141_inst_value_12q_slope(inst_value: pd.Series) -> pd.Series:
    """OLS slope of aggregate institutional value over 12-quarter window."""
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
    return inst_value.rolling(_TD_3Y, min_periods=4).apply(_slope, raw=True)


def iex_142_holder_count_qoq_negrun_sum(inst_holders: pd.Series) -> pd.Series:
    """
    Rolling 4q sum of negative QoQ holder changes only (magnitude of declines).
    """
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    neg_only = diff.where(diff < 0, 0.0)
    return _rolling_sum(neg_only, _TD_YEAR)


def iex_143_shares_qoq_negrun_sum(inst_shares: pd.Series) -> pd.Series:
    """Rolling 4q sum of negative QoQ shares changes only."""
    diff = inst_shares - inst_shares.shift(_TD_QTR)
    neg_only = diff.where(diff < 0, 0.0)
    return _rolling_sum(neg_only, _TD_YEAR)


def iex_144_inst_pct_qoq_negrun_sum(inst_pct: pd.Series) -> pd.Series:
    """Rolling 4q sum of negative QoQ ownership-fraction changes only."""
    diff = inst_pct - inst_pct.shift(_TD_QTR)
    neg_only = diff.where(diff < 0, 0.0)
    return _rolling_sum(neg_only, _TD_YEAR)


def iex_145_time_since_holder_count_max(inst_holders: pd.Series) -> pd.Series:
    """
    Trading days since the all-time (expanding) maximum of holder count.
    Large values indicate a long, sustained decline.
    """
    def _days_since_max(x):
        return len(x) - 1 - int(np.argmax(x))
    return inst_holders.expanding(min_periods=1).apply(_days_since_max, raw=True)


def iex_146_time_since_inst_pct_max(inst_pct: pd.Series) -> pd.Series:
    """Trading days since the all-time (expanding) maximum of institutional ownership fraction."""
    def _days_since_max(x):
        return len(x) - 1 - int(np.argmax(x))
    return inst_pct.expanding(min_periods=1).apply(_days_since_max, raw=True)


def iex_147_time_since_inst_shares_max(inst_shares: pd.Series) -> pd.Series:
    """Trading days since the all-time (expanding) maximum of aggregate shares held."""
    def _days_since_max(x):
        return len(x) - 1 - int(np.argmax(x))
    return inst_shares.expanding(min_periods=1).apply(_days_since_max, raw=True)


def iex_148_holder_count_4q_cv(inst_holders: pd.Series) -> pd.Series:
    """Coefficient of variation of holder count over rolling 4-quarter window."""
    mu = _rolling_mean(inst_holders, _TD_YEAR)
    sigma = _rolling_std(inst_holders, _TD_YEAR)
    return _safe_div(sigma, mu.abs())


def iex_149_quad_exit_composite(inst_holders: pd.Series,
                                  inst_shares: pd.Series,
                                  inst_pct: pd.Series,
                                  inst_value: pd.Series) -> pd.Series:
    """
    Four-field composite exit score: average of QoQ % declines in all four
    core metrics (holders, shares, ownership %, value).
    More negative = broader institutional departure.
    """
    h = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                  inst_holders.shift(_TD_QTR).abs())
    s = _safe_div(inst_shares - inst_shares.shift(_TD_QTR),
                  inst_shares.shift(_TD_QTR).abs())
    p = inst_pct - inst_pct.shift(_TD_QTR)
    v = _safe_div(inst_value - inst_value.shift(_TD_QTR),
                  inst_value.shift(_TD_QTR).abs())
    return (h + s + p + v) / 4.0


def iex_150_holder_count_qoq_diff_vs_8q_mean_diff(inst_holders: pd.Series) -> pd.Series:
    """
    Ratio of current QoQ holder-count change to the 8-quarter rolling mean of
    QoQ holder-count changes.  Values < 1 indicate current decline exceeds trend.
    """
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    mean_diff = _rolling_mean(diff, _TD_2Y)
    return _safe_div_abs(diff, mean_diff)


def iex_176_inst_value_vs_expanding_mean(inst_value: pd.Series) -> pd.Series:
    """Ratio of aggregate institutional value to its expanding historical mean."""
    return _safe_div(inst_value, inst_value.expanding(min_periods=1).mean())


def iex_177_inst_value_3y_diff(inst_value: pd.Series) -> pd.Series:
    """3-year change in aggregate institutional USD value."""
    return inst_value - inst_value.shift(_TD_3Y)


def iex_178_inst_value_8q_rolling_rank(inst_value: pd.Series) -> pd.Series:
    """Rolling 8-quarter percentile rank of aggregate institutional value."""
    return _rolling_rank_pct(inst_value, _TD_2Y)


def iex_179_inst_value_ewm_span8q_deviation(inst_value: pd.Series) -> pd.Series:
    """Deviation of aggregate institutional value from EWM (span=8q)."""
    return inst_value - _ewm_mean(inst_value, _TD_2Y)


def iex_180_inst_value_ewm_ratio(inst_value: pd.Series) -> pd.Series:
    """Ratio of aggregate institutional value to its EWM (span=4q)."""
    return _safe_div(inst_value, _ewm_mean(inst_value, _TD_YEAR))


def iex_181_closed_positions_8q_sum(closed_positions: pd.Series) -> pd.Series:
    """Rolling 8-quarter cumulative sum of fully-closed positions."""
    return _rolling_sum(closed_positions, _TD_2Y)


def iex_182_net_exits_8q_rolling_sum(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """Rolling 8-quarter sum of net exits."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_sum(net, _TD_2Y)


def iex_183_holder_count_qoq_diff_8q_sum(inst_holders: pd.Series) -> pd.Series:
    """Rolling 8-quarter sum of QoQ holder-count changes (cumulative pressure)."""
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    return _rolling_sum(diff, _TD_2Y)


def iex_184_inst_shares_qoq_diff_8q_sum(inst_shares: pd.Series) -> pd.Series:
    """Rolling 8-quarter sum of QoQ shares changes."""
    diff = inst_shares - inst_shares.shift(_TD_QTR)
    return _rolling_sum(diff, _TD_2Y)


def iex_185_inst_pct_pct_from_8q_min(inst_pct: pd.Series) -> pd.Series:
    """Distance of institutional ownership fraction above its 8q rolling min."""
    mn = _rolling_min(inst_pct, _TD_2Y)
    return _safe_div(inst_pct - mn, mn.abs())


def iex_186_holder_count_below_8q_mean_streak(inst_holders: pd.Series) -> pd.Series:
    """Count of consecutive days holder count is below its 8q rolling mean."""
    mean8q = _rolling_mean(inst_holders, _TD_2Y)
    below = (inst_holders < mean8q).astype(int)
    result = below.copy().astype(float)
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_187_inst_shares_below_8q_mean_streak(inst_shares: pd.Series) -> pd.Series:
    """Count of consecutive days aggregate shares is below its 8q rolling mean."""
    mean8q = _rolling_mean(inst_shares, _TD_2Y)
    below = (inst_shares < mean8q).astype(int)
    result = below.copy().astype(float)
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_188_exit_breadth_8q_zscore(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    """Z-score of exit breadth over rolling 8-quarter window."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _zscore_rolling(breadth, _TD_2Y)


def iex_189_net_exits_ratio_4q_mean(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     new_positions: pd.Series,
                                     increased_positions: pd.Series) -> pd.Series:
    """4-quarter rolling mean of the exit/entry ratio."""
    ratio = _safe_div(closed_positions + decreased_positions,
                      new_positions + increased_positions)
    return _rolling_mean(ratio, _TD_YEAR)


def iex_190_new_positions_yoy_pct(new_positions: pd.Series) -> pd.Series:
    """Year-over-year % change in count of new positions initiated."""
    return _safe_div(new_positions - new_positions.shift(_TD_YEAR),
                     new_positions.shift(_TD_YEAR).abs())


def iex_191_increased_positions_yoy_pct(increased_positions: pd.Series) -> pd.Series:
    """Year-over-year % change in count of increased positions."""
    return _safe_div(increased_positions - increased_positions.shift(_TD_YEAR),
                     increased_positions.shift(_TD_YEAR).abs())


def iex_192_closed_positions_ewm_ratio(closed_positions: pd.Series) -> pd.Series:
    """Ratio of closed positions to their EWM (span=4q); spikes = abnormal exits."""
    return _safe_div(closed_positions, _ewm_mean(closed_positions, _TD_YEAR))


def iex_193_decreased_positions_ewm_ratio(decreased_positions: pd.Series) -> pd.Series:
    """Ratio of decreased positions to their EWM (span=4q)."""
    return _safe_div(decreased_positions, _ewm_mean(decreased_positions, _TD_YEAR))


def iex_194_holder_count_vs_4q_median(inst_holders: pd.Series) -> pd.Series:
    """Ratio of holder count to its 4-quarter rolling median."""
    med = _rolling_median(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders, med)


def iex_195_inst_shares_vs_4q_median(inst_shares: pd.Series) -> pd.Series:
    """Ratio of aggregate shares to the 4-quarter rolling median."""
    med = _rolling_median(inst_shares, _TD_YEAR)
    return _safe_div(inst_shares, med)


def iex_196_inst_pct_vs_4q_median(inst_pct: pd.Series) -> pd.Series:
    """Ratio of institutional ownership fraction to its 4-quarter rolling median."""
    med = _rolling_median(inst_pct, _TD_YEAR)
    return _safe_div(inst_pct, med)


def iex_197_value_drawdown_pct_from_8q_max(inst_value: pd.Series) -> pd.Series:
    """Aggregate value drawdown from its 3-year rolling min (rebound distance)."""
    mn = _rolling_min(inst_value, _TD_3Y)
    return _safe_div(inst_value - mn, mn.abs())


def iex_198_closed_to_decreased_ratio(closed_positions: pd.Series,
                                       decreased_positions: pd.Series) -> pd.Series:
    """Ratio of full closures to partial decreases (composition of the exit)."""
    return _safe_div(closed_positions, decreased_positions)


def iex_199_entry_exit_total_activity(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """Total institutional activity = exits + entries (level of churn)."""
    return closed_positions + decreased_positions + new_positions + increased_positions


def iex_200_exit_fraction_of_total_activity(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             new_positions: pd.Series,
                                             increased_positions: pd.Series) -> pd.Series:
    """Exit actions as fraction of total activity (0..1; above 0.5 = exits dominate)."""
    exits = closed_positions + decreased_positions
    total = exits + new_positions + increased_positions
    return _safe_div(exits, total)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
INSTITUTIONAL_EXIT_REGISTRY_076_150 = {
    "iex_076_holder_count_3q_diff": {"inputs": ["inst_holders"], "func": iex_076_holder_count_3q_diff},
    "iex_077_holder_count_6q_diff": {"inputs": ["inst_holders"], "func": iex_077_holder_count_6q_diff},
    "iex_078_holder_count_rolling_std_4q": {"inputs": ["inst_holders"], "func": iex_078_holder_count_rolling_std_4q},
    "iex_079_holder_count_rolling_std_8q": {"inputs": ["inst_holders"], "func": iex_079_holder_count_rolling_std_8q},
    "iex_080_inst_shares_rolling_std_4q": {"inputs": ["inst_shares"], "func": iex_080_inst_shares_rolling_std_4q},
    "iex_081_inst_value_rolling_std_4q": {"inputs": ["inst_value"], "func": iex_081_inst_value_rolling_std_4q},
    "iex_082_closed_positions_zscore_4q": {"inputs": ["closed_positions"], "func": iex_082_closed_positions_zscore_4q},
    "iex_083_closed_positions_ewm_deviation": {"inputs": ["closed_positions"], "func": iex_083_closed_positions_ewm_deviation},
    "iex_084_decreased_positions_zscore_4q": {"inputs": ["decreased_positions"], "func": iex_084_decreased_positions_zscore_4q},
    "iex_085_decreased_positions_ewm_deviation": {"inputs": ["decreased_positions"], "func": iex_085_decreased_positions_ewm_deviation},
    "iex_086_exit_vs_entry_spread": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_086_exit_vs_entry_spread},
    "iex_087_exit_vs_entry_spread_4q_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_087_exit_vs_entry_spread_4q_mean},
    "iex_088_exit_vs_entry_spread_zscore": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_088_exit_vs_entry_spread_zscore},
    "iex_089_holder_count_2q_vs_4q_slope_ratio": {"inputs": ["inst_holders"], "func": iex_089_holder_count_2q_vs_4q_slope_ratio},
    "iex_090_holder_count_6q_slope": {"inputs": ["inst_holders"], "func": iex_090_holder_count_6q_slope},
    "iex_091_inst_value_4q_slope": {"inputs": ["inst_value"], "func": iex_091_inst_value_4q_slope},
    "iex_092_shares_per_holder_qoq_diff": {"inputs": ["inst_shares", "inst_holders"], "func": iex_092_shares_per_holder_qoq_diff},
    "iex_093_shares_per_holder_yoy_pct": {"inputs": ["inst_shares", "inst_holders"], "func": iex_093_shares_per_holder_yoy_pct},
    "iex_094_shares_per_holder_zscore_4q": {"inputs": ["inst_shares", "inst_holders"], "func": iex_094_shares_per_holder_zscore_4q},
    "iex_095_value_per_holder_qoq_diff": {"inputs": ["inst_value", "inst_holders"], "func": iex_095_value_per_holder_qoq_diff},
    "iex_096_value_per_holder_yoy_pct": {"inputs": ["inst_value", "inst_holders"], "func": iex_096_value_per_holder_yoy_pct},
    "iex_097_value_per_holder_zscore_4q": {"inputs": ["inst_value", "inst_holders"], "func": iex_097_value_per_holder_zscore_4q},
    "iex_098_holder_count_pct_from_3y_max": {"inputs": ["inst_holders"], "func": iex_098_holder_count_pct_from_3y_max},
    "iex_099_inst_shares_pct_from_3y_max": {"inputs": ["inst_shares"], "func": iex_099_inst_shares_pct_from_3y_max},
    "iex_100_inst_pct_pct_from_3y_max": {"inputs": ["inst_pct"], "func": iex_100_inst_pct_pct_from_3y_max},
    "iex_101_net_exits_4q_rolling_sum": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_101_net_exits_4q_rolling_sum},
    "iex_102_net_exits_4q_rolling_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_102_net_exits_4q_rolling_mean},
    "iex_103_net_exits_zscore_4q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_103_net_exits_zscore_4q},
    "iex_104_net_exits_zscore_8q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_104_net_exits_zscore_8q},
    "iex_105_holder_count_vs_expanding_mean": {"inputs": ["inst_holders"], "func": iex_105_holder_count_vs_expanding_mean},
    "iex_106_inst_shares_vs_expanding_mean": {"inputs": ["inst_shares"], "func": iex_106_inst_shares_vs_expanding_mean},
    "iex_107_inst_pct_vs_expanding_mean": {"inputs": ["inst_pct"], "func": iex_107_inst_pct_vs_expanding_mean},
    "iex_108_holder_count_ewm_span8q_deviation": {"inputs": ["inst_holders"], "func": iex_108_holder_count_ewm_span8q_deviation},
    "iex_109_inst_shares_ewm_span8q_deviation": {"inputs": ["inst_shares"], "func": iex_109_inst_shares_ewm_span8q_deviation},
    "iex_110_inst_pct_ewm_span8q_deviation": {"inputs": ["inst_pct"], "func": iex_110_inst_pct_ewm_span8q_deviation},
    "iex_111_closed_positions_pct_rank_4q": {"inputs": ["closed_positions"], "func": iex_111_closed_positions_pct_rank_4q},
    "iex_112_decreased_positions_pct_rank_4q": {"inputs": ["decreased_positions"], "func": iex_112_decreased_positions_pct_rank_4q},
    "iex_113_net_exits_pct_rank_4q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_113_net_exits_pct_rank_4q},
    "iex_114_net_exits_pct_rank_8q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_114_net_exits_pct_rank_8q},
    "iex_115_holder_count_vs_12q_ago": {"inputs": ["inst_holders"], "func": iex_115_holder_count_vs_12q_ago},
    "iex_116_inst_shares_vs_12q_ago": {"inputs": ["inst_shares"], "func": iex_116_inst_shares_vs_12q_ago},
    "iex_117_inst_pct_vs_12q_ago": {"inputs": ["inst_pct"], "func": iex_117_inst_pct_vs_12q_ago},
    "iex_118_exit_breadth_expanding_pct_rank": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_118_exit_breadth_expanding_pct_rank},
    "iex_119_holder_count_pct_chg_rolling_mean_4q": {"inputs": ["inst_holders"], "func": iex_119_holder_count_pct_chg_rolling_mean_4q},
    "iex_120_inst_shares_pct_chg_rolling_mean_4q": {"inputs": ["inst_shares"], "func": iex_120_inst_shares_pct_chg_rolling_mean_4q},
    "iex_121_inst_pct_pct_chg_rolling_mean_4q": {"inputs": ["inst_pct"], "func": iex_121_inst_pct_pct_chg_rolling_mean_4q},
    "iex_122_holder_count_qoq_below_zero_freq": {"inputs": ["inst_holders"], "func": iex_122_holder_count_qoq_below_zero_freq},
    "iex_123_inst_shares_qoq_below_zero_freq": {"inputs": ["inst_shares"], "func": iex_123_inst_shares_qoq_below_zero_freq},
    "iex_124_inst_pct_qoq_below_zero_freq": {"inputs": ["inst_pct"], "func": iex_124_inst_pct_qoq_below_zero_freq},
    "iex_125_holder_count_qoq_below_zero_freq_8q": {"inputs": ["inst_holders"], "func": iex_125_holder_count_qoq_below_zero_freq_8q},
    "iex_126_net_exits_4q_sum_vs_8q_sum_ratio": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_126_net_exits_4q_sum_vs_8q_sum_ratio},
    "iex_127_holder_count_min_4q_vs_current": {"inputs": ["inst_holders"], "func": iex_127_holder_count_min_4q_vs_current},
    "iex_128_holder_count_pct_above_4q_min": {"inputs": ["inst_holders"], "func": iex_128_holder_count_pct_above_4q_min},
    "iex_129_inst_shares_min_8q_vs_current": {"inputs": ["inst_shares"], "func": iex_129_inst_shares_min_8q_vs_current},
    "iex_130_inst_pct_min_8q_vs_current": {"inputs": ["inst_pct"], "func": iex_130_inst_pct_min_8q_vs_current},
    "iex_131_value_per_share_qoq_diff": {"inputs": ["inst_value", "inst_shares"], "func": iex_131_value_per_share_qoq_diff},
    "iex_132_holder_decay_rate_ewm": {"inputs": ["inst_holders"], "func": iex_132_holder_decay_rate_ewm},
    "iex_133_shares_decay_rate_ewm": {"inputs": ["inst_shares"], "func": iex_133_shares_decay_rate_ewm},
    "iex_134_inst_pct_decay_rate_ewm": {"inputs": ["inst_pct"], "func": iex_134_inst_pct_decay_rate_ewm},
    "iex_135_holder_count_cross_below_8q_mean": {"inputs": ["inst_holders"], "func": iex_135_holder_count_cross_below_8q_mean},
    "iex_136_inst_pct_cross_below_8q_mean": {"inputs": ["inst_pct"], "func": iex_136_inst_pct_cross_below_8q_mean},
    "iex_137_closed_increased_ratio": {"inputs": ["closed_positions", "increased_positions"], "func": iex_137_closed_increased_ratio},
    "iex_138_decreased_new_ratio": {"inputs": ["decreased_positions", "new_positions"], "func": iex_138_decreased_new_ratio},
    "iex_139_net_exit_fraction_of_holders": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"], "func": iex_139_net_exit_fraction_of_holders},
    "iex_140_holder_count_12q_slope": {"inputs": ["inst_holders"], "func": iex_140_holder_count_12q_slope},
    "iex_141_inst_value_12q_slope": {"inputs": ["inst_value"], "func": iex_141_inst_value_12q_slope},
    "iex_142_holder_count_qoq_negrun_sum": {"inputs": ["inst_holders"], "func": iex_142_holder_count_qoq_negrun_sum},
    "iex_143_shares_qoq_negrun_sum": {"inputs": ["inst_shares"], "func": iex_143_shares_qoq_negrun_sum},
    "iex_144_inst_pct_qoq_negrun_sum": {"inputs": ["inst_pct"], "func": iex_144_inst_pct_qoq_negrun_sum},
    "iex_145_time_since_holder_count_max": {"inputs": ["inst_holders"], "func": iex_145_time_since_holder_count_max},
    "iex_146_time_since_inst_pct_max": {"inputs": ["inst_pct"], "func": iex_146_time_since_inst_pct_max},
    "iex_147_time_since_inst_shares_max": {"inputs": ["inst_shares"], "func": iex_147_time_since_inst_shares_max},
    "iex_148_holder_count_4q_cv": {"inputs": ["inst_holders"], "func": iex_148_holder_count_4q_cv},
    "iex_149_quad_exit_composite": {"inputs": ["inst_holders", "inst_shares", "inst_pct", "inst_value"], "func": iex_149_quad_exit_composite},
    "iex_150_holder_count_qoq_diff_vs_8q_mean_diff": {"inputs": ["inst_holders"], "func": iex_150_holder_count_qoq_diff_vs_8q_mean_diff},
    "iex_176_inst_value_vs_expanding_mean": {"inputs": ["inst_value"], "func": iex_176_inst_value_vs_expanding_mean},
    "iex_177_inst_value_3y_diff": {"inputs": ["inst_value"], "func": iex_177_inst_value_3y_diff},
    "iex_178_inst_value_8q_rolling_rank": {"inputs": ["inst_value"], "func": iex_178_inst_value_8q_rolling_rank},
    "iex_179_inst_value_ewm_span8q_deviation": {"inputs": ["inst_value"], "func": iex_179_inst_value_ewm_span8q_deviation},
    "iex_180_inst_value_ewm_ratio": {"inputs": ["inst_value"], "func": iex_180_inst_value_ewm_ratio},
    "iex_181_closed_positions_8q_sum": {"inputs": ["closed_positions"], "func": iex_181_closed_positions_8q_sum},
    "iex_182_net_exits_8q_rolling_sum": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_182_net_exits_8q_rolling_sum},
    "iex_183_holder_count_qoq_diff_8q_sum": {"inputs": ["inst_holders"], "func": iex_183_holder_count_qoq_diff_8q_sum},
    "iex_184_inst_shares_qoq_diff_8q_sum": {"inputs": ["inst_shares"], "func": iex_184_inst_shares_qoq_diff_8q_sum},
    "iex_185_inst_pct_pct_from_8q_min": {"inputs": ["inst_pct"], "func": iex_185_inst_pct_pct_from_8q_min},
    "iex_186_holder_count_below_8q_mean_streak": {"inputs": ["inst_holders"], "func": iex_186_holder_count_below_8q_mean_streak},
    "iex_187_inst_shares_below_8q_mean_streak": {"inputs": ["inst_shares"], "func": iex_187_inst_shares_below_8q_mean_streak},
    "iex_188_exit_breadth_8q_zscore": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_188_exit_breadth_8q_zscore},
    "iex_189_net_exits_ratio_4q_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_189_net_exits_ratio_4q_mean},
    "iex_190_new_positions_yoy_pct": {"inputs": ["new_positions"], "func": iex_190_new_positions_yoy_pct},
    "iex_191_increased_positions_yoy_pct": {"inputs": ["increased_positions"], "func": iex_191_increased_positions_yoy_pct},
    "iex_192_closed_positions_ewm_ratio": {"inputs": ["closed_positions"], "func": iex_192_closed_positions_ewm_ratio},
    "iex_193_decreased_positions_ewm_ratio": {"inputs": ["decreased_positions"], "func": iex_193_decreased_positions_ewm_ratio},
    "iex_194_holder_count_vs_4q_median": {"inputs": ["inst_holders"], "func": iex_194_holder_count_vs_4q_median},
    "iex_195_inst_shares_vs_4q_median": {"inputs": ["inst_shares"], "func": iex_195_inst_shares_vs_4q_median},
    "iex_196_inst_pct_vs_4q_median": {"inputs": ["inst_pct"], "func": iex_196_inst_pct_vs_4q_median},
    "iex_197_value_drawdown_pct_from_8q_max": {"inputs": ["inst_value"], "func": iex_197_value_drawdown_pct_from_8q_max},
    "iex_198_closed_to_decreased_ratio": {"inputs": ["closed_positions", "decreased_positions"], "func": iex_198_closed_to_decreased_ratio},
    "iex_199_entry_exit_total_activity": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_199_entry_exit_total_activity},
    "iex_200_exit_fraction_of_total_activity": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_200_exit_fraction_of_total_activity},
}
