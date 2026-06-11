"""
91_institutional_exit — Extended Features 001-075
==================================================
Domain: QoQ DECLINE in the institutional holder base — additional exit
variants NOT covered by the four base files. Explores new horizons (3q, 3y),
exit-intensity ratios, holder-bleed streak depth, drawdown duration of shares
and value, decay-weighted exit scores, dispersion of the exodus, and
cross-series composite departure signals.

NOT in scope: accumulation/new-position features (folder 93),
concentration/HHI features (folder 92), forced-liquidation breadth (folder 95).

Quarterly -> Daily Alignment Contract
--------------------------------------
All inputs are daily-frequency pandas Series forward-filled from quarterly
Sharadar SF3 13F snapshots (~63 trading days per update). Computed series are
stepwise/sparse on a daily index — expected and correct.

Input fields (all daily-frequency pandas Series, ff-filled from SF3):
    inst_holders, inst_shares, inst_value, inst_pct,
    new_positions, closed_positions, increased_positions, decreased_positions

Cadence constants: 1q=63, 2q=126, 3q=189, 1y=252, 2y=504, 3y=756 trading days.
All features are backward-looking only; no forward information.
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


def _align_quarterly_to_daily(series: pd.Series) -> pd.Series:
    """Forward-fill a quarterly Series to a daily index (idempotent if daily)."""
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


def _consec_decline_streak(s, lag):
    """Count of consecutive observations where s declined vs `lag` rows prior."""
    diff = s - s.shift(lag)
    declining = (diff < 0).astype(int)
    result = declining.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if declining.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


# ---------------------------------------------------------------------------
# Feature functions 001-075
# ---------------------------------------------------------------------------

# --- Group A (001-012): Additional decline horizons (3-quarter, 3-year) ---

def iex_ext_001_holder_count_3q_diff(inst_holders: pd.Series) -> pd.Series:
    """3-quarter change in institutional holder count."""
    h = _align_quarterly_to_daily(inst_holders)
    return h - h.shift(_TD_3Q)


def iex_ext_002_holder_count_3q_pct(inst_holders: pd.Series) -> pd.Series:
    """3-quarter % change in institutional holder count."""
    h = _align_quarterly_to_daily(inst_holders)
    return _safe_div_abs(h - h.shift(_TD_3Q), h.shift(_TD_3Q))


def iex_ext_003_inst_shares_3q_pct(inst_shares: pd.Series) -> pd.Series:
    """3-quarter % change in aggregate institutional shares held."""
    s = _align_quarterly_to_daily(inst_shares)
    return _safe_div_abs(s - s.shift(_TD_3Q), s.shift(_TD_3Q))


def iex_ext_004_inst_value_3q_pct(inst_value: pd.Series) -> pd.Series:
    """3-quarter % change in aggregate institutional USD value."""
    v = _align_quarterly_to_daily(inst_value)
    return _safe_div_abs(v - v.shift(_TD_3Q), v.shift(_TD_3Q))


def iex_ext_005_holder_count_3y_diff(inst_holders: pd.Series) -> pd.Series:
    """3-year change in institutional holder count."""
    h = _align_quarterly_to_daily(inst_holders)
    return h - h.shift(_TD_3Y)


def iex_ext_006_inst_shares_3y_pct(inst_shares: pd.Series) -> pd.Series:
    """3-year % change in aggregate institutional shares held."""
    s = _align_quarterly_to_daily(inst_shares)
    return _safe_div_abs(s - s.shift(_TD_3Y), s.shift(_TD_3Y))


def iex_ext_007_inst_pct_3q_diff(inst_pct: pd.Series) -> pd.Series:
    """3-quarter change in institutional ownership fraction."""
    p = _align_quarterly_to_daily(inst_pct)
    return p - p.shift(_TD_3Q)


def iex_ext_008_holder_count_qoq_pct_abs(inst_holders: pd.Series) -> pd.Series:
    """Absolute QoQ % change in holder count (magnitude of the move)."""
    h = _align_quarterly_to_daily(inst_holders)
    return _safe_div_abs(h - h.shift(_TD_QTR), h.shift(_TD_QTR)).abs()


def iex_ext_009_inst_value_2q_pct(inst_value: pd.Series) -> pd.Series:
    """2-quarter % change in aggregate institutional USD value."""
    v = _align_quarterly_to_daily(inst_value)
    return _safe_div_abs(v - v.shift(_TD_2Q), v.shift(_TD_2Q))


def iex_ext_010_holder_count_2q_pct(inst_holders: pd.Series) -> pd.Series:
    """2-quarter % change in institutional holder count."""
    h = _align_quarterly_to_daily(inst_holders)
    return _safe_div_abs(h - h.shift(_TD_2Q), h.shift(_TD_2Q))


def iex_ext_011_inst_pct_3y_diff(inst_pct: pd.Series) -> pd.Series:
    """3-year change in institutional ownership fraction."""
    p = _align_quarterly_to_daily(inst_pct)
    return p - p.shift(_TD_3Y)


def iex_ext_012_inst_shares_2q_pct(inst_shares: pd.Series) -> pd.Series:
    """2-quarter % change in aggregate institutional shares held."""
    s = _align_quarterly_to_daily(inst_shares)
    return _safe_div_abs(s - s.shift(_TD_2Q), s.shift(_TD_2Q))


# --- Group B (013-024): Drawdown depth / duration on shares, value, pct ---

def iex_ext_013_holder_count_pct_from_3y_max(inst_holders: pd.Series) -> pd.Series:
    """Holder count as % drawdown from 3-year rolling max."""
    h = _align_quarterly_to_daily(inst_holders)
    mx = _rolling_max(h, _TD_3Y)
    return _safe_div(h - mx, mx.abs())


def iex_ext_014_inst_shares_pct_from_3y_max(inst_shares: pd.Series) -> pd.Series:
    """Aggregate shares as % drawdown from 3-year rolling max."""
    s = _align_quarterly_to_daily(inst_shares)
    mx = _rolling_max(s, _TD_3Y)
    return _safe_div(s - mx, mx.abs())


def iex_ext_015_inst_pct_pct_from_3y_max(inst_pct: pd.Series) -> pd.Series:
    """Institutional ownership fraction as % drawdown from 3-year rolling max."""
    p = _align_quarterly_to_daily(inst_pct)
    mx = _rolling_max(p, _TD_3Y)
    return _safe_div(p - mx, mx.abs())


def iex_ext_016_inst_pct_pct_from_8q_max(inst_pct: pd.Series) -> pd.Series:
    """Institutional ownership fraction as % drawdown from 8-quarter rolling max."""
    p = _align_quarterly_to_daily(inst_pct)
    mx = _rolling_max(p, _TD_2Y)
    return _safe_div(p - mx, mx.abs())


def iex_ext_017_shares_drawdown_duration_3y(inst_shares: pd.Series) -> pd.Series:
    """Trading days since the 3-year rolling peak in aggregate shares."""
    s = _align_quarterly_to_daily(inst_shares)
    return s.rolling(_TD_3Y, min_periods=1).apply(
        lambda x: len(x) - 1 - np.argmax(x[::-1]), raw=True
    )


def iex_ext_018_value_drawdown_duration_3y(inst_value: pd.Series) -> pd.Series:
    """Trading days since the 3-year rolling peak in aggregate value."""
    v = _align_quarterly_to_daily(inst_value)
    return v.rolling(_TD_3Y, min_periods=1).apply(
        lambda x: len(x) - 1 - np.argmax(x[::-1]), raw=True
    )


def iex_ext_019_inst_pct_drawdown_duration_3y(inst_pct: pd.Series) -> pd.Series:
    """Trading days since the 3-year rolling peak in ownership fraction."""
    p = _align_quarterly_to_daily(inst_pct)
    return p.rolling(_TD_3Y, min_periods=1).apply(
        lambda x: len(x) - 1 - np.argmax(x[::-1]), raw=True
    )


def iex_ext_020_holder_count_at_3y_low_flag(inst_holders: pd.Series) -> pd.Series:
    """Binary: 1 if holder count equals its 3-year rolling minimum."""
    h = _align_quarterly_to_daily(inst_holders)
    return (h <= _rolling_min(h, _TD_3Y) + _EPS).astype(float)


def iex_ext_021_inst_shares_at_3y_low_flag(inst_shares: pd.Series) -> pd.Series:
    """Binary: 1 if aggregate shares equal their 3-year rolling minimum."""
    s = _align_quarterly_to_daily(inst_shares)
    return (s <= _rolling_min(s, _TD_3Y) + _EPS).astype(float)


def iex_ext_022_inst_value_drawdown_depth_2y(inst_value: pd.Series) -> pd.Series:
    """Aggregate value drawdown depth from 2-year rolling max (negative = below)."""
    v = _align_quarterly_to_daily(inst_value)
    mx = _rolling_max(v, _TD_2Y)
    return _safe_div(v - mx, mx.abs())


def iex_ext_023_holder_count_recovery_gap_3y(inst_holders: pd.Series) -> pd.Series:
    """Holder count shortfall vs 3-year max as a positive depletion magnitude."""
    h = _align_quarterly_to_daily(inst_holders)
    mx = _rolling_max(h, _TD_3Y)
    return (mx - h).clip(lower=0)


def iex_ext_024_inst_pct_below_3y_mean_flag(inst_pct: pd.Series) -> pd.Series:
    """Binary: 1 if ownership fraction is below its 3-year rolling mean."""
    p = _align_quarterly_to_daily(inst_pct)
    return (p < _rolling_mean(p, _TD_3Y)).astype(float)


# --- Group C (025-036): Holder-bleed streaks and exit-persistence depth ---

def iex_ext_025_consec_yoy_holder_declines(inst_holders: pd.Series) -> pd.Series:
    """Count of consecutive YoY-declining observations in holder count."""
    return _consec_decline_streak(_align_quarterly_to_daily(inst_holders), _TD_YEAR)


def iex_ext_026_consec_qoq_shares_declines(inst_shares: pd.Series) -> pd.Series:
    """Count of consecutive QoQ-declining observations in aggregate shares."""
    return _consec_decline_streak(_align_quarterly_to_daily(inst_shares), _TD_QTR)


def iex_ext_027_consec_qoq_value_declines(inst_value: pd.Series) -> pd.Series:
    """Count of consecutive QoQ-declining observations in aggregate value."""
    return _consec_decline_streak(_align_quarterly_to_daily(inst_value), _TD_QTR)


def iex_ext_028_consec_qoq_inst_pct_declines(inst_pct: pd.Series) -> pd.Series:
    """Count of consecutive QoQ-declining observations in ownership fraction."""
    return _consec_decline_streak(_align_quarterly_to_daily(inst_pct), _TD_QTR)


def iex_ext_029_holder_decline_streak_max_2y(inst_holders: pd.Series) -> pd.Series:
    """Longest QoQ holder-decline streak observed in trailing 504 days."""
    streak = _consec_decline_streak(_align_quarterly_to_daily(inst_holders), _TD_QTR)
    return _rolling_max(streak, _TD_2Y)


def iex_ext_030_holder_below_4q_mean_frac_2y(inst_holders: pd.Series) -> pd.Series:
    """Fraction of last 504 days holder count was below its 4q rolling mean."""
    h = _align_quarterly_to_daily(inst_holders)
    below = (h < _rolling_mean(h, _TD_YEAR)).astype(float)
    return _rolling_mean(below, _TD_2Y)


def iex_ext_031_shares_below_4q_mean_streak(inst_shares: pd.Series) -> pd.Series:
    """Count of consecutive days aggregate shares are below their 4q rolling mean."""
    s = _align_quarterly_to_daily(inst_shares)
    below = (s < _rolling_mean(s, _TD_YEAR)).astype(int)
    result = below.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_ext_032_value_below_4q_mean_streak(inst_value: pd.Series) -> pd.Series:
    """Count of consecutive days aggregate value is below its 4q rolling mean."""
    v = _align_quarterly_to_daily(inst_value)
    below = (v < _rolling_mean(v, _TD_YEAR)).astype(int)
    result = below.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_ext_033_net_exit_positive_streak(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series) -> pd.Series:
    """Count of consecutive days net exits are positive (exits exceed entries)."""
    net = ((_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions))
           - (_align_quarterly_to_daily(new_positions) + _align_quarterly_to_daily(increased_positions)))
    pos = (net > 0).astype(int)
    result = pos.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if pos.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


def iex_ext_034_holder_decline_frac_2y(inst_holders: pd.Series) -> pd.Series:
    """Fraction of last 504 days with a negative QoQ holder-count change."""
    h = _align_quarterly_to_daily(inst_holders)
    declining = (h - h.shift(_TD_QTR) < 0).astype(float)
    return _rolling_mean(declining, _TD_2Y)


def iex_ext_035_shares_decline_frac_2y(inst_shares: pd.Series) -> pd.Series:
    """Fraction of last 504 days with a negative QoQ shares change."""
    s = _align_quarterly_to_daily(inst_shares)
    declining = (s - s.shift(_TD_QTR) < 0).astype(float)
    return _rolling_mean(declining, _TD_2Y)


def iex_ext_036_inst_pct_below_8q_mean_streak(inst_pct: pd.Series) -> pd.Series:
    """Count of consecutive days ownership fraction is below its 8q rolling mean."""
    p = _align_quarterly_to_daily(inst_pct)
    below = (p < _rolling_mean(p, _TD_2Y)).astype(int)
    result = below.astype(float).copy()
    count = 0.0
    for i in range(len(result)):
        if below.iloc[i] == 1:
            count += 1.0
        else:
            count = 0.0
        result.iloc[i] = count
    return result


# --- Group D (037-050): Exit-intensity ratios and position-flow variants ---

def iex_ext_037_closed_to_new_ratio(closed_positions: pd.Series,
                                    new_positions: pd.Series) -> pd.Series:
    """Closed positions divided by new positions (above 1 = net exit)."""
    return _safe_div(_align_quarterly_to_daily(closed_positions),
                     _align_quarterly_to_daily(new_positions))


def iex_ext_038_decreased_to_increased_ratio(decreased_positions: pd.Series,
                                             increased_positions: pd.Series) -> pd.Series:
    """Decreased positions divided by increased positions (above 1 = net trimming)."""
    return _safe_div(_align_quarterly_to_daily(decreased_positions),
                     _align_quarterly_to_daily(increased_positions))


def iex_ext_039_exit_count_share(closed_positions: pd.Series,
                                 decreased_positions: pd.Series,
                                 new_positions: pd.Series,
                                 increased_positions: pd.Series) -> pd.Series:
    """Exiting positions as a fraction of all position-change events."""
    exit_c = _align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions)
    total = exit_c + _align_quarterly_to_daily(new_positions) + _align_quarterly_to_daily(increased_positions)
    return _safe_div(exit_c, total)


def iex_ext_040_closed_share_of_holders_1y_mean(closed_positions: pd.Series,
                                                inst_holders: pd.Series) -> pd.Series:
    """1-year rolling mean of (closed positions / total holders)."""
    ratio = _safe_div(_align_quarterly_to_daily(closed_positions),
                      _align_quarterly_to_daily(inst_holders))
    return _rolling_mean(ratio, _TD_YEAR)


def iex_ext_041_net_exit_share_of_holders(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          inst_holders: pd.Series) -> pd.Series:
    """Net exits as a fraction of total institutional holders."""
    net = ((_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions))
           - (_align_quarterly_to_daily(new_positions) + _align_quarterly_to_daily(increased_positions)))
    return _safe_div(net, _align_quarterly_to_daily(inst_holders))


def iex_ext_042_exit_breadth_8q_zscore(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Z-score of exit breadth over an 8-quarter rolling window."""
    breadth = _safe_div(_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions),
                        _align_quarterly_to_daily(inst_holders))
    return _zscore_rolling(breadth, _TD_2Y)


