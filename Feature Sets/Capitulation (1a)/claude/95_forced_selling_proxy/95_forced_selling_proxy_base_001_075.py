"""
95_forced_selling_proxy — Base Features 001-100
===============================================
Domain: Signatures of FORCED / DISTRESSED LIQUIDATION by small institutions.
The target signal is ABRUPTNESS + BREADTH + SYNCHRONICITY (a fire sale), NOT a
slow gradual decline.  Folder 91 owns the slow-bleed trend; this folder owns
the sudden coordinated exodus.

Quarterly -> Daily Alignment Contract
--------------------------------------
All input Series are daily-indexed pandas Series that have been **forward-filled**
from quarterly Sharadar SF3 / 13F snapshots.  Because the underlying data updates
only once per quarter (~63 trading days), every derived Series will be stepwise /
sparse on a daily index — that is expected and correct.

Cadence constants (trading days):
  1 quarter  =  63 td
  1 year     = 252 td
  2 years    = 504 td
  3 years    = 756 td

Available input fields (all daily Series, forward-filled from quarterly data):
  closed_positions    — count of holders fully exiting this quarter
  decreased_positions — count of holders trimming this quarter
  new_positions       — count of holders initiating this quarter
  increased_positions — count of holders adding this quarter
  inst_holders        — count of institutional holders
  inst_shares         — aggregate shares held by all institutions
  inst_value          — aggregate USD value held by all institutions
  avg_position        — mean shares per institutional holder
  inst_pct            — institutional ownership as fraction of shares outstanding (0..1)

Each feature function is standalone: takes only the Series it needs, returns a
pandas Series of the same index.  Backward-looking only (positive shifts,
rolling/expanding/ewm windows).
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

def _align_quarterly_to_daily(s: pd.Series) -> pd.Series:
    """Return s unchanged — caller is responsible for forward-filling from quarterly."""
    return s


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / (den.replace(0, np.nan) + _EPS)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    return num.abs() / (den.abs().replace(0, np.nan) + _EPS)


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


# ===========================================================================
# Feature Functions 001 – 075
# ===========================================================================

def fsp_001_closed_pos_breadth_ratio(closed_positions: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """Closed positions as fraction of total holders — breadth of full exits."""
    return _safe_div(closed_positions, inst_holders)


def fsp_002_decreased_pos_breadth_ratio(decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """Decreased positions as fraction of total holders — breadth of trims."""
    return _safe_div(decreased_positions, inst_holders)


def fsp_003_combined_selling_breadth(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """(Closed + Decreased) / inst_holders — synchronized selling breadth."""
    return _safe_div(closed_positions + decreased_positions, inst_holders)


def fsp_004_closed_pos_zscore_4q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over trailing 4-quarter window (252 td)."""
    return _zscore_rolling(closed_positions, _TD_YEAR)


def fsp_005_closed_pos_zscore_2q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over trailing 2-quarter window (126 td)."""
    return _zscore_rolling(closed_positions, _TD_2Q)


def fsp_006_combined_selling_zscore_4q(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """Z-score of (closed + decreased) over 4-quarter window."""
    return _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR)


def fsp_007_closed_vs_4q_max_ratio(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-4Q max — spike detector."""
    mx = _rolling_max(closed_positions, _TD_YEAR)
    return _safe_div(closed_positions, mx)


