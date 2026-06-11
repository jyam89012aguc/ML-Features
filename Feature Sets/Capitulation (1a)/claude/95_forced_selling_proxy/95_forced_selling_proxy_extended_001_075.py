"""
95_forced_selling_proxy — Extended Features 001-075
====================================================
Domain: Signatures of FORCED / DISTRESSED LIQUIDATION by institutions — the
        target is ABRUPTNESS + BREADTH + SYNCHRONICITY (a fire sale), not a slow
        gradual decline. Additional variants: new lookback windows, fresh
        thresholds, percentile ranks, exit streaks, EWM crossovers, cliff-drop
        depths and composite fire-sale distress scores.
Asset class: US equities | Sharadar SF3 13F institutional ownership (quarterly,
        forward-filled to a daily index).
All features are backward-looking only; no forward information.

These extended features do NOT duplicate base_001_075, base_076_150,
2nd_derivatives or 3rd_derivatives — they explore different windows, thresholds,
smoothing and composite angles within the same forced-liquidation domain.

QUARTERLY -> DAILY ALIGNMENT CONTRACT
-------------------------------------
All input Series are daily-indexed pandas Series forward-filled from quarterly
Sharadar SF3 / 13F snapshots (~63 trading days per print). Derived Series are
therefore stepwise / sparse on a daily index — expected and correct.
`_align_quarterly_to_daily` documents the contract; alignment is upstream.

Available input fields (all daily Series, forward-filled from quarterly data):
  closed_positions, decreased_positions, new_positions, increased_positions,
  inst_holders, inst_shares, inst_value, avg_position, inst_pct.

Cadence constants (trading days):
  1 quarter = 63 td   1 year = 252 td   2 years = 504 td   3 years = 756 td
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

def _align_quarterly_to_daily(s: pd.Series) -> pd.Series:
    """Return s unchanged — caller is responsible for forward-filling from quarterly."""
    return s


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / (den.replace(0, np.nan) + _EPS)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).apply(
        lambda x: pd.Series(x).rank(pct=True).iloc[-1], raw=False
    )


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    mu = _rolling_mean(s, w)
    sigma = _rolling_std(s, w)
    return (s - mu) / (sigma + _EPS)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, adjust=False).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    grp = (~cond).cumsum()
    return c.groupby(grp).cumsum().astype(float)


def _combined_selling(closed_positions: pd.Series, decreased_positions: pd.Series) -> pd.Series:
    return closed_positions.fillna(0) + decreased_positions.fillna(0)


# ===========================================================================
# Extended Features 001 - 075
# ===========================================================================

# --- Group A (001-010): Exit-spike detectors, new lookback windows ---

def fsp_ext_001_closed_vs_3q_mean_ratio(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing 3-quarter mean — spike vs 3Q norm."""
    return _safe_div(closed_positions, _rolling_mean(closed_positions, _TD_3Q))