def iex_ext_043_net_exits_qoq_pct(closed_positions: pd.Series,
                                  decreased_positions: pd.Series,
                                  new_positions: pd.Series,
                                  increased_positions: pd.Series) -> pd.Series:
    """QoQ % change in the net-exit series."""
    net = ((_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions))
           - (_align_quarterly_to_daily(new_positions) + _align_quarterly_to_daily(increased_positions)))
    return _safe_div_abs(net - net.shift(_TD_QTR), net.shift(_TD_QTR))


def iex_ext_044_closed_positions_2y_sum(closed_positions: pd.Series) -> pd.Series:
    """Rolling 8-quarter cumulative sum of fully-closed positions."""
    return _rolling_sum(_align_quarterly_to_daily(closed_positions), _TD_2Y)


def iex_ext_045_decreased_positions_2y_sum(decreased_positions: pd.Series) -> pd.Series:
    """Rolling 8-quarter cumulative sum of decreased positions."""
    return _rolling_sum(_align_quarterly_to_daily(decreased_positions), _TD_2Y)


def iex_ext_046_net_exits_3q_diff(closed_positions: pd.Series,
                                  decreased_positions: pd.Series,
                                  new_positions: pd.Series,
                                  increased_positions: pd.Series) -> pd.Series:
    """3-quarter change in the net-exit series."""
    net = ((_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions))
           - (_align_quarterly_to_daily(new_positions) + _align_quarterly_to_daily(increased_positions)))
    return net - net.shift(_TD_3Q)