def fsp_008_closed_vs_4q_mean_ratio(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-4Q mean — level relative to recent average."""
    mu = _rolling_mean(closed_positions, _TD_YEAR)
    return _safe_div(closed_positions, mu)


def fsp_009_inst_shares_qoq_drop(inst_shares: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in aggregate shares (negative = liquidation)."""
    return inst_shares - inst_shares.shift(_TD_QTR)


def fsp_010_inst_shares_pct_drop_qoq(inst_shares: pd.Series) -> pd.Series:
    """Percentage QoQ change in aggregate shares held."""
    prev = inst_shares.shift(_TD_QTR)
    return _safe_div(inst_shares - prev, prev)


def fsp_011_inst_value_qoq_drop(inst_value: pd.Series) -> pd.Series:
    """Quarter-over-quarter change in aggregate institutional value."""
    return inst_value - inst_value.shift(_TD_QTR)


def fsp_012_inst_value_pct_drop_qoq(inst_value: pd.Series) -> pd.Series:
    """Percentage QoQ change in aggregate institutional value held."""
    prev = inst_value.shift(_TD_QTR)
    return _safe_div(inst_value - prev, prev)


def fsp_013_avg_position_qoq_collapse(avg_position: pd.Series) -> pd.Series:
    """QoQ change in average position size — fire-sale shrinkage."""
    return avg_position - avg_position.shift(_TD_QTR)


def fsp_014_avg_position_pct_collapse_qoq(avg_position: pd.Series) -> pd.Series:
    """Percentage QoQ collapse in average position size."""
    prev = avg_position.shift(_TD_QTR)
    return _safe_div(avg_position - prev, prev)


def fsp_015_avg_position_zscore_4q(avg_position: pd.Series) -> pd.Series:
    """Z-score of avg_position over 4-quarter trailing window."""
    return _zscore_rolling(avg_position, _TD_YEAR)


def fsp_016_avg_position_vs_4q_max_ratio(avg_position: pd.Series) -> pd.Series:
    """Avg position / trailing-4Q max — how far below recent peak."""
    mx = _rolling_max(avg_position, _TD_YEAR)
    return _safe_div(avg_position, mx)


def fsp_017_holders_qoq_drop(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in institutional holder count — abrupt departure."""
    return inst_holders - inst_holders.shift(_TD_QTR)


def fsp_018_holders_pct_drop_qoq(inst_holders: pd.Series) -> pd.Series:
    """Percentage QoQ drop in holder count."""
    prev = inst_holders.shift(_TD_QTR)
    return _safe_div(inst_holders - prev, prev)


def fsp_019_holders_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    """Z-score of holder count over trailing 4-quarter window."""
    return _zscore_rolling(inst_holders, _TD_YEAR)


def fsp_020_holders_vs_4q_min_ratio(inst_holders: pd.Series) -> pd.Series:
    """Holder count / trailing-4Q min — proximity to recent low."""
    mn = _rolling_min(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders, mn)


def fsp_021_inst_pct_qoq_drop(inst_pct: pd.Series) -> pd.Series:
    """QoQ change in institutional ownership pct — abrupt ownership loss."""
    return inst_pct - inst_pct.shift(_TD_QTR)


def fsp_022_inst_pct_zscore_4q(inst_pct: pd.Series) -> pd.Series:
    """Z-score of inst_pct over 4-quarter trailing window."""
    return _zscore_rolling(inst_pct, _TD_YEAR)


def fsp_023_closed_net_of_new(closed_positions: pd.Series,
                               new_positions: pd.Series) -> pd.Series:
    """Closed minus new positions — net number of departing institutions."""
    return closed_positions - new_positions


def fsp_024_closed_net_of_new_ratio(closed_positions: pd.Series,
                                     new_positions: pd.Series,
                                     inst_holders: pd.Series) -> pd.Series:
    """(Closed - New) / inst_holders — net exit breadth."""
    return _safe_div(closed_positions - new_positions, inst_holders)


def fsp_025_sell_buy_imbalance_ratio(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / (New+Increased+EPS) — sell/buy institutional flow ratio."""
    sells = closed_positions + decreased_positions
    buys  = new_positions + increased_positions
    return _safe_div(sells, buys + _EPS)


def fsp_026_sell_buy_imbalance_zscore_4q(closed_positions: pd.Series,
                                          decreased_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series) -> pd.Series:
    """Z-score of the sell/buy imbalance ratio over 4 quarters."""
    ratio = _safe_div(closed_positions + decreased_positions,
                      new_positions + increased_positions + _EPS)
    return _zscore_rolling(ratio, _TD_YEAR)


def fsp_027_closed_pos_spike_2q(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing 2-quarter mean — spike vs near-term norm."""
    mu = _rolling_mean(closed_positions, _TD_2Q)
    return _safe_div(closed_positions, mu)


def fsp_028_combined_selling_spike_2q(closed_positions: pd.Series,
                                       decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing 2Q mean — combined selling spike."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_mean(s, _TD_2Q))


def fsp_029_inst_shares_cliff_drop_2q(inst_shares: pd.Series) -> pd.Series:
    """Shares held now vs 2-quarter-ago max — cliff-drop detection."""
    mx = _rolling_max(inst_shares, _TD_2Q)
    return _safe_div(inst_shares - mx, mx)


def fsp_030_inst_value_cliff_drop_2q(inst_value: pd.Series) -> pd.Series:
    """Value held now vs 2-quarter-ago max — cliff-drop detection."""
    mx = _rolling_max(inst_value, _TD_2Q)
    return _safe_div(inst_value - mx, mx)


def fsp_031_avg_position_cliff_drop_2q(avg_position: pd.Series) -> pd.Series:
    """Avg position now vs 2Q max — single-quarter collapse."""
    mx = _rolling_max(avg_position, _TD_2Q)
    return _safe_div(avg_position - mx, mx)


def fsp_032_closed_pos_4q_rank_pct(closed_positions: pd.Series) -> pd.Series:
    """Percentile rank of closed positions within trailing 4-quarter window."""
    return _rolling_rank_pct(closed_positions, _TD_YEAR)


def fsp_033_combined_selling_4q_rank_pct(closed_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """Percentile rank of (closed+decreased) within trailing 4Q window."""
    return _rolling_rank_pct(closed_positions + decreased_positions, _TD_YEAR)


def fsp_034_holders_drop_4q_rank_pct(inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of holder count within trailing 4Q window (low = exodus)."""
    return _rolling_rank_pct(inst_holders, _TD_YEAR)


def fsp_035_avg_position_drop_4q_rank_pct(avg_position: pd.Series) -> pd.Series:
    """Percentile rank of avg_position within trailing 4Q window (low = collapse)."""
    return _rolling_rank_pct(avg_position, _TD_YEAR)


def fsp_036_inst_shares_drop_4q_rank_pct(inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of inst_shares within trailing 4Q window (low = exodus)."""
    return _rolling_rank_pct(inst_shares, _TD_YEAR)


def fsp_037_inst_value_drop_4q_rank_pct(inst_value: pd.Series) -> pd.Series:
    """Percentile rank of inst_value within trailing 4Q window (low = exodus)."""
    return _rolling_rank_pct(inst_value, _TD_YEAR)


def fsp_038_closed_pos_ewm_spike(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / EWM(span=252) — spike vs long-run EWM baseline."""
    return _safe_div(closed_positions, _ewm_mean(closed_positions, _TD_YEAR))


def fsp_039_combined_selling_ewm_spike(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / EWM(span=252) — combined selling vs long EWM."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _ewm_mean(s, _TD_YEAR))


def fsp_040_inst_shares_ewm_deviation(inst_shares: pd.Series) -> pd.Series:
    """Inst shares deviation from EWM(span=252) — sudden departure from trend."""
    return inst_shares - _ewm_mean(inst_shares, _TD_YEAR)


def fsp_041_avg_position_ewm_deviation(avg_position: pd.Series) -> pd.Series:
    """Avg position deviation from EWM(span=252)."""
    return avg_position - _ewm_mean(avg_position, _TD_YEAR)


def fsp_042_holders_ewm_deviation(inst_holders: pd.Series) -> pd.Series:
    """Holder count deviation from EWM(span=252)."""
    return inst_holders - _ewm_mean(inst_holders, _TD_YEAR)


def fsp_043_closed_pos_2q_acceleration(closed_positions: pd.Series) -> pd.Series:
    """QoQ change in closed positions — acceleration of exits."""
    return closed_positions - closed_positions.shift(_TD_QTR)


def fsp_044_combined_selling_2q_acceleration(closed_positions: pd.Series,
                                              decreased_positions: pd.Series) -> pd.Series:
    """QoQ change in (closed+decreased) — acceleration of combined selling."""
    s = closed_positions + decreased_positions
    return s - s.shift(_TD_QTR)


def fsp_045_avg_position_2q_acceleration(avg_position: pd.Series) -> pd.Series:
    """QoQ change in avg_position collapse rate."""
    return avg_position - avg_position.shift(_TD_QTR)


def fsp_046_holders_2q_acceleration(inst_holders: pd.Series) -> pd.Series:
    """QoQ change in holder count — abruptness of departure."""
    return inst_holders - inst_holders.shift(_TD_QTR)


def fsp_047_closed_pct_of_total_activity(closed_positions: pd.Series,
                                          new_positions: pd.Series,
                                          increased_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """Closed / total (closed+new+increased+decreased) — liquidation share of all activity."""
    total = closed_positions + new_positions + increased_positions + decreased_positions
    return _safe_div(closed_positions, total)


def fsp_048_net_holder_loss_pct(closed_positions: pd.Series,
                                 new_positions: pd.Series,
                                 inst_holders: pd.Series) -> pd.Series:
    """(Closed - New) / inst_holders.shift(63) — net percentage holder loss."""
    prev_holders = inst_holders.shift(_TD_QTR)
    return _safe_div(closed_positions - new_positions, prev_holders)


def fsp_049_inst_pct_cliff_drop_2q(inst_pct: pd.Series) -> pd.Series:
    """Inst_pct now vs 2Q max — cliff-drop in ownership fraction."""
    mx = _rolling_max(inst_pct, _TD_2Q)
    return _safe_div(inst_pct - mx, mx)


def fsp_050_inst_pct_zscore_8q(inst_pct: pd.Series) -> pd.Series:
    """Z-score of inst_pct over 8-quarter (2-year) window."""
    return _zscore_rolling(inst_pct, _TD_2Y)


def fsp_051_closed_pos_zscore_8q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over 8-quarter (2-year) window."""
    return _zscore_rolling(closed_positions, _TD_2Y)


def fsp_052_combined_selling_zscore_8q(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """Z-score of (closed+decreased) over 2-year trailing window."""
    return _zscore_rolling(closed_positions + decreased_positions, _TD_2Y)


def fsp_053_avg_position_zscore_8q(avg_position: pd.Series) -> pd.Series:
    """Z-score of avg_position over 8-quarter (2-year) window."""
    return _zscore_rolling(avg_position, _TD_2Y)


def fsp_054_inst_shares_zscore_8q(inst_shares: pd.Series) -> pd.Series:
    """Z-score of inst_shares over 2-year trailing window."""
    return _zscore_rolling(inst_shares, _TD_2Y)


def fsp_055_inst_value_zscore_8q(inst_value: pd.Series) -> pd.Series:
    """Z-score of inst_value over 2-year trailing window."""
    return _zscore_rolling(inst_value, _TD_2Y)


def fsp_056_closed_pos_vs_8q_max(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-8Q max — spike vs 2-year peak."""
    return _safe_div(closed_positions, _rolling_max(closed_positions, _TD_2Y))


def fsp_057_combined_selling_vs_8q_max(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing-8Q max — spike vs 2-year combined peak."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_max(s, _TD_2Y))


def fsp_058_holders_vs_8q_min(inst_holders: pd.Series) -> pd.Series:
    """Holder count / trailing-8Q min — proximity to 2-year low."""
    return _safe_div(inst_holders, _rolling_min(inst_holders, _TD_2Y))


def fsp_059_avg_position_vs_8q_min(avg_position: pd.Series) -> pd.Series:
    """Avg position / trailing-8Q min — proximity to 2-year low."""
    return _safe_div(avg_position, _rolling_min(avg_position, _TD_2Y))


def fsp_060_inst_shares_vs_8q_min(inst_shares: pd.Series) -> pd.Series:
    """Inst shares / trailing-8Q min — proximity to 2-year low."""
    return _safe_div(inst_shares, _rolling_min(inst_shares, _TD_2Y))


def fsp_061_closed_pos_median_spike_4q(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-4Q median — spike above typical quarterly level."""
    med = _rolling_median(closed_positions, _TD_YEAR)
    return _safe_div(closed_positions, med)


def fsp_062_combined_selling_median_spike_4q(closed_positions: pd.Series,
                                              decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing-4Q median — selling spike above typical level."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_median(s, _TD_YEAR))


def fsp_063_selling_breadth_zscore_2q(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Z-score of (closed+decreased)/inst_holders over 2Q trailing window."""
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_2Q)


def fsp_064_selling_breadth_zscore_4q(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Z-score of (closed+decreased)/inst_holders over 4Q trailing window."""
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def fsp_065_closed_breadth_zscore_4q(closed_positions: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """Z-score of closed/inst_holders breadth ratio over 4Q window."""
    ratio = _safe_div(closed_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def fsp_066_inst_shares_2q_acceleration(inst_shares: pd.Series) -> pd.Series:
    """2Q rate of change in inst_shares — abruptness of share exodus."""
    return inst_shares - inst_shares.shift(_TD_2Q)


def fsp_067_inst_value_2q_acceleration(inst_value: pd.Series) -> pd.Series:
    """2Q rate of change in inst_value — abruptness of value destruction."""
    return inst_value - inst_value.shift(_TD_2Q)


def fsp_068_holders_2q_pct_drop(inst_holders: pd.Series) -> pd.Series:
    """Percentage holder change over 2 quarters — abrupt multi-quarter departure."""
    prev = inst_holders.shift(_TD_2Q)
    return _safe_div(inst_holders - prev, prev)


def fsp_069_avg_position_2q_pct_collapse(avg_position: pd.Series) -> pd.Series:
    """Percentage change in avg_position over 2 quarters."""
    prev = avg_position.shift(_TD_2Q)
    return _safe_div(avg_position - prev, prev)


def fsp_070_sell_pressure_index(closed_positions: pd.Series,
                                 decreased_positions: pd.Series,
                                 inst_holders: pd.Series,
                                 inst_shares: pd.Series) -> pd.Series:
    """Composite: breadth_ratio * z-score of inst_shares drop — fire-sale pressure index."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    z_shares = _zscore_rolling(inst_shares, _TD_YEAR)
    return breadth * z_shares.clip(upper=0).abs()


def fsp_071_liquidation_synchrony_score(closed_positions: pd.Series,
                                         inst_holders: pd.Series,
                                         avg_position: pd.Series) -> pd.Series:
    """Breadth of exits * avg_position collapse z-score — synchrony signal."""
    breadth = _safe_div(closed_positions, inst_holders)
    z_pos = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    return breadth * z_pos


def fsp_072_firesale_composite_score(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      inst_holders: pd.Series,
                                      inst_shares: pd.Series,
                                      avg_position: pd.Series) -> pd.Series:
    """Sum of abruptness z-scores: closed_pos + combined_selling + shares + avg_position.
    Higher = more fire-sale-like."""
    z1 = _zscore_rolling(closed_positions, _TD_YEAR)
    z2 = _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR)
    z3 = _zscore_rolling(inst_shares, _TD_YEAR)
    z4 = _zscore_rolling(avg_position, _TD_YEAR)
    return z1 + z2 + z3.clip(upper=0) + z4.clip(upper=0)


def fsp_073_holders_drop_vs_closed_ratio(inst_holders: pd.Series,
                                          closed_positions: pd.Series) -> pd.Series:
    """QoQ holder count drop / closed positions — measures if closed positions explain holder loss."""
    holder_drop = (inst_holders - inst_holders.shift(_TD_QTR)).clip(upper=0).abs()
    return _safe_div(holder_drop, closed_positions + _EPS)


def fsp_074_inst_pct_vs_8q_min(inst_pct: pd.Series) -> pd.Series:
    """Inst_pct / trailing-8Q min — proximity to 2-year ownership low."""
    return _safe_div(inst_pct, _rolling_min(inst_pct, _TD_2Y))


def fsp_075_net_selling_flow_normalized(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """((Closed+Decreased)-(New+Increased)) / inst_holders — net normalized selling flow."""
    net = (closed_positions + decreased_positions) - (new_positions + increased_positions)
    return _safe_div(net, inst_holders)


# ===========================================================================
# Feature Functions 151 – 175
# ===========================================================================

def fsp_151_inst_pct_vs_4q_min(inst_pct: pd.Series) -> pd.Series:
    """Inst_pct / trailing-4Q min — proximity to 1-year ownership floor."""
    return _safe_div(inst_pct, _rolling_min(inst_pct, _TD_YEAR))


def fsp_152_closed_pos_2q_rank_pct(closed_positions: pd.Series) -> pd.Series:
    """Percentile rank of closed positions within trailing 2Q window."""
    return _rolling_rank_pct(closed_positions, _TD_2Q)


def fsp_153_combined_selling_2q_rank_pct(closed_positions: pd.Series,
                                          decreased_positions: pd.Series) -> pd.Series:
    """Percentile rank of (closed+decreased) within trailing 2Q window."""
    return _rolling_rank_pct(closed_positions + decreased_positions, _TD_2Q)


def fsp_154_holders_ewm_span63_deviation(inst_holders: pd.Series) -> pd.Series:
    """Holder count deviation from EWM(span=63) — very short-term departure."""
    return inst_holders - _ewm_mean(inst_holders, _TD_QTR)


def fsp_155_avg_position_ewm_span63_deviation(avg_position: pd.Series) -> pd.Series:
    """Avg position deviation from EWM(span=63) — abrupt intra-quarter collapse."""
    return avg_position - _ewm_mean(avg_position, _TD_QTR)


def fsp_156_inst_shares_pct_drop_2q(inst_shares: pd.Series) -> pd.Series:
    """Percentage change in inst_shares over 2 quarters."""
    prev = inst_shares.shift(_TD_2Q)
    return _safe_div(inst_shares - prev, prev)


def fsp_157_inst_value_pct_drop_2q(inst_value: pd.Series) -> pd.Series:
    """Percentage change in inst_value over 2 quarters."""
    prev = inst_value.shift(_TD_2Q)
    return _safe_div(inst_value - prev, prev)


def fsp_158_sell_surplus_pct_of_holders(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """Max(0, sells-buys) / inst_holders — selling surplus breadth."""
    surplus = ((closed_positions + decreased_positions) -
               (new_positions + increased_positions)).clip(lower=0)
    return _safe_div(surplus, inst_holders)


def fsp_159_closed_pos_vs_4q_median_deviation(closed_positions: pd.Series) -> pd.Series:
    """Closed positions - trailing-4Q median — signed deviation from typical level."""
    return closed_positions - _rolling_median(closed_positions, _TD_YEAR)


def fsp_160_inst_value_per_share_qoq(inst_value: pd.Series,
                                      inst_shares: pd.Series) -> pd.Series:
    """QoQ change in inst_value/inst_shares (implied price proxy) — forced price drop signal."""
    vps = _safe_div(inst_value, inst_shares)
    return vps - vps.shift(_TD_QTR)


def fsp_161_inst_value_per_share_zscore_4q(inst_value: pd.Series,
                                             inst_shares: pd.Series) -> pd.Series:
    """Z-score of inst_value/inst_shares over 4Q window."""
    return _zscore_rolling(_safe_div(inst_value, inst_shares), _TD_YEAR)


def fsp_162_closed_pos_zscore_3q(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over 3-quarter (189 td) trailing window."""
    return _zscore_rolling(closed_positions, 3 * _TD_QTR)


def fsp_163_holders_vs_2q_min(inst_holders: pd.Series) -> pd.Series:
    """Holder count / trailing-2Q min — proximity to 6-month holder floor."""
    return _safe_div(inst_holders, _rolling_min(inst_holders, _TD_2Q))


def fsp_164_inst_shares_vs_2q_min(inst_shares: pd.Series) -> pd.Series:
    """Inst shares / trailing-2Q min — proximity to 6-month share-count floor."""
    return _safe_div(inst_shares, _rolling_min(inst_shares, _TD_2Q))


def fsp_165_inst_pct_2q_rank_pct(inst_pct: pd.Series) -> pd.Series:
    """Percentile rank of inst_pct within trailing 2Q window (low = exodus)."""
    return _rolling_rank_pct(inst_pct, _TD_2Q)


def fsp_166_avg_position_3q_drop(avg_position: pd.Series) -> pd.Series:
    """Change in avg_position over 3 quarters — multi-quarter position collapse."""
    return avg_position - avg_position.shift(3 * _TD_QTR)


def fsp_167_inst_holders_3q_drop(inst_holders: pd.Series) -> pd.Series:
    """Change in inst_holders over 3 quarters — sustained departure signal."""
    return inst_holders - inst_holders.shift(3 * _TD_QTR)


def fsp_168_sell_buy_ratio_ewm_spike(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      new_positions: pd.Series,
                                      increased_positions: pd.Series) -> pd.Series:
    """Sell/buy imbalance ratio / EWM(span=252) of that ratio — spike vs long-run norm."""
    ratio = _safe_div(closed_positions + decreased_positions,
                      new_positions + increased_positions + _EPS)
    return _safe_div(ratio, _ewm_mean(ratio, _TD_YEAR))


def fsp_169_closed_pos_4q_sum_zscore_3y(closed_positions: pd.Series) -> pd.Series:
    """Z-score of trailing-4Q sum of closed positions over 3-year window."""
    return _zscore_rolling(_rolling_sum(closed_positions, _TD_YEAR), _TD_3Y)


def fsp_170_combined_selling_4q_sum_zscore_3y(closed_positions: pd.Series,
                                               decreased_positions: pd.Series) -> pd.Series:
    """Z-score of trailing-4Q sum of (closed+decreased) over 3-year window."""
    s = closed_positions + decreased_positions
    return _zscore_rolling(_rolling_sum(s, _TD_YEAR), _TD_3Y)


def fsp_171_inst_shares_vs_4q_mean_ratio(inst_shares: pd.Series) -> pd.Series:
    """Inst shares / trailing-4Q mean — below-average share level signal."""
    return _safe_div(inst_shares, _rolling_mean(inst_shares, _TD_YEAR))


def fsp_172_inst_value_vs_4q_mean_ratio(inst_value: pd.Series) -> pd.Series:
    """Inst value / trailing-4Q mean — below-average value level signal."""
    return _safe_div(inst_value, _rolling_mean(inst_value, _TD_YEAR))


def fsp_173_new_pos_pct_of_activity(closed_positions: pd.Series,
                                     new_positions: pd.Series,
                                     increased_positions: pd.Series,
                                     decreased_positions: pd.Series) -> pd.Series:
    """New positions / total activity — low value during fire sales (inverse signal)."""
    total = closed_positions + new_positions + increased_positions + decreased_positions
    return _safe_div(new_positions, total)


def fsp_174_holder_net_chg_vs_closed_zscore(inst_holders: pd.Series,
                                              closed_positions: pd.Series) -> pd.Series:
    """Z-score of (QoQ holder drop / closed_positions) over 4Q window — explanatory gap."""
    holder_drop = (inst_holders - inst_holders.shift(_TD_QTR)).clip(upper=0).abs()
    ratio = _safe_div(holder_drop, closed_positions + _EPS)
    return _zscore_rolling(ratio, _TD_YEAR)


def fsp_175_liquidation_depth_score(closed_positions: pd.Series,
                                     decreased_positions: pd.Series,
                                     inst_holders: pd.Series,
                                     inst_shares: pd.Series,
                                     avg_position: pd.Series,
                                     inst_pct: pd.Series) -> pd.Series:
    """Depth score: product proxy of breadth z-score and 3 dimension z-scores (cbrt).
    Signals simultaneous multi-dimension collapse depth."""
    z_b = _zscore_rolling(_safe_div(closed_positions + decreased_positions, inst_holders),
                          _TD_YEAR).clip(lower=0)
    z_s = _zscore_rolling(inst_shares, _TD_YEAR).clip(upper=0).abs()
    z_p = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    z_pct = _zscore_rolling(inst_pct, _TD_YEAR).clip(upper=0).abs()
    return np.cbrt(z_b * z_s * z_p * z_pct)


# ===========================================================================
# Registry
# ===========================================================================

FORCED_SELLING_PROXY_REGISTRY_001_075 = {
    "fsp_001_closed_pos_breadth_ratio":          {"inputs": ["closed_positions", "inst_holders"],                                                          "func": fsp_001_closed_pos_breadth_ratio},
    "fsp_002_decreased_pos_breadth_ratio":        {"inputs": ["decreased_positions", "inst_holders"],                                                       "func": fsp_002_decreased_pos_breadth_ratio},
    "fsp_003_combined_selling_breadth":           {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                   "func": fsp_003_combined_selling_breadth},
    "fsp_004_closed_pos_zscore_4q":               {"inputs": ["closed_positions"],                                                                          "func": fsp_004_closed_pos_zscore_4q},
    "fsp_005_closed_pos_zscore_2q":               {"inputs": ["closed_positions"],                                                                          "func": fsp_005_closed_pos_zscore_2q},
    "fsp_006_combined_selling_zscore_4q":         {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_006_combined_selling_zscore_4q},
    "fsp_007_closed_vs_4q_max_ratio":             {"inputs": ["closed_positions"],                                                                          "func": fsp_007_closed_vs_4q_max_ratio},
    "fsp_008_closed_vs_4q_mean_ratio":            {"inputs": ["closed_positions"],                                                                          "func": fsp_008_closed_vs_4q_mean_ratio},
    "fsp_009_inst_shares_qoq_drop":               {"inputs": ["inst_shares"],                                                                               "func": fsp_009_inst_shares_qoq_drop},
    "fsp_010_inst_shares_pct_drop_qoq":           {"inputs": ["inst_shares"],                                                                               "func": fsp_010_inst_shares_pct_drop_qoq},
    "fsp_011_inst_value_qoq_drop":                {"inputs": ["inst_value"],                                                                                "func": fsp_011_inst_value_qoq_drop},
    "fsp_012_inst_value_pct_drop_qoq":            {"inputs": ["inst_value"],                                                                                "func": fsp_012_inst_value_pct_drop_qoq},
    "fsp_013_avg_position_qoq_collapse":          {"inputs": ["avg_position"],                                                                              "func": fsp_013_avg_position_qoq_collapse},
    "fsp_014_avg_position_pct_collapse_qoq":      {"inputs": ["avg_position"],                                                                              "func": fsp_014_avg_position_pct_collapse_qoq},
    "fsp_015_avg_position_zscore_4q":             {"inputs": ["avg_position"],                                                                              "func": fsp_015_avg_position_zscore_4q},
    "fsp_016_avg_position_vs_4q_max_ratio":       {"inputs": ["avg_position"],                                                                              "func": fsp_016_avg_position_vs_4q_max_ratio},
    "fsp_017_holders_qoq_drop":                   {"inputs": ["inst_holders"],                                                                              "func": fsp_017_holders_qoq_drop},
    "fsp_018_holders_pct_drop_qoq":               {"inputs": ["inst_holders"],                                                                              "func": fsp_018_holders_pct_drop_qoq},
    "fsp_019_holders_zscore_4q":                  {"inputs": ["inst_holders"],                                                                              "func": fsp_019_holders_zscore_4q},
    "fsp_020_holders_vs_4q_min_ratio":            {"inputs": ["inst_holders"],                                                                              "func": fsp_020_holders_vs_4q_min_ratio},
    "fsp_021_inst_pct_qoq_drop":                  {"inputs": ["inst_pct"],                                                                                  "func": fsp_021_inst_pct_qoq_drop},
    "fsp_022_inst_pct_zscore_4q":                 {"inputs": ["inst_pct"],                                                                                  "func": fsp_022_inst_pct_zscore_4q},
    "fsp_023_closed_net_of_new":                  {"inputs": ["closed_positions", "new_positions"],                                                         "func": fsp_023_closed_net_of_new},
    "fsp_024_closed_net_of_new_ratio":            {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                         "func": fsp_024_closed_net_of_new_ratio},
    "fsp_025_sell_buy_imbalance_ratio":           {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],           "func": fsp_025_sell_buy_imbalance_ratio},
    "fsp_026_sell_buy_imbalance_zscore_4q":       {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],           "func": fsp_026_sell_buy_imbalance_zscore_4q},
    "fsp_027_closed_pos_spike_2q":                {"inputs": ["closed_positions"],                                                                          "func": fsp_027_closed_pos_spike_2q},
    "fsp_028_combined_selling_spike_2q":          {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_028_combined_selling_spike_2q},
    "fsp_029_inst_shares_cliff_drop_2q":          {"inputs": ["inst_shares"],                                                                               "func": fsp_029_inst_shares_cliff_drop_2q},
    "fsp_030_inst_value_cliff_drop_2q":           {"inputs": ["inst_value"],                                                                                "func": fsp_030_inst_value_cliff_drop_2q},
    "fsp_031_avg_position_cliff_drop_2q":         {"inputs": ["avg_position"],                                                                              "func": fsp_031_avg_position_cliff_drop_2q},
    "fsp_032_closed_pos_4q_rank_pct":             {"inputs": ["closed_positions"],                                                                          "func": fsp_032_closed_pos_4q_rank_pct},
    "fsp_033_combined_selling_4q_rank_pct":       {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_033_combined_selling_4q_rank_pct},
    "fsp_034_holders_drop_4q_rank_pct":           {"inputs": ["inst_holders"],                                                                              "func": fsp_034_holders_drop_4q_rank_pct},
    "fsp_035_avg_position_drop_4q_rank_pct":      {"inputs": ["avg_position"],                                                                              "func": fsp_035_avg_position_drop_4q_rank_pct},
    "fsp_036_inst_shares_drop_4q_rank_pct":       {"inputs": ["inst_shares"],                                                                               "func": fsp_036_inst_shares_drop_4q_rank_pct},
    "fsp_037_inst_value_drop_4q_rank_pct":        {"inputs": ["inst_value"],                                                                                "func": fsp_037_inst_value_drop_4q_rank_pct},
    "fsp_038_closed_pos_ewm_spike":               {"inputs": ["closed_positions"],                                                                          "func": fsp_038_closed_pos_ewm_spike},
    "fsp_039_combined_selling_ewm_spike":         {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_039_combined_selling_ewm_spike},
    "fsp_040_inst_shares_ewm_deviation":          {"inputs": ["inst_shares"],                                                                               "func": fsp_040_inst_shares_ewm_deviation},
    "fsp_041_avg_position_ewm_deviation":         {"inputs": ["avg_position"],                                                                              "func": fsp_041_avg_position_ewm_deviation},
    "fsp_042_holders_ewm_deviation":              {"inputs": ["inst_holders"],                                                                              "func": fsp_042_holders_ewm_deviation},
    "fsp_043_closed_pos_2q_acceleration":         {"inputs": ["closed_positions"],                                                                          "func": fsp_043_closed_pos_2q_acceleration},
    "fsp_044_combined_selling_2q_acceleration":   {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_044_combined_selling_2q_acceleration},
    "fsp_045_avg_position_2q_acceleration":       {"inputs": ["avg_position"],                                                                              "func": fsp_045_avg_position_2q_acceleration},
    "fsp_046_holders_2q_acceleration":            {"inputs": ["inst_holders"],                                                                              "func": fsp_046_holders_2q_acceleration},
    "fsp_047_closed_pct_of_total_activity":       {"inputs": ["closed_positions", "new_positions", "increased_positions", "decreased_positions"],           "func": fsp_047_closed_pct_of_total_activity},
    "fsp_048_net_holder_loss_pct":                {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                         "func": fsp_048_net_holder_loss_pct},
    "fsp_049_inst_pct_cliff_drop_2q":             {"inputs": ["inst_pct"],                                                                                  "func": fsp_049_inst_pct_cliff_drop_2q},
    "fsp_050_inst_pct_zscore_8q":                 {"inputs": ["inst_pct"],                                                                                  "func": fsp_050_inst_pct_zscore_8q},
    "fsp_051_closed_pos_zscore_8q":               {"inputs": ["closed_positions"],                                                                          "func": fsp_051_closed_pos_zscore_8q},
    "fsp_052_combined_selling_zscore_8q":         {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_052_combined_selling_zscore_8q},
    "fsp_053_avg_position_zscore_8q":             {"inputs": ["avg_position"],                                                                              "func": fsp_053_avg_position_zscore_8q},
    "fsp_054_inst_shares_zscore_8q":              {"inputs": ["inst_shares"],                                                                               "func": fsp_054_inst_shares_zscore_8q},
    "fsp_055_inst_value_zscore_8q":               {"inputs": ["inst_value"],                                                                                "func": fsp_055_inst_value_zscore_8q},
    "fsp_056_closed_pos_vs_8q_max":               {"inputs": ["closed_positions"],                                                                          "func": fsp_056_closed_pos_vs_8q_max},
    "fsp_057_combined_selling_vs_8q_max":         {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_057_combined_selling_vs_8q_max},
    "fsp_058_holders_vs_8q_min":                  {"inputs": ["inst_holders"],                                                                              "func": fsp_058_holders_vs_8q_min},
    "fsp_059_avg_position_vs_8q_min":             {"inputs": ["avg_position"],                                                                              "func": fsp_059_avg_position_vs_8q_min},
    "fsp_060_inst_shares_vs_8q_min":              {"inputs": ["inst_shares"],                                                                               "func": fsp_060_inst_shares_vs_8q_min},
    "fsp_061_closed_pos_median_spike_4q":         {"inputs": ["closed_positions"],                                                                          "func": fsp_061_closed_pos_median_spike_4q},
    "fsp_062_combined_selling_median_spike_4q":   {"inputs": ["closed_positions", "decreased_positions"],                                                   "func": fsp_062_combined_selling_median_spike_4q},
    "fsp_063_selling_breadth_zscore_2q":          {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                   "func": fsp_063_selling_breadth_zscore_2q},
    "fsp_064_selling_breadth_zscore_4q":          {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                   "func": fsp_064_selling_breadth_zscore_4q},
    "fsp_065_closed_breadth_zscore_4q":           {"inputs": ["closed_positions", "inst_holders"],                                                          "func": fsp_065_closed_breadth_zscore_4q},
    "fsp_066_inst_shares_2q_acceleration":        {"inputs": ["inst_shares"],                                                                               "func": fsp_066_inst_shares_2q_acceleration},
    "fsp_067_inst_value_2q_acceleration":         {"inputs": ["inst_value"],                                                                                "func": fsp_067_inst_value_2q_acceleration},
    "fsp_068_holders_2q_pct_drop":                {"inputs": ["inst_holders"],                                                                              "func": fsp_068_holders_2q_pct_drop},
    "fsp_069_avg_position_2q_pct_collapse":       {"inputs": ["avg_position"],                                                                              "func": fsp_069_avg_position_2q_pct_collapse},
    "fsp_070_sell_pressure_index":                {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares"],                    "func": fsp_070_sell_pressure_index},
    "fsp_071_liquidation_synchrony_score":        {"inputs": ["closed_positions", "inst_holders", "avg_position"],                                          "func": fsp_071_liquidation_synchrony_score},
    "fsp_072_firesale_composite_score":           {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position"],    "func": fsp_072_firesale_composite_score},
    "fsp_073_holders_drop_vs_closed_ratio":       {"inputs": ["inst_holders", "closed_positions"],                                                          "func": fsp_073_holders_drop_vs_closed_ratio},
    "fsp_074_inst_pct_vs_8q_min":                 {"inputs": ["inst_pct"],                                                                                  "func": fsp_074_inst_pct_vs_8q_min},
    "fsp_075_net_selling_flow_normalized":        {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"], "func": fsp_075_net_selling_flow_normalized},
    "fsp_151_inst_pct_vs_4q_min":                {"inputs": ["inst_pct"],                                                                                          "func": fsp_151_inst_pct_vs_4q_min},
    "fsp_152_closed_pos_2q_rank_pct":            {"inputs": ["closed_positions"],                                                                                  "func": fsp_152_closed_pos_2q_rank_pct},
    "fsp_153_combined_selling_2q_rank_pct":      {"inputs": ["closed_positions", "decreased_positions"],                                                           "func": fsp_153_combined_selling_2q_rank_pct},
    "fsp_154_holders_ewm_span63_deviation":      {"inputs": ["inst_holders"],                                                                                      "func": fsp_154_holders_ewm_span63_deviation},
    "fsp_155_avg_position_ewm_span63_deviation": {"inputs": ["avg_position"],                                                                                      "func": fsp_155_avg_position_ewm_span63_deviation},
    "fsp_156_inst_shares_pct_drop_2q":           {"inputs": ["inst_shares"],                                                                                       "func": fsp_156_inst_shares_pct_drop_2q},
    "fsp_157_inst_value_pct_drop_2q":            {"inputs": ["inst_value"],                                                                                        "func": fsp_157_inst_value_pct_drop_2q},
    "fsp_158_sell_surplus_pct_of_holders":       {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],   "func": fsp_158_sell_surplus_pct_of_holders},
    "fsp_159_closed_pos_vs_4q_median_deviation": {"inputs": ["closed_positions"],                                                                                  "func": fsp_159_closed_pos_vs_4q_median_deviation},
    "fsp_160_inst_value_per_share_qoq":          {"inputs": ["inst_value", "inst_shares"],                                                                         "func": fsp_160_inst_value_per_share_qoq},
    "fsp_161_inst_value_per_share_zscore_4q":    {"inputs": ["inst_value", "inst_shares"],                                                                         "func": fsp_161_inst_value_per_share_zscore_4q},
    "fsp_162_closed_pos_zscore_3q":              {"inputs": ["closed_positions"],                                                                                   "func": fsp_162_closed_pos_zscore_3q},
    "fsp_163_holders_vs_2q_min":                 {"inputs": ["inst_holders"],                                                                                      "func": fsp_163_holders_vs_2q_min},
    "fsp_164_inst_shares_vs_2q_min":             {"inputs": ["inst_shares"],                                                                                       "func": fsp_164_inst_shares_vs_2q_min},
    "fsp_165_inst_pct_2q_rank_pct":              {"inputs": ["inst_pct"],                                                                                          "func": fsp_165_inst_pct_2q_rank_pct},
    "fsp_166_avg_position_3q_drop":              {"inputs": ["avg_position"],                                                                                      "func": fsp_166_avg_position_3q_drop},
    "fsp_167_inst_holders_3q_drop":              {"inputs": ["inst_holders"],                                                                                      "func": fsp_167_inst_holders_3q_drop},
    "fsp_168_sell_buy_ratio_ewm_spike":          {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                   "func": fsp_168_sell_buy_ratio_ewm_spike},
    "fsp_169_closed_pos_4q_sum_zscore_3y":       {"inputs": ["closed_positions"],                                                                                  "func": fsp_169_closed_pos_4q_sum_zscore_3y},
    "fsp_170_combined_selling_4q_sum_zscore_3y": {"inputs": ["closed_positions", "decreased_positions"],                                                           "func": fsp_170_combined_selling_4q_sum_zscore_3y},
    "fsp_171_inst_shares_vs_4q_mean_ratio":      {"inputs": ["inst_shares"],                                                                                       "func": fsp_171_inst_shares_vs_4q_mean_ratio},
    "fsp_172_inst_value_vs_4q_mean_ratio":       {"inputs": ["inst_value"],                                                                                        "func": fsp_172_inst_value_vs_4q_mean_ratio},
    "fsp_173_new_pos_pct_of_activity":           {"inputs": ["closed_positions", "new_positions", "increased_positions", "decreased_positions"],                   "func": fsp_173_new_pos_pct_of_activity},
    "fsp_174_holder_net_chg_vs_closed_zscore":   {"inputs": ["inst_holders", "closed_positions"],                                                                  "func": fsp_174_holder_net_chg_vs_closed_zscore},
    "fsp_175_liquidation_depth_score":           {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position", "inst_pct"],"func": fsp_175_liquidation_depth_score},
}