def fsp_ext_002_closed_vs_8q_mean_ratio(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing 8-quarter mean — spike vs 2-year norm."""
    return _safe_div(closed_positions, _rolling_mean(closed_positions, _TD_2Y))


def fsp_ext_003_closed_vs_12q_mean_ratio(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing 12-quarter mean — spike vs 3-year norm."""
    return _safe_div(closed_positions, _rolling_mean(closed_positions, _TD_3Y))


def fsp_ext_004_combined_selling_vs_3q_mean(closed_positions: pd.Series,
                                             decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing 3Q mean — combined selling spike."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _safe_div(s, _rolling_mean(s, _TD_3Q))


def fsp_ext_005_combined_selling_vs_12q_mean(closed_positions: pd.Series,
                                              decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing 12Q mean — combined selling vs 3-year norm."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _safe_div(s, _rolling_mean(s, _TD_3Y))


def fsp_ext_006_decreased_vs_4q_mean_ratio(decreased_positions: pd.Series) -> pd.Series:
    """Decreased positions / trailing 4Q mean — trim spike detector."""
    return _safe_div(decreased_positions, _rolling_mean(decreased_positions, _TD_YEAR))


def fsp_ext_007_decreased_vs_4q_max_ratio(decreased_positions: pd.Series) -> pd.Series:
    """Decreased positions / trailing 4Q max — trim level vs recent peak."""
    return _safe_div(decreased_positions, _rolling_max(decreased_positions, _TD_YEAR))


def fsp_ext_008_closed_vs_12q_max_ratio(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing 12Q max — spike vs 3-year peak."""
    return _safe_div(closed_positions, _rolling_max(closed_positions, _TD_3Y))


def fsp_ext_009_combined_selling_vs_12q_max(closed_positions: pd.Series,
                                             decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing 12Q max — combined selling vs 3-year peak."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _safe_div(s, _rolling_max(s, _TD_3Y))


def fsp_ext_010_combined_selling_vs_3q_max(closed_positions: pd.Series,
                                            decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing 3Q max — combined selling spike vs 3Q peak."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _safe_div(s, _rolling_max(s, _TD_3Q))


# --- Group B (011-020): Z-score variants, mixed windows ---

def fsp_ext_011_closed_pos_zscore_3q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over trailing 3-quarter window."""
    return _zscore_rolling(closed_positions, _TD_3Q)


def fsp_ext_012_closed_pos_zscore_12q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over trailing 12-quarter (3-year) window."""
    return _zscore_rolling(closed_positions, _TD_3Y)


def fsp_ext_013_decreased_pos_zscore_4q(decreased_positions: pd.Series) -> pd.Series:
    """Z-score of decreased positions over trailing 4-quarter window."""
    return _zscore_rolling(decreased_positions, _TD_YEAR)


def fsp_ext_014_decreased_pos_zscore_8q(decreased_positions: pd.Series) -> pd.Series:
    """Z-score of decreased positions over trailing 8-quarter window."""
    return _zscore_rolling(decreased_positions, _TD_2Y)


def fsp_ext_015_combined_selling_zscore_3q(closed_positions: pd.Series,
                                            decreased_positions: pd.Series) -> pd.Series:
    """Z-score of (closed+decreased) over trailing 3-quarter window."""
    return _zscore_rolling(_combined_selling(closed_positions, decreased_positions), _TD_3Q)


def fsp_ext_016_combined_selling_zscore_12q(closed_positions: pd.Series,
                                             decreased_positions: pd.Series) -> pd.Series:
    """Z-score of (closed+decreased) over trailing 12-quarter window."""
    return _zscore_rolling(_combined_selling(closed_positions, decreased_positions), _TD_3Y)


def fsp_ext_017_inst_shares_zscore_12q(inst_shares: pd.Series) -> pd.Series:
    """Z-score of inst_shares over trailing 12-quarter (3-year) window."""
    return _zscore_rolling(inst_shares, _TD_3Y)


def fsp_ext_018_inst_value_zscore_12q(inst_value: pd.Series) -> pd.Series:
    """Z-score of inst_value over trailing 12-quarter (3-year) window."""
    return _zscore_rolling(inst_value, _TD_3Y)


def fsp_ext_019_avg_position_zscore_12q(avg_position: pd.Series) -> pd.Series:
    """Z-score of avg_position over trailing 12-quarter (3-year) window."""
    return _zscore_rolling(avg_position, _TD_3Y)


def fsp_ext_020_holders_zscore_8q(inst_holders: pd.Series) -> pd.Series:
    """Z-score of holder count over trailing 8-quarter (2-year) window."""
    return _zscore_rolling(inst_holders, _TD_2Y)


# --- Group C (021-030): Percentile-rank exodus / spike detectors ---

def fsp_ext_021_closed_pos_rank_8q(closed_positions: pd.Series) -> pd.Series:
    """Percentile rank of closed positions within trailing 8-quarter window."""
    return _rolling_rank_pct(closed_positions, _TD_2Y)


def fsp_ext_022_closed_pos_rank_12q(closed_positions: pd.Series) -> pd.Series:
    """Percentile rank of closed positions within trailing 12-quarter window."""
    return _rolling_rank_pct(closed_positions, _TD_3Y)


def fsp_ext_023_combined_selling_rank_8q(closed_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """Percentile rank of (closed+decreased) within trailing 8Q window."""
    return _rolling_rank_pct(_combined_selling(closed_positions, decreased_positions), _TD_2Y)


def fsp_ext_024_decreased_pos_rank_4q(decreased_positions: pd.Series) -> pd.Series:
    """Percentile rank of decreased positions within trailing 4Q window."""
    return _rolling_rank_pct(decreased_positions, _TD_YEAR)


def fsp_ext_025_holders_rank_8q(inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of holder count within trailing 8Q window (low = exodus)."""
    return _rolling_rank_pct(inst_holders, _TD_2Y)


def fsp_ext_026_avg_position_rank_8q(avg_position: pd.Series) -> pd.Series:
    """Percentile rank of avg_position within trailing 8Q window (low = collapse)."""
    return _rolling_rank_pct(avg_position, _TD_2Y)


def fsp_ext_027_inst_shares_rank_8q(inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of inst_shares within trailing 8Q window (low = exodus)."""
    return _rolling_rank_pct(inst_shares, _TD_2Y)


def fsp_ext_028_inst_pct_rank_8q(inst_pct: pd.Series) -> pd.Series:
    """Percentile rank of inst_pct within trailing 8Q window (low = ownership loss)."""
    return _rolling_rank_pct(inst_pct, _TD_2Y)


def fsp_ext_029_selling_breadth_rank_4q(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of (closed+decreased)/inst_holders breadth within 4Q window."""
    ratio = _safe_div(_combined_selling(closed_positions, decreased_positions), inst_holders)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def fsp_ext_030_closed_pos_expanding_rank(closed_positions: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of closed positions (1 = worst ever)."""
    def _r(x):
        if len(x) < 2:
            return np.nan
        return (x[:-1] < x[-1]).sum() / (len(x) - 1)
    return closed_positions.expanding(min_periods=2).apply(_r, raw=True)


# --- Group D (031-042): Cliff-drop depth on new windows ---

def fsp_ext_031_inst_shares_cliff_drop_4q(inst_shares: pd.Series) -> pd.Series:
    """Inst shares now vs trailing-4Q max — fractional cliff-drop over a year."""
    mx = _rolling_max(inst_shares, _TD_YEAR)
    return _safe_div(inst_shares - mx, mx)


def fsp_ext_032_inst_shares_cliff_drop_8q(inst_shares: pd.Series) -> pd.Series:
    """Inst shares now vs trailing-8Q max — fractional cliff-drop over 2 years."""
    mx = _rolling_max(inst_shares, _TD_2Y)
    return _safe_div(inst_shares - mx, mx)


def fsp_ext_033_inst_value_cliff_drop_4q(inst_value: pd.Series) -> pd.Series:
    """Inst value now vs trailing-4Q max — fractional cliff-drop over a year."""
    mx = _rolling_max(inst_value, _TD_YEAR)
    return _safe_div(inst_value - mx, mx)


def fsp_ext_034_inst_value_cliff_drop_8q(inst_value: pd.Series) -> pd.Series:
    """Inst value now vs trailing-8Q max — fractional cliff-drop over 2 years."""
    mx = _rolling_max(inst_value, _TD_2Y)
    return _safe_div(inst_value - mx, mx)


def fsp_ext_035_avg_position_cliff_drop_4q(avg_position: pd.Series) -> pd.Series:
    """Avg position now vs trailing-4Q max — fractional collapse over a year."""
    mx = _rolling_max(avg_position, _TD_YEAR)
    return _safe_div(avg_position - mx, mx)


def fsp_ext_036_avg_position_cliff_drop_8q(avg_position: pd.Series) -> pd.Series:
    """Avg position now vs trailing-8Q max — fractional collapse over 2 years."""
    mx = _rolling_max(avg_position, _TD_2Y)
    return _safe_div(avg_position - mx, mx)


def fsp_ext_037_holders_cliff_drop_4q(inst_holders: pd.Series) -> pd.Series:
    """Holder count now vs trailing-4Q max — fractional holder-base cliff-drop."""
    mx = _rolling_max(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders - mx, mx)


def fsp_ext_038_holders_cliff_drop_8q(inst_holders: pd.Series) -> pd.Series:
    """Holder count now vs trailing-8Q max — fractional holder-base cliff-drop, 2y."""
    mx = _rolling_max(inst_holders, _TD_2Y)
    return _safe_div(inst_holders - mx, mx)


def fsp_ext_039_inst_pct_cliff_drop_4q(inst_pct: pd.Series) -> pd.Series:
    """Inst_pct now vs trailing-4Q max — fractional ownership cliff-drop."""
    mx = _rolling_max(inst_pct, _TD_YEAR)
    return _safe_div(inst_pct - mx, mx)


def fsp_ext_040_inst_shares_drop_depth_below_median(inst_shares: pd.Series) -> pd.Series:
    """Fractional shortfall of inst_shares below its 4Q rolling median (0 when above)."""
    med = _rolling_median(inst_shares, _TD_YEAR)
    return _safe_div(med - inst_shares, med).clip(lower=0)


def fsp_ext_041_avg_position_drop_depth_below_median(avg_position: pd.Series) -> pd.Series:
    """Fractional shortfall of avg_position below its 4Q rolling median (0 when above)."""
    med = _rolling_median(avg_position, _TD_YEAR)
    return _safe_div(med - avg_position, med).clip(lower=0)


def fsp_ext_042_holders_drop_depth_below_median(inst_holders: pd.Series) -> pd.Series:
    """Fractional shortfall of holder count below its 4Q rolling median (0 when above)."""
    med = _rolling_median(inst_holders, _TD_YEAR)
    return _safe_div(med - inst_holders, med).clip(lower=0)


# --- Group E (043-052): Exit / liquidation streaks and persistence ---

def fsp_ext_043_consec_days_closed_above_median(closed_positions: pd.Series) -> pd.Series:
    """Consecutive days closed positions exceeded their trailing-4Q median."""
    return _consec_streak(closed_positions > _rolling_median(closed_positions, _TD_YEAR))


def fsp_ext_044_consec_days_combined_selling_above_median(closed_positions: pd.Series,
                                                           decreased_positions: pd.Series) -> pd.Series:
    """Consecutive days (closed+decreased) exceeded its trailing-4Q median."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _consec_streak(s > _rolling_median(s, _TD_YEAR))


def fsp_ext_045_consec_days_inst_shares_falling(inst_shares: pd.Series) -> pd.Series:
    """Consecutive days inst_shares fell below its QoQ-prior value."""
    return _consec_streak(inst_shares < inst_shares.shift(_TD_QTR))


def fsp_ext_046_consec_days_holders_falling(inst_holders: pd.Series) -> pd.Series:
    """Consecutive days holder count fell below its QoQ-prior value."""
    return _consec_streak(inst_holders < inst_holders.shift(_TD_QTR))


def fsp_ext_047_consec_days_avg_position_falling(avg_position: pd.Series) -> pd.Series:
    """Consecutive days avg_position fell below its QoQ-prior value."""
    return _consec_streak(avg_position < avg_position.shift(_TD_QTR))


def fsp_ext_048_consec_days_sell_dominates_buy(closed_positions: pd.Series,
                                                decreased_positions: pd.Series,
                                                new_positions: pd.Series,
                                                increased_positions: pd.Series) -> pd.Series:
    """Consecutive days sells (closed+decreased) exceeded buys (new+increased)."""
    sells = _combined_selling(closed_positions, decreased_positions)
    buys = new_positions.fillna(0) + increased_positions.fillna(0)
    return _consec_streak(sells > buys)


def fsp_ext_049_inst_shares_falling_days_2y(inst_shares: pd.Series) -> pd.Series:
    """Count of trailing-2y days inst_shares was below its QoQ-prior value."""
    return _rolling_sum((inst_shares < inst_shares.shift(_TD_QTR)).astype(float), _TD_2Y)


def fsp_ext_050_holders_falling_days_2y(inst_holders: pd.Series) -> pd.Series:
    """Count of trailing-2y days holder count was below its QoQ-prior value."""
    return _rolling_sum((inst_holders < inst_holders.shift(_TD_QTR)).astype(float), _TD_2Y)


def fsp_ext_051_max_sell_dominates_streak_2y(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              new_positions: pd.Series,
                                              increased_positions: pd.Series) -> pd.Series:
    """Longest run of sell-dominated days within trailing 2 years."""
    sells = _combined_selling(closed_positions, decreased_positions)
    buys = new_positions.fillna(0) + increased_positions.fillna(0)
    return _rolling_max(_consec_streak(sells > buys), _TD_2Y)


def fsp_ext_052_high_closed_days_2y(closed_positions: pd.Series) -> pd.Series:
    """Count of trailing-2y days closed positions sat above their trailing-4Q mean."""
    flag = (closed_positions > _rolling_mean(closed_positions, _TD_YEAR)).astype(float)
    return _rolling_sum(flag, _TD_2Y)


# --- Group F (053-062): EWM smoothing and crossovers ---

def fsp_ext_053_closed_pos_ewm_1q(closed_positions: pd.Series) -> pd.Series:
    """EWM (span=1 quarter) of closed positions — smoothed exit baseline."""
    return _ewm_mean(closed_positions, _TD_QTR)


def fsp_ext_054_closed_pos_ewm_spike_2q(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / EWM(span=126) — spike vs medium-run EWM baseline."""
    return _safe_div(closed_positions, _ewm_mean(closed_positions, _TD_2Q))


def fsp_ext_055_combined_selling_ewm_spike_2q(closed_positions: pd.Series,
                                               decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / EWM(span=126) — combined selling spike vs medium EWM."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _safe_div(s, _ewm_mean(s, _TD_2Q))


def fsp_ext_056_closed_pos_ewm_short_minus_long(closed_positions: pd.Series) -> pd.Series:
    """Closed positions EWM(1q) minus EWM(1y) — exit-momentum crossover."""
    return _ewm_mean(closed_positions, _TD_QTR) - _ewm_mean(closed_positions, _TD_YEAR)


def fsp_ext_057_combined_selling_ewm_short_minus_long(closed_positions: pd.Series,
                                                       decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) EWM(1q) minus EWM(1y) — combined-selling momentum crossover."""
    s = _combined_selling(closed_positions, decreased_positions)
    return _ewm_mean(s, _TD_QTR) - _ewm_mean(s, _TD_YEAR)


def fsp_ext_058_inst_shares_ewm_deviation_2q(inst_shares: pd.Series) -> pd.Series:
    """Inst shares deviation from EWM(span=126) — sudden 2Q-scale departure from trend."""
    return inst_shares - _ewm_mean(inst_shares, _TD_2Q)


def fsp_ext_059_inst_value_ewm_deviation_1y(inst_value: pd.Series) -> pd.Series:
    """Inst value deviation from EWM(span=252) — departure from 1-year trend."""
    return inst_value - _ewm_mean(inst_value, _TD_YEAR)


def fsp_ext_060_inst_pct_ewm_deviation_1y(inst_pct: pd.Series) -> pd.Series:
    """Inst_pct deviation from EWM(span=252) — sudden ownership departure from trend."""
    return inst_pct - _ewm_mean(inst_pct, _TD_YEAR)


def fsp_ext_061_avg_position_ewm_deviation_2q(avg_position: pd.Series) -> pd.Series:
    """Avg position deviation from EWM(span=126)."""
    return avg_position - _ewm_mean(avg_position, _TD_2Q)


def fsp_ext_062_decreased_pos_ewm_spike(decreased_positions: pd.Series) -> pd.Series:
    """Decreased positions / EWM(span=252) — trim spike vs long EWM baseline."""
    return _safe_div(decreased_positions, _ewm_mean(decreased_positions, _TD_YEAR))


# --- Group G (063-068): Multi-quarter acceleration / drop dynamics ---

def fsp_ext_063_closed_pos_3q_acceleration(closed_positions: pd.Series) -> pd.Series:
    """3-quarter change in closed positions — multi-quarter acceleration of exits."""
    return closed_positions - closed_positions.shift(_TD_3Q)


def fsp_ext_064_combined_selling_3q_acceleration(closed_positions: pd.Series,
                                                  decreased_positions: pd.Series) -> pd.Series:
    """3-quarter change in (closed+decreased) — multi-quarter selling acceleration."""
    s = _combined_selling(closed_positions, decreased_positions)
    return s - s.shift(_TD_3Q)


def fsp_ext_065_inst_shares_3q_pct_drop(inst_shares: pd.Series) -> pd.Series:
    """Percentage change in inst_shares over 3 quarters — multi-quarter exodus."""
    prev = inst_shares.shift(_TD_3Q)
    return _safe_div(inst_shares - prev, prev)


def fsp_ext_066_inst_value_3q_pct_drop(inst_value: pd.Series) -> pd.Series:
    """Percentage change in inst_value over 3 quarters — multi-quarter value loss."""
    prev = inst_value.shift(_TD_3Q)
    return _safe_div(inst_value - prev, prev)


def fsp_ext_067_holders_3q_pct_drop(inst_holders: pd.Series) -> pd.Series:
    """Percentage holder change over 3 quarters — multi-quarter departure."""
    prev = inst_holders.shift(_TD_3Q)
    return _safe_div(inst_holders - prev, prev)


def fsp_ext_068_inst_pct_2q_drop(inst_pct: pd.Series) -> pd.Series:
    """Change in inst_pct over 2 quarters — multi-quarter ownership loss."""
    return inst_pct - inst_pct.shift(_TD_2Q)


# --- Group H (069-075): Composite fire-sale distress scores ---

def fsp_ext_069_exit_breadth_4q_mean(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """Trailing-4Q mean of (closed+decreased)/inst_holders selling breadth."""
    ratio = _safe_div(_combined_selling(closed_positions, decreased_positions), inst_holders)
    return _rolling_mean(ratio, _TD_YEAR)


def fsp_ext_070_sell_buy_imbalance_zscore_8q(closed_positions: pd.Series,
                                              decreased_positions: pd.Series,
                                              new_positions: pd.Series,
                                              increased_positions: pd.Series) -> pd.Series:
    """8-quarter z-score of the sell/buy institutional-flow imbalance ratio."""
    sells = _combined_selling(closed_positions, decreased_positions)
    buys = new_positions.fillna(0) + increased_positions.fillna(0)
    ratio = _safe_div(sells, buys + _EPS)
    return _zscore_rolling(ratio, _TD_2Y)


def fsp_ext_071_firesale_breadth_pctile_index(closed_positions: pd.Series,
                                               decreased_positions: pd.Series,
                                               inst_holders: pd.Series) -> pd.Series:
    """4Q percentile rank of selling breadth * deep-breadth flag (breadth > 25% of holders)."""
    ratio = _safe_div(_combined_selling(closed_positions, decreased_positions), inst_holders)
    pct = _rolling_rank_pct(ratio, _TD_YEAR)
    flag = (ratio > 0.25).astype(float)
    return pct * flag


def fsp_ext_072_synchrony_shares_holders_score(closed_positions: pd.Series,
                                                inst_holders: pd.Series,
                                                inst_shares: pd.Series) -> pd.Series:
    """Exit breadth * |negative inst_shares z-score| — share-exodus synchrony score."""
    breadth = _safe_div(closed_positions, inst_holders)
    z_shares = _zscore_rolling(inst_shares, _TD_2Y).clip(upper=0).abs()
    return breadth * z_shares


def fsp_ext_073_distress_acceleration_composite(closed_positions: pd.Series,
                                                 decreased_positions: pd.Series,
                                                 inst_holders: pd.Series) -> pd.Series:
    """QoQ change in selling-breadth ratio * its 4Q z-score — accelerating-distress composite."""
    ratio = _safe_div(_combined_selling(closed_positions, decreased_positions), inst_holders)
    accel = (ratio - ratio.shift(_TD_QTR)).clip(lower=0)
    return accel * _zscore_rolling(ratio, _TD_YEAR).clip(lower=0)


def fsp_ext_074_firesale_composite_score_2y(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             inst_shares: pd.Series,
                                             avg_position: pd.Series) -> pd.Series:
    """Sum of 2-year abruptness z-scores: closed positions and combined selling on the
    upside, inst_shares and avg_position collapse on the downside. Higher = more fire-sale."""
    z1 = _zscore_rolling(closed_positions, _TD_2Y).clip(lower=0)
    z2 = _zscore_rolling(_combined_selling(closed_positions, decreased_positions), _TD_2Y).clip(lower=0)
    z3 = _zscore_rolling(inst_shares, _TD_2Y).clip(upper=0).abs()
    z4 = _zscore_rolling(avg_position, _TD_2Y).clip(upper=0).abs()
    return z1 + z2 + z3 + z4


def fsp_ext_075_capitulation_liquidation_composite(closed_positions: pd.Series,
                                                    decreased_positions: pd.Series,
                                                    new_positions: pd.Series,
                                                    increased_positions: pd.Series,
                                                    inst_holders: pd.Series,
                                                    inst_shares: pd.Series) -> pd.Series:
    """Capitulation liquidation composite: selling-breadth percentile + net-selling-flow
    positivity flag + |negative inst_shares 2y z-score|. Higher = stronger forced-selling
    fire-sale signal."""
    breadth = _safe_div(_combined_selling(closed_positions, decreased_positions), inst_holders)
    breadth_pct = _rolling_rank_pct(breadth, _TD_YEAR).fillna(0.5)
    net = (_combined_selling(closed_positions, decreased_positions)
           - (new_positions.fillna(0) + increased_positions.fillna(0)))
    net_flag = (net > 0).astype(float)
    z_shares = _zscore_rolling(inst_shares, _TD_2Y).clip(upper=0).abs()
    return breadth_pct + net_flag + z_shares.clip(upper=3.0)


# ===========================================================================
# Registry
# ===========================================================================
FORCED_SELLING_PROXY_EXTENDED_REGISTRY_001_075 = {
    "fsp_ext_001_closed_vs_3q_mean_ratio": {"inputs": ["closed_positions"], "func": fsp_ext_001_closed_vs_3q_mean_ratio},
    "fsp_ext_002_closed_vs_8q_mean_ratio": {"inputs": ["closed_positions"], "func": fsp_ext_002_closed_vs_8q_mean_ratio},
    "fsp_ext_003_closed_vs_12q_mean_ratio": {"inputs": ["closed_positions"], "func": fsp_ext_003_closed_vs_12q_mean_ratio},
    "fsp_ext_004_combined_selling_vs_3q_mean": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_004_combined_selling_vs_3q_mean},
    "fsp_ext_005_combined_selling_vs_12q_mean": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_005_combined_selling_vs_12q_mean},
    "fsp_ext_006_decreased_vs_4q_mean_ratio": {"inputs": ["decreased_positions"], "func": fsp_ext_006_decreased_vs_4q_mean_ratio},
    "fsp_ext_007_decreased_vs_4q_max_ratio": {"inputs": ["decreased_positions"], "func": fsp_ext_007_decreased_vs_4q_max_ratio},
    "fsp_ext_008_closed_vs_12q_max_ratio": {"inputs": ["closed_positions"], "func": fsp_ext_008_closed_vs_12q_max_ratio},
    "fsp_ext_009_combined_selling_vs_12q_max": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_009_combined_selling_vs_12q_max},
    "fsp_ext_010_combined_selling_vs_3q_max": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_010_combined_selling_vs_3q_max},
    "fsp_ext_011_closed_pos_zscore_3q": {"inputs": ["closed_positions"], "func": fsp_ext_011_closed_pos_zscore_3q},
    "fsp_ext_012_closed_pos_zscore_12q": {"inputs": ["closed_positions"], "func": fsp_ext_012_closed_pos_zscore_12q},
    "fsp_ext_013_decreased_pos_zscore_4q": {"inputs": ["decreased_positions"], "func": fsp_ext_013_decreased_pos_zscore_4q},
    "fsp_ext_014_decreased_pos_zscore_8q": {"inputs": ["decreased_positions"], "func": fsp_ext_014_decreased_pos_zscore_8q},
    "fsp_ext_015_combined_selling_zscore_3q": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_015_combined_selling_zscore_3q},
    "fsp_ext_016_combined_selling_zscore_12q": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_016_combined_selling_zscore_12q},
    "fsp_ext_017_inst_shares_zscore_12q": {"inputs": ["inst_shares"], "func": fsp_ext_017_inst_shares_zscore_12q},
    "fsp_ext_018_inst_value_zscore_12q": {"inputs": ["inst_value"], "func": fsp_ext_018_inst_value_zscore_12q},
    "fsp_ext_019_avg_position_zscore_12q": {"inputs": ["avg_position"], "func": fsp_ext_019_avg_position_zscore_12q},
    "fsp_ext_020_holders_zscore_8q": {"inputs": ["inst_holders"], "func": fsp_ext_020_holders_zscore_8q},
    "fsp_ext_021_closed_pos_rank_8q": {"inputs": ["closed_positions"], "func": fsp_ext_021_closed_pos_rank_8q},
    "fsp_ext_022_closed_pos_rank_12q": {"inputs": ["closed_positions"], "func": fsp_ext_022_closed_pos_rank_12q},
    "fsp_ext_023_combined_selling_rank_8q": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_023_combined_selling_rank_8q},
    "fsp_ext_024_decreased_pos_rank_4q": {"inputs": ["decreased_positions"], "func": fsp_ext_024_decreased_pos_rank_4q},
    "fsp_ext_025_holders_rank_8q": {"inputs": ["inst_holders"], "func": fsp_ext_025_holders_rank_8q},
    "fsp_ext_026_avg_position_rank_8q": {"inputs": ["avg_position"], "func": fsp_ext_026_avg_position_rank_8q},
    "fsp_ext_027_inst_shares_rank_8q": {"inputs": ["inst_shares"], "func": fsp_ext_027_inst_shares_rank_8q},
    "fsp_ext_028_inst_pct_rank_8q": {"inputs": ["inst_pct"], "func": fsp_ext_028_inst_pct_rank_8q},
    "fsp_ext_029_selling_breadth_rank_4q": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": fsp_ext_029_selling_breadth_rank_4q},
    "fsp_ext_030_closed_pos_expanding_rank": {"inputs": ["closed_positions"], "func": fsp_ext_030_closed_pos_expanding_rank},
    "fsp_ext_031_inst_shares_cliff_drop_4q": {"inputs": ["inst_shares"], "func": fsp_ext_031_inst_shares_cliff_drop_4q},
    "fsp_ext_032_inst_shares_cliff_drop_8q": {"inputs": ["inst_shares"], "func": fsp_ext_032_inst_shares_cliff_drop_8q},
    "fsp_ext_033_inst_value_cliff_drop_4q": {"inputs": ["inst_value"], "func": fsp_ext_033_inst_value_cliff_drop_4q},
    "fsp_ext_034_inst_value_cliff_drop_8q": {"inputs": ["inst_value"], "func": fsp_ext_034_inst_value_cliff_drop_8q},
    "fsp_ext_035_avg_position_cliff_drop_4q": {"inputs": ["avg_position"], "func": fsp_ext_035_avg_position_cliff_drop_4q},
    "fsp_ext_036_avg_position_cliff_drop_8q": {"inputs": ["avg_position"], "func": fsp_ext_036_avg_position_cliff_drop_8q},
    "fsp_ext_037_holders_cliff_drop_4q": {"inputs": ["inst_holders"], "func": fsp_ext_037_holders_cliff_drop_4q},
    "fsp_ext_038_holders_cliff_drop_8q": {"inputs": ["inst_holders"], "func": fsp_ext_038_holders_cliff_drop_8q},
    "fsp_ext_039_inst_pct_cliff_drop_4q": {"inputs": ["inst_pct"], "func": fsp_ext_039_inst_pct_cliff_drop_4q},
    "fsp_ext_040_inst_shares_drop_depth_below_median": {"inputs": ["inst_shares"], "func": fsp_ext_040_inst_shares_drop_depth_below_median},
    "fsp_ext_041_avg_position_drop_depth_below_median": {"inputs": ["avg_position"], "func": fsp_ext_041_avg_position_drop_depth_below_median},
    "fsp_ext_042_holders_drop_depth_below_median": {"inputs": ["inst_holders"], "func": fsp_ext_042_holders_drop_depth_below_median},
    "fsp_ext_043_consec_days_closed_above_median": {"inputs": ["closed_positions"], "func": fsp_ext_043_consec_days_closed_above_median},
    "fsp_ext_044_consec_days_combined_selling_above_median": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_044_consec_days_combined_selling_above_median},
    "fsp_ext_045_consec_days_inst_shares_falling": {"inputs": ["inst_shares"], "func": fsp_ext_045_consec_days_inst_shares_falling},
    "fsp_ext_046_consec_days_holders_falling": {"inputs": ["inst_holders"], "func": fsp_ext_046_consec_days_holders_falling},
    "fsp_ext_047_consec_days_avg_position_falling": {"inputs": ["avg_position"], "func": fsp_ext_047_consec_days_avg_position_falling},
    "fsp_ext_048_consec_days_sell_dominates_buy": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": fsp_ext_048_consec_days_sell_dominates_buy},
    "fsp_ext_049_inst_shares_falling_days_2y": {"inputs": ["inst_shares"], "func": fsp_ext_049_inst_shares_falling_days_2y},
    "fsp_ext_050_holders_falling_days_2y": {"inputs": ["inst_holders"], "func": fsp_ext_050_holders_falling_days_2y},
    "fsp_ext_051_max_sell_dominates_streak_2y": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": fsp_ext_051_max_sell_dominates_streak_2y},
    "fsp_ext_052_high_closed_days_2y": {"inputs": ["closed_positions"], "func": fsp_ext_052_high_closed_days_2y},
    "fsp_ext_053_closed_pos_ewm_1q": {"inputs": ["closed_positions"], "func": fsp_ext_053_closed_pos_ewm_1q},
    "fsp_ext_054_closed_pos_ewm_spike_2q": {"inputs": ["closed_positions"], "func": fsp_ext_054_closed_pos_ewm_spike_2q},
    "fsp_ext_055_combined_selling_ewm_spike_2q": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_055_combined_selling_ewm_spike_2q},
    "fsp_ext_056_closed_pos_ewm_short_minus_long": {"inputs": ["closed_positions"], "func": fsp_ext_056_closed_pos_ewm_short_minus_long},
    "fsp_ext_057_combined_selling_ewm_short_minus_long": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_057_combined_selling_ewm_short_minus_long},
    "fsp_ext_058_inst_shares_ewm_deviation_2q": {"inputs": ["inst_shares"], "func": fsp_ext_058_inst_shares_ewm_deviation_2q},
    "fsp_ext_059_inst_value_ewm_deviation_1y": {"inputs": ["inst_value"], "func": fsp_ext_059_inst_value_ewm_deviation_1y},
    "fsp_ext_060_inst_pct_ewm_deviation_1y": {"inputs": ["inst_pct"], "func": fsp_ext_060_inst_pct_ewm_deviation_1y},
    "fsp_ext_061_avg_position_ewm_deviation_2q": {"inputs": ["avg_position"], "func": fsp_ext_061_avg_position_ewm_deviation_2q},
    "fsp_ext_062_decreased_pos_ewm_spike": {"inputs": ["decreased_positions"], "func": fsp_ext_062_decreased_pos_ewm_spike},
    "fsp_ext_063_closed_pos_3q_acceleration": {"inputs": ["closed_positions"], "func": fsp_ext_063_closed_pos_3q_acceleration},
    "fsp_ext_064_combined_selling_3q_acceleration": {"inputs": ["closed_positions", "decreased_positions"], "func": fsp_ext_064_combined_selling_3q_acceleration},
    "fsp_ext_065_inst_shares_3q_pct_drop": {"inputs": ["inst_shares"], "func": fsp_ext_065_inst_shares_3q_pct_drop},
    "fsp_ext_066_inst_value_3q_pct_drop": {"inputs": ["inst_value"], "func": fsp_ext_066_inst_value_3q_pct_drop},
    "fsp_ext_067_holders_3q_pct_drop": {"inputs": ["inst_holders"], "func": fsp_ext_067_holders_3q_pct_drop},
    "fsp_ext_068_inst_pct_2q_drop": {"inputs": ["inst_pct"], "func": fsp_ext_068_inst_pct_2q_drop},
    "fsp_ext_069_exit_breadth_4q_mean": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": fsp_ext_069_exit_breadth_4q_mean},
    "fsp_ext_070_sell_buy_imbalance_zscore_8q": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"], "func": fsp_ext_070_sell_buy_imbalance_zscore_8q},
    "fsp_ext_071_firesale_breadth_pctile_index": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": fsp_ext_071_firesale_breadth_pctile_index},
    "fsp_ext_072_synchrony_shares_holders_score": {"inputs": ["closed_positions", "inst_holders", "inst_shares"], "func": fsp_ext_072_synchrony_shares_holders_score},
    "fsp_ext_073_distress_acceleration_composite": {"inputs": ["closed_positions", "decreased_positions", "inst_holders"], "func": fsp_ext_073_distress_acceleration_composite},
    "fsp_ext_074_firesale_composite_score_2y": {"inputs": ["closed_positions", "decreased_positions", "inst_shares", "avg_position"], "func": fsp_ext_074_firesale_composite_score_2y},
    "fsp_ext_075_capitulation_liquidation_composite": {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders", "inst_shares"], "func": fsp_ext_075_capitulation_liquidation_composite},
}
