"""
91_institutional_exit — Base Features 001–100
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
# Feature functions 001–075
# ---------------------------------------------------------------------------

def iex_001_holder_count_qoq_diff(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in institutional holder count (1-quarter lag)."""
    return inst_holders - inst_holders.shift(_TD_QTR)


def iex_002_holder_count_qoq_pct(inst_holders: pd.Series) -> pd.Series:
    """QoQ % change in institutional holder count."""
    return _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                     inst_holders.shift(_TD_QTR).abs())


def iex_003_holder_count_yoy_diff(inst_holders: pd.Series) -> pd.Series:
    """Year-over-year change in institutional holder count."""
    return inst_holders - inst_holders.shift(_TD_YEAR)


def iex_004_holder_count_yoy_pct(inst_holders: pd.Series) -> pd.Series:
    """Year-over-year % change in institutional holder count."""
    return _safe_div(inst_holders - inst_holders.shift(_TD_YEAR),
                     inst_holders.shift(_TD_YEAR).abs())


def iex_005_holder_count_2y_pct(inst_holders: pd.Series) -> pd.Series:
    """2-year cumulative % change in institutional holder count."""
    return _safe_div(inst_holders - inst_holders.shift(_TD_2Y),
                     inst_holders.shift(_TD_2Y).abs())


def iex_006_holder_count_3y_pct(inst_holders: pd.Series) -> pd.Series:
    """3-year cumulative % change in institutional holder count."""
    return _safe_div(inst_holders - inst_holders.shift(_TD_3Y),
                     inst_holders.shift(_TD_3Y).abs())


def iex_007_holder_count_rolling_min_4q(inst_holders: pd.Series) -> pd.Series:
    """Rolling 4-quarter minimum of holder count (depth of trough)."""
    return _rolling_min(inst_holders, _TD_YEAR)


def iex_008_holder_count_pct_from_4q_max(inst_holders: pd.Series) -> pd.Series:
    """Current holder count as % drawdown from 4-quarter rolling max."""
    mx = _rolling_max(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders - mx, mx.abs())


def iex_009_holder_count_pct_from_8q_max(inst_holders: pd.Series) -> pd.Series:
    """Current holder count as % drawdown from 8-quarter rolling max."""
    mx = _rolling_max(inst_holders, _TD_2Y)
    return _safe_div(inst_holders - mx, mx.abs())


def iex_010_holder_count_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    """Z-score of holder count over rolling 4-quarter window."""
    return _zscore_rolling(inst_holders, _TD_YEAR)


def iex_011_holder_count_zscore_8q(inst_holders: pd.Series) -> pd.Series:
    """Z-score of holder count over rolling 8-quarter window."""
    return _zscore_rolling(inst_holders, _TD_2Y)


def iex_012_holder_count_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """Deviation of holder count from its EWM (span=4q)."""
    return inst_holders - _ewm_mean(inst_holders, _TD_YEAR)


def iex_013_consecutive_qoq_holder_declines(inst_holders: pd.Series) -> pd.Series:
    """Count of consecutive quarters with declining holder count."""
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    declining = (diff < 0).astype(int)
    result = declining.copy().astype(float)
    count = 0.0
    for i in range(len(result)):
        if declining.iloc[i] == 1:
            count += 1
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_014_inst_shares_qoq_diff(inst_shares: pd.Series) -> pd.Series:
    """QoQ change in aggregate institutional shares held."""
    return inst_shares - inst_shares.shift(_TD_QTR)


def iex_015_inst_shares_qoq_pct(inst_shares: pd.Series) -> pd.Series:
    """QoQ % change in aggregate institutional shares held."""
    return _safe_div(inst_shares - inst_shares.shift(_TD_QTR),
                     inst_shares.shift(_TD_QTR).abs())


def iex_016_inst_shares_yoy_pct(inst_shares: pd.Series) -> pd.Series:
    """Year-over-year % change in aggregate institutional shares held."""
    return _safe_div(inst_shares - inst_shares.shift(_TD_YEAR),
                     inst_shares.shift(_TD_YEAR).abs())


def iex_017_inst_shares_2y_pct(inst_shares: pd.Series) -> pd.Series:
    """2-year % change in aggregate institutional shares held."""
    return _safe_div(inst_shares - inst_shares.shift(_TD_2Y),
                     inst_shares.shift(_TD_2Y).abs())


def iex_018_inst_shares_pct_from_4q_max(inst_shares: pd.Series) -> pd.Series:
    """Aggregate shares drawdown from 4q rolling maximum."""
    mx = _rolling_max(inst_shares, _TD_YEAR)
    return _safe_div(inst_shares - mx, mx.abs())


def iex_019_inst_shares_pct_from_8q_max(inst_shares: pd.Series) -> pd.Series:
    """Aggregate shares drawdown from 8q rolling maximum."""
    mx = _rolling_max(inst_shares, _TD_2Y)
    return _safe_div(inst_shares - mx, mx.abs())


def iex_020_inst_shares_zscore_4q(inst_shares: pd.Series) -> pd.Series:
    """Z-score of aggregate shares over rolling 4-quarter window."""
    return _zscore_rolling(inst_shares, _TD_YEAR)


