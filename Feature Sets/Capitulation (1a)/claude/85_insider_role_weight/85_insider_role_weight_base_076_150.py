"""
85_insider_role_weight — Base Features 076-200
Domain: insider role/seniority weighting — CEO/CFO vs officer vs director vs 10%-owner
Asset class: US equities | Sharadar SF2 insider transactions (daily event-aggregated)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

SF2 Daily Event-Aggregated Series Contract
-------------------------------------------
All inputs to feature functions in this file are daily-frequency pandas Series
aggregated from Sharadar SF2 insider transaction filings.  The pipeline produces
one row per (ticker, date) summing all transactions filed on that date.
IMPORTANT: these are EVENT-DRIVEN series — most days are ZERO because no filing
occurred.  Do NOT forward-fill.  Features aggregate over trailing windows using
rolling SUMS so that sparse filing days accumulate correctly.
All functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Trading-day cadence: 1 week = 5 days, 1 month = 21 days,
1 quarter = 63 days, 1 year = 252 days, 2 years = 504 days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_WEEK  = 5
_TD_MONTH = 21
_TD_QTR   = 63
_TD_HALF  = 126
_TD_YEAR  = 252
_TD_2Y    = 504
_EPS      = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Role-weighted buy value across additional windows and angles ---

def irw_076_role_weighted_buy_score_half(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over half-year (126 days): CEO/CFO=4, officer=3, director=2, 10%=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_HALF)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_HALF)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_HALF)
        + 2.0 * _rolling_sum(director_buy_value, _TD_HALF)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_HALF)
    )


def irw_077_role_weighted_buy_score_week(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1 week (5 days): CEO/CFO=4, officer=3, director=2, 10%=1."""
    return (
        4.0 * _rolling_sum(ceo_buy_value, _TD_WEEK)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_WEEK)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_WEEK)
        + 2.0 * _rolling_sum(director_buy_value, _TD_WEEK)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_WEEK)
    )


