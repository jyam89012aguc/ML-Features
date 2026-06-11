"""
95_forced_selling_proxy — Base Features 076-200
================================================
Domain: Signatures of FORCED / DISTRESSED LIQUIDATION by small institutions.
The target signal is ABRUPTNESS + BREADTH + SYNCHRONICITY (a fire sale), NOT a
slow gradual decline.

Quarterly -> Daily Alignment Contract
--------------------------------------
All inputs are daily pandas Series forward-filled from quarterly SF3/13F data.
Data changes at most once per ~63 trading days — derived series are stepwise.

Cadence constants (trading days):
  1 quarter  =  63 td
  1 year     = 252 td
  2 years    = 504 td
  3 years    = 756 td

Available input fields:
  closed_positions, decreased_positions, new_positions, increased_positions,
  inst_holders, inst_shares, inst_value, avg_position, inst_pct

Each function is standalone, backward-looking only.
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
    """Return s unchanged — caller is responsible for forward-filling."""
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
# Feature Functions 076 – 150
# ===========================================================================

def fsp_076_closed_pos_3y_zscore(closed_positions: pd.Series) -> pd.Series:
    """Z-score of closed positions over 3-year (756 td) trailing window."""
    return _zscore_rolling(closed_positions, _TD_3Y)


def fsp_077_combined_selling_3y_zscore(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """Z-score of (closed+decreased) over 3-year trailing window."""
    return _zscore_rolling(closed_positions + decreased_positions, _TD_3Y)


def fsp_078_avg_position_3y_zscore(avg_position: pd.Series) -> pd.Series:
    """Z-score of avg_position over 3-year trailing window."""
    return _zscore_rolling(avg_position, _TD_3Y)


def fsp_079_inst_holders_3y_zscore(inst_holders: pd.Series) -> pd.Series:
    """Z-score of holder count over 3-year trailing window."""
    return _zscore_rolling(inst_holders, _TD_3Y)


def fsp_080_inst_shares_3y_zscore(inst_shares: pd.Series) -> pd.Series:
    """Z-score of inst_shares over 3-year trailing window."""
    return _zscore_rolling(inst_shares, _TD_3Y)


def fsp_081_inst_value_3y_zscore(inst_value: pd.Series) -> pd.Series:
    """Z-score of inst_value over 3-year trailing window."""
    return _zscore_rolling(inst_value, _TD_3Y)


def fsp_082_closed_vs_3y_max(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-3Y max — spike vs 3-year ceiling."""
    return _safe_div(closed_positions, _rolling_max(closed_positions, _TD_3Y))