def iex_021_inst_shares_ewm_deviation(inst_shares: pd.Series) -> pd.Series:
    """Deviation of aggregate shares from EWM (span=4q)."""
    return inst_shares - _ewm_mean(inst_shares, _TD_YEAR)


def iex_022_inst_value_qoq_diff(inst_value: pd.Series) -> pd.Series:
    """QoQ change in aggregate institutional USD value held."""
    return inst_value - inst_value.shift(_TD_QTR)


def iex_023_inst_value_qoq_pct(inst_value: pd.Series) -> pd.Series:
    """QoQ % change in aggregate institutional USD value held."""
    return _safe_div(inst_value - inst_value.shift(_TD_QTR),
                     inst_value.shift(_TD_QTR).abs())


def iex_024_inst_value_yoy_pct(inst_value: pd.Series) -> pd.Series:
    """Year-over-year % change in aggregate institutional USD value."""
    return _safe_div(inst_value - inst_value.shift(_TD_YEAR),
                     inst_value.shift(_TD_YEAR).abs())


def iex_025_inst_value_2y_pct(inst_value: pd.Series) -> pd.Series:
    """2-year % change in aggregate institutional USD value."""
    return _safe_div(inst_value - inst_value.shift(_TD_2Y),
                     inst_value.shift(_TD_2Y).abs())


def iex_026_inst_value_pct_from_4q_max(inst_value: pd.Series) -> pd.Series:
    """Aggregate value drawdown from 4q rolling maximum."""
    mx = _rolling_max(inst_value, _TD_YEAR)
    return _safe_div(inst_value - mx, mx.abs())


def iex_027_inst_value_zscore_4q(inst_value: pd.Series) -> pd.Series:
    """Z-score of aggregate value over rolling 4-quarter window."""
    return _zscore_rolling(inst_value, _TD_YEAR)