def irw_078_ceo_buy_value_1y(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of CEO buy value."""
    return _rolling_sum(ceo_buy_value, _TD_YEAR)


def irw_079_cfo_buy_value_1y(cfo_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of CFO buy value."""
    return _rolling_sum(cfo_buy_value, _TD_YEAR)


def irw_080_officer_buy_value_1y(officer_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of all-officer buy value."""
    return _rolling_sum(officer_buy_value, _TD_YEAR)


def irw_081_director_buy_value_1y(director_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of director buy value."""
    return _rolling_sum(director_buy_value, _TD_YEAR)


def irw_082_tenpct_buy_value_1y(tenpct_buy_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of 10%-owner buy value."""
    return _rolling_sum(tenpct_buy_value, _TD_YEAR)


def irw_083_officer_buy_count_1q(officer_buy_count: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of officer transaction count."""
    return _rolling_sum(officer_buy_count, _TD_QTR)


def irw_084_director_buy_count_1q(director_buy_count: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of director transaction count."""
    return _rolling_sum(director_buy_count, _TD_QTR)


def irw_085_tenpct_buy_count_1q(tenpct_buy_count: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of 10%-owner transaction count."""
    return _rolling_sum(tenpct_buy_count, _TD_QTR)


def irw_086_officer_buy_count_1y(officer_buy_count: pd.Series) -> pd.Series:
    """Rolling 1-year sum of officer transaction count."""
    return _rolling_sum(officer_buy_count, _TD_YEAR)


def irw_087_director_buy_count_1y(director_buy_count: pd.Series) -> pd.Series:
    """Rolling 1-year sum of director transaction count."""
    return _rolling_sum(director_buy_count, _TD_YEAR)


def irw_088_tenpct_buy_count_1y(tenpct_buy_count: pd.Series) -> pd.Series:
    """Rolling 1-year sum of 10%-owner transaction count."""
    return _rolling_sum(tenpct_buy_count, _TD_YEAR)


def irw_089_ceo_buy_value_2y(ceo_buy_value: pd.Series) -> pd.Series:
    """Rolling 2-year sum of CEO buy value."""
    return _rolling_sum(ceo_buy_value, _TD_2Y)


def irw_090_officer_buy_value_2y(officer_buy_value: pd.Series) -> pd.Series:
    """Rolling 2-year sum of all-officer buy value."""
    return _rolling_sum(officer_buy_value, _TD_2Y)


# --- Group G (091-105): Role-level net buy (buy minus sell) ---

def irw_091_officer_net_buy_value_1q(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net buy value (buy - sell) over 1 quarter."""
    return _rolling_sum(officer_buy_value - officer_sell_value, _TD_QTR)


def irw_092_officer_net_buy_value_1y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net buy value (buy - sell) over 1 year."""
    return _rolling_sum(officer_buy_value - officer_sell_value, _TD_YEAR)


def irw_093_director_net_buy_value_1q(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director net buy value (buy - sell) over 1 quarter."""
    return _rolling_sum(director_buy_value - director_sell_value, _TD_QTR)


def irw_094_director_net_buy_value_1y(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director net buy value (buy - sell) over 1 year."""
    return _rolling_sum(director_buy_value - director_sell_value, _TD_YEAR)


def irw_095_officer_buy_to_sell_ratio_1q(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer buy value divided by officer sell value over 1 quarter."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                     _rolling_sum(officer_sell_value, _TD_QTR))


def irw_096_director_buy_to_sell_ratio_1q(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director buy value divided by director sell value over 1 quarter."""
    return _safe_div(_rolling_sum(director_buy_value, _TD_QTR),
                     _rolling_sum(director_sell_value, _TD_QTR))


def irw_097_officer_net_buy_fraction_1q(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Officer net buy as fraction of total officer flow (buy+sell) over 1Q."""
    buy  = _rolling_sum(officer_buy_value, _TD_QTR)
    sell = _rolling_sum(officer_sell_value, _TD_QTR)
    return _safe_div(buy - sell, (buy + sell).replace(0, np.nan))


def irw_098_director_net_buy_fraction_1q(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Director net buy as fraction of total director flow over 1Q."""
    buy  = _rolling_sum(director_buy_value, _TD_QTR)
    sell = _rolling_sum(director_sell_value, _TD_QTR)
    return _safe_div(buy - sell, (buy + sell).replace(0, np.nan))


def irw_099_officer_net_buy_zscore_1y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Z-score of officer daily net buy value within a trailing 1-year window."""
    net = officer_buy_value - officer_sell_value
    return _zscore_rolling(net, _TD_YEAR)


def irw_100_director_net_buy_zscore_1y(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Z-score of director daily net buy value within a trailing 1-year window."""
    net = director_buy_value - director_sell_value
    return _zscore_rolling(net, _TD_YEAR)


def irw_101_officer_sell_value_1q(officer_sell_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of officer sell value (supply-side role signal)."""
    return _rolling_sum(officer_sell_value, _TD_QTR)


def irw_102_director_sell_value_1q(director_sell_value: pd.Series) -> pd.Series:
    """Rolling 1-quarter sum of director sell value."""
    return _rolling_sum(director_sell_value, _TD_QTR)


def irw_103_officer_net_buy_positive_flag_1q(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if net officer buying (buy > sell) over trailing 1 quarter."""
    net = _rolling_sum(officer_buy_value - officer_sell_value, _TD_QTR)
    return (net > 0).astype(float)


def irw_104_director_net_buy_positive_flag_1q(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if net director buying (buy > sell) over trailing 1 quarter."""
    net = _rolling_sum(director_buy_value - director_sell_value, _TD_QTR)
    return (net > 0).astype(float)


def irw_105_officer_and_director_net_buy_both_1q(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if both officers AND directors show net buying over 1Q."""
    off_net = _rolling_sum(officer_buy_value - officer_sell_value, _TD_QTR)
    dir_net = _rolling_sum(director_buy_value - director_sell_value, _TD_QTR)
    return ((off_net > 0) & (dir_net > 0)).astype(float)


# --- Group H (106-120): Expanding and long-horizon role seniority features ---

def irw_106_top_officer_value_share_expanding(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Expanding share of all-time insider buy value attributable to CEO + CFO."""
    num = (ceo_buy_value + cfo_buy_value).expanding(min_periods=1).sum()
    den = insider_buy_value.expanding(min_periods=1).sum()
    return _safe_div(num, den)


def irw_107_officer_value_share_expanding(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Expanding share of all-time insider buy value from officers."""
    num = officer_buy_value.expanding(min_periods=1).sum()
    den = insider_buy_value.expanding(min_periods=1).sum()
    return _safe_div(num, den)


def irw_108_seniority_conviction_expanding(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Expanding all-time seniority conviction index (weighted share of total buy value)."""
    num = (
        1.0 * ceo_buy_value + 0.9 * cfo_buy_value + 0.6 * officer_buy_value
        + 0.4 * director_buy_value + 0.2 * tenpct_buy_value
    ).expanding(min_periods=1).sum()
    den = insider_buy_value.expanding(min_periods=1).sum()
    return _safe_div(num, den)


def irw_109_ceo_buy_value_expanding_max(ceo_buy_value: pd.Series) -> pd.Series:
    """Expanding maximum of rolling-1Q CEO buy value — all-time peak CEO buying intensity."""
    roll = _rolling_sum(ceo_buy_value, _TD_QTR)
    return roll.expanding(min_periods=1).max()


def irw_110_top_officer_value_pct_rank_expanding(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Expanding percentile rank of the daily CEO+CFO buy value (how extreme is today's buy)."""
    combined = ceo_buy_value + cfo_buy_value
    return combined.expanding(min_periods=2).rank(pct=True)


def irw_111_officer_buy_value_pct_rank_expanding(officer_buy_value: pd.Series) -> pd.Series:
    """Expanding percentile rank of the daily officer buy value."""
    return officer_buy_value.expanding(min_periods=2).rank(pct=True)


def irw_112_seniority_conviction_pct_rank_expanding(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Expanding percentile rank of the daily seniority conviction score."""
    daily_sci = _safe_div(
        1.0 * ceo_buy_value + 0.9 * cfo_buy_value + 0.6 * officer_buy_value
        + 0.4 * director_buy_value + 0.2 * tenpct_buy_value,
        insider_buy_value
    ).fillna(0.0)
    return daily_sci.expanding(min_periods=2).rank(pct=True)


def irw_113_role_weighted_score_expanding_zscore(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Expanding z-score of the daily role-weighted buy score."""
    score = (
        4.0 * ceo_buy_value + 4.0 * cfo_buy_value + 3.0 * officer_buy_value
        + 2.0 * director_buy_value + 1.0 * tenpct_buy_value
    )
    m  = score.expanding(min_periods=2).mean()
    sd = score.expanding(min_periods=2).std()
    return _safe_div(score - m, sd)


def irw_114_director_buy_value_2y(director_buy_value: pd.Series) -> pd.Series:
    """Rolling 2-year sum of director buy value."""
    return _rolling_sum(director_buy_value, _TD_2Y)


def irw_115_tenpct_buy_value_2y(tenpct_buy_value: pd.Series) -> pd.Series:
    """Rolling 2-year sum of 10%-owner buy value."""
    return _rolling_sum(tenpct_buy_value, _TD_2Y)


def irw_116_officer_buy_count_2y(officer_buy_count: pd.Series) -> pd.Series:
    """Rolling 2-year sum of officer buy count."""
    return _rolling_sum(officer_buy_count, _TD_2Y)


def irw_117_director_buy_count_2y(director_buy_count: pd.Series) -> pd.Series:
    """Rolling 2-year sum of director buy count."""
    return _rolling_sum(director_buy_count, _TD_2Y)


def irw_118_tenpct_buy_count_2y(tenpct_buy_count: pd.Series) -> pd.Series:
    """Rolling 2-year sum of 10%-owner buy count."""
    return _rolling_sum(tenpct_buy_count, _TD_2Y)


def irw_119_role_weighted_buy_score_normalized_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over 1Y divided by total insider buy value (normalized)."""
    num = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_YEAR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_YEAR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_YEAR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_YEAR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_YEAR)
    )
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    return _safe_div(num, den)


def irw_120_officer_to_director_value_ratio_2y(
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
) -> pd.Series:
    """Ratio of officer buy value to director buy value over 2 years."""
    return _safe_div(_rolling_sum(officer_buy_value, _TD_2Y),
                     _rolling_sum(director_buy_value, _TD_2Y))


# --- Group I (121-135): Momentum / recent-vs-prior role shift ---

def irw_121_top_officer_share_1q_vs_prior_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in top-officer value share: current 1Q minus prior 1Q (1Q ago)."""
    top_curr = _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR),
                         _rolling_sum(insider_buy_value, _TD_QTR))
    top_prior = top_curr.shift(_TD_QTR)
    return top_curr - top_prior


def irw_122_officer_share_1q_vs_prior_1q(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in officer value share: current 1Q minus prior 1Q."""
    share = _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR))
    return share - share.shift(_TD_QTR)


def irw_123_director_share_1q_vs_prior_1q(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in director value share: current 1Q minus prior 1Q."""
    share = _safe_div(_rolling_sum(director_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR))
    return share - share.shift(_TD_QTR)


def irw_124_seniority_conviction_1q_vs_prior_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in 1Q seniority conviction index vs prior quarter (momentum)."""
    num = (
        1.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 0.9 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 0.6 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 0.4 * _rolling_sum(director_buy_value, _TD_QTR)
        + 0.2 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    sci = _safe_div(num, den)
    return sci - sci.shift(_TD_QTR)


def irw_125_role_weighted_score_1q_vs_prior_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Change in 1Q role-weighted buy score vs prior quarter."""
    score = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_QTR)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_QTR)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_QTR)
        + 2.0 * _rolling_sum(director_buy_value, _TD_QTR)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_QTR)
    )
    return score - score.shift(_TD_QTR)


def irw_126_ceo_buy_value_1q_vs_prior_1q(ceo_buy_value: pd.Series) -> pd.Series:
    """Change in CEO buy value: current 1Q minus prior 1Q."""
    roll = _rolling_sum(ceo_buy_value, _TD_QTR)
    return roll - roll.shift(_TD_QTR)


def irw_127_cfo_buy_value_1q_vs_prior_1q(cfo_buy_value: pd.Series) -> pd.Series:
    """Change in CFO buy value: current 1Q minus prior 1Q."""
    roll = _rolling_sum(cfo_buy_value, _TD_QTR)
    return roll - roll.shift(_TD_QTR)


def irw_128_officer_buy_value_1q_vs_prior_1q(officer_buy_value: pd.Series) -> pd.Series:
    """Change in officer buy value: current 1Q minus prior 1Q."""
    roll = _rolling_sum(officer_buy_value, _TD_QTR)
    return roll - roll.shift(_TD_QTR)


def irw_129_director_buy_value_1q_vs_prior_1q(director_buy_value: pd.Series) -> pd.Series:
    """Change in director buy value: current 1Q minus prior 1Q."""
    roll = _rolling_sum(director_buy_value, _TD_QTR)
    return roll - roll.shift(_TD_QTR)


def irw_130_tenpct_buy_value_1q_vs_prior_1q(tenpct_buy_value: pd.Series) -> pd.Series:
    """Change in 10%-owner buy value: current 1Q minus prior 1Q."""
    roll = _rolling_sum(tenpct_buy_value, _TD_QTR)
    return roll - roll.shift(_TD_QTR)


def irw_131_top_officer_share_1y_vs_prior_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in top-officer value share: current 1Y minus prior 1Y."""
    share = _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_YEAR),
                      _rolling_sum(insider_buy_value, _TD_YEAR))
    return share - share.shift(_TD_YEAR)


def irw_132_officer_share_1y_vs_prior_1y(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in officer value share: current 1Y minus prior 1Y."""
    share = _safe_div(_rolling_sum(officer_buy_value, _TD_YEAR),
                      _rolling_sum(insider_buy_value, _TD_YEAR))
    return share - share.shift(_TD_YEAR)


def irw_133_director_share_1y_vs_prior_1y(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Change in director value share: current 1Y minus prior 1Y."""
    share = _safe_div(_rolling_sum(director_buy_value, _TD_YEAR),
                      _rolling_sum(insider_buy_value, _TD_YEAR))
    return share - share.shift(_TD_YEAR)


def irw_134_ceo_buy_value_1y_vs_prior_1y(ceo_buy_value: pd.Series) -> pd.Series:
    """Change in CEO buy value: current 1Y minus prior 1Y."""
    roll = _rolling_sum(ceo_buy_value, _TD_YEAR)
    return roll - roll.shift(_TD_YEAR)


def irw_135_role_weighted_score_ewm_deviation(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
) -> pd.Series:
    """Daily role-weighted buy score minus its EWM (span=63): deviation from short-term trend."""
    score = (
        4.0 * ceo_buy_value + 4.0 * cfo_buy_value + 3.0 * officer_buy_value
        + 2.0 * director_buy_value + 1.0 * tenpct_buy_value
    )
    return score - _ewm_mean(score, _TD_QTR)


# --- Group J (136-150): Additional conviction, concentration and composite ---

def irw_136_officer_active_days_ratio_1q(
    officer_buy_count: pd.Series,
) -> pd.Series:
    """Fraction of 1Q days on which any officer buy was filed (filing frequency)."""
    indicator = (officer_buy_count > 0).astype(float)
    return _rolling_sum(indicator, _TD_QTR) / _TD_QTR


def irw_137_director_active_days_ratio_1q(
    director_buy_count: pd.Series,
) -> pd.Series:
    """Fraction of 1Q days on which any director buy was filed."""
    indicator = (director_buy_count > 0).astype(float)
    return _rolling_sum(indicator, _TD_QTR) / _TD_QTR


def irw_138_tenpct_active_days_ratio_1q(
    tenpct_buy_count: pd.Series,
) -> pd.Series:
    """Fraction of 1Q days on which any 10%-owner buy was filed."""
    indicator = (tenpct_buy_count > 0).astype(float)
    return _rolling_sum(indicator, _TD_QTR) / _TD_QTR


def irw_139_officer_active_days_ratio_1y(
    officer_buy_count: pd.Series,
) -> pd.Series:
    """Fraction of 1-year days on which any officer buy was filed."""
    indicator = (officer_buy_count > 0).astype(float)
    return _rolling_sum(indicator, _TD_YEAR) / _TD_YEAR


def irw_140_top_officer_buy_streak_days(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """
    Count of consecutive calendar days (within trailing 1Q window) where some CEO or CFO
    buy activity has been observed — proxied by rolling sum of daily binary indicator.
    """
    indicator = ((ceo_buy_value + cfo_buy_value) > 0).astype(float)
    return _rolling_sum(indicator, _TD_QTR)


def irw_141_officer_vs_tenpct_share_diff_1q(
    officer_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Officer value share minus 10%-owner value share over 1Q (relative seniority lean)."""
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    off_share = _safe_div(_rolling_sum(officer_buy_value, _TD_QTR), den)
    ten_share = _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), den)
    return off_share.fillna(0.0) - ten_share.fillna(0.0)


def irw_142_director_vs_tenpct_share_diff_1q(
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Director value share minus 10%-owner value share over 1Q."""
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    dir_share = _safe_div(_rolling_sum(director_buy_value, _TD_QTR), den)
    ten_share = _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), den)
    return dir_share.fillna(0.0) - ten_share.fillna(0.0)


def irw_143_weighted_role_herfindahl_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Herfindahl-like role concentration: sum of squared value shares over 1Q.
    High values = buying dominated by one role class.
    """
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    s_ceo = _safe_div(_rolling_sum(ceo_buy_value, _TD_QTR), den).fillna(0.0)
    s_cfo = _safe_div(_rolling_sum(cfo_buy_value, _TD_QTR), den).fillna(0.0)
    s_off = _safe_div(_rolling_sum(officer_buy_value, _TD_QTR), den).fillna(0.0)
    s_dir = _safe_div(_rolling_sum(director_buy_value, _TD_QTR), den).fillna(0.0)
    s_ten = _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), den).fillna(0.0)
    return s_ceo**2 + s_cfo**2 + s_off**2 + s_dir**2 + s_ten**2


def irw_144_role_diversity_index_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Role diversity: 1 - Herfindahl. High values = buying spread across multiple role classes.
    """
    den = _rolling_sum(insider_buy_value, _TD_QTR)
    s_ceo = _safe_div(_rolling_sum(ceo_buy_value, _TD_QTR), den).fillna(0.0)
    s_cfo = _safe_div(_rolling_sum(cfo_buy_value, _TD_QTR), den).fillna(0.0)
    s_off = _safe_div(_rolling_sum(officer_buy_value, _TD_QTR), den).fillna(0.0)
    s_dir = _safe_div(_rolling_sum(director_buy_value, _TD_QTR), den).fillna(0.0)
    s_ten = _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR), den).fillna(0.0)
    herf = s_ceo**2 + s_cfo**2 + s_off**2 + s_dir**2 + s_ten**2
    return 1.0 - herf


def irw_145_top_two_roles_dominate_flag_1q(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if CEO+CFO together account for >50% of 1Q insider buy value."""
    share = _safe_div(_rolling_sum(ceo_buy_value + cfo_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR)).fillna(0.0)
    return (share > 0.5).astype(float)


def irw_146_officer_dominated_flag_1q(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if officers (all) account for >50% of 1Q insider buy value."""
    share = _safe_div(_rolling_sum(officer_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR)).fillna(0.0)
    return (share > 0.5).astype(float)


def irw_147_director_dominated_flag_1q(
    director_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if directors account for >50% of 1Q insider buy value."""
    share = _safe_div(_rolling_sum(director_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR)).fillna(0.0)
    return (share > 0.5).astype(float)


def irw_148_tenpct_dominated_flag_1q(
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if 10%-owners account for >50% of 1Q insider buy value."""
    share = _safe_div(_rolling_sum(tenpct_buy_value, _TD_QTR),
                      _rolling_sum(insider_buy_value, _TD_QTR)).fillna(0.0)
    return (share > 0.5).astype(float)


def irw_149_role_weighted_buy_score_half_normalized(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Role-weighted buy score over half year divided by total insider buy value."""
    num = (
        4.0 * _rolling_sum(ceo_buy_value, _TD_HALF)
        + 4.0 * _rolling_sum(cfo_buy_value, _TD_HALF)
        + 3.0 * _rolling_sum(officer_buy_value, _TD_HALF)
        + 2.0 * _rolling_sum(director_buy_value, _TD_HALF)
        + 1.0 * _rolling_sum(tenpct_buy_value, _TD_HALF)
    )
    den = _rolling_sum(insider_buy_value, _TD_HALF)
    return _safe_div(num, den)


def irw_150_composite_role_conviction_all_windows(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Composite role conviction across windows: equally weighted average of
    1M, 1Q, and 1Y seniority conviction indices.
    Captures consistent senior-buyer presence across time horizons.
    """
    def _sci(w: int) -> pd.Series:
        num = (
            1.0 * _rolling_sum(ceo_buy_value, w)
            + 0.9 * _rolling_sum(cfo_buy_value, w)
            + 0.6 * _rolling_sum(officer_buy_value, w)
            + 0.4 * _rolling_sum(director_buy_value, w)
            + 0.2 * _rolling_sum(tenpct_buy_value, w)
        )
        den = _rolling_sum(insider_buy_value, w)
        return _safe_div(num, den).fillna(0.0)

    return (_sci(_TD_MONTH) + _sci(_TD_QTR) + _sci(_TD_YEAR)) / 3.0


# --- Group K (176-200): Advanced cross-role, EWM variants, concentration, composite ---

def irw_176_ceo_cfo_zscore_2y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
) -> pd.Series:
    """Z-score of combined CEO+CFO buy value within trailing 2-year window."""
    return _zscore_rolling(ceo_buy_value + cfo_buy_value, _TD_2Y)


def irw_177_officer_net_buy_zscore_2y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Z-score of officer daily net buy value within trailing 2-year window."""
    return _zscore_rolling(officer_buy_value - officer_sell_value, _TD_2Y)


def irw_178_director_net_buy_zscore_2y(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Z-score of director daily net buy value within trailing 2-year window."""
    return _zscore_rolling(director_buy_value - director_sell_value, _TD_2Y)


def irw_179_officer_sell_value_1y(officer_sell_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of officer sell value."""
    return _rolling_sum(officer_sell_value, _TD_YEAR)


def irw_180_director_sell_value_1y(director_sell_value: pd.Series) -> pd.Series:
    """Rolling 1-year sum of director sell value."""
    return _rolling_sum(director_sell_value, _TD_YEAR)


def irw_181_officer_sell_value_half(officer_sell_value: pd.Series) -> pd.Series:
    """Rolling half-year sum of officer sell value."""
    return _rolling_sum(officer_sell_value, _TD_HALF)


def irw_182_director_sell_value_half(director_sell_value: pd.Series) -> pd.Series:
    """Rolling half-year sum of director sell value."""
    return _rolling_sum(director_sell_value, _TD_HALF)


def irw_183_officer_net_buy_positive_flag_1y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if net officer buying over trailing 1 year."""
    return (_rolling_sum(officer_buy_value - officer_sell_value, _TD_YEAR) > 0).astype(float)


def irw_184_director_net_buy_positive_flag_1y(
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if net director buying over trailing 1 year."""
    return (_rolling_sum(director_buy_value - director_sell_value, _TD_YEAR) > 0).astype(float)


def irw_185_tenpct_value_share_half(
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of half-year insider buy value from 10%-owners."""
    return _safe_div(_rolling_sum(tenpct_buy_value, _TD_HALF),
                     _rolling_sum(insider_buy_value, _TD_HALF))


def irw_186_ceo_buy_active_days_1y(ceo_buy_value: pd.Series) -> pd.Series:
    """Count of days with any CEO buy filing in trailing 1 year."""
    return _rolling_sum((ceo_buy_value > 0).astype(float), _TD_YEAR)


def irw_187_officer_active_days_1y(officer_buy_value: pd.Series) -> pd.Series:
    """Count of days with any officer buy filing in trailing 1 year."""
    return _rolling_sum((officer_buy_value > 0).astype(float), _TD_YEAR)


def irw_188_director_active_days_1y(director_buy_value: pd.Series) -> pd.Series:
    """Count of days with any director buy filing in trailing 1 year."""
    return _rolling_sum((director_buy_value > 0).astype(float), _TD_YEAR)


def irw_189_tenpct_active_days_1y(tenpct_buy_value: pd.Series) -> pd.Series:
    """Count of days with any 10%-owner buy filing in trailing 1 year."""
    return _rolling_sum((tenpct_buy_value > 0).astype(float), _TD_YEAR)


def irw_190_officer_share_ewm_1y(
    officer_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=252) of the daily officer buy value share."""
    daily = _safe_div(officer_buy_value, insider_buy_value).fillna(0.0)
    return _ewm_mean(daily, _TD_YEAR)


def irw_191_top_officer_share_ewm_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """EWM (span=252) of the daily CEO+CFO buy value share."""
    daily = _safe_div(ceo_buy_value + cfo_buy_value, insider_buy_value).fillna(0.0)
    return _ewm_mean(daily, _TD_YEAR)


def irw_192_weighted_role_herfindahl_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Herfindahl-like role concentration (sum of squared value shares) over 1 year."""
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    s = [_safe_div(_rolling_sum(v, _TD_YEAR), den).fillna(0.0)
         for v in (ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)]
    return s[0]**2 + s[1]**2 + s[2]**2 + s[3]**2 + s[4]**2


def irw_193_role_diversity_index_1y(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Role diversity (1 - Herfindahl) over 1 year."""
    den = _rolling_sum(insider_buy_value, _TD_YEAR)
    s = [_safe_div(_rolling_sum(v, _TD_YEAR), den).fillna(0.0)
         for v in (ceo_buy_value, cfo_buy_value, officer_buy_value, director_buy_value, tenpct_buy_value)]
    return 1.0 - (s[0]**2 + s[1]**2 + s[2]**2 + s[3]**2 + s[4]**2)


def irw_194_ceo_value_share_1y(
    ceo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value from CEO alone."""
    return _safe_div(_rolling_sum(ceo_buy_value, _TD_YEAR),
                     _rolling_sum(insider_buy_value, _TD_YEAR))


def irw_195_cfo_value_share_1y(
    cfo_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """Share of 1-year insider buy value from CFO alone."""
    return _safe_div(_rolling_sum(cfo_buy_value, _TD_YEAR),
                     _rolling_sum(insider_buy_value, _TD_YEAR))


def irw_196_officer_and_director_net_buy_both_1y(
    officer_buy_value: pd.Series,
    officer_sell_value: pd.Series,
    director_buy_value: pd.Series,
    director_sell_value: pd.Series,
) -> pd.Series:
    """Binary: 1 if both officers AND directors show net buying over 1 year."""
    off_net = _rolling_sum(officer_buy_value - officer_sell_value, _TD_YEAR)
    dir_net = _rolling_sum(director_buy_value - director_sell_value, _TD_YEAR)
    return ((off_net > 0) & (dir_net > 0)).astype(float)


def irw_197_tenpct_buy_count_half(tenpct_buy_count: pd.Series) -> pd.Series:
    """Rolling half-year sum of 10%-owner buy count."""
    return _rolling_sum(tenpct_buy_count, _TD_HALF)


def irw_198_officer_buy_count_half(officer_buy_count: pd.Series) -> pd.Series:
    """Rolling half-year sum of officer buy count."""
    return _rolling_sum(officer_buy_count, _TD_HALF)


def irw_199_director_buy_count_half(director_buy_count: pd.Series) -> pd.Series:
    """Rolling half-year sum of director buy count."""
    return _rolling_sum(director_buy_count, _TD_HALF)


def irw_200_composite_role_conviction_weighted(
    ceo_buy_value: pd.Series,
    cfo_buy_value: pd.Series,
    officer_buy_value: pd.Series,
    director_buy_value: pd.Series,
    tenpct_buy_value: pd.Series,
    insider_buy_value: pd.Series,
) -> pd.Series:
    """
    Composite role conviction: weighted avg of 1Q (wt=0.5), half (wt=0.3), 1Y (wt=0.2) SCI.
    Emphasises recent seniority signal while anchoring to longer horizon.
    """
    def _sci(w: int) -> pd.Series:
        num = (
            1.0 * _rolling_sum(ceo_buy_value, w)
            + 0.9 * _rolling_sum(cfo_buy_value, w)
            + 0.6 * _rolling_sum(officer_buy_value, w)
            + 0.4 * _rolling_sum(director_buy_value, w)
            + 0.2 * _rolling_sum(tenpct_buy_value, w)
        )
        return _safe_div(num, _rolling_sum(insider_buy_value, w)).fillna(0.0)
    return 0.5 * _sci(_TD_QTR) + 0.3 * _sci(_TD_HALF) + 0.2 * _sci(_TD_YEAR)


# ── Registry 076-150 ──────────────────────────────────────────────────────────

INSIDER_ROLE_WEIGHT_REGISTRY_076_150 = {
    "irw_076_role_weighted_buy_score_half": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_076_role_weighted_buy_score_half,
    },
    "irw_077_role_weighted_buy_score_week": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_077_role_weighted_buy_score_week,
    },
    "irw_078_ceo_buy_value_1y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_078_ceo_buy_value_1y,
    },
    "irw_079_cfo_buy_value_1y": {
        "inputs": ["cfo_buy_value"],
        "func": irw_079_cfo_buy_value_1y,
    },
    "irw_080_officer_buy_value_1y": {
        "inputs": ["officer_buy_value"],
        "func": irw_080_officer_buy_value_1y,
    },
    "irw_081_director_buy_value_1y": {
        "inputs": ["director_buy_value"],
        "func": irw_081_director_buy_value_1y,
    },
    "irw_082_tenpct_buy_value_1y": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_082_tenpct_buy_value_1y,
    },
    "irw_083_officer_buy_count_1q": {
        "inputs": ["officer_buy_count"],
        "func": irw_083_officer_buy_count_1q,
    },
    "irw_084_director_buy_count_1q": {
        "inputs": ["director_buy_count"],
        "func": irw_084_director_buy_count_1q,
    },
    "irw_085_tenpct_buy_count_1q": {
        "inputs": ["tenpct_buy_count"],
        "func": irw_085_tenpct_buy_count_1q,
    },
    "irw_086_officer_buy_count_1y": {
        "inputs": ["officer_buy_count"],
        "func": irw_086_officer_buy_count_1y,
    },
    "irw_087_director_buy_count_1y": {
        "inputs": ["director_buy_count"],
        "func": irw_087_director_buy_count_1y,
    },
    "irw_088_tenpct_buy_count_1y": {
        "inputs": ["tenpct_buy_count"],
        "func": irw_088_tenpct_buy_count_1y,
    },
    "irw_089_ceo_buy_value_2y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_089_ceo_buy_value_2y,
    },
    "irw_090_officer_buy_value_2y": {
        "inputs": ["officer_buy_value"],
        "func": irw_090_officer_buy_value_2y,
    },
    "irw_091_officer_net_buy_value_1q": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_091_officer_net_buy_value_1q,
    },
    "irw_092_officer_net_buy_value_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_092_officer_net_buy_value_1y,
    },
    "irw_093_director_net_buy_value_1q": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_093_director_net_buy_value_1q,
    },
    "irw_094_director_net_buy_value_1y": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_094_director_net_buy_value_1y,
    },
    "irw_095_officer_buy_to_sell_ratio_1q": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_095_officer_buy_to_sell_ratio_1q,
    },
    "irw_096_director_buy_to_sell_ratio_1q": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_096_director_buy_to_sell_ratio_1q,
    },
    "irw_097_officer_net_buy_fraction_1q": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_097_officer_net_buy_fraction_1q,
    },
    "irw_098_director_net_buy_fraction_1q": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_098_director_net_buy_fraction_1q,
    },
    "irw_099_officer_net_buy_zscore_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_099_officer_net_buy_zscore_1y,
    },
    "irw_100_director_net_buy_zscore_1y": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_100_director_net_buy_zscore_1y,
    },
    "irw_101_officer_sell_value_1q": {
        "inputs": ["officer_sell_value"],
        "func": irw_101_officer_sell_value_1q,
    },
    "irw_102_director_sell_value_1q": {
        "inputs": ["director_sell_value"],
        "func": irw_102_director_sell_value_1q,
    },
    "irw_103_officer_net_buy_positive_flag_1q": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_103_officer_net_buy_positive_flag_1q,
    },
    "irw_104_director_net_buy_positive_flag_1q": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_104_director_net_buy_positive_flag_1q,
    },
    "irw_105_officer_and_director_net_buy_both_1q": {
        "inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"],
        "func": irw_105_officer_and_director_net_buy_both_1q,
    },
    "irw_106_top_officer_value_share_expanding": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_106_top_officer_value_share_expanding,
    },
    "irw_107_officer_value_share_expanding": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_107_officer_value_share_expanding,
    },
    "irw_108_seniority_conviction_expanding": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_108_seniority_conviction_expanding,
    },
    "irw_109_ceo_buy_value_expanding_max": {
        "inputs": ["ceo_buy_value"],
        "func": irw_109_ceo_buy_value_expanding_max,
    },
    "irw_110_top_officer_value_pct_rank_expanding": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_110_top_officer_value_pct_rank_expanding,
    },
    "irw_111_officer_buy_value_pct_rank_expanding": {
        "inputs": ["officer_buy_value"],
        "func": irw_111_officer_buy_value_pct_rank_expanding,
    },
    "irw_112_seniority_conviction_pct_rank_expanding": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_112_seniority_conviction_pct_rank_expanding,
    },
    "irw_113_role_weighted_score_expanding_zscore": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_113_role_weighted_score_expanding_zscore,
    },
    "irw_114_director_buy_value_2y": {
        "inputs": ["director_buy_value"],
        "func": irw_114_director_buy_value_2y,
    },
    "irw_115_tenpct_buy_value_2y": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_115_tenpct_buy_value_2y,
    },
    "irw_116_officer_buy_count_2y": {
        "inputs": ["officer_buy_count"],
        "func": irw_116_officer_buy_count_2y,
    },
    "irw_117_director_buy_count_2y": {
        "inputs": ["director_buy_count"],
        "func": irw_117_director_buy_count_2y,
    },
    "irw_118_tenpct_buy_count_2y": {
        "inputs": ["tenpct_buy_count"],
        "func": irw_118_tenpct_buy_count_2y,
    },
    "irw_119_role_weighted_buy_score_normalized_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_119_role_weighted_buy_score_normalized_1y,
    },
    "irw_120_officer_to_director_value_ratio_2y": {
        "inputs": ["officer_buy_value", "director_buy_value"],
        "func": irw_120_officer_to_director_value_ratio_2y,
    },
    "irw_121_top_officer_share_1q_vs_prior_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_121_top_officer_share_1q_vs_prior_1q,
    },
    "irw_122_officer_share_1q_vs_prior_1q": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_122_officer_share_1q_vs_prior_1q,
    },
    "irw_123_director_share_1q_vs_prior_1q": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_123_director_share_1q_vs_prior_1q,
    },
    "irw_124_seniority_conviction_1q_vs_prior_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_124_seniority_conviction_1q_vs_prior_1q,
    },
    "irw_125_role_weighted_score_1q_vs_prior_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_125_role_weighted_score_1q_vs_prior_1q,
    },
    "irw_126_ceo_buy_value_1q_vs_prior_1q": {
        "inputs": ["ceo_buy_value"],
        "func": irw_126_ceo_buy_value_1q_vs_prior_1q,
    },
    "irw_127_cfo_buy_value_1q_vs_prior_1q": {
        "inputs": ["cfo_buy_value"],
        "func": irw_127_cfo_buy_value_1q_vs_prior_1q,
    },
    "irw_128_officer_buy_value_1q_vs_prior_1q": {
        "inputs": ["officer_buy_value"],
        "func": irw_128_officer_buy_value_1q_vs_prior_1q,
    },
    "irw_129_director_buy_value_1q_vs_prior_1q": {
        "inputs": ["director_buy_value"],
        "func": irw_129_director_buy_value_1q_vs_prior_1q,
    },
    "irw_130_tenpct_buy_value_1q_vs_prior_1q": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_130_tenpct_buy_value_1q_vs_prior_1q,
    },
    "irw_131_top_officer_share_1y_vs_prior_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_131_top_officer_share_1y_vs_prior_1y,
    },
    "irw_132_officer_share_1y_vs_prior_1y": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_132_officer_share_1y_vs_prior_1y,
    },
    "irw_133_director_share_1y_vs_prior_1y": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_133_director_share_1y_vs_prior_1y,
    },
    "irw_134_ceo_buy_value_1y_vs_prior_1y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_134_ceo_buy_value_1y_vs_prior_1y,
    },
    "irw_135_role_weighted_score_ewm_deviation": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value"],
        "func": irw_135_role_weighted_score_ewm_deviation,
    },
    "irw_136_officer_active_days_ratio_1q": {
        "inputs": ["officer_buy_count"],
        "func": irw_136_officer_active_days_ratio_1q,
    },
    "irw_137_director_active_days_ratio_1q": {
        "inputs": ["director_buy_count"],
        "func": irw_137_director_active_days_ratio_1q,
    },
    "irw_138_tenpct_active_days_ratio_1q": {
        "inputs": ["tenpct_buy_count"],
        "func": irw_138_tenpct_active_days_ratio_1q,
    },
    "irw_139_officer_active_days_ratio_1y": {
        "inputs": ["officer_buy_count"],
        "func": irw_139_officer_active_days_ratio_1y,
    },
    "irw_140_top_officer_buy_streak_days": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_140_top_officer_buy_streak_days,
    },
    "irw_141_officer_vs_tenpct_share_diff_1q": {
        "inputs": ["officer_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_141_officer_vs_tenpct_share_diff_1q,
    },
    "irw_142_director_vs_tenpct_share_diff_1q": {
        "inputs": ["director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_142_director_vs_tenpct_share_diff_1q,
    },
    "irw_143_weighted_role_herfindahl_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_143_weighted_role_herfindahl_1q,
    },
    "irw_144_role_diversity_index_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_144_role_diversity_index_1q,
    },
    "irw_145_top_two_roles_dominate_flag_1q": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_145_top_two_roles_dominate_flag_1q,
    },
    "irw_146_officer_dominated_flag_1q": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_146_officer_dominated_flag_1q,
    },
    "irw_147_director_dominated_flag_1q": {
        "inputs": ["director_buy_value", "insider_buy_value"],
        "func": irw_147_director_dominated_flag_1q,
    },
    "irw_148_tenpct_dominated_flag_1q": {
        "inputs": ["tenpct_buy_value", "insider_buy_value"],
        "func": irw_148_tenpct_dominated_flag_1q,
    },
    "irw_149_role_weighted_buy_score_half_normalized": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_149_role_weighted_buy_score_half_normalized,
    },
    "irw_150_composite_role_conviction_all_windows": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_150_composite_role_conviction_all_windows,
    },
    "irw_176_ceo_cfo_zscore_2y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value"],
        "func": irw_176_ceo_cfo_zscore_2y,
    },
    "irw_177_officer_net_buy_zscore_2y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_177_officer_net_buy_zscore_2y,
    },
    "irw_178_director_net_buy_zscore_2y": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_178_director_net_buy_zscore_2y,
    },
    "irw_179_officer_sell_value_1y": {
        "inputs": ["officer_sell_value"],
        "func": irw_179_officer_sell_value_1y,
    },
    "irw_180_director_sell_value_1y": {
        "inputs": ["director_sell_value"],
        "func": irw_180_director_sell_value_1y,
    },
    "irw_181_officer_sell_value_half": {
        "inputs": ["officer_sell_value"],
        "func": irw_181_officer_sell_value_half,
    },
    "irw_182_director_sell_value_half": {
        "inputs": ["director_sell_value"],
        "func": irw_182_director_sell_value_half,
    },
    "irw_183_officer_net_buy_positive_flag_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value"],
        "func": irw_183_officer_net_buy_positive_flag_1y,
    },
    "irw_184_director_net_buy_positive_flag_1y": {
        "inputs": ["director_buy_value", "director_sell_value"],
        "func": irw_184_director_net_buy_positive_flag_1y,
    },
    "irw_185_tenpct_value_share_half": {
        "inputs": ["tenpct_buy_value", "insider_buy_value"],
        "func": irw_185_tenpct_value_share_half,
    },
    "irw_186_ceo_buy_active_days_1y": {
        "inputs": ["ceo_buy_value"],
        "func": irw_186_ceo_buy_active_days_1y,
    },
    "irw_187_officer_active_days_1y": {
        "inputs": ["officer_buy_value"],
        "func": irw_187_officer_active_days_1y,
    },
    "irw_188_director_active_days_1y": {
        "inputs": ["director_buy_value"],
        "func": irw_188_director_active_days_1y,
    },
    "irw_189_tenpct_active_days_1y": {
        "inputs": ["tenpct_buy_value"],
        "func": irw_189_tenpct_active_days_1y,
    },
    "irw_190_officer_share_ewm_1y": {
        "inputs": ["officer_buy_value", "insider_buy_value"],
        "func": irw_190_officer_share_ewm_1y,
    },
    "irw_191_top_officer_share_ewm_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "insider_buy_value"],
        "func": irw_191_top_officer_share_ewm_1y,
    },
    "irw_192_weighted_role_herfindahl_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_192_weighted_role_herfindahl_1y,
    },
    "irw_193_role_diversity_index_1y": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_193_role_diversity_index_1y,
    },
    "irw_194_ceo_value_share_1y": {
        "inputs": ["ceo_buy_value", "insider_buy_value"],
        "func": irw_194_ceo_value_share_1y,
    },
    "irw_195_cfo_value_share_1y": {
        "inputs": ["cfo_buy_value", "insider_buy_value"],
        "func": irw_195_cfo_value_share_1y,
    },
    "irw_196_officer_and_director_net_buy_both_1y": {
        "inputs": ["officer_buy_value", "officer_sell_value", "director_buy_value", "director_sell_value"],
        "func": irw_196_officer_and_director_net_buy_both_1y,
    },
    "irw_197_tenpct_buy_count_half": {
        "inputs": ["tenpct_buy_count"],
        "func": irw_197_tenpct_buy_count_half,
    },
    "irw_198_officer_buy_count_half": {
        "inputs": ["officer_buy_count"],
        "func": irw_198_officer_buy_count_half,
    },
    "irw_199_director_buy_count_half": {
        "inputs": ["director_buy_count"],
        "func": irw_199_director_buy_count_half,
    },
    "irw_200_composite_role_conviction_weighted": {
        "inputs": ["ceo_buy_value", "cfo_buy_value", "officer_buy_value", "director_buy_value", "tenpct_buy_value", "insider_buy_value"],
        "func": irw_200_composite_role_conviction_weighted,
    },
}