def fsp_083_combined_selling_vs_3y_max(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing-3Y max — selling vs 3-year ceiling."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_max(s, _TD_3Y))


def fsp_084_holders_vs_3y_min(inst_holders: pd.Series) -> pd.Series:
    """Holder count / trailing-3Y min — proximity to 3-year low (1.0 = at min)."""
    return _safe_div(inst_holders, _rolling_min(inst_holders, _TD_3Y))


def fsp_085_avg_position_vs_3y_min(avg_position: pd.Series) -> pd.Series:
    """Avg position / trailing-3Y min — proximity to 3-year floor."""
    return _safe_div(avg_position, _rolling_min(avg_position, _TD_3Y))


def fsp_086_inst_shares_vs_3y_min(inst_shares: pd.Series) -> pd.Series:
    """Inst shares / trailing-3Y min — proximity to 3-year share-count floor."""
    return _safe_div(inst_shares, _rolling_min(inst_shares, _TD_3Y))


def fsp_087_inst_value_vs_3y_min(inst_value: pd.Series) -> pd.Series:
    """Inst value / trailing-3Y min — proximity to 3-year value floor."""
    return _safe_div(inst_value, _rolling_min(inst_value, _TD_3Y))


def fsp_088_selling_breadth_3y_rank_pct(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of selling breadth within 3-year window."""
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _rolling_rank_pct(ratio, _TD_3Y)


def fsp_089_closed_breadth_3y_rank_pct(closed_positions: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of closed/inst_holders within 3-year window."""
    ratio = _safe_div(closed_positions, inst_holders)
    return _rolling_rank_pct(ratio, _TD_3Y)


def fsp_090_avg_position_3y_rank_pct(avg_position: pd.Series) -> pd.Series:
    """Percentile rank of avg_position within 3-year window (low = collapse)."""
    return _rolling_rank_pct(avg_position, _TD_3Y)


def fsp_091_holders_3y_rank_pct(inst_holders: pd.Series) -> pd.Series:
    """Percentile rank of holder count within 3-year window (low = exodus)."""
    return _rolling_rank_pct(inst_holders, _TD_3Y)


def fsp_092_inst_shares_3y_rank_pct(inst_shares: pd.Series) -> pd.Series:
    """Percentile rank of inst_shares within 3-year window (low = exodus)."""
    return _rolling_rank_pct(inst_shares, _TD_3Y)


def fsp_093_sell_buy_imbalance_3y_rank_pct(closed_positions: pd.Series,
                                            decreased_positions: pd.Series,
                                            new_positions: pd.Series,
                                            increased_positions: pd.Series) -> pd.Series:
    """Percentile rank of sell/buy imbalance ratio within 3-year window."""
    ratio = _safe_div(closed_positions + decreased_positions,
                      new_positions + increased_positions + _EPS)
    return _rolling_rank_pct(ratio, _TD_3Y)


def fsp_094_ewm_closed_pos_deviation(closed_positions: pd.Series) -> pd.Series:
    """Closed positions - EWM(span=126) — short-term deviation from smoothed baseline."""
    return closed_positions - _ewm_mean(closed_positions, _TD_2Q)


def fsp_095_ewm_combined_selling_deviation(closed_positions: pd.Series,
                                            decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) - EWM(span=126) — short-term deviation from smoothed baseline."""
    s = closed_positions + decreased_positions
    return s - _ewm_mean(s, _TD_2Q)


def fsp_096_ewm_holders_deviation(inst_holders: pd.Series) -> pd.Series:
    """Holder count - EWM(span=126) — short-term departure from smoothed level."""
    return inst_holders - _ewm_mean(inst_holders, _TD_2Q)


def fsp_097_ewm_avg_position_deviation(avg_position: pd.Series) -> pd.Series:
    """Avg position - EWM(span=126) — short-term position collapse signal."""
    return avg_position - _ewm_mean(avg_position, _TD_2Q)


def fsp_098_ewm_inst_shares_deviation(inst_shares: pd.Series) -> pd.Series:
    """Inst shares - EWM(span=126) — short-term share exodus signal."""
    return inst_shares - _ewm_mean(inst_shares, _TD_2Q)


def fsp_099_ewm_inst_value_deviation(inst_value: pd.Series) -> pd.Series:
    """Inst value - EWM(span=126) — short-term value exodus signal."""
    return inst_value - _ewm_mean(inst_value, _TD_2Q)


def fsp_100_closed_pos_expanding_zscore(closed_positions: pd.Series) -> pd.Series:
    """Expanding-window z-score of closed positions — all-time spike intensity."""
    mu = closed_positions.expanding(min_periods=4).mean()
    sigma = closed_positions.expanding(min_periods=4).std()
    return (closed_positions - mu) / (sigma + _EPS)


def fsp_101_combined_selling_expanding_zscore(closed_positions: pd.Series,
                                               decreased_positions: pd.Series) -> pd.Series:
    """Expanding-window z-score of (closed+decreased) — all-time spike intensity."""
    s = closed_positions + decreased_positions
    mu = s.expanding(min_periods=4).mean()
    sigma = s.expanding(min_periods=4).std()
    return (s - mu) / (sigma + _EPS)


def fsp_102_avg_position_expanding_zscore(avg_position: pd.Series) -> pd.Series:
    """Expanding-window z-score of avg_position — all-time collapse intensity."""
    mu = avg_position.expanding(min_periods=4).mean()
    sigma = avg_position.expanding(min_periods=4).std()
    return (avg_position - mu) / (sigma + _EPS)


def fsp_103_holders_expanding_zscore(inst_holders: pd.Series) -> pd.Series:
    """Expanding-window z-score of holder count — all-time exodus intensity."""
    mu = inst_holders.expanding(min_periods=4).mean()
    sigma = inst_holders.expanding(min_periods=4).std()
    return (inst_holders - mu) / (sigma + _EPS)


def fsp_104_inst_shares_expanding_zscore(inst_shares: pd.Series) -> pd.Series:
    """Expanding-window z-score of inst_shares — all-time exodus intensity."""
    mu = inst_shares.expanding(min_periods=4).mean()
    sigma = inst_shares.expanding(min_periods=4).std()
    return (inst_shares - mu) / (sigma + _EPS)


def fsp_105_selling_burst_ratio_1q_vs_4q(closed_positions: pd.Series,
                                           decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing-4Q mean of (Closed+Decreased) — burst factor."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_mean(s, _TD_YEAR))


def fsp_106_closed_burst_ratio_1q_vs_8q(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-8Q mean — burst vs 2-year average."""
    return _safe_div(closed_positions, _rolling_mean(closed_positions, _TD_2Y))


def fsp_107_combined_selling_burst_1q_vs_8q(closed_positions: pd.Series,
                                              decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing-8Q mean — burst vs 2-year average."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_mean(s, _TD_2Y))


def fsp_108_holders_drop_abs_4q_max(inst_holders: pd.Series) -> pd.Series:
    """Absolute QoQ holder drop / trailing-4Q max of that drop — spike in departure rate."""
    drop = (inst_holders - inst_holders.shift(_TD_QTR)).clip(upper=0).abs()
    return _safe_div(drop, _rolling_max(drop, _TD_YEAR))


def fsp_109_avg_position_drop_abs_4q_max(avg_position: pd.Series) -> pd.Series:
    """Absolute QoQ avg_position drop / trailing-4Q max of drops."""
    drop = (avg_position - avg_position.shift(_TD_QTR)).clip(upper=0).abs()
    return _safe_div(drop, _rolling_max(drop, _TD_YEAR))


def fsp_110_inst_shares_drop_abs_4q_max(inst_shares: pd.Series) -> pd.Series:
    """Absolute QoQ inst_shares drop / trailing-4Q max of drops."""
    drop = (inst_shares - inst_shares.shift(_TD_QTR)).clip(upper=0).abs()
    return _safe_div(drop, _rolling_max(drop, _TD_YEAR))


def fsp_111_inst_value_drop_abs_4q_max(inst_value: pd.Series) -> pd.Series:
    """Absolute QoQ inst_value drop / trailing-4Q max of drops."""
    drop = (inst_value - inst_value.shift(_TD_QTR)).clip(upper=0).abs()
    return _safe_div(drop, _rolling_max(drop, _TD_YEAR))


def fsp_112_selling_breadth_ewm_spike(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Selling breadth / EWM(span=252) of that breadth — spike vs long-run EWM."""
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _safe_div(ratio, _ewm_mean(ratio, _TD_YEAR))


def fsp_113_closed_breadth_ewm_spike(closed_positions: pd.Series,
                                      inst_holders: pd.Series) -> pd.Series:
    """Closed/holders / EWM(span=252) of that ratio — spike vs long-run EWM."""
    ratio = _safe_div(closed_positions, inst_holders)
    return _safe_div(ratio, _ewm_mean(ratio, _TD_YEAR))


def fsp_114_net_selling_flow_zscore_4q(closed_positions: pd.Series,
                                        decreased_positions: pd.Series,
                                        new_positions: pd.Series,
                                        increased_positions: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """Z-score of net normalized selling flow over 4Q window."""
    net = _safe_div((closed_positions + decreased_positions) -
                    (new_positions + increased_positions), inst_holders)
    return _zscore_rolling(net, _TD_YEAR)


def fsp_115_net_selling_flow_zscore_8q(closed_positions: pd.Series,
                                        decreased_positions: pd.Series,
                                        new_positions: pd.Series,
                                        increased_positions: pd.Series,
                                        inst_holders: pd.Series) -> pd.Series:
    """Z-score of net normalized selling flow over 8Q window."""
    net = _safe_div((closed_positions + decreased_positions) -
                    (new_positions + increased_positions), inst_holders)
    return _zscore_rolling(net, _TD_2Y)


def fsp_116_holder_turnover_rate(closed_positions: pd.Series,
                                  new_positions: pd.Series,
                                  inst_holders: pd.Series) -> pd.Series:
    """(Closed+New) / inst_holders — holder churn rate; high churn + high closed = fire sale."""
    return _safe_div(closed_positions + new_positions, inst_holders)


def fsp_117_holder_turnover_zscore_4q(closed_positions: pd.Series,
                                       new_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Z-score of holder turnover rate over 4Q window."""
    turnover = _safe_div(closed_positions + new_positions, inst_holders)
    return _zscore_rolling(turnover, _TD_YEAR)


def fsp_118_inst_shares_per_holder_zscore_4q(inst_shares: pd.Series,
                                              inst_holders: pd.Series) -> pd.Series:
    """Z-score of inst_shares/inst_holders — same as avg_position z-score but computed fresh."""
    avg = _safe_div(inst_shares, inst_holders)
    return _zscore_rolling(avg, _TD_YEAR)


def fsp_119_inst_value_per_holder_qoq_pct(inst_value: pd.Series,
                                           inst_holders: pd.Series) -> pd.Series:
    """QoQ percentage change in value-per-holder — fire-sale per-institution cost signal."""
    val_per = _safe_div(inst_value, inst_holders)
    prev = val_per.shift(_TD_QTR)
    return _safe_div(val_per - prev, prev)


def fsp_120_inst_value_per_holder_zscore_4q(inst_value: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """Z-score of value-per-holder over 4Q window."""
    val_per = _safe_div(inst_value, inst_holders)
    return _zscore_rolling(val_per, _TD_YEAR)


def fsp_121_decreased_pos_zscore_4q(decreased_positions: pd.Series) -> pd.Series:
    """Z-score of decreased positions alone over 4Q window — trim breadth spike."""
    return _zscore_rolling(decreased_positions, _TD_YEAR)


def fsp_122_decreased_vs_4q_max(decreased_positions: pd.Series) -> pd.Series:
    """Decreased positions / trailing-4Q max — trim-breadth spike ratio."""
    return _safe_div(decreased_positions, _rolling_max(decreased_positions, _TD_YEAR))


def fsp_123_decreased_vs_holders_zscore(decreased_positions: pd.Series,
                                         inst_holders: pd.Series) -> pd.Series:
    """Z-score of decreased/inst_holders over 4Q window."""
    ratio = _safe_div(decreased_positions, inst_holders)
    return _zscore_rolling(ratio, _TD_YEAR)


def fsp_124_closed_pos_3q_cumsum_zscore(closed_positions: pd.Series) -> pd.Series:
    """Z-score of trailing-3Q sum of closed positions — clustered exit over 3 quarters."""
    cumsum3 = _rolling_sum(closed_positions, 3 * _TD_QTR)
    return _zscore_rolling(cumsum3, _TD_2Y)


def fsp_125_combined_selling_3q_cumsum_zscore(closed_positions: pd.Series,
                                               decreased_positions: pd.Series) -> pd.Series:
    """Z-score of trailing-3Q sum of (closed+decreased)."""
    s = closed_positions + decreased_positions
    return _zscore_rolling(_rolling_sum(s, 3 * _TD_QTR), _TD_2Y)


def fsp_126_holder_drop_3q_cumsum_zscore(inst_holders: pd.Series) -> pd.Series:
    """Z-score of total holder drop over trailing 3 quarters."""
    drop = (inst_holders - inst_holders.shift(_TD_QTR)).clip(upper=0).abs()
    return _zscore_rolling(_rolling_sum(drop, 3 * _TD_QTR), _TD_2Y)


def fsp_127_avg_position_drop_3q_cumsum(avg_position: pd.Series) -> pd.Series:
    """Cumulative avg_position decline over 3 quarters."""
    drop = (avg_position - avg_position.shift(_TD_QTR)).clip(upper=0).abs()
    return _rolling_sum(drop, 3 * _TD_QTR)


def fsp_128_inst_shares_drop_3q_cumsum(inst_shares: pd.Series) -> pd.Series:
    """Cumulative inst_shares decline over 3 quarters."""
    drop = (inst_shares - inst_shares.shift(_TD_QTR)).clip(upper=0).abs()
    return _rolling_sum(drop, 3 * _TD_QTR)


def fsp_129_inst_value_drop_3q_cumsum(inst_value: pd.Series) -> pd.Series:
    """Cumulative inst_value decline over 3 quarters."""
    drop = (inst_value - inst_value.shift(_TD_QTR)).clip(upper=0).abs()
    return _rolling_sum(drop, 3 * _TD_QTR)


def fsp_130_inst_pct_drop_zscore_4q(inst_pct: pd.Series) -> pd.Series:
    """Z-score of QoQ inst_pct change over 4Q window."""
    chg = inst_pct - inst_pct.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def fsp_131_selling_over_buying_surplus(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         new_positions: pd.Series,
                                         increased_positions: pd.Series) -> pd.Series:
    """Max(0, (Closed+Decreased) - (New+Increased)) — raw selling surplus."""
    return ((closed_positions + decreased_positions) -
            (new_positions + increased_positions)).clip(lower=0)


def fsp_132_selling_surplus_zscore_4q(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       new_positions: pd.Series,
                                       increased_positions: pd.Series) -> pd.Series:
    """Z-score of selling surplus (clipped at 0) over 4Q window."""
    surplus = ((closed_positions + decreased_positions) -
               (new_positions + increased_positions)).clip(lower=0)
    return _zscore_rolling(surplus, _TD_YEAR)


def fsp_133_closed_pos_std_spike(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-4Q std — units-of-std spike above mean."""
    std = _rolling_std(closed_positions, _TD_YEAR)
    return _safe_div(closed_positions - _rolling_mean(closed_positions, _TD_YEAR), std)


def fsp_134_combined_selling_std_spike(closed_positions: pd.Series,
                                        decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) spike in units of trailing-4Q std."""
    s = closed_positions + decreased_positions
    return _safe_div(s - _rolling_mean(s, _TD_YEAR), _rolling_std(s, _TD_YEAR))


def fsp_135_holders_pct_drop_zscore_4q(inst_holders: pd.Series) -> pd.Series:
    """Z-score of QoQ holder pct drop over 4Q window."""
    pct_chg = _safe_div(inst_holders - inst_holders.shift(_TD_QTR),
                        inst_holders.shift(_TD_QTR))
    return _zscore_rolling(pct_chg, _TD_YEAR)


def fsp_136_avg_position_drop_zscore_4q(avg_position: pd.Series) -> pd.Series:
    """Z-score of QoQ avg_position drop over 4Q window."""
    chg = avg_position - avg_position.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def fsp_137_inst_shares_drop_zscore_4q(inst_shares: pd.Series) -> pd.Series:
    """Z-score of QoQ inst_shares change over 4Q window."""
    chg = inst_shares - inst_shares.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def fsp_138_inst_value_drop_zscore_4q(inst_value: pd.Series) -> pd.Series:
    """Z-score of QoQ inst_value change over 4Q window."""
    chg = inst_value - inst_value.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_YEAR)


def fsp_139_firesale_breadth_x_severity(closed_positions: pd.Series,
                                         decreased_positions: pd.Series,
                                         inst_holders: pd.Series,
                                         avg_position: pd.Series) -> pd.Series:
    """Breadth ratio * |avg_position z-score| — fire-sale breadth times severity."""
    breadth = _safe_div(closed_positions + decreased_positions, inst_holders)
    sev = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    return breadth * sev


def fsp_140_exodus_velocity(inst_holders: pd.Series) -> pd.Series:
    """EWM(span=21) of QoQ holder drops — smoothed velocity of departure."""
    drop = (inst_holders - inst_holders.shift(_TD_QTR))
    return _ewm_mean(drop, 21)


def fsp_141_closed_pos_above_2std(closed_positions: pd.Series) -> pd.Series:
    """Binary: 1 if closed_positions > mean + 2*std (trailing 4Q), else 0."""
    mu = _rolling_mean(closed_positions, _TD_YEAR)
    std = _rolling_std(closed_positions, _TD_YEAR)
    return (closed_positions > mu + 2 * std).astype(float)


def fsp_142_combined_selling_above_2std(closed_positions: pd.Series,
                                         decreased_positions: pd.Series) -> pd.Series:
    """Binary: 1 if (closed+decreased) > mean + 2*std (trailing 4Q)."""
    s = closed_positions + decreased_positions
    mu = _rolling_mean(s, _TD_YEAR)
    std = _rolling_std(s, _TD_YEAR)
    return (s > mu + 2 * std).astype(float)


def fsp_143_holders_below_2std(inst_holders: pd.Series) -> pd.Series:
    """Binary: 1 if holder count < mean - 2*std (trailing 4Q), else 0."""
    mu = _rolling_mean(inst_holders, _TD_YEAR)
    std = _rolling_std(inst_holders, _TD_YEAR)
    return (inst_holders < mu - 2 * std).astype(float)


def fsp_144_avg_position_below_2std(avg_position: pd.Series) -> pd.Series:
    """Binary: 1 if avg_position < mean - 2*std (trailing 4Q)."""
    mu = _rolling_mean(avg_position, _TD_YEAR)
    std = _rolling_std(avg_position, _TD_YEAR)
    return (avg_position < mu - 2 * std).astype(float)


def fsp_145_liquidation_cluster_score(closed_positions: pd.Series,
                                       decreased_positions: pd.Series,
                                       inst_holders: pd.Series,
                                       inst_shares: pd.Series,
                                       avg_position: pd.Series,
                                       inst_pct: pd.Series) -> pd.Series:
    """Multi-signal cluster score: sum of negative z-scores across 4 dimensions.
    Measures how many dimensions simultaneously show forced liquidation."""
    z1 = _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR).clip(lower=0)
    z2 = _zscore_rolling(inst_holders, _TD_YEAR).clip(upper=0).abs()
    z3 = _zscore_rolling(inst_shares, _TD_YEAR).clip(upper=0).abs()
    z4 = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    z5 = _zscore_rolling(inst_pct, _TD_YEAR).clip(upper=0).abs()
    return z1 + z2 + z3 + z4 + z5


def fsp_146_inst_shares_drawdown_from_4q_peak(inst_shares: pd.Series) -> pd.Series:
    """(inst_shares - rolling-4Q-max) / rolling-4Q-max — drawdown from recent peak."""
    pk = _rolling_max(inst_shares, _TD_YEAR)
    return _safe_div(inst_shares - pk, pk)


def fsp_147_inst_value_drawdown_from_4q_peak(inst_value: pd.Series) -> pd.Series:
    """(inst_value - rolling-4Q-max) / rolling-4Q-max — drawdown from recent peak."""
    pk = _rolling_max(inst_value, _TD_YEAR)
    return _safe_div(inst_value - pk, pk)


def fsp_148_avg_position_drawdown_from_4q_peak(avg_position: pd.Series) -> pd.Series:
    """(avg_position - rolling-4Q-max) / rolling-4Q-max — drawdown from recent peak."""
    pk = _rolling_max(avg_position, _TD_YEAR)
    return _safe_div(avg_position - pk, pk)


def fsp_149_holders_drawdown_from_4q_peak(inst_holders: pd.Series) -> pd.Series:
    """(inst_holders - rolling-4Q-max) / rolling-4Q-max — drawdown from recent peak."""
    pk = _rolling_max(inst_holders, _TD_YEAR)
    return _safe_div(inst_holders - pk, pk)


def fsp_150_abrupt_selling_index(closed_positions: pd.Series,
                                  decreased_positions: pd.Series,
                                  inst_holders: pd.Series,
                                  avg_position: pd.Series,
                                  inst_shares: pd.Series) -> pd.Series:
    """Composite abruptness index: (breadth_z * abs(shares_z) * abs(pos_z))^(1/3).
    Geometric mean of z-score extremes — all three must spike simultaneously."""
    z_breadth = _zscore_rolling(_safe_div(closed_positions + decreased_positions,
                                          inst_holders), _TD_YEAR).clip(lower=0)
    z_shares  = _zscore_rolling(inst_shares, _TD_YEAR).clip(upper=0).abs()
    z_pos     = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    product   = z_breadth * z_shares * z_pos
    return np.cbrt(product)


# ===========================================================================
# Feature Functions 176 – 200
# ===========================================================================

def fsp_176_inst_pct_3q_drop(inst_pct: pd.Series) -> pd.Series:
    """Change in inst_pct over 3 quarters — sustained ownership erosion."""
    return inst_pct - inst_pct.shift(3 * _TD_QTR)


def fsp_177_inst_pct_3y_rank_pct(inst_pct: pd.Series) -> pd.Series:
    """Percentile rank of inst_pct within 3-year window (low = multi-year low)."""
    return _rolling_rank_pct(inst_pct, _TD_3Y)


def fsp_178_inst_shares_qoq_drop_zscore_3y(inst_shares: pd.Series) -> pd.Series:
    """Z-score of QoQ inst_shares change over 3-year window."""
    chg = inst_shares - inst_shares.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_3Y)


def fsp_179_inst_value_qoq_drop_zscore_3y(inst_value: pd.Series) -> pd.Series:
    """Z-score of QoQ inst_value change over 3-year window."""
    chg = inst_value - inst_value.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_3Y)


def fsp_180_holders_qoq_drop_zscore_3y(inst_holders: pd.Series) -> pd.Series:
    """Z-score of QoQ holder count change over 3-year window."""
    chg = inst_holders - inst_holders.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_3Y)


def fsp_181_avg_position_qoq_drop_zscore_3y(avg_position: pd.Series) -> pd.Series:
    """Z-score of QoQ avg_position change over 3-year window."""
    chg = avg_position - avg_position.shift(_TD_QTR)
    return _zscore_rolling(chg, _TD_3Y)


def fsp_182_closed_pos_1q_vs_3y_mean(closed_positions: pd.Series) -> pd.Series:
    """Closed positions / trailing-3Y mean — burst vs 3-year average."""
    return _safe_div(closed_positions, _rolling_mean(closed_positions, _TD_3Y))


def fsp_183_combined_selling_1q_vs_3y_mean(closed_positions: pd.Series,
                                             decreased_positions: pd.Series) -> pd.Series:
    """(Closed+Decreased) / trailing-3Y mean — burst vs 3-year combined average."""
    s = closed_positions + decreased_positions
    return _safe_div(s, _rolling_mean(s, _TD_3Y))


def fsp_184_inst_shares_drawdown_from_8q_peak(inst_shares: pd.Series) -> pd.Series:
    """(inst_shares - rolling-8Q-max) / rolling-8Q-max — drawdown from 2-year peak."""
    pk = _rolling_max(inst_shares, _TD_2Y)
    return _safe_div(inst_shares - pk, pk)


def fsp_185_inst_value_drawdown_from_8q_peak(inst_value: pd.Series) -> pd.Series:
    """(inst_value - rolling-8Q-max) / rolling-8Q-max — drawdown from 2-year peak."""
    pk = _rolling_max(inst_value, _TD_2Y)
    return _safe_div(inst_value - pk, pk)


def fsp_186_avg_position_drawdown_from_8q_peak(avg_position: pd.Series) -> pd.Series:
    """(avg_position - rolling-8Q-max) / rolling-8Q-max — drawdown from 2-year peak."""
    pk = _rolling_max(avg_position, _TD_2Y)
    return _safe_div(avg_position - pk, pk)


def fsp_187_holders_drawdown_from_8q_peak(inst_holders: pd.Series) -> pd.Series:
    """(inst_holders - rolling-8Q-max) / rolling-8Q-max — drawdown from 2-year peak."""
    pk = _rolling_max(inst_holders, _TD_2Y)
    return _safe_div(inst_holders - pk, pk)


def fsp_188_inst_pct_drawdown_from_4q_peak(inst_pct: pd.Series) -> pd.Series:
    """(inst_pct - rolling-4Q-max) / rolling-4Q-max — drawdown of ownership from 1-year peak."""
    pk = _rolling_max(inst_pct, _TD_YEAR)
    return _safe_div(inst_pct - pk, pk)


def fsp_189_decreased_pos_expanding_zscore(decreased_positions: pd.Series) -> pd.Series:
    """Expanding-window z-score of decreased positions — all-time trim breadth spike."""
    mu = decreased_positions.expanding(min_periods=4).mean()
    sigma = decreased_positions.expanding(min_periods=4).std()
    return (decreased_positions - mu) / (sigma + _EPS)


def fsp_190_increased_pos_expanding_zscore(increased_positions: pd.Series) -> pd.Series:
    """Expanding-window z-score of increased positions — collapse in buying breadth."""
    mu = increased_positions.expanding(min_periods=4).mean()
    sigma = increased_positions.expanding(min_periods=4).std()
    return (increased_positions - mu) / (sigma + _EPS)


def fsp_191_net_exit_flow_3q(closed_positions: pd.Series,
                               new_positions: pd.Series) -> pd.Series:
    """Trailing-3Q sum of (closed - new) — sustained net exit flow over 3 quarters."""
    net = closed_positions - new_positions
    return _rolling_sum(net, 3 * _TD_QTR)


def fsp_192_selling_breadth_2q_vs_8q_ratio(closed_positions: pd.Series,
                                             decreased_positions: pd.Series,
                                             inst_holders: pd.Series) -> pd.Series:
    """(Selling breadth 2Q mean) / (selling breadth 8Q mean) — short vs long norm ratio."""
    ratio = _safe_div(closed_positions + decreased_positions, inst_holders)
    return _safe_div(_rolling_mean(ratio, _TD_2Q), _rolling_mean(ratio, _TD_2Y))


def fsp_193_holder_turnover_ewm_spike(closed_positions: pd.Series,
                                       new_positions: pd.Series,
                                       inst_holders: pd.Series) -> pd.Series:
    """Holder turnover rate / EWM(span=252) of turnover — spike in churn."""
    turnover = _safe_div(closed_positions + new_positions, inst_holders)
    return _safe_div(turnover, _ewm_mean(turnover, _TD_YEAR))


def fsp_194_inst_shares_3y_rank_pct_drop_ratio(inst_shares: pd.Series,
                                                 inst_holders: pd.Series) -> pd.Series:
    """3Y rank of inst_shares_per_holder — normalized position-size collapse signal."""
    sph = _safe_div(inst_shares, inst_holders)
    return _rolling_rank_pct(sph, _TD_3Y)


def fsp_195_closed_pos_above_3std(closed_positions: pd.Series) -> pd.Series:
    """Binary: 1 if closed_positions > mean + 3*std (trailing 4Q), else 0 — extreme spike."""
    mu = _rolling_mean(closed_positions, _TD_YEAR)
    std = _rolling_std(closed_positions, _TD_YEAR)
    return (closed_positions > mu + 3 * std).astype(float)


def fsp_196_combined_selling_above_3std(closed_positions: pd.Series,
                                         decreased_positions: pd.Series) -> pd.Series:
    """Binary: 1 if (closed+decreased) > mean + 3*std (trailing 4Q)."""
    s = closed_positions + decreased_positions
    mu = _rolling_mean(s, _TD_YEAR)
    std = _rolling_std(s, _TD_YEAR)
    return (s > mu + 3 * std).astype(float)


def fsp_197_holders_below_3std(inst_holders: pd.Series) -> pd.Series:
    """Binary: 1 if holder count < mean - 3*std (trailing 4Q) — extreme holder loss."""
    mu = _rolling_mean(inst_holders, _TD_YEAR)
    std = _rolling_std(inst_holders, _TD_YEAR)
    return (inst_holders < mu - 3 * std).astype(float)


def fsp_198_inst_pct_zscore_3y(inst_pct: pd.Series) -> pd.Series:
    """Z-score of inst_pct over 3-year trailing window."""
    return _zscore_rolling(inst_pct, _TD_3Y)


def fsp_199_exodus_velocity_ewm21_zscore(inst_holders: pd.Series) -> pd.Series:
    """Z-score of EWM(span=21) of QoQ holder drop over 4Q window — smoothed velocity spike."""
    drop = inst_holders - inst_holders.shift(_TD_QTR)
    vel = _ewm_mean(drop, 21)
    return _zscore_rolling(vel, _TD_YEAR)


def fsp_200_grand_firesale_composite(closed_positions: pd.Series,
                                      decreased_positions: pd.Series,
                                      inst_holders: pd.Series,
                                      inst_shares: pd.Series,
                                      avg_position: pd.Series,
                                      inst_pct: pd.Series) -> pd.Series:
    """Grand composite: sum of 5 negative z-score dimensions + selling z-score.
    Peak when all six dimensions simultaneously signal forced liquidation."""
    z_sell = _zscore_rolling(closed_positions + decreased_positions, _TD_YEAR).clip(lower=0)
    z_h = _zscore_rolling(inst_holders, _TD_YEAR).clip(upper=0).abs()
    z_s = _zscore_rolling(inst_shares, _TD_YEAR).clip(upper=0).abs()
    z_p = _zscore_rolling(avg_position, _TD_YEAR).clip(upper=0).abs()
    z_pct = _zscore_rolling(inst_pct, _TD_YEAR).clip(upper=0).abs()
    z_br = _zscore_rolling(_safe_div(closed_positions + decreased_positions,
                                     inst_holders), _TD_YEAR).clip(lower=0)
    return z_sell + z_h + z_s + z_p + z_pct + z_br


# ===========================================================================
# Registry
# ===========================================================================

FORCED_SELLING_PROXY_REGISTRY_076_150 = {
    "fsp_076_closed_pos_3y_zscore":              {"inputs": ["closed_positions"],                                                                                       "func": fsp_076_closed_pos_3y_zscore},
    "fsp_077_combined_selling_3y_zscore":        {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_077_combined_selling_3y_zscore},
    "fsp_078_avg_position_3y_zscore":            {"inputs": ["avg_position"],                                                                                           "func": fsp_078_avg_position_3y_zscore},
    "fsp_079_inst_holders_3y_zscore":            {"inputs": ["inst_holders"],                                                                                           "func": fsp_079_inst_holders_3y_zscore},
    "fsp_080_inst_shares_3y_zscore":             {"inputs": ["inst_shares"],                                                                                            "func": fsp_080_inst_shares_3y_zscore},
    "fsp_081_inst_value_3y_zscore":              {"inputs": ["inst_value"],                                                                                             "func": fsp_081_inst_value_3y_zscore},
    "fsp_082_closed_vs_3y_max":                  {"inputs": ["closed_positions"],                                                                                       "func": fsp_082_closed_vs_3y_max},
    "fsp_083_combined_selling_vs_3y_max":        {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_083_combined_selling_vs_3y_max},
    "fsp_084_holders_vs_3y_min":                 {"inputs": ["inst_holders"],                                                                                           "func": fsp_084_holders_vs_3y_min},
    "fsp_085_avg_position_vs_3y_min":            {"inputs": ["avg_position"],                                                                                           "func": fsp_085_avg_position_vs_3y_min},
    "fsp_086_inst_shares_vs_3y_min":             {"inputs": ["inst_shares"],                                                                                            "func": fsp_086_inst_shares_vs_3y_min},
    "fsp_087_inst_value_vs_3y_min":              {"inputs": ["inst_value"],                                                                                             "func": fsp_087_inst_value_vs_3y_min},
    "fsp_088_selling_breadth_3y_rank_pct":       {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                                "func": fsp_088_selling_breadth_3y_rank_pct},
    "fsp_089_closed_breadth_3y_rank_pct":        {"inputs": ["closed_positions", "inst_holders"],                                                                       "func": fsp_089_closed_breadth_3y_rank_pct},
    "fsp_090_avg_position_3y_rank_pct":          {"inputs": ["avg_position"],                                                                                           "func": fsp_090_avg_position_3y_rank_pct},
    "fsp_091_holders_3y_rank_pct":               {"inputs": ["inst_holders"],                                                                                           "func": fsp_091_holders_3y_rank_pct},
    "fsp_092_inst_shares_3y_rank_pct":           {"inputs": ["inst_shares"],                                                                                            "func": fsp_092_inst_shares_3y_rank_pct},
    "fsp_093_sell_buy_imbalance_3y_rank_pct":    {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                        "func": fsp_093_sell_buy_imbalance_3y_rank_pct},
    "fsp_094_ewm_closed_pos_deviation":          {"inputs": ["closed_positions"],                                                                                       "func": fsp_094_ewm_closed_pos_deviation},
    "fsp_095_ewm_combined_selling_deviation":    {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_095_ewm_combined_selling_deviation},
    "fsp_096_ewm_holders_deviation":             {"inputs": ["inst_holders"],                                                                                           "func": fsp_096_ewm_holders_deviation},
    "fsp_097_ewm_avg_position_deviation":        {"inputs": ["avg_position"],                                                                                           "func": fsp_097_ewm_avg_position_deviation},
    "fsp_098_ewm_inst_shares_deviation":         {"inputs": ["inst_shares"],                                                                                            "func": fsp_098_ewm_inst_shares_deviation},
    "fsp_099_ewm_inst_value_deviation":          {"inputs": ["inst_value"],                                                                                             "func": fsp_099_ewm_inst_value_deviation},
    "fsp_100_closed_pos_expanding_zscore":       {"inputs": ["closed_positions"],                                                                                       "func": fsp_100_closed_pos_expanding_zscore},
    "fsp_101_combined_selling_expanding_zscore": {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_101_combined_selling_expanding_zscore},
    "fsp_102_avg_position_expanding_zscore":     {"inputs": ["avg_position"],                                                                                           "func": fsp_102_avg_position_expanding_zscore},
    "fsp_103_holders_expanding_zscore":          {"inputs": ["inst_holders"],                                                                                           "func": fsp_103_holders_expanding_zscore},
    "fsp_104_inst_shares_expanding_zscore":      {"inputs": ["inst_shares"],                                                                                            "func": fsp_104_inst_shares_expanding_zscore},
    "fsp_105_selling_burst_ratio_1q_vs_4q":      {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_105_selling_burst_ratio_1q_vs_4q},
    "fsp_106_closed_burst_ratio_1q_vs_8q":       {"inputs": ["closed_positions"],                                                                                       "func": fsp_106_closed_burst_ratio_1q_vs_8q},
    "fsp_107_combined_selling_burst_1q_vs_8q":   {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_107_combined_selling_burst_1q_vs_8q},
    "fsp_108_holders_drop_abs_4q_max":           {"inputs": ["inst_holders"],                                                                                           "func": fsp_108_holders_drop_abs_4q_max},
    "fsp_109_avg_position_drop_abs_4q_max":      {"inputs": ["avg_position"],                                                                                           "func": fsp_109_avg_position_drop_abs_4q_max},
    "fsp_110_inst_shares_drop_abs_4q_max":       {"inputs": ["inst_shares"],                                                                                            "func": fsp_110_inst_shares_drop_abs_4q_max},
    "fsp_111_inst_value_drop_abs_4q_max":        {"inputs": ["inst_value"],                                                                                             "func": fsp_111_inst_value_drop_abs_4q_max},
    "fsp_112_selling_breadth_ewm_spike":         {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                                "func": fsp_112_selling_breadth_ewm_spike},
    "fsp_113_closed_breadth_ewm_spike":          {"inputs": ["closed_positions", "inst_holders"],                                                                       "func": fsp_113_closed_breadth_ewm_spike},
    "fsp_114_net_selling_flow_zscore_4q":        {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],        "func": fsp_114_net_selling_flow_zscore_4q},
    "fsp_115_net_selling_flow_zscore_8q":        {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions", "inst_holders"],        "func": fsp_115_net_selling_flow_zscore_8q},
    "fsp_116_holder_turnover_rate":              {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                                       "func": fsp_116_holder_turnover_rate},
    "fsp_117_holder_turnover_zscore_4q":         {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                                       "func": fsp_117_holder_turnover_zscore_4q},
    "fsp_118_inst_shares_per_holder_zscore_4q":  {"inputs": ["inst_shares", "inst_holders"],                                                                            "func": fsp_118_inst_shares_per_holder_zscore_4q},
    "fsp_119_inst_value_per_holder_qoq_pct":     {"inputs": ["inst_value", "inst_holders"],                                                                             "func": fsp_119_inst_value_per_holder_qoq_pct},
    "fsp_120_inst_value_per_holder_zscore_4q":   {"inputs": ["inst_value", "inst_holders"],                                                                             "func": fsp_120_inst_value_per_holder_zscore_4q},
    "fsp_121_decreased_pos_zscore_4q":           {"inputs": ["decreased_positions"],                                                                                    "func": fsp_121_decreased_pos_zscore_4q},
    "fsp_122_decreased_vs_4q_max":               {"inputs": ["decreased_positions"],                                                                                    "func": fsp_122_decreased_vs_4q_max},
    "fsp_123_decreased_vs_holders_zscore":       {"inputs": ["decreased_positions", "inst_holders"],                                                                    "func": fsp_123_decreased_vs_holders_zscore},
    "fsp_124_closed_pos_3q_cumsum_zscore":       {"inputs": ["closed_positions"],                                                                                       "func": fsp_124_closed_pos_3q_cumsum_zscore},
    "fsp_125_combined_selling_3q_cumsum_zscore": {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_125_combined_selling_3q_cumsum_zscore},
    "fsp_126_holder_drop_3q_cumsum_zscore":      {"inputs": ["inst_holders"],                                                                                           "func": fsp_126_holder_drop_3q_cumsum_zscore},
    "fsp_127_avg_position_drop_3q_cumsum":       {"inputs": ["avg_position"],                                                                                           "func": fsp_127_avg_position_drop_3q_cumsum},
    "fsp_128_inst_shares_drop_3q_cumsum":        {"inputs": ["inst_shares"],                                                                                            "func": fsp_128_inst_shares_drop_3q_cumsum},
    "fsp_129_inst_value_drop_3q_cumsum":         {"inputs": ["inst_value"],                                                                                             "func": fsp_129_inst_value_drop_3q_cumsum},
    "fsp_130_inst_pct_drop_zscore_4q":           {"inputs": ["inst_pct"],                                                                                               "func": fsp_130_inst_pct_drop_zscore_4q},
    "fsp_131_selling_over_buying_surplus":       {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                        "func": fsp_131_selling_over_buying_surplus},
    "fsp_132_selling_surplus_zscore_4q":         {"inputs": ["closed_positions", "decreased_positions", "new_positions", "increased_positions"],                        "func": fsp_132_selling_surplus_zscore_4q},
    "fsp_133_closed_pos_std_spike":              {"inputs": ["closed_positions"],                                                                                       "func": fsp_133_closed_pos_std_spike},
    "fsp_134_combined_selling_std_spike":        {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_134_combined_selling_std_spike},
    "fsp_135_holders_pct_drop_zscore_4q":        {"inputs": ["inst_holders"],                                                                                           "func": fsp_135_holders_pct_drop_zscore_4q},
    "fsp_136_avg_position_drop_zscore_4q":       {"inputs": ["avg_position"],                                                                                           "func": fsp_136_avg_position_drop_zscore_4q},
    "fsp_137_inst_shares_drop_zscore_4q":        {"inputs": ["inst_shares"],                                                                                            "func": fsp_137_inst_shares_drop_zscore_4q},
    "fsp_138_inst_value_drop_zscore_4q":         {"inputs": ["inst_value"],                                                                                             "func": fsp_138_inst_value_drop_zscore_4q},
    "fsp_139_firesale_breadth_x_severity":       {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "avg_position"],                                "func": fsp_139_firesale_breadth_x_severity},
    "fsp_140_exodus_velocity":                   {"inputs": ["inst_holders"],                                                                                           "func": fsp_140_exodus_velocity},
    "fsp_141_closed_pos_above_2std":             {"inputs": ["closed_positions"],                                                                                       "func": fsp_141_closed_pos_above_2std},
    "fsp_142_combined_selling_above_2std":       {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_142_combined_selling_above_2std},
    "fsp_143_holders_below_2std":                {"inputs": ["inst_holders"],                                                                                           "func": fsp_143_holders_below_2std},
    "fsp_144_avg_position_below_2std":           {"inputs": ["avg_position"],                                                                                           "func": fsp_144_avg_position_below_2std},
    "fsp_145_liquidation_cluster_score":         {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position", "inst_pct"],     "func": fsp_145_liquidation_cluster_score},
    "fsp_146_inst_shares_drawdown_from_4q_peak": {"inputs": ["inst_shares"],                                                                                            "func": fsp_146_inst_shares_drawdown_from_4q_peak},
    "fsp_147_inst_value_drawdown_from_4q_peak":  {"inputs": ["inst_value"],                                                                                             "func": fsp_147_inst_value_drawdown_from_4q_peak},
    "fsp_148_avg_position_drawdown_from_4q_peak":{"inputs": ["avg_position"],                                                                                           "func": fsp_148_avg_position_drawdown_from_4q_peak},
    "fsp_149_holders_drawdown_from_4q_peak":     {"inputs": ["inst_holders"],                                                                                           "func": fsp_149_holders_drawdown_from_4q_peak},
    "fsp_150_abrupt_selling_index":              {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "avg_position", "inst_shares"],                 "func": fsp_150_abrupt_selling_index},
    "fsp_176_inst_pct_3q_drop":                  {"inputs": ["inst_pct"],                                                                                               "func": fsp_176_inst_pct_3q_drop},
    "fsp_177_inst_pct_3y_rank_pct":              {"inputs": ["inst_pct"],                                                                                               "func": fsp_177_inst_pct_3y_rank_pct},
    "fsp_178_inst_shares_qoq_drop_zscore_3y":    {"inputs": ["inst_shares"],                                                                                            "func": fsp_178_inst_shares_qoq_drop_zscore_3y},
    "fsp_179_inst_value_qoq_drop_zscore_3y":     {"inputs": ["inst_value"],                                                                                             "func": fsp_179_inst_value_qoq_drop_zscore_3y},
    "fsp_180_holders_qoq_drop_zscore_3y":        {"inputs": ["inst_holders"],                                                                                           "func": fsp_180_holders_qoq_drop_zscore_3y},
    "fsp_181_avg_position_qoq_drop_zscore_3y":   {"inputs": ["avg_position"],                                                                                           "func": fsp_181_avg_position_qoq_drop_zscore_3y},
    "fsp_182_closed_pos_1q_vs_3y_mean":          {"inputs": ["closed_positions"],                                                                                       "func": fsp_182_closed_pos_1q_vs_3y_mean},
    "fsp_183_combined_selling_1q_vs_3y_mean":    {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_183_combined_selling_1q_vs_3y_mean},
    "fsp_184_inst_shares_drawdown_from_8q_peak": {"inputs": ["inst_shares"],                                                                                            "func": fsp_184_inst_shares_drawdown_from_8q_peak},
    "fsp_185_inst_value_drawdown_from_8q_peak":  {"inputs": ["inst_value"],                                                                                             "func": fsp_185_inst_value_drawdown_from_8q_peak},
    "fsp_186_avg_position_drawdown_from_8q_peak":{"inputs": ["avg_position"],                                                                                           "func": fsp_186_avg_position_drawdown_from_8q_peak},
    "fsp_187_holders_drawdown_from_8q_peak":     {"inputs": ["inst_holders"],                                                                                           "func": fsp_187_holders_drawdown_from_8q_peak},
    "fsp_188_inst_pct_drawdown_from_4q_peak":    {"inputs": ["inst_pct"],                                                                                               "func": fsp_188_inst_pct_drawdown_from_4q_peak},
    "fsp_189_decreased_pos_expanding_zscore":    {"inputs": ["decreased_positions"],                                                                                    "func": fsp_189_decreased_pos_expanding_zscore},
    "fsp_190_increased_pos_expanding_zscore":    {"inputs": ["increased_positions"],                                                                                    "func": fsp_190_increased_pos_expanding_zscore},
    "fsp_191_net_exit_flow_3q":                  {"inputs": ["closed_positions", "new_positions"],                                                                      "func": fsp_191_net_exit_flow_3q},
    "fsp_192_selling_breadth_2q_vs_8q_ratio":    {"inputs": ["closed_positions", "decreased_positions", "inst_holders"],                                                "func": fsp_192_selling_breadth_2q_vs_8q_ratio},
    "fsp_193_holder_turnover_ewm_spike":         {"inputs": ["closed_positions", "new_positions", "inst_holders"],                                                      "func": fsp_193_holder_turnover_ewm_spike},
    "fsp_194_inst_shares_3y_rank_pct_drop_ratio":{"inputs": ["inst_shares", "inst_holders"],                                                                            "func": fsp_194_inst_shares_3y_rank_pct_drop_ratio},
    "fsp_195_closed_pos_above_3std":             {"inputs": ["closed_positions"],                                                                                       "func": fsp_195_closed_pos_above_3std},
    "fsp_196_combined_selling_above_3std":       {"inputs": ["closed_positions", "decreased_positions"],                                                                "func": fsp_196_combined_selling_above_3std},
    "fsp_197_holders_below_3std":                {"inputs": ["inst_holders"],                                                                                           "func": fsp_197_holders_below_3std},
    "fsp_198_inst_pct_zscore_3y":                {"inputs": ["inst_pct"],                                                                                               "func": fsp_198_inst_pct_zscore_3y},
    "fsp_199_exodus_velocity_ewm21_zscore":      {"inputs": ["inst_holders"],                                                                                           "func": fsp_199_exodus_velocity_ewm21_zscore},
    "fsp_200_grand_firesale_composite":          {"inputs": ["closed_positions", "decreased_positions", "inst_holders", "inst_shares", "avg_position", "inst_pct"],     "func": fsp_200_grand_firesale_composite},
}