def iex_ext_047_closed_positions_zscore_8q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed-position count over an 8-quarter rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(closed_positions), _TD_2Y)


def iex_ext_048_exit_breadth_rank_8q(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    """Rolling 8-quarter percentile rank of exit breadth."""
    breadth = _safe_div(_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions),
                        _align_quarterly_to_daily(inst_holders))
    return _rolling_rank_pct(breadth, _TD_2Y)


def iex_ext_049_new_vs_closed_ratio_yoy_chg(new_positions: pd.Series,
                                            closed_positions: pd.Series) -> pd.Series:
    """YoY change in the (new / closed) position ratio."""
    ratio = _safe_div(_align_quarterly_to_daily(new_positions),
                      _align_quarterly_to_daily(closed_positions))
    return ratio - ratio.shift(_TD_YEAR)


def iex_ext_050_avg_shares_per_holder_qoq_pct(inst_shares: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """QoQ % change in average shares held per institutional holder."""
    avg = _safe_div(_align_quarterly_to_daily(inst_shares),
                    _align_quarterly_to_daily(inst_holders))
    return _safe_div_abs(avg - avg.shift(_TD_QTR), avg.shift(_TD_QTR))


# --- Group E (051-062): Decay-weighted and dispersion exit metrics ---

def iex_ext_051_holder_count_ewm_dev_8q(inst_holders: pd.Series) -> pd.Series:
    """Deviation of holder count from its EWM (span=8 quarters)."""
    h = _align_quarterly_to_daily(inst_holders)
    return h - _ewm_mean(h, _TD_2Y)


def iex_ext_052_inst_shares_ewm_ratio_8q(inst_shares: pd.Series) -> pd.Series:
    """Ratio of aggregate shares to its EWM (span=8 quarters)."""
    s = _align_quarterly_to_daily(inst_shares)
    return _safe_div(s, _ewm_mean(s, _TD_2Y))


def iex_ext_053_inst_value_ewm_ratio_8q(inst_value: pd.Series) -> pd.Series:
    """Ratio of aggregate value to its EWM (span=8 quarters)."""
    v = _align_quarterly_to_daily(inst_value)
    return _safe_div(v, _ewm_mean(v, _TD_2Y))


def iex_ext_054_inst_pct_ewm_dev_8q(inst_pct: pd.Series) -> pd.Series:
    """Deviation of ownership fraction from its EWM (span=8 quarters)."""
    p = _align_quarterly_to_daily(inst_pct)
    return p - _ewm_mean(p, _TD_2Y)


def iex_ext_055_net_exit_ewm_ratio_8q(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """Ratio of net exits to its EWM (span=8 quarters)."""
    net = ((_align_quarterly_to_daily(closed_positions) + _align_quarterly_to_daily(decreased_positions))
           - (_align_quarterly_to_daily(new_positions) + _align_quarterly_to_daily(increased_positions)))
    return _safe_div(net, _ewm_mean(net, _TD_2Y))


def iex_ext_056_holder_count_8q_cv(inst_holders: pd.Series) -> pd.Series:
    """Coefficient of variation of holder count over an 8-quarter window."""
    h = _align_quarterly_to_daily(inst_holders)
    return _safe_div(_rolling_std(h, _TD_2Y), _rolling_mean(h, _TD_2Y).abs())


def iex_ext_057_holder_count_qoq_diff_std_8q(inst_holders: pd.Series) -> pd.Series:
    """Rolling 8-quarter standard deviation of the QoQ holder-count change."""
    h = _align_quarterly_to_daily(inst_holders)
    return _rolling_std(h - h.shift(_TD_QTR), _TD_2Y)


def iex_ext_058_inst_shares_qoq_diff_std_8q(inst_shares: pd.Series) -> pd.Series:
    """Rolling 8-quarter standard deviation of the QoQ shares change."""
    s = _align_quarterly_to_daily(inst_shares)
    return _rolling_std(s - s.shift(_TD_QTR), _TD_2Y)


def iex_ext_059_holder_count_3y_cv(inst_holders: pd.Series) -> pd.Series:
    """Coefficient of variation of holder count over a 3-year window."""
    h = _align_quarterly_to_daily(inst_holders)
    return _safe_div(_rolling_std(h, _TD_3Y), _rolling_mean(h, _TD_3Y).abs())


def iex_ext_060_inst_pct_8q_cv(inst_pct: pd.Series) -> pd.Series:
    """Coefficient of variation of ownership fraction over an 8-quarter window."""
    p = _align_quarterly_to_daily(inst_pct)
    return _safe_div(_rolling_std(p, _TD_2Y), _rolling_mean(p, _TD_2Y).abs())


def iex_ext_061_holder_count_downside_dev_8q(inst_holders: pd.Series) -> pd.Series:
    """Rolling 8-quarter downside deviation of QoQ holder-count changes."""
    h = _align_quarterly_to_daily(inst_holders)
    diff = h - h.shift(_TD_QTR)
    downside = diff.clip(upper=0.0)
    return (downside ** 2).rolling(_TD_2Y, min_periods=2).mean() ** 0.5


def iex_ext_062_inst_value_downside_dev_8q(inst_value: pd.Series) -> pd.Series:
    """Rolling 8-quarter downside deviation of QoQ value % changes."""
    v = _align_quarterly_to_daily(inst_value)
    pct = _safe_div_abs(v - v.shift(_TD_QTR), v.shift(_TD_QTR))
    downside = pct.clip(upper=0.0)
    return (downside ** 2).rolling(_TD_2Y, min_periods=2).mean() ** 0.5


# --- Group F (063-075): Ranks, percentiles and composite departure signals ---

def iex_ext_063_holder_count_3y_rolling_rank(inst_holders: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of holder count."""
    return _rolling_rank_pct(_align_quarterly_to_daily(inst_holders), _TD_3Y)


def iex_ext_064_inst_shares_3y_rolling_rank(inst_shares: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of aggregate shares."""
    return _rolling_rank_pct(_align_quarterly_to_daily(inst_shares), _TD_3Y)


def iex_ext_065_inst_value_3y_rolling_rank(inst_value: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of aggregate value."""
    return _rolling_rank_pct(_align_quarterly_to_daily(inst_value), _TD_3Y)


def iex_ext_066_inst_pct_3y_rolling_rank(inst_pct: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of ownership fraction."""
    return _rolling_rank_pct(_align_quarterly_to_daily(inst_pct), _TD_3Y)


def iex_ext_067_holder_count_8q_zscore_abs(inst_holders: pd.Series) -> pd.Series:
    """Absolute z-score of holder count over an 8-quarter window."""
    return _zscore_rolling(_align_quarterly_to_daily(inst_holders), _TD_2Y).abs()


def iex_ext_068_inst_shares_8q_zscore(inst_shares: pd.Series) -> pd.Series:
    """Z-score of aggregate shares over an 8-quarter rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(inst_shares), _TD_2Y)


def iex_ext_069_inst_pct_3y_zscore(inst_pct: pd.Series) -> pd.Series:
    """Z-score of ownership fraction over a 3-year rolling window."""
    return _zscore_rolling(_align_quarterly_to_daily(inst_pct), _TD_3Y)


def iex_ext_070_holder_count_value_3q_composite(inst_holders: pd.Series,
                                                inst_value: pd.Series) -> pd.Series:
    """Average of 3-quarter % declines in holder count and aggregate value."""
    h = _align_quarterly_to_daily(inst_holders)
    v = _align_quarterly_to_daily(inst_value)
    h_pct = _safe_div_abs(h - h.shift(_TD_3Q), h.shift(_TD_3Q))
    v_pct = _safe_div_abs(v - v.shift(_TD_3Q), v.shift(_TD_3Q))
    return (h_pct + v_pct) / 2.0


def iex_ext_071_triple_drawdown_composite(inst_holders: pd.Series,
                                          inst_shares: pd.Series,
                                          inst_value: pd.Series) -> pd.Series:
    """Average drawdown-from-3y-max across holders, shares and value."""
    h = _align_quarterly_to_daily(inst_holders)
    s = _align_quarterly_to_daily(inst_shares)
    v = _align_quarterly_to_daily(inst_value)
    dd_h = _safe_div(h - _rolling_max(h, _TD_3Y), _rolling_max(h, _TD_3Y).abs())
    dd_s = _safe_div(s - _rolling_max(s, _TD_3Y), _rolling_max(s, _TD_3Y).abs())
    dd_v = _safe_div(v - _rolling_max(v, _TD_3Y), _rolling_max(v, _TD_3Y).abs())
    return (dd_h + dd_s + dd_v) / 3.0


def iex_ext_072_exit_intensity_composite(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """
    Exit-intensity composite: average of net-exit share of holders and the
    exit-count share of all position-change events. Higher = stronger exodus.
    """
    closed = _align_quarterly_to_daily(closed_positions)
    decr = _align_quarterly_to_daily(decreased_positions)
    new = _align_quarterly_to_daily(new_positions)
    incr = _align_quarterly_to_daily(increased_positions)
    holders = _align_quarterly_to_daily(inst_holders)
    net_share = _safe_div((closed + decr) - (new + incr), holders)
    exit_share = _safe_div(closed + decr, closed + decr + new + incr)
    return (net_share + exit_share) / 2.0


def iex_ext_073_quad_decline_count(inst_holders: pd.Series,
                                   inst_shares: pd.Series,
                                   inst_value: pd.Series,
                                   inst_pct: pd.Series) -> pd.Series:
    """Count of the four ownership metrics with a negative QoQ change (0-4)."""
    flags = []
    for raw in (inst_holders, inst_shares, inst_value, inst_pct):
        x = _align_quarterly_to_daily(raw)
        flags.append((x - x.shift(_TD_QTR) < 0).astype(float))
    result = flags[0]
    for f in flags[1:]:
        result = result + f
    return result


def iex_ext_074_all_metrics_declining_flag(inst_holders: pd.Series,
                                           inst_shares: pd.Series,
                                           inst_value: pd.Series,
                                           inst_pct: pd.Series) -> pd.Series:
    """Binary: 1 if holders, shares, value AND ownership % all declined QoQ."""
    conds = []
    for raw in (inst_holders, inst_shares, inst_value, inst_pct):
        x = _align_quarterly_to_daily(raw)
        conds.append(x - x.shift(_TD_QTR) < 0)
    combined = conds[0]
    for c in conds[1:]:
        combined = combined & c
    return combined.astype(float)


def iex_ext_075_institutional_departure_score(inst_holders: pd.Series,
                                              inst_shares: pd.Series,
                                              inst_pct: pd.Series,
                                              closed_positions: pd.Series,
                                              inst_value: pd.Series) -> pd.Series:
    """
    Departure score combining four normalized signals (each ~0-1, higher = worse):
      - magnitude of negative YoY holder-count % change (clipped 0-1)
      - magnitude of negative YoY shares % change (clipped 0-1)
      - shortfall of ownership % vs its 2-year max (clipped 0-1)
      - 1-year mean of closed-positions share of holders (clipped 0-1)
    Average of the four.
    """
    h = _align_quarterly_to_daily(inst_holders)
    s = _align_quarterly_to_daily(inst_shares)
    p = _align_quarterly_to_daily(inst_pct)
    v = _align_quarterly_to_daily(inst_value)  # accepted for signature completeness
    closed = _align_quarterly_to_daily(closed_positions)
    h_drop = (-_safe_div_abs(h - h.shift(_TD_YEAR), h.shift(_TD_YEAR))).clip(lower=0.0, upper=1.0)
    s_drop = (-_safe_div_abs(s - s.shift(_TD_YEAR), s.shift(_TD_YEAR))).clip(lower=0.0, upper=1.0)
    mx = _rolling_max(p, _TD_2Y)
    p_short = (-_safe_div(p - mx, mx.abs())).clip(lower=0.0, upper=1.0)
    closed_share = _rolling_mean(_safe_div(closed, h), _TD_YEAR).clip(lower=0.0, upper=1.0)
    base = (h_drop + s_drop + p_short + closed_share) / 4.0
    return base + 0.0 * v


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
INSTITUTIONAL_EXIT_EXTENDED_REGISTRY_001_075 = {
    "iex_ext_001_holder_count_3q_diff": {"inputs": ["inst_holders"], "func": iex_ext_001_holder_count_3q_diff},
    "iex_ext_002_holder_count_3q_pct": {"inputs": ["inst_holders"], "func": iex_ext_002_holder_count_3q_pct},
    "iex_ext_003_inst_shares_3q_pct": {"inputs": ["inst_shares"], "func": iex_ext_003_inst_shares_3q_pct},
    "iex_ext_004_inst_value_3q_pct": {"inputs": ["inst_value"], "func": iex_ext_004_inst_value_3q_pct},
    "iex_ext_005_holder_count_3y_diff": {"inputs": ["inst_holders"], "func": iex_ext_005_holder_count_3y_diff},
    "iex_ext_006_inst_shares_3y_pct": {"inputs": ["inst_shares"], "func": iex_ext_006_inst_shares_3y_pct},
    "iex_ext_007_inst_pct_3q_diff": {"inputs": ["inst_pct"], "func": iex_ext_007_inst_pct_3q_diff},
    "iex_ext_008_holder_count_qoq_pct_abs": {"inputs": ["inst_holders"], "func": iex_ext_008_holder_count_qoq_pct_abs},
    "iex_ext_009_inst_value_2q_pct": {"inputs": ["inst_value"], "func": iex_ext_009_inst_value_2q_pct},
    "iex_ext_010_holder_count_2q_pct": {"inputs": ["inst_holders"], "func": iex_ext_010_holder_count_2q_pct},
    "iex_ext_011_inst_pct_3y_diff": {"inputs": ["inst_pct"], "func": iex_ext_011_inst_pct_3y_diff},
    "iex_ext_012_inst_shares_2q_pct": {"inputs": ["inst_shares"], "func": iex_ext_012_inst_shares_2q_pct},
    "iex_ext_013_holder_count_pct_from_3y_max": {"inputs": ["inst_holders"], "func": iex_ext_013_holder_count_pct_from_3y_max},
    "iex_ext_014_inst_shares_pct_from_3y_max": {"inputs": ["inst_shares"], "func": iex_ext_014_inst_shares_pct_from_3y_max},
    "iex_ext_015_inst_pct_pct_from_3y_max": {"inputs": ["inst_pct"], "func": iex_ext_015_inst_pct_pct_from_3y_max},
    "iex_ext_016_inst_pct_pct_from_8q_max": {"inputs": ["inst_pct"], "func": iex_ext_016_inst_pct_pct_from_8q_max},
    "iex_ext_017_shares_drawdown_duration_3y": {"inputs": ["inst_shares"], "func": iex_ext_017_shares_drawdown_duration_3y},
    "iex_ext_018_value_drawdown_duration_3y": {"inputs": ["inst_value"], "func": iex_ext_018_value_drawdown_duration_3y},
    "iex_ext_019_inst_pct_drawdown_duration_3y": {"inputs": ["inst_pct"], "func": iex_ext_019_inst_pct_drawdown_duration_3y},
    "iex_ext_020_holder_count_at_3y_low_flag": {"inputs": ["inst_holders"], "func": iex_ext_020_holder_count_at_3y_low_flag},
    "iex_ext_021_inst_shares_at_3y_low_flag": {"inputs": ["inst_shares"], "func": iex_ext_021_inst_shares_at_3y_low_flag},
    "iex_ext_022_inst_value_drawdown_depth_2y": {"inputs": ["inst_value"], "func": iex_ext_022_inst_value_drawdown_depth_2y},
    "iex_ext_023_holder_count_recovery_gap_3y": {"inputs": ["inst_holders"], "func": iex_ext_023_holder_count_recovery_gap_3y},
    "iex_ext_024_inst_pct_below_3y_mean_flag": {"inputs": ["inst_pct"], "func": iex_ext_024_inst_pct_below_3y_mean_flag},
    "iex_ext_025_consec_yoy_holder_declines": {"inputs": ["inst_holders"], "func": iex_ext_025_consec_yoy_holder_declines},
    "iex_ext_026_consec_qoq_shares_declines": {"inputs": ["inst_shares"], "func": iex_ext_026_consec_qoq_shares_declines},
    "iex_ext_027_consec_qoq_value_declines": {"inputs": ["inst_value"], "func": iex_ext_027_consec_qoq_value_declines},
    "iex_ext_028_consec_qoq_inst_pct_declines": {"inputs": ["inst_pct"], "func": iex_ext_028_consec_qoq_inst_pct_declines},
    "iex_ext_029_holder_decline_streak_max_2y": {"inputs": ["inst_holders"], "func": iex_ext_029_holder_decline_streak_max_2y},
    "iex_ext_030_holder_below_4q_mean_frac_2y": {"inputs": ["inst_holders"], "func": iex_ext_030_holder_below_4q_mean_frac_2y},
    "iex_ext_031_shares_below_4q_mean_streak": {"inputs": ["inst_shares"], "func": iex_ext_031_shares_below_4q_mean_streak},
    "iex_ext_032_value_below_4q_mean_streak": {"inputs": ["inst_value"], "func": iex_ext_032_value_below_4q_mean_streak},
    "iex_ext_033_net_exit_positive_streak": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_ext_033_net_exit_positive_streak},
    "iex_ext_034_holder_decline_frac_2y": {"inputs": ["inst_holders"], "func": iex_ext_034_holder_decline_frac_2y},
    "iex_ext_035_shares_decline_frac_2y": {"inputs": ["inst_shares"], "func": iex_ext_035_shares_decline_frac_2y},
    "iex_ext_036_inst_pct_below_8q_mean_streak": {"inputs": ["inst_pct"], "func": iex_ext_036_inst_pct_below_8q_mean_streak},
    "iex_ext_037_closed_to_new_ratio": {"inputs": ["closed_positions", "new_positions"], "func": iex_ext_037_closed_to_new_ratio},
    "iex_ext_038_decreased_to_increased_ratio": {"inputs": ["decreased_positions", "increased_positions"], "func": iex_ext_038_decreased_to_increased_ratio},
    "iex_ext_039_exit_count_share": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_ext_039_exit_count_share},
    "iex_ext_040_closed_share_of_holders_1y_mean": {"inputs": ["closed_positions", "inst_holders"], "func": iex_ext_040_closed_share_of_holders_1y_mean},
    "iex_ext_041_net_exit_share_of_holders": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"], "func": iex_ext_041_net_exit_share_of_holders},
    "iex_ext_042_exit_breadth_8q_zscore": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_ext_042_exit_breadth_8q_zscore},
    "iex_ext_043_net_exits_qoq_pct": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_ext_043_net_exits_qoq_pct},
    "iex_ext_044_closed_positions_2y_sum": {"inputs": ["closed_positions"], "func": iex_ext_044_closed_positions_2y_sum},
    "iex_ext_045_decreased_positions_2y_sum": {"inputs": ["decreased_positions"], "func": iex_ext_045_decreased_positions_2y_sum},
    "iex_ext_046_net_exits_3q_diff": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_ext_046_net_exits_3q_diff},
    "iex_ext_047_closed_positions_zscore_8q": {"inputs": ["closed_positions"], "func": iex_ext_047_closed_positions_zscore_8q},
    "iex_ext_048_exit_breadth_rank_8q": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": iex_ext_048_exit_breadth_rank_8q},
    "iex_ext_049_new_vs_closed_ratio_yoy_chg": {"inputs": ["new_positions", "closed_positions"], "func": iex_ext_049_new_vs_closed_ratio_yoy_chg},
    "iex_ext_050_avg_shares_per_holder_qoq_pct": {"inputs": ["inst_shares", "inst_holders"], "func": iex_ext_050_avg_shares_per_holder_qoq_pct},
    "iex_ext_051_holder_count_ewm_dev_8q": {"inputs": ["inst_holders"], "func": iex_ext_051_holder_count_ewm_dev_8q},
    "iex_ext_052_inst_shares_ewm_ratio_8q": {"inputs": ["inst_shares"], "func": iex_ext_052_inst_shares_ewm_ratio_8q},
    "iex_ext_053_inst_value_ewm_ratio_8q": {"inputs": ["inst_value"], "func": iex_ext_053_inst_value_ewm_ratio_8q},
    "iex_ext_054_inst_pct_ewm_dev_8q": {"inputs": ["inst_pct"], "func": iex_ext_054_inst_pct_ewm_dev_8q},
    "iex_ext_055_net_exit_ewm_ratio_8q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": iex_ext_055_net_exit_ewm_ratio_8q},
    "iex_ext_056_holder_count_8q_cv": {"inputs": ["inst_holders"], "func": iex_ext_056_holder_count_8q_cv},
    "iex_ext_057_holder_count_qoq_diff_std_8q": {"inputs": ["inst_holders"], "func": iex_ext_057_holder_count_qoq_diff_std_8q},
    "iex_ext_058_inst_shares_qoq_diff_std_8q": {"inputs": ["inst_shares"], "func": iex_ext_058_inst_shares_qoq_diff_std_8q},
    "iex_ext_059_holder_count_3y_cv": {"inputs": ["inst_holders"], "func": iex_ext_059_holder_count_3y_cv},
    "iex_ext_060_inst_pct_8q_cv": {"inputs": ["inst_pct"], "func": iex_ext_060_inst_pct_8q_cv},
    "iex_ext_061_holder_count_downside_dev_8q": {"inputs": ["inst_holders"], "func": iex_ext_061_holder_count_downside_dev_8q},
    "iex_ext_062_inst_value_downside_dev_8q": {"inputs": ["inst_value"], "func": iex_ext_062_inst_value_downside_dev_8q},
    "iex_ext_063_holder_count_3y_rolling_rank": {"inputs": ["inst_holders"], "func": iex_ext_063_holder_count_3y_rolling_rank},
    "iex_ext_064_inst_shares_3y_rolling_rank": {"inputs": ["inst_shares"], "func": iex_ext_064_inst_shares_3y_rolling_rank},
    "iex_ext_065_inst_value_3y_rolling_rank": {"inputs": ["inst_value"], "func": iex_ext_065_inst_value_3y_rolling_rank},
    "iex_ext_066_inst_pct_3y_rolling_rank": {"inputs": ["inst_pct"], "func": iex_ext_066_inst_pct_3y_rolling_rank},
    "iex_ext_067_holder_count_8q_zscore_abs": {"inputs": ["inst_holders"], "func": iex_ext_067_holder_count_8q_zscore_abs},
    "iex_ext_068_inst_shares_8q_zscore": {"inputs": ["inst_shares"], "func": iex_ext_068_inst_shares_8q_zscore},
    "iex_ext_069_inst_pct_3y_zscore": {"inputs": ["inst_pct"], "func": iex_ext_069_inst_pct_3y_zscore},
    "iex_ext_070_holder_count_value_3q_composite": {"inputs": ["inst_holders", "inst_value"], "func": iex_ext_070_holder_count_value_3q_composite},
    "iex_ext_071_triple_drawdown_composite": {"inputs": ["inst_holders", "inst_shares", "inst_value"], "func": iex_ext_071_triple_drawdown_composite},
    "iex_ext_072_exit_intensity_composite": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"], "func": iex_ext_072_exit_intensity_composite},
    "iex_ext_073_quad_decline_count": {"inputs": ["inst_holders", "inst_shares", "inst_value", "inst_pct"], "func": iex_ext_073_quad_decline_count},
    "iex_ext_074_all_metrics_declining_flag": {"inputs": ["inst_holders", "inst_shares", "inst_value", "inst_pct"], "func": iex_ext_074_all_metrics_declining_flag},
    "iex_ext_075_institutional_departure_score": {"inputs": ["inst_holders", "inst_shares", "inst_pct", "closed_positions", "inst_value"], "func": iex_ext_075_institutional_departure_score},
}