def iex_028_inst_pct_qoq_diff(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in institutional ownership fraction."""
    return inst_pct - inst_pct.shift(_TD_QTR)


def iex_029_inst_pct_yoy_diff(inst_pct: pd.Series) -> pd.Series:
    """Year-over-year change in institutional ownership fraction."""
    return inst_pct - inst_pct.shift(_TD_YEAR)


def iex_030_inst_pct_2y_diff(inst_pct: pd.Series) -> pd.Series:
    """2-year change in institutional ownership fraction."""
    return inst_pct - inst_pct.shift(_TD_2Y)


def iex_031_inst_pct_3y_diff(inst_pct: pd.Series) -> pd.Series:
    """3-year change in institutional ownership fraction."""
    return inst_pct - inst_pct.shift(_TD_3Y)


def iex_032_inst_pct_pct_from_4q_max(inst_pct: pd.Series) -> pd.Series:
    """Institutional ownership fraction drawdown from 4q max."""
    mx = _rolling_max(inst_pct, _TD_YEAR)
    return _safe_div(inst_pct - mx, mx.abs())


def iex_033_inst_pct_zscore_4q(inst_pct: pd.Series) -> pd.Series:
    """Z-score of inst_pct over rolling 4-quarter window."""
    return _zscore_rolling(inst_pct, _TD_YEAR)


def iex_034_inst_pct_rolling_min_4q(inst_pct: pd.Series) -> pd.Series:
    """Rolling 4q minimum of institutional ownership fraction."""
    return _rolling_min(inst_pct, _TD_YEAR)


def iex_035_net_exits_qoq(closed_positions: pd.Series,
                           decreased_positions: pd.Series,
                           new_positions: pd.Series,
                           increased_positions: pd.Series) -> pd.Series:
    """Net exits = (closed + decreased) - (new + increased) this quarter."""
    return (closed_positions + decreased_positions) - (new_positions + increased_positions)


def iex_036_net_exits_ratio(closed_positions: pd.Series,
                             decreased_positions: pd.Series,
                             new_positions: pd.Series,
                             increased_positions: pd.Series) -> pd.Series:
    """Net exits ratio = (closed+decreased) / (new+increased+EPS)."""
    return _safe_div(closed_positions + decreased_positions,
                     new_positions + increased_positions)


def iex_037_closed_positions_qoq_diff(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in count of fully-closed positions."""
    return closed_positions - closed_positions.shift(_TD_QTR)


def iex_038_closed_positions_yoy_pct(closed_positions: pd.Series) -> pd.Series:
    """YoY % change in count of fully-closed positions."""
    return _safe_div(closed_positions - closed_positions.shift(_TD_YEAR),
                     closed_positions.shift(_TD_YEAR).abs())


def iex_039_closed_positions_share_of_holders(closed_positions: pd.Series,
                                               inst_holders: pd.Series) -> pd.Series:
    """Closed positions as a fraction of total institutional holders."""
    return _safe_div(closed_positions, inst_holders)


def iex_040_decreased_positions_share(decreased_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Decreased positions as a fraction of total institutional holders."""
    return _safe_div(decreased_positions, inst_holders)


def iex_041_exit_breadth(closed_positions: pd.Series,
                          decreased_positions: pd.Series,
                          inst_holders: pd.Series) -> pd.Series:
    """(Closed + decreased) / total holders — fraction of base reducing."""
    return _safe_div(closed_positions + decreased_positions, inst_holders)


def iex_042_exit_breadth_rolling_mean_4q(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """4-quarter rolling mean of exit breadth."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _rolling_mean(breadth, _TD_YEAR)


def iex_043_exit_breadth_zscore_4q(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    inst_holders: pd.Series) -> pd.Series:
    """Z-score of exit breadth over 4-quarter window."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _zscore_rolling(breadth, _TD_YEAR)


def iex_044_new_vs_closed_ratio(new_positions: pd.Series,
                                 closed_positions: pd.Series) -> pd.Series:
    """Ratio of new positions opened to positions closed (below 1 = net exit)."""
    return _safe_div(new_positions, closed_positions)


def iex_045_new_vs_closed_ratio_4q_mean(new_positions: pd.Series,
                                         closed_positions: pd.Series) -> pd.Series:
    """4q rolling mean of (new / closed) ratio."""
    ratio = _safe_div(new_positions, closed_positions)
    return _rolling_mean(ratio, _TD_YEAR)


def iex_046_holder_count_4q_slope(inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder count over rolling 4-quarter window."""
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
    return inst_holders.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def iex_047_holder_count_8q_slope(inst_holders: pd.Series) -> pd.Series:
    """OLS slope of holder count over rolling 8-quarter window."""
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
    return inst_holders.rolling(_TD_2Y, min_periods=4).apply(_slope, raw=True)


def iex_048_inst_shares_4q_slope(inst_shares: pd.Series) -> pd.Series:
    """OLS slope of aggregate shares over rolling 4-quarter window."""
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
    return inst_shares.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def iex_049_inst_pct_4q_slope(inst_pct: pd.Series) -> pd.Series:
    """OLS slope of institutional ownership fraction over 4-quarter window."""
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
    return inst_pct.rolling(_TD_YEAR, min_periods=4).apply(_slope, raw=True)


def iex_050_holder_count_expanding_pct_rank(inst_holders: pd.Series) -> pd.Series:
    """Expanding percentile rank of current holder count (low = historically depleted)."""
    return inst_holders.expanding(min_periods=2).rank(pct=True)


def iex_051_inst_shares_expanding_pct_rank(inst_shares: pd.Series) -> pd.Series:
    """Expanding percentile rank of aggregate shares held."""
    return inst_shares.expanding(min_periods=2).rank(pct=True)


def iex_052_inst_pct_expanding_pct_rank(inst_pct: pd.Series) -> pd.Series:
    """Expanding percentile rank of institutional ownership fraction."""
    return inst_pct.expanding(min_periods=2).rank(pct=True)


def iex_053_holder_count_drawdown_duration(inst_holders: pd.Series) -> pd.Series:
    """
    Number of trading days since the rolling 4-year peak in holder count
    (proxy for duration of the institutional exit episode).
    """
    win = _TD_YEAR * 4
    rolling_peak_idx = inst_holders.rolling(win, min_periods=1).apply(
        lambda x: len(x) - 1 - np.argmax(x[::-1]), raw=True
    )
    return rolling_peak_idx


def iex_054_inst_shares_drawdown_from_peak(inst_shares: pd.Series) -> pd.Series:
    """Drawdown of aggregate shares from expanding historical maximum."""
    peak = inst_shares.expanding(min_periods=1).max()
    return _safe_div(inst_shares - peak, peak.abs())


def iex_055_inst_pct_drawdown_from_peak(inst_pct: pd.Series) -> pd.Series:
    """Drawdown of institutional ownership fraction from expanding historical maximum."""
    peak = inst_pct.expanding(min_periods=1).max()
    return _safe_div(inst_pct - peak, peak.abs())


def iex_056_holders_drawdown_from_peak(inst_holders: pd.Series) -> pd.Series:
    """Drawdown of holder count from expanding historical maximum."""
    peak = inst_holders.expanding(min_periods=1).max()
    return _safe_div(inst_holders - peak, peak.abs())


def iex_057_value_drawdown_from_peak(inst_value: pd.Series) -> pd.Series:
    """Drawdown of aggregate institutional value from expanding historical maximum."""
    peak = inst_value.expanding(min_periods=1).max()
    return _safe_div(inst_value - peak, peak.abs())


def iex_058_exit_acceleration_1q(closed_positions: pd.Series,
                                   decreased_positions: pd.Series,
                                   new_positions: pd.Series,
                                   increased_positions: pd.Series) -> pd.Series:
    """1Q acceleration of net exits (2nd diff of net exit series)."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return (net - net.shift(_TD_QTR)) - (net.shift(_TD_QTR) - net.shift(_TD_2Q))


def iex_059_holder_decline_acceleration(inst_holders: pd.Series) -> pd.Series:
    """Acceleration of holder count decline (2nd diff QoQ)."""
    diff1 = inst_holders - inst_holders.shift(_TD_QTR)
    diff2 = diff1 - diff1.shift(_TD_QTR)
    return diff2


def iex_060_shares_decline_acceleration(inst_shares: pd.Series) -> pd.Series:
    """Acceleration of aggregate-shares decline (2nd diff QoQ)."""
    diff1 = inst_shares - inst_shares.shift(_TD_QTR)
    diff2 = diff1 - diff1.shift(_TD_QTR)
    return diff2


def iex_061_inst_pct_decline_acceleration(inst_pct: pd.Series) -> pd.Series:
    """Acceleration of institutional ownership fraction decline (2nd diff QoQ)."""
    diff1 = inst_pct - inst_pct.shift(_TD_QTR)
    diff2 = diff1 - diff1.shift(_TD_QTR)
    return diff2


def iex_062_holder_count_4q_rolling_rank(inst_holders: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of holder count."""
    return _rolling_rank_pct(inst_holders, _TD_YEAR)


def iex_063_inst_shares_4q_rolling_rank(inst_shares: pd.Series) -> pd.Series:
    """Rolling 4-quarter percentile rank of aggregate shares."""
    return _rolling_rank_pct(inst_shares, _TD_YEAR)


def iex_064_inst_pct_8q_rolling_rank(inst_pct: pd.Series) -> pd.Series:
    """Rolling 8-quarter percentile rank of institutional ownership fraction."""
    return _rolling_rank_pct(inst_pct, _TD_2Y)


def iex_065_holder_count_ewm_ratio(inst_holders: pd.Series) -> pd.Series:
    """Ratio of holder count to its EWM (span=4q); below 1 = below trend."""
    return _safe_div(inst_holders, _ewm_mean(inst_holders, _TD_YEAR))


def iex_066_inst_shares_ewm_ratio(inst_shares: pd.Series) -> pd.Series:
    """Ratio of aggregate shares to EWM (span=4q)."""
    return _safe_div(inst_shares, _ewm_mean(inst_shares, _TD_YEAR))


def iex_067_inst_pct_ewm_ratio(inst_pct: pd.Series) -> pd.Series:
    """Ratio of institutional ownership fraction to EWM (span=4q)."""
    return _safe_div(inst_pct, _ewm_mean(inst_pct, _TD_YEAR))


def iex_068_net_exit_ewm_deviation(closed_positions: pd.Series,
                                    decreased_positions: pd.Series,
                                    new_positions: pd.Series,
                                    increased_positions: pd.Series) -> pd.Series:
    """EWM deviation of net exits (current - EWM(span=4q))."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return net - _ewm_mean(net, _TD_YEAR)


def iex_069_holder_count_value_composite(inst_holders: pd.Series,
                                          inst_value: pd.Series) -> pd.Series:
    """
    Composite exit score: average of QoQ % declines in holder count and USD value.
    Negative = institutions shrinking both dimensions simultaneously.
    """
    h_pct = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                      inst_holders.shift(_TD_QTR).abs())
    v_pct = _safe_div(inst_value - inst_value.shift(_TD_QTR),
                      inst_value.shift(_TD_QTR).abs())
    return (h_pct + v_pct) / 2.0


def iex_070_triple_exit_composite(inst_holders: pd.Series,
                                   inst_shares: pd.Series,
                                   inst_pct: pd.Series) -> pd.Series:
    """
    Triple composite: average of QoQ % change in holders, shares, and ownership %.
    All negative = broad institutional departure signal.
    """
    h = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                  inst_holders.shift(_TD_QTR).abs())
    s = _safe_div(inst_shares - inst_shares.shift(_TD_QTR),
                  inst_shares.shift(_TD_QTR).abs())
    p = inst_pct - inst_pct.shift(_TD_QTR)
    return (h + s + p) / 3.0


def iex_071_holder_count_below_4q_mean(inst_holders: pd.Series) -> pd.Series:
    """Binary: 1 if holder count is below its 4-quarter rolling mean."""
    mean4q = _rolling_mean(inst_holders, _TD_YEAR)
    return (inst_holders < mean4q).astype(float)


def iex_072_consecutive_below_4q_mean(inst_holders: pd.Series) -> pd.Series:
    """Count of consecutive days holder count is below its 4q rolling mean."""
    mean4q = _rolling_mean(inst_holders, _TD_YEAR)
    below = (inst_holders < mean4q).astype(int)
    result = below.copy().astype(float)
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_073_inst_pct_below_4q_mean_streak(inst_pct: pd.Series) -> pd.Series:
    """Count of consecutive days institutional ownership fraction is below its 4q mean."""
    mean4q = _rolling_mean(inst_pct, _TD_YEAR)
    below = (inst_pct < mean4q).astype(int)
    result = below.copy().astype(float)
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_074_closed_to_total_ratio_rolling_mean(closed_positions: pd.Series,
                                                inst_holders: pd.Series) -> pd.Series:
    """4q rolling mean of (closed positions / total holders)."""
    ratio = _safe_div(closed_positions, inst_holders)
    return _rolling_mean(ratio, _TD_YEAR)


def iex_075_holder_count_median_deviation(inst_holders: pd.Series) -> pd.Series:
    """Deviation of holder count from 4-quarter rolling median."""
    med = _rolling_median(inst_holders, _TD_YEAR)
    return inst_holders - med


def iex_151_inst_value_zscore_8q(inst_value: pd.Series) -> pd.Series:
    """Z-score of aggregate institutional value over rolling 8-quarter window."""
    return _zscore_rolling(inst_value, _TD_2Y)


def iex_152_inst_value_pct_from_8q_max(inst_value: pd.Series) -> pd.Series:
    """Aggregate value drawdown from 8q rolling maximum."""
    mx = _rolling_max(inst_value, _TD_2Y)
    return _safe_div(inst_value - mx, mx.abs())


def iex_153_inst_value_pct_from_3y_max(inst_value: pd.Series) -> pd.Series:
    """Aggregate value drawdown from 3-year rolling maximum."""
    mx = _rolling_max(inst_value, _TD_3Y)
    return _safe_div(inst_value - mx, mx.abs())


def iex_154_inst_value_expanding_pct_rank(inst_value: pd.Series) -> pd.Series:
    """Expanding percentile rank of aggregate institutional value."""
    return inst_value.expanding(min_periods=2).rank(pct=True)


def iex_155_inst_shares_rolling_std_8q(inst_shares: pd.Series) -> pd.Series:
    """Rolling 8q standard deviation of aggregate shares held."""
    return _rolling_std(inst_shares, _TD_2Y)


def iex_156_inst_pct_rolling_std_4q(inst_pct: pd.Series) -> pd.Series:
    """Rolling 4q standard deviation of institutional ownership fraction."""
    return _rolling_std(inst_pct, _TD_YEAR)


def iex_157_inst_pct_rolling_std_8q(inst_pct: pd.Series) -> pd.Series:
    """Rolling 8q standard deviation of institutional ownership fraction."""
    return _rolling_std(inst_pct, _TD_2Y)


def iex_158_inst_value_4q_cv(inst_value: pd.Series) -> pd.Series:
    """Coefficient of variation of aggregate value over rolling 4-quarter window."""
    mu = _rolling_mean(inst_value, _TD_YEAR)
    sigma = _rolling_std(inst_value, _TD_YEAR)
    return _safe_div(sigma, mu.abs())


def iex_159_inst_shares_4q_cv(inst_shares: pd.Series) -> pd.Series:
    """Coefficient of variation of aggregate shares over rolling 4-quarter window."""
    mu = _rolling_mean(inst_shares, _TD_YEAR)
    sigma = _rolling_std(inst_shares, _TD_YEAR)
    return _safe_div(sigma, mu.abs())


def iex_160_closed_positions_4q_sum(closed_positions: pd.Series) -> pd.Series:
    """Rolling 4-quarter cumulative sum of fully-closed positions."""
    return _rolling_sum(closed_positions, _TD_YEAR)


def iex_161_decreased_positions_4q_sum(decreased_positions: pd.Series) -> pd.Series:
    """Rolling 4-quarter cumulative sum of decreased positions."""
    return _rolling_sum(decreased_positions, _TD_YEAR)


def iex_162_new_positions_4q_sum(new_positions: pd.Series) -> pd.Series:
    """Rolling 4-quarter cumulative sum of new positions."""
    return _rolling_sum(new_positions, _TD_YEAR)


def iex_163_increased_positions_4q_sum(increased_positions: pd.Series) -> pd.Series:
    """Rolling 4-quarter cumulative sum of increased positions."""
    return _rolling_sum(increased_positions, _TD_YEAR)


def iex_164_closed_positions_qoq_pct(closed_positions: pd.Series) -> pd.Series:
    """QoQ % change in closed-position count."""
    return _safe_div(closed_positions - closed_positions.shift(_TD_QTR),
                     closed_positions.shift(_TD_QTR).abs())


def iex_165_decreased_positions_qoq_pct(decreased_positions: pd.Series) -> pd.Series:
    """QoQ % change in decreased-position count."""
    return _safe_div(decreased_positions - decreased_positions.shift(_TD_QTR),
                     decreased_positions.shift(_TD_QTR).abs())


def iex_166_new_positions_qoq_pct(new_positions: pd.Series) -> pd.Series:
    """QoQ % change in new-position count."""
    return _safe_div(new_positions - new_positions.shift(_TD_QTR),
                     new_positions.shift(_TD_QTR).abs())


def iex_167_holder_count_qoq_diff_normalized(inst_holders: pd.Series) -> pd.Series:
    """QoQ holder-count diff normalized by rolling 4q std (signal-to-noise)."""
    diff = inst_holders - inst_holders.shift(_TD_QTR)
    sigma = _rolling_std(diff, _TD_YEAR)
    return _safe_div(diff, sigma)


def iex_168_inst_shares_qoq_diff_normalized(inst_shares: pd.Series) -> pd.Series:
    """QoQ shares diff normalized by rolling 4q std."""
    diff = inst_shares - inst_shares.shift(_TD_QTR)
    sigma = _rolling_std(diff, _TD_YEAR)
    return _safe_div(diff, sigma)


def iex_169_inst_pct_rolling_min_8q(inst_pct: pd.Series) -> pd.Series:
    """Rolling 8-quarter minimum of institutional ownership fraction."""
    return _rolling_min(inst_pct, _TD_2Y)


def iex_170_inst_shares_rolling_min_8q(inst_shares: pd.Series) -> pd.Series:
    """Rolling 8-quarter minimum of aggregate shares held."""
    return _rolling_min(inst_shares, _TD_2Y)


def iex_171_exit_breadth_8q_rolling_mean(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """8-quarter rolling mean of exit breadth."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _rolling_mean(breadth, _TD_2Y)


def iex_172_net_exits_8q_rolling_mean(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """Rolling 8-quarter mean of net exits."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _rolling_mean(net, _TD_2Y)


def iex_173_holder_count_2q_diff(inst_holders: pd.Series) -> pd.Series:
    """Change in holder count over 2 quarters."""
    return inst_holders - inst_holders.shift(_TD_2Q)


def iex_174_inst_shares_2q_diff(inst_shares: pd.Series) -> pd.Series:
    """Change in aggregate shares held over 2 quarters."""
    return inst_shares - inst_shares.shift(_TD_2Q)


def iex_175_inst_pct_2q_diff(inst_pct: pd.Series) -> pd.Series:
    """Change in institutional ownership fraction over 2 quarters."""
    return inst_pct - inst_pct.shift(_TD_2Q)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
INSTITUTIONAL_EXIT_REGISTRY_001_075 = {
    "iex_001_holder_count_qoq_diff": {"inputs": ["inst_holders"], "func": iex_001_holder_count_qoq_diff},
    "iex_002_holder_count_qoq_pct": {"inputs": ["inst_holders"], "func": iex_002_holder_count_qoq_pct},
    "iex_003_holder_count_yoy_diff": {"inputs": ["inst_holders"], "func": iex_003_holder_count_yoy_diff},
    "iex_004_holder_count_yoy_pct": {"inputs": ["inst_holders"], "func": iex_004_holder_count_yoy_pct},
    "iex_005_holder_count_2y_pct": {"inputs": ["inst_holders"], "func": iex_005_holder_count_2y_pct},
    "iex_006_holder_count_3y_pct": {"inputs": ["inst_holders"], "func": iex_006_holder_count_3y_pct},
    "iex_007_holder_count_rolling_min_4q": {"inputs": ["inst_holders"], "func": iex_007_holder_count_rolling_min_4q},
    "iex_008_holder_count_pct_from_4q_max": {"inputs": ["inst_holders"], "func": iex_008_holder_count_pct_from_4q_max},
    "iex_009_holder_count_pct_from_8q_max": {"inputs": ["inst_holders"], "func": iex_009_holder_count_pct_from_8q_max},
    "iex_010_holder_count_zscore_4q": {"inputs": ["inst_holders"], "func": iex_010_holder_count_zscore_4q},
    "iex_011_holder_count_zscore_8q": {"inputs": ["inst_holders"], "func": iex_011_holder_count_zscore_8q},
    "iex_012_holder_count_ewm_deviation": {"inputs": ["inst_holders"], "func": iex_012_holder_count_ewm_deviation},
    "iex_013_consecutive_qoq_holder_declines": {"inputs": ["inst_holders"], "func": iex_013_consecutive_qoq_holder_declines},
    "iex_014_inst_shares_qoq_diff": {"inputs": ["inst_shares"], "func": iex_014_inst_shares_qoq_diff},
    "iex_015_inst_shares_qoq_pct": {"inputs": ["inst_shares"], "func": iex_015_inst_shares_qoq_pct},
    "iex_016_inst_shares_yoy_pct": {"inputs": ["inst_shares"], "func": iex_016_inst_shares_yoy_pct},
    "iex_017_inst_shares_2y_pct": {"inputs": ["inst_shares"], "func": iex_017_inst_shares_2y_pct},
    "iex_018_inst_shares_pct_from_4q_max": {"inputs": ["inst_shares"], "func": iex_018_inst_shares_pct_from_4q_max},
    "iex_019_inst_shares_pct_from_8q_max": {"inputs": ["inst_shares"], "func": iex_019_inst_shares_pct_from_8q_max},
    "iex_020_inst_shares_zscore_4q": {"inputs": ["inst_shares"], "func": iex_020_inst_shares_zscore_4q},
    "iex_021_inst_shares_ewm_deviation": {"inputs": ["inst_shares"], "func": iex_021_inst_shares_ewm_deviation},
    "iex_022_inst_value_qoq_diff": {"inputs": ["inst_value"], "func": iex_022_inst_value_qoq_diff},
    "iex_023_inst_value_qoq_pct": {"inputs": ["inst_value"], "func": iex_023_inst_value_qoq_pct},
    "iex_024_inst_value_yoy_pct": {"inputs": ["inst_value"], "func": iex_024_inst_value_yoy_pct},
    "iex_025_inst_value_2y_pct": {"inputs": ["inst_value"], "func": iex_025_inst_value_2y_pct},
    "iex_026_inst_value_pct_from_4q_max": {"inputs": ["inst_value"], "func": iex_026_inst_value_pct_from_4q_max},
    "iex_027_inst_value_zscore_4q": {"inputs": ["inst_value"], "func": iex_027_inst_value_zscore_4q},
    "iex_028_inst_pct_qoq_diff": {"inputs": ["inst_pct"], "func": iex_028_inst_pct_qoq_diff},
    "iex_029_inst_pct_yoy_diff": {"inputs": ["inst_pct"], "func": iex_029_inst_pct_yoy_diff},
    "iex_030_inst_pct_2y_diff": {"inputs": ["inst_pct"], "func": iex_030_inst_pct_2y_diff},
    "iex_031_inst_pct_3y_diff": {"inputs": ["inst_pct"], "func": iex_031_inst_pct_3y_diff},
    "iex_032_inst_pct_pct_from_4q_max": {"inputs": ["inst_pct"], "func": iex_032_inst_pct_pct_from_4q_max},
    "iex_033_inst_pct_zscore_4q": {"inputs": ["inst_pct"], "func": iex_033_inst_pct_zscore_4q},
    "iex_034_inst_pct_rolling_min_4q": {"inputs": ["inst_pct"], "func": iex_034_inst_pct_rolling_min_4q},
    "iex_035_net_exits_qoq": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_035_net_exits_qoq},
    "iex_036_net_exits_ratio": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_036_net_exits_ratio},
    "iex_037_closed_positions_qoq_diff": {"inputs": ["closed_positions"], "func": iex_037_closed_positions_qoq_diff},
    "iex_038_closed_positions_yoy_pct": {"inputs": ["closed_positions"], "func": iex_038_closed_positions_yoy_pct},
    "iex_039_closed_positions_share_of_holders": {"inputs": ["closed_positions", "inst_holders"], "func": iex_039_closed_positions_share_of_holders},
    "iex_040_decreased_positions_share": {"inputs": ["decreased_positions", "inst_holders"], "func": iex_040_decreased_positions_share},
    "iex_041_exit_breadth": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_041_exit_breadth},
    "iex_042_exit_breadth_rolling_mean_4q": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_042_exit_breadth_rolling_mean_4q},
    "iex_043_exit_breadth_zscore_4q": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_043_exit_breadth_zscore_4q},
    "iex_044_new_vs_closed_ratio": {"inputs": ["new_positions", "closed_positions"], "func": iex_044_new_vs_closed_ratio},
    "iex_045_new_vs_closed_ratio_4q_mean": {"inputs": ["new_positions", "closed_positions"], "func": iex_045_new_vs_closed_ratio_4q_mean},
    "iex_046_holder_count_4q_slope": {"inputs": ["inst_holders"], "func": iex_046_holder_count_4q_slope},
    "iex_047_holder_count_8q_slope": {"inputs": ["inst_holders"], "func": iex_047_holder_count_8q_slope},
    "iex_048_inst_shares_4q_slope": {"inputs": ["inst_shares"], "func": iex_048_inst_shares_4q_slope},
    "iex_049_inst_pct_4q_slope": {"inputs": ["inst_pct"], "func": iex_049_inst_pct_4q_slope},
    "iex_050_holder_count_expanding_pct_rank": {"inputs": ["inst_holders"], "func": iex_050_holder_count_expanding_pct_rank},
    "iex_051_inst_shares_expanding_pct_rank": {"inputs": ["inst_shares"], "func": iex_051_inst_shares_expanding_pct_rank},
    "iex_052_inst_pct_expanding_pct_rank": {"inputs": ["inst_pct"], "func": iex_052_inst_pct_expanding_pct_rank},
    "iex_053_holder_count_drawdown_duration": {"inputs": ["inst_holders"], "func": iex_053_holder_count_drawdown_duration},
    "iex_054_inst_shares_drawdown_from_peak": {"inputs": ["inst_shares"], "func": iex_054_inst_shares_drawdown_from_peak},
    "iex_055_inst_pct_drawdown_from_peak": {"inputs": ["inst_pct"], "func": iex_055_inst_pct_drawdown_from_peak},
    "iex_056_holders_drawdown_from_peak": {"inputs": ["inst_holders"], "func": iex_056_holders_drawdown_from_peak},
    "iex_057_value_drawdown_from_peak": {"inputs": ["inst_value"], "func": iex_057_value_drawdown_from_peak},
    "iex_058_exit_acceleration_1q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_058_exit_acceleration_1q},
    "iex_059_holder_decline_acceleration": {"inputs": ["inst_holders"], "func": iex_059_holder_decline_acceleration},
    "iex_060_shares_decline_acceleration": {"inputs": ["inst_shares"], "func": iex_060_shares_decline_acceleration},
    "iex_061_inst_pct_decline_acceleration": {"inputs": ["inst_pct"], "func": iex_061_inst_pct_decline_acceleration},
    "iex_062_holder_count_4q_rolling_rank": {"inputs": ["inst_holders"], "func": iex_062_holder_count_4q_rolling_rank},
    "iex_063_inst_shares_4q_rolling_rank": {"inputs": ["inst_shares"], "func": iex_063_inst_shares_4q_rolling_rank},
    "iex_064_inst_pct_8q_rolling_rank": {"inputs": ["inst_pct"], "func": iex_064_inst_pct_8q_rolling_rank},
    "iex_065_holder_count_ewm_ratio": {"inputs": ["inst_holders"], "func": iex_065_holder_count_ewm_ratio},
    "iex_066_inst_shares_ewm_ratio": {"inputs": ["inst_shares"], "func": iex_066_inst_shares_ewm_ratio},
    "iex_067_inst_pct_ewm_ratio": {"inputs": ["inst_pct"], "func": iex_067_inst_pct_ewm_ratio},
    "iex_068_net_exit_ewm_deviation": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_068_net_exit_ewm_deviation},
    "iex_069_holder_count_value_composite": {"inputs": ["inst_holders", "inst_value"], "func": iex_069_holder_count_value_composite},
    "iex_070_triple_exit_composite": {"inputs": ["inst_holders", "inst_shares", "inst_pct"], "func": iex_070_triple_exit_composite},
    "iex_071_holder_count_below_4q_mean": {"inputs": ["inst_holders"], "func": iex_071_holder_count_below_4q_mean},
    "iex_072_consecutive_below_4q_mean": {"inputs": ["inst_holders"], "func": iex_072_consecutive_below_4q_mean},
    "iex_073_inst_pct_below_4q_mean_streak": {"inputs": ["inst_pct"], "func": iex_073_inst_pct_below_4q_mean_streak},
    "iex_074_closed_to_total_ratio_rolling_mean": {"inputs": ["closed_positions", "inst_holders"], "func": iex_074_closed_to_total_ratio_rolling_mean},
    "iex_075_holder_count_median_deviation": {"inputs": ["inst_holders"], "func": iex_075_holder_count_median_deviation},
    "iex_151_inst_value_zscore_8q": {"inputs": ["inst_value"], "func": iex_151_inst_value_zscore_8q},
    "iex_152_inst_value_pct_from_8q_max": {"inputs": ["inst_value"], "func": iex_152_inst_value_pct_from_8q_max},
    "iex_153_inst_value_pct_from_3y_max": {"inputs": ["inst_value"], "func": iex_153_inst_value_pct_from_3y_max},
    "iex_154_inst_value_expanding_pct_rank": {"inputs": ["inst_value"], "func": iex_154_inst_value_expanding_pct_rank},
    "iex_155_inst_shares_rolling_std_8q": {"inputs": ["inst_shares"], "func": iex_155_inst_shares_rolling_std_8q},
    "iex_156_inst_pct_rolling_std_4q": {"inputs": ["inst_pct"], "func": iex_156_inst_pct_rolling_std_4q},
    "iex_157_inst_pct_rolling_std_8q": {"inputs": ["inst_pct"], "func": iex_157_inst_pct_rolling_std_8q},
    "iex_158_inst_value_4q_cv": {"inputs": ["inst_value"], "func": iex_158_inst_value_4q_cv},
    "iex_159_inst_shares_4q_cv": {"inputs": ["inst_shares"], "func": iex_159_inst_shares_4q_cv},
    "iex_160_closed_positions_4q_sum": {"inputs": ["closed_positions"], "func": iex_160_closed_positions_4q_sum},
    "iex_161_decreased_positions_4q_sum": {"inputs": ["decreased_positions"], "func": iex_161_decreased_positions_4q_sum},
    "iex_162_new_positions_4q_sum": {"inputs": ["new_positions"], "func": iex_162_new_positions_4q_sum},
    "iex_163_increased_positions_4q_sum": {"inputs": ["increased_positions"], "func": iex_163_increased_positions_4q_sum},
    "iex_164_closed_positions_qoq_pct": {"inputs": ["closed_positions"], "func": iex_164_closed_positions_qoq_pct},
    "iex_165_decreased_positions_qoq_pct": {"inputs": ["decreased_positions"], "func": iex_165_decreased_positions_qoq_pct},
    "iex_166_new_positions_qoq_pct": {"inputs": ["new_positions"], "func": iex_166_new_positions_qoq_pct},
    "iex_167_holder_count_qoq_diff_normalized": {"inputs": ["inst_holders"], "func": iex_167_holder_count_qoq_diff_normalized},
    "iex_168_inst_shares_qoq_diff_normalized": {"inputs": ["inst_shares"], "func": iex_168_inst_shares_qoq_diff_normalized},
    "iex_169_inst_pct_rolling_min_8q": {"inputs": ["inst_pct"], "func": iex_169_inst_pct_rolling_min_8q},
    "iex_170_inst_shares_rolling_min_8q": {"inputs": ["inst_shares"], "func": iex_170_inst_shares_rolling_min_8q},
    "iex_171_exit_breadth_8q_rolling_mean": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_171_exit_breadth_8q_rolling_mean},
    "iex_172_net_exits_8q_rolling_mean": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_172_net_exits_8q_rolling_mean},
    "iex_173_holder_count_2q_diff": {"inputs": ["inst_holders"], "func": iex_173_holder_count_2q_diff},
    "iex_174_inst_shares_2q_diff": {"inputs": ["inst_shares"], "func": iex_174_inst_shares_2q_diff},
    "iex_175_inst_pct_2q_diff": {"inputs": ["inst_pct"], "func": iex_175_inst_pct_2q_diff},
}
